from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class FireAlarm:

    def __init__(self, status: bool, fire_Alarm_system13: "Fire_Alarm_system" = None):
        self.status = status
        self.fire_Alarm_system13 = fire_Alarm_system13
        
        pass
    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: bool):
        self.__status = status

    @property
    def fire_Alarm_system13(self):
        return self.__fire_Alarm_system13
    @fire_Alarm_system13.setter
    def fire_Alarm_system13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FireAlarm__fire_Alarm_system13", None)
        self.__fire_Alarm_system13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fireAlarm12"):
                opp_val = getattr(old_value, "fireAlarm12", None)
                if opp_val == self:
                    setattr(old_value, "fireAlarm12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fireAlarm12"):
                opp_val = getattr(value, "fireAlarm12", None)
                setattr(value, "fireAlarm12", self)



class securityAlarm:

    def __init__(self, status: bool, home_Security_System10: "Home_Security_System" = None):
        self.status = status
        self.home_Security_System10 = home_Security_System10
        
        pass
    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: bool):
        self.__status = status

    @property
    def home_Security_System10(self):
        return self.__home_Security_System10
    @home_Security_System10.setter
    def home_Security_System10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_securityAlarm__home_Security_System10", None)
        self.__home_Security_System10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "securityAlarm11"):
                opp_val = getattr(old_value, "securityAlarm11", None)
                if opp_val == self:
                    setattr(old_value, "securityAlarm11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "securityAlarm11"):
                opp_val = getattr(value, "securityAlarm11", None)
                setattr(value, "securityAlarm11", self)



class Police:

    def __init__(self, name: str, home_Security_System8: "Home_Security_System" = None):
        self.name = name
        self.home_Security_System8 = home_Security_System8
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def home_Security_System8(self):
        return self.__home_Security_System8
    @home_Security_System8.setter
    def home_Security_System8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Police__home_Security_System8", None)
        self.__home_Security_System8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "police9"):
                opp_val = getattr(old_value, "police9", None)
                if opp_val == self:
                    setattr(old_value, "police9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "police9"):
                opp_val = getattr(value, "police9", None)
                setattr(value, "police9", self)



class smokeAlarm:

    def __init__(self, status: bool, fire_Alarm_system6: "Fire_Alarm_system" = None):
        self.status = status
        self.fire_Alarm_system6 = fire_Alarm_system6
        
        pass
    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: bool):
        self.__status = status

    @property
    def fire_Alarm_system6(self):
        return self.__fire_Alarm_system6
    @fire_Alarm_system6.setter
    def fire_Alarm_system6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smokeAlarm__fire_Alarm_system6", None)
        self.__fire_Alarm_system6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smokeAlarm7"):
                opp_val = getattr(old_value, "smokeAlarm7", None)
                if opp_val == self:
                    setattr(old_value, "smokeAlarm7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smokeAlarm7"):
                opp_val = getattr(value, "smokeAlarm7", None)
                setattr(value, "smokeAlarm7", self)



class Department:

    def __init__(self, name: str, fire_Alarm_system4: "Fire_Alarm_system" = None):
        self.name = name
        self.fire_Alarm_system4 = fire_Alarm_system4
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fire_Alarm_system4(self):
        return self.__fire_Alarm_system4
    @fire_Alarm_system4.setter
    def fire_Alarm_system4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Department__fire_Alarm_system4", None)
        self.__fire_Alarm_system4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "department5"):
                opp_val = getattr(old_value, "department5", None)
                if opp_val == self:
                    setattr(old_value, "department5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "department5"):
                opp_val = getattr(value, "department5", None)
                setattr(value, "department5", self)



class Home_Security_System:

    def __init__(self, system_On: bool, system_Off: bool, police9: "Police" = None, securityAlarm11: "securityAlarm" = None):
        self.system_On = system_On
        self.system_Off = system_Off
        self.police9 = police9
        self.securityAlarm11 = securityAlarm11
        
        pass
    @property
    def system_On(self):
        return self.__system_On
    @system_On.setter
    def system_On(self, system_On: bool):
        self.__system_On = system_On

    @property
    def system_Off(self):
        return self.__system_Off
    @system_Off.setter
    def system_Off(self, system_Off: bool):
        self.__system_Off = system_Off

    @property
    def police9(self):
        return self.__police9
    @police9.setter
    def police9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Home_Security_System__police9", None)
        self.__police9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "home_Security_System8"):
                opp_val = getattr(old_value, "home_Security_System8", None)
                if opp_val == self:
                    setattr(old_value, "home_Security_System8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "home_Security_System8"):
                opp_val = getattr(value, "home_Security_System8", None)
                setattr(value, "home_Security_System8", self)

    @property
    def securityAlarm11(self):
        return self.__securityAlarm11
    @securityAlarm11.setter
    def securityAlarm11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Home_Security_System__securityAlarm11", None)
        self.__securityAlarm11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "home_Security_System10"):
                opp_val = getattr(old_value, "home_Security_System10", None)
                if opp_val == self:
                    setattr(old_value, "home_Security_System10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "home_Security_System10"):
                opp_val = getattr(value, "home_Security_System10", None)
                setattr(value, "home_Security_System10", self)



class Fire_Alarm_system:

    def __init__(self, system_On: bool, system_Off: bool, department5: "Department" = None, smokeAlarm7: "smokeAlarm" = None, fireAlarm12: "FireAlarm" = None):
        self.system_On = system_On
        self.system_Off = system_Off
        self.department5 = department5
        self.smokeAlarm7 = smokeAlarm7
        self.fireAlarm12 = fireAlarm12
        
        pass
    @property
    def system_On(self):
        return self.__system_On
    @system_On.setter
    def system_On(self, system_On: bool):
        self.__system_On = system_On

    @property
    def system_Off(self):
        return self.__system_Off
    @system_Off.setter
    def system_Off(self, system_Off: bool):
        self.__system_Off = system_Off

    @property
    def fireAlarm12(self):
        return self.__fireAlarm12
    @fireAlarm12.setter
    def fireAlarm12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Fire_Alarm_system__fireAlarm12", None)
        self.__fireAlarm12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fire_Alarm_system13"):
                opp_val = getattr(old_value, "fire_Alarm_system13", None)
                if opp_val == self:
                    setattr(old_value, "fire_Alarm_system13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fire_Alarm_system13"):
                opp_val = getattr(value, "fire_Alarm_system13", None)
                setattr(value, "fire_Alarm_system13", self)

    @property
    def smokeAlarm7(self):
        return self.__smokeAlarm7
    @smokeAlarm7.setter
    def smokeAlarm7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Fire_Alarm_system__smokeAlarm7", None)
        self.__smokeAlarm7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fire_Alarm_system6"):
                opp_val = getattr(old_value, "fire_Alarm_system6", None)
                if opp_val == self:
                    setattr(old_value, "fire_Alarm_system6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fire_Alarm_system6"):
                opp_val = getattr(value, "fire_Alarm_system6", None)
                setattr(value, "fire_Alarm_system6", self)

    @property
    def department5(self):
        return self.__department5
    @department5.setter
    def department5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Fire_Alarm_system__department5", None)
        self.__department5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fire_Alarm_system4"):
                opp_val = getattr(old_value, "fire_Alarm_system4", None)
                if opp_val == self:
                    setattr(old_value, "fire_Alarm_system4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fire_Alarm_system4"):
                opp_val = getattr(value, "fire_Alarm_system4", None)
                setattr(value, "fire_Alarm_system4", self)



class Appliances:

    def __init__(self, On_status: bool, Off_status: bool):
        self.On_status = On_status
        self.Off_status = Off_status
        
        pass
    @property
    def Off_status(self):
        return self.__Off_status
    @Off_status.setter
    def Off_status(self, Off_status: bool):
        self.__Off_status = Off_status

    @property
    def On_status(self):
        return self.__On_status
    @On_status.setter
    def On_status(self, On_status: bool):
        self.__On_status = On_status



class system:

    def __init__(self, status: bool, login23: "Login" = None):
        self.status = status
        self.login23 = login23
        
        pass
    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: bool):
        self.__status = status

    @property
    def login23(self):
        return self.__login23
    @login23.setter
    def login23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_system__login23", None)
        self.__login23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "system2"):
                opp_val = getattr(old_value, "system2", None)
                if opp_val == self:
                    setattr(old_value, "system2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "system2"):
                opp_val = getattr(value, "system2", None)
                setattr(value, "system2", self)



class Login:

    def __init__(self, name: str, password: str, owner1: "Owner" = None, system2: "system" = None):
        self.name = name
        self.password = password
        self.owner1 = owner1
        self.system2 = system2
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def system2(self):
        return self.__system2
    @system2.setter
    def system2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Login__system2", None)
        self.__system2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "login23"):
                opp_val = getattr(old_value, "login23", None)
                if opp_val == self:
                    setattr(old_value, "login23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "login23"):
                opp_val = getattr(value, "login23", None)
                setattr(value, "login23", self)

    @property
    def owner1(self):
        return self.__owner1
    @owner1.setter
    def owner1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Login__owner1", None)
        self.__owner1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "login0"):
                opp_val = getattr(old_value, "login0", None)
                if opp_val == self:
                    setattr(old_value, "login0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "login0"):
                opp_val = getattr(value, "login0", None)
                setattr(value, "login0", self)



class Owner:

    def __init__(self, name: str, login0: "Login" = None):
        self.name = name
        self.login0 = login0
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def login0(self):
        return self.__login0
    @login0.setter
    def login0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Owner__login0", None)
        self.__login0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner1"):
                opp_val = getattr(old_value, "owner1", None)
                if opp_val == self:
                    setattr(old_value, "owner1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner1"):
                opp_val = getattr(value, "owner1", None)
                setattr(value, "owner1", self)

