#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import os.path
import re
import sys

#################     配置  ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  #######################
###  help ->> https://github.com/Rdxer/FileNameTools  

ROOT_PATH =  "" 
PATTERN = ".*?\.ass$"
FUNCTION = ["rep","A","b"]


"""
默认内置功能


1.rm:"文件名去除一部分",注意不包括后缀
    1   参数携带  fromIndex,len,
        例子: ["rm",0,10]  删除 从 0 开始 删除 10 个长度
    1   参数携带  str
        例子: ["rm","123"]  删除出现的 "123"


# 2.rep:"替换",注意不包括后缀
#   1   参数携带  fromStr,toStr
#       例子: ["rep","123","321"] 将 123 替换成 321
#   2   参数携带  strIndex,len,toStr
#       例子: ["rep",1,3,"321"] 将 1开始三个长度的 替换成 "321"
#       例子: ["rep",1,0,"321"] 将 1开始0个长度的 替换成 "321" 也就是"123"插入到1处

::可选[删除数量,默认1,最后添加就行,不添加也行]
"""

IS_INCLUDE_DIR = False

#自定义 使用自定义的反回newNameList,则忽略 FUNCTION 字段
def func_custom(list):
    """
    :param list: oldList
    :return: newNameList or None
    """

    return None



#################     配置 ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑   #######################

############################################################
##################   录入rootpath    #######################
############################################################

def input_file_path():
    """
    让用户输入一个路径
    :return:  路径 or None
    """
    if sys.version_info < (3,0):
        file_path = raw_input("你选择要修改的路径(默认当前脚本所在的目录)")
    else:
        file_path = input("你选择要修改的路径(默认当前脚本所在的目录):")+""
    file_path = file_path.lstrip()
    file_path = file_path.rstrip()

    if file_path != "":
        return file_path
def need_file_path():
    """
    用户输入一个路径否则,输入错误重复输入,为空则使用当前脚本路径
    :return:
    """
    file_path = None

    while file_path == None:
        file_path = input_file_path()
        if file_path == None:
            print("使用当前目录...")
            return os.path.split(os.path.realpath(__file__))[0]
        elif os.path.isdir(file_path):
            return file_path
        else:
            print("输入的不是目录...")
            file_path = None

############################################################
###################    内置功能   ###########################
############################################################


def func_rm(list,startIndedx=0,len=0,str=None,count=1):
    res = []

    if str != None:
        for file_name in list:
            file_name1,file_postfix = os.path.splitext(file_name)
            file_name1 = file_name1.replace(str,"",count)
            res.append(file_name1+file_postfix)

        return res

    for file_name in list:
        file_name1,file_postfix = os.path.splitext(file_name)
        file_name1 = file_name1[:startIndedx] + file_name1[startIndedx+len:]
        res.append(file_name1+file_postfix)

    return res

def func_rep(list,startIndedx=0,len=0,fromStr=None,toStr=None,count=1):
    res = []

    if fromStr != None:
        for file_name in list:
            file_name1,file_postfix = os.path.splitext(file_name)
            file_name1 = file_name1.replace(fromStr,toStr,count)
            res.append(file_name1+file_postfix)

        return res

    for file_name in list:
        file_name1,file_postfix = os.path.splitext(file_name)
        file_name1 = file_name1[:startIndedx]+ toStr + file_name1[startIndedx+len:]
        res.append(file_name1+file_postfix)

    return res


############################################################
###################      run     ###########################
############################################################


if __name__=="__main__":

    if ROOT_PATH == "" or ROOT_PATH == None:
       ROOT_PATH = need_file_path()
    root,dirs,files = next(os.walk(ROOT_PATH))

    if IS_INCLUDE_DIR:
        targer_all = dirs + files
    else:
        targer_all = files

    if PATTERN != "":
        targer_all = filter(lambda str:(re.match(PATTERN,str) != None),targer_all)
        targer_all = list(targer_all)

    targer_all.sort()

    res = func_custom(targer_all)

    if res == None:
        if FUNCTION[0] == "rm":

            if type(FUNCTION[1]) is int:
                res = func_rm(targer_all,startIndedx=FUNCTION[1],len=FUNCTION[2])
            else:
                res = func_rm(targer_all,str=FUNCTION[1])

        elif FUNCTION[0] == "rep":
            if type(FUNCTION[1]) is int:
                res = func_rep(targer_all,startIndedx=FUNCTION[1],len=FUNCTION[2],toStr=FUNCTION[3])
            else:
                res = func_rep(targer_all,fromStr=FUNCTION[1],toStr=FUNCTION[2])
        else:
            exit("设置的内置功能的参数出错...")


    target = []

    for index in range(len(res)):
        target.append((targer_all[index],res[index]))

    # print(target)

    print('''############################################################
############################################################
    ''')
    print("最后生成:")
    for item1,item2 in target:
        print(item1+" ==>> "+item2)

    print('''>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    ''')

    if sys.version_info < (3,0):
        f = raw_input("输入(YES)确认:")
    else:
        f = input("输入(YES)确认:")

    if f.upper() != "YES":
        exit("未输入(YES)中止运行~")

    for item1,item2 in target:
        old = os.path.join(root,item1)
        new = os.path.join(root,item2)
        if old == new:
            continue
        flag = None
        while True:
            if os.path.exists(new):
                if flag == None:
                    flag = item2
                fileName1,postfix = os.path.splitext(item2)
                item2 = fileName1+"-"+postfix
                new = os.path.join(root,item2)
            else:
                if flag != None:
                    print("名字重复:"+item1+"(原文件名):"+flag+"(需要改成的文件名) => "+item2 +"最终文件名")
                    flag = None
                break

        os.rename(old,new)

    print('''修改完毕!''')

    print('''------------------------------------------------''')
