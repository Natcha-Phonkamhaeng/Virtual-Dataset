import random

name_list = []

name = ['Sheldon Cooper', 'Penny Hofstedter', 'Sheldon Cooper']
domain = '@fakemail.com'

for i in name:
	i = i.lower().split()
	name = '.'.join(i)	
	if name in name_list:
		rand = random.randint(1,10)
		name = name+'_'+str(rand)		
	name_list.append(name)

my_list = []
for i in name_list:
	i = i+domain
	my_list.append(i)

print(my_list)





