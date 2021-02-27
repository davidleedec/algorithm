class MaxHeap:
    def __init__(self):
        self.items = [None]
    #1. 새 노드를 맨끝에 추가한다.
    #2. 지금 넣은 새 노드를 부오와 비교한다. 만약 부모보다 크다면 교체한다.
    #3. 이과정을 꼭대기까지 반복한다.

    def insert(self, value):
        # 구현해보세요!
        self.items.append(value)
        current_index = len(self.items) -1

        while current_index > 1:
            parent_index = current_index //2
            if self.items[current_index] > self.items[parent_index]:
                self.items[current_index], self.items[parent_index] = self.items[parent_index], self.items[current_index]
                current_index = parent_index
            else:
                break
            
        return


max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!