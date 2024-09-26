import backend_info
import save_data

def short_description_db():
    for key, el1 in backend_info.BackendInfo.DB.items():
        print("-------------------------------------"
        "\n| " + str(key) + " | Название: " + el1[0] + f" | Бренд: {el1[2]}\n"
        f"-------------------------------------")

class MainBackendProject:

    def __init__(self, id_product: int | str = None, name_product: str = None,
                 amount_product: int = None, brand_product: str = None, opt_price_product: int = None,
                 retail_price_product: int = None, margin_product: int = None):
        self.id_product = id_product  # ID продукта
        self.name_product = name_product  # Название продукта
        self.amount_product = amount_product  # Количество продукта
        self.brand_product = brand_product  # Бренд товара
        self.opt_price_product = opt_price_product  # Цена за опт
        self.retail_price_product = retail_price_product  # Цена за розницу
        self.margin_product = margin_product  # Маржа продукта (розница - опт = маржа)

    def preparation_zip_info_str(self, name_product, amount_product, brand_product, opt_price_product,
                                 retail_price_product):
        self.name_product = name_product
        self.amount_product = amount_product
        self.brand_product = brand_product
        self.opt_price_product = opt_price_product
        self.retail_price_product = retail_price_product
        # Сначала проверяем тип данных
        if CheckType.check_type_product(
                name_product, amount_product, brand_product,
                opt_price_product, retail_price_product):
            # Если все хорошо, тогда переменной TIME_VALUE присваиваем строку значений через "|"
            backend_info.BackendInfo.time_value = (f"{name_product}|{amount_product}|"
                               f"{brand_product}|{opt_price_product}|"
                               f"{retail_price_product}")
            return backend_info.BackendInfo.time_value
        else:
            print("Проверьте пожалуйста еще раз, все ли вы правильно прописали. Возникла синтаксическая ошибка")


class SearchProduct(MainBackendProject):
    @classmethod
    def search_product_in_db(cls, key):
        for i in backend_info.BackendInfo.DB.keys():
            if i == key:
                return True

    @classmethod
    def search_info_product(cls, key):
        for id_ in backend_info.BackendInfo.DB:
            if id_ == key:
                value = backend_info.BackendInfo.DB[id_]
                name, amount, brand, opt, retail = value
                print(f"1. ID товара: {id_}\n"
                      f"2. Название: {name}\n"
                      f"3. Количество: {amount}\n"
                      f"4. Бренд | Марка: {brand}\n"
                      f"5. Оптовая цена: {opt}\n"
                      f"6. Розничная цена: {retail}\n"
                      f"Маржа -> {int(retail) - int(opt)}")

    @staticmethod
    def search_product_to_id():
        print("Мы перешли в раздел -> Поиск.\n\n"
              "Для того чтобы найти необходимый Вам товар, пожалуйста, следуйте инструкции:\n"
              "1.Вам будет показано предложено 2 варианта\n"
              "- Поиск товара по ID (Вы должны знать IDшник товара)\n"
              "- Поиск товара по краткому описанию (Будет вывод всей БД, и вы должны указать номер нужного товара)\n"
              "2.Выберите один из предложенных вариантов, после чего будет произведен поиск\n")
        val = input("1. Поиск товара по ID\n2. Поиск товара по краткому описанию\nВвод: ")
        if val == "1":
            val = input("Введите ID: ")
            if SearchProduct.search_product_in_db(val):
                print("Товар успешно найден!\nТовар: \n------------------------")
                SearchProduct.search_info_product(val)
                print("------------------------")
            else:
                print("\n------------------------------------------------------------------------------\n"
                      "Такого ID нет. Повторите попытку. Если не помните ID, лучше выберете 2-й вариант\n"
                      "------------------------------------------------------------------------------\n")
        elif val == "2":
            short_description_db()
            val = input("Введите ID товара: ")
            if val in backend_info.BackendInfo.DB.keys():
                print("Товар: \n------------------------")
                SearchProduct.search_info_product(val)
                print("------------------------")
            else:
                print("\n-------------------------------------------------\n"
                      "Ошибка: Такого ID нет. Проверьте пожалуйста еще раз\n"
                      "---------------------------------------------------\n")
        else:
            print("Вы вышли за предел диапазона. Повторите пожалуйста попытку. [ Диапазон: 1-2 ]")


class CheckType(MainBackendProject):
    """Класс отвечает за проверку тип данных"""

    @staticmethod
    def check_type_product(name, amount, brand, opt, retail):
        if (isinstance(name, str) and amount.isdigit() and isinstance(brand, str)  # Проверка на равенство типов
                and opt.isdigit() and retail.isdigit()):
            return True

class DeleteProduct:

    @staticmethod
    def delete_method(id_product):
        """Метод, который удаляет товар по ID"""
        del backend_info.BackendInfo.DB[id_product]


class RedactProduct:
    word_db = None

    def __init__(self, value_redaction):
        self.value_redaction = value_redaction
        self.id_product = self.value_redaction
        self.name = backend_info.BackendInfo.DB[self.id_product][0]
        self.amount = backend_info.BackendInfo.DB[self.id_product][1]
        self.brand = backend_info.BackendInfo.DB[self.id_product][2]
        self.opt = backend_info.BackendInfo.DB[self.id_product][3]
        self.retail = backend_info.BackendInfo.DB[self.id_product][4]

    def redaction_method(self, word_db):
        self.word_db = word_db
        key = None
        time_dict = {"1": self.id_product, "2": self.name, "3": self.amount, "4": self.brand, "5": self.opt,
                     "6": self.retail}
        if word_db is None:
            print("Вы ввели что-то не так. Напоминаем что вы должны выбрать в пределах диапазона 1-6."
                  "\nПовторите попытку")
        else:
            if word_db not in ["1","2","3","4","5","6"]:
                print("Вы вышли за диапазон. Повторите пожалуйста попытку")
            else:
                for key, item in time_dict.items():
                    if key == word_db:
                        print(f"Вы выбрали -> {item}")
                        break
                word_db = input("Введите новое значение: ")
                if key == "1":
                    backend_info.BackendInfo.DB[word_db] = backend_info.BackendInfo.DB.pop(key)
                else:
                    backend_info.BackendInfo.DB[self.id_product][int(key) - 2] = word_db
                return backend_info.BackendInfo.DB

    def choice_info_in_db(self, value_redaction):
        """Задача этого метода:
        1. Распаковать значение выбранного товара.
        2. Передать в переменную word_db это значение, для дальнейшего изменения"""
        self.value_redaction = value_redaction
        if value_redaction is not None:
            value = backend_info.BackendInfo.DB[value_redaction]
            name, amount, brand, opt, retail = value
            print(
                f"Мы вошли в БД по ID -> {value_redaction}.\nВыберите что необходимо изменить.\n------------------------\n"
                f"1. ID товара: {value_redaction}\n"
                f"2. Название: {name}\n"
                f"3. Количество: {amount}\n"
                f"4. Бренд | Марка: {brand}\n"
                f"5. Оптовая цена: {opt}\n"
                f"6. Розничная цена: {retail}\n"
                f" -> Маржа: {int(retail) - int(opt)}\n------------------------\n")
            self.word_db = input("Ввод: ")
            return self.word_db, value_redaction, self.redaction_method(self.word_db)
        else:
            print("Вы нечего не ввели. Попробуйте еще раз")


class AddProduct(CheckType, MainBackendProject):

    @staticmethod
    def add_set_product(key, value):
        """Сеттер для добавления товаров в словарь MainBackendProject.DB"""
        value = value.split("|")
        value = list(value)
        name, amount, brand, opt, retail = value
        if CheckType.check_type_product(name, amount, brand, opt, retail):
            value_list = list(value)
            backend_info.BackendInfo.DB[key] = value_list
        else:
            print("\n-----------------------------------------------------------\n"
                  "Проверьте пожалуйста введенные вами данные. Произошла ошибка.\n"
                  "-------------------------------------------------------------\n")

    @staticmethod
    def add_get_product(key):
        return backend_info.BackendInfo.DB[key]

if __name__ == '__main__':

    class Main(AddProduct, RedactProduct, DeleteProduct, CheckType, SearchProduct, MainBackendProject):
        backend = MainBackendProject()
        delete = DeleteProduct()
        backend_info = backend_info.BackendInfo



        save_data.SaveData.read_db()
        save_data.SaveData.write_db(save_data.SaveData.time_result)

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
                "5. Сохранить\n"
                "6. Выйти\n"
                "Ввод: ")

            if value_choice_in_menu not in ["1", "2", "3", "4", "5", "6"]:
                print("Произошла ошибка: Выход за границы. Необходимо ввести в диапазоне 1-6.\nПопробуйте еще раз :)\n")
            else:
                match value_choice_in_menu:

                    case "1":
                        print("Мы перешли в раздел -> Добавления товара.\n"
                              "Заполните поэтапные шаги:\n")
                        backend.id_product = input("ID товара: ")
                        backend.name_product = input("Название: ")
                        backend.amount_product = input("Количество: ")
                        backend.brand_product = input("Бренд | Марка: ")
                        backend.opt_price_product = input("Оптовая цена: ")
                        backend.retail_price_product = input("Розничная цена: ")

                        print(f"\nПроверка: Все ли правильно было заполнено ?"
                              f"\n------------------------\n"
                              f"ID товара: {backend.id_product}\n"
                              f"Название: {backend.name_product}\n"
                              f"Количество: {backend.amount_product}\n"
                              f"Бренд | Марка: {backend.brand_product}\n"
                              f"Оптовая цена: {backend.opt_price_product}\n"
                              f"Розничная цена: {backend.retail_price_product}\n"
                              f"------------------------\n")
                        val = input("1.Да\n2.Нет\nВвод: ")
                        if val == "1":
                            if val in backend_info.DB.keys():
                                print("Ошибка: ID не могут совпадать!")
                            else:
                                backend.preparation_zip_info_str(
                                    backend.name_product, backend.amount_product, backend.brand_product,
                                    backend.opt_price_product, backend.retail_price_product)
                                if backend_info.time_value is not None:
                                    AddProduct.add_set_product(backend.id_product, backend_info.time_value)
                        elif val == "2":
                            print("Добавление успешно отменено!")
                    case "2":
                        print("Мы перешли в раздел -> Редактирования.\n\n"
                              "Для правильного редактирования, следуйте пожалуйста инструкции:\n"
                              "1.Вам будет показано краткое описание всех товаров, которые есть в БД\n"
                              "2.Выберите по номеру, какой из товаров необходимо отредактировать\n"
                              "3.После того, как вы выбрали, выбранный вами товар, будет разделен на категории.\n"
                              "4.Выберите необходимую вам категорию, для редактирования, и нажмите -> Сохранить\n")
                        short_description_db()
                        value_redaction = input("\nВвод: ")
                        if value_redaction in backend_info.DB.keys():
                            redact = RedactProduct(value_redaction)
                            redact.choice_info_in_db(value_redaction)
                        else:
                            print("Такого ID нет. Проверьте пожалуйста еще раз, и повторите попытку")
                    case "3":
                        print("Мы перешли в раздел -> Удаления.\n\n"
                              "Для корректного удаления, следуйте пожалуйста инструкции:\n"
                              "1.Вам будет показано краткое описание всех товаров, которые есть в БД\n"
                              "2.Выберите по номеру, какой из товаров необходимо удалить\n"
                              "3.Выберите необходимый товар, и подтвердите удаление\n")
                        short_description_db()
                        value_id = input("Введите ID товара: ")
                        if value_id in backend_info.DB.keys():
                            v = input(f"Вы точно хотите удалить товар по ID -> {value_id}?\nЕсли Да, нажмите -> 1.\nЕсли Нет -> 2.\nВвод: ")
                            if v == "1":
                                delete.delete_method(value_id)
                                print("Товар был успешно удален")
                        else:
                            print("Удаление было прервано.")
                    case "4":
                        SearchProduct.search_product_to_id()
                    case "5":
                        save_data.SaveData.save_all_data_in_db()
                        save_data.SaveData.read_db()
                        print("\n------------------------------------------------------------------------------\n"
                              "                     Все данные были успешно сохранены :)\n"
                              "------------------------------------------------------------------------------\n")
                    case "6":
                        break