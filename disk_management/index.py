from pandas import DataFrame
from read_file import read_lines

total_storage = 2581.57

class User:
    def __init__(self, name, used_storage):
        self._name = name
        self._used_storage = self.calculate_used_storage(used_storage)
        self._used_storage_percent = self.calculate_used_storage_percent(used_storage)
    
    def calculate_used_storage(self, used_storage):
        return round(used_storage * .000000953667432, 2)

    def calculate_used_storage_percent(self, used_storage):
        return round((100 * self._used_storage) / total_storage, 2)

def transform_in_data_frame(values):
    data_frame = DataFrame({
        'Nr.': list(range(1, len(values) + 1)),
        'Usuário': [ value._name.capitalize() for value in values ],
        'Espaço Utilizado': [f'{value._used_storage} MB' for value in values],
        '% do uso': [ f'{value._used_storage_percent}%' for value in values ]
    })

    return data_frame

data = [data.split() for data in read_lines('users.txt', 'r')]
users = [User(name, int(used_storage)) for name, used_storage in data]

users_df = transform_in_data_frame(users)

print('ACME Inc. Uso do espaço em disco pelos usuários')
print('-----------------------------------------------')
print(users_df)
