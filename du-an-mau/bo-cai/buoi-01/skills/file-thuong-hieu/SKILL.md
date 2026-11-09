---
name: file-thuong-hieu
description: Phỏng vấn chủ dự án rồi viết hoặc cập nhật file thương hiệu .agents/rules/thuong-hieu.md (tên, sản phẩm, khách hàng, màu, chữ, giọng văn, điều cấm, quy tắc video). Dùng khi người dùng nói "viết file thương hiệu", "cập nhật thương hiệu", "đổi màu thương hiệu", hoặc gõ /file-thuong-hieu.
---

# Viết file thương hiệu

File thương hiệu là sổ tay mọi skill khác đọc trước khi làm việc. Viết đúng một lần, mọi video sau đều đúng màu, đúng giọng.

## Các bước

1. Mở file `.agents/rules/thuong-hieu.md` hiện có để xem bố cục.
2. Hỏi chủ dự án **lần lượt từng câu**, chờ trả lời rồi mới hỏi câu tiếp:
   1. Tên thương hiệu là gì?
   2. Sản phẩm chính muốn làm video là gì? Giá bao nhiêu?
   3. Khách hàng chính là ai (tuổi, nghề, thói quen)?
   4. Một câu thông điệp bạn muốn khách nhớ?
   5. Màu thương hiệu (nếu có mã màu thì cho mã, chưa có thì mô tả, ví dụ "xanh lá đậm")?
   6. Font chữ đang dùng (chưa có thì bỏ qua)?
   7. Giọng văn: xưng gì, gọi khách là gì, trang trọng hay vui vẻ?
   8. Những từ, lời hứa không được nói?
3. Chưa có mã màu thì đề xuất 3 màu (chính, phụ, nhấn) hợp với mô tả, ghi mã màu, hỏi chủ dự án có đồng ý không.
4. Viết bản nháp đúng bố cục file mẫu: Thương hiệu, Màu sắc, Chữ, Giọng văn, Quy tắc video. Giữ dòng `trigger: always_on` ở đầu file.
5. Cho chủ dự án xem toàn bộ bản nháp. Đồng ý thì:
   - Chép file cũ vào `_backup/thuong-hieu_<ngày-giờ>.md`.
   - Ghi bản mới vào `.agents/rules/thuong-hieu.md`.
6. Báo lại đường dẫn file đã lưu.

## Lưu ý

- Không bịa số liệu, giải thưởng, lời khen của khách.
- Chủ dự án chưa có thương hiệu riêng thì giữ nguyên file mẫu Cà Phê Mây Núi.
