import time
import random
import matplotlib.pyplot as plt
import networkx as nx

# Поиск в глубину по графу
# graph - граф для топологической сортировки
# currentVert - текущая вершина из которой идем
# used - равно 0 => не посещалась, 1 => зашли в вершину, 2 => вышли из вершины
# ans - ответ
def dfs(graph, currentVert, used, ans):
    used[currentVert] = 1
    for item in graph[currentVert]:
        if(used[item] == 0):
            dfs(graph, item, used, ans)
        elif(used[item] == 1):
            pass #В графе есть циклы

    used[currentVert] = 2
    ans.append(currentVert)

def topological_sort(graph):
    size = len(graph)
    used = []
    answer = []
    for i in range(size):
        used.append(0)
    for i in range(size):
        if(used[i] == 0):
            dfs(graph, i, used, answer)
    answer.reverse()
    return answer


def graph_generator(maxVert):
    graph = []
    for i in range(maxVert):
        if i == 0:
            pathes = 0
        else:
            pathes = random.randint(0, i)
        curVertList = []
        for j in range(pathes):
            while(True):
                if i == 1:
                    new = 0
                else:
                    new = random.randint(0, i - 1)
                if(new not in curVertList):
                    break
            curVertList.append(new)
        graph.append(curVertList)
    return graph

#Отрисовка графа
def draw_graph(graph, num):
    nodes = []
    for i in range(len(graph)):
        nodes.append(i)
    diGraph = nx.DiGraph()
    diGraph.add_nodes_from(nodes)
    for i in range(len(graph)):
        for j in graph[i]:
            diGraph.add_edge(i, j)
    plt.subplot(num)
    nx.draw_circular(diGraph,
         node_color='orange',
         node_size=450,
         with_labels=True)
    return diGraph

if __name__ == "__main__":
    graph = graph_generator(random.randint(2, 10))
    print("Исходный граф в виде списка смежности:", graph)
    start_time = time.time()
    answer = topological_sort(graph)
    print("Линейный порядок вершин после топологической сортировки: ", answer)
    print("Время работы: ", time.time() - start_time)
    diGraph = draw_graph(graph, 221)
    mapping = {}
    for i, item in enumerate(answer):
        mapping[item] = i
    diGraph = nx.relabel_nodes(diGraph, mapping)
    plt.subplot(222)
    nx.draw_circular(diGraph,
         node_color='blue',
         node_size=450,
         with_labels=True)
    plt.show()
    