class Heap:
    def __init__(self):
        self.heap = [None]

    def _insert(self, data):
        """Insert one element to heap.
        Best Case: O(1)
        Average & Worst Case: O(log n)

        Arguments:
            data {any} -- item to be inserted
        """
        self.heap.append(data)
        n = len(self.heap)-1
        p = n//2
        while p>0 and self.heap[p]<self.heap[n]:
            self.heap[p], self.heap[n] = self.heap[n], self.heap[p]
            n = p
            p = n//2

    def heapify(self, n=None, pos=1):
        if not n:
            n = len(self.heap)-1

        largest = pos
        left, right = 2*pos, 2*pos + 1

        if left<n and self.heap[largest]<self.heap[left]:
            largest = left
        if right<n and self.heap[largest]<self.heap[right]:
            largest = right
        if largest!=pos:
            self.heap[pos], self.heap[largest] = self.heap[largest], self.heap[pos]

            self.heapify(n=n,pos=largest)

    def _delete(self):
        self.heap[1] = self.heap[len(self.heap)-1]
        self.heap.pop()
        self.heapify()

    def _sort(self):
        for i in range(len(self.heap)-1, 1,-1):
            self.heap[1], self.heap[i] = self.heap[i], self.heap[1]
            self.heapify(n=i-1)

    def _print(self):
        print(self.heap[1:])

if __name__ == "__main__":
    heap = Heap()

    while True:
        data = int(input())
        if data==-1:
            break
        heap._insert(data)
    heap._print()
    heap._delete()
    heap._print()
    heap._sort()
    heap._print()
