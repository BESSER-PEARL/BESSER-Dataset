from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Contact_Center_Agent_Actor:

    pass


class Customer_Actor:

    pass


class Qaboos_Reservation_System_Manage_Booking_UseCase:

    pass


class Qaboos_Reservation_System_Choose_Seats_UseCase:

    pass


class Qaboos_Reservation_System_Update_Flight_Details_UseCase:

    pass


class Qaboos_Reservation_System_Join__Qaboos_FPP_Club_UseCase:

    pass


class Qaboos_Reservation_System_Check_In_Online_UseCase:

    pass


class Qaboos_Reservation_System_Cancel_booking_UseCase:

    pass


class Qaboos_Reservation_System_Make_Payment_UseCase:

    pass


class Qaboos_Reservation_System_Confirm_booking__UseCase:

    pass


class Qaboos_Reservation_System_Enter_Passengers_Details_UseCase:

    pass


class Qaboos_Reservation_System_Book_ticket__UseCase:

    pass


class Qaboos_Reservation_System_Check_Flights_Availability_UseCase:

    pass


class Qaboos_Reservation_System_Enter_flight_Details_UseCase:

    pass





class First_Class:

    def __init__(self, First_Seat_ID: str, First_Seat_Price: str):
        self.First_Seat_ID = First_Seat_ID
        self.First_Seat_Price = First_Seat_Price
        
        pass
    @property
    def First_Seat_ID(self):
        return self.__First_Seat_ID
    @First_Seat_ID.setter
    def First_Seat_ID(self, First_Seat_ID: str):
        self.__First_Seat_ID = First_Seat_ID

    @property
    def First_Seat_Price(self):
        return self.__First_Seat_Price
    @First_Seat_Price.setter
    def First_Seat_Price(self, First_Seat_Price: str):
        self.__First_Seat_Price = First_Seat_Price



class Business_Seats:

    def __init__(self, Buiss_Seat_ID: str, Buiss_Seat_Price: str):
        self.Buiss_Seat_ID = Buiss_Seat_ID
        self.Buiss_Seat_Price = Buiss_Seat_Price
        
        pass
    @property
    def Buiss_Seat_Price(self):
        return self.__Buiss_Seat_Price
    @Buiss_Seat_Price.setter
    def Buiss_Seat_Price(self, Buiss_Seat_Price: str):
        self.__Buiss_Seat_Price = Buiss_Seat_Price

    @property
    def Buiss_Seat_ID(self):
        return self.__Buiss_Seat_ID
    @Buiss_Seat_ID.setter
    def Buiss_Seat_ID(self, Buiss_Seat_ID: str):
        self.__Buiss_Seat_ID = Buiss_Seat_ID



class Economy_Seats:

    def __init__(self, Eco_Seat_ID: str, Eco_Seat_Price: str):
        self.Eco_Seat_ID = Eco_Seat_ID
        self.Eco_Seat_Price = Eco_Seat_Price
        
        pass
    @property
    def Eco_Seat_ID(self):
        return self.__Eco_Seat_ID
    @Eco_Seat_ID.setter
    def Eco_Seat_ID(self, Eco_Seat_ID: str):
        self.__Eco_Seat_ID = Eco_Seat_ID

    @property
    def Eco_Seat_Price(self):
        return self.__Eco_Seat_Price
    @Eco_Seat_Price.setter
    def Eco_Seat_Price(self, Eco_Seat_Price: str):
        self.__Eco_Seat_Price = Eco_Seat_Price



class Seats:

    def __init__(self, Seat_ID: str, Seat_NO: str, Seat_Catoegry: str, passengers29: "Passengers" = None):
        self.Seat_ID = Seat_ID
        self.Seat_NO = Seat_NO
        self.Seat_Catoegry = Seat_Catoegry
        self.passengers29 = passengers29
        
        pass
    @property
    def Seat_ID(self):
        return self.__Seat_ID
    @Seat_ID.setter
    def Seat_ID(self, Seat_ID: str):
        self.__Seat_ID = Seat_ID

    @property
    def Seat_NO(self):
        return self.__Seat_NO
    @Seat_NO.setter
    def Seat_NO(self, Seat_NO: str):
        self.__Seat_NO = Seat_NO

    @property
    def Seat_Catoegry(self):
        return self.__Seat_Catoegry
    @Seat_Catoegry.setter
    def Seat_Catoegry(self, Seat_Catoegry: str):
        self.__Seat_Catoegry = Seat_Catoegry

    @property
    def passengers29(self):
        return self.__passengers29
    @passengers29.setter
    def passengers29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Seats__passengers29", None)
        self.__passengers29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seats28"):
                opp_val = getattr(old_value, "seats28", None)
                if opp_val == self:
                    setattr(old_value, "seats28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seats28"):
                opp_val = getattr(value, "seats28", None)
                setattr(value, "seats28", self)



class Infant:

    def __init__(self, Infant_No: str, Infant_Seat_Price: str):
        self.Infant_No = Infant_No
        self.Infant_Seat_Price = Infant_Seat_Price
        
        pass
    @property
    def Infant_No(self):
        return self.__Infant_No
    @Infant_No.setter
    def Infant_No(self, Infant_No: str):
        self.__Infant_No = Infant_No

    @property
    def Infant_Seat_Price(self):
        return self.__Infant_Seat_Price
    @Infant_Seat_Price.setter
    def Infant_Seat_Price(self, Infant_Seat_Price: str):
        self.__Infant_Seat_Price = Infant_Seat_Price



class Child:

    def __init__(self, Child_ID: str, Child_Seat_Price: str):
        self.Child_ID = Child_ID
        self.Child_Seat_Price = Child_Seat_Price
        
        pass
    @property
    def Child_ID(self):
        return self.__Child_ID
    @Child_ID.setter
    def Child_ID(self, Child_ID: str):
        self.__Child_ID = Child_ID

    @property
    def Child_Seat_Price(self):
        return self.__Child_Seat_Price
    @Child_Seat_Price.setter
    def Child_Seat_Price(self, Child_Seat_Price: str):
        self.__Child_Seat_Price = Child_Seat_Price



class Adult:

    def __init__(self, Adult_ID: str, Adult_Seat_Price: str):
        self.Adult_ID = Adult_ID
        self.Adult_Seat_Price = Adult_Seat_Price
        
        pass
    @property
    def Adult_ID(self):
        return self.__Adult_ID
    @Adult_ID.setter
    def Adult_ID(self, Adult_ID: str):
        self.__Adult_ID = Adult_ID

    @property
    def Adult_Seat_Price(self):
        return self.__Adult_Seat_Price
    @Adult_Seat_Price.setter
    def Adult_Seat_Price(self, Adult_Seat_Price: str):
        self.__Adult_Seat_Price = Adult_Seat_Price



class Offers:

    def __init__(self, Offer_NO: str, Offer_Det: str, Offer_Expiry_Date: str, passengers25: "Passengers" = None):
        self.Offer_NO = Offer_NO
        self.Offer_Det = Offer_Det
        self.Offer_Expiry_Date = Offer_Expiry_Date
        self.passengers25 = passengers25
        
        pass
    @property
    def Offer_NO(self):
        return self.__Offer_NO
    @Offer_NO.setter
    def Offer_NO(self, Offer_NO: str):
        self.__Offer_NO = Offer_NO

    @property
    def Offer_Det(self):
        return self.__Offer_Det
    @Offer_Det.setter
    def Offer_Det(self, Offer_Det: str):
        self.__Offer_Det = Offer_Det

    @property
    def Offer_Expiry_Date(self):
        return self.__Offer_Expiry_Date
    @Offer_Expiry_Date.setter
    def Offer_Expiry_Date(self, Offer_Expiry_Date: str):
        self.__Offer_Expiry_Date = Offer_Expiry_Date

    @property
    def passengers25(self):
        return self.__passengers25
    @passengers25.setter
    def passengers25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Offers__passengers25", None)
        self.__passengers25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "offers24"):
                opp_val = getattr(old_value, "offers24", None)
                if opp_val == self:
                    setattr(old_value, "offers24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "offers24"):
                opp_val = getattr(value, "offers24", None)
                setattr(value, "offers24", self)



class FFP_Members:

    def __init__(self, FFP_ID: str, FFP_Category: str, FFP_Qmiles: str, passengers27: "Passengers" = None):
        self.FFP_ID = FFP_ID
        self.FFP_Category = FFP_Category
        self.FFP_Qmiles = FFP_Qmiles
        self.passengers27 = passengers27
        
        pass
    @property
    def FFP_Category(self):
        return self.__FFP_Category
    @FFP_Category.setter
    def FFP_Category(self, FFP_Category: str):
        self.__FFP_Category = FFP_Category

    @property
    def FFP_ID(self):
        return self.__FFP_ID
    @FFP_ID.setter
    def FFP_ID(self, FFP_ID: str):
        self.__FFP_ID = FFP_ID

    @property
    def FFP_Qmiles(self):
        return self.__FFP_Qmiles
    @FFP_Qmiles.setter
    def FFP_Qmiles(self, FFP_Qmiles: str):
        self.__FFP_Qmiles = FFP_Qmiles

    @property
    def passengers27(self):
        return self.__passengers27
    @passengers27.setter
    def passengers27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FFP_Members__passengers27", None)
        self.__passengers27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fFP_Members26"):
                opp_val = getattr(old_value, "fFP_Members26", None)
                if opp_val == self:
                    setattr(old_value, "fFP_Members26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fFP_Members26"):
                opp_val = getattr(value, "fFP_Members26", None)
                setattr(value, "fFP_Members26", self)



class Flight:

    def __init__(self, Flgt_NO: str, Flgt_Details: str, qaboos_Airways19: "Qaboos_Airways" = None, passengers23: "Passengers" = None):
        self.Flgt_NO = Flgt_NO
        self.Flgt_Details = Flgt_Details
        self.qaboos_Airways19 = qaboos_Airways19
        self.passengers23 = passengers23
        
        pass
    @property
    def Flgt_Details(self):
        return self.__Flgt_Details
    @Flgt_Details.setter
    def Flgt_Details(self, Flgt_Details: str):
        self.__Flgt_Details = Flgt_Details

    @property
    def Flgt_NO(self):
        return self.__Flgt_NO
    @Flgt_NO.setter
    def Flgt_NO(self, Flgt_NO: str):
        self.__Flgt_NO = Flgt_NO

    @property
    def passengers23(self):
        return self.__passengers23
    @passengers23.setter
    def passengers23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Flight__passengers23", None)
        self.__passengers23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flight22"):
                opp_val = getattr(old_value, "flight22", None)
                if opp_val == self:
                    setattr(old_value, "flight22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flight22"):
                opp_val = getattr(value, "flight22", None)
                setattr(value, "flight22", self)

    @property
    def qaboos_Airways19(self):
        return self.__qaboos_Airways19
    @qaboos_Airways19.setter
    def qaboos_Airways19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Flight__qaboos_Airways19", None)
        self.__qaboos_Airways19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flight18"):
                opp_val = getattr(old_value, "flight18", None)
                if opp_val == self:
                    setattr(old_value, "flight18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flight18"):
                opp_val = getattr(value, "flight18", None)
                setattr(value, "flight18", self)



class Passengers:

    def __init__(self, passenger_name: str, Passenger_TKT_No: str, Passenger_Details: str, qaboos_Airways21: "Qaboos_Airways" = None, flight22: "Flight" = None, offers24: "Offers" = None, fFP_Members26: "FFP_Members" = None, seats28: "Seats" = None):
        self.passenger_name = passenger_name
        self.Passenger_TKT_No = Passenger_TKT_No
        self.Passenger_Details = Passenger_Details
        self.qaboos_Airways21 = qaboos_Airways21
        self.flight22 = flight22
        self.offers24 = offers24
        self.fFP_Members26 = fFP_Members26
        self.seats28 = seats28
        
        pass
    @property
    def passenger_name(self):
        return self.__passenger_name
    @passenger_name.setter
    def passenger_name(self, passenger_name: str):
        self.__passenger_name = passenger_name

    @property
    def Passenger_TKT_No(self):
        return self.__Passenger_TKT_No
    @Passenger_TKT_No.setter
    def Passenger_TKT_No(self, Passenger_TKT_No: str):
        self.__Passenger_TKT_No = Passenger_TKT_No

    @property
    def Passenger_Details(self):
        return self.__Passenger_Details
    @Passenger_Details.setter
    def Passenger_Details(self, Passenger_Details: str):
        self.__Passenger_Details = Passenger_Details

    @property
    def offers24(self):
        return self.__offers24
    @offers24.setter
    def offers24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Passengers__offers24", None)
        self.__offers24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "passengers25"):
                opp_val = getattr(old_value, "passengers25", None)
                if opp_val == self:
                    setattr(old_value, "passengers25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "passengers25"):
                opp_val = getattr(value, "passengers25", None)
                setattr(value, "passengers25", self)

    @property
    def flight22(self):
        return self.__flight22
    @flight22.setter
    def flight22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Passengers__flight22", None)
        self.__flight22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "passengers23"):
                opp_val = getattr(old_value, "passengers23", None)
                if opp_val == self:
                    setattr(old_value, "passengers23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "passengers23"):
                opp_val = getattr(value, "passengers23", None)
                setattr(value, "passengers23", self)

    @property
    def fFP_Members26(self):
        return self.__fFP_Members26
    @fFP_Members26.setter
    def fFP_Members26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Passengers__fFP_Members26", None)
        self.__fFP_Members26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "passengers27"):
                opp_val = getattr(old_value, "passengers27", None)
                if opp_val == self:
                    setattr(old_value, "passengers27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "passengers27"):
                opp_val = getattr(value, "passengers27", None)
                setattr(value, "passengers27", self)

    @property
    def seats28(self):
        return self.__seats28
    @seats28.setter
    def seats28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Passengers__seats28", None)
        self.__seats28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "passengers29"):
                opp_val = getattr(old_value, "passengers29", None)
                if opp_val == self:
                    setattr(old_value, "passengers29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "passengers29"):
                opp_val = getattr(value, "passengers29", None)
                setattr(value, "passengers29", self)

    @property
    def qaboos_Airways21(self):
        return self.__qaboos_Airways21
    @qaboos_Airways21.setter
    def qaboos_Airways21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Passengers__qaboos_Airways21", None)
        self.__qaboos_Airways21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "passengers20"):
                opp_val = getattr(old_value, "passengers20", None)
                if opp_val == self:
                    setattr(old_value, "passengers20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "passengers20"):
                opp_val = getattr(value, "passengers20", None)
                setattr(value, "passengers20", self)



class Qaboos_Airways:

    def __init__(self, Comp_Commercial_NO: str, Comp_location: str, flight18: "Flight" = None, passengers20: "Passengers" = None):
        self.Comp_Commercial_NO = Comp_Commercial_NO
        self.Comp_location = Comp_location
        self.flight18 = flight18
        self.passengers20 = passengers20
        
        pass
    @property
    def Comp_location(self):
        return self.__Comp_location
    @Comp_location.setter
    def Comp_location(self, Comp_location: str):
        self.__Comp_location = Comp_location

    @property
    def Comp_Commercial_NO(self):
        return self.__Comp_Commercial_NO
    @Comp_Commercial_NO.setter
    def Comp_Commercial_NO(self, Comp_Commercial_NO: str):
        self.__Comp_Commercial_NO = Comp_Commercial_NO

    @property
    def passengers20(self):
        return self.__passengers20
    @passengers20.setter
    def passengers20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Qaboos_Airways__passengers20", None)
        self.__passengers20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qaboos_Airways21"):
                opp_val = getattr(old_value, "qaboos_Airways21", None)
                if opp_val == self:
                    setattr(old_value, "qaboos_Airways21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qaboos_Airways21"):
                opp_val = getattr(value, "qaboos_Airways21", None)
                setattr(value, "qaboos_Airways21", self)

    @property
    def flight18(self):
        return self.__flight18
    @flight18.setter
    def flight18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Qaboos_Airways__flight18", None)
        self.__flight18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qaboos_Airways19"):
                opp_val = getattr(old_value, "qaboos_Airways19", None)
                if opp_val == self:
                    setattr(old_value, "qaboos_Airways19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qaboos_Airways19"):
                opp_val = getattr(value, "qaboos_Airways19", None)
                setattr(value, "qaboos_Airways19", self)

