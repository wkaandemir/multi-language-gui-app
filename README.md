# multi-language-gui-app
 
Bu proje, çok dilli bir grafik kullanıcı arayüzü (GUI) uygulamasıdır. Python kullanılarak geliştirilmiş ve tkinter kütüphanesi ile oluşturulmuştur. Uygulama, İngilizce ve Türkçe dillerinde destek sunar.

## Özellikler

- Kullanıcıya hoş geldin mesajı
- Kullanıcının adını alarak kişiselleştirilmiş selamlama
- İngilizce ve Türkçe dil seçenekleri

## Kurulum

1. Proje dizinine gidin:
    ```bash
    cd multi-language-gui-app
    ```

2. Gerekli Python paketlerini yükleyin:
    ```bash
    pip install polib
    ```
3. `messages.po` dosyalarını ekleyin:
    - locale/en/LC_MESSAGES/messages.po
    ```bash
    msgid ""
    msgstr ""
    "Content-Type: text/plain; charset=UTF-8\n"

    msgid "Sample Application"
    msgstr "Sample Application"

    msgid "Hello, world!"
    msgstr "Hello, world!"

    msgid "Please enter your name:"
    msgstr "Please enter your name:"

    msgid "Greet"
    msgstr "Greet"

    msgid "Hello, {}!"
    msgstr "Hello, {}!"
    ```

    - locale/tr/LC_MESSAGES/messages.po
    ```bash
    msgid ""
    msgstr ""
    "Content-Type: text/plain; charset=UTF-8\n"

    msgid "Sample Application"
    msgstr "Örnek Uygulama"

    msgid "Hello, world!"
    msgstr "Merhaba, dünya!"

    msgid "Please enter your name:"
    msgstr "Lütfen adınızı girin:"

    msgid "Greet"
    msgstr "Selamla"

    msgid "Hello, {}!"
    msgstr "Merhaba, {}!"
    ```
4. `compile_po_to_mo.py` dosyasını çalıştırarak `messages.po` Dosyalarını `messages.mo` Dosyalarına Derleyin:
    ```bash
    python compile_po_to_mo.py
    ```
5. `app.py` dosyasını çalıştırarak uygulamayı başlatın:
    ```bash
    python app.py
    ```

## Katkıda Bulunma

Katkıda bulunmak istiyorsanız, lütfen bir çekme isteği gönderin. Büyük değişikliklerden önce lütfen değişikliklerinizi tartışmak için bir konu açın.

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Daha fazla bilgi için [LICENSE](LICENSE) dosyasına bakın.
