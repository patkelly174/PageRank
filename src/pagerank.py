pages_count = 0
inlink_count = {}
graph = {}
i = {}
r = {}
lamda = 0.15
tau = 0.0001

#Patrick Kelly

def convergence(r, i):
    norm = 0
    for page in r:
        total += abs(r[page] - i[page])
    return norm

with open("links.srt", "r") as f:
    for line in f:
        words = line.split()
        source = words[0]
        target = words[1]
        if not target in inlink_count:
            inlink_count[target] = 1
        else:
            inlink_count[target] += 1
        if source in graph:
            graph[source].append(target)
        else:
            graph[source] = [target]
        if target not in graph:
            graph[target] = []
        pages_count += 1
        r[source] = None
        r[target] = None
        i[source] = None
        i[target] = None
    f.close()

############## PAGE RANK ALGO #################
r = dict.fromkeys(r, lamda / pages_count)
i = dict.fromkeys(i, 1 / pages_count)
while not convergence(r, i) < tau:
    r = dict.fromkeys(r, lamda / pages_count)
    for page in graph:
        q = graph[page]
        accumulator = {}
        if len(q) > 0:
            for q_page in q:
                r[q_page] = r[q_page] + ((1 - lamda) * i[page]) / abs(len(q))
        else:
            accumulator[page] = ((1 - lamda) * i[page]) / abs(pages_count)
    for page in accumulator:
        r[page] += accumulator[page]
    i = r
############## END PAGE RANK ALGO #################

with open("pagerank.txt", "w") as f:
    sorted_pagerank = sorted(r, key = r.get, reverse = True)[:75]
    count = 1
    for pagerank in sorted_pagerank:
        f.write(str(count) + " " + pagerank + " " + str(r[pagerank]) + "\n")
        count += 1

with open("inlinks.txt", "w") as f:
    sorted_inlink = sorted(inlink_count, key = inlink_count.get, reverse = True)[:75]
    count = 1
    for inlink in sorted_inlink:
        f.write(str(count) + " " + inlink + " " + str(inlink_count[inlink]) + "\n")
        count += 1
