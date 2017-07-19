{
	"obj":[
		{
			"name":"baclground",
			"tex":"bg.jpg",
			"pos":[0,0,0],
			"scale":1.5
		},
		{
			"name": "sun",
			"tex": "sun.png",
			"scale": 0.3,
			"pos": [100, 100, 20]
		},
		{
			"name": "xiaoming",
			"tex": "xiaoming.png",
			"pos": [100, 500, 40]
		}
	],
	"actions":[
		{
			"name": "move",
			"par": ["sun", [0, -200], 2],
			"time": [2, 7]
		},
		{
			"name": "route",
			"par": ["xiaoming"],
			"time": [3, 20],
			"routes": [[120, 500],[120, 480],[125, 500],[125, 520]]
		}
	]
}
