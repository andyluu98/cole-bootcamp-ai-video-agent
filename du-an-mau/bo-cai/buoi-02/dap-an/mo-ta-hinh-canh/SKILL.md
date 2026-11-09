---
name: mo-ta-hinh-canh
description: Tách mô tả hình ảnh từng cảnh từ một kịch bản đã viết trong kich-ban/ ra file danh sách riêng, mỗi cảnh đủ nhân vật, sản phẩm, bối cảnh, ánh sáng, góc máy, chuyển động máy quay, ảnh đầu cảnh và ảnh cuối cảnh, để tạo ảnh ở buổi 3. Dùng khi người dùng nói "tách mô tả hình", "mô tả hình cảnh", "chuẩn bị tạo ảnh từng cảnh", hoặc gõ /mo-ta-hinh-canh. Không dùng để viết kịch bản mới.
---

# Tách mô tả hình ảnh từng cảnh

Bản đáp án tham khảo của giảng viên. Học viên tự tạo skill này ở buổi 2; bài của bạn không cần giống từng chữ, chỉ cần ra đúng file và đúng định dạng.

Kịch bản do `/kich-ban-video` viết đã có phần mô tả hình ảnh, nhưng nằm lẫn trong kịch bản. Skill này tách phần đó ra một file danh sách riêng, giữ nhân vật giống hệt nhau ở mọi cảnh, và thêm gợi ý ảnh đầu cảnh, ảnh cuối cảnh. Buổi 3, skill `hinh-anh-nhan-vat` đọc file này để tạo ảnh.

## Trước khi làm

1. Tìm kịch bản trong `kich-ban/` (file `kich-ban-<ten-san-pham>.md`). Có nhiều file mà người dùng chưa nói rõ thì hỏi đúng 1 câu: "Tách mô tả hình cho kịch bản nào?"
2. Đọc `.agents/rules/thuong-hieu.md`: màu chính, màu phụ, màu nhấn, điều cấm.
3. Đọc file kịch bản: bảng phân cảnh (cột Cảnh, Giây, Hình ảnh, Chuyển động máy quay) và phần **Mô tả hình ảnh từng cảnh**.
4. Đọc thông tin sản phẩm trong `du-lieu/`.
5. Đọc khung `.agents/skills/mo-ta-hinh-canh/mau/mau-mo-ta-hinh-canh.md` và bài mẫu `.agents/skills/mo-ta-hinh-canh/examples/vi-du-mo-ta-hinh-canh.md`.
6. Trình bày kế hoạch ngắn: kịch bản nguồn, số cảnh, số nhân vật, tên file sẽ lưu. Chờ người dùng đồng ý rồi mới làm.

## Các bước

1. **Nhân vật cố định:** gom mô tả nhân vật trong các cảnh. Mỗi nhân vật viết một đoạn liền: tuổi, giới tính, khuôn mặt, tóc, trang phục (màu theo mã màu thương hiệu), phụ kiện. Kịch bản tả lệch giữa các cảnh (ví dụ cảnh 2 áo kem, cảnh 4 áo trắng) thì liệt kê chỗ lệch và hỏi người dùng chọn bản nào, không tự chọn.
2. **Bảng tổng các cảnh:** mỗi cảnh một dòng, số cảnh hai chữ số (01, 02...), kèm tên file ảnh buổi 3 sẽ tạo: `canh-NN-dau.png`, `canh-NN-cuoi.png`.
3. **Mô tả từng cảnh:** mỗi cảnh đủ các mục Nhân vật, Sản phẩm, Bối cảnh, Ánh sáng, Góc máy, Chuyển động máy quay, Ảnh đầu cảnh, Ảnh cuối cảnh, Tỷ lệ.
   - Cảnh có nhân vật: mục Nhân vật dán **nguyên văn** đoạn nhân vật cố định, rồi thêm đang làm gì, biểu cảm.
   - Chuyển động máy quay: chép đúng cột trong kịch bản.
   - Ảnh cuối cảnh chỉ khác ảnh đầu cảnh ở tư thế hoặc khoảng cách máy, suy ra từ chuyển động máy quay: "đẩy vào gần" thì ảnh cuối cận hơn; "kéo ra xa" thì ảnh cuối rộng hơn; "lia ngang" thì khung lệch sang bên; "đứng yên" thì nhân vật đổi một động tác nhỏ.
4. **Cần kiểm tra:** ghi các chỗ nhân vật lệch, chỗ `[CHỜ BỔ SUNG]`.

## Quy tắc

- Không thêm chữ, logo, giá, khẩu hiệu vào mô tả ảnh. Chữ và logo thêm lúc dựng video ở buổi 4.
- Không bịa chi tiết sản phẩm ngoài file trong `du-lieu/`. Thiếu thì ghi `[CHỜ BỔ SUNG]`.
- Nhân vật là người hư cấu, không tả giống người thật hay người nổi tiếng.
- Không sửa file kịch bản. Thấy kịch bản thiếu mô tả ở cảnh nào thì báo người dùng.

## Kết quả

1. Lưu vào `kich-ban/mo-ta-hinh-canh-<ten-san-pham>.md`, phần `<ten-san-pham>` giống hệt tên trong file kịch bản (ví dụ kịch bản `kich-ban-ca-phe-arabica-cau-dat.md` thì lưu `mo-ta-hinh-canh-ca-phe-arabica-cau-dat.md`). Giữ đúng tên và thứ tự 5 mục trong khung.
2. File trùng tên đã có: chép bản cũ vào `_backup/mo-ta-hinh-canh-<ten-san-pham>_<ngày-giờ>.md` trước, rồi mới ghi bản mới.
3. Báo lại đường dẫn file, số cảnh, các chỗ cần kiểm tra. Gợi ý bước tiếp: gọi agent `nguoi-soat` soát file, buổi 3 dùng file này với `/hinh-anh-nhan-vat`.

## Lưu ý

- Chỉ đọc, ghi trong thư mục dự án. Không xóa file nào.
