import json
import random

def test(df):
	m={
		"name":"kitchen",
		"tex":"paint/house_inside9.jpg",
		"pos":[0,0,0],
		"scale":0.5,

	}
	df['obj'].append(m)
	m={
		"name":"human",
		"tex":"paint/boy2.png",
		"pos":[0,300,0],
		"scale":0.3,
	}
	df['obj'].append(m)
	m={
		"type":"move",
		"obj":"human",
		"offset":[550,0],
		"start":0,
		"v":3
	}
	df['actions'].append(m)
	m={
		"type":"move",
		"obj":"human",
		"offset":[0,-150],
		"start":3.3,
		"v":3
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
	#create sun
	m={
		"name":"sun",
		"tex":"paint/sun.png",
		"pos":[150,80,0],
		"scale":1
	}
	df['obj'].append(m)
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
			"start":2+interval_time*i+random.randint(-interval_time+1,0)
		}
		df['actions'].append(m)
		m={
			"type":"move",
			'obj':"cloud"+str(i),
			"start":2+interval_time*i+random.randint(-interval_time+1,0),
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
		"type":"bezier",
		"obj":"human",
		"start":13,
		"end":15,
		"seq":[[600,650],[800,650],[900,550]],
		"v":0.001
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
		"start":15
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
		"start":15
	}
	df['actions'].append(m)
	m={
		"type":"move",
		"obj":"human_1",
		"offset":[550,0],
		"start":15,
		"v":3
	}
	df['actions'].append(m)
	m={
		"type":"move",
		"obj":"human_1",
		"offset":[0,-150],
		"start":18.3,
		"v":3
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
df=clear(df,15)
df=kitchen(df)
df=human_1(df)

#df=test(df)
with open("stage1.json",'w') as f:
	json.dump(df,f)