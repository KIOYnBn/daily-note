GLU: Gate Linear Unit.门控线性单元
## 1. 数学原理
$$\text{GLU}(X) = X_1 \odot \sigma(X_2$$
符号说明
$$\begin{align*}
&X:输入张量， 通道维度长度为2d。\\
&X_1, X_2：沿通道维度均分获得两个子张量，维度为d。 \\
&X_1为主特征分量， X_2为特征权重。\\
&\sigma：Sigmoid激活函数.\sigma(x)=\frac{1}{1+e^{-x}} \\
&\bigodot:逐元素相乘 \\
\end{align*}$$

## 2. 代码实现
```python
import torch.nn.functional as F
F.glu(x, dim=1)
```
## 3. 代码示例
[[Conv1D+GLU]]
## 4. 拓展变体
- ReGLU：将 Sigmoid 替换 ReLU
$$\text{ReGLU}=X_1\odot\text{ReLU}(X_2)$$
- SwiGLU：结合 Swish 激活，广泛用于大语言模型