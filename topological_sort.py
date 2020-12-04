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
    edges = 0
    for i in range(maxVert):
        curVertList = []
        pathes = random.randint(1, maxVert - 1)
        for j in range(pathes):
            if edges != maxVert:
                while(True):
                    new = random.randint(0, maxVert - 1)
                    if(new != i and new not in curVertList):
                        break
                curVertList.append(new)
                edges += 1
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

    for i in range(10):
        length = 50000 * (i + 1)
        print("Вершин | Рёбер: ", length , " | ", length)
        for j in range(20):
            graph = graph_generator(length)
            times = []
            start_time = time.time()
            topological_sort(graph)
            res_time = time.time() - start_time
            times.append(res_time)
        res = 0
        for t in times:
            res += t
        res /= len(times)
        print("Время среднее: ", res)

