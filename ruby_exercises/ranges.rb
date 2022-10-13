x = (1..10)

puts "x -> #{x}"
puts "x.class -> #{x.class}"

puts "x.to_a -> #{x.to_a}"

x = (1...10)
puts "x -> #{x}"
puts "x.class -> #{x.class}"
puts "x.to_a -> #{x.to_a}"

a = ("a".."g")
puts "a.to_a -> #{a.to_a}"
