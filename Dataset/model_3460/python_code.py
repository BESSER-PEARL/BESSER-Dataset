from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Operator:

    pass
class fm_OrOperator(Operator):

    pass
class fm_AndOperator(Operator):

    pass
class fm_Operator:

    pass
class fm_Operation:

    def __init__(self, value: int, fm_Operation21: "fm_Feature" = None, fm_Operation: "fm_CardExConstraint" = None, fm_Operation17: "fm_CardExConstraint" = None):
        self.value = value
        self.fm_Operation21 = fm_Operation21
        self.fm_Operation = fm_Operation
        self.fm_Operation17 = fm_Operation17
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def fm_Operation21(self):
        return self.__fm_Operation21

    @fm_Operation21.setter
    def fm_Operation21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fm_Operation__fm_Operation21", None)
        self.__fm_Operation21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fm_Feature22"):
                opp_val = getattr(old_value, "fm_Feature22", None)
                if opp_val == self:
                    setattr(old_value, "fm_Feature22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fm_Feature22"):
                opp_val = getattr(value, "fm_Feature22", None)
                setattr(value, "fm_Feature22", self)

    @property
    def fm_Operation17(self):
        return self.__fm_Operation17

    @fm_Operation17.setter
    def fm_Operation17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fm_Operation__fm_Operation17", None)
        self.__fm_Operation17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fm_CardExConstraint16"):
                opp_val = getattr(old_value, "fm_CardExConstraint16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fm_CardExConstraint16"):
                opp_val = getattr(value, "fm_CardExConstraint16", None)
                if opp_val is None:
                    setattr(value, "fm_CardExConstraint16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fm_Operation(self):
        return self.__fm_Operation

    @fm_Operation.setter
    def fm_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fm_Operation__fm_Operation", None)
        self.__fm_Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fm_CardExConstraint"):
                opp_val = getattr(old_value, "fm_CardExConstraint", None)
                if opp_val == self:
                    setattr(old_value, "fm_CardExConstraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fm_CardExConstraint"):
                opp_val = getattr(value, "fm_CardExConstraint", None)
                setattr(value, "fm_CardExConstraint", self)

class fm_Cardinality:

    def __init__(self, max: int, min: int):
        self.max = max
        self.min = min
        
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

class OrFeature:

    pass
class fm_XorFeature(OrFeature):

    pass
class Feature:

    pass
class fm_OrFeature(Feature):

    pass
class Constraints:

    pass
class fm_BooleanConstraints(Constraints):

    pass
class fm_CardExConstraint(Constraints):

    pass
class Cardinality:

    pass
class fm_GroupCardinality(Cardinality):

    pass
class fm_Constraints:

    pass
class fm_Feature:

    def __init__(self, name: str, fm_Feature5: "fm_Feature" = None, fm_Feature3: set["fm_Feature"] = None, fm_Feature7: "fm_FeatureCardinality" = None, fm_Feature9: set["fm_Attribute"] = None, fm_Feature: "fm_FeatureModel" = None, fm_Feature11: "fm_OrFeature" = None, fm_Feature22: "fm_Operation" = None, fm_Feature24: "fm_BooleanConstraints" = None, fm_Feature27: "fm_BooleanConstraints" = None):
        self.name = name
        self.fm_Feature5 = fm_Feature5
        self.fm_Feature3 = fm_Feature3 if fm_Feature3 is not None else set()
        self.fm_Feature7 = fm_Feature7
        self.fm_Feature9 = fm_Feature9 if fm_Feature9 is not None else set()
        self.fm_Feature = fm_Feature
        self.fm_Feature11 = fm_Feature11
        self.fm_Feature22 = fm_Feature22
        self.fm_Feature24 = fm_Feature24
        self.fm_Feature27 = fm_Feature27
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fm_Feature5(self):
        return self.__fm_Feature5

    @fm_Feature5.setter
    def fm_Feature5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fm_Feature__fm_Feature5", None)
        self.__fm_Feature5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fm_Feature3"):
                opp_val = getattr(old_value, "fm_Feature3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fm_Feature3"):
                opp_val = getattr(value, "fm_Feature3", None)
                if opp_val is None:
                    setattr(value, "fm_Feature3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fm_Feature7(self):
        return self.__fm_Feature7

    @fm_Feature7.setter
    def fm_Feature7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fm_Feature__fm_Feature7", None)
        self.__fm_Feature7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fm_FeatureCardinality"):
                opp_val = getattr(old_value, "fm_FeatureCardinality", None)
                if opp_val == self:
                    setattr(old_value, "fm_FeatureCardinality", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fm_FeatureCardinality"):
                opp_val = getattr(value, "fm_FeatureCardinality", None)
                setattr(value, "fm_FeatureCardinality", self)

    @property
    def fm_Feature22(self):
        return self.__fm_Feature22

    @fm_Feature22.setter
    def fm_Feature22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fm_Feature__fm_Feature22", None)
        self.__fm_Feature22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fm_Operation21"):
                opp_val = getattr(old_value, "fm_Operation21", None)
                if opp_val == self:
                    setattr(old_value, "fm_Operation21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fm_Operation21"):
                opp_val = getattr(value, "fm_Operation21", None)
                setattr(value, "fm_Operation21", self)

    @property
    def fm_Feature27(self):
        return self.__fm_Feature27

    @fm_Feature27.setter
    def fm_Feature27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fm_Feature__fm_Feature27", None)
        self.__fm_Feature27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fm_BooleanConstraints26"):
                opp_val = getattr(old_value, "fm_BooleanConstraints26", None)
                if opp_val == self:
                    setattr(old_value, "fm_BooleanConstraints26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fm_BooleanConstraints26"):
                opp_val = getattr(value, "fm_BooleanConstraints26", None)
                setattr(value, "fm_BooleanConstraints26", self)

    @property
    def fm_Feature9(self):
        return self.__fm_Feature9

    @fm_Feature9.setter
    def fm_Feature9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fm_Feature__fm_Feature9", None)
        self.__fm_Feature9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fm_Attribute"):
                    opp_val = getattr(item, "fm_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "fm_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fm_Attribute"):
                    opp_val = getattr(item, "fm_Attribute", None)
                    
                    setattr(item, "fm_Attribute", self)
                    

    @property
    def fm_Feature(self):
        return self.__fm_Feature

    @fm_Feature.setter
    def fm_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fm_Feature__fm_Feature", None)
        self.__fm_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fm_FeatureModel"):
                opp_val = getattr(old_value, "fm_FeatureModel", None)
                if opp_val == self:
                    setattr(old_value, "fm_FeatureModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fm_FeatureModel"):
                opp_val = getattr(value, "fm_FeatureModel", None)
                setattr(value, "fm_FeatureModel", self)

    @property
    def fm_Feature24(self):
        return self.__fm_Feature24

    @fm_Feature24.setter
    def fm_Feature24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fm_Feature__fm_Feature24", None)
        self.__fm_Feature24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fm_BooleanConstraints"):
                opp_val = getattr(old_value, "fm_BooleanConstraints", None)
                if opp_val == self:
                    setattr(old_value, "fm_BooleanConstraints", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fm_BooleanConstraints"):
                opp_val = getattr(value, "fm_BooleanConstraints", None)
                setattr(value, "fm_BooleanConstraints", self)

    @property
    def fm_Feature11(self):
        return self.__fm_Feature11

    @fm_Feature11.setter
    def fm_Feature11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fm_Feature__fm_Feature11", None)
        self.__fm_Feature11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fm_OrFeature"):
                opp_val = getattr(old_value, "fm_OrFeature", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fm_OrFeature"):
                opp_val = getattr(value, "fm_OrFeature", None)
                if opp_val is None:
                    setattr(value, "fm_OrFeature", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fm_Feature3(self):
        return self.__fm_Feature3

    @fm_Feature3.setter
    def fm_Feature3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fm_Feature__fm_Feature3", None)
        self.__fm_Feature3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fm_Feature5"):
                    opp_val = getattr(item, "fm_Feature5", None)
                    
                    if opp_val == self:
                        setattr(item, "fm_Feature5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fm_Feature5"):
                    opp_val = getattr(item, "fm_Feature5", None)
                    
                    setattr(item, "fm_Feature5", self)
                    

class fm_FeatureModel:

    pass
class fm_Attribute:

    def __init__(self, name: str, value: str, fm_Attribute: "fm_Feature" = None):
        self.name = name
        self.value = value
        self.fm_Attribute = fm_Attribute
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fm_Attribute(self):
        return self.__fm_Attribute

    @fm_Attribute.setter
    def fm_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fm_Attribute__fm_Attribute", None)
        self.__fm_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fm_Feature9"):
                opp_val = getattr(old_value, "fm_Feature9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fm_Feature9"):
                opp_val = getattr(value, "fm_Feature9", None)
                if opp_val is None:
                    setattr(value, "fm_Feature9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class fm_FeatureCardinality(Cardinality):

    pass