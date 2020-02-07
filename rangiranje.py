def rangiraj(counters, links):
    mylist = list()
    for path in counters:
        element = (counters[path], links[path])
        mylist.append(element)
    return mylist