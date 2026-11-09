# Checklist chấm video quảng cáo 9:16

Dùng để chấm video trước khi đăng. Agent `nguoi-cham-video` chấm theo đúng bảng này; bạn cũng tự chấm tay được.

Ngưỡng trong bảng là quy ước của khóa học, lấy theo file thương hiệu mẫu, quy tắc kịch bản buổi 2 và thông số mặc định của VideoMotion. Thương hiệu của bạn có quy tắc khác thì theo file thương hiệu.

## Thông tin video

| Mục | Ghi |
|---|---|
| File video | `video/....mp4` |
| Kịch bản gốc | `kich-ban/....md` |
| Ngày chấm | |
| Người chấm | agent `nguoi-cham-video` / tự chấm |

## Bảng chấm

| # | Tiêu chí | Đạt khi | Cách kiểm | Kết quả |
|---|---|---|---|---|
| 1 | Hook 3 giây | Trong 3 giây đầu đã có hình chính rõ và câu hook (lời đọc hoặc chữ) đúng như kịch bản; không mở đầu bằng màn hình trống, logo đứng yên hay chữ chào hỏi | Xem khung ở giây 0,5; 1,5; 2,5. Đối chiếu câu đầu trong `phude.srt` với hook trong kịch bản | Đạt / Chưa đạt |
| 2 | Phụ đề đọc kịp | Mỗi dòng phụ đề hiện ít nhất 1 giây; không quá 34 ký tự một dòng; lời đọc không quá khoảng 3 chữ mỗi giây; đúng chính tả, đủ dấu; khớp lời đọc; nằm ở phần đáy khung, không bị hình che | Đọc `phude.srt`, đếm thời gian và số ký tự từng dòng; xem khung có phụ đề | Đạt / Chưa đạt |
| 3 | Đúng màu thương hiệu | Màu nền, chữ, điểm nhấn dùng đúng màu chính, màu phụ, màu nhấn trong file thương hiệu; không có màu lạ lấn át | Đối chiếu `theme.css` của dự án video với `.agents/rules/thuong-hieu.md`; nhìn các khung | Đạt / Chưa đạt |
| 4 | Logo | Có logo (hoặc tên thương hiệu) đúng vị trí trong file thương hiệu (mẫu: góc phải phía trên); rõ nét, không méo, không che phụ đề hay sản phẩm | Xem khung đầu, giữa, cuối | Đạt / Chưa đạt |
| 5 | Âm lượng giọng và nhạc | Độ to tổng khoảng -14 LUFS (từ -14,5 tới -13,5), đỉnh không quá -1,0 dBTP; nghe rõ từng chữ của giọng, nhạc nằm dưới giọng, không có tiếng rè, tiếng bị cắt | Đo bằng lệnh đo của VideoMotion; **bạn tự nghe** ít nhất một lượt bằng tai nghe | Đạt / Chưa đạt |
| 6 | Tỷ lệ 9:16 | Khung dọc 1080 x 1920; không viền đen, không bị bóp méo | `ffprobe` đọc kích thước | Đạt / Chưa đạt |
| 7 | Thời lượng | Trong khoảng thời lượng của file thương hiệu (mẫu: 15 tới 30 giây); lệch nhiều so với kịch bản thì ghi chú | `ffprobe` đọc thời lượng; so với tổng thời lượng trong kịch bản | Đạt / Chưa đạt |
| 8 | Lỗi hình | Không có: chữ tràn mép hay sát mép khung, ảnh vỡ hoặc méo, khung đen hoặc trắng bất thường, vật bị ẩn mãi không hiện, chữ sai dấu, chữ lỗi do AI vẽ trong ảnh, hình giật hay đứng hình lâu bất thường | Xem các khung trích ra; **bạn tự xem** cả video một lượt | Đạt / Chưa đạt |

## Phần thêm trước khi đăng

| # | Tiêu chí | Đạt khi | Kết quả |
|---|---|---|---|
| 9 | Kêu gọi hành động (CTA) | Cảnh cuối nói rõ người xem cần làm gì, đúng CTA trong kịch bản | Đạt / Chưa đạt |
| 10 | Không bịa thông tin | Giá, ưu đãi, công dụng trên video khớp file sản phẩm trong `du-lieu/`; không có từ bị cấm trong file thương hiệu | Đạt / Chưa đạt |
| 11 | Bản quyền và nhãn AI | Nhạc, phông chữ có quyền dùng cho quảng cáo; đã ghi nhớ bật nhãn nội dung AI khi đăng | Đạt / Chưa đạt |

## Kết luận

- **Đạt:** cả 8 tiêu chí chính đều Đạt, phần thêm không có lỗi.
- **Sửa rồi chấm lại:** có tiêu chí Chưa đạt. Ghi rõ chỗ lỗi (giây thứ mấy, cảnh nào) và cách sửa, sửa xong chấm lại đúng tiêu chí đó.
