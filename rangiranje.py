def rangiraj(counters, links):
    mylist = list()
    for path in counters:
        print(path)
        path = path.replace('\\', '\\\\')
        print(path)
        element = (counters[path], links[path])
        #mylist.append(element)
    return mylist