import sys
trees = {}
n=0
while True:
    s = sys.stdin.readline().rstrip()
    if not s: break
    if s in trees:
        trees[s] +=1
    else:
        trees[s] =1
    n+=1

tree_list = list(trees.keys())
tree_list.sort()

for tree in tree_list:
    print('%s %.4f' %(tree, trees[tree]/n*100))