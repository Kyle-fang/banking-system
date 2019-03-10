from card import Card
from user import User
import random
class ATM(object):
    def __init__(self,allUser):
        self.allUser = allUser  #卡号--用户

    def createUser(self):
        name = input("请输入您的姓名：")
        idCard = input("请输入您的身份证号码：")
        phone = input("请输入您的电话号码：")

        prestoreMoney = input("请输入您的预存款：")
        if int(prestoreMoney) < 0:
            print("预存款输入有误！开户失败....")
            return -1

        onePasswd = input("请设置密码：")
        #验证密码
        if not self.checkPasswd(onePasswd):
            print("两次输入密码不一致！开户失败....")

        #
        cardstr = self.randomCardId()
        print(cardstr)

        card = Card(cardstr,onePasswd,prestoreMoney)
        user = User(name,idCard,phone,card)

        #存到字典
        self.allUser[cardstr] = user
        print("开户成功！请记住账户： %s "%cardstr)


    def searchUserinformation(self):
        cardNumber = input("请输入您的卡号：")
        '''
        user = self.allUser.get(cardNumber)

        #验证是否存在该卡号
        if not user:
            print("该卡号不存在！！查询失败....")
            return -1

        #判断账号是否被锁定
        if user.card.cardLock:
           print("该账户已被锁定！！，请解锁后在操作.....")
           return -1

        #验证密码
        if not self.checkPasswd(user.card.cardPasswd):
            print("密码输入错误!!该卡已被锁定！请解锁后再进行其他操作.....")
            user.card.cardLock = True
            return -1
        '''
        #用键从字典中取出值赋给变量user，若无匹配的键则返回False
        user = self.allUser.get(cardNumber)
        self.validate(cardNumber,user)
        print("姓名：%s  账号：%s  余额：%s" %(user.name,user.card.cardId, user.card.cardMoney))



    def withDram(self):
        cardNumber = input("请输入卡号：")

        '''
        #判断是否存在该卡号
        user = self.allUser.get(cardNumber)
        if not user:
            print("该卡号不存在！")
            return -1

        #验证密码
        if not self.checkPasswd(user.card.cardPasswd):
            print("密码输入错误！")
            return -1
        '''
        #用键从字典中取出值赋给变量user，若无匹配的键则返回False
        user = self.allUser.get(cardNumber)
        self.validate(cardNumber,user)
        #取钱
        moneyNumber = int(input("请输入你要取出的金额："))
        if moneyNumber>int(user.card.cardMoney):
            print("余额不足！")
            return -1
        user.card.cardMoney = int(user.card.cardMoney)-int(moneyNumber)
        print("操作成功！")



    def Deposit(self):
        cardNumber = input("请输入卡号：")
        '''
        #判断是否存在该卡号
        user = self.allUser.get(cardNumber)
        #判断账号是否被锁定
        if user.card.cardLock:
            print("该账户已被锁定！！，请解锁后在操作.....")
            return -1
        if not user:
            print("该卡号不存在！")
            return -1

        #验证密码
        if not self.checkPasswd(user.card.cardPasswd):
            print("密码输入错误！")
            return -1
        '''
        #用键从字典中取出值赋给变量user，若无匹配的键则返回False
        user = self.allUser.get(cardNumber)
        self.validate(cardNumber,user)
        #存钱
        moneyNumber = input("请输入你要存入的金额：")
        user.card.cardMoney = int(user.card.cardMoney)+int(moneyNumber)
        print("操作成功！")


    def Transfer(self):
        cardNumber = input("请输入卡号：")
        '''
        #判断是否存在该卡号
        user = self.allUser.get(cardNumber)
        #判断账号是否被锁定
        if user.card.cardLock:
            print("该账户已被锁定！！，请解锁后在操作.....")
            return -1
        if not user:
            print("该卡号不存在！")
            return -1

        #验证密码
        if not self.checkPasswd(user.card.cardPasswd):
            print("密码输入错误！")
            return -1
        '''
        #用键从字典中取出值赋给变量user，若无匹配的键则返回False
        user = self.allUser.get(cardNumber)

        self.validate(cardNumber,user)

        #转账
        transferMoney = int(input("请输入转账的金额："))
        if transferMoney>int(user.card.cardMoney):
            print("余额不足！")
            return -1
        #exporter = input("请输入输出者账号：")
        receiver = input("请输入接受者账号：")
        #user2 = self.allUser.get(exporter)
        user1 = self.allUser.get(receiver)
        user.card.cardMoney = int(user.card.cardMoney)-transferMoney
        user1.card.cardMoney = int(user1.card.cardMoney)+transferMoney
        print("操作成功！")


    def Tighten(self):
        cardNumber = input("请输入卡号：")
        '''
        #判断是否存在该卡号
        user = self.allUser.get(cardNumber)
        #判断账号是否被锁定
        if user.card.cardLock:
            print("该账户已被锁定！！，请解锁后在操作.....")
            return -1
        if not user:
            print("该卡号不存在！")
            return -1

        #验证密码
        if not self.checkPasswd(user.card.cardPasswd):
            print("密码输入错误！")
            return -1
        '''
        #用键从字典中取出值赋给变量user，若无匹配的键则返回False
        user = self.allUser.get(cardNumber)

        self.validate(cardNumber,user)

        #改密
        changeKey = input("请输入新密码：")
        user.card.cardPasswd = changeKey
        print("操作成功！")


    def Locking(self):
        cardNumber = input("请输入您的卡号：")
        '''
        # 验证是否存在该卡号
        user = self.allUser.get(cardNumber)
        if not user:
            print("该卡号不存在！！锁定失败....")
            return -1

        if user.card.cardLock:
            print("该卡已被锁定!!请在解锁后使用其他功能.....")
            return -1

        #判断是否锁定
        if user.card.cardLock:
            print("该卡已被锁定！请解锁后再进行其他操作.....")
            return -1


        # 验证密码
        if not self.checkPasswd(user.card.cardPasswd):
            print("密码输入错误!!该卡已被锁定！请解锁后再进行其他操作.....")
            user.card.cardLock = True
            return -1
        '''
        #用键从字典中取出值赋给变量user，若无匹配的键则返回False
        user = self.allUser.get(cardNumber)

        self.validate(cardNumber,user)

        #验证身份证号
        tempIdCard = input("请输入您的身份证号：")
        if tempIdCard != user.idCard:
            print("身份证号输入错误！！锁定失败....")
            return -1

        #锁定
        user.card.cardLock = True
        print("锁定成功！")


    def Deblocking(self):
        cardNumber = input("请输入您的卡号：")
        '''
        # 验证是否存在该卡号
        user = self.allUser.get(cardNumber)
        if not user:
            print("该卡号不存在！！解锁失败....")
            return -1

        #判断是否锁定
        if not user.card.cardLock:
            print("该卡已解锁！")
            return -1

        # 验证密码
        if not self.checkPasswd(user.card.cardPasswd):
            print("密码输入错误!!")
            user.card.cardLock = True
            return -1
        '''
        #用键从字典中取出值赋给变量user，若无匹配的键则返回False
        user = self.allUser.get(cardNumber)

        self.validate(cardNumber,user)

        #验证身份证号
        tempIdCard = input("请输入您的身份证号：")
        if tempIdCard != user.idCard:
            print("身份证号输入错误！！解锁失败....")
            return -1

        #锁定
        user.card.cardLock = False
        print("解锁成功！")

    def Supcard(self):
        cardNumber = input("请输入卡号：")
        '''
        #判断是否存在该卡号
        user = self.allUser.get(cardNumber)
        #判断账号是否被锁定
        if user.card.cardLock:
            print("该账户已被锁定！！，请解锁后在操作.....")
            return -1
        if not user:
            print("该卡号不存在！")
            return -1

        #验证身份证号
        Id = input("请输入身份证号：")
        if Id != user.idCard:
            print("输入错误！")
            return -1

        #验证密码
        if not self.checkPasswd(user.card.cardPasswd):
            print("密码输入错误！")
            return -1
        '''
        #用键从字典中取出值赋给变量user，若无匹配的键则返回False
        user = self.allUser.get(cardNumber)

        self.validate(cardNumber,user)

        #补卡

        newNumber = self.randomCardId()
        self.allUser[newNumber]=user
        self.allUser.pop(cardNumber)
        print("新卡号为：%s"%(newNumber)+'\n'+"操作成功！")




    def Colsing(self):
        ''''
        cardNumber = input("请输入卡号：")
        #判断是否存在该卡号
        user = self.allUser.get(cardNumber)
        #判断账号是否被锁定
        if user.card.cardLock:
            print("该账户已被锁定！！，请解锁后在操作.....")
            return -1
        if not user:
            print("该卡号不存在！")
            return - 1
        # 验证密码
        if not self.checkPasswd(user.card.cardPasswd):
            print("密码输入错误！")
            return -1
        '''
        cardNumber = input("请输入卡号：")
        #用键从字典中取出值赋给变量user，若无匹配的键则返回False
        user = self.allUser.get(cardNumber)
        #验证
        self.validate(cardNumber,user)
        #销户
        self.allUser.pop(cardNumber)
        print("操作成功！")


    #验证密码
    def checkPasswd(self,realPasswd):
        for i in range(3):
            tempPasswd = input("请输入密码：")
            if tempPasswd == realPasswd:
                return True
        return False

    #生成卡号
    def randomCardId(self):
        while True:
            str = ""
            for i in range(6):
                ch = chr(random.randrange(ord('0'),ord('9')+1))
                str += ch
            #判断是否重复
            if not self.allUser.get(str):
                return str



    #验证
    def validate(self,cardNumber,user):
        #用键从字典中取出值赋给变量user，若无匹配的键则返回False
        #user = self.allUser.get(cardNumber)
        # 判断是否存在该卡号
        if not user:
            print("该卡号不存在！")
            return - 1
        #判断账号是否被锁定
        if user.card.cardLock:
            print("该账户已被锁定！！，请解锁后在操作.....")
            return -1

        # 验证密码
        if not self.checkPasswd(user.card.cardPasswd):
            print("密码输入错误！账户已锁定，请解锁后使用！")
            user.card.cardLock=True
            return -1
