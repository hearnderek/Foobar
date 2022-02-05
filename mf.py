class Node:
    def __init__(self, m,f, parent):
        self.as_tuple = (m,f)
        self.m = m
        self.f = f
        self.parents = [parent]
        self.gen_m = (self.m+self.f, self.f)
        self.gen_f = (self.m, self.m+self.f)
        self.key = (m,f)
        self.gen_num = parent.gen_num+1 if parent else 0
        pass

    def make_m(self):
        return (self.m+self.f, self.f)

    def make_f(self):
        return (self.m, self.m+self.f)

    def get_generations(self):
        return (Node(self.gen_m[0],self.gen_m[1],self), Node(self.gen_f[0],self.gen_f[1], self))

    def add_parent(self, parent):
        self.parents.append(parent)

        # Keeps track of # of smallest number of generations to reach self
        would_be_gen = parent.gen_num+1
        if would_be_gen < self.gen_m:
            self.gen_num = would_be_gen

    def greater_than(self, other):
        return self.m > other.m or self.f > other.f

def solution(wanted_m, wanted_f):
    wanted_m = int(wanted_m)
    wanted_f = int(wanted_f)

    goal = Node(wanted_m, wanted_f, None)

    head = Node(1,1, None)

    queue = [head]
    lookup = {head.key: head}

    while(any(queue)):
        cur = queue.pop(0)
        m,f = cur.get_generations()

        if goal.key == m.key:
            return m.gen_num
        if goal.key == f.key:
            return f.gen_num

        if m.key in lookup:
            lookup[m.key].parents += cur.key
        elif goal.greater_than(m):
            queue.append(m)
            lookup[m.key] = m

        if f.key in lookup:
            lookup[f.key].add_parent(cur)
        elif goal.greater_than(f):
            queue.append(f)
            lookup[f.key] = f

    return 'impossible'