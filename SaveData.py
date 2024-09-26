import BackendInfo

path = "DataBaseProduct.txt"


class SaveData:
    time_result = None

    @staticmethod
    def save_all_data_in_db():
        with open(path, "w", encoding="utf-8") as file:
            for key, el1 in BackendInfo.BackendInfo.DB.items():
                file.write(f"\n------------------------\n"
                           f"ID: {str(key)} \n"
                           f"Название: {el1[0]} \n"
                           f"Количество: {el1[1]} \n"
                           f"Бренд | Марка: {el1[2]} \n"
                           f"Оптовая цена: {el1[3]} \n"
                           f"Розничная цена: {el1[4]} \n"
                           f"Маржа: {int(el1[4]) - int(el1[3])}")

    @staticmethod
    def read_db():
        with open(path, "r", encoding="utf-8") as file:
            SaveData.time_result = file.readlines()
            return SaveData.time_result

    @staticmethod
    def write_db(time_result):
        indexes = None
        name = None
        amount = None
        brand = None
        opt = None
        retail = None
        marja = None
        for item in time_result:
            item = item.strip("\n")
            if "ID:" in item:
                indexes = item.split("ID:")
                indexes = str(indexes[1]).strip()
            elif "Название:" in item:
                name = item.split("Название:")
                name = str(name[1]).strip()
            elif "Количество:" in item:
                amount = item.split("Количество:")
                amount = str(amount[1]).strip()
            elif "Бренд | Марка:" in item:
                brand = item.split("Бренд | Марка:")
                brand = str(brand[1]).strip()
            elif "Оптовая цена:" in item:
                opt = item.split("Оптовая цена:")
                opt = str(opt[1]).strip()
            elif "Розничная цена:" in item:
                retail = item.split("Розничная цена:")
                retail = str(retail[1]).strip()
                time_result = [name, amount, brand, opt, retail]
                BackendInfo.BackendInfo.DB[indexes] = time_result
                time_result = None

        return BackendInfo.BackendInfo.DB, time_result
