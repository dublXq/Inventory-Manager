import MainBackendProject as Backend

class DeleteProduct:

    @staticmethod
    def delete_method(id_product):
        """Метод, который удаляет товар по ID"""
        del Backend.MainBackendProject.DB[id_product]