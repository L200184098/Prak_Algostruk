#Latihan
def swap(A,p,q) :
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp

K = [50,20,70,30]
print(K)
print("swap!")
swap(K,1,3)
print(K)
print()
    
def cariPosisiYangTerkecil(A, dariSini, sampaiSini) :
    posisiYangTerkecil = dariSini
    for i in range(dariSini+1, sampaiSini):
        if A[i] < A[posisiYangTerkecil] :
            posisiYangTerkecil = i
    return posisiYangTerkecil

A = [18,13,44,25,66,107,78,89]
print(A)
print("posisi terkecil nya")
k = cariPosisiYangTerkecil(A,2,len(A))
print(k)

def bubbleSort(A) :
    n = len(A)
    for i in range(n-1) :
        for j in range(n-i-1):
            if A[j] > A[j+1] :
                swap(A,j,j+1)

def selectionSort(A) :
    n = len(A)
    for i in range(n-1) :
        indexKecil = cariPosisiYangTerkecil(A, i, n)
        if indexKecil != i :
            swap(A, i, indexKecil)

def insertionSort(A) :
    n = len(A)
    for i in range(1,n) :
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos - 1] :
            A[pos] = A[pos-1]
            pos = pos - 1
        A[pos] = nilai



class MhsTIF(object):
    def __init__(self, nama, NIM, alamat,us):
        self.nama = nama
        self.NIM = NIM
        self.alamat = alamat
        self.us = us

    def __str__(self):
        s = self.nama + "NIM" + str(self.NIM)\
            + ". Menetap di " + self.alamat\
            + ". Uang Saku Rp. " + str(self.us)\
            + " Setiap Minggu."
        
def swap(A,p,q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp
    
#Nomor1    
List = [MhsTIF('Sufyan', "L200184098", 'Sragen', 400000),
          MhsTIF('Alip', "L200180215", 'Surakarta', 500000),
          MhsTIF('Aldy', "L200180175", 'Sukoharjo', 600000),
          MhsTIF('Naura', "L200180207", 'Caruban', 700000),
          MhsTIF('Damping', "L200180213", 'Karanganyar', 100000),
          MhsTIF('Kevin', "L200184033", 'Purworejo', 110000),
          MhsTIF('Fakhar', "L200180183", 'Batam', 750000),
          MhsTIF('Herlangga', "L200180186", 'Karanganyar', 83000),
          MhsTIF('Bintang', "L200180193", 'Surakarta', 780000),
          MhsTIF('Vio', "L200180173", 'Klaten', 650000)]

def cekNIM(object):
    for i in object:
        print (i.NIM)
         
          
def urutNIM(object):
    n = len(object)
    for i in range(n-1):
        for j in range(n-i-1):
            if object[j].NIM > object[j+1].NIM:
                swap(object,j,j+1)

#Nomer2
list1 = [1,6,7,8,10]
list2 = [2,3,4,5,9]

def combine(A, B):
    la = len(A)
    lb = len(B)
    c = list()
    i = 0
    j = 0
    while i < la and j < lb:
        if A[i] < B[j]:
            c.append(A[i])
            i += 1
        else:
            c.append(B[j])
            j += 1
    while i < la:
        c.append(A[i])
        i += 1
    while j < lb:
        c.append(B[j])
        j += 1
    return c

def swap(A,p,q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp

def cariPosisiYangTerkecil(A, dariSini, sampaiSini):
    posisiTerkecil = dariSini
    for i in range(dariSini+1, sampaiSini):
        if A[1] < A[posisiTerkecil]:
            posisiTerkecil = 1
    return posisiTerkecil

def bubbleSort(A):
    n = len(A)
    for i in range(n-1):
        for j in range(n-i-1):
            if A[j] > A[j+1]:
                swap(A,j,j+1)

def selectionSort(A):
    n = len(A)
    for i in range(n-1):
        indexKecil = cariPosisiYangTerkecil(A, i, n)
        if indexKecil != i:
            swap(A, i, indexKecil)

def insertionSort(A):
    n = len(A)
    for i in range(1,n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos-1]:
            A[pos] = A[pos-1]
            pos = pos-1
        A[pos] = nilai
        
def swap(A,p,q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp

def cariPosisiYangTerkecil(A, dariSini, sampaiSini):
    posisiTerkecil = dariSini
    for i in range(dariSini+1, sampaiSini):
        if A[1] < A[posisiTerkecil]:
            posisiTerkecil = 1
    return posisiTerkecil

def bubbleSort(A):
    n = len(A)
    for i in range(n-1):
        for j in range(n-i-1):
            if A[j] > A[j+1]:
                swap(A,j,j+1)

def selectionSort(A):
    n = len(A)
    for i in range(n-1):
        indexKecil = cariPosisiYangTerkecil(A, i, n)
        if indexKecil != i:
            swap(A, i, indexKecil)

def insertionSort(A):
    n = len(A)
    for i in range(1,n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos-1]:
            A[pos] = A[pos-1]
            pos = pos-1
        A[pos] = nilai
        
#Nomor3
from time import time as detak
from random import shuffle as kocok

k = [i for i in range(1,6001)]
kocok(k)
u_bub = k[:]
u_sel = k[:]
u_ins = k[:]

aw = detak();bubbleSort(u_bub);ak=detak();print("Bubble    : %g detik"%(ak-aw));
aw = detak();selectionSort(u_sel);ak=detak();print("Selection : %g detik"%(ak-aw));
aw = detak();insertionSort(u_ins);ak=detak();print("Insertion : %g detik"%(ak-aw));
