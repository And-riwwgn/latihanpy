import random

x = 'y'
print("uji kehokianmu")
print("Menang jika mendapatkan 0 nenbentuk garis lurus")
print("\n")
while x== "y" :
    tidak = random.randint (1,7)

    if tidak ==1:
        print("[------]")
        print("[      ]")
        print("[   0  ]")
        print("[      ]")
        print("[------]")
        print("Kasian ga hoki")
    if tidak ==2:
        print("[------]")
        print("[0     ]")
        print("[      ]")
        print("[    0 ]")
        print("[------]")
        print("Kasian ga hoki")
    if tidak ==3:
        print("[------]")
        print("[0     ]")
        print("[  0   ]")
        print("[    0 ]")
        print("[------]")
        print("CUMA KEBETULAN AJA NI")
    if tidak ==4:
        print("[------]")
        print("[      ]")
        print("[0 0 0 ]")
        print("[      ]")
        print("[------]")
        print("HOKI SETAHUN KEPAKE")
    if tidak ==5:
        print("[------]")
        print("[      ]")
        print("[      ]")
        print("[      ]")
        print("[------]")
        print("KAMU SIAL BANGET BRO")
    if tidak ==6:
        print("[------]")
        print("[   0  ]")
        print("[   0  ]")
        print("[   0  ]")
        print("[------]")
        print("SELAMAT ANDA MENANG")
    if tidak ==7:
        print("[------]")
        print("[     0]")
        print("[      ]")
        print("[ 0   0]")
        print("[------]")
        print("Kasian ga hoki")

    x = input("Klik y untuk mengulang dan n untuk keluar : ")
    print("\n")