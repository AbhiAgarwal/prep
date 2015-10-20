- Singleton pattern: is a design pattern that restricts the instantiation of a class to one object. This is useful when exactly one object is needed to coordinate actions across the system.

Lazy initialization

```java
public class SingletonDemo {
    private static volatile SingletonDemo instance;
    private SingletonDemo() { }

    public static SingletonDemo getInstance() {
        if (instance == null ) {
            synchronized (SingletonDemo.class) {
                if (instance == null) {
                    instance = new SingletonDemo();
                }
            }
        }

        return instance;
    }
}
```

[Golang](http://stackoverflow.com/questions/1823286/singleton-in-go)

```go
package singleton

type single struct {
        O interface{};
}

var instantiated *single = nil

func New() *single {
        if instantiated == nil {
                instantiated = new(single);
        }
        return instantiated;
}
```

- Factory pattern: create object without exposing the creation logic to the client and refer to newly created object using a common interface.
    - In object-oriented programming (OOP), a factory is an object for creating other objects – formally a factory is simply an object that returns an object from some method call, which is assumed to be "new".

Shape.java

```java
public interface Shape {
   void draw();
}
```

Rectangle.java

```java
public class Rectangle implements Shape {

   @Override
   public void draw() {
      System.out.println("Inside Rectangle::draw() method.");
   }
}
```

Square.java

```java
public class Square implements Shape {

   @Override
   public void draw() {
      System.out.println("Inside Square::draw() method.");
   }
}
```

Circle.java

```java
public class Circle implements Shape {

   @Override
   public void draw() {
      System.out.println("Inside Circle::draw() method.");
   }
}
```

ShapeFactory.java

```java
public class ShapeFactory {
    
   //use getShape method to get object of type shape 
   public Shape getShape(String shapeType){
      if(shapeType == null){
         return null;
      }     
      if(shapeType.equalsIgnoreCase("CIRCLE")){
         return new Circle();
         
      } else if(shapeType.equalsIgnoreCase("RECTANGLE")){
         return new Rectangle();
         
      } else if(shapeType.equalsIgnoreCase("SQUARE")){
         return new Square();
      }
      
      return null;
   }
}
```

FactoryPatternDemo.java

```java
public class FactoryPatternDemo {

   public static void main(String[] args) {
      ShapeFactory shapeFactory = new ShapeFactory();

      //get an object of Circle and call its draw method.
      Shape shape1 = shapeFactory.getShape("CIRCLE");

      //call draw method of Circle
      shape1.draw();

      //get an object of Rectangle and call its draw method.
      Shape shape2 = shapeFactory.getShape("RECTANGLE");

      //call draw method of Rectangle
      shape2.draw();

      //get an object of Square and call its draw method.
      Shape shape3 = shapeFactory.getShape("SQUARE");

      //call draw method of circle
      shape3.draw();
   }
}
```