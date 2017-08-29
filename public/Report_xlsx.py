import xlsxwriter
from time import ctime
workbook = xlsxwriter.Workbook("test_report.xlsx")
#添加工作簿
wooksheet = workbook.add_worksheet("接口测试概览")
wooksheet2 = workbook.add_worksheet("接口测试详情")
def get_sheet1(isert_version,case_count,pass_count,error_count):
    # 设置单元格样式  让表格中的内容上下居中
    wookstyle = workbook.add_format({
        'align': 'center',
        'valign': 'vcenter',
        'border': 1
    })
    book_H1_Style = workbook.add_format({
        'bg_color': '#000080',
        'font_color': '#FFFFFF',
        'align': 'center',
        'valign': 'vcenter',
        'border': 1
    })
    book_H2_Style = workbook.add_format({
        'bg_color': '#FFA500',
        'valign': 'vcenter',
        'border': 1
    })
    titile = workbook.add_format({
        "align": 'center',
        "valign": 'vcenter',
        'border': 1
    })
    ##########################
    # 设置单元格高度
    wooksheet.set_row(0, 26)
    wooksheet.set_row(1, 22)
    wooksheet.set_row(2, 30)
    wooksheet.set_row(3, 30)
    wooksheet.set_row(4, 30)
    wooksheet.set_row(5, 30)
    wooksheet.set_row(6, 22)
    wooksheet.set_row(7, 30)
    wooksheet.set_row(8, 22)
    wooksheet.set_row(9, 30)
    wooksheet.set_row(10, 22)
    wooksheet.set_row(11, 30)
    wooksheet.set_row(12, 30)
    #############################
    # 单元格列的宽度
    wooksheet.set_column("A:A", 12)
    wooksheet.set_column("B:B", 30)
    wooksheet.set_column("C:C", 12)
    wooksheet.set_column("D:D", 30)
    wooksheet.set_column("E:E", 12)
    wooksheet.set_column("F:F", 30)
    ###########################################################
    ## 编写测试报告 表头单元格内容 和 报告样式
    wooksheet.merge_range("A1:F1", '测试报告概览', book_H1_Style)
    wooksheet.merge_range("A2:F2", "应用基本信息", book_H2_Style)
    wooksheet.merge_range("A9:F9", "测试环境设置", book_H2_Style)
    wooksheet.merge_range("A7:F7", "测试基本信息", book_H2_Style)
    wooksheet.merge_range("A11:F11", "测试概况", book_H2_Style)
    ## 设置普通单元格内容
    wooksheet.write("A3", "应用名称", wookstyle)
    wooksheet.merge_range("B3:C3", "", wookstyle)
    wooksheet.write("D3", "应用版本", wookstyle)
    wooksheet.merge_range("A4:A6", "应用更新内容", workbook.add_format({'align': 'center', 'valign': 'vcenter', 'border': 1}))
    wooksheet.write("B4", "新增", titile)
    wooksheet.write("B5", "删除", titile)
    wooksheet.write("B6", "修改", titile)
    ############################################################
    ## 测试基本信息
    wooksheet.write("A8", "测试版本", wookstyle)
    wooksheet.write("C8", "测试平台", wookstyle)
    wooksheet.write("E8", "测试负责人", wookstyle)
    ############################################################
    ## 测试环境设置
    wooksheet.write("A10", "硬件要求", wookstyle)
    wooksheet.write("C10", "软件要求", wookstyle)
    wooksheet.write("E10", "网络环境", wookstyle)
    ############################################################
    ## 测试概况
    wooksheet.write("A12", "接口版本", wookstyle)
    wooksheet.write("C12", "接口总数", wookstyle)
    wooksheet.write("E12", "测试日期", wookstyle)
    wooksheet.write("A13", "通过总数", wookstyle)
    wooksheet.write("B13", "", wookstyle)
    wooksheet.write("C13", "失败总数", wookstyle)
    wooksheet.write("D13", "", wookstyle)
    wooksheet.write("E13", "通过率", wookstyle)
    wooksheet.write("F13", "", wookstyle)
    #####################################################################  应用基本信息
    Version = "V1.0.45"
    product = "《易通汇》"
    wooksheet.merge_range("E3:F3", Version, wookstyle)
    wooksheet.write("B3", product, wookstyle)
    ##################################################################### 版本更新内容
    content = {
        'add': "1、APP整体换肤" \
               "2、登录时密码增加一键清空icon" \
               "3、导航栏不做分隔刷新效果，在导航栏以下查看品种行情时做下拉刷新效果" \
               "4、行情品种前加旗子或其他图标，所有的“美元兑瑞士法郎”改成“美元瑞郎”，“美元兑离岸人民币”改成“美元人民币”，所有品种“兑”字都去掉" \
               "5、加公告栏和弹窗" \
               "6、品种右上角加详情",
        'update': '无',
        'delete': '无'
    }
    # 需要设置自动换行样式
    bank_Style = workbook.add_format({
        'align': 'center',
        'valign': 'vcenter',
        'border': 1
    })
    bank_Style.set_text_wrap()
    wooksheet.merge_range("C4:F4", content['add'], bank_Style)
    wooksheet.merge_range("C5:F5", content['update'], wookstyle)
    wooksheet.merge_range("C6:F6", content['delete'], wookstyle)
    #################################################################### 测试基本信息
    platfrom = 'Android'
    testuser = '薛俊峰'
    wooksheet.write("B8", Version, wookstyle)
    wooksheet.write("D8", platfrom, wookstyle)
    wooksheet.write("F8", testuser, wookstyle)
    ############################################### 测试环境设置
    Hardware = '无'
    software = '无'
    network = 'wifi、4G、3G'
    wooksheet.write("B10", Hardware, wookstyle)
    wooksheet.write("D10", software, wookstyle)
    wooksheet.write("F10", network, wookstyle)
    ############################################### 测试概况
    wooksheet.write("F12", ctime(), wookstyle)
    ######################################################################
    ###     创建测试概览表单，但是会留下格式统计部分信息需要测试结束后写入数据
    # 其中包含 测试用例总数、通过总数 、失败总数
    # B12 接口版本；D12 用例总数 ；B13 通过总数；D13 失败总数；F13 测试通过率
    wooksheet.write("B12",isert_version,wookstyle)
    wooksheet.write("D12",case_count,wookstyle)
    wooksheet.write("B13",pass_count,wookstyle)
    wooksheet.write("D13",error_count,wookstyle)
    #####################################################################
    # 专用测试报告百分比格式
    number_style1 = workbook.add_format({'align':'center','valign':'vcenter','border':1})
    number_style1.set_num_format(0x0a)
    ####################################################################
    wooksheet.write("F13","=B13/D12",number_style1)
    workbook.close()
def get_sheet2():
    return  wooksheet2