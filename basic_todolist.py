

# To Do List Python
# 5200411400 / Alfansyah Nori Pratama
# S1 - Informatika G


import os

aktvitas = []

def fungsi():
	os.system('cls')
	print("===================")
	print("TO DO LIST")
	if len(aktvitas) == 0 :
		print("Belum ada aktvitas")
	else:
		index = 0
		while index < len(aktvitas):
			print(index+1,".",aktvitas[index])
			index += 1

	print("===================")
	cek_menu = input("Tekan Enter Untuk Melihat Menu")

	if(cek_menu == ""):
		print("\nMENU")
		print("1. Tambah To Do List")
		print("2. Coret To Do List")
		print("3. Keluar")
		menu = input("Pilih Menu : ")
		if int(menu) == 1:
			print("")
			tambahAktivitas = input("Tambah Aktivitas : ")
			if(tambahAktivitas != ""):
				aktvitas.append(tambahAktivitas)
				fungsi()
			else:
				print("Input Kosong")
				fungsi()
		elif int(menu) == 2:
			print("")
			if len(aktvitas) != 0:
				print("")
				nomorCoret = int(input("Pilih Nomor yang Ingin Dicoret : "))
				if nomorCoret > len(aktvitas):
					print("Nomor tidak ada !")
				else:
					aktvitas.pop(nomorCoret - 1)
					fungsi()
			else:
				print("Daftar To Do List / Aktivitas Kosong")
				fungsi()
		elif int(menu) == 3:
			confirm = input("Akan keluar dari program, yakin? [Y/N]")
			if confirm == "Y":
				quit()
			elif confirm == "N":
				fungsi()
			else:
				quit()


fungsi()