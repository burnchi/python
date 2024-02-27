import mysql.connector
import requests
from lxml import etree
import re
import os
#
# cnx = mysql.connector.connect(user='root', password='root',
#                               host='127.0.0.1',
#                               database='books')
# cursor = cnx.cursor()
#
# cursor.execute("SELECT image_url FROM xuanhuan_books")
#
# result = cursor.fetchall()
# print(result[:10])
# print(len(result))
root_dir = '/home/burnchi/Pictures/novelfengmian'
root_dir1 = '/home/burnchi/Pictures/'

# true
# for i in result:
#     image_url = i[0]
#     with open(root_dir1 + 'book1.txt', 'a') as f:
#         f.write(image_url+'\r\n')

# false
# with open(root_dir1 + 'book.txt', 'r') as f:
#     result = f.readlines()
# print(result)


# strip repeat
# def remove_duplicates(input_file, output_file):
#     lines_seen = set()  # 用于存储已出现的行
#     with open(input_file, 'r') as file_in, open(output_file, 'w') as file_out:
#         for line in file_in:
#             line = line.strip()  # 去除行尾的换行符和空白字符
#             if line not in lines_seen:
#                 file_out.write(line + '\n')  # 将不重复的行写入输出文件
#                 lines_seen.add(line)  # 将行添加到集合中
#
# # 示例用法
# input_file = root_dir1+'book.txt'  # 输入文件名
# output_file = 'output.txt'  # 输出文件名
# remove_duplicates(input_file, output_file)


# true
# cursor.close()
# cnx.close()

# true
# for i in result:
#     # image_url = i[0]
#     image_url = i.strip()
#     # print(image_url)
#     # handle url: default image will skip
#     if image_url == "img.uukanshu.net/static/www/images/fengmian.jpg":
#         continue
#     #
#     try:
#         # re.find url suffix
#         relative_path = re.findall(r"(/\d{4}.*?$)", image_url)[0]
#         image_name = relative_path.split('/')[-1]
#         directory_name = re.findall(f"(^.*?)/{image_name}$", relative_path)[0]
#         absolute_path = root_dir + directory_name
#
#         # /2023/9/638291836115274765.jpg 638291836115274765.jpg /2023/9
#         # print(relative_path, image_name, directory_name, absolute_path)
#         # create directory
#         if not os.path.exists(absolute_path):
#             os.makedirs(absolute_path)
#             print(f'[+] {absolute_path} is created !!')
#
#         # request image content
#         pic_content = requests.get(
#             "https://" + image_url, headers={'Connection': 'close'}, verify=False)
#         with open(absolute_path + '/' + image_name, 'wb') as f:
#             f.write(pic_content.content)
#             print(f'[+] {image_name}下载完毕')
#     #
#     #     #
#     except Exception as e:
#         print(e)
