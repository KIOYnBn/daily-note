* OOP核心特性： 封装， 继承， 多态

---
# 基本概念
| 对比维度 | 类属性                     | 实例属性                         |
| ---- | ----------------------- | ---------------------------- |
| 定义位置 | 类内部，方法外部                | 类内部的 `__init__` 方法中（或对象动态添加） |
| 访问方式 | 类.类属性、对象.类属性            | 对象.实例属性（类无法访问实例属性）           |
| 共享性  | 所有对象共享，一个对象修改类属性，其他对象可见 | 每个对象独有，对象之间的实例属性相互独立         |
| 内存占用 | 仅占用一份内存，节省空间            | 每个对象占用一份内存，对象多时占用空间大         |

|对比维度|实例方法|类方法|静态方法|
|---|---|---|---|
|装饰器|无（默认）|`@classmethod`|`@staticmethod`|
|默认参数|`self`（指代当前实例对象）|`cls`（指代当前类）|无默认参数|
|访问属性|可访问实例属性和类属性|仅可访问类属性（不可访问实例属性）|不可访问实例属性和类属性（独立于类和实例）|
|调用方式|对象.方法名()、类.方法名(对象)|类.方法名()、对象.方法名()|类.方法名()、对象.方法名()|
|核心作用|操作实例属性，实现对象的特有行为|操作类属性，实现与类相关的功能|实现与类和对象无关的通用功能，提高代码复用|

---
# 封装
* `"_"`： 浅度封装， 外部依然可以访问
* `"__"`：深度封装， 外部只能通过`对象._类名__属性名`访问
* `@property`： 装饰器封装。用于将方法”伪装成属性“

## property
* 用法
	1. `@property`：将方法变为属性
		* 定义访问器，用于获取私有属性的值，调用时无需加括号（像访问普通属性一样）。
	2. `@属性名.setter`：定义修改器，用于修改私有属性的值，赋值时直接使用「对象.属性名 = 值」。
		* 数据验证
	3. 配套用法——Deleter——清理
```python
class User:
	def __init__(self, age):
		self._age = None
		self.age = age # 当给age赋值时调用
	@property
	def age(self):
		return self._age
	@age.setter
	def age(self, value):
		if value < 0 or value > 150:
			raise ValueError("年龄必须在0~150之间")
		self._age = value
	@age.deleter
	def age(self):
		print("正在删除age属性")
		self._age = None

user = User(25)
del user.age
```

### 动态获取对象
* getattr(object, name, default)
	* 优点： 相对于object.name， 可以通过变量名动态获取
	* object： 对象
	* name： 变量名
	* default： 变量名不存在时返回的值
```python
attr_name = "age"
value = getattr(person, attr_name)

for attr in ["name", "age"]
	value = getattr(person, attr)
```
### 动态设置对象
* setattr(object, name, value)
	* 等同于obj.name = value

---
# 继承
## 继承的方法
* 单继承：`class 子类名(父类名)`
* 多继承： `class 子类名(父类1， 父类2...)`
	* 多继承时， 方法解析顺序原则
		1. 子类优先父类
		2. 左父类优先右父类
* super()函数：调用父类构造方法(`__init__`)， 初始化父类属性
	* 用法： `super().__init__(参数)`

---

# 类的魔法方法
* 以「双下划线开头+双下划线结尾」的方法。无需手动调用，会在特定场景下自动触发执行
* 常见的魔法方法
<table>
	<tr>
		<th>魔法方法</th>
		<th>介绍</th>
	</tr>
	<tr>
		<th>__init__(self)</th>
		<th>实例化对象时自动触发</th>
	</tr>
	<tr>
		<th>__del__(self)</th>
		<th>销毁对象时触发</th>
	</tr>
	<tr>
		<th>__str__(self)</th>
		<th>调用print(对象), str(对象)时触发</th>
	</tr>
	<tr>
		<th>__repr__(self)</th>
		<th>调用repr(对象)触发</th>
	</tr>
	<tr>
		<th>__call__(self)</th>
		<th>将对象当作函数调用时触发</th>
	</tr>
	<tr>
		<th>__eq__(self, other)</th>
		<th>调用==比较俩个对象时触发</th>
	</tr>
</table>

---
## __call__
### 基本用法
* 作用： 将实例变成可调用对象
	* callable(object): 检查对象是否可调用
```python
class MyClass:
	def __call__(self):
		print("我被调用了")
	
obj = MyClass()
obj()
```

### 常见用途
#### 计数器
```python
class Counter:
	def __init__(self):
		self.count = 0
	def __call__(self):
		self.count += 1
		return self.count
		
c = Counter()
for i in range(10):
	print(c())
```
#### 类装饰器
```python
class Timer:
	def __init__(self, func):
		self.func = func
	def __call__(self):
		print("开始计时")
		self.func()
		print("结束计时")
	@Timer
	def task():
		print("执行任务")
		
task()
```

