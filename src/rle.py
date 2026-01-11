def rle_encode(text):
    if not text:
        return ""

    encoded = ""
    count = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            encoded += str(count) + text[i - 1]
            count = 1

    encoded += str(count) + text[-1]
    return encoded


def rle_decode(encoded_text):
    decoded = ""
    count = ""

    for char in encoded_text:
        if char.isdigit():
            count += char
        else:
            decoded += char * int(count)
            count = ""

    return decoded


def compression_ratio(original, compressed):
    if len(original) == 0:
        return 0.0

    return ((len(original) - len(compressed)) / len(original)) * 100


# -------- ANA PROGRAM --------
text = input("Metin giriniz: ").strip()

encoded = rle_encode(text)
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
