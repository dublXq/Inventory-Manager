import MainBackendProject as Backend
import AddProduct
import RedactProduct
import DeleteProduct
backend = Backend.MainBackendProject()
import SearchProduct

def short_description_db():
    for key, el1 in backend.DB.items():
        print("-------------------------------------"
              "\n| " + str(key) + " | Название: " + el1[0] + f" | Бренд: {el1[2]}\n"
            f"-------------------------------------")


class Main:

    print("Добро пожаловать в главное меню! Вас приветствует Менеджер товаров.\n"
          "Я умею: Добавлять товары в БД, удалять по ID, редактировать товары по необходимости\n"
          "А так же, производить поиск и сохранять данные. Ниже приведено понятное меню, с которым можно работать.\n"
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

                    print(f"\nПроверка: Все ли правильно было заполнено ?\n------------------------\n"
                          f"ID товара: {Backend.MainBackendProject.id_product}\n"
                          f"Название: {Backend.MainBackendProject.name_product}\n"
                          f"Количество: {Backend.MainBackendProject.amount_product}\n"
                          f"Бренд | Марка: {Backend.MainBackendProject.brand_product}\n"
                          f"Оптовая цена: {Backend.MainBackendProject.opt_price_product}\n"
                          f"Розничная цена: {Backend.MainBackendProject.retail_price_product}\n------------------------")

                    val = input("1.Да\n2.Нет\nВвод: ")
                    if val == "1":
                        backend.preparation_zip_info_str(Backend.MainBackendProject.name_product, Backend.MainBackendProject.amount_product,
                                                         Backend.MainBackendProject.brand_product, Backend.MainBackendProject.opt_price_product,
                                                         Backend.MainBackendProject.retail_price_product)
                        AddProduct.AddProduct.add_set_product(Backend.MainBackendProject.id_product, backend.time_value)
                    else:
                        break

                case "2":
                    print("Мы перешли в раздел -> Редактирования.\n\n"
                          "Для правильного редактирования, следуйте пожалуйста инструкции:\n"
                          "1.Вам будет показано краткое описание всех товаров, которые есть в БД\n"
                          "2.Выберите по номеру, какой из товаров необходимо отредактировать\n"
                          "3.После того, как вы выбрали, выбранный вами товар, будет разделен на категории.\n"
                          "4.Выберите необходимую вам категорию, для редактирования, и нажмите -> Сохранить\n")
                    short_description_db()
                    value_redaction = input("\nВвод: ")
                    redact = RedactProduct.RedactProduct(value_redaction)
                    redact.choice_info_in_db(value_redaction)
                case "3":
                    print("Мы перешли в раздел -> Удаления.\n\n"
                         "Для корректного удаления, следуйте пожалуйста инструкции:\n"
                         "1.Вам будет показано краткое описание всех товаров, которые есть в БД\n"
                         "2.Выберите по номеру, какой из товаров необходимо удалить\n"
                         "3.Выберите необходимый товар, и подтвердите удаление\n")
                    short_description_db()
                    value_id = input("Введите ID товара: ")
                    v = input(f"Вы точно хотите удалить товар по ID -> {value_id}?\nЕсли Да, нажмите -> 1.\nЕсли Нет -> 2.\nВвод: ")
                    if v == "1":
                        DeleteProduct.DeleteProduct.delete_method(value_id)
                    else:
                        print("Удаление было прервано...")
                case "4":
                        SearchProduct.SearchProduct.search_product_to_id()
                case "5":
                    pass
                case "6":
                    break
