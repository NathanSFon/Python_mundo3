#Times na ordem do compeonato em 10/10/2022 

tabela = ('Palmeiras','Internacional','Corinthians','Flamengo','Fluminense','Athletico-PR','Atlético-MG','América-MG','Botafogo','Fortaleza','São Paulo','Bragantino','Goiás','Santos','Coritiba','Ceará','Cuiabá','Atlético-GO','Avaí','Juventude')

# A
print(tabela[:5])

# B
print(tabela[16:])

# C 
print(sorted(tabela))

# D
pos = tabela.index('Flamengo')+1
print(f'O Flamengo esta na {pos} posicao')