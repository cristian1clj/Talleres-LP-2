# String
name = "Brad Pitt"          # -> tambien se puede definir como a = %q(Brad Pitt)
puts "name -> #{name}"
puts "Hello #{name}"            # -> no funciona con '', solo con "" y %q()

puts "name.upcase -> #{name.upcase}"
puts "name.downcase -> #{name.downcase}"

puts "+ -> Hello " + "World"
puts "* -> #{name * 3}"
puts "name[3] -> #{name[3]}"

name_2 = name.gsub("Pitt", "Perez")
puts "name -> #{name} ; name_2 -> #{name_2}"
name.gsub!("Pitt", "Ronaldo")
puts "name -> #{name}"
