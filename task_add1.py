
types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}

def ticket_unic(dict_tick):
    for prt in dict_tick.keys():
        for tick in dict_tick.get(prt):
            for j in range(prt+1, 6):
                if tick in dict_tick.get(j):
                    dict_tick[j].remove(tick)

def dict_prt_tick(dict_prt, dict_tick):
    dict_fin = {}
    for prt in dict_prt.keys():
        dict_fin[dict_prt.get(prt)] = dict_tick.get(prt)
    return dict_fin

            

ticket_unic(tickets)    
print(dict_prt_tick(types, tickets))
