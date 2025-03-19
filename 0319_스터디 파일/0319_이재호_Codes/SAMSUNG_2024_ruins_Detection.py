# 전체
# 5x5 # 각 칸 다양한 유물 조각
# 총 7가지 1부터 7로 표현


회전 많이, 격자 최적 조건 찾는 게



# 전략 1. library 2. init 3-1. [1], 3-2. [2]
# 1. Library
import sys
# input = sys.stdin.readline
from typing import List, Tuple
from collections import deque

def rotate(arr,si,sj): # 암기하기
    narr = [x[:] for x in arr]
    size = 3
    for i in range(size): #
        for j in range(size):
            narr[si+i][sj+j] = arr[si+size-j-1][sj+i]
    return narr

def bfs(arr, v, si, sj, clr):
    q = []
    cnt = 0
    sset = set()

    q.append((si,sj))
    v[si][sj]=1
    sset.add((si,sj)) # 방문한 위치 체크
    cnt+=1

    while q:
        ci,cj =q.pop(0)
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj
            if 0 <= ni < 5 and 0 <= nj < 5 and v[ni][nj] == 0 and arr[ci][cj] == arr[ni][nj]:
                # 격자 내 # 방문 여부 # 추가조건: 같은 숫자
                q.append((ni,nj))
                v[ni][nj]=1
                sset.add((ni,nj))
                cnt += 1
    if cnt >= 3:
        if clr == 1:
            for i,j in sset:
                arr[i][j] = 0
        return cnt
    else:
        return 0


def count_clear(arr,clr):
    v = [[0]*5 for _ in range(5)] # visit list
    cnt = 0 # adjascent counting
    for i in range(5):
        for j in range(5):
            if v[i][j]==0:
                # 값은 값이면, 3개 이상인 경우
                t = bfs(arr,v,i,j,clr) # flag
                cnt += t

    return cnt

# 2. initialization
K, M = map(int, input().split()) # K: 총 반복 턴 수, M: 벽면에 적힌 유물 조각의 개수
arr = [list(map(int,input().split())) for _ in range(5) ] # 유적의 유물 조각 정보
lst = list(map(int,input().split()))
ans = []

for _ in range(K): # K 턴을 진행 (유물이 없는 경우, 즉시 종료)

    # 최적의 격자 회전 상태 찾기
    mx_cnt = 0

    # Priority order
    for rot in range(1,4):
        for sj in range(3):
            for si in range(3):

                narr = [x[:] for x in arr] # partly deep copy
                for _ in range(rot):
                    narr = rotate(narr, si, sj)

                t = count_clear(narr, 0) # flag arg
                if mx_cnt < t:
                    mx_cnt = t
                    marr = narr

    if mx_cnt == 0: # 유물이 없음
        break

    cnt = 0 # 매턴 유물 획득량
    arr = marr # optimized case
    while True:
        t = count_clear(arr,1)
        if t == 0:
            break # 연쇄획득 종료 -> 다음 턴으로
        cnt += t

        # 빈칸 채우기
        for j in range(5):
            for i in range(4,-1,-1):
                if arr[i][j] == 0:
                    arr[i][j] = lst.pop(0)
    ans.append(cnt)

print(*ans)