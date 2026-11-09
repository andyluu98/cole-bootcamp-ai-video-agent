---
name: hinh-anh-nhan-vat
description: Tạo bộ hình ảnh cho video từ kịch bản buổi 2 bằng MCP chatgpt-image, gồm phiếu nhân vật cố định, ảnh nhân vật gốc, ảnh sản phẩm, poster 1:1, 9:16, 16:9, ảnh từng cảnh và cặp ảnh đầu cảnh, cuối cảnh giữ nguyên nhân vật. Đọc file thương hiệu và kịch bản trước khi tạo. Dùng khi người dùng nói "tạo ảnh", "khóa nhân vật", "nhân vật đại diện", "ảnh từng cảnh", "ảnh đầu cảnh cuối cảnh", "làm poster", hoặc gõ /hinh-anh-nhan-vat.
---

# Tạo hình ảnh và khóa nhân vật

Video cần một nhân vật xuất hiện ở nhiều cảnh. Nếu mỗi cảnh tả nhân vật một kiểu, AI sẽ vẽ ra mỗi cảnh một người khác. Cách khóa: viết một **phiếu nhân vật** cố định, tạo một **ảnh nhân vật gốc**, rồi cảnh nào cũng dán nguyên đoạn mô tả trong phiếu và đính kèm ảnh gốc làm tham chiếu.

## Công cụ dùng

MCP `chatgpt-image`, tool `generate_image`. Các tham số dùng trong skill này:

| Tham số | Giá trị dùng | Ghi chú |
|---|---|---|
| `prompt` | đoạn mô tả ảnh | ghép theo khung ở mục "Khung prompt ảnh" |
| `aspect` | `1:1`, `9:16`, `16:9` | ChatGPT giữ đúng tỷ lệ, kích thước pixel tự chuẩn hóa |
| `n` | `1` | mỗi lần gọi một ảnh, tránh quá thời gian chờ |
| `out_dir` | **đường dẫn tuyệt đối** tới thư mục con trong `anh/` của dự án | để trống hoặc ghi đường dẫn tương đối thì ảnh rơi vào thư mục của MCP, không vào dự án |
| `enhance` | `false` | giữ nguyên prompt, không để công cụ tự viết lại |
| `style` | `auto` | không dùng `slide`, `fintech` (hai kiểu đó dành cho slide) |
| `ref_image` | đường dẫn tuyệt đối tới ảnh tham chiếu | mỗi lần gọi chỉ đính kèm được **một** ảnh |
| `ref_mode` | xem mục "Chọn ảnh tham chiếu" | |

Công cụ tự đặt tên file dạng `img-<số>-0.png` và trả về đường dẫn trong `paths`. Mỗi ảnh mất khoảng 30 tới 90 giây.

Trước việc đầu tiên, gọi tool `login_status`. Kết quả chưa đăng nhập thì dừng, báo người dùng chạy lại bước đăng nhập của buổi 3, không tự chạy lệnh đăng nhập.

## Trước khi tạo ảnh

1. Đọc `.agents/rules/thuong-hieu.md`: tên thương hiệu, khách hàng, màu chính, màu phụ, màu nhấn, điều cấm.
2. Đọc kịch bản trong `kich-ban/` (thường là `kich-ban/kich-ban-<ten-san-pham>.md`), lấy phần **Mô tả hình ảnh từng cảnh** và cột **Chuyển động máy quay** của từng cảnh. Có nhiều kịch bản mà người dùng chưa nói rõ thì hỏi đúng 1 câu: "Làm ảnh cho kịch bản nào?"
3. Đọc thông tin sản phẩm trong `du-lieu/`. Tìm ảnh sản phẩm thật (`.png`, `.jpg`) và file logo (nếu có) trong `du-lieu/`.
4. Hỏi người dùng muốn làm phần nào (có thể làm tất cả, theo thứ tự):
   - Phần A: phiếu nhân vật và ảnh nhân vật gốc.
   - Phần B: ảnh sản phẩm và poster 3 tỷ lệ.
   - Phần C: ảnh từng cảnh, cặp đầu cảnh và cuối cảnh.
5. Trình bày kế hoạch: phần sẽ làm, danh sách ảnh sẽ tạo (tên file, tỷ lệ, ảnh tham chiếu), tổng số lần gọi tool. Chờ người dùng đồng ý rồi mới tạo.

## Thư mục lưu ảnh

```
anh/
├── nhan-vat/
│   ├── phieu-nhan-vat.md        phiếu nhân vật cố định
│   ├── nhan-vat-goc.png         ảnh gốc đã chọn, dùng làm tham chiếu
│   └── ban-thu-01.png ...       các bản thử chưa chọn
├── san-pham/san-pham-1x1.png
├── poster/poster-1x1.png, poster-9x16.png, poster-16x9.png
├── canh/canh-01-dau.png, canh-01-cuoi.png, canh-02-dau.png ...
└── danh-sach-anh.md             bảng mọi ảnh đã tạo
```

Quy tắc lưu (bắt buộc):
- `out_dir` là đường dẫn tuyệt đối tới đúng thư mục con ở trên. Chưa có thư mục thì tạo mới.
- Tạo xong, đổi tên file `img-...png` thành tên đúng như bảng trên.
- **Không ghi đè.** Tên đích đã có file: chuyển file cũ vào `_backup/` với tên `ten-file_ngay-gio.png` (ví dụ `_backup/canh-01-dau_1711-2130.png`) rồi mới đổi tên file mới.
- Không xóa ảnh nào, kể cả ảnh hỏng. Ảnh không dùng thì chuyển vào `_backup/`.

## Phần A: phiếu nhân vật và ảnh nhân vật gốc

### A1. Viết phiếu nhân vật

1. Lấy mô tả nhân vật trong kịch bản (mục "Nhân vật" của các cảnh). Kịch bản không có người ở cảnh nào thì hỏi người dùng có cần nhân vật đại diện không.
2. Đề xuất **2 phương án** nhân vật hợp với khách hàng mục tiêu trong file thương hiệu, mỗi phương án 2 dòng. Người dùng chọn rồi mới viết phiếu.
3. Viết phiếu theo mẫu dưới, lưu `anh/nhan-vat/phieu-nhan-vat.md`:

```markdown
# Phiếu nhân vật: TÊN GỌI NHÂN VẬT

Nhân vật hư cấu, không dựa trên người thật hay người nổi tiếng.

| Mục | Mô tả cố định |
|---|---|
| Vai trò | ví dụ: nhân viên pha chế đại diện thương hiệu |
| Tuổi, giới tính | |
| Khuôn mặt | dáng mặt, mắt, lông mày, mũi, miệng, một nét riêng dễ nhận (ví dụ nốt ruồi nhỏ dưới mắt trái) |
| Da | tông da, kết cấu da thật (có lỗ chân lông, không mịn như nhựa) |
| Tóc | độ dài, màu, kiểu, mái |
| Vóc dáng | |
| Trang phục | từng món, màu theo mã màu thương hiệu |
| Logo trên trang phục | hình đơn giản không có chữ, vị trí, kích thước (ví dụ biểu tượng núi và mây thêu nhỏ ở ngực trái) |
| Phụ kiện | |
| Biểu cảm thường gặp | |
| Không bao giờ thay đổi | danh sách điểm giữ cố định ở mọi cảnh |

## Đoạn mô tả cố định (dán nguyên văn vào mọi prompt có nhân vật)

(Viết bằng tiếng Anh, 1 đoạn liền, gồm đủ các mục trên. Không sửa chữ nào giữa các cảnh.)

## Ảnh gốc

- File: anh/nhan-vat/nhan-vat-goc.png
- Prompt đã dùng: (chép nguyên văn)
```

Quy tắc phiếu:
- Nhân vật **hư cấu**. Không lấy tên, khuôn mặt, dáng người của người thật, người nổi tiếng, người mẫu, khách hàng. Người dùng yêu cầu "giống ca sĩ X", "giống tôi", "giống người trong ảnh này" thì từ chối nhẹ nhàng, giải thích lý do (quyền hình ảnh, quảng cáo dễ bị gỡ) và đề nghị tạo nhân vật mới.
- Màu trang phục lấy đúng mã màu trong file thương hiệu.
- Logo trên trang phục chỉ là **hình**, không có chữ, vì AI hay vẽ chữ méo. Logo có chữ của thương hiệu ghép thêm lúc dựng video ở buổi 4.

### A2. Tạo ảnh nhân vật gốc

1. Ảnh chân dung nửa người, nhìn thẳng máy, nền trơn màu phụ của thương hiệu, ánh sáng cửa sổ dịu. Tỷ lệ `3:4` hoặc `1:1`, không đính kèm ảnh tham chiếu.
2. Tạo **3 bản thử** (3 lần gọi, mỗi lần `n=1`), lưu `anh/nhan-vat/ban-thu-01.png`, `ban-thu-02.png`, `ban-thu-03.png`.
3. Cho người dùng xem 3 bản, hỏi chọn bản nào. Bản được chọn: chép thành `anh/nhan-vat/nhan-vat-goc.png`. Ghi đường dẫn và prompt vào phiếu.
4. Không bản nào ưng: hỏi người dùng muốn đổi điểm gì, sửa phiếu (sao lưu phiếu cũ vào `_backup/` trước), tạo lại.

## Phần B: ảnh sản phẩm và poster 3 tỷ lệ

1. **Ảnh sản phẩm** `anh/san-pham/san-pham-1x1.png`, tỷ lệ `1:1`: sản phẩm đặt trên bề mặt thật (gỗ, vải lanh, đá), nền theo màu phụ, có đồ vật phụ liên quan.
   - Có ảnh sản phẩm thật trong `du-lieu/`: đính kèm làm `ref_image`, `ref_mode` = `asset`, để giữ đúng bao bì.
   - Không có ảnh thật: tả bao bì theo file sản phẩm, ghi rõ trong `danh-sach-anh.md` là "bao bì AI vẽ, cần thay bằng ảnh thật trước khi đăng".
2. **Poster** cùng một ý, 3 tỷ lệ: `poster-1x1.png` (bài đăng), `poster-9x16.png` (story, video dọc), `poster-16x9.png` (ảnh bìa, YouTube).
   - Poster **không có chữ trong ảnh**. Chừa một vùng trống sạch (ví dụ một phần ba phía trên) để thêm tiêu đề, giá, logo sau bằng công cụ thiết kế.
   - Tạo bản 1:1 trước, người dùng ưng thì tạo 9:16 và 16:9 với `ref_image` là bản 1:1 vừa chọn, `ref_mode` = `style`, để 3 bản cùng màu, cùng ánh sáng.
   - Có file logo thật trong `du-lieu/` và người dùng muốn đặt logo vào poster: dùng `ref_image` là file logo, `ref_mode` = `logo`. Mỗi lần gọi chỉ một ảnh tham chiếu, nên khi đã dùng logo thì tả lại màu, ánh sáng bằng chữ.

## Phần C: ảnh từng cảnh, cặp đầu cảnh và cuối cảnh

Ở buổi 4, công cụ dựng video sẽ nhận **ảnh đầu cảnh** (khung hình mở đầu) và **ảnh cuối cảnh** (khung hình kết thúc) rồi tạo chuyển động ở giữa. Vì vậy hai ảnh của một cảnh phải cùng bối cảnh, cùng ánh sáng, cùng nhân vật, chỉ khác tư thế hoặc khoảng cách máy.

Với mỗi cảnh trong kịch bản, làm lần lượt:

1. **Ảnh đầu cảnh** `anh/canh/canh-NN-dau.png`, tỷ lệ `9:16`:
   - Prompt = đoạn mô tả cố định trong phiếu (nếu cảnh có nhân vật) + mô tả cảnh trong kịch bản + khung chống "ảnh AI".
   - Cảnh có nhân vật: `ref_image` = `anh/nhan-vat/nhan-vat-goc.png`.
   - Cảnh chỉ có sản phẩm: `ref_image` = ảnh sản phẩm thật (nếu có), `ref_mode` = `asset`.
2. **Ảnh cuối cảnh** `anh/canh/canh-NN-cuoi.png`, tỷ lệ `9:16`:
   - `ref_image` = ảnh đầu cảnh vừa tạo, `ref_mode` = `style`.
   - Prompt giữ nguyên phần nhân vật, bối cảnh, ánh sáng; chỉ đổi phần tư thế, khoảng cách máy theo cột "Chuyển động máy quay". Ví dụ: "đẩy vào gần" thì ảnh cuối cận hơn; "lia ngang" thì ảnh cuối lệch khung sang bên; "đứng yên" thì nhân vật đổi động tác nhỏ (cầm ly lên, mỉm cười).
3. Xong mỗi cảnh, cho người dùng xem cặp ảnh, hỏi "Dùng được, hay tạo lại ảnh nào?" rồi mới làm cảnh tiếp.

Đánh số cảnh hai chữ số theo kịch bản: `canh-01-dau.png`, `canh-01-cuoi.png`, `canh-02-dau.png`...

### Chọn ảnh tham chiếu (`ref_mode`)

| Ảnh tham chiếu | `ref_mode` | Công cụ hiểu là |
|---|---|---|
| Ảnh nhân vật gốc | xem ghi chú dưới | giữ nhân vật |
| Ảnh sản phẩm thật, file logo | `asset` (hoặc `logo`) | đặt đúng vật đó vào ảnh, không vẽ lại |
| Ảnh đầu cảnh, poster đã chọn | `style` | chỉ mượn màu, ánh sáng, không khí |

Ghi chú cho ảnh nhân vật gốc: đọc mô tả tool `generate_image`. Mô tả có nhắc `ref_mode` dành cho nhân vật (ví dụ `character`) thì dùng giá trị đó; không có thì dùng `style`. Dù dùng giá trị nào, **đoạn mô tả cố định trong phiếu mới là phần giữ nhân vật chính**, ảnh gốc chỉ hỗ trợ. AI không giữ khuôn mặt giống tuyệt đối, cảnh nào lệch nhiều thì tạo lại.

## Khung prompt ảnh (chống "ảnh AI")

Ghép prompt theo thứ tự sau, viết bằng tiếng Anh, một đoạn liền:

1. **Loại ảnh:** "Candid photograph shot on a real camera" (ảnh chụp thật) hoặc "Product photograph".
2. **Nhân vật:** dán nguyên văn đoạn mô tả cố định trong phiếu. Thêm: "fictional person, does not resemble any real person or celebrity".
3. **Hành động, sản phẩm, bối cảnh:** lấy từ kịch bản. Màu chủ đạo ghi bằng tên màu và mã màu thương hiệu.
4. **Ánh sáng:** "soft natural daylight from a side window, neutral white balance around 5500K, true-to-life colors, no yellow or orange color cast".
5. **Máy ảnh:** "35mm lens, f/2.8, eye-level" (đổi theo góc máy trong kịch bản: cận dùng 50mm hoặc 85mm, toàn dùng 24mm hoặc 35mm).
6. **Chất liệu thật:** "natural skin texture with visible pores, slight fabric wrinkles, real wood grain, a few small everyday imperfections, slightly off-center composition".
7. **Cấm:** "no text, no letters, no numbers, no captions, no watermark, no signage, no extra fingers, no distorted hands, no plastic-looking skin, no oversaturated colors, no HDR look, no cinematic orange-teal grading".
8. **Tỷ lệ:** "vertical 9:16 frame" (hoặc "square 1:1", "horizontal 16:9") khớp với `aspect`.

Ví dụ ảnh đầu cảnh (chỉ minh họa cách ghép, thay bằng nội dung kịch bản thật):

```
Candid photograph shot on a real camera. [ĐOẠN MÔ TẢ CỐ ĐỊNH TRONG PHIẾU]. Fictional person, does not resemble any real person or celebrity. She pours hot water from a gooseneck kettle into an aluminium phin filter on a light oak kitchen counter, a 250g coffee bag beside the cup, cream-colored wall (#F2E6D8), a small green plant. Soft natural morning daylight from a side window, neutral white balance around 5500K, true-to-life colors, no yellow or orange color cast. 35mm lens, f/2.8, eye-level, medium shot. Natural skin texture with visible pores, slight fabric wrinkles, real wood grain, a few small everyday imperfections, slightly off-center composition. No text, no letters, no numbers, no captions, no watermark, no signage, no extra fingers, no distorted hands, no plastic-looking skin, no oversaturated colors, no HDR look. Vertical 9:16 frame.
```

## Ghi danh sách ảnh

Sau mỗi phần, cập nhật `anh/danh-sach-anh.md` (sao lưu bản cũ vào `_backup/` trước khi sửa). Bảng gồm các cột: File, Dùng cho (nhân vật gốc, sản phẩm, poster, cảnh NN đầu, cảnh NN cuối), Tỷ lệ, Ảnh tham chiếu, Prompt (chép nguyên văn), Trạng thái (đã duyệt, cần tạo lại). Buổi 4 đọc bảng này để dựng video.

## Kết quả

1. Báo danh sách file đã tạo, đường dẫn, phần nào còn thiếu.
2. Gợi ý bước tiếp: gọi agent `nguoi-soat-anh` để soát bộ ảnh.

## Lưu ý

- Chỉ đọc, ghi trong thư mục dự án. Không xóa file nào.
- Tool báo lỗi quá thời gian chờ: báo người dùng, chờ đồng ý rồi gọi lại đúng ảnh đó, không tự gọi lại nhiều lần.
- ChatGPT từ chối prompt: báo nguyên văn lý do, đề xuất cách sửa prompt, chờ người dùng đồng ý.
- Không đưa chữ, giá, khẩu hiệu vào ảnh. Chữ thêm lúc dựng video hoặc thiết kế.
- Không tạo ảnh người thật, trẻ em, nhân vật có thương hiệu khác, logo của hãng khác.
