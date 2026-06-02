## 一、核心概念 
- PCA：主成分分析，用于*特征冗余分析、降维、特征重要性评估*。 
- **核心思想**：找到一组*正交新坐标轴*，使数据在新轴上方差从大到小排列，保留主要信息。 
- *关键定义* 
	- 行 = 样本 
	- 列 = 特征/维度 
	- 方差 = 信息量大 
	- 特征值 λ = 某方向的方差大小 
	- 特征向量 v = 新坐标轴的方向 
--- 
## 二、标准计算步骤（固定 5 步） 
给定数据矩阵 $X \in \mathbb{R}^{N \times D}$ 
1. 中心化 $X_c = X - \mu，\mu$ 为每列均值 
2. 计算协方差矩阵 $\Sigma = \frac{1}{N-1}X_c^\top X_c$ 
3. 特征值分解$\Sigma v = \lambda v$ 解方程：$\det(\Sigma - \lambda I) = 0$ 
4. 排序 按λ 从大到小 排列，得到 PC1、PC2、PC3… 
5. 投影（降维） $Z = X_c \cdot V$，保留前 m 个主成分 
--- 
## 三、关键公式与规则 
1. 2×2 行列式 $\begin{vmatrix}a&b\\c&d\end{vmatrix}=ad-bc$ 
2. 3×3 行列式$a(ei−fh)−b(di−fg)+c(dh−eg)$ 
3. 单位矩阵 I 仅对角线为 1，其余为 0 → λ 只出现在对角线 
4. *方差贡献率* 单PC：$\frac{\lambda_i}{\sum\lambda}$ 累计：$\sum_{k=1}^m\frac{\lambda_k}{\sum\lambda}$
5. *降维原则* 保留累计方差 ≥ **95%** 的前 m 个主成分
--- 
## 四、特征值 λ 的意义 
- λ 越大：该方向方差越大、信息越多、越重要 
- λ=0：该方向无信息，可直接丢弃 
- 排序：*λ 最大 = PC1（第一新维度）*
--- 
## 五、特征向量 v 的意义 
- 特征向量 = 新坐标轴方向 
- 每个数字 = 对应**原始特征的权重 
- 符号： - 同号 → 正相关 - 异号 → 负相关 
- 示例： 
	- v=[1,1] → 两特征同等重要、正相关 
	- v=[1,2,3] → 特征3权重最高 
--- 
## 六、PCA 两大用途
### 1. 降维 
- 扔掉 λ 小的主成分 
- 用更少维度保留 ≥95% 信息
- 不丢失核心规律 
### 2. 特征重要性评估 
- 看 **PC1 特征向量的权重** - 权重绝对值越大 → 该原始特征越重要
## 七 代码示例

```python
import numpy as np 
from sklearn.decomposition import PCA 
from sklearn.preprocessing import StandardScaler 
import matplotlib.pyplot as plt 
import seaborn as sns 
# ===================== 0. 生成模拟数据（严格匹配AF2BIND论文特征结构） ===================== 
# 论文参数：67个蛋白 → 21322个残基样本，每个样本 20个诱饵氨基酸 × 256维pair特征 
n_samples = 21322 # 样本数：残基数量 
n_baits = 20 # 诱饵氨基酸数量（固定20） 
n_feat = 256 # 每个pair的特征维度（固定256） 
# 生成模拟特征：(样本数, 20诱饵, 256维) 
np.random.seed(42) # 固定随机种子，结果可复现 
pair_features = np.random.randn(n_samples, n_baits, n_feat) * 0.8 + 0.2 
# 模拟真实特征分布 
# ===================== 任务1：5120维全特征PCA（论文：特征冗余性分析） ===================== 
print("="*60) 
print("【步骤1】5120维全特征 PCA 分析（验证特征冗余）") 
print("="*60) 
# 1. 展平特征：(21322, 20, 256) → (21322, 5120) 20×256=5120 
features_flat = pair_features.reshape(n_samples, -1) 
# 2. 标准化（PCA必须步骤） 
scaler = StandardScaler() 
features_scaled = scaler.fit_transform(features_flat) 
# 3. PCA拟合 
pca_full = PCA() 
pca_full.fit(features_scaled) 
# 4. 计算累计方差贡献率（论文核心指标：95%方差需要多少主成分） 
cumulative_variance = np.cumsum(pca_full.explained_variance_ratio_) 
n_95 = np.argmax(cumulative_variance >= 0.95) + 1 
# 覆盖95%方差的PC数量 
# 输出论文式结论 
print(f"✅ 覆盖95%方差需要 前 {n_95} 个主成分") 
print(f"✅ 5120维原始特征存在大量冗余（需要大量PC覆盖方差）\n")
```
