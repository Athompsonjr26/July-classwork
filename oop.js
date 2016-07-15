function Person(name) {
  this.name = name;
}

Person.prototype.sayHello = function() {
  console.log('Hello, I am ' + this.name + '!');
};

var aditi = new Person('Aditi');
aditi.sayHello();
