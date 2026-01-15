from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class TreeConstraint:

    pass
class myDsl_MandatoryTreeConstraint(TreeConstraint):

    pass
class myDsl_OrAlternativeTreeConstraint(TreeConstraint):

    def __init__(self, min: int, max: int, myDsl_OrAlternativeTreeConstraint: set["myDsl_Feature"] = None):
        self.min = min
        self.max = max
        self.myDsl_OrAlternativeTreeConstraint = myDsl_OrAlternativeTreeConstraint if myDsl_OrAlternativeTreeConstraint is not None else set()
        
    @property
    def min(self) -> int:
        return self.__min

    @min.setter
    def min(self, min: int):
        self.__min = min

    @property
    def max(self) -> int:
        return self.__max

    @max.setter
    def max(self, max: int):
        self.__max = max

    @property
    def myDsl_OrAlternativeTreeConstraint(self):
        return self.__myDsl_OrAlternativeTreeConstraint

    @myDsl_OrAlternativeTreeConstraint.setter
    def myDsl_OrAlternativeTreeConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_OrAlternativeTreeConstraint__myDsl_OrAlternativeTreeConstraint", None)
        self.__myDsl_OrAlternativeTreeConstraint = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_Feature17"):
                    opp_val = getattr(item, "myDsl_Feature17", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_Feature17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_Feature17"):
                    opp_val = getattr(item, "myDsl_Feature17", None)
                    
                    setattr(item, "myDsl_Feature17", self)
                    

class myDsl_OptionalTreeConstraint(TreeConstraint):

    pass
class myDsl_ParentChildConstraint:

    pass
class myDsl_TreeConstraint:

    pass
class myDsl_CrossTreeConstraint:

    def __init__(self, type: str, myDsl_CrossTreeConstraint: "myDsl_FM" = None, myDsl_CrossTreeConstraint19: "myDsl_Feature" = None, myDsl_CrossTreeConstraint22: "myDsl_Feature" = None):
        self.type = type
        self.myDsl_CrossTreeConstraint = myDsl_CrossTreeConstraint
        self.myDsl_CrossTreeConstraint19 = myDsl_CrossTreeConstraint19
        self.myDsl_CrossTreeConstraint22 = myDsl_CrossTreeConstraint22
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def myDsl_CrossTreeConstraint(self):
        return self.__myDsl_CrossTreeConstraint

    @myDsl_CrossTreeConstraint.setter
    def myDsl_CrossTreeConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_CrossTreeConstraint__myDsl_CrossTreeConstraint", None)
        self.__myDsl_CrossTreeConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_FM6"):
                opp_val = getattr(old_value, "myDsl_FM6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_FM6"):
                opp_val = getattr(value, "myDsl_FM6", None)
                if opp_val is None:
                    setattr(value, "myDsl_FM6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_CrossTreeConstraint19(self):
        return self.__myDsl_CrossTreeConstraint19

    @myDsl_CrossTreeConstraint19.setter
    def myDsl_CrossTreeConstraint19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_CrossTreeConstraint__myDsl_CrossTreeConstraint19", None)
        self.__myDsl_CrossTreeConstraint19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Feature20"):
                opp_val = getattr(old_value, "myDsl_Feature20", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Feature20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Feature20"):
                opp_val = getattr(value, "myDsl_Feature20", None)
                setattr(value, "myDsl_Feature20", self)

    @property
    def myDsl_CrossTreeConstraint22(self):
        return self.__myDsl_CrossTreeConstraint22

    @myDsl_CrossTreeConstraint22.setter
    def myDsl_CrossTreeConstraint22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_CrossTreeConstraint__myDsl_CrossTreeConstraint22", None)
        self.__myDsl_CrossTreeConstraint22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Feature23"):
                opp_val = getattr(old_value, "myDsl_Feature23", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Feature23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Feature23"):
                opp_val = getattr(value, "myDsl_Feature23", None)
                setattr(value, "myDsl_Feature23", self)

class myDsl_FeatureAttribute:

    def __init__(self, attributeType: str, minValue: int, maxValue: int, defaultValue: int, nullValue: int, myDsl_FeatureAttribute: "myDsl_FM" = None, myDsl_FeatureAttribute25: "myDsl_Feature" = None):
        self.attributeType = attributeType
        self.minValue = minValue
        self.maxValue = maxValue
        self.defaultValue = defaultValue
        self.nullValue = nullValue
        self.myDsl_FeatureAttribute = myDsl_FeatureAttribute
        self.myDsl_FeatureAttribute25 = myDsl_FeatureAttribute25
        
    @property
    def nullValue(self) -> int:
        return self.__nullValue

    @nullValue.setter
    def nullValue(self, nullValue: int):
        self.__nullValue = nullValue

    @property
    def minValue(self) -> int:
        return self.__minValue

    @minValue.setter
    def minValue(self, minValue: int):
        self.__minValue = minValue

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
    def defaultValue(self) -> int:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: int):
        self.__defaultValue = defaultValue

    @property
    def myDsl_FeatureAttribute25(self):
        return self.__myDsl_FeatureAttribute25

    @myDsl_FeatureAttribute25.setter
    def myDsl_FeatureAttribute25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_FeatureAttribute__myDsl_FeatureAttribute25", None)
        self.__myDsl_FeatureAttribute25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Feature26"):
                opp_val = getattr(old_value, "myDsl_Feature26", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Feature26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Feature26"):
                opp_val = getattr(value, "myDsl_Feature26", None)
                setattr(value, "myDsl_Feature26", self)

    @property
    def myDsl_FeatureAttribute(self):
        return self.__myDsl_FeatureAttribute

    @myDsl_FeatureAttribute.setter
    def myDsl_FeatureAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_FeatureAttribute__myDsl_FeatureAttribute", None)
        self.__myDsl_FeatureAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_FM4"):
                opp_val = getattr(old_value, "myDsl_FM4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_FM4"):
                opp_val = getattr(value, "myDsl_FM4", None)
                if opp_val is None:
                    setattr(value, "myDsl_FM4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myDsl_Feature:

    def __init__(self, name: str, myDsl_Feature9: "myDsl_ParentChildConstraint" = None, myDsl_Feature: "myDsl_FM" = None, myDsl_Feature13: "myDsl_MandatoryTreeConstraint" = None, myDsl_Feature15: "myDsl_OptionalTreeConstraint" = None, myDsl_Feature17: "myDsl_OrAlternativeTreeConstraint" = None, myDsl_Feature26: "myDsl_FeatureAttribute" = None, myDsl_Feature20: "myDsl_CrossTreeConstraint" = None, myDsl_Feature23: "myDsl_CrossTreeConstraint" = None):
        self.name = name
        self.myDsl_Feature9 = myDsl_Feature9
        self.myDsl_Feature = myDsl_Feature
        self.myDsl_Feature13 = myDsl_Feature13
        self.myDsl_Feature15 = myDsl_Feature15
        self.myDsl_Feature17 = myDsl_Feature17
        self.myDsl_Feature26 = myDsl_Feature26
        self.myDsl_Feature20 = myDsl_Feature20
        self.myDsl_Feature23 = myDsl_Feature23
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_Feature9(self):
        return self.__myDsl_Feature9

    @myDsl_Feature9.setter
    def myDsl_Feature9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Feature__myDsl_Feature9", None)
        self.__myDsl_Feature9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_ParentChildConstraint8"):
                opp_val = getattr(old_value, "myDsl_ParentChildConstraint8", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_ParentChildConstraint8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_ParentChildConstraint8"):
                opp_val = getattr(value, "myDsl_ParentChildConstraint8", None)
                setattr(value, "myDsl_ParentChildConstraint8", self)

    @property
    def myDsl_Feature26(self):
        return self.__myDsl_Feature26

    @myDsl_Feature26.setter
    def myDsl_Feature26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Feature__myDsl_Feature26", None)
        self.__myDsl_Feature26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_FeatureAttribute25"):
                opp_val = getattr(old_value, "myDsl_FeatureAttribute25", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_FeatureAttribute25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_FeatureAttribute25"):
                opp_val = getattr(value, "myDsl_FeatureAttribute25", None)
                setattr(value, "myDsl_FeatureAttribute25", self)

    @property
    def myDsl_Feature15(self):
        return self.__myDsl_Feature15

    @myDsl_Feature15.setter
    def myDsl_Feature15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Feature__myDsl_Feature15", None)
        self.__myDsl_Feature15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_OptionalTreeConstraint"):
                opp_val = getattr(old_value, "myDsl_OptionalTreeConstraint", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_OptionalTreeConstraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_OptionalTreeConstraint"):
                opp_val = getattr(value, "myDsl_OptionalTreeConstraint", None)
                setattr(value, "myDsl_OptionalTreeConstraint", self)

    @property
    def myDsl_Feature13(self):
        return self.__myDsl_Feature13

    @myDsl_Feature13.setter
    def myDsl_Feature13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Feature__myDsl_Feature13", None)
        self.__myDsl_Feature13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_MandatoryTreeConstraint"):
                opp_val = getattr(old_value, "myDsl_MandatoryTreeConstraint", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_MandatoryTreeConstraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_MandatoryTreeConstraint"):
                opp_val = getattr(value, "myDsl_MandatoryTreeConstraint", None)
                setattr(value, "myDsl_MandatoryTreeConstraint", self)

    @property
    def myDsl_Feature17(self):
        return self.__myDsl_Feature17

    @myDsl_Feature17.setter
    def myDsl_Feature17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Feature__myDsl_Feature17", None)
        self.__myDsl_Feature17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_OrAlternativeTreeConstraint"):
                opp_val = getattr(old_value, "myDsl_OrAlternativeTreeConstraint", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_OrAlternativeTreeConstraint"):
                opp_val = getattr(value, "myDsl_OrAlternativeTreeConstraint", None)
                if opp_val is None:
                    setattr(value, "myDsl_OrAlternativeTreeConstraint", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_Feature23(self):
        return self.__myDsl_Feature23

    @myDsl_Feature23.setter
    def myDsl_Feature23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Feature__myDsl_Feature23", None)
        self.__myDsl_Feature23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_CrossTreeConstraint22"):
                opp_val = getattr(old_value, "myDsl_CrossTreeConstraint22", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_CrossTreeConstraint22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_CrossTreeConstraint22"):
                opp_val = getattr(value, "myDsl_CrossTreeConstraint22", None)
                setattr(value, "myDsl_CrossTreeConstraint22", self)

    @property
    def myDsl_Feature20(self):
        return self.__myDsl_Feature20

    @myDsl_Feature20.setter
    def myDsl_Feature20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Feature__myDsl_Feature20", None)
        self.__myDsl_Feature20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_CrossTreeConstraint19"):
                opp_val = getattr(old_value, "myDsl_CrossTreeConstraint19", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_CrossTreeConstraint19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_CrossTreeConstraint19"):
                opp_val = getattr(value, "myDsl_CrossTreeConstraint19", None)
                setattr(value, "myDsl_CrossTreeConstraint19", self)

    @property
    def myDsl_Feature(self):
        return self.__myDsl_Feature

    @myDsl_Feature.setter
    def myDsl_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Feature__myDsl_Feature", None)
        self.__myDsl_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_FM"):
                opp_val = getattr(old_value, "myDsl_FM", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_FM"):
                opp_val = getattr(value, "myDsl_FM", None)
                if opp_val is None:
                    setattr(value, "myDsl_FM", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myDsl_FM:

    pass