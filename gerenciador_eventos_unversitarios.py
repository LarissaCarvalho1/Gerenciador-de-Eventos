MENU_ALUNO = """"
-=- MENU ALUNO -=-
1 - Visualizar Eventos Disponíveis.
2 - Inscrever-se em Eventos.
"""
MENU_COORDENADOR = """"
-=- MENU COORDENADOR -=-
1 - Cadastrar Evento. 
2 - Atualizar Evento.
3 - Visualizar Inscrições.
4 - Excluir Evento.
"""

def menu_aluno(operacao):
    match operacao:
        case '1':
            print('Visualizar eventos disponíveis.')
        case '2':
            print('Inscrever-se em Eventos.')
        case _:
            print('Operação Inválida')

def menu_coordenador(operacao):
    match operacao:
        case '1':
            print('Cadastrar Evento.')
        case '2':
            print('Atualizar Evento.')
        case '3':
            print('Visualiar Evento.')
        case '4':
            print('Excluir Evento.')
        case _: 
            print('Operação Inválida')

# Exibe o menu baseado no tipo de usuário
def exibir_menu(usuario):
    if usuario == '1':
        print(MENU_ALUNO)
        operacao = input('Escolha uma das opções acima para prosseguir:').strip()
        menu_aluno(operacao)
    elif usuario == '2':
        print(MENU_COORDENADOR)
        operacao = input('Escolha uma das opções acima para prosseguir:').strip()
        menu_coordenador(operacao)

# Ponto de entrada no sistema
def main():
    print('Gerenciador de Eventos UniFECAF')
    print('-=-'*11)
    print('Escolha um perfil para acessar o sistema')
    print('-'*33)
    perfil_user = input('1 - Aluno \n2 - Coordenador \nAcessar como: ').strip()

    if perfil_user in ['1', '2']:
        exibir_menu(perfil_user)
    else: 
        print('[ERRO] \nEscolha apenas uma das opções existentes. \nTente novamente.')

# Execução do programa
if __name__ == "__main__":
    main()


