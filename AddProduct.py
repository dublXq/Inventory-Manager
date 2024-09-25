import MainBackendProject as Backend
import CheckType as Check

class AddProduct:

    @staticmethod
    def add_set_product(key, value):
        """Сеттер для добавления товаров в словарь MainBackendProject.DB"""
        value = value.split("|")
        value = list(value)
        name, amount, brand, opt, retail = value
        if Check.CheckType.check_type_product(name, amount, brand, opt, retail):
            value_list = list(value)
            Backend.MainBackendProject.DB[key] = value_list
        else:
            print("Проверьте пожалуйста введенные вами данные. Произошла ошибка.")

    @staticmethod
    def add_get_product(key):
        return Backend.MainBackendProject.DB[key]