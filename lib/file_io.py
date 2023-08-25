def write_file(file_name, file_content):
    a_file_name = open(f"{file_name}.txt", mode='w', encoding='utf-8')
    a_file_name.write(file_content)
    a_file_name.close()

def append_file(file_name, append_content):
    with open(f"{file_name}.txt", encoding='utf-8', mode='a') as a_file_name:
        a_file_name.write(append_content)

def read_file(file_name):
    with open(f"{file_name}.txt", encoding='utf-8', mode='r') as a_file_name:
        return a_file_name.read()
