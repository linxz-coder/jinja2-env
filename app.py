from jinja2 import Environment, FileSystemLoader

import webbrowser
import os

# 设置模板文件的目录
env = Environment(loader=FileSystemLoader('templates'))

template = env.get_template('hello.html')

data = {'name': 'Linxz'}
print(template.render(data))

# 生成html文件
html_content = template.render(data)

# 保存到一个临时文件
with open('output.html', 'w') as file:
    file.write(html_content)

# 在浏览器中打开
webbrowser.open('file://' + os.path.realpath('output.html'))