from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Credit_Card:

    def __init__(self, Pin_No_: str, Card_No_: str, payment11: "Payment" = None):
        self.Pin_No_ = Pin_No_
        self.Card_No_ = Card_No_
        self.payment11 = payment11
        
        pass
    @property
    def Card_No_(self):
        return self.__Card_No_
    @Card_No_.setter
    def Card_No_(self, Card_No_: str):
        self.__Card_No_ = Card_No_

    @property
    def Pin_No_(self):
        return self.__Pin_No_
    @Pin_No_.setter
    def Pin_No_(self, Pin_No_: str):
        self.__Pin_No_ = Pin_No_

    @property
    def payment11(self):
        return self.__payment11
    @payment11.setter
    def payment11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Credit_Card__payment11", None)
        self.__payment11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "credit_Card10"):
                opp_val = getattr(old_value, "credit_Card10", None)
                if opp_val == self:
                    setattr(old_value, "credit_Card10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "credit_Card10"):
                opp_val = getattr(value, "credit_Card10", None)
                setattr(value, "credit_Card10", self)



class Debit_Card:

    def __init__(self, Pin_No_: str, Card_No_: str, payment9: "Payment" = None):
        self.Pin_No_ = Pin_No_
        self.Card_No_ = Card_No_
        self.payment9 = payment9
        
        pass
    @property
    def Pin_No_(self):
        return self.__Pin_No_
    @Pin_No_.setter
    def Pin_No_(self, Pin_No_: str):
        self.__Pin_No_ = Pin_No_

    @property
    def Card_No_(self):
        return self.__Card_No_
    @Card_No_.setter
    def Card_No_(self, Card_No_: str):
        self.__Card_No_ = Card_No_

    @property
    def payment9(self):
        return self.__payment9
    @payment9.setter
    def payment9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Debit_Card__payment9", None)
        self.__payment9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "debit_Card8"):
                opp_val = getattr(old_value, "debit_Card8", None)
                if opp_val == self:
                    setattr(old_value, "debit_Card8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "debit_Card8"):
                opp_val = getattr(value, "debit_Card8", None)
                setattr(value, "debit_Card8", self)



class Hotel:

    def __init__(self, Hotel_ID: str, Hotel_Name: str, Hotel_Type: str, Hotel_Address: str, Hotel_Rent: str, booking13: "Booking" = None, customer15: "Customer" = None, admin17: "Admin" = None, payment23: "Payment" = None, room5: "Room" = None):
        self.Hotel_ID = Hotel_ID
        self.Hotel_Name = Hotel_Name
        self.Hotel_Type = Hotel_Type
        self.Hotel_Address = Hotel_Address
        self.Hotel_Rent = Hotel_Rent
        self.booking13 = booking13
        self.customer15 = customer15
        self.admin17 = admin17
        self.payment23 = payment23
        self.room5 = room5
        
        pass
    @property
    def Hotel_Address(self):
        return self.__Hotel_Address
    @Hotel_Address.setter
    def Hotel_Address(self, Hotel_Address: str):
        self.__Hotel_Address = Hotel_Address

    @property
    def Hotel_ID(self):
        return self.__Hotel_ID
    @Hotel_ID.setter
    def Hotel_ID(self, Hotel_ID: str):
        self.__Hotel_ID = Hotel_ID

    @property
    def Hotel_Rent(self):
        return self.__Hotel_Rent
    @Hotel_Rent.setter
    def Hotel_Rent(self, Hotel_Rent: str):
        self.__Hotel_Rent = Hotel_Rent

    @property
    def Hotel_Name(self):
        return self.__Hotel_Name
    @Hotel_Name.setter
    def Hotel_Name(self, Hotel_Name: str):
        self.__Hotel_Name = Hotel_Name

    @property
    def Hotel_Type(self):
        return self.__Hotel_Type
    @Hotel_Type.setter
    def Hotel_Type(self, Hotel_Type: str):
        self.__Hotel_Type = Hotel_Type

    @property
    def room5(self):
        return self.__room5
    @room5.setter
    def room5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hotel__room5", None)
        self.__room5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hotel4"):
                opp_val = getattr(old_value, "hotel4", None)
                if opp_val == self:
                    setattr(old_value, "hotel4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hotel4"):
                opp_val = getattr(value, "hotel4", None)
                setattr(value, "hotel4", self)

    @property
    def payment23(self):
        return self.__payment23
    @payment23.setter
    def payment23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hotel__payment23", None)
        self.__payment23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hotel22"):
                opp_val = getattr(old_value, "hotel22", None)
                if opp_val == self:
                    setattr(old_value, "hotel22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hotel22"):
                opp_val = getattr(value, "hotel22", None)
                setattr(value, "hotel22", self)

    @property
    def booking13(self):
        return self.__booking13
    @booking13.setter
    def booking13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hotel__booking13", None)
        self.__booking13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hotel12"):
                opp_val = getattr(old_value, "hotel12", None)
                if opp_val == self:
                    setattr(old_value, "hotel12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hotel12"):
                opp_val = getattr(value, "hotel12", None)
                setattr(value, "hotel12", self)

    @property
    def customer15(self):
        return self.__customer15
    @customer15.setter
    def customer15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hotel__customer15", None)
        self.__customer15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hotel14"):
                opp_val = getattr(old_value, "hotel14", None)
                if opp_val == self:
                    setattr(old_value, "hotel14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hotel14"):
                opp_val = getattr(value, "hotel14", None)
                setattr(value, "hotel14", self)

    @property
    def admin17(self):
        return self.__admin17
    @admin17.setter
    def admin17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hotel__admin17", None)
        self.__admin17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hotel16"):
                opp_val = getattr(old_value, "hotel16", None)
                if opp_val == self:
                    setattr(old_value, "hotel16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hotel16"):
                opp_val = getattr(value, "hotel16", None)
                setattr(value, "hotel16", self)



class Payment:

    def __init__(self, Customer_s_Id: str, Amount: str, Payment_Description: str, Payment_Date: str, booking18: "Booking" = None, room20: "Room" = None, hotel22: "Hotel" = None, customer7: "Customer" = None, debit_Card8: "Debit_Card" = None, credit_Card10: "Credit_Card" = None):
        self.Customer_s_Id = Customer_s_Id
        self.Amount = Amount
        self.Payment_Description = Payment_Description
        self.Payment_Date = Payment_Date
        self.booking18 = booking18
        self.room20 = room20
        self.hotel22 = hotel22
        self.customer7 = customer7
        self.debit_Card8 = debit_Card8
        self.credit_Card10 = credit_Card10
        
        pass
    @property
    def Payment_Description(self):
        return self.__Payment_Description
    @Payment_Description.setter
    def Payment_Description(self, Payment_Description: str):
        self.__Payment_Description = Payment_Description

    @property
    def Payment_Date(self):
        return self.__Payment_Date
    @Payment_Date.setter
    def Payment_Date(self, Payment_Date: str):
        self.__Payment_Date = Payment_Date

    @property
    def Customer_s_Id(self):
        return self.__Customer_s_Id
    @Customer_s_Id.setter
    def Customer_s_Id(self, Customer_s_Id: str):
        self.__Customer_s_Id = Customer_s_Id

    @property
    def Amount(self):
        return self.__Amount
    @Amount.setter
    def Amount(self, Amount: str):
        self.__Amount = Amount

    @property
    def credit_Card10(self):
        return self.__credit_Card10
    @credit_Card10.setter
    def credit_Card10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__credit_Card10", None)
        self.__credit_Card10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payment11"):
                opp_val = getattr(old_value, "payment11", None)
                if opp_val == self:
                    setattr(old_value, "payment11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payment11"):
                opp_val = getattr(value, "payment11", None)
                setattr(value, "payment11", self)

    @property
    def booking18(self):
        return self.__booking18
    @booking18.setter
    def booking18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__booking18", None)
        self.__booking18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payment19"):
                opp_val = getattr(old_value, "payment19", None)
                if opp_val == self:
                    setattr(old_value, "payment19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payment19"):
                opp_val = getattr(value, "payment19", None)
                setattr(value, "payment19", self)

    @property
    def debit_Card8(self):
        return self.__debit_Card8
    @debit_Card8.setter
    def debit_Card8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__debit_Card8", None)
        self.__debit_Card8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payment9"):
                opp_val = getattr(old_value, "payment9", None)
                if opp_val == self:
                    setattr(old_value, "payment9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payment9"):
                opp_val = getattr(value, "payment9", None)
                setattr(value, "payment9", self)

    @property
    def hotel22(self):
        return self.__hotel22
    @hotel22.setter
    def hotel22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__hotel22", None)
        self.__hotel22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payment23"):
                opp_val = getattr(old_value, "payment23", None)
                if opp_val == self:
                    setattr(old_value, "payment23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payment23"):
                opp_val = getattr(value, "payment23", None)
                setattr(value, "payment23", self)

    @property
    def customer7(self):
        return self.__customer7
    @customer7.setter
    def customer7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__customer7", None)
        self.__customer7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payment6"):
                opp_val = getattr(old_value, "payment6", None)
                if opp_val == self:
                    setattr(old_value, "payment6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payment6"):
                opp_val = getattr(value, "payment6", None)
                setattr(value, "payment6", self)

    @property
    def room20(self):
        return self.__room20
    @room20.setter
    def room20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__room20", None)
        self.__room20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payment21"):
                opp_val = getattr(old_value, "payment21", None)
                if opp_val == self:
                    setattr(old_value, "payment21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payment21"):
                opp_val = getattr(value, "payment21", None)
                setattr(value, "payment21", self)



class Room:

    def __init__(self, Room_Id: str, Room_number: str, Room_type: str, Room_description: str, payment21: "Payment" = None, admin3: "Admin" = None, hotel4: "Hotel" = None):
        self.Room_Id = Room_Id
        self.Room_number = Room_number
        self.Room_type = Room_type
        self.Room_description = Room_description
        self.payment21 = payment21
        self.admin3 = admin3
        self.hotel4 = hotel4
        
        pass
    @property
    def Room_description(self):
        return self.__Room_description
    @Room_description.setter
    def Room_description(self, Room_description: str):
        self.__Room_description = Room_description

    @property
    def Room_type(self):
        return self.__Room_type
    @Room_type.setter
    def Room_type(self, Room_type: str):
        self.__Room_type = Room_type

    @property
    def Room_Id(self):
        return self.__Room_Id
    @Room_Id.setter
    def Room_Id(self, Room_Id: str):
        self.__Room_Id = Room_Id

    @property
    def Room_number(self):
        return self.__Room_number
    @Room_number.setter
    def Room_number(self, Room_number: str):
        self.__Room_number = Room_number

    @property
    def admin3(self):
        return self.__admin3
    @admin3.setter
    def admin3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Room__admin3", None)
        self.__admin3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room2"):
                opp_val = getattr(old_value, "room2", None)
                if opp_val == self:
                    setattr(old_value, "room2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room2"):
                opp_val = getattr(value, "room2", None)
                setattr(value, "room2", self)

    @property
    def hotel4(self):
        return self.__hotel4
    @hotel4.setter
    def hotel4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Room__hotel4", None)
        self.__hotel4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room5"):
                opp_val = getattr(old_value, "room5", None)
                if opp_val == self:
                    setattr(old_value, "room5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room5"):
                opp_val = getattr(value, "room5", None)
                setattr(value, "room5", self)

    @property
    def payment21(self):
        return self.__payment21
    @payment21.setter
    def payment21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Room__payment21", None)
        self.__payment21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room20"):
                opp_val = getattr(old_value, "room20", None)
                if opp_val == self:
                    setattr(old_value, "room20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room20"):
                opp_val = getattr(value, "room20", None)
                setattr(value, "room20", self)



class Admin:

    def __init__(self, Name: str, Id: str, Password: str, hotel16: "Hotel" = None, booking0: "Booking" = None, room2: "Room" = None):
        self.Name = Name
        self.Id = Id
        self.Password = Password
        self.hotel16 = hotel16
        self.booking0 = booking0
        self.room2 = room2
        
        pass
    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def Id(self):
        return self.__Id
    @Id.setter
    def Id(self, Id: str):
        self.__Id = Id

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def booking0(self):
        return self.__booking0
    @booking0.setter
    def booking0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Admin__booking0", None)
        self.__booking0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "admin1"):
                opp_val = getattr(old_value, "admin1", None)
                if opp_val == self:
                    setattr(old_value, "admin1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "admin1"):
                opp_val = getattr(value, "admin1", None)
                setattr(value, "admin1", self)

    @property
    def hotel16(self):
        return self.__hotel16
    @hotel16.setter
    def hotel16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Admin__hotel16", None)
        self.__hotel16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "admin17"):
                opp_val = getattr(old_value, "admin17", None)
                if opp_val == self:
                    setattr(old_value, "admin17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "admin17"):
                opp_val = getattr(value, "admin17", None)
                setattr(value, "admin17", self)

    @property
    def room2(self):
        return self.__room2
    @room2.setter
    def room2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Admin__room2", None)
        self.__room2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "admin3"):
                opp_val = getattr(old_value, "admin3", None)
                if opp_val == self:
                    setattr(old_value, "admin3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "admin3"):
                opp_val = getattr(value, "admin3", None)
                setattr(value, "admin3", self)



class Customer:

    def __init__(self, Address: str, Mobile_no___Email: str, Name: str, Id: str, hotel14: "Hotel" = None, payment6: "Payment" = None):
        self.Address = Address
        self.Mobile_no___Email = Mobile_no___Email
        self.Name = Name
        self.Id = Id
        self.hotel14 = hotel14
        self.payment6 = payment6
        
        pass
    @property
    def Id(self):
        return self.__Id
    @Id.setter
    def Id(self, Id: str):
        self.__Id = Id

    @property
    def Mobile_no___Email(self):
        return self.__Mobile_no___Email
    @Mobile_no___Email.setter
    def Mobile_no___Email(self, Mobile_no___Email: str):
        self.__Mobile_no___Email = Mobile_no___Email

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
    def hotel14(self):
        return self.__hotel14
    @hotel14.setter
    def hotel14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__hotel14", None)
        self.__hotel14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer15"):
                opp_val = getattr(old_value, "customer15", None)
                if opp_val == self:
                    setattr(old_value, "customer15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer15"):
                opp_val = getattr(value, "customer15", None)
                setattr(value, "customer15", self)

    @property
    def payment6(self):
        return self.__payment6
    @payment6.setter
    def payment6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__payment6", None)
        self.__payment6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer7"):
                opp_val = getattr(old_value, "customer7", None)
                if opp_val == self:
                    setattr(old_value, "customer7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer7"):
                opp_val = getattr(value, "customer7", None)
                setattr(value, "customer7", self)



class Booking:

    def __init__(self, Id: str, Date: str, Description: str, Type: str, hotel12: "Hotel" = None, payment19: "Payment" = None, admin1: "Admin" = None):
        self.Id = Id
        self.Date = Date
        self.Description = Description
        self.Type = Type
        self.hotel12 = hotel12
        self.payment19 = payment19
        self.admin1 = admin1
        
        pass
    @property
    def Date(self):
        return self.__Date
    @Date.setter
    def Date(self, Date: str):
        self.__Date = Date

    @property
    def Description(self):
        return self.__Description
    @Description.setter
    def Description(self, Description: str):
        self.__Description = Description

    @property
    def Id(self):
        return self.__Id
    @Id.setter
    def Id(self, Id: str):
        self.__Id = Id

    @property
    def Type(self):
        return self.__Type
    @Type.setter
    def Type(self, Type: str):
        self.__Type = Type

    @property
    def hotel12(self):
        return self.__hotel12
    @hotel12.setter
    def hotel12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Booking__hotel12", None)
        self.__hotel12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "booking13"):
                opp_val = getattr(old_value, "booking13", None)
                if opp_val == self:
                    setattr(old_value, "booking13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "booking13"):
                opp_val = getattr(value, "booking13", None)
                setattr(value, "booking13", self)

    @property
    def admin1(self):
        return self.__admin1
    @admin1.setter
    def admin1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Booking__admin1", None)
        self.__admin1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "booking0"):
                opp_val = getattr(old_value, "booking0", None)
                if opp_val == self:
                    setattr(old_value, "booking0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "booking0"):
                opp_val = getattr(value, "booking0", None)
                setattr(value, "booking0", self)

    @property
    def payment19(self):
        return self.__payment19
    @payment19.setter
    def payment19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Booking__payment19", None)
        self.__payment19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "booking18"):
                opp_val = getattr(old_value, "booking18", None)
                if opp_val == self:
                    setattr(old_value, "booking18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "booking18"):
                opp_val = getattr(value, "booking18", None)
                setattr(value, "booking18", self)

