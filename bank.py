'''
人:
类名：user
属性：姓名，身份证号，电话号，卡
行为（方法）：

银行:
类名：bank
属性:用户列表，提款机

卡:
类名：card
属性：卡号，密码，余额，锁定
行为：

取款机:
类名：ATM
属性：
行为：开户， 查询，取款，存款，转账，改密，锁定，解锁，补卡，销户，退出

管理员:
类名：admin
属性：
行为：管理员界面，管理员登入，管理员操作，系统功能界面，退出
'''

import time
from admin import Admin
from atm import ATM
import pickle
import os
def main():

    #界面对象
    view = Admin()
    view.printAdminView()

    #管理员开机
    #if view.printAdminView():
    if view.adminLogin():
        return -1
    #view.printSystemFunctionView()

    #储存所有用户的信息
    allUserInformation = {}

    #提款机对象

    path = 'E:\pycharm project\Tkinter1/allUser.txt'
    file2 = open(path,"rb")
    alluser = pickle.load(file2)
    #print("***********")
    #print(alluser)
    atm = ATM(alluser)



    while True:
        view.printSystemFunctionView()
        time.sleep(1)
        #等待用户的操作
        option = input('请输入您的操作：')
        if option =='open':
            atm.createUser()
        elif option == 'search':
            atm.searchUserinformation()
        elif option == 'withdram':
            atm.withDram()
        elif option == 'deposit':
            atm.Deposit()
        elif option == 'transfer':
            atm.Transfer()
        elif option == 'tighten':
            atm.Tighten()
        elif option == 'locking':
            atm.Locking()
        elif option ==' deblocking':
            atm.Deblocking()
        elif option == 'supcard':
            atm.Supcard()
        elif option == 'colsing':
            atm.Colsing()
        elif option == 'quit':
            if not view.adminoption():
                #将当前系统中的用户信息保存到文件中
                absPath = os.getcwd()
                filePath = os.path.join(absPath,'allUser.txt')
                print(filePath)
                file = open(filePath,"wb")
                pickle.dump(atm.allUser,file)
                file.close()
                return -1

        time.sleep(1)



if __name__ =="__main__":
    main()
