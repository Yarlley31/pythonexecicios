CBF = ('palmeiras', 'botafogo', 'gremio', 'bragantino',         
        'atletico-MG', 'flamengo', 'athletico-PR', 'fluminense',
        'cuiaba', 'sao paulo', 'corinthias', 'fortaleza',
        'internacional','santos', 'vasco', 'bahia', 'cruzeiro',
        'goias', 'coritiba', 'america-MG')
print('-=-' * 20)
print('TABELA DO BRASILEIRÃO!')
print('-=' * 33)
print(f'Os 5 primeiros colocados são {CBF[:5]}')
print('-=' * 33)
print(f'Os últimos 4 da tabela são {CBF[16:]}')
print('-=' * 33)
print(f'Os times em ordem alfabetica fica: {sorted(CBF)}')
print('-=' * 33)
print(f'O Chapecoense não esta entre os primeiros 20 colocados na série A do Brasileirão!')