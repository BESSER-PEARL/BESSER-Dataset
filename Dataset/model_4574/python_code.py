from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class dsl_ElseDoSpec:

    pass
class dsl_ElseIfDoSpec:

    pass
class dsl_IfDoSpec:

    pass
class dsl_Trigger:

    pass
class Element:

    pass
class dsl_SmallerElement(Element):

    pass
class dsl_AndElement(Element):

    pass
class dsl_DivisionElement(Element):

    pass
class dsl_Resource_Object(Element):

    pass
class dsl_LargerEqualElement(Element):

    pass
class dsl_NegateElement(Element):

    pass
class dsl_State_Object(Element):

    pass
class dsl_SmallerEqualElement(Element):

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

class dsl_LargerElement(Element):

    pass
class dsl_EqualElement(Element):

    pass
class dsl_MultiplicationElement(Element):

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
class dsl_ModuloElement(Element):

    pass
class dsl_MinusElement(Element):

    pass
class dsl_PlusElement(Element):

    pass
class dsl_OrElement(Element):

    pass
class dsl_Action:

    pass
class dsl_Element:

    pass
class dsl_Specification:

    def __init__(self, specID: str, priority: int, dsl_Specification: "dsl_AppMetaData" = None, dsl_Specification7: set["dsl_Trigger"] = None, dsl_Specification9: "dsl_IfDoSpec" = None, dsl_Specification11: set["dsl_ElseIfDoSpec"] = None, dsl_Specification13: "dsl_ElseDoSpec" = None):
        self.specID = specID
        self.priority = priority
        self.dsl_Specification = dsl_Specification
        self.dsl_Specification7 = dsl_Specification7 if dsl_Specification7 is not None else set()
        self.dsl_Specification9 = dsl_Specification9
        self.dsl_Specification11 = dsl_Specification11 if dsl_Specification11 is not None else set()
        self.dsl_Specification13 = dsl_Specification13
        
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
    def dsl_Specification13(self):
        return self.__dsl_Specification13

    @dsl_Specification13.setter
    def dsl_Specification13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Specification__dsl_Specification13", None)
        self.__dsl_Specification13 = value
        
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

    @property
    def dsl_Specification9(self):
        return self.__dsl_Specification9

    @dsl_Specification9.setter
    def dsl_Specification9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Specification__dsl_Specification9", None)
        self.__dsl_Specification9 = value
        
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
    def dsl_Specification7(self):
        return self.__dsl_Specification7

    @dsl_Specification7.setter
    def dsl_Specification7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Specification__dsl_Specification7", None)
        self.__dsl_Specification7 = value if value is not None else set()
        
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
    def dsl_Specification11(self):
        return self.__dsl_Specification11

    @dsl_Specification11.setter
    def dsl_Specification11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Specification__dsl_Specification11", None)
        self.__dsl_Specification11 = value if value is not None else set()
        
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
    def dsl_Specification(self):
        return self.__dsl_Specification

    @dsl_Specification.setter
    def dsl_Specification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Specification__dsl_Specification", None)
        self.__dsl_Specification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_AppMetaData5"):
                opp_val = getattr(old_value, "dsl_AppMetaData5", None)
                if opp_val == self:
                    setattr(old_value, "dsl_AppMetaData5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_AppMetaData5"):
                opp_val = getattr(value, "dsl_AppMetaData5", None)
                setattr(value, "dsl_AppMetaData5", self)

class dsl_Resource:

    def __init__(self, name: str, dsl_Resource: set["dsl_State"] = None, dsl_Resource16: "dsl_Trigger" = None, dsl_Resource35: "dsl_EnvironmentMetaData" = None, dsl_Resource38: "dsl_Action" = None, dsl_Resource108: "dsl_Resource_Object" = None):
        self.name = name
        self.dsl_Resource = dsl_Resource if dsl_Resource is not None else set()
        self.dsl_Resource16 = dsl_Resource16
        self.dsl_Resource35 = dsl_Resource35
        self.dsl_Resource38 = dsl_Resource38
        self.dsl_Resource108 = dsl_Resource108
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dsl_Resource38(self):
        return self.__dsl_Resource38

    @dsl_Resource38.setter
    def dsl_Resource38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Resource__dsl_Resource38", None)
        self.__dsl_Resource38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Action37"):
                opp_val = getattr(old_value, "dsl_Action37", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Action37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Action37"):
                opp_val = getattr(value, "dsl_Action37", None)
                setattr(value, "dsl_Action37", self)

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
    def dsl_Resource108(self):
        return self.__dsl_Resource108

    @dsl_Resource108.setter
    def dsl_Resource108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Resource__dsl_Resource108", None)
        self.__dsl_Resource108 = value
        
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

    @property
    def dsl_Resource35(self):
        return self.__dsl_Resource35

    @dsl_Resource35.setter
    def dsl_Resource35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Resource__dsl_Resource35", None)
        self.__dsl_Resource35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_EnvironmentMetaData34"):
                opp_val = getattr(old_value, "dsl_EnvironmentMetaData34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_EnvironmentMetaData34"):
                opp_val = getattr(value, "dsl_EnvironmentMetaData34", None)
                if opp_val is None:
                    setattr(value, "dsl_EnvironmentMetaData34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dsl_Resource16(self):
        return self.__dsl_Resource16

    @dsl_Resource16.setter
    def dsl_Resource16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Resource__dsl_Resource16", None)
        self.__dsl_Resource16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Trigger15"):
                opp_val = getattr(old_value, "dsl_Trigger15", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Trigger15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Trigger15"):
                opp_val = getattr(value, "dsl_Trigger15", None)
                setattr(value, "dsl_Trigger15", self)

class dsl_State:

    def __init__(self, name: str, dsl_State: "dsl_Resource" = None, dsl_State19: "dsl_Trigger" = None, dsl_State41: "dsl_Action" = None, dsl_State110: "dsl_State_Object" = None):
        self.name = name
        self.dsl_State = dsl_State
        self.dsl_State19 = dsl_State19
        self.dsl_State41 = dsl_State41
        self.dsl_State110 = dsl_State110
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dsl_State110(self):
        return self.__dsl_State110

    @dsl_State110.setter
    def dsl_State110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_State__dsl_State110", None)
        self.__dsl_State110 = value
        
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
    def dsl_State41(self):
        return self.__dsl_State41

    @dsl_State41.setter
    def dsl_State41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_State__dsl_State41", None)
        self.__dsl_State41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Action40"):
                opp_val = getattr(old_value, "dsl_Action40", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Action40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Action40"):
                opp_val = getattr(value, "dsl_Action40", None)
                setattr(value, "dsl_Action40", self)

    @property
    def dsl_State19(self):
        return self.__dsl_State19

    @dsl_State19.setter
    def dsl_State19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_State__dsl_State19", None)
        self.__dsl_State19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Trigger18"):
                opp_val = getattr(old_value, "dsl_Trigger18", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Trigger18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Trigger18"):
                opp_val = getattr(value, "dsl_Trigger18", None)
                setattr(value, "dsl_Trigger18", self)

class dsl_AppMetaData:

    def __init__(self, appID: str, dsl_AppMetaData: "dsl_RunTimeModel" = None, dsl_AppMetaData5: "dsl_Specification" = None):
        self.appID = appID
        self.dsl_AppMetaData = dsl_AppMetaData
        self.dsl_AppMetaData5 = dsl_AppMetaData5
        
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
    def dsl_AppMetaData5(self):
        return self.__dsl_AppMetaData5

    @dsl_AppMetaData5.setter
    def dsl_AppMetaData5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_AppMetaData__dsl_AppMetaData5", None)
        self.__dsl_AppMetaData5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Specification"):
                opp_val = getattr(old_value, "dsl_Specification", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Specification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Specification"):
                opp_val = getattr(value, "dsl_Specification", None)
                setattr(value, "dsl_Specification", self)

class dsl_EnvironmentMetaData:

    pass
class dsl_RunTimeModel:

    pass