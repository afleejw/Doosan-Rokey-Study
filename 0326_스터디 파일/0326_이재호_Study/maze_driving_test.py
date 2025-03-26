def solution(n, m, tests):  # n: row (0~n), m: col (0~m)
    # test: start point, distance, arrive check
    set_lists = []
    nums = len(tests)
    for i in range(nums):
        x, y = tests[i][0], tests[i][1]
        distance = tests[i][2]
        flag = tests[i][3] # flag 1: arrive else: 0

        if flag:
            aset = set()
            aset = bfs(n, m, x, y, flag, aset, distance)  # 다른 방법 가능 범위 체크로
            set_lists.append(aset)
        else:
            bset = set()
            bset = bfs(n, m, x, y, flag, bset, distance)  # 범위 계산만으로 가능
            set_lists.append(bset)

    temp = set_lists[0]
    for i in range(1, len(set_lists)):
        intersection = temp & set_lists[i]
        temp = intersection
    answer = len(temp)

    return answer


def bfs(n, m, x, y, flag, abset, distance): # n: row (0~n), m: col (0~m)
    q = []

    visited = [[-1]*(m+1) for _ in range(n + 1)] # not-visited = 0

    q.append((x, y))
    visited[x][y] += 1
    if flag:
        if visited[x][y] <= distance:
            abset.add((x, y))

    else:
        if visited[x][y] > distance:
            abset.add((x, y))

    abset.add((x, y))
    while q:
        cx, cy = q.pop(0)

        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = cx + dx, cy + dy
            if 0 <= nx <= n and 0 <= ny <= m:
                if visited[nx][ny] == -1:
                    q.append((nx, ny))
                    visited[nx][ny] = 1 + visited[cx][cy]
                    if flag:
                        if visited[nx][ny] <= distance:
                            abset.add((nx, ny))
                    else:
                        if visited[nx][ny] > distance:
                            abset.add((nx, ny))

    return abset

print(solution(3,	5,[[2, 3, 2, 1], [1, 0, 4, 0], [0, 4, 1, 0]]))
