import json
import pandas as pd
import os

class Node:
    def __init__(self, info):
        self.info = info
        self.next = None

class LinkedList:
    def __init__(self):
        self.awal = None
    def isEmpty(self):
        return self.awal == None
    def addFirst(self, data):
        newNode = Node(data)
        newNode.next = self.awal
        self.awal = newNode
    def get(self, index):
        if self.isEmpty() or index<1 or index>self.size():
            return None
        else:
            bantu = self.awal
            posisi = 1
            while posisi < index :
                bantu = bantu.next
                posisi = posisi + 1
            return bantu
    def getFirst(self):
        return self.awal
    def size(self):
        if self.isEmpty():
            banyakNode = 0
        else:
            bantu = self.awal
            banyakNode = 1
            while bantu.next is not None:
                banyakNode = banyakNode + 1
                bantu = bantu.next
        return banyakNode
    def getLast(self):
        if self.isEmpty():
            return None
        else:
            bantu = self.awal
            while bantu.next is not None:
                bantu = bantu.next
            return bantu
    def addData(self, data):
        if self.isEmpty():
            self.addFirst(data)
        else:
            newNode = Node(data)
            last = self.getLast()
            last.next = newNode
        print("\n Data Berhasil Ditambahkan \n")
    def removeFirst(self):
        if self.isEmpty():
            print("Penghapusan gagal karena data kosong")
        else:
            first = self.getFirst()
            self.awal = self.awal.next 
            del first
    def remove(self, index):
        if self.isEmpty():
            print("Penghapusan gagal karena data kosong")
        elif index+1 ==1:
            self.removeFirst()
            print("\nData Berhasil Dihapus")
        else:
            prevNode = self.get(index)
            if prevNode is None:
                print("Data yang akan dihapus tidak ditemukan")
            else:
                removedNode = prevNode.next
                prevNode.next = removedNode.next
                del removedNode
                print("\nData Berhasil Dihapus")
    def sendJson(self):
        if self.isEmpty():
            return "Belum ada data"
        else:
            bantu = self.awal
            datajs = []
            while bantu is not None:
                datajs.append(bantu.info)
                bantu = bantu.next
                
            return datajs
    def update(self, index):
        nodeUpdate = self.get(index+1)
        if nodeUpdate is None:
            print("Data yang akan diedit tidak ditemukan")
        else:
            nodeUpdate.info = {
                'Nama': input("Masukan Nama                   : "),
                'No HP': input("Masukan Pilihan No HP          : "),
                'No HP Ortu': input("Masukan Pilihan No HP Orangtua : "),
                'Lama Kost (Bulan)': int(input("Berapa Bulan                   : ")),
                'Daerah Asal': (input("Daerah Asal                    : "))
            }
            print("\nData Berhasil Diedit")

data = LinkedList()

# Mengkonversi Data Json ke LinkedList

if os.path.exists('datakost.json'):
    with open('datakost.json', 'r') as f:
        dataKost = json.load(f)

    for i in dataKost:
        data.addData(i)

# Main Menu

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def mainMenu():
    clear()
    print("=====================================")
    print("=             Menu Utama            =")
    print("=      Data Anak Kost Pak Budi      =")
    print("=====================================")
    print("\n")
    print("1. Tambah Data Anak Kost Baru")
    print("2. Edit Data Anak Kost")
    print("3. Hapus Data Anak Kost")
    print("4. Tampilkan Semua Data Anak Kost")
    print("5. Credit Program")
    print("0. Exit")
    print("\n")
    pilih = int(input("Pilih Menu : "))
    return pilih

def tambahData():
        clear()
        print("=====================================")
        print("=            Tambah Data            =")
        print("=      Data Anak Kost Pak Budi      =")
        print("=====================================")
        print("\n")
        berapaData = int(input("Berapa Data yang akan Ditambah ? "))
        print("")
        while berapaData:
            data.addData(
            {
                'Nama': input("Masukan Nama                   : "),
                'No HP': input("Masukan Pilihan No HP          : "),
                'No HP Ortu': input("Masukan Pilihan No HP Orangtua : "),
                'Lama Kost (Bulan)': int(input("Berapa Bulan                   : ")),
                'Daerah Asal': (input("Daerah Asal                    : "))
            })
            berapaData -= 1
        print("\n")
        input("Tekan Enter Untuk Kembali ke Menu Utama")
        clear()

def tampilkanData():
    if data.isEmpty():
        return print("Data Kosong")
    else:
        with open('datakost.json', 'r') as f:
            dataKost = json.load(f)
            dataKost = pd.DataFrame(dataKost)
        return print(dataKost)

def editData():
    clear()
    print("=====================================")
    print("=                Edit               =")
    print("=      Data Anak Kost Pak Budi      =")
    print("=====================================")
    print("\n")
    tampilkanData()
    print("\n")
    index = int(input("Data Index Keberapa yang akan diedit ? "))
    print("\n")
    data.update(index)
    print("\n")
    input("Tekan Enter Untuk Kembali ke Menu Utama")
    clear()

def hapusData():
    clear()
    print("=====================================")
    print("=               Hapus               =")
    print("=      Data Anak Kost Pak Budi      =")
    print("=====================================")
    print("\n")
    tampilkanData()
    print("\n")
    index = int(input("Data Index Keberapa yang akan diedit ? "))
    data.remove(index)
    print("\n")
    input("Tekan Enter Untuk Kembali ke Menu Utama")
    clear()

def creditProgram():
    clear()
    print("=====================================")
    print("=           Credit Program          =")
    print("=      Data Anak Kost Pak Budi      =")
    print("=====================================")
    print("\n")
    print("Nama  : Fajar Wahyu Gumelar")
    print("Kelas : IF-6")
    print("NIM   : 10121242")
    print("\n")
    print("Referensi : ")
    print("1. LinkedList Andri Heryandi, M.T. ")
    print("2. https://www.programiz.com/python-programming/json")
    print("3. https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html")
    print("4. https://stackoverflow.com/questions/2084508/clear-terminal-in-python")
    print("5. https://careerkarma.com/blog/python-check-if-file-exists/")
    print("\n")

    input("Tekan Enter Untuk Kembali ke Menu Utama")
    clear()

while True:

    # Convert Linkedlist To Json
    with open('datakost.json', 'w') as json_file:
        json.dump(data.sendJson(), json_file, indent=4)

    pilih = mainMenu()

    if pilih == 1:
        tambahData()
    elif pilih == 2:
        editData()
    elif pilih == 3:
        hapusData()
    elif pilih == 4:
        clear()
        print("=====================================")
        print("=          Tampilan Tabel           =")
        print("=      Data Anak Kost Pak Budi      =")
        print("=====================================")
        print("\n")
        tampilkanData()
        print("\n")
        input("Tekan Enter Untuk Kembali ke Menu Utama")
        clear()
    elif pilih == 5:
        creditProgram()
    elif pilih == 0:
        break
    else:
        print("Salah memilih angka !")




