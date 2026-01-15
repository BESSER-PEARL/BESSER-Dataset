from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Type(Enum):
    double = "double"
    integer = "integer"
    string = "string"
    boolean = "boolean"
    ServiceAskMode = "ServiceAskMode"
    ServiceOfferMode = "ServiceOfferMode"
    Double1 = "Double1"
    Integer1 = "Integer1"
    String1 = "String1"
    Boolean1 = "Boolean1"
class Mode(Enum):
    CanDo = "CanDo"
    CanTeach = "CanTeach"
    Both = "Both"
    KnowsWhoCanBoth = "KnowsWhoCanBoth"
    KnowsWhoCanDo = "KnowsWhoCanDo"
    KnowsWhoCanTeach = "KnowsWhoCanTeach"
    None = "None"


############################################
# Definition of Classes
############################################

class State:

    pass
class selflet_FinalState(State):

    pass
class selflet_AbilityState(State):

    pass
class selflet_IntermediateState(State):

    pass
class selflet_InitialState(State):

    pass
class selflet_State:

    def __init__(self, name: str, selflet_State: "selflet_ElementaryBehavior" = None, selflet_State60: "selflet_ComplexBehavior" = None, selflet_State63: "selflet_State" = None, selflet_State61: set["selflet_State"] = None):
        self.name = name
        self.selflet_State = selflet_State
        self.selflet_State60 = selflet_State60
        self.selflet_State63 = selflet_State63
        self.selflet_State61 = selflet_State61 if selflet_State61 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def selflet_State63(self):
        return self.__selflet_State63

    @selflet_State63.setter
    def selflet_State63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_selflet_State__selflet_State63", None)
        self.__selflet_State63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "selflet_State61"):
                opp_val = getattr(old_value, "selflet_State61", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "selflet_State61"):
                opp_val = getattr(value, "selflet_State61", None)
                if opp_val is None:
                    setattr(value, "selflet_State61", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def selflet_State60(self):
        return self.__selflet_State60

    @selflet_State60.setter
    def selflet_State60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_selflet_State__selflet_State60", None)
        self.__selflet_State60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "selflet_ComplexBehavior"):
                opp_val = getattr(old_value, "selflet_ComplexBehavior", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "selflet_ComplexBehavior"):
                opp_val = getattr(value, "selflet_ComplexBehavior", None)
                if opp_val is None:
                    setattr(value, "selflet_ComplexBehavior", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def selflet_State61(self):
        return self.__selflet_State61

    @selflet_State61.setter
    def selflet_State61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_selflet_State__selflet_State61", None)
        self.__selflet_State61 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "selflet_State63"):
                    opp_val = getattr(item, "selflet_State63", None)
                    
                    if opp_val == self:
                        setattr(item, "selflet_State63", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "selflet_State63"):
                    opp_val = getattr(item, "selflet_State63", None)
                    
                    setattr(item, "selflet_State63", self)
                    

    @property
    def selflet_State(self):
        return self.__selflet_State

    @selflet_State.setter
    def selflet_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_selflet_State__selflet_State", None)
        self.__selflet_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "selflet_ElementaryBehavior"):
                opp_val = getattr(old_value, "selflet_ElementaryBehavior", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "selflet_ElementaryBehavior"):
                opp_val = getattr(value, "selflet_ElementaryBehavior", None)
                if opp_val is None:
                    setattr(value, "selflet_ElementaryBehavior", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Behavior:

    pass
class selflet_ComplexBehavior(Behavior):

    pass
class selflet_ElementaryBehavior(Behavior):

    pass
class selflet_Services:

    pass
class selflet_TypeKnowledge:

    pass
class selflet_SelfletResources:

    pass
class selflet_SelfletProperties:

    def __init__(self, author: str, description: str, limePort: str, enableOptimizationPolicy: str, enableCloudOptimizationPolicy: str, selflet_SelfletProperties: "selflet_Selflet" = None, selflet_SelfletProperties17: "selflet_Empty" = None, selflet_SelfletProperties19: "selflet_Active" = None, selflet_SelfletProperties21: "selflet_Reds" = None, selflet_SelfletProperties23: "selflet_GeneralKnowledge" = None, selflet_SelfletProperties26: "selflet_TypeKnowledge" = None):
        self.author = author
        self.description = description
        self.limePort = limePort
        self.enableOptimizationPolicy = enableOptimizationPolicy
        self.enableCloudOptimizationPolicy = enableCloudOptimizationPolicy
        self.selflet_SelfletProperties = selflet_SelfletProperties
        self.selflet_SelfletProperties17 = selflet_SelfletProperties17
        self.selflet_SelfletProperties19 = selflet_SelfletProperties19
        self.selflet_SelfletProperties21 = selflet_SelfletProperties21
        self.selflet_SelfletProperties23 = selflet_SelfletProperties23
        self.selflet_SelfletProperties26 = selflet_SelfletProperties26
        
    @property
    def enableOptimizationPolicy(self) -> str:
        return self.__enableOptimizationPolicy

    @enableOptimizationPolicy.setter
    def enableOptimizationPolicy(self, enableOptimizationPolicy: str):
        self.__enableOptimizationPolicy = enableOptimizationPolicy

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author

    @property
    def enableCloudOptimizationPolicy(self) -> str:
        return self.__enableCloudOptimizationPolicy

    @enableCloudOptimizationPolicy.setter
    def enableCloudOptimizationPolicy(self, enableCloudOptimizationPolicy: str):
        self.__enableCloudOptimizationPolicy = enableCloudOptimizationPolicy

    @property
    def limePort(self) -> str:
        return self.__limePort

    @limePort.setter
    def limePort(self, limePort: str):
        self.__limePort = limePort

    @property
    def selflet_SelfletProperties23(self):
        return self.__selflet_SelfletProperties23

    @selflet_SelfletProperties23.setter
    def selflet_SelfletProperties23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_selflet_SelfletProperties__selflet_SelfletProperties23", None)
        self.__selflet_SelfletProperties23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "selflet_GeneralKnowledge24"):
                opp_val = getattr(old_value, "selflet_GeneralKnowledge24", None)
                if opp_val == self:
                    setattr(old_value, "selflet_GeneralKnowledge24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "selflet_GeneralKnowledge24"):
                opp_val = getattr(value, "selflet_GeneralKnowledge24", None)
                setattr(value, "selflet_GeneralKnowledge24", self)

    @property
    def selflet_SelfletProperties26(self):
        return self.__selflet_SelfletProperties26

    @selflet_SelfletProperties26.setter
    def selflet_SelfletProperties26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_selflet_SelfletProperties__selflet_SelfletProperties26", None)
        self.__selflet_SelfletProperties26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "selflet_TypeKnowledge"):
                opp_val = getattr(old_value, "selflet_TypeKnowledge", None)
                if opp_val == self:
                    setattr(old_value, "selflet_TypeKnowledge", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "selflet_TypeKnowledge"):
                opp_val = getattr(value, "selflet_TypeKnowledge", None)
                setattr(value, "selflet_TypeKnowledge", self)

    @property
    def selflet_SelfletProperties(self):
        return self.__selflet_SelfletProperties

    @selflet_SelfletProperties.setter
    def selflet_SelfletProperties(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_selflet_SelfletProperties__selflet_SelfletProperties", None)
        self.__selflet_SelfletProperties = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "selflet_Selflet"):
                opp_val = getattr(old_value, "selflet_Selflet", None)
                if opp_val == self:
                    setattr(old_value, "selflet_Selflet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "selflet_Selflet"):
                opp_val = getattr(value, "selflet_Selflet", None)
                setattr(value, "selflet_Selflet", self)

    @property
    def selflet_SelfletProperties17(self):
        return self.__selflet_SelfletProperties17

    @selflet_SelfletProperties17.setter
    def selflet_SelfletProperties17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_selflet_SelfletProperties__selflet_SelfletProperties17", None)
        self.__selflet_SelfletProperties17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "selflet_Empty"):
                opp_val = getattr(old_value, "selflet_Empty", None)
                if opp_val == self:
                    setattr(old_value, "selflet_Empty", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "selflet_Empty"):
                opp_val = getattr(value, "selflet_Empty", None)
                setattr(value, "selflet_Empty", self)

    @property
    def selflet_SelfletProperties21(self):
        return self.__selflet_SelfletProperties21

    @selflet_SelfletProperties21.setter
    def selflet_SelfletProperties21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_selflet_SelfletProperties__selflet_SelfletProperties21", None)
        self.__selflet_SelfletProperties21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "selflet_Reds"):
                opp_val = getattr(old_value, "selflet_Reds", None)
                if opp_val == self:
                    setattr(old_value, "selflet_Reds", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "selflet_Reds"):
                opp_val = getattr(value, "selflet_Reds", None)
                setattr(value, "selflet_Reds", self)

    @property
    def selflet_SelfletProperties19(self):
        return self.__selflet_SelfletProperties19

    @selflet_SelfletProperties19.setter
    def selflet_SelfletProperties19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_selflet_SelfletProperties__selflet_SelfletProperties19", None)
        self.__selflet_SelfletProperties19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "selflet_Active"):
                opp_val = getattr(old_value, "selflet_Active", None)
                if opp_val == self:
                    setattr(old_value, "selflet_Active", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "selflet_Active"):
                opp_val = getattr(value, "selflet_Active", None)
                setattr(value, "selflet_Active", self)

class selflet_Selflet:

    def __init__(self, name: str, selflet_Selflet: "selflet_SelfletProperties" = None, selflet_Selflet15: "selflet_SelfletResources" = None):
        self.name = name
        self.selflet_Selflet = selflet_Selflet
        self.selflet_Selflet15 = selflet_Selflet15
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def selflet_Selflet15(self):
        return self.__selflet_Selflet15

    @selflet_Selflet15.setter
    def selflet_Selflet15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_selflet_Selflet__selflet_Selflet15", None)
        self.__selflet_Selflet15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "selflet_SelfletResources"):
                opp_val = getattr(old_value, "selflet_SelfletResources", None)
                if opp_val == self:
                    setattr(old_value, "selflet_SelfletResources", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "selflet_SelfletResources"):
                opp_val = getattr(value, "selflet_SelfletResources", None)
                setattr(value, "selflet_SelfletResources", self)

    @property
    def selflet_Selflet(self):
        return self.__selflet_Selflet

    @selflet_Selflet.setter
    def selflet_Selflet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_selflet_Selflet__selflet_Selflet", None)
        self.__selflet_Selflet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "selflet_SelfletProperties"):
                opp_val = getattr(old_value, "selflet_SelfletProperties", None)
                if opp_val == self:
                    setattr(old_value, "selflet_SelfletProperties", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "selflet_SelfletProperties"):
                opp_val = getattr(value, "selflet_SelfletProperties", None)
                setattr(value, "selflet_SelfletProperties", self)

class selflet_Rule:

    def __init__(self, file: str, selflet_Rule: "selflet_Rules" = None):
        self.file = file
        self.selflet_Rule = selflet_Rule
        
    @property
    def file(self) -> str:
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = file

    @property
    def selflet_Rule(self):
        return self.__selflet_Rule

    @selflet_Rule.setter
    def selflet_Rule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_selflet_Rule__selflet_Rule", None)
        self.__selflet_Rule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "selflet_Rules"):
                opp_val = getattr(old_value, "selflet_Rules", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "selflet_Rules"):
                opp_val = getattr(value, "selflet_Rules", None)
                if opp_val is None:
                    setattr(value, "selflet_Rules", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class selflet_Rules:

    pass
class selflet_Reds:

    def __init__(self, ipAddress: str, port: str, selflet_Reds: "selflet_SelfletProperties" = None):
        self.ipAddress = ipAddress
        self.port = port
        self.selflet_Reds = selflet_Reds
        
    @property
    def ipAddress(self) -> str:
        return self.__ipAddress

    @ipAddress.setter
    def ipAddress(self, ipAddress: str):
        self.__ipAddress = ipAddress

    @property
    def port(self) -> str:
        return self.__port

    @port.setter
    def port(self, port: str):
        self.__port = port

    @property
    def selflet_Reds(self):
        return self.__selflet_Reds

    @selflet_Reds.setter
    def selflet_Reds(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_selflet_Reds__selflet_Reds", None)
        self.__selflet_Reds = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "selflet_SelfletProperties21"):
                opp_val = getattr(old_value, "selflet_SelfletProperties21", None)
                if opp_val == self:
                    setattr(old_value, "selflet_SelfletProperties21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "selflet_SelfletProperties21"):
                opp_val = getattr(value, "selflet_SelfletProperties21", None)
                setattr(value, "selflet_SelfletProperties21", self)

class selflet_Output:

    pass
class selflet_OfferMode:

    def __init__(self, mode: str, selflet_OfferMode: "selflet_Service" = None):
        self.mode = mode
        self.selflet_OfferMode = selflet_OfferMode
        
    @property
    def mode(self) -> str:
        return self.__mode

    @mode.setter
    def mode(self, mode: str):
        self.__mode = mode

    @property
    def selflet_OfferMode(self):
        return self.__selflet_OfferMode

    @selflet_OfferMode.setter
    def selflet_OfferMode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_selflet_OfferMode__selflet_OfferMode", None)
        self.__selflet_OfferMode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "selflet_Service51"):
                opp_val = getattr(old_value, "selflet_Service51", None)
                if opp_val == self:
                    setattr(old_value, "selflet_Service51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "selflet_Service51"):
                opp_val = getattr(value, "selflet_Service51", None)
                setattr(value, "selflet_Service51", self)

class selflet_Method:

    def __init__(self, name: str, paramType: str, selflet_Method: "selflet_Methods" = None):
        self.name = name
        self.paramType = paramType
        self.selflet_Method = selflet_Method
        
    @property
    def paramType(self) -> str:
        return self.__paramType

    @paramType.setter
    def paramType(self, paramType: str):
        self.__paramType = paramType

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def selflet_Method(self):
        return self.__selflet_Method

    @selflet_Method.setter
    def selflet_Method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_selflet_Method__selflet_Method", None)
        self.__selflet_Method = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "selflet_Methods9"):
                opp_val = getattr(old_value, "selflet_Methods9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "selflet_Methods9"):
                opp_val = getattr(value, "selflet_Methods9", None)
                if opp_val is None:
                    setattr(value, "selflet_Methods9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class selflet_Parameter:

    def __init__(self, name: str, type: str, selflet_Parameter: "selflet_Input" = None, selflet_Parameter11: "selflet_Output" = None):
        self.name = name
        self.type = type
        self.selflet_Parameter = selflet_Parameter
        self.selflet_Parameter11 = selflet_Parameter11
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def selflet_Parameter11(self):
        return self.__selflet_Parameter11

    @selflet_Parameter11.setter
    def selflet_Parameter11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_selflet_Parameter__selflet_Parameter11", None)
        self.__selflet_Parameter11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "selflet_Output"):
                opp_val = getattr(old_value, "selflet_Output", None)
                if opp_val == self:
                    setattr(old_value, "selflet_Output", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "selflet_Output"):
                opp_val = getattr(value, "selflet_Output", None)
                setattr(value, "selflet_Output", self)

    @property
    def selflet_Parameter(self):
        return self.__selflet_Parameter

    @selflet_Parameter.setter
    def selflet_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_selflet_Parameter__selflet_Parameter", None)
        self.__selflet_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "selflet_Input"):
                opp_val = getattr(old_value, "selflet_Input", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "selflet_Input"):
                opp_val = getattr(value, "selflet_Input", None)
                if opp_val is None:
                    setattr(value, "selflet_Input", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class selflet_Input:

    pass
class selflet_SelfLetProperty:

    def __init__(self, name: str, type: str, value: str, selflet_SelfLetProperty: "selflet_GeneralKnowledge" = None, selflet_SelfLetProperty57: "selflet_TypeKnowledge" = None):
        self.name = name
        self.type = type
        self.value = value
        self.selflet_SelfLetProperty = selflet_SelfLetProperty
        self.selflet_SelfLetProperty57 = selflet_SelfLetProperty57
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def selflet_SelfLetProperty(self):
        return self.__selflet_SelfLetProperty

    @selflet_SelfLetProperty.setter
    def selflet_SelfLetProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_selflet_SelfLetProperty__selflet_SelfLetProperty", None)
        self.__selflet_SelfLetProperty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "selflet_GeneralKnowledge"):
                opp_val = getattr(old_value, "selflet_GeneralKnowledge", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "selflet_GeneralKnowledge"):
                opp_val = getattr(value, "selflet_GeneralKnowledge", None)
                if opp_val is None:
                    setattr(value, "selflet_GeneralKnowledge", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def selflet_SelfLetProperty57(self):
        return self.__selflet_SelfLetProperty57

    @selflet_SelfLetProperty57.setter
    def selflet_SelfLetProperty57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_selflet_SelfLetProperty__selflet_SelfLetProperty57", None)
        self.__selflet_SelfLetProperty57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "selflet_TypeKnowledge56"):
                opp_val = getattr(old_value, "selflet_TypeKnowledge56", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "selflet_TypeKnowledge56"):
                opp_val = getattr(value, "selflet_TypeKnowledge56", None)
                if opp_val is None:
                    setattr(value, "selflet_TypeKnowledge56", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class selflet_GeneralKnowledge:

    pass
class selflet_Empty:

    pass
class selflet_CPUUtilization:

    def __init__(self, lowerBound: str, upperBound: str):
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        
    @property
    def lowerBound(self) -> str:
        return self.__lowerBound

    @lowerBound.setter
    def lowerBound(self, lowerBound: str):
        self.__lowerBound = lowerBound

    @property
    def upperBound(self) -> str:
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: str):
        self.__upperBound = upperBound

class selflet_Condition:

    def __init__(self, file: str, selflet_Condition: "selflet_Conditions" = None):
        self.file = file
        self.selflet_Condition = selflet_Condition
        
    @property
    def file(self) -> str:
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = file

    @property
    def selflet_Condition(self):
        return self.__selflet_Condition

    @selflet_Condition.setter
    def selflet_Condition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_selflet_Condition__selflet_Condition", None)
        self.__selflet_Condition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "selflet_Conditions"):
                opp_val = getattr(old_value, "selflet_Conditions", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "selflet_Conditions"):
                opp_val = getattr(value, "selflet_Conditions", None)
                if opp_val is None:
                    setattr(value, "selflet_Conditions", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class selflet_Conditions:

    pass
class selflet_Service:

    def __init__(self, active: str, revenue: str, maxResponseTime: str, name: str, selflet_Service: "selflet_Behavior" = None, selflet_Service43: "selflet_Services" = None, selflet_Service45: "selflet_Input" = None, selflet_Service48: "selflet_Output" = None, selflet_Service51: "selflet_OfferMode" = None, selflet_Service53: set["selflet_Behavior"] = None, selflet_Service67: "selflet_IntermediateState" = None):
        self.active = active
        self.revenue = revenue
        self.maxResponseTime = maxResponseTime
        self.name = name
        self.selflet_Service = selflet_Service
        self.selflet_Service43 = selflet_Service43
        self.selflet_Service45 = selflet_Service45
        self.selflet_Service48 = selflet_Service48
        self.selflet_Service51 = selflet_Service51
        self.selflet_Service53 = selflet_Service53 if selflet_Service53 is not None else set()
        self.selflet_Service67 = selflet_Service67
        
    @property
    def maxResponseTime(self) -> str:
        return self.__maxResponseTime

    @maxResponseTime.setter
    def maxResponseTime(self, maxResponseTime: str):
        self.__maxResponseTime = maxResponseTime

    @property
    def revenue(self) -> str:
        return self.__revenue

    @revenue.setter
    def revenue(self, revenue: str):
        self.__revenue = revenue

    @property
    def active(self) -> str:
        return self.__active

    @active.setter
    def active(self, active: str):
        self.__active = active

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def selflet_Service43(self):
        return self.__selflet_Service43

    @selflet_Service43.setter
    def selflet_Service43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_selflet_Service__selflet_Service43", None)
        self.__selflet_Service43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "selflet_Services42"):
                opp_val = getattr(old_value, "selflet_Services42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "selflet_Services42"):
                opp_val = getattr(value, "selflet_Services42", None)
                if opp_val is None:
                    setattr(value, "selflet_Services42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def selflet_Service67(self):
        return self.__selflet_Service67

    @selflet_Service67.setter
    def selflet_Service67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_selflet_Service__selflet_Service67", None)
        self.__selflet_Service67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "selflet_IntermediateState"):
                opp_val = getattr(old_value, "selflet_IntermediateState", None)
                if opp_val == self:
                    setattr(old_value, "selflet_IntermediateState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "selflet_IntermediateState"):
                opp_val = getattr(value, "selflet_IntermediateState", None)
                setattr(value, "selflet_IntermediateState", self)

    @property
    def selflet_Service(self):
        return self.__selflet_Service

    @selflet_Service.setter
    def selflet_Service(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_selflet_Service__selflet_Service", None)
        self.__selflet_Service = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "selflet_Behavior"):
                opp_val = getattr(old_value, "selflet_Behavior", None)
                if opp_val == self:
                    setattr(old_value, "selflet_Behavior", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "selflet_Behavior"):
                opp_val = getattr(value, "selflet_Behavior", None)
                setattr(value, "selflet_Behavior", self)

    @property
    def selflet_Service53(self):
        return self.__selflet_Service53

    @selflet_Service53.setter
    def selflet_Service53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_selflet_Service__selflet_Service53", None)
        self.__selflet_Service53 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "selflet_Behavior54"):
                    opp_val = getattr(item, "selflet_Behavior54", None)
                    
                    if opp_val == self:
                        setattr(item, "selflet_Behavior54", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "selflet_Behavior54"):
                    opp_val = getattr(item, "selflet_Behavior54", None)
                    
                    setattr(item, "selflet_Behavior54", self)
                    

    @property
    def selflet_Service45(self):
        return self.__selflet_Service45

    @selflet_Service45.setter
    def selflet_Service45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_selflet_Service__selflet_Service45", None)
        self.__selflet_Service45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "selflet_Input46"):
                opp_val = getattr(old_value, "selflet_Input46", None)
                if opp_val == self:
                    setattr(old_value, "selflet_Input46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "selflet_Input46"):
                opp_val = getattr(value, "selflet_Input46", None)
                setattr(value, "selflet_Input46", self)

    @property
    def selflet_Service48(self):
        return self.__selflet_Service48

    @selflet_Service48.setter
    def selflet_Service48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_selflet_Service__selflet_Service48", None)
        self.__selflet_Service48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "selflet_Output49"):
                opp_val = getattr(old_value, "selflet_Output49", None)
                if opp_val == self:
                    setattr(old_value, "selflet_Output49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "selflet_Output49"):
                opp_val = getattr(value, "selflet_Output49", None)
                setattr(value, "selflet_Output49", self)

    @property
    def selflet_Service51(self):
        return self.__selflet_Service51

    @selflet_Service51.setter
    def selflet_Service51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_selflet_Service__selflet_Service51", None)
        self.__selflet_Service51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "selflet_OfferMode"):
                opp_val = getattr(old_value, "selflet_OfferMode", None)
                if opp_val == self:
                    setattr(old_value, "selflet_OfferMode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "selflet_OfferMode"):
                opp_val = getattr(value, "selflet_OfferMode", None)
                setattr(value, "selflet_OfferMode", self)

class selflet_Behavior:

    def __init__(self, elementaryBehaviorCost: str, elementaryBehaviorCPUTime: str, fileName: str, isDefaultBehavior: str, name: str, selflet_Behavior: "selflet_Service" = None, selflet_Behavior54: "selflet_Service" = None):
        self.elementaryBehaviorCost = elementaryBehaviorCost
        self.elementaryBehaviorCPUTime = elementaryBehaviorCPUTime
        self.fileName = fileName
        self.isDefaultBehavior = isDefaultBehavior
        self.name = name
        self.selflet_Behavior = selflet_Behavior
        self.selflet_Behavior54 = selflet_Behavior54
        
    @property
    def isDefaultBehavior(self) -> str:
        return self.__isDefaultBehavior

    @isDefaultBehavior.setter
    def isDefaultBehavior(self, isDefaultBehavior: str):
        self.__isDefaultBehavior = isDefaultBehavior

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def elementaryBehaviorCPUTime(self) -> str:
        return self.__elementaryBehaviorCPUTime

    @elementaryBehaviorCPUTime.setter
    def elementaryBehaviorCPUTime(self, elementaryBehaviorCPUTime: str):
        self.__elementaryBehaviorCPUTime = elementaryBehaviorCPUTime

    @property
    def fileName(self) -> str:
        return self.__fileName

    @fileName.setter
    def fileName(self, fileName: str):
        self.__fileName = fileName

    @property
    def elementaryBehaviorCost(self) -> str:
        return self.__elementaryBehaviorCost

    @elementaryBehaviorCost.setter
    def elementaryBehaviorCost(self, elementaryBehaviorCost: str):
        self.__elementaryBehaviorCost = elementaryBehaviorCost

    @property
    def selflet_Behavior(self):
        return self.__selflet_Behavior

    @selflet_Behavior.setter
    def selflet_Behavior(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_selflet_Behavior__selflet_Behavior", None)
        self.__selflet_Behavior = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "selflet_Service"):
                opp_val = getattr(old_value, "selflet_Service", None)
                if opp_val == self:
                    setattr(old_value, "selflet_Service", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "selflet_Service"):
                opp_val = getattr(value, "selflet_Service", None)
                setattr(value, "selflet_Service", self)

    @property
    def selflet_Behavior54(self):
        return self.__selflet_Behavior54

    @selflet_Behavior54.setter
    def selflet_Behavior54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_selflet_Behavior__selflet_Behavior54", None)
        self.__selflet_Behavior54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "selflet_Service53"):
                opp_val = getattr(old_value, "selflet_Service53", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "selflet_Service53"):
                opp_val = getattr(value, "selflet_Service53", None)
                if opp_val is None:
                    setattr(value, "selflet_Service53", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class selflet_Active:

    def __init__(self, mainService: str, selflet_Active: "selflet_SelfletProperties" = None):
        self.mainService = mainService
        self.selflet_Active = selflet_Active
        
    @property
    def mainService(self) -> str:
        return self.__mainService

    @mainService.setter
    def mainService(self, mainService: str):
        self.__mainService = mainService

    @property
    def selflet_Active(self):
        return self.__selflet_Active

    @selflet_Active.setter
    def selflet_Active(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_selflet_Active__selflet_Active", None)
        self.__selflet_Active = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "selflet_SelfletProperties19"):
                opp_val = getattr(old_value, "selflet_SelfletProperties19", None)
                if opp_val == self:
                    setattr(old_value, "selflet_SelfletProperties19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "selflet_SelfletProperties19"):
                opp_val = getattr(value, "selflet_SelfletProperties19", None)
                setattr(value, "selflet_SelfletProperties19", self)

class selflet_Action:

    def __init__(self, file: str, selflet_Action: "selflet_Actions" = None, selflet_Action65: "selflet_AbilityState" = None):
        self.file = file
        self.selflet_Action = selflet_Action
        self.selflet_Action65 = selflet_Action65
        
    @property
    def file(self) -> str:
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = file

    @property
    def selflet_Action(self):
        return self.__selflet_Action

    @selflet_Action.setter
    def selflet_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_selflet_Action__selflet_Action", None)
        self.__selflet_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "selflet_Actions"):
                opp_val = getattr(old_value, "selflet_Actions", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "selflet_Actions"):
                opp_val = getattr(value, "selflet_Actions", None)
                if opp_val is None:
                    setattr(value, "selflet_Actions", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def selflet_Action65(self):
        return self.__selflet_Action65

    @selflet_Action65.setter
    def selflet_Action65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_selflet_Action__selflet_Action65", None)
        self.__selflet_Action65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "selflet_AbilityState"):
                opp_val = getattr(old_value, "selflet_AbilityState", None)
                if opp_val == self:
                    setattr(old_value, "selflet_AbilityState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "selflet_AbilityState"):
                opp_val = getattr(value, "selflet_AbilityState", None)
                setattr(value, "selflet_AbilityState", self)

class selflet_Actions:

    pass
class selflet_Methods:

    pass
class selflet_Ability:

    def __init__(self, service: str, file: str, selflet_Ability: "selflet_Abilities" = None, selflet_Ability2: "selflet_Methods" = None):
        self.service = service
        self.file = file
        self.selflet_Ability = selflet_Ability
        self.selflet_Ability2 = selflet_Ability2
        
    @property
    def file(self) -> str:
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = file

    @property
    def service(self) -> str:
        return self.__service

    @service.setter
    def service(self, service: str):
        self.__service = service

    @property
    def selflet_Ability2(self):
        return self.__selflet_Ability2

    @selflet_Ability2.setter
    def selflet_Ability2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_selflet_Ability__selflet_Ability2", None)
        self.__selflet_Ability2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "selflet_Methods"):
                opp_val = getattr(old_value, "selflet_Methods", None)
                if opp_val == self:
                    setattr(old_value, "selflet_Methods", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "selflet_Methods"):
                opp_val = getattr(value, "selflet_Methods", None)
                setattr(value, "selflet_Methods", self)

    @property
    def selflet_Ability(self):
        return self.__selflet_Ability

    @selflet_Ability.setter
    def selflet_Ability(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_selflet_Ability__selflet_Ability", None)
        self.__selflet_Ability = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "selflet_Abilities"):
                opp_val = getattr(old_value, "selflet_Abilities", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "selflet_Abilities"):
                opp_val = getattr(value, "selflet_Abilities", None)
                if opp_val is None:
                    setattr(value, "selflet_Abilities", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class selflet_Abilities:

    pass