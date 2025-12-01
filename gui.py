import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from run import run
import sys
import _thread

window = tk.Tk()
window.title("bl_sbx GUI")
window.geometry("400x300")
window.resizable(False, False)

path_var = tk.StringVar()
path_var.set("")
title_frame = tk.Frame(window)
title = tk.Label(title_frame, text="bl_sbx patch GUI", font=("San Francisco", 25), anchor="center")
spacer = tk.Frame(title_frame, width=200, height=0)
title.pack(side=tk.LEFT)
spacer.pack(side=tk.LEFT)
title_frame.pack()

over_path_var = tk.StringVar()
over_path_var.set("None")

def set_to_mgpath():
    global path_var
    mg_path = "/private/var/containers/Shared/SystemGroup/systemgroup.com.apple.mobilegestaltcache/Library/Caches/com.apple.MobileGestalt.plist"
    path_var.set(mg_path)

path_typing = tk.Frame(window)
path_label = ttk.Label(path_typing, text="Path to be override file in iOS: ")
path_label.pack(side=tk.LEFT)
path_entry = ttk.Entry(path_typing, width=30, textvariable=path_var)
path_entry.pack(side=tk.LEFT)
path_typing.pack()

shortcut = tk.Frame(window)
shortcut_label = ttk.Label(shortcut, text="Shortcuts: ")
shortcut_label.pack(side=tk.LEFT)
set_to_mgpath_btn = ttk.Button(shortcut, text="MobileGestalt")
set_to_mgpath_btn["command"] = set_to_mgpath
set_to_mgpath_btn.pack(side=tk.LEFT)
spacer = tk.Frame(shortcut, width=200, height=0)
spacer.pack(side=tk.LEFT)
shortcut.pack()

over_path_typing = tk.Frame(window)
over_path_label = ttk.Label(over_path_typing, textvariable=over_path_var)
get_path_btn = ttk.Button(over_path_typing, text="Choose Override File")
get_path_btn["command"] = lambda: over_path_var.set(filedialog.askopenfilename(title="Choose a file to override", filetypes=[("All Files", "*.*")]))
get_path_btn.pack(side=tk.LEFT)
over_path_label.pack(side=tk.LEFT)
spacer = tk.Frame(over_path_typing, width=200, height=0)
spacer.pack(side=tk.LEFT)
over_path_typing.pack()

apply_btn = ttk.Button(window, text="Apply", width=20)
apply_btn.pack(pady=20)

def apply_func():
    try:
        run(over_path_var.get(), path_var.get())
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        print("Exception:", exc_type.__name__, (exc_value if exc_value != "" else "Unknown"))
        # raise e
        messagebox.showerror("Error", f"An error occurred: {exc_type.__name__}: {(exc_value.args[0] if exc_value.args[0] != '' else 'Unknown') if exc_value.args else 'Unknown'}")
apply_btn["command"] = apply_func

window.mainloop()