# Bootcamp AI Agent for Video Marketing

Tài liệu học viên khóa **Bootcamp AI Agent for Video Marketing** của Cole.vn. Giảng viên: Lưu Tuấn Anh.

Học online, 20:00 tới 22:00, thứ 3 và thứ 5 hằng tuần, khai giảng thứ 3 ngày 10/11/2026.

## Học xong 5 buổi, bạn có gì

- Máy của bạn chạy được AI Agent, cài được skill từ GitHub, nối được MCP.
- 01 video quảng cáo dọc 9:16, xuất MP4, đúng màu thương hiệu, có phụ đề, giọng đọc, nhạc nền.
- 01 quy trình tự động: kịch bản, hình ảnh, video, đăng bài, chạy bằng một câu lệnh, bạn duyệt trước khi đăng.
- Bộ 4 skill mang về: kịch bản, hình ảnh và nhân vật, dựng video, đăng bài.

## Lộ trình

| Buổi | Nội dung | Thư mục |
|---|---|---|
| 1 | Nền tảng: Agent, Skill, MCP và cách làm việc | [01-buoi-01-nen-tang-agent-skill-mcp](01-buoi-01-nen-tang-agent-skill-mcp/) |
| 2 | Kịch bản video bằng Agent | cập nhật trước buổi 2 |
| 3 | Hình ảnh và khóa nhân vật | cập nhật trước buổi 3 |
| 4 | Dựng và hiệu chỉnh video | cập nhật trước buổi 4 |
| 5 | Đăng bài tự động và đấu nối quy trình | cập nhật trước buổi 5 |

## Chuẩn bị trước buổi 1

1. **Máy tính:** Windows 10/11 hoặc macOS, RAM từ 8GB, ổ đĩa còn trống tối thiểu 30GB.
2. **Tài khoản:**
   - Claude Pro (để dùng Claude Code). Gói miễn phí của Claude không dùng được Claude Code.
   - Hoặc tài khoản Google nếu bạn dùng Antigravity thay cho Claude Code.
   - Tài khoản GitHub miễn phí: đăng ký tại https://github.com/signup
   - ChatGPT Plus: cần từ buổi 3 (tạo hình ảnh), chưa cần ở buổi 1.
3. **Cài một trong hai AI Agent:**
   - **Claude Code**, mở PowerShell (Windows) rồi dán lệnh:
     ```powershell
     irm https://claude.ai/install.ps1 | iex
     ```
     Trên macOS mở Terminal rồi dán:
     ```bash
     curl -fsSL https://claude.ai/install.sh | bash
     ```
     Cài xong gõ `claude` để đăng nhập bằng tài khoản Claude Pro. Windows nên cài thêm Git for Windows (https://git-scm.com/downloads/win) để Claude Code chạy lệnh ổn định hơn.
   - **Antigravity**: tải tại https://antigravity.google rồi đăng nhập bằng tài khoản Google.
4. **Tải tài liệu khóa về máy:** bấm nút xanh **Code** ở đầu trang này, chọn **Download ZIP**, giải nén ra một thư mục, ví dụ `Documents\bootcamp-video`. Bạn nào đã cài Git thì dùng lệnh:
   ```bash
   git clone https://github.com/andyluu98/cole-bootcamp-ai-video-agent.git
   ```

Lệnh cài tra từ tài liệu chính thức https://code.claude.com/docs/en/setup ngày 09/11/2026. Nhà cung cấp có thể đổi lệnh, nếu lệnh lỗi hãy chụp màn hình gửi vào nhóm lớp.

## Cấu trúc thư mục

```
cole-bootcamp-ai-video-agent/
├── README.md                              # trang bạn đang đọc
├── 01-buoi-01-nen-tang-agent-skill-mcp/
│   ├── bai-hoc-buoi-01.md                 # làm theo từng bước trên lớp
│   └── mau/                               # file thương hiệu mẫu để sửa thành của bạn
└── bo-skill/                              # các skill của khóa, thêm dần theo buổi
    └── hook-video-3-giay/SKILL.md         # skill đầu tiên (buổi 1)
```

## Lưu ý khi học

- Dùng dữ liệu sản phẩm, thương hiệu của bạn hoặc dữ liệu mẫu trong khóa; không dán mật khẩu, mã khóa (API key) vào khung chat hay vào nhóm lớp.
- Đăng bài tự động (buổi 5) nên thử trên tài khoản TikTok, Facebook phụ trước.
- Nhạc nền, font, giọng đọc dùng cho quảng cáo cần có bản quyền thương mại; nội dung làm bằng AI gắn nhãn theo quy định của từng nền tảng.
