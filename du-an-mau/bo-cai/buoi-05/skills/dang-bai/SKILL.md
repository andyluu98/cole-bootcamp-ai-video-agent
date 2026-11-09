---
name: dang-bai
description: Viết caption và hashtag theo file thương hiệu cho một video đã duyệt, gắn nhãn nội dung AI, rồi nhờ subagent browser mở trang đăng (TikTok Studio hoặc Meta Business Suite), điền sẵn và DỪNG trước nút Đăng để chủ dự án tự bấm. Đăng từng bài, không hàng loạt. Dùng khi người dùng nói "đăng bài", "đăng video", "đăng TikTok", "đăng Reels", "đăng Facebook", hoặc gõ /dang-bai.
---

# Đăng bài có duyệt

Agent chuẩn bị mọi thứ tới sát nút Đăng. **Người bấm Đăng luôn là chủ dự án.** Giống nhân viên soạn sẵn thư, để sếp đọc rồi tự bấm Gửi.

## Trước khi làm

1. Đọc `.agents/rules/thuong-hieu.md`: tên thương hiệu, giọng văn, điều cấm, quy tắc gắn nhãn AI.
2. Đọc thông tin sản phẩm trong `du-lieu/` và kịch bản của video trong `kich-ban/`.
3. Hỏi đúng 1 câu nếu chưa rõ: "Bạn đăng video nào (file trong thư mục video/), lên kênh nào: TikTok, Facebook hay Reels?"
4. Kiểm tra file video có thật trong `video/`. Không có thì dừng, báo chủ dự án.
5. Nhắc một lần: "Nên đăng thử trên tài khoản phụ trước khi đăng lên tài khoản chính."

## Bước 1. Viết caption và hashtag

1. Viết 2 phương án caption, mỗi phương án:
   - Dòng đầu là hook (lấy từ kịch bản), tối đa 12 chữ.
   - 2 tới 3 câu ngắn nói lợi ích, đúng giọng văn thương hiệu.
   - Một lời kêu gọi hành động (ví dụ: "Nhắn Mây Núi để đặt").
   - Dòng cuối: `Nội dung có sử dụng AI`.
2. Hashtag: 3 tới 5 cái, gồm tên thương hiệu, tên sản phẩm, 1 tới 2 hashtag chủ đề. Không dùng hashtag không liên quan để câu lượt xem.
3. Quy tắc:
   - Chỉ dùng giá, ưu đãi, con số có trong file sản phẩm. Không bịa lời khen, giải thưởng.
   - Không dùng từ bị cấm trong file thương hiệu.
4. Gọi agent `nguoi-soat` soát 2 phương án. Sửa theo bảng soát.
5. Lưu vào `kich-ban/dang-bai-<ten-san-pham>.md`. File trùng tên thì chép bản cũ vào `_backup/` trước.
6. **Duyệt caption:** cho chủ dự án xem 2 phương án, hỏi chọn phương án nào. Chưa chọn thì không làm tiếp.

## Bước 2. Mở trang đăng và điền sẵn

Dùng subagent dựng sẵn `browser` của Antigravity (gọi bằng `/browser`). Giao cho nó đúng các việc dưới đây, **mỗi lần một bài, một kênh**:

| Kênh | Trang mở |
|---|---|
| TikTok | TikTok Studio: `https://www.tiktok.com/tiktokstudio/upload` |
| Facebook, Reels | Meta Business Suite: `https://business.facebook.com/`, chọn tạo thước phim (Reel) |

Việc giao cho subagent browser:
1. Mở trang đăng của kênh đã chọn.
2. Trang đòi đăng nhập: **dừng lại**, báo chủ dự án tự đăng nhập. Không gõ mật khẩu, không đọc mật khẩu.
3. Chọn file video từ thư mục `video/`. Không chọn được file thì báo chủ dự án tự kéo thả video vào trang, rồi làm tiếp.
4. Dán caption và hashtag đã duyệt.
5. Tìm mục gắn nhãn nội dung AI và bật lên (TikTok thường nằm trong phần cài đặt thêm; tên mục có thể khác trên máy bạn). Không tìm thấy thì báo chủ dự án, caption vẫn giữ dòng `Nội dung có sử dụng AI`.
6. Chụp màn hình trang đã điền, lưu vào `kich-ban/anh-chup-dang-<ten-san-pham>-<kenh>.png` (trong dự án).
7. **DỪNG. Không bấm Đăng, Post, Publish, Share, Lên lịch.**

Trang hiện captcha hay hỏi xác minh: dừng ngay, báo chủ dự án. Không tìm cách vượt qua.

## Bước 3. Điểm duyệt trước khi đăng

Báo chủ dự án bảng sau, rồi chờ:

| Mục | Nội dung |
|---|---|
| Kênh, tài khoản | ví dụ TikTok, tài khoản phụ |
| File video | đường dẫn trong `video/` |
| Caption | nguyên văn |
| Nhãn AI | đã bật / chưa tìm thấy mục |
| Ảnh chụp trang | đường dẫn ảnh |

Câu chốt: "Bạn xem trang đăng trên trình duyệt. Ưng thì **bạn tự bấm Đăng**. Muốn sửa gì thì nói tôi."

## Bước 4. Sau khi chủ dự án báo đã đăng

1. Hỏi link bài đăng, ghi vào cuối file `kich-ban/dang-bai-<ten-san-pham>.md`: ngày giờ, kênh, link.
2. Muốn đăng thêm kênh khác thì quay lại Bước 2 cho kênh đó. Mỗi kênh một lần duyệt riêng.

## Ranh giới

- Không tự bấm nút Đăng, kể cả khi được bảo "cứ đăng luôn đi". Lần nào cũng để chủ dự án bấm.
- Không đăng hàng loạt, không lên lịch nhiều bài một lúc, không like, comment, theo dõi tài khoản khác.
- Không lưu mật khẩu, cookie, mã đăng nhập vào file hay khung chat.
- Không đăng video chưa qua `nguoi-cham-video` (buổi 4).
