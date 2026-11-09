# Buổi 1: Nền tảng Agent, Skill, MCP và cách làm việc

Thứ 3, 10/11/2026, 20:00 tới 22:00.

**Hết buổi bạn có:** máy chạy được AI Agent, một file thương hiệu của chính bạn, một skill đầu tiên cài từ GitHub và chạy được.

---

## Phần 1. Ba khái niệm, hiểu bằng ví dụ

| Khái niệm | Hiểu đơn giản | Ví dụ trong khóa |
|---|---|---|
| **Chatbot** | Bạn hỏi, nó trả lời một đoạn chữ. Muốn ra file thì bạn tự chép, tự làm tiếp | ChatGPT trên web |
| **AI Agent** | Một trợ lý làm việc ngay trên máy bạn: tự lập kế hoạch, mở file, tạo file, chạy công cụ, làm xong báo lại | Claude Code, Antigravity |
| **Skill** | Một quy trình được viết sẵn thành file. Gõ tên skill là Agent làm đúng các bước đó, lần nào cũng như nhau | Skill viết hook 3 giây (hôm nay), skill kịch bản (buổi 2) |
| **MCP** | Cái "ổ cắm" để Agent nối sang công cụ khác: tạo ảnh, đọc mạng xã hội, điều khiển trình duyệt | ChatGPT Image MCP (buổi 3) |

Hình dung: Agent là một nhân viên mới. Skill là sổ tay quy trình bạn đưa cho nhân viên đó. MCP là chìa khóa để nhân viên vào được các phần mềm khác của công ty.

---

## Phần 2. Mở dự án đầu tiên

1. Tạo một thư mục cho dự án video, ví dụ `Documents\du-an-video`.
2. Chép thư mục `bo-skill` và thư mục `01-buoi-01-nen-tang-agent-skill-mcp\mau` (đã tải ở bước chuẩn bị) vào thư mục dự án.
3. Mở Agent ngay trong thư mục dự án:
   - **Claude Code:** mở thư mục trong File Explorer, bấm vào thanh địa chỉ, gõ `powershell`, Enter. Trong cửa sổ hiện ra gõ `claude`.
   - **Antigravity:** mở ứng dụng, chọn **Open Folder**, chọn thư mục dự án.
4. Gõ thử câu đầu tiên:

```
Chào bạn. Hãy cho tôi biết trong thư mục này đang có những file và thư mục nào, mỗi cái dùng để làm gì.
```

---

## Phần 3. Cách giao việc cho Agent

Bốn bước, áp dụng cho mọi việc trong khóa:

1. **Giao việc rõ:** nói bạn gửi gì, cần làm gì, kết quả là file gì, lưu ở đâu.
2. **Để Agent lập kế hoạch trước:** bảo Agent trình bày cách làm, chưa làm ngay.
   - Claude Code: bấm `Shift+Tab` tới khi thấy chữ *plan mode*.
   - Antigravity: chọn chế độ *Planning* trước khi gửi.
3. **Duyệt rồi mới cho làm:** đọc kế hoạch, sửa chỗ chưa đúng, rồi đồng ý.
4. **Kiểm tra kết quả:** mở file Agent tạo ra, xem có đúng yêu cầu không.

Mẫu giao việc:

```
Tôi gửi bạn: file mau/CLAUDE.md, đây là bộ nhận diện của một thương hiệu mẫu.

Việc cần làm:
1. Đọc file đó.
2. Tóm tắt lại cho tôi trong 5 gạch đầu dòng: thương hiệu bán gì, cho ai, màu chính, giọng văn, điều cấm.
3. Trình bày kế hoạch trước, tôi đồng ý thì mới làm.

Kết quả: trả lời ngay trong khung chat, không tạo file.
```

---

## Phần 4. GitHub cơ bản

- **GitHub** là nơi lưu và chia sẻ code, tài liệu, skill. Mỗi dự án trên GitHub gọi là một **repo** (kho).
- Tải một repo về máy: bấm nút xanh **Code**, chọn **Download ZIP**, giải nén. Đã cài Git thì dùng `git clone <đường link repo>`.
- Rất nhiều skill hay được chia sẻ miễn phí trên GitHub. Trước khi cài skill lạ, mở file `SKILL.md` ra đọc xem nó làm gì.

---

## Phần 5. Cài skill đầu tiên

Skill phải nằm đúng thư mục thì Agent mới thấy:

| Agent | Thư mục skill của dự án |
|---|---|
| Claude Code | `.claude/skills/<tên-skill>/SKILL.md` |
| Antigravity | `.agents/skills/<tên-skill>/SKILL.md` |

Cách dễ nhất là nhờ chính Agent cài:

```
Tôi gửi bạn: thư mục bo-skill/hook-video-3-giay, trong đó có file SKILL.md là một skill viết câu mở đầu video.

Việc cần làm:
1. Mở file SKILL.md, nói cho tôi biết skill này làm gì, có lệnh nào nguy hiểm không.
2. Chép cả thư mục hook-video-3-giay vào thư mục skill của dự án (Claude Code: .claude/skills/, Antigravity: .agents/skills/). Chưa có thư mục thì tạo mới.
3. Kiểm tra lại đường dẫn sau khi chép.

Kết quả: báo tôi đường dẫn file SKILL.md sau khi cài.
```

Cài xong, đóng Agent rồi mở lại để Agent nhận skill mới.

---

## Phần 6. Viết file thương hiệu của bạn

File thương hiệu là "sổ tay" Agent đọc trước mỗi việc, để video nào cũng đúng màu, đúng giọng.

| Agent | Tên và chỗ để file thương hiệu |
|---|---|
| Claude Code | `CLAUDE.md` ở thư mục gốc dự án |
| Antigravity | `.agents/rules/thuong-hieu.md` trong dự án |

Nhờ Agent phỏng vấn bạn rồi tự viết:

```
Tôi gửi bạn: file mau/CLAUDE.md, đây là file thương hiệu mẫu của Cà Phê Mây Núi.

Việc cần làm:
1. Hỏi tôi từng câu một để lấy thông tin thương hiệu của tôi: tên, sản phẩm, khách hàng, thông điệp, màu sắc, font, giọng văn, điều cấm.
2. Hỏi xong, viết file thương hiệu của tôi theo đúng bố cục file mẫu.
3. Cho tôi xem trước, tôi đồng ý thì mới lưu.

Kết quả: lưu thành file CLAUDE.md ở thư mục gốc dự án (dùng Antigravity thì lưu vào .agents/rules/thuong-hieu.md).
```

Chưa có thương hiệu riêng thì dùng luôn file mẫu Cà Phê Mây Núi để thực hành.

---

## Phần 7. Chạy skill đầu tiên

Claude Code gõ:

```
/hook-video-3-giay Viết hook cho video giới thiệu sản phẩm chính của thương hiệu tôi.
```

Antigravity gõ:

```
Dùng skill hook-video-3-giay viết hook cho video giới thiệu sản phẩm chính của thương hiệu tôi.
```

Agent sẽ đọc file thương hiệu, trả về bảng 5 hook. Kiểm tra: hook có đúng giọng văn không, có dùng từ bị cấm không.

---

## Kiểm tra cuối buổi

- [ ] Mở được Agent trong thư mục dự án.
- [ ] Có file thương hiệu của mình (`CLAUDE.md` hoặc `.agents/rules/thuong-hieu.md`).
- [ ] Đã cài skill `hook-video-3-giay` và chạy ra bảng 5 hook.

Chụp màn hình bảng hook gửi vào nhóm lớp.

## Bài tập trước buổi 2

1. Sửa file thương hiệu cho thật đầy đủ: thêm 1 tới 2 sản phẩm bạn muốn làm video.
2. Chạy skill hook cho từng sản phẩm, chọn ra 1 hook ưng nhất.
3. Chuẩn bị thông tin sản phẩm (tên, công dụng, giá, ảnh sản phẩm nếu có) để buổi 2 viết kịch bản.

---

Đường dẫn thư mục skill, file thương hiệu tra theo tài liệu chính thức của Claude Code (https://code.claude.com/docs/en/skills) và Antigravity (https://antigravity.google/docs/skills) ngày 09/11/2026.
