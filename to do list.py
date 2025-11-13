task = []
def add_task():
    new_task = input('\nEnter Your Task: ').lower()
    task.append(new_task)
    print('\nSucessfully Added')
    return
def remove_task():
    item = input('\nWhich Task Would You Like To Remove: ').lower()
    try:
        task.remove(item)
        print('\nSuccessfully Removed')
    except ValueError:
        print("\nTask Not Found")
    return
def remaning_task():
    print('\n')
    print(task)
    return
def mark_as_done():
    tasks_completed = input('\nWhich Task Would You Like to Mark as Done: ').lower()
    try:
        task.remove(tasks_completed)
        print('\nDone')
    except ValueError:
        print('Not Found')
    return
    



while True:
    print('\n1. Add Task\n2. Remove Task\n3. Remaining Tasks\n4. Mark as Done \n5. Exit ')
    try:
        choice = int(input('Enter Your Choice: '))
        if choice == 1:
            add_task()
        elif choice == 2:
            remove_task() 
        elif choice == 3:
            remaning_task()
        elif choice == 4:
            mark_as_done()
        elif choice == 5:
            print('\nExiting...')
            break
        else:
            print('\nSelect a Valid Option')
    except ValueError:
        print("\nInvalid Choice")