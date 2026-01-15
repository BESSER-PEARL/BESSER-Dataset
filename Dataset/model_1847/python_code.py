from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class timetrack_TimeEntry:

    def __init__(self, duration: date, factured: bool, notes: str, sync_date: date, day: date, from: date, till: date, timetrack_TimeEntry7: "timetrack_Library" = None, timetrack_TimeEntry: "timetrack_User" = None, timetrack_TimeEntry2: "timetrack_Project" = None):
        self.duration = duration
        self.factured = factured
        self.notes = notes
        self.sync_date = sync_date
        self.day = day
        self.from = from
        self.till = till
        self.timetrack_TimeEntry7 = timetrack_TimeEntry7
        self.timetrack_TimeEntry = timetrack_TimeEntry
        self.timetrack_TimeEntry2 = timetrack_TimeEntry2
        
    @property
    def from(self) -> date:
        return self.__from

    @from.setter
    def from(self, from: date):
        self.__from = from

    @property
    def till(self) -> date:
        return self.__till

    @till.setter
    def till(self, till: date):
        self.__till = till

    @property
    def duration(self) -> date:
        return self.__duration

    @duration.setter
    def duration(self, duration: date):
        self.__duration = duration

    @property
    def notes(self) -> str:
        return self.__notes

    @notes.setter
    def notes(self, notes: str):
        self.__notes = notes

    @property
    def day(self) -> date:
        return self.__day

    @day.setter
    def day(self, day: date):
        self.__day = day

    @property
    def factured(self) -> bool:
        return self.__factured

    @factured.setter
    def factured(self, factured: bool):
        self.__factured = factured

    @property
    def sync_date(self) -> date:
        return self.__sync_date

    @sync_date.setter
    def sync_date(self, sync_date: date):
        self.__sync_date = sync_date

    @property
    def timetrack_TimeEntry2(self):
        return self.__timetrack_TimeEntry2

    @timetrack_TimeEntry2.setter
    def timetrack_TimeEntry2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_timetrack_TimeEntry__timetrack_TimeEntry2", None)
        self.__timetrack_TimeEntry2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "timetrack_Project"):
                opp_val = getattr(old_value, "timetrack_Project", None)
                if opp_val == self:
                    setattr(old_value, "timetrack_Project", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "timetrack_Project"):
                opp_val = getattr(value, "timetrack_Project", None)
                setattr(value, "timetrack_Project", self)

    @property
    def timetrack_TimeEntry7(self):
        return self.__timetrack_TimeEntry7

    @timetrack_TimeEntry7.setter
    def timetrack_TimeEntry7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_timetrack_TimeEntry__timetrack_TimeEntry7", None)
        self.__timetrack_TimeEntry7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "timetrack_Library6"):
                opp_val = getattr(old_value, "timetrack_Library6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "timetrack_Library6"):
                opp_val = getattr(value, "timetrack_Library6", None)
                if opp_val is None:
                    setattr(value, "timetrack_Library6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def timetrack_TimeEntry(self):
        return self.__timetrack_TimeEntry

    @timetrack_TimeEntry.setter
    def timetrack_TimeEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_timetrack_TimeEntry__timetrack_TimeEntry", None)
        self.__timetrack_TimeEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "timetrack_User"):
                opp_val = getattr(old_value, "timetrack_User", None)
                if opp_val == self:
                    setattr(old_value, "timetrack_User", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "timetrack_User"):
                opp_val = getattr(value, "timetrack_User", None)
                setattr(value, "timetrack_User", self)

class timetrack_Project:

    def __init__(self, number: str, name: str, timetrack_Project: "timetrack_TimeEntry" = None, timetrack_Project10: "timetrack_Library" = None):
        self.number = number
        self.name = name
        self.timetrack_Project = timetrack_Project
        self.timetrack_Project10 = timetrack_Project10
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def number(self) -> str:
        return self.__number

    @number.setter
    def number(self, number: str):
        self.__number = number

    @property
    def timetrack_Project(self):
        return self.__timetrack_Project

    @timetrack_Project.setter
    def timetrack_Project(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_timetrack_Project__timetrack_Project", None)
        self.__timetrack_Project = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "timetrack_TimeEntry2"):
                opp_val = getattr(old_value, "timetrack_TimeEntry2", None)
                if opp_val == self:
                    setattr(old_value, "timetrack_TimeEntry2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "timetrack_TimeEntry2"):
                opp_val = getattr(value, "timetrack_TimeEntry2", None)
                setattr(value, "timetrack_TimeEntry2", self)

    @property
    def timetrack_Project10(self):
        return self.__timetrack_Project10

    @timetrack_Project10.setter
    def timetrack_Project10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_timetrack_Project__timetrack_Project10", None)
        self.__timetrack_Project10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "timetrack_Library9"):
                opp_val = getattr(old_value, "timetrack_Library9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "timetrack_Library9"):
                opp_val = getattr(value, "timetrack_Library9", None)
                if opp_val is None:
                    setattr(value, "timetrack_Library9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class timetrack_User:

    def __init__(self, name: str, password: str, sap_name: str, sap_password: str, timetrack_User4: "timetrack_Library" = None, timetrack_User: "timetrack_TimeEntry" = None):
        self.name = name
        self.password = password
        self.sap_name = sap_name
        self.sap_password = sap_password
        self.timetrack_User4 = timetrack_User4
        self.timetrack_User = timetrack_User
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def sap_name(self) -> str:
        return self.__sap_name

    @sap_name.setter
    def sap_name(self, sap_name: str):
        self.__sap_name = sap_name

    @property
    def sap_password(self) -> str:
        return self.__sap_password

    @sap_password.setter
    def sap_password(self, sap_password: str):
        self.__sap_password = sap_password

    @property
    def timetrack_User(self):
        return self.__timetrack_User

    @timetrack_User.setter
    def timetrack_User(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_timetrack_User__timetrack_User", None)
        self.__timetrack_User = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "timetrack_TimeEntry"):
                opp_val = getattr(old_value, "timetrack_TimeEntry", None)
                if opp_val == self:
                    setattr(old_value, "timetrack_TimeEntry", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "timetrack_TimeEntry"):
                opp_val = getattr(value, "timetrack_TimeEntry", None)
                setattr(value, "timetrack_TimeEntry", self)

    @property
    def timetrack_User4(self):
        return self.__timetrack_User4

    @timetrack_User4.setter
    def timetrack_User4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_timetrack_User__timetrack_User4", None)
        self.__timetrack_User4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "timetrack_Library"):
                opp_val = getattr(old_value, "timetrack_Library", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "timetrack_Library"):
                opp_val = getattr(value, "timetrack_Library", None)
                if opp_val is None:
                    setattr(value, "timetrack_Library", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class timetrack_Library:

    pass