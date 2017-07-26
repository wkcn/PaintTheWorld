import json
import random

def test(df):
	m={
		"name":"scene",
		"tex":"paint/cartoon-stone-forest-scene-3d-model-max.jpg",
		"pos":[0,0,0],
		"scale":1.7,
	}
	df['obj'].append(m)

	m={
		"name":"human_3",
		"tex":"paint/boy2.png",
		"pos":[0,370,0],
		"scale":0.3,
	}
	df['obj'].append(m)

	m={
		"name":"monster",
		"tex":"paint/bc3c66bac6c21ab1896f37b663d34a64.png",
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
		"tex":"paint/house_in_the_forest_1280x800.jpg",
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

	return df

def sun(df):
	#draw sun
	m={
		"type":"draw",
		"window":[100,0,200,200],
		"kind":"sun",
		"start":1
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
		"offset":[0,-80]
	}
	df['actions'].append(m)
	m={
		"type":"rotate",
		"obj":"sun",
		"v":5,
		"start":1
	}
	df['actions'].append(m)
	return df

def cloud(df):
	interval_time=3
	#draw cloud
	m={
		"type":"draw",
		"window":[300,0,500,100],
		"kind":"cloud",
		"start":3
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
	return df

def carema(df):
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
		"name":"house_inside",
		"tex":"paint/house_inside6.jpg",
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
		"tex":"paint/boy2.png",
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
		"window":[300,0,0,0],
		"kind":"face",
		"start":17
	}
	df['actions'].append(m)	
	return df

def kitchen(df):
	#create obj
	m={
		"name":"kitchen",
		"tex":"paint/house_inside9.jpg",
		"pos":[300,300,0],
		"scale":0.5,
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
		"window":[650,250,100,100],
		"kind":"face",
		"start":24
	}
	df['actions'].append(m)	
	return df

def human_1(df):
	m={
		"name":"human_1",
		"tex":"paint/boy2.png",
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

def tunnel(df):
	#create obj
	m={
		"name":"kitchen",
		"tex":"paint/house_inside9.jpg",
		"pos":[300,300,0],
		"scale":0.5,
		'hide':True
	}
	df['obj'].append(m)
	m={
		"type":"show",
		"obj":"kitchen",
		"start":19
	}
	df['actions'].append(m)
	return df

def time_travel(df):
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
		"start":25
	}
	df['actions'].append(m)
	m={
		"name":"time_machine",
		"tex":"paint/time_machine.png",
		"pos":[450,600,0],
		"scale":0.75,
		'hide':True
	}
	df['obj'].append(m)
	m={
		"type":"show",
		"obj":"time_machine",
		"start":25
	}
	df['actions'].append(m)
	m={
		"name":"human_2",
		"tex":"paint/boy2.png",
		"pos":[560,720,0],
		"scale":0.15,
		'hide':True
	}
	df['obj'].append(m)
	m={
		"type":"show",
		"obj":"human_2",
		"start":25
	}
	df['actions'].append(m)
	m={
		"type":'move',
		"obj":'time_machine',
		"start":25,
		'v':1,
		"offset":[200,-200]
	}
	df['actions'].append(m)
	m={
		"type":'move',
		"obj":'human_2',
		"start":25,
		'v':1,
		"offset":[200,-200]
	}
	df['actions'].append(m)
	return df

def beat_monster(df):
	m={
		"name":"scene",
		"tex":"paint/cartoon-stone-forest-scene-3d-model-max.jpg",
		"pos":[300,300,0],
		"scale":1.7,
		'hide':True
	}
	df['obj'].append(m)
	m={
		"type":"show",
		"obj":"scene",
		"start":28
	}
	df['actions'].append(m)
	m={
		"name":"human_3",
		"tex":"paint/boy2.png",
		"pos":[300,670,0],
		"scale":0.3,
		'hide':True
	}
	df['obj'].append(m)
	m={
		"type":"show",
		"obj":"human_3",
		"start":28
	}
	df['actions'].append(m)
	m={
		"name":"monster",
		"tex":"paint/bc3c66bac6c21ab1896f37b663d34a64.png",
		"pos":[900,700,0],
		"scale":0.2,
		'hide':True
	}
	df['obj'].append(m)
	m={
		"type":"show",
		"obj":"monster",
		"start":28
	}
	df['actions'].append(m)
	m={
		"type":'move',
		"obj":'human_3',
		"start":29,
		'v':2,
		"offset":[200,0]
	}
	df['actions'].append(m)
	m={
		"type":'move',
		"obj":'monster',
		"start":29,
		'v':2,
		"offset":[-200,0]
	}
	df['actions'].append(m)
	#draw weapon
	m={
		"type":"draw",
		"window":[300,470,100,100],
		"kind":"weapon",
		"start":31
	}
	df['actions'].append(m)	
	m={
		"type":"hide",
		"obj":"monster",
		"start":32
	}
	df['actions'].append(m)
	m={
		"type":'move',
		"obj":'human_3',
		"start":32,
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
df=clear(df,25)

df=time_travel(df)
df=clear(df,28)

df=beat_monster(df)
#df=test(df)
with open("stage1.json",'w') as f:
	json.dump(df,f)