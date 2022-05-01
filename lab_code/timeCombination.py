def DFSUtil(ans, temp, n, left, k):
    if k == 0:
        if not(ans and ans[-1] == temp[:-1]):
            ans.append(list(temp[:-1]))
        return

    for i in range(left, n + 1):
        temp.append(i)
        DFSUtil(ans, temp, n, i + 1, k - 1)
        temp.pop()

def DFS(n, k):
    ans = []
    temp = []
    DFSUtil(ans, temp, n, 1, k)
    return ans

if __name__ == "__main__":
    n = 5
    k = 3
    ans = DFS(n, k)
    for i in range(len(ans)):
        for j in range(len(ans[i])):
            print(ans[i][j], end=' ')
        print()