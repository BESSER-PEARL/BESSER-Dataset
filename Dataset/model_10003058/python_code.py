from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Ticket:

    def __init__(self, Id: int, Price: bool, Customer_Name: str, Type: str, Owner4: "Customer" = None, flight6: "Flight" = None):
        self.Id = Id
        self.Price = Price
        self.Customer_Name = Customer_Name
        self.Type = Type
        self.Owner4 = Owner4
        self.flight6 = flight6
        
        pass
    @property
    def Customer_Name(self):
        return self.__Customer_Name
    @Customer_Name.setter
    def Customer_Name(self, Customer_Name: str):
        self.__Customer_Name = Customer_Name

    @property
    def Id(self):
        return self.__Id
    @Id.setter
    def Id(self, Id: int):
        self.__Id = Id

    @property
    def Type(self):
        return self.__Type
    @Type.setter
    def Type(self, Type: str):
        self.__Type = Type

    @property
    def Price(self):
        return self.__Price
    @Price.setter
    def Price(self, Price: bool):
        self.__Price = Price

    @property
    def flight6(self):
        return self.__flight6
    @flight6.setter
    def flight6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ticket__flight6", None)
        self.__flight6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ticket7"):
                opp_val = getattr(old_value, "ticket7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ticket7"):
                opp_val = getattr(value, "ticket7", None)
                if opp_val is None:
                    setattr(value, "ticket7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Owner4(self):
        return self.__Owner4
    @Owner4.setter
    def Owner4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ticket__Owner4", None)
        self.__Owner4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Owns5"):
                opp_val = getattr(old_value, "Owns5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Owns5"):
                opp_val = getattr(value, "Owns5", None)
                if opp_val is None:
                    setattr(value, "Owns5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Administrator:

    def __init__(self, Fullname: str, Account: str, Manage1: set["Customer"] = None):
        self.Fullname = Fullname
        self.Account = Account
        self.Manage1 = Manage1 if Manage1 is not None else set()
        
        pass
    @property
    def Fullname(self):
        return self.__Fullname
    @Fullname.setter
    def Fullname(self, Fullname: str):
        self.__Fullname = Fullname

    @property
    def Account(self):
        return self.__Account
    @Account.setter
    def Account(self, Account: str):
        self.__Account = Account

    @property
    def Manage1(self):
        return self.__Manage1
    @Manage1.setter
    def Manage1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Administrator__Manage1", None)
        self.__Manage1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Request0"):
                    opp_val = getattr(item, "Request0", None)
                    
                    if opp_val == self:
                        setattr(item, "Request0", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Request0"):
                    opp_val = getattr(item, "Request0", None)
                    
                    setattr(item, "Request0", self)
                    



class Flight:

    def __init__(self, Number_of_seats: int, Name: str, Id: Flight, Destination: str, Time: int, Source: str, ticket7: set["Ticket"] = None):
        self.Number_of_seats = Number_of_seats
        self.Name = Name
        self.Id = Id
        self.Destination = Destination
        self.Time = Time
        self.Source = Source
        self.ticket7 = ticket7 if ticket7 is not None else set()
        
        pass
    @property
    def Source(self):
        return self.__Source
    @Source.setter
    def Source(self, Source: str):
        self.__Source = Source

    @property
    def Destination(self):
        return self.__Destination
    @Destination.setter
    def Destination(self, Destination: str):
        self.__Destination = Destination

    @property
    def Number_of_seats(self):
        return self.__Number_of_seats
    @Number_of_seats.setter
    def Number_of_seats(self, Number_of_seats: int):
        self.__Number_of_seats = Number_of_seats

    @property
    def Time(self):
        return self.__Time
    @Time.setter
    def Time(self, Time: int):
        self.__Time = Time

    @property
    def Id(self):
        return self.__Id
    @Id.setter
    def Id(self, Id: Flight):
        self.__Id = Id

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def ticket7(self):
        return self.__ticket7
    @ticket7.setter
    def ticket7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Flight__ticket7", None)
        self.__ticket7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "flight6"):
                    opp_val = getattr(item, "flight6", None)
                    
                    if opp_val == self:
                        setattr(item, "flight6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "flight6"):
                    opp_val = getattr(item, "flight6", None)
                    
                    setattr(item, "flight6", self)
                    



class Bank:

    def __init__(self, Name: str, Account: int, customer2: set["Customer"] = None):
        self.Name = Name
        self.Account = Account
        self.customer2 = customer2 if customer2 is not None else set()
        
        pass
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Account(self):
        return self.__Account
    @Account.setter
    def Account(self, Account: int):
        self.__Account = Account

    @property
    def customer2(self):
        return self.__customer2
    @customer2.setter
    def customer2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bank__customer2", None)
        self.__customer2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bank3"):
                    opp_val = getattr(item, "bank3", None)
                    
                    if opp_val == self:
                        setattr(item, "bank3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bank3"):
                    opp_val = getattr(item, "bank3", None)
                    
                    setattr(item, "bank3", self)
                    



class Customer:

    def __init__(self, Fullname: str, Location: str, Card_details: int, Gender: str, Request0: "Administrator" = None, bank3: "Bank" = None, Owns5: set["Ticket"] = None):
        self.Fullname = Fullname
        self.Location = Location
        self.Card_details = Card_details
        self.Gender = Gender
        self.Request0 = Request0
        self.bank3 = bank3
        self.Owns5 = Owns5 if Owns5 is not None else set()
        
        pass
    @property
    def Fullname(self):
        return self.__Fullname
    @Fullname.setter
    def Fullname(self, Fullname: str):
        self.__Fullname = Fullname

    @property
    def Card_details(self):
        return self.__Card_details
    @Card_details.setter
    def Card_details(self, Card_details: int):
        self.__Card_details = Card_details

    @property
    def Location(self):
        return self.__Location
    @Location.setter
    def Location(self, Location: str):
        self.__Location = Location

    @property
    def Gender(self):
        return self.__Gender
    @Gender.setter
    def Gender(self, Gender: str):
        self.__Gender = Gender

    @property
    def Owns5(self):
        return self.__Owns5
    @Owns5.setter
    def Owns5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__Owns5", None)
        self.__Owns5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Owner4"):
                    opp_val = getattr(item, "Owner4", None)
                    
                    if opp_val == self:
                        setattr(item, "Owner4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Owner4"):
                    opp_val = getattr(item, "Owner4", None)
                    
                    setattr(item, "Owner4", self)
                    

    @property
    def bank3(self):
        return self.__bank3
    @bank3.setter
    def bank3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__bank3", None)
        self.__bank3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer2"):
                opp_val = getattr(old_value, "customer2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer2"):
                opp_val = getattr(value, "customer2", None)
                if opp_val is None:
                    setattr(value, "customer2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Request0(self):
        return self.__Request0
    @Request0.setter
    def Request0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__Request0", None)
        self.__Request0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Manage1"):
                opp_val = getattr(old_value, "Manage1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Manage1"):
                opp_val = getattr(value, "Manage1", None)
                if opp_val is None:
                    setattr(value, "Manage1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

