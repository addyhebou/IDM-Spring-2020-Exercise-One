let a = 1
let b = 2

setTimeout(function() { // setTimeout is an asynchronous 
    console.log("Async")
}, 1000)

console.log("Synchronous")

console.log(a)
console.log(b)