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
        'status': True
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
        'status': True
    }]
eventos_cancelados = []
evento_ativo = True

PERFIL_USER = """
1 - Aluno
2 - Coordenador
0 - Sair do Sistema
"""
MENU_ALUNO = """
1 - Visualizar Eventos Disponíveis.
2 - Inscrever-se em Eventos.
0 - Acessar Perfis
"""
MENU_COORDENADOR = """
1 - Cadastrar Evento. 
2 - Atualizar Evento.
3 - Visualizar Inscrições.
4 - Cancelar Evento.
5 - Excluir Evento.
0 - Acessar Perfis
"""

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
                print('Operação Inválida')
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
                visualiza_inscricoes()
            case '4':
                cancela_evento()
            case '5':
                exclui_evento()
            case '0':
                main()
                break
            case _: 
                print('Operação Inválida')
        operacao = None

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
            'descricao': f'\n{descricao}\n',
            'data': f'{dia}/{mes}/{ano}',
            'quantidade_maxima_participantes': quantidade_participantes,
            'inscritos': 0,
            'vagas_disponiveis': quantidade_participantes,
            'lista_inscritos': [],
            'status': evento_ativo
        }
        eventos.append(novo_evento)
        print(f'\nEvento cadastrado com sucesso!')
        # print(eventos)
    
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

def exibe_eventos_disponiveis():
    titulo('EVENTOS DISPONÍVEIS')
    for evento in eventos:
        print(f'EVENTO: {evento['nome_evento']} | INSCRITOS: {evento['inscritos']} | VAGAS: {evento['vagas_disponiveis']}')
        print(f'DATA: {evento['data']}')
        print(f'\nDESCRIÇÃO: {evento['descricao']}\n')
        print('--' * 50)
    aguarda_enter()
    
def inscricao_evento():
    titulo('INSCRIÇÃO EVENTO')
    subtitulo('Preencha os campos abaixo para efetuar a inscrição.')
    print(f'\n{("Eventos Disponíveis"):^50}\n')

    for indice, evento in enumerate(eventos):
        print(f'{indice + 1}° - {evento['nome_evento']}')

    while True:
        nome_evento_inscricao = input('\nInforme o nome do Evento: ').strip().title()
        evento_encontrado = None

        if nome_evento_inscricao == '':
            exibir_erro('Preencha o nome do evento corretamente!')
            continue
        for evento in eventos:
            if evento['nome_evento'] == nome_evento_inscricao:
                evento_encontrado = evento
                break     
        if not evento_encontrado:
            exibir_erro('O evento informado não foi entrado.\nCertifique-se de informar o nome corretamente, por favor!')
            continue
        if evento_encontrado['vagas_disponiveis'] == 0:
            print('Ops! Não há mais vagas disponíveis! \nMas não desanime, explore outros eventos!')
            break
        while True:
            nome_inscrito = input('Nome completo: ').strip().title()

            if nome_inscrito == '':
                exibir_erro('Preencha o seu nome corretamente!')
                continue
            else:
                break
        while True:
            if confirma_acao('Confirmar inscrição? '):
                evento_encontrado['vagas_disponiveis'] -= 1
                evento_encontrado['inscritos'] += 1
                evento_encontrado['lista_inscritos'].append(nome_inscrito)
                print(f'\nInscrição no evendo {evento_encontrado['nome_evento']} confirmada com secesso!')
                break
            else:
                print('\nInscrição cancelada!')
                break
        if not confirma_acao('Deseja se inscrever em outro eventos? '):
            break
                  
def visualiza_inscricoes():
    titulo('VIZUALIZAR LISTA DE INSCRITOS')
    print('Escolha um evento para visualizar a lista de inscritos')
    print('Eventos Disponíveis: ')

    for indice, evento in enumerate(eventos):
        print(f'{indice + 1} - {evento['nome_evento']}')

    while True:
        try:
            indice_evento = int(input('Digite o número do evento que deseja acessar: ')) - 1
        except (ValueError, TypeError):
            exibir_erro('Por favor, informe apenas números!')
            continue
        else:
            # Valida se o indice indicado pelo usuário está dentro do intervalo [0, len(eventos) - 1]
            if 0 <= (indice_evento) < len(eventos):
                evento_escolhido = eventos[indice_evento]
                
                if not evento_escolhido['lista_inscritos']:
                    print(f'Ainda não há inscritos no evento {evento_escolhido['nome_evento']}!')
                    break
                else:
                    print(f'\nLista de inscritos no evento: {evento['nome_evento']}\n')
                    for inscrito in evento_escolhido['lista_inscritos']:
                        print(inscrito)
            else:
                exibir_erro('Não há um evento com esse número. Tente novamente!')
                continue

        if confirma_acao('Consultar a lista de outro evento?'):
            continue
        else:
            break

def cancela_evento():
    titulo('CANCELAR EVENTO')
    while True:
        for indice, evento in enumerate(eventos):
            print(f'{indice + 1} - {evento['nome_evento']}')

        try:
            indice_evento = int(input('Informe o número do evento para cancelamento: ')) - 1
        except(ValueError, TypeError):
            exibir_erro('Por favor, informe apenas números!')
            continue
        else:
            if 0 <= indice_evento < len(eventos):
                evento_escolhido = eventos[indice_evento]

                if confirma_acao('Deseja mesmo cancelar? '):
                    evento_ativo = False
                    evento_escolhido['status'] = evento_ativo
                    eventos_cancelados.append(evento_escolhido)
                    eventos.remove(evento_escolhido)
                    print('Evento cancelado com sucesso!')
            else:
                exibir_erro('Não há um evento com esse número. Tente novamente!')
                continue
        if not confirma_acao('Cancelar outro evento? '):
            break

def exclui_evento():
    titulo('EXCLUIR EVENTO')

    if not eventos_cancelados:
        print('Não há eventos cancelados aguardando exclusão!')
        print('Caso deseje excluir um evento, utilize a opção CANCELAR EVENTO\n e depois acesse EXCLUIR EVENTO.')
        return
    
    for indice, evento_cancelado in enumerate(eventos_cancelados):
        print(f'{indice + 1} - {evento_cancelado['nome_evento']}')
    
    while True:
        try:
            indice_evento_cancelado = int('Informe o número do evento para excluí-lo: ') - 1
        except(ValueError, TypeError):
            exibir_erro('Por favor, informe apenas números!')
        else:
            if 0 <= indice_evento_cancelado < len(eventos_cancelados):
                evento_cancelado_escolhido = eventos_cancelados[indice_evento_cancelado]

                if confirma_acao('Deseja mesmo excluir? '):
                    eventos_cancelados.remove(evento_cancelado_escolhido)
                    print('Evento excluído com sucesso!')
                    print(eventos_cancelados)
                else:
                    print('Evento NÃO excluído.')
            else:
                exibir_erro('Não há um evento com esse número. Tente novamente!')
                continue
        if not confirma_acao('Deseja excluir outro evento?'):
            break

def titulo(titulo):
    print('--'*26)
    print(f'{(titulo):^50}')
    print('--'*26)

def subtitulo(subtitulo):
    print(f'{(subtitulo):^50}')

def exibir_erro(mensagem):
    print(f'\n{mensagem}\n')
    
def confirma_acao(pergunta):
    while True:
        resposta = input(f'\n{pergunta} [S/N] ').strip().upper()
        if resposta in ['S', 'N']:
            return resposta == 'S'
        exibir_erro('Escolha apenas [S] ou [N] para prosseguir.')
    
def aguarda_enter():
    while True:
        resposta = input('Pressione Enter para voltar ao Menu.').strip()
        if resposta == '':
            break
        else: 
            exibir_erro('Não digite nada, apenas pressione Enter.')

# Execução do programa
main()