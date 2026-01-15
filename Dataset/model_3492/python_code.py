from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Abstract_ATT_ID:

    pass
class vM_PairAttributeValue:

    def __init__(self, value: str, vM_PairAttributeValue132: "vM_TableBasedValuationByFeature" = None, vM_PairAttributeValue134: "vM_Abstract_ATT_ID" = None, vM_PairAttributeValue: "vM_TableBasedValuationByFeatureAndClone" = None):
        self.value = value
        self.vM_PairAttributeValue132 = vM_PairAttributeValue132
        self.vM_PairAttributeValue134 = vM_PairAttributeValue134
        self.vM_PairAttributeValue = vM_PairAttributeValue
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def vM_PairAttributeValue132(self):
        return self.__vM_PairAttributeValue132

    @vM_PairAttributeValue132.setter
    def vM_PairAttributeValue132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_PairAttributeValue__vM_PairAttributeValue132", None)
        self.__vM_PairAttributeValue132 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_TableBasedValuationByFeature131"):
                opp_val = getattr(old_value, "vM_TableBasedValuationByFeature131", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_TableBasedValuationByFeature131"):
                opp_val = getattr(value, "vM_TableBasedValuationByFeature131", None)
                if opp_val is None:
                    setattr(value, "vM_TableBasedValuationByFeature131", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def vM_PairAttributeValue(self):
        return self.__vM_PairAttributeValue

    @vM_PairAttributeValue.setter
    def vM_PairAttributeValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_PairAttributeValue__vM_PairAttributeValue", None)
        self.__vM_PairAttributeValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_TableBasedValuationByFeatureAndClone126"):
                opp_val = getattr(old_value, "vM_TableBasedValuationByFeatureAndClone126", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_TableBasedValuationByFeatureAndClone126"):
                opp_val = getattr(value, "vM_TableBasedValuationByFeatureAndClone126", None)
                if opp_val is None:
                    setattr(value, "vM_TableBasedValuationByFeatureAndClone126", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def vM_PairAttributeValue134(self):
        return self.__vM_PairAttributeValue134

    @vM_PairAttributeValue134.setter
    def vM_PairAttributeValue134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_PairAttributeValue__vM_PairAttributeValue134", None)
        self.__vM_PairAttributeValue134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_Abstract_ATT_ID135"):
                opp_val = getattr(old_value, "vM_Abstract_ATT_ID135", None)
                if opp_val == self:
                    setattr(old_value, "vM_Abstract_ATT_ID135", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_Abstract_ATT_ID135"):
                opp_val = getattr(value, "vM_Abstract_ATT_ID135", None)
                setattr(value, "vM_Abstract_ATT_ID135", self)

class vM_PairFeatureReal:

    def __init__(self, value: str, vM_PairFeatureReal: "vM_TableBasedValuationByAttributeForReal" = None, vM_PairFeatureReal148: "vM_Feature" = None):
        self.value = value
        self.vM_PairFeatureReal = vM_PairFeatureReal
        self.vM_PairFeatureReal148 = vM_PairFeatureReal148
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def vM_PairFeatureReal(self):
        return self.__vM_PairFeatureReal

    @vM_PairFeatureReal.setter
    def vM_PairFeatureReal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_PairFeatureReal__vM_PairFeatureReal", None)
        self.__vM_PairFeatureReal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_TableBasedValuationByAttributeForReal146"):
                opp_val = getattr(old_value, "vM_TableBasedValuationByAttributeForReal146", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_TableBasedValuationByAttributeForReal146"):
                opp_val = getattr(value, "vM_TableBasedValuationByAttributeForReal146", None)
                if opp_val is None:
                    setattr(value, "vM_TableBasedValuationByAttributeForReal146", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def vM_PairFeatureReal148(self):
        return self.__vM_PairFeatureReal148

    @vM_PairFeatureReal148.setter
    def vM_PairFeatureReal148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_PairFeatureReal__vM_PairFeatureReal148", None)
        self.__vM_PairFeatureReal148 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_Feature149"):
                opp_val = getattr(old_value, "vM_Feature149", None)
                if opp_val == self:
                    setattr(old_value, "vM_Feature149", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_Feature149"):
                opp_val = getattr(value, "vM_Feature149", None)
                setattr(value, "vM_Feature149", self)

class vM_PairFeatureInteger:

    def __init__(self, value: str, vM_PairFeatureInteger: "vM_TableBasedValuationByAttributeForInteger" = None, vM_PairFeatureInteger141: "vM_Feature" = None):
        self.value = value
        self.vM_PairFeatureInteger = vM_PairFeatureInteger
        self.vM_PairFeatureInteger141 = vM_PairFeatureInteger141
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def vM_PairFeatureInteger(self):
        return self.__vM_PairFeatureInteger

    @vM_PairFeatureInteger.setter
    def vM_PairFeatureInteger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_PairFeatureInteger__vM_PairFeatureInteger", None)
        self.__vM_PairFeatureInteger = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_TableBasedValuationByAttributeForInteger139"):
                opp_val = getattr(old_value, "vM_TableBasedValuationByAttributeForInteger139", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_TableBasedValuationByAttributeForInteger139"):
                opp_val = getattr(value, "vM_TableBasedValuationByAttributeForInteger139", None)
                if opp_val is None:
                    setattr(value, "vM_TableBasedValuationByAttributeForInteger139", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def vM_PairFeatureInteger141(self):
        return self.__vM_PairFeatureInteger141

    @vM_PairFeatureInteger141.setter
    def vM_PairFeatureInteger141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_PairFeatureInteger__vM_PairFeatureInteger141", None)
        self.__vM_PairFeatureInteger141 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_Feature142"):
                opp_val = getattr(old_value, "vM_Feature142", None)
                if opp_val == self:
                    setattr(old_value, "vM_Feature142", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_Feature142"):
                opp_val = getattr(value, "vM_Feature142", None)
                setattr(value, "vM_Feature142", self)

class TableBasedValuationByAttribute:

    pass
class vM_TableBasedValuationByAttributeForReal(TableBasedValuationByAttribute):

    pass
class vM_TableBasedValuationByAttributeForInteger(TableBasedValuationByAttribute):

    pass
class BasicAttrValuation:

    pass
class vM_RealAttrValuation(BasicAttrValuation):

    pass
class ExtendedValuation:

    pass
class vM_TableBasedValuationByFeatureAndClone:

    def __init__(self, name: str, vM_TableBasedValuationByFeatureAndClone: "vM_AdvancedAttrValuation" = None, vM_TableBasedValuationByFeatureAndClone123: "vM_Feature" = None, vM_TableBasedValuationByFeatureAndClone126: set["vM_PairAttributeValue"] = None):
        self.name = name
        self.vM_TableBasedValuationByFeatureAndClone = vM_TableBasedValuationByFeatureAndClone
        self.vM_TableBasedValuationByFeatureAndClone123 = vM_TableBasedValuationByFeatureAndClone123
        self.vM_TableBasedValuationByFeatureAndClone126 = vM_TableBasedValuationByFeatureAndClone126 if vM_TableBasedValuationByFeatureAndClone126 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def vM_TableBasedValuationByFeatureAndClone(self):
        return self.__vM_TableBasedValuationByFeatureAndClone

    @vM_TableBasedValuationByFeatureAndClone.setter
    def vM_TableBasedValuationByFeatureAndClone(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_TableBasedValuationByFeatureAndClone__vM_TableBasedValuationByFeatureAndClone", None)
        self.__vM_TableBasedValuationByFeatureAndClone = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_AdvancedAttrValuation121"):
                opp_val = getattr(old_value, "vM_AdvancedAttrValuation121", None)
                if opp_val == self:
                    setattr(old_value, "vM_AdvancedAttrValuation121", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_AdvancedAttrValuation121"):
                opp_val = getattr(value, "vM_AdvancedAttrValuation121", None)
                setattr(value, "vM_AdvancedAttrValuation121", self)

    @property
    def vM_TableBasedValuationByFeatureAndClone126(self):
        return self.__vM_TableBasedValuationByFeatureAndClone126

    @vM_TableBasedValuationByFeatureAndClone126.setter
    def vM_TableBasedValuationByFeatureAndClone126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_TableBasedValuationByFeatureAndClone__vM_TableBasedValuationByFeatureAndClone126", None)
        self.__vM_TableBasedValuationByFeatureAndClone126 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "vM_PairAttributeValue"):
                    opp_val = getattr(item, "vM_PairAttributeValue", None)
                    
                    if opp_val == self:
                        setattr(item, "vM_PairAttributeValue", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "vM_PairAttributeValue"):
                    opp_val = getattr(item, "vM_PairAttributeValue", None)
                    
                    setattr(item, "vM_PairAttributeValue", self)
                    

    @property
    def vM_TableBasedValuationByFeatureAndClone123(self):
        return self.__vM_TableBasedValuationByFeatureAndClone123

    @vM_TableBasedValuationByFeatureAndClone123.setter
    def vM_TableBasedValuationByFeatureAndClone123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_TableBasedValuationByFeatureAndClone__vM_TableBasedValuationByFeatureAndClone123", None)
        self.__vM_TableBasedValuationByFeatureAndClone123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_Feature124"):
                opp_val = getattr(old_value, "vM_Feature124", None)
                if opp_val == self:
                    setattr(old_value, "vM_Feature124", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_Feature124"):
                opp_val = getattr(value, "vM_Feature124", None)
                setattr(value, "vM_Feature124", self)

class vM_TableBasedValuationByAttribute:

    pass
class vM_TableBasedValuationByFeature:

    pass
class vM_AdvancedAttrValuation(ExtendedValuation):

    pass
class vM_StringAttrValuation(BasicAttrValuation):

    pass
class vM_BooleanAttrValuation(BasicAttrValuation):

    pass
class vM_IntegerAttrValuation(BasicAttrValuation):

    pass
class vM_Objective:

    def __init__(self, name: str, op: str, vM_Objective94: "vM_ObjectiveExpression" = None, vM_Objective: "vM_Objectives" = None):
        self.name = name
        self.op = op
        self.vM_Objective94 = vM_Objective94
        self.vM_Objective = vM_Objective
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def vM_Objective(self):
        return self.__vM_Objective

    @vM_Objective.setter
    def vM_Objective(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_Objective__vM_Objective", None)
        self.__vM_Objective = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_Objectives"):
                opp_val = getattr(old_value, "vM_Objectives", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_Objectives"):
                opp_val = getattr(value, "vM_Objectives", None)
                if opp_val is None:
                    setattr(value, "vM_Objectives", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def vM_Objective94(self):
        return self.__vM_Objective94

    @vM_Objective94.setter
    def vM_Objective94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_Objective__vM_Objective94", None)
        self.__vM_Objective94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_ObjectiveExpression"):
                opp_val = getattr(old_value, "vM_ObjectiveExpression", None)
                if opp_val == self:
                    setattr(old_value, "vM_ObjectiveExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_ObjectiveExpression"):
                opp_val = getattr(value, "vM_ObjectiveExpression", None)
                setattr(value, "vM_ObjectiveExpression", self)

class vM_ExtendedValuation:

    pass
class vM_BooleanValuation:

    def __init__(self, notSelected: bool, vM_BooleanValuation: "vM_Configuration" = None, vM_BooleanValuation104: "vM_Feature" = None):
        self.notSelected = notSelected
        self.vM_BooleanValuation = vM_BooleanValuation
        self.vM_BooleanValuation104 = vM_BooleanValuation104
        
    @property
    def notSelected(self) -> bool:
        return self.__notSelected

    @notSelected.setter
    def notSelected(self, notSelected: bool):
        self.__notSelected = notSelected

    @property
    def vM_BooleanValuation104(self):
        return self.__vM_BooleanValuation104

    @vM_BooleanValuation104.setter
    def vM_BooleanValuation104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_BooleanValuation__vM_BooleanValuation104", None)
        self.__vM_BooleanValuation104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_Feature105"):
                opp_val = getattr(old_value, "vM_Feature105", None)
                if opp_val == self:
                    setattr(old_value, "vM_Feature105", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_Feature105"):
                opp_val = getattr(value, "vM_Feature105", None)
                setattr(value, "vM_Feature105", self)

    @property
    def vM_BooleanValuation(self):
        return self.__vM_BooleanValuation

    @vM_BooleanValuation.setter
    def vM_BooleanValuation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_BooleanValuation__vM_BooleanValuation", None)
        self.__vM_BooleanValuation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_Configuration100"):
                opp_val = getattr(old_value, "vM_Configuration100", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_Configuration100"):
                opp_val = getattr(value, "vM_Configuration100", None)
                if opp_val is None:
                    setattr(value, "vM_Configuration100", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class vM_Configuration:

    def __init__(self, name: str, vM_Configuration: "vM_Configurations" = None, vM_Configuration100: set["vM_BooleanValuation"] = None, vM_Configuration102: set["vM_ExtendedValuation"] = None):
        self.name = name
        self.vM_Configuration = vM_Configuration
        self.vM_Configuration100 = vM_Configuration100 if vM_Configuration100 is not None else set()
        self.vM_Configuration102 = vM_Configuration102 if vM_Configuration102 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def vM_Configuration100(self):
        return self.__vM_Configuration100

    @vM_Configuration100.setter
    def vM_Configuration100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_Configuration__vM_Configuration100", None)
        self.__vM_Configuration100 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "vM_BooleanValuation"):
                    opp_val = getattr(item, "vM_BooleanValuation", None)
                    
                    if opp_val == self:
                        setattr(item, "vM_BooleanValuation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "vM_BooleanValuation"):
                    opp_val = getattr(item, "vM_BooleanValuation", None)
                    
                    setattr(item, "vM_BooleanValuation", self)
                    

    @property
    def vM_Configuration102(self):
        return self.__vM_Configuration102

    @vM_Configuration102.setter
    def vM_Configuration102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_Configuration__vM_Configuration102", None)
        self.__vM_Configuration102 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "vM_ExtendedValuation"):
                    opp_val = getattr(item, "vM_ExtendedValuation", None)
                    
                    if opp_val == self:
                        setattr(item, "vM_ExtendedValuation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "vM_ExtendedValuation"):
                    opp_val = getattr(item, "vM_ExtendedValuation", None)
                    
                    setattr(item, "vM_ExtendedValuation", self)
                    

    @property
    def vM_Configuration(self):
        return self.__vM_Configuration

    @vM_Configuration.setter
    def vM_Configuration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_Configuration__vM_Configuration", None)
        self.__vM_Configuration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_Configurations"):
                opp_val = getattr(old_value, "vM_Configurations", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_Configurations"):
                opp_val = getattr(value, "vM_Configurations", None)
                if opp_val is None:
                    setattr(value, "vM_Configurations", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class vM_ObjectiveExpression:

    def __init__(self, op: str, vM_ObjectiveExpression: "vM_Objective" = None, vM_ObjectiveExpression96: "vM_PrimitiveExpression" = None):
        self.op = op
        self.vM_ObjectiveExpression = vM_ObjectiveExpression
        self.vM_ObjectiveExpression96 = vM_ObjectiveExpression96
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def vM_ObjectiveExpression(self):
        return self.__vM_ObjectiveExpression

    @vM_ObjectiveExpression.setter
    def vM_ObjectiveExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_ObjectiveExpression__vM_ObjectiveExpression", None)
        self.__vM_ObjectiveExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_Objective94"):
                opp_val = getattr(old_value, "vM_Objective94", None)
                if opp_val == self:
                    setattr(old_value, "vM_Objective94", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_Objective94"):
                opp_val = getattr(value, "vM_Objective94", None)
                setattr(value, "vM_Objective94", self)

    @property
    def vM_ObjectiveExpression96(self):
        return self.__vM_ObjectiveExpression96

    @vM_ObjectiveExpression96.setter
    def vM_ObjectiveExpression96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_ObjectiveExpression__vM_ObjectiveExpression96", None)
        self.__vM_ObjectiveExpression96 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_PrimitiveExpression97"):
                opp_val = getattr(old_value, "vM_PrimitiveExpression97", None)
                if opp_val == self:
                    setattr(old_value, "vM_PrimitiveExpression97", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_PrimitiveExpression97"):
                opp_val = getattr(value, "vM_PrimitiveExpression97", None)
                setattr(value, "vM_PrimitiveExpression97", self)

class vM_BooleanExpression_List:

    pass
class vM_NumericExpression_List:

    pass
class ComplexExpression:

    pass
class vM_If(ComplexExpression):

    pass
class vM_BiImplication(ComplexExpression):

    pass
class vM_Lessequal(ComplexExpression):

    pass
class vM_Plus(ComplexExpression):

    pass
class vM_Less(ComplexExpression):

    pass
class vM_Minus(ComplexExpression):

    pass
class vM_Requires(ComplexExpression):

    pass
class vM_Greater(ComplexExpression):

    pass
class vM_Multiplication(ComplexExpression):

    pass
class vM_Division(ComplexExpression):

    pass
class vM_LeftImplication(ComplexExpression):

    pass
class vM_Greaterequal(ComplexExpression):

    pass
class vM_RightImplication(ComplexExpression):

    pass
class vM_Inequality(ComplexExpression):

    pass
class vM_Excludes(ComplexExpression):

    pass
class vM_Equality(ComplexExpression):

    pass
class vM_And(ComplexExpression):

    pass
class vM_Or(ComplexExpression):

    pass
class vM_Expression(ComplexExpression):

    pass
class vM_ComplexExpression:

    pass
class vM_AttHead:

    def __init__(self, forAllFeatures: bool, vM_AttHead: "vM_PrimitiveExpression" = None, vM_AttHead108: "vM_BasicAttrValuation" = None, vM_AttHead151: "vM_Feature" = None, vM_AttHead155: "vM_Abstract_ATT_ID" = None):
        self.forAllFeatures = forAllFeatures
        self.vM_AttHead = vM_AttHead
        self.vM_AttHead108 = vM_AttHead108
        self.vM_AttHead151 = vM_AttHead151
        self.vM_AttHead155 = vM_AttHead155
        
    @property
    def forAllFeatures(self) -> bool:
        return self.__forAllFeatures

    @forAllFeatures.setter
    def forAllFeatures(self, forAllFeatures: bool):
        self.__forAllFeatures = forAllFeatures

    @property
    def vM_AttHead108(self):
        return self.__vM_AttHead108

    @vM_AttHead108.setter
    def vM_AttHead108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_AttHead__vM_AttHead108", None)
        self.__vM_AttHead108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_BasicAttrValuation107"):
                opp_val = getattr(old_value, "vM_BasicAttrValuation107", None)
                if opp_val == self:
                    setattr(old_value, "vM_BasicAttrValuation107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_BasicAttrValuation107"):
                opp_val = getattr(value, "vM_BasicAttrValuation107", None)
                setattr(value, "vM_BasicAttrValuation107", self)

    @property
    def vM_AttHead155(self):
        return self.__vM_AttHead155

    @vM_AttHead155.setter
    def vM_AttHead155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_AttHead__vM_AttHead155", None)
        self.__vM_AttHead155 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_Abstract_ATT_ID154"):
                opp_val = getattr(old_value, "vM_Abstract_ATT_ID154", None)
                if opp_val == self:
                    setattr(old_value, "vM_Abstract_ATT_ID154", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_Abstract_ATT_ID154"):
                opp_val = getattr(value, "vM_Abstract_ATT_ID154", None)
                setattr(value, "vM_Abstract_ATT_ID154", self)

    @property
    def vM_AttHead(self):
        return self.__vM_AttHead

    @vM_AttHead.setter
    def vM_AttHead(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_AttHead__vM_AttHead", None)
        self.__vM_AttHead = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_PrimitiveExpression72"):
                opp_val = getattr(old_value, "vM_PrimitiveExpression72", None)
                if opp_val == self:
                    setattr(old_value, "vM_PrimitiveExpression72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_PrimitiveExpression72"):
                opp_val = getattr(value, "vM_PrimitiveExpression72", None)
                setattr(value, "vM_PrimitiveExpression72", self)

    @property
    def vM_AttHead151(self):
        return self.__vM_AttHead151

    @vM_AttHead151.setter
    def vM_AttHead151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_AttHead__vM_AttHead151", None)
        self.__vM_AttHead151 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_Feature152"):
                opp_val = getattr(old_value, "vM_Feature152", None)
                if opp_val == self:
                    setattr(old_value, "vM_Feature152", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_Feature152"):
                opp_val = getattr(value, "vM_Feature152", None)
                setattr(value, "vM_Feature152", self)

class Expression:

    pass
class vM_BrackedExpression(Expression):

    pass
class vM_StringExpression(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class vM_BooleanExpression(Expression):

    def __init__(self, value: str, op: str, vM_BooleanExpression91: "vM_BooleanExpression_List" = None, vM_BooleanExpression: "vM_BooleanExpression" = None, vM_BooleanExpression76: "vM_BooleanExpression" = None, vM_BooleanExpression79: "vM_BooleanExpression_List" = None):
        self.value = value
        self.op = op
        self.vM_BooleanExpression91 = vM_BooleanExpression91
        self.vM_BooleanExpression = vM_BooleanExpression
        self.vM_BooleanExpression76 = vM_BooleanExpression76
        self.vM_BooleanExpression79 = vM_BooleanExpression79
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def vM_BooleanExpression76(self):
        return self.__vM_BooleanExpression76

    @vM_BooleanExpression76.setter
    def vM_BooleanExpression76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_BooleanExpression__vM_BooleanExpression76", None)
        self.__vM_BooleanExpression76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_BooleanExpression"):
                opp_val = getattr(old_value, "vM_BooleanExpression", None)
                if opp_val == self:
                    setattr(old_value, "vM_BooleanExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_BooleanExpression"):
                opp_val = getattr(value, "vM_BooleanExpression", None)
                setattr(value, "vM_BooleanExpression", self)

    @property
    def vM_BooleanExpression(self):
        return self.__vM_BooleanExpression

    @vM_BooleanExpression.setter
    def vM_BooleanExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_BooleanExpression__vM_BooleanExpression", None)
        self.__vM_BooleanExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_BooleanExpression76"):
                opp_val = getattr(old_value, "vM_BooleanExpression76", None)
                if opp_val == self:
                    setattr(old_value, "vM_BooleanExpression76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_BooleanExpression76"):
                opp_val = getattr(value, "vM_BooleanExpression76", None)
                setattr(value, "vM_BooleanExpression76", self)

    @property
    def vM_BooleanExpression79(self):
        return self.__vM_BooleanExpression79

    @vM_BooleanExpression79.setter
    def vM_BooleanExpression79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_BooleanExpression__vM_BooleanExpression79", None)
        self.__vM_BooleanExpression79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_BooleanExpression_List"):
                opp_val = getattr(old_value, "vM_BooleanExpression_List", None)
                if opp_val == self:
                    setattr(old_value, "vM_BooleanExpression_List", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_BooleanExpression_List"):
                opp_val = getattr(value, "vM_BooleanExpression_List", None)
                setattr(value, "vM_BooleanExpression_List", self)

    @property
    def vM_BooleanExpression91(self):
        return self.__vM_BooleanExpression91

    @vM_BooleanExpression91.setter
    def vM_BooleanExpression91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_BooleanExpression__vM_BooleanExpression91", None)
        self.__vM_BooleanExpression91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_BooleanExpression_List90"):
                opp_val = getattr(old_value, "vM_BooleanExpression_List90", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_BooleanExpression_List90"):
                opp_val = getattr(value, "vM_BooleanExpression_List90", None)
                if opp_val is None:
                    setattr(value, "vM_BooleanExpression_List90", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class vM_NumericExpression(Expression):

    def __init__(self, value: str, op: str, vM_NumericExpression: "vM_NumericExpression" = None, vM_NumericExpression82: "vM_NumericExpression" = None, vM_NumericExpression85: "vM_NumericExpression_List" = None, vM_NumericExpression88: "vM_NumericExpression_List" = None):
        self.value = value
        self.op = op
        self.vM_NumericExpression = vM_NumericExpression
        self.vM_NumericExpression82 = vM_NumericExpression82
        self.vM_NumericExpression85 = vM_NumericExpression85
        self.vM_NumericExpression88 = vM_NumericExpression88
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def vM_NumericExpression(self):
        return self.__vM_NumericExpression

    @vM_NumericExpression.setter
    def vM_NumericExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_NumericExpression__vM_NumericExpression", None)
        self.__vM_NumericExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_NumericExpression82"):
                opp_val = getattr(old_value, "vM_NumericExpression82", None)
                if opp_val == self:
                    setattr(old_value, "vM_NumericExpression82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_NumericExpression82"):
                opp_val = getattr(value, "vM_NumericExpression82", None)
                setattr(value, "vM_NumericExpression82", self)

    @property
    def vM_NumericExpression82(self):
        return self.__vM_NumericExpression82

    @vM_NumericExpression82.setter
    def vM_NumericExpression82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_NumericExpression__vM_NumericExpression82", None)
        self.__vM_NumericExpression82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_NumericExpression"):
                opp_val = getattr(old_value, "vM_NumericExpression", None)
                if opp_val == self:
                    setattr(old_value, "vM_NumericExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_NumericExpression"):
                opp_val = getattr(value, "vM_NumericExpression", None)
                setattr(value, "vM_NumericExpression", self)

    @property
    def vM_NumericExpression88(self):
        return self.__vM_NumericExpression88

    @vM_NumericExpression88.setter
    def vM_NumericExpression88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_NumericExpression__vM_NumericExpression88", None)
        self.__vM_NumericExpression88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_NumericExpression_List87"):
                opp_val = getattr(old_value, "vM_NumericExpression_List87", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_NumericExpression_List87"):
                opp_val = getattr(value, "vM_NumericExpression_List87", None)
                if opp_val is None:
                    setattr(value, "vM_NumericExpression_List87", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def vM_NumericExpression85(self):
        return self.__vM_NumericExpression85

    @vM_NumericExpression85.setter
    def vM_NumericExpression85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_NumericExpression__vM_NumericExpression85", None)
        self.__vM_NumericExpression85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_NumericExpression_List"):
                opp_val = getattr(old_value, "vM_NumericExpression_List", None)
                if opp_val == self:
                    setattr(old_value, "vM_NumericExpression_List", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_NumericExpression_List"):
                opp_val = getattr(value, "vM_NumericExpression_List", None)
                setattr(value, "vM_NumericExpression_List", self)

class vM_PrimitiveExpression(Expression):

    pass
class vM_SpecialExpression(Expression):

    def __init__(self, op: str, vM_SpecialExpression: "vM_Feature" = None):
        self.op = op
        self.vM_SpecialExpression = vM_SpecialExpression
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def vM_SpecialExpression(self):
        return self.__vM_SpecialExpression

    @vM_SpecialExpression.setter
    def vM_SpecialExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_SpecialExpression__vM_SpecialExpression", None)
        self.__vM_SpecialExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_Feature68"):
                opp_val = getattr(old_value, "vM_Feature68", None)
                if opp_val == self:
                    setattr(old_value, "vM_Feature68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_Feature68"):
                opp_val = getattr(value, "vM_Feature68", None)
                setattr(value, "vM_Feature68", self)

class vM_Constraint:

    def __init__(self, name: str, vM_Constraint: "vM_Constraints" = None, vM_Constraint66: "vM_ComplexExpression" = None):
        self.name = name
        self.vM_Constraint = vM_Constraint
        self.vM_Constraint66 = vM_Constraint66
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def vM_Constraint66(self):
        return self.__vM_Constraint66

    @vM_Constraint66.setter
    def vM_Constraint66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_Constraint__vM_Constraint66", None)
        self.__vM_Constraint66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_ComplexExpression"):
                opp_val = getattr(old_value, "vM_ComplexExpression", None)
                if opp_val == self:
                    setattr(old_value, "vM_ComplexExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_ComplexExpression"):
                opp_val = getattr(value, "vM_ComplexExpression", None)
                setattr(value, "vM_ComplexExpression", self)

    @property
    def vM_Constraint(self):
        return self.__vM_Constraint

    @vM_Constraint.setter
    def vM_Constraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_Constraint__vM_Constraint", None)
        self.__vM_Constraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_Constraints"):
                opp_val = getattr(old_value, "vM_Constraints", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_Constraints"):
                opp_val = getattr(value, "vM_Constraints", None)
                if opp_val is None:
                    setattr(value, "vM_Constraints", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class vM_Abstract_ATT_ID:

    def __init__(self, name: str, vM_Abstract_ATT_ID: "vM_AttributeDescription" = None, vM_Abstract_ATT_ID75: "vM_PrimitiveExpression" = None, vM_Abstract_ATT_ID135: "vM_PairAttributeValue" = None, vM_Abstract_ATT_ID154: "vM_AttHead" = None):
        self.name = name
        self.vM_Abstract_ATT_ID = vM_Abstract_ATT_ID
        self.vM_Abstract_ATT_ID75 = vM_Abstract_ATT_ID75
        self.vM_Abstract_ATT_ID135 = vM_Abstract_ATT_ID135
        self.vM_Abstract_ATT_ID154 = vM_Abstract_ATT_ID154
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def vM_Abstract_ATT_ID154(self):
        return self.__vM_Abstract_ATT_ID154

    @vM_Abstract_ATT_ID154.setter
    def vM_Abstract_ATT_ID154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_Abstract_ATT_ID__vM_Abstract_ATT_ID154", None)
        self.__vM_Abstract_ATT_ID154 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_AttHead155"):
                opp_val = getattr(old_value, "vM_AttHead155", None)
                if opp_val == self:
                    setattr(old_value, "vM_AttHead155", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_AttHead155"):
                opp_val = getattr(value, "vM_AttHead155", None)
                setattr(value, "vM_AttHead155", self)

    @property
    def vM_Abstract_ATT_ID135(self):
        return self.__vM_Abstract_ATT_ID135

    @vM_Abstract_ATT_ID135.setter
    def vM_Abstract_ATT_ID135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_Abstract_ATT_ID__vM_Abstract_ATT_ID135", None)
        self.__vM_Abstract_ATT_ID135 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_PairAttributeValue134"):
                opp_val = getattr(old_value, "vM_PairAttributeValue134", None)
                if opp_val == self:
                    setattr(old_value, "vM_PairAttributeValue134", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_PairAttributeValue134"):
                opp_val = getattr(value, "vM_PairAttributeValue134", None)
                setattr(value, "vM_PairAttributeValue134", self)

    @property
    def vM_Abstract_ATT_ID(self):
        return self.__vM_Abstract_ATT_ID

    @vM_Abstract_ATT_ID.setter
    def vM_Abstract_ATT_ID(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_Abstract_ATT_ID__vM_Abstract_ATT_ID", None)
        self.__vM_Abstract_ATT_ID = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_AttributeDescription63"):
                opp_val = getattr(old_value, "vM_AttributeDescription63", None)
                if opp_val == self:
                    setattr(old_value, "vM_AttributeDescription63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_AttributeDescription63"):
                opp_val = getattr(value, "vM_AttributeDescription63", None)
                setattr(value, "vM_AttributeDescription63", self)

    @property
    def vM_Abstract_ATT_ID75(self):
        return self.__vM_Abstract_ATT_ID75

    @vM_Abstract_ATT_ID75.setter
    def vM_Abstract_ATT_ID75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_Abstract_ATT_ID__vM_Abstract_ATT_ID75", None)
        self.__vM_Abstract_ATT_ID75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_PrimitiveExpression74"):
                opp_val = getattr(old_value, "vM_PrimitiveExpression74", None)
                if opp_val == self:
                    setattr(old_value, "vM_PrimitiveExpression74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_PrimitiveExpression74"):
                opp_val = getattr(value, "vM_PrimitiveExpression74", None)
                setattr(value, "vM_PrimitiveExpression74", self)

class vM_AttributeDescription:

    def __init__(self, description: str, vM_AttributeDescription: "vM_Descriptions" = None, vM_AttributeDescription60: "vM_Feature" = None, vM_AttributeDescription63: "vM_Abstract_ATT_ID" = None):
        self.description = description
        self.vM_AttributeDescription = vM_AttributeDescription
        self.vM_AttributeDescription60 = vM_AttributeDescription60
        self.vM_AttributeDescription63 = vM_AttributeDescription63
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def vM_AttributeDescription(self):
        return self.__vM_AttributeDescription

    @vM_AttributeDescription.setter
    def vM_AttributeDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_AttributeDescription__vM_AttributeDescription", None)
        self.__vM_AttributeDescription = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_Descriptions55"):
                opp_val = getattr(old_value, "vM_Descriptions55", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_Descriptions55"):
                opp_val = getattr(value, "vM_Descriptions55", None)
                if opp_val is None:
                    setattr(value, "vM_Descriptions55", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def vM_AttributeDescription63(self):
        return self.__vM_AttributeDescription63

    @vM_AttributeDescription63.setter
    def vM_AttributeDescription63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_AttributeDescription__vM_AttributeDescription63", None)
        self.__vM_AttributeDescription63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_Abstract_ATT_ID"):
                opp_val = getattr(old_value, "vM_Abstract_ATT_ID", None)
                if opp_val == self:
                    setattr(old_value, "vM_Abstract_ATT_ID", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_Abstract_ATT_ID"):
                opp_val = getattr(value, "vM_Abstract_ATT_ID", None)
                setattr(value, "vM_Abstract_ATT_ID", self)

    @property
    def vM_AttributeDescription60(self):
        return self.__vM_AttributeDescription60

    @vM_AttributeDescription60.setter
    def vM_AttributeDescription60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_AttributeDescription__vM_AttributeDescription60", None)
        self.__vM_AttributeDescription60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_Feature61"):
                opp_val = getattr(old_value, "vM_Feature61", None)
                if opp_val == self:
                    setattr(old_value, "vM_Feature61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_Feature61"):
                opp_val = getattr(value, "vM_Feature61", None)
                setattr(value, "vM_Feature61", self)

class vM_FeatureDescription:

    def __init__(self, description: str, vM_FeatureDescription: "vM_Descriptions" = None, vM_FeatureDescription57: "vM_Feature" = None):
        self.description = description
        self.vM_FeatureDescription = vM_FeatureDescription
        self.vM_FeatureDescription57 = vM_FeatureDescription57
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def vM_FeatureDescription57(self):
        return self.__vM_FeatureDescription57

    @vM_FeatureDescription57.setter
    def vM_FeatureDescription57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_FeatureDescription__vM_FeatureDescription57", None)
        self.__vM_FeatureDescription57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_Feature58"):
                opp_val = getattr(old_value, "vM_Feature58", None)
                if opp_val == self:
                    setattr(old_value, "vM_Feature58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_Feature58"):
                opp_val = getattr(value, "vM_Feature58", None)
                setattr(value, "vM_Feature58", self)

    @property
    def vM_FeatureDescription(self):
        return self.__vM_FeatureDescription

    @vM_FeatureDescription.setter
    def vM_FeatureDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_FeatureDescription__vM_FeatureDescription", None)
        self.__vM_FeatureDescription = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_Descriptions"):
                opp_val = getattr(old_value, "vM_Descriptions", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_Descriptions"):
                opp_val = getattr(value, "vM_Descriptions", None)
                if opp_val is None:
                    setattr(value, "vM_Descriptions", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class vM_IntegerDeltaDef:

    def __init__(self, value: int, vM_IntegerDeltaDef: "vM_IntegerAttrDefComplement" = None):
        self.value = value
        self.vM_IntegerDeltaDef = vM_IntegerDeltaDef
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def vM_IntegerDeltaDef(self):
        return self.__vM_IntegerDeltaDef

    @vM_IntegerDeltaDef.setter
    def vM_IntegerDeltaDef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_IntegerDeltaDef__vM_IntegerDeltaDef", None)
        self.__vM_IntegerDeltaDef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_IntegerAttrDefComplement34"):
                opp_val = getattr(old_value, "vM_IntegerAttrDefComplement34", None)
                if opp_val == self:
                    setattr(old_value, "vM_IntegerAttrDefComplement34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_IntegerAttrDefComplement34"):
                opp_val = getattr(value, "vM_IntegerAttrDefComplement34", None)
                setattr(value, "vM_IntegerAttrDefComplement34", self)

class vM_IntegerAttrDefComplement:

    def __init__(self, min: str, max: str, vM_IntegerAttrDefComplement: "vM_IntegerAttrDefBounded" = None, vM_IntegerAttrDefComplement32: "vM_IntegerAttrDefBounded" = None, vM_IntegerAttrDefComplement34: "vM_IntegerDeltaDef" = None):
        self.min = min
        self.max = max
        self.vM_IntegerAttrDefComplement = vM_IntegerAttrDefComplement
        self.vM_IntegerAttrDefComplement32 = vM_IntegerAttrDefComplement32
        self.vM_IntegerAttrDefComplement34 = vM_IntegerAttrDefComplement34
        
    @property
    def min(self) -> str:
        return self.__min

    @min.setter
    def min(self, min: str):
        self.__min = min

    @property
    def max(self) -> str:
        return self.__max

    @max.setter
    def max(self, max: str):
        self.__max = max

    @property
    def vM_IntegerAttrDefComplement(self):
        return self.__vM_IntegerAttrDefComplement

    @vM_IntegerAttrDefComplement.setter
    def vM_IntegerAttrDefComplement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_IntegerAttrDefComplement__vM_IntegerAttrDefComplement", None)
        self.__vM_IntegerAttrDefComplement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_IntegerAttrDefBounded"):
                opp_val = getattr(old_value, "vM_IntegerAttrDefBounded", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_IntegerAttrDefBounded"):
                opp_val = getattr(value, "vM_IntegerAttrDefBounded", None)
                if opp_val is None:
                    setattr(value, "vM_IntegerAttrDefBounded", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def vM_IntegerAttrDefComplement34(self):
        return self.__vM_IntegerAttrDefComplement34

    @vM_IntegerAttrDefComplement34.setter
    def vM_IntegerAttrDefComplement34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_IntegerAttrDefComplement__vM_IntegerAttrDefComplement34", None)
        self.__vM_IntegerAttrDefComplement34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_IntegerDeltaDef"):
                opp_val = getattr(old_value, "vM_IntegerDeltaDef", None)
                if opp_val == self:
                    setattr(old_value, "vM_IntegerDeltaDef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_IntegerDeltaDef"):
                opp_val = getattr(value, "vM_IntegerDeltaDef", None)
                setattr(value, "vM_IntegerDeltaDef", self)

    @property
    def vM_IntegerAttrDefComplement32(self):
        return self.__vM_IntegerAttrDefComplement32

    @vM_IntegerAttrDefComplement32.setter
    def vM_IntegerAttrDefComplement32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_IntegerAttrDefComplement__vM_IntegerAttrDefComplement32", None)
        self.__vM_IntegerAttrDefComplement32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_IntegerAttrDefBounded31"):
                opp_val = getattr(old_value, "vM_IntegerAttrDefBounded31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_IntegerAttrDefBounded31"):
                opp_val = getattr(value, "vM_IntegerAttrDefBounded31", None)
                if opp_val is None:
                    setattr(value, "vM_IntegerAttrDefBounded31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class IntegerAttrDef:

    pass
class vM_IntegerAttrDefBounded(IntegerAttrDef):

    pass
class vM_IntegerDefaultDef:

    def __init__(self, value: int, vM_IntegerDefaultDef48: "vM_EnumIntegerDef" = None, vM_IntegerDefaultDef: "vM_IntegerAttrDef" = None):
        self.value = value
        self.vM_IntegerDefaultDef48 = vM_IntegerDefaultDef48
        self.vM_IntegerDefaultDef = vM_IntegerDefaultDef
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def vM_IntegerDefaultDef48(self):
        return self.__vM_IntegerDefaultDef48

    @vM_IntegerDefaultDef48.setter
    def vM_IntegerDefaultDef48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_IntegerDefaultDef__vM_IntegerDefaultDef48", None)
        self.__vM_IntegerDefaultDef48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_EnumIntegerDef47"):
                opp_val = getattr(old_value, "vM_EnumIntegerDef47", None)
                if opp_val == self:
                    setattr(old_value, "vM_EnumIntegerDef47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_EnumIntegerDef47"):
                opp_val = getattr(value, "vM_EnumIntegerDef47", None)
                setattr(value, "vM_EnumIntegerDef47", self)

    @property
    def vM_IntegerDefaultDef(self):
        return self.__vM_IntegerDefaultDef

    @vM_IntegerDefaultDef.setter
    def vM_IntegerDefaultDef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_IntegerDefaultDef__vM_IntegerDefaultDef", None)
        self.__vM_IntegerDefaultDef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_IntegerAttrDef28"):
                opp_val = getattr(old_value, "vM_IntegerAttrDef28", None)
                if opp_val == self:
                    setattr(old_value, "vM_IntegerAttrDef28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_IntegerAttrDef28"):
                opp_val = getattr(value, "vM_IntegerAttrDef28", None)
                setattr(value, "vM_IntegerAttrDef28", self)

class vM_Enum_Real_ATT_ID(Abstract_ATT_ID):

    pass
class vM_Enum_Integer_ATT_ID(Abstract_ATT_ID):

    pass
class vM_Enum_String_ATT_ID(Abstract_ATT_ID):

    pass
class EnumAttrDef:

    pass
class vM_EnumIntegerDef(EnumAttrDef):

    pass
class vM_EnumRealDef(EnumAttrDef):

    pass
class vM_EnumStringDef(EnumAttrDef):

    pass
class vM_RealDeltaDef:

    def __init__(self, value: str, vM_RealDeltaDef: "vM_RealAttrDefComplement" = None):
        self.value = value
        self.vM_RealDeltaDef = vM_RealDeltaDef
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def vM_RealDeltaDef(self):
        return self.__vM_RealDeltaDef

    @vM_RealDeltaDef.setter
    def vM_RealDeltaDef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_RealDeltaDef__vM_RealDeltaDef", None)
        self.__vM_RealDeltaDef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_RealAttrDefComplement40"):
                opp_val = getattr(old_value, "vM_RealAttrDefComplement40", None)
                if opp_val == self:
                    setattr(old_value, "vM_RealAttrDefComplement40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_RealAttrDefComplement40"):
                opp_val = getattr(value, "vM_RealAttrDefComplement40", None)
                setattr(value, "vM_RealAttrDefComplement40", self)

class vM_RealAttrDefComplement:

    def __init__(self, min: str, max: str, vM_RealAttrDefComplement: "vM_RealAttrDefBounded" = None, vM_RealAttrDefComplement40: "vM_RealDeltaDef" = None):
        self.min = min
        self.max = max
        self.vM_RealAttrDefComplement = vM_RealAttrDefComplement
        self.vM_RealAttrDefComplement40 = vM_RealAttrDefComplement40
        
    @property
    def min(self) -> str:
        return self.__min

    @min.setter
    def min(self, min: str):
        self.__min = min

    @property
    def max(self) -> str:
        return self.__max

    @max.setter
    def max(self, max: str):
        self.__max = max

    @property
    def vM_RealAttrDefComplement40(self):
        return self.__vM_RealAttrDefComplement40

    @vM_RealAttrDefComplement40.setter
    def vM_RealAttrDefComplement40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_RealAttrDefComplement__vM_RealAttrDefComplement40", None)
        self.__vM_RealAttrDefComplement40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_RealDeltaDef"):
                opp_val = getattr(old_value, "vM_RealDeltaDef", None)
                if opp_val == self:
                    setattr(old_value, "vM_RealDeltaDef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_RealDeltaDef"):
                opp_val = getattr(value, "vM_RealDeltaDef", None)
                setattr(value, "vM_RealDeltaDef", self)

    @property
    def vM_RealAttrDefComplement(self):
        return self.__vM_RealAttrDefComplement

    @vM_RealAttrDefComplement.setter
    def vM_RealAttrDefComplement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_RealAttrDefComplement__vM_RealAttrDefComplement", None)
        self.__vM_RealAttrDefComplement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_RealAttrDefBounded"):
                opp_val = getattr(old_value, "vM_RealAttrDefBounded", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_RealAttrDefBounded"):
                opp_val = getattr(value, "vM_RealAttrDefBounded", None)
                if opp_val is None:
                    setattr(value, "vM_RealAttrDefBounded", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class RealAttrDef:

    pass
class vM_RealAttrDefUnbounded(RealAttrDef):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class vM_RealAttrDefBounded(RealAttrDef):

    pass
class vM_RealDefaultDef:

    def __init__(self, value: str, vM_RealDefaultDef: "vM_RealAttrDef" = None, vM_RealDefaultDef52: "vM_EnumRealDef" = None):
        self.value = value
        self.vM_RealDefaultDef = vM_RealDefaultDef
        self.vM_RealDefaultDef52 = vM_RealDefaultDef52
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def vM_RealDefaultDef(self):
        return self.__vM_RealDefaultDef

    @vM_RealDefaultDef.setter
    def vM_RealDefaultDef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_RealDefaultDef__vM_RealDefaultDef", None)
        self.__vM_RealDefaultDef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_RealAttrDef37"):
                opp_val = getattr(old_value, "vM_RealAttrDef37", None)
                if opp_val == self:
                    setattr(old_value, "vM_RealAttrDef37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_RealAttrDef37"):
                opp_val = getattr(value, "vM_RealAttrDef37", None)
                setattr(value, "vM_RealAttrDef37", self)

    @property
    def vM_RealDefaultDef52(self):
        return self.__vM_RealDefaultDef52

    @vM_RealDefaultDef52.setter
    def vM_RealDefaultDef52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_RealDefaultDef__vM_RealDefaultDef52", None)
        self.__vM_RealDefaultDef52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_EnumRealDef51"):
                opp_val = getattr(old_value, "vM_EnumRealDef51", None)
                if opp_val == self:
                    setattr(old_value, "vM_EnumRealDef51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_EnumRealDef51"):
                opp_val = getattr(value, "vM_EnumRealDef51", None)
                setattr(value, "vM_EnumRealDef51", self)

class vM_Real_ATT_ID(Abstract_ATT_ID):

    pass
class vM_IntegerAttrDefUnbounded(IntegerAttrDef):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class vM_AttrDef:

    def __init__(self, notTranslatable: bool, runTime: bool, notDecidable: bool, vM_AttrDef17: "vM_BasicAttrDef" = None, vM_AttrDef19: "vM_EnumAttrDef" = None, vM_AttrDef: "vM_Attributes" = None):
        self.notTranslatable = notTranslatable
        self.runTime = runTime
        self.notDecidable = notDecidable
        self.vM_AttrDef17 = vM_AttrDef17
        self.vM_AttrDef19 = vM_AttrDef19
        self.vM_AttrDef = vM_AttrDef
        
    @property
    def runTime(self) -> bool:
        return self.__runTime

    @runTime.setter
    def runTime(self, runTime: bool):
        self.__runTime = runTime

    @property
    def notDecidable(self) -> bool:
        return self.__notDecidable

    @notDecidable.setter
    def notDecidable(self, notDecidable: bool):
        self.__notDecidable = notDecidable

    @property
    def notTranslatable(self) -> bool:
        return self.__notTranslatable

    @notTranslatable.setter
    def notTranslatable(self, notTranslatable: bool):
        self.__notTranslatable = notTranslatable

    @property
    def vM_AttrDef19(self):
        return self.__vM_AttrDef19

    @vM_AttrDef19.setter
    def vM_AttrDef19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_AttrDef__vM_AttrDef19", None)
        self.__vM_AttrDef19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_EnumAttrDef"):
                opp_val = getattr(old_value, "vM_EnumAttrDef", None)
                if opp_val == self:
                    setattr(old_value, "vM_EnumAttrDef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_EnumAttrDef"):
                opp_val = getattr(value, "vM_EnumAttrDef", None)
                setattr(value, "vM_EnumAttrDef", self)

    @property
    def vM_AttrDef(self):
        return self.__vM_AttrDef

    @vM_AttrDef.setter
    def vM_AttrDef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_AttrDef__vM_AttrDef", None)
        self.__vM_AttrDef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_Attributes"):
                opp_val = getattr(old_value, "vM_Attributes", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_Attributes"):
                opp_val = getattr(value, "vM_Attributes", None)
                if opp_val is None:
                    setattr(value, "vM_Attributes", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def vM_AttrDef17(self):
        return self.__vM_AttrDef17

    @vM_AttrDef17.setter
    def vM_AttrDef17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_AttrDef__vM_AttrDef17", None)
        self.__vM_AttrDef17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_BasicAttrDef"):
                opp_val = getattr(old_value, "vM_BasicAttrDef", None)
                if opp_val == self:
                    setattr(old_value, "vM_BasicAttrDef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_BasicAttrDef"):
                opp_val = getattr(value, "vM_BasicAttrDef", None)
                setattr(value, "vM_BasicAttrDef", self)

class vM_Integer_ATT_ID(Abstract_ATT_ID):

    pass
class vM_StringDefaultDef:

    def __init__(self, value: str, vM_StringDefaultDef: "vM_StringAttrDef" = None, vM_StringDefaultDef44: "vM_EnumStringDef" = None):
        self.value = value
        self.vM_StringDefaultDef = vM_StringDefaultDef
        self.vM_StringDefaultDef44 = vM_StringDefaultDef44
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def vM_StringDefaultDef(self):
        return self.__vM_StringDefaultDef

    @vM_StringDefaultDef.setter
    def vM_StringDefaultDef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_StringDefaultDef__vM_StringDefaultDef", None)
        self.__vM_StringDefaultDef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_StringAttrDef25"):
                opp_val = getattr(old_value, "vM_StringAttrDef25", None)
                if opp_val == self:
                    setattr(old_value, "vM_StringAttrDef25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_StringAttrDef25"):
                opp_val = getattr(value, "vM_StringAttrDef25", None)
                setattr(value, "vM_StringAttrDef25", self)

    @property
    def vM_StringDefaultDef44(self):
        return self.__vM_StringDefaultDef44

    @vM_StringDefaultDef44.setter
    def vM_StringDefaultDef44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_StringDefaultDef__vM_StringDefaultDef44", None)
        self.__vM_StringDefaultDef44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_EnumStringDef43"):
                opp_val = getattr(old_value, "vM_EnumStringDef43", None)
                if opp_val == self:
                    setattr(old_value, "vM_EnumStringDef43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_EnumStringDef43"):
                opp_val = getattr(value, "vM_EnumStringDef43", None)
                setattr(value, "vM_EnumStringDef43", self)

class vM_String_ATT_ID(Abstract_ATT_ID):

    pass
class vM_BoolDefaultDef:

    def __init__(self, value: str, vM_BoolDefaultDef: "vM_BooleanAttrDef" = None):
        self.value = value
        self.vM_BoolDefaultDef = vM_BoolDefaultDef
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def vM_BoolDefaultDef(self):
        return self.__vM_BoolDefaultDef

    @vM_BoolDefaultDef.setter
    def vM_BoolDefaultDef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_BoolDefaultDef__vM_BoolDefaultDef", None)
        self.__vM_BoolDefaultDef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_BooleanAttrDef22"):
                opp_val = getattr(old_value, "vM_BooleanAttrDef22", None)
                if opp_val == self:
                    setattr(old_value, "vM_BooleanAttrDef22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_BooleanAttrDef22"):
                opp_val = getattr(value, "vM_BooleanAttrDef22", None)
                setattr(value, "vM_BooleanAttrDef22", self)

class vM_Boolean_ATT_ID(Abstract_ATT_ID):

    pass
class BasicAttrDef:

    pass
class vM_StringAttrDef(BasicAttrDef):

    def __init__(self, value: str, vM_StringAttrDef: "vM_String_ATT_ID" = None, vM_StringAttrDef25: "vM_StringDefaultDef" = None):
        self.value = value
        self.vM_StringAttrDef = vM_StringAttrDef
        self.vM_StringAttrDef25 = vM_StringAttrDef25
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def vM_StringAttrDef(self):
        return self.__vM_StringAttrDef

    @vM_StringAttrDef.setter
    def vM_StringAttrDef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_StringAttrDef__vM_StringAttrDef", None)
        self.__vM_StringAttrDef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_String_ATT_ID"):
                opp_val = getattr(old_value, "vM_String_ATT_ID", None)
                if opp_val == self:
                    setattr(old_value, "vM_String_ATT_ID", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_String_ATT_ID"):
                opp_val = getattr(value, "vM_String_ATT_ID", None)
                setattr(value, "vM_String_ATT_ID", self)

    @property
    def vM_StringAttrDef25(self):
        return self.__vM_StringAttrDef25

    @vM_StringAttrDef25.setter
    def vM_StringAttrDef25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_StringAttrDef__vM_StringAttrDef25", None)
        self.__vM_StringAttrDef25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_StringDefaultDef"):
                opp_val = getattr(old_value, "vM_StringDefaultDef", None)
                if opp_val == self:
                    setattr(old_value, "vM_StringDefaultDef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_StringDefaultDef"):
                opp_val = getattr(value, "vM_StringDefaultDef", None)
                setattr(value, "vM_StringDefaultDef", self)

class vM_IntegerAttrDef(BasicAttrDef):

    pass
class vM_RealAttrDef(BasicAttrDef):

    pass
class vM_BooleanAttrDef(BasicAttrDef):

    def __init__(self, value: str, vM_BooleanAttrDef: "vM_Boolean_ATT_ID" = None, vM_BooleanAttrDef22: "vM_BoolDefaultDef" = None):
        self.value = value
        self.vM_BooleanAttrDef = vM_BooleanAttrDef
        self.vM_BooleanAttrDef22 = vM_BooleanAttrDef22
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def vM_BooleanAttrDef22(self):
        return self.__vM_BooleanAttrDef22

    @vM_BooleanAttrDef22.setter
    def vM_BooleanAttrDef22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_BooleanAttrDef__vM_BooleanAttrDef22", None)
        self.__vM_BooleanAttrDef22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_BoolDefaultDef"):
                opp_val = getattr(old_value, "vM_BoolDefaultDef", None)
                if opp_val == self:
                    setattr(old_value, "vM_BoolDefaultDef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_BoolDefaultDef"):
                opp_val = getattr(value, "vM_BoolDefaultDef", None)
                setattr(value, "vM_BoolDefaultDef", self)

    @property
    def vM_BooleanAttrDef(self):
        return self.__vM_BooleanAttrDef

    @vM_BooleanAttrDef.setter
    def vM_BooleanAttrDef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_BooleanAttrDef__vM_BooleanAttrDef", None)
        self.__vM_BooleanAttrDef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_Boolean_ATT_ID"):
                opp_val = getattr(old_value, "vM_Boolean_ATT_ID", None)
                if opp_val == self:
                    setattr(old_value, "vM_Boolean_ATT_ID", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_Boolean_ATT_ID"):
                opp_val = getattr(value, "vM_Boolean_ATT_ID", None)
                setattr(value, "vM_Boolean_ATT_ID", self)

class vM_EnumAttrDef:

    def __init__(self, value: str, vM_EnumAttrDef: "vM_AttrDef" = None):
        self.value = value
        self.vM_EnumAttrDef = vM_EnumAttrDef
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def vM_EnumAttrDef(self):
        return self.__vM_EnumAttrDef

    @vM_EnumAttrDef.setter
    def vM_EnumAttrDef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_EnumAttrDef__vM_EnumAttrDef", None)
        self.__vM_EnumAttrDef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_AttrDef19"):
                opp_val = getattr(old_value, "vM_AttrDef19", None)
                if opp_val == self:
                    setattr(old_value, "vM_AttrDef19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_AttrDef19"):
                opp_val = getattr(value, "vM_AttrDef19", None)
                setattr(value, "vM_AttrDef19", self)

class vM_BasicAttrDef:

    pass
class vM_BasicAttrValuation(ExtendedValuation):

    def __init__(self, value: str, vM_BasicAttrValuation: "vM_Attributes" = None, vM_BasicAttrValuation107: "vM_AttHead" = None):
        self.value = value
        self.vM_BasicAttrValuation = vM_BasicAttrValuation
        self.vM_BasicAttrValuation107 = vM_BasicAttrValuation107
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def vM_BasicAttrValuation107(self):
        return self.__vM_BasicAttrValuation107

    @vM_BasicAttrValuation107.setter
    def vM_BasicAttrValuation107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_BasicAttrValuation__vM_BasicAttrValuation107", None)
        self.__vM_BasicAttrValuation107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_AttHead108"):
                opp_val = getattr(old_value, "vM_AttHead108", None)
                if opp_val == self:
                    setattr(old_value, "vM_AttHead108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_AttHead108"):
                opp_val = getattr(value, "vM_AttHead108", None)
                setattr(value, "vM_AttHead108", self)

    @property
    def vM_BasicAttrValuation(self):
        return self.__vM_BasicAttrValuation

    @vM_BasicAttrValuation.setter
    def vM_BasicAttrValuation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_BasicAttrValuation__vM_BasicAttrValuation", None)
        self.__vM_BasicAttrValuation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_Attributes15"):
                opp_val = getattr(old_value, "vM_Attributes15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_Attributes15"):
                opp_val = getattr(value, "vM_Attributes15", None)
                if opp_val is None:
                    setattr(value, "vM_Attributes15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class vM_Email:

    def __init__(self, username: str, domain: str, vM_Email: "vM_MetaDataDeclaration" = None):
        self.username = username
        self.domain = domain
        self.vM_Email = vM_Email
        
    @property
    def username(self) -> str:
        return self.__username

    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def domain(self) -> str:
        return self.__domain

    @domain.setter
    def domain(self, domain: str):
        self.__domain = domain

    @property
    def vM_Email(self):
        return self.__vM_Email

    @vM_Email.setter
    def vM_Email(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_Email__vM_Email", None)
        self.__vM_Email = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_MetaDataDeclaration5"):
                opp_val = getattr(old_value, "vM_MetaDataDeclaration5", None)
                if opp_val == self:
                    setattr(old_value, "vM_MetaDataDeclaration5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_MetaDataDeclaration5"):
                opp_val = getattr(value, "vM_MetaDataDeclaration5", None)
                setattr(value, "vM_MetaDataDeclaration5", self)

class FeaturesGroup:

    pass
class vM_CardinalityBased(FeaturesGroup):

    def __init__(self, min: str, max: str, all: bool):
        self.min = min
        self.max = max
        self.all = all
        
    @property
    def max(self) -> str:
        return self.__max

    @max.setter
    def max(self, max: str):
        self.__max = max

    @property
    def all(self) -> bool:
        return self.__all

    @all.setter
    def all(self, all: bool):
        self.__all = all

    @property
    def min(self) -> str:
        return self.__min

    @min.setter
    def min(self, min: str):
        self.__min = min

class vM_Orgroup(FeaturesGroup):

    pass
class vM_Xorgroup(FeaturesGroup):

    pass
class vM_FeatureDefinition:

    pass
class FeatureDefinition:

    pass
class vM_Feature(FeatureDefinition):

    def __init__(self, notTranslatable: bool, runTime: bool, notDecidable: bool, optional: bool, min: str, max: str, name: str, vM_Feature: "vM_FeatureHierarchy" = None, vM_Feature58: "vM_FeatureDescription" = None, vM_Feature61: "vM_AttributeDescription" = None, vM_Feature68: "vM_SpecialExpression" = None, vM_Feature70: "vM_PrimitiveExpression" = None, vM_Feature105: "vM_BooleanValuation" = None, vM_Feature142: "vM_PairFeatureInteger" = None, vM_Feature124: "vM_TableBasedValuationByFeatureAndClone" = None, vM_Feature129: "vM_TableBasedValuationByFeature" = None, vM_Feature152: "vM_AttHead" = None, vM_Feature149: "vM_PairFeatureReal" = None):
        self.notTranslatable = notTranslatable
        self.runTime = runTime
        self.notDecidable = notDecidable
        self.optional = optional
        self.min = min
        self.max = max
        self.name = name
        self.vM_Feature = vM_Feature
        self.vM_Feature58 = vM_Feature58
        self.vM_Feature61 = vM_Feature61
        self.vM_Feature68 = vM_Feature68
        self.vM_Feature70 = vM_Feature70
        self.vM_Feature105 = vM_Feature105
        self.vM_Feature142 = vM_Feature142
        self.vM_Feature124 = vM_Feature124
        self.vM_Feature129 = vM_Feature129
        self.vM_Feature152 = vM_Feature152
        self.vM_Feature149 = vM_Feature149
        
    @property
    def max(self) -> str:
        return self.__max

    @max.setter
    def max(self, max: str):
        self.__max = max

    @property
    def runTime(self) -> bool:
        return self.__runTime

    @runTime.setter
    def runTime(self, runTime: bool):
        self.__runTime = runTime

    @property
    def optional(self) -> bool:
        return self.__optional

    @optional.setter
    def optional(self, optional: bool):
        self.__optional = optional

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def min(self) -> str:
        return self.__min

    @min.setter
    def min(self, min: str):
        self.__min = min

    @property
    def notDecidable(self) -> bool:
        return self.__notDecidable

    @notDecidable.setter
    def notDecidable(self, notDecidable: bool):
        self.__notDecidable = notDecidable

    @property
    def notTranslatable(self) -> bool:
        return self.__notTranslatable

    @notTranslatable.setter
    def notTranslatable(self, notTranslatable: bool):
        self.__notTranslatable = notTranslatable

    @property
    def vM_Feature142(self):
        return self.__vM_Feature142

    @vM_Feature142.setter
    def vM_Feature142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_Feature__vM_Feature142", None)
        self.__vM_Feature142 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_PairFeatureInteger141"):
                opp_val = getattr(old_value, "vM_PairFeatureInteger141", None)
                if opp_val == self:
                    setattr(old_value, "vM_PairFeatureInteger141", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_PairFeatureInteger141"):
                opp_val = getattr(value, "vM_PairFeatureInteger141", None)
                setattr(value, "vM_PairFeatureInteger141", self)

    @property
    def vM_Feature152(self):
        return self.__vM_Feature152

    @vM_Feature152.setter
    def vM_Feature152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_Feature__vM_Feature152", None)
        self.__vM_Feature152 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_AttHead151"):
                opp_val = getattr(old_value, "vM_AttHead151", None)
                if opp_val == self:
                    setattr(old_value, "vM_AttHead151", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_AttHead151"):
                opp_val = getattr(value, "vM_AttHead151", None)
                setattr(value, "vM_AttHead151", self)

    @property
    def vM_Feature129(self):
        return self.__vM_Feature129

    @vM_Feature129.setter
    def vM_Feature129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_Feature__vM_Feature129", None)
        self.__vM_Feature129 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_TableBasedValuationByFeature128"):
                opp_val = getattr(old_value, "vM_TableBasedValuationByFeature128", None)
                if opp_val == self:
                    setattr(old_value, "vM_TableBasedValuationByFeature128", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_TableBasedValuationByFeature128"):
                opp_val = getattr(value, "vM_TableBasedValuationByFeature128", None)
                setattr(value, "vM_TableBasedValuationByFeature128", self)

    @property
    def vM_Feature68(self):
        return self.__vM_Feature68

    @vM_Feature68.setter
    def vM_Feature68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_Feature__vM_Feature68", None)
        self.__vM_Feature68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_SpecialExpression"):
                opp_val = getattr(old_value, "vM_SpecialExpression", None)
                if opp_val == self:
                    setattr(old_value, "vM_SpecialExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_SpecialExpression"):
                opp_val = getattr(value, "vM_SpecialExpression", None)
                setattr(value, "vM_SpecialExpression", self)

    @property
    def vM_Feature149(self):
        return self.__vM_Feature149

    @vM_Feature149.setter
    def vM_Feature149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_Feature__vM_Feature149", None)
        self.__vM_Feature149 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_PairFeatureReal148"):
                opp_val = getattr(old_value, "vM_PairFeatureReal148", None)
                if opp_val == self:
                    setattr(old_value, "vM_PairFeatureReal148", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_PairFeatureReal148"):
                opp_val = getattr(value, "vM_PairFeatureReal148", None)
                setattr(value, "vM_PairFeatureReal148", self)

    @property
    def vM_Feature58(self):
        return self.__vM_Feature58

    @vM_Feature58.setter
    def vM_Feature58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_Feature__vM_Feature58", None)
        self.__vM_Feature58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_FeatureDescription57"):
                opp_val = getattr(old_value, "vM_FeatureDescription57", None)
                if opp_val == self:
                    setattr(old_value, "vM_FeatureDescription57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_FeatureDescription57"):
                opp_val = getattr(value, "vM_FeatureDescription57", None)
                setattr(value, "vM_FeatureDescription57", self)

    @property
    def vM_Feature105(self):
        return self.__vM_Feature105

    @vM_Feature105.setter
    def vM_Feature105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_Feature__vM_Feature105", None)
        self.__vM_Feature105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_BooleanValuation104"):
                opp_val = getattr(old_value, "vM_BooleanValuation104", None)
                if opp_val == self:
                    setattr(old_value, "vM_BooleanValuation104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_BooleanValuation104"):
                opp_val = getattr(value, "vM_BooleanValuation104", None)
                setattr(value, "vM_BooleanValuation104", self)

    @property
    def vM_Feature(self):
        return self.__vM_Feature

    @vM_Feature.setter
    def vM_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_Feature__vM_Feature", None)
        self.__vM_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_FeatureHierarchy8"):
                opp_val = getattr(old_value, "vM_FeatureHierarchy8", None)
                if opp_val == self:
                    setattr(old_value, "vM_FeatureHierarchy8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_FeatureHierarchy8"):
                opp_val = getattr(value, "vM_FeatureHierarchy8", None)
                setattr(value, "vM_FeatureHierarchy8", self)

    @property
    def vM_Feature124(self):
        return self.__vM_Feature124

    @vM_Feature124.setter
    def vM_Feature124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_Feature__vM_Feature124", None)
        self.__vM_Feature124 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_TableBasedValuationByFeatureAndClone123"):
                opp_val = getattr(old_value, "vM_TableBasedValuationByFeatureAndClone123", None)
                if opp_val == self:
                    setattr(old_value, "vM_TableBasedValuationByFeatureAndClone123", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_TableBasedValuationByFeatureAndClone123"):
                opp_val = getattr(value, "vM_TableBasedValuationByFeatureAndClone123", None)
                setattr(value, "vM_TableBasedValuationByFeatureAndClone123", self)

    @property
    def vM_Feature70(self):
        return self.__vM_Feature70

    @vM_Feature70.setter
    def vM_Feature70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_Feature__vM_Feature70", None)
        self.__vM_Feature70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_PrimitiveExpression"):
                opp_val = getattr(old_value, "vM_PrimitiveExpression", None)
                if opp_val == self:
                    setattr(old_value, "vM_PrimitiveExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_PrimitiveExpression"):
                opp_val = getattr(value, "vM_PrimitiveExpression", None)
                setattr(value, "vM_PrimitiveExpression", self)

    @property
    def vM_Feature61(self):
        return self.__vM_Feature61

    @vM_Feature61.setter
    def vM_Feature61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_Feature__vM_Feature61", None)
        self.__vM_Feature61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_AttributeDescription60"):
                opp_val = getattr(old_value, "vM_AttributeDescription60", None)
                if opp_val == self:
                    setattr(old_value, "vM_AttributeDescription60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_AttributeDescription60"):
                opp_val = getattr(value, "vM_AttributeDescription60", None)
                setattr(value, "vM_AttributeDescription60", self)

class vM_FeaturesGroup(FeatureDefinition):

    pass
class vM_FeatureHierarchy(FeatureDefinition):

    pass
class vM_Version:

    def __init__(self, main: int, tail: int, vM_Version: "vM_MetaDataDeclaration" = None):
        self.main = main
        self.tail = tail
        self.vM_Version = vM_Version
        
    @property
    def main(self) -> int:
        return self.__main

    @main.setter
    def main(self, main: int):
        self.__main = main

    @property
    def tail(self) -> int:
        return self.__tail

    @tail.setter
    def tail(self, tail: int):
        self.__tail = tail

    @property
    def vM_Version(self):
        return self.__vM_Version

    @vM_Version.setter
    def vM_Version(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_Version__vM_Version", None)
        self.__vM_Version = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_MetaDataDeclaration"):
                opp_val = getattr(old_value, "vM_MetaDataDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "vM_MetaDataDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_MetaDataDeclaration"):
                opp_val = getattr(value, "vM_MetaDataDeclaration", None)
                setattr(value, "vM_MetaDataDeclaration", self)

class VmBlock:

    pass
class vM_MetaDataDeclaration(VmBlock):

    def __init__(self, name: str, date: str, description: str, author: str, organization: str, publication: str, vM_MetaDataDeclaration: "vM_Version" = None, vM_MetaDataDeclaration5: "vM_Email" = None):
        self.name = name
        self.date = date
        self.description = description
        self.author = author
        self.organization = organization
        self.publication = publication
        self.vM_MetaDataDeclaration = vM_MetaDataDeclaration
        self.vM_MetaDataDeclaration5 = vM_MetaDataDeclaration5
        
    @property
    def organization(self) -> str:
        return self.__organization

    @organization.setter
    def organization(self, organization: str):
        self.__organization = organization

    @property
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author

    @property
    def date(self) -> str:
        return self.__date

    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def publication(self) -> str:
        return self.__publication

    @publication.setter
    def publication(self, publication: str):
        self.__publication = publication

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def vM_MetaDataDeclaration5(self):
        return self.__vM_MetaDataDeclaration5

    @vM_MetaDataDeclaration5.setter
    def vM_MetaDataDeclaration5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_MetaDataDeclaration__vM_MetaDataDeclaration5", None)
        self.__vM_MetaDataDeclaration5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_Email"):
                opp_val = getattr(old_value, "vM_Email", None)
                if opp_val == self:
                    setattr(old_value, "vM_Email", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_Email"):
                opp_val = getattr(value, "vM_Email", None)
                setattr(value, "vM_Email", self)

    @property
    def vM_MetaDataDeclaration(self):
        return self.__vM_MetaDataDeclaration

    @vM_MetaDataDeclaration.setter
    def vM_MetaDataDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_MetaDataDeclaration__vM_MetaDataDeclaration", None)
        self.__vM_MetaDataDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vM_Version"):
                opp_val = getattr(old_value, "vM_Version", None)
                if opp_val == self:
                    setattr(old_value, "vM_Version", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vM_Version"):
                opp_val = getattr(value, "vM_Version", None)
                setattr(value, "vM_Version", self)

class vM_Configurations(VmBlock):

    pass
class vM_Attributes(VmBlock):

    pass
class vM_Relationships(VmBlock):

    pass
class vM_Descriptions(VmBlock):

    pass
class vM_Constraints(VmBlock):

    pass
class vM_ImportDeclaration(VmBlock):

    def __init__(self, importedNamespace: str):
        self.importedNamespace = importedNamespace
        
    @property
    def importedNamespace(self) -> str:
        return self.__importedNamespace

    @importedNamespace.setter
    def importedNamespace(self, importedNamespace: str):
        self.__importedNamespace = importedNamespace

class vM_Objectives(VmBlock):

    pass
class vM_PackageDeclaration(VmBlock):

    def __init__(self, name: str, vM_PackageDeclaration: set["vM_VmBlock"] = None):
        self.name = name
        self.vM_PackageDeclaration = vM_PackageDeclaration if vM_PackageDeclaration is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def vM_PackageDeclaration(self):
        return self.__vM_PackageDeclaration

    @vM_PackageDeclaration.setter
    def vM_PackageDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vM_PackageDeclaration__vM_PackageDeclaration", None)
        self.__vM_PackageDeclaration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "vM_VmBlock2"):
                    opp_val = getattr(item, "vM_VmBlock2", None)
                    
                    if opp_val == self:
                        setattr(item, "vM_VmBlock2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "vM_VmBlock2"):
                    opp_val = getattr(item, "vM_VmBlock2", None)
                    
                    setattr(item, "vM_VmBlock2", self)
                    

class vM_VmBlock:

    pass
class vM_Model:

    pass