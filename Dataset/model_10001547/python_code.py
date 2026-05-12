from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Customer:

    def __init__(self, cust_id: int, name: str, mobile: int, email: str, Address: str, restaurant3: "Restaurant" = None):
        self.cust_id = cust_id
        self.name = name
        self.mobile = mobile
        self.email = email
        self.Address = Address
        self.restaurant3 = restaurant3
        
        pass
    @property
    def cust_id(self):
        return self.__cust_id
    @cust_id.setter
    def cust_id(self, cust_id: int):
        self.__cust_id = cust_id

    @property
    def mobile(self):
        return self.__mobile
    @mobile.setter
    def mobile(self, mobile: int):
        self.__mobile = mobile

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
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def restaurant3(self):
        return self.__restaurant3
    @restaurant3.setter
    def restaurant3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__restaurant3", None)
        self.__restaurant3 = value
        
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



class Table_booking_time:

    def __init__(self, start_time: int, end_time: int, payment6: "Payment" = None, booking5: "Booking" = None):
        self.start_time = start_time
        self.end_time = end_time
        self.payment6 = payment6
        self.booking5 = booking5
        
        pass
    @property
    def start_time(self):
        return self.__start_time
    @start_time.setter
    def start_time(self, start_time: int):
        self.__start_time = start_time

    @property
    def end_time(self):
        return self.__end_time
    @end_time.setter
    def end_time(self, end_time: int):
        self.__end_time = end_time

    @property
    def payment6(self):
        return self.__payment6
    @payment6.setter
    def payment6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Table_booking_time__payment6", None)
        self.__payment6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "table_booking_time7"):
                opp_val = getattr(old_value, "table_booking_time7", None)
                if opp_val == self:
                    setattr(old_value, "table_booking_time7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "table_booking_time7"):
                opp_val = getattr(value, "table_booking_time7", None)
                setattr(value, "table_booking_time7", self)

    @property
    def booking5(self):
        return self.__booking5
    @booking5.setter
    def booking5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Table_booking_time__booking5", None)
        self.__booking5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "table_booking_time4"):
                opp_val = getattr(old_value, "table_booking_time4", None)
                if opp_val == self:
                    setattr(old_value, "table_booking_time4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "table_booking_time4"):
                opp_val = getattr(value, "table_booking_time4", None)
                setattr(value, "table_booking_time4", self)



class Booking:

    def __init__(self, customer_name: str, arrival_time: int, table_number: int, table1: "Table" = None, table_booking_time4: "Table_booking_time" = None):
        self.customer_name = customer_name
        self.arrival_time = arrival_time
        self.table_number = table_number
        self.table1 = table1
        self.table_booking_time4 = table_booking_time4
        
        pass
    @property
    def table_number(self):
        return self.__table_number
    @table_number.setter
    def table_number(self, table_number: int):
        self.__table_number = table_number

    @property
    def customer_name(self):
        return self.__customer_name
    @customer_name.setter
    def customer_name(self, customer_name: str):
        self.__customer_name = customer_name

    @property
    def arrival_time(self):
        return self.__arrival_time
    @arrival_time.setter
    def arrival_time(self, arrival_time: int):
        self.__arrival_time = arrival_time

    @property
    def table_booking_time4(self):
        return self.__table_booking_time4
    @table_booking_time4.setter
    def table_booking_time4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Booking__table_booking_time4", None)
        self.__table_booking_time4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "booking5"):
                opp_val = getattr(old_value, "booking5", None)
                if opp_val == self:
                    setattr(old_value, "booking5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "booking5"):
                opp_val = getattr(value, "booking5", None)
                setattr(value, "booking5", self)

    @property
    def table1(self):
        return self.__table1
    @table1.setter
    def table1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Booking__table1", None)
        self.__table1 = value
        
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



class Payment:

    def __init__(self, pay_hotel: int, paytm: int, credit_card: int, debit_card: int, table_booking_time7: "Table_booking_time" = None):
        self.pay_hotel = pay_hotel
        self.paytm = paytm
        self.credit_card = credit_card
        self.debit_card = debit_card
        self.table_booking_time7 = table_booking_time7
        
        pass
    @property
    def paytm(self):
        return self.__paytm
    @paytm.setter
    def paytm(self, paytm: int):
        self.__paytm = paytm

    @property
    def pay_hotel(self):
        return self.__pay_hotel
    @pay_hotel.setter
    def pay_hotel(self, pay_hotel: int):
        self.__pay_hotel = pay_hotel

    @property
    def debit_card(self):
        return self.__debit_card
    @debit_card.setter
    def debit_card(self, debit_card: int):
        self.__debit_card = debit_card

    @property
    def credit_card(self):
        return self.__credit_card
    @credit_card.setter
    def credit_card(self, credit_card: int):
        self.__credit_card = credit_card

    @property
    def table_booking_time7(self):
        return self.__table_booking_time7
    @table_booking_time7.setter
    def table_booking_time7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__table_booking_time7", None)
        self.__table_booking_time7 = value
        
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



class Table:

    def __init__(self, table_number: int, total_person: int, restaurant9: "Restaurant" = None, booking0: "Booking" = None):
        self.table_number = table_number
        self.total_person = total_person
        self.restaurant9 = restaurant9
        self.booking0 = booking0
        
        pass
    @property
    def total_person(self):
        return self.__total_person
    @total_person.setter
    def total_person(self, total_person: int):
        self.__total_person = total_person

    @property
    def table_number(self):
        return self.__table_number
    @table_number.setter
    def table_number(self, table_number: int):
        self.__table_number = table_number

    @property
    def restaurant9(self):
        return self.__restaurant9
    @restaurant9.setter
    def restaurant9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Table__restaurant9", None)
        self.__restaurant9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "table8"):
                opp_val = getattr(old_value, "table8", None)
                if opp_val == self:
                    setattr(old_value, "table8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "table8"):
                opp_val = getattr(value, "table8", None)
                setattr(value, "table8", self)

    @property
    def booking0(self):
        return self.__booking0
    @booking0.setter
    def booking0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Table__booking0", None)
        self.__booking0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "table1"):
                opp_val = getattr(old_value, "table1", None)
                if opp_val == self:
                    setattr(old_value, "table1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "table1"):
                opp_val = getattr(value, "table1", None)
                setattr(value, "table1", self)



class Restaurant:

    def __init__(self, time: int, booking: int, table8: "Table" = None, customer2: "Customer" = None):
        self.time = time
        self.booking = booking
        self.table8 = table8
        self.customer2 = customer2
        
        pass
    @property
    def time(self):
        return self.__time
    @time.setter
    def time(self, time: int):
        self.__time = time

    @property
    def booking(self):
        return self.__booking
    @booking.setter
    def booking(self, booking: int):
        self.__booking = booking

    @property
    def table8(self):
        return self.__table8
    @table8.setter
    def table8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Restaurant__table8", None)
        self.__table8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "restaurant9"):
                opp_val = getattr(old_value, "restaurant9", None)
                if opp_val == self:
                    setattr(old_value, "restaurant9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "restaurant9"):
                opp_val = getattr(value, "restaurant9", None)
                setattr(value, "restaurant9", self)

    @property
    def customer2(self):
        return self.__customer2
    @customer2.setter
    def customer2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Restaurant__customer2", None)
        self.__customer2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "restaurant3"):
                opp_val = getattr(old_value, "restaurant3", None)
                if opp_val == self:
                    setattr(old_value, "restaurant3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "restaurant3"):
                opp_val = getattr(value, "restaurant3", None)
                setattr(value, "restaurant3", self)

