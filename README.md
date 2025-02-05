# Pikachu Matching Game  

Đây là dự án trò chơi Pikachu Matching Game được phát triển bằng Python sử dụng thư viện `pygame` và cơ sở dữ liệu `SQLite`.  

# Thành viên nhóm:
1. Nguyễn Hoàng Ý Nhi 
2. Nguyễn Đức Tâm 
3. Nguyễn Nguyễn Trâm Anh 
4. Lê Hữu Nhật
5. Dương Thiên Phú
6. Lê Bảo Trân

[Link video demo](https://www.youtube.com/watch?v=Et3e5lX0GOU&t=21s)
## 1. Yêu cầu hệ thống  

### 1.1. Công cụ và thư viện cần thiết  
- Python 3.x  
- Thư viện `pygame`  
- Thư viện `sqlite3` 

## 2. Hướng dẫn triển khai  

### 2.1. Các bước thực hiện  

**Bước 1:** Clone source code về máy  
```
git clone <https://github.com/24122013/Pikachu_LDCB4>
cd <tên-thư-mục-dự-án>
```

**Bước 2:** Mở tệp `main.py` bằng IDE thích hợp  

**Bước 3:** Mở Terminal và nhập lệnh  
```
pip install pygame
pip install sqlite3
```

**Bước 4:** Chạy lệnh sau để khởi động trò chơi  
```
python main.py
```

## 3. Cấu trúc thư mục  
```
📂 PikachuMatchingGame
 ┣ 📂 __pycache__    # Thư mục cache của Python
 ┣ 📂 font           # Chứa các tệp font chữ sử dụng trong game
 ┣ 📂 images         # Chứa hình ảnh của trò chơi
 ┣ 📂 music          # Chứa nhạc nền của trò chơi
 ┣ 📂 sound          # Chứa hiệu ứng âm thanh trong game
 ┣ 📜 BFS.py         # Thuật toán tìm đường nối giữa các ô Pikachu
 ┣ 📜 main.py        # Chương trình chính để khởi chạy game
 ┣ 📜 users.db       # Cơ sở dữ liệu SQLite lưu thông tin người chơi
 ┗ 📜 README.md      # Hướng dẫn sử dụng & triển khai dự án
```

## 4. Tính năng chính  
- Giao diện đồ họa đẹp mắt sử dụng `pygame`.  
- 3 chế độ chơi: dễ, trung bình, khó với kích thước bàn chơi khác nhau.  
- Hệ thống đăng nhập & lưu tiến trình sử dụng `SQLite`.  
- Hiệu ứng âm thanh: nhạc nền, âm thanh khi ghép ô đúng/sai, thắng/thua.  
- Thuật toán BFS giúp kiểm tra đường nối giữa các ô một cách nhanh chóng.  
- Gợi ý nước đi sau 20 giây nếu người chơi chưa tìm thấy cặp hợp lệ.  

## 5. Cách chơi  
1. Chạy `main.py` để bắt đầu trò chơi.  
2. Đăng nhập hoặc tạo tài khoản mới.  
3. Chọn mức độ khó phù hợp.  
4. Tìm và ghép nối hai ô giống nhau bằng tối đa 3 đường gấp khúc.  
5. Hoàn thành màn chơi trong thời gian quy định để tiếp tục màn tiếp theo.  
6. Nếu hết thời gian hoặc không thể nối hết các ô, bạn sẽ mất 1 mạng.  
