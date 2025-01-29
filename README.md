# 🖥🎓 Gerenciador de eventos universitários UniFECAF 
![Gerenciamento](imagem2.jpg)

O sistema de gerenciamento de eventos da universidade FECAF é uma solução desenvolvida, durante a disciplina de Computational Logic Using Python, para facilitar a administração e participação em eventos promovidos pela instituição.  

O projeto opera por meio de menus interativos em um sistema de linha de comando, que permitem aos usuários navegar e executar suas operações conforme o perfil selecionado. Ao iniciar o sistema, o usuário escolhe o perfil desejado (Aluno ou Coordenador), cada um com acesso a funcionalidades específicas. O sistema usa um banco de dados em memória para armazenar informações sobre eventos, inscrições e eventos cancelados.

## ⚙ Requisitos do sistema 
- Cadastrar Evento: o sistema deve habilitar o organizador a criar novos 
eventos, especificando o nome do evento, a data, a descrição e o número 
máximo de participantes.

- Visualizar Eventos: os usuários poderão visualizar os eventos disponíveis 
com informações detalhadas (nome, data, descrição e o número de vagas restantes)

- Visualizar Inscrições: o organizador poderá visualizar a lista de inscritos para cada
evento.

- Inscrição em Eventos: os alunos podem se inscrever nos eventos que estão
disponíveis e dentro do limite de vagas.

- Atualização de Eventos: deve ser possível atualizar informações sobre eventos já
cadastrados, como alterar a data ou o número de vagas disponíveis.

- Cancelar e Excluir Eventos: deve ser possível remover eventos que foram cancelados.

## ⚙ Funcionalidades
Oferece funcionalidades voltadas para dois tipos de usuários: alunos e
coordenadores.

- Alunos: podem visualizar eventos disponíveis e se inscrever neles. 
- Coordenadores: possuem acesso a ferramentas de criação, edição,
cancelamento e exclusão de eventos, além de poderem visualizar as inscrições
realizadas.