# represent graph in python

class Vertex():
    def __init__(self,key):
        self.id = key
        # using a dictionary to store connected vertex and its weight,
        # it is the info on edges
        self.connectedTo = {} 
    
    def addNeighbor(self,nbr, weight = 0):
        self.connectedTo[nbr] = weight
    
    def __str__(self):
        return str(self.id) + 'connectedTo: ' + \
            str([x.id for x in self.connectedTo])
    
    def getConnections(self):
        return self.connectedTo.keys()
    
    def getId(self):
        return self.id
    
    def getWeight(self,nbr):
        return self.connectedTo[nbr]

class Graph():
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex
    
    def getVertex(self,key):
        if key in self.vertList:
            return self.vertList[key]
        else:
            return None

    def __contains__(self,key):
        return key in self.vertList
    
    def addEdge(self,f,t,weight=0):
        if f not in self.vertList:
            self.addVertex(f)
        if t not in self.vertList:
            self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t],weight)
    
    def getVertices(self):
        return self.vertList.keys()
    
    def __iter__(self):
        return iter(self.vertList.values())

# test
# if __name__ == "__main__":
#     g = Graph()
#     for i in range(6):
#         g.addVertex(i)
#     g.vertList
#     g.addEdge(0,1,5)
#     g.addEdge(0,5,2)
#     g.addEdge(1,2,4)
#     g.addEdge(2,3,9)
#     for vertex in g:
#         for nbr in vertex.getConnections():
#             print(f'{vertex.id} is connected to {nbr.id}')