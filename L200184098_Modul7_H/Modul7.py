##1

import re
f = open('Indonesia.txt','r', encoding='latin1')
p = r'me[\w\.-]+'
string = re.findall(p, f.read())
print(string)
print ("_____________________________________________")


###2

import re

f = open('Indonesia.txt', 'r', encoding='latin1')
p = r'di[\w\.-]+'
string = re.findall(p, f.read())
print(string)
print ("_____________________________________________")


###3

import re

f = open('Indonesia.txt', 'r', encoding='latin1')
r = r'di\s[\w\.-]+'
string3 = re.findall(r, f.read())
print(string3)
print ("_____________________________________________")



###4

import re
f = open('KEI.html', 'r', encoding='latin1')
teks = f.read()
strings = re.findall(r'title="([\w+]+)">', teks)
strings= re.findall(r'">([\w+]+)</a></td>\n<td>([0-9.]+)</td>', teks)
x = []
for y in strings:
    x.append((y[0], float(y[1])))

print(x)
