import sys
import os
import tkinter
import turtle

def yazdır(mesaj):
    print(mesaj)
def giriş(mesajs):
    return input(mesajs)

if os.name == 'nt':  # Windows
    os.system(f'title Türkçe Python')
else:  # Linux/MacOS
    sys.stdout.write(f"\x1b]2;Türkçe Python\x07")

___name___ = "NecmeddinHD tarafından Türkçe Python"
___version___ = "Sürüm: 1.0.8 Latest Release"

print(___name___)
print(___version___)
print("Kullanılan Program: "+ sys.executable)
print()

# 42 Kelimelik bir Türkçe den Python a çeviri sözlüğü
ceviriler = {
    "fonksiyon": "def",
    "Doğru": "True",
    "Yanlış": "False",
    "geri_dön": "return",
    "eğer": "if",
    "değilse": "else",
    "döngü": "while",
    "gezin": "for",
    "içinde": "in",
    "aralığında": "range",
    "sınıf": "class",
    "yazı": "str",
    "tamsayı": "int",
    "ondalık": "float",
    "doğrumu": "bool",
    "demet": "tuple",
    "küme": "set",
    "sözlük": "dict",
    "aktar": "import",
    "doğrula": "assert",
    "ekle": "add",
    "çıkar": "remove",
    "sistem": "system",
    "çıkış": "exit",
    "aç": "open",
    "klasör": "dir",
    "veritabanı": "database",
    "veri": "data",
    "buPaketten": "from",
    "çalıştır": "exec",
    "çalış": "run",
    "uznuluğu": "len",
    "boş": "None",
    "çıktısı": "stdout",
    "hata_çıktısı": "stderr",
    "yaz": "write",
    "hiç": "any",
    "hepsi": "all",
    "devam_et": "continue",
    "eğde": "elif",
    "veya": "or",
    "dene": "try",
    "yerel": "local",
    "dinle": "listen",
    "writedır": "yazdır",
    "onaltılık": "hex",
    "ikilik": "bin",
    "sekizlik": "oct",
    "değerlendir": "eval",
    "temsil": "repr",
    "çağrılabilir": "callable",
    "özelliği_var_mı": "hasattr",
    "özelliği_al": "getattr",
    "özellik_ayarla": "setattr",
    "özellik_sil": "delattr",
    "karma": "hash",
    "süper": "super",
    "sonraki": "next",
    "birleştir": "zip",
    "tersi": "reversed",
    "dilimle": "slice",
    "biçimlendir": "format",
    "giriş_yapan": "getlogin",
    "kullanıcı_id": "getuid",
    "etkili_kullanıcı_id": "geteuid",
    "grup_id": "getgid",
    "etkili_grup_id": "getegid",
    "durum": "stat",
    "izin_ver": "chmod",
    "sahip_ayarla": "chown",
    "sistem_bilgisi": "uname",
    "yürü": "walk",
    "dosya_aç": "startfile",
    "argümanlar": "argv",
    "platform": "platform",
    "sürüm": "version",
    "modüller": "modules",
    "girdi": "stdin",
    "hata": "stderr",
    "oku": "read",
    "satır_oku": "readline",
    "satırları_oku": "readlines",
    "kapat": "close",
    "tür_mü": "isinstance",
    "alt_sınıf_mı": "issubclass"
}

hata_sozlugu = {
    "ArithmeticError": "Aritmetik Hatası",
    "AssertionError": "Hata",
    "AttributeError": "Özellik Hatası",
    "BaseException": "Temel İstisna",
    "BlockingIOError": "Engellenen G/Ç Hatası",
    "B rokenPipeError": "Kırık Boru Hatası",
    "BufferError": "Tampon Hatası",
    "ChildProcessError": "Alt Süreç Hatası",
    "ConnectionAbortedError": "Bağlantı Kesildi Hatası",
    "ConnectionError": "Bağlantı Hatası",
    "ConnectionRefusedError": "Bağlantı Reddedildi Hatası",
    "ConnectionResetError": "Bağlantı Sıfırlandı Hatası",
    "DeprecationWarning": "Kullanımdan Kaldırılma Uyarısı",
    "EOFError": "Dosya Sonu Hatası",
    "EnvironmentError": "Ortam Hatası",
    "Exception": "İstisna",
    "FileExistsError": "Dosya Zaten Var Hatası",
    "FileNotFoundError": "Dosya Bulunamadı Hatası",
    "FloatingPointError": "Kayan Nokta Hatası",
    "FutureWarning": "Gelecek Uyarısı",
    "GeneratorExit": "Üreteç Çıkışı",
    "ImportError": "İçe Aktarma Hatası",
    "ImportWarning": "İçe Aktarma Uyarısı",
    "IndentationError": "Girinti Hatası",
    "IndexError": "Geçersiz Hatası",
    "InterruptedError": "Kesinti Hatası",
    "IsADirectoryError": "Bir Dizin Hatası",
    "KeyError": "Bilinmeyen Anahtar Hatası",
    "KeyboardInterrupt": "Klavye Kesintisi",
    "LookupError": "Arama Hatası",
    "MemoryError": "Bellek Hatası",
    "ModuleNotFoundError": "Modül Bulunamadı Hatası",
    "NameError": "Bilinmeyen İsim Hatası",
    "NotADirectoryError": "Bu Bir Dizin Değil Hatası",
    "NotImplementedError": "Uygulanmamış Hata",
    "OSError": "İşletim Sistemi Hatası",
    "OverflowError": "Aşırı Yükleme Hatası",
    "PendingDeprecationWarning": "Bekleyen Kullanımdan Kaldırılma Uyarısı",
    "PermissionError": "Yetersiz İzin Hatası",
    "ProcessLookupError": "Süreç Arama Hatası",
    "RecursionError": "Özyineleme Hatası",
    "ReferenceError": "Referans Hatası",
    "ResourceWarning": "Kaynak Uyarısı",
    "RuntimeError": "Çalışma Zamanı Hatası",
    "RuntimeWarning": "Çalışma Zamanı Uyarısı",
    "StopAsyncIteration": "Asenkron İterasyon Durduruldu",
    "StopIteration": "İterasyon Durduruldu",
    "SyntaxError": "Sözdizimi Hatası",
    "SyntaxWarning": "Sözdizimi Uyarısı",
    "SystemError": "Sistem Hatası",
    "SystemExit": "Sistemden Çıkış",
    "TabError": "Sekme Hatası",
    "TimeoutError": "Zaman Aşımı Hatası",
    "TypeError": "Tür Hatası",
    "UnboundLocalError": "Bağlanmamış Yerel Değişken Hatası",
    "UnicodeDecodeError": "Unicode Çözme Hatası",
    "UnicodeEncodeError": "Unicode Kodlama Hatası",
    "UnicodeError": "Unicode Hatası",
    "UnicodeTranslateError": "Unicode Çeviri Hatası",
    "UserWarning": "Kullanıcı Uyarısı",
    "ValueError": "Değer Hatası",
    "Warning": "Uyarı",
    "ZeroDivisionError": "Sıfıra Bölme Hatası",
    "is not defined": "Tanımlanmadı",
    'can only concatenate str (not "int") to str': "Yazı Sadece Yazıyla Hesaplana Bilir Sayı ile değil",
    'list index out of range': "Verilen İndeks Listedeki indeksler dışında bir indeks",
    "invalid literal for int() with base 10:": "Harfleri Sayıya çeviremezsin: ",
    "division by zero": "Herhangi bir sayıyı sıfıra bölemezsin",
    "object has no attribute ": "objesinin böyle bir özelliği yok ",
    "[Errno 2] No such file or directory:": "Böyle bir klasör veya dosya yok: " ,
    "No module named": "Böyle Bir Modül veya Paket Yok Lütfen Bulunduğundan Emin Olun: "
}


def cevir_ve_calistir(turkce_kod):
    for turkce, python in ceviriler.items():
        turkce_kod = turkce_kod.replace(turkce, python)

    try:
        exec(turkce_kod, globals(), globals())  # Artık tek satır da çalışır, fonksiyon da
        print()
        print()
    except Exception as e:
        hata_tipi = type(e).__name__
        turkce_hata = hata_sozlugu.get(hata_tipi, "Bilinmeyen Hata")
        print(f"Türkçe Hata: {turkce_hata} -> {e}")

def kodu_oku_ve_calistir(dosya_adi):
    with open(dosya_adi, 'r', encoding='utf-8') as file:
        turkce_kod = file.read()
        print(f"{dosya_adi} dosyası okundu.\nKod çalıştırılıyor...\n")
        cevir_ve_calistir(turkce_kod)

if __name__ == "__main__":
    if len(sys.argv) == 2 and os.path.isfile(sys.argv[1]):
        kodu_oku_ve_calistir(sys.argv[1])
    else:
        if "ANDROID_STORAGE" in os.environ or "ANDROID_ROOT" in os.environ:
            # Android için kullanıcıdan yol al
            girilen = input("Lütfen .trpy dosyasının adını veya yolunu yazın: ")

        # Eğer sadece dosya adı girildiyse, Android'e göre varsayılan dizini ekle
            if not os.path.isabs(girilen):
                # Android'de Pydroid için varsayılan kullanıcı dizini
                girilen = "/storage/emulated/0/" + girilen

            if os.path.isfile(girilen):
                kodu_oku_ve_calistir(girilen)
            else:
                print("❌ Dosya bulunamadı:", girilen)
        else:
            girilen = input("Lütfen .trpy dosyasının adını veya yolunu yazın: ")
            if not os.path.isabs(girilen):
                # Android'de Pydroid için varsayılan kullanıcı dizini
                bulundugu_dizin = os.path.dirname(os.path.abspath(sys.argv[0]))
                girilen = os.path.join(bulundugu_dizin, girilen)
                kodu_oku_ve_calistir(girilen)
            else:
                print("❌ Dosya bulunamadı:", girilen)
                print("Kullanım: .trpy dosyasını trpy.exe üzerine sürükleyin.")

input("Çıkmak için ENTER tuşuna basınız")