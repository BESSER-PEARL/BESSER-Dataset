from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Flight:

    def __init__(self, Id: str, Company: str, Origin: str, Destination: str, Time: str, Max_Passangers: int, Ticket_Flight_111: set["Ticket"] = None):
        self.Id = Id
        self.Company = Company
        self.Origin = Origin
        self.Destination = Destination
        self.Time = Time
        self.Max_Passangers = Max_Passangers
        self.Ticket_Flight_111 = Ticket_Flight_111 if Ticket_Flight_111 is not None else set()
        
        pass
    @property
    def Id(self):
        return self.__Id
    @Id.setter
    def Id(self, Id: str):
        self.__Id = Id

    @property
    def Origin(self):
        return self.__Origin
    @Origin.setter
    def Origin(self, Origin: str):
        self.__Origin = Origin

    @property
    def Company(self):
        return self.__Company
    @Company.setter
    def Company(self, Company: str):
        self.__Company = Company

    @property
    def Max_Passangers(self):
        return self.__Max_Passangers
    @Max_Passangers.setter
    def Max_Passangers(self, Max_Passangers: int):
        self.__Max_Passangers = Max_Passangers

    @property
    def Time(self):
        return self.__Time
    @Time.setter
    def Time(self, Time: str):
        self.__Time = Time

    @property
    def Destination(self):
        return self.__Destination
    @Destination.setter
    def Destination(self, Destination: str):
        self.__Destination = Destination

    @property
    def Ticket_Flight_111(self):
        return self.__Ticket_Flight_111
    @Ticket_Flight_111.setter
    def Ticket_Flight_111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Flight__Ticket_Flight_111", None)
        self.__Ticket_Flight_111 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Ticket_Flight_010"):
                    opp_val = getattr(item, "Ticket_Flight_010", None)
                    
                    if opp_val == self:
                        setattr(item, "Ticket_Flight_010", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Ticket_Flight_010"):
                    opp_val = getattr(item, "Ticket_Flight_010", None)
                    
                    setattr(item, "Ticket_Flight_010", self)
                    



class Answer:

    pass


class Ticket:

    def __init__(self, Id: str, Clients: Client, Seat: str, Booking_Class: str, Client_Ticket_15: "Client" = None, Booking_Ticket_17: "Booking" = None, Ticket_Flight_010: "Flight" = None):
        self.Id = Id
        self.Clients = Clients
        self.Seat = Seat
        self.Booking_Class = Booking_Class
        self.Client_Ticket_15 = Client_Ticket_15
        self.Booking_Ticket_17 = Booking_Ticket_17
        self.Ticket_Flight_010 = Ticket_Flight_010
        
        pass
    @property
    def Clients(self):
        return self.__Clients
    @Clients.setter
    def Clients(self, Clients: Client):
        self.__Clients = Clients

    @property
    def Booking_Class(self):
        return self.__Booking_Class
    @Booking_Class.setter
    def Booking_Class(self, Booking_Class: str):
        self.__Booking_Class = Booking_Class

    @property
    def Seat(self):
        return self.__Seat
    @Seat.setter
    def Seat(self, Seat: str):
        self.__Seat = Seat

    @property
    def Id(self):
        return self.__Id
    @Id.setter
    def Id(self, Id: str):
        self.__Id = Id

    @property
    def Client_Ticket_15(self):
        return self.__Client_Ticket_15
    @Client_Ticket_15.setter
    def Client_Ticket_15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ticket__Client_Ticket_15", None)
        self.__Client_Ticket_15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Client_Ticket_04"):
                opp_val = getattr(old_value, "Client_Ticket_04", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Client_Ticket_04"):
                opp_val = getattr(value, "Client_Ticket_04", None)
                if opp_val is None:
                    setattr(value, "Client_Ticket_04", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Ticket_Flight_010(self):
        return self.__Ticket_Flight_010
    @Ticket_Flight_010.setter
    def Ticket_Flight_010(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ticket__Ticket_Flight_010", None)
        self.__Ticket_Flight_010 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Ticket_Flight_111"):
                opp_val = getattr(old_value, "Ticket_Flight_111", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Ticket_Flight_111"):
                opp_val = getattr(value, "Ticket_Flight_111", None)
                if opp_val is None:
                    setattr(value, "Ticket_Flight_111", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Booking_Ticket_17(self):
        return self.__Booking_Ticket_17
    @Booking_Ticket_17.setter
    def Booking_Ticket_17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ticket__Booking_Ticket_17", None)
        self.__Booking_Ticket_17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Booking_Ticket_06"):
                opp_val = getattr(old_value, "Booking_Ticket_06", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Booking_Ticket_06"):
                opp_val = getattr(value, "Booking_Ticket_06", None)
                if opp_val is None:
                    setattr(value, "Booking_Ticket_06", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Booking:

    def __init__(self, Id: str, Tickets: Ticket, Luggage: str, Origin: str, Destination: str, Time: str, Booking_Ticket_06: set["Ticket"] = None, One_clinet_makes_the_booking_9: "Client" = None):
        self.Id = Id
        self.Tickets = Tickets
        self.Luggage = Luggage
        self.Origin = Origin
        self.Destination = Destination
        self.Time = Time
        self.Booking_Ticket_06 = Booking_Ticket_06 if Booking_Ticket_06 is not None else set()
        self.One_clinet_makes_the_booking_9 = One_clinet_makes_the_booking_9
        
        pass
    @property
    def Origin(self):
        return self.__Origin
    @Origin.setter
    def Origin(self, Origin: str):
        self.__Origin = Origin

    @property
    def Luggage(self):
        return self.__Luggage
    @Luggage.setter
    def Luggage(self, Luggage: str):
        self.__Luggage = Luggage

    @property
    def Tickets(self):
        return self.__Tickets
    @Tickets.setter
    def Tickets(self, Tickets: Ticket):
        self.__Tickets = Tickets

    @property
    def Destination(self):
        return self.__Destination
    @Destination.setter
    def Destination(self, Destination: str):
        self.__Destination = Destination

    @property
    def Time(self):
        return self.__Time
    @Time.setter
    def Time(self, Time: str):
        self.__Time = Time

    @property
    def Id(self):
        return self.__Id
    @Id.setter
    def Id(self, Id: str):
        self.__Id = Id

    @property
    def Booking_Ticket_06(self):
        return self.__Booking_Ticket_06
    @Booking_Ticket_06.setter
    def Booking_Ticket_06(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Booking__Booking_Ticket_06", None)
        self.__Booking_Ticket_06 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Booking_Ticket_17"):
                    opp_val = getattr(item, "Booking_Ticket_17", None)
                    
                    if opp_val == self:
                        setattr(item, "Booking_Ticket_17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Booking_Ticket_17"):
                    opp_val = getattr(item, "Booking_Ticket_17", None)
                    
                    setattr(item, "Booking_Ticket_17", self)
                    

    @property
    def One_clinet_makes_the_booking_9(self):
        return self.__One_clinet_makes_the_booking_9
    @One_clinet_makes_the_booking_9.setter
    def One_clinet_makes_the_booking_9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Booking__One_clinet_makes_the_booking_9", None)
        self.__One_clinet_makes_the_booking_9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Client_Booking_08"):
                opp_val = getattr(old_value, "Client_Booking_08", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Client_Booking_08"):
                opp_val = getattr(value, "Client_Booking_08", None)
                if opp_val is None:
                    setattr(value, "Client_Booking_08", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Client:

    def __init__(self, Id: str, Name: str, Bookings: Booking, Loyalty_card: str, Client_Problem_02: set["Problem"] = None, Client_Ticket_04: set["Ticket"] = None, Client_Booking_08: set["Booking"] = None):
        self.Id = Id
        self.Name = Name
        self.Bookings = Bookings
        self.Loyalty_card = Loyalty_card
        self.Client_Problem_02 = Client_Problem_02 if Client_Problem_02 is not None else set()
        self.Client_Ticket_04 = Client_Ticket_04 if Client_Ticket_04 is not None else set()
        self.Client_Booking_08 = Client_Booking_08 if Client_Booking_08 is not None else set()
        
        pass
    @property
    def Loyalty_card(self):
        return self.__Loyalty_card
    @Loyalty_card.setter
    def Loyalty_card(self, Loyalty_card: str):
        self.__Loyalty_card = Loyalty_card

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
    def Bookings(self):
        return self.__Bookings
    @Bookings.setter
    def Bookings(self, Bookings: Booking):
        self.__Bookings = Bookings

    @property
    def Client_Booking_08(self):
        return self.__Client_Booking_08
    @Client_Booking_08.setter
    def Client_Booking_08(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Client__Client_Booking_08", None)
        self.__Client_Booking_08 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "One_clinet_makes_the_booking_9"):
                    opp_val = getattr(item, "One_clinet_makes_the_booking_9", None)
                    
                    if opp_val == self:
                        setattr(item, "One_clinet_makes_the_booking_9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "One_clinet_makes_the_booking_9"):
                    opp_val = getattr(item, "One_clinet_makes_the_booking_9", None)
                    
                    setattr(item, "One_clinet_makes_the_booking_9", self)
                    

    @property
    def Client_Problem_02(self):
        return self.__Client_Problem_02
    @Client_Problem_02.setter
    def Client_Problem_02(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Client__Client_Problem_02", None)
        self.__Client_Problem_02 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Client_Problem_13"):
                    opp_val = getattr(item, "Client_Problem_13", None)
                    
                    if opp_val == self:
                        setattr(item, "Client_Problem_13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Client_Problem_13"):
                    opp_val = getattr(item, "Client_Problem_13", None)
                    
                    setattr(item, "Client_Problem_13", self)
                    

    @property
    def Client_Ticket_04(self):
        return self.__Client_Ticket_04
    @Client_Ticket_04.setter
    def Client_Ticket_04(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Client__Client_Ticket_04", None)
        self.__Client_Ticket_04 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Client_Ticket_15"):
                    opp_val = getattr(item, "Client_Ticket_15", None)
                    
                    if opp_val == self:
                        setattr(item, "Client_Ticket_15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Client_Ticket_15"):
                    opp_val = getattr(item, "Client_Ticket_15", None)
                    
                    setattr(item, "Client_Ticket_15", self)
                    



class Problem:

    def __init__(self, Id: str, Type: str, Content: str, Answer_Problem_11: set["Answer"] = None, Client_Problem_13: "Client" = None):
        self.Id = Id
        self.Type = Type
        self.Content = Content
        self.Answer_Problem_11 = Answer_Problem_11 if Answer_Problem_11 is not None else set()
        self.Client_Problem_13 = Client_Problem_13
        
        pass
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
    def Content(self):
        return self.__Content
    @Content.setter
    def Content(self, Content: str):
        self.__Content = Content

    @property
    def Client_Problem_13(self):
        return self.__Client_Problem_13
    @Client_Problem_13.setter
    def Client_Problem_13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Problem__Client_Problem_13", None)
        self.__Client_Problem_13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Client_Problem_02"):
                opp_val = getattr(old_value, "Client_Problem_02", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Client_Problem_02"):
                opp_val = getattr(value, "Client_Problem_02", None)
                if opp_val is None:
                    setattr(value, "Client_Problem_02", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Answer_Problem_11(self):
        return self.__Answer_Problem_11
    @Answer_Problem_11.setter
    def Answer_Problem_11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Problem__Answer_Problem_11", None)
        self.__Answer_Problem_11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Answer_Problem_00"):
                    opp_val = getattr(item, "Answer_Problem_00", None)
                    
                    if opp_val == self:
                        setattr(item, "Answer_Problem_00", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Answer_Problem_00"):
                    opp_val = getattr(item, "Answer_Problem_00", None)
                    
                    setattr(item, "Answer_Problem_00", self)
                    

