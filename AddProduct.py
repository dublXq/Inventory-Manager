import MainBackendProject as Backend

class AddProduct:

    @staticmethod
    def add_set_product(key, value):
        """Сеттер для добавления товаров в словарь MainBackendProject.DB"""
        value = value.split("|")
        value = list(value)
        name, amount, brand, opt, retail = value
        if (isinstance(name, str) and amount.isdigit() and isinstance(brand, str) #Проверка на равенство типов
                and opt.isdigit() and retail.isdigit()):
            value_list = list(value)
            Backend.MainBackendProject.DB[key] = value_list
        else:
            print("Проверьте пожалуйста введенные вами данные. Произошла ошибка.")

    @staticmethod
    def add_get_product():
        return Backend.MainBackendProject.DB
