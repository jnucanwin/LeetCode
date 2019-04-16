import queue
def PreOrder(T):
    S = []
    p = T
    while S or p:
        if p:
            print(p.val)
            S.append(p)
            p = p.left
        else:
            p = S.pop()
            p = p.right


def InOrder(T):
    S = []
    p = T
    while S or p:
        if p:

            S.append(p)
            p = p.left
        else:
            p = S.pop()
            print(p.val)
            p = p.right


def PostOrder1(T):
    S = []
    p = T
    while p or S:
        if p:
            S.append([p, 0])
            p = p.left
        else:
            q = S[-1]
            p = q[0]
            r = q[1]
            if p.right and r == 0:
                S[-1][1] = 1
                p = p.right
                S.append([p, 0])
                p = p.left
            else:
                q = S.pop()
                p = q[0]
                print(p.val)
                p = None


def PostOrder(T):
    S = []
    p = T
    r = None
    while p or S:
        if p:
            S.append(p)
            p = p.left
        else:
            p = S[-1]
            if p.right and p.right != r:
                p = p.right
                S.append(p)
                p = p.left
            else:
                p = S.pop()
                print(p.val)
                r = p
                p = None


def LevelOrder(T):
    if not T:
        return False
    Q = queue.Queue()
    Q.put(T)
    while not Q.empty():
        p = Q.get()
        print(p.val)
        if p.left:
            Q.put(p.left)
        if p.right:
            Q.put(p.right)