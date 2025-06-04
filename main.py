import tkinter as tk
from tkinter import filedialog, messagebox
from encryption_tool import generate_key, save_key, load_key, encrypt_file, decrypt_file

def encrypt():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    key = generate_key()
    encrypt_file(file_path, key)
    save_key(key, file_path + '.key')
    messagebox.showinfo("Success", "File encrypted and key saved.")

def decrypt():
    file_path = filedialog.askopenfilename()
    if not file_path.endswith('.enc'):
        messagebox.showwarning("Error", "Select a '.enc' encrypted file.")
        return
    key_path = filedialog.askopenfilename(title="Select Key File")
    if not key_path.endswith('.key'):
        messagebox.showwarning("Error", "Select a valid key file.")
        return
    key = load_key(key_path)
    decrypt_file(file_path, key)
    messagebox.showinfo("Success", "File decrypted.")

root = tk.Tk()
root.title("Advanced Encryption Tool")
root.geometry("300x150")

tk.Button(root, text="Encrypt File", command=encrypt).pack(pady=20)
tk.Button(root, text="Decrypt File", command=decrypt).pack()

root.mainloop()
