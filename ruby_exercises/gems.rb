# 1) Instalar bundler
# ------> gem install bundler

# 2) Verificar version
# ------> bundle --version

# 3) Inicializar el proyecto
# ------> bundle init

# 4) Se agregan los gems que se vayan a usar al Gemfile
# ------> gem 'nombre_gem', '~> version_gem'

# 5) Ejecutar el Gemfile para instalar las dependencias
# ------> bundle install

# 6) (opcional) Ver todas las gemas en el dispositivo
# ------> gem list

require "faker"

puts Faker::Name.name
puts Faker::Internet.email