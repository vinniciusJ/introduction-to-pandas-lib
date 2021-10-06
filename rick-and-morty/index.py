import pandas as pd

character_df = pd.read_json('character.json')
episode_df = pd.read_json('episodes.json')

# Quantos char existem nesse json?
print(f'1. Quantos personagens existem nessa lista? {character_df.count().id}')

# Quantos são humanos?
is_human = character_df['species'] == 'Human'

print(f'2. Quantos personagens são humanos? {len(character_df[is_human])}')

# Quantos tipos de aliens diferentes?
is_alien = character_df['species'] == 'Alien'
aliens = character_df[is_alien]

unique_aliens = aliens['type'].nunique()
print(f'4. Quantos personagens são alienígenas? {unique_aliens}')

# Quantos alienigenas são macho e quantos femeas
is_female = aliens['gender'] == 'Female'
is_male = aliens['gender'] == 'Male'

print('5. Quantos alienígenas são homens e quantos são mulheres?')
print(f'    * {len(aliens[is_female])} são fêmeas')
print(f'    * {len(aliens[is_male])} são machos')

crocubot = character_df[character_df['name'] == 'Crocubot']
crocobut_index = int(crocubot['id']) - 1

ep_url = crocubot['episode'][crocobut_index][0]
ep_id = int(ep_url[-2:])
ep_name = episode_df[episode_df['id'] == ep_id]['name'].to_string()

print(f'6. Qual o nome do episódio em que o personagem Crocubot aparece? {ep_name}')

planets = [planet['name'] for planet in character_df['origin']]
planets_counter = [1 for i in planets if 'Earth' in i]

print(f'7. Quantos personagens estão em planetas chamados Earth, independente do Universo? {sum(planets_counter)}')
