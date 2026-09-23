import os
import re
import shutil
from ultralytics import YOLO
"""  
# Klasör yolları
image_folder = r"Data/images/val"
label_folder = r"Data/labels/val"
os.makedirs(label_folder, exist_ok=True)

if os.path.exists(label_folder):
    shutil.rmtree(label_folder)
os.makedirs(label_folder)

CLASSES = ['Clean', 'Dust','Bird','Electrical','Physical','Snow']
class2id = {c.lower(): i for i, c in enumerate(CLASSES)}

for fname in os.listdir(image_folder):  
    if not fname.lower().endswith((".jpg", ".jpeg", ".png")):
        continue

    stem = os.path.splitext(fname)[0]
    class_name = stem.split(" (")[0].strip().lower()
    cid = class2id.get(class_name)
    if cid is None:
        print("[SKIP]", fname)
        continue

    with open(os.path.join(label_folder, stem + ".txt"), "w", encoding="utf-8") as f:
        f.write(f"{cid} 0.5 0.5 1 1\n")
 """



def main():
    model = YOLO("yolo11n.pt")
    # data.yaml dosyasının bilgisayarınızdaki tam yolunu buraya yazın
    results = model.train(data="data.yaml", epochs=100, imgsz=640)

if __name__ == "__main__":
    from multiprocessing import freeze_support
    freeze_support()
    main() 

