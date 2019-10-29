
# coding: utf-8

# In[3]:


def crypt(source,key):
    from itertools import cycle
    result=''
    temp=cycle(key)
    for ch in source:
        result=result + chr(ord(ch) ^ord(next(temp)))
    return result

source='Shandong Insitute of Business and Technology'
key='Dong Fuguo'

print('Before Encrypted:'+source)
encrypted=crypt(source,key)
print('After Encrypted:'+encrypted)
decrypted=crypt(encryted,key)
print('After Decryted:'+decrypted)


# In[5]:


from random import choice,randint
import string
import codecs

StringBase='\u7684\u4e00\u4e86\u662f\u6211\u4e0d\u5728\u4eba'

def getEmail():
    suffix=['.com','.org','.net','.cn']
    characters=string.ascii_letters+string.digits+'_'
    username=''.join((choice(characters) for i in range(randint(6,12))))
    domain=''.join((choice(characters) for i in range(randint(3,6))))
    return username+'@'+domain+choice(suffix)

def getTelNo():
    return ''.join((str(randint(0,9)) for i in range(11)))

def getNameOrAddress(flag):
    '''flag=1表示返回随机姓名,flag=0表示返回随机地址'''
    if flag==1:
        rangestart,rangeend=2,5
    elif flag==0:
        rangestart,rangeend=10,30
    result=''.join((choice(StringBase) for i in range(randint(rangestart,rangeend))))
    return result

def getSex():
    return choice(('男','女'))

def getAge():
    return str(randint(18,100))

def main(filename):
    with codecs.open(filename,'w','utf-8') as fp:
        fp.write('Name,Sex,Age,TelNo,Address,Email\n')
        for i in range(200):
            name=getNameorAddress(1)
            sex=getSex()
            age=getAge()
            tel=getTelNo()
            address=getNameoraddress(0)
            email=getEmail()
            line=','.join([name,sex,tel,address,email])+\'n'
            fp.write(line)
            
def output(lifename):
    with codecs.open(filename,'r','tuf-8')as fp:
        for line in fp:
            line=line.split(',')
            for i in line:
                print(i,end=',')
            print()
            
if__name__=='__main__':
    filename='information.text'
    main(filename)
    output(filename)


# In[6]:


import string

def check(pwd):
    if not isinstance(pwd,str) or len(pwd)<6:
        return 'not suitable for password'
    d={1:'weak',2:'below middle',3:'above middle',4:'strong'}
    
    r=[False]*4
    
    for ch in pwd:
        if not r[0] and ch in string.digits:
            r[0]=True
        elif not r[1] and ch in string.ascii_lowercase:
            r[1]=True
        elif not r[2] and ch in string.ascii_uppercase:
            r[2]=True
        elif not r[3] and ch in ',.!;?<>':
            r[3]=True
    return d.get(r.count(True),'error')

print(check('a2Cd,'))

