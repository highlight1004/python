import re
s='''我的电子邮件tom@gmail.com. 
将什么发送到jerry123@163.com或者3123432@qq.com.
若遇特殊情况打电话给182123445678.'''
email1=re.search(r'[\w-]+(\.[\w-]+)*@[\w-]+(\.[\w-]+)+',s,re.A)
print('邮箱1：',email1)
email2=re.search(r'[\w-]+(\.[\w-]+)*@?163.com',s,re.A)
print('邮箱2：',email2)
email3=re.search(r'[\w-]+(\.[\w-]+)*@?qq.com',s,re.A)
print('邮箱3：',email3)
phone=re.search(r'(\d+){12}',s)
print('电话号码：',phone)
