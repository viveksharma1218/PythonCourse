# splitting and joining

fruits = "apple,banana,oragne";
items = fruits.split(',');
print(items);

allFruits = " | ".join(items);
print(allFruits);

words = "i am practicing python in VS code".split();

print(words);

# strip and replace

raw = " hello    ";
print(raw.strip());
print(raw.rstrip());
print(raw.lstrip);

s = "I like cats and cats are fast";
print(s.replace('cats' , 'dogs'));