import random

names = [
    '강ㅅ☆', '김ㅅ☆', '김ㅇ☆☆', '김ㅈ☆', '남ㄱ☆', 
    '박ㅅ☆', '박ㅈ☆', '배ㅇ☆', '사ㅂ☆', '서ㅎ☆', 
    '이ㅅ☆', '이ㅅ☆', '이ㅈ☆', '이ㅈ☆', '이ㅊ☆', 
    '주ㅎ☆', '최ㅇ☆', '하ㅈ☆', '한ㄷ☆', '황ㅎ☆'
]

# 0. 총 학생 정보 표시
print(f"우리반에는 {", ".join(names)} 이(가) 있습니다.")

print() # 줄바꿈용

# 1. 조의 개수 입력받기
num_teams = int(input(f"현재 총 인원은 {len(names)}명입니다. 몇 개의 조로 나눌까요? [숫자만 입력]: "))

print() # 줄바꿈용

if num_teams <= 0:
    print("조의 개수는 1개 이상이어야 합니다.")
    
    print() # 줄바꿈용
        
# 최소 조 당 한 명 이상씩의 조건을 걸겠음!       
elif len(names) < num_teams * 2:
    print(f"인원이 부족합니다! {num_teams}개의 조를 만들려면 최소 {num_teams * 2}명이 필요합니다.")
    
    print() # 줄바꿈용

else:        
    # 무작위 섞기
    random.shuffle(names)

    # 조 나누기
    teams = [[] for _ in range(num_teams)]

    for i in range(num_teams):
        # teams[i].append()
        teams[i].append(names.pop()) # pop() : 리스트의 맨 마지막 원소를 teams 리스트에 append하고 해당 원소는 삭제
        
    index = 0

    # 리스트에 이름이 남아있는 동안 계속 반복
    while names:
        # 리스트의 맨 마지막 요소를 꺼내오고, 그 요소는 원본 리스트에서 삭제. (끝에서부터 한 명씩 뽑는 셈.)
        teams[index % num_teams].append(names.pop())
        index += 1
        
    print("\n--- 조 편성 결과 ---")
    for i, team in enumerate(teams):
        print(f"{i + 1}조: {" | ".join(team)} (총 {len(team)}명)")