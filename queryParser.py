import string

def parse(query):
    splittedQuery = query.split(' ')
    logop = ""
    search = []
    #search = query.split(' ')
    for word in splittedQuery:
        if word == "AND":
            logop = word
        elif word == "OR":
            logop = word
        elif word == "NOT":
            logop = word
        else:
            search.append(word)
    #print(search)
    #print(logop)
    return logop,search
