import os
import re
import time

file_path = r'E:\vscodecode\python\文件操作\1.txt'
# 获取md中图片样式
picpattern = "!\[.*?\]\(E:\\\\mdpic\\\\(.*?)\)"

#修改md样式为Next组件
def replacement_function(match):
    image_name = match.group(1)
    return f"""<Image
src="/mdpic/{image_name}"
width="1920"
height="1080"
alt="{image_name}"
quality={100}
className='w-full'
/>
"""

try:
    # 逐个打开并读取内容
    with open(file_path, "r",encoding="utf-8") as file:
        file_content = file.read()
    
    # 找到md中图片样式后替换成Next组件
    if re.findall(picpattern,file_content):
        print('isHere')

        modified_text = re.sub(picpattern, replacement_function, file_content)

        # 写入文件
        with open(file_path, "w",encoding="utf-8") as file:
            file.write(modified_text)
            print(f"{file_path} 写入成功")

        time.sleep(0.5)
    print()
except Exception as e:
    print("发生了异常:", e)
