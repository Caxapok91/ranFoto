import tkinter
from tkinter.filedialog import askdirectory
import os
import random
from PIL import ImageTk, Image

root = tkinter.Tk()
width_screen = root.winfo_screenwidth()
height_screen = root.winfo_screenheight()
width_win_app = 500
height_win_app = 500
root.title('Случайное фото')
root.geometry(
    f'{width_win_app}x{width_win_app}+{width_screen // 2 - width_win_app // 2}+{height_screen // 2 - height_win_app // 2}')
path_to_folder = None
list_files_in_folder = []
res_Image = None
rel_h_lbl = 0.3
rel_w_lbl = 0.4
lbl_h = int(height_win_app * rel_h_lbl)
lbl_w = int(width_win_app * rel_w_lbl)


def open_folder():
    global path_to_folder, list_files_in_folder
    path_to_folder = askdirectory()
    list_files_in_folder = os.listdir(path_to_folder)
    len_list_f = len(list_files_in_folder)
    lbl_info.config(text=f'Загружено\n{len_list_f} файлов')
    lbl_path.config(text =f'путь: {path_to_folder}')


def rand_ch():
    global path_to_folder, list_files_in_folder, res_Image
    r_elem = random.choice(list_files_in_folder)
    lbl_ch.config(text=f'случайное фото: {r_elem}')
    img1 = Image.open(f'{path_to_folder}/{r_elem}')
    newImage = img1.resize((lbl_w, lbl_h))
    res_Image = ImageTk.PhotoImage(newImage)
    lbl_im.config(image=res_Image)


btn_load_dir = tkinter.Button(text='Открыть папку', command=open_folder)
btn_load_dir.place(relx=0.3, rely=0.1, relheigh=0.1, relwidth=0.2)

btn_ch = tkinter.Button(text='Сгенерировать', command=rand_ch)
btn_ch.place(relx=0.3, rely=0.3, relheigh=0.1, relwidth=0.4)

lbl_info = tkinter.Label(text='Загружено\n0 файлов')
lbl_info.place(relx=0.5, rely=0.1, relheigh=0.1, relwidth=0.2)
lbl_path = tkinter.Label(text='')
lbl_path.place(relx=0.3, rely=0.2)

lbl_ch = tkinter.Label(text='')
lbl_ch.place(relx=0.3, rely=0.4, relheigh=0.1, relwidth=0.4)

placeholder = Image.open('placeholder.png')
placeholder_res = placeholder.resize((lbl_w, lbl_h))
image_res = ImageTk.PhotoImage(placeholder_res)
lbl_im = tkinter.Label(text='', bg='white', image=image_res)
lbl_im.place(relx=0.3, rely=0.5, relheigh=f'{rel_h_lbl}', relwidth=f'{rel_w_lbl}')


root.mainloop()
