import re
file=open('data.txt')
data={}
for line in file:
    line=line.strip()
    #print(line)
    part=re.findall('[A/ca/cA/C]+[ ]+[NoNO]+\.[A-Za-z0-9]+',line)
    part1=re.findall('[creditedCreditedCREDITED]+[ ]+[a-zA-z]+[ ]+[rsRsRS]+\.[0-9]+',line)
    part2=re.findall('[AVBL]+[ ]+[bal]+[ ]+[is]+[ ]+[rsRsRS]+\.[0-9]+',line)
#from ICIC A/c linked to example@com(UPI RefNo: 1000000000000)
    part3=re.findall('[from]+[ ]+[A-Za-z]+[A/cA/Ca/c]+[ ]+[a-zA-z]+[ ]+[a-zA-z]+[ ]+[a-zA-z]+@[a-z]',line)
    part4=re.findall('[UPIupiUpi]+[ ]+[A-Za-z]+[:]+[0-9]+',line)
    if part:
        p=part[0]
        k=list(p.split())
        data['Account']=(k[-1])
    if part1:
        p=part1[0]
        k=list(p.split())
        data['Credit Balance']=(k[-1])
    if part2:
        p=part2[0]
        k=list(p.split())
        data['Available Balance']=k[-1]
    if part3:
        p=part3[0]
        k=list(p.split())
        data['From Account']=k[-1]
    if part4:
        p=part4[0]
        k=list(p.split())
        data['UPI']=k[-1]
for i in data:
    print(i,":",data[i])

