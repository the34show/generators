import random
def get_name():
    context_to_char={}
    f=open("baby-names.csv","r")
    header=f.readline()
    for line in f:
        line=line.split(",")
        name=line[1]
        name=name.strip('"')
        for index in range(len(name)):
            char=name[index]
            if index+1>=len(name):
                context=" "
            else:
                context=name[index+1]
            if char in context_to_char:
                context_to_char[char].append(context)
            else:
                context_to_char[char]=[context]
    f.close()
    return context_to_char

    
    
def create_name():
    global context_to_char
    context_to_char=get_name()
    inital=input("What letter would you like to start with? ")
    length=int(input("min long of a name? "))
    letter=inital
    word=""
    while len(word) < length:
        letter=inital
        while letter!= " ":
            word+=letter
            letter= random.choice(context_to_char[letter])
            #letter= random.sample(context_to_char[letter],1)[0]
    return word
    
    