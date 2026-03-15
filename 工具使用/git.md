# 基础流程
```
创建仓库: git init
添加内容： git add .
提交: git commit -m "description"
设置远程仓库: git remote add 自定义名称 url(http/ssh)
查看令牌文件: ls -a ~/.ssh
创建新令牌文件： ssh-keygen -t rsa -C "youremail@example.com" -f ~/.ssh/自定义令牌问价名称
添加令牌到ssh： vim ~/.ssh/config
	添加
		Host github.com
			HostName ssh.github.com
			Port 433
			User git
			IdentityFile ~/.ssh/配置文件的名字

提交远程仓库: git push -u 自定义名称
```


# 进阶
feat: new feature
fix: fix bug
docs： document
refactor： reaconstruction
test： test
```
---
# branch
* check branch： git branch
* create branch： git branch dev
* switch branch： git checkout dev or git switch dev
* merge branch： git merge dev
---
# revocation
* working area revocation: git checkout -- file.txt
* temp region revocation: git reeset HEAD file.txt
* commit revocation: git revert commit 
----
# work flow
* main: stable version
* develop: daily development
* feature
* release
* hotfix: fix
