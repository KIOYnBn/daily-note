# 特征器
## 分子特征化器
### OneHotFeaturizer

```python
>>> import deepchem as dc
>>> featurizer = dc.feat.OneHotFeaturizer()
>>> smiles = ['CCC']
>>> encodings = featurizer.featurize(smiles)
>>> type(encodings[0])
<class 'numpy.ndarray'>
>>> encodings[0].shape
(100, 35)
>>> featurizer.untransform(encodings[0])
'CCC'
```

### 计算原子坐标

```python
>>> import deepchem as dc
>>> from rdkit import Chem
>>> mol = Chem.MolFromSmiles('C1C=CC=CC=1')
>>> n_atoms = len(mol.GetAtoms())
>>> n_atoms
6
>>> featurizer = dc.feat.AtomicCoordinates(use_bohr=False)
>>> features = featurizer.featurize([mol])
>>> type(features[0])
<class 'numpy.ndarray'>
>>> features[0].shape # (n_atoms, 3)
(6, 3)
```

### 库伦矩阵

库仑矩阵提供了电子结构的表示 一个分子。对于具有N个原子的分子，库仑矩阵是一个N×N矩阵，其中每个元素给出 两个原子之间的静电相互作用。该方法如下描述 更详细的见[[1]_](https://deepchem.readthedocs.io/en/latest/api_reference/featurizers.html#id202)。

```python
>>> import deepchem as dc
>>> featurizers = dc.feat.CoulombMatrix(max_atoms=23)
>>> input_file = 'deepchem/feat/tests/data/water.sdf' # really backed by water.sdf.csv
>>> tasks = ["atomization_energy"]
>>> loader = dc.data.SDFLoader(tasks, featurizer=featurizers)
>>> dataset = loader.create_dataset(input_file)
```

### Mol2Vec指纹

需要安装mol2vec。

```python
>>> import deepchem as dc
>>> from rdkit import Chem
>>> smiles = ['CCC']
>>> featurizer = dc.feat.Mol2VecFingerprint()
>>> features = featurizer.featurize(smiles)
>>> type(features)
<class 'numpy.ndarray'>
>>> features[0].shape
(300,)
```

### MATFeaturizer

该类是分子注意力变换器的特征化器。返回的值是一个numpy数组，由分子图描述组成：
> - 节点特性
> - 邻接矩阵
> - 距离矩阵


```python
>>> import deepchem as dc
>>> feat = dc.feat.MATFeaturizer()
>>> out = feat.featurize("CCC")
```

### RDKitConformerFeaturizer

将RDKit的mol对象特征化为带有3D坐标的GraphData对象。三维坐标表示在形状为 [num_atoms * num_conformers， 3] 的 GraphData 对象的 node_pos_features 属性中。

ETKDGv2算法用于生成该分子的三维坐标。

```python
>>> from deepchem.feat.molecule_featurizers.conformer_featurizer import RDKitConformerFeaturizer
>>> featurizer = RDKitConformerFeaturizer()
>>> molecule = "CCO"
>>> conformer = featurizer.featurize(molecule)
>>> print (type(conformer[0]))
<class 'deepchem.feat.graph_data.GraphData'>
```

#### DMPNNFeaturizer

默认节点表示通过串接以下数值构建，特征长度为133。
- 原子数：该原子的单热矢量，原子范围为前100个。
- 度数：该原子度数（0-5）的单热矢量。
- 形式电荷：整数电子电荷，-1，-2,1,2,0。
- 手性：该原子手性标签（0-3）的单热矢量。
- 氢数：该原子连接的氢数（0-4）的单热向量。
- 杂交：单热向量的“SP”、“SP2”、“SP3”、“SP3D”、“SP3D2”。
- 芳香族：一个单热向量，判断原子是否属于芳香环。
- 质量：原子质量 * 0.01
默认边表示是通过串接以下数值构建的， 而本片时长为14。
- 键型：键型的单热矢量，“单”、“双”、“三”或“芳香”。
- 同环：一热向量，判断该一对原子是否属于同一环。
- 共轭：判断该键是否共轭的单热矢量。
- 立体声：键合体体态（0-5）的单热矢量。

```python
>>> smiles = ["C1=CC=CN=C1", "C1CCC1"]
>>> featurizer = DMPNNFeaturizer()
>>> out = featurizer.featurize(smiles)
>>> type(out[0])
<class 'deepchem.feat.graph_data.GraphData'>
>>> out[0].num_nodes
6
>>> out[0].num_node_features
133
>>> out[0].node_features.shape
(6, 133)
>>> out[0].num_edge_features
14
>>> out[0].num_edges
12
>>> out[0].edge_features.shape
(12, 14)
```

### 等变图特征器
等变图神经网络特征化器。
该特征化器构建分子结构的图表示， 捕捉原子特征、成对距离和空间位置。这些 特征针对QM9数据集的等变模型进行定制
功能包括： - **节点特性**：原子一热编码及附加描述符。 - **边缘特征**：原子对之间的矢量位移。 - **边权重**：单热编码中的离散化成对距离。 - **原子坐标**：原子的三维位置。

```python
>>> from rdkit import Chem
>>> import deepchem as dc
>>> mol = Chem.MolFromSmiles('CCO')
>>> featurizer = dc.feat.EquivariantGraphFeaturizer(fully_connected=True, embeded=True)
>>> features = featurizer.featurize([mol])
>>> type(features[0])
<class 'deepchem.feat.graph_data.GraphData'>
>>> features[0].node_features.shape  # (N, F)
(3, 6)
```

### MolGraphConvFeaturizer

该类是分子一般图卷积网络的特征化器。
基于 [WeaveNet 论文](https://arxiv.org/abs/1603.00856)。
默认节点表示是通过串接以下值构建的， 长片长度为30。
- 原子类型：该原子的单热矢量，“C”、“N”、“O”、“F”、“P”、“S”、“Cl”、“Br”、“I”、“其他原子”。
- 形式电荷：整数电子电荷。
- 杂交：一个单热向量的“sp”、“sp2”、“sp3”。
- 氢键：用一热方式判断该原子是氢键供体还是受体。
- 芳香族：一个单热向量，判断原子是否属于芳香环。
- 度数：该原子度数（0-5）的单热矢量。
- 氢数：该原子连接的氢数（0-4）的单热向量。
- 手性：手性“R”或“S”的单热向量。（可选）
- 部分电荷：计算出的部分电荷。（可选）
默认边表示通过串接以下数值构建，特征长度为11。
- 键型：键型的单热矢量，“单”、“双”、“三”或“芳香”。
- 同环：一热向量，判断该一对原子是否属于同一环。
- 共轭：判断该键是否共轭的单热矢量。
- 立体：键合立体配置的单热矢量。

```python
>>> smiles = ["C1CCC1", "C1=CC=CN=C1"]
>>> featurizer = MolGraphConvFeaturizer(use_edges=True)
>>> out = featurizer.featurize(smiles)
>>> type(out[0])
<class 'deepchem.feat.graph_data.GraphData'>
>>> out[0].num_node_features
30
>>> out[0].num_edge_features
11
```

### ConvMolFeaturizer

```python
>>> import deepchem as dc
>>> smiles = ["C", "CCC"]
>>> featurizer=dc.feat.ConvMolFeaturizer(per_atom_fragmentation=False)
>>> f = featurizer.featurize(smiles)
>>> # Using ConvMolFeaturizer to create featurized fragments derived from molecules of interest.
... # This is used only in the context of performing interpretation of models using atomic
... # contributions (atom-based model interpretation)
... smiles = ["C", "CCC"]
>>> featurizer=dc.feat.ConvMolFeaturizer(per_atom_fragmentation=True)
>>> f = featurizer.featurize(smiles)
>>> len(f) # contains 2 lists with  featurized fragments from 2 mols
2
```