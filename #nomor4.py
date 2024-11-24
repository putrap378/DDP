#nomor4
print('------ Soal No 4 ------')

#Fungsi untuk menampilkan bilangan ganjil yang kurang argumens
def bilangan(n): #parameter
    ganjil = [str(i) for i in range(1, n, 2)] 
    print(",".join(ganjil))

bilangan(20)