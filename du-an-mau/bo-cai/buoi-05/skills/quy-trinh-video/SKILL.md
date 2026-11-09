---
name: quy-trinh-video
description: Quy trình tổng chạy bằng một câu lệnh, đi từ thương hiệu, sản phẩm, hook, kịch bản, ảnh, video tới đăng bài. Có 3 điểm duyệt (sau kịch bản, sau ảnh, trước khi đăng), mỗi bước đều gọi agent soát hoặc chấm. Dùng khi người dùng nói "làm trọn một video", "chạy cả quy trình", "từ sản phẩm ra video rồi đăng", hoặc gõ /quy-trinh-video.
---

# Quy trình video một câu lệnh

Skill này không tự làm từng việc. Nó gọi lần lượt các skill đã cài từ buổi 1 tới buổi 5, giống quản đốc cầm danh sách việc: xong khâu nào thì cho người kiểm tra khâu đó, tới điểm duyệt thì đưa chủ dự án xem.

## Câu lệnh mẫu

```
/quy-trinh-video
Làm video cho sản phẩm trong du-lieu/TEN-FILE-SAN-PHAM.md, đăng lên TIKTOK.
```

## Trước khi chạy

1. Kiểm tra đã cài đủ các skill và agent sau trong `.agents/`. Thiếu cái nào thì dừng, báo tên cái đang thiếu và buổi học có nó:

| Buổi | Skill | Agent soát, chấm |
|---|---|---|
| 1 | `file-thuong-hieu`, `hook-video-3-giay` | `nguoi-soat` |
| 2 | `kich-ban-video` | `nguoi-cham-kich-ban` |
| 3 | `hinh-anh-nhan-vat` | `nguoi-soat-anh` |
| 4 | `dung-video` | `nguoi-cham-video` |
| 5 | `dang-bai`, `quy-trinh-video` | `dao-dien` |

2. Hỏi đúng 1 câu nếu câu lệnh chưa nói: "Video cho sản phẩm nào (file trong du-lieu/), đăng lên kênh nào?"
3. Trình bày kế hoạch 7 bước bên dưới, chờ chủ dự án đồng ý rồi mới chạy.
4. Tạo file nhật ký `kich-ban/quy-trinh-<ten-san-pham>.md`. Xong mỗi bước ghi một dòng: giờ, bước, file đã tạo, kết quả soát. Nhờ vậy dừng giữa chừng thì lần sau làm tiếp được từ bước còn dở.

## 7 bước

| Bước | Việc | Gọi skill | Gọi agent | Kết quả |
|---|---|---|---|---|
| 1 | Thương hiệu | đọc `.agents/rules/thuong-hieu.md`; file còn là mẫu mà chủ dự án có thương hiệu riêng thì hỏi có muốn chạy `file-thuong-hieu` không | | đã nắm màu, giọng, điều cấm |
| 2 | Sản phẩm | đọc file sản phẩm trong `du-lieu/` | | thiếu giá, ưu đãi thì hỏi, không bịa |
| 3 | Hook | `hook-video-3-giay` | `nguoi-soat` | `kich-ban/hook-<ten>.md` |
| 4 | Kịch bản | `kich-ban-video` (dùng hook tốt nhất) | `nguoi-cham-kich-ban` | file kịch bản trong `kich-ban/` |
| | **Điểm duyệt 1** | | `dao-dien` tổng hợp | chủ dự án duyệt kịch bản |
| 5 | Ảnh, nhân vật | `hinh-anh-nhan-vat` | `nguoi-soat-anh` | ảnh trong `anh/` |
| | **Điểm duyệt 2** | | `dao-dien` tổng hợp | chủ dự án duyệt ảnh |
| 6 | Video | `dung-video` | `nguoi-cham-video` | video MP4 trong `video/` |
| 7 | Đăng | `dang-bai` | `nguoi-soat` (soát caption) | trang đăng điền sẵn, dừng trước nút Đăng |
| | **Điểm duyệt 3** | | `dao-dien` tổng hợp | chủ dự án tự bấm Đăng |

## Cách chạy từng bước

1. Gọi skill của bước đó, làm đúng theo hướng dẫn trong skill.
2. Xong thì gọi agent soát, chấm của bước đó. Agent báo lỗi thì sửa theo bảng soát, tối đa 2 vòng. Sau 2 vòng vẫn chưa đạt thì dừng, hỏi chủ dự án.
3. Ghi một dòng vào file nhật ký.
4. Sang bước tiếp theo. Bước nào cần dùng kết quả bước trước thì lấy đúng file đã lưu, không viết lại.

## Ba điểm duyệt (bắt buộc dừng)

Tới mỗi điểm duyệt:
1. Gọi agent `dao-dien` đọc kết quả các bước vừa xong và kết quả soát, viết báo cáo ngắn.
2. Đưa báo cáo cho chủ dự án, hỏi: "Bạn duyệt để làm tiếp, hay cần sửa chỗ nào?"
3. Chỉ chạy tiếp khi chủ dự án trả lời rõ là đồng ý. Im lặng, "để xem", "chắc được" đều coi là chưa duyệt.

| Điểm duyệt | Vì sao dừng ở đây |
|---|---|
| 1. Sau kịch bản | Sửa chữ thì rẻ. Kịch bản sai mà đi tiếp thì phải làm lại cả ảnh lẫn video. |
| 2. Sau ảnh | Tạo ảnh tốn lượt dùng ChatGPT. Ảnh lệch nhân vật, sai màu thì sửa trước khi dựng. |
| 3. Trước khi đăng | Bài đăng đi ra ngoài, người khác thấy. Chủ dự án tự bấm Đăng. |

## Dùng lại cho sản phẩm khác

Chỉ cần đổi tên file sản phẩm trong câu lệnh. Thương hiệu, nhân vật, phong cách giữ nguyên nên video thứ hai đồng bộ với video thứ nhất. Sản phẩm thuộc thương hiệu khác thì chạy `file-thuong-hieu` trước.

## Ranh giới

- Không bỏ qua điểm duyệt nào, kể cả khi chủ dự án bảo "chạy một mạch luôn". Có thể rút gọn báo cáo, không bỏ bước hỏi.
- Không tự bấm Đăng. Không đăng hàng loạt.
- Không xóa file. Bản cũ chép vào `_backup/` trước khi sửa, theo `AGENTS.md`.
- Khi chạy theo lịch (không có chủ dự án ngồi trước máy): chỉ làm tới Điểm duyệt 1 rồi dừng, ghi nhật ký, chờ chủ dự án vào duyệt.
