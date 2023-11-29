from prompt_toolkit.shortcuts import radiolist_dialog
from prompt_toolkit.styles import Style

from address_book import addressbook_main
from note import note_main
from sort_folders import sort_main


def main():
    result = 0
    while result is not None:
        result = radiolist_dialog(
            title="Welcome to Exponenta app.",
            text='''Here you can:
        1. make your own address book,
        2. write some notes,
        3. sort your folder with random files
What would you like to do ? ''',
            values=[
                ("addressbook", "Address book"),
                ("notebook", "Notebook"),
                ("sort", "Sort directory"),
            ],
            style=Style.from_dict({
                'dialog': 'bg:#539ce6',
                # 'button': 'bg:#bf99a4',
                'checkbox': '#e8612c',
                'dialog.body': 'bg:#a9cfd0',
                # 'dialog shadow': 'bg:#3540bd',
                'frame.label': '#280e6e',
                'dialog.body label': '#613ccf',
            })
        ).run()
        if result == "addressbook":
            addressbook_main()
        elif result == "notebook":
            note_main()
        elif result == "sort":
            sort_main()


if __name__ == "__main__":
    main()
