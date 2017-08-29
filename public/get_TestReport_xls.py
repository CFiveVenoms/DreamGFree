import xlsxwriter
def get_testReport_xls(Object):
    # 设置测试报表头部样式

    head_style = {
        'align':'center',
        'valign':'vcenter',
        'bold':True,
        'border':1,
        'fg_color':'#EE6A50',
    }
    title_style = {
        'align':'center',
        'valign':'vcenter',
        'bold':True,
        'border':1,
        'fg_color':'#EE6A50',
    }
    content_style = {
        'align':'right',
        'valign':'vcenter',
        'border':1
    }
