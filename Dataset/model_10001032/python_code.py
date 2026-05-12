from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class student_Actor:

    pass


class admin_Actor:

    pass





class logout_external:

    pass


class check_attendance_external:

    pass


class add_student_external:

    pass


class view_student_external:

    pass


class student_login_external:

    pass


class ADMIN:

    def __init__(self, id: str, password: str, fACULTY17: set["FACULTY"] = None, sTUDENT19: set["STUDENT"] = None, pARENT21: set["PARENT"] = None):
        self.id = id
        self.password = password
        self.fACULTY17 = fACULTY17 if fACULTY17 is not None else set()
        self.sTUDENT19 = sTUDENT19 if sTUDENT19 is not None else set()
        self.pARENT21 = pARENT21 if pARENT21 is not None else set()
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def fACULTY17(self):
        return self.__fACULTY17
    @fACULTY17.setter
    def fACULTY17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ADMIN__fACULTY17", None)
        self.__fACULTY17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aDMIN16"):
                    opp_val = getattr(item, "aDMIN16", None)
                    
                    if opp_val == self:
                        setattr(item, "aDMIN16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aDMIN16"):
                    opp_val = getattr(item, "aDMIN16", None)
                    
                    setattr(item, "aDMIN16", self)
                    

    @property
    def sTUDENT19(self):
        return self.__sTUDENT19
    @sTUDENT19.setter
    def sTUDENT19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ADMIN__sTUDENT19", None)
        self.__sTUDENT19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aDMIN18"):
                    opp_val = getattr(item, "aDMIN18", None)
                    
                    if opp_val == self:
                        setattr(item, "aDMIN18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aDMIN18"):
                    opp_val = getattr(item, "aDMIN18", None)
                    
                    setattr(item, "aDMIN18", self)
                    

    @property
    def pARENT21(self):
        return self.__pARENT21
    @pARENT21.setter
    def pARENT21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ADMIN__pARENT21", None)
        self.__pARENT21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aDMIN20"):
                    opp_val = getattr(item, "aDMIN20", None)
                    
                    if opp_val == self:
                        setattr(item, "aDMIN20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aDMIN20"):
                    opp_val = getattr(item, "aDMIN20", None)
                    
                    setattr(item, "aDMIN20", self)
                    



class PARENT:

    def __init__(self, id: str, password: str, phoneNumber: int, aDMIN20: "ADMIN" = None):
        self.id = id
        self.password = password
        self.phoneNumber = phoneNumber
        self.aDMIN20 = aDMIN20
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def phoneNumber(self):
        return self.__phoneNumber
    @phoneNumber.setter
    def phoneNumber(self, phoneNumber: int):
        self.__phoneNumber = phoneNumber

    @property
    def aDMIN20(self):
        return self.__aDMIN20
    @aDMIN20.setter
    def aDMIN20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PARENT__aDMIN20", None)
        self.__aDMIN20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pARENT21"):
                opp_val = getattr(old_value, "pARENT21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pARENT21"):
                opp_val = getattr(value, "pARENT21", None)
                if opp_val is None:
                    setattr(value, "pARENT21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class STUDENT:

    def __init__(self, id: str, password: str, fACULTY15: set["FACULTY"] = None, aDMIN18: "ADMIN" = None):
        self.id = id
        self.password = password
        self.fACULTY15 = fACULTY15 if fACULTY15 is not None else set()
        self.aDMIN18 = aDMIN18
        
        pass
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def aDMIN18(self):
        return self.__aDMIN18
    @aDMIN18.setter
    def aDMIN18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_STUDENT__aDMIN18", None)
        self.__aDMIN18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sTUDENT19"):
                opp_val = getattr(old_value, "sTUDENT19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sTUDENT19"):
                opp_val = getattr(value, "sTUDENT19", None)
                if opp_val is None:
                    setattr(value, "sTUDENT19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fACULTY15(self):
        return self.__fACULTY15
    @fACULTY15.setter
    def fACULTY15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_STUDENT__fACULTY15", None)
        self.__fACULTY15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sTUDENT14"):
                    opp_val = getattr(item, "sTUDENT14", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sTUDENT14"):
                    opp_val = getattr(item, "sTUDENT14", None)
                    
                    if opp_val is None:
                        setattr(item, "sTUDENT14", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class FACULTY:

    def __init__(self, id: str, password: str, sTUDENT14: set["STUDENT"] = None, aDMIN16: "ADMIN" = None):
        self.id = id
        self.password = password
        self.sTUDENT14 = sTUDENT14 if sTUDENT14 is not None else set()
        self.aDMIN16 = aDMIN16
        
        pass
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def sTUDENT14(self):
        return self.__sTUDENT14
    @sTUDENT14.setter
    def sTUDENT14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FACULTY__sTUDENT14", None)
        self.__sTUDENT14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fACULTY15"):
                    opp_val = getattr(item, "fACULTY15", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fACULTY15"):
                    opp_val = getattr(item, "fACULTY15", None)
                    
                    if opp_val is None:
                        setattr(item, "fACULTY15", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def aDMIN16(self):
        return self.__aDMIN16
    @aDMIN16.setter
    def aDMIN16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FACULTY__aDMIN16", None)
        self.__aDMIN16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fACULTY17"):
                opp_val = getattr(old_value, "fACULTY17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fACULTY17"):
                opp_val = getattr(value, "fACULTY17", None)
                if opp_val is None:
                    setattr(value, "fACULTY17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class _Component:

    pass
