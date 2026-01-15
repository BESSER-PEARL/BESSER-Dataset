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
class ActionType(Enum):
    AUTOMATIC = "AUTOMATIC"
    MANUAL = "MANUAL"
    FM = "FM"


############################################
# Definition of Classes
############################################

class spinefm_ActionModel_Rule:

    def __init__(self, id: str, spinefm_ActionModel_Rule92: "ConfigurationState" = None, spinefm_ActionModel_Rule: "Action" = None):
        self.id = id
        self.spinefm_ActionModel_Rule92 = spinefm_ActionModel_Rule92
        self.spinefm_ActionModel_Rule = spinefm_ActionModel_Rule
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

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
            if hasattr(old_value, "Action90"):
                opp_val = getattr(old_value, "Action90", None)
                if opp_val == self:
                    setattr(old_value, "Action90", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Action90"):
                opp_val = getattr(value, "Action90", None)
                setattr(value, "Action90", self)

    @property
    def spinefm_ActionModel_Rule92(self):
        return self.__spinefm_ActionModel_Rule92

    @spinefm_ActionModel_Rule92.setter
    def spinefm_ActionModel_Rule92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_ActionModel_Rule__spinefm_ActionModel_Rule92", None)
        self.__spinefm_ActionModel_Rule92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ConfigurationState93"):
                opp_val = getattr(old_value, "ConfigurationState93", None)
                if opp_val == self:
                    setattr(old_value, "ConfigurationState93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ConfigurationState93"):
                opp_val = getattr(value, "ConfigurationState93", None)
                setattr(value, "ConfigurationState93", self)

    def createInverseRule(self) -> str:
        # TODO: Implement createInverseRule method
        pass

class spinefm_ActionModel_Action(ABC):

    def __init__(self, id: str, type: str, spinefm_ActionModel_Action: "Feature" = None, spinefm_ActionModel_Action97: "FeatureModel" = None):
        self.id = id
        self.type = type
        self.spinefm_ActionModel_Action = spinefm_ActionModel_Action
        self.spinefm_ActionModel_Action97 = spinefm_ActionModel_Action97
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def spinefm_ActionModel_Action97(self):
        return self.__spinefm_ActionModel_Action97

    @spinefm_ActionModel_Action97.setter
    def spinefm_ActionModel_Action97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_ActionModel_Action__spinefm_ActionModel_Action97", None)
        self.__spinefm_ActionModel_Action97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FeatureModel98"):
                opp_val = getattr(old_value, "FeatureModel98", None)
                if opp_val == self:
                    setattr(old_value, "FeatureModel98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FeatureModel98"):
                opp_val = getattr(value, "FeatureModel98", None)
                setattr(value, "FeatureModel98", self)

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
            if hasattr(old_value, "Feature95"):
                opp_val = getattr(old_value, "Feature95", None)
                if opp_val == self:
                    setattr(old_value, "Feature95", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Feature95"):
                opp_val = getattr(value, "Feature95", None)
                setattr(value, "Feature95", self)

    def applyAction(self, confName: str, fma: str):
        # TODO: Implement applyAction method
        pass

    def isSameObject(self, o: str) -> bool:
        # TODO: Implement isSameObject method
        pass

class spinefm_ActionModel_ConfigurationState:

    def __init__(self, id: str, spinefm_ActionModel_ConfigurationState: set["Feature"] = None, spinefm_ActionModel_ConfigurationState84: set["Feature"] = None, spinefm_ActionModel_ConfigurationState87: "FeatureModel" = None):
        self.id = id
        self.spinefm_ActionModel_ConfigurationState = spinefm_ActionModel_ConfigurationState if spinefm_ActionModel_ConfigurationState is not None else set()
        self.spinefm_ActionModel_ConfigurationState84 = spinefm_ActionModel_ConfigurationState84 if spinefm_ActionModel_ConfigurationState84 is not None else set()
        self.spinefm_ActionModel_ConfigurationState87 = spinefm_ActionModel_ConfigurationState87
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def spinefm_ActionModel_ConfigurationState84(self):
        return self.__spinefm_ActionModel_ConfigurationState84

    @spinefm_ActionModel_ConfigurationState84.setter
    def spinefm_ActionModel_ConfigurationState84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_ActionModel_ConfigurationState__spinefm_ActionModel_ConfigurationState84", None)
        self.__spinefm_ActionModel_ConfigurationState84 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Feature85"):
                    opp_val = getattr(item, "Feature85", None)
                    
                    if opp_val == self:
                        setattr(item, "Feature85", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Feature85"):
                    opp_val = getattr(item, "Feature85", None)
                    
                    setattr(item, "Feature85", self)
                    

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
                if hasattr(item, "Feature82"):
                    opp_val = getattr(item, "Feature82", None)
                    
                    if opp_val == self:
                        setattr(item, "Feature82", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Feature82"):
                    opp_val = getattr(item, "Feature82", None)
                    
                    setattr(item, "Feature82", self)
                    

    @property
    def spinefm_ActionModel_ConfigurationState87(self):
        return self.__spinefm_ActionModel_ConfigurationState87

    @spinefm_ActionModel_ConfigurationState87.setter
    def spinefm_ActionModel_ConfigurationState87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_ActionModel_ConfigurationState__spinefm_ActionModel_ConfigurationState87", None)
        self.__spinefm_ActionModel_ConfigurationState87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FeatureModel88"):
                opp_val = getattr(old_value, "FeatureModel88", None)
                if opp_val == self:
                    setattr(old_value, "FeatureModel88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FeatureModel88"):
                opp_val = getattr(value, "FeatureModel88", None)
                setattr(value, "FeatureModel88", self)

    def isIncludedIn(self, otherState: str) -> bool:
        # TODO: Implement isIncludedIn method
        pass

class Rule:

    pass
class spinefm_ActionModel_RestrictionFunction:

    def __init__(self, id: str, spinefm_ActionModel_RestrictionFunction: set["Rule"] = None, spinefm_ActionModel_RestrictionFunction79: "RestrictionFunction" = None):
        self.id = id
        self.spinefm_ActionModel_RestrictionFunction = spinefm_ActionModel_RestrictionFunction if spinefm_ActionModel_RestrictionFunction is not None else set()
        self.spinefm_ActionModel_RestrictionFunction79 = spinefm_ActionModel_RestrictionFunction79
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def spinefm_ActionModel_RestrictionFunction79(self):
        return self.__spinefm_ActionModel_RestrictionFunction79

    @spinefm_ActionModel_RestrictionFunction79.setter
    def spinefm_ActionModel_RestrictionFunction79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_ActionModel_RestrictionFunction__spinefm_ActionModel_RestrictionFunction79", None)
        self.__spinefm_ActionModel_RestrictionFunction79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RestrictionFunction80"):
                opp_val = getattr(old_value, "RestrictionFunction80", None)
                if opp_val == self:
                    setattr(old_value, "RestrictionFunction80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RestrictionFunction80"):
                opp_val = getattr(value, "RestrictionFunction80", None)
                setattr(value, "RestrictionFunction80", self)

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
            if hasattr(old_value, "Context76"):
                opp_val = getattr(old_value, "Context76", None)
                if opp_val == self:
                    setattr(old_value, "Context76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Context76"):
                opp_val = getattr(value, "Context76", None)
                setattr(value, "Context76", self)

class LocalContext:

    pass
class GlobalContext:

    pass
class Context:

    pass
class spinefm_ProcessModel_ContextManager:

    def __init__(self, spinefm_ProcessModel_ContextManager: "MultipleSoftwareProductLine" = None, spinefm_ProcessModel_ContextManager72: "GlobalContext" = None, spinefm_ProcessModel_ContextManager74: set["LocalContext"] = None):
        self.spinefm_ProcessModel_ContextManager = spinefm_ProcessModel_ContextManager
        self.spinefm_ProcessModel_ContextManager72 = spinefm_ProcessModel_ContextManager72
        self.spinefm_ProcessModel_ContextManager74 = spinefm_ProcessModel_ContextManager74 if spinefm_ProcessModel_ContextManager74 is not None else set()
        
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
            if hasattr(old_value, "MultipleSoftwareProductLine70"):
                opp_val = getattr(old_value, "MultipleSoftwareProductLine70", None)
                if opp_val == self:
                    setattr(old_value, "MultipleSoftwareProductLine70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MultipleSoftwareProductLine70"):
                opp_val = getattr(value, "MultipleSoftwareProductLine70", None)
                setattr(value, "MultipleSoftwareProductLine70", self)

    @property
    def spinefm_ProcessModel_ContextManager74(self):
        return self.__spinefm_ProcessModel_ContextManager74

    @spinefm_ProcessModel_ContextManager74.setter
    def spinefm_ProcessModel_ContextManager74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_ProcessModel_ContextManager__spinefm_ProcessModel_ContextManager74", None)
        self.__spinefm_ProcessModel_ContextManager74 = value if value is not None else set()
        
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
                    

    @property
    def spinefm_ProcessModel_ContextManager72(self):
        return self.__spinefm_ProcessModel_ContextManager72

    @spinefm_ProcessModel_ContextManager72.setter
    def spinefm_ProcessModel_ContextManager72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_ProcessModel_ContextManager__spinefm_ProcessModel_ContextManager72", None)
        self.__spinefm_ProcessModel_ContextManager72 = value
        
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

    def createNewContext(self) -> str:
        # TODO: Implement createNewContext method
        pass

    def setFMAdapter(self, fma: str):
        # TODO: Implement setFMAdapter method
        pass

    def propagate(self, CPS: str, context: str):
        # TODO: Implement propagate method
        pass

    def linkConfigurationsAndManageContexts(self, confSource: str, confTarget: str, association: str) -> str:
        # TODO: Implement linkConfigurationsAndManageContexts method
        pass

    def init(self):
        # TODO: Implement init method
        pass

    def createNewContextCloningCPS(self, cps: str) -> str:
        # TODO: Implement createNewContextCloningCPS method
        pass

    def getContextFromId(self, id: str) -> str:
        # TODO: Implement getContextFromId method
        pass

class spinefm_ProcessModel_LocalContext(Context):

    pass
class CompositeConfiguration:

    pass
class spinefm_ProcessModel_GlobalContext(Context):

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
                if hasattr(item, "ConfigurationProcessStep65"):
                    opp_val = getattr(item, "ConfigurationProcessStep65", None)
                    
                    if opp_val == self:
                        setattr(item, "ConfigurationProcessStep65", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ConfigurationProcessStep65"):
                    opp_val = getattr(item, "ConfigurationProcessStep65", None)
                    
                    setattr(item, "ConfigurationProcessStep65", self)
                    

    def addCPS(self, cps: str):
        # TODO: Implement addCPS method
        pass

    def mergeExternalCPS(self, externalCPS: str):
        # TODO: Implement mergeExternalCPS method
        pass

    def getCPSOfDE(self, de: str) -> str:
        # TODO: Implement getCPSOfDE method
        pass

class Action:

    pass
class spinefm_ActionModel_ActionSelect(Action):

    pass
class spinefm_ActionModel_ActionAddCTConstraint(Action):

    pass
class spinefm_ActionModel_ActionDeselect(Action):

    pass
class spinefm_ProcessModel_ConfigurationProcessStep:

    def __init__(self, userConfig: bool, id: str, description: str, spinefm_ProcessModel_ConfigurationProcessStep: set["Action"] = None, spinefm_ProcessModel_ConfigurationProcessStep55: "DomainElement" = None, spinefm_ProcessModel_ConfigurationProcessStep58: set["Action"] = None, Configuration63: "Configuration" = None, spinefm_ProcessModel_ConfigurationProcessStep61: "Context" = None):
        self.userConfig = userConfig
        self.id = id
        self.description = description
        self.spinefm_ProcessModel_ConfigurationProcessStep = spinefm_ProcessModel_ConfigurationProcessStep if spinefm_ProcessModel_ConfigurationProcessStep is not None else set()
        self.spinefm_ProcessModel_ConfigurationProcessStep55 = spinefm_ProcessModel_ConfigurationProcessStep55
        self.spinefm_ProcessModel_ConfigurationProcessStep58 = spinefm_ProcessModel_ConfigurationProcessStep58 if spinefm_ProcessModel_ConfigurationProcessStep58 is not None else set()
        self.Configuration63 = Configuration63
        self.spinefm_ProcessModel_ConfigurationProcessStep61 = spinefm_ProcessModel_ConfigurationProcessStep61
        
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
    def Configuration63(self):
        return self.__Configuration63

    @Configuration63.setter
    def Configuration63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_ProcessModel_ConfigurationProcessStep__Configuration63", None)
        self.__Configuration63 = value
        
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
    def spinefm_ProcessModel_ConfigurationProcessStep61(self):
        return self.__spinefm_ProcessModel_ConfigurationProcessStep61

    @spinefm_ProcessModel_ConfigurationProcessStep61.setter
    def spinefm_ProcessModel_ConfigurationProcessStep61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_ProcessModel_ConfigurationProcessStep__spinefm_ProcessModel_ConfigurationProcessStep61", None)
        self.__spinefm_ProcessModel_ConfigurationProcessStep61 = value
        
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
    def spinefm_ProcessModel_ConfigurationProcessStep55(self):
        return self.__spinefm_ProcessModel_ConfigurationProcessStep55

    @spinefm_ProcessModel_ConfigurationProcessStep55.setter
    def spinefm_ProcessModel_ConfigurationProcessStep55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_ProcessModel_ConfigurationProcessStep__spinefm_ProcessModel_ConfigurationProcessStep55", None)
        self.__spinefm_ProcessModel_ConfigurationProcessStep55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DomainElement56"):
                opp_val = getattr(old_value, "DomainElement56", None)
                if opp_val == self:
                    setattr(old_value, "DomainElement56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DomainElement56"):
                opp_val = getattr(value, "DomainElement56", None)
                setattr(value, "DomainElement56", self)

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
    def spinefm_ProcessModel_ConfigurationProcessStep58(self):
        return self.__spinefm_ProcessModel_ConfigurationProcessStep58

    @spinefm_ProcessModel_ConfigurationProcessStep58.setter
    def spinefm_ProcessModel_ConfigurationProcessStep58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_ProcessModel_ConfigurationProcessStep__spinefm_ProcessModel_ConfigurationProcessStep58", None)
        self.__spinefm_ProcessModel_ConfigurationProcessStep58 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Action59"):
                    opp_val = getattr(item, "Action59", None)
                    
                    if opp_val == self:
                        setattr(item, "Action59", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Action59"):
                    opp_val = getattr(item, "Action59", None)
                    
                    setattr(item, "Action59", self)
                    

    def alreadyHaveAction(self, a: str) -> bool:
        # TODO: Implement alreadyHaveAction method
        pass

    def getState(self) -> str:
        # TODO: Implement getState method
        pass

    def setFMA(self, fma: str):
        # TODO: Implement setFMA method
        pass

    def mergeWithExternalCPS(self, cps: str):
        # TODO: Implement mergeWithExternalCPS method
        pass

    def isCompatibleWithConfiguration(self, conf: str) -> bool:
        # TODO: Implement isCompatibleWithConfiguration method
        pass

    def isComplete(self) -> bool:
        # TODO: Implement isComplete method
        pass

    def addActionToDo(self, a: str):
        # TODO: Implement addActionToDo method
        pass

    def getConfName(self) -> str:
        # TODO: Implement getConfName method
        pass

    def apply(self) -> bool:
        # TODO: Implement apply method
        pass

class MultipleSoftwareProductLine:

    pass
class FeatureModel:

    pass
class spinefm_ConfigurationModel_CompositeConfiguration:

    def __init__(self, name: str, spinefm_ConfigurationModel_CompositeConfiguration: set["Configuration"] = None, spinefm_ConfigurationModel_CompositeConfiguration49: set["Link"] = None, spinefm_ConfigurationModel_CompositeConfiguration52: "MultipleSoftwareProductLine" = None):
        self.name = name
        self.spinefm_ConfigurationModel_CompositeConfiguration = spinefm_ConfigurationModel_CompositeConfiguration if spinefm_ConfigurationModel_CompositeConfiguration is not None else set()
        self.spinefm_ConfigurationModel_CompositeConfiguration49 = spinefm_ConfigurationModel_CompositeConfiguration49 if spinefm_ConfigurationModel_CompositeConfiguration49 is not None else set()
        self.spinefm_ConfigurationModel_CompositeConfiguration52 = spinefm_ConfigurationModel_CompositeConfiguration52
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def spinefm_ConfigurationModel_CompositeConfiguration52(self):
        return self.__spinefm_ConfigurationModel_CompositeConfiguration52

    @spinefm_ConfigurationModel_CompositeConfiguration52.setter
    def spinefm_ConfigurationModel_CompositeConfiguration52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_ConfigurationModel_CompositeConfiguration__spinefm_ConfigurationModel_CompositeConfiguration52", None)
        self.__spinefm_ConfigurationModel_CompositeConfiguration52 = value
        
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
    def spinefm_ConfigurationModel_CompositeConfiguration49(self):
        return self.__spinefm_ConfigurationModel_CompositeConfiguration49

    @spinefm_ConfigurationModel_CompositeConfiguration49.setter
    def spinefm_ConfigurationModel_CompositeConfiguration49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_ConfigurationModel_CompositeConfiguration__spinefm_ConfigurationModel_CompositeConfiguration49", None)
        self.__spinefm_ConfigurationModel_CompositeConfiguration49 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Link50"):
                    opp_val = getattr(item, "Link50", None)
                    
                    if opp_val == self:
                        setattr(item, "Link50", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Link50"):
                    opp_val = getattr(item, "Link50", None)
                    
                    setattr(item, "Link50", self)
                    

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
                if hasattr(item, "Configuration47"):
                    opp_val = getattr(item, "Configuration47", None)
                    
                    if opp_val == self:
                        setattr(item, "Configuration47", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Configuration47"):
                    opp_val = getattr(item, "Configuration47", None)
                    
                    setattr(item, "Configuration47", self)
                    

    def getCompatibleConfigurations(self, asso: str, confSource: str) -> str:
        # TODO: Implement getCompatibleConfigurations method
        pass

    def isValid(self) -> bool:
        # TODO: Implement isValid method
        pass

    def getConfigurationByName(self, confName: str) -> str:
        # TODO: Implement getConfigurationByName method
        pass

    def addConfiguration(self, conf: str):
        # TODO: Implement addConfiguration method
        pass

    def createConfigurationLink(self, confSource: str, asso: str, confTarget: str):
        # TODO: Implement createConfigurationLink method
        pass

class Configuration:

    pass
class spinefm_ConfigurationModel_Link:

    def __init__(self, id: str, spinefm_ConfigurationModel_Link: "Configuration" = None, spinefm_ConfigurationModel_Link41: "DEAssociation" = None, spinefm_ConfigurationModel_Link44: "Configuration" = None):
        self.id = id
        self.spinefm_ConfigurationModel_Link = spinefm_ConfigurationModel_Link
        self.spinefm_ConfigurationModel_Link41 = spinefm_ConfigurationModel_Link41
        self.spinefm_ConfigurationModel_Link44 = spinefm_ConfigurationModel_Link44
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def spinefm_ConfigurationModel_Link44(self):
        return self.__spinefm_ConfigurationModel_Link44

    @spinefm_ConfigurationModel_Link44.setter
    def spinefm_ConfigurationModel_Link44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_ConfigurationModel_Link__spinefm_ConfigurationModel_Link44", None)
        self.__spinefm_ConfigurationModel_Link44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Configuration45"):
                opp_val = getattr(old_value, "Configuration45", None)
                if opp_val == self:
                    setattr(old_value, "Configuration45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Configuration45"):
                opp_val = getattr(value, "Configuration45", None)
                setattr(value, "Configuration45", self)

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
    def spinefm_ConfigurationModel_Link41(self):
        return self.__spinefm_ConfigurationModel_Link41

    @spinefm_ConfigurationModel_Link41.setter
    def spinefm_ConfigurationModel_Link41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_ConfigurationModel_Link__spinefm_ConfigurationModel_Link41", None)
        self.__spinefm_ConfigurationModel_Link41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DEAssociation42"):
                opp_val = getattr(old_value, "DEAssociation42", None)
                if opp_val == self:
                    setattr(old_value, "DEAssociation42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DEAssociation42"):
                opp_val = getattr(value, "DEAssociation42", None)
                setattr(value, "DEAssociation42", self)

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

    def __init__(self, id: str, description: str, ConfigurationProcessStep: "ConfigurationProcessStep" = None, spinefm_ConfigurationModel_Configuration: set["Link"] = None, spinefm_ConfigurationModel_Configuration32: "ConfigurationState" = None, spinefm_ConfigurationModel_Configuration34: "DomainElement" = None, spinefm_ConfigurationModel_Configuration37: set["ConfigurationProcessStep"] = None):
        self.id = id
        self.description = description
        self.ConfigurationProcessStep = ConfigurationProcessStep
        self.spinefm_ConfigurationModel_Configuration = spinefm_ConfigurationModel_Configuration if spinefm_ConfigurationModel_Configuration is not None else set()
        self.spinefm_ConfigurationModel_Configuration32 = spinefm_ConfigurationModel_Configuration32
        self.spinefm_ConfigurationModel_Configuration34 = spinefm_ConfigurationModel_Configuration34
        self.spinefm_ConfigurationModel_Configuration37 = spinefm_ConfigurationModel_Configuration37 if spinefm_ConfigurationModel_Configuration37 is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def spinefm_ConfigurationModel_Configuration34(self):
        return self.__spinefm_ConfigurationModel_Configuration34

    @spinefm_ConfigurationModel_Configuration34.setter
    def spinefm_ConfigurationModel_Configuration34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_ConfigurationModel_Configuration__spinefm_ConfigurationModel_Configuration34", None)
        self.__spinefm_ConfigurationModel_Configuration34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DomainElement35"):
                opp_val = getattr(old_value, "DomainElement35", None)
                if opp_val == self:
                    setattr(old_value, "DomainElement35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DomainElement35"):
                opp_val = getattr(value, "DomainElement35", None)
                setattr(value, "DomainElement35", self)

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
    def spinefm_ConfigurationModel_Configuration37(self):
        return self.__spinefm_ConfigurationModel_Configuration37

    @spinefm_ConfigurationModel_Configuration37.setter
    def spinefm_ConfigurationModel_Configuration37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_ConfigurationModel_Configuration__spinefm_ConfigurationModel_Configuration37", None)
        self.__spinefm_ConfigurationModel_Configuration37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ConfigurationProcessStep38"):
                    opp_val = getattr(item, "ConfigurationProcessStep38", None)
                    
                    if opp_val == self:
                        setattr(item, "ConfigurationProcessStep38", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ConfigurationProcessStep38"):
                    opp_val = getattr(item, "ConfigurationProcessStep38", None)
                    
                    setattr(item, "ConfigurationProcessStep38", self)
                    

    def getAllCPS(self) -> str:
        # TODO: Implement getAllCPS method
        pass

    def getLinkedConfigurationsOfDomainElement(self, de: str) -> str:
        # TODO: Implement getLinkedConfigurationsOfDomainElement method
        pass

    def getFeatureModel(self) -> str:
        # TODO: Implement getFeatureModel method
        pass

    def isCompletlyLinked(self) -> bool:
        # TODO: Implement isCompletlyLinked method
        pass

    def canBeLinked(self, association: str) -> bool:
        # TODO: Implement canBeLinked method
        pass

class DEAssociation:

    pass
class DomainElement:

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

    def respectBoundaries(self, value: int) -> bool:
        # TODO: Implement respectBoundaries method
        pass

    def isExactlyOne(self) -> bool:
        # TODO: Implement isExactlyOne method
        pass

    def isLowerThanUpperBound(self, value: int) -> bool:
        # TODO: Implement isLowerThanUpperBound method
        pass

class DEAssociationEnd:

    pass
class RestrictionFunction:

    pass
class spinefm_MSPLModel_DEAssociation:

    def __init__(self, id: str, spinefm_MSPLModel_DEAssociation: set["RestrictionFunction"] = None, spinefm_MSPLModel_DEAssociation11: "DEAssociationEnd" = None, spinefm_MSPLModel_DEAssociation13: "DEAssociationEnd" = None, spinefm_MSPLModel_DEAssociation16: "DEAssociation" = None):
        self.id = id
        self.spinefm_MSPLModel_DEAssociation = spinefm_MSPLModel_DEAssociation if spinefm_MSPLModel_DEAssociation is not None else set()
        self.spinefm_MSPLModel_DEAssociation11 = spinefm_MSPLModel_DEAssociation11
        self.spinefm_MSPLModel_DEAssociation13 = spinefm_MSPLModel_DEAssociation13
        self.spinefm_MSPLModel_DEAssociation16 = spinefm_MSPLModel_DEAssociation16
        
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

class spinefm_MSPLModel_MultipleSoftwareProductLine:

    def __init__(self, spinefm_MSPLModel_MultipleSoftwareProductLine: set["DomainElement"] = None, spinefm_MSPLModel_MultipleSoftwareProductLine8: set["DEAssociation"] = None):
        self.spinefm_MSPLModel_MultipleSoftwareProductLine = spinefm_MSPLModel_MultipleSoftwareProductLine if spinefm_MSPLModel_MultipleSoftwareProductLine is not None else set()
        self.spinefm_MSPLModel_MultipleSoftwareProductLine8 = spinefm_MSPLModel_MultipleSoftwareProductLine8 if spinefm_MSPLModel_MultipleSoftwareProductLine8 is not None else set()
        
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
class spinefm_FMModel_Feature:

    def __init__(self, id: str, name: str, spinefm_FMModel_Feature: set["Group"] = None):
        self.id = id
        self.name = name
        self.spinefm_FMModel_Feature = spinefm_FMModel_Feature if spinefm_FMModel_Feature is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

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
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

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
                    

    def getFeatureFromName(self, name: str) -> str:
        # TODO: Implement getFeatureFromName method
        pass

    def addFeature(self, state: str, feature: str, name: str):
        # TODO: Implement addFeature method
        pass

    def getStateFT(self, feature: str) -> str:
        # TODO: Implement getStateFT method
        pass
