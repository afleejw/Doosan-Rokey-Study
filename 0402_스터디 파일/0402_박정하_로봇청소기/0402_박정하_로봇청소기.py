import sys

read = sys.stdin.readline
N,M = map(int, read().split())
r,c,d = map(int, read().split())
Map = [list(map(int, read().split())) for _ in range(N)]

# print(N,M)
# print(r,c,d)
# print(Map)


def is_clear(Map, position):   #주변에 청소 가능 지역 있는지 판단. 있으면 True, 없으면 False
    n_r, n_c = position[0],position[1]
    near = [(1,0),(-1,0),(0,1),(0,-1)]
    count = 0
    for dy, dx in near:
        a_r, a_c = n_r+dy, n_c+dx
        if (a_r, a_c) in cleaned_area or Map[a_r][a_c] != 0:
            count +=1
    if count == 4:
        return False
    else:
        return True

def move_1(Map, position, direction):
    n_r, n_c = position[0],position[1]
    if direction == 'n':
        a_r = n_r + 1 # 북쪽 바라보며 후진
        a_c = n_c
    elif direction == 's':
        a_r = n_r - 1
        a_c = n_c
    elif direction == 'e':
        a_c = n_c -1
        a_r = n_r
    elif direction == 'w':
        a_c = n_c +1
        a_r = n_r
    if Map[a_r][a_c] != 1:  #후진 가능하면 후진한 위치값 반환
        cleaned_area.add((a_r,a_c))
        return (a_r,a_c)
    else:
        return None   #후진 불가면 일단 False
    
def move_2(Map, position, direction):
    n_r, n_c = position[0],position[1]
    if direction == 'n':   # 반시계 90도 회전
        direction = 'w'   # 그리고 전진 이동까지 아마도 지도 테두리가 다 1로 채워져 있어 r, c에 대한 범위 지정 필요 없을듯
        a_c = n_c - 1
        a_r = n_r
    elif direction == 's':
        direction = 'e'
        a_c = n_c +1
        a_r = n_r
    elif direction == 'e':
        direction = 'n'
        a_r = n_r - 1
        a_c = n_c
    elif direction == 'w':
        direction = 's'
        a_r = n_r + 1
        a_c = n_c

    if Map[a_r][a_c] !=0  or (a_r,a_c) in cleaned_area:  #전진진 가능하면 후진한 위치값 반환

        return move_2(Map, position,direction) 
    else:
           # 재귀로 이동 가능할때까지지
        cleaned_area.add((a_r,a_c))
        return (a_r,a_c), direction


if d == 0:
    direction = 'n'
elif d== 1:
    direction = 'e'
elif d == 2:
    direction = 's'
elif d== 3 :
    direction = 'w'
finsh = False
now_pos = (r,c)
cleaned_area = {now_pos}


while True:
    
    # print('현재 위치',now_pos)
    if not is_clear(Map, now_pos) : 
        now_pos = move_1(Map, now_pos, direction)

        if now_pos == None:
       
            finsh = True
    elif is_clear(Map, now_pos):
 
        now_pos, direction = move_2(Map, now_pos, direction)
        # print('direction :', direction)
    if finsh:
        print(len(cleaned_area))
        break
