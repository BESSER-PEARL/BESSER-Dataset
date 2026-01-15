from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Element:

    pass
class dsl_Resource_Object(Element):

    pass
class dsl_Number_Object(Element):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class dsl_DiffElement(Element):

    pass
class dsl_EqualElement(Element):

    pass
class dsl_State_Object(Element):

    pass
class dsl_AndElement(Element):

    pass
class dsl_SmallerElement(Element):

    pass
class dsl_MultiplicationElement(Element):

    pass
class dsl_LargerElement(Element):

    pass
class dsl_MinusElement(Element):

    pass
class dsl_SmallerEqualElement(Element):

    pass
class dsl_NegateElement(Element):

    pass
class dsl_LargerEqualElement(Element):

    pass
class dsl_DivisionElement(Element):

    pass
class dsl_Boolean_Object(Element):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class dsl_PlusElement(Element):

    pass
class dsl_ModuloElement(Element):

    pass
class dsl_OrElement(Element):

    pass
class dsl_Action:

    pass
class dsl_Element:

    pass
class dsl_ElseDoSpec:

    pass
class dsl_ElseIfDoSpec:

    pass
class dsl_IfDoSpec:

    pass
class dsl_Trigger:

    pass
class dsl_Specification:

    def __init__(self, specID: str, priority: int, dsl_Specification: "dsl_AppMetaData" = None, dsl_Specification9: set["dsl_Trigger"] = None, dsl_Specification11: "dsl_IfDoSpec" = None, dsl_Specification13: set["dsl_ElseIfDoSpec"] = None, dsl_Specification15: "dsl_ElseDoSpec" = None):
        self.specID = specID
        self.priority = priority
        self.dsl_Specification = dsl_Specification
        self.dsl_Specification9 = dsl_Specification9 if dsl_Specification9 is not None else set()
        self.dsl_Specification11 = dsl_Specification11
        self.dsl_Specification13 = dsl_Specification13 if dsl_Specification13 is not None else set()
        self.dsl_Specification15 = dsl_Specification15
        
    @property
    def specID(self) -> str:
        return self.__specID

    @specID.setter
    def specID(self, specID: str):
        self.__specID = specID

    @property
    def priority(self) -> int:
        return self.__priority

    @priority.setter
    def priority(self, priority: int):
        self.__priority = priority

    @property
    def dsl_Specification11(self):
        return self.__dsl_Specification11

    @dsl_Specification11.setter
    def dsl_Specification11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Specification__dsl_Specification11", None)
        self.__dsl_Specification11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_IfDoSpec"):
                opp_val = getattr(old_value, "dsl_IfDoSpec", None)
                if opp_val == self:
                    setattr(old_value, "dsl_IfDoSpec", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_IfDoSpec"):
                opp_val = getattr(value, "dsl_IfDoSpec", None)
                setattr(value, "dsl_IfDoSpec", self)

    @property
    def dsl_Specification13(self):
        return self.__dsl_Specification13

    @dsl_Specification13.setter
    def dsl_Specification13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Specification__dsl_Specification13", None)
        self.__dsl_Specification13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dsl_ElseIfDoSpec"):
                    opp_val = getattr(item, "dsl_ElseIfDoSpec", None)
                    
                    if opp_val == self:
                        setattr(item, "dsl_ElseIfDoSpec", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dsl_ElseIfDoSpec"):
                    opp_val = getattr(item, "dsl_ElseIfDoSpec", None)
                    
                    setattr(item, "dsl_ElseIfDoSpec", self)
                    

    @property
    def dsl_Specification9(self):
        return self.__dsl_Specification9

    @dsl_Specification9.setter
    def dsl_Specification9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Specification__dsl_Specification9", None)
        self.__dsl_Specification9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dsl_Trigger"):
                    opp_val = getattr(item, "dsl_Trigger", None)
                    
                    if opp_val == self:
                        setattr(item, "dsl_Trigger", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dsl_Trigger"):
                    opp_val = getattr(item, "dsl_Trigger", None)
                    
                    setattr(item, "dsl_Trigger", self)
                    

    @property
    def dsl_Specification(self):
        return self.__dsl_Specification

    @dsl_Specification.setter
    def dsl_Specification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Specification__dsl_Specification", None)
        self.__dsl_Specification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_AppMetaData7"):
                opp_val = getattr(old_value, "dsl_AppMetaData7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_AppMetaData7"):
                opp_val = getattr(value, "dsl_AppMetaData7", None)
                if opp_val is None:
                    setattr(value, "dsl_AppMetaData7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dsl_Specification15(self):
        return self.__dsl_Specification15

    @dsl_Specification15.setter
    def dsl_Specification15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Specification__dsl_Specification15", None)
        self.__dsl_Specification15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_ElseDoSpec"):
                opp_val = getattr(old_value, "dsl_ElseDoSpec", None)
                if opp_val == self:
                    setattr(old_value, "dsl_ElseDoSpec", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_ElseDoSpec"):
                opp_val = getattr(value, "dsl_ElseDoSpec", None)
                setattr(value, "dsl_ElseDoSpec", self)

class Metadata:

    pass
class dsl_Resource:

    def __init__(self, name: str, dsl_Resource37: "dsl_EnvironmentMetaData" = None, dsl_Resource: set["dsl_State"] = None, dsl_Resource18: "dsl_Trigger" = None, dsl_Resource40: "dsl_Action" = None, dsl_Resource110: "dsl_Resource_Object" = None):
        self.name = name
        self.dsl_Resource37 = dsl_Resource37
        self.dsl_Resource = dsl_Resource if dsl_Resource is not None else set()
        self.dsl_Resource18 = dsl_Resource18
        self.dsl_Resource40 = dsl_Resource40
        self.dsl_Resource110 = dsl_Resource110
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dsl_Resource40(self):
        return self.__dsl_Resource40

    @dsl_Resource40.setter
    def dsl_Resource40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Resource__dsl_Resource40", None)
        self.__dsl_Resource40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Action39"):
                opp_val = getattr(old_value, "dsl_Action39", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Action39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Action39"):
                opp_val = getattr(value, "dsl_Action39", None)
                setattr(value, "dsl_Action39", self)

    @property
    def dsl_Resource37(self):
        return self.__dsl_Resource37

    @dsl_Resource37.setter
    def dsl_Resource37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Resource__dsl_Resource37", None)
        self.__dsl_Resource37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_EnvironmentMetaData36"):
                opp_val = getattr(old_value, "dsl_EnvironmentMetaData36", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_EnvironmentMetaData36"):
                opp_val = getattr(value, "dsl_EnvironmentMetaData36", None)
                if opp_val is None:
                    setattr(value, "dsl_EnvironmentMetaData36", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dsl_Resource(self):
        return self.__dsl_Resource

    @dsl_Resource.setter
    def dsl_Resource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Resource__dsl_Resource", None)
        self.__dsl_Resource = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dsl_State"):
                    opp_val = getattr(item, "dsl_State", None)
                    
                    if opp_val == self:
                        setattr(item, "dsl_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dsl_State"):
                    opp_val = getattr(item, "dsl_State", None)
                    
                    setattr(item, "dsl_State", self)
                    

    @property
    def dsl_Resource18(self):
        return self.__dsl_Resource18

    @dsl_Resource18.setter
    def dsl_Resource18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Resource__dsl_Resource18", None)
        self.__dsl_Resource18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Trigger17"):
                opp_val = getattr(old_value, "dsl_Trigger17", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Trigger17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Trigger17"):
                opp_val = getattr(value, "dsl_Trigger17", None)
                setattr(value, "dsl_Trigger17", self)

    @property
    def dsl_Resource110(self):
        return self.__dsl_Resource110

    @dsl_Resource110.setter
    def dsl_Resource110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Resource__dsl_Resource110", None)
        self.__dsl_Resource110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Resource_Object"):
                opp_val = getattr(old_value, "dsl_Resource_Object", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Resource_Object", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Resource_Object"):
                opp_val = getattr(value, "dsl_Resource_Object", None)
                setattr(value, "dsl_Resource_Object", self)

class dsl_State:

    def __init__(self, name: str, dsl_State: "dsl_Resource" = None, dsl_State21: "dsl_Trigger" = None, dsl_State43: "dsl_Action" = None, dsl_State112: "dsl_State_Object" = None):
        self.name = name
        self.dsl_State = dsl_State
        self.dsl_State21 = dsl_State21
        self.dsl_State43 = dsl_State43
        self.dsl_State112 = dsl_State112
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dsl_State112(self):
        return self.__dsl_State112

    @dsl_State112.setter
    def dsl_State112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_State__dsl_State112", None)
        self.__dsl_State112 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_State_Object"):
                opp_val = getattr(old_value, "dsl_State_Object", None)
                if opp_val == self:
                    setattr(old_value, "dsl_State_Object", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_State_Object"):
                opp_val = getattr(value, "dsl_State_Object", None)
                setattr(value, "dsl_State_Object", self)

    @property
    def dsl_State21(self):
        return self.__dsl_State21

    @dsl_State21.setter
    def dsl_State21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_State__dsl_State21", None)
        self.__dsl_State21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Trigger20"):
                opp_val = getattr(old_value, "dsl_Trigger20", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Trigger20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Trigger20"):
                opp_val = getattr(value, "dsl_Trigger20", None)
                setattr(value, "dsl_Trigger20", self)

    @property
    def dsl_State(self):
        return self.__dsl_State

    @dsl_State.setter
    def dsl_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_State__dsl_State", None)
        self.__dsl_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Resource"):
                opp_val = getattr(old_value, "dsl_Resource", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Resource"):
                opp_val = getattr(value, "dsl_Resource", None)
                if opp_val is None:
                    setattr(value, "dsl_Resource", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dsl_State43(self):
        return self.__dsl_State43

    @dsl_State43.setter
    def dsl_State43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_State__dsl_State43", None)
        self.__dsl_State43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Action42"):
                opp_val = getattr(old_value, "dsl_Action42", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Action42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Action42"):
                opp_val = getattr(value, "dsl_Action42", None)
                setattr(value, "dsl_Action42", self)

class dsl_Metadata:

    pass
class dsl_ServiceMetaData(Metadata):

    def __init__(self, serviceID: str, dsl_ServiceMetaData: "dsl_RunTimeModel" = None):
        self.serviceID = serviceID
        self.dsl_ServiceMetaData = dsl_ServiceMetaData
        
    @property
    def serviceID(self) -> str:
        return self.__serviceID

    @serviceID.setter
    def serviceID(self, serviceID: str):
        self.__serviceID = serviceID

    @property
    def dsl_ServiceMetaData(self):
        return self.__dsl_ServiceMetaData

    @dsl_ServiceMetaData.setter
    def dsl_ServiceMetaData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_ServiceMetaData__dsl_ServiceMetaData", None)
        self.__dsl_ServiceMetaData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_RunTimeModel4"):
                opp_val = getattr(old_value, "dsl_RunTimeModel4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_RunTimeModel4"):
                opp_val = getattr(value, "dsl_RunTimeModel4", None)
                if opp_val is None:
                    setattr(value, "dsl_RunTimeModel4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dsl_AppMetaData(Metadata):

    def __init__(self, appID: str, dsl_AppMetaData: "dsl_RunTimeModel" = None, dsl_AppMetaData7: set["dsl_Specification"] = None):
        self.appID = appID
        self.dsl_AppMetaData = dsl_AppMetaData
        self.dsl_AppMetaData7 = dsl_AppMetaData7 if dsl_AppMetaData7 is not None else set()
        
    @property
    def appID(self) -> str:
        return self.__appID

    @appID.setter
    def appID(self, appID: str):
        self.__appID = appID

    @property
    def dsl_AppMetaData(self):
        return self.__dsl_AppMetaData

    @dsl_AppMetaData.setter
    def dsl_AppMetaData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_AppMetaData__dsl_AppMetaData", None)
        self.__dsl_AppMetaData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_RunTimeModel2"):
                opp_val = getattr(old_value, "dsl_RunTimeModel2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_RunTimeModel2"):
                opp_val = getattr(value, "dsl_RunTimeModel2", None)
                if opp_val is None:
                    setattr(value, "dsl_RunTimeModel2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dsl_AppMetaData7(self):
        return self.__dsl_AppMetaData7

    @dsl_AppMetaData7.setter
    def dsl_AppMetaData7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_AppMetaData__dsl_AppMetaData7", None)
        self.__dsl_AppMetaData7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dsl_Specification"):
                    opp_val = getattr(item, "dsl_Specification", None)
                    
                    if opp_val == self:
                        setattr(item, "dsl_Specification", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dsl_Specification"):
                    opp_val = getattr(item, "dsl_Specification", None)
                    
                    setattr(item, "dsl_Specification", self)
                    

class dsl_EnvironmentMetaData(Metadata):

    pass
class dsl_RunTimeModel:

    pass