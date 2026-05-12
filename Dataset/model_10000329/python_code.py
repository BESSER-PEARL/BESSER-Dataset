from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Date(Enum):
    pass
class ReservationType(Enum):
    pass
class ReservationType2(Enum):
    pass

############################################
# Definition of Classes
############################################










class Online_Customer:

    pass


class Staff:

    def __init__(self, Staff_ID: str, Name: str, JobType: str, Phone: str):
        self.Staff_ID = Staff_ID
        self.Name = Name
        self.JobType = JobType
        self.Phone = Phone
        
        pass
    @property
    def Staff_ID(self):
        return self.__Staff_ID
    @Staff_ID.setter
    def Staff_ID(self, Staff_ID: str):
        self.__Staff_ID = Staff_ID

    @property
    def JobType(self):
        return self.__JobType
    @JobType.setter
    def JobType(self, JobType: str):
        self.__JobType = JobType

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
    def Phone(self, Phone: str):
        self.__Phone = Phone



class Payment:

    pass


class Bill:

    def __init__(self, Tax: int, Tip: int, TotalAmount: int, waiter7: "Waiter" = None):
        self.Tax = Tax
        self.Tip = Tip
        self.TotalAmount = TotalAmount
        self.waiter7 = waiter7
        
        pass
    @property
    def TotalAmount(self):
        return self.__TotalAmount
    @TotalAmount.setter
    def TotalAmount(self, TotalAmount: int):
        self.__TotalAmount = TotalAmount

    @property
    def Tax(self):
        return self.__Tax
    @Tax.setter
    def Tax(self, Tax: int):
        self.__Tax = Tax

    @property
    def Tip(self):
        return self.__Tip
    @Tip.setter
    def Tip(self, Tip: int):
        self.__Tip = Tip

    @property
    def waiter7(self):
        return self.__waiter7
    @waiter7.setter
    def waiter7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bill__waiter7", None)
        self.__waiter7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bill6"):
                opp_val = getattr(old_value, "bill6", None)
                if opp_val == self:
                    setattr(old_value, "bill6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bill6"):
                opp_val = getattr(value, "bill6", None)
                setattr(value, "bill6", self)



class Party:

    def __init__(self, Number_of_Guests: int, Number_Of_Adults: int, Number_Of_Children: int):
        self.Number_of_Guests = Number_of_Guests
        self.Number_Of_Adults = Number_Of_Adults
        self.Number_Of_Children = Number_Of_Children
        
        pass
    @property
    def Number_of_Guests(self):
        return self.__Number_of_Guests
    @Number_of_Guests.setter
    def Number_of_Guests(self, Number_of_Guests: int):
        self.__Number_of_Guests = Number_of_Guests

    @property
    def Number_Of_Adults(self):
        return self.__Number_Of_Adults
    @Number_Of_Adults.setter
    def Number_Of_Adults(self, Number_Of_Adults: int):
        self.__Number_Of_Adults = Number_Of_Adults

    @property
    def Number_Of_Children(self):
        return self.__Number_Of_Children
    @Number_Of_Children.setter
    def Number_Of_Children(self, Number_Of_Children: int):
        self.__Number_Of_Children = Number_Of_Children



class Table:

    def __init__(self, Capacity: int, TableID: str, waiter9: "Waiter" = None, reservation11: "Reservation" = None):
        self.Capacity = Capacity
        self.TableID = TableID
        self.waiter9 = waiter9
        self.reservation11 = reservation11
        
        pass
    @property
    def TableID(self):
        return self.__TableID
    @TableID.setter
    def TableID(self, TableID: str):
        self.__TableID = TableID

    @property
    def Capacity(self):
        return self.__Capacity
    @Capacity.setter
    def Capacity(self, Capacity: int):
        self.__Capacity = Capacity

    @property
    def waiter9(self):
        return self.__waiter9
    @waiter9.setter
    def waiter9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Table__waiter9", None)
        self.__waiter9 = value
        
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
    def reservation11(self):
        return self.__reservation11
    @reservation11.setter
    def reservation11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Table__reservation11", None)
        self.__reservation11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "table10"):
                opp_val = getattr(old_value, "table10", None)
                if opp_val == self:
                    setattr(old_value, "table10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "table10"):
                opp_val = getattr(value, "table10", None)
                setattr(value, "table10", self)



class Reservation:

    def __init__(self, Date: Date, Time: str, ReservationID: str, host1: "Host" = None, table10: "Table" = None):
        self.Date = Date
        self.Time = Time
        self.ReservationID = ReservationID
        self.host1 = host1
        self.table10 = table10
        
        pass
    @property
    def Time(self):
        return self.__Time
    @Time.setter
    def Time(self, Time: str):
        self.__Time = Time

    @property
    def Date(self):
        return self.__Date
    @Date.setter
    def Date(self, Date: Date):
        self.__Date = Date

    @property
    def ReservationID(self):
        return self.__ReservationID
    @ReservationID.setter
    def ReservationID(self, ReservationID: str):
        self.__ReservationID = ReservationID

    @property
    def table10(self):
        return self.__table10
    @table10.setter
    def table10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Reservation__table10", None)
        self.__table10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reservation11"):
                opp_val = getattr(old_value, "reservation11", None)
                if opp_val == self:
                    setattr(old_value, "reservation11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reservation11"):
                opp_val = getattr(value, "reservation11", None)
                setattr(value, "reservation11", self)

    @property
    def host1(self):
        return self.__host1
    @host1.setter
    def host1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Reservation__host1", None)
        self.__host1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reservation0"):
                opp_val = getattr(old_value, "reservation0", None)
                if opp_val == self:
                    setattr(old_value, "reservation0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reservation0"):
                opp_val = getattr(value, "reservation0", None)
                setattr(value, "reservation0", self)



class Kitchen:

    pass


class Guest:

    def __init__(self, Name: str, Phone: str, Guest_ID: str):
        self.Name = Name
        self.Phone = Phone
        self.Guest_ID = Guest_ID
        
        pass
    @property
    def Guest_ID(self):
        return self.__Guest_ID
    @Guest_ID.setter
    def Guest_ID(self, Guest_ID: str):
        self.__Guest_ID = Guest_ID

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
    def Phone(self, Phone: str):
        self.__Phone = Phone



class Order:

    pass


class Host:

    pass


class Waiter:

    pass
