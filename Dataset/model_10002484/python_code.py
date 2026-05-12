from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class admin_Actor:

    pass


class student_Actor:

    pass





class modify_list_of_students_external:

    pass


class login_external:

    pass


class view_cumiliative_attendance_external:

    pass


class view_subject_wise_attendance_external:

    pass


class ADMIN:

    def __init__(self, id: str, password: str, fACULTY13: set["FACULTY"] = None, sTUDENT15: set["STUDENT"] = None, pARENT17: set["PARENT"] = None):
        self.id = id
        self.password = password
        self.fACULTY13 = fACULTY13 if fACULTY13 is not None else set()
        self.sTUDENT15 = sTUDENT15 if sTUDENT15 is not None else set()
        self.pARENT17 = pARENT17 if pARENT17 is not None else set()
        
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
    def pARENT17(self):
        return self.__pARENT17
    @pARENT17.setter
    def pARENT17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ADMIN__pARENT17", None)
        self.__pARENT17 = value if value is not None else set()
        
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
    def fACULTY13(self):
        return self.__fACULTY13
    @fACULTY13.setter
    def fACULTY13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ADMIN__fACULTY13", None)
        self.__fACULTY13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aDMIN12"):
                    opp_val = getattr(item, "aDMIN12", None)
                    
                    if opp_val == self:
                        setattr(item, "aDMIN12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aDMIN12"):
                    opp_val = getattr(item, "aDMIN12", None)
                    
                    setattr(item, "aDMIN12", self)
                    

    @property
    def sTUDENT15(self):
        return self.__sTUDENT15
    @sTUDENT15.setter
    def sTUDENT15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ADMIN__sTUDENT15", None)
        self.__sTUDENT15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aDMIN14"):
                    opp_val = getattr(item, "aDMIN14", None)
                    
                    if opp_val == self:
                        setattr(item, "aDMIN14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aDMIN14"):
                    opp_val = getattr(item, "aDMIN14", None)
                    
                    setattr(item, "aDMIN14", self)
                    



class PARENT:

    def __init__(self, id: str, password: str, phoneNumber: int, aDMIN16: "ADMIN" = None):
        self.id = id
        self.password = password
        self.phoneNumber = phoneNumber
        self.aDMIN16 = aDMIN16
        
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
    def aDMIN16(self):
        return self.__aDMIN16
    @aDMIN16.setter
    def aDMIN16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PARENT__aDMIN16", None)
        self.__aDMIN16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pARENT17"):
                opp_val = getattr(old_value, "pARENT17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pARENT17"):
                opp_val = getattr(value, "pARENT17", None)
                if opp_val is None:
                    setattr(value, "pARENT17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class STUDENT:

    def __init__(self, id: str, password: str, fACULTY11: set["FACULTY"] = None, aDMIN14: "ADMIN" = None):
        self.id = id
        self.password = password
        self.fACULTY11 = fACULTY11 if fACULTY11 is not None else set()
        self.aDMIN14 = aDMIN14
        
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
    def aDMIN14(self):
        return self.__aDMIN14
    @aDMIN14.setter
    def aDMIN14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_STUDENT__aDMIN14", None)
        self.__aDMIN14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sTUDENT15"):
                opp_val = getattr(old_value, "sTUDENT15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sTUDENT15"):
                opp_val = getattr(value, "sTUDENT15", None)
                if opp_val is None:
                    setattr(value, "sTUDENT15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fACULTY11(self):
        return self.__fACULTY11
    @fACULTY11.setter
    def fACULTY11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_STUDENT__fACULTY11", None)
        self.__fACULTY11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sTUDENT10"):
                    opp_val = getattr(item, "sTUDENT10", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sTUDENT10"):
                    opp_val = getattr(item, "sTUDENT10", None)
                    
                    if opp_val is None:
                        setattr(item, "sTUDENT10", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class FACULTY:

    def __init__(self, id: str, password: str, sTUDENT10: set["STUDENT"] = None, aDMIN12: "ADMIN" = None):
        self.id = id
        self.password = password
        self.sTUDENT10 = sTUDENT10 if sTUDENT10 is not None else set()
        self.aDMIN12 = aDMIN12
        
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
    def aDMIN12(self):
        return self.__aDMIN12
    @aDMIN12.setter
    def aDMIN12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FACULTY__aDMIN12", None)
        self.__aDMIN12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fACULTY13"):
                opp_val = getattr(old_value, "fACULTY13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fACULTY13"):
                opp_val = getattr(value, "fACULTY13", None)
                if opp_val is None:
                    setattr(value, "fACULTY13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sTUDENT10(self):
        return self.__sTUDENT10
    @sTUDENT10.setter
    def sTUDENT10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FACULTY__sTUDENT10", None)
        self.__sTUDENT10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fACULTY11"):
                    opp_val = getattr(item, "fACULTY11", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fACULTY11"):
                    opp_val = getattr(item, "fACULTY11", None)
                    
                    if opp_val is None:
                        setattr(item, "fACULTY11", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class _Component:

    pass
