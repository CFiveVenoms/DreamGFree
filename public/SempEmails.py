import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import xlrd
import time
"""
@author : 汤中华
@dection： 测试报告生成后，自动给指定人员发送邮件
"""
def put_Email():
    ###################################################################################################################
    sender = "1194127720@qq.com"  # 发件箱
    # 们用的是QQ邮箱服务器，所以设置为QQ服务器）
    host = "smtp.qq.com"
    # 发件箱服务端口
    port = 465
    Inboxs = ['tangzhonghua@etohui.com','xuejunfeng@etohui.com']  # 格式['1','2'...]
    pwd = "lgnpsbtpwymfffjg"          # 邮箱授权码，不是采用邮箱内容登录的，需要使用授权码登录
    ###################################################################################################################
    # 设置邮件内容 （首先是标题 +  附件报告 + 图片或者表格）
    msg = MIMEMultipart()   # 采用内嵌资源的邮件体
    #设置邮件Header中 发件人
    msg['From'] = sender
    #这是邮件Header中 收件人
    for for_adr in Inboxs:
        msg['To'] = for_adr
    # 设置邮件主题
    msg['Subject'] = "测试报告"
    #设置邮件主体内容
    version = '1.1.1'      # 测试报告版本号
    text = "<html><body>&nbsp;&nbsp;《易通汇测试报告》,这是"+version+"简要概述本次版本测试结果信息，详细内容，请见图<br/><br/>" \
                                                          "<img src='cid:test' />" \
                                                          "</body></html>"
    msgtxt = MIMEText(text,'html','utf-8')   #设置邮件内容主体格式
    msg.attach(msgtxt)
    #设置邮件附件信息，用户添加测试报告xls报告
    xls = MIMEText(open("..\\model\\test_report.xlsx",'rb').read(),'base64','utf-8')
    xls["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字 (必须要加上描述，不然邮件中无法显示附件，并且格式要正确,最好和文件名字格式统一)
    xls["Content-Disposition"] = 'attachment; filename="test_report.xlsx"'
    # 往邮件中添加内容
    msg.attach(xls)

    #设置图片（内嵌在邮件内容中，并非图片附件）
    img = MIMEImage(open('..\\img\\9-160HP91406.jpg','rb').read())
    img.add_header('Content-ID','test')
    msg.attach(img)
    ###################################################################################################################
    start = time.clock()
    # 和服务器创建连接
    connect = smtplib.SMTP_SSL(host,port)
    # 连接成功后，登录邮件服务器
    lg = connect.login(sender,pwd)
    # 登录成功后发送邮件
    connect.sendmail(sender,Inboxs,msg.as_string())
    # 邮件发送完成后关闭和服务器之间的连接
    connect.quit()
    end = time.clock()
    return end - start
def read_xls():
    # 打开文件
    workboot = xlrd.open_workbook(r'..\\model\\test_report.xlsx')
    # 获取sheet1
    sheet_name = workboot.sheet_names()[0]
    # 根据sheet索引或者名称获取sheet内容
    sheet = workboot.sheet_by_name(sheet_name)
    # sheet的名称，行数，列数
    rows = sheet.nrows
    cols = sheet.ncols
    row = sheet.row_values(3) #  获取第四行内容
    col = sheet.col_values(2) # 获取第三列内容
    print(row)
    print(col)
    ####################################################################################################################
if __name__ == '__main__':
    # numbers = put_Email()
    read_xls()


