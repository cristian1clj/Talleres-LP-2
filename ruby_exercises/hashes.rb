numeros = {}
puts "numeros -> #{numeros}"
puts "numeros.class -> #{numeros.class}"

numeros = {"uno" => 1}
puts "numeros -> #{numeros}"

numeros["dos"] = 2
numeros["tres"] = 3
numeros["cuatro"] = 4
numeros["cinco"] = 5
numeros["seis"] = 6
numeros["siete"] = 7
numeros["ocho"] = 8
numeros["nueve"] = 9
puts "numeros -> #{numeros}"

puts "numeros[%q(seis)] -> #{numeros[%q(seis)]}"
puts "numeros[%q(tres)] -> #{numeros[%q(tres)]}"

puts "numeros.size -> #{numeros.size}"
puts "numeros.empty? -> #{numeros.empty?}"
puts "numeros.has_key? %q(ocho) -> #{numeros.has_key? "ocho"}"
puts "numeros.has_value? 7 -> #{numeros.has_value? 7}"

numeros_2 = {"diez" => 10, "once" => 11}
puts numeros.merge numeros_2
puts numeros.merge({"cero" => 0, "uno negativo" => -1})