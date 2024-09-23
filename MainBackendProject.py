class MainBackendProject:

    DB = {}

    def __init__(self, id_product=None, name_product=None,
                 amount_product=None,brand_product=None,opt_price_product=None,
                 retail_price_product=None,margin_product=None):

        self.id_product = id_product #ID продукта
        self.name_product = name_product #Название продукта
        self.amount_product = amount_product #Количество продукта
        self.brand_product = brand_product #Бренд товара
        self.opt_price_product = opt_price_product #Цена за опт
        self.retail_price_product = retail_price_product #Цена за розницу
        self.margin_product = margin_product #Маржа продукта (розница - опт = маржа)
