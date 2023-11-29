from prompt_toolkit.completion import NestedCompleter
from prompt_toolkit import prompt


class Output:

    def output(self, value):
        raise NotImplementedError()


class Out(Output):

    def output(self, value):
        self.value = value
        print(self.value)


def choose_command(COMMANDS_DICT):
    menu_completer = NestedCompleter.from_nested_dict(COMMANDS_DICT)
    command = prompt("Enter command or 'help' for help: ",
                     completer=menu_completer)
    return command
