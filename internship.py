import tkinter as tk
from tkinter import filedialog

class SimpleEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Text Editor")
        self.text_area = tk.Text(self.root, wrap="word")
        self.text_area.pack(expand="yes", fill="both")

        # Create a menu bar
        menu_bar = tk.Menu(root)
        root.config(menu=menu_bar)

        # Create File menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.destroy)

        # Create Edit menu
        edit_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Edit", menu=edit_menu)
        
        # Text Align submenu
        align_submenu = tk.Menu(edit_menu, tearoff=0)
        edit_menu.add_cascade(label="Text Align", menu=align_submenu)
        align_submenu.add_command(label="Left", command=lambda: self.set_text_align("left"))
        align_submenu.add_command(label="Center", command=lambda: self.set_text_align("center"))
        align_submenu.add_command(label="Right", command=lambda: self.set_text_align("right"))

    def new_file(self):
        self.text_area.delete(1.0, tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, file.read())

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))

    def set_text_align(self, alignment):
        self.text_area.tag_configure("align", justify=alignment)
        self.text_area.tag_add("align", 1.0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    editor = SimpleEditor(root)
    root.mainloop()
