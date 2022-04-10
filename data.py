from faker import Faker
import random
import pandas as pd
import uuid

# number of user
num_users = 10
fake = Faker()

# columns name for dataframe
col = [
	'id',
	'name',
	'gender',
	'email',
	'education',
	'age'
]

# creating columns using Pandas Dataframe
df = pd.DataFrame(columns=col)

# generate unique id
id_list = []
for i in range(num_users):
	i = uuid.uuid4().hex
	id_list.append(i)
df['id'] = id_list

# generate gender
gender_list = ['male', 'female']
gender = random.choices(gender_list, weights=(40,70), k=num_users)
df['gender'] = gender

# generate name base on gender
name_list = []
for i in df['gender']:
	if i == 'male':
		i = fake.name_male()
	elif i == 'female':
		i = fake.name_female()
	name_list.append(i)
df['name'] = name_list

# generate unique email
domain = '@fakemail.com'
my_list = []
for i in df['name']:
	i = i.lower().split()
	name = '.'.join(i)
	if name in my_list:
		rand = random.randint(0,20)
		name = name+str(rand)
	my_list.append(name)

email_list = []
for i in my_list:
	i = i+domain
	email_list.append(i)

df['email'] = email_list

# generate education
edu_list = []
edu = ['High School', 'Bachelor', 'Master']

for i in df['name']:
	if i.startswith('Dr.'):
		rand = 'PhD'
	else:
		rand = random.choice(edu)
	edu_list.append(rand)
df['education'] = edu_list

# generate age columns
# High School 18 above
# Bachelor 22 above
# Master 24 above
# PhD 26 above
age_list = []
for i in df['education']:
	if i == 'PhD':
		i = random.randint(26, 60)
	elif i == 'Master':
		i = random.randint(24, 60)
	elif i == 'Bachelor':
		i = random.randint(22, 60)
	else:
		i = random.randint(18, 60)
	age_list.append(i)

df['age'] = age_list

print(df)


