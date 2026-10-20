import re

# TASK 1
file1 = open('task1-en.txt').read()


r1 = re.findall(r'[a-zA-Z]+e ', file1)
r1_2 = re.findall(r'\([0-9]+\)', file1)
r1 = [r1[i][:-1] for i in range(len(r1))]


# print(r1)
# print(r1_2)

# TASK 2
file2 = open('task2.html').read()
r2 = re.findall(r'[0-9]+x[0-9]+', file2)

# print(r2)

# TASK 3
file3 = open('task3.txt').read()
file3 = file3.replace(' ', '  ')
id = re.findall(r' [0-9]+ ', file3)
surname = re.findall(r' [a-zA-Z]+ ', file3) 
email = re.findall(r'[0-9]*[a-z]+[0-9]*@[a-z\-]+\.[a-z]+', file3) 
registration_date = re.findall(r'[0-9]{4}-[0-9]{2}-[0-9]{2}', file3)
site = re.findall(r'https?://[^\s]+/', file3)

# output = open('result.csv', 'w')
# output.write(f"ID;SURNAME;EMAIL;REGISTRATION DATE;SITE\n")
# for i in range(250):
#     output.write(f"{id[i]};{surname[i]};{email[i]};{registration_date[i]};{site[i]}\n")
# output.close()

# ADDITIONAL TASK 

fileadd = open('task_add.txt').read()

dates = re.findall(r' [0-9]{2,4}[-/.]{1}[0-9]{2,4}[-/.]{1}[0-9]{2,4}', fileadd)
emails = re.findall(r'[a-zA-Z0-9]+@[a-z]+\.[a-z]+', fileadd)
sites = re.findall(r'https?://[a-zA-Z0-9]+\.[a-z]+', fileadd)

# print(dates)
# print(emails)
# print(sites)
