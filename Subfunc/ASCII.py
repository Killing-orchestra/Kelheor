ss5l="Ⱖ"
strr="Привет, мир! Отпусти меня, чудо-девочка! Hello, World!"
print(strr)
old_list=list(strr)
print(old_list)
new_list = list()
new_new_list= list()
new_new_new_list= list()
for x in old_list:
    new_list.append("0"*(5-len(str(ord(x))))+str(ord(x)))
print(new_list)
strig=""
for x in new_list:
    strig=strig+str(x)
print(strig)
#Выбор режима:
#Чистоганом гнать?
#Шифром гнать? При шифре длина кода-3 символа. Ξ
for x in range(0, len(strig), 5):
    new_new_list.append(int(strig[x:x+5]))
print(new_new_list)

for x in new_new_list:
    new_new_new_list.append(chr(x))
print(new_new_new_list)

striga=""

for x in new_new_new_list:
    striga=striga+x
print(striga)


#chr()

#ord(u'あ')
#12354

##print(chr(97))
##print(chr(int("0097")))
