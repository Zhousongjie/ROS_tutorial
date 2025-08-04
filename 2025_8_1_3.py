from collections import Counter
from typing import List

def minimumOperations(nums: List[int]) -> int:
    n = len(nums)
    if n == 1:
        return 0
    
    # 统计偶数索引和奇数索引的数字频率
    even_counts = Counter(nums[::2])
    odd_counts = Counter(nums[1::2])
    
    # 获取频率最高的两个数字及其频率
    even_top = even_counts.most_common(2)
    odd_top = odd_counts.most_common(2)
    
    # 处理可能的不足两个的情况
    if len(even_top) == 1:
        even_top.append((None, 0))
    if len(odd_top) == 1:
        odd_top.append((None, 0))
    
    # 尝试两种可能的模式
    min_ops = float('inf')
    
    # 模式1：偶数索引为even_top[0][0]，奇数索引为odd_top[0][0]
    a, a_cnt = even_top[0]
    b, b_cnt = odd_top[0]
    if a != b:
        ops = (n + 1) // 2 - a_cnt + n // 2 - b_cnt
        min_ops = min(min_ops, ops)
    else:
        # 如果a和b相同，尝试even_top[0]和odd_top[1]
        if odd_top[1][0] is not None:
            b, b_cnt = odd_top[1]
            ops = (n + 1) // 2 - a_cnt + n // 2 - b_cnt
            min_ops = min(min_ops, ops)
        # 或者even_top[1]和odd_top[0]
        if even_top[1][0] is not None:
            a, a_cnt = even_top[1]
            b, b_cnt = odd_top[0]
            ops = (n + 1) // 2 - a_cnt + n // 2 - b_cnt
            min_ops = min(min_ops, ops)
    
    # 模式2：偶数索引为even_top[0][0]，奇数索引为odd_top[1][0]（如果与a不同）
    # 这部分已经在上面处理了
    
    # 另一种可能是even_top[1][0]和odd_top[0][0]（如果与b不同）
    # 这部分也在上面处理了
    
    # 还有一种可能是even_top[1][0]和odd_top[1][0]
    a, a_cnt = even_top[1]
    b, b_cnt = odd_top[1]
    if a != b:
        ops = (n + 1) // 2 - a_cnt + n // 2 - b_cnt
        min_ops = min(min_ops, ops)
    
    return min_ops

# 测试示例
print(minimumOperations([3, 1, 3, 2, 4, 3]))  # 输出应为3
print(minimumOperations([1, 2, 2, 2, 2]))    # 输出应为2