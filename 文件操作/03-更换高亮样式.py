import os
import re
import time

# 替换成你的根文件夹路径
root_folder =  r"E:\next-blog\10-21-blog1\posts" + '\\'  
file_list = []
# 获取md中图片样式
highlightpattern = "==(.*?)=="

#修改md样式为Next组件
def replacement_function(match):
    htext = match.group(1)
    return f"""<HighlightEle>{htext}</HighlightEle>"""

# 收集根目录下的所有文件路径
for root, dirs, files in os.walk(root_folder):
    for file in files:
        file_path = os.path.join(root, file)
        file_list.append(file_path)

# 遍历所有文件的路径
for file_path in file_list:
    # print(file_path)
    try:
        # 逐个打开并读取内容
        with open(file_path, "r",encoding="utf-8") as file:
            file_content = file.read()

        if re.findall(highlightpattern,file_content):
            print(file_path,'存在',highlightpattern)
            modified_text = re.sub(highlightpattern, replacement_function, file_content)
            # 写入文件
            with open(file_path, "w",encoding="utf-8") as file:
                file.write(modified_text)
                print(f"{file_path} 写入成功")
            print('-' * 50)
            time.sleep(0.5)
            continue

        print(file_path,'不存在',highlightpattern)
        
    except Exception as e:
        print("发生了异常:", e)
