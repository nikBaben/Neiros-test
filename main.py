from editor import Menu


def main() -> None:
    menu = Menu()

    while True:
        menu.main_menu()

        try:
            choice = int(input("Выберите пункт меню: ").strip())
        except ValueError:
            print("Ошибка: введено не число.")
            continue

        if choice == 1:
            menu.clear_screen()
            menu.create_point()

        elif choice == 2:
            menu.clear_screen()
            menu.create_line()

        elif choice == 3:
            menu.clear_screen()
            menu.create_square()

        elif choice == 4:
            menu.clear_screen()
            menu.create_rectangle()
        
        elif choice == 5:
            menu.clear_screen()
            menu.create_circle()
        
        elif choice == 6:
            menu.clear_screen()
            menu.create_oval()

        elif choice == 7:
            menu.clear_screen()
            menu.editor.list()

        elif choice == 8:
            menu.clear_screen()
            try:
                menu.delete_shape()
            except ValueError as error:
                print(error)

        elif choice == 9:
            menu.clear_screen()
            try:
                menu.delete_all_shapes()
            except ValueError as error:
                print(error)
        
        elif choice == 10:
            menu.clear_screen()
            while True:
                menu.file_menu()
                
                try:
                    choice = int(input("Выберите пункт меню: ").strip())
                except ValueError:              
                    print("Ошибка: введено не число.")
                    continue

                if choice == 1:
                    menu.clear_screen()
                    menu.file()
                    choice = str(input())
                    menu.register_file(choice)
                
                elif choice == 2: 
                    menu.clear_screen()
                    menu.save_to_file()
                elif choice == 3: 
                    menu.clear_screen()
                    menu.load_from_file()

                elif choice == 0:
                    print("Выход из меню работы с файлами.")
                    break
            
        elif choice == 0:
            print("Выход из программы.")
            break

        else:
            print("Неверный пункт меню.")


if __name__ == "__main__":
    main()