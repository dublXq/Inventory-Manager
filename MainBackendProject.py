import CheckType as Check

class MainBackendProject:

    DB = {}
    time_value = None

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

    def preparation_zip_info_str(self, name_product, amount_product, brand_product, opt_price_product, retail_price_product):
        self.name_product = name_product
        self.amount_product = amount_product
        self.brand_product = brand_product
        self.opt_price_product = opt_price_product
        self.retail_price_product = retail_price_product
        # Сначала проверяем тип данных
        if Check.CheckType.check_type_product(
                name_product, amount_product, brand_product,
                opt_price_product, retail_price_product):
            # Если все хорошо, тогда переменной TIME_VALUE присваиваем строку значений через "|"
            self.time_value = (f"{name_product}|{amount_product}|"
                          f"{brand_product}|{opt_price_product}|"
                          f"{retail_price_product}")
            return self.time_value
