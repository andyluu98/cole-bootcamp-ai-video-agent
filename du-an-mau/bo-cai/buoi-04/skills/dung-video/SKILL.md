---
name: dung-video
description: Dựng video quảng cáo dọc 9:16 từ kịch bản (thư mục kich-ban/) và bộ ảnh (thư mục anh/) theo đúng file thương hiệu, bằng quy trình VideoMotion, gồm giọng đọc tiếng Việt, nhạc nền, phụ đề, màu thương hiệu, xuất MP4 vào thư mục video/. Dùng khi người dùng nói "dựng video", "làm video từ kịch bản", "xuất video", "đổi nhạc", "sửa phụ đề", "đổi màu video", hoặc gõ /dung-video.
---

# Dựng video quảng cáo 9:16 từ kịch bản và bộ ảnh

Skill này là cầu nối: nó gom kịch bản, ảnh, thương hiệu của dự án rồi chạy quy trình dựng của VideoMotion (bộ công cụ đã tải về `cong-cu/VideoMotion/`). Kết quả là 01 file MP4 dọc 9:16 có giọng đọc, nhạc nền, phụ đề, đúng màu thương hiệu.

## 0. Kiểm tra trước khi làm

1. Tìm thư mục VideoMotion: `cong-cu/VideoMotion/`, bên trong phải có `skills/videomotion/SKILL.md` và `tools/setup/doctor.py`. Không thấy thì dừng, báo người dùng làm phần "Cài VideoMotion" của buổi 4.
2. Gọi thư mục đó là **VV** (dùng đường dẫn tuyệt đối). Các file hướng dẫn của VideoMotion viết `$VV` hay `${CLAUDE_PLUGIN_ROOT}` thì hiểu là thư mục này.
3. Python của VideoMotion nằm ở:
   - Windows: `%USERPROFILE%\.motionfly\venv\Scripts\python.exe`
   - macOS: `~/.motionfly/venv/bin/python`
   Gọi là **PY**. Trước mỗi lệnh Python đặt biến môi trường `PYTHONUTF8=1`. Trên Windows dùng cú pháp của Terminal đang mở (PowerShell: `$env:PYTHONUTF8="1"`).
4. Chạy kiểm tra máy: `python "VV/tools/setup/doctor.py"`. Phải thấy dòng `SAN SANG`. Chưa thấy thì dừng, đọc `VV/skills/vm-cai-dat/SKILL.md` và báo người dùng dòng nào còn `THIẾU`. Không tự cài phần mềm hệ thống.
5. Ngoại lệ về thư mục: VideoMotion lưu môi trường Python và model giọng ở thư mục `.motionfly` trong thư mục người dùng (ngoài dự án). Chỉ được ghi vào đó qua lệnh cài của VideoMotion và khi người dùng đã đồng ý.

## 1. Đọc đầu vào

1. `.agents/rules/thuong-hieu.md`: tên thương hiệu, màu chính, màu phụ, màu nhấn (mã màu), phông chữ, giọng văn, quy tắc video (thời lượng, phụ đề, vị trí logo, nhãn AI).
2. Kịch bản trong `kich-ban/`: file `kich-ban-<ten-san-pham>.md` (buổi 2). Có nhiều file thì hỏi đúng 1 câu: "Dựng video từ kịch bản nào?". Lấy ra: tổng thời lượng, từng cảnh (giây, hình ảnh, chuyển động máy quay, lời thoại, chữ trên màn hình), CTA, nhạc nền gợi ý.
3. Ảnh trong `anh/` (buổi 3): đọc bảng `anh/danh-sach-anh.md`, chỉ lấy ảnh có trạng thái "đã duyệt". Ảnh cảnh nằm ở `anh/canh/canh-NN-dau.png` và `anh/canh/canh-NN-cuoi.png` (NN là số cảnh hai chữ số, ví dụ `canh-01-dau.png`); cảnh nào có cả ảnh đầu và ảnh cuối thì dùng ảnh đầu khi vào cảnh, chuyển sang ảnh cuối trước khi hết cảnh. Không có bảng hoặc tên không rõ cảnh nào thì liệt kê ảnh và hỏi người dùng ghép, một câu một lần.
4. Logo: tìm file có chữ `logo` trong `du-lieu/`. Không có thì hỏi người dùng có file logo không; không có thì ghi tên thương hiệu bằng chữ ở vị trí logo.
5. Nhạc: người dùng có file nhạc (trong `du-lieu/`) thì hỏi đúng 1 câu "Nhạc này bạn có quyền dùng cho quảng cáo không?". Chưa có file thì dùng nhạc tổng hợp bằng code của VideoMotion.
6. Thiếu kịch bản hoặc thiếu ảnh thì dừng, báo người dùng thiếu gì. Không tự viết kịch bản mới, không tự tạo ảnh.

## 2. Trình bày kế hoạch, chờ duyệt

Gửi người dùng một bảng ngắn rồi chờ đồng ý:

| Mục | Nội dung |
|---|---|
| Kịch bản dùng | đường dẫn file |
| Thời lượng, số cảnh | theo kịch bản |
| Ảnh từng cảnh | cảnh 1: `anh/...`, cảnh 2: ... |
| Giọng đọc | mặc định Ngọc Huyền, hoặc giọng người dùng chọn |
| Nhạc nền | file của người dùng hoặc nhạc tổng hợp (mood gợi ý) |
| Màu | màu chính, phụ, nhấn lấy từ file thương hiệu |
| Style VideoMotion | một style hợp thương hiệu, tra trong `VV/styles/INDEX.md` |
| Thư mục làm việc | `video/<slug>/` |
| File xuất | `video/<slug>-<ddmmyyyy>.mp4` |

`<slug>` viết thường, không dấu, nối bằng gạch ngang (ví dụ `ca-phe-arabica-cau-dat`).

## 3. Dựng theo VideoMotion

Đọc kỹ rồi làm theo, theo thứ tự: `VV/skills/videomotion/SKILL.md` (hướng dẫn chính), `VV/skills/vm-giong/SKILL.md`, `VV/skills/vm-nhac/SKILL.md`, `VV/skills/vm-dung/SKILL.md`, `VV/agents/vm-canh.md`. Thư mục dự án video (`<du-an>` trong các file đó) là `video/<slug>/` của dự án này, không phải `videos/` của VideoMotion.

Những điểm phải theo kịch bản và thương hiệu của dự án:

1. **brief.json:** `aspect` là `9:16`; `duration_s` lấy từ kịch bản; `message` là thông điệp chính trong file thương hiệu; `auto` là `true` vì kịch bản đã được duyệt ở buổi 2. Ghi nguồn: đường dẫn file kịch bản, file sản phẩm.
2. **script.json:** mỗi cảnh trong kịch bản là một cảnh, `say` là **đúng nguyên văn lời thoại** trong kịch bản; cảnh "(không lời)" thì báo người dùng vì VideoMotion dựng cảnh theo lời đọc. Không thêm, không bớt ý, không bịa số liệu.
3. **Ảnh:** chép (không di chuyển) ảnh của từng cảnh vào `video/<slug>/assets/`. Trong `storyboard.json`, phần `visual` của cảnh ghi rõ ảnh nào làm hình chính (ví dụ `assets/canh-01-dau.png`) và chuyển động máy quay của kịch bản đổi thành chuyển động của ảnh: "đẩy vào gần" là phóng to dần, "kéo ra xa" là thu nhỏ dần, "lia ngang" là trượt ngang.
4. **Chữ trên màn hình:** lấy đúng cột "Chữ trên màn hình" của kịch bản. Chữ là chữ HTML, không vẽ chữ vào ảnh.
5. **Màu thương hiệu:** trong `theme.css`, `--bg`, `--ink`, `--accent` lấy từ bảng màu của file thương hiệu (màu chính, màu phụ, màu nhấn), không lấy màu của thẻ style. Phụ đề (`--cap-bg`, `--cap-ink`) phải đọc rõ, tương phản ít nhất 4,5:1.
6. **Phông:** dùng phông trong file thương hiệu nếu tải được bằng `VV/tools/fonts.py`; không được thì dùng Be Vietnam Pro.
7. **Logo:** đặt đúng vị trí ghi trong file thương hiệu (mẫu: góc phải phía trên), hiện suốt video, không che phụ đề.
8. **Dựng từng cảnh:** công cụ này không chạy được agent con của Claude Code, nên tự dựng **lần lượt từng cảnh** theo `VV/agents/vm-canh.md` (đúng cách README của VideoMotion hướng dẫn cho công cụ khác). Trong dự án đã cài agent `vm-canh` ở `.agents/agents/` thì có thể giao cho agent đó.
9. **Kiểm tra kỹ thuật và render:** làm đúng lệnh trong `VV/skills/vm-dung/SKILL.md` (chạy `hyperframes check` tới khi đạt, render, ghép âm, phụ đề). Lệnh nào cài thêm phần mềm hay tải dữ liệu lớn thì nói rõ và chờ người dùng đồng ý.

## 4. Xuất file, không ghi đè

1. File MP4 VideoMotion xuất ra nằm trong `video/<slug>/renders/`.
2. Chép file đó ra `video/<slug>-<ddmmyyyy>.mp4`. Đã có file trùng tên thì **chuyển file cũ vào `_backup/`** với tên `<slug>-<ddmmyyyy>_<gio-phut>.mp4` rồi mới chép bản mới. Không xóa file nào.
3. Dựng lại trong cùng thư mục `video/<slug>/`: trước khi render lại, chép các file trong `renders/` sang `_backup/` như trên.

## 5. Mở cho người dùng xem và chỉnh

1. Báo người dùng lệnh mở HyperFrames Studio (trình chỉnh timeline trong trình duyệt): chạy `npx -y hyperframes@0.8.145 preview` trong thư mục `video/<slug>/`. Studio mở trên trình duyệt, người dùng xem và chỉnh từng cảnh.
2. Người dùng sửa bằng lời (ví dụ "nhạc nhỏ lại", "phụ đề to hơn", "cảnh 2 dài thêm") thì sửa đúng chỗ đó theo các skill vm-* của VideoMotion rồi xuất lại theo mục 4.
   - Nhạc to nhỏ: chạy lại bước trộn của `vm-nhac` với `--music-db` khác.
   - Màu, phụ đề: sửa `theme.css`.
   - Lời đọc: sửa `script.json` rồi sinh lại giọng theo `vm-giong`.

## 6. Báo cáo cuối

Báo người dùng:
- Đường dẫn file MP4 và file phụ đề `phude.srt`.
- Thời lượng, kích thước khung hình, giọng đọc, nguồn nhạc.
- Gợi ý bước tiếp: gọi agent `nguoi-cham-video` để chấm video theo checklist.

Luôn nhắc 3 điều trước khi đăng:
1. **Nhạc:** nhạc tổng hợp bằng code của VideoMotion do máy tạo; nhạc người dùng đưa vào thì phải có quyền dùng cho quảng cáo.
2. **Phông chữ:** phông tải từ Google Fonts theo giấy phép của từng phông; phông khác phải có giấy phép thương mại.
3. **Nhãn AI:** video có giọng đọc, hình ảnh làm bằng AI; bật nhãn nội dung AI của nền tảng khi đăng (theo quy tắc trong file thương hiệu).

## Lưu ý

- Chỉ đọc, ghi trong thư mục dự án (trừ ngoại lệ ở bước 0). Không sửa file nào trong `cong-cu/VideoMotion/`.
- Không xóa file. Bản cũ chuyển vào `_backup/`.
- Không bịa số liệu, giá, ưu đãi, lời khen. Mọi chữ trên video lấy từ kịch bản, file sản phẩm, file thương hiệu.
