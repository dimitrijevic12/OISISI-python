def rangiraj(graf, recnikStranica):
    mylist = list()
    rang=0
    for key in recnikStranica:
        m=0
        rang=0
        for i in graf.get_pred(key):
            for j in recnikStranica:
                if i==j:
                    m=m+recnikStranica[j]
                    break
        a=recnikStranica[key]
        b=len(graf.get_pred(key))
        rang=a+b+m
        element = (key,rang,a,b,m)
        mylist.append(element)

    def takeSecond(elem):
        return elem[1]
    mylist.sort(key=takeSecond,reverse=True)
    return mylist