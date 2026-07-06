# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.

if __name__ == '__main__':
    N = int(input())
    list1=[]
    for i in range(N):
        user_cmd = input().split()
        cmd = user_cmd[0]
    
        if cmd=="insert":
            index = int(user_cmd[1])
            element = int(user_cmd[2])
            list1.insert(index,element)
        elif cmd == "print":
            print(list1)
        elif cmd == "remove":
            element = int(user_cmd[1])
            list1.remove(element)
        elif cmd == "append":
            element = int(user_cmd[1])
            list1.append(element)
        elif cmd == "sort":
            list1.sort()
        elif cmd == "pop":
            list1.pop()
        elif cmd == "reverse":
            list1.reverse()
