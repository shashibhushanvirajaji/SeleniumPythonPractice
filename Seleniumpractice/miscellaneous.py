from datetime import  datetime


print(datetime.now())
str = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
str1 = str.replace('/','_').replace(',','_').replace(' ','_').replace(':','_')
print(str1)
