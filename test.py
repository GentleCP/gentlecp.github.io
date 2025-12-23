# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test
   Description :
   Author :       GentleCP
   date：          2025/10/18
-------------------------------------------------
   Change Activity:
                  
-------------------------------------------------
"""

from collections import deque
def min_transfers(a, b):
    # BFS队列，元素是当前城市和步数
    queue = deque([(a, 0)])
    visited = set([a])
    while queue:
        current_city, steps = queue.popleft()
        # 如果已经到达目标城市
        if current_city == b:
            return steps
        # 生成所有可能的下一步
        next_cities = [current_city * 2, current_city // 2, current_city + 1]

        for next_city in next_cities:
            if next_city not in visited:
                visited.add(next_city)
                queue.append((next_city, steps + 1))
    return -1  # 如果无法到达（理论上不会发生）
# 输入
a, b = map(int, input().split())

# 输出最少传送次数
print(min_transfers(a, b))
