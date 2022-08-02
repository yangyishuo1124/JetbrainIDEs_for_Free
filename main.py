import sqlite3
import sys
import time
import pyperclip
import wget
import os
import requests


def 下载(安装包名字: str):
    link = ''
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    name = c.execute('SELECT * FROM 下载源').fetchall()
    for i in name:
        if i[1] == 安装包名字:
            link = i[2]
    os.chdir('./tmp')  # 切换目录
    if not os.path.exists(wget.filename_from_url(link)):
        start = time.time()  # 下载开始时间
        response = requests.get(link, stream=True)
        size = 0  # 初始化已下载大小
        chunk_size = 1024  # 每次下载的数据大小
        content_size = int(response.headers['content-length'])  # 下载文件总大小

        try:
            if response.status_code == 200:  # 判断是否响应成功
                print('开始下载 ' + 安装包名字 + ',[文件大小]:{size:.2f} MB'.format(
                    size=content_size / chunk_size / 1024))  # 开始下载，显示下载文件大小
                filepath = wget.filename_from_url(link)  # 设置图片name，注：必须加上扩展名
                with open(filepath, 'wb') as file:  # 显示进度条
                    for data in response.iter_content(chunk_size=chunk_size):
                        file.write(data)
                        size += len(data)
                        print('\r' + '[下载进度]:%s%.2f%%' % (
                            '>' * int(size * 50 / content_size), float(size / content_size * 100)), end=' ')
            end = time.time()  # 下载结束时间
            print('下载完成!,用时: %.2f秒' % (end - start))  # 输出下载用时时间
        except:
            print('出错了!')

        os.startfile(wget.filename_from_url(link))
    else:

        os.startfile(wget.filename_from_url(link))
        c.close()
    return


def 获取激活码(安装包名字):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    code = ''
    name = c.execute('SELECT * FROM Code').fetchall()
    for i in name:
        if i[1] == 安装包名字:
            code = i[2]
    pyperclip.copy(code)
    c.close()
    return code


def 破解(安装包名字):
    print('运行破解程序需要一些时间，所需时间根据所安装JetBrain IDE的数量决定')
    print('开始破解，期间没有任何提示，请不要关闭程序')
    os.popen('wscript ./Chark/scripts/install-current-user.vbs')
    获取激活码(安装包名字)
    print('\033[0;37;41m下面需要你手动破解，按照提示进行操作\033[0m')
    print('\033[0;33;40m1.打开所安装的IDE\033[0m')
    print('\033[0;33;40m2.进入激活页面\033[0m')
    print('\033[0;33;40m3.选择’Activation code‘\033[0m')
    print('\033[0;33;40m4.按Ctrl+V将激活码粘贴进去（已经将激活码复制到你的剪贴板）\033[0m')
    print('\033[0;33;40m5.点击’Activation‘\n( 如果提示Key is invalid，请重启后再用本程序的获取激活码功能重试\033[0m')
    print('\033[0;33;40m6.破解完成\033[0m')
    return


def 前置():
    print('第一次运行需清除所有激活记录，后面将会自动操作，期间没有任何提示，请勿关闭程序')
    os.popen('wscript ./Chark/scripts/uninstall-current-user.vbs')
    print('完成')


if __name__ == '__main__':
    while True:
        print('欢迎使用JetBrainIDE自动安装器')
        print('''1.一键安装IDE并破解\n2.运行破解脚本\n3.获取激活码''')
        aaa = input('请输入序号:')
        if aaa == '1':
            print('''1.IntelliJ IDEA\n2.PyCharm\n3.PhpStorm\n4.WebStorm\n5.AppCode\n6.DataGrip\n7.Rider\n8.GoLand\n9.RubyMine\n10.CLion''')
            name = input('请输入需要安装的IDE的序号')
            前置()
            字典 = {1: 'IntelliJ IDEA', 2: 'PyCharm', 3: 'PhpStorm', 4: 'WebStorm', 5: 'AppCode ', 6: 'DataGrip',
                    7: 'Rider', 8: 'GoLand', 9: 'RubyMine', 10: 'CLion'}
            if name == '5':
                print('AppCode暂不支持Windows')
                continue
            下载(字典.get(int(name)))
            if input('安装完成输入y并回车') == 'y':
                os.chdir('..')
                破解(字典.get(int(name)))
        if aaa == '2':
            print('''1.IntelliJ IDEA\n2.PyCharm\n3.PhpStorm\n4.WebStorm\n5.AppCode\n6.DataGrip\n7.Rider\n8.GoLand\n9.RubyMine\n10.CLion''')
            name = input('请输入需要安装的IDE的序号')
            字典 = {1: 'IntelliJ IDEA', 2: 'PyCharm', 3: 'PhpStorm', 4: 'WebStorm', 5: 'AppCode ', 6: 'DataGrip',
                    7: 'Rider', 8: 'GoLand', 9: 'RubyMine', 10: 'CLion'}
            破解(字典.get(int(name)))
        if aaa == '3':
            print('''1.IntelliJ IDEA\n2.PyCharm\n3.PhpStorm\n4.WebStorm\n5.AppCode\n6.DataGrip\n7.Rider\n8.GoLand\n9.RubyMine\n10.CLion''')
            name = input('请输入需要获取激活码的IDE的序号')
            字典 = {1: 'IntelliJ IDEA', 2: 'PyCharm', 3: 'PhpStorm', 4: 'WebStorm', 5: 'AppCode ', 6: 'DataGrip',
                    7: 'Rider', 8: 'GoLand', 9: 'RubyMine', 10: 'CLion'}
            print(获取激活码(字典.get(int(name))))
            print('\033[0;37;41m已经复制到剪切板\033[0m')