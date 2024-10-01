# CHATBOT WITH PDF AND DOC
![Miêu tả source code](https://github.com/NguyenHuy31072002/chatbot_pdf_1/blob/main/img/pdf.png)

## Overview
Kho lưu trữ này chứa cách triển khai cơ bản của một ứng dụng web bằng API chatbot Gemini AI. Ứng dụng web được xây dựng bằng khung Streamlit trong Python. Chatbot Gemini AI được cung cấp bởi API Gemini flash, cho phép người dùng tương tác với chatbot được đào tạo trên bộ dữ liệu khổng lồ gồm 1,5 nghìn tỷ mã thông báo. 
Xin lưu ý rằng API Gemini cho phép 60 truy vấn mỗi phút.

## Local Setup
### Bước 1: Sao chép kho lưu trữ
```bash
git clone https://github.com/NguyenHuy31072002/chatbot_pdf_1.git
```

### Bước 2: Thêm API Key
Thay thế dòng mã sau trong .env bằng khóa API Gemini của bạn và sử dụng ứng dung lưu trữ ảnh trên cloudinary:
```python
GOOGLE_API_KEY=YOUR_API_KEY
TOGETHER_API_KEY=YOUR_API_KEY
CLOUDINARY_CLOUD_NAME=YOUR_CLOUD
CLOUDINARY_API_KEY=YOUR_CLOUDINARY_API_KEY
CLOUDINARY_API_SECRET=YOUR_CLOUDINARY_API_SECRET
```
Bạn có thể lấy khóa API của mình từ [tại đây](https://makersuite.google.com/app/apikey). Khi bạn có chìa khóa, hãy chuyển sang bước tiếp theo.
