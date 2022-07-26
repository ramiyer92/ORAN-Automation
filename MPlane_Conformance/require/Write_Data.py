import configparser


# Writing Data
def WriteData(dic,filename):
    config = configparser.ConfigParser()
    try:
        config.read(filename)
    except Exception as e:
        print(e)

    try:
        config.add_section("INFO")
    except configparser.DuplicateSectionError:
        pass
    for key,val in dic.items():
        config.set("INFO", key, val)
    with open(filename, "w") as config_file:
        config.write(config_file)
    print('Data append...')
