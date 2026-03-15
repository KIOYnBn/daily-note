```python
import os
print('hellow')
```
# 分子读取

```python
from rdkit import Chem

mol = Chem.MolFromSmiles('Cc1ccccc1')
mol1 = Chem.FromMolFile('data/input.mol')
mols = Chem.SDMolSupplier('mols.sdf')

```

# 分子转化成SMILES

```python
from rdkit import Chem
mol = Chem.MolFromSmiles('Cc1cccc1')
smiles = Chem.MolToSmiles(mol)

```

# 分子写入文件

```python
from rdkit import Chem
with Chem.SDWriter('mols.sdf') as w:
	w.write(m)

```

# 分子可视化
```python
from rdkit import Chem

mol = Chem.MolFromSmiles('Cc1cccc1')
img = Chem.Draw.MolToImage(mol)
```

# 特征提取

## 结构特征

### 三维坐标获取

```python
from rdkit.Chem import AllChem
from rdkit import Chem
mol = Chem.MolFromFile('mol.sdf')
mol = Chem.AddHs(mol)
params = Allchem.ETKDGv3()
params.randomSeed = 0xf00d
AllChem.EmbedMolecule(mol. params)
print(Chem.MolToMolBlock(mol))
mol = Chem.RemoveHs(mol)
print(Chem.MolToMOlBlock(mol))



```

```python
from rdkit import Chem  
from rdkit.Chem import AllChem  
from rdkit.Chem.rdMolTransforms import GetDihedralDeg  
  
# 生成分子  
mol = Chem.MolFromSmiles("C1CCCCC1")  
mol = Chem.AddHs(mol)  
  
# 生成3D构象  
mol_old = AllChem.EmbedMolecule(mol)  
print("构象ID:", mol_old)  # 输出构象ID（通常为0）  
  
# 力场优化  
mol_new = AllChem.MMFFOptimizeMolecule(mol)  
print("优化状态:", "成功" if mol_new == 0 else "失败")  
  
# 提取坐标  
conf = mol.GetConformer()  
print("原子坐标:")  
for i in range(mol.GetNumAtoms()):  
    pos = conf.GetAtomPosition(i)  
    print(f"Atom {i}: ({pos.x:.3f}, {pos.y:.3f}, {pos.z:.3f})")  
  
# 计算能量  
mol_props = AllChem.MMFFGetMoleculeProperties(mol)  
ff = AllChem.MMFFGetMoleculeForceField(mol, mol_props)  
print(f"优化能量: {ff.CalcEnergy():.4f} kcal/mol")  
  
# 验证环己烷构象  
dihedral = GetDihedralDeg(conf, 0, 1, 2, 3)  
print(f"二面角: {dihedral:.1f}°")
```

### 分子环信息获取

```python

from rdkit import Chem

# 原子
m.GetAtomWithIds(0).IsInRing()
# 健
m.GetBondWithIds(1).IsInRing()
```

### 可旋转健

```python
from rdkit.Chem import Draw  
  
mol = Chem.MolFromSmiles("CC(=O)Oc1ccccc1C(=O)O")  
for bond in mol.GetBonds():  
    if bond.GetBondType() == Chem.BondType.SINGLE and not bond.IsInRing():  
        print(f"可旋转键：原子 {bond.GetBeginAtomIdx()} - {bond.GetEndAtomIdx()}")  
  
Draw.MolToImage(mol)
```

## 化学特征

### 原子电荷获取
```python
from rdkit import Chem

m = Chem.MolFromSmiles('c1ccccc1C(=O))')
AllChem.ComputeGasteigerCharges(m)
charges = []
for atom in mol.GetAtoms():
	charge = atom.GetDoubleProp('_GasteigerCharge')
	charges.append((atom.GetIdx(), atom.GetSymbol(), charge))
    
```

# 蛋白质序列转化为SMILES

```python
sequence = "ACD"  
smiles = "".join([{"A":"CC(C)N", "C":"NC(C)C=S", "D":"NC(CCC(=O)[O-])"}[aa] for aa in sequence])  
# 输出：CC(C)NNC(C)C=SNC(CCC(=O)[O-])  
from rdkit import Chem  
mol = Chem.MolFromSmiles("CC(C)N")  # 丙氨酸  
print(Chem.MolToSmiles(mol))       # 输出标准化形式
```

# 氢键供体识别

```python
from rdkit import Chem  
  
mol = Chem.MolFromSmiles("CC(=O)Oc1ccccc1C(=O)O")  # 阿司匹林  
mol = Chem.AddHs(mol)  # 显式添加氢原子  
h_donors = []  
for atom in mol.GetAtoms():  
    # 判断是否为 O/N/S 且带 1 个氢  
    if atom.GetAtomicNum() in [7, 8, 16] and atom.GetTotalNumHs() == 1:  
        # 排除电荷异常（如带正电荷的 NH4+）  
        if abs(atom.GetFormalCharge()) < 0.1:  
            h_donors.append(atom.GetIdx())  
  
  
print("氢键供体原子索引及坐标：")  
print(h_donors)  
for idx in h_donors:  
    atom = mol.GetAtomWithIdx(idx)  
    pos = mol.GetConformer().GetAtomPosition(idx)  
    print(f"原子 {idx} ({atom.GetSymbol()}): 坐标 {pos:.3f}")
```

# PDB写入

```python
from rdkit import Chem  
from rdkit.Chem import AllChem  
smi='[nH]1CCCC1C(=O)[nH]1CCCC1C(=O)[nH]1CCCC1C(=O)[nH]1CCCC1C(=O)[nH]1CCCC1C(=O)[nH]1CCCC1C(=O)[nH]1CCCC1C(=O)'  
m2=Chem.MolFromSmiles(smi)  
m2 = Chem.AddHs(m2)  
  
AllChem.EmbedMultipleConfs(m2, numConfs=1)  
m3 = Chem.RemoveHs(m2)  
res = AllChem.MMFFOptimizeMoleculeConfs(m2)  
writer = Chem.PDBWriter('1.pdb')  
writer.write(m2)  
writer.close()
```

```python
from rdkit import Chem  
from rdkit.Chem import AllChem  
  
smi = '[nH]1CCCC1C(=O)[nH]1CCCC1C(=O)[nH]1CCCC1C(=O)[nH]1CCCC1C(=O)[nH]1CCCC1C(=O)[nH]1CCCC1C(=O)[nH]1CCCC1C(=O)'  
  
# 从SMILES生成分子并添加氢原子  
m2 = Chem.MolFromSmiles(smi)  
m2 = Chem.AddHs(m2) # 添加氢原子对于生成3D构象很重要:cite[4]  
  
# 生成并优化3D构象  
AllChem.EmbedMultipleConfs(m2, numConfs=1)  
# 使用力场优化生成的构象:cite[4]  
res = AllChem.MMFFOptimizeMoleculeConfs(m2)  
  
# 设置残基信息（以PRO为例）  
for atom in m2.GetAtoms():  
    # 设置残基名称、序号等，这里以PRO B 40为例  
    atom_info = atom.GetMonomerInfo()  
    print(atom.)  
    if atom_info is None:  
        # 如果原子没有MonomerInfo，则创建它。这里需要您根据实际原子类型映射到具体的氨基酸原子名称(CA, CB, N, C, O等)  
        # 注意：以下是一个示例，您需要根据实际分子结构为每个原子设置正确的名称  
        # 由于您的分子是一个多聚体，直接完全对应到PRO氨基酸的原子名称(CA, CB等)可能不适用。  
        # 更常见的做法是将其视为一个有机小分子配体（HETATM），或者如果您确实想将其模拟为氨基酸链，需要复杂的映射。  
        # 此处先以设置残基名和序号为例：  
        new_info = Chem.AtomPDBResidueInfo(  
            atomName = f" {atom.GetSymbol():<3}", # 原子名，需要根据实际情况调整，此处为简易设置  
            serialNumber = atom.GetIdx() + 1,  
            residueName = "UNL", # 残基名，对于未知分子常用UNL (UNKnown Ligand)  
            residueNumber = 1,  
            chainId = "A"  
        )  
        atom.SetMonomerInfo(new_info)  
    # 如果已有MonomerInfo，可以类似地进行修改  
  
# 写入PDB文件  
writer = Chem.PDBWriter('1.pdb')  
writer.write(m2)  
writer.close()
```