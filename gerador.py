import random

capitais = {
    'Acre': 'Rio Branco',
    'Alagoas': 'Maceió',
    'Amapá': 'Macapá',
    'Amazonas': 'Manaus',
    'Bahia': 'Salvador',
    'Ceará': 'Fortaleza',
    'Espírito Santo': 'Vitória',
    'Goiás': 'Goiânia',
    'Maranhão': 'São Luís',
    'Mato Grosso': 'Cuiabá',
    'Mato Grosso do Sul': 'Campo Grande',
    'Minas Gerais': 'Belo Horizonte',
    'Pará': 'Belém',
    'Paraíba': 'João Pessoa',
    'Paraná': 'Curitiba',
    'Pernambuco': 'Recife',
    'Piauí': 'Teresina',
    'Rio de Janeiro': 'Rio de Janeiro',
    'Rio Grande do Norte': 'Natal',
    'Rio Grande do Sul': 'Porto Alegre',
    'Rondônia': 'Porto Velho',
    'Roraima': 'Boa Vista',
    'Santa Catarina': 'Florianópolis',
    'São Paulo': 'São Paulo',
    'Sergipe': 'Aracaju',
    'Tocantins': 'Palmas',
    'Distrito Federal': 'Brasília'
}

for prova in range(30):
    arquivo_prova = open(f'prova-geografia-{prova + 1}.txt', 'w',encoding='utf8')
    arquivo_resposta = open(f'prova-geografia-respostas-{prova + 1}.txt', 'w',encoding='utf8')
    
    arquivo_prova.write('Nome:\n\nData:\n\nPeríodo:\n\n')
    arquivo_prova.write((' ' * 20) + f'Prova Capitais Brasileiras (Questionário {prova + 1})')
    arquivo_prova.write('\n\n')
    
    
    estados = list(capitais.keys())
    random.shuffle(estados)
    
    
    for questao in range(26):
        resposta_certa = capitais[estados[questao]]
        respostas_errada = list(capitais.values())
        del respostas_errada[respostas_errada.index(resposta_certa)]
        respostas_errada = random.sample(respostas_errada,3)
        respostas_disponiveis = respostas_errada + [resposta_certa]
        random.shuffle(respostas_disponiveis)
        
        arquivo_prova.write(f'{questao + 1}. Qual é a capital de {estados[questao]}?\n')
        for i in range(4):
            arquivo_prova.write(f"    {'ABCD'[i]}. {respostas_disponiveis[i]}\n")
        arquivo_prova.write("\n")
        
        arquivo_resposta.write(f"{questao + 1}. {'ABCD'[respostas_disponiveis.index(resposta_certa)]}\n")