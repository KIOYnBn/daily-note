# 用途
* 频繁在列表添加元素， 同时不频繁访问元素时可替代普通列表
# 用法
```python
from collections import deque
lst:list = [1,2, 3]
d_lst = deque(lst)

dq.append(4)       # 末尾添加，O(1)
dq.appendleft(0)   # 开头添加，O(1)
dq.pop()           # 末尾弹出，O(1)
dq.popleft()       # 开头弹出，O(1)
```

| 方法                     | 说明                |
| ---------------------- | ----------------- |
| `append(x)`            | 尾部添加元素 `x`        |
| `appendleft(x)`        | 头部添加元素 `x`        |
| `pop()`                | 尾部删除元素，返回该元素      |
| `popleft()`            | 头部删除元素，返回该元素      |
| `extend(iterable)`     | 尾部扩展可迭代对象         |
| `extendleft(iterable)` | 头部扩展可迭代对象（元素顺序反转） |
| `clear()`              | 清空双端队列            |

# 与普通list对比
## 时间复杂度对比

| 操作                         | `list`        | `deque`              |
| -------------------------- | ------------- | -------------------- |
| 索引访问（`list[i]`）            | O(1)          | O(1)（但常数较大，实际比list慢） |
| 在末尾添加/弹出（append/pop）       | O(1) 均摊       | O(1)                 |
| 在开头添加/弹出（insert(0)/pop(0)） | O(n)（需移动所有元素） | O(1)                 |
| 在中间插入/删除                   | O(n)          | O(n)（需要遍历到中间位置）      |
| 查找元素（in操作）                 | O(n)          | O(n)                 |