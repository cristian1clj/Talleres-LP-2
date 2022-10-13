# declaracion de regex: /expresion/
# --->      edad_persona = /\d{2}/

is_gmail = /\w+@gmail.com/

puts "%q(cristian@gmail.com).match is_gmail -> #{"cristian@gmail.com".match is_gmail}"
puts "%q(cristian@gmail).match is_gmail -> #{"cristian@gmail".match is_gmail}"