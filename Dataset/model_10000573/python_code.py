from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class door_alarm_system:

    def __init__(self, door_alarm_system: bool, door_sensor10: set["door_sensor"] = None, eventlog16: "eventlog" = None, control_panel30: "control_panel" = None):
        self.door_alarm_system = door_alarm_system
        self.door_sensor10 = door_sensor10 if door_sensor10 is not None else set()
        self.eventlog16 = eventlog16
        self.control_panel30 = control_panel30
        
        pass
    @property
    def door_alarm_system(self):
        return self.__door_alarm_system
    @door_alarm_system.setter
    def door_alarm_system(self, door_alarm_system: bool):
        self.__door_alarm_system = door_alarm_system

    @property
    def door_sensor10(self):
        return self.__door_sensor10
    @door_sensor10.setter
    def door_sensor10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_door_alarm_system__door_sensor10", None)
        self.__door_sensor10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "door_alarm_system11"):
                    opp_val = getattr(item, "door_alarm_system11", None)
                    
                    if opp_val == self:
                        setattr(item, "door_alarm_system11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "door_alarm_system11"):
                    opp_val = getattr(item, "door_alarm_system11", None)
                    
                    setattr(item, "door_alarm_system11", self)
                    

    @property
    def eventlog16(self):
        return self.__eventlog16
    @eventlog16.setter
    def eventlog16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_door_alarm_system__eventlog16", None)
        self.__eventlog16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "door_alarm_system17"):
                opp_val = getattr(old_value, "door_alarm_system17", None)
                if opp_val == self:
                    setattr(old_value, "door_alarm_system17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "door_alarm_system17"):
                opp_val = getattr(value, "door_alarm_system17", None)
                setattr(value, "door_alarm_system17", self)

    @property
    def control_panel30(self):
        return self.__control_panel30
    @control_panel30.setter
    def control_panel30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_door_alarm_system__control_panel30", None)
        self.__control_panel30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "door_alarm_system31"):
                opp_val = getattr(old_value, "door_alarm_system31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "door_alarm_system31"):
                opp_val = getattr(value, "door_alarm_system31", None)
                if opp_val is None:
                    setattr(value, "door_alarm_system31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class ClassJ:

    pass


class flood_alarm_system:

    def __init__(self, flood_alarm_system: bool, flood_sensor8: set["flood_sensor"] = None, eventlog15: "eventlog" = None, control_panel28: "control_panel" = None):
        self.flood_alarm_system = flood_alarm_system
        self.flood_sensor8 = flood_sensor8 if flood_sensor8 is not None else set()
        self.eventlog15 = eventlog15
        self.control_panel28 = control_panel28
        
        pass
    @property
    def flood_alarm_system(self):
        return self.__flood_alarm_system
    @flood_alarm_system.setter
    def flood_alarm_system(self, flood_alarm_system: bool):
        self.__flood_alarm_system = flood_alarm_system

    @property
    def eventlog15(self):
        return self.__eventlog15
    @eventlog15.setter
    def eventlog15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flood_alarm_system__eventlog15", None)
        self.__eventlog15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flood_alarm_system14"):
                opp_val = getattr(old_value, "flood_alarm_system14", None)
                if opp_val == self:
                    setattr(old_value, "flood_alarm_system14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flood_alarm_system14"):
                opp_val = getattr(value, "flood_alarm_system14", None)
                setattr(value, "flood_alarm_system14", self)

    @property
    def control_panel28(self):
        return self.__control_panel28
    @control_panel28.setter
    def control_panel28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flood_alarm_system__control_panel28", None)
        self.__control_panel28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flood_alarm_system29"):
                opp_val = getattr(old_value, "flood_alarm_system29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flood_alarm_system29"):
                opp_val = getattr(value, "flood_alarm_system29", None)
                if opp_val is None:
                    setattr(value, "flood_alarm_system29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def flood_sensor8(self):
        return self.__flood_sensor8
    @flood_sensor8.setter
    def flood_sensor8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flood_alarm_system__flood_sensor8", None)
        self.__flood_sensor8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "flood_alarm_system9"):
                    opp_val = getattr(item, "flood_alarm_system9", None)
                    
                    if opp_val == self:
                        setattr(item, "flood_alarm_system9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "flood_alarm_system9"):
                    opp_val = getattr(item, "flood_alarm_system9", None)
                    
                    setattr(item, "flood_alarm_system9", self)
                    



class fire_alarm_system:

    def __init__(self, fire_alarm_system_on: bool, smoke_sensor4: set["smoke_sensor"] = None, temp_sensor6: set["temp_sensor"] = None, eventlog13: "eventlog" = None, fire_alarm_system24: "fire_alarm_system" = None, fire_alarm_system25: "fire_alarm_system" = None, control_panel26: "control_panel" = None):
        self.fire_alarm_system_on = fire_alarm_system_on
        self.smoke_sensor4 = smoke_sensor4 if smoke_sensor4 is not None else set()
        self.temp_sensor6 = temp_sensor6 if temp_sensor6 is not None else set()
        self.eventlog13 = eventlog13
        self.fire_alarm_system24 = fire_alarm_system24
        self.fire_alarm_system25 = fire_alarm_system25
        self.control_panel26 = control_panel26
        
        pass
    @property
    def fire_alarm_system_on(self):
        return self.__fire_alarm_system_on
    @fire_alarm_system_on.setter
    def fire_alarm_system_on(self, fire_alarm_system_on: bool):
        self.__fire_alarm_system_on = fire_alarm_system_on

    @property
    def fire_alarm_system24(self):
        return self.__fire_alarm_system24
    @fire_alarm_system24.setter
    def fire_alarm_system24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fire_alarm_system__fire_alarm_system24", None)
        self.__fire_alarm_system24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fire_alarm_system25"):
                opp_val = getattr(old_value, "fire_alarm_system25", None)
                if opp_val == self:
                    setattr(old_value, "fire_alarm_system25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fire_alarm_system25"):
                opp_val = getattr(value, "fire_alarm_system25", None)
                setattr(value, "fire_alarm_system25", self)

    @property
    def control_panel26(self):
        return self.__control_panel26
    @control_panel26.setter
    def control_panel26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fire_alarm_system__control_panel26", None)
        self.__control_panel26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fire_alarm_system27"):
                opp_val = getattr(old_value, "fire_alarm_system27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fire_alarm_system27"):
                opp_val = getattr(value, "fire_alarm_system27", None)
                if opp_val is None:
                    setattr(value, "fire_alarm_system27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def temp_sensor6(self):
        return self.__temp_sensor6
    @temp_sensor6.setter
    def temp_sensor6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fire_alarm_system__temp_sensor6", None)
        self.__temp_sensor6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fire_alarm_system7"):
                    opp_val = getattr(item, "fire_alarm_system7", None)
                    
                    if opp_val == self:
                        setattr(item, "fire_alarm_system7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fire_alarm_system7"):
                    opp_val = getattr(item, "fire_alarm_system7", None)
                    
                    setattr(item, "fire_alarm_system7", self)
                    

    @property
    def eventlog13(self):
        return self.__eventlog13
    @eventlog13.setter
    def eventlog13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fire_alarm_system__eventlog13", None)
        self.__eventlog13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fire_alarm_system12"):
                opp_val = getattr(old_value, "fire_alarm_system12", None)
                if opp_val == self:
                    setattr(old_value, "fire_alarm_system12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fire_alarm_system12"):
                opp_val = getattr(value, "fire_alarm_system12", None)
                setattr(value, "fire_alarm_system12", self)

    @property
    def fire_alarm_system25(self):
        return self.__fire_alarm_system25
    @fire_alarm_system25.setter
    def fire_alarm_system25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fire_alarm_system__fire_alarm_system25", None)
        self.__fire_alarm_system25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fire_alarm_system24"):
                opp_val = getattr(old_value, "fire_alarm_system24", None)
                if opp_val == self:
                    setattr(old_value, "fire_alarm_system24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fire_alarm_system24"):
                opp_val = getattr(value, "fire_alarm_system24", None)
                setattr(value, "fire_alarm_system24", self)

    @property
    def smoke_sensor4(self):
        return self.__smoke_sensor4
    @smoke_sensor4.setter
    def smoke_sensor4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fire_alarm_system__smoke_sensor4", None)
        self.__smoke_sensor4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fire_alarm_system5"):
                    opp_val = getattr(item, "fire_alarm_system5", None)
                    
                    if opp_val == self:
                        setattr(item, "fire_alarm_system5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fire_alarm_system5"):
                    opp_val = getattr(item, "fire_alarm_system5", None)
                    
                    setattr(item, "fire_alarm_system5", self)
                    



class timelog:

    def __init__(self, day: int, month: int, year: int, hour: int, minutes: int, seconds: int, eventlog21: "eventlog" = None, notification_System22: "Notification_System" = None):
        self.day = day
        self.month = month
        self.year = year
        self.hour = hour
        self.minutes = minutes
        self.seconds = seconds
        self.eventlog21 = eventlog21
        self.notification_System22 = notification_System22
        
        pass
    @property
    def minutes(self):
        return self.__minutes
    @minutes.setter
    def minutes(self, minutes: int):
        self.__minutes = minutes

    @property
    def day(self):
        return self.__day
    @day.setter
    def day(self, day: int):
        self.__day = day

    @property
    def year(self):
        return self.__year
    @year.setter
    def year(self, year: int):
        self.__year = year

    @property
    def hour(self):
        return self.__hour
    @hour.setter
    def hour(self, hour: int):
        self.__hour = hour

    @property
    def seconds(self):
        return self.__seconds
    @seconds.setter
    def seconds(self, seconds: int):
        self.__seconds = seconds

    @property
    def month(self):
        return self.__month
    @month.setter
    def month(self, month: int):
        self.__month = month

    @property
    def eventlog21(self):
        return self.__eventlog21
    @eventlog21.setter
    def eventlog21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_timelog__eventlog21", None)
        self.__eventlog21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "timelog20"):
                opp_val = getattr(old_value, "timelog20", None)
                if opp_val == self:
                    setattr(old_value, "timelog20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "timelog20"):
                opp_val = getattr(value, "timelog20", None)
                setattr(value, "timelog20", self)

    @property
    def notification_System22(self):
        return self.__notification_System22
    @notification_System22.setter
    def notification_System22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_timelog__notification_System22", None)
        self.__notification_System22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "timelog23"):
                opp_val = getattr(old_value, "timelog23", None)
                if opp_val == self:
                    setattr(old_value, "timelog23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "timelog23"):
                opp_val = getattr(value, "timelog23", None)
                setattr(value, "timelog23", self)



class eventlog:

    def __init__(self, event_id: int, event_time: int, event_info: str, assoc_02: "login" = None, fire_alarm_system12: "fire_alarm_system" = None, flood_alarm_system14: "flood_alarm_system" = None, door_alarm_system17: "door_alarm_system" = None, timelog20: "timelog" = None):
        self.event_id = event_id
        self.event_time = event_time
        self.event_info = event_info
        self.assoc_02 = assoc_02
        self.fire_alarm_system12 = fire_alarm_system12
        self.flood_alarm_system14 = flood_alarm_system14
        self.door_alarm_system17 = door_alarm_system17
        self.timelog20 = timelog20
        
        pass
    @property
    def event_time(self):
        return self.__event_time
    @event_time.setter
    def event_time(self, event_time: int):
        self.__event_time = event_time

    @property
    def event_id(self):
        return self.__event_id
    @event_id.setter
    def event_id(self, event_id: int):
        self.__event_id = event_id

    @property
    def event_info(self):
        return self.__event_info
    @event_info.setter
    def event_info(self, event_info: str):
        self.__event_info = event_info

    @property
    def flood_alarm_system14(self):
        return self.__flood_alarm_system14
    @flood_alarm_system14.setter
    def flood_alarm_system14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eventlog__flood_alarm_system14", None)
        self.__flood_alarm_system14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eventlog15"):
                opp_val = getattr(old_value, "eventlog15", None)
                if opp_val == self:
                    setattr(old_value, "eventlog15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eventlog15"):
                opp_val = getattr(value, "eventlog15", None)
                setattr(value, "eventlog15", self)

    @property
    def assoc_02(self):
        return self.__assoc_02
    @assoc_02.setter
    def assoc_02(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eventlog__assoc_02", None)
        self.__assoc_02 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "assoc_13"):
                opp_val = getattr(old_value, "assoc_13", None)
                if opp_val == self:
                    setattr(old_value, "assoc_13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "assoc_13"):
                opp_val = getattr(value, "assoc_13", None)
                setattr(value, "assoc_13", self)

    @property
    def door_alarm_system17(self):
        return self.__door_alarm_system17
    @door_alarm_system17.setter
    def door_alarm_system17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eventlog__door_alarm_system17", None)
        self.__door_alarm_system17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eventlog16"):
                opp_val = getattr(old_value, "eventlog16", None)
                if opp_val == self:
                    setattr(old_value, "eventlog16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eventlog16"):
                opp_val = getattr(value, "eventlog16", None)
                setattr(value, "eventlog16", self)

    @property
    def fire_alarm_system12(self):
        return self.__fire_alarm_system12
    @fire_alarm_system12.setter
    def fire_alarm_system12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eventlog__fire_alarm_system12", None)
        self.__fire_alarm_system12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eventlog13"):
                opp_val = getattr(old_value, "eventlog13", None)
                if opp_val == self:
                    setattr(old_value, "eventlog13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eventlog13"):
                opp_val = getattr(value, "eventlog13", None)
                setattr(value, "eventlog13", self)

    @property
    def timelog20(self):
        return self.__timelog20
    @timelog20.setter
    def timelog20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eventlog__timelog20", None)
        self.__timelog20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eventlog21"):
                opp_val = getattr(old_value, "eventlog21", None)
                if opp_val == self:
                    setattr(old_value, "eventlog21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eventlog21"):
                opp_val = getattr(value, "eventlog21", None)
                setattr(value, "eventlog21", self)



class login:

    def __init__(self, username: str, password: str, loginattempt: int, lockout: int, loginapp: str, logoutapp: str, owner_details_login_11: "owner_details" = None, assoc_13: "eventlog" = None):
        self.username = username
        self.password = password
        self.loginattempt = loginattempt
        self.lockout = lockout
        self.loginapp = loginapp
        self.logoutapp = logoutapp
        self.owner_details_login_11 = owner_details_login_11
        self.assoc_13 = assoc_13
        
        pass
    @property
    def loginapp(self):
        return self.__loginapp
    @loginapp.setter
    def loginapp(self, loginapp: str):
        self.__loginapp = loginapp

    @property
    def logoutapp(self):
        return self.__logoutapp
    @logoutapp.setter
    def logoutapp(self, logoutapp: str):
        self.__logoutapp = logoutapp

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def lockout(self):
        return self.__lockout
    @lockout.setter
    def lockout(self, lockout: int):
        self.__lockout = lockout

    @property
    def loginattempt(self):
        return self.__loginattempt
    @loginattempt.setter
    def loginattempt(self, loginattempt: int):
        self.__loginattempt = loginattempt

    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def assoc_13(self):
        return self.__assoc_13
    @assoc_13.setter
    def assoc_13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_login__assoc_13", None)
        self.__assoc_13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "assoc_02"):
                opp_val = getattr(old_value, "assoc_02", None)
                if opp_val == self:
                    setattr(old_value, "assoc_02", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "assoc_02"):
                opp_val = getattr(value, "assoc_02", None)
                setattr(value, "assoc_02", self)

    @property
    def owner_details_login_11(self):
        return self.__owner_details_login_11
    @owner_details_login_11.setter
    def owner_details_login_11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_login__owner_details_login_11", None)
        self.__owner_details_login_11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner_details_login_00"):
                opp_val = getattr(old_value, "owner_details_login_00", None)
                if opp_val == self:
                    setattr(old_value, "owner_details_login_00", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner_details_login_00"):
                opp_val = getattr(value, "owner_details_login_00", None)
                setattr(value, "owner_details_login_00", self)



class owner_details:

    def __init__(self, ownerName: str, owner_details_login_00: "login" = None):
        self.ownerName = ownerName
        self.owner_details_login_00 = owner_details_login_00
        
        pass
    @property
    def ownerName(self):
        return self.__ownerName
    @ownerName.setter
    def ownerName(self, ownerName: str):
        self.__ownerName = ownerName

    @property
    def owner_details_login_00(self):
        return self.__owner_details_login_00
    @owner_details_login_00.setter
    def owner_details_login_00(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_owner_details__owner_details_login_00", None)
        self.__owner_details_login_00 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner_details_login_11"):
                opp_val = getattr(old_value, "owner_details_login_11", None)
                if opp_val == self:
                    setattr(old_value, "owner_details_login_11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner_details_login_11"):
                opp_val = getattr(value, "owner_details_login_11", None)
                setattr(value, "owner_details_login_11", self)



class Notification_System:

    def __init__(self, OwnerNum__Integer: str, OwnerEmail: str, PublicSafetyNumber: int, PublicSafetyPage: int, control_panel18: "control_panel" = None, timelog23: "timelog" = None):
        self.OwnerNum__Integer = OwnerNum__Integer
        self.OwnerEmail = OwnerEmail
        self.PublicSafetyNumber = PublicSafetyNumber
        self.PublicSafetyPage = PublicSafetyPage
        self.control_panel18 = control_panel18
        self.timelog23 = timelog23
        
        pass
    @property
    def OwnerNum__Integer(self):
        return self.__OwnerNum__Integer
    @OwnerNum__Integer.setter
    def OwnerNum__Integer(self, OwnerNum__Integer: str):
        self.__OwnerNum__Integer = OwnerNum__Integer

    @property
    def PublicSafetyNumber(self):
        return self.__PublicSafetyNumber
    @PublicSafetyNumber.setter
    def PublicSafetyNumber(self, PublicSafetyNumber: int):
        self.__PublicSafetyNumber = PublicSafetyNumber

    @property
    def OwnerEmail(self):
        return self.__OwnerEmail
    @OwnerEmail.setter
    def OwnerEmail(self, OwnerEmail: str):
        self.__OwnerEmail = OwnerEmail

    @property
    def PublicSafetyPage(self):
        return self.__PublicSafetyPage
    @PublicSafetyPage.setter
    def PublicSafetyPage(self, PublicSafetyPage: int):
        self.__PublicSafetyPage = PublicSafetyPage

    @property
    def timelog23(self):
        return self.__timelog23
    @timelog23.setter
    def timelog23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Notification_System__timelog23", None)
        self.__timelog23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "notification_System22"):
                opp_val = getattr(old_value, "notification_System22", None)
                if opp_val == self:
                    setattr(old_value, "notification_System22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "notification_System22"):
                opp_val = getattr(value, "notification_System22", None)
                setattr(value, "notification_System22", self)

    @property
    def control_panel18(self):
        return self.__control_panel18
    @control_panel18.setter
    def control_panel18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Notification_System__control_panel18", None)
        self.__control_panel18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "notification_System19"):
                opp_val = getattr(old_value, "notification_System19", None)
                if opp_val == self:
                    setattr(old_value, "notification_System19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "notification_System19"):
                opp_val = getattr(value, "notification_System19", None)
                setattr(value, "notification_System19", self)



class flood_sensor:

    def __init__(self, flood_sensor_id: int, flood_sensor_status: bool, flood_sensor_loaction: str, waterlevel_breach_status: bool, flood_alarm_system9: "flood_alarm_system" = None):
        self.flood_sensor_id = flood_sensor_id
        self.flood_sensor_status = flood_sensor_status
        self.flood_sensor_loaction = flood_sensor_loaction
        self.waterlevel_breach_status = waterlevel_breach_status
        self.flood_alarm_system9 = flood_alarm_system9
        
        pass
    @property
    def flood_sensor_id(self):
        return self.__flood_sensor_id
    @flood_sensor_id.setter
    def flood_sensor_id(self, flood_sensor_id: int):
        self.__flood_sensor_id = flood_sensor_id

    @property
    def waterlevel_breach_status(self):
        return self.__waterlevel_breach_status
    @waterlevel_breach_status.setter
    def waterlevel_breach_status(self, waterlevel_breach_status: bool):
        self.__waterlevel_breach_status = waterlevel_breach_status

    @property
    def flood_sensor_status(self):
        return self.__flood_sensor_status
    @flood_sensor_status.setter
    def flood_sensor_status(self, flood_sensor_status: bool):
        self.__flood_sensor_status = flood_sensor_status

    @property
    def flood_sensor_loaction(self):
        return self.__flood_sensor_loaction
    @flood_sensor_loaction.setter
    def flood_sensor_loaction(self, flood_sensor_loaction: str):
        self.__flood_sensor_loaction = flood_sensor_loaction

    @property
    def flood_alarm_system9(self):
        return self.__flood_alarm_system9
    @flood_alarm_system9.setter
    def flood_alarm_system9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_flood_sensor__flood_alarm_system9", None)
        self.__flood_alarm_system9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flood_sensor8"):
                opp_val = getattr(old_value, "flood_sensor8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flood_sensor8"):
                opp_val = getattr(value, "flood_sensor8", None)
                if opp_val is None:
                    setattr(value, "flood_sensor8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class door_sensor:

    def __init__(self, door_sensor_id: int, door_open_status: bool, door_location: str, door_alarm_system11: "door_alarm_system" = None):
        self.door_sensor_id = door_sensor_id
        self.door_open_status = door_open_status
        self.door_location = door_location
        self.door_alarm_system11 = door_alarm_system11
        
        pass
    @property
    def door_open_status(self):
        return self.__door_open_status
    @door_open_status.setter
    def door_open_status(self, door_open_status: bool):
        self.__door_open_status = door_open_status

    @property
    def door_sensor_id(self):
        return self.__door_sensor_id
    @door_sensor_id.setter
    def door_sensor_id(self, door_sensor_id: int):
        self.__door_sensor_id = door_sensor_id

    @property
    def door_location(self):
        return self.__door_location
    @door_location.setter
    def door_location(self, door_location: str):
        self.__door_location = door_location

    @property
    def door_alarm_system11(self):
        return self.__door_alarm_system11
    @door_alarm_system11.setter
    def door_alarm_system11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_door_sensor__door_alarm_system11", None)
        self.__door_alarm_system11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "door_sensor10"):
                opp_val = getattr(old_value, "door_sensor10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "door_sensor10"):
                opp_val = getattr(value, "door_sensor10", None)
                if opp_val is None:
                    setattr(value, "door_sensor10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class control_panel:

    def __init__(self, system_on: bool, notification_System19: "Notification_System" = None, fire_alarm_system27: set["fire_alarm_system"] = None, flood_alarm_system29: set["flood_alarm_system"] = None, door_alarm_system31: set["door_alarm_system"] = None, camera_records33: "camera_records" = None):
        self.system_on = system_on
        self.notification_System19 = notification_System19
        self.fire_alarm_system27 = fire_alarm_system27 if fire_alarm_system27 is not None else set()
        self.flood_alarm_system29 = flood_alarm_system29 if flood_alarm_system29 is not None else set()
        self.door_alarm_system31 = door_alarm_system31 if door_alarm_system31 is not None else set()
        self.camera_records33 = camera_records33
        
        pass
    @property
    def system_on(self):
        return self.__system_on
    @system_on.setter
    def system_on(self, system_on: bool):
        self.__system_on = system_on

    @property
    def camera_records33(self):
        return self.__camera_records33
    @camera_records33.setter
    def camera_records33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_control_panel__camera_records33", None)
        self.__camera_records33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "control_panel32"):
                opp_val = getattr(old_value, "control_panel32", None)
                if opp_val == self:
                    setattr(old_value, "control_panel32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "control_panel32"):
                opp_val = getattr(value, "control_panel32", None)
                setattr(value, "control_panel32", self)

    @property
    def fire_alarm_system27(self):
        return self.__fire_alarm_system27
    @fire_alarm_system27.setter
    def fire_alarm_system27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_control_panel__fire_alarm_system27", None)
        self.__fire_alarm_system27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "control_panel26"):
                    opp_val = getattr(item, "control_panel26", None)
                    
                    if opp_val == self:
                        setattr(item, "control_panel26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "control_panel26"):
                    opp_val = getattr(item, "control_panel26", None)
                    
                    setattr(item, "control_panel26", self)
                    

    @property
    def door_alarm_system31(self):
        return self.__door_alarm_system31
    @door_alarm_system31.setter
    def door_alarm_system31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_control_panel__door_alarm_system31", None)
        self.__door_alarm_system31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "control_panel30"):
                    opp_val = getattr(item, "control_panel30", None)
                    
                    if opp_val == self:
                        setattr(item, "control_panel30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "control_panel30"):
                    opp_val = getattr(item, "control_panel30", None)
                    
                    setattr(item, "control_panel30", self)
                    

    @property
    def notification_System19(self):
        return self.__notification_System19
    @notification_System19.setter
    def notification_System19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_control_panel__notification_System19", None)
        self.__notification_System19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "control_panel18"):
                opp_val = getattr(old_value, "control_panel18", None)
                if opp_val == self:
                    setattr(old_value, "control_panel18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "control_panel18"):
                opp_val = getattr(value, "control_panel18", None)
                setattr(value, "control_panel18", self)

    @property
    def flood_alarm_system29(self):
        return self.__flood_alarm_system29
    @flood_alarm_system29.setter
    def flood_alarm_system29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_control_panel__flood_alarm_system29", None)
        self.__flood_alarm_system29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "control_panel28"):
                    opp_val = getattr(item, "control_panel28", None)
                    
                    if opp_val == self:
                        setattr(item, "control_panel28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "control_panel28"):
                    opp_val = getattr(item, "control_panel28", None)
                    
                    setattr(item, "control_panel28", self)
                    



class temp_sensor:

    def __init__(self, temp_level_breach: bool, temp_sensor_id: int, temp_sensor_status: bool, temp_sensor_location: str, fire_alarm_system7: "fire_alarm_system" = None):
        self.temp_level_breach = temp_level_breach
        self.temp_sensor_id = temp_sensor_id
        self.temp_sensor_status = temp_sensor_status
        self.temp_sensor_location = temp_sensor_location
        self.fire_alarm_system7 = fire_alarm_system7
        
        pass
    @property
    def temp_sensor_id(self):
        return self.__temp_sensor_id
    @temp_sensor_id.setter
    def temp_sensor_id(self, temp_sensor_id: int):
        self.__temp_sensor_id = temp_sensor_id

    @property
    def temp_sensor_location(self):
        return self.__temp_sensor_location
    @temp_sensor_location.setter
    def temp_sensor_location(self, temp_sensor_location: str):
        self.__temp_sensor_location = temp_sensor_location

    @property
    def temp_sensor_status(self):
        return self.__temp_sensor_status
    @temp_sensor_status.setter
    def temp_sensor_status(self, temp_sensor_status: bool):
        self.__temp_sensor_status = temp_sensor_status

    @property
    def temp_level_breach(self):
        return self.__temp_level_breach
    @temp_level_breach.setter
    def temp_level_breach(self, temp_level_breach: bool):
        self.__temp_level_breach = temp_level_breach

    @property
    def fire_alarm_system7(self):
        return self.__fire_alarm_system7
    @fire_alarm_system7.setter
    def fire_alarm_system7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_temp_sensor__fire_alarm_system7", None)
        self.__fire_alarm_system7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "temp_sensor6"):
                opp_val = getattr(old_value, "temp_sensor6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "temp_sensor6"):
                opp_val = getattr(value, "temp_sensor6", None)
                if opp_val is None:
                    setattr(value, "temp_sensor6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class InterfaceO_Interface:

    pass


class camera_records:

    def __init__(self, camera_id: int, camera_status_on: bool, camera_location: str, control_panel32: "control_panel" = None):
        self.camera_id = camera_id
        self.camera_status_on = camera_status_on
        self.camera_location = camera_location
        self.control_panel32 = control_panel32
        
        pass
    @property
    def camera_status_on(self):
        return self.__camera_status_on
    @camera_status_on.setter
    def camera_status_on(self, camera_status_on: bool):
        self.__camera_status_on = camera_status_on

    @property
    def camera_id(self):
        return self.__camera_id
    @camera_id.setter
    def camera_id(self, camera_id: int):
        self.__camera_id = camera_id

    @property
    def camera_location(self):
        return self.__camera_location
    @camera_location.setter
    def camera_location(self, camera_location: str):
        self.__camera_location = camera_location

    @property
    def control_panel32(self):
        return self.__control_panel32
    @control_panel32.setter
    def control_panel32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_camera_records__control_panel32", None)
        self.__control_panel32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "camera_records33"):
                opp_val = getattr(old_value, "camera_records33", None)
                if opp_val == self:
                    setattr(old_value, "camera_records33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "camera_records33"):
                opp_val = getattr(value, "camera_records33", None)
                setattr(value, "camera_records33", self)



class smoke_sensor:

    def __init__(self, smoke_sensor_id: int, smoke_sensor_status: bool, smoke_sensor_location: str, smoke_level_breach: bool, fire_alarm_system5: "fire_alarm_system" = None):
        self.smoke_sensor_id = smoke_sensor_id
        self.smoke_sensor_status = smoke_sensor_status
        self.smoke_sensor_location = smoke_sensor_location
        self.smoke_level_breach = smoke_level_breach
        self.fire_alarm_system5 = fire_alarm_system5
        
        pass
    @property
    def smoke_sensor_location(self):
        return self.__smoke_sensor_location
    @smoke_sensor_location.setter
    def smoke_sensor_location(self, smoke_sensor_location: str):
        self.__smoke_sensor_location = smoke_sensor_location

    @property
    def smoke_sensor_status(self):
        return self.__smoke_sensor_status
    @smoke_sensor_status.setter
    def smoke_sensor_status(self, smoke_sensor_status: bool):
        self.__smoke_sensor_status = smoke_sensor_status

    @property
    def smoke_level_breach(self):
        return self.__smoke_level_breach
    @smoke_level_breach.setter
    def smoke_level_breach(self, smoke_level_breach: bool):
        self.__smoke_level_breach = smoke_level_breach

    @property
    def smoke_sensor_id(self):
        return self.__smoke_sensor_id
    @smoke_sensor_id.setter
    def smoke_sensor_id(self, smoke_sensor_id: int):
        self.__smoke_sensor_id = smoke_sensor_id

    @property
    def fire_alarm_system5(self):
        return self.__fire_alarm_system5
    @fire_alarm_system5.setter
    def fire_alarm_system5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smoke_sensor__fire_alarm_system5", None)
        self.__fire_alarm_system5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smoke_sensor4"):
                opp_val = getattr(old_value, "smoke_sensor4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smoke_sensor4"):
                opp_val = getattr(value, "smoke_sensor4", None)
                if opp_val is None:
                    setattr(value, "smoke_sensor4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

