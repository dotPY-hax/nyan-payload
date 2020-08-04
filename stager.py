import base64


def write_file(base64_content, file_name):
    with open(file_name, "wb") as file:
        file_content = base64.b64decode(base64_content)
        file.write(file_content)


def write_files(file_list):
    for file in file_list:
        content, file_name = file
        write_file(content, file_name)
