array = ["q", 2, "e", 3.6, :symbol, "y", [1, 2, "r"], "i", "p"]
puts array
puts array.class

puts "array.size -> #{array.size}"
puts "array.include? %q(r) -> #{array.include? %q(r)}"
puts "array.first -> #{array.first}"

puts "array[4] -> #{array[4]}"
puts "array[-1] -> #{array[-1]}"
puts "array[300] -> #{array[300]}"
