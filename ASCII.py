def str2int(message: str, crypto: bool):
    if crypto==True:
        startsymbol="Ξ"
        consym=3
    else:
        startsymbol="Ⱖ"
        consym=5
    message=startsymbol+message
    old_list=list(message)
    new_list = list()
    for x in old_list:
        new_list.append("0"*(consym-len(str(ord(x))))+str(ord(x)))
    k=""
    for x in new_list:
        k=k+str(x)
    return int(k)

#Выбор режима:
#Чистоганом гнать?
#Шифром гнать? При шифре длина кода-3 символа. Ξ
def int2message(k: int, crypto: bool):
    new_new_list=list()
    new_new_new_list=list()
    k=str(k)
    if crypto==True:
        startsymbol="Ξ"
        consym=3
    else:
        startsymbol="Ⱖ"
        consym=5
    for x in range(0, len(k), consym):
        new_new_list.append(int(k[x:x+consym]))
    for x in new_new_list:
        new_new_new_list.append(chr(x))
    striga=""
    for x in new_new_new_list:
        striga=striga+x
    striga=striga.replace(startsymbol, '', 1) 
    return striga

