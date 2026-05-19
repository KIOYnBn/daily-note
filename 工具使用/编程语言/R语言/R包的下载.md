## 来源
### 在线下载
```R
# CRAN： 官方仓库
install.packages("包名") 

# 专注生物信息学Bioconductor
install.packages("BiocManager")
BiocManager::install("包名")

# Github
install.packages("devtools")
devtools::install_github("包名")
```
### 本地下载
```mermaid
graph LR
	A[tools]-->B[install packages]-->C[tar.gz]
```
## 调用
```R
library("包名")
```
## 查看帮助
```R
help("包名")
```
## 移除包
右下角的"Packages"
## 更新包
```R
update.packages("包名")
```
