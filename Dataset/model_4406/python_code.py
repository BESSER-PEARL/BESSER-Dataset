from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class CPSStatus(Enum):
    PartiallyConfigured = "PartiallyConfigured"
    Configured = "Configured"
    Unconfigurable = "Unconfigurable"
class GroupState(Enum):
    MANDATORY = "MANDATORY"
    OPTIONAL = "OPTIONAL"
    ALTERNATIVE = "ALTERNATIVE"
    OR = "OR"
    MUTEX = "MUTEX"
class ActionMode(Enum):
    AUTOMATIC = "AUTOMATIC"
    MANUAL = "MANUAL"
    FM = "FM"


############################################
# Definition of Classes
############################################

class spinefm_RFModel_Rule:

    def __init__(self, id: str, spinefm_RFModel_Rule: "SystemActionModel_ActionOnFM" = None, spinefm_RFModel_Rule164: "ConfigurationState" = None):
        self.id = id
        self.spinefm_RFModel_Rule = spinefm_RFModel_Rule
        self.spinefm_RFModel_Rule164 = spinefm_RFModel_Rule164
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def spinefm_RFModel_Rule164(self):
        return self.__spinefm_RFModel_Rule164

    @spinefm_RFModel_Rule164.setter
    def spinefm_RFModel_Rule164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_RFModel_Rule__spinefm_RFModel_Rule164", None)
        self.__spinefm_RFModel_Rule164 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ConfigurationState165"):
                opp_val = getattr(old_value, "ConfigurationState165", None)
                if opp_val == self:
                    setattr(old_value, "ConfigurationState165", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ConfigurationState165"):
                opp_val = getattr(value, "ConfigurationState165", None)
                setattr(value, "ConfigurationState165", self)

    @property
    def spinefm_RFModel_Rule(self):
        return self.__spinefm_RFModel_Rule

    @spinefm_RFModel_Rule.setter
    def spinefm_RFModel_Rule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_RFModel_Rule__spinefm_RFModel_Rule", None)
        self.__spinefm_RFModel_Rule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SystemActionModel_ActionOnFM162"):
                opp_val = getattr(old_value, "SystemActionModel_ActionOnFM162", None)
                if opp_val == self:
                    setattr(old_value, "SystemActionModel_ActionOnFM162", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SystemActionModel_ActionOnFM162"):
                opp_val = getattr(value, "SystemActionModel_ActionOnFM162", None)
                setattr(value, "SystemActionModel_ActionOnFM162", self)

    def createInverseRule(self) :
        # TODO: Implement createInverseRule method
        pass

class spinefm_RFModel_ConfigurationState:

    def __init__(self, id: str, spinefm_RFModel_ConfigurationState: set["Feature"] = None, spinefm_RFModel_ConfigurationState156: set["Feature"] = None, spinefm_RFModel_ConfigurationState159: "FeatureModel" = None):
        self.id = id
        self.spinefm_RFModel_ConfigurationState = spinefm_RFModel_ConfigurationState if spinefm_RFModel_ConfigurationState is not None else set()
        self.spinefm_RFModel_ConfigurationState156 = spinefm_RFModel_ConfigurationState156 if spinefm_RFModel_ConfigurationState156 is not None else set()
        self.spinefm_RFModel_ConfigurationState159 = spinefm_RFModel_ConfigurationState159
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def spinefm_RFModel_ConfigurationState159(self):
        return self.__spinefm_RFModel_ConfigurationState159

    @spinefm_RFModel_ConfigurationState159.setter
    def spinefm_RFModel_ConfigurationState159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_RFModel_ConfigurationState__spinefm_RFModel_ConfigurationState159", None)
        self.__spinefm_RFModel_ConfigurationState159 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FeatureModel160"):
                opp_val = getattr(old_value, "FeatureModel160", None)
                if opp_val == self:
                    setattr(old_value, "FeatureModel160", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FeatureModel160"):
                opp_val = getattr(value, "FeatureModel160", None)
                setattr(value, "FeatureModel160", self)

    @property
    def spinefm_RFModel_ConfigurationState(self):
        return self.__spinefm_RFModel_ConfigurationState

    @spinefm_RFModel_ConfigurationState.setter
    def spinefm_RFModel_ConfigurationState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_RFModel_ConfigurationState__spinefm_RFModel_ConfigurationState", None)
        self.__spinefm_RFModel_ConfigurationState = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Feature154"):
                    opp_val = getattr(item, "Feature154", None)
                    
                    if opp_val == self:
                        setattr(item, "Feature154", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Feature154"):
                    opp_val = getattr(item, "Feature154", None)
                    
                    setattr(item, "Feature154", self)
                    

    @property
    def spinefm_RFModel_ConfigurationState156(self):
        return self.__spinefm_RFModel_ConfigurationState156

    @spinefm_RFModel_ConfigurationState156.setter
    def spinefm_RFModel_ConfigurationState156(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_RFModel_ConfigurationState__spinefm_RFModel_ConfigurationState156", None)
        self.__spinefm_RFModel_ConfigurationState156 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Feature157"):
                    opp_val = getattr(item, "Feature157", None)
                    
                    if opp_val == self:
                        setattr(item, "Feature157", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Feature157"):
                    opp_val = getattr(item, "Feature157", None)
                    
                    setattr(item, "Feature157", self)
                    

    def isIncludedIn(self, spinefm_otherState) :
        # TODO: Implement isIncludedIn method
        pass

class Rule:

    pass
class spinefm_RFModel_RestrictionFunction:

    def __init__(self, id: str, spinefm_RFModel_RestrictionFunction: set["Rule"] = None, spinefm_RFModel_RestrictionFunction145: "RestrictionFunction" = None, spinefm_RFModel_RestrictionFunction148: "DomainElement" = None, spinefm_RFModel_RestrictionFunction151: "DomainElement" = None):
        self.id = id
        self.spinefm_RFModel_RestrictionFunction = spinefm_RFModel_RestrictionFunction if spinefm_RFModel_RestrictionFunction is not None else set()
        self.spinefm_RFModel_RestrictionFunction145 = spinefm_RFModel_RestrictionFunction145
        self.spinefm_RFModel_RestrictionFunction148 = spinefm_RFModel_RestrictionFunction148
        self.spinefm_RFModel_RestrictionFunction151 = spinefm_RFModel_RestrictionFunction151
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def spinefm_RFModel_RestrictionFunction151(self):
        return self.__spinefm_RFModel_RestrictionFunction151

    @spinefm_RFModel_RestrictionFunction151.setter
    def spinefm_RFModel_RestrictionFunction151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_RFModel_RestrictionFunction__spinefm_RFModel_RestrictionFunction151", None)
        self.__spinefm_RFModel_RestrictionFunction151 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DomainElement152"):
                opp_val = getattr(old_value, "DomainElement152", None)
                if opp_val == self:
                    setattr(old_value, "DomainElement152", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DomainElement152"):
                opp_val = getattr(value, "DomainElement152", None)
                setattr(value, "DomainElement152", self)

    @property
    def spinefm_RFModel_RestrictionFunction(self):
        return self.__spinefm_RFModel_RestrictionFunction

    @spinefm_RFModel_RestrictionFunction.setter
    def spinefm_RFModel_RestrictionFunction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_RFModel_RestrictionFunction__spinefm_RFModel_RestrictionFunction", None)
        self.__spinefm_RFModel_RestrictionFunction = value if value is not None else set()
        
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
    def spinefm_RFModel_RestrictionFunction148(self):
        return self.__spinefm_RFModel_RestrictionFunction148

    @spinefm_RFModel_RestrictionFunction148.setter
    def spinefm_RFModel_RestrictionFunction148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_RFModel_RestrictionFunction__spinefm_RFModel_RestrictionFunction148", None)
        self.__spinefm_RFModel_RestrictionFunction148 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DomainElement149"):
                opp_val = getattr(old_value, "DomainElement149", None)
                if opp_val == self:
                    setattr(old_value, "DomainElement149", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DomainElement149"):
                opp_val = getattr(value, "DomainElement149", None)
                setattr(value, "DomainElement149", self)

    @property
    def spinefm_RFModel_RestrictionFunction145(self):
        return self.__spinefm_RFModel_RestrictionFunction145

    @spinefm_RFModel_RestrictionFunction145.setter
    def spinefm_RFModel_RestrictionFunction145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_RFModel_RestrictionFunction__spinefm_RFModel_RestrictionFunction145", None)
        self.__spinefm_RFModel_RestrictionFunction145 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RestrictionFunction146"):
                opp_val = getattr(old_value, "RestrictionFunction146", None)
                if opp_val == self:
                    setattr(old_value, "RestrictionFunction146", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RestrictionFunction146"):
                opp_val = getattr(value, "RestrictionFunction146", None)
                setattr(value, "RestrictionFunction146", self)

    def createAndAssociateInverseRestFunc(self) :
        # TODO: Implement createAndAssociateInverseRestFunc method
        pass

class spinefm_HistoryModel_Past:

    def __init__(self, id: str, rootPath: str, modelPath: str, description: str, spinefm_HistoryModel_Past: set["Step"] = None, spinefm_HistoryModel_Past141: set["LocalContext"] = None):
        self.id = id
        self.rootPath = rootPath
        self.modelPath = modelPath
        self.description = description
        self.spinefm_HistoryModel_Past = spinefm_HistoryModel_Past if spinefm_HistoryModel_Past is not None else set()
        self.spinefm_HistoryModel_Past141 = spinefm_HistoryModel_Past141 if spinefm_HistoryModel_Past141 is not None else set()
        
        pass
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def modelPath(self):
        return self.__modelPath

    @modelPath.setter
    def modelPath(self, modelPath: str):
        self.__modelPath = modelPath


    @property
    def rootPath(self):
        return self.__rootPath

    @rootPath.setter
    def rootPath(self, rootPath: str):
        self.__rootPath = rootPath


    @property
    def spinefm_HistoryModel_Past141(self):
        return self.__spinefm_HistoryModel_Past141

    @spinefm_HistoryModel_Past141.setter
    def spinefm_HistoryModel_Past141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_HistoryModel_Past__spinefm_HistoryModel_Past141", None)
        self.__spinefm_HistoryModel_Past141 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "LocalContext142"):
                    opp_val = getattr(item, "LocalContext142", None)
                    
                    if opp_val == self:
                        setattr(item, "LocalContext142", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "LocalContext142"):
                    opp_val = getattr(item, "LocalContext142", None)
                    
                    setattr(item, "LocalContext142", self)
                    

    @property
    def spinefm_HistoryModel_Past(self):
        return self.__spinefm_HistoryModel_Past

    @spinefm_HistoryModel_Past.setter
    def spinefm_HistoryModel_Past(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_HistoryModel_Past__spinefm_HistoryModel_Past", None)
        self.__spinefm_HistoryModel_Past = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Step139"):
                    opp_val = getattr(item, "Step139", None)
                    
                    if opp_val == self:
                        setattr(item, "Step139", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Step139"):
                    opp_val = getattr(item, "Step139", None)
                    
                    setattr(item, "Step139", self)
                    

    def undoLastAction(self):
        # TODO: Implement undoLastAction method
        pass

    def createStep(self, spinefm_action) :
        # TODO: Implement createStep method
        pass

    def undoAction(self, spinefm_step):
        # TODO: Implement undoAction method
        pass

    def clonePastWithoutSystemActions(self) :
        # TODO: Implement clonePastWithoutSystemActions method
        pass

    def getStepFromId(self, spinefm_stepId) :
        # TODO: Implement getStepFromId method
        pass

class SystemActionModel_SystemAction:

    pass
class UserActionModel_UserAction:

    pass
class spinefm_HistoryModel_Step:

    def __init__(self, id: str, step: "UserActionModel_UserAction" = None, step137: set["SystemActionModel_SystemAction"] = None):
        self.id = id
        self.step = step
        self.step137 = step137 if step137 is not None else set()
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def step137(self):
        return self.__step137

    @step137.setter
    def step137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_HistoryModel_Step__step137", None)
        self.__step137 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SystemAction"):
                    opp_val = getattr(item, "SystemAction", None)
                    
                    if opp_val == self:
                        setattr(item, "SystemAction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SystemAction"):
                    opp_val = getattr(item, "SystemAction", None)
                    
                    setattr(item, "SystemAction", self)
                    

    @property
    def step(self):
        return self.__step

    @step.setter
    def step(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_HistoryModel_Step__step", None)
        self.__step = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UserAction"):
                opp_val = getattr(old_value, "UserAction", None)
                if opp_val == self:
                    setattr(old_value, "UserAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UserAction"):
                opp_val = getattr(value, "UserAction", None)
                setattr(value, "UserAction", self)

    def getDescription(self) :
        # TODO: Implement getDescription method
        pass

    def undoActions(self):
        # TODO: Implement undoActions method
        pass

    def cloneStepWithoutSystemActions(self) :
        # TODO: Implement cloneStepWithoutSystemActions method
        pass

class UserActionModel_spinefm_EObject:

    pass
class UserAction:

    pass
class spinefm_UserActionModel_UserPropagate(UserAction):

    def __init__(self, domainElementName: str, contextID: str):
        self.domainElementName = domainElementName
        self.contextID = contextID
        
        pass
    @property
    def domainElementName(self):
        return self.__domainElementName

    @domainElementName.setter
    def domainElementName(self, domainElementName: str):
        self.__domainElementName = domainElementName


    @property
    def contextID(self):
        return self.__contextID

    @contextID.setter
    def contextID(self, contextID: str):
        self.__contextID = contextID


class spinefm_UserActionModel_UserGenerate(UserAction):

    def __init__(self, path: str):
        self.path = path
        
        pass
    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path


class spinefm_UserActionModel_UserValidConfiguration(UserAction):

    def __init__(self, domainElementName: str, contextID: str):
        self.domainElementName = domainElementName
        self.contextID = contextID
        
        pass
    @property
    def contextID(self):
        return self.__contextID

    @contextID.setter
    def contextID(self, contextID: str):
        self.__contextID = contextID


    @property
    def domainElementName(self):
        return self.__domainElementName

    @domainElementName.setter
    def domainElementName(self, domainElementName: str):
        self.__domainElementName = domainElementName


class spinefm_UserActionModel_UserRenameElement(UserAction):

    def __init__(self, name: str, elementType: str, elementID: str):
        self.name = name
        self.elementType = elementType
        self.elementID = elementID
        
        pass
    @property
    def elementType(self):
        return self.__elementType

    @elementType.setter
    def elementType(self, elementType: str):
        self.__elementType = elementType


    @property
    def elementID(self):
        return self.__elementID

    @elementID.setter
    def elementID(self, elementID: str):
        self.__elementID = elementID


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class spinefm_UserActionModel_UserSavePast(UserAction):

    def __init__(self, destPath: str):
        self.destPath = destPath
        
        pass
    @property
    def destPath(self):
        return self.__destPath

    @destPath.setter
    def destPath(self, destPath: str):
        self.__destPath = destPath


class spinefm_UserActionModel_UserDeselect(UserAction):

    def __init__(self, domainElementName: str, contextID: str, featureName: str):
        self.domainElementName = domainElementName
        self.contextID = contextID
        self.featureName = featureName
        
        pass
    @property
    def domainElementName(self):
        return self.__domainElementName

    @domainElementName.setter
    def domainElementName(self, domainElementName: str):
        self.__domainElementName = domainElementName


    @property
    def contextID(self):
        return self.__contextID

    @contextID.setter
    def contextID(self, contextID: str):
        self.__contextID = contextID


    @property
    def featureName(self):
        return self.__featureName

    @featureName.setter
    def featureName(self, featureName: str):
        self.__featureName = featureName


class spinefm_UserActionModel_UserInit(UserAction):

    def __init__(self, filePath: str, pastPath: str, confDescription: str):
        self.filePath = filePath
        self.pastPath = pastPath
        self.confDescription = confDescription
        
        pass
    @property
    def confDescription(self):
        return self.__confDescription

    @confDescription.setter
    def confDescription(self, confDescription: str):
        self.__confDescription = confDescription


    @property
    def pastPath(self):
        return self.__pastPath

    @pastPath.setter
    def pastPath(self, pastPath: str):
        self.__pastPath = pastPath


    @property
    def filePath(self):
        return self.__filePath

    @filePath.setter
    def filePath(self, filePath: str):
        self.__filePath = filePath


class spinefm_UserActionModel_UserCreateContext(UserAction):

    pass
class spinefm_UserActionModel_UserLinkConfiguration(UserAction):

    def __init__(self, confSourceName: str, confTargetName: str, assoName: str):
        self.confSourceName = confSourceName
        self.confTargetName = confTargetName
        self.assoName = assoName
        
        pass
    @property
    def assoName(self):
        return self.__assoName

    @assoName.setter
    def assoName(self, assoName: str):
        self.__assoName = assoName


    @property
    def confSourceName(self):
        return self.__confSourceName

    @confSourceName.setter
    def confSourceName(self, confSourceName: str):
        self.__confSourceName = confSourceName


    @property
    def confTargetName(self):
        return self.__confTargetName

    @confTargetName.setter
    def confTargetName(self, confTargetName: str):
        self.__confTargetName = confTargetName


class spinefm_UserActionModel_UserCloneContext(UserAction):

    def __init__(self, contextID: str):
        self.contextID = contextID
        
        pass
    @property
    def contextID(self):
        return self.__contextID

    @contextID.setter
    def contextID(self, contextID: str):
        self.__contextID = contextID


class spinefm_UserActionModel_UserSelect(UserAction):

    def __init__(self, contextID: str, featureName: str, domainElementName: str):
        self.contextID = contextID
        self.featureName = featureName
        self.domainElementName = domainElementName
        
        pass
    @property
    def domainElementName(self):
        return self.__domainElementName

    @domainElementName.setter
    def domainElementName(self, domainElementName: str):
        self.__domainElementName = domainElementName


    @property
    def featureName(self):
        return self.__featureName

    @featureName.setter
    def featureName(self, featureName: str):
        self.__featureName = featureName


    @property
    def contextID(self):
        return self.__contextID

    @contextID.setter
    def contextID(self, contextID: str):
        self.__contextID = contextID


class spinefm_UserActionModel_UserAction(ABC):

    def __init__(self, type: str, launchingAction: "Step" = None, spinefm_UserActionModel_UserAction: "ContextManager" = None, spinefm_UserActionModel_UserAction134: "UserActionModel_spinefm_EObject" = None):
        self.type = type
        self.launchingAction = launchingAction
        self.spinefm_UserActionModel_UserAction = spinefm_UserActionModel_UserAction
        self.spinefm_UserActionModel_UserAction134 = spinefm_UserActionModel_UserAction134
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def launchingAction(self):
        return self.__launchingAction

    @launchingAction.setter
    def launchingAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_UserActionModel_UserAction__launchingAction", None)
        self.__launchingAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Step130"):
                opp_val = getattr(old_value, "Step130", None)
                if opp_val == self:
                    setattr(old_value, "Step130", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Step130"):
                opp_val = getattr(value, "Step130", None)
                setattr(value, "Step130", self)

    @property
    def spinefm_UserActionModel_UserAction(self):
        return self.__spinefm_UserActionModel_UserAction

    @spinefm_UserActionModel_UserAction.setter
    def spinefm_UserActionModel_UserAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_UserActionModel_UserAction__spinefm_UserActionModel_UserAction", None)
        self.__spinefm_UserActionModel_UserAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ContextManager132"):
                opp_val = getattr(old_value, "ContextManager132", None)
                if opp_val == self:
                    setattr(old_value, "ContextManager132", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ContextManager132"):
                opp_val = getattr(value, "ContextManager132", None)
                setattr(value, "ContextManager132", self)

    @property
    def spinefm_UserActionModel_UserAction134(self):
        return self.__spinefm_UserActionModel_UserAction134

    @spinefm_UserActionModel_UserAction134.setter
    def spinefm_UserActionModel_UserAction134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_UserActionModel_UserAction__spinefm_UserActionModel_UserAction134", None)
        self.__spinefm_UserActionModel_UserAction134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UserActionModel_spinefm_EObject"):
                opp_val = getattr(old_value, "UserActionModel_spinefm_EObject", None)
                if opp_val == self:
                    setattr(old_value, "UserActionModel_spinefm_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UserActionModel_spinefm_EObject"):
                opp_val = getattr(value, "UserActionModel_spinefm_EObject", None)
                setattr(value, "UserActionModel_spinefm_EObject", self)

    def cloneActionWithStringAttributes(self) :
        # TODO: Implement cloneActionWithStringAttributes method
        pass

    def postcondition(self):
        # TODO: Implement postcondition method
        pass

    def initManualAction(self, spinefm_contextManager):
        # TODO: Implement initManualAction method
        pass

    def getDescription(self) :
        # TODO: Implement getDescription method
        pass

    def precondition(self) :
        # TODO: Implement precondition method
        pass

    def transformContextNameToSave(self, spinefm_contextID) :
        # TODO: Implement transformContextNameToSave method
        pass

    def apply(self):
        # TODO: Implement apply method
        pass

class ActionAbstractRename:

    pass
class spinefm_SystemActionModel_ActionRenameProduct(ActionAbstractRename):

    pass
class spinefm_SystemActionModel_ActionRenameConfig(ActionAbstractRename):

    pass
class spinefm_SystemActionModel_ActionSetProductDescription(ActionAbstractRename):

    pass
class spinefm_SystemActionModel_ActionRenameCPS(ActionAbstractRename):

    pass
class ActionOnFM:

    pass
class spinefm_SystemActionModel_ActionAddCTConstraint(ActionOnFM):

    pass
class spinefm_SystemActionModel_ActionDeselect(ActionOnFM):

    pass
class spinefm_SystemActionModel_ActionSelect(ActionOnFM):

    pass
class spinefm_SystemActionModel_SystemAction(ABC):

    def __init__(self, cpsHistory: str, type: str, launchedActions: "Step" = None):
        self.cpsHistory = cpsHistory
        self.type = type
        self.launchedActions = launchedActions
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def cpsHistory(self):
        return self.__cpsHistory

    @cpsHistory.setter
    def cpsHistory(self, cpsHistory: str):
        self.__cpsHistory = cpsHistory


    @property
    def launchedActions(self):
        return self.__launchedActions

    @launchedActions.setter
    def launchedActions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_SystemActionModel_SystemAction__launchedActions", None)
        self.__launchedActions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Step"):
                opp_val = getattr(old_value, "Step", None)
                if opp_val == self:
                    setattr(old_value, "Step", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Step"):
                opp_val = getattr(value, "Step", None)
                setattr(value, "Step", self)

    def undo(self):
        # TODO: Implement undo method
        pass

    def isSameObject(self, spinefm_o) :
        # TODO: Implement isSameObject method
        pass

    def apply(self):
        # TODO: Implement apply method
        pass

class ContextManager:

    pass
class SystemAction:

    pass
class spinefm_SystemActionModel_ActionLink(SystemAction):

    pass
class spinefm_SystemActionModel_ActionDeleteContext(SystemAction):

    pass
class spinefm_SystemActionModel_ActionCreateContext(SystemAction):

    pass
class spinefm_SystemActionModel_ActionAbstractRename(SystemAction):

    def __init__(self, oldName: str, newName: str):
        self.oldName = oldName
        self.newName = newName
        
        pass
    @property
    def oldName(self):
        return self.__oldName

    @oldName.setter
    def oldName(self, oldName: str):
        self.__oldName = oldName


    @property
    def newName(self):
        return self.__newName

    @newName.setter
    def newName(self, newName: str):
        self.__newName = newName


class spinefm_SystemActionModel_ActionMoveConfiguration(SystemAction):

    pass
class spinefm_SystemActionModel_ActionOnFM(SystemAction):

    def __init__(self, fma: str, spinefm_SystemActionModel_ActionOnFM: "FeatureModel" = None, spinefm_SystemActionModel_ActionOnFM113: "ConfigurationProcessStep" = None):
        self.fma = fma
        self.spinefm_SystemActionModel_ActionOnFM = spinefm_SystemActionModel_ActionOnFM
        self.spinefm_SystemActionModel_ActionOnFM113 = spinefm_SystemActionModel_ActionOnFM113
        
        pass
    @property
    def fma(self):
        return self.__fma

    @fma.setter
    def fma(self, fma: str):
        self.__fma = fma


    @property
    def spinefm_SystemActionModel_ActionOnFM113(self):
        return self.__spinefm_SystemActionModel_ActionOnFM113

    @spinefm_SystemActionModel_ActionOnFM113.setter
    def spinefm_SystemActionModel_ActionOnFM113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_SystemActionModel_ActionOnFM__spinefm_SystemActionModel_ActionOnFM113", None)
        self.__spinefm_SystemActionModel_ActionOnFM113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ConfigurationProcessStep114"):
                opp_val = getattr(old_value, "ConfigurationProcessStep114", None)
                if opp_val == self:
                    setattr(old_value, "ConfigurationProcessStep114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ConfigurationProcessStep114"):
                opp_val = getattr(value, "ConfigurationProcessStep114", None)
                setattr(value, "ConfigurationProcessStep114", self)

    @property
    def spinefm_SystemActionModel_ActionOnFM(self):
        return self.__spinefm_SystemActionModel_ActionOnFM

    @spinefm_SystemActionModel_ActionOnFM.setter
    def spinefm_SystemActionModel_ActionOnFM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_SystemActionModel_ActionOnFM__spinefm_SystemActionModel_ActionOnFM", None)
        self.__spinefm_SystemActionModel_ActionOnFM = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FeatureModel111"):
                opp_val = getattr(old_value, "FeatureModel111", None)
                if opp_val == self:
                    setattr(old_value, "FeatureModel111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FeatureModel111"):
                opp_val = getattr(value, "FeatureModel111", None)
                setattr(value, "FeatureModel111", self)

    def cloneAction(self) :
        # TODO: Implement cloneAction method
        pass

class spinefm_SystemActionModel_ActionCreateConfiguration(SystemAction):

    pass
class Step:

    pass
class GlobalContext:

    pass
class spinefm_ProcessModel_DeletedContextInformations:

    def __init__(self, deletedContext: str, spinefm_ProcessModel_DeletedContextInformations: "Context" = None):
        self.deletedContext = deletedContext
        self.spinefm_ProcessModel_DeletedContextInformations = spinefm_ProcessModel_DeletedContextInformations
        
        pass
    @property
    def deletedContext(self):
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
            if hasattr(old_value, "Context72"):
                opp_val = getattr(old_value, "Context72", None)
                if opp_val == self:
                    setattr(old_value, "Context72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Context72"):
                opp_val = getattr(value, "Context72", None)
                setattr(value, "Context72", self)

class Past:

    pass
class LocalContext:

    pass
class spinefm_ProcessModel_Context(ABC):

    def __init__(self, id: str, spinefm_ProcessModel_Context: set["ConfigurationProcessStep"] = None):
        self.id = id
        self.spinefm_ProcessModel_Context = spinefm_ProcessModel_Context if spinefm_ProcessModel_Context is not None else set()
        
        pass
    @property
    def id(self):
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
                if hasattr(item, "ConfigurationProcessStep59"):
                    opp_val = getattr(item, "ConfigurationProcessStep59", None)
                    
                    if opp_val == self:
                        setattr(item, "ConfigurationProcessStep59", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ConfigurationProcessStep59"):
                    opp_val = getattr(item, "ConfigurationProcessStep59", None)
                    
                    setattr(item, "ConfigurationProcessStep59", self)
                    

    def getCPSOfDE(self, spinefm_de) :
        # TODO: Implement getCPSOfDE method
        pass

    def mergeExternalCPS(self, spinefm_cm, spinefm_step, spinefm_externalCPS):
        # TODO: Implement mergeExternalCPS method
        pass

    def addCPS(self, spinefm_cps):
        # TODO: Implement addCPS method
        pass

class SystemActionModel_ActionOnFM:

    pass
class spinefm_ProcessModel_ContextManager:

    def __init__(self, fma: str, id: str, spinefm_ProcessModel_ContextManager68: set["LocalContext"] = None, spinefm_ProcessModel_ContextManager70: "Past" = None, spinefm_ProcessModel_ContextManager: "MultipleSoftwareProductLine" = None, spinefm_ProcessModel_ContextManager66: "GlobalContext" = None):
        self.fma = fma
        self.id = id
        self.spinefm_ProcessModel_ContextManager68 = spinefm_ProcessModel_ContextManager68 if spinefm_ProcessModel_ContextManager68 is not None else set()
        self.spinefm_ProcessModel_ContextManager70 = spinefm_ProcessModel_ContextManager70
        self.spinefm_ProcessModel_ContextManager = spinefm_ProcessModel_ContextManager
        self.spinefm_ProcessModel_ContextManager66 = spinefm_ProcessModel_ContextManager66
        
        pass
    @property
    def fma(self):
        return self.__fma

    @fma.setter
    def fma(self, fma: str):
        self.__fma = fma


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def spinefm_ProcessModel_ContextManager70(self):
        return self.__spinefm_ProcessModel_ContextManager70

    @spinefm_ProcessModel_ContextManager70.setter
    def spinefm_ProcessModel_ContextManager70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_ProcessModel_ContextManager__spinefm_ProcessModel_ContextManager70", None)
        self.__spinefm_ProcessModel_ContextManager70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Past"):
                opp_val = getattr(old_value, "Past", None)
                if opp_val == self:
                    setattr(old_value, "Past", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Past"):
                opp_val = getattr(value, "Past", None)
                setattr(value, "Past", self)

    @property
    def spinefm_ProcessModel_ContextManager68(self):
        return self.__spinefm_ProcessModel_ContextManager68

    @spinefm_ProcessModel_ContextManager68.setter
    def spinefm_ProcessModel_ContextManager68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_ProcessModel_ContextManager__spinefm_ProcessModel_ContextManager68", None)
        self.__spinefm_ProcessModel_ContextManager68 = value if value is not None else set()
        
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
    def spinefm_ProcessModel_ContextManager66(self):
        return self.__spinefm_ProcessModel_ContextManager66

    @spinefm_ProcessModel_ContextManager66.setter
    def spinefm_ProcessModel_ContextManager66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_ProcessModel_ContextManager__spinefm_ProcessModel_ContextManager66", None)
        self.__spinefm_ProcessModel_ContextManager66 = value
        
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
    def spinefm_ProcessModel_ContextManager(self):
        return self.__spinefm_ProcessModel_ContextManager

    @spinefm_ProcessModel_ContextManager.setter
    def spinefm_ProcessModel_ContextManager(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_ProcessModel_ContextManager__spinefm_ProcessModel_ContextManager", None)
        self.__spinefm_ProcessModel_ContextManager = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MultipleSoftwareProductLine64"):
                opp_val = getattr(old_value, "MultipleSoftwareProductLine64", None)
                if opp_val == self:
                    setattr(old_value, "MultipleSoftwareProductLine64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MultipleSoftwareProductLine64"):
                opp_val = getattr(value, "MultipleSoftwareProductLine64", None)
                setattr(value, "MultipleSoftwareProductLine64", self)

    def propagate(self, spinefm_CPS, spinefm_context, spinefm_step):
        # TODO: Implement propagate method
        pass

    def restoreContext(self, spinefm_context):
        # TODO: Implement restoreContext method
        pass

    def getCPSFromId(self, spinefm_id) :
        # TODO: Implement getCPSFromId method
        pass

    def getContextFromId(self, spinefm_id) :
        # TODO: Implement getContextFromId method
        pass

    def cloningExistingContext(self, spinefm_contextSource) :
        # TODO: Implement cloningExistingContext method
        pass

    def init(self, spinefm_step):
        # TODO: Implement init method
        pass

    def removeContext(self, spinefm_context):
        # TODO: Implement removeContext method
        pass

    def createNewContext(self, spinefm_step) :
        # TODO: Implement createNewContext method
        pass

class CompositeConfiguration:

    pass
class spinefm_ProcessModel_ConfigurationProcessStep:

    def __init__(self, id: str, description: str, userConfig: bool, history: str, status: str, spinefm_ProcessModel_ConfigurationProcessStep: "DomainElement" = None, spinefm_ProcessModel_ConfigurationProcessStep50: "Context" = None, CPSRef: "Configuration" = None, spinefm_ProcessModel_ConfigurationProcessStep54: "ConfigurationState" = None, spinefm_ProcessModel_ConfigurationProcessStep57: set["SystemActionModel_ActionOnFM"] = None):
        self.id = id
        self.description = description
        self.userConfig = userConfig
        self.history = history
        self.status = status
        self.spinefm_ProcessModel_ConfigurationProcessStep = spinefm_ProcessModel_ConfigurationProcessStep
        self.spinefm_ProcessModel_ConfigurationProcessStep50 = spinefm_ProcessModel_ConfigurationProcessStep50
        self.CPSRef = CPSRef
        self.spinefm_ProcessModel_ConfigurationProcessStep54 = spinefm_ProcessModel_ConfigurationProcessStep54
        self.spinefm_ProcessModel_ConfigurationProcessStep57 = spinefm_ProcessModel_ConfigurationProcessStep57 if spinefm_ProcessModel_ConfigurationProcessStep57 is not None else set()
        
        pass
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def history(self):
        return self.__history

    @history.setter
    def history(self, history: str):
        self.__history = history


    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status


    @property
    def userConfig(self):
        return self.__userConfig

    @userConfig.setter
    def userConfig(self, userConfig: bool):
        self.__userConfig = userConfig


    @property
    def spinefm_ProcessModel_ConfigurationProcessStep54(self):
        return self.__spinefm_ProcessModel_ConfigurationProcessStep54

    @spinefm_ProcessModel_ConfigurationProcessStep54.setter
    def spinefm_ProcessModel_ConfigurationProcessStep54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_ProcessModel_ConfigurationProcessStep__spinefm_ProcessModel_ConfigurationProcessStep54", None)
        self.__spinefm_ProcessModel_ConfigurationProcessStep54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ConfigurationState55"):
                opp_val = getattr(old_value, "ConfigurationState55", None)
                if opp_val == self:
                    setattr(old_value, "ConfigurationState55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ConfigurationState55"):
                opp_val = getattr(value, "ConfigurationState55", None)
                setattr(value, "ConfigurationState55", self)

    @property
    def spinefm_ProcessModel_ConfigurationProcessStep57(self):
        return self.__spinefm_ProcessModel_ConfigurationProcessStep57

    @spinefm_ProcessModel_ConfigurationProcessStep57.setter
    def spinefm_ProcessModel_ConfigurationProcessStep57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_ProcessModel_ConfigurationProcessStep__spinefm_ProcessModel_ConfigurationProcessStep57", None)
        self.__spinefm_ProcessModel_ConfigurationProcessStep57 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SystemActionModel_ActionOnFM"):
                    opp_val = getattr(item, "SystemActionModel_ActionOnFM", None)
                    
                    if opp_val == self:
                        setattr(item, "SystemActionModel_ActionOnFM", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SystemActionModel_ActionOnFM"):
                    opp_val = getattr(item, "SystemActionModel_ActionOnFM", None)
                    
                    setattr(item, "SystemActionModel_ActionOnFM", self)
                    

    @property
    def spinefm_ProcessModel_ConfigurationProcessStep(self):
        return self.__spinefm_ProcessModel_ConfigurationProcessStep

    @spinefm_ProcessModel_ConfigurationProcessStep.setter
    def spinefm_ProcessModel_ConfigurationProcessStep(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_ProcessModel_ConfigurationProcessStep__spinefm_ProcessModel_ConfigurationProcessStep", None)
        self.__spinefm_ProcessModel_ConfigurationProcessStep = value
        
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
    def CPSRef(self):
        return self.__CPSRef

    @CPSRef.setter
    def CPSRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_ProcessModel_ConfigurationProcessStep__CPSRef", None)
        self.__CPSRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Configuration52"):
                opp_val = getattr(old_value, "Configuration52", None)
                if opp_val == self:
                    setattr(old_value, "Configuration52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Configuration52"):
                opp_val = getattr(value, "Configuration52", None)
                setattr(value, "Configuration52", self)

    @property
    def spinefm_ProcessModel_ConfigurationProcessStep50(self):
        return self.__spinefm_ProcessModel_ConfigurationProcessStep50

    @spinefm_ProcessModel_ConfigurationProcessStep50.setter
    def spinefm_ProcessModel_ConfigurationProcessStep50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_ProcessModel_ConfigurationProcessStep__spinefm_ProcessModel_ConfigurationProcessStep50", None)
        self.__spinefm_ProcessModel_ConfigurationProcessStep50 = value
        
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

    def getConfName(self) :
        # TODO: Implement getConfName method
        pass

    def isComplete(self) :
        # TODO: Implement isComplete method
        pass

    def recordActionDone(self, spinefm_aof, spinefm_feature):
        # TODO: Implement recordActionDone method
        pass

    def setFMA(self, spinefm_step, spinefm_fma):
        # TODO: Implement setFMA method
        pass

    def isMergeableWithCPS(self, spinefm_cps) :
        # TODO: Implement isMergeableWithCPS method
        pass

    def captureImplicitActions(self, spinefm_aof, spinefm_step):
        # TODO: Implement captureImplicitActions method
        pass

    def setFeatureUnselected(self, spinefm_feature):
        # TODO: Implement setFeatureUnselected method
        pass

    def alreadyHaveAction(self, spinefm_a) :
        # TODO: Implement alreadyHaveAction method
        pass

    def mergeWithExternalCPS(self, spinefm_confCPS, spinefm_step, spinefm_cm):
        # TODO: Implement mergeWithExternalCPS method
        pass

class MultipleSoftwareProductLine:

    pass
class Context:

    pass
class spinefm_ProcessModel_GlobalContext(Context):

    pass
class spinefm_ProcessModel_LocalContext(Context):

    pass
class Configuration:

    pass
class spinefm_ConfigurationModel_Link:

    def __init__(self, id: str, spinefm_ConfigurationModel_Link38: "Configuration" = None, spinefm_ConfigurationModel_Link: "Configuration" = None, spinefm_ConfigurationModel_Link35: "DEAssociation" = None):
        self.id = id
        self.spinefm_ConfigurationModel_Link38 = spinefm_ConfigurationModel_Link38
        self.spinefm_ConfigurationModel_Link = spinefm_ConfigurationModel_Link
        self.spinefm_ConfigurationModel_Link35 = spinefm_ConfigurationModel_Link35
        
        pass
    @property
    def id(self):
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

    def getAssociatedConfiguration(self, spinefm_conf) :
        # TODO: Implement getAssociatedConfiguration method
        pass

class ConfigurationState:

    pass
class spinefm_ConfigurationModel_CompositeConfiguration:

    def __init__(self, name: str, description: str, spinefm_ConfigurationModel_CompositeConfiguration: set["Configuration"] = None, spinefm_ConfigurationModel_CompositeConfiguration43: set["Link"] = None, spinefm_ConfigurationModel_CompositeConfiguration46: "MultipleSoftwareProductLine" = None):
        self.name = name
        self.description = description
        self.spinefm_ConfigurationModel_CompositeConfiguration = spinefm_ConfigurationModel_CompositeConfiguration if spinefm_ConfigurationModel_CompositeConfiguration is not None else set()
        self.spinefm_ConfigurationModel_CompositeConfiguration43 = spinefm_ConfigurationModel_CompositeConfiguration43 if spinefm_ConfigurationModel_CompositeConfiguration43 is not None else set()
        self.spinefm_ConfigurationModel_CompositeConfiguration46 = spinefm_ConfigurationModel_CompositeConfiguration46
        
        pass
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def name(self):
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
                    

    @property
    def spinefm_ConfigurationModel_CompositeConfiguration46(self):
        return self.__spinefm_ConfigurationModel_CompositeConfiguration46

    @spinefm_ConfigurationModel_CompositeConfiguration46.setter
    def spinefm_ConfigurationModel_CompositeConfiguration46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_ConfigurationModel_CompositeConfiguration__spinefm_ConfigurationModel_CompositeConfiguration46", None)
        self.__spinefm_ConfigurationModel_CompositeConfiguration46 = value
        
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

    def addConfiguration(self, spinefm_conf):
        # TODO: Implement addConfiguration method
        pass

    def isValid(self) :
        # TODO: Implement isValid method
        pass

    def createConfigurationLink(self, spinefm_confTarget, spinefm_asso, spinefm_confSource):
        # TODO: Implement createConfigurationLink method
        pass

    def getConfigurationByName(self, spinefm_confName) :
        # TODO: Implement getConfigurationByName method
        pass

    def getCompatibleConfigurations(self, spinefm_asso, spinefm_confSource) :
        # TODO: Implement getCompatibleConfigurations method
        pass

class FeatureModel:

    pass
class spinefm_MSPLModel_DomainElement:

    def __init__(self, id: str, spinefm_MSPLModel_DomainElement21: set["DEAssociation"] = None, spinefm_MSPLModel_DomainElement: "MultiplicityElement" = None, spinefm_MSPLModel_DomainElement19: "FeatureModel" = None):
        self.id = id
        self.spinefm_MSPLModel_DomainElement21 = spinefm_MSPLModel_DomainElement21 if spinefm_MSPLModel_DomainElement21 is not None else set()
        self.spinefm_MSPLModel_DomainElement = spinefm_MSPLModel_DomainElement
        self.spinefm_MSPLModel_DomainElement19 = spinefm_MSPLModel_DomainElement19
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


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
            if hasattr(old_value, "MultiplicityElement17"):
                opp_val = getattr(old_value, "MultiplicityElement17", None)
                if opp_val == self:
                    setattr(old_value, "MultiplicityElement17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MultiplicityElement17"):
                opp_val = getattr(value, "MultiplicityElement17", None)
                setattr(value, "MultiplicityElement17", self)

    @property
    def spinefm_MSPLModel_DomainElement19(self):
        return self.__spinefm_MSPLModel_DomainElement19

    @spinefm_MSPLModel_DomainElement19.setter
    def spinefm_MSPLModel_DomainElement19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_MSPLModel_DomainElement__spinefm_MSPLModel_DomainElement19", None)
        self.__spinefm_MSPLModel_DomainElement19 = value
        
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

    @property
    def spinefm_MSPLModel_DomainElement21(self):
        return self.__spinefm_MSPLModel_DomainElement21

    @spinefm_MSPLModel_DomainElement21.setter
    def spinefm_MSPLModel_DomainElement21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_MSPLModel_DomainElement__spinefm_MSPLModel_DomainElement21", None)
        self.__spinefm_MSPLModel_DomainElement21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DEAssociation22"):
                    opp_val = getattr(item, "DEAssociation22", None)
                    
                    if opp_val == self:
                        setattr(item, "DEAssociation22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DEAssociation22"):
                    opp_val = getattr(item, "DEAssociation22", None)
                    
                    setattr(item, "DEAssociation22", self)
                    

class MultiplicityElement:

    pass
class spinefm_MSPLModel_DEAssociationEnd:

    def __init__(self, id: str, spinefm_MSPLModel_DEAssociationEnd: "MultiplicityElement" = None, spinefm_MSPLModel_DEAssociationEnd14: "DomainElement" = None):
        self.id = id
        self.spinefm_MSPLModel_DEAssociationEnd = spinefm_MSPLModel_DEAssociationEnd
        self.spinefm_MSPLModel_DEAssociationEnd14 = spinefm_MSPLModel_DEAssociationEnd14
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def spinefm_MSPLModel_DEAssociationEnd14(self):
        return self.__spinefm_MSPLModel_DEAssociationEnd14

    @spinefm_MSPLModel_DEAssociationEnd14.setter
    def spinefm_MSPLModel_DEAssociationEnd14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_MSPLModel_DEAssociationEnd__spinefm_MSPLModel_DEAssociationEnd14", None)
        self.__spinefm_MSPLModel_DEAssociationEnd14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DomainElement15"):
                opp_val = getattr(old_value, "DomainElement15", None)
                if opp_val == self:
                    setattr(old_value, "DomainElement15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DomainElement15"):
                opp_val = getattr(value, "DomainElement15", None)
                setattr(value, "DomainElement15", self)

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

class Link:

    pass
class ConfigurationProcessStep:

    pass
class spinefm_ConfigurationModel_Configuration:

    def __init__(self, id: str, description: str, configuration: "ConfigurationProcessStep" = None, spinefm_ConfigurationModel_Configuration: set["Link"] = None, spinefm_ConfigurationModel_Configuration26: "ConfigurationState" = None, spinefm_ConfigurationModel_Configuration28: "DomainElement" = None, spinefm_ConfigurationModel_Configuration31: set["ConfigurationProcessStep"] = None):
        self.id = id
        self.description = description
        self.configuration = configuration
        self.spinefm_ConfigurationModel_Configuration = spinefm_ConfigurationModel_Configuration if spinefm_ConfigurationModel_Configuration is not None else set()
        self.spinefm_ConfigurationModel_Configuration26 = spinefm_ConfigurationModel_Configuration26
        self.spinefm_ConfigurationModel_Configuration28 = spinefm_ConfigurationModel_Configuration28
        self.spinefm_ConfigurationModel_Configuration31 = spinefm_ConfigurationModel_Configuration31 if spinefm_ConfigurationModel_Configuration31 is not None else set()
        
        pass
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def spinefm_ConfigurationModel_Configuration26(self):
        return self.__spinefm_ConfigurationModel_Configuration26

    @spinefm_ConfigurationModel_Configuration26.setter
    def spinefm_ConfigurationModel_Configuration26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_ConfigurationModel_Configuration__spinefm_ConfigurationModel_Configuration26", None)
        self.__spinefm_ConfigurationModel_Configuration26 = value
        
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
    def configuration(self):
        return self.__configuration

    @configuration.setter
    def configuration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_ConfigurationModel_Configuration__configuration", None)
        self.__configuration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ConfigurationProcessStep"):
                opp_val = getattr(old_value, "ConfigurationProcessStep", None)
                if opp_val == self:
                    setattr(old_value, "ConfigurationProcessStep", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ConfigurationProcessStep"):
                opp_val = getattr(value, "ConfigurationProcessStep", None)
                setattr(value, "ConfigurationProcessStep", self)

    @property
    def spinefm_ConfigurationModel_Configuration28(self):
        return self.__spinefm_ConfigurationModel_Configuration28

    @spinefm_ConfigurationModel_Configuration28.setter
    def spinefm_ConfigurationModel_Configuration28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_ConfigurationModel_Configuration__spinefm_ConfigurationModel_Configuration28", None)
        self.__spinefm_ConfigurationModel_Configuration28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DomainElement29"):
                opp_val = getattr(old_value, "DomainElement29", None)
                if opp_val == self:
                    setattr(old_value, "DomainElement29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DomainElement29"):
                opp_val = getattr(value, "DomainElement29", None)
                setattr(value, "DomainElement29", self)

    @property
    def spinefm_ConfigurationModel_Configuration31(self):
        return self.__spinefm_ConfigurationModel_Configuration31

    @spinefm_ConfigurationModel_Configuration31.setter
    def spinefm_ConfigurationModel_Configuration31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_ConfigurationModel_Configuration__spinefm_ConfigurationModel_Configuration31", None)
        self.__spinefm_ConfigurationModel_Configuration31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ConfigurationProcessStep32"):
                    opp_val = getattr(item, "ConfigurationProcessStep32", None)
                    
                    if opp_val == self:
                        setattr(item, "ConfigurationProcessStep32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ConfigurationProcessStep32"):
                    opp_val = getattr(item, "ConfigurationProcessStep32", None)
                    
                    setattr(item, "ConfigurationProcessStep32", self)
                    

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
                    

    def getLinkedConfigurationsOfDomainElement(self, spinefm_de) :
        # TODO: Implement getLinkedConfigurationsOfDomainElement method
        pass

    def isCompletlyLinked(self) :
        # TODO: Implement isCompletlyLinked method
        pass

    def canBeLinked(self, spinefm_association) :
        # TODO: Implement canBeLinked method
        pass

    def getAllCPS(self) :
        # TODO: Implement getAllCPS method
        pass

    def getFeatureModel(self) :
        # TODO: Implement getFeatureModel method
        pass

class spinefm_MSPLModel_DEAssociation:

    def __init__(self, id: str, spinefm_MSPLModel_DEAssociation11: set["DEAssociationEnd"] = None, spinefm_MSPLModel_DEAssociation: set["RestrictionFunction"] = None):
        self.id = id
        self.spinefm_MSPLModel_DEAssociation11 = spinefm_MSPLModel_DEAssociation11 if spinefm_MSPLModel_DEAssociation11 is not None else set()
        self.spinefm_MSPLModel_DEAssociation = spinefm_MSPLModel_DEAssociation if spinefm_MSPLModel_DEAssociation is not None else set()
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def spinefm_MSPLModel_DEAssociation11(self):
        return self.__spinefm_MSPLModel_DEAssociation11

    @spinefm_MSPLModel_DEAssociation11.setter
    def spinefm_MSPLModel_DEAssociation11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_MSPLModel_DEAssociation__spinefm_MSPLModel_DEAssociation11", None)
        self.__spinefm_MSPLModel_DEAssociation11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DEAssociationEnd"):
                    opp_val = getattr(item, "DEAssociationEnd", None)
                    
                    if opp_val == self:
                        setattr(item, "DEAssociationEnd", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DEAssociationEnd"):
                    opp_val = getattr(item, "DEAssociationEnd", None)
                    
                    setattr(item, "DEAssociationEnd", self)
                    

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
                    

    def getExtremityOfDE(self, spinefm_de) :
        # TODO: Implement getExtremityOfDE method
        pass

    def getOppositeExtremity(self, spinefm_source) :
        # TODO: Implement getOppositeExtremity method
        pass

    def createAndAssociateInverseAssociation(self):
        # TODO: Implement createAndAssociateInverseAssociation method
        pass

    def isLinkBetweenDEs(self, spinefm_firstExtremity, spinefm_secondExtremity) :
        # TODO: Implement isLinkBetweenDEs method
        pass

    def computeActionsToDo(self, spinefm_CPSSource, spinefm_CPSTarget) :
        # TODO: Implement computeActionsToDo method
        pass

class DEAssociation:

    pass
class DomainElement:

    pass
class spinefm_MSPLModel_MultiplicityElement:

    def __init__(self, lowerBound: int, upperBound: int, id: str):
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.id = id
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def lowerBound(self):
        return self.__lowerBound

    @lowerBound.setter
    def lowerBound(self, lowerBound: int):
        self.__lowerBound = lowerBound


    @property
    def upperBound(self):
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: int):
        self.__upperBound = upperBound


    def isLowerThanUpperBound(self, spinefm_value) :
        # TODO: Implement isLowerThanUpperBound method
        pass

    def isExactlyOne(self) :
        # TODO: Implement isExactlyOne method
        pass

    def respectBoundaries(self, spinefm_value) :
        # TODO: Implement respectBoundaries method
        pass

class DEAssociationEnd:

    pass
class RestrictionFunction:

    pass
class spinefm_FMModel_Feature:

    def __init__(self, id: str, name: str, spinefm_FMModel_Feature: set["Group"] = None):
        self.id = id
        self.name = name
        self.spinefm_FMModel_Feature = spinefm_FMModel_Feature if spinefm_FMModel_Feature is not None else set()
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def name(self):
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
                    

    def getAllChildrenFeatures(self) :
        # TODO: Implement getAllChildrenFeatures method
        pass

class Constraint:

    pass
class Feature:

    pass
class spinefm_MSPLModel_MultipleSoftwareProductLine:

    def __init__(self, id: str, spinefm_MSPLModel_MultipleSoftwareProductLine: set["DomainElement"] = None, spinefm_MSPLModel_MultipleSoftwareProductLine8: set["DEAssociation"] = None):
        self.id = id
        self.spinefm_MSPLModel_MultipleSoftwareProductLine = spinefm_MSPLModel_MultipleSoftwareProductLine if spinefm_MSPLModel_MultipleSoftwareProductLine is not None else set()
        self.spinefm_MSPLModel_MultipleSoftwareProductLine8 = spinefm_MSPLModel_MultipleSoftwareProductLine8 if spinefm_MSPLModel_MultipleSoftwareProductLine8 is not None else set()
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


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
                    

    def getDomainElementByName(self, spinefm_name) :
        # TODO: Implement getDomainElementByName method
        pass

    def getAssociationByName(self, spinefm_assoName) :
        # TODO: Implement getAssociationByName method
        pass

    def getValidAssociationsForDEs(self, spinefm_source, spinefm_target) :
        # TODO: Implement getValidAssociationsForDEs method
        pass

class spinefm_FMModel_Constraint:

    def __init__(self, Rule: str):
        self.Rule = Rule
        
        pass
    @property
    def Rule(self):
        return self.__Rule

    @Rule.setter
    def Rule(self, Rule: str):
        self.__Rule = Rule


class spinefm_FMModel_Group:

    def __init__(self, state: str, spinefm_FMModel_Group: set["Feature"] = None):
        self.state = state
        self.spinefm_FMModel_Group = spinefm_FMModel_Group if spinefm_FMModel_Group is not None else set()
        
        pass
    @property
    def state(self):
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
                    

    def getAllChildren(self) :
        # TODO: Implement getAllChildren method
        pass

class Group:

    pass
class spinefm_FMModel_FeatureModel:

    def __init__(self, name: str, id: str, spinefm_FMModel_FeatureModel: "Feature" = None, spinefm_FMModel_FeatureModel2: set["Constraint"] = None):
        self.name = name
        self.id = id
        self.spinefm_FMModel_FeatureModel = spinefm_FMModel_FeatureModel
        self.spinefm_FMModel_FeatureModel2 = spinefm_FMModel_FeatureModel2 if spinefm_FMModel_FeatureModel2 is not None else set()
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


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
                    

    def getFeatureFromName(self, spinefm_name) :
        # TODO: Implement getFeatureFromName method
        pass

    def addFeature(self, spinefm_name, spinefm_feature, spinefm_state):
        # TODO: Implement addFeature method
        pass

    def getStateFT(self, spinefm_feature) :
        # TODO: Implement getStateFT method
        pass
