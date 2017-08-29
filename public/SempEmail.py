# coding:utf-8
import smtplib
from email.mime.text import MIMEText  # 引入smtplib和MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import time
def put_Emal():
    host = 'smtp.qq.com'  # 设置发件服务器地址
    port = 465  # 设置发件服务器端口号。注意，这里有SSL和非SSL两种形式
    sender = '110@qq.com'  # 设置发件邮箱，一定要自己注册的邮箱
    pwd = ''  # 设置发件邮箱的，如果不能直接使用验证码登录，使用邮箱授权密码登录（邮箱 - 设置 - 账号 - 授权码）
    receiver = 'tan@eto.com'  # 设置邮件接收人，可以是扣扣邮箱
    #################################################################################
    message = MIMEMultipart()
    # 邮件正文内容
    message.attach(MIMEText('接口自动化测试报告', 'plain', 'utf-8'))
    message['subject'] = 'Hello world'  # 设置邮件标题
    message['from'] = sender  # 设置发送人
    message['to'] = receiver  # 设置接收人
    # 构造附件1，传送当前目录下的 test.txt 文件
    att1 = MIMEText(open('D:\\PycharmProjects\\etonhui_\\model\\test_report.xlsx', 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att1["Content-Disposition"] = 'attachment; filename="test_report.xlsx"'
    message.attach(att1)
    s = smtplib.SMTP_SSL(host, port)  # 注意！如果是使用SSL端口，这里就要改为SMTP_SSL
    s.login(sender, pwd)  # 登陆邮箱
    s.sendmail(sender, receiver, message.as_string())  # 发送邮件！
    ###############################################################################

def Put_Email():
    host = "smtp.qq.com"    # 发送邮件服务器
    Port = "465"    # 发送端口
    sender = "110@qq.com"    # 发件箱地址
    pwd = "lgnpsbt"        # 发件箱密码  如果为开启stmp服务，需要登录邮箱开启服务、如果开启之后依然报错，需要查看是否使用验证码服务（非登录密码，而是授权码，授权登录）
    reciver  = "tang@etohui.com"   # 收件箱地址,如果是多个用户，采用列表形式，例如： ['1194127720@qq.com','1801716288@qq.com']
    ###################################################################
    fp = open('D:\\PycharmProjects\\etonhui_\\img\\9-160HP91406.jpg','rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    msgImage.add_header('Content-ID','test')
    msgRoot = MIMEMultipart()
    msgRoot['subject'] = '接口自动化测试报告' # 邮件标题
    msgRoot['from'] = sender
    msgRoot['to'] = reciver
    content = MIMEText('<pre>这是一封测试邮件，主要是为了配置邮件标题，邮件内容图片和表格，同时呢为了检查邮件内容格式，有一种办法内就是通过发送邮件后，<br/>然后查看源代码，看看内容格式是什么'
                       '然后再拷贝其中的内容，添加至邮件中，看看结果</pre><img src="cid:test">','html','utf-8')
    msgRoot.attach(content)
    msgRoot.attach(msgImage)
    start = time.clock()
    s = smtplib.SMTP_SSL(host,Port)   # 和发送邮件服务器创建连接
    s.login(sender,pwd)               # 发件箱的账号和密码，模拟用户登录
    s.sendmail(sender,reciver,msgRoot.as_string())      # 发件箱，收件箱
    end = time.clock()
    hours = end - start
    return hours

if __name__ == '__main__':
    hours = Put_Email()
    print("发送邮件执行了：%f s" % hours)
