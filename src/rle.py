def rle_encode(text):
    # Eğer metin boşsa boş string döndür
    if not text:
        return ""

    encoded = ""   # Sıkıştırılmış metni tutacak değişken
    count = 1      # Tekrar sayısını tutan sayaç

    # Metni ikinci karakterden başlayarak dolaş
    for i in range(1, len(text)):
        # Eğer mevcut karakter bir öncekiyle aynıysa sayaç artırılır
        if text[i] == text[i - 1]:
            count += 1
        else:
            encoded += str(count) + text[i - 1]
            count = 1    # Sayaça yine 1 değeri yazdırılır

    # Döngü bittikten sonra son karakter grubu eklenir
    encoded += str(count) + text[-1]
    return encoded


def rle_decode(encoded_text):
    decoded = ""    # Geri açılmış metni tutar
    count = ""      # Sayı karakterlerini tutmak için string

    # Sıkıştırılmış metni karakter karakter dolaş
    for char in encoded_text:
        if char.isdigit():
            count += char
        else:
            decoded += char * int(count)
            count = ""    # Sayı sıfırlanır

    return decoded


def compression_ratio(original, compressed):
    # Orijinal metin boşsa hata olmaması için 0 döndür
    if len(original) == 0:
        return 0.0
    # Sıkıştırma oranı formülü
    return ((len(original) - len(compressed)) / len(original)) * 100

text = input("Metin giriniz: ").strip()

# Encode
encoded = rle_encode(text)
# Decode
decoded = rle_decode(encoded)
ratio = compression_ratio(text, encoded)

print("\n------ SONUÇLAR ------")
print("Orijinal Metin           :", text)
print("Orijinal Uzunluk         :", len(text))
print("Sıkıştırılmış Metin      :", encoded)
print("Sıkıştırılmış Uzunluk    :", len(encoded))
print("Geri Açılmış Metin       :", decoded)

print("Sıkıştırma Oranı (%)     : {:.2f}".format(ratio))

if ratio <= 0:
    print("⚠️ Not: Bu veri için sıkıştırma sağlanamamıştır.")
