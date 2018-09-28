# Constants used in the batteries_included.ipynb

pokedex = 'podekex'
pikachu_id = 25
ids = [1, 2, 3]
pokemons = ['Bulbasaur', 'Ivysaur', 'Venusaur']

pokemon_names = ['Bulbasaur', 'Ivysaur', 'Venusaur', 'Charmander', 'Charmeleon', 'Charizard', 'Squirtle', 'Wartortle', 'Blastoise', 'Caterpie', 'Metapod', 'Butterfree', 'Weedle', 'Kakuna', 'Beedrill', 'Pidgey', 'Pidgeotto', 'Pidgeot', 'Rattata', 'Raticate', 'Spearow', 'Fearow', 'Ekans', 'Arbok', 'Pikachu', 'Raichu', 'Sandshrew', 'Sandslash', 'Nidoran♀', 'Nidorina', 'Nidoqueen', 'Nidoran♂', 'Nidorino', 'Nidoking', 'Clefairy', 'Clefable', 'Vulpix', 'Ninetales', 'Jigglypuff', 'Wigglytuff', 'Zubat', 'Golbat', 'Oddish', 'Gloom', 'Vileplume', 'Paras', 'Parasect', 'Venonat', 'Venomoth', 'Diglett', 'Dugtrio', 'Meowth', 'Persian', 'Psyduck', 'Golduck', 'Mankey', 'Primeape', 'Growlithe', 'Arcanine', 'Poliwag', 'Poliwhirl', 'Poliwrath', 'Abra', 'Kadabra', 'Alakazam', 'Machop', 'Machoke', 'Machamp', 'Bellsprout', 'Weepinbell', 'Victreebel', 'Tentacool', 'Tentacruel', 'Geodude', 'Graveler', 'Golem', 'Ponyta', 'Rapidash', 'Slowpoke', 'Slowbro', 'Magnemite', 'Magneton', "Farfetch'd", 'Doduo', 'Dodrio', 'Seel', 'Dewgong', 'Grimer', 'Muk', 'Shellder', 'Cloyster', 'Gastly', 'Haunter', 'Gengar', 'Onix', 'Drowzee', 'Hypno', 'Krabby', 'Kingler', 'Voltorb', 'Electrode', 'Exeggcute', 'Exeggutor', 'Cubone', 'Marowak', 'Hitmonlee', 'Hitmonchan', 'Lickitung', 'Koffing', 'Weezing', 'Rhyhorn', 'Rhydon', 'Chansey', 'Tangela', 'Kangaskhan', 'Horsea', 'Seadra', 'Goldeen', 'Seaking', 'Staryu', 'Starmie', 'Mr. Mime', 'Scyther', 'Jynx', 'Electabuzz', 'Magmar', 'Pinsir', 'Tauros', 'Magikarp', 'Gyarados', 'Lapras', 'Ditto', 'Eevee', 'Vaporeon', 'Jolteon', 'Flareon', 'Porygon', 'Omanyte', 'Omastar', 'Kabuto', 'Kabutops', 'Aerodactyl', 'Snorlax', 'Articuno', 'Zapdos', 'Moltres', 'Dratini', 'Dragonair', 'Dragonite', 'Mewtwo', 'Mew']

pokemon_types = (('Bulbasaur', 'Grass'), ('Ivysaur', 'Grass'), ('Venusaur', 'Grass'), ('Charmander', 'Fire'), ('Charmeleon', 'Fire'), ('Charizard', 'Fire'), ('Squirtle', 'Water'), ('Wartortle', 'Water'), ('Blastoise', 'Water'), ('Caterpie', 'Bug'), ('Metapod', 'Bug'), ('Butterfree', 'Bug'), ('Weedle', 'Bug'), ('Kakuna', 'Bug'), ('Beedrill', 'Bug'), ('Pidgey', 'Normal'), ('Pidgeotto', 'Normal'), ('Pidgeot', 'Normal'), ('Rattata', 'Normal'), ('Raticate', 'Normal'))

bulbasaur = {'id': 1, 'name': 'bulbasaur', 'base_experience': 64, 'height': 7, 'is_default': True, 'order': 1, 'weight': 69, 'abilities': [{'is_hidden': True, 'slot': 3, 'ability': {'name': 'chlorophyll', 'url': 'http://pokeapi.co/api/v2/ability/34/'}}], 'forms': [{'name': 'bulbasaur', 'url': 'http://pokeapi.co/api/v2/pokemon-form/1/'}], 'game_indices': [{'game_index': 1, 'version': {'name': 'white-2', 'url': 'http://pokeapi.co/api/v2/version/22/'}}], 'held_items': [], 'location_area_encounters': [], 'moves': [{'move': {'name': 'captivate', 'url': 'http://pokeapi.co/api/v2/move/445/'}, 'version_group_details': [{'level_learned_at': 0, 'version_group': {'name': 'heartgold-soulsilver', 'url': 'http://pokeapi.co/api/v2/version-group/10/'}, 'move_learn_method': {'name': 'machine', 'url': 'http://pokeapi.co/api/v2/move-learn-method/4/'}}, {'level_learned_at': 0, 'version_group': {'name': 'platinum', 'url': 'http://pokeapi.co/api/v2/version-group/9/'}, 'move_learn_method': {'name': 'machine', 'url': 'http://pokeapi.co/api/v2/move-learn-method/4/'}}, {'level_learned_at': 0, 'version_group': {'name': 'diamond-pearl', 'url': 'http://pokeapi.co/api/v2/version-group/8/'}, 'move_learn_method': {'name': 'machine', 'url': 'http://pokeapi.co/api/v2/move-learn-method/4/'}}]}], 'species': {'name': 'bulbasaur', 'url': 'http://pokeapi.co/api/v2/pokemon-species/1/'}, 'stats': [{'base_stat': 45, 'effort': 0, 'stat': {'name': 'speed', 'url': 'http://pokeapi.co/api/v2/stat/6/'}}], 'types': [{'slot': 2, 'type': {'name': 'poison', 'url': 'http://pokeapi.co/api/v2/type/4/'}}]}

pikachu = (25, 'Pikachu', 'Electric')

headers = {'User-Agent': 'Mozilla/5.0'}
