# while loop
# check node
class Node:
    def __init__(self, x):
        self.value = x
        self.next = None

    def __repr__(self):
        return f"{self.value}, {self.next}"

node1 = Node(1000)
node2 = Node(1000)
node1.next = node2

l = node1
k = 1000



def solution(l, k, node, prev=None):
    if not node:
        return l

    print(node)
    if node.value == k:
        if not prev:
            # first node case
            l = node.next
            return solution(l, node.next, prev)
        else:
            # general case
            prev.next = node.next
            return solution(l, node.next, prev)
    else:
        return solution(l, k, node.next, node)

solution(l,k,l)