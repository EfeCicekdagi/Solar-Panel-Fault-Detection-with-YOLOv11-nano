from ultralytics import YOLO

def main():
    model = YOLO("runs/detect/train/weights/best.pt")
    metrics = model.val(
        data="C:/Users/hp/Desktop/AI/Solar Panel Project/Task4_EfeÇiçekdağı/Data/data.yaml",
        split="test",
        imgsz=640,
        batch=16,
        workers=2,   
        device=0
    )
    print(metrics)

if __name__ == "__main__":
    from multiprocessing import freeze_support
    freeze_support()
    main()