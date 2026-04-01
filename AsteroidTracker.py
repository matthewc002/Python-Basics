#Hello Func

name= input('Hello, what is your name? ')

import time

print(f'''{name},... 

Accessing Asteroid files... ''')

print('...')

time.sleep(2)

#Dictionary of Asteroids

asteroids= {
    'Apophis':{'size': 370, 'mass': 2.7e10, 'threat': 3, 'close approach': 2029, 'type': 'NEA'},
    'Bennu': {'size': 490, 'mass': 7.8e10, 'threat': 2, 'close approach': 2135, 'type': 'NEA'},
    'Eros': {'size': 16800, 'mass': 6.7e15, 'threat': 1, 'close approach': 2056, 'type': 'NEA'},
    'Ganymed': {'size': 35000, 'mass': 1.25e17, 'threat': 0, 'close approach': 0, 'type': 'NEA'}

}

#Asteroid Sorting

#Size
sorted_by_size = sorted(asteroids.items(), key=lambda x: x[1]['size'], reverse=True)
print('''
      Asteroids, sorted by size (Largest to Smallest)''')
for name, info in sorted_by_size:
    print (f'''{name}: {info['size']} meters''')

print('...')

time.sleep(6)

#Mass
sorted_by_mass = sorted(asteroids.items(), key=lambda x: x[1]['mass'], reverse=True)
print('''
      Asteroids, sorted by mass (Heaviest to Lightest)''')
for name, info in sorted_by_mass:
    print(f'''{name}: {info['mass']} kg''')

print('...')

time.sleep(6)

#Threat
sorted_by_threat = sorted(asteroids.items(), key=lambda x: x[1]['threat'], reverse=True)
print('''
      Asteroids, sorted by threat level (Greatest to Smallest)''')
for name, info in sorted_by_threat:
    print(f'''{name}: Level {info['threat']} threat''')

print('...')

time.sleep(6)

#Approach
sorted_by_approach = sorted(asteroids.items(), key=lambda x: x[1]['close approach'])
print('''
      Asteroids, sorted by estimated approach date (0=NA)''')
for name, info in sorted_by_approach:
    print(f'''{name}: Year {info['close approach']}''')

print('...')

time.sleep(6)

#Goodbye Func
print(f'''This is all information currently available ...
      ...

Thank You.
    ''')