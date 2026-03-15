---
thesis_type: Review
tags:
  - 已阅读
---

# Content
## 主要内容
* 关于蛋白质的金属配位预测
	* 基于序列的模型
	* 基于结构的模型
* 关于蛋白质金属位点的功能
* 预测蛋白质配位的挑战
	* 蛋白质金属结合位点的混乱
		* 蛋白质能结合多个离子， 配位离子的物化特性又太过相似
	* 蛋白质金属位点在配位环境中作用不同， 太过复杂
	* 蛋白质结构的变化（动态区域）会掩盖金属结合位点
	* 人工蛋白设计——略读
## Chapter SEQUENCE-BASED PREDICTION OF METAL COORDINATION
* 序列基础模型
	* bindEmbed21DL [Littmannet al., 2021]
		* based on ProtT5
		* a fixed-length vector(embedding) for each protein's amino acid residue
	* mebipred [Aptekmann et al., 2022]
		* machine learning
		* from PDB
		* 金属结合位点5埃内残基为阳性
		* 提取220种特征
			* 氨基酸组成
			* 物理化学
			* 
	* MetalNet
		* machine learning
		* sequence and contact
		* CHED
		* metalnet2
* 数据库
	* RCSB(Reserach Collaboratory for structural Bioinformatics)
	* PDB
	* MESPEUS(MEtal Sites in Proteins at Edinburgh UniverSity)
	* MetalPDB