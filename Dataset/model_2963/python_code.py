from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class sample_Car:

    def __init__(self, horsePower: int, sample_Car: "sample_Person" = None):
        self.horsePower = horsePower
        self.sample_Car = sample_Car
        
    @property
    def horsePower(self) -> int:
        return self.__horsePower

    @horsePower.setter
    def horsePower(self, horsePower: int):
        self.__horsePower = horsePower

    @property
    def sample_Car(self):
        return self.__sample_Car

    @sample_Car.setter
    def sample_Car(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_Car__sample_Car", None)
        self.__sample_Car = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sample_Person"):
                opp_val = getattr(old_value, "sample_Person", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sample_Person"):
                opp_val = getattr(value, "sample_Person", None)
                if opp_val is None:
                    setattr(value, "sample_Person", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sample_Person:

    def __init__(self, firstName: str, lastName: str, sample_Person: set["sample_Car"] = None):
        self.firstName = firstName
        self.lastName = lastName
        self.sample_Person = sample_Person if sample_Person is not None else set()
        
    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def sample_Person(self):
        return self.__sample_Person

    @sample_Person.setter
    def sample_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_Person__sample_Person", None)
        self.__sample_Person = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sample_Car"):
                    opp_val = getattr(item, "sample_Car", None)
                    
                    if opp_val == self:
                        setattr(item, "sample_Car", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sample_Car"):
                    opp_val = getattr(item, "sample_Car", None)
                    
                    setattr(item, "sample_Car", self)
                    

    def buy(self, car: str):
        # TODO: Implement buy method
        pass
