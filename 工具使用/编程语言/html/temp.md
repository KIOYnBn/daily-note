# 学习进度
暂时无法在飞书文档外展示此内容
# 技术内容
 1. HTML
 2. CSS
 3. Javascript
# 技术学习方式
 1. MDN WEB DOCS网站
# 工作流程
 1. 浏览器向服务器发送请求
 2. Apache服务器收到PHP请求， 查询信息
 3. PHP脚本执行， 根据数据和html模板生成页面
 4. HTML文本返回给Apache， 发送到浏览器
 5. 浏览器接受html文件， javascript加工
# HTML
- 功能： 网页框架
- 注意事项：
	1. HTML标签不区分大小写， 一般推荐大写
	2.  HTML中多个连续空格只识别为一个空格
## 元素
### 文本元素
- 标题：`<h>`
	- 示例
		- `<h1>`这是一个一级标题`</h1>`
		- h1这个一级标题每个页面中只使用一次
- 段落：`<p>`
	- 示例
		- `<p>` My cat is very grumpy`</p>`
- 换行： `<br>`
	- 在段落中换行
	- 示例
```HTML
`<p>`
	举头望明月`<br />`
	低头思故乡
`</p>`
```
- 水平分割线：`<hr>`
	- 示例
```HTML
`<p>`
	nb
`</p>`
`<hr />`
`<p>`
	更nb
`</p>`
```
- 斜体： `<em>` or `<i>`
	- 示例
		- `<em>` context`</em>`
		- `<i>` context`</i>`
- 粗体： `<strong>` or `<b>`
	- 示例
		- `<p>` My cat is `<strong>`very`</strong>` grumpy.`</p>`
		- `<p>` My cat is `<b>`very`</b>` grumpy.`</p>`
	- 注意事项：
>` 1. strong元素在p元素前关闭
- 高亮： `<mark>`
	- 示例
		- `<p>``<mark>`这是一段高亮文字`</mark>`
- 下划线： `<u>`
	- 示例
		- `<u>` 这是一个链接`</u>`
- 列表
	- 有序列表：`<ol>` `<li>`
		- 示例
			```HTML
			`<ol>`
				`<li>` 这是1`</li>`
				`<li>` second`</li>`
			`</ol>`
			```
	- 无序列表：`<ul>` `<li>`
		- 示例
			```HTML
			`<ul>`
				`<li>`one`</li>`
				`<li>`two`</li>`
			`</ul>`
			```
- 缩进： `<dl>` `<dt>` `<dd>`
	- 示例
		```HTML
		`<dl>`
			`<dt>`旁白`</dt>`
			`<dd>`
				戏剧中， 为了。。。
			`</dd>`
			`<dd>`
				写作中， 为了。。。
			`</dd>`
		`</dl>`
		```
- 引用
	- 块引用：`<blockquote>`
		- 示例
			```HTML
			`<blockquote
				cite="http:......">`
				`<p>`
					这一段都是引用内容
				`</p>`
			`</blockquote>`
			```
	- 行内引用： `<q>`
		- 示例
			```HTML
			`<p>`
				鲁迅说过：`<q cite="鲁迅">`世上本没有路。。。`</q>`
			`</p>`
			```
	- 引用属性元素： `<cite>`
- 缩略语: `<abbr>`
	- 元素：title, 鼠标停留时的显示， 非必要
	- 示例
		```HTML
		`<p>`
			我是使用`<abbr>`HTML`</abbr>`来组织网页文档
		`</p>`
		`<p>`
			`<abbr title="protein-protein interaction">` PPI`</abbr>` 是我的研究领域
		`</p>`   
		```
- 标记联系方式: `<address>`
	- 示例
		```HTML
		`<address>`
			`<P>`
				LJY`<br />`
				鲁迅`<br />`
			`</p>`
			`<ul>`
				`<li>`Email: ....@mail.imu.edu.cn`</li>`
				`<li>`phone number: 130276..`</li>`
			`</ul>`
		`</address>`
		```
- 上下标： `<sup>`, `<sub>`
	- 示例
		```HTML
		`<p>` 25`<sup>`th`</sup>``</p>`
		`<p>` C`<sub>`30`</sub>``</p>`
		```
- 标记时间： time
	- 属性： datetime
	- 示例
		```HTML
		`<time datetime="2025-7-12">` 2025年7月12日`</time>`
		```
### 媒体元素
- 图片插入： `<img>`
	- 属性
		- Src： 资源链接
		- Alt： 备选文本——图片加载错误时显示
		- Width
		- Heigth
		- Title： 图片标题， 一般不用
	- 示例
		![](https://my.feishu.cn/space/api/box/stream/download/asynccode/?code=ZTEzNTcyYWJlMWVkOGQ4ZTMxODJlNDk3NjlmNjNjZjZfblVqODRJeGZNMlFGOVh0QjU3eDVWVW1qaW1hM3Z1YkhfVG9rZW46T1FuVmJRUjh1b1B1Yzd4STRjMWNiTTMwbkZlXzE3NzQxMDU0ODM6MTc3NDEwOTA4M19WNA)
	- 插入图片描述
		- 元素
			- `<Figure>`
			- `<figcaption>`
		- 示例
			```HTML
			`<figure>`
				`<img
					src="images.jpg"
					alt="一个图片"
					width="400"
					height="300"
				`<figcaption>`
					workflow
				`</figcaption>`
			`</figure>`
			```
- 视频插入： `<video>`
	- 属性
		- Controls: 用户可以控制视频或音频的播放
		- Src： 文件路径
		- Width
		- Height
		- Autoplay： 内容自动播放， 布尔属性
		- Loop： 视频循环， 布尔属性
		- Muted： 酶体播放时， 默认关闭声音， 布尔属性
		- Preload： 用来缓冲较大的文件
			- 值
				- "none"： 不缓冲文件
				- "auto"： 页面加载后缓冲媒体文件
				- "metadata"： 进缓冲文件的元数据
		- Poster: 指向图像的url， 用于视频播放前显示
	- 示例
		```HTML
		`<video src="rabbite320.webm" controls>`
			`<!--video中插入的文字可以在视频加载错误时显示-->`
			`<p>`
				你的浏览器不支持html视频， 点击`<a href="rabbit320.mp4">`观看。
			`</p>`
		`</video>`
		`<video
			controls
			width="400"
			height="400"
			autoplay
			loop
			muted
			preload="auto"
			poster="poster.png">`
			`<!--source元素是用于媒体属性中多资源嵌套， 避免单一格式兼容问题-->`
			`<source src="rabbit320.mp4 type="video/mp4" />`
			`<source src="rabbit320.webm" type="video/webm" />`
			`<p>` 你的浏览器不支持此视频
			`</p>`
		`</video>`
		```
- 音频插入： `<audio>`
	- 说明
		- 与video基本相同， 但没有width， heigth， poster属性
	- 示例
		```HTML
		`<audio controls>`
			`<source src="viper.mp3" type="audio/mp3" />`
			`<source src="viper.ogg" type="audio.ogg" />`
			`<p>`   你的浏览器不支持该音频， 电极`<a href="viper.mp3">` 此链接`</a>`收听
			`</P>`
		`</audio>`
		```
- 音频文本显示： `<track>`
	- 文件： webvtt文件格式， .vtt后缀
		- 示例
			```HTML
			WEBVTT
			00:00:02.000 -->` 00:00:05.000
			第一句字幕文本
			00:00:06.000 -->` 00:00:10.000
			第二句字幕文本
			```
	- 可以插入audio或video中
	- 属性
		- Kind： 轨道类型
			- Subtitles: 字幕
			- Captions： 标题， 包含非语言信息
			- Chapters： 章节， 用于用户跳转
			- Descriptions： 为用户口头描述内容
			- metadata： 元数据， 不显示， 供javascript调用
		- Src： 文件链接
		- Srclang： 轨道语言类型， 如“en”
		- Label: 说明轨道语言名称， 用户可见， 如“简体中文”
	- 示例
		```HTML
		`<video controls>`
			`<source src="example.mp4" type="video/mp4" />`
			`<track kind="subtitles" src="subtitles.vtt" srclang="es" label="Spanish" />`
		`</video>`
		```
- 外部资源插入： `<link>`
	- 一般图片文件放在html文件同一目录下
	- 示例
		- `<link rel="icon" href="favicon.ico" type="image/x-icon" / >`
		- `<link rel="apple-touch-icon" sizes="167x167" href="/apple-touch-icon-167x167.png" />`
- 超链接：`<a>`
	- 链接到文档某一部分：
		- 链接到本文当某地方：
			```HTML
			`<nav>`
				`<a href="#chapter1">`跳转至章节1`</a>`
			`</nav>`
			`<h2 id="chapter1">`章节1`</h2>`
			```
	- 发送邮件
		- 示例
			```HTML
			`<a>
				href="mailto:twb72743075@126.com:
				向我发送邮箱
			`</a>`
			```
	- 属性：
		- herf： 声明web超链接
			- 示例：
				- href="https://www.mozilla.org/""
		- Title: 为超链接声明额外信息， 鼠标悬停时的提示
		- Target: 指定链接如何呈现
			- 示例
				- target="_blank"： 在新标签页显现
				- 未填： 在当前页显示连接
		- download：链接到下载的资源
			- 示例：
				```HTML
				`<a
					href="https:....."
					download="firefox.exe">`
					下载firefox
				`</a>`
				```
### 表单元素
#### 表单
- `<form>`: 外部包装器
	- 属性
		- action： 提交到要处理的页面路径。
		- method： 表单数据传输的数据方法
- `<filedset>`: 表单分组
	- 属性
		- Disable: 禁用表单元素
	- `<legend>`： 为表单每个分组命名
	- 示例
		```HTML
		`<fieldset disabled>`
			`<legend>` 高级选项（未激活）`</legend>`
			`<!--表单-->`
		`</fieldset>`
		```
- `<button>`: 按钮
	- 属性： type
		- submit： 提交
		- reset： 重置输入状态
		- button： 默认不执行任何操作， 需要javascript
- `<input>`：输入数据
	- 属性：
		- Type: 类型
			- 文本输入类
				- Text: 单行文本输入框， 用户名， 短文本
					- `<input type="text" name="username" placeholder="请输入用户名">`
				- Password: 输入内容显示为圆点或星号
					- `<input type="password" name="pwd" placeholder="密码">`
				- email： 邮箱输入框， 提交时验证格式
					- `<input type="email" name="email required>`
				- url： url输入框， 验证是否符合网址格式
					- `<input type="url" name="website"
				- tel： 电话号码输入框， 使用pattern属性自定义格式
					- `<input type="tel" name="phone" pattern="[0-9]{3}-{0-9]{8}">`
				- search： 搜索框
					- `<input type="search" name="q" placeholder="搜索内容">`
				- number： 数字输入框， 支持限制范围和步长
					```HTML
					`<input type="number" name="age" min="18" max="99"
					```
			- 选择类
				- radio： 单选按钮
					- 示例
				```HTML
				`<fieldset>`
					`<legend>`Choose hotel room type: `</lengd>`
					`<div>`
						`<input
							type="radio"
							id="hotelChoice1"
							name="hotel"
							value="economy"
							checked />`
							`<!--checked：默认选择-->`
						`<label for="hotelChoice1">`Economy `</label>`
						`<input
							type="radio"
							id="hotelChoice2"
							nmae="hotel"
							value="superior"
							/>`
						`<label for="hotelChoice2">`Superior`</label>`
						`<input
							type="radio"
							id="hotelChoice3"
							name="hotel"
							value="penthouse"
							disabled />`
							`<!--disbale：禁用表单控件-->`
						`<label for="hotelChoice3">`Penthouse`</label>`
					`</div>`
				`</fieldset>`
				```
				- Checkbox: 复选框
					- 示例
						```HTML
						`<fieldset>`
							`<legend>`Choose classes to attend:`</legend>`
							`<div>`
								`<input type="checkbox" id="yoga" name="yoga" />`
								`<label for="yoga">` Yoga`</label>`
								`<input type="checkbox" id="coffee" name="coffee" />`
								`<label for="coffee">`Coffee roasting`</label>`
							`</div>`
						`</fieldset>`
						```
				- Select and option： 下拉菜单
					- 示例
						```HTML
						`<label for "transport">`How are you getting here:`</label>`
						`<select name="transport" id="transport">`
							`<option value="">`--Please choose an option--`</option>`
							`<option value="plane">`Plane`</option>`
							`<optiob value="bike">`Bike`</optioin>`
						`</select>`
						```
				- file： 文件上传
					```HTML
					`<input type="file" name="doc" accept=".pdf,.docx"
					```
				- color： 颜色选择器， 返回十六进制
					```HTML
					`<input type="color" name="theme"
					```
			- 功能类
				- submit： 提交
					```HTML
					`<input type="submit" value="submit">`
					```
				- reset： 重置按钮
					```HTML
					`<input type="reset" value="reset"
					```
				- button： 类似按钮
					```HTML
					`<input type="button" value="button" onclick="alert()">`
					```
				- image： 提交图片
					```HTML
					`<input type="image" src="submit.png" alt="submit">`
					```
				- range： 滑动条， 选择数值范围
					```HTML
					`<input type="range" name="volume" min="0" max="100"
					```
			- 时间选择类
				- Data: 日期选择器
					```HTML
					`<input type="data" name="birthday">`
					```
				- time： 时间选择器
				- month： 月份选择器
				- week： 周选择器
				- datetime-local： 本地时间
		- Name： 数据项名称， 以数值对形式发送
		- Id： 标识id， 用于于label
		- Required：要求提交表单前必须输入
		- Textarea: 多行文本输入字段
			- 示例
				```HTML
				`<label for="comments">`Any other comments"`</label>`
				`<textarea id="comments" name="comments" row="5" cols="33">`
				`</textarea>`
				```
- `<label>`: 标识标签
	- 属性
		- For
	- 示例
		```HTML
		`<label for="name">`Nmae (required):`</label
		`<input type="text" name="name" id="name" required />`
		or
		`<label>`
			Name(required):
				`<input type="text" name="name" requreid />`
			`</label>`
			```
#### 表格
- 元素
	- 表格可以嵌套表格
	- 单元格： `<td>`
	- 行分隔： `<tr>`
	- 标题行： `<th>`
	- 标题： `<caption>`
	- 格式设置： `<col>`, `<colgroup>`
	- 表头： `<thead>`
	- 表尾: `<tfoot>`
	- 主要内容: `<tbody>`
	- scope： 定义表头的类型——行表头or列表头
		- 示例
			```HTML
			`<thead>`
				`<tr>`
					`<th colspan="3" scope="colgroup">` 衣物`</th>`
					`<th rowspan="2" scope="rowgroup">`金额`</th>`
				`</tr>`
			`</thead>`
			```
- 示例
	```HTML
	`<head>`
		`<style>`
			tbody{
				font-size=90%;
				font-style:italic；
			}
			tfoot{
				font-weight:bold;
			}
		`</style>`
	`</head>`
	`<body>`
		`<table>`
			`<colgroup>`
				`<col />`
				`<col sytle="backgroud-color: yellow" />`
			`</colgroup>`
			`<caption>`
				我的数据
			`</caption>`
			`<thead>`
				`<tr>`
					`<th>`数据1`</th>`
					`<th>` 数据2`<th>`
				`</tr>`
			`</thead>`       
			`<tbody>`
				`<tr>`
					`<td>`加尔各答`</td>`
					`<td>`橙汁`</td>`
				`</tr>`
			`</tbody>`
			`<tfoot>`
			`<tr>`
				`<td>`机器人`</td>`
				`<td>`爵士乐`</td>`
			`</tr>`
			`</tfoot>`
		`</table>`
	`</body>`
		```
### 结构元素
- 容器属性
- 内联容器： `<span>`， 默认不换行
	- 无法设置宽高， 适合文本级修饰， 如何高亮， 变色
	- 用于设置段内操作， 应用css， javascript
	- 示例
		- `<p>``<span sytle="font-size: 32px; margin: 21px 0; display: block;">`这是一段文字`</span>`
			- margin控制元素间距， 负值缩小空白
			- 0表示水平居中， 可以调节垂直距离
	- 如果对整个段落应用， 可以直接在p元素中设置
		- 示例
			- `<h1 sytle="font-size: 32px; margin 21px 0;">`这个一个一级标题`</h1>`
- 块级容器：`<div>`， 默认换行
	- 划分文档独立区块， 可设置宽度， 高度， 边距等， 控制布局尺寸和位置
	- 示例
		- `<div class="header">`网站标题`</div>`
	- 
## 基础知识
属性： 附加在标签内的键值对
- 属性与元素名称， 属性与属性之间通过空号分割
- 每个属性值通过引号引起来
- 属性名称+“=”+属性值
- 注意事项
	1.  有些网页中属性值没有被引号包裹， 这种情况有时被允许， 但是容易出错， 不建议
	2.  单引号或双引号都可以， 但是不要二者同时用， 但是可以嵌套
		- 示例
	        - `<p class="editor-note">`My cat is very strong`</p>`
- 常见属性
	- 布尔属性
		- 是一种没有值的属性， 或者说值于名称相同， 当然也可以写上值
		- 示例:
			- `<input type="text" disabled />`
			- `<input type="text" disabled="disabled" />`
			- disabled禁止用户输入
### 页面框架
```Plain
# 文档类型声明。
`<!doctype html>`   
# html元素： 包裹页面所有内容
`<html lang="zh-CN">`
	# head元素： 包含不在html页面显示的内容。
	# 如： 搜索结果中出现的关键词和页面描述， css样式等
	`<head>`
		# meta元素： 包括元数据， 如base， link
		#script， sytle， title元素
		`<meta charset="utf-8" />`
		# title元素： 页面标题
		`<title>`我的测试站点`</title>`
	`</head>`
	# body元素： 页面显示内容
	`<body>`
		`<p>`这是我的2页面`</p>`
	`</body>`
`</html>`
```
### 特殊符号
- 以&开始， 以分号；结束

| 原义字符 | 等价字符引用 |
| ---- | ------ |
| `<   | &lt;   |
| >`   | &gt;   |
| "    | &quot; |
| '    | &apos; |
| &    | &amp;  |
- 注释
    - 使用`<!--和-->`包裹
    - 示例
        - `<!-- <p>我在注释里面! </p> -->`
- head元素中的内容
    - 元数据： `<meta>`元素, 指用来描述数据的数据
    - 字符编码： charset:
        - utf-8
        - IOS-8859-1: 拉丁字母表的字符集
    - `<name>` 元素和`<content>`元素
        - 示例
        ```Plain
        `<meta name="author" content="LJY" />`
        `<meta
            name="description"
            content="This is the first html file made by me" />`
        ```
- 为文档设置主语言
    - lang属性
    - 示例
        - `<html lang="zh-CN">`
    - 也可以将不同分段设置不同语言
        - 示例：
            - `<p>`Japanese example: `<span lang="ja">` ご飯が熱い。`</span>`.`</p>`
- CSS和JvaScript的应用
    - CSS
        - link： 位于文档头部， 包含rel， href两个属性
            - rel： 表明这是文档样式表
            - href： 样式表文件路径
        - 示例
            - `<link rel="stylesheet" href="my-css-file.css" />`
    - JavaScript
        - script元素：位于文档头部 包含src， defer两个属性
            - src： 说明JavaScript文件路径
            - defer： 告诉浏览器解析完成html后再加载JavaScript。
        - 示例
            - `<script src="my-js-file.js" defer>``</script>`
- 区块化
    - 元素
        - 页眉: `<header>`
        - 导航栏: `<nav>`
        - 主内容: `<main>`， 位于`<body>`中
            - 子内容： `<article>`, `<section>`, `<div>`
                - `<article>`包围的内容为一篇文章
                - `<section>`： 适用于组织页面分块， 可以将一篇article分开位于不同section中
        - 侧边栏: `<aside>`， 通常嵌套在`<main>`中
            - 包含一些间接信息——术语条目， 作者简介， 相关链接
        - 页脚：`<footer>`
    - 示例
        ```HTML
        `<!doctype html>`
        `<html>`
            `<head>`
                `<meta charset="utf-8" />`
                `<title>`二次元俱乐部`</title>`
                `<link
                    href="https://fonts.googleapis.com/css?family=Open+Sans+Condensed:300|Sonsie+One"
                    rel="stylesheet" />`
            `</head>`
            `<body>`
                `<header>`
                    `<h1>`聆听电子天籁之音`</h1>`
                `</header>`
                `<nav>`
                    `<ul>`
                        `<li>``<a href="#">`主页`</a>``</li>`
                    `</ul>`
                    `<form>`
                        `<input type="search" name="q" placeholder="要搜索的内容“ />`
                        `<input type="submit" value="搜索" />`
                    `</form>`
                `</nav>`
                `<main>`
                    `<article>`
                    `</artile>`
                    `<aside>`
                        `<h2>`相关链接`</h2>`
                        `<ul>`
                            `<li>``<a href="#">`这是一个超链接`</a>``</li>`
                        `</ul>`
                    `</aside>`
                `</main>`
                `<footer>`
                    `<p>` 2050某某保留所有权利`</p>`
                `</footer>`
            `</body>`
        `</html>`
        ```
# CSS
- 测试部分的能力要求
    - 挑战： 基本的css理解
        - css外部导入
        - 行高： line-height
    - 挑战： 创建精美的信纸
        - 多个图片背景
        - 盒子阴影： filter: drop-shadow, box-shadow
    - 挑战： 一个漂亮的盒子
        - 宽度： width
        - 高度： height
        - 盒子类型： display
        - 文本纵向和横向居中： align-items, justify-content
        - 字体颜色: color
        - 对角线渐变： to bottom right
        - 多盒阴影： x y radius color
- 功能： 界面优化
## 选择器
- 选择器： 定义元素的属性值
### 类选择器（元素选择器）
- 示例
	```CSS
	h1 {
		color: red;
		font-size: 2.5em;
	}
	```
- 多选择器同时定位： 逗号分隔
	```CSS
	p,
	li {
		color: green;
	}
	```
- 自定义类：
	```CSS
	.special {
		color: orange;
		font-weight: bold;
	}
	h1.light(
		color: organe;
		font-weight: bold;
	}
	```
	```CSS
	`<ul>`
		`<li class="special">` Item two`</li>`
	`</ul>`
	`<h1 class="light">`class light`</h1>`
	```
- 多类选择器
	```CSS
	.notebox.warning {
		border-color: orange;
		font-weight: bold;
	}
	```
	```HTML
	`<!--空格表示且-->`
	`<div class="notebox warning">` oooo `</div>`
	```
### ID选择器
```CSS
#one {
	background-color: yellow;
}
h1#heading {
	color: rebeccapurple;
}
```
```HTML
`<h1 id="heading">` ID selector`</h1>`
`<p id="one">`
	oooo
`</p>`
```
- 选择全部内容：*
```CSS
* {
	margin: 0;
}
```
### 选择器组合
- 后代选择器： 空格分割
	```CSS
	/* 影响li中的em， 不影响li*/
	li em {
		color: rebeccapurple;
	}
	```
- 子代选择器： >`连接， 元素嵌套
	```CSS
	ul >` li {
		border-top: 5px solid red;
	}
            ```
- 相邻选择器： +连接， 元素按顺序出现
```CSS
/* 影响h1后的ul后的p， 即严格按照顺序出现的p*/
h1 + ul + p{
	border-left: 3px solid;
}
```
- 通用选择器： ~连接
```CSS
/* 选中h1后的所有p */
h1 ~ p {
	font-weight: bold;
	background-color: #333;
	color: #fff;
	padding: 0.5em;
}
```
### 属性选择器
- 类型
	```CSS
	/* 匹配带有x属性的元素 */
	li[class] {
		font-size: 120%;
	}
	/* 匹配x属性的值只为y的元素 */
	li[class="a"] {
		backgroud-color: yellow;
	}
	/* 匹配x属性的值中有y的元素 */
	li[class~="a"] {
		color: red;
	}
	/* 匹配x属性开头有y的元素 */
	li[class^="a"] {
		font-size: 120%;
	}
	/* 匹配x属性以y结尾的元素 */
	li[class$="a"] {
		background-color: yellow;
	}
	/* 匹配x属性含有y的元素 */
	li[class*="a"] {
		color: red;
	}
	/* 忽略大小写 */
	a[href$="pdf." i] {
		background: url('pdf-icon.png');
	}
	```
- 应用
    - 外部样式表
        ```HTML
        `<link rel="stylesheet" href="styles.css" />`
        ```
    - 内部样式表
        ```HTML
        `<head>`
            `<style>`
                p {
                    color:purple;
                }
            `</style>`
        `</head>`
        ```
    - 内联样式
        ```HTML
        `<span style="color: purple; font-weight: bold">`span element`</span>`
        ```
- 注释
    - /* */
- 函数
    - calc： 进行数学运算
        - 示例
            ```CSS
            .box {
                width: calc(90% - 30px);
            }
            ```
    - min（）， max（）clamp（）——中间值
    - transform属性的值
        - 如rotate
            - 示例
                ```CSS
                .box {
                    margin: 30px;
                    width: 100px;
                    height: 100px;
                    background-color: rebeccapurple;
                    transform: rotate(0.8turn);
                }
                ```
        - translate： 水平或垂直移动某物
    - scale： 放大或缩小某物
- 伪类和伪元素： 特定状态下的类或元素
    - 伪类： 一个：
        - 简单伪类：
            - :first-child
                ```CSS
                article p: first-child {
                    font-size: 120%;
                    font-weight;
                }
                ```
                ```HTML
                `<!--只会影响第一个p中的-->`
                `<article>`
                    `<p>`
                        fdasojfsdojfjasofjoisajfiosajdfo;
                    `</p>`
                    `<p>`
                        oajfoasjfoisajfoisajf
                    `</p>`
                `</article>`
                ```
            - :last-child
            - :invalid
        - 用户行为伪类： 与用户交互
            - 链接
                - 元素
                    - :link: 有目的地的链接
                    - :visited: 已访问过
                    - :hover: 用户的指针挪到元素上激活
                    - :focus： 用户使用键盘选定元素时激活
                    - Activate: 点击（激活）
                    - 示例
                        ```CSS
                        a: link,
                        a: visitied {
                            color: rebeccapurple;
                            font-weight: bold;
                        }
                        a: hover {
                            color: hotpink;
                        }
                        ```
                - 属性
                    - color： 文字颜色
                    - cursor： 改变鼠标光标的样式
                    - outline： 改变文字轮廓
    - 伪元素: 两个：：
        - ::first-line
            ```CSS
            /* article后的p的第一行*/
            article p:: first-line {
                font-size: 120%;
                font-weight: bold;
            }
            /* 内容添加——before, after */
            .box::before {
                content: " 这显示在内容之前";
            }
            ```
## 盒模型
### 类型
- 标准盒模型： width和height仅定义内容区域的尺寸
- 替代盒模型： width和height定义整个盒的大小
- 设置
	- 默认使用标准盒
	- 替代盒：使用box-sizing设置
		```CSS
		.box {
			box-sizing: border-box;
		}
		```
### 属性
- width：
- Height
- Padding
	- Padding-top
	- Padding-right
	- Padding-bottom
	- padding-left
- Border
	- 类型
		- Border-top
		- Border-right
		- Border-bottom
		- Border-left
	- 样式
		- Border-width
			- border-top-width
		- Border-style
		- border-color
	- 示例
		```CSS
		/* 四个边框都设置 */
		.box {
			border: 1px solid black;
		}
		.box {
			border-top: 1px solid black;
		}
		.box {
			border-width: 1px;
			border-style: solid;
			border-color: black;
		}
		```
- Margin
	- Margin-top
	- Margin-right
	- Margin-bottom
	- margin-left
- 圆角： border-radius
	```CSS
	/* 盒子四个角都有10px的圆角半径*/
	.box {
		border-radius: 10px;
	}
	/* 右上角水平半径1em， 垂直半径10% */
	.box {
		border-top-right-radius: 1em 10%;
	}
	```
- 示例
	```CSS
	.box {
		width: 350px;
		height: 150px;
		margin: 10px;
		padding: 25px;
		border: 5px solid black;
	}
	```
- 背景
	- 颜色： background-color
	- 图像: background-image
		- 示例
			```CSS
			.a {
				background-image: url(....);
			}
			```
		- 平铺： background-repeat
			- No: repeat: 阻止背景重复平铺
			- repeat-x： 水平方向上重复平铺
			- repeat-y： 垂直方向
			- repeat： 水平和垂直
		- 调整大小： background-size
			- 示例
				```CSS
				.box {
					background-size: 80px 10em;
				}
				```
			- 关键词：
				- cover： 图像覆盖盒子， 部分区域超出盒子
				- contain： 图像保持在盒子内， 出现空隙
		- 定位： background-position
			- 接受top， left， bottom， right， center等关键词
			```CSS
			.box {
				background-position: (0, 0);
			}
			.box {
				background-position: top center;
			}
			.box {
				background-position: 20px 10%;
			}
			.box {
				background-position: 20px top;
			}
			.box {
				background-position: top 20px right 10px;
			}
			/* 盒子右移40像素 */
			.box {
				background-position: right 40px;
			}
			.box {
				background-position: 120px 1em;
			}
			```
		- 渐变
			```CSS
			.gradient {
				background-image: linear-gradient (
					90deg,
					rgb(119 0 255 / 39%),
					rgb(0 212 255 / 100%)
				);
			}
			```
		- 背景附加: background-attachment
			- Scroll: 随页面滚动滚动
			- Fixed: 背景固定
			- local： 背景固定在设置的元素上
- 媒体元素
	- 大小控制： object-fit
		- 值：
			- Fill: 拉伸图像填满
			- Contain: 图像缩放到放入盒子中
			- Cover: 充满盒子， 不拉伸， 裁剪
		- 示例
			```CSS
			.contain {
				object-fit: contain;
			}
			```
- 表格元素
	- 合并表格： border-collapse
		```CSS
		table {
			border-collapse;
		}
		```
- 按元素类型划分
	- display属性： 设置盒子类型
	- 区块盒子： block boxes， 换行
		- Display: block
		- 应用于`<div>` `<p>`等
	- 行内盒子： inline boxes
		- Display: inline
		- 应用于`<span>` `<a>`等
		- 属性
			- 没有width和height
			- 边距设置不会推开其他盒子
	- 行内块盒子： inline-block box
		- Display: inline-block
		- 属性
			- 设置完整width， height盒边距
	- 弹性盒子： 不需要手动设置width和height。
		- 弹性区块盒子——display： flex
			- Flex-direction： 排列方向
				- 默认： row
			- Align-items与align-content， justify-items与justify-content
				- align-items与align-content
					|   |   |   |
					|---|---|---|
					||align-items|align-content|
					|作用对象|容器（父元素|   |
					|作用内容|控制子项在交叉轴（垂直方向上的对齐方式|控制多行/多列整体在交叉轴上的分布方式|
					|取值|- start-顶部对齐`<br>`    `<br>`- end-底部对齐`<br>`    `<br>`- center-居中对齐`<br>`    `<br>`- stretch-拉伸填满容器|- flex-start-所有行靠顶部`<br>`    `<br>`- flex-end-所有行靠底部`<br>`    `<br>`- center-所有行整体居中`<br>`    `<br>`- space-between-行于行均匀分布， 首尾无间距`<br>`    `<br>`- space-around-行与行均匀分布， 首位有半间距|
					|使用场景|flex/grid|多行/多列的flex/grid|
					||||
				- justify-items与justify-content

|   |   |   |
|---|---|---|
||justify-content|justify-items|
|作用对象|容器|容器子项（grid）|
|作用内容|主轴上子项整体如何分布|子项在自身单元格内主轴上的对齐方式|
|取值|- flex-start-靠头部对齐`<br>`    `<br>`- flex-end-靠尾部对齐`<br>`    `<br>`- center-曲中`<br>`    `<br>`- space-between-两端对齐， 子项间距均分`<br>`    `<br>`- space-around-子项间距均分， 首尾有半间距`<br>`    `<br>`- space-evenly-所有间距完全相等|- start-单元格内靠头部对齐`<br>`    `<br>`- end-单元格内靠尾部对齐`<br>`    `<br>`- center-单元格内居中`<br>`    `<br>`- stretch-拉伸填满单元格|
|场景|flex/grid|grid|
                        
                - Flex: flex的动态尺寸
				- ```CSS
                    /* 每项占用空间相同*/
                    article {
                    flex 1;
                    }
                    /* 或者使用
                    justify-content: space-content;
                    /* 假如总共有3个元素， 这第三下占总共的1/2
                    article:mth-of-type(3) {
                        flex: 2;
                    }
```
                - 水平或垂直对齐
			- ```CSS
                    div {
                        display: flex;
                        align-items: center;
                        justify-content: space-around;
                    }
```
                - flex具体项的排序： order。order默认是0
```CSS
                    button:first-child {
                        order: 1;
                    }
```
            - 弹性行内盒子——display： inline-flex
    - 处理内容溢出：overflow
        - 属性
            - Overflow-x
            - overflow-y
        - 值
            - visiable： 默认
            - hidden： 溢出内容隐藏
            - scroll： 滚动
            - auto： 自动调整
        - 示例
            ```CSS
            .box {
                overflow: hidden;
            }
            .box {
                overflow: scroll;
            }
            .box {
                overflow-y: scroll;
            }
             .box {
                 overflow: auto;
             }
             .box {
                 overflow: hidden, scroll;
             } 
            ```
- 冲突规则
    - 层叠： 当应用两条同级别的规则到同一元素时， 后写规则发挥作用
    - 优先级：
        - 选择器包含元素/伪元素： 1分
        - 选择器包含类： 10分
        - 选择器包含id： 100分
        - 示例
            ![](https://my.feishu.cn/space/api/box/stream/download/asynccode/?code=OWI3OTZkNDlmZjg0MzY2YjA2MmE2YjYxOTRmZjAwNThfUGpOTFZ4MkdWTDlFNFY2eEsyVElaZGZJSzl1MmU2RmFfVG9rZW46UzNjbWJyZTBjb08wZml4STluSmNMUnFobldnXzE3NzQxMDU0ODM6MTc3NDEwOTA4M19WNA)
    - 继承： 一般文本属性继承， 格式属性不继承
        - inherit： 开启继承
        - initial： 属性值设置为初始值
        - revert： 设置为浏览器默认样式
        - revert-layer： 设置为上一个层叠层建立的值
        - unset： 重置为自然值
- 常见的属性和值类型
    - 长度
        - 最常用： px——像素， 1px=0.2646mm
        - 相对长度单位
            - 字体大小
                - em： 表示相对本元素的字体大小
                - rem： 相对根元素的字体大小
            - 宽度：
                - px： 固定大小
                - vw： 相对视口宽度， 百分比
                - vh： 视口高度
                    - 示例
                        ```CSS
                        .vm {
                            width: 10vw;
                        }
                        .px {
                            width: 200px;
                        }
                        ```
            - 行高单位
                - lh： 相对元素的行高
                - rlh： 表示相对根元素行高
    - 百分比
        - 示例
            ```CSS
            .percent {
                width: 40%;
            }
            ```
    - 数字
        - 示例
            - 不透明度： 0-1.0表示完全透明
    - 颜色
        - 颜色关键词： 如green
        - 十六进制RGB值
        - RGB值
            - rgb函数接受三个值， 由/分割的第四个参数表示透明度
            - 值为十进制或百分数
            - 透明度为0-1之间
            - 示例
                ```CSS
                .one {
                    background-color: rgb(2 121 139 / 0.5);
                }
                ```
        - 色相
            - 包含色相组件的函数
                - hsl():
                    - 类似于rgb
                        - 色相： 0-360之间， 色轮的角度
                        - 白度：0-100%(完全白色)， 表示颜色中有多少白色
                        - 黑度： 0-100%之间
                - hwb()
                    - 色相
                    - 饱和度： 0-100%
                    - 亮度： 0-100%。0表示黑色， /后的第四个元素表示透明度
                - lch()
- 尺寸设置
    - min(max)-尺寸
        - 示例
            ```CSS
            .box {
                border 5px solid darkblue;
                min-height: 100px;
                width: 200px;
            }
            ```
- 文本设置
    - 颜色： color
        ```CSS
        p {
            color: red;
        }
        ```
    - 字体： font-family
        ```CSS
        p {
            font-family: arial, sans-serif;
        }
        ```
    - 在线字体设置： @font-face。具体较为麻烦， 目前忽略
    - 字体大小： font-size
        ```CSS
        p {
            font-size: 1.4rem;
        }
        ```
    - 斜体： font-style
        - 值
            - normal： 斜体关闭
            - itallic： 若斜体可用， 设置为斜体，否则使用obique模拟斜体
            - oblique： 模拟斜体——普通文本倾斜
    - 文字的粗体大小： font-weight
        - normal： 普通
        - bold： 加粗
        - lighter： 比父元素粗体更细
        - bolder： 比父元素粗体更粗
    - text-transform： 文本转换
        - uppercase： 文本转为大写
        - lowercase： 文本转为小写
        - capitalize： 首字母大写
        - Full-width: 设置全角
    - text-decoration： 文本装饰
        - underline： 文本下划线
        - overline： 文本上划线
        - line-through： 穿过文本的线
    - 文字阴影： text-shadow
        ```CSS
        text-shadow: 4px 4px 5px red;
        ```
    - 文本对齐: text-align
        - Left: 左对齐
        - Right
        - Center
        - justify： 所有文本行宽度相同
    - 行高： line-height
    - 字母间距： letter-spacing
    - 单词间距： word-spacing
- 列表设置
    - 项目符号类型： list-sytle-type
        ```CSS
        ol {
            list-style-type: upper-roman;
        }
        ```
    - 项目符号在列表内还是外： list-style-position
        - Outside or inside
    - 自定义项目符号： list-sytle-image
        ```CSS
        ul {
            list-style-image: url(star.svg);
        }
        ```
    - 计数
        - 起始： start
            ```HTML
            `<ol start="4">`
                `<li>`...`</li>`
            `</ol>`
            ```
        - 反向计数： reversed
            ```HTML
            `<ol start="4" reversed>`
                `<li>` .... `</li>`
            `</ol>`
            ```
        - 为特定项设值： value
            ```HTML
            `<ol>`
                `<li value="2">` ...`</li>`
            `</ol>`
            ```
- 布局设置
    - 正常布局流： 默认， 按上到下依次排列
    - [display](https://qqeggtfhkm7.feishu.cn/docx/DUm1dvl0Dod7QcxSK3JcMSTEnBc#share-WdMRdRwWUo49VUxcCBKcy6Yuneg)
    - grid布局
        - 属性
            - display： grid
            - Grid-template-rows: 定义列轨迹
            - grid-template-columns： 定义行轨道
            - Grid-gap
            - grid-column和grid-row具体指定特定元素的位置
            - Grid-areas and grid-template-areas:
                ```CSS
                .grid {
                  display: grid;
                  gap: 20px;
                  grid-template-columns: 1fr 2fr;
                  grid-template-areas:
                    "aa aa"
                    "bb cc"
                    ". dd";
                }
                .one {
                  grid-area: aa;
                }
                .two {
                  grid-area: bb;
                }
                .three {
                  grid-area: cc;
                }
                .four {
                  grid-area: dd;
                }
                ```
        - 示例
            ```CSS
            .wrapper {
                display: grid;
                grid-template-columns: 1fr 1fr 1fr;
                grid-template-rows: 100px 100px;
                grid-10px;
            }
            .box1 {
                grid-column: 2 / 4;
                grid-row: 1;
            ```
    - 浮动布局
        - 属性
            - float：
                - 值
                    - Left
                    - Right
                    - None
                    - Inherit
            - 示例
                ```CSS
                .box {
                    float: left;
                    width: 150px;
                    height: 150px;
                    margin-right: 30px;
                ```
        - 清除浮动：clear。——在要清除浮动影响的位置加入clear
            ```CSS
            .wrapper {
                clear: left;
            }
            ```
    - 定位
        - Z轴： z-index， 元素重叠时覆盖顺序
            - 示例
                ```CSS
                z-index: 1;
                ```
        - 静态定位： 默认
        - 相对定位： relative， 将元素在正常位置的进行移动
            ```CSS
            /* 将元素向右下推*/
            .positioned {
                position: relative;
                top: 30px;
                left: 30px;
            }
            ```
        - 绝对定位： absolute， 将元素放置在单独的图层
            ```CSS
            .positioned {
                position: absolute;
                top: 30px;
                left: 30px;
            }
            ```
        - 固定定位： fixed。 根据浏览器视口进行固定
        - 粘性定位： sticky。 当元素的相对视口位置到达某个值时， 像固定定位一样
            - 应用
                - 滚动布局
                    ```CSS
                    dt {
                        background-color: balck;
                        color: white;
                        padding: 10px;
                        position: sticky;
                        top: 0;
                        left：0;
                        margin: 1em  0;
                    }
                    ```
    - 表格布局： table-row
    - 多列布局
        - 属性
            - column-count： 多少列
            - Column-width：每列宽度多少
# Javascript
- 功能： 交互作用实现
- 应用
    - 内部
        - 在/body之前添加script
        - 示例
            ```HTML
            `<script>`
                //在此编写javascript
            `</script>`
            ```
    - 外部： js为后缀
        - 在`</head>` 之前添加script
        - 示例
            ```HTML
            `<script type="module" src="script.js">``</script>`
            `<!--如果失败， 使用下列代码-->`
            `<script defer src="script.js">``</script>`
            ```
- 注释
    - 单行
        ```JavaScript
        // 这是一个单行注释
        ONE
        /*
            这是一条多行注释
        */
        ```
- 变量
    - 声明： let
        ```JavaScript
        let yourName
        let myName = "Chris"
        ```
    - 命名规则
        - 不能以下划线和数字开头
        - 小写驼峰命名法： 多个单词组在一起时， 小写第一个命名的第一个字母， 其他的单词首字母大写
    - 变量类型
        - String
            - 多行：
                - 在字符串中加入\n
                ```JavaScript
                let lines = "this is the first line. \n This is the second line.
                ```
            - 表达式嵌入： ${}
                ```JavaScript
                const one = "me"
                console.log(`${one}`)
                //注意， 双引号和单引号不会引起表达式嵌入， 而是`， 即英文下的esc下的按键
                ```
            - 方法属性
                - 长度： length
                    ```JavaScript
                    let browserType = "mozilla";
                    browserTye.length;
                    ```
                - 切片
                    ```JavaScript
                    browserType[0];
                    browserType[browserType.length - 1];
                    browserType.slice(0, 3); // 0-不包括最后一个位置
                    broserType.sclice(2); //2后的所有字符
                    ```
                - 检索： indexOf（）
                    ```JavaScript
                    browserType.indexOf("zilla")
                    //没有时返回-1. 有时返回位置
                    ```
                - 大小写
                    ```JavaScript
                    let radData = "MY name is Mud";
                    radData.toLowerCase();
                    radData.toUpperCase();
                    ```
                - 替换： replace
                    ```JavaScript
                    browerType.replace("moz", "van");
                    ```
        - Number
            - 小数点位数: toFixed()
                ```JavaScript
                // Final result should be 4633.33
                let result = (7 + 13 / 9) + 7;
                let result2 = 100 / 2 * 6;
                result *= result2;
                const finalResult = result.toFixed(2);
                ```
        - Boolean
        - Array
            - 属性方法
                - 字符串和数组的转化
                    - 字符串转化成数组： split
                        ```JavaScript
                        let myArray = myData.split(",");
                        ```
                    - 数组转化成字符串： join
                        ```JavaScript
                        let myNewString = myArray.join(",");
                        //or
                        myNewString.toString();
                        ```
                - 添加删除： push， pop or unshift, shift(后二者在起始位置添加）
                    ```JavaScript
                    //默认删除最后一项
                    myArray.pop();
                    myArray.push("Bradford", "brighton");
                    ```
                - 变量： forEach((element, index)
                    ```JavaScript
                    myArray.forEach((element, index) =>` {const newElement = `${element} (${index})`;
                      myArray[index] = newElement;});
                    ```
                - 过滤器： filter
                    ```JavaScript
                    function startsWithE(bird) {return bird.startsWith("E");}
                    const eBirds = birds.filter(startsWithE);
                    ```
                - 索引的删除替换： splice
                    ```Java
                    const birds = ["Parrots", "Falcons", "Eagles", "Emus", "Caracaras", "Egrets"];
                    const eaglesIndex = birds.indexOf("Eagles");
                    birds.splice(eaglesIndex, 1);
                    ```
    - 常量： const
        ```JavaScript
        const guesses = document.querySElector(".guesses");
        ```
- 运算符
    - 等于： ===
    - 不等于： ！==
    - 大于： >`
    - 小于： `<
- 语句
    - 条件语句：
        - && 表示与
        - || 表示或
        - If else
            ```JavaScript
            if (guessCount === 1) {
                guesses.textContent = "Previous guesses:";
            }
            if (condition1) {
            } else if (condition 2) {
            } else {
            }
            ```
        - Switch
            ```JavaScript
            switch (expresssion) {
                case choice1:
                    break;
                case choice2:
                    break;
                default:
                    break;
            }
            let response;
            switch (true) {
              case (score `< 0 || score >` 100):
                response = "This is not possible, an error has occurred.";
                break;
              case (score `< 20):
                response = "That was a terrible score — total fail!";
                break;
              case (score `< 40):
                response = "You know some things, but it's a pretty bad score. Needs improvement.";
                break;
              case (score `< 70):
                response = "You did a passable job, not bad!";
                break;
              case (score `< 90):
                response = "That's a great score, you really know your stuff.";
                break;
              case (score `<= 100): // 隐含 score >`= 90（因前序条件已过滤）
                response = "What an amazing score! Did you cheat? Are you for real?";
                break;
              default:
                response = "Invalid score input"; // 处理 NaN 等异常值
            }
            ```
        - 三元运算符： condition ? 运行此代码 : 否则运行此代码
            ```JavaScript
            const greeting = isBirthday ? "小王生日快乐“ : ”小王早上好";
            ```
    - 循环语句：
        - 标准for循环： 类似于c语言
            ```JavaScript
            for (initializer; condition; final-expresssion) {
            }
            for (var i = 0; i `< cats.length; i++) {
                info += cats[i] + ",";
            }
            ```
        - while和do while语句
            ```JavaScript
            while (condition) {
            }
            do {
            } while (condition)
            do {
                info += cats[i];
            } while (i `< cats.length);
            ```
        - For of
            ```JavaScript
            const fruits = ["apples", "bananas"];
            for (const fruit of fruits) {
            console.log(fruit);
            }
            ```
- 函数
    - 常规函数
        ```JavaScript
        function checkGuess() {
            alert("I am a placeholder");
        }
        ```
    - 匿名函数
        ```JavaScript
        (function () {
            alert("你好");
        })
        text.Box.addEventListener("keydown", function (event) {
            console.log("you pressed '${event.key}'");
        });
        ```
    - 箭头函数： 用（event) =>` 代替function(event):
        ```JavaScript
        textBox.addEventListener("keydown", (event) =>` {
            console.log("you pressed '${event.key}'");
        });
        ```
- 事件
    - 事件监听器： addEventListener
        - 同一个事件可以添加多个监听器
        ```JavaScript
        guessSubmit.addEventListener("click", checkguess);
        //checkguess是一个函数， 作为事件处理器
        guessSubmit.remove("click", checkguess);
        ```
    - 事件类型
        - Click： 点击
        - focus： 聚焦
        - blur： 失焦
        - dblclick： 双击
        - mouseover： 鼠标悬停
        - mouseout： 鼠标移除按钮
        - play： 只对video等元素有效
        - keydown： 键盘点击
    - 事件处理器属性
        - 比如： onclick
        - 但是事件处理器属性对于同一事件不能叠加， 会覆盖
            ```JavaScript
            btn.onclick = () =>` {
                ....
            };
            ```
    - 内联事件处理器： 不要使用
        ![](https://my.feishu.cn/space/api/box/stream/download/asynccode/?code=MWIyYjQ4NGQ4MDBiMDMzYjE5YzMyZGM1Mzg2NjQ4YmRfTU1DN1hwUHd0aVNsQk4wQzlZTlJubU9SdFFZWFZocHlfVG9rZW46R3ZqeWJnS2l2b1Q2NFJ4VU1mc2Nkd0x4bmVjXzE3NzQxMDU0ODM6MTc3NDEwOTA4M19WNA)
    - 控制器： AbortController()。用于与事件相关联， 监听事件
        ```JavaScript
        const controller = new AbortController();
        btn.addEventListener("click",
          () =>` {
            const rndCol = `rgb(${random(255)}, ${random(255)}, ${random(255)})`;
            document.body.style.backgroundColor = rndCol;
          },
          { signal: controller.signal } // 向该处理器传递 AbortSignal
        );
        controller.abort(); // 移除任何/所有与该控制器相关的事件处理器
        ```
    - 事件对象：event / evt / e。 位于事件处理函数内部， 自动传递给事件处理函数
        ```JavaScript
        const btn = document.querySelector("button");
        function random(number) {
          return Math.floor(Math.random() * (number + 1));
        }
        function bgChange(e) {
          const rndCol = `rgb(${random(255)}, ${random(255)}, ${random(255)})`;
          e.target.style.backgroundColor = rndCol;
          console.log(e);
        }
        btn.addEventListener("click", bgChange);
        ```
    - 事件对象属性
        - 获取事件对象的特定属性： target.getAttribute():
            ```JavaScript
            const buttonBar = document.querySelector(".button-bar");
            function setColor(e) {
              buttonBar.style.backgroundColor = e.target.getAttribute("data-color");
            }
            buttonBar.addEventListener("click", setColor);
            ```
        - preventDefault(): 停止事件
            - 比如说提交表单时存在空内容
            ```JavaScript
            const form = document.querySelector("form");
            const fname = document.getElementById("fname");
            const lname = document.getElementById("lname");
            const para = document.querySelector("p");
            form.addEventListener("submit", (e) =>` {
              if (fname.value === "" || lname.value === "") {
                e.preventDefault();
                para.textContent = "You need to fill in both names!";
              }
            });
            ```
        - 特定事件对象有特定的属性
            - 比如： KeyboardEvent有key属性， 表示哪个键被按下
    - 事件冒泡： 指子元素的事件发生， 同时会触发父元素的事件
        - 优点：
            - 可以在父元素设置监听器， 而不是在子元素中设置
        - 停止事件冒泡： stopPropagation()
            ```JavaScript
            const btn = document.querySelctor("button");
            const box = document.querSelector("div");
            const video = document.querSelector("video");
            btn.addEventListener("click", () =>` box.classList.remove("hidden"));
            video.addEventListener("click", (event) =>` {
            event.stopPropagation();
            video.play();
            })
            box.addEventListener("click", () =>` box.classList.add("hidden"));
            ```
    - 事件捕获： 与事件冒泡类似， 不过事件发生顺序是先发生父元素事件， 后发生子元素事件
        - capture： 默认禁用
        ```JavaScript
        document.body.addEventListener("click", handleClick, { capture: true });
        ```
- 正则表达式
    ```JavaScript
    let text = ":inserta: and :insertb:";
    text = text.replace(/:inserta:/g, "Apple")
              .replace(/:insertb:/g, "Banana");
    // 结果："Apple and Banana"
    ```
- 对象
    - 创建
        ```JavaScript
        const person = {
          name: ["Bob", "Smith"],
          age: 32,
          bio: function () {
            console.log(`${this.name[0]} ${this.name[1]} 现在 ${this.age} 岁了。`);
          },
          introduceSelf: function () {
            console.log(`你好！我是 ${this.name[0]}。`);
          },
        };
        ```
    - 属性访问
        - 点表示法： person.age
        - 括号表示法： person["age"]
            - 括号表示法的优点： 创建新属性时， 成员名称可以使用变量
                ```JavaScript
                person[myDataName] = myDataValue;
                ```
    - 构造函数
        - this： 表示对象， 用于批量创建对象
        ```JavaScript
        function Person(name) {
          this.name = name;
          this.introduceSelf = function () {
            console.log(`你好！我是 ${this.name}。`);
          };
        }
        ```
- 类
    - 原型
        - 为对象分配原型： Object.create()
            ```JavaScript
            const personPrototype = {
              greet() {
                console.log("hello!");
              },
            };
            const carl = Object.create(personPrototype);
            carl.greet(); // hello!
            ```
        - 为对象分配方法： Object.assign()
            ```JavaScript
            const personPrototype = {
              greet() {
                console.log(`hello, my name is ${this.name}!`);
              },
            };
            function Person(name) {
              this.name = name;
            }
            Object.assign(Person.prototype, personPrototype);
            // or
            // Person.prototype.greet = personPrototype.greet;
            ```
        - 检查某属性是否是对象自己的属性： Object.hasOwn()
            ```JavaScript
            const irma = new Person("Irma");
            console.log(Object.hasOwn(irma, "name")); // true
            console.log(Object.hasOwn(irma, "greet")); // false
            ```
    - 创建类
        ```JavaScript
        class Person {
          name;
          constructor(name) {
            this.name = name;
          }
          introduceSelf() {
            console.log(`Hi! I'm ${this.name}`);
          }
        }
        const giles = new Person("Giles");
        giles.introduceSelf(); // Hi! I'm Giles
        ```
    - 类的继承： extends
        ```JavaScript
        class Professor extends Person {
          teaches;
          constructor(name, teaches) {
            super(name);
            this.teaches = teaches;
          }
          introduceSelf() {
            console.log(
              `My name is ${this.name}, and I will be your ${this.teaches} professor.`,
            );
          }
          grade(paper) {
            const grade = Math.floor(Math.random() * (5 - 1) + 1);
            console.log(grade);
          }
        }
        ```
    - 类的封装
        - 私有属性
            ```JavaScript
            class Student extends Person {
              #year;
              constructor(name, year) {
                super(name);
                this.#year = year;
              }
              introduceSelf() {
                console.log(`Hi! I'm ${this.name}, and I'm in year ${this.#year}.`);
              }
              canStudyArchery() {
                return this.#year >` 1;
              }
            }
            ```
        - 私有方法
            ```JavaScript
            class Example {
              somePublicMethod() {
                this.#somePrivateMethod();
              }
              #somePrivateMethod() {
                console.log("You called me?");
              }
            }
            const myExample = new Example();
            myExample.somePublicMethod(); // 'You called me?'
            myExample.#somePrivateMethod(); // SyntaxError
            ```
- DOM脚本
    - 获取元素引用： querySelector() or querySelectorAll()
        ```JavaScript
        //引用document下的第一个section
        const sect = document.querySelector("section");
        //引用document下的所有section
        const sectAll = document.querSelectorAll("section");
        ```
    - 创建元素与其位置锚定： createElement()， appendChild()
        ```JavaScript
        const para = document.createElement("p");
        sect.appendChild(para);
        //文本节点： createTextNode
        const text = document.createTextNode("....");
        para.appendChild(text);
        ```
    - 移动元素： appendChild()
    - 删除元素： parentNode.removeChild();
        ```JavaScript
        linkPara.parentNode.removeChild(linkPara);
        ```
    - 操作css样式
        - 操作内联样式： HTMLElement.style
            ```JavaScript
            para.style.backgroundColor = "black";
            ```
        - 操作外联样式： Element.setAttribute()
            ```JavaScript
            //需要提前设置了highlight
            para.setAttribute("class", "highlight");
            ```
- 异步JavaScript
    - 异步编程： 类似于python中的多线程
    - Promise: 由异步函数返回的对象
        - promise术语
            - pending： 待定
            - fulfilled： 成功
            - rejected： 失败
        - 合并使用promise
            - 所有promise同时实现时开启下一步： Promise.all()
                ```JavaScript
                Promise.all([fetchPromise1, fetchPromise2])
                    .then(...)
                ```
            - 任意一个promise实现开启下一步： Promise.any()
    - 构建异步函数： async和await
        ```JavaScript
        async function fetchProducts() {
          try {
            const response = await fetch(
              "https://mdn.github.io/learning-area/javascript/apis/fetching-data/can-store/products.json",
            );
            if (!response.ok) {
              throw new Error(`HTTP 请求错误：${response.status}`);
            }
            const data = await response.json();
            return data;
          } catch (error) {
            console.error(`无法获取产品列表：${error}`);
          }
        }
        const promise = fetchProducts();
        promise.then((data) =>` console.log(data[0].name));
        ```
    - 异步编程实现从服务器获取数据
        - fetch(url): 返回一个promise对象
        - then(): 构建promise链
        - 捕获错误： catch
    - promise构造器
        - 格式
            ```JavaScript
            //其中resolve, reject是由promise内部提供
            var promise = new Promise(function(resolve, reject){ // executor })
            ```
- Worker： 书写脚本
    - 由于较麻烦， 直接观看[教程](https://developer.mozilla.org/zh-CN/docs/Learn_web_development/Extensions/Async_JS/Introducing_workers)
- Json
    - json中只使用双引号
    - 从网页获取json数据
        - 示例
            ```JavaScript
            async function populate() {
              const requestURL =
                "https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json";
              const request = new Request(requestURL);
              const response = await fetch(request);
              const superHeroes = await response.json();
              populateHeader(superHeroes);
              populateHeroes(superHeroes);
            }
            ```
        - json对象与字符串类型间的转换
            - 字符串转化为json: JSON.parse()
                ```JavaScript
                async function populate() {
                  const requestURL =
                    "https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json";
                  const request = new Request(requestURL);
                  const response = await fetch(request);
                  const superHeroesText = await response.text();
                  const superHeroes = JSON.parse(superHeroesText);
                  populateHeader(superHeroes);
                  populateHeroes(superHeroes);
                }
                ```
            - json转化为字符串： JSON.stringify()
                ```JavaScript
                let myObj = { name: "Chris", age: 38 };
                myObj;
                let myString = JSON.stringify(myObj);
                myString;
                ```
- 常见库
    - Math.floor: 向下取整
    - Math.random: 产生[0, 1) 的随机数