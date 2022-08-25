from re import M


arr = [0,0,0]

def DFS(depth): # 
    if(depth == 3): # base case
        for i in range(depth):
            print(arr[i])
        print("\n")
        return

    for i in range(1,7): # recursive case
        arr[depth] = i
        DFS(depth +1) # 다음 깊이로 넘어감


DFS(0)
