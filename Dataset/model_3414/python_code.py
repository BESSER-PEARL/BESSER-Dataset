from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Award(Enum):
    Unspecified = "Unspecified"
    GrandChampion = "GrandChampion"
    ReserveChampion = "ReserveChampion"
    BlueRibbon = "BlueRibbon"
    RedRibbon = "RedRibbon"
    WhiteRibbon = "WhiteRibbon"
    PinkRibbon = "PinkRibbon"


############################################
# Definition of Classes
############################################

class Person:

    pass
class fair_YoungPerson(Person):

    pass
class fair_Class:

    def __init__(self, comments: str, name: str, Class: "fair_Department" = None, class: set["fair_Lot"] = None, fair_Class: set["fair_Person"] = None, classes: "fair_Department" = None, Class28: "fair_Lot" = None):
        self.comments = comments
        self.name = name
        self.Class = Class
        self.class = class if class is not None else set()
        self.fair_Class = fair_Class if fair_Class is not None else set()
        self.classes = classes
        self.Class28 = Class28
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def comments(self) -> str:
        return self.__comments

    @comments.setter
    def comments(self, comments: str):
        self.__comments = comments

    @property
    def classes(self):
        return self.__classes

    @classes.setter
    def classes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fair_Class__classes", None)
        self.__classes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Department25"):
                opp_val = getattr(old_value, "Department25", None)
                if opp_val == self:
                    setattr(old_value, "Department25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Department25"):
                opp_val = getattr(value, "Department25", None)
                setattr(value, "Department25", self)

    @property
    def Class(self):
        return self.__Class

    @Class.setter
    def Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fair_Class__Class", None)
        self.__Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "department"):
                opp_val = getattr(old_value, "department", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "department"):
                opp_val = getattr(value, "department", None)
                if opp_val is None:
                    setattr(value, "department", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fair_Class(self):
        return self.__fair_Class

    @fair_Class.setter
    def fair_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fair_Class__fair_Class", None)
        self.__fair_Class = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fair_Person23"):
                    opp_val = getattr(item, "fair_Person23", None)
                    
                    if opp_val == self:
                        setattr(item, "fair_Person23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fair_Person23"):
                    opp_val = getattr(item, "fair_Person23", None)
                    
                    setattr(item, "fair_Person23", self)
                    

    @property
    def class(self):
        return self.__class

    @class.setter
    def class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fair_Class__class", None)
        self.__class = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Lot21"):
                    opp_val = getattr(item, "Lot21", None)
                    
                    if opp_val == self:
                        setattr(item, "Lot21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Lot21"):
                    opp_val = getattr(item, "Lot21", None)
                    
                    setattr(item, "Lot21", self)
                    

    @property
    def Class28(self):
        return self.__Class28

    @Class28.setter
    def Class28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fair_Class__Class28", None)
        self.__Class28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lots"):
                opp_val = getattr(old_value, "lots", None)
                if opp_val == self:
                    setattr(old_value, "lots", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lots"):
                opp_val = getattr(value, "lots", None)
                setattr(value, "lots", self)

class fair_Lot:

    def __init__(self, name: str, comments: str, Lot: "fair_Exhibit" = None, lot: set["fair_Exhibit"] = None, Lot21: "fair_Class" = None, lots: "fair_Class" = None):
        self.name = name
        self.comments = comments
        self.Lot = Lot
        self.lot = lot if lot is not None else set()
        self.Lot21 = Lot21
        self.lots = lots
        
    @property
    def comments(self) -> str:
        return self.__comments

    @comments.setter
    def comments(self, comments: str):
        self.__comments = comments

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Lot(self):
        return self.__Lot

    @Lot.setter
    def Lot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fair_Lot__Lot", None)
        self.__Lot = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "exhibits"):
                opp_val = getattr(old_value, "exhibits", None)
                if opp_val == self:
                    setattr(old_value, "exhibits", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "exhibits"):
                opp_val = getattr(value, "exhibits", None)
                setattr(value, "exhibits", self)

    @property
    def lot(self):
        return self.__lot

    @lot.setter
    def lot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fair_Lot__lot", None)
        self.__lot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Exhibit"):
                    opp_val = getattr(item, "Exhibit", None)
                    
                    if opp_val == self:
                        setattr(item, "Exhibit", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Exhibit"):
                    opp_val = getattr(item, "Exhibit", None)
                    
                    setattr(item, "Exhibit", self)
                    

    @property
    def lots(self):
        return self.__lots

    @lots.setter
    def lots(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fair_Lot__lots", None)
        self.__lots = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class28"):
                opp_val = getattr(old_value, "Class28", None)
                if opp_val == self:
                    setattr(old_value, "Class28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class28"):
                opp_val = getattr(value, "Class28", None)
                setattr(value, "Class28", self)

    @property
    def Lot21(self):
        return self.__Lot21

    @Lot21.setter
    def Lot21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fair_Lot__Lot21", None)
        self.__Lot21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "class"):
                opp_val = getattr(old_value, "class", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "class"):
                opp_val = getattr(value, "class", None)
                if opp_val is None:
                    setattr(value, "class", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class fair_Animal:

    pass
class fair_Department:

    def __init__(self, name: str, comments: str, Department: "fair_Division" = None, department: set["fair_Class"] = None, fair_Department: set["fair_Person"] = None, departments: "fair_Division" = None, Department25: "fair_Class" = None):
        self.name = name
        self.comments = comments
        self.Department = Department
        self.department = department if department is not None else set()
        self.fair_Department = fair_Department if fair_Department is not None else set()
        self.departments = departments
        self.Department25 = Department25
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def comments(self) -> str:
        return self.__comments

    @comments.setter
    def comments(self, comments: str):
        self.__comments = comments

    @property
    def departments(self):
        return self.__departments

    @departments.setter
    def departments(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fair_Department__departments", None)
        self.__departments = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Division"):
                opp_val = getattr(old_value, "Division", None)
                if opp_val == self:
                    setattr(old_value, "Division", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Division"):
                opp_val = getattr(value, "Division", None)
                setattr(value, "Division", self)

    @property
    def fair_Department(self):
        return self.__fair_Department

    @fair_Department.setter
    def fair_Department(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fair_Department__fair_Department", None)
        self.__fair_Department = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fair_Person18"):
                    opp_val = getattr(item, "fair_Person18", None)
                    
                    if opp_val == self:
                        setattr(item, "fair_Person18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fair_Person18"):
                    opp_val = getattr(item, "fair_Person18", None)
                    
                    setattr(item, "fair_Person18", self)
                    

    @property
    def Department(self):
        return self.__Department

    @Department.setter
    def Department(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fair_Department__Department", None)
        self.__Department = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "division"):
                opp_val = getattr(old_value, "division", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "division"):
                opp_val = getattr(value, "division", None)
                if opp_val is None:
                    setattr(value, "division", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Department25(self):
        return self.__Department25

    @Department25.setter
    def Department25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fair_Department__Department25", None)
        self.__Department25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classes"):
                opp_val = getattr(old_value, "classes", None)
                if opp_val == self:
                    setattr(old_value, "classes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classes"):
                opp_val = getattr(value, "classes", None)
                setattr(value, "classes", self)

    @property
    def department(self):
        return self.__department

    @department.setter
    def department(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fair_Department__department", None)
        self.__department = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Class"):
                    opp_val = getattr(item, "Class", None)
                    
                    if opp_val == self:
                        setattr(item, "Class", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Class"):
                    opp_val = getattr(item, "Class", None)
                    
                    setattr(item, "Class", self)
                    

class fair_Premises:

    pass
class fair_Division:

    def __init__(self, name: str, comments: str, fair_Division: "fair_Fair" = None, division: set["fair_Department"] = None, Division: "fair_Department" = None):
        self.name = name
        self.comments = comments
        self.fair_Division = fair_Division
        self.division = division if division is not None else set()
        self.Division = Division
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def comments(self) -> str:
        return self.__comments

    @comments.setter
    def comments(self, comments: str):
        self.__comments = comments

    @property
    def division(self):
        return self.__division

    @division.setter
    def division(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fair_Division__division", None)
        self.__division = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Department"):
                    opp_val = getattr(item, "Department", None)
                    
                    if opp_val == self:
                        setattr(item, "Department", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Department"):
                    opp_val = getattr(item, "Department", None)
                    
                    setattr(item, "Department", self)
                    

    @property
    def Division(self):
        return self.__Division

    @Division.setter
    def Division(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fair_Division__Division", None)
        self.__Division = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "departments"):
                opp_val = getattr(old_value, "departments", None)
                if opp_val == self:
                    setattr(old_value, "departments", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "departments"):
                opp_val = getattr(value, "departments", None)
                setattr(value, "departments", self)

    @property
    def fair_Division(self):
        return self.__fair_Division

    @fair_Division.setter
    def fair_Division(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fair_Division__fair_Division", None)
        self.__fair_Division = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fair_Fair2"):
                opp_val = getattr(old_value, "fair_Fair2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fair_Fair2"):
                opp_val = getattr(value, "fair_Fair2", None)
                if opp_val is None:
                    setattr(value, "fair_Fair2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class fair_YouthClub:

    def __init__(self, name: str, comments: str, fair_YouthClub: "fair_Fair" = None, fair_YouthClub13: set["fair_Person"] = None, fair_YouthClub33: "fair_YoungPerson" = None):
        self.name = name
        self.comments = comments
        self.fair_YouthClub = fair_YouthClub
        self.fair_YouthClub13 = fair_YouthClub13 if fair_YouthClub13 is not None else set()
        self.fair_YouthClub33 = fair_YouthClub33
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def comments(self) -> str:
        return self.__comments

    @comments.setter
    def comments(self, comments: str):
        self.__comments = comments

    @property
    def fair_YouthClub33(self):
        return self.__fair_YouthClub33

    @fair_YouthClub33.setter
    def fair_YouthClub33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fair_YouthClub__fair_YouthClub33", None)
        self.__fair_YouthClub33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fair_YoungPerson32"):
                opp_val = getattr(old_value, "fair_YoungPerson32", None)
                if opp_val == self:
                    setattr(old_value, "fair_YoungPerson32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fair_YoungPerson32"):
                opp_val = getattr(value, "fair_YoungPerson32", None)
                setattr(value, "fair_YoungPerson32", self)

    @property
    def fair_YouthClub13(self):
        return self.__fair_YouthClub13

    @fair_YouthClub13.setter
    def fair_YouthClub13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fair_YouthClub__fair_YouthClub13", None)
        self.__fair_YouthClub13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fair_Person14"):
                    opp_val = getattr(item, "fair_Person14", None)
                    
                    if opp_val == self:
                        setattr(item, "fair_Person14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fair_Person14"):
                    opp_val = getattr(item, "fair_Person14", None)
                    
                    setattr(item, "fair_Person14", self)
                    

    @property
    def fair_YouthClub(self):
        return self.__fair_YouthClub

    @fair_YouthClub.setter
    def fair_YouthClub(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fair_YouthClub__fair_YouthClub", None)
        self.__fair_YouthClub = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fair_Fair"):
                opp_val = getattr(old_value, "fair_Fair", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fair_Fair"):
                opp_val = getattr(value, "fair_Fair", None)
                if opp_val is None:
                    setattr(value, "fair_Fair", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class fair_Fair:

    def __init__(self, comments: str, name: str, fair_Fair6: set["fair_Person"] = None, fair_Fair: set["fair_YouthClub"] = None, fair_Fair2: set["fair_Division"] = None, fair_Fair4: "fair_Premises" = None):
        self.comments = comments
        self.name = name
        self.fair_Fair6 = fair_Fair6 if fair_Fair6 is not None else set()
        self.fair_Fair = fair_Fair if fair_Fair is not None else set()
        self.fair_Fair2 = fair_Fair2 if fair_Fair2 is not None else set()
        self.fair_Fair4 = fair_Fair4
        
    @property
    def comments(self) -> str:
        return self.__comments

    @comments.setter
    def comments(self, comments: str):
        self.__comments = comments

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fair_Fair2(self):
        return self.__fair_Fair2

    @fair_Fair2.setter
    def fair_Fair2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fair_Fair__fair_Fair2", None)
        self.__fair_Fair2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fair_Division"):
                    opp_val = getattr(item, "fair_Division", None)
                    
                    if opp_val == self:
                        setattr(item, "fair_Division", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fair_Division"):
                    opp_val = getattr(item, "fair_Division", None)
                    
                    setattr(item, "fair_Division", self)
                    

    @property
    def fair_Fair6(self):
        return self.__fair_Fair6

    @fair_Fair6.setter
    def fair_Fair6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fair_Fair__fair_Fair6", None)
        self.__fair_Fair6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fair_Person"):
                    opp_val = getattr(item, "fair_Person", None)
                    
                    if opp_val == self:
                        setattr(item, "fair_Person", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fair_Person"):
                    opp_val = getattr(item, "fair_Person", None)
                    
                    setattr(item, "fair_Person", self)
                    

    @property
    def fair_Fair(self):
        return self.__fair_Fair

    @fair_Fair.setter
    def fair_Fair(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fair_Fair__fair_Fair", None)
        self.__fair_Fair = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fair_YouthClub"):
                    opp_val = getattr(item, "fair_YouthClub", None)
                    
                    if opp_val == self:
                        setattr(item, "fair_YouthClub", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fair_YouthClub"):
                    opp_val = getattr(item, "fair_YouthClub", None)
                    
                    setattr(item, "fair_YouthClub", self)
                    

    @property
    def fair_Fair4(self):
        return self.__fair_Fair4

    @fair_Fair4.setter
    def fair_Fair4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fair_Fair__fair_Fair4", None)
        self.__fair_Fair4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fair_Premises"):
                opp_val = getattr(old_value, "fair_Premises", None)
                if opp_val == self:
                    setattr(old_value, "fair_Premises", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fair_Premises"):
                opp_val = getattr(value, "fair_Premises", None)
                setattr(value, "fair_Premises", self)

    def exhibits(self) -> str:
        # TODO: Implement exhibits method
        pass

class fair_Exhibit:

    def __init__(self, name: str, number: int, comments: str, salesOrder: int, inAuction: bool, award: str, fair_Exhibit: "fair_Animal" = None, fair_Exhibit9: "fair_Person" = None, exhibits: "fair_Lot" = None, Exhibit: "fair_Lot" = None):
        self.name = name
        self.number = number
        self.comments = comments
        self.salesOrder = salesOrder
        self.inAuction = inAuction
        self.award = award
        self.fair_Exhibit = fair_Exhibit
        self.fair_Exhibit9 = fair_Exhibit9
        self.exhibits = exhibits
        self.Exhibit = Exhibit
        
    @property
    def comments(self) -> str:
        return self.__comments

    @comments.setter
    def comments(self, comments: str):
        self.__comments = comments

    @property
    def inAuction(self) -> bool:
        return self.__inAuction

    @inAuction.setter
    def inAuction(self, inAuction: bool):
        self.__inAuction = inAuction

    @property
    def number(self) -> int:
        return self.__number

    @number.setter
    def number(self, number: int):
        self.__number = number

    @property
    def salesOrder(self) -> int:
        return self.__salesOrder

    @salesOrder.setter
    def salesOrder(self, salesOrder: int):
        self.__salesOrder = salesOrder

    @property
    def award(self) -> str:
        return self.__award

    @award.setter
    def award(self, award: str):
        self.__award = award

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Exhibit(self):
        return self.__Exhibit

    @Exhibit.setter
    def Exhibit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fair_Exhibit__Exhibit", None)
        self.__Exhibit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lot"):
                opp_val = getattr(old_value, "lot", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lot"):
                opp_val = getattr(value, "lot", None)
                if opp_val is None:
                    setattr(value, "lot", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fair_Exhibit(self):
        return self.__fair_Exhibit

    @fair_Exhibit.setter
    def fair_Exhibit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fair_Exhibit__fair_Exhibit", None)
        self.__fair_Exhibit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fair_Animal"):
                opp_val = getattr(old_value, "fair_Animal", None)
                if opp_val == self:
                    setattr(old_value, "fair_Animal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fair_Animal"):
                opp_val = getattr(value, "fair_Animal", None)
                setattr(value, "fair_Animal", self)

    @property
    def exhibits(self):
        return self.__exhibits

    @exhibits.setter
    def exhibits(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fair_Exhibit__exhibits", None)
        self.__exhibits = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Lot"):
                opp_val = getattr(old_value, "Lot", None)
                if opp_val == self:
                    setattr(old_value, "Lot", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Lot"):
                opp_val = getattr(value, "Lot", None)
                setattr(value, "Lot", self)

    @property
    def fair_Exhibit9(self):
        return self.__fair_Exhibit9

    @fair_Exhibit9.setter
    def fair_Exhibit9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fair_Exhibit__fair_Exhibit9", None)
        self.__fair_Exhibit9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fair_Person10"):
                opp_val = getattr(old_value, "fair_Person10", None)
                if opp_val == self:
                    setattr(old_value, "fair_Person10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fair_Person10"):
                opp_val = getattr(value, "fair_Person10", None)
                setattr(value, "fair_Person10", self)

class fair_Person:

    def __init__(self, firstName: str, lastName: str, phone: str, street: str, city: str, state: str, zipCode: str, name: str, comments: str, pin: str, salesOrder: int, fair_Person: "fair_Fair" = None, fair_Person10: "fair_Exhibit" = None, fair_Person14: "fair_YouthClub" = None, fair_Person18: "fair_Department" = None, fair_Person23: "fair_Class" = None, fair_Person30: "fair_YoungPerson" = None):
        self.firstName = firstName
        self.lastName = lastName
        self.phone = phone
        self.street = street
        self.city = city
        self.state = state
        self.zipCode = zipCode
        self.name = name
        self.comments = comments
        self.pin = pin
        self.salesOrder = salesOrder
        self.fair_Person = fair_Person
        self.fair_Person10 = fair_Person10
        self.fair_Person14 = fair_Person14
        self.fair_Person18 = fair_Person18
        self.fair_Person23 = fair_Person23
        self.fair_Person30 = fair_Person30
        
    @property
    def city(self) -> str:
        return self.__city

    @city.setter
    def city(self, city: str):
        self.__city = city

    @property
    def phone(self) -> str:
        return self.__phone

    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone

    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def zipCode(self) -> str:
        return self.__zipCode

    @zipCode.setter
    def zipCode(self, zipCode: str):
        self.__zipCode = zipCode

    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def comments(self) -> str:
        return self.__comments

    @comments.setter
    def comments(self, comments: str):
        self.__comments = comments

    @property
    def salesOrder(self) -> int:
        return self.__salesOrder

    @salesOrder.setter
    def salesOrder(self, salesOrder: int):
        self.__salesOrder = salesOrder

    @property
    def street(self) -> str:
        return self.__street

    @street.setter
    def street(self, street: str):
        self.__street = street

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pin(self) -> str:
        return self.__pin

    @pin.setter
    def pin(self, pin: str):
        self.__pin = pin

    @property
    def fair_Person30(self):
        return self.__fair_Person30

    @fair_Person30.setter
    def fair_Person30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fair_Person__fair_Person30", None)
        self.__fair_Person30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fair_YoungPerson"):
                opp_val = getattr(old_value, "fair_YoungPerson", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fair_YoungPerson"):
                opp_val = getattr(value, "fair_YoungPerson", None)
                if opp_val is None:
                    setattr(value, "fair_YoungPerson", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fair_Person18(self):
        return self.__fair_Person18

    @fair_Person18.setter
    def fair_Person18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fair_Person__fair_Person18", None)
        self.__fair_Person18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fair_Department"):
                opp_val = getattr(old_value, "fair_Department", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fair_Department"):
                opp_val = getattr(value, "fair_Department", None)
                if opp_val is None:
                    setattr(value, "fair_Department", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fair_Person23(self):
        return self.__fair_Person23

    @fair_Person23.setter
    def fair_Person23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fair_Person__fair_Person23", None)
        self.__fair_Person23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fair_Class"):
                opp_val = getattr(old_value, "fair_Class", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fair_Class"):
                opp_val = getattr(value, "fair_Class", None)
                if opp_val is None:
                    setattr(value, "fair_Class", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fair_Person(self):
        return self.__fair_Person

    @fair_Person.setter
    def fair_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fair_Person__fair_Person", None)
        self.__fair_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fair_Fair6"):
                opp_val = getattr(old_value, "fair_Fair6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fair_Fair6"):
                opp_val = getattr(value, "fair_Fair6", None)
                if opp_val is None:
                    setattr(value, "fair_Fair6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fair_Person14(self):
        return self.__fair_Person14

    @fair_Person14.setter
    def fair_Person14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fair_Person__fair_Person14", None)
        self.__fair_Person14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fair_YouthClub13"):
                opp_val = getattr(old_value, "fair_YouthClub13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fair_YouthClub13"):
                opp_val = getattr(value, "fair_YouthClub13", None)
                if opp_val is None:
                    setattr(value, "fair_YouthClub13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fair_Person10(self):
        return self.__fair_Person10

    @fair_Person10.setter
    def fair_Person10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fair_Person__fair_Person10", None)
        self.__fair_Person10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fair_Exhibit9"):
                opp_val = getattr(old_value, "fair_Exhibit9", None)
                if opp_val == self:
                    setattr(old_value, "fair_Exhibit9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fair_Exhibit9"):
                opp_val = getattr(value, "fair_Exhibit9", None)
                setattr(value, "fair_Exhibit9", self)
