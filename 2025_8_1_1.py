def count_symmetric_integers(low: int, high: int) -> int:
    count = 0
    for num in range(low, high + 1):
        s = str(num)
        length = len(s)
        # 只有偶数位的数字才可能是对称整数
        if length % 2 != 0:
            continue
        n = length // 2
        # 计算前半部分和后半部分的数字之和
        sum_first = sum(int(c) for c in s[:n])
        sum_second = sum(int(c) for c in s[n:])
        if sum_first == sum_second:
            count += 1
    return count

# 测试示例
print(count_symmetric_integers(1, 100))      # 输出: 9
print(count_symmetric_integers(1200, 1230))  # 输出: 4
