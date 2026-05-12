from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class VALIDATE:

    def __init__(self, USERNAME: str, PASSWORD: str):
        self.USERNAME = USERNAME
        self.PASSWORD = PASSWORD
        
        pass
    @property
    def PASSWORD(self):
        return self.__PASSWORD
    @PASSWORD.setter
    def PASSWORD(self, PASSWORD: str):
        self.__PASSWORD = PASSWORD

    @property
    def USERNAME(self):
        return self.__USERNAME
    @USERNAME.setter
    def USERNAME(self, USERNAME: str):
        self.__USERNAME = USERNAME



class STUDENT:

    def __init__(self, NAME: str, STUD_ID: int, COURSE: str, QUALIFICATION: str, EMAIL_ID: str, CONTACT_NO: int, eMPLOYEE1: set["EMPLOYEE"] = None, aDMIN5: "ADMIN" = None):
        self.NAME = NAME
        self.STUD_ID = STUD_ID
        self.COURSE = COURSE
        self.QUALIFICATION = QUALIFICATION
        self.EMAIL_ID = EMAIL_ID
        self.CONTACT_NO = CONTACT_NO
        self.eMPLOYEE1 = eMPLOYEE1 if eMPLOYEE1 is not None else set()
        self.aDMIN5 = aDMIN5
        
        pass
    @property
    def EMAIL_ID(self):
        return self.__EMAIL_ID
    @EMAIL_ID.setter
    def EMAIL_ID(self, EMAIL_ID: str):
        self.__EMAIL_ID = EMAIL_ID

    @property
    def CONTACT_NO(self):
        return self.__CONTACT_NO
    @CONTACT_NO.setter
    def CONTACT_NO(self, CONTACT_NO: int):
        self.__CONTACT_NO = CONTACT_NO

    @property
    def QUALIFICATION(self):
        return self.__QUALIFICATION
    @QUALIFICATION.setter
    def QUALIFICATION(self, QUALIFICATION: str):
        self.__QUALIFICATION = QUALIFICATION

    @property
    def STUD_ID(self):
        return self.__STUD_ID
    @STUD_ID.setter
    def STUD_ID(self, STUD_ID: int):
        self.__STUD_ID = STUD_ID

    @property
    def NAME(self):
        return self.__NAME
    @NAME.setter
    def NAME(self, NAME: str):
        self.__NAME = NAME

    @property
    def COURSE(self):
        return self.__COURSE
    @COURSE.setter
    def COURSE(self, COURSE: str):
        self.__COURSE = COURSE

    @property
    def aDMIN5(self):
        return self.__aDMIN5
    @aDMIN5.setter
    def aDMIN5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_STUDENT__aDMIN5", None)
        self.__aDMIN5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sTUDENT4"):
                opp_val = getattr(old_value, "sTUDENT4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sTUDENT4"):
                opp_val = getattr(value, "sTUDENT4", None)
                if opp_val is None:
                    setattr(value, "sTUDENT4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eMPLOYEE1(self):
        return self.__eMPLOYEE1
    @eMPLOYEE1.setter
    def eMPLOYEE1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_STUDENT__eMPLOYEE1", None)
        self.__eMPLOYEE1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sTUDENT0"):
                    opp_val = getattr(item, "sTUDENT0", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sTUDENT0"):
                    opp_val = getattr(item, "sTUDENT0", None)
                    
                    if opp_val is None:
                        setattr(item, "sTUDENT0", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class EMPLOYEE:

    def __init__(self, NAME: str, EMP_ID: int, QULIFICATION: str, EMAIL_ID: str, CONTACT_NO: int, sTUDENT0: set["STUDENT"] = None, aDMIN3: "ADMIN" = None):
        self.NAME = NAME
        self.EMP_ID = EMP_ID
        self.QULIFICATION = QULIFICATION
        self.EMAIL_ID = EMAIL_ID
        self.CONTACT_NO = CONTACT_NO
        self.sTUDENT0 = sTUDENT0 if sTUDENT0 is not None else set()
        self.aDMIN3 = aDMIN3
        
        pass
    @property
    def EMP_ID(self):
        return self.__EMP_ID
    @EMP_ID.setter
    def EMP_ID(self, EMP_ID: int):
        self.__EMP_ID = EMP_ID

    @property
    def CONTACT_NO(self):
        return self.__CONTACT_NO
    @CONTACT_NO.setter
    def CONTACT_NO(self, CONTACT_NO: int):
        self.__CONTACT_NO = CONTACT_NO

    @property
    def NAME(self):
        return self.__NAME
    @NAME.setter
    def NAME(self, NAME: str):
        self.__NAME = NAME

    @property
    def EMAIL_ID(self):
        return self.__EMAIL_ID
    @EMAIL_ID.setter
    def EMAIL_ID(self, EMAIL_ID: str):
        self.__EMAIL_ID = EMAIL_ID

    @property
    def QULIFICATION(self):
        return self.__QULIFICATION
    @QULIFICATION.setter
    def QULIFICATION(self, QULIFICATION: str):
        self.__QULIFICATION = QULIFICATION

    @property
    def aDMIN3(self):
        return self.__aDMIN3
    @aDMIN3.setter
    def aDMIN3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EMPLOYEE__aDMIN3", None)
        self.__aDMIN3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eMPLOYEE2"):
                opp_val = getattr(old_value, "eMPLOYEE2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eMPLOYEE2"):
                opp_val = getattr(value, "eMPLOYEE2", None)
                if opp_val is None:
                    setattr(value, "eMPLOYEE2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sTUDENT0(self):
        return self.__sTUDENT0
    @sTUDENT0.setter
    def sTUDENT0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EMPLOYEE__sTUDENT0", None)
        self.__sTUDENT0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eMPLOYEE1"):
                    opp_val = getattr(item, "eMPLOYEE1", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eMPLOYEE1"):
                    opp_val = getattr(item, "eMPLOYEE1", None)
                    
                    if opp_val is None:
                        setattr(item, "eMPLOYEE1", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class ADMIN:

    def __init__(self, NAME: str, PASSWORD: str, eMPLOYEE2: set["EMPLOYEE"] = None, sTUDENT4: set["STUDENT"] = None):
        self.NAME = NAME
        self.PASSWORD = PASSWORD
        self.eMPLOYEE2 = eMPLOYEE2 if eMPLOYEE2 is not None else set()
        self.sTUDENT4 = sTUDENT4 if sTUDENT4 is not None else set()
        
        pass
    @property
    def NAME(self):
        return self.__NAME
    @NAME.setter
    def NAME(self, NAME: str):
        self.__NAME = NAME

    @property
    def PASSWORD(self):
        return self.__PASSWORD
    @PASSWORD.setter
    def PASSWORD(self, PASSWORD: str):
        self.__PASSWORD = PASSWORD

    @property
    def eMPLOYEE2(self):
        return self.__eMPLOYEE2
    @eMPLOYEE2.setter
    def eMPLOYEE2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ADMIN__eMPLOYEE2", None)
        self.__eMPLOYEE2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aDMIN3"):
                    opp_val = getattr(item, "aDMIN3", None)
                    
                    if opp_val == self:
                        setattr(item, "aDMIN3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aDMIN3"):
                    opp_val = getattr(item, "aDMIN3", None)
                    
                    setattr(item, "aDMIN3", self)
                    

    @property
    def sTUDENT4(self):
        return self.__sTUDENT4
    @sTUDENT4.setter
    def sTUDENT4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ADMIN__sTUDENT4", None)
        self.__sTUDENT4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aDMIN5"):
                    opp_val = getattr(item, "aDMIN5", None)
                    
                    if opp_val == self:
                        setattr(item, "aDMIN5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aDMIN5"):
                    opp_val = getattr(item, "aDMIN5", None)
                    
                    setattr(item, "aDMIN5", self)
                    

