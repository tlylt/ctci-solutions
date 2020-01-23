# transform a word into a target word, while every step of transformation
# must contain transforming a valid word to another valid word
# find the smallest number of transformation needed

# 1. represent the relationships between words as a graph
# 2. breadth first search

from graph_representation import Graph, Vertex

def buildGraph(wordFile):
    d = {}
    g = Graph()
    wfile = open(wordFile,'r')
    #create buckets of words that differ by one letter
    for line in wfile:
        word = line[:1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:] # buckets are like _OOL, F_OOL, FO_L
            if bucket in d: # if bucket has been initialized, add word under it
                d[bucket].append(word)
            else:
                d[bucket]=[word]
    # add vertices and edges for words in the same bucket
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1,word2)
    return g


class Queue():
    def __init__(self):
        self.container = []
    def enqueue(self,data):
        self.container.append(data)
    def dequeue(self):
        if self.container:
            item = self.container[0]
            self.container = self.container[1:]
            return item
        return None