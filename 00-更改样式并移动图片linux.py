import os
import re
import time
import shutil

# 替换成项目文章路径
root_folder =  r"/home/burnchi/NextjsProject/my-next-blog/posts" + '/'  
# typora存放图片的路径
pic_source_folder = r"/home/burnchi/mdpic" + '/'
# 将typora图片复制到的路径
pic_dest_folder = r"/home/burnchi/NextjsProject/my-next-blog/public/mdpic" + '/'
file_list = []
pic_list = []
# 匹配md中的图片
picpattern = "!\[.*?\]\(/home/burnchi/mdpic/(.*?)\)"
picpattern1 = r"""<img src="/home/burnchi/mdpic/(.*?)".*?/>"""
# 匹配自定义组件的src
picpattern2 = """\<MyImage[\s\S]*?src=\"/mdpic/(image-.*?)\""""


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

# 检查路径是否存在
if not os.path.exists(pic_dest_folder):
    # 如果不存在，则创建文件夹
    os.makedirs(pic_dest_folder)
    print(f"文件夹 '{pic_dest_folder}' 已创建。")
else:
    print(f"文件夹 '{pic_dest_folder}' 已存在。")


# 遍历所有文件的路径更改样式
for file_path in file_list:
    try:
        # 逐个打开并读取内容
        with open(file_path, "r",encoding="utf-8") as file:
            file_content = file.read()
        
        str = re.findall(picpattern,file_content)
        str1 = re.findall(picpattern1,file_content)
        if  str or str1:
            # 找到md中图片样式后替换成Next组件
            modified_text1 = re.sub(picpattern, replacement_function, file_content)
            modified_text2 = re.sub(picpattern1, replacement_function, modified_text1)

            # 写入文件
            with open(file_path, "w",encoding="utf-8") as file:
                file.write(modified_text2)
                print(f"{file_path} 改写组件成功")

            time.sleep(0.2)

            # 找到图片信息,截取image-20231027230732133.png这部分
            # src="/mdpic/image-20231027230732133.png"
            pic = re.findall(picpattern2,modified_text2)
            if pic:
                pic_list += pic
            
    except Exception as e:
        print("发生了异常:", e)

# 拿图片名列表拼接图片路径
# print(pic_list)
for i in pic_list:
    pic_s_path = pic_source_folder + i
    pic_d_path = pic_dest_folder + i
    # 将所有读到的图片路径复制到项目中
    # print(pic_s_path)
    try:
        # 如果目的有图片就不移动图片
        if not os.path.exists(pic_d_path):
            shutil.copy(pic_s_path, pic_d_path)
            print(i,"图片已复制到",pic_dest_folder)
    except Exception as e:
        print("发生了异常:", e) 
    time.sleep(0.2)

