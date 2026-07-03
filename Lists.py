if __name__ == '__main__':
    N = int(input())
    my_list = []
    
    for _ in range(N):
        parts = input().split()
        command = parts[0]
        
        if command == "print":
            print(my_list)
        else:
            args = map(int, parts[1:])
            getattr(my_list, command)(*args)
