import sounddevice as sd
import soundfile as sf

# Ses kaydı yapılacak dosyanın adını alın
dosya_adı = input("Kaydedilecek ses dosyasının adını girin (Dosya adının sonuna .wav yazınız.):  ")

# Kayıt ayarları
süre = int(input("Kaç saniye kayıt yapmak istersiniz? "))
örneklem_sıklığı = 45100

# Ses kaydını yap
print("Ses kaydı başlatılıyor...")
ses_kaydı = sd.rec(int(süre * örneklem_sıklığı), samplerate=örneklem_sıklığı, channels=2)
sd.wait()

# Ses kaydını belirlediğiniz dosyaya kaydet
sf.write(dosya_adı, ses_kaydı, örneklem_sıklığı)

print(f"Ses kaydı başarıyla kaydedildi: {dosya_adı}")

# Ses dosyasını okuyun
ses, örneklem_sıklığı = sf.read(dosya_adı)

# Ses dosyasını çal
print("Ses çalınıyor...")
sd.play(ses, örneklem_sıklığı)
sd.wait()

print("Ses çalma işlemi tamamlandı.")