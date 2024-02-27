import re

str = """**没运行前就提示错误**
<Image
src="/mdpic/image-20231003140558861.png"
width="718"
height="404"
alt="image-20231003140558861.png"
/>

## 非异常故障检测
"""
picpattern = """\<Image[\s\S]*?src=\"/mdpic/(image-.*?)\"[\s\S]*?\/\>"""
# str = re.findall(picpattern,str)

#修改md样式为Next组件
def replacement_function(match):
    image_name = match.group(1)
    return f"""
<MyImage 
src="/mdpic/{image_name}"
alt="{image_name}"
/>
"""
modified_text1 = re.sub(picpattern, replacement_function, str)

print(modified_text1)