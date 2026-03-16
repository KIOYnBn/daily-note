# 数组
- 创建：
	- 创建指定数组：知道数组的每一个元素，如：np.array([1, 2, 3])   
	- 创建递增数组：np.arange(10)， np.arange(10, 20, 2)   
	- 创建同值数组：np.zeros((1, 3)) or np.ones((1,3))   
	- 创建随机数组：np.random.random(5)   
	- 正态分布：np.random.normal（0，1，（2，3））
		- 0指均值，1指标准差，（2，3）指形参
		- 和random函数的用法一致   
- 类型
	- 整型数组： Arr1 = np.array([1, 2, 3]）
	- 浮点型数组：Arr2 = np.array([1.0 , 2, 3]) or [1.0, 2.0, 3.0]
	- 布尔型数组：可以通过比较产生
	- Note： 
		1. 整型数组插入浮点数，浮点数小数会被截断
		2. 浮点数插入整型，整型升级称整数
- 条件运算符:           
	- &：与             
	- |：或           
	- ~：非           
- 数组的运算       
	- np.sum:       
	- np.any(arr)： 数组中有一个true就返回true
	- np.all(arr)： 数组中全是true才返回ture
- 数组类型转换
	-  np.astype()： arr2 = np.astype(int)
	- 通过计算转化： arr1+0.0
- 维度转化  
     - Np. reshape(形参)
         - 例如
             - Arr = np.arange(10)
             - arr2 = arr.reshape((1,10)
	 - 可以空一个参数填为-1，让系统计算.
		 - arr2 = arr.reshape((1,-1))
 - 数组的翻转
     - arr.T： 将横纵列转换
         - 例如：arr = array([[1, 2, 3], [4, 5, 6]])
     - np.flipud(arr)： 左右反转
     - np.fliplr(arr)： 上下反转
---
- 数组的计算
	 - 逐元素运算
	 - 运算符运算：
		 - arr2 =Arr + 1 = [1, 2, 3]
		 - 对每个元素都运算，其他运算符同理
     - 矩阵运算
         - arr3 = arr1+arr2
- 数组的访问
	 - Arr = np.array([1, 2, 3])
 - 多个元素访问（花式索引）：

     - arr[[a, b], [x, y]]

         - 指输入(a, x), (b, y)位置的元素

 - 以及切片操作，和字符串相似

---

数组的copy

 - 与普通的赋值和copy用法相同

 - Arr = np.arange(10)

 - arr1 = arr[:3].copy()

 - 没有deepcopy了

---

数组的拼接

 - 向量（一维数组）拼接

     - np.concatenate[arr, arr1]

 - 数组拼接

     - np.concatenate([arr, arr1], axis=0/1)#axis默认为0，为行拼接，1为列拼接

     - 数组和向量没法拼接

---

数组的分裂

 - np.split(arr, [x, y], axis=0/1)

 - [x, y] 表示指针

 - axis表示从横或纵轴分割 # 向量就不需要axis了

---

常见数学函数

 - np.abs(arr)：绝对值

 - np.sin(arr)

 - np.exp(x)

 - np.log(x)/np.log(2) = log2(x)

 - np.max(arr, axis=0/1)

     - Axis = 1时，对比不同行之间的数

     - min同理

     - 不写时求全体

 - np.sum(arr,axis=0/1)

     - 与max同理

     - 不写时求和

 - np.mean(arr,axis)：求均值

     - 同max

 - np.std(arr,axis)：求标准差

     - 同max

 - 安全版：大型数据可能有数据缺失，导致报错，可以在前nan使用安全版

     - 安全版会忽略缺失值

     - 如：np.nanmean

---

数组的条件选择

 - 直接比较

     - Arr = np.array([1, 2, 3, 4])

     - arr1 = arr[arr1] or arr[arrarr3]

         - 输出符合条件的

 - np.where(arr1)

 - 这两种方法输出的结果不一样

---

numpy和pytorch的转换

 - array对应tensor（张量）

     - array和tensor的转化

         - Ts = torchl.tensor(arr)

         - Arr = np.array(ts)