def teks(doc):
    try:
        with open (doc, 'r') as file:
            isi=file.read().lower()
            kata=isi.split()
            return set(kata)
    except FileNotFoundError:
        print("File tidak ditemukan.")
        
doc1=input("Masukkan nama file1: ")
doc2=input("Masukkan nama file2: ")

kata_doc1=teks(doc1)
kata_doc2=teks(doc2)

if kata_doc1 and kata_doc2 is not None:
    sama=kata_doc1&kata_doc2
    print("Kata yang sama: ", sama)
else:
    print("Kata sama tidak ditemukan.")