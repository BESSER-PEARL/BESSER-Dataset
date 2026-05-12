from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Enumeration(Enum):
    pass
class Enumeration1(Enum):
    pass

############################################
# Definition of Classes
############################################







class list_of_outdated_components_UseCase:

    pass


class check_bank_account_for_payments_UseCase:

    pass


class owner_System_Actor:

    pass


class UseCase_UseCase:

    pass


class Generate_payment_cheque_employes_UseCase:

    pass


class create_invoice_UseCase:

    pass


class weekly_plan_dishes_UseCase:

    pass


class prepration_plan_dishes_UseCase:

    pass


class daily_weekly_monthly_plan_UseCase:

    pass


class order_missing_components_UseCase:

    pass


class add_constraints_UseCase:

    pass


class add_and_get_from_storage_check_storage_UseCase:

    pass


class Employee_Actor:

    pass


class chef_Actor:

    pass


class sign_up_login_logout_UseCase:

    pass


class payorder_UseCase:

    pass


class weekly_plan_of_each_cutomer_UseCase:

    pass


class order_catering_service_UseCase:

    pass


class select_from_menu_UseCase:

    pass


class customer_Actor:

    pass





class catering:

    pass


class owner__system:

    def __init__(self, attribute: str, component163: "Component" = None, component173: "Component" = None, component149: "Component" = None):
        self.attribute = attribute
        self.component163 = component163
        self.component173 = component173
        self.component149 = component149
        
        pass
    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def component149(self):
        return self.__component149
    @component149.setter
    def component149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_owner__system__component149", None)
        self.__component149 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner__system148"):
                opp_val = getattr(old_value, "owner__system148", None)
                if opp_val == self:
                    setattr(old_value, "owner__system148", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner__system148"):
                opp_val = getattr(value, "owner__system148", None)
                setattr(value, "owner__system148", self)

    @property
    def component173(self):
        return self.__component173
    @component173.setter
    def component173(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_owner__system__component173", None)
        self.__component173 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner__system172"):
                opp_val = getattr(old_value, "owner__system172", None)
                if opp_val == self:
                    setattr(old_value, "owner__system172", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner__system172"):
                opp_val = getattr(value, "owner__system172", None)
                setattr(value, "owner__system172", self)

    @property
    def component163(self):
        return self.__component163
    @component163.setter
    def component163(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_owner__system__component163", None)
        self.__component163 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner__system162"):
                opp_val = getattr(old_value, "owner__system162", None)
                if opp_val == self:
                    setattr(old_value, "owner__system162", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner__system162"):
                opp_val = getattr(value, "owner__system162", None)
                setattr(value, "owner__system162", self)



class account_type:

    def __init__(self, name: str, id: str, email: str, password: str, _attr: str):
        self.name = name
        self.id = id
        self.email = email
        self.password = password
        self._attr = _attr
        
        pass
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def _attr(self):
        return self.___attr
    @_attr.setter
    def _attr(self, _attr: str):
        self.___attr = _attr



class account_registration:

    pass


class Account_for_employee:

    def __init__(self, name: str, id: str, email: str, password: str, getaccount: str, attribute: str):
        self.name = name
        self.id = id
        self.email = email
        self.password = password
        self.getaccount = getaccount
        self.attribute = attribute
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def getaccount(self):
        return self.__getaccount
    @getaccount.setter
    def getaccount(self, getaccount: str):
        self.__getaccount = getaccount

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
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute



class Account1:

    def __init__(self, Name: str, id: str, email: str, password: str, _attr: str, attribute: str):
        self.Name = Name
        self.id = id
        self.email = email
        self.password = password
        self._attr = _attr
        self.attribute = attribute
        
        pass
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def _attr(self):
        return self.___attr
    @_attr.setter
    def _attr(self, _attr: str):
        self.___attr = _attr

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password



class Account:

    def __init__(self, Name: str, id: str, email: str, password: str, _attr: str, attribute: str):
        self.Name = Name
        self.id = id
        self.email = email
        self.password = password
        self._attr = _attr
        self.attribute = attribute
        
        pass
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def _attr(self):
        return self.___attr
    @_attr.setter
    def _attr(self, _attr: str):
        self.___attr = _attr

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute



class Owner2:

    pass


class Owner1:

    pass


class solid1:

    def __init__(self, name: str, weight__kg_: str, pieces: int, state: str):
        self.name = name
        self.weight__kg_ = weight__kg_
        self.pieces = pieces
        self.state = state
        
        pass
    @property
    def weight__kg_(self):
        return self.__weight__kg_
    @weight__kg_.setter
    def weight__kg_(self, weight__kg_: str):
        self.__weight__kg_ = weight__kg_

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def state(self):
        return self.__state
    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def pieces(self):
        return self.__pieces
    @pieces.setter
    def pieces(self, pieces: int):
        self.__pieces = pieces



class customer_account:

    pass


class shopping_cart:

    pass


class payment:

    def __init__(self, amount: str, _attr: str, total_amount: str, shopping_cart133: set["shopping_cart"] = None, shopping_cart171: "shopping_cart" = None):
        self.amount = amount
        self._attr = _attr
        self.total_amount = total_amount
        self.shopping_cart133 = shopping_cart133 if shopping_cart133 is not None else set()
        self.shopping_cart171 = shopping_cart171
        
        pass
    @property
    def total_amount(self):
        return self.__total_amount
    @total_amount.setter
    def total_amount(self, total_amount: str):
        self.__total_amount = total_amount

    @property
    def _attr(self):
        return self.___attr
    @_attr.setter
    def _attr(self, _attr: str):
        self.___attr = _attr

    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self, amount: str):
        self.__amount = amount

    @property
    def shopping_cart171(self):
        return self.__shopping_cart171
    @shopping_cart171.setter
    def shopping_cart171(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_payment__shopping_cart171", None)
        self.__shopping_cart171 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payment170"):
                opp_val = getattr(old_value, "payment170", None)
                if opp_val == self:
                    setattr(old_value, "payment170", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payment170"):
                opp_val = getattr(value, "payment170", None)
                setattr(value, "payment170", self)

    @property
    def shopping_cart133(self):
        return self.__shopping_cart133
    @shopping_cart133.setter
    def shopping_cart133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_payment__shopping_cart133", None)
        self.__shopping_cart133 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "payment132"):
                    opp_val = getattr(item, "payment132", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "payment132"):
                    opp_val = getattr(item, "payment132", None)
                    
                    if opp_val is None:
                        setattr(item, "payment132", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Csutomer:

    def __init__(self, id: str, email: str, password: str, tel_no: str, register: str, attribute: str, Adress: str, name: str, menu123: "menu" = None, order127: set["order"] = None, shopping_cart128: "shopping_cart" = None, catering174: "catering" = None):
        self.id = id
        self.email = email
        self.password = password
        self.tel_no = tel_no
        self.register = register
        self.attribute = attribute
        self.Adress = Adress
        self.name = name
        self.menu123 = menu123
        self.order127 = order127 if order127 is not None else set()
        self.shopping_cart128 = shopping_cart128
        self.catering174 = catering174
        
        pass
    @property
    def Adress(self):
        return self.__Adress
    @Adress.setter
    def Adress(self, Adress: str):
        self.__Adress = Adress

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def register(self):
        return self.__register
    @register.setter
    def register(self, register: str):
        self.__register = register

    @property
    def tel_no(self):
        return self.__tel_no
    @tel_no.setter
    def tel_no(self, tel_no: str):
        self.__tel_no = tel_no

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def shopping_cart128(self):
        return self.__shopping_cart128
    @shopping_cart128.setter
    def shopping_cart128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Csutomer__shopping_cart128", None)
        self.__shopping_cart128 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "csutomer129"):
                opp_val = getattr(old_value, "csutomer129", None)
                if opp_val == self:
                    setattr(old_value, "csutomer129", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "csutomer129"):
                opp_val = getattr(value, "csutomer129", None)
                setattr(value, "csutomer129", self)

    @property
    def catering174(self):
        return self.__catering174
    @catering174.setter
    def catering174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Csutomer__catering174", None)
        self.__catering174 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "csutomer175"):
                opp_val = getattr(old_value, "csutomer175", None)
                if opp_val == self:
                    setattr(old_value, "csutomer175", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "csutomer175"):
                opp_val = getattr(value, "csutomer175", None)
                setattr(value, "csutomer175", self)

    @property
    def order127(self):
        return self.__order127
    @order127.setter
    def order127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Csutomer__order127", None)
        self.__order127 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "csutomer126"):
                    opp_val = getattr(item, "csutomer126", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "csutomer126"):
                    opp_val = getattr(item, "csutomer126", None)
                    
                    if opp_val is None:
                        setattr(item, "csutomer126", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def menu123(self):
        return self.__menu123
    @menu123.setter
    def menu123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Csutomer__menu123", None)
        self.__menu123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "csutomer122"):
                opp_val = getattr(old_value, "csutomer122", None)
                if opp_val == self:
                    setattr(old_value, "csutomer122", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "csutomer122"):
                opp_val = getattr(value, "csutomer122", None)
                setattr(value, "csutomer122", self)



class events:

    def __init__(self, get_employee_name: str, duration: str, attribute: str, catering_location: str, planning135: "dayplan" = None, component140: "Component" = None, weekly_planning_of_dishes__by_waiter142: "events" = None, weekly_planning_of_dishes__by_waiter143: "events" = None, waiter144: "kitchen_worker" = None, food_dish160: "food_dish" = None, food_dish164: set["food_dish"] = None, weekly_planning_of_dishes__for__waiter178: set["Component"] = None, weekly_planning_of_dishes__for__waiter180: set["food_dish"] = None, order182: set["order"] = None, waiter146: set["kitchen_worker"] = None):
        self.get_employee_name = get_employee_name
        self.duration = duration
        self.attribute = attribute
        self.catering_location = catering_location
        self.planning135 = planning135
        self.component140 = component140
        self.weekly_planning_of_dishes__by_waiter142 = weekly_planning_of_dishes__by_waiter142
        self.weekly_planning_of_dishes__by_waiter143 = weekly_planning_of_dishes__by_waiter143
        self.waiter144 = waiter144
        self.food_dish160 = food_dish160
        self.food_dish164 = food_dish164 if food_dish164 is not None else set()
        self.weekly_planning_of_dishes__for__waiter178 = weekly_planning_of_dishes__for__waiter178 if weekly_planning_of_dishes__for__waiter178 is not None else set()
        self.weekly_planning_of_dishes__for__waiter180 = weekly_planning_of_dishes__for__waiter180 if weekly_planning_of_dishes__for__waiter180 is not None else set()
        self.order182 = order182 if order182 is not None else set()
        self.waiter146 = waiter146 if waiter146 is not None else set()
        
        pass
    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def get_employee_name(self):
        return self.__get_employee_name
    @get_employee_name.setter
    def get_employee_name(self, get_employee_name: str):
        self.__get_employee_name = get_employee_name

    @property
    def catering_location(self):
        return self.__catering_location
    @catering_location.setter
    def catering_location(self, catering_location: str):
        self.__catering_location = catering_location

    @property
    def duration(self):
        return self.__duration
    @duration.setter
    def duration(self, duration: str):
        self.__duration = duration

    @property
    def component140(self):
        return self.__component140
    @component140.setter
    def component140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_events__component140", None)
        self.__component140 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "weekly_planning_of_dishes__by_waiter141"):
                opp_val = getattr(old_value, "weekly_planning_of_dishes__by_waiter141", None)
                if opp_val == self:
                    setattr(old_value, "weekly_planning_of_dishes__by_waiter141", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "weekly_planning_of_dishes__by_waiter141"):
                opp_val = getattr(value, "weekly_planning_of_dishes__by_waiter141", None)
                setattr(value, "weekly_planning_of_dishes__by_waiter141", self)

    @property
    def weekly_planning_of_dishes__for__waiter178(self):
        return self.__weekly_planning_of_dishes__for__waiter178
    @weekly_planning_of_dishes__for__waiter178.setter
    def weekly_planning_of_dishes__for__waiter178(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_events__weekly_planning_of_dishes__for__waiter178", None)
        self.__weekly_planning_of_dishes__for__waiter178 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "component179"):
                    opp_val = getattr(item, "component179", None)
                    
                    if opp_val == self:
                        setattr(item, "component179", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "component179"):
                    opp_val = getattr(item, "component179", None)
                    
                    setattr(item, "component179", self)
                    

    @property
    def weekly_planning_of_dishes__by_waiter143(self):
        return self.__weekly_planning_of_dishes__by_waiter143
    @weekly_planning_of_dishes__by_waiter143.setter
    def weekly_planning_of_dishes__by_waiter143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_events__weekly_planning_of_dishes__by_waiter143", None)
        self.__weekly_planning_of_dishes__by_waiter143 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "weekly_planning_of_dishes__by_waiter142"):
                opp_val = getattr(old_value, "weekly_planning_of_dishes__by_waiter142", None)
                if opp_val == self:
                    setattr(old_value, "weekly_planning_of_dishes__by_waiter142", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "weekly_planning_of_dishes__by_waiter142"):
                opp_val = getattr(value, "weekly_planning_of_dishes__by_waiter142", None)
                setattr(value, "weekly_planning_of_dishes__by_waiter142", self)

    @property
    def weekly_planning_of_dishes__by_waiter142(self):
        return self.__weekly_planning_of_dishes__by_waiter142
    @weekly_planning_of_dishes__by_waiter142.setter
    def weekly_planning_of_dishes__by_waiter142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_events__weekly_planning_of_dishes__by_waiter142", None)
        self.__weekly_planning_of_dishes__by_waiter142 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "weekly_planning_of_dishes__by_waiter143"):
                opp_val = getattr(old_value, "weekly_planning_of_dishes__by_waiter143", None)
                if opp_val == self:
                    setattr(old_value, "weekly_planning_of_dishes__by_waiter143", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "weekly_planning_of_dishes__by_waiter143"):
                opp_val = getattr(value, "weekly_planning_of_dishes__by_waiter143", None)
                setattr(value, "weekly_planning_of_dishes__by_waiter143", self)

    @property
    def order182(self):
        return self.__order182
    @order182.setter
    def order182(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_events__order182", None)
        self.__order182 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "events183"):
                    opp_val = getattr(item, "events183", None)
                    
                    if opp_val == self:
                        setattr(item, "events183", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "events183"):
                    opp_val = getattr(item, "events183", None)
                    
                    setattr(item, "events183", self)
                    

    @property
    def weekly_planning_of_dishes__for__waiter180(self):
        return self.__weekly_planning_of_dishes__for__waiter180
    @weekly_planning_of_dishes__for__waiter180.setter
    def weekly_planning_of_dishes__for__waiter180(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_events__weekly_planning_of_dishes__for__waiter180", None)
        self.__weekly_planning_of_dishes__for__waiter180 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "food_dish181"):
                    opp_val = getattr(item, "food_dish181", None)
                    
                    if opp_val == self:
                        setattr(item, "food_dish181", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "food_dish181"):
                    opp_val = getattr(item, "food_dish181", None)
                    
                    setattr(item, "food_dish181", self)
                    

    @property
    def waiter144(self):
        return self.__waiter144
    @waiter144.setter
    def waiter144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_events__waiter144", None)
        self.__waiter144 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "weekly_planning_of_dishes__by_waiter145"):
                opp_val = getattr(old_value, "weekly_planning_of_dishes__by_waiter145", None)
                if opp_val == self:
                    setattr(old_value, "weekly_planning_of_dishes__by_waiter145", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "weekly_planning_of_dishes__by_waiter145"):
                opp_val = getattr(value, "weekly_planning_of_dishes__by_waiter145", None)
                setattr(value, "weekly_planning_of_dishes__by_waiter145", self)

    @property
    def planning135(self):
        return self.__planning135
    @planning135.setter
    def planning135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_events__planning135", None)
        self.__planning135 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "weekly_planning_of_dishes__by_waiter134"):
                opp_val = getattr(old_value, "weekly_planning_of_dishes__by_waiter134", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "weekly_planning_of_dishes__by_waiter134"):
                opp_val = getattr(value, "weekly_planning_of_dishes__by_waiter134", None)
                if opp_val is None:
                    setattr(value, "weekly_planning_of_dishes__by_waiter134", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def food_dish160(self):
        return self.__food_dish160
    @food_dish160.setter
    def food_dish160(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_events__food_dish160", None)
        self.__food_dish160 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "weekly_planning_of_dishes__by_waiter161"):
                opp_val = getattr(old_value, "weekly_planning_of_dishes__by_waiter161", None)
                if opp_val == self:
                    setattr(old_value, "weekly_planning_of_dishes__by_waiter161", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "weekly_planning_of_dishes__by_waiter161"):
                opp_val = getattr(value, "weekly_planning_of_dishes__by_waiter161", None)
                setattr(value, "weekly_planning_of_dishes__by_waiter161", self)

    @property
    def food_dish164(self):
        return self.__food_dish164
    @food_dish164.setter
    def food_dish164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_events__food_dish164", None)
        self.__food_dish164 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "weekly_planning_of_dishes__for__waiter165"):
                    opp_val = getattr(item, "weekly_planning_of_dishes__for__waiter165", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "weekly_planning_of_dishes__for__waiter165"):
                    opp_val = getattr(item, "weekly_planning_of_dishes__for__waiter165", None)
                    
                    if opp_val is None:
                        setattr(item, "weekly_planning_of_dishes__for__waiter165", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def waiter146(self):
        return self.__waiter146
    @waiter146.setter
    def waiter146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_events__waiter146", None)
        self.__waiter146 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "weekly_planning_of_dishes__by_waiter147"):
                    opp_val = getattr(item, "weekly_planning_of_dishes__by_waiter147", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "weekly_planning_of_dishes__by_waiter147"):
                    opp_val = getattr(item, "weekly_planning_of_dishes__by_waiter147", None)
                    
                    if opp_val is None:
                        setattr(item, "weekly_planning_of_dishes__by_waiter147", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class solid:

    def __init__(self, must_be_unit_in_kg: str, component109: "Component" = None):
        self.must_be_unit_in_kg = must_be_unit_in_kg
        self.component109 = component109
        
        pass
    @property
    def must_be_unit_in_kg(self):
        return self.__must_be_unit_in_kg
    @must_be_unit_in_kg.setter
    def must_be_unit_in_kg(self, must_be_unit_in_kg: str):
        self.__must_be_unit_in_kg = must_be_unit_in_kg

    @property
    def component109(self):
        return self.__component109
    @component109.setter
    def component109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_solid__component109", None)
        self.__component109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "solid108"):
                opp_val = getattr(old_value, "solid108", None)
                if opp_val == self:
                    setattr(old_value, "solid108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "solid108"):
                opp_val = getattr(value, "solid108", None)
                setattr(value, "solid108", self)



class liquid:

    def __init__(self, must_be_unit_in_ml: str, name: str, quantiy: str, component111: "Component" = None):
        self.must_be_unit_in_ml = must_be_unit_in_ml
        self.name = name
        self.quantiy = quantiy
        self.component111 = component111
        
        pass
    @property
    def must_be_unit_in_ml(self):
        return self.__must_be_unit_in_ml
    @must_be_unit_in_ml.setter
    def must_be_unit_in_ml(self, must_be_unit_in_ml: str):
        self.__must_be_unit_in_ml = must_be_unit_in_ml

    @property
    def quantiy(self):
        return self.__quantiy
    @quantiy.setter
    def quantiy(self, quantiy: str):
        self.__quantiy = quantiy

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def component111(self):
        return self.__component111
    @component111.setter
    def component111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_liquid__component111", None)
        self.__component111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "liquid110"):
                opp_val = getattr(old_value, "liquid110", None)
                if opp_val == self:
                    setattr(old_value, "liquid110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "liquid110"):
                opp_val = getattr(value, "liquid110", None)
                setattr(value, "liquid110", self)



class drink:

    def __init__(self, type: str, component116: "Component" = None, menu121: "menu" = None):
        self.type = type
        self.component116 = component116
        self.menu121 = menu121
        
        pass
    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def component116(self):
        return self.__component116
    @component116.setter
    def component116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drink__component116", None)
        self.__component116 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drink117"):
                opp_val = getattr(old_value, "drink117", None)
                if opp_val == self:
                    setattr(old_value, "drink117", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drink117"):
                opp_val = getattr(value, "drink117", None)
                setattr(value, "drink117", self)

    @property
    def menu121(self):
        return self.__menu121
    @menu121.setter
    def menu121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drink__menu121", None)
        self.__menu121 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drink120"):
                opp_val = getattr(old_value, "drink120", None)
                if opp_val == self:
                    setattr(old_value, "drink120", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drink120"):
                opp_val = getattr(value, "drink120", None)
                setattr(value, "drink120", self)



class chef2:

    pass


class kitchen_worker:

    pass


class dayplan:

    def __init__(self, Monday: str, tuesday: str, wenesday: str, thursday: str, friday: str, saturday: str, sunday: str, plan_per_date: str, weekly_planning_of_dishes__by_waiter134: set["events"] = None, chef136: "chef2" = None, chef151: "chef2" = None):
        self.Monday = Monday
        self.tuesday = tuesday
        self.wenesday = wenesday
        self.thursday = thursday
        self.friday = friday
        self.saturday = saturday
        self.sunday = sunday
        self.plan_per_date = plan_per_date
        self.weekly_planning_of_dishes__by_waiter134 = weekly_planning_of_dishes__by_waiter134 if weekly_planning_of_dishes__by_waiter134 is not None else set()
        self.chef136 = chef136
        self.chef151 = chef151
        
        pass
    @property
    def tuesday(self):
        return self.__tuesday
    @tuesday.setter
    def tuesday(self, tuesday: str):
        self.__tuesday = tuesday

    @property
    def Monday(self):
        return self.__Monday
    @Monday.setter
    def Monday(self, Monday: str):
        self.__Monday = Monday

    @property
    def thursday(self):
        return self.__thursday
    @thursday.setter
    def thursday(self, thursday: str):
        self.__thursday = thursday

    @property
    def wenesday(self):
        return self.__wenesday
    @wenesday.setter
    def wenesday(self, wenesday: str):
        self.__wenesday = wenesday

    @property
    def saturday(self):
        return self.__saturday
    @saturday.setter
    def saturday(self, saturday: str):
        self.__saturday = saturday

    @property
    def plan_per_date(self):
        return self.__plan_per_date
    @plan_per_date.setter
    def plan_per_date(self, plan_per_date: str):
        self.__plan_per_date = plan_per_date

    @property
    def sunday(self):
        return self.__sunday
    @sunday.setter
    def sunday(self, sunday: str):
        self.__sunday = sunday

    @property
    def friday(self):
        return self.__friday
    @friday.setter
    def friday(self, friday: str):
        self.__friday = friday

    @property
    def weekly_planning_of_dishes__by_waiter134(self):
        return self.__weekly_planning_of_dishes__by_waiter134
    @weekly_planning_of_dishes__by_waiter134.setter
    def weekly_planning_of_dishes__by_waiter134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dayplan__weekly_planning_of_dishes__by_waiter134", None)
        self.__weekly_planning_of_dishes__by_waiter134 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "planning135"):
                    opp_val = getattr(item, "planning135", None)
                    
                    if opp_val == self:
                        setattr(item, "planning135", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "planning135"):
                    opp_val = getattr(item, "planning135", None)
                    
                    setattr(item, "planning135", self)
                    

    @property
    def chef151(self):
        return self.__chef151
    @chef151.setter
    def chef151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dayplan__chef151", None)
        self.__chef151 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "planning150"):
                opp_val = getattr(old_value, "planning150", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "planning150"):
                opp_val = getattr(value, "planning150", None)
                if opp_val is None:
                    setattr(value, "planning150", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def chef136(self):
        return self.__chef136
    @chef136.setter
    def chef136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dayplan__chef136", None)
        self.__chef136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "planning137"):
                opp_val = getattr(old_value, "planning137", None)
                if opp_val == self:
                    setattr(old_value, "planning137", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "planning137"):
                opp_val = getattr(value, "planning137", None)
                setattr(value, "planning137", self)



class order:

    def __init__(self, order_id: str, ordered_item: str, status: str, _attr: str, date: str, menu125: "menu" = None, csutomer126: set["Csutomer"] = None, shopping_cart130: "shopping_cart" = None, shopping_cart158: set["shopping_cart"] = None, events183: "events" = None, menu169: set["menu"] = None):
        self.order_id = order_id
        self.ordered_item = ordered_item
        self.status = status
        self._attr = _attr
        self.date = date
        self.menu125 = menu125
        self.csutomer126 = csutomer126 if csutomer126 is not None else set()
        self.shopping_cart130 = shopping_cart130
        self.shopping_cart158 = shopping_cart158 if shopping_cart158 is not None else set()
        self.events183 = events183
        self.menu169 = menu169 if menu169 is not None else set()
        
        pass
    @property
    def order_id(self):
        return self.__order_id
    @order_id.setter
    def order_id(self, order_id: str):
        self.__order_id = order_id

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def _attr(self):
        return self.___attr
    @_attr.setter
    def _attr(self, _attr: str):
        self.___attr = _attr

    @property
    def ordered_item(self):
        return self.__ordered_item
    @ordered_item.setter
    def ordered_item(self, ordered_item: str):
        self.__ordered_item = ordered_item

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def menu125(self):
        return self.__menu125
    @menu125.setter
    def menu125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_order__menu125", None)
        self.__menu125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order124"):
                opp_val = getattr(old_value, "order124", None)
                if opp_val == self:
                    setattr(old_value, "order124", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order124"):
                opp_val = getattr(value, "order124", None)
                setattr(value, "order124", self)

    @property
    def shopping_cart130(self):
        return self.__shopping_cart130
    @shopping_cart130.setter
    def shopping_cart130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_order__shopping_cart130", None)
        self.__shopping_cart130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order131"):
                opp_val = getattr(old_value, "order131", None)
                if opp_val == self:
                    setattr(old_value, "order131", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order131"):
                opp_val = getattr(value, "order131", None)
                setattr(value, "order131", self)

    @property
    def shopping_cart158(self):
        return self.__shopping_cart158
    @shopping_cart158.setter
    def shopping_cart158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_order__shopping_cart158", None)
        self.__shopping_cart158 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "order159"):
                    opp_val = getattr(item, "order159", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "order159"):
                    opp_val = getattr(item, "order159", None)
                    
                    if opp_val is None:
                        setattr(item, "order159", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def events183(self):
        return self.__events183
    @events183.setter
    def events183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_order__events183", None)
        self.__events183 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order182"):
                opp_val = getattr(old_value, "order182", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order182"):
                opp_val = getattr(value, "order182", None)
                if opp_val is None:
                    setattr(value, "order182", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def csutomer126(self):
        return self.__csutomer126
    @csutomer126.setter
    def csutomer126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_order__csutomer126", None)
        self.__csutomer126 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "order127"):
                    opp_val = getattr(item, "order127", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "order127"):
                    opp_val = getattr(item, "order127", None)
                    
                    if opp_val is None:
                        setattr(item, "order127", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def menu169(self):
        return self.__menu169
    @menu169.setter
    def menu169(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_order__menu169", None)
        self.__menu169 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "order168"):
                    opp_val = getattr(item, "order168", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "order168"):
                    opp_val = getattr(item, "order168", None)
                    
                    if opp_val is None:
                        setattr(item, "order168", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class food_dish:

    def __init__(self, type: str, attribute: str, attribute2: str, component112: "Component" = None, component114: "Component" = None, menu119: "menu" = None, weekly_planning_of_dishes__by_waiter161: "events" = None, weekly_planning_of_dishes__for__waiter165: set["events"] = None, food_dish181: "events" = None, food_dish152: set["Component"] = None, food_dish157: set["menu"] = None):
        self.type = type
        self.attribute = attribute
        self.attribute2 = attribute2
        self.component112 = component112
        self.component114 = component114
        self.menu119 = menu119
        self.weekly_planning_of_dishes__by_waiter161 = weekly_planning_of_dishes__by_waiter161
        self.weekly_planning_of_dishes__for__waiter165 = weekly_planning_of_dishes__for__waiter165 if weekly_planning_of_dishes__for__waiter165 is not None else set()
        self.food_dish181 = food_dish181
        self.food_dish152 = food_dish152 if food_dish152 is not None else set()
        self.food_dish157 = food_dish157 if food_dish157 is not None else set()
        
        pass
    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def attribute2(self):
        return self.__attribute2
    @attribute2.setter
    def attribute2(self, attribute2: str):
        self.__attribute2 = attribute2

    @property
    def weekly_planning_of_dishes__for__waiter165(self):
        return self.__weekly_planning_of_dishes__for__waiter165
    @weekly_planning_of_dishes__for__waiter165.setter
    def weekly_planning_of_dishes__for__waiter165(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_food_dish__weekly_planning_of_dishes__for__waiter165", None)
        self.__weekly_planning_of_dishes__for__waiter165 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "food_dish164"):
                    opp_val = getattr(item, "food_dish164", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "food_dish164"):
                    opp_val = getattr(item, "food_dish164", None)
                    
                    if opp_val is None:
                        setattr(item, "food_dish164", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def food_dish152(self):
        return self.__food_dish152
    @food_dish152.setter
    def food_dish152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_food_dish__food_dish152", None)
        self.__food_dish152 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "component153"):
                    opp_val = getattr(item, "component153", None)
                    
                    if opp_val == self:
                        setattr(item, "component153", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "component153"):
                    opp_val = getattr(item, "component153", None)
                    
                    setattr(item, "component153", self)
                    

    @property
    def food_dish181(self):
        return self.__food_dish181
    @food_dish181.setter
    def food_dish181(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_food_dish__food_dish181", None)
        self.__food_dish181 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "weekly_planning_of_dishes__for__waiter180"):
                opp_val = getattr(old_value, "weekly_planning_of_dishes__for__waiter180", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "weekly_planning_of_dishes__for__waiter180"):
                opp_val = getattr(value, "weekly_planning_of_dishes__for__waiter180", None)
                if opp_val is None:
                    setattr(value, "weekly_planning_of_dishes__for__waiter180", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def component114(self):
        return self.__component114
    @component114.setter
    def component114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_food_dish__component114", None)
        self.__component114 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "food_dish115"):
                opp_val = getattr(old_value, "food_dish115", None)
                if opp_val == self:
                    setattr(old_value, "food_dish115", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "food_dish115"):
                opp_val = getattr(value, "food_dish115", None)
                setattr(value, "food_dish115", self)

    @property
    def component112(self):
        return self.__component112
    @component112.setter
    def component112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_food_dish__component112", None)
        self.__component112 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "food_dish113"):
                opp_val = getattr(old_value, "food_dish113", None)
                if opp_val == self:
                    setattr(old_value, "food_dish113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "food_dish113"):
                opp_val = getattr(value, "food_dish113", None)
                setattr(value, "food_dish113", self)

    @property
    def food_dish157(self):
        return self.__food_dish157
    @food_dish157.setter
    def food_dish157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_food_dish__food_dish157", None)
        self.__food_dish157 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "menu156"):
                    opp_val = getattr(item, "menu156", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "menu156"):
                    opp_val = getattr(item, "menu156", None)
                    
                    if opp_val is None:
                        setattr(item, "menu156", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def weekly_planning_of_dishes__by_waiter161(self):
        return self.__weekly_planning_of_dishes__by_waiter161
    @weekly_planning_of_dishes__by_waiter161.setter
    def weekly_planning_of_dishes__by_waiter161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_food_dish__weekly_planning_of_dishes__by_waiter161", None)
        self.__weekly_planning_of_dishes__by_waiter161 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "food_dish160"):
                opp_val = getattr(old_value, "food_dish160", None)
                if opp_val == self:
                    setattr(old_value, "food_dish160", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "food_dish160"):
                opp_val = getattr(value, "food_dish160", None)
                setattr(value, "food_dish160", self)

    @property
    def menu119(self):
        return self.__menu119
    @menu119.setter
    def menu119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_food_dish__menu119", None)
        self.__menu119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "food_dish118"):
                opp_val = getattr(old_value, "food_dish118", None)
                if opp_val == self:
                    setattr(old_value, "food_dish118", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "food_dish118"):
                opp_val = getattr(value, "food_dish118", None)
                setattr(value, "food_dish118", self)



class menu:

    def __init__(self, dishname: str, price: str, dish_quantity: str, attribute: str, drinkname: str, food_dish118: "food_dish" = None, drink120: "drink" = None, csutomer122: "Csutomer" = None, order124: "order" = None, catering176: "catering" = None, drink154: "Component" = None, menu156: set["food_dish"] = None, order168: set["order"] = None):
        self.dishname = dishname
        self.price = price
        self.dish_quantity = dish_quantity
        self.attribute = attribute
        self.drinkname = drinkname
        self.food_dish118 = food_dish118
        self.drink120 = drink120
        self.csutomer122 = csutomer122
        self.order124 = order124
        self.catering176 = catering176
        self.drink154 = drink154
        self.menu156 = menu156 if menu156 is not None else set()
        self.order168 = order168 if order168 is not None else set()
        
        pass
    @property
    def drinkname(self):
        return self.__drinkname
    @drinkname.setter
    def drinkname(self, drinkname: str):
        self.__drinkname = drinkname

    @property
    def dish_quantity(self):
        return self.__dish_quantity
    @dish_quantity.setter
    def dish_quantity(self, dish_quantity: str):
        self.__dish_quantity = dish_quantity

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: str):
        self.__price = price

    @property
    def dishname(self):
        return self.__dishname
    @dishname.setter
    def dishname(self, dishname: str):
        self.__dishname = dishname

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def menu156(self):
        return self.__menu156
    @menu156.setter
    def menu156(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_menu__menu156", None)
        self.__menu156 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "food_dish157"):
                    opp_val = getattr(item, "food_dish157", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "food_dish157"):
                    opp_val = getattr(item, "food_dish157", None)
                    
                    if opp_val is None:
                        setattr(item, "food_dish157", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def catering176(self):
        return self.__catering176
    @catering176.setter
    def catering176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_menu__catering176", None)
        self.__catering176 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "menu177"):
                opp_val = getattr(old_value, "menu177", None)
                if opp_val == self:
                    setattr(old_value, "menu177", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "menu177"):
                opp_val = getattr(value, "menu177", None)
                setattr(value, "menu177", self)

    @property
    def order168(self):
        return self.__order168
    @order168.setter
    def order168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_menu__order168", None)
        self.__order168 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "menu169"):
                    opp_val = getattr(item, "menu169", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "menu169"):
                    opp_val = getattr(item, "menu169", None)
                    
                    if opp_val is None:
                        setattr(item, "menu169", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def drink154(self):
        return self.__drink154
    @drink154.setter
    def drink154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_menu__drink154", None)
        self.__drink154 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "component155"):
                opp_val = getattr(old_value, "component155", None)
                if opp_val == self:
                    setattr(old_value, "component155", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "component155"):
                opp_val = getattr(value, "component155", None)
                setattr(value, "component155", self)

    @property
    def drink120(self):
        return self.__drink120
    @drink120.setter
    def drink120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_menu__drink120", None)
        self.__drink120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "menu121"):
                opp_val = getattr(old_value, "menu121", None)
                if opp_val == self:
                    setattr(old_value, "menu121", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "menu121"):
                opp_val = getattr(value, "menu121", None)
                setattr(value, "menu121", self)

    @property
    def food_dish118(self):
        return self.__food_dish118
    @food_dish118.setter
    def food_dish118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_menu__food_dish118", None)
        self.__food_dish118 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "menu119"):
                opp_val = getattr(old_value, "menu119", None)
                if opp_val == self:
                    setattr(old_value, "menu119", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "menu119"):
                opp_val = getattr(value, "menu119", None)
                setattr(value, "menu119", self)

    @property
    def order124(self):
        return self.__order124
    @order124.setter
    def order124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_menu__order124", None)
        self.__order124 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "menu125"):
                opp_val = getattr(old_value, "menu125", None)
                if opp_val == self:
                    setattr(old_value, "menu125", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "menu125"):
                opp_val = getattr(value, "menu125", None)
                setattr(value, "menu125", self)

    @property
    def csutomer122(self):
        return self.__csutomer122
    @csutomer122.setter
    def csutomer122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_menu__csutomer122", None)
        self.__csutomer122 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "menu123"):
                opp_val = getattr(old_value, "menu123", None)
                if opp_val == self:
                    setattr(old_value, "menu123", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "menu123"):
                opp_val = getattr(value, "menu123", None)
                setattr(value, "menu123", self)



class Component(ABC):

    def __init__(self, ID: str, Name: str, Type: str, Storage_or_sehlf: str, Expiry_date: str, attribute: str, solid108: "solid" = None, liquid110: "liquid" = None, food_dish113: "food_dish" = None, food_dish115: "food_dish" = None, drink117: "drink" = None, waiter138: set["kitchen_worker"] = None, weekly_planning_of_dishes__by_waiter141: "events" = None, owner__system162: "owner__system" = None, owner__system172: "owner__system" = None, component179: "events" = None, owner__system148: "owner__system" = None, component153: "food_dish" = None, component155: "menu" = None):
        self.ID = ID
        self.Name = Name
        self.Type = Type
        self.Storage_or_sehlf = Storage_or_sehlf
        self.Expiry_date = Expiry_date
        self.attribute = attribute
        self.solid108 = solid108
        self.liquid110 = liquid110
        self.food_dish113 = food_dish113
        self.food_dish115 = food_dish115
        self.drink117 = drink117
        self.waiter138 = waiter138 if waiter138 is not None else set()
        self.weekly_planning_of_dishes__by_waiter141 = weekly_planning_of_dishes__by_waiter141
        self.owner__system162 = owner__system162
        self.owner__system172 = owner__system172
        self.component179 = component179
        self.owner__system148 = owner__system148
        self.component153 = component153
        self.component155 = component155
        
        pass
    @property
    def Type(self):
        return self.__Type
    @Type.setter
    def Type(self, Type: str):
        self.__Type = Type

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Expiry_date(self):
        return self.__Expiry_date
    @Expiry_date.setter
    def Expiry_date(self, Expiry_date: str):
        self.__Expiry_date = Expiry_date

    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def Storage_or_sehlf(self):
        return self.__Storage_or_sehlf
    @Storage_or_sehlf.setter
    def Storage_or_sehlf(self, Storage_or_sehlf: str):
        self.__Storage_or_sehlf = Storage_or_sehlf

    @property
    def waiter138(self):
        return self.__waiter138
    @waiter138.setter
    def waiter138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Component__waiter138", None)
        self.__waiter138 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "component139"):
                    opp_val = getattr(item, "component139", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "component139"):
                    opp_val = getattr(item, "component139", None)
                    
                    if opp_val is None:
                        setattr(item, "component139", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def component155(self):
        return self.__component155
    @component155.setter
    def component155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Component__component155", None)
        self.__component155 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drink154"):
                opp_val = getattr(old_value, "drink154", None)
                if opp_val == self:
                    setattr(old_value, "drink154", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drink154"):
                opp_val = getattr(value, "drink154", None)
                setattr(value, "drink154", self)

    @property
    def component153(self):
        return self.__component153
    @component153.setter
    def component153(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Component__component153", None)
        self.__component153 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "food_dish152"):
                opp_val = getattr(old_value, "food_dish152", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "food_dish152"):
                opp_val = getattr(value, "food_dish152", None)
                if opp_val is None:
                    setattr(value, "food_dish152", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def liquid110(self):
        return self.__liquid110
    @liquid110.setter
    def liquid110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Component__liquid110", None)
        self.__liquid110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "component111"):
                opp_val = getattr(old_value, "component111", None)
                if opp_val == self:
                    setattr(old_value, "component111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "component111"):
                opp_val = getattr(value, "component111", None)
                setattr(value, "component111", self)

    @property
    def drink117(self):
        return self.__drink117
    @drink117.setter
    def drink117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Component__drink117", None)
        self.__drink117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "component116"):
                opp_val = getattr(old_value, "component116", None)
                if opp_val == self:
                    setattr(old_value, "component116", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "component116"):
                opp_val = getattr(value, "component116", None)
                setattr(value, "component116", self)

    @property
    def food_dish113(self):
        return self.__food_dish113
    @food_dish113.setter
    def food_dish113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Component__food_dish113", None)
        self.__food_dish113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "component112"):
                opp_val = getattr(old_value, "component112", None)
                if opp_val == self:
                    setattr(old_value, "component112", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "component112"):
                opp_val = getattr(value, "component112", None)
                setattr(value, "component112", self)

    @property
    def owner__system162(self):
        return self.__owner__system162
    @owner__system162.setter
    def owner__system162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Component__owner__system162", None)
        self.__owner__system162 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "component163"):
                opp_val = getattr(old_value, "component163", None)
                if opp_val == self:
                    setattr(old_value, "component163", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "component163"):
                opp_val = getattr(value, "component163", None)
                setattr(value, "component163", self)

    @property
    def food_dish115(self):
        return self.__food_dish115
    @food_dish115.setter
    def food_dish115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Component__food_dish115", None)
        self.__food_dish115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "component114"):
                opp_val = getattr(old_value, "component114", None)
                if opp_val == self:
                    setattr(old_value, "component114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "component114"):
                opp_val = getattr(value, "component114", None)
                setattr(value, "component114", self)

    @property
    def owner__system172(self):
        return self.__owner__system172
    @owner__system172.setter
    def owner__system172(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Component__owner__system172", None)
        self.__owner__system172 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "component173"):
                opp_val = getattr(old_value, "component173", None)
                if opp_val == self:
                    setattr(old_value, "component173", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "component173"):
                opp_val = getattr(value, "component173", None)
                setattr(value, "component173", self)

    @property
    def owner__system148(self):
        return self.__owner__system148
    @owner__system148.setter
    def owner__system148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Component__owner__system148", None)
        self.__owner__system148 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "component149"):
                opp_val = getattr(old_value, "component149", None)
                if opp_val == self:
                    setattr(old_value, "component149", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "component149"):
                opp_val = getattr(value, "component149", None)
                setattr(value, "component149", self)

    @property
    def component179(self):
        return self.__component179
    @component179.setter
    def component179(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Component__component179", None)
        self.__component179 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "weekly_planning_of_dishes__for__waiter178"):
                opp_val = getattr(old_value, "weekly_planning_of_dishes__for__waiter178", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "weekly_planning_of_dishes__for__waiter178"):
                opp_val = getattr(value, "weekly_planning_of_dishes__for__waiter178", None)
                if opp_val is None:
                    setattr(value, "weekly_planning_of_dishes__for__waiter178", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def weekly_planning_of_dishes__by_waiter141(self):
        return self.__weekly_planning_of_dishes__by_waiter141
    @weekly_planning_of_dishes__by_waiter141.setter
    def weekly_planning_of_dishes__by_waiter141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Component__weekly_planning_of_dishes__by_waiter141", None)
        self.__weekly_planning_of_dishes__by_waiter141 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "component140"):
                opp_val = getattr(old_value, "component140", None)
                if opp_val == self:
                    setattr(old_value, "component140", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "component140"):
                opp_val = getattr(value, "component140", None)
                setattr(value, "component140", self)

    @property
    def solid108(self):
        return self.__solid108
    @solid108.setter
    def solid108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Component__solid108", None)
        self.__solid108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "component109"):
                opp_val = getattr(old_value, "component109", None)
                if opp_val == self:
                    setattr(old_value, "component109", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "component109"):
                opp_val = getattr(value, "component109", None)
                setattr(value, "component109", self)



class Chef:

    pass


class Owner:

    pass


class Waiter:

    pass


class Employee1:

    def __init__(self, ID: str, Name: str, Email: str, Password: str, attribute: str):
        self.ID = ID
        self.Name = Name
        self.Email = Email
        self.Password = Password
        self.attribute = attribute
        
        pass
    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email



class Dish:

    def __init__(self, _attr: str, menu104: "Menu1" = None, menu107: set["Menu1"] = None):
        self._attr = _attr
        self.menu104 = menu104
        self.menu107 = menu107 if menu107 is not None else set()
        
        pass
    @property
    def _attr(self):
        return self.___attr
    @_attr.setter
    def _attr(self, _attr: str):
        self.___attr = _attr

    @property
    def menu107(self):
        return self.__menu107
    @menu107.setter
    def menu107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Dish__menu107", None)
        self.__menu107 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dish106"):
                    opp_val = getattr(item, "dish106", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dish106"):
                    opp_val = getattr(item, "dish106", None)
                    
                    if opp_val is None:
                        setattr(item, "dish106", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def menu104(self):
        return self.__menu104
    @menu104.setter
    def menu104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Dish__menu104", None)
        self.__menu104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dish105"):
                opp_val = getattr(old_value, "dish105", None)
                if opp_val == self:
                    setattr(old_value, "dish105", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dish105"):
                opp_val = getattr(value, "dish105", None)
                setattr(value, "dish105", self)



class bank_account:

    pass


class Web_master:

    pass


class Shopping_cart1:

    def __init__(self, Dishname: str, price: int, Quantity: int, time: str, attribute: str, menu54: "Menu1" = None, menu95: "Menu1" = None):
        self.Dishname = Dishname
        self.price = price
        self.Quantity = Quantity
        self.time = time
        self.attribute = attribute
        self.menu54 = menu54
        self.menu95 = menu95
        
        pass
    @property
    def time(self):
        return self.__time
    @time.setter
    def time(self, time: str):
        self.__time = time

    @property
    def Quantity(self):
        return self.__Quantity
    @Quantity.setter
    def Quantity(self, Quantity: int):
        self.__Quantity = Quantity

    @property
    def Dishname(self):
        return self.__Dishname
    @Dishname.setter
    def Dishname(self, Dishname: str):
        self.__Dishname = Dishname

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: int):
        self.__price = price

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def menu54(self):
        return self.__menu54
    @menu54.setter
    def menu54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Shopping_cart1__menu54", None)
        self.__menu54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shopping_cart55"):
                opp_val = getattr(old_value, "shopping_cart55", None)
                if opp_val == self:
                    setattr(old_value, "shopping_cart55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shopping_cart55"):
                opp_val = getattr(value, "shopping_cart55", None)
                setattr(value, "shopping_cart55", self)

    @property
    def menu95(self):
        return self.__menu95
    @menu95.setter
    def menu95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Shopping_cart1__menu95", None)
        self.__menu95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shopping_cart94"):
                opp_val = getattr(old_value, "shopping_cart94", None)
                if opp_val == self:
                    setattr(old_value, "shopping_cart94", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shopping_cart94"):
                opp_val = getattr(value, "shopping_cart94", None)
                setattr(value, "shopping_cart94", self)



class Order1:

    def __init__(self, OrderID: int, Customerid: int, Dishname: str, attribute: str, date: str, customer52: "Customer1" = None, payment56: "Payment1" = None, customer93: "Customer1" = None):
        self.OrderID = OrderID
        self.Customerid = Customerid
        self.Dishname = Dishname
        self.attribute = attribute
        self.date = date
        self.customer52 = customer52
        self.payment56 = payment56
        self.customer93 = customer93
        
        pass
    @property
    def Customerid(self):
        return self.__Customerid
    @Customerid.setter
    def Customerid(self, Customerid: int):
        self.__Customerid = Customerid

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def OrderID(self):
        return self.__OrderID
    @OrderID.setter
    def OrderID(self, OrderID: int):
        self.__OrderID = OrderID

    @property
    def Dishname(self):
        return self.__Dishname
    @Dishname.setter
    def Dishname(self, Dishname: str):
        self.__Dishname = Dishname

    @property
    def customer52(self):
        return self.__customer52
    @customer52.setter
    def customer52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order1__customer52", None)
        self.__customer52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order53"):
                opp_val = getattr(old_value, "order53", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order53"):
                opp_val = getattr(value, "order53", None)
                if opp_val is None:
                    setattr(value, "order53", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def payment56(self):
        return self.__payment56
    @payment56.setter
    def payment56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order1__payment56", None)
        self.__payment56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order57"):
                opp_val = getattr(old_value, "order57", None)
                if opp_val == self:
                    setattr(old_value, "order57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order57"):
                opp_val = getattr(value, "order57", None)
                setattr(value, "order57", self)

    @property
    def customer93(self):
        return self.__customer93
    @customer93.setter
    def customer93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order1__customer93", None)
        self.__customer93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order92"):
                opp_val = getattr(old_value, "order92", None)
                if opp_val == self:
                    setattr(old_value, "order92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order92"):
                opp_val = getattr(value, "order92", None)
                setattr(value, "order92", self)



class contact:

    def __init__(self, Name: str, Adress: str, Email: str, Tel: int, attribute: str, web_master63: "Web_master" = None, system73: "System1" = None):
        self.Name = Name
        self.Adress = Adress
        self.Email = Email
        self.Tel = Tel
        self.attribute = attribute
        self.web_master63 = web_master63
        self.system73 = system73
        
        pass
    @property
    def Tel(self):
        return self.__Tel
    @Tel.setter
    def Tel(self, Tel: int):
        self.__Tel = Tel

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

    @property
    def Adress(self):
        return self.__Adress
    @Adress.setter
    def Adress(self, Adress: str):
        self.__Adress = Adress

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def web_master63(self):
        return self.__web_master63
    @web_master63.setter
    def web_master63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contact__web_master63", None)
        self.__web_master63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contact62"):
                opp_val = getattr(old_value, "contact62", None)
                if opp_val == self:
                    setattr(old_value, "contact62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contact62"):
                opp_val = getattr(value, "contact62", None)
                setattr(value, "contact62", self)

    @property
    def system73(self):
        return self.__system73
    @system73.setter
    def system73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contact__system73", None)
        self.__system73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contact72"):
                opp_val = getattr(old_value, "contact72", None)
                if opp_val == self:
                    setattr(old_value, "contact72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contact72"):
                opp_val = getattr(value, "contact72", None)
                setattr(value, "contact72", self)



class help:

    pass


class Plan1:

    def __init__(self, weekly_plan: str, Monthly_plan: str, day_plan: str, chef46: set["chef1"] = None, customer88: "Customer1" = None, kitchen_worker90: set["Kitchen_worker"] = None):
        self.weekly_plan = weekly_plan
        self.Monthly_plan = Monthly_plan
        self.day_plan = day_plan
        self.chef46 = chef46 if chef46 is not None else set()
        self.customer88 = customer88
        self.kitchen_worker90 = kitchen_worker90 if kitchen_worker90 is not None else set()
        
        pass
    @property
    def weekly_plan(self):
        return self.__weekly_plan
    @weekly_plan.setter
    def weekly_plan(self, weekly_plan: str):
        self.__weekly_plan = weekly_plan

    @property
    def Monthly_plan(self):
        return self.__Monthly_plan
    @Monthly_plan.setter
    def Monthly_plan(self, Monthly_plan: str):
        self.__Monthly_plan = Monthly_plan

    @property
    def day_plan(self):
        return self.__day_plan
    @day_plan.setter
    def day_plan(self, day_plan: str):
        self.__day_plan = day_plan

    @property
    def chef46(self):
        return self.__chef46
    @chef46.setter
    def chef46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Plan1__chef46", None)
        self.__chef46 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "plan47"):
                    opp_val = getattr(item, "plan47", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "plan47"):
                    opp_val = getattr(item, "plan47", None)
                    
                    if opp_val is None:
                        setattr(item, "plan47", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def kitchen_worker90(self):
        return self.__kitchen_worker90
    @kitchen_worker90.setter
    def kitchen_worker90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Plan1__kitchen_worker90", None)
        self.__kitchen_worker90 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "plan91"):
                    opp_val = getattr(item, "plan91", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "plan91"):
                    opp_val = getattr(item, "plan91", None)
                    
                    if opp_val is None:
                        setattr(item, "plan91", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def customer88(self):
        return self.__customer88
    @customer88.setter
    def customer88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Plan1__customer88", None)
        self.__customer88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "plan89"):
                opp_val = getattr(old_value, "plan89", None)
                if opp_val == self:
                    setattr(old_value, "plan89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "plan89"):
                opp_val = getattr(value, "plan89", None)
                setattr(value, "plan89", self)



class System1:

    def __init__(self, WebAdmin_or_owner: str, Email: str, Password: str, bank_account68: "bank_account" = None, bank_account70: "bank_account" = None, contact72: "contact" = None, help74: "help" = None, storage86: "Storage1" = None):
        self.WebAdmin_or_owner = WebAdmin_or_owner
        self.Email = Email
        self.Password = Password
        self.bank_account68 = bank_account68
        self.bank_account70 = bank_account70
        self.contact72 = contact72
        self.help74 = help74
        self.storage86 = storage86
        
        pass
    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def WebAdmin_or_owner(self):
        return self.__WebAdmin_or_owner
    @WebAdmin_or_owner.setter
    def WebAdmin_or_owner(self, WebAdmin_or_owner: str):
        self.__WebAdmin_or_owner = WebAdmin_or_owner

    @property
    def storage86(self):
        return self.__storage86
    @storage86.setter
    def storage86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_System1__storage86", None)
        self.__storage86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "system87"):
                opp_val = getattr(old_value, "system87", None)
                if opp_val == self:
                    setattr(old_value, "system87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "system87"):
                opp_val = getattr(value, "system87", None)
                setattr(value, "system87", self)

    @property
    def bank_account68(self):
        return self.__bank_account68
    @bank_account68.setter
    def bank_account68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_System1__bank_account68", None)
        self.__bank_account68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "system69"):
                opp_val = getattr(old_value, "system69", None)
                if opp_val == self:
                    setattr(old_value, "system69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "system69"):
                opp_val = getattr(value, "system69", None)
                setattr(value, "system69", self)

    @property
    def contact72(self):
        return self.__contact72
    @contact72.setter
    def contact72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_System1__contact72", None)
        self.__contact72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "system73"):
                opp_val = getattr(old_value, "system73", None)
                if opp_val == self:
                    setattr(old_value, "system73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "system73"):
                opp_val = getattr(value, "system73", None)
                setattr(value, "system73", self)

    @property
    def bank_account70(self):
        return self.__bank_account70
    @bank_account70.setter
    def bank_account70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_System1__bank_account70", None)
        self.__bank_account70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "system71"):
                opp_val = getattr(old_value, "system71", None)
                if opp_val == self:
                    setattr(old_value, "system71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "system71"):
                opp_val = getattr(value, "system71", None)
                setattr(value, "system71", self)

    @property
    def help74(self):
        return self.__help74
    @help74.setter
    def help74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_System1__help74", None)
        self.__help74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "system75"):
                opp_val = getattr(old_value, "system75", None)
                if opp_val == self:
                    setattr(old_value, "system75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "system75"):
                opp_val = getattr(value, "system75", None)
                setattr(value, "system75", self)



class Storage1:

    def __init__(self, Component_id: int, Component_Name: str, Employee45: set["Kitchen_worker"] = None, system87: "System1" = None, kitchen_worker96: set["Kitchen_worker"] = None, chef64: set["chef1"] = None):
        self.Component_id = Component_id
        self.Component_Name = Component_Name
        self.Employee45 = Employee45 if Employee45 is not None else set()
        self.system87 = system87
        self.kitchen_worker96 = kitchen_worker96 if kitchen_worker96 is not None else set()
        self.chef64 = chef64 if chef64 is not None else set()
        
        pass
    @property
    def Component_id(self):
        return self.__Component_id
    @Component_id.setter
    def Component_id(self, Component_id: int):
        self.__Component_id = Component_id

    @property
    def Component_Name(self):
        return self.__Component_Name
    @Component_Name.setter
    def Component_Name(self, Component_Name: str):
        self.__Component_Name = Component_Name

    @property
    def Employee45(self):
        return self.__Employee45
    @Employee45.setter
    def Employee45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Storage1__Employee45", None)
        self.__Employee45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "storage44"):
                    opp_val = getattr(item, "storage44", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "storage44"):
                    opp_val = getattr(item, "storage44", None)
                    
                    if opp_val is None:
                        setattr(item, "storage44", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def chef64(self):
        return self.__chef64
    @chef64.setter
    def chef64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Storage1__chef64", None)
        self.__chef64 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "storage65"):
                    opp_val = getattr(item, "storage65", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "storage65"):
                    opp_val = getattr(item, "storage65", None)
                    
                    if opp_val is None:
                        setattr(item, "storage65", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def kitchen_worker96(self):
        return self.__kitchen_worker96
    @kitchen_worker96.setter
    def kitchen_worker96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Storage1__kitchen_worker96", None)
        self.__kitchen_worker96 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "storage97"):
                    opp_val = getattr(item, "storage97", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "storage97"):
                    opp_val = getattr(item, "storage97", None)
                    
                    if opp_val is None:
                        setattr(item, "storage97", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def system87(self):
        return self.__system87
    @system87.setter
    def system87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Storage1__system87", None)
        self.__system87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "storage86"):
                opp_val = getattr(old_value, "storage86", None)
                if opp_val == self:
                    setattr(old_value, "storage86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "storage86"):
                opp_val = getattr(value, "storage86", None)
                setattr(value, "storage86", self)



class Kitchen_worker:

    def __init__(self, ID: int, Name: str, Email: str, password: str, attribute: str, accounnt41: "Accounnt1" = None, storage44: set["Storage1"] = None, plan91: set["Plan1"] = None, storage97: set["Storage1"] = None):
        self.ID = ID
        self.Name = Name
        self.Email = Email
        self.password = password
        self.attribute = attribute
        self.accounnt41 = accounnt41
        self.storage44 = storage44 if storage44 is not None else set()
        self.plan91 = plan91 if plan91 is not None else set()
        self.storage97 = storage97 if storage97 is not None else set()
        
        pass
    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def plan91(self):
        return self.__plan91
    @plan91.setter
    def plan91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Kitchen_worker__plan91", None)
        self.__plan91 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "kitchen_worker90"):
                    opp_val = getattr(item, "kitchen_worker90", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "kitchen_worker90"):
                    opp_val = getattr(item, "kitchen_worker90", None)
                    
                    if opp_val is None:
                        setattr(item, "kitchen_worker90", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def storage44(self):
        return self.__storage44
    @storage44.setter
    def storage44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Kitchen_worker__storage44", None)
        self.__storage44 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Employee45"):
                    opp_val = getattr(item, "Employee45", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Employee45"):
                    opp_val = getattr(item, "Employee45", None)
                    
                    if opp_val is None:
                        setattr(item, "Employee45", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def accounnt41(self):
        return self.__accounnt41
    @accounnt41.setter
    def accounnt41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Kitchen_worker__accounnt41", None)
        self.__accounnt41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee40"):
                opp_val = getattr(old_value, "employee40", None)
                if opp_val == self:
                    setattr(old_value, "employee40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee40"):
                opp_val = getattr(value, "employee40", None)
                setattr(value, "employee40", self)

    @property
    def storage97(self):
        return self.__storage97
    @storage97.setter
    def storage97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Kitchen_worker__storage97", None)
        self.__storage97 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "kitchen_worker96"):
                    opp_val = getattr(item, "kitchen_worker96", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "kitchen_worker96"):
                    opp_val = getattr(item, "kitchen_worker96", None)
                    
                    if opp_val is None:
                        setattr(item, "kitchen_worker96", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class PrintRecipts1:

    def __init__(self, PaymentID: str, CustomerID: int, Amount: str, Dishname: str, Quantity: int, time: str, date: str, payment59: "Payment1" = None):
        self.PaymentID = PaymentID
        self.CustomerID = CustomerID
        self.Amount = Amount
        self.Dishname = Dishname
        self.Quantity = Quantity
        self.time = time
        self.date = date
        self.payment59 = payment59
        
        pass
    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def CustomerID(self):
        return self.__CustomerID
    @CustomerID.setter
    def CustomerID(self, CustomerID: int):
        self.__CustomerID = CustomerID

    @property
    def Dishname(self):
        return self.__Dishname
    @Dishname.setter
    def Dishname(self, Dishname: str):
        self.__Dishname = Dishname

    @property
    def time(self):
        return self.__time
    @time.setter
    def time(self, time: str):
        self.__time = time

    @property
    def Amount(self):
        return self.__Amount
    @Amount.setter
    def Amount(self, Amount: str):
        self.__Amount = Amount

    @property
    def PaymentID(self):
        return self.__PaymentID
    @PaymentID.setter
    def PaymentID(self, PaymentID: str):
        self.__PaymentID = PaymentID

    @property
    def Quantity(self):
        return self.__Quantity
    @Quantity.setter
    def Quantity(self, Quantity: int):
        self.__Quantity = Quantity

    @property
    def payment59(self):
        return self.__payment59
    @payment59.setter
    def payment59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PrintRecipts1__payment59", None)
        self.__payment59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "printRecipts58"):
                opp_val = getattr(old_value, "printRecipts58", None)
                if opp_val == self:
                    setattr(old_value, "printRecipts58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "printRecipts58"):
                opp_val = getattr(value, "printRecipts58", None)
                setattr(value, "printRecipts58", self)



class Payment1:

    def __init__(self, PaymentID: int, Amount: str, OrderID: int, CustomerID: int, date: str, time: str, order57: "Order1" = None, printRecipts58: "PrintRecipts1" = None, bank_account66: "bank_account" = None):
        self.PaymentID = PaymentID
        self.Amount = Amount
        self.OrderID = OrderID
        self.CustomerID = CustomerID
        self.date = date
        self.time = time
        self.order57 = order57
        self.printRecipts58 = printRecipts58
        self.bank_account66 = bank_account66
        
        pass
    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def OrderID(self):
        return self.__OrderID
    @OrderID.setter
    def OrderID(self, OrderID: int):
        self.__OrderID = OrderID

    @property
    def time(self):
        return self.__time
    @time.setter
    def time(self, time: str):
        self.__time = time

    @property
    def PaymentID(self):
        return self.__PaymentID
    @PaymentID.setter
    def PaymentID(self, PaymentID: int):
        self.__PaymentID = PaymentID

    @property
    def CustomerID(self):
        return self.__CustomerID
    @CustomerID.setter
    def CustomerID(self, CustomerID: int):
        self.__CustomerID = CustomerID

    @property
    def Amount(self):
        return self.__Amount
    @Amount.setter
    def Amount(self, Amount: str):
        self.__Amount = Amount

    @property
    def printRecipts58(self):
        return self.__printRecipts58
    @printRecipts58.setter
    def printRecipts58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment1__printRecipts58", None)
        self.__printRecipts58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payment59"):
                opp_val = getattr(old_value, "payment59", None)
                if opp_val == self:
                    setattr(old_value, "payment59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payment59"):
                opp_val = getattr(value, "payment59", None)
                setattr(value, "payment59", self)

    @property
    def bank_account66(self):
        return self.__bank_account66
    @bank_account66.setter
    def bank_account66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment1__bank_account66", None)
        self.__bank_account66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payment67"):
                opp_val = getattr(old_value, "payment67", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payment67"):
                opp_val = getattr(value, "payment67", None)
                if opp_val is None:
                    setattr(value, "payment67", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def order57(self):
        return self.__order57
    @order57.setter
    def order57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment1__order57", None)
        self.__order57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payment56"):
                opp_val = getattr(old_value, "payment56", None)
                if opp_val == self:
                    setattr(old_value, "payment56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payment56"):
                opp_val = getattr(value, "payment56", None)
                setattr(value, "payment56", self)



class Accounnt1:

    def __init__(self, Email: str, password: str, Accounttype: str, customer37: "Customer1" = None, chef39: "chef1" = None, employee40: "Kitchen_worker" = None, chef100: "chef1" = None, customer103: "Customer1" = None, customer98: "Customer1" = None):
        self.Email = Email
        self.password = password
        self.Accounttype = Accounttype
        self.customer37 = customer37
        self.chef39 = chef39
        self.employee40 = employee40
        self.chef100 = chef100
        self.customer103 = customer103
        self.customer98 = customer98
        
        pass
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

    @property
    def Accounttype(self):
        return self.__Accounttype
    @Accounttype.setter
    def Accounttype(self, Accounttype: str):
        self.__Accounttype = Accounttype

    @property
    def customer37(self):
        return self.__customer37
    @customer37.setter
    def customer37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Accounnt1__customer37", None)
        self.__customer37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "accounnt36"):
                opp_val = getattr(old_value, "accounnt36", None)
                if opp_val == self:
                    setattr(old_value, "accounnt36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "accounnt36"):
                opp_val = getattr(value, "accounnt36", None)
                setattr(value, "accounnt36", self)

    @property
    def customer98(self):
        return self.__customer98
    @customer98.setter
    def customer98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Accounnt1__customer98", None)
        self.__customer98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "accounnt99"):
                opp_val = getattr(old_value, "accounnt99", None)
                if opp_val == self:
                    setattr(old_value, "accounnt99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "accounnt99"):
                opp_val = getattr(value, "accounnt99", None)
                setattr(value, "accounnt99", self)

    @property
    def employee40(self):
        return self.__employee40
    @employee40.setter
    def employee40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Accounnt1__employee40", None)
        self.__employee40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "accounnt41"):
                opp_val = getattr(old_value, "accounnt41", None)
                if opp_val == self:
                    setattr(old_value, "accounnt41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "accounnt41"):
                opp_val = getattr(value, "accounnt41", None)
                setattr(value, "accounnt41", self)

    @property
    def chef39(self):
        return self.__chef39
    @chef39.setter
    def chef39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Accounnt1__chef39", None)
        self.__chef39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "accounnt38"):
                opp_val = getattr(old_value, "accounnt38", None)
                if opp_val == self:
                    setattr(old_value, "accounnt38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "accounnt38"):
                opp_val = getattr(value, "accounnt38", None)
                setattr(value, "accounnt38", self)

    @property
    def chef100(self):
        return self.__chef100
    @chef100.setter
    def chef100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Accounnt1__chef100", None)
        self.__chef100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "accounnt101"):
                opp_val = getattr(old_value, "accounnt101", None)
                if opp_val == self:
                    setattr(old_value, "accounnt101", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "accounnt101"):
                opp_val = getattr(value, "accounnt101", None)
                setattr(value, "accounnt101", self)

    @property
    def customer103(self):
        return self.__customer103
    @customer103.setter
    def customer103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Accounnt1__customer103", None)
        self.__customer103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "accounnt102"):
                opp_val = getattr(old_value, "accounnt102", None)
                if opp_val == self:
                    setattr(old_value, "accounnt102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "accounnt102"):
                opp_val = getattr(value, "accounnt102", None)
                setattr(value, "accounnt102", self)



class chef1:

    def __init__(self, Name: str, Employee_ID: int, Email: str, passowrd: str, Room_no: int, accounnt38: "Accounnt1" = None, plan47: set["Plan1"] = None, accounnt101: "Accounnt1" = None, storage65: set["Storage1"] = None):
        self.Name = Name
        self.Employee_ID = Employee_ID
        self.Email = Email
        self.passowrd = passowrd
        self.Room_no = Room_no
        self.accounnt38 = accounnt38
        self.plan47 = plan47 if plan47 is not None else set()
        self.accounnt101 = accounnt101
        self.storage65 = storage65 if storage65 is not None else set()
        
        pass
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Room_no(self):
        return self.__Room_no
    @Room_no.setter
    def Room_no(self, Room_no: int):
        self.__Room_no = Room_no

    @property
    def passowrd(self):
        return self.__passowrd
    @passowrd.setter
    def passowrd(self, passowrd: str):
        self.__passowrd = passowrd

    @property
    def Employee_ID(self):
        return self.__Employee_ID
    @Employee_ID.setter
    def Employee_ID(self, Employee_ID: int):
        self.__Employee_ID = Employee_ID

    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

    @property
    def plan47(self):
        return self.__plan47
    @plan47.setter
    def plan47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_chef1__plan47", None)
        self.__plan47 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "chef46"):
                    opp_val = getattr(item, "chef46", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "chef46"):
                    opp_val = getattr(item, "chef46", None)
                    
                    if opp_val is None:
                        setattr(item, "chef46", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def accounnt38(self):
        return self.__accounnt38
    @accounnt38.setter
    def accounnt38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_chef1__accounnt38", None)
        self.__accounnt38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "chef39"):
                opp_val = getattr(old_value, "chef39", None)
                if opp_val == self:
                    setattr(old_value, "chef39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "chef39"):
                opp_val = getattr(value, "chef39", None)
                setattr(value, "chef39", self)

    @property
    def storage65(self):
        return self.__storage65
    @storage65.setter
    def storage65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_chef1__storage65", None)
        self.__storage65 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "chef64"):
                    opp_val = getattr(item, "chef64", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "chef64"):
                    opp_val = getattr(item, "chef64", None)
                    
                    if opp_val is None:
                        setattr(item, "chef64", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def accounnt101(self):
        return self.__accounnt101
    @accounnt101.setter
    def accounnt101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_chef1__accounnt101", None)
        self.__accounnt101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "chef100"):
                opp_val = getattr(old_value, "chef100", None)
                if opp_val == self:
                    setattr(old_value, "chef100", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "chef100"):
                opp_val = getattr(value, "chef100", None)
                setattr(value, "chef100", self)



class Customer_Balance1:

    def __init__(self, Account_balance: str, CustomerID: int, CustomerName: str, Adress: str, Date: str, customer43: "Customer1" = None):
        self.Account_balance = Account_balance
        self.CustomerID = CustomerID
        self.CustomerName = CustomerName
        self.Adress = Adress
        self.Date = Date
        self.customer43 = customer43
        
        pass
    @property
    def Date(self):
        return self.__Date
    @Date.setter
    def Date(self, Date: str):
        self.__Date = Date

    @property
    def CustomerID(self):
        return self.__CustomerID
    @CustomerID.setter
    def CustomerID(self, CustomerID: int):
        self.__CustomerID = CustomerID

    @property
    def Adress(self):
        return self.__Adress
    @Adress.setter
    def Adress(self, Adress: str):
        self.__Adress = Adress

    @property
    def Account_balance(self):
        return self.__Account_balance
    @Account_balance.setter
    def Account_balance(self, Account_balance: str):
        self.__Account_balance = Account_balance

    @property
    def CustomerName(self):
        return self.__CustomerName
    @CustomerName.setter
    def CustomerName(self, CustomerName: str):
        self.__CustomerName = CustomerName

    @property
    def customer43(self):
        return self.__customer43
    @customer43.setter
    def customer43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer_Balance1__customer43", None)
        self.__customer43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer_Balance42"):
                opp_val = getattr(old_value, "customer_Balance42", None)
                if opp_val == self:
                    setattr(old_value, "customer_Balance42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer_Balance42"):
                opp_val = getattr(value, "customer_Balance42", None)
                setattr(value, "customer_Balance42", self)



class Catering1:

    def __init__(self, Menu: str, attribute: str, menu49: set["Menu1"] = None, customer51: set["Customer1"] = None):
        self.Menu = Menu
        self.attribute = attribute
        self.menu49 = menu49 if menu49 is not None else set()
        self.customer51 = customer51 if customer51 is not None else set()
        
        pass
    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def Menu(self):
        return self.__Menu
    @Menu.setter
    def Menu(self, Menu: str):
        self.__Menu = Menu

    @property
    def customer51(self):
        return self.__customer51
    @customer51.setter
    def customer51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Catering1__customer51", None)
        self.__customer51 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "catering50"):
                    opp_val = getattr(item, "catering50", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "catering50"):
                    opp_val = getattr(item, "catering50", None)
                    
                    if opp_val is None:
                        setattr(item, "catering50", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def menu49(self):
        return self.__menu49
    @menu49.setter
    def menu49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Catering1__menu49", None)
        self.__menu49 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "catering48"):
                    opp_val = getattr(item, "catering48", None)
                    
                    if opp_val == self:
                        setattr(item, "catering48", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "catering48"):
                    opp_val = getattr(item, "catering48", None)
                    
                    setattr(item, "catering48", self)
                    



class Menu1:

    def __init__(self, DishName: str, Price: str, Quantity: str, Components: str, catering48: "Catering1" = None, shopping_cart55: "Shopping_cart1" = None, dish105: "Dish" = None, dish106: set["Dish"] = None, shopping_cart94: "Shopping_cart1" = None):
        self.DishName = DishName
        self.Price = Price
        self.Quantity = Quantity
        self.Components = Components
        self.catering48 = catering48
        self.shopping_cart55 = shopping_cart55
        self.dish105 = dish105
        self.dish106 = dish106 if dish106 is not None else set()
        self.shopping_cart94 = shopping_cart94
        
        pass
    @property
    def Price(self):
        return self.__Price
    @Price.setter
    def Price(self, Price: str):
        self.__Price = Price

    @property
    def Quantity(self):
        return self.__Quantity
    @Quantity.setter
    def Quantity(self, Quantity: str):
        self.__Quantity = Quantity

    @property
    def Components(self):
        return self.__Components
    @Components.setter
    def Components(self, Components: str):
        self.__Components = Components

    @property
    def DishName(self):
        return self.__DishName
    @DishName.setter
    def DishName(self, DishName: str):
        self.__DishName = DishName

    @property
    def dish106(self):
        return self.__dish106
    @dish106.setter
    def dish106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Menu1__dish106", None)
        self.__dish106 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "menu107"):
                    opp_val = getattr(item, "menu107", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "menu107"):
                    opp_val = getattr(item, "menu107", None)
                    
                    if opp_val is None:
                        setattr(item, "menu107", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def shopping_cart94(self):
        return self.__shopping_cart94
    @shopping_cart94.setter
    def shopping_cart94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Menu1__shopping_cart94", None)
        self.__shopping_cart94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "menu95"):
                opp_val = getattr(old_value, "menu95", None)
                if opp_val == self:
                    setattr(old_value, "menu95", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "menu95"):
                opp_val = getattr(value, "menu95", None)
                setattr(value, "menu95", self)

    @property
    def dish105(self):
        return self.__dish105
    @dish105.setter
    def dish105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Menu1__dish105", None)
        self.__dish105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "menu104"):
                opp_val = getattr(old_value, "menu104", None)
                if opp_val == self:
                    setattr(old_value, "menu104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "menu104"):
                opp_val = getattr(value, "menu104", None)
                setattr(value, "menu104", self)

    @property
    def catering48(self):
        return self.__catering48
    @catering48.setter
    def catering48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Menu1__catering48", None)
        self.__catering48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "menu49"):
                opp_val = getattr(old_value, "menu49", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "menu49"):
                opp_val = getattr(value, "menu49", None)
                if opp_val is None:
                    setattr(value, "menu49", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def shopping_cart55(self):
        return self.__shopping_cart55
    @shopping_cart55.setter
    def shopping_cart55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Menu1__shopping_cart55", None)
        self.__shopping_cart55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "menu54"):
                opp_val = getattr(old_value, "menu54", None)
                if opp_val == self:
                    setattr(old_value, "menu54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "menu54"):
                opp_val = getattr(value, "menu54", None)
                setattr(value, "menu54", self)



class Customer1:

    def __init__(self, Name: str, ID: int, Address: str, Email: str, Password: str, Accontbalance: str, Phone: int, attribute: str, _attr: str, Adress: str, accounnt36: "Accounnt1" = None, customer_Balance42: "Customer_Balance1" = None, catering50: set["Catering1"] = None, order53: set["Order1"] = None, accounnt102: "Accounnt1" = None, plan89: "Plan1" = None, order92: "Order1" = None, accounnt99: "Accounnt1" = None):
        self.Name = Name
        self.ID = ID
        self.Address = Address
        self.Email = Email
        self.Password = Password
        self.Accontbalance = Accontbalance
        self.Phone = Phone
        self.attribute = attribute
        self._attr = _attr
        self.Adress = Adress
        self.accounnt36 = accounnt36
        self.customer_Balance42 = customer_Balance42
        self.catering50 = catering50 if catering50 is not None else set()
        self.order53 = order53 if order53 is not None else set()
        self.accounnt102 = accounnt102
        self.plan89 = plan89
        self.order92 = order92
        self.accounnt99 = accounnt99
        
        pass
    @property
    def _attr(self):
        return self.___attr
    @_attr.setter
    def _attr(self, _attr: str):
        self.___attr = _attr

    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def Accontbalance(self):
        return self.__Accontbalance
    @Accontbalance.setter
    def Accontbalance(self, Accontbalance: str):
        self.__Accontbalance = Accontbalance

    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

    @property
    def Phone(self):
        return self.__Phone
    @Phone.setter
    def Phone(self, Phone: int):
        self.__Phone = Phone

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def Adress(self):
        return self.__Adress
    @Adress.setter
    def Adress(self, Adress: str):
        self.__Adress = Adress

    @property
    def order92(self):
        return self.__order92
    @order92.setter
    def order92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer1__order92", None)
        self.__order92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer93"):
                opp_val = getattr(old_value, "customer93", None)
                if opp_val == self:
                    setattr(old_value, "customer93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer93"):
                opp_val = getattr(value, "customer93", None)
                setattr(value, "customer93", self)

    @property
    def catering50(self):
        return self.__catering50
    @catering50.setter
    def catering50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer1__catering50", None)
        self.__catering50 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "customer51"):
                    opp_val = getattr(item, "customer51", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "customer51"):
                    opp_val = getattr(item, "customer51", None)
                    
                    if opp_val is None:
                        setattr(item, "customer51", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def accounnt102(self):
        return self.__accounnt102
    @accounnt102.setter
    def accounnt102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer1__accounnt102", None)
        self.__accounnt102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer103"):
                opp_val = getattr(old_value, "customer103", None)
                if opp_val == self:
                    setattr(old_value, "customer103", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer103"):
                opp_val = getattr(value, "customer103", None)
                setattr(value, "customer103", self)

    @property
    def plan89(self):
        return self.__plan89
    @plan89.setter
    def plan89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer1__plan89", None)
        self.__plan89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer88"):
                opp_val = getattr(old_value, "customer88", None)
                if opp_val == self:
                    setattr(old_value, "customer88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer88"):
                opp_val = getattr(value, "customer88", None)
                setattr(value, "customer88", self)

    @property
    def accounnt36(self):
        return self.__accounnt36
    @accounnt36.setter
    def accounnt36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer1__accounnt36", None)
        self.__accounnt36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer37"):
                opp_val = getattr(old_value, "customer37", None)
                if opp_val == self:
                    setattr(old_value, "customer37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer37"):
                opp_val = getattr(value, "customer37", None)
                setattr(value, "customer37", self)

    @property
    def customer_Balance42(self):
        return self.__customer_Balance42
    @customer_Balance42.setter
    def customer_Balance42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer1__customer_Balance42", None)
        self.__customer_Balance42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer43"):
                opp_val = getattr(old_value, "customer43", None)
                if opp_val == self:
                    setattr(old_value, "customer43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer43"):
                opp_val = getattr(value, "customer43", None)
                setattr(value, "customer43", self)

    @property
    def order53(self):
        return self.__order53
    @order53.setter
    def order53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer1__order53", None)
        self.__order53 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "customer52"):
                    opp_val = getattr(item, "customer52", None)
                    
                    if opp_val == self:
                        setattr(item, "customer52", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "customer52"):
                    opp_val = getattr(item, "customer52", None)
                    
                    setattr(item, "customer52", self)
                    

    @property
    def accounnt99(self):
        return self.__accounnt99
    @accounnt99.setter
    def accounnt99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer1__accounnt99", None)
        self.__accounnt99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer98"):
                opp_val = getattr(old_value, "customer98", None)
                if opp_val == self:
                    setattr(old_value, "customer98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer98"):
                opp_val = getattr(value, "customer98", None)
                setattr(value, "customer98", self)



class Accounnt:

    def __init__(self, Email: str, password: str, Accounttype: str, Employee_ID: str, chef35: "chef" = None):
        self.Email = Email
        self.password = password
        self.Accounttype = Accounttype
        self.Employee_ID = Employee_ID
        self.chef35 = chef35
        
        pass
    @property
    def Accounttype(self):
        return self.__Accounttype
    @Accounttype.setter
    def Accounttype(self, Accounttype: str):
        self.__Accounttype = Accounttype

    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def Employee_ID(self):
        return self.__Employee_ID
    @Employee_ID.setter
    def Employee_ID(self, Employee_ID: str):
        self.__Employee_ID = Employee_ID

    @property
    def chef35(self):
        return self.__chef35
    @chef35.setter
    def chef35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Accounnt__chef35", None)
        self.__chef35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "accounnt34"):
                opp_val = getattr(old_value, "accounnt34", None)
                if opp_val == self:
                    setattr(old_value, "accounnt34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "accounnt34"):
                opp_val = getattr(value, "accounnt34", None)
                setattr(value, "accounnt34", self)



class Customer_Balance:

    def __init__(self, CustomerID: int, CustomerName: str, Adress: str, Date: str, Account_balance: str):
        self.CustomerID = CustomerID
        self.CustomerName = CustomerName
        self.Adress = Adress
        self.Date = Date
        self.Account_balance = Account_balance
        
        pass
    @property
    def Adress(self):
        return self.__Adress
    @Adress.setter
    def Adress(self, Adress: str):
        self.__Adress = Adress

    @property
    def Date(self):
        return self.__Date
    @Date.setter
    def Date(self, Date: str):
        self.__Date = Date

    @property
    def CustomerID(self):
        return self.__CustomerID
    @CustomerID.setter
    def CustomerID(self, CustomerID: int):
        self.__CustomerID = CustomerID

    @property
    def CustomerName(self):
        return self.__CustomerName
    @CustomerName.setter
    def CustomerName(self, CustomerName: str):
        self.__CustomerName = CustomerName

    @property
    def Account_balance(self):
        return self.__Account_balance
    @Account_balance.setter
    def Account_balance(self, Account_balance: str):
        self.__Account_balance = Account_balance



class date2:

    pass


class Shopping_cart:

    def __init__(self, Dishname: str, price: int, Quantity: int, time: str, attribute: str):
        self.Dishname = Dishname
        self.price = price
        self.Quantity = Quantity
        self.time = time
        self.attribute = attribute
        
        pass
    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def Quantity(self):
        return self.__Quantity
    @Quantity.setter
    def Quantity(self, Quantity: int):
        self.__Quantity = Quantity

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: int):
        self.__price = price

    @property
    def Dishname(self):
        return self.__Dishname
    @Dishname.setter
    def Dishname(self, Dishname: str):
        self.__Dishname = Dishname

    @property
    def time(self):
        return self.__time
    @time.setter
    def time(self, time: str):
        self.__time = time



class Catering:

    def __init__(self, Menu: str, attribute: str):
        self.Menu = Menu
        self.attribute = attribute
        
        pass
    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def Menu(self):
        return self.__Menu
    @Menu.setter
    def Menu(self, Menu: str):
        self.__Menu = Menu



class System:

    pass


class PrintRecipts:

    def __init__(self, time: str, date: str, PaymentID: str, CustomerID: int, Amount: str, Dishname: str, Quantity: int):
        self.time = time
        self.date = date
        self.PaymentID = PaymentID
        self.CustomerID = CustomerID
        self.Amount = Amount
        self.Dishname = Dishname
        self.Quantity = Quantity
        
        pass
    @property
    def time(self):
        return self.__time
    @time.setter
    def time(self, time: str):
        self.__time = time

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def PaymentID(self):
        return self.__PaymentID
    @PaymentID.setter
    def PaymentID(self, PaymentID: str):
        self.__PaymentID = PaymentID

    @property
    def Quantity(self):
        return self.__Quantity
    @Quantity.setter
    def Quantity(self, Quantity: int):
        self.__Quantity = Quantity

    @property
    def CustomerID(self):
        return self.__CustomerID
    @CustomerID.setter
    def CustomerID(self, CustomerID: int):
        self.__CustomerID = CustomerID

    @property
    def Amount(self):
        return self.__Amount
    @Amount.setter
    def Amount(self, Amount: str):
        self.__Amount = Amount

    @property
    def Dishname(self):
        return self.__Dishname
    @Dishname.setter
    def Dishname(self, Dishname: str):
        self.__Dishname = Dishname



class Payment:

    def __init__(self, PaymentID: int, Amount: str, OrderID: int, CustomerID: int, date: str, time: str):
        self.PaymentID = PaymentID
        self.Amount = Amount
        self.OrderID = OrderID
        self.CustomerID = CustomerID
        self.date = date
        self.time = time
        
        pass
    @property
    def PaymentID(self):
        return self.__PaymentID
    @PaymentID.setter
    def PaymentID(self, PaymentID: int):
        self.__PaymentID = PaymentID

    @property
    def Amount(self):
        return self.__Amount
    @Amount.setter
    def Amount(self, Amount: str):
        self.__Amount = Amount

    @property
    def CustomerID(self):
        return self.__CustomerID
    @CustomerID.setter
    def CustomerID(self, CustomerID: int):
        self.__CustomerID = CustomerID

    @property
    def time(self):
        return self.__time
    @time.setter
    def time(self, time: str):
        self.__time = time

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def OrderID(self):
        return self.__OrderID
    @OrderID.setter
    def OrderID(self, OrderID: int):
        self.__OrderID = OrderID



class Order:

    def __init__(self, OrderID: int, Customerid: int, Dishname: str, attribute: str, date: str):
        self.OrderID = OrderID
        self.Customerid = Customerid
        self.Dishname = Dishname
        self.attribute = attribute
        self.date = date
        
        pass
    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def Customerid(self):
        return self.__Customerid
    @Customerid.setter
    def Customerid(self, Customerid: int):
        self.__Customerid = Customerid

    @property
    def OrderID(self):
        return self.__OrderID
    @OrderID.setter
    def OrderID(self, OrderID: int):
        self.__OrderID = OrderID

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def Dishname(self):
        return self.__Dishname
    @Dishname.setter
    def Dishname(self, Dishname: str):
        self.__Dishname = Dishname



class Menu:

    def __init__(self, DishName: str, Price: str, Quantity: str, Components: str):
        self.DishName = DishName
        self.Price = Price
        self.Quantity = Quantity
        self.Components = Components
        
        pass
    @property
    def Components(self):
        return self.__Components
    @Components.setter
    def Components(self, Components: str):
        self.__Components = Components

    @property
    def Quantity(self):
        return self.__Quantity
    @Quantity.setter
    def Quantity(self, Quantity: str):
        self.__Quantity = Quantity

    @property
    def DishName(self):
        return self.__DishName
    @DishName.setter
    def DishName(self, DishName: str):
        self.__DishName = DishName

    @property
    def Price(self):
        return self.__Price
    @Price.setter
    def Price(self, Price: str):
        self.__Price = Price



class Customer:

    def __init__(self, Name: str, ID: int, Address: str, Email: str, Password: str, Accontbalance: str, Phone: int):
        self.Name = Name
        self.ID = ID
        self.Address = Address
        self.Email = Email
        self.Password = Password
        self.Accontbalance = Accontbalance
        self.Phone = Phone
        
        pass
    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def Accontbalance(self):
        return self.__Accontbalance
    @Accontbalance.setter
    def Accontbalance(self, Accontbalance: str):
        self.__Accontbalance = Accontbalance

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Phone(self):
        return self.__Phone
    @Phone.setter
    def Phone(self, Phone: int):
        self.__Phone = Phone

    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID



class Plan:

    def __init__(self, weekly_plan: str, Monthly_plan: str, day_plan: str, employee3: set["Employee"] = None):
        self.weekly_plan = weekly_plan
        self.Monthly_plan = Monthly_plan
        self.day_plan = day_plan
        self.employee3 = employee3 if employee3 is not None else set()
        
        pass
    @property
    def weekly_plan(self):
        return self.__weekly_plan
    @weekly_plan.setter
    def weekly_plan(self, weekly_plan: str):
        self.__weekly_plan = weekly_plan

    @property
    def Monthly_plan(self):
        return self.__Monthly_plan
    @Monthly_plan.setter
    def Monthly_plan(self, Monthly_plan: str):
        self.__Monthly_plan = Monthly_plan

    @property
    def day_plan(self):
        return self.__day_plan
    @day_plan.setter
    def day_plan(self, day_plan: str):
        self.__day_plan = day_plan

    @property
    def employee3(self):
        return self.__employee3
    @employee3.setter
    def employee3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Plan__employee3", None)
        self.__employee3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "plan2"):
                    opp_val = getattr(item, "plan2", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "plan2"):
                    opp_val = getattr(item, "plan2", None)
                    
                    if opp_val is None:
                        setattr(item, "plan2", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Storage:

    def __init__(self, Component_id: int, Component_Name: str, employee1: set["Employee"] = None):
        self.Component_id = Component_id
        self.Component_Name = Component_Name
        self.employee1 = employee1 if employee1 is not None else set()
        
        pass
    @property
    def Component_id(self):
        return self.__Component_id
    @Component_id.setter
    def Component_id(self, Component_id: int):
        self.__Component_id = Component_id

    @property
    def Component_Name(self):
        return self.__Component_Name
    @Component_Name.setter
    def Component_Name(self, Component_Name: str):
        self.__Component_Name = Component_Name

    @property
    def employee1(self):
        return self.__employee1
    @employee1.setter
    def employee1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Storage__employee1", None)
        self.__employee1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "storage0"):
                    opp_val = getattr(item, "storage0", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "storage0"):
                    opp_val = getattr(item, "storage0", None)
                    
                    if opp_val is None:
                        setattr(item, "storage0", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Employee:

    def __init__(self, Email: str, password: str, attribute: str, ID: int, Name: str, storage0: set["Storage"] = None, plan2: set["Plan"] = None):
        self.Email = Email
        self.password = password
        self.attribute = attribute
        self.ID = ID
        self.Name = Name
        self.storage0 = storage0 if storage0 is not None else set()
        self.plan2 = plan2 if plan2 is not None else set()
        
        pass
    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

    @property
    def plan2(self):
        return self.__plan2
    @plan2.setter
    def plan2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Employee__plan2", None)
        self.__plan2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "employee3"):
                    opp_val = getattr(item, "employee3", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "employee3"):
                    opp_val = getattr(item, "employee3", None)
                    
                    if opp_val is None:
                        setattr(item, "employee3", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def storage0(self):
        return self.__storage0
    @storage0.setter
    def storage0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Employee__storage0", None)
        self.__storage0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "employee1"):
                    opp_val = getattr(item, "employee1", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "employee1"):
                    opp_val = getattr(item, "employee1", None)
                    
                    if opp_val is None:
                        setattr(item, "employee1", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class chef:

    def __init__(self, Name: str, Employee_ID: int, Email: str, passowrd: str, Room_no: int, accounnt34: "Accounnt" = None):
        self.Name = Name
        self.Employee_ID = Employee_ID
        self.Email = Email
        self.passowrd = passowrd
        self.Room_no = Room_no
        self.accounnt34 = accounnt34
        
        pass
    @property
    def Room_no(self):
        return self.__Room_no
    @Room_no.setter
    def Room_no(self, Room_no: int):
        self.__Room_no = Room_no

    @property
    def Employee_ID(self):
        return self.__Employee_ID
    @Employee_ID.setter
    def Employee_ID(self, Employee_ID: int):
        self.__Employee_ID = Employee_ID

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

    @property
    def passowrd(self):
        return self.__passowrd
    @passowrd.setter
    def passowrd(self, passowrd: str):
        self.__passowrd = passowrd

    @property
    def accounnt34(self):
        return self.__accounnt34
    @accounnt34.setter
    def accounnt34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_chef__accounnt34", None)
        self.__accounnt34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "chef35"):
                opp_val = getattr(old_value, "chef35", None)
                if opp_val == self:
                    setattr(old_value, "chef35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "chef35"):
                opp_val = getattr(value, "chef35", None)
                setattr(value, "chef35", self)

