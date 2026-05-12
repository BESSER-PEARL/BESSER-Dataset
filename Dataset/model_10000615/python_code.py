from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Client_Relationship_Team_Actor:

    pass


class Clent_Relationship_Team_Actor:

    pass


class Cient_Relationship_Team_Actor:

    pass


class Tenants_Buyer_Actor:

    pass


class Broker_Actor:

    pass


class Landlord_Actor:

    pass


class Meeting_With_the_Clent_UseCase:

    pass


class View_the_Buyers_List_UseCase:

    pass


class Sales_Team_Actor:

    pass


class Add_property_to_whishlist_UseCase:

    pass


class Liked_Property_UseCase:

    pass


class City_UseCase:

    pass


class Price_UseCase:

    pass


class State_UseCase:

    pass


class Search_Property_UseCase:

    pass


class Registration_UseCase:

    pass


class Username__Password_UseCase:

    pass


class Forgot_Password_UseCase:

    pass


class Login_UseCase:

    pass


class Buyer_Actor:

    pass





class Add_Property_Deatilas_external:

    pass


class Search_Property_external:

    pass


class Look_For_Tenants_external:

    pass


class Reacives_Lead_external:

    pass


class HH_Service_Selected_external:

    pass


class Property_Onboarding___Readiness_external:

    pass


class Look_For_Supply_external:

    pass


class Visit_Scheduled_external:

    pass


class Recieve_s_Lead_external:

    pass


class Create_Property_Mgmt_Lead_external:

    pass


class Assign_Lead_to_Client_Relationship_Team_external:

    pass


class Like_A_Property_external:

    pass


class Log_In_Interest_external:

    pass


class Select_Homzhub_Service_external:

    pass


class Assign_Transaction_Type_external:

    pass


class Add_Property_external:

    pass


class Register_external:

    pass


class Login_external:

    pass


class IndependentHouse:

    def __init__(self, Size: str, Bedroom: str, Bathroom: str, YardSpace: str, Price: str, property63: "Property" = None):
        self.Size = Size
        self.Bedroom = Bedroom
        self.Bathroom = Bathroom
        self.YardSpace = YardSpace
        self.Price = Price
        self.property63 = property63
        
        pass
    @property
    def Price(self):
        return self.__Price
    @Price.setter
    def Price(self, Price: str):
        self.__Price = Price

    @property
    def Bedroom(self):
        return self.__Bedroom
    @Bedroom.setter
    def Bedroom(self, Bedroom: str):
        self.__Bedroom = Bedroom

    @property
    def YardSpace(self):
        return self.__YardSpace
    @YardSpace.setter
    def YardSpace(self, YardSpace: str):
        self.__YardSpace = YardSpace

    @property
    def Bathroom(self):
        return self.__Bathroom
    @Bathroom.setter
    def Bathroom(self, Bathroom: str):
        self.__Bathroom = Bathroom

    @property
    def Size(self):
        return self.__Size
    @Size.setter
    def Size(self, Size: str):
        self.__Size = Size

    @property
    def property63(self):
        return self.__property63
    @property63.setter
    def property63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_IndependentHouse__property63", None)
        self.__property63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Property_IndependentHouse_062"):
                opp_val = getattr(old_value, "Property_IndependentHouse_062", None)
                if opp_val == self:
                    setattr(old_value, "Property_IndependentHouse_062", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Property_IndependentHouse_062"):
                opp_val = getattr(value, "Property_IndependentHouse_062", None)
                setattr(value, "Property_IndependentHouse_062", self)



class ResidentialApartment:

    def __init__(self, Size: str, BEDROOMS: str, PARKING: str, MAINTAINENCE: str, Price: str):
        self.Size = Size
        self.BEDROOMS = BEDROOMS
        self.PARKING = PARKING
        self.MAINTAINENCE = MAINTAINENCE
        self.Price = Price
        
        pass
    @property
    def Price(self):
        return self.__Price
    @Price.setter
    def Price(self, Price: str):
        self.__Price = Price

    @property
    def PARKING(self):
        return self.__PARKING
    @PARKING.setter
    def PARKING(self, PARKING: str):
        self.__PARKING = PARKING

    @property
    def MAINTAINENCE(self):
        return self.__MAINTAINENCE
    @MAINTAINENCE.setter
    def MAINTAINENCE(self, MAINTAINENCE: str):
        self.__MAINTAINENCE = MAINTAINENCE

    @property
    def BEDROOMS(self):
        return self.__BEDROOMS
    @BEDROOMS.setter
    def BEDROOMS(self, BEDROOMS: str):
        self.__BEDROOMS = BEDROOMS

    @property
    def Size(self):
        return self.__Size
    @Size.setter
    def Size(self, Size: str):
        self.__Size = Size



class Presales_team:

    def __init__(self, usename: str, password: str):
        self.usename = usename
        self.password = password
        
        pass
    @property
    def usename(self):
        return self.__usename
    @usename.setter
    def usename(self, usename: str):
        self.__usename = usename

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password



class Owner:

    def __init__(self, name: str, Address: str, property61: "Property" = None):
        self.name = name
        self.Address = Address
        self.property61 = property61
        
        pass
    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def property61(self):
        return self.__property61
    @property61.setter
    def property61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Owner__property61", None)
        self.__property61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner60"):
                opp_val = getattr(old_value, "owner60", None)
                if opp_val == self:
                    setattr(old_value, "owner60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner60"):
                opp_val = getattr(value, "owner60", None)
                setattr(value, "owner60", self)



class Client_Relationship_Team:

    def __init__(self, username: str, password: str, property59: "Property" = None):
        self.username = username
        self.password = password
        self.property59 = property59
        
        pass
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def property59(self):
        return self.__property59
    @property59.setter
    def property59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Client_Relationship_Team__property59", None)
        self.__property59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "client_Relationship_Team58"):
                opp_val = getattr(old_value, "client_Relationship_Team58", None)
                if opp_val == self:
                    setattr(old_value, "client_Relationship_Team58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "client_Relationship_Team58"):
                opp_val = getattr(value, "client_Relationship_Team58", None)
                setattr(value, "client_Relationship_Team58", self)



class User1:

    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password
        
        pass
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password



class Property1:

    def __init__(self, property_id: str, property_type: str, address: str, location: str):
        self.property_id = property_id
        self.property_type = property_type
        self.address = address
        self.location = location
        
        pass
    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def property_type(self):
        return self.__property_type
    @property_type.setter
    def property_type(self, property_type: str):
        self.__property_type = property_type

    @property
    def location(self):
        return self.__location
    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def property_id(self):
        return self.__property_id
    @property_id.setter
    def property_id(self, property_id: str):
        self.__property_id = property_id



class Client_Relationship_Team_Actor1:

    pass


class Property_Onbording__Component:

    pass


class Supply_Lead_Management_Client_Relationship_Team__Component:

    pass


class Clent_Realtionship_Team_Demand_Lead_Mgmt__Component:

    pass


class Demand_Component:

    pass


class Supplier_Component:

    pass


class Buyer_Component:

    pass


class Seller:

    def __init__(self, seller_id: str, property_id: str, property1: set["Property"] = None):
        self.seller_id = seller_id
        self.property_id = property_id
        self.property1 = property1 if property1 is not None else set()
        
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
    def property1(self):
        return self.__property1
    @property1.setter
    def property1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Seller__property1", None)
        self.__property1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "owner0"):
                    opp_val = getattr(item, "owner0", None)
                    
                    if opp_val == self:
                        setattr(item, "owner0", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "owner0"):
                    opp_val = getattr(item, "owner0", None)
                    
                    setattr(item, "owner0", self)
                    



class Buyer:

    def __init__(self, buyer_id: str, property3: set["Property"] = None):
        self.buyer_id = buyer_id
        self.property3 = property3 if property3 is not None else set()
        
        pass
    @property
    def buyer_id(self):
        return self.__buyer_id
    @buyer_id.setter
    def buyer_id(self, buyer_id: str):
        self.__buyer_id = buyer_id

    @property
    def property3(self):
        return self.__property3
    @property3.setter
    def property3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Buyer__property3", None)
        self.__property3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "user2"):
                    opp_val = getattr(item, "user2", None)
                    
                    if opp_val == self:
                        setattr(item, "user2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "user2"):
                    opp_val = getattr(item, "user2", None)
                    
                    setattr(item, "user2", self)
                    



class Rent:

    def __init__(self, rent_id: str):
        self.rent_id = rent_id
        
        pass
    @property
    def rent_id(self):
        return self.__rent_id
    @rent_id.setter
    def rent_id(self, rent_id: str):
        self.__rent_id = rent_id



class Unreg_User:

    pass


class Reg_User:

    def __init__(self, username: str, password: str, Address: str):
        self.username = username
        self.password = password
        self.Address = Address
        
        pass
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

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



class User:

    def __init__(self, email: str, location: str):
        self.email = email
        self.location = location
        
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



class Property:

    def __init__(self, property_id: str, property_type: str, address: str, location: str, owner0: "Seller" = None, user2: "Buyer" = None, client_Relationship_Team58: "Client_Relationship_Team" = None, owner60: "Owner" = None, Property_IndependentHouse_062: "IndependentHouse" = None):
        self.property_id = property_id
        self.property_type = property_type
        self.address = address
        self.location = location
        self.owner0 = owner0
        self.user2 = user2
        self.client_Relationship_Team58 = client_Relationship_Team58
        self.owner60 = owner60
        self.Property_IndependentHouse_062 = Property_IndependentHouse_062
        
        pass
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
    def location(self):
        return self.__location
    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def user2(self):
        return self.__user2
    @user2.setter
    def user2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Property__user2", None)
        self.__user2 = value
        
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
    def Property_IndependentHouse_062(self):
        return self.__Property_IndependentHouse_062
    @Property_IndependentHouse_062.setter
    def Property_IndependentHouse_062(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Property__Property_IndependentHouse_062", None)
        self.__Property_IndependentHouse_062 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "property63"):
                opp_val = getattr(old_value, "property63", None)
                if opp_val == self:
                    setattr(old_value, "property63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "property63"):
                opp_val = getattr(value, "property63", None)
                setattr(value, "property63", self)

    @property
    def client_Relationship_Team58(self):
        return self.__client_Relationship_Team58
    @client_Relationship_Team58.setter
    def client_Relationship_Team58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Property__client_Relationship_Team58", None)
        self.__client_Relationship_Team58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "property59"):
                opp_val = getattr(old_value, "property59", None)
                if opp_val == self:
                    setattr(old_value, "property59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "property59"):
                opp_val = getattr(value, "property59", None)
                setattr(value, "property59", self)

    @property
    def owner0(self):
        return self.__owner0
    @owner0.setter
    def owner0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Property__owner0", None)
        self.__owner0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "property1"):
                opp_val = getattr(old_value, "property1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "property1"):
                opp_val = getattr(value, "property1", None)
                if opp_val is None:
                    setattr(value, "property1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def owner60(self):
        return self.__owner60
    @owner60.setter
    def owner60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Property__owner60", None)
        self.__owner60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "property61"):
                opp_val = getattr(old_value, "property61", None)
                if opp_val == self:
                    setattr(old_value, "property61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "property61"):
                opp_val = getattr(value, "property61", None)
                setattr(value, "property61", self)

