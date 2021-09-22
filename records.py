from peewee import *




#A menu - you need to add the database and fill in the functions. 
db = SqliteDatabase('records.sqlite')

class Record(Model):
    record = CharField()

    class Meta:
        database = db

    def __str__(self):
        return f'{self.record}'


def main():
    menu_text = """
    1. Display all records
    2. Add new record
    3. Edit existing record
    4. Delete record 
    5. Quit
    """

    while True:
        print(menu_text)
        choice = input('Enter your choice: ')
        if choice == '1':
            display_all_records()
        elif choice == '2':
            add_new_record()
        elif choice == '3':
            edit_existing_record()
        elif choice == '4':
            delete_record()
        elif choice == '5':
            break
        else:
            print('Not a valid selection, please try again')


def display_all_records():
    results = Record.select()
    print(list(results))
   # print('todo display all records')


def add_new_record():
    print('todo add new record. What if user wants to add a record that already exists?')
    record_name = input('enter a record')
    add_new_record = Record(record=record_name)
    add_new_record.save()

def edit_existing_record():
    print('todo edit existing record. What if user wants to edit record that does not exist?') 
    change_record = input('enter a record to save')
    Record.update().where(Record.record == change_record).execute()

def delete_record():
    print('todo delete existing record. What if user wants to delete record that does not exist?') 
    record_to_delete = input('enter a record to delete')
    Record.delete().where(Record.record == record_to_delete)

if __name__ == '__main__':
    main()