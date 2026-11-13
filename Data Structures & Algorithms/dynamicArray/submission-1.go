type DynamicArray struct {
    capacity int
    length int
    array []int
}

func NewDynamicArray(capacity int) *DynamicArray {
    return &DynamicArray{
        capacity: capacity,
        length: 0,
        array: make([]int, capacity),
    }
}

func (da *DynamicArray) Get(i int) int {
    return da.array[i]
}

func (da *DynamicArray) Set(i int, n int) {
    da.array[i] = n
}

func (da *DynamicArray) Pushback(n int) {
    if da.length == da.capacity {
        da.resize()
    }
    da.array[da.length] = n
    da.length++
}

func (da *DynamicArray) Popback() int {
    if da.length > 0 {
        da.length--
    }
    return da.array[da.length]
}

func (da *DynamicArray) resize() {
    da.capacity = 2 * da.capacity
    newArray := make([]int, da.capacity)
    
    for i := 0; i < da.length; i++ {
        newArray[i] = da.array[i]
    }
    da.array = newArray
}

func (da *DynamicArray) GetSize() int {
    return da.length
}

func (da *DynamicArray) GetCapacity() int {
    return da.capacity
}
