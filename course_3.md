## Array 

A single variable that is used to store different elements

````
// Initialization
let a = [];   // The variable a refers to an empty array.
let a = ["a","b","c"];

// Add an item to the end of an Array
let fruits = ['Apple', 'Banana']
fruits.push('Orange')

// Loop over an Array
let fruits = ['Apple', 'Banana']
for ( var index=0; index<fruits.length; index++) {
    console.log(fruits[index]);
}
````
        
    **Quiz:**
        ````
        // create a function to count words in a sentence
        
        console.log(count("hello world")      // should output 2
        console.log(count("I am very happy")  // should output 4
        
        function count(sentence) {
          // implement your code
        }
        
        // Hint: please check string "split" function
        ````
        
        ````
        // create a function to reverse the sentence
        
        console.log(count("hello world")      // should output world hello
        console.log(count("I am very happy") // should output happy very am I
        
        function reverse(sentence) {
          // implement your code
        }
        
        // Hint: please check string "split" function
        ````        
    **Reference:**
        More Array build-in function. Plear check this link. [&#8594;](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)   
        
## Set 

Set object lets you store unique values of any type

````
// Initialization
let mySet = new Set()

// Add an item to the set
let mySet = new Set()
mySet.add(1)        
mySet.add(5)         
mySet.add(5)           

// Loop over an Array - Method 1
let fruits = ['Apple', 'Banana']
let fruitsArr = Array.from(fruits)  // Convert a Set to Array
for ( var index=0; index<fruitsArr.length; index++) {
    console.log(fruitsArr[index]);
}

// Loop over an Array - Method 2
let fruits = new Set()
fruits.add("orange")
fruits.add("apple")
fruits.forEach( v => {
    console.log(v)
})
````
        
    **Quiz:**
        ````
        // create a function to count unique words in a sentence
        
        console.log(count("hello world"))      // should output 2
        console.log(count("Hello Hello Hello"))  // should output 1
        
        function countUnique(sentence) {
          // implement your code
        }
        
        ````
        
        ````
        // create a function to print unique word
        
        printUniquecount("hello world")      // should output hello world
        printUniquecount("hello world hello moon") // should output hello world moon
        
        function printUnique(sentence) {
          // implement your code
        }
        ````        
    **Reference:**
        More Array build-in function. Plear check this link. [&#8594;](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set)   
        
## Map 

Holds key-value pairs and remembers the original insertion order of the keys

````
// Initialization
let prices = new Map()

// Add a key-value pair to map
let prices = new Map()
prices.set('beef', 8.2)
prices.set('pork', 5.8)
prices.set('beef', 9)
      
// Length of a map
console.log(prices.size)

// Loop over a Map - Method 1
prices.forEach(function(value, key) {
  console.log(key + ' = ' + value)
})

// Loop over an Map - Method 2
let myMap = new Map()
myMap.set(0, 'zero')
myMap.set(1, 'one')

for (let [key, value] of myMap) {
  console.log(key + ' = ' + value)
}
````
        
    **Quiz:**
        ````
        // create a function to collect the occurrance of each unique worlds
        
        // should output
        // hello = 1
        // world = 1
        printUniqueWordOccurrances("hello world")
        
        // should output
        // Hello = 3
        printUniqueWordOccurrances(count("Hello Hello Hello")
        
        function printUniqueWordOccurrances(sentence) {
          // implement your code
        }
        
        // Hint 
        ````
     
    **Reference:**
        More Array build-in function. Plear check this link. [&#8594;](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)  
