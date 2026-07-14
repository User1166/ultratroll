import sys
import pyautogui
import random
import time
import os
import threading
from pynput import keyboard
import pygame
import ctypes
# Failsafe'i devre dışı bırak
pyautogui.FAILSAFE = False

# Global değişkenler
stop_program = False  # Programı durdurmak için bayrak

#Rastgele kelimeler
def show_ctypes_error():
    messages = [
        "Kritik Sistem Hatası! Bilgisayarınız yeniden başlatılmalı.",
        "Disk yazma hatası oluştu. Lütfen kontrol edin.",
        "Yetersiz Bellek! Uygulamalarınız yanıt vermiyor.",
        "Dosya sistemi bozulmuş olabilir!",
        "Güvenlik Uyarısı: Yetkisiz erişim tespit edildi!",
        "CPU aşırı ısınma tespit edildi!",
        "RAM kontrol hatası: Bellek arızası olabilir.",
        "Bilinmeyen bir program sistem kaynaklarını tüketiyor!",
        "Ağ bağlantısı kesildi! IP çakışması tespit edildi.",
        "Sürücü hatası: Donanım uyumsuzluğu algılandı.",
        "Windows Lisans Doğrulaması Başarısız!",
        "Fatal Error: Kernel Panic Detected!",
        "Boot Sector Corrupt! Sistemi kapatmanız gerekiyor.",
        "Antivirüs yazılımınız devre dışı bırakıldı!",
        "Güç dalgalanması tespit edildi! Donanım zarar görebilir.",
        "Bilinmeyen aygıt algılandı! Sürücü yüklenemedi.",
        "Kritik Güncelleme Başarısız! Sistem kararsız hale geldi.",
        "Kullanıcı Profili Yüklenemedi. Devam etmek için çıkış yapın.",
        "Veri Yolu Hatası: Bellek modülleri yanlış takılmış olabilir.",
        "Bilinmeyen Uygulama Çökmesi Algılandı!",
        "Sistem Başlatılamıyor: Eksik dosya tespit edildi.",
        "Yazılım çakışması algılandı! Kapatılması gerekiyor.",
        "Bilgisayarınız kilitlendi! Şifreleme anahtarları kayboldu.",
        "USB Aygıtı Tanınmadı. Donanımı kontrol edin.",
        "Mavi Ekran: SYSTEM_THREAD_EXCEPTION_NOT_HANDLED",
        "Cihazınız güvenlik tehditlerine maruz kaldı!",
        "Bellek Yetersiz! Kritik işlemler kapatılacak.",
        "Ağ güvenlik duvarı devre dışı bırakıldı!",
        "BIOS Güncellemesi Başarısız! Sistem açılmayabilir.",
        "Sistem Kendi Kendine Onarım Modunda Başlatıldı!",
        "Windows Update tamamlanamadı, sistem dengesiz hale gelebilir.",
        "Sistem ısınma seviyeleri kritik! Lütfen cihazı kapatın.",
        "Dosya Şifreleme Tamamlanamadı! Lütfen tekrar deneyin.",
        "Veritabanı Bağlantısı Kesildi! Yeniden bağlanılıyor...",
        "Bellek testi başarısız oldu! Arızalı RAM algılandı.",
        "Ağ Güvenliği İhlali! Yetkisiz erişim algılandı.",
        "Cihaz Yöneticisi: Aygıt başlatılamadı (Kod 43)",
        "Donanım arızası tespit edildi! Yedekleme önerilir."
    ]
    while not stop_program:
        time_to_wait = random.uniform(15, 30)
        time.sleep(time_to_wait)
        message = random.choice(messages)
        ctypes.windll.user32.MessageBoxW(0, message, "Sistem Hatası", 0x10)





def random_words():
    messages = ["Hello there!", "General Kenobi!", "Bazinga!", 
        "Never gonna give you up...", "Bruh", "What the dog doin'?", 
        "Amogus!", "Error 404: Brain not found.", "Why u bully me?", 
        "Insert coin to continue...", "Fatal Error: User not found.",
        "Keyboard not detected. Press any key to continue.",
        "I'm watching you...", "Critical System Failure!", 
        "Congratulations! You played yourself.", "A wild error appeared!"]
    while not stop_program:
        time_to_wait = random.uniform(10, 25)
        time.sleep(time_to_wait)
        random_message = random.choice(messages)
        pyautogui.typewrite(random_message, interval=0.1)
        pyautogui.press("enter")

# Rastgele ses çalma işlemi
def random_sound():
    pygame.mixer.init()
    sounds = [
        "aaa.mp3", "wth.mp3", "amogus.mp3", "boom.mp3", "flash.mp3",
        "bruh.mp3", "bye.mp3", "emotional.mp3", "error.mp3", "fen.mp3",
        "gtasa.mp3", "mario.mp3", "pipe.mp3", "au.mp3", "rizz.mp3",
        "spi.mp3", "what.mp3","eos.mp3","alsana","muhaha.mp3","lingangu.mp3",
        "orhann.mp3","wp.mp3","yok.mp3","alarm.mp3"
    ]  
    while not stop_program:
        time_to_wait = random.uniform(15, 30)
        time.sleep(time_to_wait)
        if stop_program:
            break
        selected_sound = random.choice(sounds)
        sound_path = os.path.join("sounds", selected_sound)
        try:
            pygame.mixer.music.load(sound_path)
            pygame.mixer.music.play()
            print(f"Çalınıyor: {selected_sound}")
            while pygame.mixer.music.get_busy():
                if stop_program:
                    pygame.mixer.music.stop()
                    break
                time.sleep(0.1)
        except pygame.error as e:
            print(f"Ses dosyası yüklenemedi: {e}")
    print("Ses çalma işlemi durduruldu.")

# Rastgele fare hareketi
def random_mouse_move():
    while not stop_program:
        time_to_wait = random.uniform(2, 8)
        time.sleep(time_to_wait)
        screen_width, screen_height = pyautogui.size()
        x = random.randint(0, screen_width - 1)
        y = random.randint(0, screen_height - 1)
        pyautogui.moveTo(x, y)

# Rastgele uygulama açma
def random_open_application():
    while not stop_program:
        time_to_wait = random.uniform(5, 20)
        time.sleep(time_to_wait)
        apps = ["notepad", "calc", "mspaint", "write", "cmd"]
        app = random.choice(apps)
        os.system(app)

# Bilgisayar kapatma işlemi
def shutdown_computer():
    print("Bilgisayar 5 dakika içinde kapanacak...")
    os.system('shutdown /s /f /t 300')

# Alt + Tab tuşu simülasyonu
def alt_tab_switch():
    while not stop_program:
        time_to_wait = random.uniform(8, 15)
        time.sleep(time_to_wait)
        pyautogui.hotkey('alt', 'tab')

# Windows+D tuşu simülasyonu
def press_windows_d():
    while not stop_program:
        time_to_wait = random.uniform(15, 20)
        time.sleep(time_to_wait)
        pyautogui.hotkey('win', 'd')

# F6 tuşuna basıldığında programı durdurma
def on_press(key):
    global stop_program
    try:
        if key == keyboard.Key.f6:
            stop_program = True
            cancel_shutdown()
            print("Program durduruldu.")
            pygame.mixer.music.stop()
            return False
    except AttributeError:
        pass

# Bilgisayar kapanmasını iptal etme
def cancel_shutdown():
    print("Bilgisayar kapatma iptal edildi.")
    os.system('shutdown -a')

# Ana işlem
if __name__ == "__main__":
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    threading.Thread(target=random_mouse_move, daemon=True).start()
    threading.Thread(target=random_open_application, daemon=True).start()
    threading.Thread(target=random_sound, daemon=True).start()
    threading.Thread(target=alt_tab_switch, daemon=True).start()
    threading.Thread(target=press_windows_d, daemon=True).start()
    threading.Thread(target=random_words, daemon=True).start()
    threading.Thread(target=show_ctypes_error, daemon=True).start()

    listener.join()
