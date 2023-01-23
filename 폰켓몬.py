def solution(nums):
    answer = 0
    _len = len(nums)
    distinct_len= len(set(nums))
    
    if distinct_len >= _len // 2:
        return _len//2
    else:
        return distinct_len #[3,3,3,2,2,2] -> [2,3] +2 or [2,3] + 3
    
