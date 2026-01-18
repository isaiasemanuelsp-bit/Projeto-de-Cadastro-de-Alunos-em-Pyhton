lnome = []
lidade = []
lnota = []

def adicionar_aluno(nome, idade, nota):
    nome = input('\nDigite o nome do aluno(a): ')
    idade = int(input('Digite a idade do aluno(a): '))
    while True:
        nota = float(input('Digite a nota do aluno(a): '))
        if nota >= 0 and nota <= 10:
            break
        else:
            print('Nota inválida. A nota deve deve ser de 0 a 10.')

    lnome.append(nome)
    lidade.append(idade)
    lnota.append(nota)

    print(f'\nO aluno(a) {nome}, de idade {idade} e nota {nota} foi adicionado.')

def listar_alunos(lnome, lidade, lnota):
    for aluno in range(len(lnome)):
        print(f'Aluno(a): {lnome[aluno]} | Idade: {lidade[aluno]} | Nota: {lnota[aluno]}')

def buscar_aluno(lnome):
    busca = input('Digite o nome do(a) aluno(a) que você deseja buscar: ').lower()
    if busca in [nome.lower() for nome in lnome]:
        aluno = [nome.lower() for nome in lnome].index(busca)
        print(f'\nBusca encontrada!\nAluno(a): {lnome[aluno]} | Idade: {lidade[aluno]} | Nota: {lnota[aluno]}')
    else:
        print('\nAluno(a) não encontrado(a)!')

def remover_aluno(lnome):
    remover = input('Digite o nome do aluno(a) que você deseja remover: ').lower()
    if remover in [nome.lower() for nome in lnome]:
        i = [nome.lower() for nome in lnome].index(remover)
        lnome.pop(i)
        lidade.pop(i)
        lnota.pop(i)
        print(f'\nAluno(a) removido(a).')
    else:
        print('\nAlunoa(a) não encontrado(a!')

def media_notas(lnota):
    media = 0
    for nota in lnota:
        media += nota
    print(f'A média de notas é {media / (len(lnota)):.2f}.')

while True:
    menu = int(input(
        '\n O que deseja fazer?\n1. Adicionar aluno(a)\n2. Listar todos os alunos\n3. Buscar aluno(a) pelo nome\n4. Remover aluno(a)\n5. Mostrar média geral das notas\n6. Sair\n\nDigite a opção que deseja selecionar: '
        ))
    match menu:
        case 1:
            adicionar_aluno(lnome, lidade, lnota)
        case 2:
            if len(lnome) == 0:
                print('\nNão existe nenhum aluno cadastrado.')
            else:
                listar_alunos(lnome, lidade, lnota)
        case 3:
            if len(lnome) == 0:
                print('\nNão existe nenhum aluno cadastrado.')
            else:
                buscar_aluno(lnome)
        case 4:
            remover_aluno(lnome)
        case 5:
            media_notas(lnota)
        case 6:
            print('\n     Fechando programa...\n')
            break
        case _:
            print('\nOpção inválida.')
