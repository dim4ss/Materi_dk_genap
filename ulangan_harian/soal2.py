#program menghitung jumlah banyak bilangan ganjil dari 1-100
for i in range(0,100,2):
    if i % 2==1:
        print(f"{i}adalah bilangan ganjil {i//2+1}")