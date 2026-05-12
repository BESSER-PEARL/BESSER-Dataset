from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class TV:

    pass


class Fire_Alarm:

    def __init__(self, systemOn: bool, systemOff: bool):
        self.systemOn = systemOn
        self.systemOff = systemOff
        
        pass
    @property
    def systemOn(self):
        return self.__systemOn
    @systemOn.setter
    def systemOn(self, systemOn: bool):
        self.__systemOn = systemOn

    @property
    def systemOff(self):
        return self.__systemOff
    @systemOff.setter
    def systemOff(self, systemOff: bool):
        self.__systemOff = systemOff



class Security_System:

    def __init__(self, systemOn: bool, systemOff: bool):
        self.systemOn = systemOn
        self.systemOff = systemOff
        
        pass
    @property
    def systemOn(self):
        return self.__systemOn
    @systemOn.setter
    def systemOn(self, systemOn: bool):
        self.__systemOn = systemOn

    @property
    def systemOff(self):
        return self.__systemOff
    @systemOff.setter
    def systemOff(self, systemOff: bool):
        self.__systemOff = systemOff



class Fan:

    pass


class Light:

    pass


class System:

    def __init__(self, status: bool, _user1: "Login" = None):
        self.status = status
        self._user1 = _user1
        
        pass
    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: bool):
        self.__status = status

    @property
    def _user1(self):
        return self.___user1
    @_user1.setter
    def _user1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_System___user1", None)
        self.___user1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "_handle0"):
                opp_val = getattr(old_value, "_handle0", None)
                if opp_val == self:
                    setattr(old_value, "_handle0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "_handle0"):
                opp_val = getattr(value, "_handle0", None)
                setattr(value, "_handle0", self)



class Login:

    def __init__(self, Name: str, Password: str, _handle0: "System" = None, _user2: "User" = None):
        self.Name = Name
        self.Password = Password
        self._handle0 = _handle0
        self._user2 = _user2
        
        pass
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def _handle0(self):
        return self.___handle0
    @_handle0.setter
    def _handle0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Login___handle0", None)
        self.___handle0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "_user1"):
                opp_val = getattr(old_value, "_user1", None)
                if opp_val == self:
                    setattr(old_value, "_user1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "_user1"):
                opp_val = getattr(value, "_user1", None)
                setattr(value, "_user1", self)

    @property
    def _user2(self):
        return self.___user2
    @_user2.setter
    def _user2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Login___user2", None)
        self.___user2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "_access3"):
                opp_val = getattr(old_value, "_access3", None)
                if opp_val == self:
                    setattr(old_value, "_access3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "_access3"):
                opp_val = getattr(value, "_access3", None)
                setattr(value, "_access3", self)



class User:

    def __init__(self, Name: str, _access3: "Login" = None):
        self.Name = Name
        self._access3 = _access3
        
        pass
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def _access3(self):
        return self.___access3
    @_access3.setter
    def _access3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User___access3", None)
        self.___access3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "_user2"):
                opp_val = getattr(old_value, "_user2", None)
                if opp_val == self:
                    setattr(old_value, "_user2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "_user2"):
                opp_val = getattr(value, "_user2", None)
                setattr(value, "_user2", self)

