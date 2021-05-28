import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time
#密文输入密码
from getpass import getpass


def email():
    try:
        #这两个参数必须要，不然就会出现554的错误，不然少参数
        msg['from']=sender
        msg['to']=receiver
        #连接发送邮箱
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login(user,password)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()
        print("第",i,"次发送，成功!")
        time.sleep(2)
    except:
        print("第",i,"次发送，失败!")
        time.sleep(2)


#发送邮箱服务器
smtpserver = "smtp.sina.com"
#发送邮箱的账号/密码
user= input("请输入你的新浪邮箱账号:")
#password=input("请输入密码:")
#以密文的方式输入
password=getpass("请输入你的密码:")
#发送邮箱
sender=user
#收件箱
receiver =input("请输入收件人邮箱:")
#发送主题
subject = input("请输入邮件的主题:")
#编写HTML类型的邮件正文
zw=str(input("请输入邮件内容:"))
msg = MIMEText(zw,"plain","utf-8")
msg['Subject'] = Header(subject, 'utf-8')

while True:
    try:
        n=input("请输入发送次数")
        n=int(n)
        break
    except:
        print("请输入你要发送的次数，必须是正整数~")

i=1
while i<=n:
    email()
    i +=1
print("执行完毕")


"""zmail 仅支持 Python3, pip3 install zmail 
相比 zmail，yagmail 实现发送邮件的方式更加简洁优雅,pip3 install yagmail 
"""