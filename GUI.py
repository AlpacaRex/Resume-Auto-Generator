import tkinter as tk
from tkinter import ttk
from main import makepdf
import tkinter.filedialog
import os

def add_edu():
    eduExpList1.insert(tk.END, eduExpTime.get())
    eduExpList2.insert(tk.END, eduExp.get())
    eduExpTime.delete(0, tk.END)
    eduExp.delete(0, tk.END)


def add_work():
    workExpList1.insert(tk.END, workExpTime.get())
    workExpList2.insert(tk.END, workExp.get())
    workExpTime.delete(0, tk.END)
    workExp.delete(0, tk.END)


def processpdf():
    makepdf(pdf_path.get(), name.get(), edu.get(), age.get(), tel.get(), sex.get(), email.get(), pic_path.get(),
            eduExpList1, eduExpList2,workExpList1, workExpList2, tech.get('0.0', tk.END), eva.get('0.0', tk.END))


def select_picpath():
    path = tk.filedialog.askopenfilename()
    path = path.replace("/", "\\")
    pic_path.delete(0, tk.END)
    pic_path.insert(0, path)


def select_pdfpath():
    path = tk.filedialog.asksaveasfilename(defaultextension='.pdf', filetypes=[("pdf files", '*.pdf')])
    path = path.replace("/", "\\")
    pdf_path.delete(0, tk.END)
    pdf_path.insert(0, path)


window = tk.Tk()
window.title('简历自动生成工具')
window.geometry('500x800')

mighty1 = ttk.LabelFrame(window, text=' 基本信息 ')  # 限制在第一个子框架内
mighty1.pack(padx=5, pady=5)  # 子框架位置

tk.Label(mighty1, text="姓名：").grid(row=0, column=0, padx=2, pady=3)
name = tk.Entry(mighty1, width=25)
name.grid(row=0, column=1, padx=2, pady=3)
tk.Label(mighty1, text="年龄：").grid(row=1, column=0, padx=2, pady=3)
age = tk.Entry(mighty1, width=25)
age.grid(row=1, column=1, padx=2, pady=3)
tk.Label(mighty1, text="性别：").grid(row=2, column=0, padx=2, pady=3)
sex = tk.Entry(mighty1, width=25)
sex.grid(row=2, column=1, padx=2, pady=3)
tk.Label(mighty1, text="学历：").grid(row=0, column=2, padx=2, pady=3)
edu = tk.Entry(mighty1, width=25)
edu.grid(row=0, column=3, padx=2, pady=3)
tk.Label(mighty1, text="电话：").grid(row=1, column=2, padx=2, pady=3)
tel = tk.Entry(mighty1, width=25)
tel.grid(row=1, column=3, padx=2, pady=3)
tk.Label(mighty1, text="邮箱：").grid(row=2, column=2, padx=2, pady=3)
email = tk.Entry(mighty1, width=25)
email.grid(row=2, column=3, padx=2, pady=3)
pic_path = tk.Entry(mighty1, width=55)
pic_path.grid(row=3, column=0, columnspan=4, padx=2, pady=3, sticky=tk.W)
tk.Button(mighty1, text="选择图片", command=select_picpath).grid(row=3, column=3, padx=2, pady=3, sticky=tk.E)


mighty2 = ttk.LabelFrame(window, text=' 教育背景 ')
mighty2.pack(padx=5, pady=10)

eduExpList1 = tk.Listbox(mighty2, width=15, height=5)
eduExpList2 = tk.Listbox(mighty2, width=45, height=5)
eduExpTime = tk.Entry(mighty2, width=10)
eduExp = tk.Entry(mighty2, width=35)
eduExpList1.grid(row=0, column=0, columnspan=2, padx=0, pady=3)
eduExpList2.grid(row=0, column=2, columnspan=3, padx=0, pady=3)
tk.Label(mighty2, text="时间：").grid(row=1, column=0, padx=2, pady=3)
eduExpTime.grid(row=1, column=1, padx=2, pady=3)
tk.Label(mighty2, text="经历：").grid(row=1, column=2, padx=2, pady=3)
eduExp.grid(row=1, column=3, padx=2, pady=3)
tk.Button(mighty2, text="添加", command=add_edu).grid(row=1, column=4, padx=2, pady=3)


mighty3 = ttk.LabelFrame(window, text=' 工作经历 ')
mighty3.pack(padx=5, pady=5)

workExpList1 = tk.Listbox(mighty3, width=15, height=5)
workExpList2 = tk.Listbox(mighty3, width=45, height=5)
workExpTime = tk.Entry(mighty3, width=10)
workExp = tk.Entry(mighty3, width=35)
workExpList1.grid(row=0, column=0, columnspan=2, padx=0, pady=3)
workExpList2.grid(row=0, column=2, columnspan=3, padx=0, pady=3)
tk.Label(mighty3, text="时间：").grid(row=1, column=0, padx=2, pady=3)
workExpTime.grid(row=1, column=1, padx=2, pady=3)
tk.Label(mighty3, text="经历：").grid(row=1, column=2, padx=2, pady=3)
workExp.grid(row=1, column=3, padx=2, pady=3)
tk.Button(mighty3, text="添加", command=add_work).grid(row=1, column=4, padx=2, pady=3)


mighty4 = ttk.LabelFrame(window, text=' 技能特长 ')
mighty4.pack(padx=5, pady=5)
tech = tk.Text(mighty4, width=64, height=5)
tech.pack(padx=5, pady=5)

mighty5 = ttk.LabelFrame(window, text=' 自我评价 ')
mighty5.pack(padx=5, pady=5)
eva = tk.Text(mighty5, width=64, height=5)
eva.pack(padx=5, pady=5)


mighty6 = ttk.LabelFrame(window)
mighty6.pack(padx=5, pady=5)
pdf_path = tk.Entry(mighty6, width=45)
pdf_path.grid(row=0, column=0, padx=2, pady=3)
tk.Button(mighty6, text="选择保存路径", command=select_pdfpath).grid(row=0, column=1, padx=2, pady=3)
tk.Button(mighty6, text="生成pdf", command=processpdf).grid(row=0, column=2, padx=2, pady=3)

window.mainloop()



