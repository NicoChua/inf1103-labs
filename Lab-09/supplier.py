class Supplier:
    def __init__(self, supplier_id: str, name: str, contact_email: str) -> None:
        self.__supplier_id: str = supplier_id
        self.__name: str = name
        self.__contact_email: str = contact_email

    # Getters
    def get_supplier_id(self) -> str:
        return self.__supplier_id

    def get_name(self) -> str:
        return self.__name

    def get_contact_email(self) -> str:
        return self.__contact_email

    def display_information(self) -> None:
        print(f"Supplier ID : {self.__supplier_id}")
        print(f"Name : {self.__name}")
        print(f"Contact Email : {self.__contact_email}")

    # Returns supplier data as a dictionary for saving to JSON
    def to_dict(self) -> dict:
        return {"id": self.__supplier_id, "name": self.__name, "contact_email": self.__contact_email}
