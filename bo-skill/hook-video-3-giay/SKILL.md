---
name: hook-video-3-giay
description: Viết câu mở đầu (hook) 3 giây cho video ngắn bán hàng, theo đúng file thương hiệu của dự án. Dùng khi người dùng nói "viết hook", "câu mở đầu video", "3 giây đầu", hoặc gõ /hook-video-3-giay.
---

# Viết hook 3 giây cho video ngắn

Hook là câu nói hoặc dòng chữ xuất hiện trong 3 giây đầu video, quyết định người xem lướt qua hay xem tiếp.

## Trước khi viết

1. Đọc file thương hiệu của dự án: `CLAUDE.md` (Claude Code) hoặc file trong `.agents/rules/` (Antigravity). Lấy ra: tên thương hiệu, sản phẩm, khách hàng mục tiêu, giọng văn, những từ không được dùng.
2. Nếu người dùng chưa nói video về sản phẩm nào, hỏi đúng 1 câu: "Video này giới thiệu sản phẩm nào, cho ai xem?"
3. Không có file thương hiệu thì báo người dùng và hỏi 3 thông tin: sản phẩm, khách hàng, giọng văn.

## Cách viết

Viết 5 hook, mỗi hook theo một kiểu khác nhau:

| Kiểu | Ý tưởng |
|---|---|
| Nỗi đau | Nói thẳng điều khách đang khó chịu |
| Câu hỏi | Hỏi một câu khách muốn biết đáp án |
| Con số | Một con số cụ thể gây tò mò (chỉ dùng số có thật trong file thương hiệu) |
| Trái ngược | Nói điều ngược với suy nghĩ thông thường |
| Kết quả | Cho thấy ngay kết quả sau khi dùng sản phẩm |

Quy tắc:
- Mỗi hook tối đa 12 chữ, đọc to hết trong 3 giây.
- Đúng giọng văn trong file thương hiệu; không dùng từ bị cấm.
- Không hứa điều sản phẩm không làm được, không bịa con số.

## Kết quả trả về

Một bảng 5 dòng: kiểu hook, câu hook, gợi ý hình ảnh cho 3 giây đầu. Cuối bảng ghi hook em đề xuất dùng và lý do trong một câu.

Nếu người dùng muốn lưu, ghi bảng vào file `hook/hook-<ten-san-pham>.md` trong dự án.
