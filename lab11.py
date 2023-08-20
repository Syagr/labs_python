""" 1 """
""" import tkinter as tk

def button_click():
    print("Button clicked!")

root = tk.Tk()

button = tk.Button(root, text="Click me!", command=button_click)
button.pack()

root.mainloop() """

""" 2 """
""" import tkinter as tk

def update_label():
    text = entry.get()
    label.config(text=text)

root = tk.Tk()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Update", command=update_label)
button.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()
"""

""" 3 """
""" import tkinter as tk
import tkinter.simpledialog as sd

class ListBoxDemo:
    def __init__(self, master):
        self.master = master
        master.title("Listbox Demo")

        self.listbox = tk.Listbox(master)
        self.listbox.pack()

        self.listbox.insert(tk.END, "Item 1")
        self.listbox.insert(tk.END, "Item 2")
        self.listbox.insert(tk.END, "Item 3")

        self.add_button = tk.Button(master, text="Add", command=self.add_item)
        self.add_button.pack()

        self.remove_button = tk.Button(master, text="Remove", command=self.remove_item)
        self.remove_button.pack()

    def add_item(self):
       
        new_item = sd.askstring("Add Item", "Enter a new item:")

        if new_item:
            self.listbox.insert(tk.END, new_item)

    def remove_item(self):
        
        selected_index = self.listbox.curselection()

      
        if selected_index:
            self.listbox.delete(selected_index)


root = tk.Tk()
app = ListBoxDemo(root)
root.mainloop()
"""

""" 4 """
""" import tkinter as tk

class DrawingApp:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(self.master, width=500, height=500, bg='white')
        self.canvas.pack()
        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_move_press)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)
        self.start_x = None
        self.start_y = None
        self.rect = None
        self.circle = None
        self.line = None

    def on_button_press(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def on_move_press(self, event):
        if self.rect:
            self.canvas.delete(self.rect)
        if self.circle:
            self.canvas.delete(self.circle)
        if self.line:
            self.canvas.delete(self.line)

        if event.x > self.start_x and event.y > self.start_y:
            self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, event.x, event.y, outline='black')
        elif event.x < self.start_x and event.y > self.start_y:
            self.rect = self.canvas.create_rectangle(event.x, self.start_y, self.start_x, event.y, outline='black')
        elif event.x > self.start_x and event.y < self.start_y:
            self.rect = self.canvas.create_rectangle(self.start_x, event.y, event.x, self.start_y, outline='black')
        else:
            self.rect = self.canvas.create_rectangle(event.x, event.y, self.start_x, self.start_y, outline='black')

        if event.x > self.start_x and event.y > self.start_y:
            self.circle = self.canvas.create_oval(self.start_x, self.start_y, event.x, event.y, outline='black')
        elif event.x < self.start_x and event.y > self.start_y:
            self.circle = self.canvas.create_oval(event.x, self.start_y, self.start_x, event.y, outline='black')
        elif event.x > self.start_x and event.y < self.start_y:
            self.circle = self.canvas.create_oval(self.start_x, event.y, event.x, self.start_y, outline='black')
        else:
            self.circle = self.canvas.create_oval(event.x, event.y, self.start_x, self.start_y, outline='black')

        self.line = self.canvas.create_line(self.start_x, self.start_y, event.x, event.y, fill='black')

    def on_button_release(self, event):
        self.start_x = None
        self.start_y = None

if __name__ == '__main__':
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()
"""

""" 5 """
""" import tkinter as tk
from PIL import Image, ImageTk

class ImageApp:
    def __init__(self, master, image_path):
        self.master = master
        self.master.title('Image App')

        self.image = Image.open(image_path)

        self.photo_image = ImageTk.PhotoImage(self.image)

        self.canvas = tk.Canvas(self.master, width=self.image.width, height=self.image.height)
        self.canvas.pack()

        self.canvas.create_image(0, 0, image=self.photo_image, anchor='nw')

        self.zoom_in_button = tk.Button(self.master, text='+', command=self.zoom_in)
        self.zoom_out_button = tk.Button(self.master, text='-', command=self.zoom_out)
        self.zoom_in_button.pack(side='left')
        self.zoom_out_button.pack(side='left')

        self.zoom_level = tk.Scale(self.master, from_=1, to=10, orient='horizontal', command=self.set_zoom_level)
        self.zoom_level.set(5)
        self.zoom_level.pack()

    def zoom_in(self):
        self.set_zoom_level(self.zoom_level.get() + 1)

    def zoom_out(self):
        self.set_zoom_level(self.zoom_level.get() - 1)

    def set_zoom_level(self, level):
        percent = int(level) * 10
        width = int(self.image.width * percent / 100)
        height = int(self.image.height * percent / 100)
        resized_image = self.image.resize((width, height))

        self.photo_image = ImageTk.PhotoImage(resized_image)

        self.canvas.config(width=width, height=height)
        self.canvas.create_image(0, 0, image=self.photo_image, anchor='nw')

if __name__ == '__main__':
    root = tk.Tk()
    app = ImageApp(root, './image.jpg')
    root.mainloop()
"""

""" 6 """
""" import tkinter as tk

class Table:
    def __init__(self, master, rows=3, columns=3):
        self.rows = rows
        self.columns = columns
        self.cells = [[None for j in range(columns)] for i in range(rows)]
        for i in range(rows):
            for j in range(columns):
                cell = tk.Entry(master)
                cell.grid(row=i, column=j)
                self.cells[i][j] = cell

root = tk.Tk()
table = Table(root)
root.mainloop() """

""" 7 """
import tkinter as tk

class MenuBar:
    def __init__(self, master):
        self.master = master
        self.menu_bar = tk.Menu(master)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.view_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.create_menus()
        master.config(menu=self.menu_bar)

    def create_menus(self):
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.master.quit)

        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Cut", command=self.cut_text)
        self.edit_menu.add_command(label="Copy", command=self.copy_text)
        self.edit_menu.add_command(label="Paste", command=self.paste_text)

        self.menu_bar.add_cascade(label="View", menu=self.view_menu)
        self.view_menu.add_command(label="Toggle Fullscreen", command=self.toggle_fullscreen)

    def new_file(self):
        print("Creating new file...")

    def open_file(self):
        print("Opening file...")

    def save_file(self):
        print("Saving file...")

    def cut_text(self):
        print("Cutting text...")

    def copy_text(self):
        print("Copying text...")

    def paste_text(self):
        print("Pasting text...")

    def toggle_fullscreen(self):
        self.master.attributes("-fullscreen", not self.master.attributes("-fullscreen"))

root = tk.Tk()
menu = MenuBar(root)
root.mainloop()

""" 8 """
""" import tkinter as tk
from tkinter import ttk
import threading
import time

class ProgressBar:
    def __init__(self, master):
        self.master = master
        self.progress_bar = ttk.Progressbar(master, orient="horizontal", length=200, mode="determinate")
        self.progress_bar.grid(row=0, column=0, padx=10, pady=10)
        self.start_button = tk.Button(master, text="Start Download", command=self.start_download)
        self.start_button.grid(row=1, column=0, padx=10, pady=10)

    def start_download(self):
        self.start_button.config(state="disabled")
        self.progress_bar.config(maximum=100)
        self.progress_bar.start()
        self.download_thread = threading.Thread(target=self.download_file)
        self.download_thread.start()

    def download_file(self):
        # Simulate download
        for i in range(101):
            time.sleep(0.05) # Simulate processing time
            self.progress_bar.step(1)
            self.master.update_idletasks()

        self.progress_bar.stop()
        self.progress_bar.config(value=0)
        self.start_button.config(state="normal")

root = tk.Tk()
progress_bar = ProgressBar(root)
root.mainloop()
"""

""" 9 """
""" import tkinter as tk
from tkinter import filedialog

class FileViewer:
    def __init__(self, master):
        self.master = master
        self.file_label = tk.Label(master, text="")
        self.file_label.pack(pady=10)
        self.select_button = tk.Button(master, text="Select File", command=self.select_file)
        self.select_button.pack(pady=10)

    def select_file(self):
        file_path = filedialog.askopenfilename(title="Select a file", filetypes=(("Text files", "*.txt"), ("JSON files", "*.json")))
        if file_path:
            with open(file_path, "r") as f:
                file_contents = f.read()
            self.file_label.config(text=file_contents)

root = tk.Tk()
file_viewer = FileViewer(root)
root.mainloop()
"""