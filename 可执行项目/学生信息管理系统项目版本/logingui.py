from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
import os
from datetime import datetime
import maingui


class LoginWindow(Tk):
    """
    创建登录窗体的GUI界面已经登录的方法
    """

    def __init__(self):
        super().__init__()  # 先执行tk这个类的初始化
        self.title("登录界面")
        self.geometry("620x445+320+180")  # 加号表示窗体打开时出现的坐标位置，分别代表x坐标和y坐标
        self.resizable(0, 0)  # 窗体大小不允许变，两个参数分别代表x轴和y轴
        # self.iconbitmap("."+os.sep+"img"+os.sep+"logo.ico")
        # self["bg"] = "royalblue"
        # 加载窗体
        self.setup_UI()
        # 定义变量（定义全局变量，后面的函数都能访问到）
        self.file_path = "." + os.sep + "Studentmgr" + os.sep + "User.txt"  # 文件路劲
        self.user_list = []  # 存储用户信息
        self.var_password_error_times = 0
        self.user = ""  # 当前的用户
        self.password = ""  # 当前用户的密码
        self.current_user_list = []  # 当前用户的用户名、密码、状态信息

        # 自动执行文件中账号的加载
        self.load_file_info()

    def setup_UI(self):
        # ttk中控件使用style对象设定
        self.Style01 = Style()
        self.Style01.configure("user.TLabel", font=("微软雅黑", 18, "bold"), foreground="black")
        self.Style01.configure("TEntry", font=("微软雅黑", 20, "bold"))
        self.Style01.configure("TButton", font=("微软雅黑", 16, "bold"), foreground="royalblue")

        # 创建一个Label标签展示图片
        self.Login_image = PhotoImage(file="." + os.sep + "img" + os.sep + "logingui.png")
        self.Label_image = Label(self, image=self.Login_image)
        self.Label_image.pack(padx=10, pady=10)

        # 创建一个Label标签 + Entry   --- 用户名
        self.Label_user = Label(self, text="用户名:", style="user.TLabel")
        self.Label_user.pack(side=LEFT, padx=25, pady=5)
        self.var_user = StringVar()  # 判断输入值是否正确，输入框需要捆绑变量
        self.Entry_user = Entry(self, width=15, textvariable=self.var_user, style="TEntry")
        self.Entry_user.pack(side=LEFT, padx=5, pady=8)

        # 创建一个Label标签 + Entry   --- 密码
        self.Label_password = Label(self, text="密码:", style="user.TLabel")
        self.Label_password.pack(side=LEFT, padx=15, pady=5)
        self.var_password = StringVar()
        self.Entry_password = Entry(self, width=15, textvariable=self.var_password, show="*",
                                    style="TEntry")  # 密码以什么符号显示，使用show方法
        self.Entry_password.pack(side=LEFT, padx=5, pady=8)
        # 创建一个按钮    --- 登录
        self.Button_login = Button(self, text="登录", width=7, command=self.login)
        self.Button_login.pack(side=LEFT, padx=20, pady=5)

    def load_file_info(self):
        """
        读取用户名、密码、状态
        :return:
        """
        if not os.path.exists(self.file_path):
            showinfo("系统消息", "提供的文件名不存在！")
        else:
            try:
                with open(file=self.file_path, mode="r") as fd:
                    # 一次读一行
                    current_line = fd.readline()
                    while current_line:
                        temp_list = current_line.split(",")  # 长字符串分割层三个
                        self.user_list.append(temp_list)
                        # 读取下一行,读完了循环就结束了
                        current_line = fd.readline()
            except:
                showinfo("系统消息", "文件读取出现异常！")

    def login(self):
        # 获取用户的用户名和密码
        self.user = self.var_user.get()
        self.password = self.var_password.get()
        # 实现身份验证，遍历用户信息列表
        for index in range(len(self.user_list)):
            # 用户名是否正确
            if self.user.strip().lower() == str(self.user_list[index][0]).strip().lower():
                # 判断账号是否被禁用
                if "0" in str(self.user_list[index][2]).strip().lower():
                    showinfo("系统消息", "账号已禁用,请联系管理员")
                    break
                # 密码是否正确
                if self.password != str(self.user_list[index][1]).strip().lower():
                    self.var_password_error_times += 1

                    # 判读错误是否到三次
                    if self.var_password_error_times >= 3:
                        showinfo("系统消息", "密码错误已达三次，账号已锁定！")
                        # 改变状态
                        self.user_list[index][2] = "0\n"
                        # 信息写入到文件
                        self.write_file_info()

                    else:
                        showinfo("系统消息", "输入的密码错误")
                    # 判断成功后整个循环退出，不要执行后面的判断用户名不存在的语句了
                    break
                else:
                    # 如果在三次之内输入正确了，把错误次数归零
                    self.var_password_error_times = 0
                    # 把用户名和密码写入list
                    self.current_user_list = self.user_list[index]
                    # 加载主窗体
                    self.load_main()
                    # showinfo("系统消息", "登录成功！")
                    break
            # 如果校验到最后都没有相同的用户名,则用户名不存在
            if index == len(self.user_list) - 1:
                showinfo("系统消息", "输入的用户名不存在")

    def write_file_info(self):
        # 1.清空文件；2.写入
        try:
            with open(file=self.file_path, mode="w") as fd:
                fd.write("")
            with open(file=self.file_path, mode="a") as fd:
                for item in self.user_list:
                    fd.write(",".join(item))
        except:
            showinfo("系统消息", "写入文件出现异常")

    def load_main(self):
        # 关闭当前窗体
        self.destroy()
        # 加载新窗体
        main_window = maingui.MainWindow(self.current_user_list, self.get_now_time())

    def get_now_time(self):
        today = datetime.today()
        return ("%04d-%02d-%02d %02d:%02d:%02d" % (today.year,
                                                   today.month, today.day, today.hour, today.minute, today.second))


if __name__ == '__main__':
    this_login = LoginWindow()
    this_login.mainloop()

