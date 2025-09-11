# 🌞 Solar Panel Fault Detection with YOLOv11-nano

This repository contains code to **train** and **evaluate** a YOLOv11-nano model for detecting multiple types of solar panel faults.

- Framework: **Ultralytics YOLO**
- Model: **yolo11n.pt** (COCO-pretrained)
- Classes: **Clean, Dust, Bird, Electrical, Physical, Snow**
- Dataset: Custom-labeled dataset (based on solar panel images)

---

## 📂 Repository Structure

- Data  
  - images  
    - train  # training images  
    - val    # validation images
    - test   # test images 
  - labels  
    - train  # YOLO-format labels for training  
    - val    # YOLO-format labels for validation
    - test   # test images 
  - data.yaml
- runs/               # training outputs (weights, logs, results)
- train.py            # training script
- test.py             # evaluation script
- yolo11n.pt          # pretrained weights

---

## 🧱 Dataset & Labels

The dataset contains **6 fault classes**:

- **Clean**
- **Dust**
- **Bird**
- **Electrical**
- **Physical**
- **Snow**

> Labels follow the YOLO format:  
> `<class_id> <x_center> <y_center> <width> <height>` (normalized values).

The dataset is split into **train (80%)** , **validation (10%)** and **test (10%)** sets.  
Make sure your dataset matches the expected folder structure before training.

---

## ⚙️ Setup

```bash
# (Optional) Create a clean environment
conda create -n yolo-solar python=3.10 -y
conda activate yolo-solar

# Install dependencies
pip install ultralytics opencv-python numpy pandas matplotlib

# (GPU) Ensure CUDA-compatible PyTorch is installed
python -c "import torch; print(torch.cuda.is_available())"

```

## 🚀 Training

- To start training the YOLOv11-nano model on your dataset  
- Loads COCO-pretrained yolo11n.pt checkpoint.  
- Trains for 100 epochs at 640×640 resolution (adjustable).  
- Update the data.yaml path in train.py:  
  - results = model.train(data="C:/path/to/data.yaml", epochs=100, imgsz=640)
- Results are saved to:
  - weights/best.pt — best performing weights
  - weights/last.pt — last epoch weights
  - results.png — training curves (loss, mAP, precision, recall)

---

## 🔎 Inference / Testing

After training, you can run inference on **test images**:

---

## 🧰 Tips & Troubleshooting

- Dataset Paths  
  - Ensure data.yaml points to the correct images/train, images/val, labels/train, and labels/val directories.

- Windows Multiprocessing train.py uses:
  - from multiprocessing import freeze_support
- GPU Acceleration:    
  - If GPU is not used, check PyTorch CUDA support  
- Auto-Labeling (Optional)  
  - train.py contains a commented-out block to auto-generate YOLO labels from filenames ending with _0 or _1.

---

## 📜 License & Credit

- **Code:** Licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.  
- **Dataset:** [Kaggle — Solar Panels Dirt Detection](https://www.kaggle.com/datasets/pythonafroz/solar-panel-images) — **Unknown License**  
  > No explicit license information provided on the dataset page at the time of download.  
  > Please check the dataset’s Kaggle page for any updates or restrictions before public/commercial use.


