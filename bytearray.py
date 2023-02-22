class Cat:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        
cat = Cat('A',2)

cat_byteArray = bytearray(source=cat)

print(cat)
print(cat_byteArray)