import string

def parse(query):
    cases = ("AND", "OR", "NOT")
    splittedQuery = query.split(' ')
    first = splittedQuery[0]
    logop = ""
    search = []
    if first == "":
        print("Uneli ste prazan upit")
        return False, logop, search
    elif len(splittedQuery) == 1 and first not in cases:
        logop = "OR"
        search.append(first.lower())
        return True, logop, search
    if first in cases:
        print("Prva rec upita ne sme biti logicki operator")
        return False, logop, search

    else:
        if len(splittedQuery) == 1:
            search.append(first.lower())
            return True, logop, search
        else:
            second = splittedQuery[1]
            if second in cases:
                logop = second
                if len(splittedQuery) == 4:
                    print("Upit koji sadrzi logicki operator(kod kojeg prva rec nije log. operator NOT) mora sadrzati tacno 2 reci i jedan logicki operator")
                    return False, logop, search
                elif len(splittedQuery) == 2:
                    print("Logicki operator ne moze stajati na poslednjem mestu, mora stajati izmedju dve reci")
                    return False, logop, search
                else:
                    if splittedQuery[2] in cases:
                        print("Ne mogu stajati dva logicka operatora, jedan za drugim")
                        return False, logop, search
                    else:
                        search.append(splittedQuery[0].lower())
                        search.append(splittedQuery[2].lower())
            else:
                logop = "OR"
                for word in splittedQuery:
                    if word in cases:
                        print("Logicki operatori rade samo kada stoje izmedju tacno dve reci")
                        return False, logop, search
                    else:
                        search.append(word.lower())
    return True, logop,search
