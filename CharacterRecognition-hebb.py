X1 = [
    '#...#',
    '.#.#.',
    '.....',
    '.#.#.',
    '#...#',
]

X2 = [
    '#...#',
    '.....',
    '..#..',
    '.#.#.',
    '#...#',
]

X3 = [
    '#...#',
    '.#.#.',
    '..#..',
    '.....',
    '#...#',
]

X4 = [
    '.....',
    '.#.#.',
    '..#..',
    '.#.#.',
    '.....',
]

O1 = [
    '.###.',
    '#...#',
    '#...#',
    '#...#',
    '.###.',
]

O2 = [
    '.....',
    '#####',
    '#...#',
    '#####',
    '.....',
]

O3 = [
    '..#..',
    '#...#',
    '#...#',
    '#...#',
    '..#..',
]

O4 = [
    '.###.',
    '#...#',
    '.....',
    '#...#',
    '.###.',
]

def convert(char):
    return [
        -1 if pixel == '.' else 1
        for line in char
        for pixel in line
    ]


train= [
    [convert(X1), +1],
    [convert(X2), +1],
    [convert(X3), +1],
    [convert(X4), +1],
    [convert(O1), -1],
    [convert(O2), -1],
    [convert(O3), -1],
    [convert(O4), -1]
]

b = 0
w = [0] * len(train[0][0])

for x, y in train:
    for i in range(len(w)):
        w[i] = w[i] + x[i] * y
        b = b + y


def dot(x, y):
    return sum([x_i * y_i for x_i, y_i in zip(x, y)])


def threshold(y):
   if y >= 0:
       return 'class x'
   else: 
        return 'class O'


for x, y in train:
    response = dot(w, x) + b
    print(f'Prediction: {threshold(response)}')
    print(f'Label: {threshold(y)}','\n')


t1O = [
    '..##.',
    '.#..#',
    '.#..#',
    '.#..#',
    '..##.',
]

t2O = [
    '..##.',
    '.....',
    '.#..#',
    '.#..#',
    '..##.',
]

t1X = [
    '#....',
    '.#.#.',
    '..#..',
    '.#.#.',
    '....#',
]

t2X = [
    '#....',
    '.#.#.',
    '.....',
    '.#.#.',
    '.....',
]
test = [
    convert(t1O),
    convert(t2O),
    convert(t1X),
    convert(t2X),
]
print('\nresult with test:\n')
for x in test:
    response = dot(w, x) + b
    print(f'Prediction: {threshold(response)}','\n')