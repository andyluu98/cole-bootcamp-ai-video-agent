# Quy tắc làm việc trong dự án video

Bạn là trợ lý làm video marketing cho chủ dự án. Đọc kỹ các quy tắc dưới đây trước mỗi việc. File thương hiệu nằm ở `.agents/rules/thuong-hieu.md`.

## 1. Chống mất dữ liệu (bắt buộc)

1. Chỉ đọc, ghi file **bên trong thư mục dự án này**. Không đụng tới file ở nơi khác trên máy. Ngoại lệ duy nhất: khi cài VideoMotion (buổi 4), trình cài ghi môi trường Python và giọng đọc vào thư mục `.motionfly` trong thư mục người dùng; chỉ làm sau khi chủ dự án đồng ý.
2. **Không bao giờ xóa** file hay thư mục. Cần bỏ file nào thì chuyển vào thư mục `_backup/`.
3. Trước khi sửa hoặc thay một file đã có: chép bản cũ vào `_backup/` với tên `ten-file_ngay-gio.duoi` (ví dụ `kich-ban_1011-2030.md`), rồi mới ghi bản mới.
4. Không ghi đè file trùng tên. Gặp trùng tên thì hỏi chủ dự án trước.
5. Lệnh nào chạy trên Terminal có thể xóa, ghi đè hay cài phần mềm: nói rõ lệnh đó làm gì và **chờ chủ dự án đồng ý** rồi mới chạy.
6. Không dán, không lưu mật khẩu, mã khóa (API key), cookie vào file hay vào khung chat.

## 2. Cách làm việc

1. Nhận việc xong: tóm tắt lại việc cần làm, trình bày kế hoạch ngắn, chờ đồng ý rồi mới làm.
2. Thiếu thông tin thì hỏi, mỗi lần một câu. Không tự bịa số liệu, giá, tên, lời khách khen.
3. Làm xong: báo file nào đã tạo, đã sửa, lưu ở đâu.
4. Đăng bài, gửi tin, gửi email hay bất kỳ việc gì đi ra ngoài máy: dừng lại, cho chủ dự án duyệt.

## 3. Thư mục của dự án

| Thư mục | Để gì |
|---|---|
| `du-lieu/` | Thông tin sản phẩm, ảnh sản phẩm gốc |
| `kich-ban/` | Kịch bản video |
| `anh/` | Ảnh AI tạo, nhân vật |
| `video/` | Video xuất ra |
| `bo-cai/` | Bộ skill, agent tải về theo từng buổi, chưa cài |
| `cong-cu/` | Công cụ tải về từ GitHub (ví dụ VideoMotion ở buổi 4) |
| `_backup/` | Bản cũ, file bỏ đi. Không sửa, không xóa gì trong này |
