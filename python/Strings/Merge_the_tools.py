def merge_the_tools(string, k):
    
    for i in range(0, len(string), k):
        sub = string[i:i + k]
        u = ''.join(dict.fromkeys(sub))
        print(u)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)