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
class ActionMode(Enum):
    AUTOMATIC = "AUTOMATIC"
    MANUAL = "MANUAL"
    FM = "FM"
class GroupState(Enum):
    MANDATORY = "MANDATORY"
    OPTIONAL = "OPTIONAL"
    ALTERNATIVE = "ALTERNATIVE"
    OR = "OR"
    MUTEX = "MUTEX"


############################################
# Definition of Classes
############################################

class spinefm_RFModel_Rule:

    def __init__(self, id: str, spinefm_RFModel_Rule: "SystemActionModel_ActionOnFM" = None, spinefm_RFModel_Rule165: "ConfigurationState" = None):
        self.id = id
        self.spinefm_RFModel_Rule = spinefm_RFModel_Rule
        self.spinefm_RFModel_Rule165 = spinefm_RFModel_Rule165
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

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
            if hasattr(old_value, "SystemActionModel_ActionOnFM163"):
                opp_val = getattr(old_value, "SystemActionModel_ActionOnFM163", None)
                if opp_val == self:
                    setattr(old_value, "SystemActionModel_ActionOnFM163", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SystemActionModel_ActionOnFM163"):
                opp_val = getattr(value, "SystemActionModel_ActionOnFM163", None)
                setattr(value, "SystemActionModel_ActionOnFM163", self)

    @property
    def spinefm_RFModel_Rule165(self):
        return self.__spinefm_RFModel_Rule165

    @spinefm_RFModel_Rule165.setter
    def spinefm_RFModel_Rule165(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_RFModel_Rule__spinefm_RFModel_Rule165", None)
        self.__spinefm_RFModel_Rule165 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ConfigurationState166"):
                opp_val = getattr(old_value, "ConfigurationState166", None)
                if opp_val == self:
                    setattr(old_value, "ConfigurationState166", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ConfigurationState166"):
                opp_val = getattr(value, "ConfigurationState166", None)
                setattr(value, "ConfigurationState166", self)

    def createInverseRule(self) -> str:
        # TODO: Implement createInverseRule method
        pass

class spinefm_RFModel_ConfigurationState:

    def __init__(self, id: str, spinefm_RFModel_ConfigurationState: set["Feature"] = None, spinefm_RFModel_ConfigurationState157: set["Feature"] = None, spinefm_RFModel_ConfigurationState160: "FeatureModel" = None):
        self.id = id
        self.spinefm_RFModel_ConfigurationState = spinefm_RFModel_ConfigurationState if spinefm_RFModel_ConfigurationState is not None else set()
        self.spinefm_RFModel_ConfigurationState157 = spinefm_RFModel_ConfigurationState157 if spinefm_RFModel_ConfigurationState157 is not None else set()
        self.spinefm_RFModel_ConfigurationState160 = spinefm_RFModel_ConfigurationState160
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

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
                if hasattr(item, "Feature155"):
                    opp_val = getattr(item, "Feature155", None)
                    
                    if opp_val == self:
                        setattr(item, "Feature155", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Feature155"):
                    opp_val = getattr(item, "Feature155", None)
                    
                    setattr(item, "Feature155", self)
                    

    @property
    def spinefm_RFModel_ConfigurationState160(self):
        return self.__spinefm_RFModel_ConfigurationState160

    @spinefm_RFModel_ConfigurationState160.setter
    def spinefm_RFModel_ConfigurationState160(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_RFModel_ConfigurationState__spinefm_RFModel_ConfigurationState160", None)
        self.__spinefm_RFModel_ConfigurationState160 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FeatureModel161"):
                opp_val = getattr(old_value, "FeatureModel161", None)
                if opp_val == self:
                    setattr(old_value, "FeatureModel161", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FeatureModel161"):
                opp_val = getattr(value, "FeatureModel161", None)
                setattr(value, "FeatureModel161", self)

    @property
    def spinefm_RFModel_ConfigurationState157(self):
        return self.__spinefm_RFModel_ConfigurationState157

    @spinefm_RFModel_ConfigurationState157.setter
    def spinefm_RFModel_ConfigurationState157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_RFModel_ConfigurationState__spinefm_RFModel_ConfigurationState157", None)
        self.__spinefm_RFModel_ConfigurationState157 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Feature158"):
                    opp_val = getattr(item, "Feature158", None)
                    
                    if opp_val == self:
                        setattr(item, "Feature158", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Feature158"):
                    opp_val = getattr(item, "Feature158", None)
                    
                    setattr(item, "Feature158", self)
                    

    def isIncludedIn(self, otherState: str) -> bool:
        # TODO: Implement isIncludedIn method
        pass

class spinefm_HistoryModel_Past:

    def __init__(self, modelPath: str, description: str, id: str, rootPath: str, spinefm_HistoryModel_Past: set["Step"] = None, spinefm_HistoryModel_Past142: set["LocalContext"] = None):
        self.modelPath = modelPath
        self.description = description
        self.id = id
        self.rootPath = rootPath
        self.spinefm_HistoryModel_Past = spinefm_HistoryModel_Past if spinefm_HistoryModel_Past is not None else set()
        self.spinefm_HistoryModel_Past142 = spinefm_HistoryModel_Past142 if spinefm_HistoryModel_Past142 is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def rootPath(self) -> str:
        return self.__rootPath

    @rootPath.setter
    def rootPath(self, rootPath: str):
        self.__rootPath = rootPath

    @property
    def modelPath(self) -> str:
        return self.__modelPath

    @modelPath.setter
    def modelPath(self, modelPath: str):
        self.__modelPath = modelPath

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

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
                if hasattr(item, "Step140"):
                    opp_val = getattr(item, "Step140", None)
                    
                    if opp_val == self:
                        setattr(item, "Step140", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Step140"):
                    opp_val = getattr(item, "Step140", None)
                    
                    setattr(item, "Step140", self)
                    

    @property
    def spinefm_HistoryModel_Past142(self):
        return self.__spinefm_HistoryModel_Past142

    @spinefm_HistoryModel_Past142.setter
    def spinefm_HistoryModel_Past142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_HistoryModel_Past__spinefm_HistoryModel_Past142", None)
        self.__spinefm_HistoryModel_Past142 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "LocalContext143"):
                    opp_val = getattr(item, "LocalContext143", None)
                    
                    if opp_val == self:
                        setattr(item, "LocalContext143", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "LocalContext143"):
                    opp_val = getattr(item, "LocalContext143", None)
                    
                    setattr(item, "LocalContext143", self)
                    

    def createStep(self, action: str) -> str:
        # TODO: Implement createStep method
        pass

    def undoAction(self, step: str):
        # TODO: Implement undoAction method
        pass

    def getStepFromId(self, stepId: str) -> str:
        # TODO: Implement getStepFromId method
        pass

    def clonePastWithoutSystemActions(self) -> str:
        # TODO: Implement clonePastWithoutSystemActions method
        pass

    def undoLastAction(self):
        # TODO: Implement undoLastAction method
        pass

class SystemActionModel_SystemAction:

    pass
class UserActionModel_UserAction:

    pass
class Rule:

    pass
class spinefm_RFModel_RestrictionFunction:

    def __init__(self, id: str, spinefm_RFModel_RestrictionFunction: set["Rule"] = None, spinefm_RFModel_RestrictionFunction146: "RestrictionFunction" = None, spinefm_RFModel_RestrictionFunction149: "DomainElement" = None, spinefm_RFModel_RestrictionFunction152: "DomainElement" = None):
        self.id = id
        self.spinefm_RFModel_RestrictionFunction = spinefm_RFModel_RestrictionFunction if spinefm_RFModel_RestrictionFunction is not None else set()
        self.spinefm_RFModel_RestrictionFunction146 = spinefm_RFModel_RestrictionFunction146
        self.spinefm_RFModel_RestrictionFunction149 = spinefm_RFModel_RestrictionFunction149
        self.spinefm_RFModel_RestrictionFunction152 = spinefm_RFModel_RestrictionFunction152
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def spinefm_RFModel_RestrictionFunction152(self):
        return self.__spinefm_RFModel_RestrictionFunction152

    @spinefm_RFModel_RestrictionFunction152.setter
    def spinefm_RFModel_RestrictionFunction152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_RFModel_RestrictionFunction__spinefm_RFModel_RestrictionFunction152", None)
        self.__spinefm_RFModel_RestrictionFunction152 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DomainElement153"):
                opp_val = getattr(old_value, "DomainElement153", None)
                if opp_val == self:
                    setattr(old_value, "DomainElement153", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DomainElement153"):
                opp_val = getattr(value, "DomainElement153", None)
                setattr(value, "DomainElement153", self)

    @property
    def spinefm_RFModel_RestrictionFunction149(self):
        return self.__spinefm_RFModel_RestrictionFunction149

    @spinefm_RFModel_RestrictionFunction149.setter
    def spinefm_RFModel_RestrictionFunction149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_RFModel_RestrictionFunction__spinefm_RFModel_RestrictionFunction149", None)
        self.__spinefm_RFModel_RestrictionFunction149 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DomainElement150"):
                opp_val = getattr(old_value, "DomainElement150", None)
                if opp_val == self:
                    setattr(old_value, "DomainElement150", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DomainElement150"):
                opp_val = getattr(value, "DomainElement150", None)
                setattr(value, "DomainElement150", self)

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
    def spinefm_RFModel_RestrictionFunction146(self):
        return self.__spinefm_RFModel_RestrictionFunction146

    @spinefm_RFModel_RestrictionFunction146.setter
    def spinefm_RFModel_RestrictionFunction146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_RFModel_RestrictionFunction__spinefm_RFModel_RestrictionFunction146", None)
        self.__spinefm_RFModel_RestrictionFunction146 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RestrictionFunction147"):
                opp_val = getattr(old_value, "RestrictionFunction147", None)
                if opp_val == self:
                    setattr(old_value, "RestrictionFunction147", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RestrictionFunction147"):
                opp_val = getattr(value, "RestrictionFunction147", None)
                setattr(value, "RestrictionFunction147", self)

    def createAndAssociateInverseRestFunc(self) -> str:
        # TODO: Implement createAndAssociateInverseRestFunc method
        pass

class UserActionModel_spinefm_EObject:

    pass
class spinefm_HistoryModel_Step:

    def __init__(self, id: str, UserActionModel: "UserActionModel_UserAction" = None, SystemActionModel: set["SystemActionModel_SystemAction"] = None):
        self.id = id
        self.UserActionModel = UserActionModel
        self.SystemActionModel = SystemActionModel if SystemActionModel is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def SystemActionModel(self):
        return self.__SystemActionModel

    @SystemActionModel.setter
    def SystemActionModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_HistoryModel_Step__SystemActionModel", None)
        self.__SystemActionModel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActionModel138"):
                    opp_val = getattr(item, "ActionModel138", None)
                    
                    if opp_val == self:
                        setattr(item, "ActionModel138", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActionModel138"):
                    opp_val = getattr(item, "ActionModel138", None)
                    
                    setattr(item, "ActionModel138", self)
                    

    @property
    def UserActionModel(self):
        return self.__UserActionModel

    @UserActionModel.setter
    def UserActionModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_HistoryModel_Step__UserActionModel", None)
        self.__UserActionModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ActionModel"):
                opp_val = getattr(old_value, "ActionModel", None)
                if opp_val == self:
                    setattr(old_value, "ActionModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ActionModel"):
                opp_val = getattr(value, "ActionModel", None)
                setattr(value, "ActionModel", self)

    def undoActions(self):
        # TODO: Implement undoActions method
        pass

    def cloneStepWithoutSystemActions(self) -> str:
        # TODO: Implement cloneStepWithoutSystemActions method
        pass

    def getDescription(self) -> str:
        # TODO: Implement getDescription method
        pass

class ActionAbstractRename:

    pass
class spinefm_SystemActionModel_ActionRenameCPS(ActionAbstractRename):

    pass
class ActionOnFM:

    pass
class spinefm_SystemActionModel_ActionDeselect(ActionOnFM):

    pass
class spinefm_SystemActionModel_ActionAddCTConstraint(ActionOnFM):

    pass
class spinefm_SystemActionModel_ActionSelect(ActionOnFM):

    pass
class spinefm_UserActionModel_UserAction(ABC):

    def __init__(self, type: str, Step130: "Step" = None, spinefm_UserActionModel_UserAction: "ContextManager" = None, spinefm_UserActionModel_UserAction135: "UserActionModel_spinefm_EObject" = None):
        self.type = type
        self.Step130 = Step130
        self.spinefm_UserActionModel_UserAction = spinefm_UserActionModel_UserAction
        self.spinefm_UserActionModel_UserAction135 = spinefm_UserActionModel_UserAction135
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

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
            if hasattr(old_value, "ContextManager133"):
                opp_val = getattr(old_value, "ContextManager133", None)
                if opp_val == self:
                    setattr(old_value, "ContextManager133", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ContextManager133"):
                opp_val = getattr(value, "ContextManager133", None)
                setattr(value, "ContextManager133", self)

    @property
    def Step130(self):
        return self.__Step130

    @Step130.setter
    def Step130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_UserActionModel_UserAction__Step130", None)
        self.__Step130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HistoryModel131"):
                opp_val = getattr(old_value, "HistoryModel131", None)
                if opp_val == self:
                    setattr(old_value, "HistoryModel131", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HistoryModel131"):
                opp_val = getattr(value, "HistoryModel131", None)
                setattr(value, "HistoryModel131", self)

    @property
    def spinefm_UserActionModel_UserAction135(self):
        return self.__spinefm_UserActionModel_UserAction135

    @spinefm_UserActionModel_UserAction135.setter
    def spinefm_UserActionModel_UserAction135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_UserActionModel_UserAction__spinefm_UserActionModel_UserAction135", None)
        self.__spinefm_UserActionModel_UserAction135 = value
        
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

    def transformContextNameToSave(self, contextID: str) -> str:
        # TODO: Implement transformContextNameToSave method
        pass

    def getDescription(self) -> str:
        # TODO: Implement getDescription method
        pass

    def postcondition(self):
        # TODO: Implement postcondition method
        pass

    def initManualAction(self, contextManager: str):
        # TODO: Implement initManualAction method
        pass

    def cloneActionWithStringAttributes(self) -> str:
        # TODO: Implement cloneActionWithStringAttributes method
        pass

    def apply(self):
        # TODO: Implement apply method
        pass

    def precondition(self) -> str:
        # TODO: Implement precondition method
        pass

class UserAction:

    pass
class spinefm_UserActionModel_UserCreateContext(UserAction):

    pass
class spinefm_UserActionModel_UserLinkConfiguration(UserAction):

    def __init__(self, confSourceName: str, confTargetName: str, assoName: str):
        self.confSourceName = confSourceName
        self.confTargetName = confTargetName
        self.assoName = assoName
        
    @property
    def assoName(self) -> str:
        return self.__assoName

    @assoName.setter
    def assoName(self, assoName: str):
        self.__assoName = assoName

    @property
    def confSourceName(self) -> str:
        return self.__confSourceName

    @confSourceName.setter
    def confSourceName(self, confSourceName: str):
        self.__confSourceName = confSourceName

    @property
    def confTargetName(self) -> str:
        return self.__confTargetName

    @confTargetName.setter
    def confTargetName(self, confTargetName: str):
        self.__confTargetName = confTargetName

class spinefm_UserActionModel_UserCloneContext(UserAction):

    def __init__(self, contextID: str):
        self.contextID = contextID
        
    @property
    def contextID(self) -> str:
        return self.__contextID

    @contextID.setter
    def contextID(self, contextID: str):
        self.__contextID = contextID

class spinefm_UserActionModel_UserValidConfiguration(UserAction):

    def __init__(self, domainElementName: str, contextID: str):
        self.domainElementName = domainElementName
        self.contextID = contextID
        
    @property
    def domainElementName(self) -> str:
        return self.__domainElementName

    @domainElementName.setter
    def domainElementName(self, domainElementName: str):
        self.__domainElementName = domainElementName

    @property
    def contextID(self) -> str:
        return self.__contextID

    @contextID.setter
    def contextID(self, contextID: str):
        self.__contextID = contextID

class spinefm_UserActionModel_UserDeselect(UserAction):

    def __init__(self, domainElementName: str, contextID: str, featureName: str):
        self.domainElementName = domainElementName
        self.contextID = contextID
        self.featureName = featureName
        
    @property
    def featureName(self) -> str:
        return self.__featureName

    @featureName.setter
    def featureName(self, featureName: str):
        self.__featureName = featureName

    @property
    def contextID(self) -> str:
        return self.__contextID

    @contextID.setter
    def contextID(self, contextID: str):
        self.__contextID = contextID

    @property
    def domainElementName(self) -> str:
        return self.__domainElementName

    @domainElementName.setter
    def domainElementName(self, domainElementName: str):
        self.__domainElementName = domainElementName

class spinefm_UserActionModel_UserSavePast(UserAction):

    def __init__(self, destPath: str):
        self.destPath = destPath
        
    @property
    def destPath(self) -> str:
        return self.__destPath

    @destPath.setter
    def destPath(self, destPath: str):
        self.__destPath = destPath

class spinefm_UserActionModel_UserGenerate(UserAction):

    def __init__(self, path: str):
        self.path = path
        
    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path

class spinefm_UserActionModel_UserRenameElement(UserAction):

    def __init__(self, name: str, elementType: str, elementID: str):
        self.name = name
        self.elementType = elementType
        self.elementID = elementID
        
    @property
    def elementType(self) -> str:
        return self.__elementType

    @elementType.setter
    def elementType(self, elementType: str):
        self.__elementType = elementType

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def elementID(self) -> str:
        return self.__elementID

    @elementID.setter
    def elementID(self, elementID: str):
        self.__elementID = elementID

class spinefm_UserActionModel_UserPropagate(UserAction):

    def __init__(self, domainElementName: str, contextID: str):
        self.domainElementName = domainElementName
        self.contextID = contextID
        
    @property
    def domainElementName(self) -> str:
        return self.__domainElementName

    @domainElementName.setter
    def domainElementName(self, domainElementName: str):
        self.__domainElementName = domainElementName

    @property
    def contextID(self) -> str:
        return self.__contextID

    @contextID.setter
    def contextID(self, contextID: str):
        self.__contextID = contextID

class spinefm_UserActionModel_UserInit(UserAction):

    def __init__(self, filePath: str, pastPath: str, confDescription: str):
        self.filePath = filePath
        self.pastPath = pastPath
        self.confDescription = confDescription
        
    @property
    def confDescription(self) -> str:
        return self.__confDescription

    @confDescription.setter
    def confDescription(self, confDescription: str):
        self.__confDescription = confDescription

    @property
    def pastPath(self) -> str:
        return self.__pastPath

    @pastPath.setter
    def pastPath(self, pastPath: str):
        self.__pastPath = pastPath

    @property
    def filePath(self) -> str:
        return self.__filePath

    @filePath.setter
    def filePath(self, filePath: str):
        self.__filePath = filePath

class spinefm_UserActionModel_UserSelect(UserAction):

    def __init__(self, domainElementName: str, contextID: str, featureName: str):
        self.domainElementName = domainElementName
        self.contextID = contextID
        self.featureName = featureName
        
    @property
    def contextID(self) -> str:
        return self.__contextID

    @contextID.setter
    def contextID(self, contextID: str):
        self.__contextID = contextID

    @property
    def featureName(self) -> str:
        return self.__featureName

    @featureName.setter
    def featureName(self, featureName: str):
        self.__featureName = featureName

    @property
    def domainElementName(self) -> str:
        return self.__domainElementName

    @domainElementName.setter
    def domainElementName(self, domainElementName: str):
        self.__domainElementName = domainElementName

class spinefm_SystemActionModel_ActionSetProductDescription(ActionAbstractRename):

    pass
class spinefm_SystemActionModel_ActionRenameProduct(ActionAbstractRename):

    pass
class spinefm_SystemActionModel_ActionRenameConfig(ActionAbstractRename):

    pass
class ContextManager:

    pass
class SystemAction:

    pass
class spinefm_SystemActionModel_ActionLink(SystemAction):

    pass
class spinefm_SystemActionModel_ActionAbstractRename(SystemAction):

    def __init__(self, oldName: str, newName: str):
        self.oldName = oldName
        self.newName = newName
        
    @property
    def oldName(self) -> str:
        return self.__oldName

    @oldName.setter
    def oldName(self, oldName: str):
        self.__oldName = oldName

    @property
    def newName(self) -> str:
        return self.__newName

    @newName.setter
    def newName(self, newName: str):
        self.__newName = newName

class spinefm_SystemActionModel_ActionCreateContext(SystemAction):

    pass
class spinefm_SystemActionModel_ActionCreateConfiguration(SystemAction):

    pass
class spinefm_SystemActionModel_ActionOnFM(SystemAction):

    def __init__(self, fma: str, spinefm_SystemActionModel_ActionOnFM: "FeatureModel" = None, spinefm_SystemActionModel_ActionOnFM113: "ConfigurationProcessStep" = None):
        self.fma = fma
        self.spinefm_SystemActionModel_ActionOnFM = spinefm_SystemActionModel_ActionOnFM
        self.spinefm_SystemActionModel_ActionOnFM113 = spinefm_SystemActionModel_ActionOnFM113
        
    @property
    def fma(self) -> str:
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

    def cloneAction(self) -> str:
        # TODO: Implement cloneAction method
        pass

class spinefm_SystemActionModel_ActionDeleteContext(SystemAction):

    pass
class spinefm_SystemActionModel_ActionMoveConfiguration(SystemAction):

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
class GlobalContext:

    pass
class Step:

    pass
class spinefm_SystemActionModel_SystemAction(ABC):

    def __init__(self, cpsHistory: str, type: str, Step: "Step" = None):
        self.cpsHistory = cpsHistory
        self.type = type
        self.Step = Step
        
    @property
    def cpsHistory(self) -> str:
        return self.__cpsHistory

    @cpsHistory.setter
    def cpsHistory(self, cpsHistory: str):
        self.__cpsHistory = cpsHistory

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def Step(self):
        return self.__Step

    @Step.setter
    def Step(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_SystemActionModel_SystemAction__Step", None)
        self.__Step = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HistoryModel"):
                opp_val = getattr(old_value, "HistoryModel", None)
                if opp_val == self:
                    setattr(old_value, "HistoryModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HistoryModel"):
                opp_val = getattr(value, "HistoryModel", None)
                setattr(value, "HistoryModel", self)

    def isSameObject(self, o: str) -> bool:
        # TODO: Implement isSameObject method
        pass

    def apply(self):
        # TODO: Implement apply method
        pass

    def undo(self):
        # TODO: Implement undo method
        pass

class CompositeConfiguration:

    pass
class spinefm_ProcessModel_ContextManager:

    def __init__(self, fma: str, id: str, spinefm_ProcessModel_ContextManager: "MultipleSoftwareProductLine" = None, spinefm_ProcessModel_ContextManager66: "GlobalContext" = None, spinefm_ProcessModel_ContextManager68: set["LocalContext"] = None, spinefm_ProcessModel_ContextManager70: "Past" = None):
        self.fma = fma
        self.id = id
        self.spinefm_ProcessModel_ContextManager = spinefm_ProcessModel_ContextManager
        self.spinefm_ProcessModel_ContextManager66 = spinefm_ProcessModel_ContextManager66
        self.spinefm_ProcessModel_ContextManager68 = spinefm_ProcessModel_ContextManager68 if spinefm_ProcessModel_ContextManager68 is not None else set()
        self.spinefm_ProcessModel_ContextManager70 = spinefm_ProcessModel_ContextManager70
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def fma(self) -> str:
        return self.__fma

    @fma.setter
    def fma(self, fma: str):
        self.__fma = fma

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

    def cloningExistingContext(self, contextSource: str) -> str:
        # TODO: Implement cloningExistingContext method
        pass

    def createNewContext(self, step: str) -> str:
        # TODO: Implement createNewContext method
        pass

    def restoreContext(self, context: str):
        # TODO: Implement restoreContext method
        pass

    def getContextFromId(self, id: str) -> str:
        # TODO: Implement getContextFromId method
        pass

    def propagate(self, CPS: str, step: str, context: str):
        # TODO: Implement propagate method
        pass

    def getCPSFromId(self, id: str) -> str:
        # TODO: Implement getCPSFromId method
        pass

    def init(self, step: str):
        # TODO: Implement init method
        pass

    def removeContext(self, context: str):
        # TODO: Implement removeContext method
        pass

class Context:

    pass
class spinefm_ProcessModel_GlobalContext(Context):

    pass
class spinefm_ProcessModel_LocalContext(Context):

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
                    

    def getCPSOfDE(self, de: str) -> str:
        # TODO: Implement getCPSOfDE method
        pass

    def addCPS(self, cps: str):
        # TODO: Implement addCPS method
        pass

    def mergeExternalCPS(self, cm: str, step: str, externalCPS: str):
        # TODO: Implement mergeExternalCPS method
        pass

class SystemActionModel_ActionOnFM:

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
class spinefm_ProcessModel_ConfigurationProcessStep:

    def __init__(self, userConfig: bool, history: str, status: str, id: str, description: str, Configuration52: "Configuration" = None, spinefm_ProcessModel_ConfigurationProcessStep54: "ConfigurationState" = None, spinefm_ProcessModel_ConfigurationProcessStep57: set["SystemActionModel_ActionOnFM"] = None, spinefm_ProcessModel_ConfigurationProcessStep: "DomainElement" = None, spinefm_ProcessModel_ConfigurationProcessStep50: "Context" = None):
        self.userConfig = userConfig
        self.history = history
        self.status = status
        self.id = id
        self.description = description
        self.Configuration52 = Configuration52
        self.spinefm_ProcessModel_ConfigurationProcessStep54 = spinefm_ProcessModel_ConfigurationProcessStep54
        self.spinefm_ProcessModel_ConfigurationProcessStep57 = spinefm_ProcessModel_ConfigurationProcessStep57 if spinefm_ProcessModel_ConfigurationProcessStep57 is not None else set()
        self.spinefm_ProcessModel_ConfigurationProcessStep = spinefm_ProcessModel_ConfigurationProcessStep
        self.spinefm_ProcessModel_ConfigurationProcessStep50 = spinefm_ProcessModel_ConfigurationProcessStep50
        
    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def userConfig(self) -> bool:
        return self.__userConfig

    @userConfig.setter
    def userConfig(self, userConfig: bool):
        self.__userConfig = userConfig

    @property
    def history(self) -> str:
        return self.__history

    @history.setter
    def history(self, history: str):
        self.__history = history

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
    def Configuration52(self):
        return self.__Configuration52

    @Configuration52.setter
    def Configuration52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spinefm_ProcessModel_ConfigurationProcessStep__Configuration52", None)
        self.__Configuration52 = value
        
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

    def setFMA(self, step: str, fma: str):
        # TODO: Implement setFMA method
        pass

    def getConfName(self) -> str:
        # TODO: Implement getConfName method
        pass

    def captureImplicitActions(self, step: str, aof: str):
        # TODO: Implement captureImplicitActions method
        pass

    def isComplete(self) -> bool:
        # TODO: Implement isComplete method
        pass

    def recordActionDone(self, feature: str, aof: str):
        # TODO: Implement recordActionDone method
        pass

    def setFeatureUnselected(self, feature: str):
        # TODO: Implement setFeatureUnselected method
        pass

    def isMergeableWithCPS(self, cps: str) -> bool:
        # TODO: Implement isMergeableWithCPS method
        pass

    def mergeWithExternalCPS(self, confCPS: str, step: str, cm: str):
        # TODO: Implement mergeWithExternalCPS method
        pass

    def alreadyHaveAction(self, a: str) -> bool:
        # TODO: Implement alreadyHaveAction method
        pass

class MultipleSoftwareProductLine:

    pass
class spinefm_ConfigurationModel_CompositeConfiguration:

    def __init__(self, name: str, description: str, spinefm_ConfigurationModel_CompositeConfiguration: set["Configuration"] = None, spinefm_ConfigurationModel_CompositeConfiguration43: set["Link"] = None, spinefm_ConfigurationModel_CompositeConfiguration46: "MultipleSoftwareProductLine" = None):
        self.name = name
        self.description = description
        self.spinefm_ConfigurationModel_CompositeConfiguration = spinefm_ConfigurationModel_CompositeConfiguration if spinefm_ConfigurationModel_CompositeConfiguration is not None else set()
        self.spinefm_ConfigurationModel_CompositeConfiguration43 = spinefm_ConfigurationModel_CompositeConfiguration43 if spinefm_ConfigurationModel_CompositeConfiguration43 is not None else set()
        self.spinefm_ConfigurationModel_CompositeConfiguration46 = spinefm_ConfigurationModel_CompositeConfiguration46
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

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

    def getCompatibleConfigurations(self, confSource: str, asso: str) -> str:
        # TODO: Implement getCompatibleConfigurations method
        pass

    def isValid(self) -> bool:
        # TODO: Implement isValid method
        pass

    def createConfigurationLink(self, confTarget: str, confSource: str, asso: str):
        # TODO: Implement createConfigurationLink method
        pass

    def getConfigurationByName(self, confName: str) -> str:
        # TODO: Implement getConfigurationByName method
        pass

    def addConfiguration(self, conf: str):
        # TODO: Implement addConfiguration method
        pass

class MultiplicityElement:

    pass
class spinefm_MSPLModel_DEAssociationEnd:

    def __init__(self, id: str, spinefm_MSPLModel_DEAssociationEnd: "MultiplicityElement" = None, spinefm_MSPLModel_DEAssociationEnd14: "DomainElement" = None):
        self.id = id
        self.spinefm_MSPLModel_DEAssociationEnd = spinefm_MSPLModel_DEAssociationEnd
        self.spinefm_MSPLModel_DEAssociationEnd14 = spinefm_MSPLModel_DEAssociationEnd14
        
    @property
    def id(self) -> str:
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

class spinefm_MSPLModel_MultiplicityElement:

    def __init__(self, lowerBound: int, upperBound: int, id: str):
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

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
class spinefm_ConfigurationModel_Configuration:

    def __init__(self, id: str, description: str, ConfigurationProcessStep: "ConfigurationProcessStep" = None, spinefm_ConfigurationModel_Configuration: set["Link"] = None, spinefm_ConfigurationModel_Configuration26: "ConfigurationState" = None, spinefm_ConfigurationModel_Configuration28: "DomainElement" = None, spinefm_ConfigurationModel_Configuration31: set["ConfigurationProcessStep"] = None):
        self.id = id
        self.description = description
        self.ConfigurationProcessStep = ConfigurationProcessStep
        self.spinefm_ConfigurationModel_Configuration = spinefm_ConfigurationModel_Configuration if spinefm_ConfigurationModel_Configuration is not None else set()
        self.spinefm_ConfigurationModel_Configuration26 = spinefm_ConfigurationModel_Configuration26
        self.spinefm_ConfigurationModel_Configuration28 = spinefm_ConfigurationModel_Configuration28
        self.spinefm_ConfigurationModel_Configuration31 = spinefm_ConfigurationModel_Configuration31 if spinefm_ConfigurationModel_Configuration31 is not None else set()
        
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

    def canBeLinked(self, association: str) -> bool:
        # TODO: Implement canBeLinked method
        pass

    def isCompletlyLinked(self) -> bool:
        # TODO: Implement isCompletlyLinked method
        pass

    def getAllCPS(self) -> str:
        # TODO: Implement getAllCPS method
        pass

    def getLinkedConfigurationsOfDomainElement(self, de: str) -> str:
        # TODO: Implement getLinkedConfigurationsOfDomainElement method
        pass

    def getFeatureModel(self) -> str:
        # TODO: Implement getFeatureModel method
        pass

class FeatureModel:

    pass
class spinefm_MSPLModel_DomainElement:

    def __init__(self, id: str, spinefm_MSPLModel_DomainElement: "MultiplicityElement" = None, spinefm_MSPLModel_DomainElement19: "FeatureModel" = None, spinefm_MSPLModel_DomainElement21: set["DEAssociation"] = None):
        self.id = id
        self.spinefm_MSPLModel_DomainElement = spinefm_MSPLModel_DomainElement
        self.spinefm_MSPLModel_DomainElement19 = spinefm_MSPLModel_DomainElement19
        self.spinefm_MSPLModel_DomainElement21 = spinefm_MSPLModel_DomainElement21 if spinefm_MSPLModel_DomainElement21 is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

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
class spinefm_MSPLModel_DEAssociation:

    def __init__(self, id: str, spinefm_MSPLModel_DEAssociation: set["RestrictionFunction"] = None, spinefm_MSPLModel_DEAssociation11: set["DEAssociationEnd"] = None):
        self.id = id
        self.spinefm_MSPLModel_DEAssociation = spinefm_MSPLModel_DEAssociation if spinefm_MSPLModel_DEAssociation is not None else set()
        self.spinefm_MSPLModel_DEAssociation11 = spinefm_MSPLModel_DEAssociation11 if spinefm_MSPLModel_DEAssociation11 is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

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
                    

    def getExtremityOfDE(self, de: str) -> str:
        # TODO: Implement getExtremityOfDE method
        pass

    def createAndAssociateInverseAssociation(self):
        # TODO: Implement createAndAssociateInverseAssociation method
        pass

    def isLinkBetweenDEs(self, secondExtremity: str, firstExtremity: str) -> bool:
        # TODO: Implement isLinkBetweenDEs method
        pass

    def computeActionsToDo(self, CPSSource: str, CPSTarget: str) -> str:
        # TODO: Implement computeActionsToDo method
        pass

    def getOppositeExtremity(self, source: str) -> str:
        # TODO: Implement getOppositeExtremity method
        pass

class DEAssociation:

    pass
class DomainElement:

    pass
class spinefm_MSPLModel_MultipleSoftwareProductLine:

    def __init__(self, id: str, spinefm_MSPLModel_MultipleSoftwareProductLine: set["DomainElement"] = None, spinefm_MSPLModel_MultipleSoftwareProductLine8: set["DEAssociation"] = None):
        self.id = id
        self.spinefm_MSPLModel_MultipleSoftwareProductLine = spinefm_MSPLModel_MultipleSoftwareProductLine if spinefm_MSPLModel_MultipleSoftwareProductLine is not None else set()
        self.spinefm_MSPLModel_MultipleSoftwareProductLine8 = spinefm_MSPLModel_MultipleSoftwareProductLine8 if spinefm_MSPLModel_MultipleSoftwareProductLine8 is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

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
                    

    def getValidAssociationsForDEs(self, target: str, source: str) -> str:
        # TODO: Implement getValidAssociationsForDEs method
        pass

    def getDomainElementByName(self, name: str) -> str:
        # TODO: Implement getDomainElementByName method
        pass

    def getAssociationByName(self, assoName: str) -> str:
        # TODO: Implement getAssociationByName method
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

    def getStateFT(self, feature: str) -> str:
        # TODO: Implement getStateFT method
        pass

    def addFeature(self, feature: str, state: str, name: str):
        # TODO: Implement addFeature method
        pass
