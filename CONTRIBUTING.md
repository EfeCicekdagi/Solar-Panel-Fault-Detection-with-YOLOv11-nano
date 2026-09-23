# Katkıda Bulunma Rehberi (Contributing)

Bu projeye katkıda bulunmayı düşündüğünüz için teşekkürler! Aşağıdaki adımlar, projeyi yerelde nasıl kuracağınızı ve nasıl katkı sağlayacağınızı açıklamaktadır.

## Projeyi Yerelde Kurma

1. Repoyu bilgisayarınıza klonlayın:
   ```bash
   git clone https://github.com/EfeCicekdagi/Solar-Panel-Fault-Detection-with-YOLOv11-nano.git
   cd Solar-Panel-Fault-Detection-with-YOLOv11-nano
   ```

2. (İsteğe bağlı ancak önerilir) Yeni bir sanal ortam oluşturun:
   ```bash
   conda create -n yolo-solar python=3.10 -y
   conda activate yolo-solar
   ```

3. Gerekli bağımlılıkları yükleyin:
   ```bash
   pip install ultralytics opencv-python numpy pandas matplotlib
   ```

## Test Etme

Yaptığınız değişikliklerin projeyi bozmadığından emin olmak için modeli test edebilirsiniz. Test işlemi için `test.py` dosyasını çalıştırabilir veya CLI üzerinden `yolo` komutunu kullanabilirsiniz:

```bash
python test.py
```
veya
```bash
yolo predict model=runs/detect/train/weights/best.pt source=Data/images/test
```

*Not: Kendi verisetinizde deniyorsanız, `data.yaml` içindeki yolların doğru yapılandırıldığından emin olun.*

## Hata Bildirme (Bug Report)

Karşılaştığınız hataları bildirmek için GitHub'daki **Issues** sekmesini kullanın. Hata bildirimi yaparken, hatayı yeniden üretebilmemiz için sağlanan "Bug Report" şablonunu eksiksiz doldurmaya özen gösterin (İşletim sistemi, Python sürümü, hatanın adımları vb.).

## Pull Request (PR) Açma

1. Yeni bir dal (branch) oluşturun: `git checkout -b ozellik-veya-hata-adi`
2. Değişikliklerinizi yapın ve test edin (`test.py` sorunsuz çalışmalıdır).
3. Commit mesajlarınızı açıklayıcı bir şekilde yazın.
4. Değişikliklerinizi push'layın: `git push origin ozellik-veya-hata-adi`
5. GitHub üzerinden bir Pull Request açın. PR açarken size sunulan şablonu doldurun.
