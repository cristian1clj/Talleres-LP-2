x = 0

# While
puts "While"
while x < 5
    puts x
    x += 1
end

# Loop
puts "Loop"
loop do         # -> similar a "while True: "
    puts x
    
    break if x == 0
    x -= 1
end

# For
puts "For"
for i in 1..5 do        # -> for valor in lista
    puts "i -> #{i}"
end

for _ in 1..5 do
    puts "x -> #{x}"
    x += 1
end