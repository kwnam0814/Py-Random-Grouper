# Python 기반 무작위 조 편성 프로그램

## 핵심 기능 (Key Features)
- Dynamic Partitioning : 전체 인원수와 사용자가 원하는 조의 개수를 바탕으로 균등하게 팀을 분배
- Validation Logic : 예외 상황(조 개수 오류, 최소 인원 미달)에 대한 방어 코드(Error Handling)를 구현
- Randomized Allocation: random.shuffle 및 pop() 메서드를 활용하여 데이터의 중복 없는 완전 무작위성을 보장

## 기술 스택 (Tech Stack)
- Language: Python 3.x
- Library: random (Standard Library)

## 로직 설명 (How It Works)
1. Input Validation :
    - **len(names) < num_teams * 2** 조건을 통해 한 조에 최소 2명 이상 배치되도록 제한하는 비즈니스 로직을 적용
2. Algorithm :
    - 먼저 각 팀에 1명씩 우선 배정하여 빈 팀이 생기지 않도록 보장
    - 나머지 인원은 **while 루프**와 **index % num_teams**을 활용해 순환하며 공평하게 분배
    - **pop() 메서드**를 사용하여 메모리 효율적으로 리스트 데이터를 처리

## Execution Example (실행 예시)
```shell
현재 총 인원은 20명입니다. 몇 개의 조로 나눌까요? [숫자만 입력]: 4

--- 조 편성 결과 ---
1조: 강ㅅ☆ | 이ㅈ☆ | 주ㅎ☆ | 박ㅅ☆ | 최ㅇ☆ (총 5명)
2조: 김ㅅ☆ | 남ㄱ☆ | 배ㅇ☆ | 서ㅎ☆ | 이ㅊ☆ (총 5명)
3조: 박ㅈ☆ | 사ㅂ☆ | 이ㅅ☆ | 하ㅈ☆ | 한ㄷ☆ (총 5명)
4조: 김ㅇ☆☆ | 김ㅈ☆ | 이ㅅ☆ | 주ㅎ☆ | 황ㅎ☆ (총 5명)