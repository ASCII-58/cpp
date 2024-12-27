import tkinter as tk
from tkinter import messagebox
import json
import os

# 定义JSON文件路径
DATA_FILE = 'inventory.json'

# 初始化数据
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump([], f)

# 读取数据
def load_data():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

# 保存数据
def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

# 添加商品
def add_item():
    name = entry_name.get()
    quantity = entry_quantity.get()
    if not name or not quantity:
        messagebox.showwarning("输入错误", "请填写所有字段")
        return

    try:
        quantity = int(quantity)
    except ValueError:
        messagebox.showwarning("输入错误", "数量必须是整数")
        return

    data = load_data()
    data.append({"name": name, "quantity": quantity})
    save_data(data)
    messagebox.showinfo("成功", "商品已添加")
    entry_name.delete(0, tk.END)
    entry_quantity.delete(0, tk.END)
    update_inventory_list()

# 更新库存列表
def update_inventory_list():
    inventory_list.delete(0, tk.END)
    data = load_data()
    for item in data:
        inventory_list.insert(tk.END, f"{item['name']}: {item['quantity']}")

# 创建主窗口
root = tk.Tk()
root.title("库存管理系统")

# 商品名称输入
tk.Label(root, text="商品名称").grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

# 商品数量输入
tk.Label(root, text="商品数量").grid(row=1, column=0)
entry_quantity = tk.Entry(root)
entry_quantity.grid(row=1, column=1)

# 添加商品按钮
btn_add = tk.Button(root, text="添加商品", command=add_item)
btn_add.grid(row=2, column=0, columnspan=2)

# 库存列表
inventory_list = tk.Listbox(root)
inventory_list.grid(row=3, column=0, columnspan=2, sticky="nsew")

# 更新库存列表
update_inventory_list()

# 运行主循环
root.mainloop()
