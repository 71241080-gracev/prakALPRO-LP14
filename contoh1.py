#contoh={'aja', 90, 'k', 3}
#sypaj=('paul verlaine', 'mori ogai', 'akutagawa')
#baru=set(sypaj)
#print(baru)

#penulis_buku=set()

#nama_penulis=('paul verlaine', 'mori ogai', 'natsume soseki', 'osamu dazai', 'nakahara chuuya')
#jumlah=len(nama_penulis)
#print(jumlah)
#for i in nama_penulis:
#    print(i)

#random=set()
#random.add('7124100')
#random.add('7124101')
#print(random)
#random.add('7124100')
#print(random)
#print(len(random))

#angka={0,1,2,3,4,5,6,7,8,9}
#list_angka=set([0,1,2,3,4,5,6,7,8,9])
#print(list_angka)
#list_angka.remove(6)
#list_angka.add(90)
#print(list_angka)
#angka.clear()
#print(angka)
#angkanw=angka.pop()
#print(angka)
#print(angkanw)
#angkanw=angka.pop()
#print(angka)
#print(angkanw)
#angka.remove(0)
#print('angka 0 ada dalam set', angka)
#angka.remove(90)
#print('angka 90 tidak ada dalam set', angka)
#angka.discard(89)
#print("angka 89 tidak ada dalam set", angka)
#angka.discard(8)
#print("angka 8 ada dalam set", angka)

merk_hp={'samsung', 'vivo', 'oppo', 'apple', 'huawei'}
merk_laptop={'apple', 'acer', 'asus', 'huawei', 'axio'}
satu=merk_laptop^merk_hp
print(satu)
#selisih=merk_hp-merk_laptop
#print(selisih)
#irisan=merk_laptop&merk_hp
#print(irisan)
#gabungan=merk_hp|merk_laptop
#print(gabungan)