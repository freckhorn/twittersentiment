h = open('teslar.p', 'wb')
import pickle as pk
import os
fileslist = os.listdir("/user/research/ptan/data/Twitter")
output = []

for k in range(500):#len(fileslist)):
	print(k)
	opened = "/user/research/ptan/data/Twitter/" + fileslist[k]
	f = open(opened,"r")
	i = 0
	j = 3
	while True:
		split = f.readline()#.split("{}")
		if len(split) == 0:
			break
		if i % 2 == 0:
			if 3 < len(split.split(',')):
				if " tesla " in split.split(',')[3]:
					tw = {'ind':0, 'txt': str(), 'date': None}
					tw['ind'] = i
					tw['txt'] = split.split(',')[3][8:-1]
					tw['date'] = split.split(',')[0][15:-1]
					print(tw)
					output.append(tw)
		i += 1
	pk.dump(output, open("tesla2.p", "wb"))
	

	d = pk.load( open( "tesla2.p", "rb" ) )

	print("length is ", len(d))
h.close()
