## 1. 数学原理
Layernorm: 层归一化
作用： **分布矫正**：对 D 维特征做均值归零、方差归一
$$\text{LN}(x) = \frac{x-\mu}{\sigma}\cdot \gamma + \beta$$
只改变数值分布，**不压缩、不删除任何维度信息**
用途：**稳定训练**，让深层网络收敛更快
## 2. 代码实现
```python
import torch
self.ln = nn.LayerNorm(hid_dim)
```
## 3. 示例