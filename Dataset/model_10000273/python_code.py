from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class customer_Actor:

    pass


class print_ticket_UseCase:

    pass


class reserve_seats_UseCase:

    pass


class make_payment_UseCase:

    pass


class confirm_purchase_UseCase:

    pass


class select_flight_UseCase:

    pass


class search_flights_UseCase:

    pass


class enter_no__of_tickets_UseCase:

    pass


class enter_date_UseCase:

    pass


class round_trip_or_one_way__UseCase:

    pass


class UseCase_UseCase:

    pass


class enter_airport_UseCase:

    pass


class round_trip_or_one_way_UseCase:

    pass


class Reservation_System_Actor:

    pass





class Ticket:

    def __init__(self, source: str, destination: str, dateofjourney: date, time: int, flight_No: str, flight_name: str, customer27: "Customer" = None, booking_counter28: "Booking_counter" = None, agent30: "Agent" = None):
        self.source = source
        self.destination = destination
        self.dateofjourney = dateofjourney
        self.time = time
        self.flight_No = flight_No
        self.flight_name = flight_name
        self.customer27 = customer27
        self.booking_counter28 = booking_counter28
        self.agent30 = agent30
        
        pass
    @property
    def flight_No(self):
        return self.__flight_No
    @flight_No.setter
    def flight_No(self, flight_No: str):
        self.__flight_No = flight_No

    @property
    def time(self):
        return self.__time
    @time.setter
    def time(self, time: int):
        self.__time = time

    @property
    def destination(self):
        return self.__destination
    @destination.setter
    def destination(self, destination: str):
        self.__destination = destination

    @property
    def source(self):
        return self.__source
    @source.setter
    def source(self, source: str):
        self.__source = source

    @property
    def flight_name(self):
        return self.__flight_name
    @flight_name.setter
    def flight_name(self, flight_name: str):
        self.__flight_name = flight_name

    @property
    def dateofjourney(self):
        return self.__dateofjourney
    @dateofjourney.setter
    def dateofjourney(self, dateofjourney: date):
        self.__dateofjourney = dateofjourney

    @property
    def customer27(self):
        return self.__customer27
    @customer27.setter
    def customer27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ticket__customer27", None)
        self.__customer27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ticket26"):
                opp_val = getattr(old_value, "ticket26", None)
                if opp_val == self:
                    setattr(old_value, "ticket26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ticket26"):
                opp_val = getattr(value, "ticket26", None)
                setattr(value, "ticket26", self)

    @property
    def agent30(self):
        return self.__agent30
    @agent30.setter
    def agent30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ticket__agent30", None)
        self.__agent30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ticket31"):
                opp_val = getattr(old_value, "ticket31", None)
                if opp_val == self:
                    setattr(old_value, "ticket31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ticket31"):
                opp_val = getattr(value, "ticket31", None)
                setattr(value, "ticket31", self)

    @property
    def booking_counter28(self):
        return self.__booking_counter28
    @booking_counter28.setter
    def booking_counter28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ticket__booking_counter28", None)
        self.__booking_counter28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ticket29"):
                opp_val = getattr(old_value, "ticket29", None)
                if opp_val == self:
                    setattr(old_value, "ticket29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ticket29"):
                opp_val = getattr(value, "ticket29", None)
                setattr(value, "ticket29", self)



class Booking_counter:

    pass


class Agent:

    def __init__(self, name: str, ticket31: "Ticket" = None):
        self.name = name
        self.ticket31 = ticket31
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ticket31(self):
        return self.__ticket31
    @ticket31.setter
    def ticket31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Agent__ticket31", None)
        self.__ticket31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "agent30"):
                opp_val = getattr(old_value, "agent30", None)
                if opp_val == self:
                    setattr(old_value, "agent30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "agent30"):
                opp_val = getattr(value, "agent30", None)
                setattr(value, "agent30", self)



class Customer:

    def __init__(self, name: str, address: str, ph_no: int, booking_counter24: "Booking_counter" = None, ticket26: "Ticket" = None):
        self.name = name
        self.address = address
        self.ph_no = ph_no
        self.booking_counter24 = booking_counter24
        self.ticket26 = ticket26
        
        pass
    @property
    def ph_no(self):
        return self.__ph_no
    @ph_no.setter
    def ph_no(self, ph_no: int):
        self.__ph_no = ph_no

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ticket26(self):
        return self.__ticket26
    @ticket26.setter
    def ticket26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__ticket26", None)
        self.__ticket26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer27"):
                opp_val = getattr(old_value, "customer27", None)
                if opp_val == self:
                    setattr(old_value, "customer27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer27"):
                opp_val = getattr(value, "customer27", None)
                setattr(value, "customer27", self)

    @property
    def booking_counter24(self):
        return self.__booking_counter24
    @booking_counter24.setter
    def booking_counter24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__booking_counter24", None)
        self.__booking_counter24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer25"):
                opp_val = getattr(old_value, "customer25", None)
                if opp_val == self:
                    setattr(old_value, "customer25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer25"):
                opp_val = getattr(value, "customer25", None)
                setattr(value, "customer25", self)



class Common_fuctions:

    pass


class enter_airport_UseCase1:

    pass


class Reservation_System_Actor1:

    pass
