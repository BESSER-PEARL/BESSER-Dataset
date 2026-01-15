from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class ArchElementToArchElement:

    pass
class safetyDSL_Commands(ArchElementToArchElement):

    pass
class safetyDSL_Writes(ArchElementToArchElement):

    pass
class safetyDSL_Reads(ArchElementToArchElement):

    pass
class State:

    pass
class safetyDSL_SafeState(State):

    pass
class MonitorToArchitecturalElement:

    pass
class safetyDSL_Starts(MonitorToArchitecturalElement):

    pass
class safetyDSL_Restarts(MonitorToArchitecturalElement):

    pass
class safetyDSL_Monitors(MonitorToArchitecturalElement):

    pass
class safetyDSL_Inits(MonitorToArchitecturalElement):

    pass
class safetyDSL_Stops(MonitorToArchitecturalElement):

    pass
class safetyDSL_ClassTestCaseRelation:

    def __init__(self, testCases: str, safetyDSL_ClassTestCaseRelation72: "safetyDSL_ClassDef" = None, safetyDSL_ClassTestCaseRelation: "safetyDSL_ImplementationDetail" = None):
        self.testCases = testCases
        self.safetyDSL_ClassTestCaseRelation72 = safetyDSL_ClassTestCaseRelation72
        self.safetyDSL_ClassTestCaseRelation = safetyDSL_ClassTestCaseRelation
        
    @property
    def testCases(self) -> str:
        return self.__testCases

    @testCases.setter
    def testCases(self, testCases: str):
        self.__testCases = testCases

    @property
    def safetyDSL_ClassTestCaseRelation(self):
        return self.__safetyDSL_ClassTestCaseRelation

    @safetyDSL_ClassTestCaseRelation.setter
    def safetyDSL_ClassTestCaseRelation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_safetyDSL_ClassTestCaseRelation__safetyDSL_ClassTestCaseRelation", None)
        self.__safetyDSL_ClassTestCaseRelation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "safetyDSL_ImplementationDetail65"):
                opp_val = getattr(old_value, "safetyDSL_ImplementationDetail65", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "safetyDSL_ImplementationDetail65"):
                opp_val = getattr(value, "safetyDSL_ImplementationDetail65", None)
                if opp_val is None:
                    setattr(value, "safetyDSL_ImplementationDetail65", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def safetyDSL_ClassTestCaseRelation72(self):
        return self.__safetyDSL_ClassTestCaseRelation72

    @safetyDSL_ClassTestCaseRelation72.setter
    def safetyDSL_ClassTestCaseRelation72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_safetyDSL_ClassTestCaseRelation__safetyDSL_ClassTestCaseRelation72", None)
        self.__safetyDSL_ClassTestCaseRelation72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "safetyDSL_ClassDef73"):
                opp_val = getattr(old_value, "safetyDSL_ClassDef73", None)
                if opp_val == self:
                    setattr(old_value, "safetyDSL_ClassDef73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "safetyDSL_ClassDef73"):
                opp_val = getattr(value, "safetyDSL_ClassDef73", None)
                setattr(value, "safetyDSL_ClassDef73", self)

class safetyDSL_ModuleClassRelation:

    pass
class CriticalityLevel:

    pass
class safetyDSL_LevelD(CriticalityLevel):

    pass
class safetyDSL_LevelC(CriticalityLevel):

    pass
class safetyDSL_LevelB(CriticalityLevel):

    pass
class safetyDSL_LevelA(CriticalityLevel):

    pass
class FaultTreeNode:

    pass
class safetyDSL_ANDNodeExpression(FaultTreeNode):

    pass
class safetyDSL_ORNodeExpression(FaultTreeNode):

    pass
class safetyDSL_ClassDef:

    def __init__(self, name: str, safetyDSL_ClassDef: "safetyDSL_ModuleClassRelation" = None, safetyDSL_ClassDef73: "safetyDSL_ClassTestCaseRelation" = None):
        self.name = name
        self.safetyDSL_ClassDef = safetyDSL_ClassDef
        self.safetyDSL_ClassDef73 = safetyDSL_ClassDef73
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def safetyDSL_ClassDef(self):
        return self.__safetyDSL_ClassDef

    @safetyDSL_ClassDef.setter
    def safetyDSL_ClassDef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_safetyDSL_ClassDef__safetyDSL_ClassDef", None)
        self.__safetyDSL_ClassDef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "safetyDSL_ModuleClassRelation70"):
                opp_val = getattr(old_value, "safetyDSL_ModuleClassRelation70", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "safetyDSL_ModuleClassRelation70"):
                opp_val = getattr(value, "safetyDSL_ModuleClassRelation70", None)
                if opp_val is None:
                    setattr(value, "safetyDSL_ModuleClassRelation70", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def safetyDSL_ClassDef73(self):
        return self.__safetyDSL_ClassDef73

    @safetyDSL_ClassDef73.setter
    def safetyDSL_ClassDef73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_safetyDSL_ClassDef__safetyDSL_ClassDef73", None)
        self.__safetyDSL_ClassDef73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "safetyDSL_ClassTestCaseRelation72"):
                opp_val = getattr(old_value, "safetyDSL_ClassTestCaseRelation72", None)
                if opp_val == self:
                    setattr(old_value, "safetyDSL_ClassTestCaseRelation72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "safetyDSL_ClassTestCaseRelation72"):
                opp_val = getattr(value, "safetyDSL_ClassTestCaseRelation72", None)
                setattr(value, "safetyDSL_ClassTestCaseRelation72", self)

class SafetyCriticalRelation:

    pass
class safetyDSL_ArchElementToArchElement(SafetyCriticalRelation):

    pass
class safetyDSL_ReportsFault(SafetyCriticalRelation):

    pass
class safetyDSL_MonitorToArchitecturalElement(SafetyCriticalRelation):

    pass
class safetyDSL_SafetyCriticalRelation:

    pass
class safetyDSL_ArchitecturalElement:

    def __init__(self, name: str, safetyDSL_ArchitecturalElement: "safetyDSL_SafetyCriticalViewpoint" = None, safetyDSL_ArchitecturalElement48: "safetyDSL_ArchElementToArchElement" = None, safetyDSL_ArchitecturalElement51: "safetyDSL_ArchElementToArchElement" = None, safetyDSL_ArchitecturalElement68: "safetyDSL_ModuleClassRelation" = None):
        self.name = name
        self.safetyDSL_ArchitecturalElement = safetyDSL_ArchitecturalElement
        self.safetyDSL_ArchitecturalElement48 = safetyDSL_ArchitecturalElement48
        self.safetyDSL_ArchitecturalElement51 = safetyDSL_ArchitecturalElement51
        self.safetyDSL_ArchitecturalElement68 = safetyDSL_ArchitecturalElement68
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def safetyDSL_ArchitecturalElement68(self):
        return self.__safetyDSL_ArchitecturalElement68

    @safetyDSL_ArchitecturalElement68.setter
    def safetyDSL_ArchitecturalElement68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_safetyDSL_ArchitecturalElement__safetyDSL_ArchitecturalElement68", None)
        self.__safetyDSL_ArchitecturalElement68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "safetyDSL_ModuleClassRelation67"):
                opp_val = getattr(old_value, "safetyDSL_ModuleClassRelation67", None)
                if opp_val == self:
                    setattr(old_value, "safetyDSL_ModuleClassRelation67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "safetyDSL_ModuleClassRelation67"):
                opp_val = getattr(value, "safetyDSL_ModuleClassRelation67", None)
                setattr(value, "safetyDSL_ModuleClassRelation67", self)

    @property
    def safetyDSL_ArchitecturalElement(self):
        return self.__safetyDSL_ArchitecturalElement

    @safetyDSL_ArchitecturalElement.setter
    def safetyDSL_ArchitecturalElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_safetyDSL_ArchitecturalElement__safetyDSL_ArchitecturalElement", None)
        self.__safetyDSL_ArchitecturalElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "safetyDSL_SafetyCriticalViewpoint"):
                opp_val = getattr(old_value, "safetyDSL_SafetyCriticalViewpoint", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "safetyDSL_SafetyCriticalViewpoint"):
                opp_val = getattr(value, "safetyDSL_SafetyCriticalViewpoint", None)
                if opp_val is None:
                    setattr(value, "safetyDSL_SafetyCriticalViewpoint", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def safetyDSL_ArchitecturalElement48(self):
        return self.__safetyDSL_ArchitecturalElement48

    @safetyDSL_ArchitecturalElement48.setter
    def safetyDSL_ArchitecturalElement48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_safetyDSL_ArchitecturalElement__safetyDSL_ArchitecturalElement48", None)
        self.__safetyDSL_ArchitecturalElement48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "safetyDSL_ArchElementToArchElement"):
                opp_val = getattr(old_value, "safetyDSL_ArchElementToArchElement", None)
                if opp_val == self:
                    setattr(old_value, "safetyDSL_ArchElementToArchElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "safetyDSL_ArchElementToArchElement"):
                opp_val = getattr(value, "safetyDSL_ArchElementToArchElement", None)
                setattr(value, "safetyDSL_ArchElementToArchElement", self)

    @property
    def safetyDSL_ArchitecturalElement51(self):
        return self.__safetyDSL_ArchitecturalElement51

    @safetyDSL_ArchitecturalElement51.setter
    def safetyDSL_ArchitecturalElement51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_safetyDSL_ArchitecturalElement__safetyDSL_ArchitecturalElement51", None)
        self.__safetyDSL_ArchitecturalElement51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "safetyDSL_ArchElementToArchElement50"):
                opp_val = getattr(old_value, "safetyDSL_ArchElementToArchElement50", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "safetyDSL_ArchElementToArchElement50"):
                opp_val = getattr(value, "safetyDSL_ArchElementToArchElement50", None)
                if opp_val is None:
                    setattr(value, "safetyDSL_ArchElementToArchElement50", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class safetyDSL_State:

    def __init__(self, name: str, safetyDSL_State: "safetyDSL_SafetyCritical" = None):
        self.name = name
        self.safetyDSL_State = safetyDSL_State
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def safetyDSL_State(self):
        return self.__safetyDSL_State

    @safetyDSL_State.setter
    def safetyDSL_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_safetyDSL_State__safetyDSL_State", None)
        self.__safetyDSL_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "safetyDSL_SafetyCritical42"):
                opp_val = getattr(old_value, "safetyDSL_SafetyCritical42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "safetyDSL_SafetyCritical42"):
                opp_val = getattr(value, "safetyDSL_SafetyCritical42", None)
                if opp_val is None:
                    setattr(value, "safetyDSL_SafetyCritical42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class safetyDSL_CriticalityLevel:

    pass
class ArchitecturalElement:

    pass
class safetyDSL_NonSafetyCritical(ArchitecturalElement):

    pass
class safetyDSL_Monitor(ArchitecturalElement):

    pass
class safetyDSL_SafetyCritical(ArchitecturalElement):

    pass
class HazardRelation:

    pass
class safetyDSL_Causes(HazardRelation):

    pass
class safetyDSL_DerivedFrom(HazardRelation):

    pass
class SafetyTactic:

    pass
class safetyDSL_FaultContainment(SafetyTactic):

    pass
class safetyDSL_FaultDetection(SafetyTactic):

    pass
class safetyDSL_FaultAvoidance(SafetyTactic):

    pass
class safetyDSL_SafetyTactic:

    def __init__(self, name: str, type: str, safetyDSL_SafetyTactic: "safetyDSL_SafetyTacticViewpoint" = None, safetyDSL_SafetyTactic26: set["safetyDSL_Fault"] = None, safetyDSL_SafetyTactic37: "safetyDSL_SafetyCritical" = None, safetyDSL_SafetyTactic46: "safetyDSL_Monitor" = None):
        self.name = name
        self.type = type
        self.safetyDSL_SafetyTactic = safetyDSL_SafetyTactic
        self.safetyDSL_SafetyTactic26 = safetyDSL_SafetyTactic26 if safetyDSL_SafetyTactic26 is not None else set()
        self.safetyDSL_SafetyTactic37 = safetyDSL_SafetyTactic37
        self.safetyDSL_SafetyTactic46 = safetyDSL_SafetyTactic46
        
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
    def safetyDSL_SafetyTactic26(self):
        return self.__safetyDSL_SafetyTactic26

    @safetyDSL_SafetyTactic26.setter
    def safetyDSL_SafetyTactic26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_safetyDSL_SafetyTactic__safetyDSL_SafetyTactic26", None)
        self.__safetyDSL_SafetyTactic26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "safetyDSL_Fault27"):
                    opp_val = getattr(item, "safetyDSL_Fault27", None)
                    
                    if opp_val == self:
                        setattr(item, "safetyDSL_Fault27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "safetyDSL_Fault27"):
                    opp_val = getattr(item, "safetyDSL_Fault27", None)
                    
                    setattr(item, "safetyDSL_Fault27", self)
                    

    @property
    def safetyDSL_SafetyTactic37(self):
        return self.__safetyDSL_SafetyTactic37

    @safetyDSL_SafetyTactic37.setter
    def safetyDSL_SafetyTactic37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_safetyDSL_SafetyTactic__safetyDSL_SafetyTactic37", None)
        self.__safetyDSL_SafetyTactic37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "safetyDSL_SafetyCritical36"):
                opp_val = getattr(old_value, "safetyDSL_SafetyCritical36", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "safetyDSL_SafetyCritical36"):
                opp_val = getattr(value, "safetyDSL_SafetyCritical36", None)
                if opp_val is None:
                    setattr(value, "safetyDSL_SafetyCritical36", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def safetyDSL_SafetyTactic46(self):
        return self.__safetyDSL_SafetyTactic46

    @safetyDSL_SafetyTactic46.setter
    def safetyDSL_SafetyTactic46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_safetyDSL_SafetyTactic__safetyDSL_SafetyTactic46", None)
        self.__safetyDSL_SafetyTactic46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "safetyDSL_Monitor"):
                opp_val = getattr(old_value, "safetyDSL_Monitor", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "safetyDSL_Monitor"):
                opp_val = getattr(value, "safetyDSL_Monitor", None)
                if opp_val is None:
                    setattr(value, "safetyDSL_Monitor", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def safetyDSL_SafetyTactic(self):
        return self.__safetyDSL_SafetyTactic

    @safetyDSL_SafetyTactic.setter
    def safetyDSL_SafetyTactic(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_safetyDSL_SafetyTactic__safetyDSL_SafetyTactic", None)
        self.__safetyDSL_SafetyTactic = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "safetyDSL_SafetyTacticViewpoint"):
                opp_val = getattr(old_value, "safetyDSL_SafetyTacticViewpoint", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "safetyDSL_SafetyTacticViewpoint"):
                opp_val = getattr(value, "safetyDSL_SafetyTacticViewpoint", None)
                if opp_val is None:
                    setattr(value, "safetyDSL_SafetyTacticViewpoint", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class safetyDSL_CausedBy(HazardRelation):

    pass
class HazardElement:

    pass
class safetyDSL_SafetyRequirement(HazardElement):

    pass
class safetyDSL_Hazard(HazardElement):

    pass
class safetyDSL_FaultTreeNode:

    pass
class safetyDSL_FaultTree(HazardElement):

    pass
class safetyDSL_Fault(HazardElement):

    pass
class safetyDSL_Consequence(HazardElement):

    pass
class safetyDSL_SafetyViewpoint:

    def __init__(self, name: str, safetyDSL_SafetyViewpoint: "safetyDSL_SafetyFramework" = None):
        self.name = name
        self.safetyDSL_SafetyViewpoint = safetyDSL_SafetyViewpoint
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def safetyDSL_SafetyViewpoint(self):
        return self.__safetyDSL_SafetyViewpoint

    @safetyDSL_SafetyViewpoint.setter
    def safetyDSL_SafetyViewpoint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_safetyDSL_SafetyViewpoint__safetyDSL_SafetyViewpoint", None)
        self.__safetyDSL_SafetyViewpoint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "safetyDSL_SafetyFramework"):
                opp_val = getattr(old_value, "safetyDSL_SafetyFramework", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "safetyDSL_SafetyFramework"):
                opp_val = getattr(value, "safetyDSL_SafetyFramework", None)
                if opp_val is None:
                    setattr(value, "safetyDSL_SafetyFramework", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class safetyDSL_SafetyFramework:

    pass
class safetyDSL_HazardRelation:

    pass
class safetyDSL_HazardElement:

    def __init__(self, name: str, safetyDSL_HazardElement: "safetyDSL_HazardViewpoint" = None):
        self.name = name
        self.safetyDSL_HazardElement = safetyDSL_HazardElement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def safetyDSL_HazardElement(self):
        return self.__safetyDSL_HazardElement

    @safetyDSL_HazardElement.setter
    def safetyDSL_HazardElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_safetyDSL_HazardElement__safetyDSL_HazardElement", None)
        self.__safetyDSL_HazardElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "safetyDSL_HazardViewpoint"):
                opp_val = getattr(old_value, "safetyDSL_HazardViewpoint", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "safetyDSL_HazardViewpoint"):
                opp_val = getattr(value, "safetyDSL_HazardViewpoint", None)
                if opp_val is None:
                    setattr(value, "safetyDSL_HazardViewpoint", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class SafetyViewpoint:

    pass
class safetyDSL_SafetyCriticalViewpoint(SafetyViewpoint):

    pass
class safetyDSL_SafetyTacticViewpoint(SafetyViewpoint):

    pass
class safetyDSL_HazardViewpoint(SafetyViewpoint):

    pass
class safetyDSL_ImplementationDetail:

    pass