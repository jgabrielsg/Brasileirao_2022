from team import Team, Player
from game import soccer_match, semifinal, final
import random
import pandas as pd

internacional = Team("Internacional")
internacional.players.append(Player("Keiler", "Goleiro"))
internacional.players.append(Player("Mercado", "Defensor"))
internacional.players.append(Player("Vitão", "Defensor"))
internacional.players.append(Player("Renê", "Defensor"))
internacional.players.append(Player("Igor Gomes", "Defensor"))
internacional.players.append(Player("De Pena", "Meia"))
internacional.players.append(Player("Maurício", "Meia"))
internacional.players.append(Player("Alan Patrick", "Meia"))
internacional.players.append(Player("Wanderson", "Atacante"))
internacional.players.append(Player("Pedro Henrique", "Atacante"))
internacional.players.append(Player("Alemão", "Atacante"))


grêmio = Team("Grêmio")
grêmio.players.append(Player("Adriel", "Goleiro"))
grêmio.players.append(Player("Bruno Alves", "Defensor"))
grêmio.players.append(Player("Kannemann", "Defensor"))
grêmio.players.append(Player("Diogo Barbosa", "Defensor"))
grêmio.players.append(Player("João Pedro", "Defensor"))
grêmio.players.append(Player("Lucas Silva", "Meia"))
grêmio.players.append(Player("Bitello", "Meia"))
grêmio.players.append(Player("Cristaldo", "Meia"))
grêmio.players.append(Player("Vina", "Atacante"))
grêmio.players.append(Player("Ferreira", "Atacante"))
grêmio.players.append(Player("Suarez", "Atacante"))

corinthians = Team("Corinthians")
corinthians.players.append(Player("Cássio", "Goleiro"))
corinthians.players.append(Player("Fagner", "Defensor"))
corinthians.players.append(Player("Gil", "Defensor"))
corinthians.players.append(Player("Murillo", "Defensor"))
corinthians.players.append(Player("Mateus Bidu", "Defensor"))
corinthians.players.append(Player("Rony", "Meia"))
corinthians.players.append(Player("Fausto", "Meia"))
corinthians.players.append(Player("Maycon", "Meia"))
corinthians.players.append(Player("Roger Guedes", "Atacante"))
corinthians.players.append(Player("Yuri Alberto", "Atacante"))
corinthians.players.append(Player("Renato Augusto", "Atacante"))



são_paulo = Team("São Paulo")
são_paulo.players.append(Player("Rafael", "Goleiro"))
são_paulo.players.append(Player("Raí", "Defensor"))
são_paulo.players.append(Player("Diego Costa", "Defensor"))
são_paulo.players.append(Player("Beraldo", "Defensor"))
são_paulo.players.append(Player("Caio Paulista", "Defensor"))
são_paulo.players.append(Player("Luan", "Meia"))
são_paulo.players.append(Player("Pablo Maia", "Meia"))
são_paulo.players.append(Player("Nestor", "Meia"))
são_paulo.players.append(Player("Alisson", "Atacante"))
são_paulo.players.append(Player("Wellington Rato", "Atacante"))
são_paulo.players.append(Player("Luciano", "Atacante"))


flamengo = Team("Flamengo")
flamengo.players.append(Player("Santos", "Goleiro"))
flamengo.players.append(Player("Leo Pereira", "Defensor"))
flamengo.players.append(Player("Wesley", "Defensor"))
flamengo.players.append(Player("Fabrício Bruno", "Defensor"))
flamengo.players.append(Player("Vidal", "Defensor"))
flamengo.players.append(Player("Thiago Maia", "Meia"))
flamengo.players.append(Player("Evérton Ribeiro", "Meia"))
flamengo.players.append(Player("Arrascaeta", "Meia"))
flamengo.players.append(Player("Gabigol", "Atacante"))
flamengo.players.append(Player("Bruno Henrique", "Atacante"))
flamengo.players.append(Player("Pedro", "Atacante"))


palmeiras = Team("Palmeiras")
palmeiras.players.append(Player("Weverton", "Goleiro"))
palmeiras.players.append(Player("Marcos Rocha", "Defensor"))
palmeiras.players.append(Player("Gustavo Gomes", "Defensor"))
palmeiras.players.append(Player("Murulo", "Defensor"))
palmeiras.players.append(Player("Piquerez", "Defensor"))
palmeiras.players.append(Player("Zé Rafael", "Meia"))
palmeiras.players.append(Player("Gabriel Menino", "Meia"))
palmeiras.players.append(Player("Arthur", "Meia"))
palmeiras.players.append(Player("Dudu", "Atacante"))
palmeiras.players.append(Player("Endrick", "Atacante"))
palmeiras.players.append(Player("Flaco López", "Atacante"))



atlético_pr = Team("Atlético-PR")
atlético_pr.players.append(Player("Bento", "Goleiro"))
atlético_pr.players.append(Player("Khellven", "Defensor"))
atlético_pr.players.append(Player("Pedro Henrique", "Defensor"))
atlético_pr.players.append(Player("Zé Ivaldo", "Defensor"))
atlético_pr.players.append(Player("Pedrinho", "Defensor"))
atlético_pr.players.append(Player("Erick", "Meia"))
atlético_pr.players.append(Player("Fernandinho", "Meia"))
atlético_pr.players.append(Player("Vitor Bueno", "Meia"))
atlético_pr.players.append(Player("Vitor Roque", "Atacante"))
atlético_pr.players.append(Player("Terans", "Atacante"))
atlético_pr.players.append(Player("Cannobio", "Atacante"))


cruzeiro = Team("Cruzeiro")
cruzeiro.players.append(Player("Rafael Cabral", "Goleiro"))
cruzeiro.players.append(Player("William", "Defensor"))
cruzeiro.players.append(Player("Lucas Oliveira", "Defensor"))
cruzeiro.players.append(Player("Luciano Castan", "Defensor"))
cruzeiro.players.append(Player("Marlon", "Defensor"))
cruzeiro.players.append(Player("Machado", "Meia"))
cruzeiro.players.append(Player("Matheus Vital", "Meia"))
cruzeiro.players.append(Player("Fabrício", "Meia"))
cruzeiro.players.append(Player("Nikão", "Atacante"))
cruzeiro.players.append(Player("Gilberto", "Atacante"))
cruzeiro.players.append(Player("Bruno Rodrigues", "Atacante"))


bahia = Team("Bahia")
bahia.players.append(Player("Marcos Felipe", "Goleiro"))
bahia.players.append(Player("Kanu", "Defensor"))
bahia.players.append(Player("David Duarte", "Defensor"))
bahia.players.append(Player("Rezende", "Defensor"))
bahia.players.append(Player("Jacaré", "Defensor"))
bahia.players.append(Player("Acevedo", "Meia"))
bahia.players.append(Player("Thaciano", "Meia"))
bahia.players.append(Player("Cauly", "Meia"))
bahia.players.append(Player("Matheus Bahia", "Atacante"))
bahia.players.append(Player("Ademir", "Atacante"))
bahia.players.append(Player("Everaldo", "Atacante"))


vasco = Team("Vasco da Gama")
vasco.players.append(Player("Ivan", "Goleiro"))
vasco.players.append(Player("Pumita", "Defensor"))
vasco.players.append(Player("Miranda", "Defensor"))
vasco.players.append(Player("Léo", "Defensor"))
vasco.players.append(Player("Píton", "Defensor"))
vasco.players.append(Player("Rodrigo", "Meia"))
vasco.players.append(Player("Andrey", "Meia"))
vasco.players.append(Player("Jair", "Meia"))
vasco.players.append(Player("Pec", "Atacante"))
vasco.players.append(Player("Alex Teixeira", "Atacante"))
vasco.players.append(Player("Pedro Raul", "Atacante"))


# soccer_match(internacional, grêmio, 3, 1)
# soccer_match(são_paulo, internacional, 4, 3)

# print(internacional.points, internacional.goals_scored, internacional.goals_against)

teams = [internacional, grêmio, corinthians, são_paulo, flamengo, palmeiras, atlético_pr, cruzeiro, bahia, vasco]

for i in range(len(teams)):
    for j in range(i+1, len(teams)):
        goals1 = int(random.choices([0, 1, 2, 3, 4, 5, 6], 
                    weights=[0.2, 0.3, 0.2, 0.1, 0.1, 0.05, 0.05])[0])
        goals2 = int(random.choices([0, 1, 2, 3, 4, 5, 6], 
                    weights=[0.2, 0.35, 0.2, 0.1, 0.1, 0.04, 0.01])[0])
        soccer_match(teams[i], teams[j], goals1, goals2)
        print(f'{teams[i].name} {goals1} x {goals2} {teams[j].name}')
        
# Conversão dos objetos Team em dicionários
teams_dict = [vars(team) for team in teams]

brasileirao = pd.DataFrame(teams_dict, columns=['name', 'points', 'victory', 'draw', 'lost', 'goals_scored', 'goals_against'])
brasileirao = brasileirao.sort_values(by='points', ascending=False)
brasileirao = brasileirao.reset_index(drop=True)
brasileirao.index = brasileirao.index + 1

print(brasileirao)
print("\n")

top_4 = brasileirao.head(4)

print(top_4)

print("Agora teremos as semi-finais definindo o campeão!")

first = brasileirao.iloc[0]['name']
second = brasileirao.iloc[1]['name']
third = brasileirao.iloc[2]['name']
fourth = brasileirao.iloc[3]['name']

print(f'{first} x {fourth}')
print(f'{second} x {third}')

print('\n')

finalist1 = semifinal(first, fourth, 
          int(random.choices([0, 1, 2, 3, 4, 5, 6], 
                    weights=[0.2, 0.3, 0.2, 0.1, 0.1, 0.05, 0.05])[0]),
          int(random.choices([0, 1, 2, 3, 4, 5, 6], 
                    weights=[0.2, 0.3, 0.2, 0.1, 0.1, 0.05, 0.05])[0]))
print('\n')


finalist2 = semifinal(second, third, 
          int(random.choices([0, 1, 2, 3, 4, 5, 6], 
                    weights=[0.2, 0.3, 0.2, 0.1, 0.1, 0.05, 0.05])[0]),
          int(random.choices([0, 1, 2, 3, 4, 5, 6], 
                    weights=[0.2, 0.3, 0.2, 0.1, 0.1, 0.05, 0.05])[0]))

print("\nA FINAL SERÁ ENTRE: ")
print(f'{finalist1} x {finalist2}')

champion = final(finalist1, finalist2, 
          int(random.choices([0, 1, 2, 3, 4, 5, 6], 
                    weights=[0.2, 0.3, 0.2, 0.1, 0.1, 0.05, 0.05])[0]),
          int(random.choices([0, 1, 2, 3, 4, 5, 6], 
                    weights=[0.2, 0.3, 0.2, 0.1, 0.1, 0.05, 0.05])[0]))

player_data = []
for team in teams:
    for player in team.players:
        player_data.append({
            'name': player.name,
            'team': team.name,
            'goals': player.goals
        })

# criar um DataFrame com os dados dos jogadores
artilharia = pd.DataFrame(player_data)

# ordenar o DataFrame por ordem decrescente dos gols marcados
artilharia = artilharia.sort_values(by='goals', ascending=False)

# Filtra os jogadores que fizeram pelo menos um gol
artilharia = artilharia.query('goals > 1')

# Ordena os jogadores pelo número de gols marcados
artilharia = artilharia.sort_values('goals', ascending=False)
artilharia = artilharia.reset_index(drop=True)
artilharia.index = artilharia.index + 1
# imprimir a lista de artilheiros
print(artilharia[['name', 'team', 'goals']])