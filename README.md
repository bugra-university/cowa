# Cloud Oriented Web Applications (COWA)

Bu proje, bulut tabanlı web uygulamaları geliştirmek için bir temel sağlar. Python dilinde yazılmıştır ve MongoDB veritabanı ile etkileşimde bulunmak için çeşitli modüller içerir.

## İçindekiler

- [Kurulum](#kurulum)
- [Kullanım](#kullanım)
- [Dosyalar](#dosyalar)
- [Katkıda Bulunanlar](#katkıda-bulunanlar)
- [Lisans](#lisans)

## Kurulum

1. Bu projeyi klonlayın:
   ```bash
   git clone https://github.com/bugra-university/cowa.git
   ```

2. Gerekli bağımlılıkları yükleyin:
   ```bash
   pip install -r requirements.txt
   ```

3. MongoDB veritabanınızı ayarlayın ve bağlantı bilgilerini `mongo_connect.py` dosyasında güncelleyin.

## Kullanım

Proje, MongoDB ile etkileşimde bulunmak için aşağıdaki modülleri içerir:

- **mongo_connect.py**: MongoDB veritabanına bağlantı sağlar.
- **mongo_create.py**: Veritabanında yeni belgeler oluşturur.
- **mongo_read.py**: Veritabanından belgeleri okur.
- **mongo_update.py**: Veritabanındaki belgeleri günceller.
- **mongo_delete.py**: Veritabanından belgeleri siler.

Her modül, belirli bir işlevi yerine getirmek için tasarlanmıştır. Kullanım örnekleri için ilgili dosyaların içeriğine göz atabilirsiniz.

## Dosyalar

- `mongo_connect.py`: MongoDB bağlantısı
- `mongo_create.py`: Yeni belge oluşturma
- `mongo_read.py`: Belge okuma
- `mongo_update.py`: Belge güncelleme
- `mongo_delete.py`: Belge silme
- `package.json`: Proje bağımlılıkları
- `package-lock.json`: Bağımlılık sürümleri

## Katkıda Bulunanlar

- Ramesh Dharavath

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için [LICENSE](LICENSE) dosyasına bakabilirsiniz.