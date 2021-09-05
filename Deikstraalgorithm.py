def GetGraph():
    print('Enter count of peaks')
    peaks = int(input())
    graph = {}
    for i in range(peaks):
        graph[i] = {}
        for j in range(peaks):
            if i != j:
                print('From peak', i, 'to peak', j, '?')
                key = input()
                if key == 'y':
                    print('Enter weight')
                    weight = int(input())
                    graph[i][j] = weight
    return graph


def GetCoastsTable(graph):
    coasts = {}
    for i in graph:
        if i != 0:
            if i in graph[0]:
                coasts[i] = graph[0][i]
            else:
                coasts[i] = float('inf')
    return coasts


def GetParents(coasts):
    parents = {}
    for i in coasts:
        if i != 0:
            if coasts[i] != float('inf'):
                parents[i] = 0
            else:
                parents[i] = None
    return parents


def FindLowestCoast(coasts, processed):
    peak = None
    lowestCoast = float('inf')
    for i in coasts:
        if coasts[i] < lowestCoast and i not in processed:
            peak = i
            lowestCoast = coasts[i]
    return peak


def Deikstra():
    graph = GetGraph()
    coasts = GetCoastsTable(graph)
    parents = GetParents(coasts)
    processed = []
    peak = FindLowestCoast(coasts, processed)
    while peak:
        for i in graph[peak]:
            if coasts[i] > coasts[peak] + graph[peak][i]:
                coasts[i] = coasts[peak] + graph[peak][i]
                parents[i] = peak
        processed.append(peak)
        peak = FindLowestCoast(coasts, processed)
    print('Enter end')
    start = 0
    end = int(input())
    while start != end:
        print(end)
        end = parents[end]
    print(0)
    return
