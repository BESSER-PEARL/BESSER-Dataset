from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Request:

    def __init__(self, request_type: str, request_id: int, request_details: str, requser_id: str, user5: "User" = None):
        self.request_type = request_type
        self.request_id = request_id
        self.request_details = request_details
        self.requser_id = requser_id
        self.user5 = user5
        
        pass
    @property
    def request_id(self):
        return self.__request_id
    @request_id.setter
    def request_id(self, request_id: int):
        self.__request_id = request_id

    @property
    def request_details(self):
        return self.__request_details
    @request_details.setter
    def request_details(self, request_details: str):
        self.__request_details = request_details

    @property
    def requser_id(self):
        return self.__requser_id
    @requser_id.setter
    def requser_id(self, requser_id: str):
        self.__requser_id = requser_id

    @property
    def request_type(self):
        return self.__request_type
    @request_type.setter
    def request_type(self, request_type: str):
        self.__request_type = request_type

    @property
    def user5(self):
        return self.__user5
    @user5.setter
    def user5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Request__user5", None)
        self.__user5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "request4"):
                opp_val = getattr(old_value, "request4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "request4"):
                opp_val = getattr(value, "request4", None)
                if opp_val is None:
                    setattr(value, "request4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Requirement:

    def __init__(self, requirement_type: str, req_description: str, requirement_location: str, user_id: str, user9: set["Reg_User"] = None):
        self.requirement_type = requirement_type
        self.req_description = req_description
        self.requirement_location = requirement_location
        self.user_id = user_id
        self.user9 = user9 if user9 is not None else set()
        
        pass
    @property
    def requirement_type(self):
        return self.__requirement_type
    @requirement_type.setter
    def requirement_type(self, requirement_type: str):
        self.__requirement_type = requirement_type

    @property
    def requirement_location(self):
        return self.__requirement_location
    @requirement_location.setter
    def requirement_location(self, requirement_location: str):
        self.__requirement_location = requirement_location

    @property
    def req_description(self):
        return self.__req_description
    @req_description.setter
    def req_description(self, req_description: str):
        self.__req_description = req_description

    @property
    def user_id(self):
        return self.__user_id
    @user_id.setter
    def user_id(self, user_id: str):
        self.__user_id = user_id

    @property
    def user9(self):
        return self.__user9
    @user9.setter
    def user9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Requirement__user9", None)
        self.__user9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "requirement8"):
                    opp_val = getattr(item, "requirement8", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "requirement8"):
                    opp_val = getattr(item, "requirement8", None)
                    
                    if opp_val is None:
                        setattr(item, "requirement8", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



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
                    



class Seller:

    def __init__(self, seller_id: str, property_id: str, property3: set["Property"] = None):
        self.seller_id = seller_id
        self.property_id = property_id
        self.property3 = property3 if property3 is not None else set()
        
        pass
    @property
    def seller_id(self):
        return self.__seller_id
    @seller_id.setter
    def seller_id(self, seller_id: str):
        self.__seller_id = seller_id

    @property
    def property_id(self):
        return self.__property_id
    @property_id.setter
    def property_id(self, property_id: str):
        self.__property_id = property_id

    @property
    def property3(self):
        return self.__property3
    @property3.setter
    def property3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Seller__property3", None)
        self.__property3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "owner2"):
                    opp_val = getattr(item, "owner2", None)
                    
                    if opp_val == self:
                        setattr(item, "owner2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "owner2"):
                    opp_val = getattr(item, "owner2", None)
                    
                    setattr(item, "owner2", self)
                    



class Buyer:

    def __init__(self, buyer_id: str, property7: set["Property"] = None):
        self.buyer_id = buyer_id
        self.property7 = property7 if property7 is not None else set()
        
        pass
    @property
    def buyer_id(self):
        return self.__buyer_id
    @buyer_id.setter
    def buyer_id(self, buyer_id: str):
        self.__buyer_id = buyer_id

    @property
    def property7(self):
        return self.__property7
    @property7.setter
    def property7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Buyer__property7", None)
        self.__property7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "user6"):
                    opp_val = getattr(item, "user6", None)
                    
                    if opp_val == self:
                        setattr(item, "user6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "user6"):
                    opp_val = getattr(item, "user6", None)
                    
                    setattr(item, "user6", self)
                    



class Unreg_User:

    pass


class Reg_User:

    def __init__(self, username: str, password: str, Address: str, requirement8: set["Requirement"] = None):
        self.username = username
        self.password = password
        self.Address = Address
        self.requirement8 = requirement8 if requirement8 is not None else set()
        
        pass
    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def requirement8(self):
        return self.__requirement8
    @requirement8.setter
    def requirement8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Reg_User__requirement8", None)
        self.__requirement8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "user9"):
                    opp_val = getattr(item, "user9", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "user9"):
                    opp_val = getattr(item, "user9", None)
                    
                    if opp_val is None:
                        setattr(item, "user9", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class User:

    def __init__(self, email: str, location: str, administrator0: "Administrator" = None, request4: set["Request"] = None):
        self.email = email
        self.location = location
        self.administrator0 = administrator0
        self.request4 = request4 if request4 is not None else set()
        
        pass
    @property
    def location(self):
        return self.__location
    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

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

    @property
    def request4(self):
        return self.__request4
    @request4.setter
    def request4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__request4", None)
        self.__request4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "user5"):
                    opp_val = getattr(item, "user5", None)
                    
                    if opp_val == self:
                        setattr(item, "user5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "user5"):
                    opp_val = getattr(item, "user5", None)
                    
                    setattr(item, "user5", self)
                    



class Property:

    def __init__(self, property_id: str, property_type: str, address: str, location: str, owner2: "Seller" = None, user6: "Buyer" = None):
        self.property_id = property_id
        self.property_type = property_type
        self.address = address
        self.location = location
        self.owner2 = owner2
        self.user6 = user6
        
        pass
    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

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
    def property_id(self):
        return self.__property_id
    @property_id.setter
    def property_id(self, property_id: str):
        self.__property_id = property_id

    @property
    def user6(self):
        return self.__user6
    @user6.setter
    def user6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Property__user6", None)
        self.__user6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "property7"):
                opp_val = getattr(old_value, "property7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "property7"):
                opp_val = getattr(value, "property7", None)
                if opp_val is None:
                    setattr(value, "property7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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

