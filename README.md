
# 🧠 ASL YOLOv11 - Nhận Diện Ngôn Ngữ Ký Hiệu Mỹ

Dự án sử dụng mô hình YOLOv11 để huấn luyện và nhận diện ngôn ngữ ký hiệu (American Sign Language - ASL). Bao gồm mã huấn luyện mô hình, nhận diện thời gian thực qua webcam, và yêu cầu môi trường cần thiết.

## 📁 Cấu Trúc Dự Án

```
.
├── app.py              # Nhận diện bàn tay và ký hiệu bằng YOLO + MediaPipe
├── train_1.py          # Script huấn luyện mô hình sử dụng YOLOv11 (dùng data.yaml)
├── train_2.py          # Script huấn luyện dùng đường dẫn tuyệt đối
├── requirements.txt    # Thư viện phụ thuộc
└── README.md           # Tài liệu hướng dẫn (file này)
```

---

## 🚀 Cài Đặt

### 1. Tạo môi trường ảo (tùy chọn nhưng khuyến nghị)

```bash
python -m venv venv
source venv/bin/activate       # Trên Linux/macOS
venv\Scripts\activate          # Trên Windows
```

### 2. Cài đặt thư viện cần thiết

```bash
pip install -r requirements.txt
```

---

## 🏋️‍♂️ Huấn Luyện Mô Hình

### Huấn luyện với `train_1.py`

```bash
python train_1.py
```

- Sử dụng file `data.yaml` trong thư mục hiện tại
- Batch size: 8
- Epochs: 100
- Kích thước ảnh: 640
- Sử dụng GPU nếu có

### Huấn luyện với `train_2.py`

```bash
python train_2.py
```

- Sử dụng đường dẫn tuyệt đối đến `data.yaml`
- Batch size: 64
- Epochs: 1000
- Kích thước ảnh: 1024
- Dùng CUDA device 0

> 🔺 Cả hai file đều sử dụng mô hình `yolo11n.pt`, hãy đảm bảo file này có trong thư mục làm việc.

---

## 📡 Nhận Diện Thời Gian Thực với `app.py`

Chạy nhận diện bàn tay bằng webcam:

```bash
python app.py
```

- Dùng mô hình YOLO để phát hiện tay
- Dùng MediaPipe để vẽ keypoints trên bàn tay
- Nhấn `q` để thoát giao diện camera

---

## 🧠 Công Nghệ Sử Dụng

- [Ultralytics YOLOv11](https://github.com/ultralytics/ultralytics)
- OpenCV
- MediaPipe
- PyTorch

---

## ✅ Yêu Cầu Phần Cứng

- GPU (nếu muốn huấn luyện nhanh)
- Webcam để chạy `app.py`

---

## 📌 Lưu Ý

- Cần chuẩn bị đúng định dạng file `data.yaml` cho YOLO (đường dẫn hình ảnh, nhãn,...).
- Hãy chắc chắn các hình ảnh trong dataset phù hợp với nhận diện ký hiệu tay.

---

## 👨‍💻 Tác Giả

Dự án được phát triển nhằm hỗ trợ việc nhận diện ngôn ngữ ký hiệu.
