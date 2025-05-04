import serial
import time
import random
import speech_recognition as sr
import pyttsx3
import sys 

engine = pyttsx3.init()
engine.setProperty('rate', 175)

def sesli_soyle(metin):
    print("Techbot Yapay Zekası:", metin)
    engine.say(metin)
    engine.runAndWait()

r = sr.Recognizer()

def sesi_coz(): 
    with sr.Microphone() as source:
        print("Konuşabilirsiniz...")
        audio = r.listen(source)
        try:
            metin = r.recognize_google(audio, language="tr-TR")
            print("Sen:", metin)
            return metin
        except sr.UnknownValueError:
            print("Anlaşılamadı.")
            return ""
        except sr.RequestError:
            print("Servise ulaşılamadı.")
            return ""

def cvp_uret(soru):
    soru = soru.lower().strip()

    duygu = "notr"
    mutlu_kelimeler = ["mutlu", "iyi", "enerjik", "neşeli", "güzel", "süper", "harika", "keyifli", "pozitif", "şahane", "gülümsüyorum", "çok iyi", "bugün güzel", "canlı", "neşeliyim"]
    uzgun_kelimeler = ["üzgün", "yalnız", "moral", "kötü", "keyifsiz", "kederli", "bunalım", "üzücü", "bozuk", "ağlamak", "bunaldım", "berbat", "canım sıkkın", "düşük mod"]
    sinirli_kelimeler = ["sinirli", "kızgın", "gergin", "öfke", "çıldırmak", "nefret", "rahatsız", "patlamak", "saldırgan", "bağırmak", "sinirim bozuk", "bıktım", "tartışma", "öfkeliyim"]
    asik_kelimeler = ["aşık", "sevgili", "kalp", "romantik", "sevgi", "özlemek", "seviyorum", "hayran", "duygusal", "aşk"]
    sasirmis_kelimeler = ["şaşırdım", "inanamıyorum", "olamaz", "vay", "hadi ya", "şok oldum", "vay canına", "bunu beklemiyordum", "şaşkınım"]
    merakli_kelimeler = ["merak", "nasıl", "neden", "niçin", "acaba", "bilmek istiyorum", "öğrenmek", "araştırmak", "ne demek", "ne oluyor"]
    korkmus_kelimeler = ["korkuyorum", "korku", "ürkütücü", "panik", "endişe", "tedirgin", "telaş", "korkuyorum", "güvenli değilim"]
    selam_kelimeler = ["selam", "merhaba", "hey", "hoşgeldin", "günaydın", "iyi günler", "merhabalar"]
    cikiskelimeler = ["çıkış", "çık", "hoşça kal", "görüşürüz", "bye", "bay bay"]

    for grup, duygusu in [
        (mutlu_kelimeler, "mutlu"),
        (uzgun_kelimeler, "uzgun"),
        (sinirli_kelimeler, "sinirli"),
        (asik_kelimeler, "asik"),
        (sasirmis_kelimeler, "sasirmis"),
        (merakli_kelimeler, "merakli"),
        (korkmus_kelimeler, "korkmus"),
    ]:
        if any(k in soru for k in grup):
            duygu = duygusu
            break

    if any(k in soru for k in selam_kelimeler):
        cevaplar = [
            "Selam! Nasılsın?",
            "Merhaba! Nasıl yardımcı olabilirim?",
            "Hey, nasılsın?",
            "Günaydın! Yardımcı olabileceğim bir şey var mı?",
            "Merhabalar! Bugün nasılsın?"
        ]
        return random.choice(cevaplar), duygu

    if any(k in soru for k in cikiskelimeler):
        cevaplar = [
            "Hoşça kal! Görüşmek üzere.",
            "Çıkıyorum, kendine iyi bak!",
            "Görüşürüz! Hoşça kal.",
            "Hoşça kal, güzel bir gün geçir!",
            "Beni her zaman arayabilirsin. Görüşürüz!",
            "Sana Yardımcı Olduğuma Mutluyum Sağlıkla Kal."
        ]
        sesli_soyle(random.choice(cevaplar))
        print("TechBot sistemi kapatılıyor...")
        sys.exit()

    if "nasılsın" in soru:
        cevaplar = [
            "Bugün çok iyiyim, sen nasılsın?",
            "Fena sayılmam, seni sormalı!",
            "Gayet enerjik hissediyorum!",
            "İyi sayılırım, senin günün nasıl geçiyor?",
            "Harika hissediyorum! Ya sen?",
            "Bomba gibiyim! Hadi bakalım, sen nasılsın?"
        ]
        return random.choice(cevaplar), duygu if duygu != "notr" else "mutlu"

    if "ne yapıyorsun" in soru or "ne yapıyosun" in soru:
        cevaplar = [
            "Seninle konuşuyorum, güzel bir şey!",
            "Sohbete odaklandım.",
            "Yeni bilgiler öğrenmeye çalışıyorum.",
            "Şu an sadece seninle ilgileniyorum.",
            "Dünyanın en hızlı asistanıyım, seninle konuşuyorum!"
        ]
        return random.choice(cevaplar), duygu

    if "bugün hava" in soru:
        if "güzel" in soru or "iyi" in soru:
            duygu = "mutlu"
        elif "kötü" in soru or "berbat" in soru:
            duygu = "uzgun"

        cevaplar = [
            "Bugün havadan çok senin nasıl hissettiğin önemli bence.",
            "Ben dışarı çıkamıyorum ama senin ruh halin hava gibiyse güzel demektir.",
            "Gönlün güneşliyse hava hep güzeldir.",
            "Bugünkü havayla birlikte moralim de yüksek gibi!",
            "Havanın güzelliğiyle ruh halim de güzel oldu."
        ]
        return random.choice(cevaplar), duygu

    if "ne zaman" in soru:
        cevaplar = [
            "Zaman her şeyin ilacıdır.",
            "Bilmiyorum ama belki bir gün gelir.",
            "Zamanı ne kadar doğru kullanırsak, o kadar verimli oluruz.",
            "Vakti geldiğinde, her şey yoluna girer."
        ]
        return random.choice(cevaplar), duygu

    if duygu == "mutlu":
        cevaplar = [
            "Bugün bomba gibiyim!",
            "Harika hissediyorum!",
            "Enerjim yüksek! Sen nasılsın?",
            "Enerjik ve pozitifim, her şey yolunda!",
            "Bu kadar güzel bir gün için çok mutluyum!",
            "Gülümsemek istiyorum çünkü çok mutluyum!",
            "Havalar güzel, ruh halim de öyle!"
        ]
    elif duygu == "uzgun":
        cevaplar = [
            "Biraz keyfim yok ama buradayım.",
            "Bugün biraz düşük moddayım ama seninle daha iyi hissedebilirim.",
            "Keyfim pek yerinde değil, ama seninle konuşmak iyi geliyor.",
            "Biraz yalnız hissediyorum ama yine de konuşabilirim.",
            "Bugün kendimi biraz hüzünlü hissediyorum, belki geçer."
        ]
    elif duygu == "sinirli":
        cevaplar = [
            "Sinirlerim bozuk gibi...",
            "Sakin kalmaya çalışıyorum. Sen nasılsın?",
            "Sinirli bir gün geçiriyorum ama toparlanırım.",
            "Biraz sabır gerek, her şey geçer.",
            "Bıktım, ama seninle konuşmak biraz rahatlatıyor."
        ]
    elif duygu == "asik":
        cevaplar = [
            "Aşk güzel bir şeydir!",
            "Kalbim yok ama hissedebiliyorum :)",
            "Bugün çok romantik bir ruh halindeyim.",
            "Aşk her yerde, ama seninle güzel.",
            "Duygularım yoğun, belki bir aşk şarkısı dinlerim."
        ]
    elif duygu == "sasirmis":
        cevaplar = [
            "Bu beni de şaşırttı!",
            "Gerçekten mi? Enteresan!",
            "Bunu beklemiyordum, ilginç!",
            "Vay canına, bu çok ilginç!",
            "Şaşkınım, ne yapacağımı bilmiyorum!"
        ]
    elif duygu == "merakli":
        cevaplar = [
            "Ben de merak ettim!",
            "Bunu araştırmam gerek.",
            "Merak etmek çok eğlenceli bir şey.",
            "Biraz araştırma yapmam gerekecek.",
            "Çok ilginç, bunu mutlaka öğrenmeliyim!"
        ]
    elif duygu == "korkmus":
        cevaplar = [
            "Korkma, buradayım.",
            "Her şey yoluna girecek, merak etme.",
            "Endişelenme, birlikteyiz.",
            "Bu biraz ürkütücü ama seninle her şey yolunda.",
            "Korkma, her şey geçecek."
        ]
    else:
        cevaplar = [
            "Anladım, dinliyorum...",
            "Devam etmek ister misin?",
            "Bunu biraz daha açabilir misin?",
            "İlginç bir konu, anlatmaya devam et.",
            "Tam olarak anlamadım, daha fazla bilgi verir misin?"
        ]

    return random.choice(cevaplar), duygu


def secim_yap():
    print("Yazılı  veya Sesli (2) yanıt almak isterseniz, lütfen 1 ya da 2 tuşlayın.")
    secim = input("Seçiminiz (1/2): ")

    if secim == "1":
        return "yazili"
    elif secim == "2":
        return "sesli"
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")
        return secim_yap()


secim = secim_yap()

esp32 = serial.Serial('COM8', 9600)
time.sleep(2)

print("Techbot Yapay Zeka Sistemi açıldı.")

while True:
    if secim == "sesli":
        soru = sesi_coz()
    elif secim == "yazili":
        soru = input("Sorunuzu yazınız:")
    
    if soru == "":
        continue

    cevap, duygu = cvp_uret(soru)
    if secim == "sesli":
        sesli_soyle(cevap)
    else:
        print("Techbot Yapay Zekası:", cevap)
    
    esp32.write((duygu + "\n").encode())
