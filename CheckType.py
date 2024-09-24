
class CheckType:
    """Класс отвечает за проверку тип данных"""

    @staticmethod
    def check_type_product(name, amount, brand, opt, retail):
        if (isinstance(name, str) and amount.isdigit() and isinstance(brand, str)  # Проверка на равенство типов
                and opt.isdigit() and retail.isdigit()):
            return True
