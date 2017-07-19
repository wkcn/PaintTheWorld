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
			"pos": [300, 450, 40],
            "scale": 0.2
		}
	],
	"actions":[
		{
			"type": "move",
            "obj": "sun",
            "start": 2,
            "end": 99999,
            "offset": [0, -100]
		},
		{
			"type": "route",
			"obj": "xiaoming",
            "start": 3,
            "end": 20,
			"routes": [[350, 440],[400, 430]],
            "v": 3
		}
	]
}
