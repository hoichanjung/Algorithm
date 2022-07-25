# 문제 설명
# 수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

# 1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

# 제한 조건
# 시험은 최대 10,000 문제로 구성되어있습니다.
# 문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
# 가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.

def solution(answers):
    answer = []
    return answer

answers	= [1,2,3,4,5]	
# return [1]
print(solution(answers))

answers = [1,3,2,4,2]	
# return [1,2,3]
print(solution(answers))

answers = [1,2,3,4,5,1,2,3,4,5,]		

print(solution(answers))

tmp1 = [1,2,3,4,5]
tmp2 = [2,1,2,3,2,4,2,5]
tmp3 = [3,3,1,1,2,2,4,4,5,5]


tmp1_count = len([tmp1[i] for i in range(len(answers)) if tmp1[i] == answers[i]])
tmp2_count = len([tmp2[i] for i in range(len(answers)) if tmp2[i] == answers[i]])
tmp3_count = len([tmp3[i] for i in range(len(answers)) if tmp3[i] == answers[i]])

count1 = 0
count2 = 0
count3 = 0

for i in range(len(answers)):
    tmp1_idx = i % 5
    tmp2_idx = i % 8
    tmp3_idx = i % 10

    if tmp1[tmp1_idx] == answers[i]:
        count1 += 1
    elif tmp2[tmp2_idx] == answers[i]:
        count2 += 1
    elif tmp1[tmp1_idx] == answers[i]:
        count1 += 1