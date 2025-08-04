import math
from typing import List

def solve(balls: List[int]) -> int:
    """
    计算为了让所有非空袋子中的玻璃球数量相等，需要拿出的最少玻璃球数量。

    Args:
      balls: 一个整数列表，代表每个袋子里的玻璃球数量。

    Returns:
      需要拿出的最少玻璃球总数。
    """
    if not balls:
        return 0

    # 候选的目标值 T 包括所有不重复的初始球数，以及 0
    possible_targets = set(balls)
    possible_targets.add(0)

    min_removals = float('inf')

    # 遍历每一个可能的目标值 T
    for target in possible_targets:
        current_removals = 0
        # 计算以当前 target 为目标时，需要拿出的总数
        for ball_count in balls:
            if ball_count > target:
                # 如果球数多于目标值，拿出多余部分
                current_removals += (ball_count - target)
            elif ball_count < target:
                # 如果球数少于目标值，只能将该袋清空
                current_removals += ball_count
        
        # 更新全局的最小值
        min_removals = min(min_removals, current_removals)

    return min_removals

# --- 测试用例 ---
# 示例 1
balls1 = [4, 1, 6, 5]
output1 = solve(balls1)
print(f"输入: {balls1}")
print(f"输出: {output1}")  # 预期输出: 4

print("-" * 20)

# 示例 2
balls2 = [2, 10, 3, 2]
output2 = solve(balls2)
print(f"输入: {balls2}")
print(f"输出: {output2}")  # 预期输出: 7