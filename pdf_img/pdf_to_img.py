from pdf2image import convert_from_path
import cloudinary
import cloudinary.uploader
import os
from dotenv import load_dotenv

# Load các biến môi trường từ file .env
load_dotenv()

def pdf_to_images_and_upload(pdf_path):
    # Cấu hình Cloudinary bằng các biến môi trường
    cloudinary.config(
        cloud_name=os.getenv('CLOUDINARY_CLOUD_NAME'),
        api_key=os.getenv('CLOUDINARY_API_KEY'),
        api_secret=os.getenv('CLOUDINARY_API_SECRET')
    )
    
    # Chuyển đổi pdf thành hình ảnh
    images = convert_from_path(pdf_path)
    image_links = []
    for page_num, image in enumerate(images):
        image_filename = f"page_{page_num + 1}.png"
        image.save(image_filename, 'JPEG')
        # Tải hình ảnh lên Cloudinary
        result = cloudinary.uploader.upload(image_filename)
        image_links.append(result['secure_url'])
        # Xóa hình ảnh sau khi tải lên
        os.remove(image_filename)
    return image_links
