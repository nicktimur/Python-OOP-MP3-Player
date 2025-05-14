# Python OOP MP3 Player 🎵

Bu proje, PyQt5 ve Pygame kullanılarak geliştirilmiş bir MP3 oynatıcıdır. Kullanıcı dostu bir arayüz ve çeşitli temalar ile şarkılarınızı kolayca dinleyebilirsiniz.

## Özellikler 🚀

- **MP3 Çalma**: Şarkıları oynatabilir, duraklatabilir, ileri/geri alabilirsiniz.
- **Tema Desteği**: Farklı temalar arasında geçiş yapabilirsiniz:
  - BlackBull
  - Default
  - Indian Rush
  - White Chocolate
  - Bleeding Rose
  - Turkey Edition
- **Şarkı Listesi**: Şarkılarınızı listeleyebilir ve çift tıklayarak oynatabilirsiniz.
- **Ses Kontrolü**: Ses seviyesini ayarlayabilirsiniz.
- **Zaman Çubuğu**: Şarkının çalma süresini ve kalan süresini görebilirsiniz.
- **Karıştırma Modu**: Şarkıları rastgele sırayla çalabilirsiniz.
- **Hakkımızda**: Geliştirici bilgilerini görüntüleyebilirsiniz.

## Kurulum 🛠️

1. Bu projeyi klonlayın:
    ```bash
    git clone https://github.com/nicktimur/Python-OOP-MP3-Player.git
    cd Python-OOP-MP3-Player
    ```

2. Gerekli bağımlılıkları yükleyin:
    ```bash
    pip install -r requirements.txt
    ```

3. Uygulamayı çalıştırın:
    ```bash
    python main.py
    ```

## Kullanım 📖

1. **Şarkı Ekleme**: `Şarkıları Ekle` butonuna tıklayarak bir klasör seçin. MP3 dosyaları otomatik olarak listeye eklenecektir.
2. **Şarkı Çalma**: Listeden bir şarkı seçin ve `▶` butonuna tıklayın.
3. **Tema Değiştirme**: Sağ taraftaki tema butonlarından birini seçerek temayı değiştirebilirsiniz.
4. **Ses Ayarı**: Ses kaydırıcısını kullanarak ses seviyesini ayarlayın.
5. **Zaman Çubuğu**: Çalma çubuğunu sürükleyerek şarkının belirli bir kısmına atlayabilirsiniz.

## Proje Yapısı 📂

- **`main.py`**: Uygulamanın giriş noktası.
- **`UI.py`**: PyQt5 ile oluşturulan kullanıcı arayüzü.
- **`Songs.py`**: Şarkıların yönetimi ve çalma işlemleri.
- **`Theme.py`**: Tema değişikliklerini yöneten sınıf.
- **`Workers.py`**: Arka planda çalışan iş parçacıkları.
- **`database.db`**: Şarkı yolları ve tema bilgilerini saklayan SQLite veritabanı.

## Gereksinimler 📋

- Python 3.10 veya üzeri
- PyQt5
- Pygame

## Geliştirici 👨‍💻

- **Timur Karakaş**  
  - Öğrenci Numarası: 20217170062  
  - [GitHub Profili](https://github.com/nicktimur)

## Lisans 📜

Bu proje MIT Lisansı ile lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına göz atabilirsiniz.

## Katkıda Bulunma 🤝

Katkıda bulunmak isterseniz, lütfen bir `pull request` gönderin veya bir `issue` açın. Her türlü katkı memnuniyetle karşılanır!