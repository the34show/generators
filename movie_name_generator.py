import random
def get_name():
    context_to_word={}
    f=open("movie_metadata.csv","r")
    header=f.readline()
    for movie in f:
        movie=movie.strip('\n')
        movie=movie[:-2]
        movie= movie.split(" ")
        for index in range(len(movie)):
            word=movie[index]
            if index+1>=len(movie):
                context=" "
            else:
                context=movie[index+1]
            if word in context_to_word: 
                context_to_word[word].append(context)
            else:
                context_to_word[word]=[context]
    f.close()
    return context_to_word

    
context_to_word=get_name()    
def create_name():
    global context_to_word
    inital=input("What word would you like to start with? ")
    inital=inital.capitalize()    
    while not inital in context_to_word:
        inital=input("Please select another word that you would like to start with? ")
        inital=inital.capitalize()
    #length=int(input("min long of a name? "))
    word=inital
    length=3
    movie=""
    while len(movie) < length:
        movie=""
        while word!= " ":
            movie+= word + " "
            word= random.choice(context_to_word[word])
            #letter= random.sample(context_to_char[letter],1)[0]
    return movie
    
