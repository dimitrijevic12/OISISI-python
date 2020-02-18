import string

def parse(query):
    cases = ("AND", "OR", "NOT")
    splittedQuery = query.split(' ')
    first = splittedQuery[0]
    logop = ""
    search = []
    if len(splittedQuery) == 1 and first not in cases:
        logop = "OR"
        search.append(first)
        return True, logop, search
    if first in cases:
        print("Prva rec upita ne sme biti logicki operator")
        return False, logop, search
    # elif first == "NOT":
    #     logop = "NOT"
    #     if len(splittedQuery) == 1:
    #         print("Logicki operator NOT ne moze stojati sam")
    #         return False, logop, search
    #     elif len(splittedQuery) == 3:
    #         print("Ako je logicki operator NOT na prvom mestu upita, onda sme samo jedna rec da stoji posle njega")
    #         return False, logop, search
    #     elif splittedQuery[1] in cases:
    #         print("Ne mogu stajati dva logicka operatora, jedan za drugim")
    #         return False, logop, search
    #     else:
    #         search.append(splittedQuery[1])
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
                    print("Upit koji sadrzi logicki operator(kod kojeg prva rec nije log. operator NOT) mora sadrzati tacno 2 reci i jedan logicki operator")
                    return False, logop, search
                else:
                    if splittedQuery[2] in cases:
                        print("Ne mogu stajati dva logicka operatora, jedan za drugim")
                        return False, logop, search
                    else:
                        search.append(splittedQuery[0])
                        search.append(splittedQuery[2])
            else:
                logop = "OR"
                for word in splittedQuery:
                    if word in cases:
                        print("Logicki operator ne moze da se nadje na kraju upita")
                        return False, logop, search
                    else:
                        search.append(word)
    #print(search)
    #print(logop)
    return True, logop,search
