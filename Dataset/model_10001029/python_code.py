from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Buyer:

    def __init__(self, buyer_id: str, property9: set["Property"] = None):
        self.buyer_id = buyer_id
        self.property9 = property9 if property9 is not None else set()
        
        pass
    @property
    def buyer_id(self):
        return self.__buyer_id
    @buyer_id.setter
    def buyer_id(self, buyer_id: str):
        self.__buyer_id = buyer_id

    @property
    def property9(self):
        return self.__property9
    @property9.setter
    def property9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Buyer__property9", None)
        self.__property9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "buyer8"):
                    opp_val = getattr(item, "buyer8", None)
                    
                    if opp_val == self:
                        setattr(item, "buyer8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "buyer8"):
                    opp_val = getattr(item, "buyer8", None)
                    
                    setattr(item, "buyer8", self)
                    



class Advertiser:

    def __init__(self, advertiser_id: str, advertiesment_id: str, advertiesment2: set["Advertiesment"] = None):
        self.advertiser_id = advertiser_id
        self.advertiesment_id = advertiesment_id
        self.advertiesment2 = advertiesment2 if advertiesment2 is not None else set()
        
        pass
    @property
    def advertiser_id(self):
        return self.__advertiser_id
    @advertiser_id.setter
    def advertiser_id(self, advertiser_id: str):
        self.__advertiser_id = advertiser_id

    @property
    def advertiesment_id(self):
        return self.__advertiesment_id
    @advertiesment_id.setter
    def advertiesment_id(self, advertiesment_id: str):
        self.__advertiesment_id = advertiesment_id

    @property
    def advertiesment2(self):
        return self.__advertiesment2
    @advertiesment2.setter
    def advertiesment2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Advertiser__advertiesment2", None)
        self.__advertiesment2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "advertiser3"):
                    opp_val = getattr(item, "advertiser3", None)
                    
                    if opp_val == self:
                        setattr(item, "advertiser3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "advertiser3"):
                    opp_val = getattr(item, "advertiser3", None)
                    
                    setattr(item, "advertiser3", self)
                    



class Unreg_User:

    pass


class Reg_User:

    def __init__(self, username: str, password: str, Address: str, requirement10: set["Requirement"] = None, payment15: "Payment" = None):
        self.username = username
        self.password = password
        self.Address = Address
        self.requirement10 = requirement10 if requirement10 is not None else set()
        self.payment15 = payment15
        
        pass
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
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def requirement10(self):
        return self.__requirement10
    @requirement10.setter
    def requirement10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Reg_User__requirement10", None)
        self.__requirement10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "reg_User11"):
                    opp_val = getattr(item, "reg_User11", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "reg_User11"):
                    opp_val = getattr(item, "reg_User11", None)
                    
                    if opp_val is None:
                        setattr(item, "reg_User11", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def payment15(self):
        return self.__payment15
    @payment15.setter
    def payment15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Reg_User__payment15", None)
        self.__payment15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reg_User14"):
                opp_val = getattr(old_value, "reg_User14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reg_User14"):
                opp_val = getattr(value, "reg_User14", None)
                if opp_val is None:
                    setattr(value, "reg_User14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class User:

    def __init__(self, email: str, location: str, administrator0: "Administrator" = None, request6: set["Request"] = None):
        self.email = email
        self.location = location
        self.administrator0 = administrator0
        self.request6 = request6 if request6 is not None else set()
        
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
    def request6(self):
        return self.__request6
    @request6.setter
    def request6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__request6", None)
        self.__request6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "user7"):
                    opp_val = getattr(item, "user7", None)
                    
                    if opp_val == self:
                        setattr(item, "user7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "user7"):
                    opp_val = getattr(item, "user7", None)
                    
                    setattr(item, "user7", self)
                    

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

    def __init__(self, property_id: str, property_type: str, address: str, location: str, seller4: "Seller" = None, buyer8: "Buyer" = None, management12: set["Management"] = None, payment17: "Payment" = None):
        self.property_id = property_id
        self.property_type = property_type
        self.address = address
        self.location = location
        self.seller4 = seller4
        self.buyer8 = buyer8
        self.management12 = management12 if management12 is not None else set()
        self.payment17 = payment17
        
        pass
    @property
    def property_id(self):
        return self.__property_id
    @property_id.setter
    def property_id(self, property_id: str):
        self.__property_id = property_id

    @property
    def property_type(self):
        return self.__property_type
    @property_type.setter
    def property_type(self, property_type: str):
        self.__property_type = property_type

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
    def seller4(self):
        return self.__seller4
    @seller4.setter
    def seller4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Property__seller4", None)
        self.__seller4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "property5"):
                opp_val = getattr(old_value, "property5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "property5"):
                opp_val = getattr(value, "property5", None)
                if opp_val is None:
                    setattr(value, "property5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def buyer8(self):
        return self.__buyer8
    @buyer8.setter
    def buyer8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Property__buyer8", None)
        self.__buyer8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "property9"):
                opp_val = getattr(old_value, "property9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "property9"):
                opp_val = getattr(value, "property9", None)
                if opp_val is None:
                    setattr(value, "property9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def management12(self):
        return self.__management12
    @management12.setter
    def management12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Property__management12", None)
        self.__management12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "property13"):
                    opp_val = getattr(item, "property13", None)
                    
                    if opp_val == self:
                        setattr(item, "property13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "property13"):
                    opp_val = getattr(item, "property13", None)
                    
                    setattr(item, "property13", self)
                    

    @property
    def payment17(self):
        return self.__payment17
    @payment17.setter
    def payment17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Property__payment17", None)
        self.__payment17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "property16"):
                opp_val = getattr(old_value, "property16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "property16"):
                opp_val = getattr(value, "property16", None)
                if opp_val is None:
                    setattr(value, "property16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Advertiesment:

    def __init__(self, advertiesment_id: int, advertiser_id: str, start_date: str, end_date: str, advertiser3: "Advertiser" = None):
        self.advertiesment_id = advertiesment_id
        self.advertiser_id = advertiser_id
        self.start_date = start_date
        self.end_date = end_date
        self.advertiser3 = advertiser3
        
        pass
    @property
    def end_date(self):
        return self.__end_date
    @end_date.setter
    def end_date(self, end_date: str):
        self.__end_date = end_date

    @property
    def start_date(self):
        return self.__start_date
    @start_date.setter
    def start_date(self, start_date: str):
        self.__start_date = start_date

    @property
    def advertiesment_id(self):
        return self.__advertiesment_id
    @advertiesment_id.setter
    def advertiesment_id(self, advertiesment_id: int):
        self.__advertiesment_id = advertiesment_id

    @property
    def advertiser_id(self):
        return self.__advertiser_id
    @advertiser_id.setter
    def advertiser_id(self, advertiser_id: str):
        self.__advertiser_id = advertiser_id

    @property
    def advertiser3(self):
        return self.__advertiser3
    @advertiser3.setter
    def advertiser3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Advertiesment__advertiser3", None)
        self.__advertiser3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "advertiesment2"):
                opp_val = getattr(old_value, "advertiesment2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "advertiesment2"):
                opp_val = getattr(value, "advertiesment2", None)
                if opp_val is None:
                    setattr(value, "advertiesment2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Management:

    def __init__(self, specialoffers: str, suggetions: str, property13: "Property" = None):
        self.specialoffers = specialoffers
        self.suggetions = suggetions
        self.property13 = property13
        
        pass
    @property
    def suggetions(self):
        return self.__suggetions
    @suggetions.setter
    def suggetions(self, suggetions: str):
        self.__suggetions = suggetions

    @property
    def specialoffers(self):
        return self.__specialoffers
    @specialoffers.setter
    def specialoffers(self, specialoffers: str):
        self.__specialoffers = specialoffers

    @property
    def property13(self):
        return self.__property13
    @property13.setter
    def property13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Management__property13", None)
        self.__property13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "management12"):
                opp_val = getattr(old_value, "management12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "management12"):
                opp_val = getattr(value, "management12", None)
                if opp_val is None:
                    setattr(value, "management12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Request:

    def __init__(self, request_type: str, request_id: int, request_details: str, requser_id: str, user7: "User" = None):
        self.request_type = request_type
        self.request_id = request_id
        self.request_details = request_details
        self.requser_id = requser_id
        self.user7 = user7
        
        pass
    @property
    def request_type(self):
        return self.__request_type
    @request_type.setter
    def request_type(self, request_type: str):
        self.__request_type = request_type

    @property
    def request_id(self):
        return self.__request_id
    @request_id.setter
    def request_id(self, request_id: int):
        self.__request_id = request_id

    @property
    def requser_id(self):
        return self.__requser_id
    @requser_id.setter
    def requser_id(self, requser_id: str):
        self.__requser_id = requser_id

    @property
    def request_details(self):
        return self.__request_details
    @request_details.setter
    def request_details(self, request_details: str):
        self.__request_details = request_details

    @property
    def user7(self):
        return self.__user7
    @user7.setter
    def user7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Request__user7", None)
        self.__user7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "request6"):
                opp_val = getattr(old_value, "request6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "request6"):
                opp_val = getattr(value, "request6", None)
                if opp_val is None:
                    setattr(value, "request6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Requirement:

    def __init__(self, requirement_type: str, req_description: str, requirement_location: str, user_id: str, reg_User11: set["Reg_User"] = None):
        self.requirement_type = requirement_type
        self.req_description = req_description
        self.requirement_location = requirement_location
        self.user_id = user_id
        self.reg_User11 = reg_User11 if reg_User11 is not None else set()
        
        pass
    @property
    def requirement_location(self):
        return self.__requirement_location
    @requirement_location.setter
    def requirement_location(self, requirement_location: str):
        self.__requirement_location = requirement_location

    @property
    def requirement_type(self):
        return self.__requirement_type
    @requirement_type.setter
    def requirement_type(self, requirement_type: str):
        self.__requirement_type = requirement_type

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
    def reg_User11(self):
        return self.__reg_User11
    @reg_User11.setter
    def reg_User11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Requirement__reg_User11", None)
        self.__reg_User11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "requirement10"):
                    opp_val = getattr(item, "requirement10", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "requirement10"):
                    opp_val = getattr(item, "requirement10", None)
                    
                    if opp_val is None:
                        setattr(item, "requirement10", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Payment:

    def __init__(self, pay_id: int, pay_mode: str, card_no: str, ex_date: str, pay_amount: str, reg_User14: set["Reg_User"] = None, property16: set["Property"] = None):
        self.pay_id = pay_id
        self.pay_mode = pay_mode
        self.card_no = card_no
        self.ex_date = ex_date
        self.pay_amount = pay_amount
        self.reg_User14 = reg_User14 if reg_User14 is not None else set()
        self.property16 = property16 if property16 is not None else set()
        
        pass
    @property
    def pay_amount(self):
        return self.__pay_amount
    @pay_amount.setter
    def pay_amount(self, pay_amount: str):
        self.__pay_amount = pay_amount

    @property
    def pay_mode(self):
        return self.__pay_mode
    @pay_mode.setter
    def pay_mode(self, pay_mode: str):
        self.__pay_mode = pay_mode

    @property
    def pay_id(self):
        return self.__pay_id
    @pay_id.setter
    def pay_id(self, pay_id: int):
        self.__pay_id = pay_id

    @property
    def ex_date(self):
        return self.__ex_date
    @ex_date.setter
    def ex_date(self, ex_date: str):
        self.__ex_date = ex_date

    @property
    def card_no(self):
        return self.__card_no
    @card_no.setter
    def card_no(self, card_no: str):
        self.__card_no = card_no

    @property
    def reg_User14(self):
        return self.__reg_User14
    @reg_User14.setter
    def reg_User14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__reg_User14", None)
        self.__reg_User14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "payment15"):
                    opp_val = getattr(item, "payment15", None)
                    
                    if opp_val == self:
                        setattr(item, "payment15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "payment15"):
                    opp_val = getattr(item, "payment15", None)
                    
                    setattr(item, "payment15", self)
                    

    @property
    def property16(self):
        return self.__property16
    @property16.setter
    def property16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__property16", None)
        self.__property16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "payment17"):
                    opp_val = getattr(item, "payment17", None)
                    
                    if opp_val == self:
                        setattr(item, "payment17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "payment17"):
                    opp_val = getattr(item, "payment17", None)
                    
                    setattr(item, "payment17", self)
                    



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

    def __init__(self, seller_id: str, property_id: str, property5: set["Property"] = None):
        self.seller_id = seller_id
        self.property_id = property_id
        self.property5 = property5 if property5 is not None else set()
        
        pass
    @property
    def property_id(self):
        return self.__property_id
    @property_id.setter
    def property_id(self, property_id: str):
        self.__property_id = property_id

    @property
    def seller_id(self):
        return self.__seller_id
    @seller_id.setter
    def seller_id(self, seller_id: str):
        self.__seller_id = seller_id

    @property
    def property5(self):
        return self.__property5
    @property5.setter
    def property5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Seller__property5", None)
        self.__property5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "seller4"):
                    opp_val = getattr(item, "seller4", None)
                    
                    if opp_val == self:
                        setattr(item, "seller4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "seller4"):
                    opp_val = getattr(item, "seller4", None)
                    
                    setattr(item, "seller4", self)
                    

