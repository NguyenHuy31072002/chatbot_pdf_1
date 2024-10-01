
chatbot_pdf/
│
├── pdf_img/
│   ├── __pycache__/             # Thư mục tạm chứa các file biên dịch Python.
│   ├── extract_text.py          # File chứa mã để trích xuất văn bản từ tệp PDF.
│   ├── pdf_to_img.py            # File chứa mã để chuyển đổi PDF thành hình ảnh.
│
├── services/
│   ├── __pycache__/             # Thư mục tạm chứa các file biên dịch Python.
│   ├── chatbot.py                # File chứa logic chính của chatbot, xử lý các câu hỏi và phản hồi.
│   ├── text_processing.py        # File chứa mã xử lý văn bản, có thể bao gồm làm sạch và chuẩn hóa dữ liệu văn bản.
│   ├── vector_store.py           # File quản lý cơ sở dữ liệu vector, có thể dùng để lưu trữ và truy vấn các vector.
│
├── utils/
│   ├── __pycache__/             # Thư mục tạm chứa các file biên dịch Python.
│   ├── embeddings.py             # File chứa mã để tạo và quản lý các vector nhúng cho văn bản.
│   ├── session.py                # File xử lý các phiên làm việc của người dùng, lưu trữ thông tin phiên.
│
├── .env                          # File cấu hình chứa các biến môi trường, như khóa API và thông tin bảo mật khác.
├── 999.pdf                       # Tệp PDF mà dự án có thể sẽ xử lý hoặc tham chiếu đến.
├── app.py                        # File chính để khởi động ứng dụng chatbot.
└── requirements.txt              # File liệt kê các thư viện cần thiết cho dự án Python.
