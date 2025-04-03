

N,M = map(int,input().split())
cleaner = list(map(int,input().split())) # r,c,dir: 북동남서 (0,1,2,3)
arr = [list(map(int,input().split())) for _ in range(N)] # map size = NxM (0,0) (N-1,M-1)//# blank cell(0), wall(1)

dx = [-1,0,1,0]
dy = [0,1,0,-1]

q = []
q.append(tuple(cleaner))
arr[cleaner[0]][cleaner[1]] -= 1

while q:
    cx,cy,cd = q.pop(0)
    candidate = []
    flag = 0 # 빈칸 있으면 > 0, 없으면 0

    for i in range(1,5):
        nd = (cd - i) % 4
        nx,ny = cx+dx[nd],cy+dy[nd]
        candidate.append((nx,ny,nd))
    for nx,ny,nd in candidate:
        if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0:
            flag += 1
            q.append((nx,ny,nd))
            arr[nx][ny] = arr[cx][cy] - 1
            break


    if not flag:
        nx,ny,nd = cx-dx[cd], cy-dy[cd], cd
        if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] != 1:
            if arr[nx][ny] == 0:
                q.append((nx,ny,nd))
                arr[nx][ny] = arr[cx][cy] - 1
            elif arr[nx][ny] < 0:
                q.append((nx,ny,nd))
                arr[nx][ny] = arr[cx][cy]
        else:
            break
    print()
min_value = 0
for x in arr:
    for cell in x:
       min_value = min(cell,min_value)
print(-min_value)