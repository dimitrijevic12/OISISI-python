def rangiraj(counters, paths, links):
    mylist = list()
    for i in range(0, len(paths)):
        element = (counters[i], paths[i], links[i])
        mylist.append(element)
    return mylist