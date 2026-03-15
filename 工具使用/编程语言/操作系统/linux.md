# 虚拟机及linux learning

- 虚拟机快照：存档
    
- linux文件目录结构：
    
    ![](https://my.feishu.cn/space/api/box/stream/download/asynccode/?code=YTI2YzE0YmE4NGJiZjYxYjUyYjIwMGJjNjZjZDIyMTJfU0s2T2hLUXh1bEhmeFFla0tTckhiNE9pTUZCUDJhOTdfVG9rZW46Skc1NWJxNnd3b0g1Y254ZTZVbWNnYVg3bkpjXzE3NzIyNjUwNjk6MTc3MjI2ODY2OV9WNA)
    
- man命令：
    
    - 帮助手册
        
- ls命令：
    
    - 作用：查看文件夹内容
        
    - 格式：ls [options] [路径]
        
        - Options:
            
            - -l: 以列表形式列出，展示更多信息
                
            - -h: 展示问价大小单位，和-l搭配才能起效果
                
            - -a: 列出包括隐藏文件夹在内的所有文件
                
            - -R:子文件的文件也会列出来
                
            - -S: 以文件容量大小排序，ls默认以文件名排序
                
            - -t：以时间排序
                
- cd命令：
    
    - 作用：改变工作目录
        
    - 格式：cd [路径]
        
    - 默认回到home
        
    - 相对路径和绝对路径
        
        - 绝对路径：/home/ynbn-t，即完整路径
            
        - 相对路径：以当前所在目录为默认前缀，如，当前在/home/bin，打开bin中的firefox，可以写cd firefox(不必加/）
            
    - 特殊路径符
        
        - . = 代表当前路径，如cd ./firefox
            
        - .. = 回退上一级目录，../.. = 回退上两级目录，如 cd ..
            
        - ~ = 代表当前账户的home路径, 如 pwd = /bin, cd ~ , pwd = /home/ynbn-t
            
- pwd命令:
    
    - 作用：展示当前工作目录
        
    - 格式：pwd
        
- mkdir命令：
    
    - 作用：创建文件夹
        
    - 格式：mkdir [-p] 路径
        
    - -p：表示创建多级文件夹
        
- touch命令
    
    - 作用：创建文件
        
    - 格式:touch 路径，如：touch /ynbn-t/home/me.txt
        
- cat-more命令：
    
    - 作用：查看文件内容
        
    - 格式：cat（more） 文件路径
        
    - more可以翻页，适合内容较多的文件
        
- cp,mv,rm命令：
    
    - cp：即copy，复制文件或文件夹
        
        - 格式：cp [参数] 路径
            
        - 参数：
            
            - -r：递归，可以复制文件夹
                
            - -f:强制复制，不管目标文件是否存在
                
            - -i：覆盖文件前询问
                
            - -S：默认以“SUFFIX”代替默认后缀
                
            - -v：显示详细命令操作
                
    - mv：即move，移动文件（文件夹）
        
        - 格式：mv [参数] 路径
            
        - 参数：
            
            - -b：覆盖文件前为其备份
                
            - -i：询问
                
            - -u：当源文件比目标文件不存在或目标文件不存在才执行移动
                
    - rm：即remove，删除文件（文件夹）
        
        - 格式：rm [参数] 路径
            
        - 参数
            
            - -r:表示递归，删除文件夹。如果同时具有文件和文件夹，加上-r
                
                - 如果要删除文件夹test下的所有文件，可以使用：rm -r ./test/*
                    
            - 和cp的f，i，r，v参数相同
                
    - 通配符：
        
        - *：表示任意
            
        - *test：表示以test结尾
            
        - test*：表示以test开头
            
        - *test*：表示含test
            
        - *：表示所以，任意
            
- apt命令:
    
    - 作用：安装应用
        
    - 格式：apt [-y] [install/remove/search] 应用名
        
        - -y 指自动安装
            
- date命令：
    
    - 显示时间日期
        
    - 格式：date [+%参数]
        
    - 参数：
        
        - %H:小时，24小时制
            
        - %I:小时，12小时制
            
        - %M:分钟
            
        - %A:星期
            
        - %B:月
            
        - %Y:年
            
        - %y:年的后两位
            
        - %m:月数字
            
        - %a:星期简称，如一
            
        - %j:一年的第几天
            
- cal命令：
    
    - 显示日历
        
    - 格式：
        
    - 参数：
        
        - -1:单月输出
            
        - -3：近三个月输出
            
        - -s：将星期日作为第一天
            
        - -m：将星期一作为第一天
            
        - -j：以一年第几天代替几日
            
        - -y：显示当年日历
            
- bc命令
    
    - 计算器
        
    - quit退出
        
    - scale=n，输出小数点后几位
        
- 在linux和windows之间传输文件
    
    - 打开xshell，连接linux
        
    - cd到需要保存的地址
        
    - 输入rz（如果是用户文件之外需要权限sudo rz）
        

### 热键

- 忘记命令时，可以连按两次tab键给提示，如输出ls，可以这样：l tab tab
    
- ctrl+c强制命令停止