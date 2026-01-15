from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class CarGroupKind(Enum):
    compact = "compact"
    intermediate = "intermediate"
    luxury = "luxury"


############################################
# Definition of Classes
############################################

class CarRental_Check:

    def __init__(self, description: str):
        self.description = description
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

class CarRental_ServiceDepot:

    def __init__(self, location: str):
        self.location = location
        
    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

class CarRental_CarGroup:

    def __init__(self, kind: str, CarGroup: "CarRental_Branch" = None, CarGroup25: "CarRental_Rental" = None, carGroup: set["CarRental_Branch"] = None, carGroup29: set["CarRental_Car"] = None, carGroup32: set["CarRental_Rental"] = None, CarGroup36: "CarRental_CarGroup" = None, lower: "CarRental_CarGroup" = None, CarGroup39: "CarRental_CarGroup" = None, higher: "CarRental_CarGroup" = None, CarGroup44: "CarRental_Car" = None):
        self.kind = kind
        self.CarGroup = CarGroup
        self.CarGroup25 = CarGroup25
        self.carGroup = carGroup if carGroup is not None else set()
        self.carGroup29 = carGroup29 if carGroup29 is not None else set()
        self.carGroup32 = carGroup32 if carGroup32 is not None else set()
        self.CarGroup36 = CarGroup36
        self.lower = lower
        self.CarGroup39 = CarGroup39
        self.higher = higher
        self.CarGroup44 = CarGroup44
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def lower(self):
        return self.__lower

    @lower.setter
    def lower(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental_CarGroup__lower", None)
        self.__lower = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CarGroup36"):
                opp_val = getattr(old_value, "CarGroup36", None)
                if opp_val == self:
                    setattr(old_value, "CarGroup36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CarGroup36"):
                opp_val = getattr(value, "CarGroup36", None)
                setattr(value, "CarGroup36", self)

    @property
    def carGroup32(self):
        return self.__carGroup32

    @carGroup32.setter
    def carGroup32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental_CarGroup__carGroup32", None)
        self.__carGroup32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Rental33"):
                    opp_val = getattr(item, "Rental33", None)
                    
                    if opp_val == self:
                        setattr(item, "Rental33", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Rental33"):
                    opp_val = getattr(item, "Rental33", None)
                    
                    setattr(item, "Rental33", self)
                    

    @property
    def CarGroup39(self):
        return self.__CarGroup39

    @CarGroup39.setter
    def CarGroup39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental_CarGroup__CarGroup39", None)
        self.__CarGroup39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "higher"):
                opp_val = getattr(old_value, "higher", None)
                if opp_val == self:
                    setattr(old_value, "higher", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "higher"):
                opp_val = getattr(value, "higher", None)
                setattr(value, "higher", self)

    @property
    def CarGroup(self):
        return self.__CarGroup

    @CarGroup.setter
    def CarGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental_CarGroup__CarGroup", None)
        self.__CarGroup = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "branch13"):
                opp_val = getattr(old_value, "branch13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "branch13"):
                opp_val = getattr(value, "branch13", None)
                if opp_val is None:
                    setattr(value, "branch13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def carGroup(self):
        return self.__carGroup

    @carGroup.setter
    def carGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental_CarGroup__carGroup", None)
        self.__carGroup = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Branch27"):
                    opp_val = getattr(item, "Branch27", None)
                    
                    if opp_val == self:
                        setattr(item, "Branch27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Branch27"):
                    opp_val = getattr(item, "Branch27", None)
                    
                    setattr(item, "Branch27", self)
                    

    @property
    def higher(self):
        return self.__higher

    @higher.setter
    def higher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental_CarGroup__higher", None)
        self.__higher = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CarGroup39"):
                opp_val = getattr(old_value, "CarGroup39", None)
                if opp_val == self:
                    setattr(old_value, "CarGroup39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CarGroup39"):
                opp_val = getattr(value, "CarGroup39", None)
                setattr(value, "CarGroup39", self)

    @property
    def CarGroup44(self):
        return self.__CarGroup44

    @CarGroup44.setter
    def CarGroup44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental_CarGroup__CarGroup44", None)
        self.__CarGroup44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "car43"):
                opp_val = getattr(old_value, "car43", None)
                if opp_val == self:
                    setattr(old_value, "car43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "car43"):
                opp_val = getattr(value, "car43", None)
                setattr(value, "car43", self)

    @property
    def CarGroup25(self):
        return self.__CarGroup25

    @CarGroup25.setter
    def CarGroup25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental_CarGroup__CarGroup25", None)
        self.__CarGroup25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rental24"):
                opp_val = getattr(old_value, "rental24", None)
                if opp_val == self:
                    setattr(old_value, "rental24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rental24"):
                opp_val = getattr(value, "rental24", None)
                setattr(value, "rental24", self)

    @property
    def carGroup29(self):
        return self.__carGroup29

    @carGroup29.setter
    def carGroup29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental_CarGroup__carGroup29", None)
        self.__carGroup29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Car30"):
                    opp_val = getattr(item, "Car30", None)
                    
                    if opp_val == self:
                        setattr(item, "Car30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Car30"):
                    opp_val = getattr(item, "Car30", None)
                    
                    setattr(item, "Car30", self)
                    

    @property
    def CarGroup36(self):
        return self.__CarGroup36

    @CarGroup36.setter
    def CarGroup36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental_CarGroup__CarGroup36", None)
        self.__CarGroup36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lower"):
                opp_val = getattr(old_value, "lower", None)
                if opp_val == self:
                    setattr(old_value, "lower", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lower"):
                opp_val = getattr(value, "lower", None)
                setattr(value, "lower", self)

class CarRental_Car:

    def __init__(self, id: str, Car: "CarRental_Branch" = None, Car18: "CarRental_Rental" = None, Car30: "CarRental_CarGroup" = None, car: "CarRental_Branch" = None, car43: "CarRental_CarGroup" = None, car46: "CarRental_Rental" = None):
        self.id = id
        self.Car = Car
        self.Car18 = Car18
        self.Car30 = Car30
        self.car = car
        self.car43 = car43
        self.car46 = car46
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def Car30(self):
        return self.__Car30

    @Car30.setter
    def Car30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental_Car__Car30", None)
        self.__Car30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "carGroup29"):
                opp_val = getattr(old_value, "carGroup29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "carGroup29"):
                opp_val = getattr(value, "carGroup29", None)
                if opp_val is None:
                    setattr(value, "carGroup29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Car18(self):
        return self.__Car18

    @Car18.setter
    def Car18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental_Car__Car18", None)
        self.__Car18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rental"):
                opp_val = getattr(old_value, "rental", None)
                if opp_val == self:
                    setattr(old_value, "rental", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rental"):
                opp_val = getattr(value, "rental", None)
                setattr(value, "rental", self)

    @property
    def car(self):
        return self.__car

    @car.setter
    def car(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental_Car__car", None)
        self.__car = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Branch41"):
                opp_val = getattr(old_value, "Branch41", None)
                if opp_val == self:
                    setattr(old_value, "Branch41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Branch41"):
                opp_val = getattr(value, "Branch41", None)
                setattr(value, "Branch41", self)

    @property
    def Car(self):
        return self.__Car

    @Car.setter
    def Car(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental_Car__Car", None)
        self.__Car = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "branch"):
                opp_val = getattr(old_value, "branch", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "branch"):
                opp_val = getattr(value, "branch", None)
                if opp_val is None:
                    setattr(value, "branch", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def car43(self):
        return self.__car43

    @car43.setter
    def car43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental_Car__car43", None)
        self.__car43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CarGroup44"):
                opp_val = getattr(old_value, "CarGroup44", None)
                if opp_val == self:
                    setattr(old_value, "CarGroup44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CarGroup44"):
                opp_val = getattr(value, "CarGroup44", None)
                setattr(value, "CarGroup44", self)

    @property
    def car46(self):
        return self.__car46

    @car46.setter
    def car46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental_Car__car46", None)
        self.__car46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Rental47"):
                opp_val = getattr(old_value, "Rental47", None)
                if opp_val == self:
                    setattr(old_value, "Rental47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Rental47"):
                opp_val = getattr(value, "Rental47", None)
                setattr(value, "Rental47", self)

class CarRental_Branch:

    def __init__(self, location: str, CarRental_Branch: "CarRental_Employee" = None, CarRental_Branch4: "CarRental_Employee" = None, CarRental_Branch6: "CarRental_Employee" = None, CarRental_Branch9: set["CarRental_Employee"] = None, branch: set["CarRental_Car"] = None, branch13: set["CarRental_CarGroup"] = None, branch15: set["CarRental_Rental"] = None, Branch: "CarRental_Rental" = None, Branch27: "CarRental_CarGroup" = None, Branch41: "CarRental_Car" = None):
        self.location = location
        self.CarRental_Branch = CarRental_Branch
        self.CarRental_Branch4 = CarRental_Branch4
        self.CarRental_Branch6 = CarRental_Branch6
        self.CarRental_Branch9 = CarRental_Branch9 if CarRental_Branch9 is not None else set()
        self.branch = branch if branch is not None else set()
        self.branch13 = branch13 if branch13 is not None else set()
        self.branch15 = branch15 if branch15 is not None else set()
        self.Branch = Branch
        self.Branch27 = Branch27
        self.Branch41 = Branch41
        
    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def CarRental_Branch(self):
        return self.__CarRental_Branch

    @CarRental_Branch.setter
    def CarRental_Branch(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental_Branch__CarRental_Branch", None)
        self.__CarRental_Branch = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CarRental_Employee"):
                opp_val = getattr(old_value, "CarRental_Employee", None)
                if opp_val == self:
                    setattr(old_value, "CarRental_Employee", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CarRental_Employee"):
                opp_val = getattr(value, "CarRental_Employee", None)
                setattr(value, "CarRental_Employee", self)

    @property
    def CarRental_Branch9(self):
        return self.__CarRental_Branch9

    @CarRental_Branch9.setter
    def CarRental_Branch9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental_Branch__CarRental_Branch9", None)
        self.__CarRental_Branch9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CarRental_Employee10"):
                    opp_val = getattr(item, "CarRental_Employee10", None)
                    
                    if opp_val == self:
                        setattr(item, "CarRental_Employee10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CarRental_Employee10"):
                    opp_val = getattr(item, "CarRental_Employee10", None)
                    
                    setattr(item, "CarRental_Employee10", self)
                    

    @property
    def branch(self):
        return self.__branch

    @branch.setter
    def branch(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental_Branch__branch", None)
        self.__branch = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Car"):
                    opp_val = getattr(item, "Car", None)
                    
                    if opp_val == self:
                        setattr(item, "Car", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Car"):
                    opp_val = getattr(item, "Car", None)
                    
                    setattr(item, "Car", self)
                    

    @property
    def branch15(self):
        return self.__branch15

    @branch15.setter
    def branch15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental_Branch__branch15", None)
        self.__branch15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Rental16"):
                    opp_val = getattr(item, "Rental16", None)
                    
                    if opp_val == self:
                        setattr(item, "Rental16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Rental16"):
                    opp_val = getattr(item, "Rental16", None)
                    
                    setattr(item, "Rental16", self)
                    

    @property
    def Branch(self):
        return self.__Branch

    @Branch.setter
    def Branch(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental_Branch__Branch", None)
        self.__Branch = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rental22"):
                opp_val = getattr(old_value, "rental22", None)
                if opp_val == self:
                    setattr(old_value, "rental22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rental22"):
                opp_val = getattr(value, "rental22", None)
                setattr(value, "rental22", self)

    @property
    def CarRental_Branch6(self):
        return self.__CarRental_Branch6

    @CarRental_Branch6.setter
    def CarRental_Branch6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental_Branch__CarRental_Branch6", None)
        self.__CarRental_Branch6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CarRental_Employee7"):
                opp_val = getattr(old_value, "CarRental_Employee7", None)
                if opp_val == self:
                    setattr(old_value, "CarRental_Employee7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CarRental_Employee7"):
                opp_val = getattr(value, "CarRental_Employee7", None)
                setattr(value, "CarRental_Employee7", self)

    @property
    def Branch27(self):
        return self.__Branch27

    @Branch27.setter
    def Branch27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental_Branch__Branch27", None)
        self.__Branch27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "carGroup"):
                opp_val = getattr(old_value, "carGroup", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "carGroup"):
                opp_val = getattr(value, "carGroup", None)
                if opp_val is None:
                    setattr(value, "carGroup", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Branch41(self):
        return self.__Branch41

    @Branch41.setter
    def Branch41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental_Branch__Branch41", None)
        self.__Branch41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "car"):
                opp_val = getattr(old_value, "car", None)
                if opp_val == self:
                    setattr(old_value, "car", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "car"):
                opp_val = getattr(value, "car", None)
                setattr(value, "car", self)

    @property
    def CarRental_Branch4(self):
        return self.__CarRental_Branch4

    @CarRental_Branch4.setter
    def CarRental_Branch4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental_Branch__CarRental_Branch4", None)
        self.__CarRental_Branch4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CarRental_Employee3"):
                opp_val = getattr(old_value, "CarRental_Employee3", None)
                if opp_val == self:
                    setattr(old_value, "CarRental_Employee3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CarRental_Employee3"):
                opp_val = getattr(value, "CarRental_Employee3", None)
                setattr(value, "CarRental_Employee3", self)

    @property
    def branch13(self):
        return self.__branch13

    @branch13.setter
    def branch13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental_Branch__branch13", None)
        self.__branch13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CarGroup"):
                    opp_val = getattr(item, "CarGroup", None)
                    
                    if opp_val == self:
                        setattr(item, "CarGroup", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CarGroup"):
                    opp_val = getattr(item, "CarGroup", None)
                    
                    setattr(item, "CarGroup", self)
                    

class CarRental_Rental:

    def __init__(self, untilDate: str, framDate: str, Rental: "CarRental_Customer" = None, Rental16: "CarRental_Branch" = None, rental: "CarRental_Car" = None, rental20: "CarRental_Customer" = None, rental22: "CarRental_Branch" = None, rental24: "CarRental_CarGroup" = None, Rental33: "CarRental_CarGroup" = None, Rental47: "CarRental_Car" = None):
        self.untilDate = untilDate
        self.framDate = framDate
        self.Rental = Rental
        self.Rental16 = Rental16
        self.rental = rental
        self.rental20 = rental20
        self.rental22 = rental22
        self.rental24 = rental24
        self.Rental33 = Rental33
        self.Rental47 = Rental47
        
    @property
    def framDate(self) -> str:
        return self.__framDate

    @framDate.setter
    def framDate(self, framDate: str):
        self.__framDate = framDate

    @property
    def untilDate(self) -> str:
        return self.__untilDate

    @untilDate.setter
    def untilDate(self, untilDate: str):
        self.__untilDate = untilDate

    @property
    def rental24(self):
        return self.__rental24

    @rental24.setter
    def rental24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental_Rental__rental24", None)
        self.__rental24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CarGroup25"):
                opp_val = getattr(old_value, "CarGroup25", None)
                if opp_val == self:
                    setattr(old_value, "CarGroup25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CarGroup25"):
                opp_val = getattr(value, "CarGroup25", None)
                setattr(value, "CarGroup25", self)

    @property
    def Rental33(self):
        return self.__Rental33

    @Rental33.setter
    def Rental33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental_Rental__Rental33", None)
        self.__Rental33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "carGroup32"):
                opp_val = getattr(old_value, "carGroup32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "carGroup32"):
                opp_val = getattr(value, "carGroup32", None)
                if opp_val is None:
                    setattr(value, "carGroup32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Rental16(self):
        return self.__Rental16

    @Rental16.setter
    def Rental16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental_Rental__Rental16", None)
        self.__Rental16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "branch15"):
                opp_val = getattr(old_value, "branch15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "branch15"):
                opp_val = getattr(value, "branch15", None)
                if opp_val is None:
                    setattr(value, "branch15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Rental47(self):
        return self.__Rental47

    @Rental47.setter
    def Rental47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental_Rental__Rental47", None)
        self.__Rental47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "car46"):
                opp_val = getattr(old_value, "car46", None)
                if opp_val == self:
                    setattr(old_value, "car46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "car46"):
                opp_val = getattr(value, "car46", None)
                setattr(value, "car46", self)

    @property
    def rental20(self):
        return self.__rental20

    @rental20.setter
    def rental20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental_Rental__rental20", None)
        self.__rental20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Customer"):
                opp_val = getattr(old_value, "Customer", None)
                if opp_val == self:
                    setattr(old_value, "Customer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Customer"):
                opp_val = getattr(value, "Customer", None)
                setattr(value, "Customer", self)

    @property
    def rental(self):
        return self.__rental

    @rental.setter
    def rental(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental_Rental__rental", None)
        self.__rental = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Car18"):
                opp_val = getattr(old_value, "Car18", None)
                if opp_val == self:
                    setattr(old_value, "Car18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Car18"):
                opp_val = getattr(value, "Car18", None)
                setattr(value, "Car18", self)

    @property
    def rental22(self):
        return self.__rental22

    @rental22.setter
    def rental22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental_Rental__rental22", None)
        self.__rental22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Branch"):
                opp_val = getattr(old_value, "Branch", None)
                if opp_val == self:
                    setattr(old_value, "Branch", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Branch"):
                opp_val = getattr(value, "Branch", None)
                setattr(value, "Branch", self)

    @property
    def Rental(self):
        return self.__Rental

    @Rental.setter
    def Rental(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental_Rental__Rental", None)
        self.__Rental = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer"):
                opp_val = getattr(old_value, "customer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer"):
                opp_val = getattr(value, "customer", None)
                if opp_val is None:
                    setattr(value, "customer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Person:

    pass
class CarRental_Employee(Person):

    def __init__(self, salary: float, CarRental_Employee: "CarRental_Branch" = None, CarRental_Employee3: "CarRental_Branch" = None, CarRental_Employee7: "CarRental_Branch" = None, CarRental_Employee10: "CarRental_Branch" = None):
        self.salary = salary
        self.CarRental_Employee = CarRental_Employee
        self.CarRental_Employee3 = CarRental_Employee3
        self.CarRental_Employee7 = CarRental_Employee7
        self.CarRental_Employee10 = CarRental_Employee10
        
    @property
    def salary(self) -> float:
        return self.__salary

    @salary.setter
    def salary(self, salary: float):
        self.__salary = salary

    @property
    def CarRental_Employee3(self):
        return self.__CarRental_Employee3

    @CarRental_Employee3.setter
    def CarRental_Employee3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental_Employee__CarRental_Employee3", None)
        self.__CarRental_Employee3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CarRental_Branch4"):
                opp_val = getattr(old_value, "CarRental_Branch4", None)
                if opp_val == self:
                    setattr(old_value, "CarRental_Branch4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CarRental_Branch4"):
                opp_val = getattr(value, "CarRental_Branch4", None)
                setattr(value, "CarRental_Branch4", self)

    @property
    def CarRental_Employee7(self):
        return self.__CarRental_Employee7

    @CarRental_Employee7.setter
    def CarRental_Employee7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental_Employee__CarRental_Employee7", None)
        self.__CarRental_Employee7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CarRental_Branch6"):
                opp_val = getattr(old_value, "CarRental_Branch6", None)
                if opp_val == self:
                    setattr(old_value, "CarRental_Branch6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CarRental_Branch6"):
                opp_val = getattr(value, "CarRental_Branch6", None)
                setattr(value, "CarRental_Branch6", self)

    @property
    def CarRental_Employee(self):
        return self.__CarRental_Employee

    @CarRental_Employee.setter
    def CarRental_Employee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental_Employee__CarRental_Employee", None)
        self.__CarRental_Employee = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CarRental_Branch"):
                opp_val = getattr(old_value, "CarRental_Branch", None)
                if opp_val == self:
                    setattr(old_value, "CarRental_Branch", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CarRental_Branch"):
                opp_val = getattr(value, "CarRental_Branch", None)
                setattr(value, "CarRental_Branch", self)

    @property
    def CarRental_Employee10(self):
        return self.__CarRental_Employee10

    @CarRental_Employee10.setter
    def CarRental_Employee10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental_Employee__CarRental_Employee10", None)
        self.__CarRental_Employee10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CarRental_Branch9"):
                opp_val = getattr(old_value, "CarRental_Branch9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CarRental_Branch9"):
                opp_val = getattr(value, "CarRental_Branch9", None)
                if opp_val is None:
                    setattr(value, "CarRental_Branch9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def raiseSalary(self, amount: float) -> float:
        # TODO: Implement raiseSalary method
        pass

class CarRental_Customer(Person):

    def __init__(self, address: str, customer: set["CarRental_Rental"] = None, Customer: "CarRental_Rental" = None):
        self.address = address
        self.customer = customer if customer is not None else set()
        self.Customer = Customer
        
    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental_Customer__customer", None)
        self.__customer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Rental"):
                    opp_val = getattr(item, "Rental", None)
                    
                    if opp_val == self:
                        setattr(item, "Rental", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Rental"):
                    opp_val = getattr(item, "Rental", None)
                    
                    setattr(item, "Rental", self)
                    

    @property
    def Customer(self):
        return self.__Customer

    @Customer.setter
    def Customer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental_Customer__Customer", None)
        self.__Customer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rental20"):
                opp_val = getattr(old_value, "rental20", None)
                if opp_val == self:
                    setattr(old_value, "rental20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rental20"):
                opp_val = getattr(value, "rental20", None)
                setattr(value, "rental20", self)

class CarRental_Person:

    def __init__(self, firstname: str, lastname: str, age: int, isMarried: bool):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.isMarried = isMarried
        
    @property
    def isMarried(self) -> bool:
        return self.__isMarried

    @isMarried.setter
    def isMarried(self, isMarried: bool):
        self.__isMarried = isMarried

    @property
    def lastname(self) -> str:
        return self.__lastname

    @lastname.setter
    def lastname(self, lastname: str):
        self.__lastname = lastname

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, age: int):
        self.__age = age

    @property
    def firstname(self) -> str:
        return self.__firstname

    @firstname.setter
    def firstname(self, firstname: str):
        self.__firstname = firstname

    def updateAge(self, newAge: int):
        # TODO: Implement updateAge method
        pass

    def email(self) -> str:
        # TODO: Implement email method
        pass
