import time
class Admin(object):
    #def __init__(self,admin,passKey):
    #   self.__admin = admin
    #   self.__passKey = passKey
    admin='1'
    passKey='123'

    def printAdminView(self):
        print("***************************************************************")
        print("*                                                             *")
        print("*                                                             *")
        print("*                       欢迎使用杰哥银行                        *")
        print("*                                                             *")
        print("*                                                             *")
        print("***************************************************************")

        '''
        inputAdmin= input("请输入管理员账号：")
        if self.admin != inputAdmin:
            print("账号输入错误")
            return -1
        inputPassKey = input("请输入管理员密码：")
        if self.passKey != inputPassKey:
            print("密码输入有误")
            return -1
        #能执行到这里说明密码输入正确
        print("登入成功！请稍后....")
        time.sleep(3)
        return 0
        '''

    def printSystemFunctionView(self):
            print("***************************************************************")
            print("*      开户（open）          查询（search）                     *")
            print("*      取款（withdram）      存款（deposit）                    *")
            print("*      转账（transfer）      改密（tighten）                    *")
            print("*      锁定（locking）       解锁（deblocking）                 *")
            print("*      补卡（Supcard）       销户（colsing）                    *")
            print("*                                                             *")
            print("*                   退出（quit）                               *")
            print("***************************************************************")

    def adminLogin(self):
        inputAdmin= input("请输入管理员账号：")
        if self.admin != inputAdmin:
            print("账号输入错误")
            return -1
        inputPassKey = input("请输入管理员密码：")
        if self.passKey != inputPassKey:
            print("密码输入有误")
            return -1
        #能执行到这里说明密码输入正确
        print("登入成功！请稍后....")
        time.sleep(1)
        return 0


    def adminoption(self):
        inputAdmin= input("请输入管理员账号：")
        if self.admin != inputAdmin:
            print("账号输入错误")
            return -1
        inputPassKey = input("请输入管理员密码：")
        if self.passKey != inputPassKey:
            print("密码输入有误")
            return -1
        #能执行到这里说明密码输入正确
        print("已退出！感谢使用！")
        time.sleep(1)
        return 0
