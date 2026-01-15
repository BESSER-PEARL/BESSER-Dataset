from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class XMessageKind(Enum):
    in = "in"
    out = "out"
    inout = "inout"


############################################
# Definition of Classes
############################################

class executablemodelingprofile_Class:

    pass
class executablemodelingprofile_ConnectorEnd:

    pass
class executablemodelingprofile_XConnectorEnd(ABC):

    def __init__(self, executablemodelingprofile_XConnectorEnd: "executablemodelingprofile_ConnectorEnd" = None):
        self.executablemodelingprofile_XConnectorEnd = executablemodelingprofile_XConnectorEnd
        
    @property
    def executablemodelingprofile_XConnectorEnd(self):
        return self.__executablemodelingprofile_XConnectorEnd

    @executablemodelingprofile_XConnectorEnd.setter
    def executablemodelingprofile_XConnectorEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_executablemodelingprofile_XConnectorEnd__executablemodelingprofile_XConnectorEnd", None)
        self.__executablemodelingprofile_XConnectorEnd = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "executablemodelingprofile_ConnectorEnd"):
                opp_val = getattr(old_value, "executablemodelingprofile_ConnectorEnd", None)
                if opp_val == self:
                    setattr(old_value, "executablemodelingprofile_ConnectorEnd", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "executablemodelingprofile_ConnectorEnd"):
                opp_val = getattr(value, "executablemodelingprofile_ConnectorEnd", None)
                setattr(value, "executablemodelingprofile_ConnectorEnd", self)

    def xConnectorEndUniqueness(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement xConnectorEndUniqueness method
        pass

    def xConnectorEndConnector(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement xConnectorEndConnector method
        pass

    def xConnectorEndRole(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement xConnectorEndRole method
        pass

class executablemodelingprofile_XGeneralization(ABC):

    def __init__(self, executablemodelingprofile_XGeneralization: "executablemodelingprofile_Generalization" = None):
        self.executablemodelingprofile_XGeneralization = executablemodelingprofile_XGeneralization
        
    @property
    def executablemodelingprofile_XGeneralization(self):
        return self.__executablemodelingprofile_XGeneralization

    @executablemodelingprofile_XGeneralization.setter
    def executablemodelingprofile_XGeneralization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_executablemodelingprofile_XGeneralization__executablemodelingprofile_XGeneralization", None)
        self.__executablemodelingprofile_XGeneralization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "executablemodelingprofile_Generalization"):
                opp_val = getattr(old_value, "executablemodelingprofile_Generalization", None)
                if opp_val == self:
                    setattr(old_value, "executablemodelingprofile_Generalization", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "executablemodelingprofile_Generalization"):
                opp_val = getattr(value, "executablemodelingprofile_Generalization", None)
                setattr(value, "executablemodelingprofile_Generalization", self)

    def xGeneralizationGeneralizationSet(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement xGeneralizationGeneralizationSet method
        pass

    def xGeneralizationClassifiers(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement xGeneralizationClassifiers method
        pass

class executablemodelingprofile_LiteralSpecification:

    pass
class executablemodelingprofile_PrimitiveType:

    pass
class executablemodelingprofile_GeneralizationSet:

    pass
class executablemodelingprofile_XGeneralizationSet(ABC):

    pass
class executablemodelingprofile_Generalization:

    pass
class executablemodelingprofile_Constraint:

    pass
class executablemodelingprofile_OpaqueBehavior:

    pass
class XActionBehavior:

    pass
class executablemodelingprofile_XOpaqueBehavior(XActionBehavior):

    def __init__(self, isExternal: str, executablemodelingprofile_XOpaqueBehavior: "executablemodelingprofile_OpaqueBehavior" = None):
        self.isExternal = isExternal
        self.executablemodelingprofile_XOpaqueBehavior = executablemodelingprofile_XOpaqueBehavior
        
    @property
    def isExternal(self) -> str:
        return self.__isExternal

    @isExternal.setter
    def isExternal(self, isExternal: str):
        self.__isExternal = isExternal

    @property
    def executablemodelingprofile_XOpaqueBehavior(self):
        return self.__executablemodelingprofile_XOpaqueBehavior

    @executablemodelingprofile_XOpaqueBehavior.setter
    def executablemodelingprofile_XOpaqueBehavior(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_executablemodelingprofile_XOpaqueBehavior__executablemodelingprofile_XOpaqueBehavior", None)
        self.__executablemodelingprofile_XOpaqueBehavior = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "executablemodelingprofile_OpaqueBehavior"):
                opp_val = getattr(old_value, "executablemodelingprofile_OpaqueBehavior", None)
                if opp_val == self:
                    setattr(old_value, "executablemodelingprofile_OpaqueBehavior", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "executablemodelingprofile_OpaqueBehavior"):
                opp_val = getattr(value, "executablemodelingprofile_OpaqueBehavior", None)
                setattr(value, "executablemodelingprofile_OpaqueBehavior", self)

    def xOpaqueBehaviorExternal(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement xOpaqueBehaviorExternal method
        pass

class executablemodelingprofile_XActivity(XActionBehavior):

    def __init__(self, executablemodelingprofile_XActivity: "executablemodelingprofile_Activity" = None):
        self.executablemodelingprofile_XActivity = executablemodelingprofile_XActivity
        
    @property
    def executablemodelingprofile_XActivity(self):
        return self.__executablemodelingprofile_XActivity

    @executablemodelingprofile_XActivity.setter
    def executablemodelingprofile_XActivity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_executablemodelingprofile_XActivity__executablemodelingprofile_XActivity", None)
        self.__executablemodelingprofile_XActivity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "executablemodelingprofile_Activity"):
                opp_val = getattr(old_value, "executablemodelingprofile_Activity", None)
                if opp_val == self:
                    setattr(old_value, "executablemodelingprofile_Activity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "executablemodelingprofile_Activity"):
                opp_val = getattr(value, "executablemodelingprofile_Activity", None)
                setattr(value, "executablemodelingprofile_Activity", self)

    def xActivityParameters(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement xActivityParameters method
        pass

    def xActivityTextualRepresentation(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement xActivityTextualRepresentation method
        pass

class executablemodelingprofile_Transition:

    pass
class executablemodelingprofile_Activity:

    pass
class executablemodelingprofile_XTransition(ABC):

    def __init__(self, executablemodelingprofile_XTransition: "executablemodelingprofile_Transition" = None):
        self.executablemodelingprofile_XTransition = executablemodelingprofile_XTransition
        
    @property
    def executablemodelingprofile_XTransition(self):
        return self.__executablemodelingprofile_XTransition

    @executablemodelingprofile_XTransition.setter
    def executablemodelingprofile_XTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_executablemodelingprofile_XTransition__executablemodelingprofile_XTransition", None)
        self.__executablemodelingprofile_XTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "executablemodelingprofile_Transition"):
                opp_val = getattr(old_value, "executablemodelingprofile_Transition", None)
                if opp_val == self:
                    setattr(old_value, "executablemodelingprofile_Transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "executablemodelingprofile_Transition"):
                opp_val = getattr(value, "executablemodelingprofile_Transition", None)
                setattr(value, "executablemodelingprofile_Transition", self)

    def xTransitionTrigger(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement xTransitionTrigger method
        pass

    def xTransitionEffect(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement xTransitionEffect method
        pass

    def xTransitionGuard(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement xTransitionGuard method
        pass

class executablemodelingprofile_Pseudostate:

    pass
class executablemodelingprofile_Vertex:

    pass
class executablemodelingprofile_XVertex(ABC):

    pass
class executablemodelingprofile_State:

    pass
class executablemodelingprofile_XRegion(ABC):

    def __init__(self, executablemodelingprofile_XRegion: "executablemodelingprofile_Region" = None):
        self.executablemodelingprofile_XRegion = executablemodelingprofile_XRegion
        
    @property
    def executablemodelingprofile_XRegion(self):
        return self.__executablemodelingprofile_XRegion

    @executablemodelingprofile_XRegion.setter
    def executablemodelingprofile_XRegion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_executablemodelingprofile_XRegion__executablemodelingprofile_XRegion", None)
        self.__executablemodelingprofile_XRegion = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "executablemodelingprofile_Region"):
                opp_val = getattr(old_value, "executablemodelingprofile_Region", None)
                if opp_val == self:
                    setattr(old_value, "executablemodelingprofile_Region", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "executablemodelingprofile_Region"):
                opp_val = getattr(value, "executablemodelingprofile_Region", None)
                setattr(value, "executablemodelingprofile_Region", self)

    def xRegionTransitions(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement xRegionTransitions method
        pass

    def xRegionSubvertexes(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement xRegionSubvertexes method
        pass

class XVertex:

    pass
class executablemodelingprofile_XPseudostate(XVertex):

    def __init__(self, executablemodelingprofile_XPseudostate: "executablemodelingprofile_Pseudostate" = None):
        self.executablemodelingprofile_XPseudostate = executablemodelingprofile_XPseudostate
        
    @property
    def executablemodelingprofile_XPseudostate(self):
        return self.__executablemodelingprofile_XPseudostate

    @executablemodelingprofile_XPseudostate.setter
    def executablemodelingprofile_XPseudostate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_executablemodelingprofile_XPseudostate__executablemodelingprofile_XPseudostate", None)
        self.__executablemodelingprofile_XPseudostate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "executablemodelingprofile_Pseudostate"):
                opp_val = getattr(old_value, "executablemodelingprofile_Pseudostate", None)
                if opp_val == self:
                    setattr(old_value, "executablemodelingprofile_Pseudostate", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "executablemodelingprofile_Pseudostate"):
                opp_val = getattr(value, "executablemodelingprofile_Pseudostate", None)
                setattr(value, "executablemodelingprofile_Pseudostate", self)

    def xPsuedostateKind(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement xPsuedostateKind method
        pass

class executablemodelingprofile_XState(XVertex):

    def __init__(self, executablemodelingprofile_XState: "executablemodelingprofile_State" = None):
        self.executablemodelingprofile_XState = executablemodelingprofile_XState
        
    @property
    def executablemodelingprofile_XState(self):
        return self.__executablemodelingprofile_XState

    @executablemodelingprofile_XState.setter
    def executablemodelingprofile_XState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_executablemodelingprofile_XState__executablemodelingprofile_XState", None)
        self.__executablemodelingprofile_XState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "executablemodelingprofile_State"):
                opp_val = getattr(old_value, "executablemodelingprofile_State", None)
                if opp_val == self:
                    setattr(old_value, "executablemodelingprofile_State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "executablemodelingprofile_State"):
                opp_val = getattr(value, "executablemodelingprofile_State", None)
                setattr(value, "executablemodelingprofile_State", self)

    def xStateNoSubmachine(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement xStateNoSubmachine method
        pass

    def xStateNoDoActivity(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement xStateNoDoActivity method
        pass

    def xStateRegions(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement xStateRegions method
        pass

    def xStateBehaviors(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement xStateBehaviors method
        pass

    def xStateOneRegion(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement xStateOneRegion method
        pass

class executablemodelingprofile_Region:

    pass
class executablemodelingprofile_StateMachine:

    pass
class XBehavior:

    pass
class executablemodelingprofile_XActionBehavior(XBehavior):

    pass
class executablemodelingprofile_XStateMachine(XBehavior):

    def __init__(self, executablemodelingprofile_XStateMachine: "executablemodelingprofile_StateMachine" = None):
        self.executablemodelingprofile_XStateMachine = executablemodelingprofile_XStateMachine
        
    @property
    def executablemodelingprofile_XStateMachine(self):
        return self.__executablemodelingprofile_XStateMachine

    @executablemodelingprofile_XStateMachine.setter
    def executablemodelingprofile_XStateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_executablemodelingprofile_XStateMachine__executablemodelingprofile_XStateMachine", None)
        self.__executablemodelingprofile_XStateMachine = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "executablemodelingprofile_StateMachine"):
                opp_val = getattr(old_value, "executablemodelingprofile_StateMachine", None)
                if opp_val == self:
                    setattr(old_value, "executablemodelingprofile_StateMachine", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "executablemodelingprofile_StateMachine"):
                opp_val = getattr(value, "executablemodelingprofile_StateMachine", None)
                setattr(value, "executablemodelingprofile_StateMachine", self)

    def xStateMachineContext(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement xStateMachineContext method
        pass

    def xStateMachineOneRegion(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement xStateMachineOneRegion method
        pass

    def xStateMachineNoParameters(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement xStateMachineNoParameters method
        pass

    def xStateMachineRegions(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement xStateMachineRegions method
        pass

    def xStateMachineInitialState(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement xStateMachineInitialState method
        pass

class executablemodelingprofile_Trigger:

    pass
class XDataType:

    pass
class executablemodelingprofile_XEnumeration(XDataType):

    def __init__(self, executablemodelingprofile_XEnumeration: "executablemodelingprofile_Enumeration" = None):
        self.executablemodelingprofile_XEnumeration = executablemodelingprofile_XEnumeration
        
    @property
    def executablemodelingprofile_XEnumeration(self):
        return self.__executablemodelingprofile_XEnumeration

    @executablemodelingprofile_XEnumeration.setter
    def executablemodelingprofile_XEnumeration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_executablemodelingprofile_XEnumeration__executablemodelingprofile_XEnumeration", None)
        self.__executablemodelingprofile_XEnumeration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "executablemodelingprofile_Enumeration"):
                opp_val = getattr(old_value, "executablemodelingprofile_Enumeration", None)
                if opp_val == self:
                    setattr(old_value, "executablemodelingprofile_Enumeration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "executablemodelingprofile_Enumeration"):
                opp_val = getattr(value, "executablemodelingprofile_Enumeration", None)
                setattr(value, "executablemodelingprofile_Enumeration", self)

    def xEnumerationAttributes(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement xEnumerationAttributes method
        pass

class executablemodelingprofile_Interface:

    pass
class executablemodelingprofile_XTrigger(ABC):

    def __init__(self, executablemodelingprofile_XTrigger: "executablemodelingprofile_Trigger" = None):
        self.executablemodelingprofile_XTrigger = executablemodelingprofile_XTrigger
        
    @property
    def executablemodelingprofile_XTrigger(self):
        return self.__executablemodelingprofile_XTrigger

    @executablemodelingprofile_XTrigger.setter
    def executablemodelingprofile_XTrigger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_executablemodelingprofile_XTrigger__executablemodelingprofile_XTrigger", None)
        self.__executablemodelingprofile_XTrigger = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "executablemodelingprofile_Trigger"):
                opp_val = getattr(old_value, "executablemodelingprofile_Trigger", None)
                if opp_val == self:
                    setattr(old_value, "executablemodelingprofile_Trigger", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "executablemodelingprofile_Trigger"):
                opp_val = getattr(value, "executablemodelingprofile_Trigger", None)
                setattr(value, "executablemodelingprofile_Trigger", self)

    def xTriggerCalledOperation(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement xTriggerCalledOperation method
        pass

    def xTriggerSignalReception(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement xTriggerSignalReception method
        pass

    def xTriggerEvents(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement xTriggerEvents method
        pass

class executablemodelingprofile_AssociationClass:

    pass
class XAssociation:

    pass
class executablemodelingprofile_Enumeration:

    pass
class executablemodelingprofile_XProtocolContainer(ABC):

    def __init__(self, executablemodelingprofile_XProtocolContainer: "executablemodelingprofile_Package" = None):
        self.executablemodelingprofile_XProtocolContainer = executablemodelingprofile_XProtocolContainer
        
    @property
    def executablemodelingprofile_XProtocolContainer(self):
        return self.__executablemodelingprofile_XProtocolContainer

    @executablemodelingprofile_XProtocolContainer.setter
    def executablemodelingprofile_XProtocolContainer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_executablemodelingprofile_XProtocolContainer__executablemodelingprofile_XProtocolContainer", None)
        self.__executablemodelingprofile_XProtocolContainer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "executablemodelingprofile_Package"):
                opp_val = getattr(old_value, "executablemodelingprofile_Package", None)
                if opp_val == self:
                    setattr(old_value, "executablemodelingprofile_Package", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "executablemodelingprofile_Package"):
                opp_val = getattr(value, "executablemodelingprofile_Package", None)
                setattr(value, "executablemodelingprofile_Package", self)

    def xProtocolContainerProtocol(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement xProtocolContainerProtocol method
        pass

class executablemodelingprofile_Connector:

    pass
class executablemodelingprofile_Package:

    pass
class executablemodelingprofile_Port:

    pass
class executablemodelingprofile_MultiplicityElement:

    pass
class executablemodelingprofile_Reception:

    pass
class executablemodelingprofile_DataType:

    pass
class executablemodelingprofile_Signal:

    pass
class executablemodelingprofile_XMultiplicityElement(ABC):

    def __init__(self, isOrderedByValue: str, isDescending: str, executablemodelingprofile_XMultiplicityElement: "executablemodelingprofile_MultiplicityElement" = None, executablemodelingprofile_XMultiplicityElement16: set["executablemodelingprofile_Property"] = None):
        self.isOrderedByValue = isOrderedByValue
        self.isDescending = isDescending
        self.executablemodelingprofile_XMultiplicityElement = executablemodelingprofile_XMultiplicityElement
        self.executablemodelingprofile_XMultiplicityElement16 = executablemodelingprofile_XMultiplicityElement16 if executablemodelingprofile_XMultiplicityElement16 is not None else set()
        
    @property
    def isDescending(self) -> str:
        return self.__isDescending

    @isDescending.setter
    def isDescending(self, isDescending: str):
        self.__isDescending = isDescending

    @property
    def isOrderedByValue(self) -> str:
        return self.__isOrderedByValue

    @isOrderedByValue.setter
    def isOrderedByValue(self, isOrderedByValue: str):
        self.__isOrderedByValue = isOrderedByValue

    @property
    def executablemodelingprofile_XMultiplicityElement16(self):
        return self.__executablemodelingprofile_XMultiplicityElement16

    @executablemodelingprofile_XMultiplicityElement16.setter
    def executablemodelingprofile_XMultiplicityElement16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_executablemodelingprofile_XMultiplicityElement__executablemodelingprofile_XMultiplicityElement16", None)
        self.__executablemodelingprofile_XMultiplicityElement16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "executablemodelingprofile_Property17"):
                    opp_val = getattr(item, "executablemodelingprofile_Property17", None)
                    
                    if opp_val == self:
                        setattr(item, "executablemodelingprofile_Property17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "executablemodelingprofile_Property17"):
                    opp_val = getattr(item, "executablemodelingprofile_Property17", None)
                    
                    setattr(item, "executablemodelingprofile_Property17", self)
                    

    @property
    def executablemodelingprofile_XMultiplicityElement(self):
        return self.__executablemodelingprofile_XMultiplicityElement

    @executablemodelingprofile_XMultiplicityElement.setter
    def executablemodelingprofile_XMultiplicityElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_executablemodelingprofile_XMultiplicityElement__executablemodelingprofile_XMultiplicityElement", None)
        self.__executablemodelingprofile_XMultiplicityElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "executablemodelingprofile_MultiplicityElement"):
                opp_val = getattr(old_value, "executablemodelingprofile_MultiplicityElement", None)
                if opp_val == self:
                    setattr(old_value, "executablemodelingprofile_MultiplicityElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "executablemodelingprofile_MultiplicityElement"):
                opp_val = getattr(value, "executablemodelingprofile_MultiplicityElement", None)
                setattr(value, "executablemodelingprofile_MultiplicityElement", self)

    def xMultiplicityElementIsOrderedByValue(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement xMultiplicityElementIsOrderedByValue method
        pass

    def xMultiplicityElementKeys(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement xMultiplicityElementKeys method
        pass

class executablemodelingprofile_Property:

    pass
class XMultiplicityElement:

    pass
class executablemodelingprofile_TypedElement:

    pass
class executablemodelingprofile_XTypedElement(ABC):

    def __init__(self, executablemodelingprofile_XTypedElement: "executablemodelingprofile_TypedElement" = None):
        self.executablemodelingprofile_XTypedElement = executablemodelingprofile_XTypedElement
        
    @property
    def executablemodelingprofile_XTypedElement(self):
        return self.__executablemodelingprofile_XTypedElement

    @executablemodelingprofile_XTypedElement.setter
    def executablemodelingprofile_XTypedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_executablemodelingprofile_XTypedElement__executablemodelingprofile_XTypedElement", None)
        self.__executablemodelingprofile_XTypedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "executablemodelingprofile_TypedElement"):
                opp_val = getattr(old_value, "executablemodelingprofile_TypedElement", None)
                if opp_val == self:
                    setattr(old_value, "executablemodelingprofile_TypedElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "executablemodelingprofile_TypedElement"):
                opp_val = getattr(value, "executablemodelingprofile_TypedElement", None)
                setattr(value, "executablemodelingprofile_TypedElement", self)

    def xTypedElementType(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement xTypedElementType method
        pass

class executablemodelingprofile_Parameter:

    pass
class XTypedElement:

    pass
class executablemodelingprofile_XParameter(XTypedElement):

    pass
class executablemodelingprofile_EncapsulatedClassifier:

    pass
class executablemodelingprofile_BehavioredClassifier:

    pass
class executablemodelingprofile_Classifier:

    pass
class XClassifier:

    pass
class executablemodelingprofile_XDataType(XClassifier):

    def __init__(self, executablemodelingprofile_XDataType: "executablemodelingprofile_DataType" = None):
        self.executablemodelingprofile_XDataType = executablemodelingprofile_XDataType
        
    @property
    def executablemodelingprofile_XDataType(self):
        return self.__executablemodelingprofile_XDataType

    @executablemodelingprofile_XDataType.setter
    def executablemodelingprofile_XDataType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_executablemodelingprofile_XDataType__executablemodelingprofile_XDataType", None)
        self.__executablemodelingprofile_XDataType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "executablemodelingprofile_DataType"):
                opp_val = getattr(old_value, "executablemodelingprofile_DataType", None)
                if opp_val == self:
                    setattr(old_value, "executablemodelingprofile_DataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "executablemodelingprofile_DataType"):
                opp_val = getattr(value, "executablemodelingprofile_DataType", None)
                setattr(value, "executablemodelingprofile_DataType", self)

    def xDataTypeOperations(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement xDataTypeOperations method
        pass

class executablemodelingprofile_XProtocol(XClassifier):

    def __init__(self, executablemodelingprofile_XProtocol: "executablemodelingprofile_BehavioredClassifier" = None):
        self.executablemodelingprofile_XProtocol = executablemodelingprofile_XProtocol
        
    @property
    def executablemodelingprofile_XProtocol(self):
        return self.__executablemodelingprofile_XProtocol

    @executablemodelingprofile_XProtocol.setter
    def executablemodelingprofile_XProtocol(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_executablemodelingprofile_XProtocol__executablemodelingprofile_XProtocol", None)
        self.__executablemodelingprofile_XProtocol = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "executablemodelingprofile_BehavioredClassifier"):
                opp_val = getattr(old_value, "executablemodelingprofile_BehavioredClassifier", None)
                if opp_val == self:
                    setattr(old_value, "executablemodelingprofile_BehavioredClassifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "executablemodelingprofile_BehavioredClassifier"):
                opp_val = getattr(value, "executablemodelingprofile_BehavioredClassifier", None)
                setattr(value, "executablemodelingprofile_BehavioredClassifier", self)

    def xProtocolOutgoingInterface(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement xProtocolOutgoingInterface method
        pass

    def xProtocolSymmetricInterface(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement xProtocolSymmetricInterface method
        pass

    def xProtocolIncomingInterface(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement xProtocolIncomingInterface method
        pass

    def xProtocolProtocolContainer(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement xProtocolProtocolContainer method
        pass

class executablemodelingprofile_XClass(XClassifier):

    def __init__(self, isExternal: str, executablemodelingprofile_XClass: "executablemodelingprofile_Class" = None):
        self.isExternal = isExternal
        self.executablemodelingprofile_XClass = executablemodelingprofile_XClass
        
    @property
    def isExternal(self) -> str:
        return self.__isExternal

    @isExternal.setter
    def isExternal(self, isExternal: str):
        self.__isExternal = isExternal

    @property
    def executablemodelingprofile_XClass(self):
        return self.__executablemodelingprofile_XClass

    @executablemodelingprofile_XClass.setter
    def executablemodelingprofile_XClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_executablemodelingprofile_XClass__executablemodelingprofile_XClass", None)
        self.__executablemodelingprofile_XClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "executablemodelingprofile_Class"):
                opp_val = getattr(old_value, "executablemodelingprofile_Class", None)
                if opp_val == self:
                    setattr(old_value, "executablemodelingprofile_Class", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "executablemodelingprofile_Class"):
                opp_val = getattr(value, "executablemodelingprofile_Class", None)
                setattr(value, "executablemodelingprofile_Class", self)

    def xClassExternal(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement xClassExternal method
        pass

    def xClassNestedClassifiers(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement xClassNestedClassifiers method
        pass

    def xClassMetaclass(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement xClassMetaclass method
        pass

class executablemodelingprofile_XConstrainedType(XClassifier):

    def __init__(self, isLowerBoundExclusive: str, isUpperBoundExclusive: str, executablemodelingprofile_XConstrainedType: "executablemodelingprofile_PrimitiveType" = None, executablemodelingprofile_XConstrainedType39: "executablemodelingprofile_LiteralSpecification" = None, executablemodelingprofile_XConstrainedType41: "executablemodelingprofile_LiteralSpecification" = None):
        self.isLowerBoundExclusive = isLowerBoundExclusive
        self.isUpperBoundExclusive = isUpperBoundExclusive
        self.executablemodelingprofile_XConstrainedType = executablemodelingprofile_XConstrainedType
        self.executablemodelingprofile_XConstrainedType39 = executablemodelingprofile_XConstrainedType39
        self.executablemodelingprofile_XConstrainedType41 = executablemodelingprofile_XConstrainedType41
        
    @property
    def isUpperBoundExclusive(self) -> str:
        return self.__isUpperBoundExclusive

    @isUpperBoundExclusive.setter
    def isUpperBoundExclusive(self, isUpperBoundExclusive: str):
        self.__isUpperBoundExclusive = isUpperBoundExclusive

    @property
    def isLowerBoundExclusive(self) -> str:
        return self.__isLowerBoundExclusive

    @isLowerBoundExclusive.setter
    def isLowerBoundExclusive(self, isLowerBoundExclusive: str):
        self.__isLowerBoundExclusive = isLowerBoundExclusive

    @property
    def executablemodelingprofile_XConstrainedType39(self):
        return self.__executablemodelingprofile_XConstrainedType39

    @executablemodelingprofile_XConstrainedType39.setter
    def executablemodelingprofile_XConstrainedType39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_executablemodelingprofile_XConstrainedType__executablemodelingprofile_XConstrainedType39", None)
        self.__executablemodelingprofile_XConstrainedType39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "executablemodelingprofile_LiteralSpecification"):
                opp_val = getattr(old_value, "executablemodelingprofile_LiteralSpecification", None)
                if opp_val == self:
                    setattr(old_value, "executablemodelingprofile_LiteralSpecification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "executablemodelingprofile_LiteralSpecification"):
                opp_val = getattr(value, "executablemodelingprofile_LiteralSpecification", None)
                setattr(value, "executablemodelingprofile_LiteralSpecification", self)

    @property
    def executablemodelingprofile_XConstrainedType(self):
        return self.__executablemodelingprofile_XConstrainedType

    @executablemodelingprofile_XConstrainedType.setter
    def executablemodelingprofile_XConstrainedType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_executablemodelingprofile_XConstrainedType__executablemodelingprofile_XConstrainedType", None)
        self.__executablemodelingprofile_XConstrainedType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "executablemodelingprofile_PrimitiveType"):
                opp_val = getattr(old_value, "executablemodelingprofile_PrimitiveType", None)
                if opp_val == self:
                    setattr(old_value, "executablemodelingprofile_PrimitiveType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "executablemodelingprofile_PrimitiveType"):
                opp_val = getattr(value, "executablemodelingprofile_PrimitiveType", None)
                setattr(value, "executablemodelingprofile_PrimitiveType", self)

    @property
    def executablemodelingprofile_XConstrainedType41(self):
        return self.__executablemodelingprofile_XConstrainedType41

    @executablemodelingprofile_XConstrainedType41.setter
    def executablemodelingprofile_XConstrainedType41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_executablemodelingprofile_XConstrainedType__executablemodelingprofile_XConstrainedType41", None)
        self.__executablemodelingprofile_XConstrainedType41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "executablemodelingprofile_LiteralSpecification42"):
                opp_val = getattr(old_value, "executablemodelingprofile_LiteralSpecification42", None)
                if opp_val == self:
                    setattr(old_value, "executablemodelingprofile_LiteralSpecification42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "executablemodelingprofile_LiteralSpecification42"):
                opp_val = getattr(value, "executablemodelingprofile_LiteralSpecification42", None)
                setattr(value, "executablemodelingprofile_LiteralSpecification42", self)

    def xConstrainedTypeBounds(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement xConstrainedTypeBounds method
        pass

    def xConstrainedTypePrimitiveType(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement xConstrainedTypePrimitiveType method
        pass

class executablemodelingprofile_XMessageSet(XClassifier):

    def __init__(self, messageKind: str, executablemodelingprofile_XMessageSet: "executablemodelingprofile_Interface" = None):
        self.messageKind = messageKind
        self.executablemodelingprofile_XMessageSet = executablemodelingprofile_XMessageSet
        
    @property
    def messageKind(self) -> str:
        return self.__messageKind

    @messageKind.setter
    def messageKind(self, messageKind: str):
        self.__messageKind = messageKind

    @property
    def executablemodelingprofile_XMessageSet(self):
        return self.__executablemodelingprofile_XMessageSet

    @executablemodelingprofile_XMessageSet.setter
    def executablemodelingprofile_XMessageSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_executablemodelingprofile_XMessageSet__executablemodelingprofile_XMessageSet", None)
        self.__executablemodelingprofile_XMessageSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "executablemodelingprofile_Interface"):
                opp_val = getattr(old_value, "executablemodelingprofile_Interface", None)
                if opp_val == self:
                    setattr(old_value, "executablemodelingprofile_Interface", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "executablemodelingprofile_Interface"):
                opp_val = getattr(value, "executablemodelingprofile_Interface", None)
                setattr(value, "executablemodelingprofile_Interface", self)

    def xMessageSetOutgoing(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement xMessageSetOutgoing method
        pass

    def xMessageSetSymmetric(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement xMessageSetSymmetric method
        pass

    def xMessageSetIncoming(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement xMessageSetIncoming method
        pass

class executablemodelingprofile_XAssociationClass(XAssociation, XClassifier):

    pass
class executablemodelingprofile_XSignal(XClassifier):

    def __init__(self, executablemodelingprofile_XSignal: "executablemodelingprofile_Signal" = None):
        self.executablemodelingprofile_XSignal = executablemodelingprofile_XSignal
        
    @property
    def executablemodelingprofile_XSignal(self):
        return self.__executablemodelingprofile_XSignal

    @executablemodelingprofile_XSignal.setter
    def executablemodelingprofile_XSignal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_executablemodelingprofile_XSignal__executablemodelingprofile_XSignal", None)
        self.__executablemodelingprofile_XSignal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "executablemodelingprofile_Signal"):
                opp_val = getattr(old_value, "executablemodelingprofile_Signal", None)
                if opp_val == self:
                    setattr(old_value, "executablemodelingprofile_Signal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "executablemodelingprofile_Signal"):
                opp_val = getattr(value, "executablemodelingprofile_Signal", None)
                setattr(value, "executablemodelingprofile_Signal", self)

    def xSignalVisibility(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement xSignalVisibility method
        pass

class executablemodelingprofile_XEncapsulatedClassifier(XClassifier):

    def __init__(self, isExternal: str, executablemodelingprofile_XEncapsulatedClassifier: "executablemodelingprofile_EncapsulatedClassifier" = None):
        self.isExternal = isExternal
        self.executablemodelingprofile_XEncapsulatedClassifier = executablemodelingprofile_XEncapsulatedClassifier
        
    @property
    def isExternal(self) -> str:
        return self.__isExternal

    @isExternal.setter
    def isExternal(self, isExternal: str):
        self.__isExternal = isExternal

    @property
    def executablemodelingprofile_XEncapsulatedClassifier(self):
        return self.__executablemodelingprofile_XEncapsulatedClassifier

    @executablemodelingprofile_XEncapsulatedClassifier.setter
    def executablemodelingprofile_XEncapsulatedClassifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_executablemodelingprofile_XEncapsulatedClassifier__executablemodelingprofile_XEncapsulatedClassifier", None)
        self.__executablemodelingprofile_XEncapsulatedClassifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "executablemodelingprofile_EncapsulatedClassifier"):
                opp_val = getattr(old_value, "executablemodelingprofile_EncapsulatedClassifier", None)
                if opp_val == self:
                    setattr(old_value, "executablemodelingprofile_EncapsulatedClassifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "executablemodelingprofile_EncapsulatedClassifier"):
                opp_val = getattr(value, "executablemodelingprofile_EncapsulatedClassifier", None)
                setattr(value, "executablemodelingprofile_EncapsulatedClassifier", self)

    def xEncapsulatedClassifierExternal(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement xEncapsulatedClassifierExternal method
        pass

    def xEncapsulatedClassifierPorts(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement xEncapsulatedClassifierPorts method
        pass

    def xEncapsulatedClassifierconnectors(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement xEncapsulatedClassifierconnectors method
        pass

class executablemodelingprofile_Behavior:

    pass
class executablemodelingprofile_XAssociation(ABC):

    def __init__(self, executablemodelingprofile_XAssociation: "executablemodelingprofile_Association" = None):
        self.executablemodelingprofile_XAssociation = executablemodelingprofile_XAssociation
        
    @property
    def executablemodelingprofile_XAssociation(self):
        return self.__executablemodelingprofile_XAssociation

    @executablemodelingprofile_XAssociation.setter
    def executablemodelingprofile_XAssociation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_executablemodelingprofile_XAssociation__executablemodelingprofile_XAssociation", None)
        self.__executablemodelingprofile_XAssociation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "executablemodelingprofile_Association"):
                opp_val = getattr(old_value, "executablemodelingprofile_Association", None)
                if opp_val == self:
                    setattr(old_value, "executablemodelingprofile_Association", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "executablemodelingprofile_Association"):
                opp_val = getattr(value, "executablemodelingprofile_Association", None)
                setattr(value, "executablemodelingprofile_Association", self)

    def xAssociationIsBinary(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement xAssociationIsBinary method
        pass

class executablemodelingprofile_Feature:

    pass
class executablemodelingprofile_NamedElement:

    pass
class executablemodelingprofile_Association:

    pass
class executablemodelingprofile_XNamedElement(ABC):

    def __init__(self, executablemodelingprofile_XNamedElement: "executablemodelingprofile_NamedElement" = None):
        self.executablemodelingprofile_XNamedElement = executablemodelingprofile_XNamedElement
        
    @property
    def executablemodelingprofile_XNamedElement(self):
        return self.__executablemodelingprofile_XNamedElement

    @executablemodelingprofile_XNamedElement.setter
    def executablemodelingprofile_XNamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_executablemodelingprofile_XNamedElement__executablemodelingprofile_XNamedElement", None)
        self.__executablemodelingprofile_XNamedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "executablemodelingprofile_NamedElement"):
                opp_val = getattr(old_value, "executablemodelingprofile_NamedElement", None)
                if opp_val == self:
                    setattr(old_value, "executablemodelingprofile_NamedElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "executablemodelingprofile_NamedElement"):
                opp_val = getattr(value, "executablemodelingprofile_NamedElement", None)
                setattr(value, "executablemodelingprofile_NamedElement", self)

    def xNamedElementName(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement xNamedElementName method
        pass

class executablemodelingprofile_Namespace:

    pass
class XNamedElement:

    pass
class executablemodelingprofile_XFeature(XNamedElement):

    def __init__(self, executablemodelingprofile_XFeature: "executablemodelingprofile_Feature" = None):
        self.executablemodelingprofile_XFeature = executablemodelingprofile_XFeature
        
    @property
    def executablemodelingprofile_XFeature(self):
        return self.__executablemodelingprofile_XFeature

    @executablemodelingprofile_XFeature.setter
    def executablemodelingprofile_XFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_executablemodelingprofile_XFeature__executablemodelingprofile_XFeature", None)
        self.__executablemodelingprofile_XFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "executablemodelingprofile_Feature"):
                opp_val = getattr(old_value, "executablemodelingprofile_Feature", None)
                if opp_val == self:
                    setattr(old_value, "executablemodelingprofile_Feature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "executablemodelingprofile_Feature"):
                opp_val = getattr(value, "executablemodelingprofile_Feature", None)
                setattr(value, "executablemodelingprofile_Feature", self)

    def xFeatureClassifier(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement xFeatureClassifier method
        pass

class executablemodelingprofile_XConstraint(XNamedElement):

    def __init__(self, executablemodelingprofile_XConstraint: "executablemodelingprofile_Constraint" = None):
        self.executablemodelingprofile_XConstraint = executablemodelingprofile_XConstraint
        
    @property
    def executablemodelingprofile_XConstraint(self):
        return self.__executablemodelingprofile_XConstraint

    @executablemodelingprofile_XConstraint.setter
    def executablemodelingprofile_XConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_executablemodelingprofile_XConstraint__executablemodelingprofile_XConstraint", None)
        self.__executablemodelingprofile_XConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "executablemodelingprofile_Constraint"):
                opp_val = getattr(old_value, "executablemodelingprofile_Constraint", None)
                if opp_val == self:
                    setattr(old_value, "executablemodelingprofile_Constraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "executablemodelingprofile_Constraint"):
                opp_val = getattr(value, "executablemodelingprofile_Constraint", None)
                setattr(value, "executablemodelingprofile_Constraint", self)

    def xConstraintSpecification(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement xConstraintSpecification method
        pass

    def xConstraintBehavior(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement xConstraintBehavior method
        pass

class executablemodelingprofile_XNamespace(XNamedElement):

    pass
class executablemodelingprofile_Operation:

    pass
class XNamespace:

    pass
class executablemodelingprofile_XBehavior(XNamespace):

    def __init__(self, executablemodelingprofile_XBehavior: "executablemodelingprofile_Behavior" = None):
        self.executablemodelingprofile_XBehavior = executablemodelingprofile_XBehavior
        
    @property
    def executablemodelingprofile_XBehavior(self):
        return self.__executablemodelingprofile_XBehavior

    @executablemodelingprofile_XBehavior.setter
    def executablemodelingprofile_XBehavior(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_executablemodelingprofile_XBehavior__executablemodelingprofile_XBehavior", None)
        self.__executablemodelingprofile_XBehavior = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "executablemodelingprofile_Behavior"):
                opp_val = getattr(old_value, "executablemodelingprofile_Behavior", None)
                if opp_val == self:
                    setattr(old_value, "executablemodelingprofile_Behavior", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "executablemodelingprofile_Behavior"):
                opp_val = getattr(value, "executablemodelingprofile_Behavior", None)
                setattr(value, "executablemodelingprofile_Behavior", self)

    def xBehaviorNoParameterSets(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement xBehaviorNoParameterSets method
        pass

class executablemodelingprofile_XClassifier(XNamespace):

    def __init__(self, executablemodelingprofile_XClassifier: "executablemodelingprofile_Classifier" = None):
        self.executablemodelingprofile_XClassifier = executablemodelingprofile_XClassifier
        
    @property
    def executablemodelingprofile_XClassifier(self):
        return self.__executablemodelingprofile_XClassifier

    @executablemodelingprofile_XClassifier.setter
    def executablemodelingprofile_XClassifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_executablemodelingprofile_XClassifier__executablemodelingprofile_XClassifier", None)
        self.__executablemodelingprofile_XClassifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "executablemodelingprofile_Classifier"):
                opp_val = getattr(old_value, "executablemodelingprofile_Classifier", None)
                if opp_val == self:
                    setattr(old_value, "executablemodelingprofile_Classifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "executablemodelingprofile_Classifier"):
                opp_val = getattr(value, "executablemodelingprofile_Classifier", None)
                setattr(value, "executablemodelingprofile_Classifier", self)

    def xClassifierConstraints(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement xClassifierConstraints method
        pass

    def xClassifierNestedClassifiers(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement xClassifierNestedClassifiers method
        pass

    def xClassifierFeatures(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement xClassifierFeatures method
        pass

    def xClassifierGenerals(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement xClassifierGenerals method
        pass

class XFeature:

    pass
class executablemodelingprofile_XProperty(XMultiplicityElement, XFeature, XTypedElement):

    pass
class executablemodelingprofile_XPart(XFeature, XTypedElement):

    def __init__(self, executablemodelingprofile_XPart: "executablemodelingprofile_Property" = None):
        self.executablemodelingprofile_XPart = executablemodelingprofile_XPart
        
    @property
    def executablemodelingprofile_XPart(self):
        return self.__executablemodelingprofile_XPart

    @executablemodelingprofile_XPart.setter
    def executablemodelingprofile_XPart(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_executablemodelingprofile_XPart__executablemodelingprofile_XPart", None)
        self.__executablemodelingprofile_XPart = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "executablemodelingprofile_Property20"):
                opp_val = getattr(old_value, "executablemodelingprofile_Property20", None)
                if opp_val == self:
                    setattr(old_value, "executablemodelingprofile_Property20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "executablemodelingprofile_Property20"):
                opp_val = getattr(value, "executablemodelingprofile_Property20", None)
                setattr(value, "executablemodelingprofile_Property20", self)

    def xPartClassifier(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement xPartClassifier method
        pass

class executablemodelingprofile_XConnector(XFeature):

    def __init__(self, executablemodelingprofile_XConnector: "executablemodelingprofile_Connector" = None):
        self.executablemodelingprofile_XConnector = executablemodelingprofile_XConnector
        
    @property
    def executablemodelingprofile_XConnector(self):
        return self.__executablemodelingprofile_XConnector

    @executablemodelingprofile_XConnector.setter
    def executablemodelingprofile_XConnector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_executablemodelingprofile_XConnector__executablemodelingprofile_XConnector", None)
        self.__executablemodelingprofile_XConnector = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "executablemodelingprofile_Connector"):
                opp_val = getattr(old_value, "executablemodelingprofile_Connector", None)
                if opp_val == self:
                    setattr(old_value, "executablemodelingprofile_Connector", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "executablemodelingprofile_Connector"):
                opp_val = getattr(value, "executablemodelingprofile_Connector", None)
                setattr(value, "executablemodelingprofile_Connector", self)

    def xtConnectorType(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement xtConnectorType method
        pass

    def xConnectorClassifier(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement xConnectorClassifier method
        pass

    def xConnectorEnds(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement xConnectorEnds method
        pass

class executablemodelingprofile_XPort(XFeature):

    def __init__(self, executablemodelingprofile_XPort: "executablemodelingprofile_Port" = None):
        self.executablemodelingprofile_XPort = executablemodelingprofile_XPort
        
    @property
    def executablemodelingprofile_XPort(self):
        return self.__executablemodelingprofile_XPort

    @executablemodelingprofile_XPort.setter
    def executablemodelingprofile_XPort(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_executablemodelingprofile_XPort__executablemodelingprofile_XPort", None)
        self.__executablemodelingprofile_XPort = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "executablemodelingprofile_Port"):
                opp_val = getattr(old_value, "executablemodelingprofile_Port", None)
                if opp_val == self:
                    setattr(old_value, "executablemodelingprofile_Port", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "executablemodelingprofile_Port"):
                opp_val = getattr(value, "executablemodelingprofile_Port", None)
                setattr(value, "executablemodelingprofile_Port", self)

    def xPortType(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement xPortType method
        pass

    def xPortOrderingUniqueness(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement xPortOrderingUniqueness method
        pass

    def xPortClassifier(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement xPortClassifier method
        pass

    def xPortBehaviorPort(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement xPortBehaviorPort method
        pass

    def xPortVisibility(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement xPortVisibility method
        pass

class executablemodelingprofile_XReception(XFeature):

    def __init__(self, executablemodelingprofile_XReception: "executablemodelingprofile_Reception" = None):
        self.executablemodelingprofile_XReception = executablemodelingprofile_XReception
        
    @property
    def executablemodelingprofile_XReception(self):
        return self.__executablemodelingprofile_XReception

    @executablemodelingprofile_XReception.setter
    def executablemodelingprofile_XReception(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_executablemodelingprofile_XReception__executablemodelingprofile_XReception", None)
        self.__executablemodelingprofile_XReception = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "executablemodelingprofile_Reception"):
                opp_val = getattr(old_value, "executablemodelingprofile_Reception", None)
                if opp_val == self:
                    setattr(old_value, "executablemodelingprofile_Reception", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "executablemodelingprofile_Reception"):
                opp_val = getattr(value, "executablemodelingprofile_Reception", None)
                setattr(value, "executablemodelingprofile_Reception", self)

    def xReceptionSignal(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement xReceptionSignal method
        pass

class executablemodelingprofile_XOperation(XNamespace, XFeature):

    def __init__(self, executablemodelingprofile_XOperation: "executablemodelingprofile_Operation" = None):
        self.executablemodelingprofile_XOperation = executablemodelingprofile_XOperation
        
    @property
    def executablemodelingprofile_XOperation(self):
        return self.__executablemodelingprofile_XOperation

    @executablemodelingprofile_XOperation.setter
    def executablemodelingprofile_XOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_executablemodelingprofile_XOperation__executablemodelingprofile_XOperation", None)
        self.__executablemodelingprofile_XOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "executablemodelingprofile_Operation"):
                opp_val = getattr(old_value, "executablemodelingprofile_Operation", None)
                if opp_val == self:
                    setattr(old_value, "executablemodelingprofile_Operation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "executablemodelingprofile_Operation"):
                opp_val = getattr(value, "executablemodelingprofile_Operation", None)
                setattr(value, "executablemodelingprofile_Operation", self)

    def xOperationParameters(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement xOperationParameters method
        pass

    def xOperationMethods(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement xOperationMethods method
        pass

    def xOperationImports(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement xOperationImports method
        pass

    def xOperationOneMethod(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement xOperationOneMethod method
        pass

    def xOperationConstraints(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement xOperationConstraints method
        pass

    def xOperationOwnedRules(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement xOperationOwnedRules method
        pass
