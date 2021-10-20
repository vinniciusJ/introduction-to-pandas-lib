import pandas as pd
from IPython.display import display

character_df = pd.read_json('character.json')
episode_df = pd.read_json('episodes.json')

# Quantos char existem nesse json?
print(f'1. Quantos personagens existem nessa lista? {character_df.count().id}')

# Quantos são humanos?
is_human = character_df['species'] == 'Human'
human_counter, _ = character_df.loc[is_human].shape

print(f'2. Quantos personagens são humanos? {human_counter}')

# Quantos tipos de aliens diferentes?
is_alien = character_df['species'] == 'Alien'
aliens = character_df[is_alien]
alien_counter, _ = aliens.shape

print(f'3. Quantos personagens são alienígenas? {alien_counter}')

diferent_alien_counter = aliens.groupby('type')
print(f'4. Há quantos tipos de alienígenas diferentes? {len(diferent_alien_counter)}')

# Quantos alienigenas são macho e quantos femeas
is_female = aliens['gender'] == 'Female'
is_male = aliens['gender'] == 'Male'

print('5. Quantos alienígenas são homens e quantos são mulheres?')
print(f'    * {aliens[is_female].shape[0]} são fêmeas')
print(f'    * {aliens[is_male].shape[0]} são machos')

crocubot = character_df[character_df['name'] == 'Crocubot']
crocobut_index = int(crocubot['id']) - 1

ep_url = crocubot['episode'][crocobut_index][0]
ep_id = int(ep_url[-2:])
ep_name = episode_df[episode_df['id'] == ep_id]['name'].to_string()

print(f'6. Qual o nome do episódio em que o personagem Crocubot aparece? {ep_name}')

planets = [planet['name'] for planet in character_df['origin']]
planets_counter = [1 for i in planets if 'Earth' in i]

print(f'7. Quantos personagens estão em planetas chamados Earth, independente do Universo? {sum(planets_counter)}')
