from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Welcome:

    def __init__(self, personal: str, academic: str, placements: str):
        self.personal = personal
        self.academic = academic
        self.placements = placements
        
        pass
    @property
    def placements(self):
        return self.__placements
    @placements.setter
    def placements(self, placements: str):
        self.__placements = placements

    @property
    def academic(self):
        return self.__academic
    @academic.setter
    def academic(self, academic: str):
        self.__academic = academic

    @property
    def personal(self):
        return self.__personal
    @personal.setter
    def personal(self, personal: str):
        self.__personal = personal



class ACADEMIC_PAGE:

    def __init__(self, BRANCH: str, STUDIES: str, lineItems0: set["PERSONAL_PAGE"] = None):
        self.BRANCH = BRANCH
        self.STUDIES = STUDIES
        self.lineItems0 = lineItems0 if lineItems0 is not None else set()
        
        pass
    @property
    def BRANCH(self):
        return self.__BRANCH
    @BRANCH.setter
    def BRANCH(self, BRANCH: str):
        self.__BRANCH = BRANCH

    @property
    def STUDIES(self):
        return self.__STUDIES
    @STUDIES.setter
    def STUDIES(self, STUDIES: str):
        self.__STUDIES = STUDIES

    @property
    def lineItems0(self):
        return self.__lineItems0
    @lineItems0.setter
    def lineItems0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ACADEMIC_PAGE__lineItems0", None)
        self.__lineItems0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "product1"):
                    opp_val = getattr(item, "product1", None)
                    
                    if opp_val == self:
                        setattr(item, "product1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "product1"):
                    opp_val = getattr(item, "product1", None)
                    
                    setattr(item, "product1", self)
                    



class PERSONAL_PAGE:

    def __init__(self, YEAR: int, BRANCH: str, product1: "ACADEMIC_PAGE" = None):
        self.YEAR = YEAR
        self.BRANCH = BRANCH
        self.product1 = product1
        
        pass
    @property
    def BRANCH(self):
        return self.__BRANCH
    @BRANCH.setter
    def BRANCH(self, BRANCH: str):
        self.__BRANCH = BRANCH

    @property
    def YEAR(self):
        return self.__YEAR
    @YEAR.setter
    def YEAR(self, YEAR: int):
        self.__YEAR = YEAR

    @property
    def product1(self):
        return self.__product1
    @product1.setter
    def product1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PERSONAL_PAGE__product1", None)
        self.__product1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lineItems0"):
                opp_val = getattr(old_value, "lineItems0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lineItems0"):
                opp_val = getattr(value, "lineItems0", None)
                if opp_val is None:
                    setattr(value, "lineItems0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class PLACEMENTS_PAGE:

    def __init__(self, SALARY: int, BRANCH: str, INTREST: str):
        self.SALARY = SALARY
        self.BRANCH = BRANCH
        self.INTREST = INTREST
        
        pass
    @property
    def INTREST(self):
        return self.__INTREST
    @INTREST.setter
    def INTREST(self, INTREST: str):
        self.__INTREST = INTREST

    @property
    def SALARY(self):
        return self.__SALARY
    @SALARY.setter
    def SALARY(self, SALARY: int):
        self.__SALARY = SALARY

    @property
    def BRANCH(self):
        return self.__BRANCH
    @BRANCH.setter
    def BRANCH(self, BRANCH: str):
        self.__BRANCH = BRANCH



class WebUser:

    def __init__(self, login: str, password: str, state: str):
        self.login = login
        self.password = password
        self.state = state
        
        pass
    @property
    def state(self):
        return self.__state
    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def login(self):
        return self.__login
    @login.setter
    def login(self, login: str):
        self.__login = login



class Database_system:

    def __init__(self, Content: bool):
        self.Content = Content
        
        pass
    @property
    def Content(self):
        return self.__Content
    @Content.setter
    def Content(self, Content: bool):
        self.__Content = Content

