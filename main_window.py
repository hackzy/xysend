
from h_ui_object import Ui_object
from main_windows_func import Main_Func
class Main_window:
    def __init__(self):
        self.ui = Ui_object()
        self.func = Main_Func(self.ui)
        self.ui.butten_connet_db.config(command=self.func.buttn_connet_db)
        self.ui.root.command = self.func.main_window_start()
        self.ui.butten.config(command=self.func.buttn_chaxun)





   
if __name__ == '__main__':
    main = Main_window()
    main.ui.root.mainloop()
