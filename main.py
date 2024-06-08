import tkinter as tk
from tkinter import filedialog, messagebox, font

# Define a global variable to store the previously saved text
saved_text = ""

def save_file():
    global saved_text
    if text_area.get("1.0", tk.END) != saved_text:
        response = messagebox.askyesnocancel("Save Changes", "Do you want to save changes?")
        if response is None:  # User clicked Cancel
            return
        elif response:  # User clicked Yes
            file_path = filedialog.asksaveasfilename(filetypes=[("Text files", "*.txt"),
                                                                 ("HTML files", "*.html"),
                                                                 ("XML files", "*.xml"),
                                                                 ("JavaScript files", "*.js"),
                                                                 ("CSS files", "*.css"),
                                                                 ("Python files", "*.py"),
                                                                 ("C++ files", "*.cpp"),
                                                                 ("C# files", "*.cs"),
                                                                 ("C files", "*.c"),
                                                                 ("Header files", "*.h"),
                                                                 ("Rust files", "*.rs"),
                                                                 ("Assembly files", "*.asm"),
                                                                 ("Assembly files (6502)", "*.s"),
                                                                 ("Java files", "*.java"),
                                                                 ("Shell files", "*.sh"),
                                                                 ("Batch files", "*.bat"),
                                                                 ("Swift files", "*.swift"),
                                                                 ("Go files", "*.go"),
                                                                 ("PHP files", "*.php"),
                                                                 ("Ruby files", "*.rb"),
                                                                 ("Perl files", "*.pl"),
                                                                 ("SQL files", "*.sql"),
                                                                 ("Markdown files", "*.md"),
                                                                 ("YAML files", "*.yaml"),
                                                                 ("JSON files", "*.json"),
                                                                 ("TeX files", "*.tex"),
                                                                 ("INI files", "*.ini"),
                                                                 ("Config files", "*.cfg"),
                                                                 ("Lock files", "*.lock"),
                                                                 ("TOML files", "*.toml"),
                                                                 ("Log files", "*.log"),
                                                                 ("All files", "*.*")])
            if file_path:
                with open(file_path, "w") as file:
                    file.write(text_area.get("1.0", tk.END))
                saved_text = text_area.get("1.0", tk.END)
        else:  # User clicked No
            pass

def open_file():
    global saved_text
    if text_area.get("1.0", tk.END) != saved_text:
        response = messagebox.askyesnocancel("Save Changes", "Do you want to save changes?")
        if response is None:  # User clicked Cancel
            return
        elif response:  # User clicked Yes
            save_file()
        else:  # User clicked No
            pass
    
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"),
                                                      ("HTML files", "*.html"),
                                                      ("XML files", "*.xml"),
                                                      ("JavaScript files", "*.js"),
                                                      ("CSS files", "*.css"),
                                                      ("Python files", "*.py"),
                                                      ("C++ files", "*.cpp"),
                                                      ("C# files", "*.cs"),
                                                      ("C files", "*.c"),
                                                      ("Header files", "*.h"),
                                                      ("Rust files", "*.rs"),
                                                      ("Assembly files", "*.asm"),
                                                      ("Assembly files (6502)", "*.s"),
                                                      ("Java files", "*.java"),
                                                      ("Shell files", "*.sh"),
                                                      ("Batch files", "*.bat"),
                                                      ("Swift files", "*.swift"),
                                                      ("Go files", "*.go"),
                                                      ("PHP files", "*.php"),
                                                      ("Ruby files", "*.rb"),
                                                      ("Perl files", "*.pl"),
                                                      ("SQL files", "*.sql"),
                                                      ("Markdown files", "*.md"),
                                                      ("YAML files", "*.yaml"),
                                                      ("JSON files", "*.json"),
                                                      ("TeX files", "*.tex"),
                                                      ("INI files", "*.ini"),
                                                      ("Config files", "*.cfg"),
                                                      ("Lock files", "*.lock"),
                                                      ("TOML files", "*.toml"),
                                                      ("Log files", "*.log"),
                                                      ("All files", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            text = file.read()
            text_area.delete("1.0", tk.END)
            text_area.insert("1.0", text)
        saved_text = text

def change_font_size(size):
    text_area.configure(font=(text_area["font"][0], size))

def change_font_family(family):
    global text_area
    font_size = int(text_area.cget("size"))
    text_area.configure(font=(family, font_size))

root = tk.Tk()
root.title("Simple Text Editor")

text_area = tk.Text(root, wrap="word")
text_area.pack(expand=True, fill="both")

menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
menu_bar.add_cascade(label="File", menu=file_menu)

font_menu = tk.Menu(menu_bar, tearoff=0)
font_menu.add_command(label="12", command=lambda: change_font_size(12))
font_menu.add_command(label="14", command=lambda: change_font_size(14))
font_menu.add_command(label="16", command=lambda: change_font_size(16))
font_menu.add_command(label="18", command=lambda: change_font_size(18))
font_menu.add_command(label="20", command=lambda: change_font_size(20))

font_family_menu = tk.Menu(menu_bar, tearoff=0)
font_family_menu.add_command(label="Arial", command=lambda: change_font_family("Arial"))
font_family_menu.add_command(label="Times New Roman", command=lambda: change_font_family("Times New Roman"))
font_family_menu.add_command(label="Courier New", command=lambda: change_font_family("Courier New"))

menu_bar.add_cascade(label="Font Size", menu=font_menu)
menu_bar.add_cascade(label="Font Family", menu=font_family_menu)

root.config(menu=menu_bar)

root.mainloop()
