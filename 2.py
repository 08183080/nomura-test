from typing import List


def solution(A: List[int]) -> int:
    choices = set()
    length = len(A)
    for i in range(length - 1):
        choices.add(A[i] + A[i+1])
    # print(choices)
    choices = list(choices)
    # print(choices)

    ans = 1
    for choice in choices:
        i = 0
        cnt = 0
        while i < length - 1:
            if A[i] + A[i+1] == choice:
                cnt += 1
                # i += 2
                # print(f'{choice} -> {i}')
                i += 2
                if i >= length:
                    break
            else:
                i += 1
        ans = max(ans, cnt)
    return ans


if __name__ == "__main__":
    A1 = [9, 9, 9, 9, 9] 
    A2 = [10, 1, 3, 1, 2, 2, 1, 0, 4]
    A3 = [5, 3, 1, 3, 2, 3]
    A4 = [1, 5, 2, 4, 3, 3]

    assert solution(A1) == 2
    assert solution(A2) == 3
    assert solution(A3) == 1
    assert solution(A4) == 3
    # print(solution(A2))
    