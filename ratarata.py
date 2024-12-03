numlist = list()

while True:
    inp = input('masukkan nilai :')
    if inp =='selesai' : break
    hasil = float(inp)
    numlist.append(hasil)

    rata = sum(numlist) / len(numlist)
    print('rata-rata : ', rata)

    # eror