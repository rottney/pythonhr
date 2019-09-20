if __name__ == '__main__':
    n = int(input())    # this came by default, idk...
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))
