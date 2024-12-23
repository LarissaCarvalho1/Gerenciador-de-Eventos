from datetime import datetime
from time import sleep

# Base de dados
eventos = [
    {
        'nome_evento': 'Workshop Agile Methods', 
        'descricao': 'Participe do Workshop Hands-On: Métodos Ágeis e mergulhe na prática das principais ferramentas\ne frameworks ágeis, como Scrum e Kanban!Por meio de atividades interativas e exercícios práticos,\nvocê terá a oportunidade de vivenciar a aplicação dos métodos ágeis em situações reais,\naprimorando sua capacidade de adaptação e entrega de valor contínuo.', 
        'data': '18/01/2025',
        'quantidade_maxima_participantes': 50, 
        'inscritos': 10,
        'vagas_disponiveis': 40,
        'lista_inscritos': ['Amanda Ribeiro Silva', 'Lucas Almeida Costa', 'Mariana Oliveira Souza', 'Gabriel Santos Lima', 'Sofia Pereira Carvalho', 'Rafael Gonçalves Machado', 'Isabela Araújo Fernandes', 'Matheus Martins Rocha', 'Giovanna Mendes Santos', 'João Victor Oliveira Nascimento'], 
    }, 
    {
        'nome_evento': 'Palestra Diversidade E Inclusão',
        'descricao': 'Descubra como a diversidade e a inclusão transformam realidades e fortalecem equipes. \nAbordaremos a importância da equidade, respeito às diferenças e combate ao preconceito, \npromovendo reflexões e ações para construir um futuro mais justo e acolhedor.\nParticipe e inspire-se para fazer a diferença!',
        'data': '25/01/2025',
        'quantidade_maxima_participantes': 150,
        'inscritos': 20,
        'vagas_disponiveis': 130,
        'lista_inscritos': ['Larissa Ferreira Andrade', 'Thiago Costa Ribeiro', 'Ana Clara Figueiredo Lopes', 'Pedro Henrique Alves Fonseca', 'Camila Rocha Menezes', 'Felipe Almeida Cardoso', 'Júlia Martins Albuquerque','Guilherme Barbosa Teixeira', 'Beatriz Vieira Monteiro', 
        'Leonardo Silva Oliveira', 'Carolina Ferreira Matos', 'Vinícius Andrade Cunha', 'Helena Lima Bastos', 'Eduardo Souza Martins', 'Yasmin Castro Moreira', 'Rodrigo Carvalho Santana', 'Bianca Oliveira Campos', 'Diego Monteiro Freitas', 'Manuela Mendes Pires', 'Bruno Rocha Cavalcante'],
    }]
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

# Ponto de entrada no sistema
def main():
    titulo('GERENCIADOR DE EVENTOS UNIFECAF')
    subtitulo('Escolha um perfil para acessar o sistema')

    while True:
        print(PERFIL_USER)
        perfil_user = input('Acessar como: ').strip()

        if perfil_user in ['1', '2']:
            exibir_menu(perfil_user)
            break
        elif perfil_user == '0':
            print('Saindo do sistema...')
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
            continue

        for evento in eventos:
            if evento['nome_evento'] == nome:
                print('\nEvento já cadastrardo!\nUtilize a opção EDITAR EVENTO.\n')
                return

        while True:
            descricao = input('Descrição: ').strip().capitalize()
            if descricao == '':
                print('\nPreencha a descrição corretamente!\n')
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
                    continue
            except (ValueError, TypeError):
                print('\nInforme apenas números válidos!')
                continue
            else:
                break

        novo_evento = {
            'nome_evento': nome,
            'descricao': f'\n{descricao}\n',
            'data': data.strftime('%d/%m/%Y'),
            'quantidade_maxima_participantes': quantidade_participantes,
            'inscritos': 0,
            'vagas_disponiveis': quantidade_participantes,
            'lista_inscritos': []
        }
        eventos.append(novo_evento)
        print(f'\nEvento cadastrado com sucesso!')
    
        if not confirma_acao('Cadastrar outro evento?'):
            break

def atualiza_evento():
    while True:
        if not eventos: 
            print('\nNão há eventos disponíveis para atualização!\nUtilize a opção CADASTRAR EVENTO.')
            return
        
        for indice, evento in enumerate(eventos):
            print(f'{indice + 1} - {evento["nome_evento"]}')   

        try:
            indice_evento = int(input('Informe o número do evento: ')) - 1

            if 0 <= indice_evento < len(eventos):
                evento_escolhido = eventos[indice_evento]
                # break
            else:
                print('\nNão há um evento com esse número. Tente novamente!\n')
                continue
        except (ValueError, TypeError):
            print('\nPor favor, informe apenas números!\n')
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
                    continue
            except (ValueError, TypeError):
                print('\nInforme apenas números válidos!\n')
                continue
            else:
                evento_escolhido['data'] = nova_data.strftime('%d/%m/%Y')
                evento_escolhido['quantidade_maxima_participantes'] = nova_quantidade_participantes
                print('\nEvento atualizado com sucesso!')
                break
            
        if not confirma_acao('Atualizar outro evento?'):
            break
                
def exibe_eventos_disponiveis():
    titulo('EVENTOS DISPONÍVEIS')
    if not eventos:
        print('\nNão há eventos disponíveis para visualização!\n')
        return

    for evento in eventos:
        print(f"EVENTO: {evento['nome_evento']} | INSCRITOS: {evento['inscritos']} | VAGAS: {evento['vagas_disponiveis']}")
        print(f"DATA: {evento['data']}")
        print(f"\nDESCRIÇÃO: {evento['descricao']}")
        print('--' * 26)
    aguarda_enter()
    
def inscricao_evento():
    titulo('INSCRIÇÃO EVENTO')
    
    while True:
        if not eventos:
            print('\nAinda não há eventos disponíveis para inscrição!\n')
            return

        subtitulo('Preencha os campos abaixo para efetuar a inscrição:')
        print(f'\n{("Eventos Disponíveis"):^50}\n')
        for indice, evento in enumerate(eventos):
            print(f"{indice + 1} - {evento['nome_evento']}")

        nome_evento_inscricao = input('\nInforme o nome do Evento: ').strip().title()
        evento_encontrado = None

        if nome_evento_inscricao == '':
            print('\nPreencha o nome do evento corretamente!\n')
            continue

        for evento in eventos:
            if evento['nome_evento'] == nome_evento_inscricao:
                evento_encontrado = evento
                break     

        if not evento_encontrado:
            print('\nO evento informado não foi encontrado.\nCertifique-se de informar o nome corretamente, por favor!\n')
            continue

        if evento_encontrado['vagas_disponiveis'] == 0:
            print('\nOps! Não há mais vagas disponíveis!\nMas não desanime, explore outros eventos!')
            break

        while True:
            nome_inscrito = input('Nome completo: ').strip().title()

            if nome_inscrito == '':
                print('\nPreencha o seu nome corretamente!\n')
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
                break

        if not confirma_acao('Deseja inscrever-se em outro evento? '):
            break
                  
def visualiza_inscricoes():
    titulo('VIZUALIZAR LISTA DE INSCRITOS')

    while True:
        if not eventos:
            print('\nNão há eventos cadastrados e listas disponíveis para\nvisualização!\n')
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
                    print(f"Ainda não há inscritos no evento {evento_escolhido['nome_evento']}!")
                    break
                else:
                    print(f"\nLista de inscritos no evento: {evento_escolhido['nome_evento']}\n")
                    for inscrito in evento_escolhido['lista_inscritos']:
                        print(inscrito)
            else:
                print('Não há um evento com esse número. Tente novamente!')
                continue
        except (ValueError, TypeError):
            print('\nPor favor, informe apenas números!')
            continue
            
        if confirma_acao('Consultar a lista de outro evento?'):
            continue
        else:
            break

def cancela_evento():
    titulo('CANCELAR EVENTO')

    while True:
        if not eventos:
            print('\nNão há eventos disponíveis para cancelamento!\n')
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
                continue
        except(ValueError, TypeError):
            print('\nPor favor, informe apenas números!')
            continue      

        if not confirma_acao('Cancelar outro evento? '):
            break

def exclui_evento():
    titulo('EXCLUIR EVENTO')

    while True:
        if not eventos_cancelados:
            print('\nNão há eventos cancelados aguardando exclusão!\n')
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
                continue
        except(ValueError, TypeError):
            print('\nPor favor, informe apenas números!')
            continue
            
        if not confirma_acao('Deseja excluir outro evento?'):
            break

main()