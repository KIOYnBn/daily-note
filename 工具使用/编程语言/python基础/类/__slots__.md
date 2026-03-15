* 作用： 大量创建对象时减少内存占用
* 注意事项
	* 类中的self变量需要在slots中声明， 不可动态添加元素
* 示例
```python
class student:
	__slots__ = ('student_id', 'name', 'age', 'score')
	def __init__(self, sid, name, age, score):
		self.student_id = sid
		self.name = name
		self.age = age
		slef.score = score
```
