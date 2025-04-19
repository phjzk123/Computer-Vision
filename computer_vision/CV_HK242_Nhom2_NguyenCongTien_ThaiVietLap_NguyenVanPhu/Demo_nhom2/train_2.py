from ultralytics import YOLO
import matplotlib
matplotlib.rcParams['backend'] = 'Agg'

class my_yolo:
    def __init__(self):
        self.base_model = YOLO('yolo11n.pt')

    def training(self):
        results = self.base_model.train(
            data="/export/users/1173171/iDragonCloud/Documents/ASL_Yolo_8/data/data.yaml",
            batch=64,
            device=0,
            pretrained=False,
            epochs=1000,
            patience=50,
            imgsz=1024,
            project='runs/test/',
        )

model = my_yolo()
model.training()
