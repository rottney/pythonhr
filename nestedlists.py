if __name__ == '__main__':
    n = int(input())
    low = 100       # assume this is the max "score"
    secondLow = 100
    students = []   # matrix
    secondLows = [] # 1-D list
    

    for i in range(n):
        students.append([])
        students[i].append(input())
        students[i].append(float(input()))
    
    for i in range(n):
        if students[i][1] < low:
            low = students[i][1]
    
    for i in range(n):
        if students[i][1] < secondLow and students[i][1] != low:
            secondLow = students[i][1]
    
    for i in range(n):
        if students[i][1] == secondLow:
            secondLows.append(students[i][0])

    secondLows.sort()
    for i in range(secondLows.__len__()):
        print(secondLows[i])
