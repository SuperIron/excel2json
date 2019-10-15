import xlrd
import xlwt
import json


def getConfig():
    config = json.load(open('./config.json', 'rb+'))

    return config


def handleExcelData(config):
    # 打开excel文件读取数据
    excel = xlrd.open_workbook(config['input'])

    sheets = excel.sheets()     # 获取所有sheets
    sheet = sheets[0]           # 也可以通过下标去访问某个具体的sheet

    # 获取sheet中行数和列数
    nrows = sheet.nrows
    ncols = sheet.ncols

    print('对应sheet：%s，行数：%d行，列数：%d列' % (sheet.name, nrows, ncols))

    fields = config['fields']   # 获取json数据的字段
    index = config['index'] or 'false'   # 是否添加索引

    items = []
    for i in range(1, nrows):

        item = {}

        if index == 'true':
            item['index'] = i - 1

        for idx, field in enumerate(fields):
            item[field] = sheet.cell(i, idx).value

        items.append(item)

    return json.dumps(items, ensure_ascii=False, indent=4)


def saveJson(info, fileName):
    fp = open(fileName + ".json", "w+b")
    fp.write(info.encode('utf8'))
    fp.close()


if __name__ == '__main__':

    config = getConfig()

    _input = config['input']
    _output = config['output'] or './'

    if not _input:

        print('input -- 不能为空')
    else:
        execlData = handleExcelData(config)
        saveJson(execlData, config['output'])

        print('导出成功')
