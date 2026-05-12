from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class PERSONAL_PAGE:

    def __init__(self, BRANCH: str, YEAR: int, wELCOME_PAGE6: "WELCOME_PAGE" = None):
        self.BRANCH = BRANCH
        self.YEAR = YEAR
        self.wELCOME_PAGE6 = wELCOME_PAGE6
        
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
    def wELCOME_PAGE6(self):
        return self.__wELCOME_PAGE6
    @wELCOME_PAGE6.setter
    def wELCOME_PAGE6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PERSONAL_PAGE__wELCOME_PAGE6", None)
        self.__wELCOME_PAGE6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pERSONAL_PAGE7"):
                opp_val = getattr(old_value, "pERSONAL_PAGE7", None)
                if opp_val == self:
                    setattr(old_value, "pERSONAL_PAGE7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pERSONAL_PAGE7"):
                opp_val = getattr(value, "pERSONAL_PAGE7", None)
                setattr(value, "pERSONAL_PAGE7", self)



class PLACEMENTS_PAGE:

    def __init__(self, SALARY: int, BRANCH: str, INTREST: str, wELCOME_PAGE9: "WELCOME_PAGE" = None):
        self.SALARY = SALARY
        self.BRANCH = BRANCH
        self.INTREST = INTREST
        self.wELCOME_PAGE9 = wELCOME_PAGE9
        
        pass
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

    @property
    def INTREST(self):
        return self.__INTREST
    @INTREST.setter
    def INTREST(self, INTREST: str):
        self.__INTREST = INTREST

    @property
    def wELCOME_PAGE9(self):
        return self.__wELCOME_PAGE9
    @wELCOME_PAGE9.setter
    def wELCOME_PAGE9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PLACEMENTS_PAGE__wELCOME_PAGE9", None)
        self.__wELCOME_PAGE9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pLACEMENTS_PAGE8"):
                opp_val = getattr(old_value, "pLACEMENTS_PAGE8", None)
                if opp_val == self:
                    setattr(old_value, "pLACEMENTS_PAGE8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pLACEMENTS_PAGE8"):
                opp_val = getattr(value, "pLACEMENTS_PAGE8", None)
                setattr(value, "pLACEMENTS_PAGE8", self)



class ACADEMIC_PAGE:

    def __init__(self, BRANCH: str, STUDIES: str, user5: "WELCOME_PAGE" = None):
        self.BRANCH = BRANCH
        self.STUDIES = STUDIES
        self.user5 = user5
        
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
    def user5(self):
        return self.__user5
    @user5.setter
    def user5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ACADEMIC_PAGE__user5", None)
        self.__user5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "group4"):
                opp_val = getattr(old_value, "group4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "group4"):
                opp_val = getattr(value, "group4", None)
                if opp_val is None:
                    setattr(value, "group4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class DATABASE_SYSTEM:

    def __init__(self, Content: bool, user3: "WELCOME_PAGE" = None):
        self.Content = Content
        self.user3 = user3
        
        pass
    @property
    def Content(self):
        return self.__Content
    @Content.setter
    def Content(self, Content: bool):
        self.__Content = Content

    @property
    def user3(self):
        return self.__user3
    @user3.setter
    def user3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DATABASE_SYSTEM__user3", None)
        self.__user3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "post2"):
                opp_val = getattr(old_value, "post2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "post2"):
                opp_val = getattr(value, "post2", None)
                if opp_val is None:
                    setattr(value, "post2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class T:

    pass


class LoginPage:

    def __init__(self, User_name: str, user1: "WELCOME_PAGE" = None):
        self.User_name = User_name
        self.user1 = user1
        
        pass
    @property
    def User_name(self):
        return self.__User_name
    @User_name.setter
    def User_name(self, User_name: str):
        self.__User_name = User_name

    @property
    def user1(self):
        return self.__user1
    @user1.setter
    def user1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LoginPage__user1", None)
        self.__user1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myprofile0"):
                opp_val = getattr(old_value, "myprofile0", None)
                if opp_val == self:
                    setattr(old_value, "myprofile0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myprofile0"):
                opp_val = getattr(value, "myprofile0", None)
                setattr(value, "myprofile0", self)



class WELCOME_PAGE:

    def __init__(self, personal: str, academic: str, placements: str, myprofile0: "LoginPage" = None, post2: set["DATABASE_SYSTEM"] = None, group4: set["ACADEMIC_PAGE"] = None, pERSONAL_PAGE7: "PERSONAL_PAGE" = None, pLACEMENTS_PAGE8: "PLACEMENTS_PAGE" = None):
        self.personal = personal
        self.academic = academic
        self.placements = placements
        self.myprofile0 = myprofile0
        self.post2 = post2 if post2 is not None else set()
        self.group4 = group4 if group4 is not None else set()
        self.pERSONAL_PAGE7 = pERSONAL_PAGE7
        self.pLACEMENTS_PAGE8 = pLACEMENTS_PAGE8
        
        pass
    @property
    def personal(self):
        return self.__personal
    @personal.setter
    def personal(self, personal: str):
        self.__personal = personal

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
    def pERSONAL_PAGE7(self):
        return self.__pERSONAL_PAGE7
    @pERSONAL_PAGE7.setter
    def pERSONAL_PAGE7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WELCOME_PAGE__pERSONAL_PAGE7", None)
        self.__pERSONAL_PAGE7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wELCOME_PAGE6"):
                opp_val = getattr(old_value, "wELCOME_PAGE6", None)
                if opp_val == self:
                    setattr(old_value, "wELCOME_PAGE6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wELCOME_PAGE6"):
                opp_val = getattr(value, "wELCOME_PAGE6", None)
                setattr(value, "wELCOME_PAGE6", self)

    @property
    def myprofile0(self):
        return self.__myprofile0
    @myprofile0.setter
    def myprofile0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WELCOME_PAGE__myprofile0", None)
        self.__myprofile0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user1"):
                opp_val = getattr(old_value, "user1", None)
                if opp_val == self:
                    setattr(old_value, "user1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user1"):
                opp_val = getattr(value, "user1", None)
                setattr(value, "user1", self)

    @property
    def group4(self):
        return self.__group4
    @group4.setter
    def group4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WELCOME_PAGE__group4", None)
        self.__group4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "user5"):
                    opp_val = getattr(item, "user5", None)
                    
                    if opp_val == self:
                        setattr(item, "user5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "user5"):
                    opp_val = getattr(item, "user5", None)
                    
                    setattr(item, "user5", self)
                    

    @property
    def pLACEMENTS_PAGE8(self):
        return self.__pLACEMENTS_PAGE8
    @pLACEMENTS_PAGE8.setter
    def pLACEMENTS_PAGE8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WELCOME_PAGE__pLACEMENTS_PAGE8", None)
        self.__pLACEMENTS_PAGE8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wELCOME_PAGE9"):
                opp_val = getattr(old_value, "wELCOME_PAGE9", None)
                if opp_val == self:
                    setattr(old_value, "wELCOME_PAGE9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wELCOME_PAGE9"):
                opp_val = getattr(value, "wELCOME_PAGE9", None)
                setattr(value, "wELCOME_PAGE9", self)

    @property
    def post2(self):
        return self.__post2
    @post2.setter
    def post2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WELCOME_PAGE__post2", None)
        self.__post2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "user3"):
                    opp_val = getattr(item, "user3", None)
                    
                    if opp_val == self:
                        setattr(item, "user3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "user3"):
                    opp_val = getattr(item, "user3", None)
                    
                    setattr(item, "user3", self)
                    

