# FileNameTools
文件名修改工具


## 环境配置

### Windows
1. 先安装Python运行环境[http://www.cnblogs.com/feeland/p/4345104.html]

>最好 3.0 以上版本

### Mac自带Python2.7


## 使用
### 打开脚本编辑:

1. 运行脚本的目标目录(文件夹)
```
ROOT_PATH = <<你的文件夹路径>>
```

2. 过滤条件
```
# 筛选文件名  正则  如果只要.png的 正则  ".*?\.png$" 匹配才会保留
PATTERN = ".*?\.png$"
# 如果没有则略过匹配
PATTERN = ""
```

3. 使用默认的内置功能

```
#1.rm:"文件名去除一部分",注意不包括后缀
#    1   参数携带  fromIndex,len,
#        例子: ["rm",0,10]  删除 从 0 开始 删除 10 个长度
#    1   参数携带  str
#        例子: ["rm","123"]  删除出现的 "123"


# 2.rep:"替换",注意不包括后缀
#   1   参数携带  fromStr,toStr
#       例子: ["rep","123","321"] 将 123 替换成 321
#   2   参数携带  strIndex,len,toStr
#       例子: ["rep",1,3,"321"] 将 1开始三个长度的 替换成 "321"
#       例子: ["rep",1,0,"321"] 将 1开始0个长度的 替换成 "321" 也就是"123"插入到1处

::可选[删除数量,默认1,最后添加就行,不添加也行]
"""

FUNCTION = ["rep","AA","CC"]  # 将文件名中的 AA 替换成 CC

```

4. 使用自定义的也可以

```
#自定义 使用自定义的反回newNameList,则忽略 FUNCTION 字段
def func_custom(list):
    """
    :param list: oldList
    :return: newNameList or None
    """

    return None

```


5. 执行脚本
  1. Windows 脱到 cmd 中即可
  2. Mac 添加权限 `chmod  777 file_name_tool.py`, 运行 `./file_name_tool.py`
