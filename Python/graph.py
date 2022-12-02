class Graph:

    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print("Vertex:", self.adj_list[vertex])

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v1 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    
    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v1 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

    def remove_vertex(self, v):
        for i in self.adj_list.keys():
            if v in self.adj_list[i]:
                self.adj_list[i].remove(v)
        if v in self.adj_list:
            try:
                del self.adj_list[v]
            except ValueError:
                pass
            return True
        
        return False

    

    

my_graph = Graph()
my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_vertex("E")
my_graph.add_edge("A", "B")
my_graph.add_edge("E", "B")
my_graph.add_edge("A", "E")
my_graph.remove_vertex("E")
my_graph.print_graph()