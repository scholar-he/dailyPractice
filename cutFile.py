#! /usr/bin/python
# -*-coding:utf8-*-

"""
Author: 
    Tony 2513141027
Date: 
    2020/9/5 15:02 
Description:
    
"""

def cutFile(filePath, count):
    """
        将一个大文件均分为多个文件
    Args:
        filePath (str)：待分割文件路径
        count (int): 分割份数
    Return:
        None
    """
    with open(filePath, "r") as f:
        lines = f.readlines()
        each = len(lines) // count
        for i in range(count):
            eachInfo = lines[i*each: (i+1)*each]
            newFile = "tmp%d.txt" % i
            with open(newFile, "w") as f:
                f.writelines(eachInfo)
        if len(lines) % count != 0:
            newFile = "tmp%d.txt" % (count + 1)
            with open(newFile, "w") as f:
                f.writelines(lines[count*each:])


if __name__ == '__main__':
    path = r"E:\project\Demo\123"
    cutFile(path, 5)
