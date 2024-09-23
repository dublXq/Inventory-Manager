import MainBackendProject as Backend
import AddProduct

class Main:

    print("Добро пожаловать в главное меню! Вас приветствует Менеджер товаров.\n"
          "Я умею: Добавлять товары в БД, удалять по ID, редактировать товары по необходимости\n"
          "А так же, производить поиск и сохранять данные. Ниже приведена понятное меню, с которым можно работать.\n"
          "Продуктивного дня! ^_-\n")

    while True:
        value_choice_in_menu = input(
            "1. Добавить товар\n"
            "2. Редактировать товар\n"
            "3. Удалить товар\n"
            "4. Найти товар\n"
            "5. Сохранение\n"
            "6. Выйти\n"
            "Ввод: ")

        if value_choice_in_menu not in ["1", "2", "3", "4", "5", "6"]:
            print("Произошла ошибка: Выход за границы. Необходимо ввести в диапазоне 1-6.\nПопробуйте еще раз :)\n")
        else:
            match value_choice_in_menu:
                case "1":
                    print("Мы перешли в раздел -> Добавления товара.\n"
                          "Заполните поэтапные шаги:\n")
                    Backend.MainBackendProject.id_product = input("ID товара: ")
                    Backend.MainBackendProject.name_product = input("Название: ")
                    Backend.MainBackendProject.amount_product = input("Количество: ")
                    Backend.MainBackendProject.brand_product = input("Бренд | Марка: ")
                    Backend.MainBackendProject.opt_price_product = input("Оптовая цена: ")
                    Backend.MainBackendProject.retail_price_product = input("Розничная цена: ")

                    print(f"Проверка: Все ли правильно было заполнено ?\n"
                          f"ID товара: {Backend.MainBackendProject.id_product}\n"
                          f"Название: {Backend.MainBackendProject.name_product}\n"
                          f"Количество: {Backend.MainBackendProject.amount_product}\n"
                          f"Бренд | Марка: {Backend.MainBackendProject.brand_product}\n"
                          f"Оптовая цена: {Backend.MainBackendProject.opt_price_product}\n"
                          f"Розничная цена: {Backend.MainBackendProject.retail_price_product}\n")

                    val = input("1.Да\n2.Нет\nВвод: ")
                    if val == "1":
                        time_value = (
                            f"{Backend.MainBackendProject.name_product}|{Backend.MainBackendProject.amount_product}|"
                            f"{Backend.MainBackendProject.brand_product}|{Backend.MainBackendProject.opt_price_product}|"
                            f"{Backend.MainBackendProject.retail_price_product}")
                        AddProduct.AddProduct.add_set_product(Backend.MainBackendProject.id_product, time_value)
                    else:
                        break

                case "2":
                    pass
                case "3":
                    pass
                case "4":
                    pass
                case "5":
                    pass
                case "6":
                    break
