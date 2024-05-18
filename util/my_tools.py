
# loads the config file for 'random' animal bank
# source of config values: https://gist.github.com/atduskgreg/3cf8ef48cb0d29cf151bedad81553a54
def load_config_file():
    pet_config = []
    with open('pet_config.txt', 'r') as config:
        for line in config:
            pet_config.append(line.strip())

    # print(pet_config)
    return pet_config