import MainBackendProject as Backend

class RedactProduct:
    word_db = None

    def __init__(self, value_redaction):
        self.value_redaction = value_redaction
        self.id_product = self.value_redaction
        self.name = Backend.MainBackendProject.DB[self.id_product][0]
        self.amount = Backend.MainBackendProject.DB[self.id_product][1]
        self.brand = Backend.MainBackendProject.DB[self.id_product][2]
        self.opt = Backend.MainBackendProject.DB[self.id_product][3]
        self.retail = Backend.MainBackendProject.DB[self.id_product][4]

    def redaction_method(self, word_db):
        self.word_db = word_db
        key = None
        time_dict = {"1": self.id_product, "2": self.name, "3": self.amount, "4": self.brand, "5": self.opt,
                     "6": self.retail}
        if word_db is None:
            print("Вы ввели что-то не так. Напоминаем что вы должны выбрать в пределах диапазона 1-6."
                  "\nПовторите попытку")
        else:
            for key, item in time_dict.items():
                if key == word_db:
                    print(f"Вы выбрали -> {item}")
                    break
            word_db = input("Введите новое значение: ")
            if key == "1":
                Backend.MainBackendProject.DB[word_db] = Backend.MainBackendProject.DB.pop(key)
            else:
                Backend.MainBackendProject.DB[self.id_product][int(key) - 2] = word_db
            return Backend.MainBackendProject.DB

    def choice_info_in_db(self, value_redaction):
        """Задача этого метода:
        1. Распаковать значение выбранного товара.
        2. Передать в переменную word_db это значение, для дальнейшего изменения"""
        self.value_redaction = value_redaction
        if value_redaction is not None:
            value = Backend.MainBackendProject.DB[value_redaction]
            name, amount, brand, opt, retail = value
            print(f"Мы вошли в БД по ID -> {value_redaction}.\nВыберите что необходимо изменить.\n------------------------\n"
                  f"1. ID товара: {value_redaction}\n"
                  f"2. Название: {name}\n"
                  f"3. Количество: {amount}\n"
                  f"4. Бренд | Марка: {brand}\n"
                  f"5. Оптовая цена: {opt}\n"
                  f"6. Розничная цена: {retail}\n------------------------\n")
            self.word_db = input("Ввод: ")
            return self.word_db, value_redaction, self.redaction_method(self.word_db)
        else:
            print("Вы нечего не ввели. Попробуйте еще раз")
