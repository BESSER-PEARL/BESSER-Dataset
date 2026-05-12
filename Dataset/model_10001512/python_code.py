from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Actor2_Actor:

    pass


class Actor_Actor:

    pass





class Manager:

    def __init__(self, Name: str, Address: str, ID: int, Contact: int, Personalnformation: str, waiter1: "Waiter" = None, customer5: "Customer" = None):
        self.Name = Name
        self.Address = Address
        self.ID = ID
        self.Contact = Contact
        self.Personalnformation = Personalnformation
        self.waiter1 = waiter1
        self.customer5 = customer5
        
        pass
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Personalnformation(self):
        return self.__Personalnformation
    @Personalnformation.setter
    def Personalnformation(self, Personalnformation: str):
        self.__Personalnformation = Personalnformation

    @property
    def Contact(self):
        return self.__Contact
    @Contact.setter
    def Contact(self, Contact: int):
        self.__Contact = Contact

    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def waiter1(self):
        return self.__waiter1
    @waiter1.setter
    def waiter1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Manager__waiter1", None)
        self.__waiter1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "manager0"):
                opp_val = getattr(old_value, "manager0", None)
                if opp_val == self:
                    setattr(old_value, "manager0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "manager0"):
                opp_val = getattr(value, "manager0", None)
                setattr(value, "manager0", self)

    @property
    def customer5(self):
        return self.__customer5
    @customer5.setter
    def customer5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Manager__customer5", None)
        self.__customer5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "manager4"):
                opp_val = getattr(old_value, "manager4", None)
                if opp_val == self:
                    setattr(old_value, "manager4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "manager4"):
                opp_val = getattr(value, "manager4", None)
                setattr(value, "manager4", self)



class Class:

    pass


class Customer:

    def __init__(self, Name: str, Contact_Number: int, Dishes_Ordered: str, Reservation: bool, date: str, reservedTables: str, waiter3: "Waiter" = None, manager4: "Manager" = None):
        self.Name = Name
        self.Contact_Number = Contact_Number
        self.Dishes_Ordered = Dishes_Ordered
        self.Reservation = Reservation
        self.date = date
        self.reservedTables = reservedTables
        self.waiter3 = waiter3
        self.manager4 = manager4
        
        pass
    @property
    def reservedTables(self):
        return self.__reservedTables
    @reservedTables.setter
    def reservedTables(self, reservedTables: str):
        self.__reservedTables = reservedTables

    @property
    def Contact_Number(self):
        return self.__Contact_Number
    @Contact_Number.setter
    def Contact_Number(self, Contact_Number: int):
        self.__Contact_Number = Contact_Number

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Reservation(self):
        return self.__Reservation
    @Reservation.setter
    def Reservation(self, Reservation: bool):
        self.__Reservation = Reservation

    @property
    def Dishes_Ordered(self):
        return self.__Dishes_Ordered
    @Dishes_Ordered.setter
    def Dishes_Ordered(self, Dishes_Ordered: str):
        self.__Dishes_Ordered = Dishes_Ordered

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def manager4(self):
        return self.__manager4
    @manager4.setter
    def manager4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__manager4", None)
        self.__manager4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer5"):
                opp_val = getattr(old_value, "customer5", None)
                if opp_val == self:
                    setattr(old_value, "customer5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer5"):
                opp_val = getattr(value, "customer5", None)
                setattr(value, "customer5", self)

    @property
    def waiter3(self):
        return self.__waiter3
    @waiter3.setter
    def waiter3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__waiter3", None)
        self.__waiter3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer2"):
                opp_val = getattr(old_value, "customer2", None)
                if opp_val == self:
                    setattr(old_value, "customer2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer2"):
                opp_val = getattr(value, "customer2", None)
                setattr(value, "customer2", self)



class Waiter:

    def __init__(self, Name: str, ID: str, Address: str, Contact: int, Personal_Information: str, manager0: "Manager" = None, customer2: "Customer" = None):
        self.Name = Name
        self.ID = ID
        self.Address = Address
        self.Contact = Contact
        self.Personal_Information = Personal_Information
        self.manager0 = manager0
        self.customer2 = customer2
        
        pass
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Contact(self):
        return self.__Contact
    @Contact.setter
    def Contact(self, Contact: int):
        self.__Contact = Contact

    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def Personal_Information(self):
        return self.__Personal_Information
    @Personal_Information.setter
    def Personal_Information(self, Personal_Information: str):
        self.__Personal_Information = Personal_Information

    @property
    def customer2(self):
        return self.__customer2
    @customer2.setter
    def customer2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Waiter__customer2", None)
        self.__customer2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "waiter3"):
                opp_val = getattr(old_value, "waiter3", None)
                if opp_val == self:
                    setattr(old_value, "waiter3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "waiter3"):
                opp_val = getattr(value, "waiter3", None)
                setattr(value, "waiter3", self)

    @property
    def manager0(self):
        return self.__manager0
    @manager0.setter
    def manager0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Waiter__manager0", None)
        self.__manager0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "waiter1"):
                opp_val = getattr(old_value, "waiter1", None)
                if opp_val == self:
                    setattr(old_value, "waiter1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "waiter1"):
                opp_val = getattr(value, "waiter1", None)
                setattr(value, "waiter1", self)

