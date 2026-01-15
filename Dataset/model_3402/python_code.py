from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Person:

    pass
class training_Trainee(Person):

    pass
class training_TrainingOrganization:

    def __init__(self, name: str, training_TrainingOrganization11: set["training_Training"] = None, training_TrainingOrganization: set["training_Person"] = None, training_TrainingOrganization8: set["training_Session"] = None):
        self.name = name
        self.training_TrainingOrganization11 = training_TrainingOrganization11 if training_TrainingOrganization11 is not None else set()
        self.training_TrainingOrganization = training_TrainingOrganization if training_TrainingOrganization is not None else set()
        self.training_TrainingOrganization8 = training_TrainingOrganization8 if training_TrainingOrganization8 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def training_TrainingOrganization(self):
        return self.__training_TrainingOrganization

    @training_TrainingOrganization.setter
    def training_TrainingOrganization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_training_TrainingOrganization__training_TrainingOrganization", None)
        self.__training_TrainingOrganization = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "training_Person6"):
                    opp_val = getattr(item, "training_Person6", None)
                    
                    if opp_val == self:
                        setattr(item, "training_Person6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "training_Person6"):
                    opp_val = getattr(item, "training_Person6", None)
                    
                    setattr(item, "training_Person6", self)
                    

    @property
    def training_TrainingOrganization11(self):
        return self.__training_TrainingOrganization11

    @training_TrainingOrganization11.setter
    def training_TrainingOrganization11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_training_TrainingOrganization__training_TrainingOrganization11", None)
        self.__training_TrainingOrganization11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "training_Training12"):
                    opp_val = getattr(item, "training_Training12", None)
                    
                    if opp_val == self:
                        setattr(item, "training_Training12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "training_Training12"):
                    opp_val = getattr(item, "training_Training12", None)
                    
                    setattr(item, "training_Training12", self)
                    

    @property
    def training_TrainingOrganization8(self):
        return self.__training_TrainingOrganization8

    @training_TrainingOrganization8.setter
    def training_TrainingOrganization8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_training_TrainingOrganization__training_TrainingOrganization8", None)
        self.__training_TrainingOrganization8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "training_Session9"):
                    opp_val = getattr(item, "training_Session9", None)
                    
                    if opp_val == self:
                        setattr(item, "training_Session9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "training_Session9"):
                    opp_val = getattr(item, "training_Session9", None)
                    
                    setattr(item, "training_Session9", self)
                    

class training_Person(ABC):

    def __init__(self, firstname: str, lastname: str, training_Person: "training_Session" = None, training_Person6: "training_TrainingOrganization" = None):
        self.firstname = firstname
        self.lastname = lastname
        self.training_Person = training_Person
        self.training_Person6 = training_Person6
        
    @property
    def firstname(self) -> str:
        return self.__firstname

    @firstname.setter
    def firstname(self, firstname: str):
        self.__firstname = firstname

    @property
    def lastname(self) -> str:
        return self.__lastname

    @lastname.setter
    def lastname(self, lastname: str):
        self.__lastname = lastname

    @property
    def training_Person(self):
        return self.__training_Person

    @training_Person.setter
    def training_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_training_Person__training_Person", None)
        self.__training_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "training_Session4"):
                opp_val = getattr(old_value, "training_Session4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "training_Session4"):
                opp_val = getattr(value, "training_Session4", None)
                if opp_val is None:
                    setattr(value, "training_Session4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def training_Person6(self):
        return self.__training_Person6

    @training_Person6.setter
    def training_Person6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_training_Person__training_Person6", None)
        self.__training_Person6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "training_TrainingOrganization"):
                opp_val = getattr(old_value, "training_TrainingOrganization", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "training_TrainingOrganization"):
                opp_val = getattr(value, "training_TrainingOrganization", None)
                if opp_val is None:
                    setattr(value, "training_TrainingOrganization", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class training_Trainer(Person):

    pass
class training_Training:

    def __init__(self, title: str, training_Training12: "training_TrainingOrganization" = None, canProvide: set["training_Trainer"] = None, training_Training: "training_Session" = None, Training: "training_Trainer" = None):
        self.title = title
        self.training_Training12 = training_Training12
        self.canProvide = canProvide if canProvide is not None else set()
        self.training_Training = training_Training
        self.Training = Training
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def Training(self):
        return self.__Training

    @Training.setter
    def Training(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_training_Training__Training", None)
        self.__Training = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "canBeProvidedBy"):
                opp_val = getattr(old_value, "canBeProvidedBy", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "canBeProvidedBy"):
                opp_val = getattr(value, "canBeProvidedBy", None)
                if opp_val is None:
                    setattr(value, "canBeProvidedBy", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def canProvide(self):
        return self.__canProvide

    @canProvide.setter
    def canProvide(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_training_Training__canProvide", None)
        self.__canProvide = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Trainer"):
                    opp_val = getattr(item, "Trainer", None)
                    
                    if opp_val == self:
                        setattr(item, "Trainer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Trainer"):
                    opp_val = getattr(item, "Trainer", None)
                    
                    setattr(item, "Trainer", self)
                    

    @property
    def training_Training12(self):
        return self.__training_Training12

    @training_Training12.setter
    def training_Training12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_training_Training__training_Training12", None)
        self.__training_Training12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "training_TrainingOrganization11"):
                opp_val = getattr(old_value, "training_TrainingOrganization11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "training_TrainingOrganization11"):
                opp_val = getattr(value, "training_TrainingOrganization11", None)
                if opp_val is None:
                    setattr(value, "training_TrainingOrganization11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def training_Training(self):
        return self.__training_Training

    @training_Training.setter
    def training_Training(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_training_Training__training_Training", None)
        self.__training_Training = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "training_Session"):
                opp_val = getattr(old_value, "training_Session", None)
                if opp_val == self:
                    setattr(old_value, "training_Session", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "training_Session"):
                opp_val = getattr(value, "training_Session", None)
                setattr(value, "training_Session", self)

class training_Session:

    def __init__(self, date: date, training_Session: "training_Training" = None, training_Session2: "training_Trainer" = None, training_Session4: set["training_Person"] = None, training_Session9: "training_TrainingOrganization" = None):
        self.date = date
        self.training_Session = training_Session
        self.training_Session2 = training_Session2
        self.training_Session4 = training_Session4 if training_Session4 is not None else set()
        self.training_Session9 = training_Session9
        
    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def training_Session9(self):
        return self.__training_Session9

    @training_Session9.setter
    def training_Session9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_training_Session__training_Session9", None)
        self.__training_Session9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "training_TrainingOrganization8"):
                opp_val = getattr(old_value, "training_TrainingOrganization8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "training_TrainingOrganization8"):
                opp_val = getattr(value, "training_TrainingOrganization8", None)
                if opp_val is None:
                    setattr(value, "training_TrainingOrganization8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def training_Session2(self):
        return self.__training_Session2

    @training_Session2.setter
    def training_Session2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_training_Session__training_Session2", None)
        self.__training_Session2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "training_Trainer"):
                opp_val = getattr(old_value, "training_Trainer", None)
                if opp_val == self:
                    setattr(old_value, "training_Trainer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "training_Trainer"):
                opp_val = getattr(value, "training_Trainer", None)
                setattr(value, "training_Trainer", self)

    @property
    def training_Session(self):
        return self.__training_Session

    @training_Session.setter
    def training_Session(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_training_Session__training_Session", None)
        self.__training_Session = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "training_Training"):
                opp_val = getattr(old_value, "training_Training", None)
                if opp_val == self:
                    setattr(old_value, "training_Training", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "training_Training"):
                opp_val = getattr(value, "training_Training", None)
                setattr(value, "training_Training", self)

    @property
    def training_Session4(self):
        return self.__training_Session4

    @training_Session4.setter
    def training_Session4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_training_Session__training_Session4", None)
        self.__training_Session4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "training_Person"):
                    opp_val = getattr(item, "training_Person", None)
                    
                    if opp_val == self:
                        setattr(item, "training_Person", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "training_Person"):
                    opp_val = getattr(item, "training_Person", None)
                    
                    setattr(item, "training_Person", self)
                    
