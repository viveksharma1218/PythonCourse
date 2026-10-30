name = 'jack sparrow';
print(name[0]);

# indexing
# we can access characters using negative value but can not go outside range
print(name[-1]);

print(name[-12]);

# this will show error
# print(name[-22]);

# slicing

print(name[1:11]);
print(name[:12]);
print(name[2:]);
#reverse
print(name[-1])

#concatenation and repetation
print('hello' + ' ' + 'world');
print('hello  : ' * 3);
# error print('hello' + 3);
print('hello  : ' + '3');