# Base de dados
eventos = [{'nome_evento': 'Evento', 
    'descricao': 'Teste testado testando testamento', 
    'data': '20/12/2024',
    'quantidade_maxima_participantes': 100, 
    'inscritos': 30,
    'vagas_diponiveis': 70,
    'lista_inscritos': ['Amanda Ribeiro Silva', 'Lucas Almeida Costa', 'Mariana Oliveira Souza', 'Gabriel Santos Lima', 'Sofia Pereira Carvalho', 'Rafael Gonçalves Machado', 'Isabela Araújo Fernandes', 'Matheus Martins Rocha', 'Giovanna Mendes Santos', 'João Victor Oliveira Nascimento','Larissa Ferreira Andrade', 'Thiago Costa Ribeiro', 'Ana Clara Figueiredo Lopes', 'Pedro Henrique Alves Fonseca', 'Camila Rocha Menezes', 'Felipe Almeida Cardoso', 'Júlia Martins Albuquerque', 'Guilherme Barbosa Teixeira', 'Beatriz Vieira Monteiro', 'Leonardo Silva Oliveira', 'Carolina Ferreira Matos', 'Vinícius Andrade Cunha', 'Helena Lima Bastos', 'Eduardo Souza Martins', 'Yasmin Castro Moreira', 'Rodrigo Carvalho Santana', 'Bianca Oliveira Campos', 'Diego Monteiro Freitas', 'Manuela Mendes Pires', 'Bruno Rocha Cavalcante']
    }]

MENU_ALUNO = """
1 - Visualizar Eventos Disponíveis.
2 - Inscrever-se em Eventos.
0 - Sair do Sistema
"""
MENU_COORDENADOR = """
1 - Cadastrar Evento. 
2 - Atualizar Evento.
3 - Visualizar Inscrições.
4 - Excluir Evento.
0 - Sair do Sistema
"""

# Ponto de entrada no sistema
def main():
    titulo('GERENCIADOR DE EVENTOS UNIFECAF')
    titulo('Escolha um Perfil Para Acessar o Sistema')
    while True:
        perfil_user = input('1 - Aluno \n2 - Coordenador \nAcessar como: ').strip()

        if perfil_user in ['1', '2']:
            exibir_menu(perfil_user)
            break
        else: 
            print('\n[ERRO] Escolha apenas uma das opções existentes. \nTente novamente.\n')
            continue

# Exibe o menu baseado no tipo de usuário
def exibir_menu(usuario):
    if usuario == '1':
        menu_aluno()
    elif usuario == '2':
        menu_coordenador()

def menu_aluno(operacao=None):
    while True:
        if operacao is None:
            titulo('MENU ALUNO')
            print(MENU_ALUNO)
            operacao = input('Escolha uma das opções acima para prosseguir: ').strip()

        match operacao:
            case '1':
                print('Visualizar eventos disponíveis.')
            case '2':
                print('Inscrever-se em Eventos.')
            case '0':
                print('Saindo do sistema...')
                break
            case _:
                print('Operação Inválida')
        operacao = None

def menu_coordenador(operacao=None):
    while True:
        if operacao is None:
            titulo('MENU COORDENADOR')
            print(MENU_COORDENADOR)
            operacao = input('Escolha uma das opções acima para prosseguir: ').strip()

        match operacao:
            case '1':
                cadastra_evento()
            case '2':
                atualiza_evento()
            case '3':
                print('Visualizar Evento.')
            case '4':
                print('Excluir Evento.')
            case '0':
                print('Saindo do sistema...')
                break
            case _: 
                print('Operação Inválida')
        operacao = None

# FIM MENU

def cadastra_evento():
    titulo('CADASTRAR EVENTO')
    while True:
        nome = input('Nome do Evento: ').strip().title()
        if nome == '':
            exibir_erro('Preencha o nome corretamente!')
            continue
        for evento in eventos:
            if evento['nome_evento'] == nome:
                print('\nEvento já cadastrardo. Utilize a opção EDITAR EVENTO.\n')
                return
        while True:
            descricao = input('Descrição: ').strip().capitalize()
            if descricao == '':
                exibir_erro('Preencha a descrição corretamente!')
                continue
            else:
                break
        while True:
            try:
                print('\nPreencha os campos abaixo para indicar a data:')
                dia = int(input('Dia: '))
                mes = int(input('Mês: '))
                ano = int(input('Ano: '))
                quantidade_participantes = int(input('Quantidade de Participantes: '))
            except (ValueError, TypeError):
                exibir_erro('Informe apenas números!')
                continue
            else:
                break
        novo_evento = {
            'nome_evento': nome,
            'descricao': descricao,
            'data': f'{dia}/{mes}/{ano}',
            'quantidade_maxima_participantes': quantidade_participantes,
            'inscritos': None,
            'vagas_diponiveis': None,
            'lista_inscritos': []
        }
        eventos.append(novo_evento)
        print(f'\nEvento cadastrado com sucesso!')
    
        if not confirma_acao('Cadastrar outro evento?'):
            break
        
def atualiza_evento():
    titulo('ATUALIZAR EVENTO')
    while True:
        nome = input('Nome do evento a ser atualizado: ').strip().title()
        evento_encontrado = None
        if nome == '':
            exibir_erro('Preencha o nome corretamente!')
            continue
        for evento in eventos:
            if evento['nome_evento'] == nome:
                evento_encontrado = evento
                break
        if not evento_encontrado:
            print('\nEvento não cadastrado. Utilize a opção CADASTRAR EVENTO.\n')
            break
        while True:
            try:
                print('Preencha os campos abaixo para atualizar a data:')
                novo_dia = int(input('Dia: '))
                novo_mes = int(input('Mês: '))
                novo_ano = int(input('Ano: '))
                nova_quantidade_participantes = int(input('Quantidade de Participantes: '))
                inscritos = int(input('Quantidade de inscritos: '))

                if novo_dia <= 0 or novo_mes <= 0 or novo_ano <= 0:
                    exibir_erro('Dia, mês e ano devem ser maior que ZERO!')
                    continue
                elif nova_quantidade_participantes <= 0:
                    exibir_erro('Quantidade de participantes deve ser maior que ZERO!')
                    continue
            except (ValueError, TypeError):
                exibir_erro('Informe apenas números!')
                continue
            else:
                evento_encontrado['data'] = f'{novo_dia}/{novo_mes}/{novo_ano}'
                evento_encontrado['quantidade_maxima_participantes'] = nova_quantidade_participantes
                print('\nEvento atualizado com sucesso!\n')
                break
        if not confirma_acao('Atualizar outro evento?'):
            break

    
def titulo(titulo):
    print('--'*26)
    print(f'|{(titulo):^50}|')
    print('--'*26)

def exibir_erro(mensagem):
    print(f'\n{mensagem}\n')
    
def confirma_acao(pergunta):
    while True:
        resposta = input(f'{pergunta} [S/N] ').strip().upper()
        if resposta in ['S', 'N']:
            return resposta == 'S'
        exibir_erro('Escolha apenas [S] ou [N] para prosseguir.')

# Execução do programa
main()


