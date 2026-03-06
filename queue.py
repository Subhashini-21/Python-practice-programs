q = int(input())
arr = []

for _ in range(q):
    value= input().split()

    if value[0] == "ENQUEUE":
        arr.append(int(value[1]))

    elif value[0] == "DEQUEUE":
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.pop(1))

    elif value[0] == "FRONT":
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[0])
