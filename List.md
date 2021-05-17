## What Is a List?

A list is a collection of items in a particular order.

### Initialize a list

````
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
birds = []
````

### Accessing Elements in a List

````
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])
````

### Modify a value in the list
````
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
bicycles[0] = "tank"
print(bicycles[0])
````

### Add a value in the list
````
# append a value
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
bicycles.append("tank")

# insert a value in the beginning
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
bicycles.insert(0, "tank")
````

### Remove a value from a list
````
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# please google and find thoe to remove element 'redline'
````

### Finding the Length of a List
````
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(len(bicycles))
````

### Iterate a List
````
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
for bicycle in bicycles:
    print(bicycle)
````

### some additional method
````
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
bicycles.sort()
print(bicycles)

bicycles.reverse()
print(bicycles)
````

### quiz

1. Write a program to combine two list in one and sort it

    bicycles = ['trek', 'cannondale', 'redline', 'specialized']
    
    cars = ['Ford', 'Honda', 'Tesla']
    
1. Iterate a list of integer. Print the minimun and maximum value.

   numbers = [2, 9, 100, 230, 3, 6, 99]
   
   
