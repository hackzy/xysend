import tkinter.messagebox as tkMessageBox
import pymysql
import configparser
from tkinter import Toplevel
class Main_Func:
    def __init__(self,ui):
        self.ui = ui
        self.config = configparser.ConfigParser()
        self.chaxun = None
    def hello_message(self):
        tkMessageBox.showinfo('hello', 'hello world')

    #连接MySQL数据库
    def connect_mysql(self):
        try:
            sql = pymysql.connect(
                            host=self.ui.entry_ip.get(),
                            port=int(self.ui.entry_port.get()),
                            user=self.ui.entry_uname.get(),
                            password=self.ui.entry_password.get(),
                            charset='utf8')
            return sql
        except:
            tkMessageBox.showinfo('错误', '连接数据库失败！')
        
    
    #连接库一
    def connect_adb(self):
        try:
            sql = pymysql.connect(
                                    host=self.ui.entry_ip.get(),
                                    port=int(self.ui.entry_port.get()),
                                    user=self.ui.entry_uname.get(),
                                    password=self.ui.entry_password.get(),
                                    db=self.ui.entry_db1.get(),
                                    charset='utf8')
            return sql
        except:
            tkMessageBox.showinfo('失败', '连接数据库失败！')
    
    #连接库二
    def connect_ddb(self):
        try:
            sql = pymysql.connect(
                                    host=self.ui.entry_ip.get(),
                                    port=int(self.ui.entry_port.get()),
                                    user=self.ui.entry_uname.get(),
                                    password=self.ui.entry_password.get(),
                                    db=self.ui.entry_db2.get(),
                                    charset='utf8')
            return sql
        except:
            tkMessageBox.showinfo('失败', '连接数据库失败！')

    #连接库三
    def connect_mdb(self):
        try:
            sql = pymysql.connect(
                                    host=self.ui.entry_ip.get(),
                                    port=int(self.ui.entry_port.get()),
                                    user=self.ui.entry_uname.get(),
                                    password=self.ui.entry_password.get(),
                                    db=self.ui.entry_db3.get(),
                                    charset='utf8')
            return sql
        except:
            tkMessageBox.showinfo('失败', '连接数据库失败！')

    #连接库四
    def connect_ldb(self):
        try:
            sql = pymysql.connect(
                                    host=self.ui.entry_ip.get(),
                                    port=int(self.ui.entry_port.get()),
                                    user=self.ui.entry_uname.get(),
                                    password=self.ui.entry_password.get(),
                                    db=self.ui.entry_db4.get(),
                                    charset='utf8')
            return sql
        except:
            tkMessageBox.showinfo('失败', '连接数据库失败！')

    '窗口启动'
    def main_window_start(self):
        self.read_ini()

    '连接数据库按钮按下'
    def buttn_connet_db(self):
        sql = self.connect_mysql()
        if sql:
            tkMessageBox.showinfo('成功', '连接数据库成功！')
        print(sql.cursor())
        self.save_ini()

    def buttn_chaxun(self):
        #查询按钮
        if self.chaxun == None:
            self.chaxun = self.load_child_window(self.ui.setting.chaxun_title,self.ui.setting.chaxun_geometry)
            self.chaxun.protocol('WM_DELETE_WINDOW',lambda:self.chaxun.destroy() or setattr(self,'chaxun',None))
            self.ui.setting.chaxun_init()
            sql = self.connect_mysql()
            cursor = sql.cursor()
            cursor.execute("show databases")
            data = cursor.fetchall()
            print(data)
            sql.close()
        else:
            #如果窗口已经存在，就把它放到最前面
            self.chaxun.attributes('-topmost',1)

    '载入子窗口函数'
    def load_child_window(self,title,geometry):
        child = Toplevel(self.ui.root)
        child.title(title)
        child.geometry(geometry)
        return child


    def save_ini(self):
        #保存配置文件
        if not self.config.read('config.ini'):
            self.config.add_section('mysql')
        self.config.set('mysql','host',self.ui.entry_ip.get())
        self.config.set('mysql','port',self.ui.entry_port.get())
        self.config.set('mysql','user',self.ui.entry_uname.get())
        self.config.set('mysql','password',self.ui.entry_password.get())
        self.config.write(open('config.ini','w'))


    def read_ini(self):
        #读取配置文件
        if not self.config.read('config.ini'):
            pass
        else:
            try:
                self.config.read('config.ini')
                self.ui.entry_ip.delete(0, 'end')
                self.ui.entry_port.delete(0, 'end')
                self.ui.entry_uname.delete(0, 'end')
                self.ui.entry_password.delete(0, 'end')
                self.ui.entry_ip.insert(0,self.config.get('mysql','host'))
                self.ui.entry_port.insert(0,self.config.get('mysql','port'))
                self.ui.entry_uname.insert(0,self.config.get('mysql','user'))
                self.ui.entry_password.insert(0,self.config.get('mysql','password'))

            except:
                print("读取配置文件失败！")