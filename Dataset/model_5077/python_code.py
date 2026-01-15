from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class CarRental2_Check:

    def __init__(self, description: str, CarRental2_Check: set["CarRental2_ServiceDepot"] = None):
        self.description = description
        self.CarRental2_Check = CarRental2_Check if CarRental2_Check is not None else set()
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def CarRental2_Check(self):
        return self.__CarRental2_Check

    @CarRental2_Check.setter
    def CarRental2_Check(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental2_Check__CarRental2_Check", None)
        self.__CarRental2_Check = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CarRental2_ServiceDepot"):
                    opp_val = getattr(item, "CarRental2_ServiceDepot", None)
                    
                    if opp_val == self:
                        setattr(item, "CarRental2_ServiceDepot", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CarRental2_ServiceDepot"):
                    opp_val = getattr(item, "CarRental2_ServiceDepot", None)
                    
                    setattr(item, "CarRental2_ServiceDepot", self)
                    

class CarRental2_ServiceDepot:

    def __init__(self, location: str, ServiceDepot: "CarRental2_Car" = None, Maintenance_ServiceDepot: set["CarRental2_Car"] = None, CarRental2_ServiceDepot: "CarRental2_Check" = None):
        self.location = location
        self.ServiceDepot = ServiceDepot
        self.Maintenance_ServiceDepot = Maintenance_ServiceDepot if Maintenance_ServiceDepot is not None else set()
        self.CarRental2_ServiceDepot = CarRental2_ServiceDepot
        
    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def Maintenance_ServiceDepot(self):
        return self.__Maintenance_ServiceDepot

    @Maintenance_ServiceDepot.setter
    def Maintenance_ServiceDepot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental2_ServiceDepot__Maintenance_ServiceDepot", None)
        self.__Maintenance_ServiceDepot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Car38"):
                    opp_val = getattr(item, "Car38", None)
                    
                    if opp_val == self:
                        setattr(item, "Car38", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Car38"):
                    opp_val = getattr(item, "Car38", None)
                    
                    setattr(item, "Car38", self)
                    

    @property
    def ServiceDepot(self):
        return self.__ServiceDepot

    @ServiceDepot.setter
    def ServiceDepot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental2_ServiceDepot__ServiceDepot", None)
        self.__ServiceDepot = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Maintenance_Car"):
                opp_val = getattr(old_value, "Maintenance_Car", None)
                if opp_val == self:
                    setattr(old_value, "Maintenance_Car", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Maintenance_Car"):
                opp_val = getattr(value, "Maintenance_Car", None)
                setattr(value, "Maintenance_Car", self)

    @property
    def CarRental2_ServiceDepot(self):
        return self.__CarRental2_ServiceDepot

    @CarRental2_ServiceDepot.setter
    def CarRental2_ServiceDepot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental2_ServiceDepot__CarRental2_ServiceDepot", None)
        self.__CarRental2_ServiceDepot = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CarRental2_Check"):
                opp_val = getattr(old_value, "CarRental2_Check", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CarRental2_Check"):
                opp_val = getattr(value, "CarRental2_Check", None)
                if opp_val is None:
                    setattr(value, "CarRental2_Check", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class CarRental2_CarGroup:

    def __init__(self, kind: str, CarGroup: "CarRental2_Branch" = None, CarGroup15: "CarRental2_Rental" = None, Offers_CarGroup: set["CarRental2_Branch"] = None, Classification_CarGroup: set["CarRental2_Car"] = None, Reservation_CarGroup: set["CarRental2_Rental"] = None, CarGroup26: "CarRental2_CarGroup" = None, Quality_CarGroup_role_higher: "CarRental2_CarGroup" = None, CarGroup29: "CarRental2_CarGroup" = None, Quality_CarGroup_role_lower: "CarRental2_CarGroup" = None, CarGroup33: "CarRental2_Car" = None):
        self.kind = kind
        self.CarGroup = CarGroup
        self.CarGroup15 = CarGroup15
        self.Offers_CarGroup = Offers_CarGroup if Offers_CarGroup is not None else set()
        self.Classification_CarGroup = Classification_CarGroup if Classification_CarGroup is not None else set()
        self.Reservation_CarGroup = Reservation_CarGroup if Reservation_CarGroup is not None else set()
        self.CarGroup26 = CarGroup26
        self.Quality_CarGroup_role_higher = Quality_CarGroup_role_higher
        self.CarGroup29 = CarGroup29
        self.Quality_CarGroup_role_lower = Quality_CarGroup_role_lower
        self.CarGroup33 = CarGroup33
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def Offers_CarGroup(self):
        return self.__Offers_CarGroup

    @Offers_CarGroup.setter
    def Offers_CarGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental2_CarGroup__Offers_CarGroup", None)
        self.__Offers_CarGroup = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Branch19"):
                    opp_val = getattr(item, "Branch19", None)
                    
                    if opp_val == self:
                        setattr(item, "Branch19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Branch19"):
                    opp_val = getattr(item, "Branch19", None)
                    
                    setattr(item, "Branch19", self)
                    

    @property
    def Quality_CarGroup_role_lower(self):
        return self.__Quality_CarGroup_role_lower

    @Quality_CarGroup_role_lower.setter
    def Quality_CarGroup_role_lower(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental2_CarGroup__Quality_CarGroup_role_lower", None)
        self.__Quality_CarGroup_role_lower = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CarGroup29"):
                opp_val = getattr(old_value, "CarGroup29", None)
                if opp_val == self:
                    setattr(old_value, "CarGroup29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CarGroup29"):
                opp_val = getattr(value, "CarGroup29", None)
                setattr(value, "CarGroup29", self)

    @property
    def Classification_CarGroup(self):
        return self.__Classification_CarGroup

    @Classification_CarGroup.setter
    def Classification_CarGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental2_CarGroup__Classification_CarGroup", None)
        self.__Classification_CarGroup = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Car21"):
                    opp_val = getattr(item, "Car21", None)
                    
                    if opp_val == self:
                        setattr(item, "Car21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Car21"):
                    opp_val = getattr(item, "Car21", None)
                    
                    setattr(item, "Car21", self)
                    

    @property
    def Quality_CarGroup_role_higher(self):
        return self.__Quality_CarGroup_role_higher

    @Quality_CarGroup_role_higher.setter
    def Quality_CarGroup_role_higher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental2_CarGroup__Quality_CarGroup_role_higher", None)
        self.__Quality_CarGroup_role_higher = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CarGroup26"):
                opp_val = getattr(old_value, "CarGroup26", None)
                if opp_val == self:
                    setattr(old_value, "CarGroup26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CarGroup26"):
                opp_val = getattr(value, "CarGroup26", None)
                setattr(value, "CarGroup26", self)

    @property
    def CarGroup15(self):
        return self.__CarGroup15

    @CarGroup15.setter
    def CarGroup15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental2_CarGroup__CarGroup15", None)
        self.__CarGroup15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Reservation_Rental"):
                opp_val = getattr(old_value, "Reservation_Rental", None)
                if opp_val == self:
                    setattr(old_value, "Reservation_Rental", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Reservation_Rental"):
                opp_val = getattr(value, "Reservation_Rental", None)
                setattr(value, "Reservation_Rental", self)

    @property
    def CarGroup(self):
        return self.__CarGroup

    @CarGroup.setter
    def CarGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental2_CarGroup__CarGroup", None)
        self.__CarGroup = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Offers_Branch"):
                opp_val = getattr(old_value, "Offers_Branch", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Offers_Branch"):
                opp_val = getattr(value, "Offers_Branch", None)
                if opp_val is None:
                    setattr(value, "Offers_Branch", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CarGroup29(self):
        return self.__CarGroup29

    @CarGroup29.setter
    def CarGroup29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental2_CarGroup__CarGroup29", None)
        self.__CarGroup29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Quality_CarGroup_role_lower"):
                opp_val = getattr(old_value, "Quality_CarGroup_role_lower", None)
                if opp_val == self:
                    setattr(old_value, "Quality_CarGroup_role_lower", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Quality_CarGroup_role_lower"):
                opp_val = getattr(value, "Quality_CarGroup_role_lower", None)
                setattr(value, "Quality_CarGroup_role_lower", self)

    @property
    def CarGroup33(self):
        return self.__CarGroup33

    @CarGroup33.setter
    def CarGroup33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental2_CarGroup__CarGroup33", None)
        self.__CarGroup33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Classification_Car"):
                opp_val = getattr(old_value, "Classification_Car", None)
                if opp_val == self:
                    setattr(old_value, "Classification_Car", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Classification_Car"):
                opp_val = getattr(value, "Classification_Car", None)
                setattr(value, "Classification_Car", self)

    @property
    def Reservation_CarGroup(self):
        return self.__Reservation_CarGroup

    @Reservation_CarGroup.setter
    def Reservation_CarGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental2_CarGroup__Reservation_CarGroup", None)
        self.__Reservation_CarGroup = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Rental23"):
                    opp_val = getattr(item, "Rental23", None)
                    
                    if opp_val == self:
                        setattr(item, "Rental23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Rental23"):
                    opp_val = getattr(item, "Rental23", None)
                    
                    setattr(item, "Rental23", self)
                    

    @property
    def CarGroup26(self):
        return self.__CarGroup26

    @CarGroup26.setter
    def CarGroup26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental2_CarGroup__CarGroup26", None)
        self.__CarGroup26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Quality_CarGroup_role_higher"):
                opp_val = getattr(old_value, "Quality_CarGroup_role_higher", None)
                if opp_val == self:
                    setattr(old_value, "Quality_CarGroup_role_higher", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Quality_CarGroup_role_higher"):
                opp_val = getattr(value, "Quality_CarGroup_role_higher", None)
                setattr(value, "Quality_CarGroup_role_higher", self)

class CarRental2_Car:

    def __init__(self, id: str, Car: "CarRental2_Branch" = None, Car17: "CarRental2_Rental" = None, Car21: "CarRental2_CarGroup" = None, Fleet_Car: "CarRental2_Branch" = None, Classification_Car: "CarRental2_CarGroup" = None, Assignment_Car: "CarRental2_Rental" = None, Maintenance_Car: "CarRental2_ServiceDepot" = None, Car38: "CarRental2_ServiceDepot" = None):
        self.id = id
        self.Car = Car
        self.Car17 = Car17
        self.Car21 = Car21
        self.Fleet_Car = Fleet_Car
        self.Classification_Car = Classification_Car
        self.Assignment_Car = Assignment_Car
        self.Maintenance_Car = Maintenance_Car
        self.Car38 = Car38
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def Car38(self):
        return self.__Car38

    @Car38.setter
    def Car38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental2_Car__Car38", None)
        self.__Car38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Maintenance_ServiceDepot"):
                opp_val = getattr(old_value, "Maintenance_ServiceDepot", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Maintenance_ServiceDepot"):
                opp_val = getattr(value, "Maintenance_ServiceDepot", None)
                if opp_val is None:
                    setattr(value, "Maintenance_ServiceDepot", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Car21(self):
        return self.__Car21

    @Car21.setter
    def Car21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental2_Car__Car21", None)
        self.__Car21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Classification_CarGroup"):
                opp_val = getattr(old_value, "Classification_CarGroup", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Classification_CarGroup"):
                opp_val = getattr(value, "Classification_CarGroup", None)
                if opp_val is None:
                    setattr(value, "Classification_CarGroup", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Classification_Car(self):
        return self.__Classification_Car

    @Classification_Car.setter
    def Classification_Car(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental2_Car__Classification_Car", None)
        self.__Classification_Car = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CarGroup33"):
                opp_val = getattr(old_value, "CarGroup33", None)
                if opp_val == self:
                    setattr(old_value, "CarGroup33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CarGroup33"):
                opp_val = getattr(value, "CarGroup33", None)
                setattr(value, "CarGroup33", self)

    @property
    def Car17(self):
        return self.__Car17

    @Car17.setter
    def Car17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental2_Car__Car17", None)
        self.__Car17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Assignment_Rental"):
                opp_val = getattr(old_value, "Assignment_Rental", None)
                if opp_val == self:
                    setattr(old_value, "Assignment_Rental", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Assignment_Rental"):
                opp_val = getattr(value, "Assignment_Rental", None)
                setattr(value, "Assignment_Rental", self)

    @property
    def Car(self):
        return self.__Car

    @Car.setter
    def Car(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental2_Car__Car", None)
        self.__Car = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Fleet_Branch"):
                opp_val = getattr(old_value, "Fleet_Branch", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Fleet_Branch"):
                opp_val = getattr(value, "Fleet_Branch", None)
                if opp_val is None:
                    setattr(value, "Fleet_Branch", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Maintenance_Car(self):
        return self.__Maintenance_Car

    @Maintenance_Car.setter
    def Maintenance_Car(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental2_Car__Maintenance_Car", None)
        self.__Maintenance_Car = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ServiceDepot"):
                opp_val = getattr(old_value, "ServiceDepot", None)
                if opp_val == self:
                    setattr(old_value, "ServiceDepot", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ServiceDepot"):
                opp_val = getattr(value, "ServiceDepot", None)
                setattr(value, "ServiceDepot", self)

    @property
    def Assignment_Car(self):
        return self.__Assignment_Car

    @Assignment_Car.setter
    def Assignment_Car(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental2_Car__Assignment_Car", None)
        self.__Assignment_Car = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Rental35"):
                opp_val = getattr(old_value, "Rental35", None)
                if opp_val == self:
                    setattr(old_value, "Rental35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Rental35"):
                opp_val = getattr(value, "Rental35", None)
                setattr(value, "Rental35", self)

    @property
    def Fleet_Car(self):
        return self.__Fleet_Car

    @Fleet_Car.setter
    def Fleet_Car(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental2_Car__Fleet_Car", None)
        self.__Fleet_Car = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Branch31"):
                opp_val = getattr(old_value, "Branch31", None)
                if opp_val == self:
                    setattr(old_value, "Branch31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Branch31"):
                opp_val = getattr(value, "Branch31", None)
                setattr(value, "Branch31", self)

    def description(self) -> str:
        # TODO: Implement description method
        pass

class CarRental2_Branch:

    def __init__(self, location: str, Branch: "CarRental2_Employee" = None, Branch3: "CarRental2_Employee" = None, Management_Branch_role_managedBranch: "CarRental2_Employee" = None, Fleet_Branch: set["CarRental2_Car"] = None, Offers_Branch: set["CarRental2_CarGroup"] = None, Provider_Branch: set["CarRental2_Rental"] = None, Branch13: "CarRental2_Rental" = None, Branch19: "CarRental2_CarGroup" = None, Branch31: "CarRental2_Car" = None, Employment_Branch_role_employer: set["CarRental2_Employee"] = None):
        self.location = location
        self.Branch = Branch
        self.Branch3 = Branch3
        self.Management_Branch_role_managedBranch = Management_Branch_role_managedBranch
        self.Fleet_Branch = Fleet_Branch if Fleet_Branch is not None else set()
        self.Offers_Branch = Offers_Branch if Offers_Branch is not None else set()
        self.Provider_Branch = Provider_Branch if Provider_Branch is not None else set()
        self.Branch13 = Branch13
        self.Branch19 = Branch19
        self.Branch31 = Branch31
        self.Employment_Branch_role_employer = Employment_Branch_role_employer if Employment_Branch_role_employer is not None else set()
        
    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def Branch19(self):
        return self.__Branch19

    @Branch19.setter
    def Branch19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental2_Branch__Branch19", None)
        self.__Branch19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Offers_CarGroup"):
                opp_val = getattr(old_value, "Offers_CarGroup", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Offers_CarGroup"):
                opp_val = getattr(value, "Offers_CarGroup", None)
                if opp_val is None:
                    setattr(value, "Offers_CarGroup", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Branch(self):
        return self.__Branch

    @Branch.setter
    def Branch(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental2_Branch__Branch", None)
        self.__Branch = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Management_Employee_role_manager"):
                opp_val = getattr(old_value, "Management_Employee_role_manager", None)
                if opp_val == self:
                    setattr(old_value, "Management_Employee_role_manager", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Management_Employee_role_manager"):
                opp_val = getattr(value, "Management_Employee_role_manager", None)
                setattr(value, "Management_Employee_role_manager", self)

    @property
    def Provider_Branch(self):
        return self.__Provider_Branch

    @Provider_Branch.setter
    def Provider_Branch(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental2_Branch__Provider_Branch", None)
        self.__Provider_Branch = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Rental10"):
                    opp_val = getattr(item, "Rental10", None)
                    
                    if opp_val == self:
                        setattr(item, "Rental10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Rental10"):
                    opp_val = getattr(item, "Rental10", None)
                    
                    setattr(item, "Rental10", self)
                    

    @property
    def Branch31(self):
        return self.__Branch31

    @Branch31.setter
    def Branch31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental2_Branch__Branch31", None)
        self.__Branch31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Fleet_Car"):
                opp_val = getattr(old_value, "Fleet_Car", None)
                if opp_val == self:
                    setattr(old_value, "Fleet_Car", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Fleet_Car"):
                opp_val = getattr(value, "Fleet_Car", None)
                setattr(value, "Fleet_Car", self)

    @property
    def Branch13(self):
        return self.__Branch13

    @Branch13.setter
    def Branch13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental2_Branch__Branch13", None)
        self.__Branch13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Provider_Rental"):
                opp_val = getattr(old_value, "Provider_Rental", None)
                if opp_val == self:
                    setattr(old_value, "Provider_Rental", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Provider_Rental"):
                opp_val = getattr(value, "Provider_Rental", None)
                setattr(value, "Provider_Rental", self)

    @property
    def Branch3(self):
        return self.__Branch3

    @Branch3.setter
    def Branch3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental2_Branch__Branch3", None)
        self.__Branch3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Employment_Employee_role_employee"):
                opp_val = getattr(old_value, "Employment_Employee_role_employee", None)
                if opp_val == self:
                    setattr(old_value, "Employment_Employee_role_employee", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Employment_Employee_role_employee"):
                opp_val = getattr(value, "Employment_Employee_role_employee", None)
                setattr(value, "Employment_Employee_role_employee", self)

    @property
    def Management_Branch_role_managedBranch(self):
        return self.__Management_Branch_role_managedBranch

    @Management_Branch_role_managedBranch.setter
    def Management_Branch_role_managedBranch(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental2_Branch__Management_Branch_role_managedBranch", None)
        self.__Management_Branch_role_managedBranch = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Employee"):
                opp_val = getattr(old_value, "Employee", None)
                if opp_val == self:
                    setattr(old_value, "Employee", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Employee"):
                opp_val = getattr(value, "Employee", None)
                setattr(value, "Employee", self)

    @property
    def Fleet_Branch(self):
        return self.__Fleet_Branch

    @Fleet_Branch.setter
    def Fleet_Branch(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental2_Branch__Fleet_Branch", None)
        self.__Fleet_Branch = value if value is not None else set()
        
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
    def Offers_Branch(self):
        return self.__Offers_Branch

    @Offers_Branch.setter
    def Offers_Branch(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental2_Branch__Offers_Branch", None)
        self.__Offers_Branch = value if value is not None else set()
        
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
                    

    @property
    def Employment_Branch_role_employer(self):
        return self.__Employment_Branch_role_employer

    @Employment_Branch_role_employer.setter
    def Employment_Branch_role_employer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental2_Branch__Employment_Branch_role_employer", None)
        self.__Employment_Branch_role_employer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Employee6"):
                    opp_val = getattr(item, "Employee6", None)
                    
                    if opp_val == self:
                        setattr(item, "Employee6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Employee6"):
                    opp_val = getattr(item, "Employee6", None)
                    
                    setattr(item, "Employee6", self)
                    

    def rentalsForDate(self):
        # TODO: Implement rentalsForDate method
        pass

class CarRental2_Rental:

    def __init__(self, fromDate: str, untilDate: str, Rental: "CarRental2_Customer" = None, Rental10: "CarRental2_Branch" = None, Booking_Rental: "CarRental2_Customer" = None, Provider_Rental: "CarRental2_Branch" = None, Reservation_Rental: "CarRental2_CarGroup" = None, Assignment_Rental: "CarRental2_Car" = None, Rental23: "CarRental2_CarGroup" = None, Rental35: "CarRental2_Car" = None):
        self.fromDate = fromDate
        self.untilDate = untilDate
        self.Rental = Rental
        self.Rental10 = Rental10
        self.Booking_Rental = Booking_Rental
        self.Provider_Rental = Provider_Rental
        self.Reservation_Rental = Reservation_Rental
        self.Assignment_Rental = Assignment_Rental
        self.Rental23 = Rental23
        self.Rental35 = Rental35
        
    @property
    def fromDate(self) -> str:
        return self.__fromDate

    @fromDate.setter
    def fromDate(self, fromDate: str):
        self.__fromDate = fromDate

    @property
    def untilDate(self) -> str:
        return self.__untilDate

    @untilDate.setter
    def untilDate(self, untilDate: str):
        self.__untilDate = untilDate

    @property
    def Reservation_Rental(self):
        return self.__Reservation_Rental

    @Reservation_Rental.setter
    def Reservation_Rental(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental2_Rental__Reservation_Rental", None)
        self.__Reservation_Rental = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CarGroup15"):
                opp_val = getattr(old_value, "CarGroup15", None)
                if opp_val == self:
                    setattr(old_value, "CarGroup15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CarGroup15"):
                opp_val = getattr(value, "CarGroup15", None)
                setattr(value, "CarGroup15", self)

    @property
    def Rental(self):
        return self.__Rental

    @Rental.setter
    def Rental(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental2_Rental__Rental", None)
        self.__Rental = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Booking_Customer"):
                opp_val = getattr(old_value, "Booking_Customer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Booking_Customer"):
                opp_val = getattr(value, "Booking_Customer", None)
                if opp_val is None:
                    setattr(value, "Booking_Customer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Rental35(self):
        return self.__Rental35

    @Rental35.setter
    def Rental35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental2_Rental__Rental35", None)
        self.__Rental35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Assignment_Car"):
                opp_val = getattr(old_value, "Assignment_Car", None)
                if opp_val == self:
                    setattr(old_value, "Assignment_Car", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Assignment_Car"):
                opp_val = getattr(value, "Assignment_Car", None)
                setattr(value, "Assignment_Car", self)

    @property
    def Rental10(self):
        return self.__Rental10

    @Rental10.setter
    def Rental10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental2_Rental__Rental10", None)
        self.__Rental10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Provider_Branch"):
                opp_val = getattr(old_value, "Provider_Branch", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Provider_Branch"):
                opp_val = getattr(value, "Provider_Branch", None)
                if opp_val is None:
                    setattr(value, "Provider_Branch", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Booking_Rental(self):
        return self.__Booking_Rental

    @Booking_Rental.setter
    def Booking_Rental(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental2_Rental__Booking_Rental", None)
        self.__Booking_Rental = value
        
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
    def Assignment_Rental(self):
        return self.__Assignment_Rental

    @Assignment_Rental.setter
    def Assignment_Rental(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental2_Rental__Assignment_Rental", None)
        self.__Assignment_Rental = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Car17"):
                opp_val = getattr(old_value, "Car17", None)
                if opp_val == self:
                    setattr(old_value, "Car17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Car17"):
                opp_val = getattr(value, "Car17", None)
                setattr(value, "Car17", self)

    @property
    def Provider_Rental(self):
        return self.__Provider_Rental

    @Provider_Rental.setter
    def Provider_Rental(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental2_Rental__Provider_Rental", None)
        self.__Provider_Rental = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Branch13"):
                opp_val = getattr(old_value, "Branch13", None)
                if opp_val == self:
                    setattr(old_value, "Branch13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Branch13"):
                opp_val = getattr(value, "Branch13", None)
                setattr(value, "Branch13", self)

    @property
    def Rental23(self):
        return self.__Rental23

    @Rental23.setter
    def Rental23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental2_Rental__Rental23", None)
        self.__Rental23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Reservation_CarGroup"):
                opp_val = getattr(old_value, "Reservation_CarGroup", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Reservation_CarGroup"):
                opp_val = getattr(value, "Reservation_CarGroup", None)
                if opp_val is None:
                    setattr(value, "Reservation_CarGroup", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Person:

    pass
class CarRental2_Employee(Person):

    def __init__(self, salary: int, Management_Employee_role_manager: "CarRental2_Branch" = None, Employment_Employee_role_employee: "CarRental2_Branch" = None, Employee: "CarRental2_Branch" = None, Employee6: "CarRental2_Branch" = None):
        self.salary = salary
        self.Management_Employee_role_manager = Management_Employee_role_manager
        self.Employment_Employee_role_employee = Employment_Employee_role_employee
        self.Employee = Employee
        self.Employee6 = Employee6
        
    @property
    def salary(self) -> int:
        return self.__salary

    @salary.setter
    def salary(self, salary: int):
        self.__salary = salary

    @property
    def Employee(self):
        return self.__Employee

    @Employee.setter
    def Employee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental2_Employee__Employee", None)
        self.__Employee = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Management_Branch_role_managedBranch"):
                opp_val = getattr(old_value, "Management_Branch_role_managedBranch", None)
                if opp_val == self:
                    setattr(old_value, "Management_Branch_role_managedBranch", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Management_Branch_role_managedBranch"):
                opp_val = getattr(value, "Management_Branch_role_managedBranch", None)
                setattr(value, "Management_Branch_role_managedBranch", self)

    @property
    def Management_Employee_role_manager(self):
        return self.__Management_Employee_role_manager

    @Management_Employee_role_manager.setter
    def Management_Employee_role_manager(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental2_Employee__Management_Employee_role_manager", None)
        self.__Management_Employee_role_manager = value
        
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
    def Employment_Employee_role_employee(self):
        return self.__Employment_Employee_role_employee

    @Employment_Employee_role_employee.setter
    def Employment_Employee_role_employee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental2_Employee__Employment_Employee_role_employee", None)
        self.__Employment_Employee_role_employee = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Branch3"):
                opp_val = getattr(old_value, "Branch3", None)
                if opp_val == self:
                    setattr(old_value, "Branch3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Branch3"):
                opp_val = getattr(value, "Branch3", None)
                setattr(value, "Branch3", self)

    @property
    def Employee6(self):
        return self.__Employee6

    @Employee6.setter
    def Employee6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental2_Employee__Employee6", None)
        self.__Employee6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Employment_Branch_role_employer"):
                opp_val = getattr(old_value, "Employment_Branch_role_employer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Employment_Branch_role_employer"):
                opp_val = getattr(value, "Employment_Branch_role_employer", None)
                if opp_val is None:
                    setattr(value, "Employment_Branch_role_employer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def raiseSalary(self) -> int:
        # TODO: Implement raiseSalary method
        pass

class CarRental2_Customer(Person):

    def __init__(self, address: str, Booking_Customer: set["CarRental2_Rental"] = None, Customer: "CarRental2_Rental" = None):
        self.address = address
        self.Booking_Customer = Booking_Customer if Booking_Customer is not None else set()
        self.Customer = Customer
        
    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def Booking_Customer(self):
        return self.__Booking_Customer

    @Booking_Customer.setter
    def Booking_Customer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarRental2_Customer__Booking_Customer", None)
        self.__Booking_Customer = value if value is not None else set()
        
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
        old_value = getattr(self, f"_CarRental2_Customer__Customer", None)
        self.__Customer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Booking_Rental"):
                opp_val = getattr(old_value, "Booking_Rental", None)
                if opp_val == self:
                    setattr(old_value, "Booking_Rental", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Booking_Rental"):
                opp_val = getattr(value, "Booking_Rental", None)
                setattr(value, "Booking_Rental", self)

class CarRental2_Person(ABC):

    def __init__(self, firstname: str, lastname: str, age: int, isMarried: bool):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.isMarried = isMarried
        
    @property
    def lastname(self) -> str:
        return self.__lastname

    @lastname.setter
    def lastname(self, lastname: str):
        self.__lastname = lastname

    @property
    def firstname(self) -> str:
        return self.__firstname

    @firstname.setter
    def firstname(self, firstname: str):
        self.__firstname = firstname

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, age: int):
        self.__age = age

    @property
    def isMarried(self) -> bool:
        return self.__isMarried

    @isMarried.setter
    def isMarried(self, isMarried: bool):
        self.__isMarried = isMarried

    def fullname(self) -> str:
        # TODO: Implement fullname method
        pass
