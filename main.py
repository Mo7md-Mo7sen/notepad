import tkinter as tk
from tkinter import filedialog, messagebox

# Create the main Notepad class
class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Notepad")
        self.root.geometry("800x600")

        # Add Text Widget
        self.text_area = tk.Text(root, font=("Arial", 14))
        self.text_area.pack(fill=tk.BOTH, expand=True)

        # Initialize the filename
        self.file_name = None

        # Add Menu Bar
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # File Menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As", command=self.save_as_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit_app)

        # Edit Menu
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Cut", command=self.cut_text)
        self.edit_menu.add_command(label="Copy", command=self.copy_text)
        self.edit_menu.add_command(label="Paste", command=self.paste_text)

        # Help Menu
        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="About", command=self.show_about)

    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.file_name = None
        self.root.title("Notepad - New File")

    def open_file(self):
        self.file_name = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
        )
        if self.file_name:
            with open(self.file_name, "r") as file:
                content = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(1.0, content)
            self.root.title(f"Notepad - {self.file_name}")

    def save_file(self):
        if self.file_name:
            with open(self.file_name, "w") as file:
                content = self.text_area.get(1.0, tk.END)
                file.write(content)
        else:
            self.save_as_file()

    def save_as_file(self):
        self.file_name = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
        )
        if self.file_name:
            with open(self.file_name, "w") as file:
                content = self.text_area.get(1.0, tk.END)
                file.write(content)
            self.root.title(f"Notepad - {self.file_name}")

    def exit_app(self):
        confirm = messagebox.askyesno("Exit", "Are you sure you want to exit?")
        if confirm:
            self.root.destroy()

    def cut_text(self):
        self.text_area.event_generate("<<Cut>>")

    def copy_text(self):
        self.text_area.event_generate("<<Copy>>")

    def paste_text(self):
        self.text_area.event_generate("<<Paste>>")

    def show_about(self):
        messagebox.showinfo("About", "Notepad using Python\nCreated with Tkinter")

# Main Function
if __name__ == "__main__":
    root = tk.Tk()
    app = Notepad(root)
    root.mainloop()
