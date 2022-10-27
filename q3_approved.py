
studentsGrades = {}
studentsStatus = {}
qtd_student = int(input('Quantidade de alunos: '))

def addNewstudent(name):
        print(name.capitalize())
        grades = input(f'Nota de cada prova: ').split(' ')
        convGrades = [float(x) for x in grades]
        studentsGrades[name] = tuple(convGrades)
        studentsStatus[name] = approved(name)


def approved(name):
    count = 0
    grades = studentsGrades[name]
    for i in grades:
        if i >= 7:
            count += 1
        else:
            continue
    
    value = studentsGrades[name]

    if count == len(value):
        return 'Approved'
    else:
        return 'Not Approved'


for i in range(qtd_student):
    name = input(f'Nome do Aluno: ')
    addNewstudent(name)

for i in studentsStatus:
    print(f'Aluno ---- {i.capitalize()} \t\t {studentsStatus[i]}')
