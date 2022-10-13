# Forma 1
class Person
    def initialize(name, age)
        @name = name
        @age = age
    end

    def name # Getter
        @name
    end

    def name=(name)  # Setter
        @name = name
    end
    
    def age # Getter
        @age
    end

    def age=(age) # Setter
        @age = age
    end
end

student = Person.new("Carlos", 23)

puts student.class
puts student.name
puts student.age


# Forma 2
class Car
    attr_accessor(:color)
    
    def initialize(color)
        @color = color
    end
end

my_car = Car.new("rojo")
puts my_car.class
puts my_car.color


# Forma 3
class Laptop < Struct.new(:brand)
end

my_laptop = Laptop.new("asus")
puts my_laptop.class
puts my_laptop.brand