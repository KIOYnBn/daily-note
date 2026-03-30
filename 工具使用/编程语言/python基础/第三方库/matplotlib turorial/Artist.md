# 常见的Artist及其创建方法

| Artist            | Axes辅助方法 |
| ----------------- | -------- |
| Annotation        | annotate |
| rectangle         | bar      |
| lline2d/rectangle | errorbar |
| polygon           | fill     |
| rectangle         | hist     |
| AxesImage         | imshow   |
| line2d            | plot     |
| polycollection    | scatter  |
| 文本                | text     |

---
# 更改Artist属性
* Artist.set
* 示例
```python
{
fig, ax = plt.subplots(figsize=(4, 2.5)
x = np.arange(0, 13, 0.2)
y = np.sin(x)
lines = ax.plot(x,y, '-', label="example', linewidth=0.2, color="blue")
line[0].set(color="green", linewidth=2)
```

---
# 查看Artist完整属性
matplolib.artist.getp

# 更改Artist数据
* set_data
* 示例
```python
{
fig, ax = plt.subplots(figsize=(4, 2.5))
x = np.arange(0, 13, 0.2)
y = np.sin(x)
lines = ax.plot(x, y, '-', label="example")
lines[0].set_ddata([x, np.cos(x)])
}
```

---
# 手动添加Artist
* 某些Artist没有axes辅助方法，需要手动添加
* axes.Axes.add_artist
* 示例
```python
{
import matplotlib.patches as mpatches

fig, ax = plt.subplots(figsize=(4, 2.5))
circle = mpatches.Circle((0.5, 0.5), 0.25, ec="none")
ax.add_artist(circle)
}
```

---
# 移除Artist
* remove
---
