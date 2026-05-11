from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class domainmodel_Feature:

    def __init__(self, not_: str, name: str, key: str, domainmodel_Feature: "domainmodel_Entity" = None, domainmodel_Feature6: "domainmodel_Type" = None):
        self.not_ = not_
        self.name = name
        self.key = key
        self.domainmodel_Feature = domainmodel_Feature
        self.domainmodel_Feature6 = domainmodel_Feature6
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def not_(self):
        return self.__not_

    @not_.setter
    def not_(self, not_: str):
        self.__not_ = not_


    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key


    @property
    def domainmodel_Feature(self):
        return self.__domainmodel_Feature

    @domainmodel_Feature.setter
    def domainmodel_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_Feature__domainmodel_Feature", None)
        self.__domainmodel_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_Entity4"):
                opp_val = getattr(old_value, "domainmodel_Entity4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_Entity4"):
                opp_val = getattr(value, "domainmodel_Entity4", None)
                if opp_val is None:
                    setattr(value, "domainmodel_Entity4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def domainmodel_Feature6(self):
        return self.__domainmodel_Feature6

    @domainmodel_Feature6.setter
    def domainmodel_Feature6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_Feature__domainmodel_Feature6", None)
        self.__domainmodel_Feature6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_Type7"):
                opp_val = getattr(old_value, "domainmodel_Type7", None)
                if opp_val == self:
                    setattr(old_value, "domainmodel_Type7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_Type7"):
                opp_val = getattr(value, "domainmodel_Type7", None)
                setattr(value, "domainmodel_Type7", self)

class Type:

    pass
class domainmodel_Entity(Type):

    pass
class domainmodel_DataType(Type):

    pass
class domainmodel_Type:

    def __init__(self, name: str, domainmodel_Type: "domainmodel_Domainmodel" = None, domainmodel_Type7: "domainmodel_Feature" = None):
        self.name = name
        self.domainmodel_Type = domainmodel_Type
        self.domainmodel_Type7 = domainmodel_Type7
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def domainmodel_Type7(self):
        return self.__domainmodel_Type7

    @domainmodel_Type7.setter
    def domainmodel_Type7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_Type__domainmodel_Type7", None)
        self.__domainmodel_Type7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_Feature6"):
                opp_val = getattr(old_value, "domainmodel_Feature6", None)
                if opp_val == self:
                    setattr(old_value, "domainmodel_Feature6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_Feature6"):
                opp_val = getattr(value, "domainmodel_Feature6", None)
                setattr(value, "domainmodel_Feature6", self)

    @property
    def domainmodel_Type(self):
        return self.__domainmodel_Type

    @domainmodel_Type.setter
    def domainmodel_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_domainmodel_Type__domainmodel_Type", None)
        self.__domainmodel_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "domainmodel_Domainmodel"):
                opp_val = getattr(old_value, "domainmodel_Domainmodel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "domainmodel_Domainmodel"):
                opp_val = getattr(value, "domainmodel_Domainmodel", None)
                if opp_val is None:
                    setattr(value, "domainmodel_Domainmodel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class domainmodel_Domainmodel:

    pass