from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Cleaning_Management_UseCase:

    pass


class Reciept____Balance_UseCase:

    pass


class Type_of_Payment_UseCase:

    pass


class Type_of_car_UseCase:

    pass


class Type_of_wash_UseCase:

    pass


class Info_UseCase:

    pass


class Payment_UseCase:

    pass


class Deliver_Actor:

    pass


class Cleaner_Actor:

    pass


class Payment_Actor:

    pass


class Client_Actor:

    pass


class Client_Id___Name_UseCase:

    pass


class Delivery_Boy_Id_UseCase:

    pass


class Delivery_Management_UseCase:

    pass


class Brushing_UseCase:

    pass


class Water_Wash_UseCase:

    pass


class Powderized_Cleaning_UseCase:

    pass





class Money_Dispenser:

    pass


class Cleaning_Management:

    def __init__(self, water: str, powderized_wash: str, brushing: str, payment3: "Payment" = None, delivering_Management4: "Delivering_Management" = None, user11: "User" = None, cleaner14: "Cleaner" = None):
        self.water = water
        self.powderized_wash = powderized_wash
        self.brushing = brushing
        self.payment3 = payment3
        self.delivering_Management4 = delivering_Management4
        self.user11 = user11
        self.cleaner14 = cleaner14
        
        pass
    @property
    def water(self):
        return self.__water
    @water.setter
    def water(self, water: str):
        self.__water = water

    @property
    def powderized_wash(self):
        return self.__powderized_wash
    @powderized_wash.setter
    def powderized_wash(self, powderized_wash: str):
        self.__powderized_wash = powderized_wash

    @property
    def brushing(self):
        return self.__brushing
    @brushing.setter
    def brushing(self, brushing: str):
        self.__brushing = brushing

    @property
    def delivering_Management4(self):
        return self.__delivering_Management4
    @delivering_Management4.setter
    def delivering_Management4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cleaning_Management__delivering_Management4", None)
        self.__delivering_Management4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cleaning_Management5"):
                opp_val = getattr(old_value, "cleaning_Management5", None)
                if opp_val == self:
                    setattr(old_value, "cleaning_Management5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cleaning_Management5"):
                opp_val = getattr(value, "cleaning_Management5", None)
                setattr(value, "cleaning_Management5", self)

    @property
    def cleaner14(self):
        return self.__cleaner14
    @cleaner14.setter
    def cleaner14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cleaning_Management__cleaner14", None)
        self.__cleaner14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cleaning_Management15"):
                opp_val = getattr(old_value, "cleaning_Management15", None)
                if opp_val == self:
                    setattr(old_value, "cleaning_Management15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cleaning_Management15"):
                opp_val = getattr(value, "cleaning_Management15", None)
                setattr(value, "cleaning_Management15", self)

    @property
    def user11(self):
        return self.__user11
    @user11.setter
    def user11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cleaning_Management__user11", None)
        self.__user11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cleaning_Management10"):
                opp_val = getattr(old_value, "cleaning_Management10", None)
                if opp_val == self:
                    setattr(old_value, "cleaning_Management10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cleaning_Management10"):
                opp_val = getattr(value, "cleaning_Management10", None)
                setattr(value, "cleaning_Management10", self)

    @property
    def payment3(self):
        return self.__payment3
    @payment3.setter
    def payment3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cleaning_Management__payment3", None)
        self.__payment3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cleaning_Management2"):
                opp_val = getattr(old_value, "cleaning_Management2", None)
                if opp_val == self:
                    setattr(old_value, "cleaning_Management2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cleaning_Management2"):
                opp_val = getattr(value, "cleaning_Management2", None)
                setattr(value, "cleaning_Management2", self)



class User:

    pass


class Delivery_Boy:

    pass


class Cleaner:

    pass


class Administrator:

    pass


class Delivering_Management:

    def __init__(self, client_name: str, client_key: str, deliver_boy_id: str, cleaning_Management5: "Cleaning_Management" = None, user13: "User" = None, delivery_Boy18: "Delivery_Boy" = None):
        self.client_name = client_name
        self.client_key = client_key
        self.deliver_boy_id = deliver_boy_id
        self.cleaning_Management5 = cleaning_Management5
        self.user13 = user13
        self.delivery_Boy18 = delivery_Boy18
        
        pass
    @property
    def client_name(self):
        return self.__client_name
    @client_name.setter
    def client_name(self, client_name: str):
        self.__client_name = client_name

    @property
    def client_key(self):
        return self.__client_key
    @client_key.setter
    def client_key(self, client_key: str):
        self.__client_key = client_key

    @property
    def deliver_boy_id(self):
        return self.__deliver_boy_id
    @deliver_boy_id.setter
    def deliver_boy_id(self, deliver_boy_id: str):
        self.__deliver_boy_id = deliver_boy_id

    @property
    def user13(self):
        return self.__user13
    @user13.setter
    def user13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Delivering_Management__user13", None)
        self.__user13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delivering_Management12"):
                opp_val = getattr(old_value, "delivering_Management12", None)
                if opp_val == self:
                    setattr(old_value, "delivering_Management12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delivering_Management12"):
                opp_val = getattr(value, "delivering_Management12", None)
                setattr(value, "delivering_Management12", self)

    @property
    def delivery_Boy18(self):
        return self.__delivery_Boy18
    @delivery_Boy18.setter
    def delivery_Boy18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Delivering_Management__delivery_Boy18", None)
        self.__delivery_Boy18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delivering_Management19"):
                opp_val = getattr(old_value, "delivering_Management19", None)
                if opp_val == self:
                    setattr(old_value, "delivering_Management19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delivering_Management19"):
                opp_val = getattr(value, "delivering_Management19", None)
                setattr(value, "delivering_Management19", self)

    @property
    def cleaning_Management5(self):
        return self.__cleaning_Management5
    @cleaning_Management5.setter
    def cleaning_Management5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Delivering_Management__cleaning_Management5", None)
        self.__cleaning_Management5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delivering_Management4"):
                opp_val = getattr(old_value, "delivering_Management4", None)
                if opp_val == self:
                    setattr(old_value, "delivering_Management4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delivering_Management4"):
                opp_val = getattr(value, "delivering_Management4", None)
                setattr(value, "delivering_Management4", self)



class Payment:

    def __init__(self, Type_of_payment: str, primary_Info1: "Primary_Info" = None, cleaning_Management2: "Cleaning_Management" = None, user9: "User" = None, money_Dispenser16: "Money_Dispenser" = None):
        self.Type_of_payment = Type_of_payment
        self.primary_Info1 = primary_Info1
        self.cleaning_Management2 = cleaning_Management2
        self.user9 = user9
        self.money_Dispenser16 = money_Dispenser16
        
        pass
    @property
    def Type_of_payment(self):
        return self.__Type_of_payment
    @Type_of_payment.setter
    def Type_of_payment(self, Type_of_payment: str):
        self.__Type_of_payment = Type_of_payment

    @property
    def cleaning_Management2(self):
        return self.__cleaning_Management2
    @cleaning_Management2.setter
    def cleaning_Management2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__cleaning_Management2", None)
        self.__cleaning_Management2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payment3"):
                opp_val = getattr(old_value, "payment3", None)
                if opp_val == self:
                    setattr(old_value, "payment3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payment3"):
                opp_val = getattr(value, "payment3", None)
                setattr(value, "payment3", self)

    @property
    def user9(self):
        return self.__user9
    @user9.setter
    def user9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__user9", None)
        self.__user9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payment8"):
                opp_val = getattr(old_value, "payment8", None)
                if opp_val == self:
                    setattr(old_value, "payment8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payment8"):
                opp_val = getattr(value, "payment8", None)
                setattr(value, "payment8", self)

    @property
    def money_Dispenser16(self):
        return self.__money_Dispenser16
    @money_Dispenser16.setter
    def money_Dispenser16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__money_Dispenser16", None)
        self.__money_Dispenser16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payment17"):
                opp_val = getattr(old_value, "payment17", None)
                if opp_val == self:
                    setattr(old_value, "payment17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payment17"):
                opp_val = getattr(value, "payment17", None)
                setattr(value, "payment17", self)

    @property
    def primary_Info1(self):
        return self.__primary_Info1
    @primary_Info1.setter
    def primary_Info1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__primary_Info1", None)
        self.__primary_Info1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payment0"):
                opp_val = getattr(old_value, "payment0", None)
                if opp_val == self:
                    setattr(old_value, "payment0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payment0"):
                opp_val = getattr(value, "payment0", None)
                setattr(value, "payment0", self)



class Primary_Info:

    def __init__(self, Type_of_wash: str, Type_of_car: str, payment0: "Payment" = None, user7: "User" = None):
        self.Type_of_wash = Type_of_wash
        self.Type_of_car = Type_of_car
        self.payment0 = payment0
        self.user7 = user7
        
        pass
    @property
    def Type_of_wash(self):
        return self.__Type_of_wash
    @Type_of_wash.setter
    def Type_of_wash(self, Type_of_wash: str):
        self.__Type_of_wash = Type_of_wash

    @property
    def Type_of_car(self):
        return self.__Type_of_car
    @Type_of_car.setter
    def Type_of_car(self, Type_of_car: str):
        self.__Type_of_car = Type_of_car

    @property
    def user7(self):
        return self.__user7
    @user7.setter
    def user7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Primary_Info__user7", None)
        self.__user7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "primary_Info6"):
                opp_val = getattr(old_value, "primary_Info6", None)
                if opp_val == self:
                    setattr(old_value, "primary_Info6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "primary_Info6"):
                opp_val = getattr(value, "primary_Info6", None)
                setattr(value, "primary_Info6", self)

    @property
    def payment0(self):
        return self.__payment0
    @payment0.setter
    def payment0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Primary_Info__payment0", None)
        self.__payment0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "primary_Info1"):
                opp_val = getattr(old_value, "primary_Info1", None)
                if opp_val == self:
                    setattr(old_value, "primary_Info1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "primary_Info1"):
                opp_val = getattr(value, "primary_Info1", None)
                setattr(value, "primary_Info1", self)

