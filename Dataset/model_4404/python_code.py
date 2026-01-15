from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class GroupState(Enum):
    MANDATORY = "MANDATORY"
    OPTIONAL = "OPTIONAL"
    ALTERNATIVE = "ALTERNATIVE"
    OR = "OR"
    MUTEX = "MUTEX"


############################################
# Definition of Classes
############################################

class spinefm_ActionModel_Action(ABC):

    def __init__(self, id: str, spinefm_ActionModel_Action: "Feature" = None, spinefm_ActionModel_Action88: "FeatureModel" = None):
        self.id = id
        self.spinefm_ActionModel_Action = spinefm_ActionModel_Action
        self.spinefm_ActionModel_Action88 = spinefm_ActionModel_Action88
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def spinefm_ActionModel_Action(self):
        return self.__spinefm_ActionModel_Action

    @spinefm_ActionModel_Action.setter
    def spinefm_ActionModel_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_ActionModel_Action__spinefm_ActionModel_Action", None)
        self.__spinefm_ActionModel_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Feature86"):
                opp_val = getattr(old_value, "Feature86", None)
                if opp_val == self:
                    setattr(old_value, "Feature86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Feature86"):
                opp_val = getattr(value, "Feature86", None)
                setattr(value, "Feature86", self)

    @property
    def spinefm_ActionModel_Action88(self):
        return self.__spinefm_ActionModel_Action88

    @spinefm_ActionModel_Action88.setter
    def spinefm_ActionModel_Action88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_ActionModel_Action__spinefm_ActionModel_Action88", None)
        self.__spinefm_ActionModel_Action88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FeatureModel89"):
                opp_val = getattr(old_value, "FeatureModel89", None)
                if opp_val == self:
                    setattr(old_value, "FeatureModel89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FeatureModel89"):
                opp_val = getattr(value, "FeatureModel89", None)
                setattr(value, "FeatureModel89", self)

    def isSameObject(self, o: str) -> bool:
        # TODO: Implement isSameObject method
        pass

    def applyAction(self, fma: str, confName: str):
        # TODO: Implement applyAction method
        pass

class spinefm_ActionModel_Rule:

    def __init__(self, id: str, spinefm_ActionModel_Rule: "Action" = None, spinefm_ActionModel_Rule83: "ConfigurationState" = None):
        self.id = id
        self.spinefm_ActionModel_Rule = spinefm_ActionModel_Rule
        self.spinefm_ActionModel_Rule83 = spinefm_ActionModel_Rule83
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def spinefm_ActionModel_Rule83(self):
        return self.__spinefm_ActionModel_Rule83

    @spinefm_ActionModel_Rule83.setter
    def spinefm_ActionModel_Rule83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_ActionModel_Rule__spinefm_ActionModel_Rule83", None)
        self.__spinefm_ActionModel_Rule83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ConfigurationState84"):
                opp_val = getattr(old_value, "ConfigurationState84", None)
                if opp_val == self:
                    setattr(old_value, "ConfigurationState84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ConfigurationState84"):
                opp_val = getattr(value, "ConfigurationState84", None)
                setattr(value, "ConfigurationState84", self)

    @property
    def spinefm_ActionModel_Rule(self):
        return self.__spinefm_ActionModel_Rule

    @spinefm_ActionModel_Rule.setter
    def spinefm_ActionModel_Rule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_ActionModel_Rule__spinefm_ActionModel_Rule", None)
        self.__spinefm_ActionModel_Rule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Action81"):
                opp_val = getattr(old_value, "Action81", None)
                if opp_val == self:
                    setattr(old_value, "Action81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Action81"):
                opp_val = getattr(value, "Action81", None)
                setattr(value, "Action81", self)

    def createInverseRule(self) -> str:
        # TODO: Implement createInverseRule method
        pass

class Rule:

    pass
class spinefm_ActionModel_RestrictionFunction:

    def __init__(self, id: str, spinefm_ActionModel_RestrictionFunction: set["Rule"] = None, spinefm_ActionModel_RestrictionFunction70: "RestrictionFunction" = None):
        self.id = id
        self.spinefm_ActionModel_RestrictionFunction = spinefm_ActionModel_RestrictionFunction if spinefm_ActionModel_RestrictionFunction is not None else set()
        self.spinefm_ActionModel_RestrictionFunction70 = spinefm_ActionModel_RestrictionFunction70
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def spinefm_ActionModel_RestrictionFunction(self):
        return self.__spinefm_ActionModel_RestrictionFunction

    @spinefm_ActionModel_RestrictionFunction.setter
    def spinefm_ActionModel_RestrictionFunction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_ActionModel_RestrictionFunction__spinefm_ActionModel_RestrictionFunction", None)
        self.__spinefm_ActionModel_RestrictionFunction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Rule"):
                    opp_val = getattr(item, "Rule", None)
                    
                    if opp_val == self:
                        setattr(item, "Rule", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Rule"):
                    opp_val = getattr(item, "Rule", None)
                    
                    setattr(item, "Rule", self)
                    

    @property
    def spinefm_ActionModel_RestrictionFunction70(self):
        return self.__spinefm_ActionModel_RestrictionFunction70

    @spinefm_ActionModel_RestrictionFunction70.setter
    def spinefm_ActionModel_RestrictionFunction70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_ActionModel_RestrictionFunction__spinefm_ActionModel_RestrictionFunction70", None)
        self.__spinefm_ActionModel_RestrictionFunction70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RestrictionFunction71"):
                opp_val = getattr(old_value, "RestrictionFunction71", None)
                if opp_val == self:
                    setattr(old_value, "RestrictionFunction71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RestrictionFunction71"):
                opp_val = getattr(value, "RestrictionFunction71", None)
                setattr(value, "RestrictionFunction71", self)

    def createAndAssociateInverseRestFunc(self) -> str:
        # TODO: Implement createAndAssociateInverseRestFunc method
        pass

class spinefm_ProcessModel_DeletedContextInformations:

    def __init__(self, deletedContext: str, spinefm_ProcessModel_DeletedContextInformations: "Context" = None):
        self.deletedContext = deletedContext
        self.spinefm_ProcessModel_DeletedContextInformations = spinefm_ProcessModel_DeletedContextInformations
        
    @property
    def deletedContext(self) -> str:
        return self.__deletedContext

    @deletedContext.setter
    def deletedContext(self, deletedContext: str):
        self.__deletedContext = deletedContext

    @property
    def spinefm_ProcessModel_DeletedContextInformations(self):
        return self.__spinefm_ProcessModel_DeletedContextInformations

    @spinefm_ProcessModel_DeletedContextInformations.setter
    def spinefm_ProcessModel_DeletedContextInformations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_ProcessModel_DeletedContextInformations__spinefm_ProcessModel_DeletedContextInformations", None)
        self.__spinefm_ProcessModel_DeletedContextInformations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Context67"):
                opp_val = getattr(old_value, "Context67", None)
                if opp_val == self:
                    setattr(old_value, "Context67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Context67"):
                opp_val = getattr(value, "Context67", None)
                setattr(value, "Context67", self)

class LocalContext:

    pass
class GlobalContext:

    pass
class MultipleSoftwareProductLine:

    pass
class spinefm_ProcessModel_ContextManager:

    def __init__(self, spinefm_ProcessModel_ContextManager: "MultipleSoftwareProductLine" = None, spinefm_ProcessModel_ContextManager63: "GlobalContext" = None, spinefm_ProcessModel_ContextManager65: set["LocalContext"] = None):
        self.spinefm_ProcessModel_ContextManager = spinefm_ProcessModel_ContextManager
        self.spinefm_ProcessModel_ContextManager63 = spinefm_ProcessModel_ContextManager63
        self.spinefm_ProcessModel_ContextManager65 = spinefm_ProcessModel_ContextManager65 if spinefm_ProcessModel_ContextManager65 is not None else set()
        
    @property
    def spinefm_ProcessModel_ContextManager(self):
        return self.__spinefm_ProcessModel_ContextManager

    @spinefm_ProcessModel_ContextManager.setter
    def spinefm_ProcessModel_ContextManager(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_ProcessModel_ContextManager__spinefm_ProcessModel_ContextManager", None)
        self.__spinefm_ProcessModel_ContextManager = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MultipleSoftwareProductLine"):
                opp_val = getattr(old_value, "MultipleSoftwareProductLine", None)
                if opp_val == self:
                    setattr(old_value, "MultipleSoftwareProductLine", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MultipleSoftwareProductLine"):
                opp_val = getattr(value, "MultipleSoftwareProductLine", None)
                setattr(value, "MultipleSoftwareProductLine", self)

    @property
    def spinefm_ProcessModel_ContextManager63(self):
        return self.__spinefm_ProcessModel_ContextManager63

    @spinefm_ProcessModel_ContextManager63.setter
    def spinefm_ProcessModel_ContextManager63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_ProcessModel_ContextManager__spinefm_ProcessModel_ContextManager63", None)
        self.__spinefm_ProcessModel_ContextManager63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GlobalContext"):
                opp_val = getattr(old_value, "GlobalContext", None)
                if opp_val == self:
                    setattr(old_value, "GlobalContext", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GlobalContext"):
                opp_val = getattr(value, "GlobalContext", None)
                setattr(value, "GlobalContext", self)

    @property
    def spinefm_ProcessModel_ContextManager65(self):
        return self.__spinefm_ProcessModel_ContextManager65

    @spinefm_ProcessModel_ContextManager65.setter
    def spinefm_ProcessModel_ContextManager65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_ProcessModel_ContextManager__spinefm_ProcessModel_ContextManager65", None)
        self.__spinefm_ProcessModel_ContextManager65 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "LocalContext"):
                    opp_val = getattr(item, "LocalContext", None)
                    
                    if opp_val == self:
                        setattr(item, "LocalContext", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "LocalContext"):
                    opp_val = getattr(item, "LocalContext", None)
                    
                    setattr(item, "LocalContext", self)
                    

    def linkConfigurationsAndManageContexts(self, association: str, confTarget: str, confSource: str) -> str:
        # TODO: Implement linkConfigurationsAndManageContexts method
        pass

    def setFMAdapter(self, fma: str):
        # TODO: Implement setFMAdapter method
        pass

    def createNewContext(self) -> str:
        # TODO: Implement createNewContext method
        pass

    def getContextFromId(self, id: str) -> str:
        # TODO: Implement getContextFromId method
        pass

    def init(self):
        # TODO: Implement init method
        pass

    def propagate(self, CPS: str, context: str):
        # TODO: Implement propagate method
        pass

class spinefm_ActionModel_ConfigurationState:

    def __init__(self, id: str, spinefm_ActionModel_ConfigurationState: set["Feature"] = None, spinefm_ActionModel_ConfigurationState75: set["Feature"] = None, spinefm_ActionModel_ConfigurationState78: "FeatureModel" = None):
        self.id = id
        self.spinefm_ActionModel_ConfigurationState = spinefm_ActionModel_ConfigurationState if spinefm_ActionModel_ConfigurationState is not None else set()
        self.spinefm_ActionModel_ConfigurationState75 = spinefm_ActionModel_ConfigurationState75 if spinefm_ActionModel_ConfigurationState75 is not None else set()
        self.spinefm_ActionModel_ConfigurationState78 = spinefm_ActionModel_ConfigurationState78
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def spinefm_ActionModel_ConfigurationState(self):
        return self.__spinefm_ActionModel_ConfigurationState

    @spinefm_ActionModel_ConfigurationState.setter
    def spinefm_ActionModel_ConfigurationState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_ActionModel_ConfigurationState__spinefm_ActionModel_ConfigurationState", None)
        self.__spinefm_ActionModel_ConfigurationState = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Feature73"):
                    opp_val = getattr(item, "Feature73", None)
                    
                    if opp_val == self:
                        setattr(item, "Feature73", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Feature73"):
                    opp_val = getattr(item, "Feature73", None)
                    
                    setattr(item, "Feature73", self)
                    

    @property
    def spinefm_ActionModel_ConfigurationState78(self):
        return self.__spinefm_ActionModel_ConfigurationState78

    @spinefm_ActionModel_ConfigurationState78.setter
    def spinefm_ActionModel_ConfigurationState78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_ActionModel_ConfigurationState__spinefm_ActionModel_ConfigurationState78", None)
        self.__spinefm_ActionModel_ConfigurationState78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FeatureModel79"):
                opp_val = getattr(old_value, "FeatureModel79", None)
                if opp_val == self:
                    setattr(old_value, "FeatureModel79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FeatureModel79"):
                opp_val = getattr(value, "FeatureModel79", None)
                setattr(value, "FeatureModel79", self)

    @property
    def spinefm_ActionModel_ConfigurationState75(self):
        return self.__spinefm_ActionModel_ConfigurationState75

    @spinefm_ActionModel_ConfigurationState75.setter
    def spinefm_ActionModel_ConfigurationState75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_ActionModel_ConfigurationState__spinefm_ActionModel_ConfigurationState75", None)
        self.__spinefm_ActionModel_ConfigurationState75 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Feature76"):
                    opp_val = getattr(item, "Feature76", None)
                    
                    if opp_val == self:
                        setattr(item, "Feature76", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Feature76"):
                    opp_val = getattr(item, "Feature76", None)
                    
                    setattr(item, "Feature76", self)
                    

    def isIncludedIn(self, otherState: str) -> bool:
        # TODO: Implement isIncludedIn method
        pass

class CompositeConfiguration:

    pass
class spinefm_ProcessModel_Context(ABC):

    def __init__(self, id: str, spinefm_ProcessModel_Context: set["ConfigurationProcessStep"] = None):
        self.id = id
        self.spinefm_ProcessModel_Context = spinefm_ProcessModel_Context if spinefm_ProcessModel_Context is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def spinefm_ProcessModel_Context(self):
        return self.__spinefm_ProcessModel_Context

    @spinefm_ProcessModel_Context.setter
    def spinefm_ProcessModel_Context(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_ProcessModel_Context__spinefm_ProcessModel_Context", None)
        self.__spinefm_ProcessModel_Context = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ConfigurationProcessStep57"):
                    opp_val = getattr(item, "ConfigurationProcessStep57", None)
                    
                    if opp_val == self:
                        setattr(item, "ConfigurationProcessStep57", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ConfigurationProcessStep57"):
                    opp_val = getattr(item, "ConfigurationProcessStep57", None)
                    
                    setattr(item, "ConfigurationProcessStep57", self)
                    

    def getCPSOfDE(self, de: str) -> str:
        # TODO: Implement getCPSOfDE method
        pass

    def mergeExternalCPS(self, externalCPS: str):
        # TODO: Implement mergeExternalCPS method
        pass

    def addCPS(self, cps: str):
        # TODO: Implement addCPS method
        pass

class Context:

    pass
class spinefm_ProcessModel_GlobalContext(Context):

    pass
class Action:

    pass
class spinefm_ActionModel_ActionAddCTConstraint(Action):

    pass
class spinefm_ActionModel_ActionDeselect(Action):

    pass
class spinefm_ActionModel_ActionSelect(Action):

    pass
class spinefm_ProcessModel_ConfigurationProcessStep:

    def __init__(self, id: str, description: str, userConfig: bool, spinefm_ProcessModel_ConfigurationProcessStep: set["Action"] = None, spinefm_ProcessModel_ConfigurationProcessStep47: "DomainElement" = None, spinefm_ProcessModel_ConfigurationProcessStep50: set["Action"] = None, spinefm_ProcessModel_ConfigurationProcessStep53: "Context" = None, Configuration55: "Configuration" = None):
        self.id = id
        self.description = description
        self.userConfig = userConfig
        self.spinefm_ProcessModel_ConfigurationProcessStep = spinefm_ProcessModel_ConfigurationProcessStep if spinefm_ProcessModel_ConfigurationProcessStep is not None else set()
        self.spinefm_ProcessModel_ConfigurationProcessStep47 = spinefm_ProcessModel_ConfigurationProcessStep47
        self.spinefm_ProcessModel_ConfigurationProcessStep50 = spinefm_ProcessModel_ConfigurationProcessStep50 if spinefm_ProcessModel_ConfigurationProcessStep50 is not None else set()
        self.spinefm_ProcessModel_ConfigurationProcessStep53 = spinefm_ProcessModel_ConfigurationProcessStep53
        self.Configuration55 = Configuration55
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def userConfig(self) -> bool:
        return self.__userConfig

    @userConfig.setter
    def userConfig(self, userConfig: bool):
        self.__userConfig = userConfig

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def spinefm_ProcessModel_ConfigurationProcessStep(self):
        return self.__spinefm_ProcessModel_ConfigurationProcessStep

    @spinefm_ProcessModel_ConfigurationProcessStep.setter
    def spinefm_ProcessModel_ConfigurationProcessStep(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_ProcessModel_ConfigurationProcessStep__spinefm_ProcessModel_ConfigurationProcessStep", None)
        self.__spinefm_ProcessModel_ConfigurationProcessStep = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Action"):
                    opp_val = getattr(item, "Action", None)
                    
                    if opp_val == self:
                        setattr(item, "Action", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Action"):
                    opp_val = getattr(item, "Action", None)
                    
                    setattr(item, "Action", self)
                    

    @property
    def spinefm_ProcessModel_ConfigurationProcessStep53(self):
        return self.__spinefm_ProcessModel_ConfigurationProcessStep53

    @spinefm_ProcessModel_ConfigurationProcessStep53.setter
    def spinefm_ProcessModel_ConfigurationProcessStep53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_ProcessModel_ConfigurationProcessStep__spinefm_ProcessModel_ConfigurationProcessStep53", None)
        self.__spinefm_ProcessModel_ConfigurationProcessStep53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Context"):
                opp_val = getattr(old_value, "Context", None)
                if opp_val == self:
                    setattr(old_value, "Context", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Context"):
                opp_val = getattr(value, "Context", None)
                setattr(value, "Context", self)

    @property
    def Configuration55(self):
        return self.__Configuration55

    @Configuration55.setter
    def Configuration55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_ProcessModel_ConfigurationProcessStep__Configuration55", None)
        self.__Configuration55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ConfigurationModel"):
                opp_val = getattr(old_value, "ConfigurationModel", None)
                if opp_val == self:
                    setattr(old_value, "ConfigurationModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ConfigurationModel"):
                opp_val = getattr(value, "ConfigurationModel", None)
                setattr(value, "ConfigurationModel", self)

    @property
    def spinefm_ProcessModel_ConfigurationProcessStep47(self):
        return self.__spinefm_ProcessModel_ConfigurationProcessStep47

    @spinefm_ProcessModel_ConfigurationProcessStep47.setter
    def spinefm_ProcessModel_ConfigurationProcessStep47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_ProcessModel_ConfigurationProcessStep__spinefm_ProcessModel_ConfigurationProcessStep47", None)
        self.__spinefm_ProcessModel_ConfigurationProcessStep47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DomainElement48"):
                opp_val = getattr(old_value, "DomainElement48", None)
                if opp_val == self:
                    setattr(old_value, "DomainElement48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DomainElement48"):
                opp_val = getattr(value, "DomainElement48", None)
                setattr(value, "DomainElement48", self)

    @property
    def spinefm_ProcessModel_ConfigurationProcessStep50(self):
        return self.__spinefm_ProcessModel_ConfigurationProcessStep50

    @spinefm_ProcessModel_ConfigurationProcessStep50.setter
    def spinefm_ProcessModel_ConfigurationProcessStep50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_ProcessModel_ConfigurationProcessStep__spinefm_ProcessModel_ConfigurationProcessStep50", None)
        self.__spinefm_ProcessModel_ConfigurationProcessStep50 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Action51"):
                    opp_val = getattr(item, "Action51", None)
                    
                    if opp_val == self:
                        setattr(item, "Action51", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Action51"):
                    opp_val = getattr(item, "Action51", None)
                    
                    setattr(item, "Action51", self)
                    

    def setFMA(self, fma: str):
        # TODO: Implement setFMA method
        pass

    def mergeWithExternalCPS(self, cps: str):
        # TODO: Implement mergeWithExternalCPS method
        pass

    def getState(self) -> str:
        # TODO: Implement getState method
        pass

    def alreadyHaveAction(self, a: str) -> bool:
        # TODO: Implement alreadyHaveAction method
        pass

    def apply(self) -> bool:
        # TODO: Implement apply method
        pass

    def isComplete(self) -> bool:
        # TODO: Implement isComplete method
        pass

    def addActionToDo(self, a: str):
        # TODO: Implement addActionToDo method
        pass

    def isCompatibleWithConfiguration(self, conf: str) -> bool:
        # TODO: Implement isCompatibleWithConfiguration method
        pass

    def getConfName(self) -> str:
        # TODO: Implement getConfName method
        pass

class spinefm_ProcessModel_LocalContext(Context):

    pass
class spinefm_ConfigurationModel_CompositeConfiguration:

    def __init__(self, name: str, spinefm_ConfigurationModel_CompositeConfiguration: set["Configuration"] = None, spinefm_ConfigurationModel_CompositeConfiguration43: set["Link"] = None):
        self.name = name
        self.spinefm_ConfigurationModel_CompositeConfiguration = spinefm_ConfigurationModel_CompositeConfiguration if spinefm_ConfigurationModel_CompositeConfiguration is not None else set()
        self.spinefm_ConfigurationModel_CompositeConfiguration43 = spinefm_ConfigurationModel_CompositeConfiguration43 if spinefm_ConfigurationModel_CompositeConfiguration43 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def spinefm_ConfigurationModel_CompositeConfiguration43(self):
        return self.__spinefm_ConfigurationModel_CompositeConfiguration43

    @spinefm_ConfigurationModel_CompositeConfiguration43.setter
    def spinefm_ConfigurationModel_CompositeConfiguration43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_ConfigurationModel_CompositeConfiguration__spinefm_ConfigurationModel_CompositeConfiguration43", None)
        self.__spinefm_ConfigurationModel_CompositeConfiguration43 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Link44"):
                    opp_val = getattr(item, "Link44", None)
                    
                    if opp_val == self:
                        setattr(item, "Link44", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Link44"):
                    opp_val = getattr(item, "Link44", None)
                    
                    setattr(item, "Link44", self)
                    

    @property
    def spinefm_ConfigurationModel_CompositeConfiguration(self):
        return self.__spinefm_ConfigurationModel_CompositeConfiguration

    @spinefm_ConfigurationModel_CompositeConfiguration.setter
    def spinefm_ConfigurationModel_CompositeConfiguration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_ConfigurationModel_CompositeConfiguration__spinefm_ConfigurationModel_CompositeConfiguration", None)
        self.__spinefm_ConfigurationModel_CompositeConfiguration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Configuration41"):
                    opp_val = getattr(item, "Configuration41", None)
                    
                    if opp_val == self:
                        setattr(item, "Configuration41", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Configuration41"):
                    opp_val = getattr(item, "Configuration41", None)
                    
                    setattr(item, "Configuration41", self)
                    

    def addConfiguration(self, conf: str):
        # TODO: Implement addConfiguration method
        pass

    def getConfigurationByName(self, confName: str) -> str:
        # TODO: Implement getConfigurationByName method
        pass

    def isValid(self) -> bool:
        # TODO: Implement isValid method
        pass

    def createConfigurationLink(self, confTarget: str, asso: str, confSource: str):
        # TODO: Implement createConfigurationLink method
        pass

    def getCompatibleConfigurations(self, asso: str, confSource: str) -> str:
        # TODO: Implement getCompatibleConfigurations method
        pass

class Configuration:

    pass
class spinefm_ConfigurationModel_Link:

    def __init__(self, id: str, spinefm_ConfigurationModel_Link: "Configuration" = None, spinefm_ConfigurationModel_Link35: "DEAssociation" = None, spinefm_ConfigurationModel_Link38: "Configuration" = None):
        self.id = id
        self.spinefm_ConfigurationModel_Link = spinefm_ConfigurationModel_Link
        self.spinefm_ConfigurationModel_Link35 = spinefm_ConfigurationModel_Link35
        self.spinefm_ConfigurationModel_Link38 = spinefm_ConfigurationModel_Link38
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def spinefm_ConfigurationModel_Link(self):
        return self.__spinefm_ConfigurationModel_Link

    @spinefm_ConfigurationModel_Link.setter
    def spinefm_ConfigurationModel_Link(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_ConfigurationModel_Link__spinefm_ConfigurationModel_Link", None)
        self.__spinefm_ConfigurationModel_Link = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Configuration"):
                opp_val = getattr(old_value, "Configuration", None)
                if opp_val == self:
                    setattr(old_value, "Configuration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Configuration"):
                opp_val = getattr(value, "Configuration", None)
                setattr(value, "Configuration", self)

    @property
    def spinefm_ConfigurationModel_Link35(self):
        return self.__spinefm_ConfigurationModel_Link35

    @spinefm_ConfigurationModel_Link35.setter
    def spinefm_ConfigurationModel_Link35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_ConfigurationModel_Link__spinefm_ConfigurationModel_Link35", None)
        self.__spinefm_ConfigurationModel_Link35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DEAssociation36"):
                opp_val = getattr(old_value, "DEAssociation36", None)
                if opp_val == self:
                    setattr(old_value, "DEAssociation36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DEAssociation36"):
                opp_val = getattr(value, "DEAssociation36", None)
                setattr(value, "DEAssociation36", self)

    @property
    def spinefm_ConfigurationModel_Link38(self):
        return self.__spinefm_ConfigurationModel_Link38

    @spinefm_ConfigurationModel_Link38.setter
    def spinefm_ConfigurationModel_Link38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_ConfigurationModel_Link__spinefm_ConfigurationModel_Link38", None)
        self.__spinefm_ConfigurationModel_Link38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Configuration39"):
                opp_val = getattr(old_value, "Configuration39", None)
                if opp_val == self:
                    setattr(old_value, "Configuration39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Configuration39"):
                opp_val = getattr(value, "Configuration39", None)
                setattr(value, "Configuration39", self)

    def getAssociatedConfiguration(self, conf: str) -> str:
        # TODO: Implement getAssociatedConfiguration method
        pass

class ConfigurationState:

    pass
class Link:

    pass
class ConfigurationProcessStep:

    pass
class spinefm_ConfigurationModel_Configuration:

    def __init__(self, id: str, description: str, ConfigurationProcessStep: "ConfigurationProcessStep" = None, spinefm_ConfigurationModel_Configuration: set["Link"] = None, spinefm_ConfigurationModel_Configuration32: "ConfigurationState" = None):
        self.id = id
        self.description = description
        self.ConfigurationProcessStep = ConfigurationProcessStep
        self.spinefm_ConfigurationModel_Configuration = spinefm_ConfigurationModel_Configuration if spinefm_ConfigurationModel_Configuration is not None else set()
        self.spinefm_ConfigurationModel_Configuration32 = spinefm_ConfigurationModel_Configuration32
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def spinefm_ConfigurationModel_Configuration(self):
        return self.__spinefm_ConfigurationModel_Configuration

    @spinefm_ConfigurationModel_Configuration.setter
    def spinefm_ConfigurationModel_Configuration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_ConfigurationModel_Configuration__spinefm_ConfigurationModel_Configuration", None)
        self.__spinefm_ConfigurationModel_Configuration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Link"):
                    opp_val = getattr(item, "Link", None)
                    
                    if opp_val == self:
                        setattr(item, "Link", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Link"):
                    opp_val = getattr(item, "Link", None)
                    
                    setattr(item, "Link", self)
                    

    @property
    def ConfigurationProcessStep(self):
        return self.__ConfigurationProcessStep

    @ConfigurationProcessStep.setter
    def ConfigurationProcessStep(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_ConfigurationModel_Configuration__ConfigurationProcessStep", None)
        self.__ConfigurationProcessStep = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ProcessModel"):
                opp_val = getattr(old_value, "ProcessModel", None)
                if opp_val == self:
                    setattr(old_value, "ProcessModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProcessModel"):
                opp_val = getattr(value, "ProcessModel", None)
                setattr(value, "ProcessModel", self)

    @property
    def spinefm_ConfigurationModel_Configuration32(self):
        return self.__spinefm_ConfigurationModel_Configuration32

    @spinefm_ConfigurationModel_Configuration32.setter
    def spinefm_ConfigurationModel_Configuration32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_ConfigurationModel_Configuration__spinefm_ConfigurationModel_Configuration32", None)
        self.__spinefm_ConfigurationModel_Configuration32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ConfigurationState"):
                opp_val = getattr(old_value, "ConfigurationState", None)
                if opp_val == self:
                    setattr(old_value, "ConfigurationState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ConfigurationState"):
                opp_val = getattr(value, "ConfigurationState", None)
                setattr(value, "ConfigurationState", self)

    def getLinkedConfigurationsOfDomainElement(self, de: str) -> str:
        # TODO: Implement getLinkedConfigurationsOfDomainElement method
        pass

    def canBeLinked(self, association: str) -> bool:
        # TODO: Implement canBeLinked method
        pass

    def isCompletlyLinked(self) -> bool:
        # TODO: Implement isCompletlyLinked method
        pass

    def getFeatureModel(self) -> str:
        # TODO: Implement getFeatureModel method
        pass

class FeatureModel:

    pass
class spinefm_MSPLModel_DomainElement:

    def __init__(self, id: str, spinefm_MSPLModel_DomainElement: "MultiplicityElement" = None, spinefm_MSPLModel_DomainElement25: "FeatureModel" = None, spinefm_MSPLModel_DomainElement27: set["DEAssociation"] = None):
        self.id = id
        self.spinefm_MSPLModel_DomainElement = spinefm_MSPLModel_DomainElement
        self.spinefm_MSPLModel_DomainElement25 = spinefm_MSPLModel_DomainElement25
        self.spinefm_MSPLModel_DomainElement27 = spinefm_MSPLModel_DomainElement27 if spinefm_MSPLModel_DomainElement27 is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def spinefm_MSPLModel_DomainElement27(self):
        return self.__spinefm_MSPLModel_DomainElement27

    @spinefm_MSPLModel_DomainElement27.setter
    def spinefm_MSPLModel_DomainElement27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_MSPLModel_DomainElement__spinefm_MSPLModel_DomainElement27", None)
        self.__spinefm_MSPLModel_DomainElement27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DEAssociation28"):
                    opp_val = getattr(item, "DEAssociation28", None)
                    
                    if opp_val == self:
                        setattr(item, "DEAssociation28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DEAssociation28"):
                    opp_val = getattr(item, "DEAssociation28", None)
                    
                    setattr(item, "DEAssociation28", self)
                    

    @property
    def spinefm_MSPLModel_DomainElement(self):
        return self.__spinefm_MSPLModel_DomainElement

    @spinefm_MSPLModel_DomainElement.setter
    def spinefm_MSPLModel_DomainElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_MSPLModel_DomainElement__spinefm_MSPLModel_DomainElement", None)
        self.__spinefm_MSPLModel_DomainElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MultiplicityElement23"):
                opp_val = getattr(old_value, "MultiplicityElement23", None)
                if opp_val == self:
                    setattr(old_value, "MultiplicityElement23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MultiplicityElement23"):
                opp_val = getattr(value, "MultiplicityElement23", None)
                setattr(value, "MultiplicityElement23", self)

    @property
    def spinefm_MSPLModel_DomainElement25(self):
        return self.__spinefm_MSPLModel_DomainElement25

    @spinefm_MSPLModel_DomainElement25.setter
    def spinefm_MSPLModel_DomainElement25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_MSPLModel_DomainElement__spinefm_MSPLModel_DomainElement25", None)
        self.__spinefm_MSPLModel_DomainElement25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FeatureModel"):
                opp_val = getattr(old_value, "FeatureModel", None)
                if opp_val == self:
                    setattr(old_value, "FeatureModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FeatureModel"):
                opp_val = getattr(value, "FeatureModel", None)
                setattr(value, "FeatureModel", self)

    def getSourcedAssociations(self) -> str:
        # TODO: Implement getSourcedAssociations method
        pass

class MultiplicityElement:

    pass
class spinefm_MSPLModel_DEAssociationEnd:

    def __init__(self, id: str, spinefm_MSPLModel_DEAssociationEnd: "MultiplicityElement" = None, spinefm_MSPLModel_DEAssociationEnd20: "DomainElement" = None):
        self.id = id
        self.spinefm_MSPLModel_DEAssociationEnd = spinefm_MSPLModel_DEAssociationEnd
        self.spinefm_MSPLModel_DEAssociationEnd20 = spinefm_MSPLModel_DEAssociationEnd20
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def spinefm_MSPLModel_DEAssociationEnd(self):
        return self.__spinefm_MSPLModel_DEAssociationEnd

    @spinefm_MSPLModel_DEAssociationEnd.setter
    def spinefm_MSPLModel_DEAssociationEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_MSPLModel_DEAssociationEnd__spinefm_MSPLModel_DEAssociationEnd", None)
        self.__spinefm_MSPLModel_DEAssociationEnd = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MultiplicityElement"):
                opp_val = getattr(old_value, "MultiplicityElement", None)
                if opp_val == self:
                    setattr(old_value, "MultiplicityElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MultiplicityElement"):
                opp_val = getattr(value, "MultiplicityElement", None)
                setattr(value, "MultiplicityElement", self)

    @property
    def spinefm_MSPLModel_DEAssociationEnd20(self):
        return self.__spinefm_MSPLModel_DEAssociationEnd20

    @spinefm_MSPLModel_DEAssociationEnd20.setter
    def spinefm_MSPLModel_DEAssociationEnd20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_MSPLModel_DEAssociationEnd__spinefm_MSPLModel_DEAssociationEnd20", None)
        self.__spinefm_MSPLModel_DEAssociationEnd20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DomainElement21"):
                opp_val = getattr(old_value, "DomainElement21", None)
                if opp_val == self:
                    setattr(old_value, "DomainElement21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DomainElement21"):
                opp_val = getattr(value, "DomainElement21", None)
                setattr(value, "DomainElement21", self)

class spinefm_MSPLModel_MultiplicityElement:

    def __init__(self, lowerBound: int, upperBound: int, id: str):
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.id = id
        
    @property
    def upperBound(self) -> int:
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: int):
        self.__upperBound = upperBound

    @property
    def lowerBound(self) -> int:
        return self.__lowerBound

    @lowerBound.setter
    def lowerBound(self, lowerBound: int):
        self.__lowerBound = lowerBound

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    def isExactlyOne(self) -> bool:
        # TODO: Implement isExactlyOne method
        pass

    def isLowerThanUpperBound(self, value: int) -> bool:
        # TODO: Implement isLowerThanUpperBound method
        pass

    def respectBoundaries(self, value: int) -> bool:
        # TODO: Implement respectBoundaries method
        pass

class DEAssociationEnd:

    pass
class RestrictionFunction:

    pass
class spinefm_MSPLModel_DEAssociation:

    def __init__(self, id: str, spinefm_MSPLModel_DEAssociation16: "DEAssociation" = None, spinefm_MSPLModel_DEAssociation: set["RestrictionFunction"] = None, spinefm_MSPLModel_DEAssociation11: "DEAssociationEnd" = None, spinefm_MSPLModel_DEAssociation13: "DEAssociationEnd" = None):
        self.id = id
        self.spinefm_MSPLModel_DEAssociation16 = spinefm_MSPLModel_DEAssociation16
        self.spinefm_MSPLModel_DEAssociation = spinefm_MSPLModel_DEAssociation if spinefm_MSPLModel_DEAssociation is not None else set()
        self.spinefm_MSPLModel_DEAssociation11 = spinefm_MSPLModel_DEAssociation11
        self.spinefm_MSPLModel_DEAssociation13 = spinefm_MSPLModel_DEAssociation13
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def spinefm_MSPLModel_DEAssociation13(self):
        return self.__spinefm_MSPLModel_DEAssociation13

    @spinefm_MSPLModel_DEAssociation13.setter
    def spinefm_MSPLModel_DEAssociation13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_MSPLModel_DEAssociation__spinefm_MSPLModel_DEAssociation13", None)
        self.__spinefm_MSPLModel_DEAssociation13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DEAssociationEnd14"):
                opp_val = getattr(old_value, "DEAssociationEnd14", None)
                if opp_val == self:
                    setattr(old_value, "DEAssociationEnd14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DEAssociationEnd14"):
                opp_val = getattr(value, "DEAssociationEnd14", None)
                setattr(value, "DEAssociationEnd14", self)

    @property
    def spinefm_MSPLModel_DEAssociation16(self):
        return self.__spinefm_MSPLModel_DEAssociation16

    @spinefm_MSPLModel_DEAssociation16.setter
    def spinefm_MSPLModel_DEAssociation16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_MSPLModel_DEAssociation__spinefm_MSPLModel_DEAssociation16", None)
        self.__spinefm_MSPLModel_DEAssociation16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DEAssociation17"):
                opp_val = getattr(old_value, "DEAssociation17", None)
                if opp_val == self:
                    setattr(old_value, "DEAssociation17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DEAssociation17"):
                opp_val = getattr(value, "DEAssociation17", None)
                setattr(value, "DEAssociation17", self)

    @property
    def spinefm_MSPLModel_DEAssociation11(self):
        return self.__spinefm_MSPLModel_DEAssociation11

    @spinefm_MSPLModel_DEAssociation11.setter
    def spinefm_MSPLModel_DEAssociation11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_MSPLModel_DEAssociation__spinefm_MSPLModel_DEAssociation11", None)
        self.__spinefm_MSPLModel_DEAssociation11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DEAssociationEnd"):
                opp_val = getattr(old_value, "DEAssociationEnd", None)
                if opp_val == self:
                    setattr(old_value, "DEAssociationEnd", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DEAssociationEnd"):
                opp_val = getattr(value, "DEAssociationEnd", None)
                setattr(value, "DEAssociationEnd", self)

    @property
    def spinefm_MSPLModel_DEAssociation(self):
        return self.__spinefm_MSPLModel_DEAssociation

    @spinefm_MSPLModel_DEAssociation.setter
    def spinefm_MSPLModel_DEAssociation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_MSPLModel_DEAssociation__spinefm_MSPLModel_DEAssociation", None)
        self.__spinefm_MSPLModel_DEAssociation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RestrictionFunction"):
                    opp_val = getattr(item, "RestrictionFunction", None)
                    
                    if opp_val == self:
                        setattr(item, "RestrictionFunction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RestrictionFunction"):
                    opp_val = getattr(item, "RestrictionFunction", None)
                    
                    setattr(item, "RestrictionFunction", self)
                    

    def createAndAssociateInverseAssociation(self) -> str:
        # TODO: Implement createAndAssociateInverseAssociation method
        pass

    def computeActionsToDo(self, CPSSource: str, CPSTarget: str) -> str:
        # TODO: Implement computeActionsToDo method
        pass

class DEAssociation:

    pass
class DomainElement:

    pass
class spinefm_MSPLModel_MultipleSoftwareProductLine:

    def __init__(self, spinefm_MSPLModel_MultipleSoftwareProductLine: set["DomainElement"] = None, spinefm_MSPLModel_MultipleSoftwareProductLine8: set["DEAssociation"] = None):
        self.spinefm_MSPLModel_MultipleSoftwareProductLine = spinefm_MSPLModel_MultipleSoftwareProductLine if spinefm_MSPLModel_MultipleSoftwareProductLine is not None else set()
        self.spinefm_MSPLModel_MultipleSoftwareProductLine8 = spinefm_MSPLModel_MultipleSoftwareProductLine8 if spinefm_MSPLModel_MultipleSoftwareProductLine8 is not None else set()
        
    @property
    def spinefm_MSPLModel_MultipleSoftwareProductLine(self):
        return self.__spinefm_MSPLModel_MultipleSoftwareProductLine

    @spinefm_MSPLModel_MultipleSoftwareProductLine.setter
    def spinefm_MSPLModel_MultipleSoftwareProductLine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_MSPLModel_MultipleSoftwareProductLine__spinefm_MSPLModel_MultipleSoftwareProductLine", None)
        self.__spinefm_MSPLModel_MultipleSoftwareProductLine = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DomainElement"):
                    opp_val = getattr(item, "DomainElement", None)
                    
                    if opp_val == self:
                        setattr(item, "DomainElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DomainElement"):
                    opp_val = getattr(item, "DomainElement", None)
                    
                    setattr(item, "DomainElement", self)
                    

    @property
    def spinefm_MSPLModel_MultipleSoftwareProductLine8(self):
        return self.__spinefm_MSPLModel_MultipleSoftwareProductLine8

    @spinefm_MSPLModel_MultipleSoftwareProductLine8.setter
    def spinefm_MSPLModel_MultipleSoftwareProductLine8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_MSPLModel_MultipleSoftwareProductLine__spinefm_MSPLModel_MultipleSoftwareProductLine8", None)
        self.__spinefm_MSPLModel_MultipleSoftwareProductLine8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DEAssociation"):
                    opp_val = getattr(item, "DEAssociation", None)
                    
                    if opp_val == self:
                        setattr(item, "DEAssociation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DEAssociation"):
                    opp_val = getattr(item, "DEAssociation", None)
                    
                    setattr(item, "DEAssociation", self)
                    

    def getDomainElementByName(self, name: str) -> str:
        # TODO: Implement getDomainElementByName method
        pass

    def getValidAssociationsForSourceAndTarget(self, target: str, source: str) -> str:
        # TODO: Implement getValidAssociationsForSourceAndTarget method
        pass

class spinefm_FMModel_Constraint:

    def __init__(self, Rule: str):
        self.Rule = Rule
        
    @property
    def Rule(self) -> str:
        return self.__Rule

    @Rule.setter
    def Rule(self, Rule: str):
        self.__Rule = Rule

class spinefm_FMModel_Group:

    def __init__(self, state: str, spinefm_FMModel_Group: set["Feature"] = None):
        self.state = state
        self.spinefm_FMModel_Group = spinefm_FMModel_Group if spinefm_FMModel_Group is not None else set()
        
    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def spinefm_FMModel_Group(self):
        return self.__spinefm_FMModel_Group

    @spinefm_FMModel_Group.setter
    def spinefm_FMModel_Group(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_FMModel_Group__spinefm_FMModel_Group", None)
        self.__spinefm_FMModel_Group = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Feature5"):
                    opp_val = getattr(item, "Feature5", None)
                    
                    if opp_val == self:
                        setattr(item, "Feature5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Feature5"):
                    opp_val = getattr(item, "Feature5", None)
                    
                    setattr(item, "Feature5", self)
                    

    def getAllChildren(self) -> str:
        # TODO: Implement getAllChildren method
        pass

class Group:

    pass
class Constraint:

    pass
class Feature:

    pass
class spinefm_FMModel_FeatureModel:

    def __init__(self, id: str, name: str, spinefm_FMModel_FeatureModel: "Feature" = None, spinefm_FMModel_FeatureModel2: set["Constraint"] = None):
        self.id = id
        self.name = name
        self.spinefm_FMModel_FeatureModel = spinefm_FMModel_FeatureModel
        self.spinefm_FMModel_FeatureModel2 = spinefm_FMModel_FeatureModel2 if spinefm_FMModel_FeatureModel2 is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def spinefm_FMModel_FeatureModel2(self):
        return self.__spinefm_FMModel_FeatureModel2

    @spinefm_FMModel_FeatureModel2.setter
    def spinefm_FMModel_FeatureModel2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_FMModel_FeatureModel__spinefm_FMModel_FeatureModel2", None)
        self.__spinefm_FMModel_FeatureModel2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Constraint"):
                    opp_val = getattr(item, "Constraint", None)
                    
                    if opp_val == self:
                        setattr(item, "Constraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Constraint"):
                    opp_val = getattr(item, "Constraint", None)
                    
                    setattr(item, "Constraint", self)
                    

    @property
    def spinefm_FMModel_FeatureModel(self):
        return self.__spinefm_FMModel_FeatureModel

    @spinefm_FMModel_FeatureModel.setter
    def spinefm_FMModel_FeatureModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_FMModel_FeatureModel__spinefm_FMModel_FeatureModel", None)
        self.__spinefm_FMModel_FeatureModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Feature"):
                opp_val = getattr(old_value, "Feature", None)
                if opp_val == self:
                    setattr(old_value, "Feature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Feature"):
                opp_val = getattr(value, "Feature", None)
                setattr(value, "Feature", self)

    def getFeatureFromName(self, name: str) -> str:
        # TODO: Implement getFeatureFromName method
        pass

    def addFeature(self, feature: str, name: str, state: str):
        # TODO: Implement addFeature method
        pass

    def getStateFT(self, feature: str) -> str:
        # TODO: Implement getStateFT method
        pass

class spinefm_FMModel_Feature:

    def __init__(self, id: str, name: str, spinefm_FMModel_Feature: set["Group"] = None):
        self.id = id
        self.name = name
        self.spinefm_FMModel_Feature = spinefm_FMModel_Feature if spinefm_FMModel_Feature is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def spinefm_FMModel_Feature(self):
        return self.__spinefm_FMModel_Feature

    @spinefm_FMModel_Feature.setter
    def spinefm_FMModel_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_FMModel_Feature__spinefm_FMModel_Feature", None)
        self.__spinefm_FMModel_Feature = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Group"):
                    opp_val = getattr(item, "Group", None)
                    
                    if opp_val == self:
                        setattr(item, "Group", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Group"):
                    opp_val = getattr(item, "Group", None)
                    
                    setattr(item, "Group", self)
                    

    def getAllChildrenFeatures(self) -> str:
        # TODO: Implement getAllChildrenFeatures method
        pass
