import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("Grocery List")
root.geometry("400x400")


def add_item():
    item = entry.get()

    if item:
        tree.insert("", "end", values=(item,))
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Enter an item!")


def delete_item():
    selected = tree.selection()

    if selected:
        tree.delete(selected)
    else:
        messagebox.showwarning("Warning", "Select an item!")


ttk.Label(root, text="Grocery List").pack(pady=10)

entry = ttk.Entry(root)
entry.pack(pady=5)


ttk.Button(root, text="Add Item", command=add_item).pack(pady=5)
ttk.Button(root, text="Delete Item", command=delete_item).pack(pady=5)


tree = ttk.Treeview(root, columns=("Item",), show="headings")
tree.heading("Item", text="Grocery Item")
tree.pack(pady=10, fill="both", expand=True)

root.mainloop()