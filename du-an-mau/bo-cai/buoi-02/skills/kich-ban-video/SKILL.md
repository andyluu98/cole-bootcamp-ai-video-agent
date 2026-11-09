---
name: kich-ban-video
description: Viết kịch bản phân cảnh cho video ngắn bán hàng dọc 9:16, dài 15 tới 30 giây, 4 tới 6 cảnh (hình ảnh, chuyển động máy quay, lời thoại, chữ trên màn hình), kèm mô tả hình ảnh từng cảnh để tạo ảnh ở buổi 3. Đọc file thương hiệu và thông tin sản phẩm trước khi viết. Dùng khi người dùng nói "viết kịch bản", "kịch bản video", "chia cảnh", "phân cảnh", hoặc gõ /kich-ban-video.
---

# Viết kịch bản phân cảnh cho video ngắn bán hàng

Kịch bản phân cảnh là bảng chia video thành từng cảnh: mỗi cảnh dài bao nhiêu giây, người xem thấy gì, nghe gì, đọc chữ gì. Có bảng này thì các bước sau (tạo ảnh, dựng video) chỉ việc làm theo.

## Trước khi viết

1. Đọc `.agents/rules/thuong-hieu.md`: tên thương hiệu, khách hàng, màu, giọng văn, cách xưng hô, điều cấm, quy tắc video.
2. Đọc thông tin sản phẩm trong `du-lieu/` (ví dụ `du-lieu/san-pham-mau.md`). Có nhiều sản phẩm mà người dùng chưa nói rõ thì hỏi đúng 1 câu: "Video này giới thiệu sản phẩm nào?"
3. Tìm file hook đã làm ở buổi 1: `kich-ban/hook-<ten-san-pham>.md`.
   - Có file: dùng hook được đánh dấu "nên dùng". Người dùng chỉ định hook khác thì dùng hook đó.
   - Không có file: tự viết 1 hook theo quy tắc ở mục "Hook 3 giây" bên dưới và ghi rõ "hook viết mới".
4. Mở khung mẫu `bo-cai/buoi-02/mau/mau-kich-ban.md` (nếu có) để viết đúng bố cục.
5. Trình bày kế hoạch ngắn: sản phẩm, hook định dùng, tổng thời lượng, số cảnh, ý chính từng cảnh. Chờ người dùng đồng ý rồi mới viết.

## Cấu trúc video

| Phần | Thời lượng | Việc của phần này |
|---|---|---|
| Hook | 3 giây đầu (cảnh 1) | Giữ người xem lại, không cho lướt qua |
| Thân | phần giữa (2 tới 4 cảnh) | Nỗi đau của khách, sản phẩm giải quyết thế nào, điểm khác biệt |
| Kêu gọi hành động (CTA) | 3 tới 5 giây cuối (cảnh cuối) | Nói rõ người xem cần làm gì: bấm vào giỏ hàng, nhắn tin, ghé fanpage |

## Quy tắc viết

- Video dọc 9:16, tổng 15 tới 30 giây, 4 tới 6 cảnh. Cộng thời lượng các cảnh phải đúng bằng tổng.
- **Lời thoại đọc kịp:** tối đa khoảng 3 chữ cho mỗi giây của cảnh (cảnh 4 giây thì lời thoại không quá 12 chữ). Cảnh không có lời thì ghi "(không lời)".
- **Chữ trên màn hình:** tối đa 8 chữ mỗi cảnh, không chép lại nguyên lời thoại.
- **Chuyển động máy quay** dùng từ dễ hiểu: đứng yên, đẩy vào gần, kéo ra xa, lia ngang, quay từ trên xuống, cận cảnh tay, máy cầm tay rung nhẹ.
- Đúng giọng văn, cách xưng hô trong file thương hiệu. Không dùng từ, lời hứa bị cấm.
- **Không bịa số liệu:** giá, ưu đãi, thành phần, thời gian, lời khen của khách chỉ lấy từ file sản phẩm và file thương hiệu. Thiếu thông tin thì để `[CHỜ BỔ SUNG]` và báo người dùng, không tự điền.
- Thương hiệu có ghi nhãn AI, logo, phụ đề trong "Quy tắc video" thì nhắc lại ở phần ghi chú cuối kịch bản.

### Hook 3 giây (khi chưa có file hook)

Tối đa 12 chữ, đọc hết trong 3 giây, chọn một kiểu: nỗi đau, câu hỏi, con số có thật trong file sản phẩm, trái ngược, kết quả.

## Mô tả hình ảnh từng cảnh (chuẩn bị cho buổi 3)

Mỗi cảnh viết một đoạn mô tả để dán vào công cụ tạo ảnh ở buổi 3. Mỗi đoạn có đủ:

| Mục | Ghi gì |
|---|---|
| Nhân vật | Tuổi, giới tính, trang phục, biểu cảm, đang làm gì. Không có người thì ghi "không có người". Cùng một nhân vật thì giữ nguyên mô tả ở mọi cảnh để buổi 3 khóa nhân vật |
| Sản phẩm | Sản phẩm xuất hiện thế nào (trên bàn, trong tay...) |
| Bối cảnh | Ở đâu, đồ vật xung quanh, màu chủ đạo theo file thương hiệu |
| Ánh sáng | Thời điểm trong ngày, hướng sáng, cảm giác (ấm, dịu, tươi) |
| Góc máy | Cận, trung, toàn; nhìn ngang, từ trên xuống |
| Tỷ lệ | 9:16 (dọc) |

Không ghi chữ, logo vào mô tả ảnh (chữ và logo thêm lúc dựng video ở buổi 4).

## Kết quả

1. Một file gồm 4 phần, đúng thứ tự:
   1. Thông tin chung: sản phẩm, tổng thời lượng, hook dùng (và nguồn hook), CTA.
   2. Bảng kịch bản phân cảnh, các cột: Cảnh, Giây (ví dụ 0 tới 3), Hình ảnh, Chuyển động máy quay, Lời thoại, Chữ trên màn hình.
   3. Mô tả hình ảnh từng cảnh (theo bảng mục ở trên).
   4. Ghi chú: các chỗ `[CHỜ BỔ SUNG]`, nhạc nền gợi ý (chỉ mô tả cảm giác, không ghi tên bài hát), quy tắc video của thương hiệu.
2. Lưu vào `kich-ban/kich-ban-<ten-san-pham>.md`, tên viết thường, không dấu, nối bằng gạch ngang (ví dụ `kich-ban/kich-ban-ca-phe-arabica-cau-dat.md`).
3. File trùng tên đã có: chép bản cũ vào `_backup/kich-ban-<ten-san-pham>_<ngày-giờ>.md` trước, rồi mới ghi bản mới.
4. Báo lại đường dẫn file, tổng thời lượng và số cảnh. Gợi ý bước tiếp: gọi agent `nguoi-cham-kich-ban` để chấm; chấm đạt rồi thì chạy `/mo-ta-hinh-canh` (nếu dự án đã có skill này) để tách mô tả hình ảnh ra file `kich-ban/mo-ta-hinh-canh-<ten-san-pham>.md` cho buổi 3.

## Lưu ý

- Chỉ đọc, ghi trong thư mục dự án. Không xóa file nào.
- Người dùng muốn sửa một cảnh thì chỉ sửa cảnh đó, sao lưu bản cũ vào `_backup/` trước khi ghi.
