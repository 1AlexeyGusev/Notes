import uuid
from datetime import datetime


def input_id():
    return str(uuid.uuid4())


def input_date():
    return datetime.now()


def input_title():
    return input("Тема: ")


def input_note():
    return input("Текст заметки: ")


def create_note():
    id = input_id()
    date = input_date()
    title = input_title()
    note = input_note()
    return f'{id}\n{date}\n{title}\n{note}\n\n'


def add_note(note):
    with open('notebook.csv', 'a', encoding='UTF-8') as file:
        file.write(note)


def show_notes():
    with open('notebook.csv', 'r', encoding='UTF-8') as file:
        notes_list = file.read()
        print(notes_list)


def search_notes():
    print(
        'Возможные варианты поиска:\n'
        '1. По id\n'
        '2. По дате\n'
        '3. По теме\n'
    )
    var_search = input('Выберите вариант поиска: ')

    while var_search not in ('1', '2', '3'):
        print('Некорректный выбор! Выберите один из предложенных вариантов:')
        var_search = input('Введите вариант поиска: ')

    index_var = int(var_search) - 1

    search = input('Введите данные для поиска: ')

    with open('notebook.txt', 'r', encoding='UTF-8') as file:
        notes_list = file.read().rstrip().split('\n\n')

    for note_str in notes_list:
        curr_note = note_str.split()
        if search in curr_note[index_var]:
            print(note_str)
def edit_note():
    with open('notebook.csv', 'r+', encoding='UTF-8') as file:
        data = file.read()
        if len(data) ==0:
            print("Заметок нет!")
            return
        notes = data.strip().split("\n\n")
        notes_size = len(notes)
        id_list = [str(i + 1) for i in range(notes_size)]
        edit_id = "0"
        while edit_id not in id_list:
            edit_id = input("Введите номер заметки для редактирования: ")
        edit_note = notes[int(edit_id) - 1]
        list_edit_note = edit_note.split("\n")
        new_note = ""
        while len(new_note) == 0:
            print(f"Старый текст заметки:\n{list_edit_note[3]}")
            new_note = input("Введите новый текст заметки:\n").strip()
        list_edit_note[3] = new_note
        notes[int(edit_id) - 1] = ""
        for i in range(len(list_edit_note)):
            notes[int(edit_id) - 1] += f"{list_edit_note[i]}\n"
        notes[int(edit_id) - 1] = notes[int(edit_id) - 1].strip()
        text = ""
        for i in range(len(notes)):
            text += notes[i] + "\n\n\n"
    with open("notebook.csv", "w", encoding="UTF-8") as file:
        file.write(text)

def delete_note():
    with open("notebook.csv", "r+", encoding="UTF-8") as file:
        text = file.read()
        if len(text) == 0:
            print("Заметки для удаления отсутствуют.")
            return
        note_list = text.rstrip().split("\n\n")
        note_list_size = len(note_list)
        print(f"Всего на данный момент заметок: {note_list_size}.")
        id_list = [str(i+1) for i in range(note_list_size)]
        del_id = "0"
        while del_id not in id_list:
            del_id = input("Введите номер заметки для удаления: ")
        note_list.pop(int(del_id)-1)
        for i in range(len(note_list)):
            cur_note = note_list[i].split("\n")
            cur_note[0] = str(i+1)
            note_list[i] = ""
            for j in range(len(cur_note)):
                note_list[i] += f"{cur_note[j]}\n"
        text = ""
        for i in range(len(note_list)):
            text += note_list[i]+"\n\n"
    # print(text)
    with open("notebook.csv", "w", encoding="UTF-8") as file:
        file.write(text)




def interface():
    with open('notebook.csv', 'a', encoding='UTF-8') as file:
        pass
    command = '-1'
    while command != '5':
        print('Выберите действие: \n'
              '1. Добавить заметку:\n'
              '2. Показать заметки:\n'
              '3. Поиск заметки:\n'
              '4. Редактировать заметку:\n'
              '5. Удалить заметку:\n'
              '6. Выход.')
        command = input('Выберите команду:')
        while command not in('1', '2', '3','4','5','6'):
            print('Некорректный ввод')
            return
        match command:
            case '1':
                add_note(create_note())
            case'2':
                show_notes()
            case'3':
                search_notes()
            case'4':
                edit_note()
            case'5':
                delete_note()
            case'6':
                print("Выход")

interface()

