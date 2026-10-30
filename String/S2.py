# String formatting in 2 ways
# using variable in between strings

#f

name = 'jack';
age = 33;

print(f"my name is {name} and my age is {age}");

# .format()

print("my name is {} and my age is {}".format(name, age));

# case conversion
print(name.upper());
print(name.lower());
print(" capitalize will convert only first character in uppercase ")
print(name.capitalize());
print("jaCK".swapcase());


# searching and checking

s = "movie: pirates of the carriabean sea is a good movie."

print(s.find('v'));
print(s.find('movie'));
#find last occurence
print(s.rfind('movie'));
print(s.index('i'));
print(s.startswith("movie"));
print(s.endswith("movie."));
#check if "hello world" contains "hello"
print("hello" in "hello world");


