if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    winner = -101   # min value is -100
    runnerUp = -101

    for i in range(n):
        if arr[i] > winner:
            winner = arr[i]
    
    for i in range(n):
        if arr[i] > runnerUp and arr[i] != winner:
            runnerUp = arr[i]
    
    print(runnerUp)
