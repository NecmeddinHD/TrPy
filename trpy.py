import sys
import os

if os.name == 'nt':  # Windows
    os.system(f'title Türkçe Python')
else:  # Linux/MacOS
    sys.stdout.write(f"\x1b]2;Türkçe Python\x07")

___name___ = " NecmeddinHD tarafından Türkçe Python"
___version___ = "1.0.5"

print(___name___)
print(___version___)
print()

ceviriler = {
    "fonksiyon": "def",
    "geri_dön": "return",
    "eğer": "if",
    "değilse": "else",
    "döngü": "while",
    "için": "for",
    "aralığında": "range",
    "yazdır": "print",
    "giriş": "input",
}

def cevir_ve_calistir(turkce_kod):
    for turkce, python in ceviriler.items():
        turkce_kod = turkce_kod.replace(turkce, python)

    try:
        exec(turkce_kod, globals())  # Artık tek satır da çalışır, fonksiyon da
        print()
        print()
    except Exception as e:
        print()
        print()
        print(f"Bir hata oluştu: {e}")

def kodu_oku_ve_calistir(dosya_adi):
    with open(dosya_adi, 'r', encoding='utf-8') as file:
        turkce_kod = file.read()
        print(f"{dosya_adi} dosyası okundu.\nKod çalıştırılıyor...\n")
        cevir_ve_calistir(turkce_kod)

if __name__ == "__main__":
    if len(sys.argv) == 2 and os.path.isfile(sys.argv[1]):
        kodu_oku_ve_calistir(sys.argv[1])
    else:
        print("Kullanım: .trpy dosyasını trpy.exe üzerine sürükleyin.")

input("Çıkmak için ENTER tuşuna basınız")