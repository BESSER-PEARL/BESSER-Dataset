from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ProjectStatus(Enum):
    active = "active"
    finished = "finished"
    suspended = "suspended"
    planned = "planned"
class ProjectSize(Enum):
    small = "small"
    medium = "medium"
    big = "big"


############################################
# Definition of Classes
############################################

class Projects_Qualification:

    pass
class Projects_Worker:

    pass
class Projects_Project:

    def __init__(self, size: str, status: str, Projects_Project9: "Projects_Company" = None, Projects_Project12: set["Projects_Worker"] = None, Projects_Project15: set["Projects_Qualification"] = None, Projects_Project19: "Projects_Project" = None, Projects_Project17: set["Projects_Project"] = None, Projects_Project: "Projects_Company" = None, Projects_Project7: "Projects_Worker" = None):
        self.size = size
        self.status = status
        self.Projects_Project9 = Projects_Project9
        self.Projects_Project12 = Projects_Project12 if Projects_Project12 is not None else set()
        self.Projects_Project15 = Projects_Project15 if Projects_Project15 is not None else set()
        self.Projects_Project19 = Projects_Project19
        self.Projects_Project17 = Projects_Project17 if Projects_Project17 is not None else set()
        self.Projects_Project = Projects_Project
        self.Projects_Project7 = Projects_Project7
        
        pass
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size


    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status


    @property
    def Projects_Project15(self):
        return self.__Projects_Project15

    @Projects_Project15.setter
    def Projects_Project15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Projects_Project__Projects_Project15", None)
        self.__Projects_Project15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Projects_Qualification16"):
                    opp_val = getattr(item, "Projects_Qualification16", None)
                    
                    if opp_val == self:
                        setattr(item, "Projects_Qualification16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Projects_Qualification16"):
                    opp_val = getattr(item, "Projects_Qualification16", None)
                    
                    setattr(item, "Projects_Qualification16", self)
                    

    @property
    def Projects_Project(self):
        return self.__Projects_Project

    @Projects_Project.setter
    def Projects_Project(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Projects_Project__Projects_Project", None)
        self.__Projects_Project = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Projects_Company"):
                opp_val = getattr(old_value, "Projects_Company", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Projects_Company"):
                opp_val = getattr(value, "Projects_Company", None)
                if opp_val is None:
                    setattr(value, "Projects_Company", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Projects_Project7(self):
        return self.__Projects_Project7

    @Projects_Project7.setter
    def Projects_Project7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Projects_Project__Projects_Project7", None)
        self.__Projects_Project7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Projects_Worker6"):
                opp_val = getattr(old_value, "Projects_Worker6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Projects_Worker6"):
                opp_val = getattr(value, "Projects_Worker6", None)
                if opp_val is None:
                    setattr(value, "Projects_Worker6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Projects_Project12(self):
        return self.__Projects_Project12

    @Projects_Project12.setter
    def Projects_Project12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Projects_Project__Projects_Project12", None)
        self.__Projects_Project12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Projects_Worker13"):
                    opp_val = getattr(item, "Projects_Worker13", None)
                    
                    if opp_val == self:
                        setattr(item, "Projects_Worker13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Projects_Worker13"):
                    opp_val = getattr(item, "Projects_Worker13", None)
                    
                    setattr(item, "Projects_Worker13", self)
                    

    @property
    def Projects_Project9(self):
        return self.__Projects_Project9

    @Projects_Project9.setter
    def Projects_Project9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Projects_Project__Projects_Project9", None)
        self.__Projects_Project9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Projects_Company10"):
                opp_val = getattr(old_value, "Projects_Company10", None)
                if opp_val == self:
                    setattr(old_value, "Projects_Company10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Projects_Company10"):
                opp_val = getattr(value, "Projects_Company10", None)
                setattr(value, "Projects_Company10", self)

    @property
    def Projects_Project19(self):
        return self.__Projects_Project19

    @Projects_Project19.setter
    def Projects_Project19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Projects_Project__Projects_Project19", None)
        self.__Projects_Project19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Projects_Project17"):
                opp_val = getattr(old_value, "Projects_Project17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Projects_Project17"):
                opp_val = getattr(value, "Projects_Project17", None)
                if opp_val is None:
                    setattr(value, "Projects_Project17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Projects_Project17(self):
        return self.__Projects_Project17

    @Projects_Project17.setter
    def Projects_Project17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Projects_Project__Projects_Project17", None)
        self.__Projects_Project17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Projects_Project19"):
                    opp_val = getattr(item, "Projects_Project19", None)
                    
                    if opp_val == self:
                        setattr(item, "Projects_Project19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Projects_Project19"):
                    opp_val = getattr(item, "Projects_Project19", None)
                    
                    setattr(item, "Projects_Project19", self)
                    

class Projects_Company:

    def __init__(self, Projects_Company10: "Projects_Project" = None, Projects_Company: set["Projects_Project"] = None, Projects_Company2: set["Projects_Worker"] = None):
        self.Projects_Company10 = Projects_Company10
        self.Projects_Company = Projects_Company if Projects_Company is not None else set()
        self.Projects_Company2 = Projects_Company2 if Projects_Company2 is not None else set()
        
        pass
    @property
    def Projects_Company10(self):
        return self.__Projects_Company10

    @Projects_Company10.setter
    def Projects_Company10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Projects_Company__Projects_Company10", None)
        self.__Projects_Company10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Projects_Project9"):
                opp_val = getattr(old_value, "Projects_Project9", None)
                if opp_val == self:
                    setattr(old_value, "Projects_Project9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Projects_Project9"):
                opp_val = getattr(value, "Projects_Project9", None)
                setattr(value, "Projects_Project9", self)

    @property
    def Projects_Company2(self):
        return self.__Projects_Company2

    @Projects_Company2.setter
    def Projects_Company2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Projects_Company__Projects_Company2", None)
        self.__Projects_Company2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Projects_Worker"):
                    opp_val = getattr(item, "Projects_Worker", None)
                    
                    if opp_val == self:
                        setattr(item, "Projects_Worker", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Projects_Worker"):
                    opp_val = getattr(item, "Projects_Worker", None)
                    
                    setattr(item, "Projects_Worker", self)
                    

    @property
    def Projects_Company(self):
        return self.__Projects_Company

    @Projects_Company.setter
    def Projects_Company(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Projects_Company__Projects_Company", None)
        self.__Projects_Company = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Projects_Project"):
                    opp_val = getattr(item, "Projects_Project", None)
                    
                    if opp_val == self:
                        setattr(item, "Projects_Project", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Projects_Project"):
                    opp_val = getattr(item, "Projects_Project", None)
                    
                    setattr(item, "Projects_Project", self)
                    

    def finish(self, Projects_p):
        # TODO: Implement finish method
        pass

    def start(self, Projects_p):
        # TODO: Implement start method
        pass

    def fire(self, Projects_w):
        # TODO: Implement fire method
        pass

    def hire(self, Projects_w):
        # TODO: Implement hire method
        pass
