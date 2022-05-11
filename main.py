from faker import Faker

# Inicializa a lib
fake = Faker()

# Cria variáveis com dados fakes
nome = fake.name()
primeiro_nomefem = fake.first_name_female()
usuario = fake.user_name()
senha = fake.password()
mes = fake.month()

# Resultados
print(f'Nome: {nome}')
print(f'Nome: Feminino {primeiro_nome_fem}')
print(f'Usuario: {usuário}')
print(f'Senha: {senha}')
print(f'Mes: {mes}')

print(f'Projeto - OliveiraHackerSecurity')
print(f'Use os dados por sua conta e risco...')
