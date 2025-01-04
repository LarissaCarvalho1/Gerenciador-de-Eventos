from datetime import datetime
from time import sleep

# Base de dados
eventos = []
eventos_cancelados = []

PERFIL_USER = """
1 - Aluno
2 - Coordenador
0 - Sair do Sistema
"""
MENU_ALUNO = """
1 - Visualizar Eventos Disponíveis
2 - Inscrever-se em Eventos
0 - Acessar Perfis
"""
MENU_COORDENADOR = """
1 - Cadastrar Evento 
2 - Atualizar Evento
3 - Visualizar Eventos
4 - Visualizar Inscrições
5 - Cancelar Evento
6 - Excluir Evento
0 - Acessar Perfis
"""
def titulo(titulo):
    print('--'*26)
    print(f'{(titulo):^50}')
    print('--'*26)

def subtitulo(subtitulo):
    print(f'{(subtitulo):^50}')

def confirma_acao(pergunta):
    while True:
        resposta = input(f'\n{pergunta} [S/N] ').strip().upper()

        if resposta in ['S', 'N']:
            return resposta == 'S'
        print('\nEscolha apenas [S] ou [N] para prosseguir.\n')
    
def aguarda_enter():
    while True:
        resposta = input('Pressione Enter para voltar ao Menu.').strip()

        if resposta == '':
            break
        else: 
            print('\nNão digite nada, apenas pressione Enter.\n')

def pausa():
    sleep(1)

# Ponto de entrada no sistema
def main():
    titulo('GERENCIADOR DE EVENTOS UNIFECAF')

    while True:
        subtitulo('Escolha um perfil para acessar o sistema')
        print(PERFIL_USER)
        perfil_user = input('Acessar como: ').strip()

        if perfil_user in ['1', '2']:
            pausa()
            exibir_menu(perfil_user)
            break
        elif perfil_user == '0':
            print('\nSaindo do sistema...\n')
            pausa()
            break
        else: 
            print('\nEscolha apenas uma das opções existentes. \nTente novamente.\n')
            pausa()
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
            operacao = input('Escolha uma opção para prosseguir: ').strip()

        match operacao:
            case '1':
                exibe_eventos_disponiveis()
            case '2':
                inscricao_evento()
            case '0':
                main()
                break
            case _:
                print('\nOperação Inválida! Tente novamente.\n')
                sleep(1)
        operacao = None

def menu_coordenador(operacao=None):
    while True:
        if operacao is None:
            titulo('MENU COORDENADOR')
            print(MENU_COORDENADOR)
            operacao = input('Escolha uma opção para prosseguir: ').strip()

        match operacao:
            case '1':
                cadastra_evento()
            case '2':
                atualiza_evento()
            case '3':
                exibe_eventos_disponiveis()
            case '4':
                visualiza_inscricoes()
            case '5':
                cancela_evento()
            case '6':
                exclui_evento()
            case '0':
                main()
                break
            case _: 
                print('\nOperação Inválida! Tente novamente.\n')
        operacao = None

def cadastra_evento():
    titulo('CADASTRAR EVENTO')
    while True:
        nome = input('Nome do Evento: ').strip().title()
        if nome == '':
            print('\nPreencha o nome corretamente!\n')
            pausa()
            continue

        for evento in eventos:
            if evento['nome_evento'] == nome:
                print('\nEvento já cadastrardo!\nUtilize a opção EDITAR EVENTO.\n')
                pausa()
                return

        while True:
            descricao = input('Descrição: ').strip().capitalize()
            if descricao == '':
                print('\nPreencha a descrição corretamente!\n')
                pausa()
                continue
            else:
                break

        while True:
            try:
                print('\nPreencha os campos abaixo para indicar a data:')
                dia = int(input('Dia: '))
                mes = int(input('Mês: '))
                ano = int(input('Ano: '))
                
                data = datetime(ano, mes, dia)

                quantidade_participantes = int(input('Quantidade de Participantes: '))
                if quantidade_participantes <= 0:
                    print('\nQuantidade de participantes deve ser maior que ZERO!\n')
                    pausa()
                    continue
            except (ValueError, TypeError):
                print('\nInforme apenas números válidos!')
                pausa()
                continue
            else:
                break

        novo_evento = {
            'nome_evento': nome,
            'descricao': descricao,
            'data': data.strftime('%d/%m/%Y'),
            'quantidade_maxima_participantes': quantidade_participantes,
            'inscritos': 0,
            'vagas_disponiveis': quantidade_participantes,
            'lista_inscritos': []
        }
        eventos.append(novo_evento)
        print(f'\nEvento cadastrado com sucesso!')
        pausa()
    
        if not confirma_acao('Cadastrar outro evento?'):
            pausa()
            break

def atualiza_evento():
    titulo('ATUALIZAR EVENTO')
    while True:
        if not eventos: 
            print('\nNão há eventos disponíveis para atualização!\nUtilize a opção CADASTRAR EVENTO.')
            pausa()
            return
        
        print(f'\n{("Eventos Disponíveis"):^50}\n')
        for indice, evento in enumerate(eventos):
            print(f'{indice + 1} - {evento["nome_evento"]}')   

        try:
            indice_evento = int(input('\nInforme o número do evento: ')) - 1

            if 0 <= indice_evento < len(eventos):
                evento_escolhido = eventos[indice_evento]
            else:
                print('\nNão há um evento com esse número. Tente novamente!\n')
                pausa()
                continue
        except (ValueError, TypeError):
            print('\nPor favor, informe apenas números!\n')
            pausa()
            continue
        
        while True:
            try:
                print('\nAtualizar data, preencha os campos abaixo:')
                novo_dia = int(input('Dia: '))
                novo_mes = int(input('Mês: '))
                novo_ano = int(input('Ano: '))

                nova_data = datetime(novo_ano, novo_mes, novo_dia)

                nova_quantidade_participantes = int(input('Quantidade de Participantes: '))
                if nova_quantidade_participantes <= 0:
                    print('Quantidade de participantes deve ser maior que ZERO!')
                    pausa()
                    continue
            except (ValueError, TypeError):
                print('\nInforme apenas números válidos!\n')
                pausa()
                continue
            else:
                evento_escolhido['data'] = nova_data.strftime('%d/%m/%Y')
                evento_escolhido['quantidade_maxima_participantes'] = nova_quantidade_participantes
                evento_escolhido['vagas_disponiveis'] = nova_quantidade_participantes - evento_escolhido['inscritos']
                print('\nEvento atualizado com sucesso!')
                pausa()
                break
            
        if not confirma_acao('Atualizar outro evento?'):
            pausa()
            break
                
def exibe_eventos_disponiveis():
    titulo('EVENTOS DISPONÍVEIS')
    if not eventos:
        print('\nNão há eventos disponíveis para visualização!\n')
        pausa()
        return

    for evento in eventos:
        print(f"EVENTO: {evento['nome_evento']} | INSCRITOS: {evento['inscritos']} | VAGAS: {evento['vagas_disponiveis']}")
        print(f"DATA: {evento['data']}")
        print(f"\nDESCRIÇÃO: {evento['descricao']}")
        print('--' * 26)
    aguarda_enter()
    pausa()
    
def inscricao_evento():
    titulo('INSCRIÇÃO EVENTO')
    
    while True:
        if not eventos:
            print('\nAinda não há eventos disponíveis para inscrição!\n')
            pausa()
            return

        subtitulo('Preencha os campos abaixo para efetuar a inscrição:')
        print(f'\n{("Eventos Disponíveis"):^50}\n')
        for indice, evento in enumerate(eventos):
            print(f"{indice + 1} - {evento['nome_evento']}")

        nome_evento_inscricao = input('\nInforme o nome do Evento: ').strip().title()
        evento_encontrado = None

        if nome_evento_inscricao == '':
            print('\nPreencha o nome do evento corretamente!\n')
            pausa()
            continue

        for evento in eventos:
            if evento['nome_evento'] == nome_evento_inscricao:
                evento_encontrado = evento
                break     

        if not evento_encontrado:
            print('\nO evento informado não foi encontrado.\nCertifique-se de informar o nome corretamente, por favor!\n')
            pausa()
            continue

        if evento_encontrado['vagas_disponiveis'] == 0:
            print('\nOps! Não há mais vagas disponíveis!\nMas não desanime, explore outros eventos!')
            pausa()
            break

        while True:
            nome_inscrito = input('Nome completo: ').strip().title()

            if nome_inscrito == '':
                print('\nPreencha o seu nome corretamente!\n')
                pausa()
                continue
            else:
                break

        while True:
            if confirma_acao('Confirmar inscrição? '):
                evento_encontrado['vagas_disponiveis'] -= 1
                evento_encontrado['inscritos'] += 1
                evento_encontrado['lista_inscritos'].append(nome_inscrito)
                print(f"\nInscrição no evento {evento_encontrado['nome_evento']} confirmada com sucesso!")
                break
            else:
                print('\nInscrição cancelada!')
                pausa()
                break

        if not confirma_acao('Inscrever-se em outro evento?'):
            pausa()
            break
                  
def visualiza_inscricoes():
    titulo('VIZUALIZAR LISTA DE INSCRITOS')

    while True:
        if not eventos:
            print('\nNão há eventos cadastrados e listas disponíveis para\nvisualização!\n')
            pausa()
            return

        subtitulo('Escolha um evento para visualizar a lista de inscritos')
        print(f'\n{("Eventos Disponíveis"):^50}\n')
        for indice, evento in enumerate(eventos):
            print(f"{indice + 1} - {evento['nome_evento']}")

        try:
            indice_evento = int(input('Digite o número do evento que deseja acessar: ')) - 1

            # Valida se o indice indicado pelo usuário está dentro do intervalo [0, len(eventos) - 1]
            if 0 <= indice_evento < len(eventos):
                evento_escolhido = eventos[indice_evento]
                
                if not evento_escolhido['lista_inscritos']:
                    print(f"\nAinda não há inscritos no evento {evento_escolhido['nome_evento']}!")
                    pausa()
                    break
                else:
                    print(f"\nLista de inscritos no evento: {evento_escolhido['nome_evento']}\n")
                    for inscrito in evento_escolhido['lista_inscritos']:
                        print(inscrito)
            else:
                print('Não há um evento com esse número. Tente novamente!')
                pausa()
                continue
        except (ValueError, TypeError):
            print('\nPor favor, informe apenas números!')
            pausa()
            continue
            
        if confirma_acao('Consultar a lista de outro evento?'):
            pausa()
            continue
        else:
            pausa()
            break

def cancela_evento():
    titulo('CANCELAR EVENTO')

    while True:
        if not eventos:
            print('\nNão há eventos disponíveis para cancelamento!\n')
            pausa()
            return

        print(f'\n{("Eventos Disponíveis"):^50}\n')
        for indice, evento in enumerate(eventos):
            print(f"{indice + 1} - {evento['nome_evento']}")

        try:
            indice_evento = int(input('Informe o número do evento para cancelamento: ')) - 1

            if 0 <= indice_evento < len(eventos):
                evento_escolhido = eventos[indice_evento]

                if confirma_acao('Deseja mesmo cancelar? '):
                    eventos_cancelados.append(evento_escolhido)
                    eventos.remove(evento_escolhido)
                    print('\nEvento cancelado com sucesso!')
            else:
                print('\nNão há um evento com esse número. Tente novamente!\n')
                pausa()
                continue
        except(ValueError, TypeError):
            print('\nPor favor, informe apenas números!')
            pausa()
            continue      

        if not confirma_acao('Cancelar outro evento? '):
            pausa()
            break

def exclui_evento():
    titulo('EXCLUIR EVENTO')

    while True:
        if not eventos_cancelados:
            print('\nNão há eventos cancelados aguardando exclusão!\n')
            pausa()
            return
        
        print(f'\n{("Eventos Disponíveis Para Exclusão"):^50}\n')
        for indice, evento_cancelado in enumerate(eventos_cancelados):
            print(f"{indice + 1} - {evento_cancelado['nome_evento']}")
    
        try:
            indice_evento_cancelado = int(input('Informe o número do evento para excluí-lo: ')) - 1

            if 0 <= indice_evento_cancelado < len(eventos_cancelados):
                evento_cancelado_escolhido = eventos_cancelados[indice_evento_cancelado]

                if confirma_acao('Deseja mesmo excluir? '):
                    eventos_cancelados.remove(evento_cancelado_escolhido)
                    print('\nEvento excluído com sucesso!')
                else:
                    print('\nEvento NÃO excluído.')
            else:
                print('\nNão há um evento com esse número. Tente novamente!\n')
                pausa()
                continue
        except(ValueError, TypeError):
            print('\nPor favor, informe apenas números!')
            pausa()
            continue
            
        if not confirma_acao('Excluir outro evento?'):
            pausa()
            break

main()