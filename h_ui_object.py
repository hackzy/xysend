import tkinter as tk
import ui_setting as ui

class Ui_object:
    def __init__(self):
        self.root = tk.Tk()
        self.chaxun = None
        self.entry_ip = tk.Entry(self.root, show=None, font=('GB2312', 10),width=17)
        self.entry_uname = tk.Entry(self.root, show=None, font=('GB2312', 10),width=12)
        self.entry_password = tk.Entry(self.root, show='*', font=('GB2312', 10),width=10)
        self.label1 = tk.Label(self.root, text='数据库地址:', font=('GB2312', 10), width=10, height=1)
        self.label2 = tk.Label(self.root, text='用户名:', font=('GB2312', 10), width=5, height=1)
        self.label3 = tk.Label(self.root, text='密码:', font=('GB2312', 10), width=4, height=1)
        self.butten = tk.Button(self.root, text='添加',  width=10, height=2)
        self.butten_connet_db = tk.Button(self.root, text='连接数据库')
        self.label_db1 = tk.Label(self.root,text='库一:')
        self.label_db2 = tk.Label(self.root,text='库二:')
        self.label_db3 = tk.Label(self.root,text='库三:')
        self.label_db4 = tk.Label(self.root,text='库四:')
        self.entry_db1 = tk.Entry(self.root, show=None, font=('GB2312', 10))
        self.entry_db2 = tk.Entry(self.root, show=None, font=('GB2312', 10))
        self.entry_db3 = tk.Entry(self.root, show=None, font=('GB2312', 10))
        self.entry_db4 = tk.Entry(self.root, show=None, font=('GB2312', 10))
        self.label_port = tk.Label(self.root, text='端口:', font=('GB2312', 10), width=4, height=1)
        self.entry_port = tk.Entry(self.root, show=None, font=('GB2312', 10),width=5)
        self.setting = ui.Ui_setting(self)
        
        '初始化子窗口控件'
    def chaxun_init(self):
        self.chaxun_label1 = tk.Label(self.chaxun, text='库一:', font=('GB2312', 10), width=4, height=1)







        
        