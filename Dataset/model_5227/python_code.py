from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class projectPlanning_Assignment:

    pass
class projectPlanning_Rating:

    def __init__(self, rating: int, projectPlanning_Rating: "projectPlanning_ProjectPlan" = None, projectPlanning_Rating17: "projectPlanning_Employee" = None, projectPlanning_Rating19: "projectPlanning_Capability" = None):
        self.rating = rating
        self.projectPlanning_Rating = projectPlanning_Rating
        self.projectPlanning_Rating17 = projectPlanning_Rating17
        self.projectPlanning_Rating19 = projectPlanning_Rating19
        
    @property
    def rating(self) -> int:
        return self.__rating

    @rating.setter
    def rating(self, rating: int):
        self.__rating = rating

    @property
    def projectPlanning_Rating(self):
        return self.__projectPlanning_Rating

    @projectPlanning_Rating.setter
    def projectPlanning_Rating(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_projectPlanning_Rating__projectPlanning_Rating", None)
        self.__projectPlanning_Rating = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "projectPlanning_ProjectPlan6"):
                opp_val = getattr(old_value, "projectPlanning_ProjectPlan6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "projectPlanning_ProjectPlan6"):
                opp_val = getattr(value, "projectPlanning_ProjectPlan6", None)
                if opp_val is None:
                    setattr(value, "projectPlanning_ProjectPlan6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def projectPlanning_Rating19(self):
        return self.__projectPlanning_Rating19

    @projectPlanning_Rating19.setter
    def projectPlanning_Rating19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_projectPlanning_Rating__projectPlanning_Rating19", None)
        self.__projectPlanning_Rating19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "projectPlanning_Capability20"):
                opp_val = getattr(old_value, "projectPlanning_Capability20", None)
                if opp_val == self:
                    setattr(old_value, "projectPlanning_Capability20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "projectPlanning_Capability20"):
                opp_val = getattr(value, "projectPlanning_Capability20", None)
                setattr(value, "projectPlanning_Capability20", self)

    @property
    def projectPlanning_Rating17(self):
        return self.__projectPlanning_Rating17

    @projectPlanning_Rating17.setter
    def projectPlanning_Rating17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_projectPlanning_Rating__projectPlanning_Rating17", None)
        self.__projectPlanning_Rating17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "projectPlanning_Employee16"):
                opp_val = getattr(old_value, "projectPlanning_Employee16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "projectPlanning_Employee16"):
                opp_val = getattr(value, "projectPlanning_Employee16", None)
                if opp_val is None:
                    setattr(value, "projectPlanning_Employee16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class projectPlanning_Project:

    def __init__(self, name: str, requiresResources: int, projectPlanning_Project: "projectPlanning_ProjectPlan" = None, projectPlanning_Project10: set["projectPlanning_Capability"] = None, projectPlanning_Project23: "projectPlanning_Assignment" = None):
        self.name = name
        self.requiresResources = requiresResources
        self.projectPlanning_Project = projectPlanning_Project
        self.projectPlanning_Project10 = projectPlanning_Project10 if projectPlanning_Project10 is not None else set()
        self.projectPlanning_Project23 = projectPlanning_Project23
        
    @property
    def requiresResources(self) -> int:
        return self.__requiresResources

    @requiresResources.setter
    def requiresResources(self, requiresResources: int):
        self.__requiresResources = requiresResources

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def projectPlanning_Project(self):
        return self.__projectPlanning_Project

    @projectPlanning_Project.setter
    def projectPlanning_Project(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_projectPlanning_Project__projectPlanning_Project", None)
        self.__projectPlanning_Project = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "projectPlanning_ProjectPlan4"):
                opp_val = getattr(old_value, "projectPlanning_ProjectPlan4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "projectPlanning_ProjectPlan4"):
                opp_val = getattr(value, "projectPlanning_ProjectPlan4", None)
                if opp_val is None:
                    setattr(value, "projectPlanning_ProjectPlan4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def projectPlanning_Project10(self):
        return self.__projectPlanning_Project10

    @projectPlanning_Project10.setter
    def projectPlanning_Project10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_projectPlanning_Project__projectPlanning_Project10", None)
        self.__projectPlanning_Project10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "projectPlanning_Capability11"):
                    opp_val = getattr(item, "projectPlanning_Capability11", None)
                    
                    if opp_val == self:
                        setattr(item, "projectPlanning_Capability11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "projectPlanning_Capability11"):
                    opp_val = getattr(item, "projectPlanning_Capability11", None)
                    
                    setattr(item, "projectPlanning_Capability11", self)
                    

    @property
    def projectPlanning_Project23(self):
        return self.__projectPlanning_Project23

    @projectPlanning_Project23.setter
    def projectPlanning_Project23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_projectPlanning_Project__projectPlanning_Project23", None)
        self.__projectPlanning_Project23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "projectPlanning_Assignment22"):
                opp_val = getattr(old_value, "projectPlanning_Assignment22", None)
                if opp_val == self:
                    setattr(old_value, "projectPlanning_Assignment22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "projectPlanning_Assignment22"):
                opp_val = getattr(value, "projectPlanning_Assignment22", None)
                setattr(value, "projectPlanning_Assignment22", self)

class projectPlanning_Employee:

    def __init__(self, name: str, hasResource: int, projectPlanning_Employee: "projectPlanning_ProjectPlan" = None, projectPlanning_Employee13: set["projectPlanning_Capability"] = None, projectPlanning_Employee16: set["projectPlanning_Rating"] = None, projectPlanning_Employee26: "projectPlanning_Assignment" = None):
        self.name = name
        self.hasResource = hasResource
        self.projectPlanning_Employee = projectPlanning_Employee
        self.projectPlanning_Employee13 = projectPlanning_Employee13 if projectPlanning_Employee13 is not None else set()
        self.projectPlanning_Employee16 = projectPlanning_Employee16 if projectPlanning_Employee16 is not None else set()
        self.projectPlanning_Employee26 = projectPlanning_Employee26
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def hasResource(self) -> int:
        return self.__hasResource

    @hasResource.setter
    def hasResource(self, hasResource: int):
        self.__hasResource = hasResource

    @property
    def projectPlanning_Employee(self):
        return self.__projectPlanning_Employee

    @projectPlanning_Employee.setter
    def projectPlanning_Employee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_projectPlanning_Employee__projectPlanning_Employee", None)
        self.__projectPlanning_Employee = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "projectPlanning_ProjectPlan2"):
                opp_val = getattr(old_value, "projectPlanning_ProjectPlan2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "projectPlanning_ProjectPlan2"):
                opp_val = getattr(value, "projectPlanning_ProjectPlan2", None)
                if opp_val is None:
                    setattr(value, "projectPlanning_ProjectPlan2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def projectPlanning_Employee16(self):
        return self.__projectPlanning_Employee16

    @projectPlanning_Employee16.setter
    def projectPlanning_Employee16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_projectPlanning_Employee__projectPlanning_Employee16", None)
        self.__projectPlanning_Employee16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "projectPlanning_Rating17"):
                    opp_val = getattr(item, "projectPlanning_Rating17", None)
                    
                    if opp_val == self:
                        setattr(item, "projectPlanning_Rating17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "projectPlanning_Rating17"):
                    opp_val = getattr(item, "projectPlanning_Rating17", None)
                    
                    setattr(item, "projectPlanning_Rating17", self)
                    

    @property
    def projectPlanning_Employee26(self):
        return self.__projectPlanning_Employee26

    @projectPlanning_Employee26.setter
    def projectPlanning_Employee26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_projectPlanning_Employee__projectPlanning_Employee26", None)
        self.__projectPlanning_Employee26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "projectPlanning_Assignment25"):
                opp_val = getattr(old_value, "projectPlanning_Assignment25", None)
                if opp_val == self:
                    setattr(old_value, "projectPlanning_Assignment25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "projectPlanning_Assignment25"):
                opp_val = getattr(value, "projectPlanning_Assignment25", None)
                setattr(value, "projectPlanning_Assignment25", self)

    @property
    def projectPlanning_Employee13(self):
        return self.__projectPlanning_Employee13

    @projectPlanning_Employee13.setter
    def projectPlanning_Employee13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_projectPlanning_Employee__projectPlanning_Employee13", None)
        self.__projectPlanning_Employee13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "projectPlanning_Capability14"):
                    opp_val = getattr(item, "projectPlanning_Capability14", None)
                    
                    if opp_val == self:
                        setattr(item, "projectPlanning_Capability14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "projectPlanning_Capability14"):
                    opp_val = getattr(item, "projectPlanning_Capability14", None)
                    
                    setattr(item, "projectPlanning_Capability14", self)
                    

class projectPlanning_Capability:

    def __init__(self, name: str, projectPlanning_Capability: "projectPlanning_ProjectPlan" = None, projectPlanning_Capability11: "projectPlanning_Project" = None, projectPlanning_Capability14: "projectPlanning_Employee" = None, projectPlanning_Capability20: "projectPlanning_Rating" = None):
        self.name = name
        self.projectPlanning_Capability = projectPlanning_Capability
        self.projectPlanning_Capability11 = projectPlanning_Capability11
        self.projectPlanning_Capability14 = projectPlanning_Capability14
        self.projectPlanning_Capability20 = projectPlanning_Capability20
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def projectPlanning_Capability11(self):
        return self.__projectPlanning_Capability11

    @projectPlanning_Capability11.setter
    def projectPlanning_Capability11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_projectPlanning_Capability__projectPlanning_Capability11", None)
        self.__projectPlanning_Capability11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "projectPlanning_Project10"):
                opp_val = getattr(old_value, "projectPlanning_Project10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "projectPlanning_Project10"):
                opp_val = getattr(value, "projectPlanning_Project10", None)
                if opp_val is None:
                    setattr(value, "projectPlanning_Project10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def projectPlanning_Capability20(self):
        return self.__projectPlanning_Capability20

    @projectPlanning_Capability20.setter
    def projectPlanning_Capability20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_projectPlanning_Capability__projectPlanning_Capability20", None)
        self.__projectPlanning_Capability20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "projectPlanning_Rating19"):
                opp_val = getattr(old_value, "projectPlanning_Rating19", None)
                if opp_val == self:
                    setattr(old_value, "projectPlanning_Rating19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "projectPlanning_Rating19"):
                opp_val = getattr(value, "projectPlanning_Rating19", None)
                setattr(value, "projectPlanning_Rating19", self)

    @property
    def projectPlanning_Capability14(self):
        return self.__projectPlanning_Capability14

    @projectPlanning_Capability14.setter
    def projectPlanning_Capability14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_projectPlanning_Capability__projectPlanning_Capability14", None)
        self.__projectPlanning_Capability14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "projectPlanning_Employee13"):
                opp_val = getattr(old_value, "projectPlanning_Employee13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "projectPlanning_Employee13"):
                opp_val = getattr(value, "projectPlanning_Employee13", None)
                if opp_val is None:
                    setattr(value, "projectPlanning_Employee13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def projectPlanning_Capability(self):
        return self.__projectPlanning_Capability

    @projectPlanning_Capability.setter
    def projectPlanning_Capability(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_projectPlanning_Capability__projectPlanning_Capability", None)
        self.__projectPlanning_Capability = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "projectPlanning_ProjectPlan"):
                opp_val = getattr(old_value, "projectPlanning_ProjectPlan", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "projectPlanning_ProjectPlan"):
                opp_val = getattr(value, "projectPlanning_ProjectPlan", None)
                if opp_val is None:
                    setattr(value, "projectPlanning_ProjectPlan", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class projectPlanning_ProjectPlan:

    pass