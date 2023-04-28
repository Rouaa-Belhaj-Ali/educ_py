import os
import re 
sh =  input("enter Hours:")
sr = input("Enter Rate: ")
fh = float(sh)
fr  = float(sr)

#print (fh, fr)
if fh > 40 :
    print("Overtime")

else :
    
    print("Regular ")

xp = fh * fr
print ("Pay",xp)

big = max('rouaa')
print(big)

zork = 0

print("Before", zork)
for thing in ['lolo','loko','toto','roro','wiwi','eleo'] :
   
    print(  thing)
print('After', zork)

stuff = list()
stuff.append('book')
stuff.append('bella')

stuff.append('cookie')
stuff.sort()
print(stuff) 
abc = 'with three words'
s = abc.split()
print(s)
print(len(s))
words = 'His e-mail is q-lar@freecodecamp.org'
pieces = words.split()
parts = pieces[3].split('-')
n = parts[1]
print(n)
x =4 
x = 5
prse = dict()
prse['money'] = 12
prse['candy'] = 3
prse['tissues'] = 48
print(prse)
my_dict = {"key1":"value1","key2":"value2","key3":"value3"}
for key, value in my_dict.items():
    print(key, value)

# Dictionnaire and loops 

counts = dict()
print('Enter a line of text :')
line = input('')
words = line.split()
print('Words', words )

print('Counting....')
for word in words:
    counts[word] =+ counts.get(word,0) + 1
print('Counts', counts)

#print a histogram 
# dictonnaries got methods
ccc = dict()
names = ['rolo','roko','bella','eolo','koko']
for name in names:
    if name not in ccc:
        ccc[name] = 1
    else :
        ccc[name] += 1
print(ccc)
if name in ccc :
      x = ccc[name]
else : 
      x = 0

x = ccc.get(name, 0) +1
print(x)

count =  'quincy mrugesh beau loil i okdocksdk'
wordie = count.split()
print(wordie)
#Counting words in a file

coco = {'ck': 145, 'fred':140, 'fofo':789 }
for  aaa,bbb in coco.items():
    print(aaa,bbb)
    

colo = dict()
print('Enter a line of text :')
line = input('')

lolos = line.split()

print('Words:', lolos)

print('Counting...')

for lolo in lolos:
    colo[lolo] = colo.get(lolo,0) +1
print('colo',colo)

#here we are going to loop through   the dict that we created by ourselves 
pipi = {'lolo': 14, 'polo':588,'roro':985}
for key in pipi.keys():
    print( pipi[key])


# bring a file text and code below will count the words in it 

with open(r"C:\Users\itc\Desktop\alo.txt")  as file:
      namo = file.read()

cola = dict()

for line in namo:
    kalimats = line.split()

for kalimat in kalimats :
    cola[kalimat] = cola.get(kalimat,0) + 1


bigcount = None
bigword = None

for kalimat , count in cola.items():
    if bigcount is None or count > bigcount:
          
        bigword = kalimat

        bigcount =  count 
      
print( bigword, bigcount)
a = tuple()
print( a)

d = {'a':10,'b':1,'c':22}
    

print( sorted ([ (v,k) for k,v in d.items()]))