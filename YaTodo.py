import time
import pickle
import os


class Task:
	def __init__(self, caption, desc):
		self.caption = caption
		self.desc = desc

	def __str__(self):
		return "\"{}\"  :\n\t{}".format(self.caption, self.desc)

class ToDoList:

	def __init__(self, tasks_caption):
		self.tasks_caption = tasks_caption
		self.lst = [] 
		self.oldlst = []
	
	def add(self, item):
		self.lst.append(item)

	def delete(self, choice):
		if choice > len(self.oldlst) or choice < 0 :
			print("Indeks tidak valid!")
			display_main_menu()
		else:
			del self.lst[choice]
	
	def deletecompleted(self, choice):
		if choice > len(self.oldlst) or choice < 0 :
			print("Indeks tidak valid!")
			return display_main_menu()

		else:
			del self.oldlst[choice]
	
	def save(self, f):
		pickle.dump(self, f)

	def get_list(self):
		return self.lst

	def check(self, choice):
		self.oldlst.append( self.lst[choice]+ '      ' +time.strftime("%d %m %Y, %H:%M") )
		del self.lst[choice]

	def get_archive(self):
		return self.oldlst


	def display_current_list(self):
		current_list_str = 'Daftar Todo Saat Ini: \n\n'  + display_list(self.get_list()) + '\n\n'
		return current_list_str

	def display_completed_list(self):
		completed_list_str = 'Daftar Todo Yang Sudah Selesai: \') \n' + display_list(self.get_archive()) + '\n\n'
		return completed_list_str

	def search_list(self, keyword):
		for i in self.lst:
			if keyword in i:
				print(f"Data {keyword} Ditemukan di Todo Saat ini index ke-{self.lst.index(i)}" + '\n')
				break
		else:
			for i in self.oldlst:
				if keyword in i:
					print(f"Data {keyword} Ditemukan di Todo Yang Sudah Selesai index ke-{self.oldlst.index(i)}" + '\n')
					break
				else:
					print(f"Data {keyword} Tidak Ditemukan di list YaTodo\n")
					break
		
		

def display_list(lst):
        return "".join([str(i) + ' : ' + lst[i] + '\n' + ('-' * 50) + '\n' \
                        for i in range(len(lst))])

def load(f):
	c = pickle.load(f)
	return c

def display_main_menu():
	main_menu_str = "-"*15 + "Selamat Datang di YaTodo - Tempat Mencatat Segala Hal :)" + "-"*15 +'''\n 
	Berikut menu yang dapat dipilih :  \n
	\t1:Tambahkan Item Kedalam List Todo Saat Ini.\n
	\t2:Tampilkan Todo List Saat Ini.\n
	\t3:Tampilkan Todo Yang Sudah Selesai.\n
	\t4:Cari data Todo.\n
	\t5:Simpan List Todo.\n 
	\t0:Keluar.\n
	'''
	return main_menu_str


######### Main program #########
def main():
	if os.path.exists("lst.tdl"): 
		with open("lst.tdl", 'rb') as f:
			tasks = pickle.load(f)
	else:
		tasks = ToDoList('Test tasks')
	while True:
		os.system('clear || cls')
		print(display_main_menu())
		choice = input('Masukkan Pilihan Anda :')
		if choice == '1':
			title = input('Masukkan Judul Todo : ')
			desc = input('Masukkan Deskripsi Todo : ')
			item = Task(title, desc)
			tasks.add(str(item))
		elif choice == '2':
			os.system('clear || cls')
			print(tasks.display_current_list())
			print('c : Checklist(Tandai Selesai) \t h: Hapus \t k: Keluar ')
			pilihan = input('Masukkan Pilihan Anda : ').lower()
			if pilihan == 'c':
				completed = int(input("Masukkan Nomor Todo Yang Ingin Ditandai: "))
				tasks.check(completed)
			elif pilihan == 'h':
				deleted = int(input("Masukkan Nomor Todo Yang Ingin Dihapus: "))
				tasks.delete(deleted)
				continue
			elif pilihan == 'k':
				continue
		elif choice == '3':
			os.system('clear || cls')
			print(tasks.display_completed_list())
			print(' h: Hapus \t k: Keluar ')
			pilihan = input('Masukkan Pilihan Anda : ').lower()
			if pilihan == 'h':
				deleted = int(input("Masukkan Nomor Todo Yang Ingin Dihapus: "))
				tasks.deletecompleted(deleted)
				continue
			elif pilihan == 'k':
				continue
		elif choice == '4':
			os.system('clear || cls')
			keyword = input("Masukkan Keyword Yang Ingin Dicari : ")
			tasks.search_list(keyword)
			
			print('k: Keluar ke Menu ')
			pilihan = input('Masukkan Pilihan Anda : ').lower()
			if pilihan == 'k':
				continue
		elif choice == '5':
			os.system('clear || cls')
			with open("lst.tdl", 'wb') as f:
				tasks.save(f)
			continue
		elif choice == '0':
			os.system('clear || cls')
			break

if __name__ == '__main__':
	main()