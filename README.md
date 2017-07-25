# Paint the World

## 脚本使用方法

脚本分为两部分：对象，动作

使用的时间轴单位为秒，绘画或暂停时计时器停止。

```json
{
	"obj":[],
	"actions":[]
}
```

## 对象(obj)格式：
```json
{
	"name":"background",
	"tex":"bg.jpg",
	"pos":[0,0,0],
	"scale":1.5
},
{
	"name": "sun",
	"tex": "sun.png",
	"scale": 0.3,
	"pos": [100, 100, 20]
}
```

其中，name为对象名称；tex为图片文件名（图片统一存储在res/文件夹下）

pos为对象位置，[x,y,z]

其中，以左上角为原点

```
*--------> x
|
|
|
|
V
Y
```

可选参数:

scale: 图像放缩比例

hide: [bool]对象初始时是否隐藏

## 动作(actions)格式：

- move 直线移动

obj为被操作的对象，start为开始动作的秒数，offset为位移

```json
{
	"type": "move",
	"obj": "sun",
	"start": 2,
	"offset": [0, -100]
}
```

- bezier 贝塞尔曲线移动 

end为终止动作的秒数[可选]

seq为贝塞尔曲线点坐标

v为移动速度

```json
{
	"type": "bezier",
	"obj": "xiaoming",
	"start": 3,
	"end": 20,
	"seq": [[300, 450], [450, 100],[650, 450]],
	"v": 0.001
}
```

- change_tex 改变对象贴图

tex为目标贴图

```json
{
	"type": "change_tex",
	"obj": "xiaoming",
	"tex": "xiaoming.png",
	"start": 3.5
}
```

- rotate 旋转

逆时针为正方向

可选参数

end: 终止旋转的时间

tovalue: 目标角度(角度制, 正图像的角度为0度）

```json
{
	"type": "rotate",
	"obj": "sun",
	"v": 2,
	"start": 1
}
```

- scale 放缩 

tovalue: 目标比例

```json
{
	"type": "scale",
	"obj": "sun",
	"v": 0.01,
	"start": 1,
	"tovalue": 0.5
}
```

- hide, show 隐藏，显示

```json
{
	"type": "show",
	"obj": "sun",
	"start": 4
}
```

- move_screen 移动屏幕

```json
{   
	"type": "move_screen",
	"offset": [200, 0],
	"start": 3,
	"v": 1
}
```

- pause 暂停

- draw 绘画

绘画窗口位置及大小：window [x,y,w,h]
绘画的正确类型: kind

```json
{
	"type": "draw",
	"window": [10,10,200, 200],
	"kind": "bird"
}
```
