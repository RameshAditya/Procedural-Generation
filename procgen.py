import random

# lets say we're in the 40th floor of a dungeon
random.seed(12)

# lets say its an n x n dungeon
n = 20

dungeon = [[0 for i in range(n)] for j in range(n)]

start = (0, 0)
end = (n-1, n-1)

for i in range(n):
    for j in range(n):
        obstacle_prob = random.randint(1, 100)/100

        # let us place an obstacle with a probability of 40%
        if obstacle_prob <= 0.4:
            dungeon[i][j] = 1

dungeon[0][0] = 0
dungeon[n-1][n-1] = 0

# let us determine if the generated dungeon is valid or not with a DFS
visited = [[0 for i in range(n)] for j in range(n)]

def issafe(curx, cury):
    return curx>=0 and curx<n and cury>=0 and cury<n

reached = 0

def dfs(curx, cury, parx, pary):
    if curx==end[0] and cury==end[1]:
        global reached
        reached = 1
        return 1
    else:
        visited[curx][cury] = 1
        ans = 0
        for x in [curx-1, curx,curx+1]:
            for y in [cury-1, cury, cury+1]:
                if x==curx and y==cury:
                    continue
                if issafe(x, y) and dungeon[x][y] == 0 and visited[x][y]==0:
                    ans |= dfs(x, y, curx, cury)
                    visited[x][y] = 1
        return ans
    
dfs(0, 0, -1, -1)

while reached==0:
    dfs(0, 0, -1, -1)
    visited = [[0 for i in range(n)] for j in range(n)]
    if reached == 1:
        break
    # if dungeon is untraversable, we perform dilation
    for i in range(n):
        for j in range(n):
            if dungeon[i][j] == 0:
                for x in [i-1, i, i+1]:
                    for y in [j-1, j, j+1]:
                        if issafe(x, y):
                            dungeon[x][y] = 0



for i in dungeon:
    print(*i)
