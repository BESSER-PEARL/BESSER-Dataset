from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class TreeConstraint:

    pass
class sPLOT2CoCo_OrAlternativeTreeConstraint(TreeConstraint):

    def __init__(self, min: int, max: int, sPLOT2CoCo_OrAlternativeTreeConstraint: set["sPLOT2CoCo_Feature"] = None):
        self.min = min
        self.max = max
        self.sPLOT2CoCo_OrAlternativeTreeConstraint = sPLOT2CoCo_OrAlternativeTreeConstraint if sPLOT2CoCo_OrAlternativeTreeConstraint is not None else set()
        
    @property
    def max(self) -> int:
        return self.__max

    @max.setter
    def max(self, max: int):
        self.__max = max

    @property
    def min(self) -> int:
        return self.__min

    @min.setter
    def min(self, min: int):
        self.__min = min

    @property
    def sPLOT2CoCo_OrAlternativeTreeConstraint(self):
        return self.__sPLOT2CoCo_OrAlternativeTreeConstraint

    @sPLOT2CoCo_OrAlternativeTreeConstraint.setter
    def sPLOT2CoCo_OrAlternativeTreeConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sPLOT2CoCo_OrAlternativeTreeConstraint__sPLOT2CoCo_OrAlternativeTreeConstraint", None)
        self.__sPLOT2CoCo_OrAlternativeTreeConstraint = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sPLOT2CoCo_Feature17"):
                    opp_val = getattr(item, "sPLOT2CoCo_Feature17", None)
                    
                    if opp_val == self:
                        setattr(item, "sPLOT2CoCo_Feature17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sPLOT2CoCo_Feature17"):
                    opp_val = getattr(item, "sPLOT2CoCo_Feature17", None)
                    
                    setattr(item, "sPLOT2CoCo_Feature17", self)
                    

class sPLOT2CoCo_OptionalTreeConstraint(TreeConstraint):

    pass
class sPLOT2CoCo_MandatoryTreeConstraint(TreeConstraint):

    pass
class sPLOT2CoCo_TreeConstraint:

    pass
class sPLOT2CoCo_CrossTreeConstraint:

    def __init__(self, type: str, sPLOT2CoCo_CrossTreeConstraint: "sPLOT2CoCo_FM" = None, sPLOT2CoCo_CrossTreeConstraint19: "sPLOT2CoCo_Feature" = None, sPLOT2CoCo_CrossTreeConstraint22: "sPLOT2CoCo_Feature" = None):
        self.type = type
        self.sPLOT2CoCo_CrossTreeConstraint = sPLOT2CoCo_CrossTreeConstraint
        self.sPLOT2CoCo_CrossTreeConstraint19 = sPLOT2CoCo_CrossTreeConstraint19
        self.sPLOT2CoCo_CrossTreeConstraint22 = sPLOT2CoCo_CrossTreeConstraint22
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def sPLOT2CoCo_CrossTreeConstraint19(self):
        return self.__sPLOT2CoCo_CrossTreeConstraint19

    @sPLOT2CoCo_CrossTreeConstraint19.setter
    def sPLOT2CoCo_CrossTreeConstraint19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sPLOT2CoCo_CrossTreeConstraint__sPLOT2CoCo_CrossTreeConstraint19", None)
        self.__sPLOT2CoCo_CrossTreeConstraint19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sPLOT2CoCo_Feature20"):
                opp_val = getattr(old_value, "sPLOT2CoCo_Feature20", None)
                if opp_val == self:
                    setattr(old_value, "sPLOT2CoCo_Feature20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sPLOT2CoCo_Feature20"):
                opp_val = getattr(value, "sPLOT2CoCo_Feature20", None)
                setattr(value, "sPLOT2CoCo_Feature20", self)

    @property
    def sPLOT2CoCo_CrossTreeConstraint(self):
        return self.__sPLOT2CoCo_CrossTreeConstraint

    @sPLOT2CoCo_CrossTreeConstraint.setter
    def sPLOT2CoCo_CrossTreeConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sPLOT2CoCo_CrossTreeConstraint__sPLOT2CoCo_CrossTreeConstraint", None)
        self.__sPLOT2CoCo_CrossTreeConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sPLOT2CoCo_FM6"):
                opp_val = getattr(old_value, "sPLOT2CoCo_FM6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sPLOT2CoCo_FM6"):
                opp_val = getattr(value, "sPLOT2CoCo_FM6", None)
                if opp_val is None:
                    setattr(value, "sPLOT2CoCo_FM6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sPLOT2CoCo_CrossTreeConstraint22(self):
        return self.__sPLOT2CoCo_CrossTreeConstraint22

    @sPLOT2CoCo_CrossTreeConstraint22.setter
    def sPLOT2CoCo_CrossTreeConstraint22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sPLOT2CoCo_CrossTreeConstraint__sPLOT2CoCo_CrossTreeConstraint22", None)
        self.__sPLOT2CoCo_CrossTreeConstraint22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sPLOT2CoCo_Feature23"):
                opp_val = getattr(old_value, "sPLOT2CoCo_Feature23", None)
                if opp_val == self:
                    setattr(old_value, "sPLOT2CoCo_Feature23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sPLOT2CoCo_Feature23"):
                opp_val = getattr(value, "sPLOT2CoCo_Feature23", None)
                setattr(value, "sPLOT2CoCo_Feature23", self)

class sPLOT2CoCo_FeatureAttribute:

    def __init__(self, attributeType: str, minValue: int, maxValue: int, defaultValue: int, nullValue: int, sPLOT2CoCo_FeatureAttribute: "sPLOT2CoCo_FM" = None, sPLOT2CoCo_FeatureAttribute25: "sPLOT2CoCo_Feature" = None):
        self.attributeType = attributeType
        self.minValue = minValue
        self.maxValue = maxValue
        self.defaultValue = defaultValue
        self.nullValue = nullValue
        self.sPLOT2CoCo_FeatureAttribute = sPLOT2CoCo_FeatureAttribute
        self.sPLOT2CoCo_FeatureAttribute25 = sPLOT2CoCo_FeatureAttribute25
        
    @property
    def nullValue(self) -> int:
        return self.__nullValue

    @nullValue.setter
    def nullValue(self, nullValue: int):
        self.__nullValue = nullValue

    @property
    def defaultValue(self) -> int:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: int):
        self.__defaultValue = defaultValue

    @property
    def attributeType(self) -> str:
        return self.__attributeType

    @attributeType.setter
    def attributeType(self, attributeType: str):
        self.__attributeType = attributeType

    @property
    def maxValue(self) -> int:
        return self.__maxValue

    @maxValue.setter
    def maxValue(self, maxValue: int):
        self.__maxValue = maxValue

    @property
    def minValue(self) -> int:
        return self.__minValue

    @minValue.setter
    def minValue(self, minValue: int):
        self.__minValue = minValue

    @property
    def sPLOT2CoCo_FeatureAttribute25(self):
        return self.__sPLOT2CoCo_FeatureAttribute25

    @sPLOT2CoCo_FeatureAttribute25.setter
    def sPLOT2CoCo_FeatureAttribute25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sPLOT2CoCo_FeatureAttribute__sPLOT2CoCo_FeatureAttribute25", None)
        self.__sPLOT2CoCo_FeatureAttribute25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sPLOT2CoCo_Feature26"):
                opp_val = getattr(old_value, "sPLOT2CoCo_Feature26", None)
                if opp_val == self:
                    setattr(old_value, "sPLOT2CoCo_Feature26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sPLOT2CoCo_Feature26"):
                opp_val = getattr(value, "sPLOT2CoCo_Feature26", None)
                setattr(value, "sPLOT2CoCo_Feature26", self)

    @property
    def sPLOT2CoCo_FeatureAttribute(self):
        return self.__sPLOT2CoCo_FeatureAttribute

    @sPLOT2CoCo_FeatureAttribute.setter
    def sPLOT2CoCo_FeatureAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sPLOT2CoCo_FeatureAttribute__sPLOT2CoCo_FeatureAttribute", None)
        self.__sPLOT2CoCo_FeatureAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sPLOT2CoCo_FM4"):
                opp_val = getattr(old_value, "sPLOT2CoCo_FM4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sPLOT2CoCo_FM4"):
                opp_val = getattr(value, "sPLOT2CoCo_FM4", None)
                if opp_val is None:
                    setattr(value, "sPLOT2CoCo_FM4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sPLOT2CoCo_ParentChildConstraint:

    pass
class sPLOT2CoCo_Feature:

    def __init__(self, name: str, sPLOT2CoCo_Feature: "sPLOT2CoCo_FM" = None, sPLOT2CoCo_Feature9: "sPLOT2CoCo_ParentChildConstraint" = None, sPLOT2CoCo_Feature13: "sPLOT2CoCo_MandatoryTreeConstraint" = None, sPLOT2CoCo_Feature15: "sPLOT2CoCo_OptionalTreeConstraint" = None, sPLOT2CoCo_Feature17: "sPLOT2CoCo_OrAlternativeTreeConstraint" = None, sPLOT2CoCo_Feature20: "sPLOT2CoCo_CrossTreeConstraint" = None, sPLOT2CoCo_Feature23: "sPLOT2CoCo_CrossTreeConstraint" = None, sPLOT2CoCo_Feature26: "sPLOT2CoCo_FeatureAttribute" = None):
        self.name = name
        self.sPLOT2CoCo_Feature = sPLOT2CoCo_Feature
        self.sPLOT2CoCo_Feature9 = sPLOT2CoCo_Feature9
        self.sPLOT2CoCo_Feature13 = sPLOT2CoCo_Feature13
        self.sPLOT2CoCo_Feature15 = sPLOT2CoCo_Feature15
        self.sPLOT2CoCo_Feature17 = sPLOT2CoCo_Feature17
        self.sPLOT2CoCo_Feature20 = sPLOT2CoCo_Feature20
        self.sPLOT2CoCo_Feature23 = sPLOT2CoCo_Feature23
        self.sPLOT2CoCo_Feature26 = sPLOT2CoCo_Feature26
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sPLOT2CoCo_Feature15(self):
        return self.__sPLOT2CoCo_Feature15

    @sPLOT2CoCo_Feature15.setter
    def sPLOT2CoCo_Feature15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sPLOT2CoCo_Feature__sPLOT2CoCo_Feature15", None)
        self.__sPLOT2CoCo_Feature15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sPLOT2CoCo_OptionalTreeConstraint"):
                opp_val = getattr(old_value, "sPLOT2CoCo_OptionalTreeConstraint", None)
                if opp_val == self:
                    setattr(old_value, "sPLOT2CoCo_OptionalTreeConstraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sPLOT2CoCo_OptionalTreeConstraint"):
                opp_val = getattr(value, "sPLOT2CoCo_OptionalTreeConstraint", None)
                setattr(value, "sPLOT2CoCo_OptionalTreeConstraint", self)

    @property
    def sPLOT2CoCo_Feature17(self):
        return self.__sPLOT2CoCo_Feature17

    @sPLOT2CoCo_Feature17.setter
    def sPLOT2CoCo_Feature17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sPLOT2CoCo_Feature__sPLOT2CoCo_Feature17", None)
        self.__sPLOT2CoCo_Feature17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sPLOT2CoCo_OrAlternativeTreeConstraint"):
                opp_val = getattr(old_value, "sPLOT2CoCo_OrAlternativeTreeConstraint", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sPLOT2CoCo_OrAlternativeTreeConstraint"):
                opp_val = getattr(value, "sPLOT2CoCo_OrAlternativeTreeConstraint", None)
                if opp_val is None:
                    setattr(value, "sPLOT2CoCo_OrAlternativeTreeConstraint", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sPLOT2CoCo_Feature20(self):
        return self.__sPLOT2CoCo_Feature20

    @sPLOT2CoCo_Feature20.setter
    def sPLOT2CoCo_Feature20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sPLOT2CoCo_Feature__sPLOT2CoCo_Feature20", None)
        self.__sPLOT2CoCo_Feature20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sPLOT2CoCo_CrossTreeConstraint19"):
                opp_val = getattr(old_value, "sPLOT2CoCo_CrossTreeConstraint19", None)
                if opp_val == self:
                    setattr(old_value, "sPLOT2CoCo_CrossTreeConstraint19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sPLOT2CoCo_CrossTreeConstraint19"):
                opp_val = getattr(value, "sPLOT2CoCo_CrossTreeConstraint19", None)
                setattr(value, "sPLOT2CoCo_CrossTreeConstraint19", self)

    @property
    def sPLOT2CoCo_Feature26(self):
        return self.__sPLOT2CoCo_Feature26

    @sPLOT2CoCo_Feature26.setter
    def sPLOT2CoCo_Feature26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sPLOT2CoCo_Feature__sPLOT2CoCo_Feature26", None)
        self.__sPLOT2CoCo_Feature26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sPLOT2CoCo_FeatureAttribute25"):
                opp_val = getattr(old_value, "sPLOT2CoCo_FeatureAttribute25", None)
                if opp_val == self:
                    setattr(old_value, "sPLOT2CoCo_FeatureAttribute25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sPLOT2CoCo_FeatureAttribute25"):
                opp_val = getattr(value, "sPLOT2CoCo_FeatureAttribute25", None)
                setattr(value, "sPLOT2CoCo_FeatureAttribute25", self)

    @property
    def sPLOT2CoCo_Feature23(self):
        return self.__sPLOT2CoCo_Feature23

    @sPLOT2CoCo_Feature23.setter
    def sPLOT2CoCo_Feature23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sPLOT2CoCo_Feature__sPLOT2CoCo_Feature23", None)
        self.__sPLOT2CoCo_Feature23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sPLOT2CoCo_CrossTreeConstraint22"):
                opp_val = getattr(old_value, "sPLOT2CoCo_CrossTreeConstraint22", None)
                if opp_val == self:
                    setattr(old_value, "sPLOT2CoCo_CrossTreeConstraint22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sPLOT2CoCo_CrossTreeConstraint22"):
                opp_val = getattr(value, "sPLOT2CoCo_CrossTreeConstraint22", None)
                setattr(value, "sPLOT2CoCo_CrossTreeConstraint22", self)

    @property
    def sPLOT2CoCo_Feature13(self):
        return self.__sPLOT2CoCo_Feature13

    @sPLOT2CoCo_Feature13.setter
    def sPLOT2CoCo_Feature13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sPLOT2CoCo_Feature__sPLOT2CoCo_Feature13", None)
        self.__sPLOT2CoCo_Feature13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sPLOT2CoCo_MandatoryTreeConstraint"):
                opp_val = getattr(old_value, "sPLOT2CoCo_MandatoryTreeConstraint", None)
                if opp_val == self:
                    setattr(old_value, "sPLOT2CoCo_MandatoryTreeConstraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sPLOT2CoCo_MandatoryTreeConstraint"):
                opp_val = getattr(value, "sPLOT2CoCo_MandatoryTreeConstraint", None)
                setattr(value, "sPLOT2CoCo_MandatoryTreeConstraint", self)

    @property
    def sPLOT2CoCo_Feature9(self):
        return self.__sPLOT2CoCo_Feature9

    @sPLOT2CoCo_Feature9.setter
    def sPLOT2CoCo_Feature9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sPLOT2CoCo_Feature__sPLOT2CoCo_Feature9", None)
        self.__sPLOT2CoCo_Feature9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sPLOT2CoCo_ParentChildConstraint8"):
                opp_val = getattr(old_value, "sPLOT2CoCo_ParentChildConstraint8", None)
                if opp_val == self:
                    setattr(old_value, "sPLOT2CoCo_ParentChildConstraint8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sPLOT2CoCo_ParentChildConstraint8"):
                opp_val = getattr(value, "sPLOT2CoCo_ParentChildConstraint8", None)
                setattr(value, "sPLOT2CoCo_ParentChildConstraint8", self)

    @property
    def sPLOT2CoCo_Feature(self):
        return self.__sPLOT2CoCo_Feature

    @sPLOT2CoCo_Feature.setter
    def sPLOT2CoCo_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sPLOT2CoCo_Feature__sPLOT2CoCo_Feature", None)
        self.__sPLOT2CoCo_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sPLOT2CoCo_FM"):
                opp_val = getattr(old_value, "sPLOT2CoCo_FM", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sPLOT2CoCo_FM"):
                opp_val = getattr(value, "sPLOT2CoCo_FM", None)
                if opp_val is None:
                    setattr(value, "sPLOT2CoCo_FM", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sPLOT2CoCo_FM:

    pass