---
name: hook-video-3-giay
description: Viết 5 câu mở đầu (hook) 3 giây cho video ngắn bán hàng, theo đúng file thương hiệu. Dùng khi người dùng nói "viết hook", "câu mở đầu video", "3 giây đầu", hoặc gõ /hook-video-3-giay.
---

# Viết hook 3 giây cho video ngắn

Hook là câu nói hoặc dòng chữ trong 3 giây đầu video, quyết định người xem lướt qua hay xem tiếp.

## Trước khi viết

1. Đọc `.agents/rules/thuong-hieu.md`: tên thương hiệu, khách hàng, giọng văn, điều cấm.
2. Đọc thông tin sản phẩm trong `du-lieu/` (ví dụ `du-lieu/san-pham-mau.md`).
3. Chưa rõ video về sản phẩm nào thì hỏi đúng 1 câu: "Video này giới thiệu sản phẩm nào, cho ai xem?"

## Cách viết

Viết 5 hook, mỗi hook một kiểu:

| Kiểu | Ý tưởng |
|---|---|
| Nỗi đau | Nói thẳng điều khách đang khó chịu |
| Câu hỏi | Hỏi một câu khách muốn biết đáp án |
| Con số | Một con số cụ thể gây tò mò, chỉ dùng số có thật trong file sản phẩm |
| Trái ngược | Nói điều ngược với suy nghĩ thông thường |
| Kết quả | Cho thấy ngay kết quả khi dùng sản phẩm |

Quy tắc:
- Mỗi hook tối đa 12 chữ, đọc to hết trong 3 giây.
- Đúng giọng văn, không dùng từ bị cấm trong file thương hiệu.
- Không hứa điều sản phẩm không làm được, không bịa con số.

## Kết quả

1. Trả về bảng 5 dòng: kiểu hook, câu hook, gợi ý hình ảnh cho 3 giây đầu.
2. Cuối bảng ghi hook nên dùng và lý do trong một câu.
3. Lưu bảng vào `kich-ban/hook-<ten-san-pham>.md`, tên viết thường, không dấu, nối bằng gạch ngang (ví dụ `hook-ca-phe-arabica-cau-dat.md`). File trùng tên thì chép bản cũ vào `_backup/` trước.
