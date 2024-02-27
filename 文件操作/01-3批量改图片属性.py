import os
import re
import time

"""
<Image
src="/mdpic/image-20231003140558861.png"
width="718"
height="404"
alt="image-20231003140558861.png"
/>

----------->
<MyImage 
src="/mdpic/{image_name}"
alt="{image_name}"
/>
"""


# 替换成项目文章路径
root_folder =  r"E:\next-blog\10-21-blog1\posts" + '\\'  
file_list = []
# 匹配md中图片
picpattern = """\<Image[\s\S]*?src=\"/mdpic/(image-.*?)\"[\s\S]*?\/\>"""

#修改md样式为Next组件
def replacement_function(match):
    image_name = match.group(1)
    return f"""
<MyImage 
src="/mdpic/{image_name}"
alt="{image_name}"
/>
"""

# 收集文章路径下的所有文件路径
for root, dirs, files in os.walk(root_folder):
    for file in files:
        file_path = os.path.join(root, file)
        file_list.append(file_path)
# print(file_list)

# 遍历所有文件的路径
for file_path in file_list:
    try:
        # 逐个打开并读取内容
        with open(file_path, "r",encoding="utf-8") as file:
            file_content = file.read()
        
        # 找到md中图片样式后替换成Next组件
        modified_text1 = re.sub(picpattern, replacement_function, file_content)

        # 写入文件
        with open(file_path, "w",encoding="utf-8") as file:
            file.write(modified_text1)
            print(f"{file_path} 写入成功")

        time.sleep(0.5)
    except Exception as e:
        print("发生了异常:", e)





