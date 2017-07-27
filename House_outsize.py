#coding=utf-8
import json
import random

def test(df):
	m={
		"name":"scene",
		"tex":"color/house.png",
		"pos":[0,0,0],
		"scale":1.7,
	}
	df['obj'].append(m)

	m={
		"name":"human_3",
		"tex":"color/boy2.png",
		"pos":[0,370,0],
		"scale":0.3,
	}
	df['obj'].append(m)

	m={
		"name":"monster",
		"tex":"color/dinosaur.png",
		"pos":[600,400,0],
		"scale":0.2,
	}
	df['obj'].append(m)
	m={
		"type":'move',
		"obj":'human_3',
		"start":0,
		'v':2,
		"offset":[200,0]
	}
	df['actions'].append(m)
	m={
		"type":'move',
		"obj":'monster',
		"start":0,
		'v':2,
		"offset":[-200,0]
	}
	df['actions'].append(m)

	m={
		"type":"hide",
		"obj":"monster",
		"start":3
	}
	df['actions'].append(m)
	m={
		"type":'move',
		"obj":'human_3',
		"start":3,
		'v':2,
		"offset":[450,0]
	}
	df['actions'].append(m)

	return df
	

def house(df):
	#create obj
	m={
		"name":"house_outside",
		"tex":"color/house.png",
		"pos":[-100,0,0],
		"scale":0.76
	}
	df['obj'].append(m)

	#scale the house_outsize in the begining
	m={
		"type":"scale",
		"obj":"house_outside",
		"v":0.5,
		"start":10,
		"tovalue":1.4
	}
	df['actions'].append(m)

	m={
        "type":"caption",
        "caption":"这是一个美好的早晨",
        "start":0
    }
	df['actions'].append(m)

	m={
        "type":"caption",
        "caption":"太阳公公起床了",
        "start":0.9
    }
	df['actions'].append(m)

	return df

def sun(df):
	#draw sun
	m={
		"type":"draw",
		"window":[100,100,200,200],
		"kind":"太阳",
		"start":0.9,
	}
	df['actions'].append(m)
	#create sun
	m={
		"name":"sun",
		"tex":"paint/sun.png",
		"pos":[150,80,0],
		"scale":1,
		'hide':True
	}
	df['obj'].append(m)
	m={
		"type":"show",
		"obj":"sun",
		"start":1
	}
	df['actions'].append(m)
	#move and rotate
	m={
		"type":'move',
		"obj":'sun',
		"start":1,
		'v':1,
		"offset":[0,-80],
        "hold":True
	}
	df['actions'].append(m)
	m={
		"type":"rotate",
		"obj":"sun",
		"v":5,
		"start":1,
        "hold":True
	}
	df['actions'].append(m)
	return df

def cloud(df):
	interval_time=3
	#draw cloud
	m={
		"type":"draw",
		"window":[400,0,200,200],
		"kind":"云",
		"start":3,
	}
	df['actions'].append(m)
	#create cloud
	for i in range(4):
		m={
			"name":"cloud"+str(i),
			"tex":"paint/cloud.png",
			"pos":[850,random.randint(-50,50),0],
			"scale":0.5,
			"hide":True
		}
		df['obj'].append(m)
		m={
			'type':"show",
			'obj':"cloud"+str(i),
			"start":4+interval_time*i+random.randint(-interval_time+1,0)
		}
		df['actions'].append(m)
		m={
			"type":"move",
			'obj':"cloud"+str(i),
			"start":4+interval_time*i+random.randint(-interval_time+1,0),
			"offset":[-1200,0]
		}
		df['actions'].append(m)


	m={
        "type":"caption",
        "caption":"云朵飘啊飘",
        "start":2.9
    }
	df['actions'].append(m)

	return df

def carema(df):

	m={
        "type":"caption",
        "caption":"真是一幅生机勃勃的景象啊！",
        "start":5
    }
	df['actions'].append(m)

	m={
        "type":"color",
        "start":7
    }
	df['actions'].append(m)

	m={
        "type":"caption",
        "caption":"让我们进入屋子里看看吧！",
        "start":9.5
    }
	df['actions'].append(m)

	m={   
	"type": "move_screen",
	"offset": [300, 300],
	"start": 10,
	"v": 1
	}
	df['actions'].append(m)
	return df
	m={
		"type":'move',
		"obj":'sun',
		"start":1,
		'v':1,
		"offset":[0,-80]
	}
	df['actions'].append(m)
df={
	"obj":[],
	"actions":[]
}


#stage2

def clear(df,time):
	for i in df['obj']:
		m={
			"type":"hide",
			"obj":i['name'],
			"start":time
		}
		df['actions'].append(m)
	
	return df

def house_inside(df):
	#create obj

	m={
        "type":"caption",
        "caption":"小朋友起床了",
        "start":12
    }
	df['actions'].append(m)

	m={
		"name":"house_inside",
		"tex":"color/bedroom.png",
		"pos":[300,300,0],
		"scale":0.57,
		'hide':True
	}
	df['obj'].append(m)
	m={
		"type":"show",
		"obj":"house_inside",
		"start":12
	}
	df['actions'].append(m)
	return df
def human(df):
	m={
		"name":"human",
		"tex":"color/boy2.png",
		"pos":[600,650,0],
		"scale":0.3,
		'hide':True
	}
	df['obj'].append(m)

	m={
		"type":"show",
		"obj":"human",
		"start":12
	}
	df['actions'].append(m)
	m={
		"name":"b",
		"tex":"board.png",
		"pos":[600,650,0],
		"scale":0.35,
		'hide':True
	}
	df['obj'].append(m)
	m={
		"type":"show",
		"obj":"b",
		"start":12
	}


	m={
        "type":"caption",
        "caption":"他走到镜子前打扮",
        "start":14
    }
	df['actions'].append(m)


	df['actions'].append(m)
	m={
		"type":"bezier",
		"obj":"human",
		"start":13,
		"end":15,
		"seq":[[600,650],[800,650],[900,550]],
		"v":0.001
	}
	df['actions'].append(m)
	m={
		"type":'move',
		"obj":'human',
		"start":15,
		'v':2,
		"offset":[100,-210]
	}
	df['actions'].append(m)
	m={
		"type":"bezier",
		"obj":"b",
		"start":13,
		"end":15,
		"seq":[[600,650],[800,650],[900,550]],
		"v":0.001
	}
	df['actions'].append(m)


	m={
        "type":"color",
        "start":15.5
    }
	df['actions'].append(m)


	m={
        "type":"caption",
        "caption":"小朋友的眼睛鼻子嘴长什么样呢？",
        "start":16
    }
	df['actions'].append(m)


	m={
		"type":'move',
		"obj":'b',
		"start":15,
		'v':2,
		"offset":[100,-210]
	}
	df['actions'].append(m)
	#draw face
	m={
		"type":"draw",
		"window":[711,109,82,52],
		"kind":["脸","鬼脸","头", "嘴巴", "耳朵", "鼻子", "眼睛"],
        "face": True,
		"start":17
	}
	df['actions'].append(m)	


	m={
        "type":"caption",
        "caption":"真是个可爱的小朋友呢！",
        "start":17.1
    }
	df['actions'].append(m)

	return df

def kitchen(df):
	#create obj

	m={
        "type":"caption",
        "caption":"小朋友走到来到餐桌前",
        "start":18.9
    }
	df['actions'].append(m)

	m={
        "type":"caption",
        "caption":"他需要补充能量",
        "start":19.5
    }
	df['actions'].append(m)

	m={
		"name":"kitchen",
		"tex":"color/kitchen.png",
		"pos":[300,300,0],
		"scale":0.5,
		'hide':True
	}
	df['obj'].append(m)


	m={
		"name":"food",
		"tex":"color/kitchen.png",
		"pos":[983,527,2],
		"scale":1.0,
		'hide':True
	}
	df['obj'].append(m)

	m={
		"type":"show",
		"obj":"kitchen",
		"start":19
	}
	df['actions'].append(m)


	#draw breakfast
	m={
		"type":"draw",
		"window":[650,220,100,100],
        "kind":["苹果", "香蕉", "面包", "蛋糕", "鱼", "汉堡", "热狗", "冰淇淋", "龙虾", "梨", "菠萝","番茄", "公鸡"],
		"start":24,
        "rep":"food"
	}
	df['actions'].append(m)	
	m={
		"type":"show",
		"obj":"food",
		"start":24.2
	}
	df['actions'].append(m)



	m={
        "type":"caption",
        "caption":"你为他准备什么食物呢？",
        "start":23.9
    }
	df['actions'].append(m)

	return df

def human_1(df):
	m={
		"name":"human_1",
		"tex":"color/boy2.png",
		"pos":[300,600,0],
		"scale":0.3,
		'hide':True
	}
	df['obj'].append(m)
	m={
		"type":"show",
		"obj":"human_1",
		"start":19
	}
	df['actions'].append(m)
	m={
		"type":"move",
		"obj":"human_1",
		"offset":[550,0],
		"start":19,
		"v":3
	}
	df['actions'].append(m)
	m={
		"type":"move",
		"obj":"human_1",
		"offset":[0,-150],
		"start":22.3,
		"v":3
	}
	df['actions'].append(m)
	return df



def time_travel(df):

	m={
        "type":"color",
        "start":24
    }
	df['actions'].append(m)

	m={
        "type":"caption",
        "caption":"嗯！吃饱了就可以出门啦！",
        "start":24.9,
    }
	df['actions'].append(m)
	m={
        "type":"caption",
        "caption":"那接下来进行时光之旅吧！",
        "start":25.9,
    }
	df['actions'].append(m)
	m={
		"name":"tunnel",
		"tex":"paint/tunnel2.jpg",
		"pos":[300,300,0],
		"scale":1.5,
		'hide':True
	}

	df['obj'].append(m)

	m={
		"type":"show",
		"obj":"tunnel",
		"start":28
	}
	df['actions'].append(m)
	m={
		"name":"time_machine",
		"tex":"color/timemachine.png",
		"pos":[650,450,0],
		"scale":0.75,
		'hide':True
	}
	df['obj'].append(m)
	m={
		"type":"show",
		"obj":"time_machine",
		"start":28
	}
	df['actions'].append(m)
	m={
		"name":"human_2",
		"tex":"color/boy2.png",
		"pos":[760,560,0],
		"scale":0.15,
		'hide':True
	}
	df['obj'].append(m)
	m={
		"type":"show",
		"obj":"human_2",
		"start":28
	}
	df['actions'].append(m)
	m={
		"type":'move',
		"obj":'time_machine',
		"start":28,
		'v':1,
		"offset":[-200,200]
	}
	df['actions'].append(m)
	m={
		"type":'move',
		"obj":'human_2',
		"start":28,
		'v':1,
		"offset":[-200,200]
	}
	df['actions'].append(m)


	m={
        "type":"color",
        "start":28.5
    }
	df['actions'].append(m)


	return df

def beat_monster(df):
	m={
        "type":"caption",
        "caption":"来到远古时代了耶！",
        "start":31,
    }
	df['actions'].append(m)
	m={
        "type":"caption",
        "caption":"不好,前面出现了怪物！",
        "start":33,
    }
	df['actions'].append(m)
	m={
        "type":"caption",
        "caption":"该用什么武器？",
        "start":35,
    }
	df['actions'].append(m)
	m={
        "type":"caption",
        "caption":"我们打败怪兽了耶！",
        "start":36,
    }
	df['actions'].append(m)
	m={
        "type":"caption",
        "caption":"我们继续旅行吧！",
        "start":37.5,
    }
	df['actions'].append(m)


	m={
        "type":"color",
        "start":38
    }
	df['actions'].append(m)


	m={
		"name":"scene",
		"tex":"color/ancient.png",
		"pos":[300,300,0],
		"scale":1.7,
		'hide':True
	}
	df['obj'].append(m)
	m={
		"type":"show",
		"obj":"scene",
		"start":31
	}
	df['actions'].append(m)
	m={
		"name":"human_3",
		"tex":"color/boy2.png",
		"pos":[300,670,0],
		"scale":0.3,
		'hide':True
	}
	df['obj'].append(m)
	m={
		"type":"show",
		"obj":"human_3",
		"start":31
	}
	df['actions'].append(m)

	m={
		"name":"monster",
		"tex":"color/dinosaur.png",
		"pos":[900,700,0],
		"scale":0.2,
		'hide':True
	}
	df['obj'].append(m)

	m={
		"name":"weapon",
		"tex":"color/dinosaur.png",
		"pos":[587,645,0],
		"scale":0.2,
		'hide':True
	}

	df['obj'].append(m)

	m={
		"type":"show",
		"obj":"monster",
		"start":33
	}
	df['actions'].append(m)
	m={
		"type":'move',
		"obj":'human_3',
		"start":31,
		'v':2,
		"offset":[200,0]
	}
	df['actions'].append(m)
	m={
		"type":'move',
		"obj":'monster',
		"start":33,
		'v':2,
		"offset":[-200,0]
	}
	df['actions'].append(m)
	#draw weapon
	m={
		"type":"draw",
		"window":[280,470,100,100],
		"kind":["苹果", "斧头", "香蕉", "啤酒杯", "长椅", "书", "碗", "回旋镖", "萝卜", "飞碟", "叉子", "平底锅", "步枪", "剪刀", "螺丝刀", "网球拍", "轮胎", "番茄"],
		"start":35,
        "rep":"weapon"
	}


	df['actions'].append(m)	


	m={
		"type":"show",
		"obj":"weapon",
		"start":35.1
	}
	df['actions'].append(m)

	m={
		"type":"move",
		"obj":"weapon",
		"start":35.2,
        "offset":[600, 0],
        "v":3
	}
	df['actions'].append(m)

	m={
		"type":"rotate",
		"obj":"weapon",
		"v":5,
		"start":35.2
	}
	df['actions'].append(m)


	m={
		"type":"hide",
		"obj":"monster",
		"start":36
	}
	df['actions'].append(m)
	m={
		"type":'move',
		"obj":'human_3',
		"start":37.5,
		'v':2,
		"offset":[450,0]
	}
	df['actions'].append(m)

	return df

df=house(df)
df=sun(df)
df=cloud(df)
df=carema(df)
df=clear(df,12)

df=house_inside(df)
df=human(df)
df=clear(df,19)

df=kitchen(df)
df=human_1(df)
df=clear(df,28)

df=time_travel(df)
df=clear(df,31)

df=beat_monster(df)
#df=test(df)
with open("stage1.json",'w') as f:
	json.dump(df,f)
