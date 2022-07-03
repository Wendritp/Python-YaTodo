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
	'''Class untuk Program Todo
	List lst(Buat list Todo Saat ini)
	List oldlst(Buat list Todo yang sudah selesai)	 
	 '''

	def __init__(self, tasks_caption):
		self.tasks_caption = tasks_caption
		self.lst = [] 
		self.oldlst = []
	
	def add(self, item):
		self.lst.append(item)

	def delete(self, choice):
		del self.lst[choice]
	
	def save(self, f):
		pickle.dump(self, f)

	def get_list(self):
		return self.lst

	def check(self, choice):
		self.oldlst.append( self.lst[choice]+ '      ' +time.ctime() )
		del self.lst[choice]

	def get_archive(self):
		return self.oldlst


	def display_current_list(self):
		current_list_str = 'Daftar Todo Saat Ini: \n\n'  + display_list(self.get_list()) + '\n\n'
		return current_list_str

	def display_completed_list(self):
		completed_list_str = 'Daftar Todo Yang Sudah Selesai: \') \n' + display_list(self.get_archive()) + '\n\n'
		return completed_list_str

def display_list(lst):
        return "".join([str(i) + ' : ' + lst[i] + '\n' + ('-' * 50) + '\n' \
                        for i in range(len(lst))])

def load(f):
	'''fungsi ini mengambil objek file dan mengembalikan objek ToDo'''
	c = pickle.load(f)
	return c

def display_main_menu():
	main_menu_str = "-"*15 + "Selamat Datang di YaTodo - Tempat Mencatat Segala Hal :)" + "-"*15 +'''\n 
	Berikut menu yang dapat dipilih :  \n
	\t1:Tambahkan Item Kedalam List Todo Saat Ini.\n
	\t2:Tampilkan Todo List Saat Ini.\n
	\t3:Tampilkan Todo Yang Sudah Selesai.\n
	\t4:Simpan List Todo.\n 
	\t0:Keluar.\n
	'''
	return main_menu_str




######### Main program #########
def main():
	'''fungsi ini hanya untuk menguji fungsionalitas kelas ToDo'''
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
			title = input('Masukkan Todo\'s Judul : ')
			desc = input('Enter the tasks\'s Deskripsi: ')
			item = Task(title, desc)
			tasks.add(str(item))
		elif choice == '2':
			os.system('clear || cls')
			print(tasks.display_current_list())
			current_list_choice = input('c : Checklist(Tandai Selesai) \t h: Hapus \t k: Keluar : ').lower()
			if current_list_choice == 'c':
				completed = int(input("Masukkan Nomor Todo Yang Ingin Ditandai: "))
				tasks.check(completed)
			elif current_list_choice == 'h':
				deleted = int(input("Masukkan Nomor Todo Yang Ingin Dihapus: "))
				tasks.delete(deleted)
			elif current_list_choice == 'k':
				continue
		elif choice == '3':
			os.system('clear || cls')
			print(tasks.display_completed_list())
			completed_list_choice = input('Quit ? (y/n) : ')
			if completed_list_choice == 'y':
				continue
		elif choice == '4':
			os.system('clear || cls')
			with open("lst.tdl", 'wb') as f:
				tasks.save(f)
			continue
		elif choice == '0':
			os.system('clear || cls')
			break

if __name__ == '__main__':
	main()
