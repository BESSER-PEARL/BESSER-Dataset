from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Person:

    pass
class training_Trainee(Person):

    pass
class training_Person(ABC):

    def __init__(self, firstname: str, lastname: str, training_Person: "training_Session" = None, training_Person5: "training_TrainingOrganization" = None):
        self.firstname = firstname
        self.lastname = lastname
        self.training_Person = training_Person
        self.training_Person5 = training_Person5
        
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
    def training_Person5(self):
        return self.__training_Person5

    @training_Person5.setter
    def training_Person5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_training_Person__training_Person5", None)
        self.__training_Person5 = value
        
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
            if hasattr(old_value, "training_Session3"):
                opp_val = getattr(old_value, "training_Session3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "training_Session3"):
                opp_val = getattr(value, "training_Session3", None)
                if opp_val is None:
                    setattr(value, "training_Session3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class training_Trainer(Person):

    pass
class training_Training:

    def __init__(self, title: str, Training: "training_Session" = None, training: "training_Session" = None, Training14: "training_Trainer" = None, training_Training: "training_TrainingOrganization" = None, canProvide: set["training_Trainer"] = None):
        self.title = title
        self.Training = Training
        self.training = training
        self.Training14 = Training14
        self.training_Training = training_Training
        self.canProvide = canProvide if canProvide is not None else set()
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def Training14(self):
        return self.__Training14

    @Training14.setter
    def Training14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_training_Training__Training14", None)
        self.__Training14 = value
        
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
    def training_Training(self):
        return self.__training_Training

    @training_Training.setter
    def training_Training(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_training_Training__training_Training", None)
        self.__training_Training = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "training_TrainingOrganization10"):
                opp_val = getattr(old_value, "training_TrainingOrganization10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "training_TrainingOrganization10"):
                opp_val = getattr(value, "training_TrainingOrganization10", None)
                if opp_val is None:
                    setattr(value, "training_TrainingOrganization10", set([self]))
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
    def training(self):
        return self.__training

    @training.setter
    def training(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_training_Training__training", None)
        self.__training = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Session"):
                opp_val = getattr(old_value, "Session", None)
                if opp_val == self:
                    setattr(old_value, "Session", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Session"):
                opp_val = getattr(value, "Session", None)
                setattr(value, "Session", self)

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
            if hasattr(old_value, "session"):
                opp_val = getattr(old_value, "session", None)
                if opp_val == self:
                    setattr(old_value, "session", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "session"):
                opp_val = getattr(value, "session", None)
                setattr(value, "session", self)

class training_TrainingOrganization:

    def __init__(self, name: str, training_TrainingOrganization: set["training_Person"] = None, training_TrainingOrganization7: set["training_Session"] = None, training_TrainingOrganization10: set["training_Training"] = None):
        self.name = name
        self.training_TrainingOrganization = training_TrainingOrganization if training_TrainingOrganization is not None else set()
        self.training_TrainingOrganization7 = training_TrainingOrganization7 if training_TrainingOrganization7 is not None else set()
        self.training_TrainingOrganization10 = training_TrainingOrganization10 if training_TrainingOrganization10 is not None else set()
        
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
                if hasattr(item, "training_Person5"):
                    opp_val = getattr(item, "training_Person5", None)
                    
                    if opp_val == self:
                        setattr(item, "training_Person5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "training_Person5"):
                    opp_val = getattr(item, "training_Person5", None)
                    
                    setattr(item, "training_Person5", self)
                    

    @property
    def training_TrainingOrganization7(self):
        return self.__training_TrainingOrganization7

    @training_TrainingOrganization7.setter
    def training_TrainingOrganization7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_training_TrainingOrganization__training_TrainingOrganization7", None)
        self.__training_TrainingOrganization7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "training_Session8"):
                    opp_val = getattr(item, "training_Session8", None)
                    
                    if opp_val == self:
                        setattr(item, "training_Session8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "training_Session8"):
                    opp_val = getattr(item, "training_Session8", None)
                    
                    setattr(item, "training_Session8", self)
                    

    @property
    def training_TrainingOrganization10(self):
        return self.__training_TrainingOrganization10

    @training_TrainingOrganization10.setter
    def training_TrainingOrganization10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_training_TrainingOrganization__training_TrainingOrganization10", None)
        self.__training_TrainingOrganization10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "training_Training"):
                    opp_val = getattr(item, "training_Training", None)
                    
                    if opp_val == self:
                        setattr(item, "training_Training", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "training_Training"):
                    opp_val = getattr(item, "training_Training", None)
                    
                    setattr(item, "training_Training", self)
                    

class training_Session:

    def __init__(self, name: str, date: date, session: "training_Training" = None, training_Session: "training_Trainer" = None, training_Session3: set["training_Person"] = None, Session: "training_Training" = None, training_Session8: "training_TrainingOrganization" = None):
        self.name = name
        self.date = date
        self.session = session
        self.training_Session = training_Session
        self.training_Session3 = training_Session3 if training_Session3 is not None else set()
        self.Session = Session
        self.training_Session8 = training_Session8
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def training_Session8(self):
        return self.__training_Session8

    @training_Session8.setter
    def training_Session8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_training_Session__training_Session8", None)
        self.__training_Session8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "training_TrainingOrganization7"):
                opp_val = getattr(old_value, "training_TrainingOrganization7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "training_TrainingOrganization7"):
                opp_val = getattr(value, "training_TrainingOrganization7", None)
                if opp_val is None:
                    setattr(value, "training_TrainingOrganization7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def session(self):
        return self.__session

    @session.setter
    def session(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_training_Session__session", None)
        self.__session = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Training"):
                opp_val = getattr(old_value, "Training", None)
                if opp_val == self:
                    setattr(old_value, "Training", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Training"):
                opp_val = getattr(value, "Training", None)
                setattr(value, "Training", self)

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
    def Session(self):
        return self.__Session

    @Session.setter
    def Session(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_training_Session__Session", None)
        self.__Session = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "training"):
                opp_val = getattr(old_value, "training", None)
                if opp_val == self:
                    setattr(old_value, "training", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "training"):
                opp_val = getattr(value, "training", None)
                setattr(value, "training", self)

    @property
    def training_Session3(self):
        return self.__training_Session3

    @training_Session3.setter
    def training_Session3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_training_Session__training_Session3", None)
        self.__training_Session3 = value if value is not None else set()
        
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
                    
