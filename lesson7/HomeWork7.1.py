def say_hi(name, age):
    return f"Hi. My name is {name} and I am {age} years old"
assert say_hi("Alex",32) == "Hi. My name is Alex and I am 32 years old", "Test1"
assert say_hi("Frank",68) == "Hi. My name is Frank and I am 68 years old", "Test2"
print("OK")