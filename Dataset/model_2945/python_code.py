from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Type:

    pass
class slolpBPM_Datatype(Type):

    pass
class slolpBPM_Feature:

    def __init__(self, many: bool, name: str, slolpBPM_Feature: "slolpBPM_Entity" = None, slolpBPM_Feature6: "slolpBPM_Type" = None):
        self.many = many
        self.name = name
        self.slolpBPM_Feature = slolpBPM_Feature
        self.slolpBPM_Feature6 = slolpBPM_Feature6
        
    @property
    def many(self) -> bool:
        return self.__many

    @many.setter
    def many(self, many: bool):
        self.__many = many

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def slolpBPM_Feature6(self):
        return self.__slolpBPM_Feature6

    @slolpBPM_Feature6.setter
    def slolpBPM_Feature6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_slolpBPM_Feature__slolpBPM_Feature6", None)
        self.__slolpBPM_Feature6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "slolpBPM_Type7"):
                opp_val = getattr(old_value, "slolpBPM_Type7", None)
                if opp_val == self:
                    setattr(old_value, "slolpBPM_Type7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "slolpBPM_Type7"):
                opp_val = getattr(value, "slolpBPM_Type7", None)
                setattr(value, "slolpBPM_Type7", self)

    @property
    def slolpBPM_Feature(self):
        return self.__slolpBPM_Feature

    @slolpBPM_Feature.setter
    def slolpBPM_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_slolpBPM_Feature__slolpBPM_Feature", None)
        self.__slolpBPM_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "slolpBPM_Entity4"):
                opp_val = getattr(old_value, "slolpBPM_Entity4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "slolpBPM_Entity4"):
                opp_val = getattr(value, "slolpBPM_Entity4", None)
                if opp_val is None:
                    setattr(value, "slolpBPM_Entity4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class slolpBPM_Entity(Type):

    pass
class slolpBPM_Type:

    def __init__(self, name: str, slolpBPM_Type: "slolpBPM_DomainModel" = None, slolpBPM_Type7: "slolpBPM_Feature" = None):
        self.name = name
        self.slolpBPM_Type = slolpBPM_Type
        self.slolpBPM_Type7 = slolpBPM_Type7
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def slolpBPM_Type(self):
        return self.__slolpBPM_Type

    @slolpBPM_Type.setter
    def slolpBPM_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_slolpBPM_Type__slolpBPM_Type", None)
        self.__slolpBPM_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "slolpBPM_DomainModel"):
                opp_val = getattr(old_value, "slolpBPM_DomainModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "slolpBPM_DomainModel"):
                opp_val = getattr(value, "slolpBPM_DomainModel", None)
                if opp_val is None:
                    setattr(value, "slolpBPM_DomainModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def slolpBPM_Type7(self):
        return self.__slolpBPM_Type7

    @slolpBPM_Type7.setter
    def slolpBPM_Type7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_slolpBPM_Type__slolpBPM_Type7", None)
        self.__slolpBPM_Type7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "slolpBPM_Feature6"):
                opp_val = getattr(old_value, "slolpBPM_Feature6", None)
                if opp_val == self:
                    setattr(old_value, "slolpBPM_Feature6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "slolpBPM_Feature6"):
                opp_val = getattr(value, "slolpBPM_Feature6", None)
                setattr(value, "slolpBPM_Feature6", self)

class slolpBPM_DomainModel:

    pass