import pandas as pd

character_df = pd.read_json('character.json')
episode_df = pd.read_json('episodes.json')

# Quantos char existem nesse json?
print(character_df.count().id)

# Quantos são humanos?
is_human = character_df['species'] == 'Human'

print(len(character_df[is_human]))

# Quantos tipos de aliens diferentes?
is_alien = character_df['species'] == 'Alien'
aliens = character_df[is_alien]

print(aliens['type'].nunique())

# Quantos alienigenas são macho e quantos femeas
is_female = aliens['gender'] == 'Female'
is_male = aliens['gender'] == 'Male'

print(len(aliens[is_female]))
print(len(aliens[is_male]))