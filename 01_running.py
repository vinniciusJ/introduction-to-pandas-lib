class Athlete:
    def __init__(self, name, leaps, avg) :
        self._name, self._leaps, self._avg = name, leaps, avg

def calculate_avg(*args):
    numbers = [float(value) for value in args]
    
    return sum(numbers) / len(numbers)

athletes = []

while True:
    name = input('Atleta: ')

    if not name: break

    inputs = ['Primeiro Salto: ', 'Segundo Salto: ', 'Terceiro Salto: ', 'Quarto Salto: ', 'Quinto Salto: ']
    leaps = [value.split()[0] for value in [input(input_message) for input_message in inputs]]
    avg = calculate_avg(*leaps)

    athletes.append(Athlete(name, leaps, avg))

for athlete in athletes:
    print('Resultado Final: ')
    print(f'Atleta: {athlete._name}')
    print(f"Saltos: {' - '.join(athlete._leaps)}")
    print(f'Média dos saltos: {athlete._avg} m')

