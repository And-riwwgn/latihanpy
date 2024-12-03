from time import sleep
import time
import sys

def print_lirik():
    lines = [
        ("Apa sudah ada kabar lain yang kau tunggu?", 0.10),
        ("Sudah adakah yang gantikanku?", 0.09),
        ("Yang khawatirkanmu setiap waktu", 0.07),
        ("Yang cerita tentang apapun sampai hal-hal tak perlu", 0.10),
    ]
    delays = [2, 2.3, 3.2, 1]

    for i, (text, char_delay) in enumerate(lines):
        for char in text:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lirik()
