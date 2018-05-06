import os

with open("/Users/zhouang/Desktop/my_file.txt", 'r', encoding="UTF-8") as f:
    lines = [(f.tell(), f.readline()) for i in range(10)]   #重点 .
    for line in lines:
        print(line)

import os
f=open("/Users/zhouang/Desktop/my_file.txt", 'w', encoding="UTF-8")
f.write("你好")  #此时并没有真正写入,只在缓存中,且把原文件已经清空
f.flush()  #重点 此时才真正写入额