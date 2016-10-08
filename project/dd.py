import re

str1='index.php?0=&152821968=&User_Data%2Fimages%2Fcollapse_gif=&attach_external_tab=&page=7'
str2='index.php?hash=3e412c1c075a8d3ca7afc8d74831dde095d246a4&page=122'
str3='index.php?from=androidqq&originuin=1659615656&uin=903816371&page=11'
str4='index.php?0=&106312512=&4=&attach_external_tab=&page=4'
ma1=re.match(r'index.php?.*&page=[1-9]?\d$',str4)
ma1.group()
ma2=re.match(r'index.php\?.*&page=[1-9]?\d?\d$',str2)
ma2.group()