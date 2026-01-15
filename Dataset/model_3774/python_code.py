from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class features_Feature:

    def __init__(self, abstract: bool, name: str, short: str, features_Feature3: "features_Feature" = None, features_Feature1: "features_Feature" = None, features_Feature6: "features_Feature" = None, features_Feature4: "features_Feature" = None, features_Feature9: "features_Feature" = None, features_Feature7: set["features_Feature"] = None, features_Feature12: "features_Feature" = None, features_Feature10: set["features_Feature"] = None, features_Feature: "features_Model" = None):
        self.abstract = abstract
        self.name = name
        self.short = short
        self.features_Feature3 = features_Feature3
        self.features_Feature1 = features_Feature1
        self.features_Feature6 = features_Feature6
        self.features_Feature4 = features_Feature4
        self.features_Feature9 = features_Feature9
        self.features_Feature7 = features_Feature7 if features_Feature7 is not None else set()
        self.features_Feature12 = features_Feature12
        self.features_Feature10 = features_Feature10 if features_Feature10 is not None else set()
        self.features_Feature = features_Feature
        
    @property
    def short(self) -> str:
        return self.__short

    @short.setter
    def short(self, short: str):
        self.__short = short

    @property
    def abstract(self) -> bool:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def features_Feature12(self):
        return self.__features_Feature12

    @features_Feature12.setter
    def features_Feature12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_features_Feature__features_Feature12", None)
        self.__features_Feature12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "features_Feature10"):
                opp_val = getattr(old_value, "features_Feature10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "features_Feature10"):
                opp_val = getattr(value, "features_Feature10", None)
                if opp_val is None:
                    setattr(value, "features_Feature10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def features_Feature6(self):
        return self.__features_Feature6

    @features_Feature6.setter
    def features_Feature6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_features_Feature__features_Feature6", None)
        self.__features_Feature6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "features_Feature4"):
                opp_val = getattr(old_value, "features_Feature4", None)
                if opp_val == self:
                    setattr(old_value, "features_Feature4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "features_Feature4"):
                opp_val = getattr(value, "features_Feature4", None)
                setattr(value, "features_Feature4", self)

    @property
    def features_Feature9(self):
        return self.__features_Feature9

    @features_Feature9.setter
    def features_Feature9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_features_Feature__features_Feature9", None)
        self.__features_Feature9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "features_Feature7"):
                opp_val = getattr(old_value, "features_Feature7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "features_Feature7"):
                opp_val = getattr(value, "features_Feature7", None)
                if opp_val is None:
                    setattr(value, "features_Feature7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def features_Feature1(self):
        return self.__features_Feature1

    @features_Feature1.setter
    def features_Feature1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_features_Feature__features_Feature1", None)
        self.__features_Feature1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "features_Feature3"):
                opp_val = getattr(old_value, "features_Feature3", None)
                if opp_val == self:
                    setattr(old_value, "features_Feature3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "features_Feature3"):
                opp_val = getattr(value, "features_Feature3", None)
                setattr(value, "features_Feature3", self)

    @property
    def features_Feature7(self):
        return self.__features_Feature7

    @features_Feature7.setter
    def features_Feature7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_features_Feature__features_Feature7", None)
        self.__features_Feature7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "features_Feature9"):
                    opp_val = getattr(item, "features_Feature9", None)
                    
                    if opp_val == self:
                        setattr(item, "features_Feature9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "features_Feature9"):
                    opp_val = getattr(item, "features_Feature9", None)
                    
                    setattr(item, "features_Feature9", self)
                    

    @property
    def features_Feature3(self):
        return self.__features_Feature3

    @features_Feature3.setter
    def features_Feature3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_features_Feature__features_Feature3", None)
        self.__features_Feature3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "features_Feature1"):
                opp_val = getattr(old_value, "features_Feature1", None)
                if opp_val == self:
                    setattr(old_value, "features_Feature1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "features_Feature1"):
                opp_val = getattr(value, "features_Feature1", None)
                setattr(value, "features_Feature1", self)

    @property
    def features_Feature4(self):
        return self.__features_Feature4

    @features_Feature4.setter
    def features_Feature4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_features_Feature__features_Feature4", None)
        self.__features_Feature4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "features_Feature6"):
                opp_val = getattr(old_value, "features_Feature6", None)
                if opp_val == self:
                    setattr(old_value, "features_Feature6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "features_Feature6"):
                opp_val = getattr(value, "features_Feature6", None)
                setattr(value, "features_Feature6", self)

    @property
    def features_Feature10(self):
        return self.__features_Feature10

    @features_Feature10.setter
    def features_Feature10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_features_Feature__features_Feature10", None)
        self.__features_Feature10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "features_Feature12"):
                    opp_val = getattr(item, "features_Feature12", None)
                    
                    if opp_val == self:
                        setattr(item, "features_Feature12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "features_Feature12"):
                    opp_val = getattr(item, "features_Feature12", None)
                    
                    setattr(item, "features_Feature12", self)
                    

    @property
    def features_Feature(self):
        return self.__features_Feature

    @features_Feature.setter
    def features_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_features_Feature__features_Feature", None)
        self.__features_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "features_Model"):
                opp_val = getattr(old_value, "features_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "features_Model"):
                opp_val = getattr(value, "features_Model", None)
                if opp_val is None:
                    setattr(value, "features_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class features_Model:

    pass