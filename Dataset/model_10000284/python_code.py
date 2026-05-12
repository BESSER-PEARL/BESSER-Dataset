from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class operation_or_contract:

    def __init__(self, operation_id: int, customer_id: str, owner_id: str, operation_type: str, Property_id: int, owner5: "owner" = None, property8: "Property" = None):
        self.operation_id = operation_id
        self.customer_id = customer_id
        self.owner_id = owner_id
        self.operation_type = operation_type
        self.Property_id = Property_id
        self.owner5 = owner5
        self.property8 = property8
        
        pass
    @property
    def operation_type(self):
        return self.__operation_type
    @operation_type.setter
    def operation_type(self, operation_type: str):
        self.__operation_type = operation_type

    @property
    def operation_id(self):
        return self.__operation_id
    @operation_id.setter
    def operation_id(self, operation_id: int):
        self.__operation_id = operation_id

    @property
    def Property_id(self):
        return self.__Property_id
    @Property_id.setter
    def Property_id(self, Property_id: int):
        self.__Property_id = Property_id

    @property
    def customer_id(self):
        return self.__customer_id
    @customer_id.setter
    def customer_id(self, customer_id: str):
        self.__customer_id = customer_id

    @property
    def owner_id(self):
        return self.__owner_id
    @owner_id.setter
    def owner_id(self, owner_id: str):
        self.__owner_id = owner_id

    @property
    def owner5(self):
        return self.__owner5
    @owner5.setter
    def owner5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operation_or_contract__owner5", None)
        self.__owner5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operation_or_contract4"):
                opp_val = getattr(old_value, "operation_or_contract4", None)
                if opp_val == self:
                    setattr(old_value, "operation_or_contract4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operation_or_contract4"):
                opp_val = getattr(value, "operation_or_contract4", None)
                setattr(value, "operation_or_contract4", self)

    @property
    def property8(self):
        return self.__property8
    @property8.setter
    def property8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operation_or_contract__property8", None)
        self.__property8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operation_or_contract9"):
                opp_val = getattr(old_value, "operation_or_contract9", None)
                if opp_val == self:
                    setattr(old_value, "operation_or_contract9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operation_or_contract9"):
                opp_val = getattr(value, "operation_or_contract9", None)
                setattr(value, "operation_or_contract9", self)



class Administrator:

    def __init__(self, admin_name: str, password: str, employee1: set["User"] = None):
        self.admin_name = admin_name
        self.password = password
        self.employee1 = employee1 if employee1 is not None else set()
        
        pass
    @property
    def admin_name(self):
        return self.__admin_name
    @admin_name.setter
    def admin_name(self, admin_name: str):
        self.__admin_name = admin_name

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def employee1(self):
        return self.__employee1
    @employee1.setter
    def employee1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Administrator__employee1", None)
        self.__employee1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "administrator0"):
                    opp_val = getattr(item, "administrator0", None)
                    
                    if opp_val == self:
                        setattr(item, "administrator0", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "administrator0"):
                    opp_val = getattr(item, "administrator0", None)
                    
                    setattr(item, "administrator0", self)
                    



class owner:

    pass


class customer:

    pass


class User:

    def __init__(self, Id: int, email: str, Address: str, phone: int, password: str, administrator0: "Administrator" = None):
        self.Id = Id
        self.email = email
        self.Address = Address
        self.phone = phone
        self.password = password
        self.administrator0 = administrator0
        
        pass
    @property
    def Id(self):
        return self.__Id
    @Id.setter
    def Id(self, Id: int):
        self.__Id = Id

    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, phone: int):
        self.__phone = phone

    @property
    def administrator0(self):
        return self.__administrator0
    @administrator0.setter
    def administrator0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__administrator0", None)
        self.__administrator0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee1"):
                opp_val = getattr(old_value, "employee1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee1"):
                opp_val = getattr(value, "employee1", None)
                if opp_val is None:
                    setattr(value, "employee1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Property:

    def __init__(self, property_id: str, property_type: str, address: str, location: str, size: str, Available: bool, owner2: "owner" = None, customer7: set["customer"] = None, operation_or_contract9: "operation_or_contract" = None):
        self.property_id = property_id
        self.property_type = property_type
        self.address = address
        self.location = location
        self.size = size
        self.Available = Available
        self.owner2 = owner2
        self.customer7 = customer7 if customer7 is not None else set()
        self.operation_or_contract9 = operation_or_contract9
        
        pass
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, size: str):
        self.__size = size

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def property_id(self):
        return self.__property_id
    @property_id.setter
    def property_id(self, property_id: str):
        self.__property_id = property_id

    @property
    def location(self):
        return self.__location
    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def property_type(self):
        return self.__property_type
    @property_type.setter
    def property_type(self, property_type: str):
        self.__property_type = property_type

    @property
    def Available(self):
        return self.__Available
    @Available.setter
    def Available(self, Available: bool):
        self.__Available = Available

    @property
    def owner2(self):
        return self.__owner2
    @owner2.setter
    def owner2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Property__owner2", None)
        self.__owner2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "property3"):
                opp_val = getattr(old_value, "property3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "property3"):
                opp_val = getattr(value, "property3", None)
                if opp_val is None:
                    setattr(value, "property3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def customer7(self):
        return self.__customer7
    @customer7.setter
    def customer7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Property__customer7", None)
        self.__customer7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "property6"):
                    opp_val = getattr(item, "property6", None)
                    
                    if opp_val == self:
                        setattr(item, "property6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "property6"):
                    opp_val = getattr(item, "property6", None)
                    
                    setattr(item, "property6", self)
                    

    @property
    def operation_or_contract9(self):
        return self.__operation_or_contract9
    @operation_or_contract9.setter
    def operation_or_contract9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Property__operation_or_contract9", None)
        self.__operation_or_contract9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "property8"):
                opp_val = getattr(old_value, "property8", None)
                if opp_val == self:
                    setattr(old_value, "property8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "property8"):
                opp_val = getattr(value, "property8", None)
                setattr(value, "property8", self)

