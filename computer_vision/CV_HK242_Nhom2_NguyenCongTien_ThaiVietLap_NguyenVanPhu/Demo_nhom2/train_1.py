import torch
import os
import matplotlib
from ultralytics import YOLO
matplotlib.rcParams['backend'] = 'Agg'

MODEL_PATH = "yolo11n.pt"

class MyYOLO:
    def __init__(self):
        self.base_model = YOLO(MODEL_PATH)  # Sử dụng YOLOv11

    def training(self):
        results = self.base_model.train(
            data='data.yaml',  # Đặt đường dẫn phù hợp nếu khác
            batch=8,  # Điều chỉnh batch size phù hợp với máy
            device='cuda' if torch.cuda.is_available() else 'cpu',  # Sử dụng GPU nếu có
            pretrained=False,
            epochs=100,
            patience=20,
            amp=False,
            imgsz=640,  # Giảm kích thước ảnh để tránh quá tải VRAM
            project='yolov11_train/',
        )

if __name__ == "__main__":
    model = MyYOLO()
    model.training()