import MainBackendProject as Backend
from Main import short_description_db
backend = Backend.MainBackendProject

class SearchProduct:

    @classmethod
    def search_product_in_db(cls, key):
        for i in Backend.MainBackendProject.DB.keys():
            if i == key:
                return True

    @classmethod
    def search_info_product(cls, key):
        for ID in backend.DB:
            if ID == key:
                value = Backend.MainBackendProject.DB[ID]
                name, amount, brand, opt, retail = value
                print(f"1. ID товара: {ID}\n"
                      f"2. Название: {name}\n"
                      f"3. Количество: {amount}\n"
                      f"4. Бренд | Марка: {brand}\n"
                      f"5. Оптовая цена: {opt}\n"
                      f"6. Розничная цена: {retail}\n"
                      f"7. Маржа: {int(retail) - int(opt)}")

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
        elif val == "2":
            short_description_db()
            val = input("Введите ID товара: ")
            print("Товар: \n------------------------")
            SearchProduct.search_info_product(val)
            print("------------------------")
        else:
            print("Вы вышли за предел диапазона. Повторите пожалуйста попытку. [ Диапазон: 1-2 ]")
