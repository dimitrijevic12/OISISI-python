import string

def parse(query):
    cases = ("AND", "OR", "NOT")
    splittedQuery = query.split(' ')
    first = splittedQuery[0]
    logop = ""
    search = []
    if first == "AND" or first == "OR":
        return False, logop, search
    elif first == "NOT":
        logop = "NOT"
        if len(splittedQuery) == 1 or splittedQuery[1] in cases:
            return False, logop, search
        else:
            search.append(splittedQuery[1])
        # for word in range(splittedQuery[1], splittedQuery[-1]):
        #     if word in cases:
        #         return False, logop, search
        #     else:
        #         search.append(word)
    else:
        if len(splittedQuery) == 1:
            search.append(first)
            return True, logop, search
        else:
            second = splittedQuery[1]
            if second in cases:
                logop = second
                if len(splittedQuery) == 4:
                    return False, logop, search
                else:
                    if splittedQuery[2] in cases:
                        return False, logop, search
                    else:
                        search.append(splittedQuery[0])
                        search.append(splittedQuery[2])
            else:
                logop = "OR"
                for word in splittedQuery:
                    if word in cases:
                        return False, logop, search
                    else:
                        search.append(word)
    #print(search)
    #print(logop)
    return True, logop,search
