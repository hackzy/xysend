
class Ui_setting:
    def __init__(self,ui) -> None:
        self.chaxun_title = '查询'
        self.chaxun_geometry = '800x600+500+300'
        ui.root.title('逍遥')
        ui.root.geometry('1024x400+500+300')
        ui.butten.place(x=100, y=100)
        ui.label1.place(x=5, y=8)
        ui.label2.place(x=213, y=8)
        ui.entry_ip.place(x=83, y=8)
        ui.entry_uname.place(x=260, y=8)
        ui.label3.place(x=350, y=8)
        ui.entry_password.place(x=392, y=8)
        ui.butten_connet_db.place(x=560,y=9,width=80,height=25)
        ui.label_db1.place(x=639,y=9,width=45,height=25)
        ui.entry_db1.place(x=685,y=9,width=45,height=25)
        ui.label_db2.place(x=731,y=9,width=45,height=25)
        ui.entry_db2.place(x=777,y=9,width=45,height=25)
        ui.label_db3.place(x=823,y=9,width=45,height=25)
        ui.entry_db3.place(x=869,y=9,width=45,height=25)
        ui.label_db4.place(x=915,y=9,width=45,height=25)
        ui.entry_db4.place(x=961,y=9,width=45,height=25)
        ui.label_port.place(x=470,y=9)
        ui.entry_port.place(x=510,y=9)
        #entry_ip的内容
        ui.entry_ip.insert(0, '请输入数据库地址')
        ui.entry_uname.insert(0, '请输入用户名')
        #entry_ip获得焦点清空内容
        ui.entry_ip.bind('<Button-1>', lambda event: ui.entry_ip.delete(0, 'end') 
                         if ui.entry_ip.get() == '请输入数据库地址' else "")
        #entry_ip失去焦点，如果内容为空，显示默认内容
        ui.entry_ip.bind('<FocusOut>', lambda event: ui.entry_ip.insert
                         (0, '请输入数据库地址') if ui.entry_ip.get() == '' else '')
        ui.entry_uname.bind('<Button-1>', lambda event: ui.entry_uname.delete(0, 'end')
                             if ui.entry_uname.get() == '请输入用户名' else "")
        ui.entry_uname.bind('<FocusOut>', lambda event: ui.entry_uname.insert
                               (0, '请输入用户名') if ui.entry_uname.get() == '' else '')
        
        ui.entry_password.insert(0, '请输入密码')
        ui.entry_password.bind('<Button-1>', lambda event: ui.entry_password.delete(0, 'end')
                               if ui.entry_password.get() == '请输入密码' else "")
        
        ui.entry_db1.insert(0, 'adb')
        ui.entry_db2.insert(0, 'ddb')
        ui.entry_db3.insert(0, 'mdb')
        ui.entry_db4.insert(0, 'ldb')
        ui.entry_port.insert(0, '3306')
        