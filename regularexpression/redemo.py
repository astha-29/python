import re
str="take up 1-3-2019 One idea.One at a time 12-11-2020"
result=re.search(r'o\w\w',str)
print(result)



result=re.findall(r'o\w\w',str)
print(result)


result=re.match(r't\w\w',str)
print(result.group())


result=re.split(r'\d+',str)
print(result)

result=re.sub(r'one','two',str)
print(result)

result=re.findall(r'O\w{1}',str)
print(result)


result=re.findall(r'\d{1,2}-\d{1,2}-\d{4}',str)
print(result)



result=re.search(r'^t\w*',str)
print(result.group())

