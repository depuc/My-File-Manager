import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog


class File_Manager:

    def __init__(self,root):
        self.root = root
        self.root.title("File Manager")
        self.root.geometry("600x400")
        self.base_dir = os.getcwd()
        self.current_dir = self.base_dir
        self.create_widget()
        self.update_file_list()

    def create_widget(self):
        self.path_label = tk.Label(self.root, text=self.current_dir)
        self.path_label.pack()
        self.file_listbox = tk.Listbox(self.root,selectmode=tk.SINGLE)
        self.file_listbox.pack(expand=True, fill=tk.BOTH)
        self.file_listbox.bind('<Double-1>', self.on_item_double_click)
        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack(fill=tk.X)
        self.create_folder = tk.Button(self.buttons_frame, text='Create Folder', command=self.create_folder)
        self.create_folder.pack(side=tk.LEFT)
        self.create_file = tk.Button(self.buttons_frame, text='Create File', command=self.create_file)
        self.create_file.pack(side=tk.LEFT)
        self.delete_button= tk.Button(self.buttons_frame, text='Delete', command=self.delete_item)
        self.delete_button.pack(side=tk.LEFT)
        self.copy_button=tk.Button(self.buttons_frame, text='Copy',command=self.copy_item)
        self.copy_button.pack(side=tk.LEFT)
        self.move_button=tk.Button(self.buttons_frame, text='Move',command=self.move_item)
        self.move_button.pack(side=tk.LEFT)

    def update_file_list(self):
        self.file_listbox.delete(0,tk.END)
        self.path_label.config(text=self.current_dir)
        for item in os.listdir(self.current_dir):
            self.file_listbox.insert(tk.END,item)
    def on_item_double_click(self, event):
        pass
    def create_folder(self):
        pass
    def create_file(self):
        pass
    def delete_item(self):
        pass
    def copy_item(self):
        pass
    def move_item(self):
        pass
    


if __name__ == "__main__":
    root = tk.Tk()
    app = File_Manager(root)
    root.mainloop()


