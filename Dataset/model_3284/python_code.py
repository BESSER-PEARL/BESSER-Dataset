from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class smachDSL_Transition:

    def __init__(self, outcome: str, smachDSL_Transition: "smachDSL_ActionState" = None, smachDSL_Transition13: "smachDSL_ActionState" = None):
        self.outcome = outcome
        self.smachDSL_Transition = smachDSL_Transition
        self.smachDSL_Transition13 = smachDSL_Transition13
        
    @property
    def outcome(self) -> str:
        return self.__outcome

    @outcome.setter
    def outcome(self, outcome: str):
        self.__outcome = outcome

    @property
    def smachDSL_Transition(self):
        return self.__smachDSL_Transition

    @smachDSL_Transition.setter
    def smachDSL_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smachDSL_Transition__smachDSL_Transition", None)
        self.__smachDSL_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smachDSL_ActionState11"):
                opp_val = getattr(old_value, "smachDSL_ActionState11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smachDSL_ActionState11"):
                opp_val = getattr(value, "smachDSL_ActionState11", None)
                if opp_val is None:
                    setattr(value, "smachDSL_ActionState11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def smachDSL_Transition13(self):
        return self.__smachDSL_Transition13

    @smachDSL_Transition13.setter
    def smachDSL_Transition13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smachDSL_Transition__smachDSL_Transition13", None)
        self.__smachDSL_Transition13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smachDSL_ActionState14"):
                opp_val = getattr(old_value, "smachDSL_ActionState14", None)
                if opp_val == self:
                    setattr(old_value, "smachDSL_ActionState14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smachDSL_ActionState14"):
                opp_val = getattr(value, "smachDSL_ActionState14", None)
                setattr(value, "smachDSL_ActionState14", self)

class smachDSL_ActionState:

    def __init__(self, name: str, smachDSL_ActionState: "smachDSL_StateMachine" = None, smachDSL_ActionState8: "smachDSL_ActionClient" = None, smachDSL_ActionState11: set["smachDSL_Transition"] = None, smachDSL_ActionState14: "smachDSL_Transition" = None):
        self.name = name
        self.smachDSL_ActionState = smachDSL_ActionState
        self.smachDSL_ActionState8 = smachDSL_ActionState8
        self.smachDSL_ActionState11 = smachDSL_ActionState11 if smachDSL_ActionState11 is not None else set()
        self.smachDSL_ActionState14 = smachDSL_ActionState14
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def smachDSL_ActionState14(self):
        return self.__smachDSL_ActionState14

    @smachDSL_ActionState14.setter
    def smachDSL_ActionState14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smachDSL_ActionState__smachDSL_ActionState14", None)
        self.__smachDSL_ActionState14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smachDSL_Transition13"):
                opp_val = getattr(old_value, "smachDSL_Transition13", None)
                if opp_val == self:
                    setattr(old_value, "smachDSL_Transition13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smachDSL_Transition13"):
                opp_val = getattr(value, "smachDSL_Transition13", None)
                setattr(value, "smachDSL_Transition13", self)

    @property
    def smachDSL_ActionState11(self):
        return self.__smachDSL_ActionState11

    @smachDSL_ActionState11.setter
    def smachDSL_ActionState11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smachDSL_ActionState__smachDSL_ActionState11", None)
        self.__smachDSL_ActionState11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smachDSL_Transition"):
                    opp_val = getattr(item, "smachDSL_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "smachDSL_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smachDSL_Transition"):
                    opp_val = getattr(item, "smachDSL_Transition", None)
                    
                    setattr(item, "smachDSL_Transition", self)
                    

    @property
    def smachDSL_ActionState8(self):
        return self.__smachDSL_ActionState8

    @smachDSL_ActionState8.setter
    def smachDSL_ActionState8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smachDSL_ActionState__smachDSL_ActionState8", None)
        self.__smachDSL_ActionState8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smachDSL_ActionClient9"):
                opp_val = getattr(old_value, "smachDSL_ActionClient9", None)
                if opp_val == self:
                    setattr(old_value, "smachDSL_ActionClient9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smachDSL_ActionClient9"):
                opp_val = getattr(value, "smachDSL_ActionClient9", None)
                setattr(value, "smachDSL_ActionClient9", self)

    @property
    def smachDSL_ActionState(self):
        return self.__smachDSL_ActionState

    @smachDSL_ActionState.setter
    def smachDSL_ActionState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smachDSL_ActionState__smachDSL_ActionState", None)
        self.__smachDSL_ActionState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smachDSL_StateMachine6"):
                opp_val = getattr(old_value, "smachDSL_StateMachine6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smachDSL_StateMachine6"):
                opp_val = getattr(value, "smachDSL_StateMachine6", None)
                if opp_val is None:
                    setattr(value, "smachDSL_StateMachine6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class smachDSL_ServiceClient:

    def __init__(self, name: str, servicename: str, servicesrv: str, smachDSL_ServiceClient: "smachDSL_StateMachine" = None):
        self.name = name
        self.servicename = servicename
        self.servicesrv = servicesrv
        self.smachDSL_ServiceClient = smachDSL_ServiceClient
        
    @property
    def servicename(self) -> str:
        return self.__servicename

    @servicename.setter
    def servicename(self, servicename: str):
        self.__servicename = servicename

    @property
    def servicesrv(self) -> str:
        return self.__servicesrv

    @servicesrv.setter
    def servicesrv(self, servicesrv: str):
        self.__servicesrv = servicesrv

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def smachDSL_ServiceClient(self):
        return self.__smachDSL_ServiceClient

    @smachDSL_ServiceClient.setter
    def smachDSL_ServiceClient(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smachDSL_ServiceClient__smachDSL_ServiceClient", None)
        self.__smachDSL_ServiceClient = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smachDSL_StateMachine4"):
                opp_val = getattr(old_value, "smachDSL_StateMachine4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smachDSL_StateMachine4"):
                opp_val = getattr(value, "smachDSL_StateMachine4", None)
                if opp_val is None:
                    setattr(value, "smachDSL_StateMachine4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class smachDSL_ActionClient:

    def __init__(self, name: str, actionname: str, actiontype: str, smachDSL_ActionClient: "smachDSL_StateMachine" = None, smachDSL_ActionClient9: "smachDSL_ActionState" = None):
        self.name = name
        self.actionname = actionname
        self.actiontype = actiontype
        self.smachDSL_ActionClient = smachDSL_ActionClient
        self.smachDSL_ActionClient9 = smachDSL_ActionClient9
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def actionname(self) -> str:
        return self.__actionname

    @actionname.setter
    def actionname(self, actionname: str):
        self.__actionname = actionname

    @property
    def actiontype(self) -> str:
        return self.__actiontype

    @actiontype.setter
    def actiontype(self, actiontype: str):
        self.__actiontype = actiontype

    @property
    def smachDSL_ActionClient(self):
        return self.__smachDSL_ActionClient

    @smachDSL_ActionClient.setter
    def smachDSL_ActionClient(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smachDSL_ActionClient__smachDSL_ActionClient", None)
        self.__smachDSL_ActionClient = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smachDSL_StateMachine2"):
                opp_val = getattr(old_value, "smachDSL_StateMachine2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smachDSL_StateMachine2"):
                opp_val = getattr(value, "smachDSL_StateMachine2", None)
                if opp_val is None:
                    setattr(value, "smachDSL_StateMachine2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def smachDSL_ActionClient9(self):
        return self.__smachDSL_ActionClient9

    @smachDSL_ActionClient9.setter
    def smachDSL_ActionClient9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smachDSL_ActionClient__smachDSL_ActionClient9", None)
        self.__smachDSL_ActionClient9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smachDSL_ActionState8"):
                opp_val = getattr(old_value, "smachDSL_ActionState8", None)
                if opp_val == self:
                    setattr(old_value, "smachDSL_ActionState8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smachDSL_ActionState8"):
                opp_val = getattr(value, "smachDSL_ActionState8", None)
                setattr(value, "smachDSL_ActionState8", self)

class smachDSL_Test:

    def __init__(self, ros: str):
        self.ros = ros
        
    @property
    def ros(self) -> str:
        return self.__ros

    @ros.setter
    def ros(self, ros: str):
        self.__ros = ros

class smachDSL_StateMachine:

    def __init__(self, name: str, smachDSL_StateMachine: "smachDSL_PrimitivePackage" = None, smachDSL_StateMachine2: set["smachDSL_ActionClient"] = None, smachDSL_StateMachine4: set["smachDSL_ServiceClient"] = None, smachDSL_StateMachine6: set["smachDSL_ActionState"] = None):
        self.name = name
        self.smachDSL_StateMachine = smachDSL_StateMachine
        self.smachDSL_StateMachine2 = smachDSL_StateMachine2 if smachDSL_StateMachine2 is not None else set()
        self.smachDSL_StateMachine4 = smachDSL_StateMachine4 if smachDSL_StateMachine4 is not None else set()
        self.smachDSL_StateMachine6 = smachDSL_StateMachine6 if smachDSL_StateMachine6 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def smachDSL_StateMachine2(self):
        return self.__smachDSL_StateMachine2

    @smachDSL_StateMachine2.setter
    def smachDSL_StateMachine2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smachDSL_StateMachine__smachDSL_StateMachine2", None)
        self.__smachDSL_StateMachine2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smachDSL_ActionClient"):
                    opp_val = getattr(item, "smachDSL_ActionClient", None)
                    
                    if opp_val == self:
                        setattr(item, "smachDSL_ActionClient", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smachDSL_ActionClient"):
                    opp_val = getattr(item, "smachDSL_ActionClient", None)
                    
                    setattr(item, "smachDSL_ActionClient", self)
                    

    @property
    def smachDSL_StateMachine6(self):
        return self.__smachDSL_StateMachine6

    @smachDSL_StateMachine6.setter
    def smachDSL_StateMachine6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smachDSL_StateMachine__smachDSL_StateMachine6", None)
        self.__smachDSL_StateMachine6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smachDSL_ActionState"):
                    opp_val = getattr(item, "smachDSL_ActionState", None)
                    
                    if opp_val == self:
                        setattr(item, "smachDSL_ActionState", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smachDSL_ActionState"):
                    opp_val = getattr(item, "smachDSL_ActionState", None)
                    
                    setattr(item, "smachDSL_ActionState", self)
                    

    @property
    def smachDSL_StateMachine(self):
        return self.__smachDSL_StateMachine

    @smachDSL_StateMachine.setter
    def smachDSL_StateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smachDSL_StateMachine__smachDSL_StateMachine", None)
        self.__smachDSL_StateMachine = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smachDSL_PrimitivePackage"):
                opp_val = getattr(old_value, "smachDSL_PrimitivePackage", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smachDSL_PrimitivePackage"):
                opp_val = getattr(value, "smachDSL_PrimitivePackage", None)
                if opp_val is None:
                    setattr(value, "smachDSL_PrimitivePackage", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def smachDSL_StateMachine4(self):
        return self.__smachDSL_StateMachine4

    @smachDSL_StateMachine4.setter
    def smachDSL_StateMachine4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smachDSL_StateMachine__smachDSL_StateMachine4", None)
        self.__smachDSL_StateMachine4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smachDSL_ServiceClient"):
                    opp_val = getattr(item, "smachDSL_ServiceClient", None)
                    
                    if opp_val == self:
                        setattr(item, "smachDSL_ServiceClient", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smachDSL_ServiceClient"):
                    opp_val = getattr(item, "smachDSL_ServiceClient", None)
                    
                    setattr(item, "smachDSL_ServiceClient", self)
                    

class smachDSL_PrimitivePackage:

    pass