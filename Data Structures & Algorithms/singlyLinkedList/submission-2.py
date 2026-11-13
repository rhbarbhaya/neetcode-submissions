class LinkedList:
    
    def __init__(self):
        self.array = list()
    
    def get(self, index: int) -> int:
        if index >= len(self.array):
            return -1
        return self.array[index]

    def insertHead(self, val: int) -> None:
        self.array = [val] + self.array

    def insertTail(self, val: int) -> None:
        self.array += [val]

    def remove(self, index: int) -> bool:
        if index >= len(self.array):
            return False
        if self.array[index]:
            self.array.pop(index)
            return True
        return False

    def getValues(self) -> List[int]:
        return self.array
