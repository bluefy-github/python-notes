# coding=utf-8
import sys
import locale

s = "小甲"

print('s:', s)
print('解释器默认解码方式:', sys.getdefaultencoding())
print('本地解码方式:', locale.getdefaultlocale())

with open("01_default.txt", "w") as f:
    f.write(s)
with open("01_utf.txt", "w", encoding="utf-8") as f:
    f.write(s)  # 只有这个文件中的文字是正常的
with open("01_gbk.txt", "w", encoding="gbk") as f:
    f.write(s)
with open("01_jis.txt", "w", encoding="shift-jis") as f:
    f.write(s)
