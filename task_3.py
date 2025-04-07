world_champions = {
    2002: 'Бразилия',
    2006: 'Италия',
    2010: 'Испания',
    2014: 'Германия',
    2018: 'Франция',
}

world_champions[2022] = 'Аргентина'

for world_champion in world_champions.items():
    print(f'{world_champion[0]} - {world_champion[1]}')

country = 'Италия'

if world_champions.get(country) == None:
    print('Италия не выигрывала чемпионат мира по футболу в 21 веке.')
else:
    print('Италия cтановилась чемпионом мира по футболу в 21 веке!')
    





 