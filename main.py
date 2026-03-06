from editor import Menu


def main() -> None:
    menu = Menu()

    while True:
        menu.print_menu()

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
            menu.create_circle()

        elif choice == 4:
            menu.clear_screen()
            menu.create_square()

        elif choice == 5:
            menu.clear_screen()
            menu.editor.list()

        elif choice == 6:
            menu.clear_screen()
            try:
                menu.delete_shape()
            except ValueError as error:
                print(error)

        elif choice == 7:
            menu.clear_screen()
            try:
                menu.delete_all_shapes()
            except ValueError as error:
                print(error)

        elif choice == 0:
            print("Выход из программы.")
            break

        else:
            print("Неверный пункт меню.")


if __name__ == "__main__":
    main()