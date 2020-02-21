from set import Set


class Graph(object):
    def __init__(self):
        self._nasl = {}
        self._pred = {}

    def add_vertex(self, vertex):
        self._nasl[vertex] = []
        if vertex not in self._pred.keys():
            self._pred[vertex] = []

    def add_edge(self, ver1, ver2):
        self._nasl[ver1].append(ver2)
        if ver2 not in self._pred.keys():
            self._pred[ver2] = []
        self._pred[ver2].append(ver1)

    def add_site(self, vertex, links):
        self.add_vertex(vertex)
        for link in links:
            self.add_edge(vertex, link)
