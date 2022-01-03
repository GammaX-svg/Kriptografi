file_asli = "dekripsi.txt"
file_enkrip = "enkrip.txt"

Fin = open(file_enkrip, "r")
Fin_lines = Fin.read()

if(Fin == None):
    print(" Berkas " + file_enkrip + " tidak ditemukan... ")

else :
    Fout = open(file_asli, "w+")

    key = input(" Kata Kunci : ")
    key_array = [int(x) for x in str(key)]

    Fin_array = bytearray(Fin_lines, "utf8")

    i = 0
    for char in Fin_array:
        key_int = key_array[i]
        chipset = char ^ key_int

        Fout.write(chr(chipset))
        i = (i + 1) % len(key_array)

    Fin.close()
    Fout.close()
