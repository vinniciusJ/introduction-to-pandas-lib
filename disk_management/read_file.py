def read_lines(path, method):
    lines = []

    with open(path, method) as file:
        lines = file.readlines()
    
    file.close()

    return lines