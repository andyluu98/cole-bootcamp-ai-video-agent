# Bootcamp AI Agent for Video Marketing

Tài liệu học viên khóa **Bootcamp AI Agent for Video Marketing** của Cole.vn. Giảng viên: Lưu Tuấn Anh.

Web khóa học: https://bootcamp-video.aithetech.com

Học online, 20:00 tới 22:00, thứ 3 và thứ 5 hằng tuần, khai giảng thứ 3 ngày 10/11/2026. Công cụ chính: Google Antigravity.

## Học xong 5 buổi, bạn có gì

- 01 video quảng cáo dọc 9:16, xuất MP4, đúng màu thương hiệu, có phụ đề, giọng đọc, nhạc nền.
- 01 quy trình tự động: kịch bản, hình ảnh, video, đăng bài, chạy bằng một câu lệnh, bạn duyệt trước khi đăng.
- Bộ skill và agent mang về.

## Bắt đầu

1. Làm trang [Chuẩn bị](https://bootcamp-video.aithetech.com/chuan-bi.html): cài Antigravity, đặt mức quyền an toàn.
2. Tải [du-an-mau.zip](https://bootcamp-video.aithetech.com/tai-ve/du-an-mau.zip), giải nén, mở thư mục `du-an-video` trong Antigravity.
3. Mỗi buổi tải bộ cài của buổi đó và làm theo trang thực hành.

## Cấu trúc repo

```
├── index.html, chuan-bi.html, buoi-1.html ... buoi-5.html   # trang web
├── slide/                     # slide trình chiếu từng buổi
├── du-an-mau/                 # thư mục dự án mẫu cho học viên
│   ├── AGENTS.md              # quy tắc làm việc, chống mất dữ liệu
│   ├── .agents/rules/         # file thương hiệu
│   └── bo-cai/buoi-0N/        # skill, agent, file mẫu của từng buổi
├── tai-ve/                    # file zip tải về (sinh bằng scripts/dong_goi.py)
└── assets/                    # giao diện web
```

## An toàn

- Agent chỉ làm trong thư mục dự án, không xóa file, bản cũ chuyển vào `_backup/` trước khi sửa.
- Không dán mật khẩu, mã khóa (API key) vào khung chat hay nhóm lớp.
- Đăng bài luôn có bước duyệt; thử trên tài khoản phụ trước.
