from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class SAMDerivatorKindEnum(Enum):
    POPULATION = "POPULATION"
    AGGREGATION = "AGGREGATION"
    OVERALL = "OVERALL"
class SAMOperatorKindEnum(Enum):
    OR = "OR"
    AND = "AND"
class PreconditionKindEnum(Enum):
    ENABLE = "ENABLE"
    REQUIRED = "REQUIRED"
    INHIBIT = "INHIBIT"
    NEUTEAL = "NEUTEAL"


############################################
# Definition of Classes
############################################

class assembly_Strategy:

    pass
class behavioral_assembly_Strategy(ABC):

    pass
class Strategy:

    pass
class behavioral_assembly_EnablingStrategy(Strategy):

    pass
class behavioral_assembly_InhibitingStrategy(Strategy):

    pass
class behavioral_assembly_NeutralStrategy(Strategy):

    pass
class behavioral_assembly_RequiredStrategy(Strategy):

    pass
class Operator:

    pass
class behavioral_assembly_OrOperator(Operator):

    pass
class behavioral_assembly_AndOperator(Operator):

    pass
class design_AbstractStatusVariable:

    pass
class Connector:

    pass
class behavioral_assembly_Synchroniser(Connector):

    pass
class behavioral_assembly_Precondition(Connector):

    pass
class behavioral_assembly_Transition(Connector):

    pass
class design_StatusValue:

    pass
class Signature:

    pass
class design_AbstractAction:

    pass
class ConnectableElement:

    pass
class behavioral_assembly_Operator(ConnectableElement):

    pass
class assembly_ConnectableElement:

    pass
class SchemaElement:

    pass
class behavioral_assembly_ConnectableElement(SchemaElement):

    pass
class behavioral_assembly_Connector(SchemaElement):

    pass
class assembly_SchemaElement:

    pass
class design_BusinessObjectNode:

    pass
class behavioral_design_BusinessObject:

    pass
class design_AbstractStatusValue:

    pass
class behavioral_assembly_StatusValueProxy(design_AbstractStatusValue, assembly_ConnectableElement, design_StatusValue):

    pass
class AbstractAction:

    pass
class behavioral_design_Action(AbstractAction):

    pass
class AbstractStatusValue:

    pass
class behavioral_design_StatusValue(AbstractStatusValue):

    pass
class AbstractStatusVariable:

    pass
class behavioral_design_StatusVariable(AbstractStatusVariable):

    pass
class design_Action:

    pass
class behavioral_assembly_ActionProxy(design_Action, design_AbstractAction, assembly_ConnectableElement):

    pass
class design_StatusVariable:

    pass
class behavioral_assembly_StatusVariableProxy(design_StatusVariable, design_AbstractStatusVariable, assembly_ConnectableElement):

    pass
class SAMDerivator:

    pass
class behavioral_status_and_action_old_SAMSchemaDerivator:

    pass
class SAMAction:

    pass
class behavioral_status_and_action_old_SAMSchemaAction:

    pass
class SAMStatusSchema:

    pass
class behavioral_status_and_action_old_SAMOperator:

    def __init__(self, kind: str, samOperators: "SAMStatusSchema" = None, samOperators68: set["SAMSchemaValue"] = None, samTargetOperators: set["SAMOperator"] = None, samSourceOperators: set["SAMOperator"] = None, samSchemaOperators: set["SAMSchemaAction"] = None):
        self.kind = kind
        self.samOperators = samOperators
        self.samOperators68 = samOperators68 if samOperators68 is not None else set()
        self.samTargetOperators = samTargetOperators if samTargetOperators is not None else set()
        self.samSourceOperators = samSourceOperators if samSourceOperators is not None else set()
        self.samSchemaOperators = samSchemaOperators if samSchemaOperators is not None else set()
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def samSourceOperators(self):
        return self.__samSourceOperators

    @samSourceOperators.setter
    def samSourceOperators(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_status_and_action_old_SAMOperator__samSourceOperators", None)
        self.__samSourceOperators = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SAMOperator72"):
                    opp_val = getattr(item, "SAMOperator72", None)
                    
                    if opp_val == self:
                        setattr(item, "SAMOperator72", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SAMOperator72"):
                    opp_val = getattr(item, "SAMOperator72", None)
                    
                    setattr(item, "SAMOperator72", self)
                    

    @property
    def samTargetOperators(self):
        return self.__samTargetOperators

    @samTargetOperators.setter
    def samTargetOperators(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_status_and_action_old_SAMOperator__samTargetOperators", None)
        self.__samTargetOperators = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SAMOperator70"):
                    opp_val = getattr(item, "SAMOperator70", None)
                    
                    if opp_val == self:
                        setattr(item, "SAMOperator70", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SAMOperator70"):
                    opp_val = getattr(item, "SAMOperator70", None)
                    
                    setattr(item, "SAMOperator70", self)
                    

    @property
    def samOperators(self):
        return self.__samOperators

    @samOperators.setter
    def samOperators(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_status_and_action_old_SAMOperator__samOperators", None)
        self.__samOperators = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SAMStatusSchema"):
                opp_val = getattr(old_value, "SAMStatusSchema", None)
                if opp_val == self:
                    setattr(old_value, "SAMStatusSchema", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SAMStatusSchema"):
                opp_val = getattr(value, "SAMStatusSchema", None)
                setattr(value, "SAMStatusSchema", self)

    @property
    def samSchemaOperators(self):
        return self.__samSchemaOperators

    @samSchemaOperators.setter
    def samSchemaOperators(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_status_and_action_old_SAMOperator__samSchemaOperators", None)
        self.__samSchemaOperators = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SAMSchemaAction74"):
                    opp_val = getattr(item, "SAMSchemaAction74", None)
                    
                    if opp_val == self:
                        setattr(item, "SAMSchemaAction74", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SAMSchemaAction74"):
                    opp_val = getattr(item, "SAMSchemaAction74", None)
                    
                    setattr(item, "SAMSchemaAction74", self)
                    

    @property
    def samOperators68(self):
        return self.__samOperators68

    @samOperators68.setter
    def samOperators68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_status_and_action_old_SAMOperator__samOperators68", None)
        self.__samOperators68 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SAMSchemaValue"):
                    opp_val = getattr(item, "SAMSchemaValue", None)
                    
                    if opp_val == self:
                        setattr(item, "SAMSchemaValue", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SAMSchemaValue"):
                    opp_val = getattr(item, "SAMSchemaValue", None)
                    
                    setattr(item, "SAMSchemaValue", self)
                    

class behavioral_status_and_action_old_SAMSchemaValue:

    def __init__(self, isInitial: bool, isInhibiting: bool, samSchemaValues: "SAMSchemaVariable" = None, samTargetSchemaValues: set["SAMSchemaAction"] = None, samTargetSchemaValues91: set["SAMSchemaValue"] = None, samSourceSchemaValues: set["SAMSchemaValue"] = None, samSchemaValues96: set["SAMOperator"] = None, samSchemaValues99: set["SAMSchemaAction"] = None):
        self.isInitial = isInitial
        self.isInhibiting = isInhibiting
        self.samSchemaValues = samSchemaValues
        self.samTargetSchemaValues = samTargetSchemaValues if samTargetSchemaValues is not None else set()
        self.samTargetSchemaValues91 = samTargetSchemaValues91 if samTargetSchemaValues91 is not None else set()
        self.samSourceSchemaValues = samSourceSchemaValues if samSourceSchemaValues is not None else set()
        self.samSchemaValues96 = samSchemaValues96 if samSchemaValues96 is not None else set()
        self.samSchemaValues99 = samSchemaValues99 if samSchemaValues99 is not None else set()
        
        pass
    @property
    def isInitial(self):
        return self.__isInitial

    @isInitial.setter
    def isInitial(self, isInitial: bool):
        self.__isInitial = isInitial


    @property
    def isInhibiting(self):
        return self.__isInhibiting

    @isInhibiting.setter
    def isInhibiting(self, isInhibiting: bool):
        self.__isInhibiting = isInhibiting


    @property
    def samTargetSchemaValues91(self):
        return self.__samTargetSchemaValues91

    @samTargetSchemaValues91.setter
    def samTargetSchemaValues91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_status_and_action_old_SAMSchemaValue__samTargetSchemaValues91", None)
        self.__samTargetSchemaValues91 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SAMSchemaValue92"):
                    opp_val = getattr(item, "SAMSchemaValue92", None)
                    
                    if opp_val == self:
                        setattr(item, "SAMSchemaValue92", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SAMSchemaValue92"):
                    opp_val = getattr(item, "SAMSchemaValue92", None)
                    
                    setattr(item, "SAMSchemaValue92", self)
                    

    @property
    def samSourceSchemaValues(self):
        return self.__samSourceSchemaValues

    @samSourceSchemaValues.setter
    def samSourceSchemaValues(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_status_and_action_old_SAMSchemaValue__samSourceSchemaValues", None)
        self.__samSourceSchemaValues = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SAMSchemaValue94"):
                    opp_val = getattr(item, "SAMSchemaValue94", None)
                    
                    if opp_val == self:
                        setattr(item, "SAMSchemaValue94", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SAMSchemaValue94"):
                    opp_val = getattr(item, "SAMSchemaValue94", None)
                    
                    setattr(item, "SAMSchemaValue94", self)
                    

    @property
    def samSchemaValues(self):
        return self.__samSchemaValues

    @samSchemaValues.setter
    def samSchemaValues(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_status_and_action_old_SAMSchemaValue__samSchemaValues", None)
        self.__samSchemaValues = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SAMSchemaVariable87"):
                opp_val = getattr(old_value, "SAMSchemaVariable87", None)
                if opp_val == self:
                    setattr(old_value, "SAMSchemaVariable87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SAMSchemaVariable87"):
                opp_val = getattr(value, "SAMSchemaVariable87", None)
                setattr(value, "SAMSchemaVariable87", self)

    @property
    def samSchemaValues99(self):
        return self.__samSchemaValues99

    @samSchemaValues99.setter
    def samSchemaValues99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_status_and_action_old_SAMSchemaValue__samSchemaValues99", None)
        self.__samSchemaValues99 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SAMSchemaAction100"):
                    opp_val = getattr(item, "SAMSchemaAction100", None)
                    
                    if opp_val == self:
                        setattr(item, "SAMSchemaAction100", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SAMSchemaAction100"):
                    opp_val = getattr(item, "SAMSchemaAction100", None)
                    
                    setattr(item, "SAMSchemaAction100", self)
                    

    @property
    def samTargetSchemaValues(self):
        return self.__samTargetSchemaValues

    @samTargetSchemaValues.setter
    def samTargetSchemaValues(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_status_and_action_old_SAMSchemaValue__samTargetSchemaValues", None)
        self.__samTargetSchemaValues = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SAMSchemaAction89"):
                    opp_val = getattr(item, "SAMSchemaAction89", None)
                    
                    if opp_val == self:
                        setattr(item, "SAMSchemaAction89", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SAMSchemaAction89"):
                    opp_val = getattr(item, "SAMSchemaAction89", None)
                    
                    setattr(item, "SAMSchemaAction89", self)
                    

    @property
    def samSchemaValues96(self):
        return self.__samSchemaValues96

    @samSchemaValues96.setter
    def samSchemaValues96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_status_and_action_old_SAMSchemaValue__samSchemaValues96", None)
        self.__samSchemaValues96 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SAMOperator97"):
                    opp_val = getattr(item, "SAMOperator97", None)
                    
                    if opp_val == self:
                        setattr(item, "SAMOperator97", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SAMOperator97"):
                    opp_val = getattr(item, "SAMOperator97", None)
                    
                    setattr(item, "SAMOperator97", self)
                    

class behavioral_status_and_action_old_SAMSchemaVariable:

    def __init__(self, hasStateGuard: bool, samSchemaVariables: "SAMStatusSchema" = None, samSchemaVariable: set["SAMSchemaValue"] = None, samSchemaVariables80: "SAMStatusVariable" = None, samSourceSchemaVariables: set["SAMSchemaDerivator"] = None, samTargetSchemaVariable: set["SAMSchemaDerivator"] = None):
        self.hasStateGuard = hasStateGuard
        self.samSchemaVariables = samSchemaVariables
        self.samSchemaVariable = samSchemaVariable if samSchemaVariable is not None else set()
        self.samSchemaVariables80 = samSchemaVariables80
        self.samSourceSchemaVariables = samSourceSchemaVariables if samSourceSchemaVariables is not None else set()
        self.samTargetSchemaVariable = samTargetSchemaVariable if samTargetSchemaVariable is not None else set()
        
        pass
    @property
    def hasStateGuard(self):
        return self.__hasStateGuard

    @hasStateGuard.setter
    def hasStateGuard(self, hasStateGuard: bool):
        self.__hasStateGuard = hasStateGuard


    @property
    def samSchemaVariables(self):
        return self.__samSchemaVariables

    @samSchemaVariables.setter
    def samSchemaVariables(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_status_and_action_old_SAMSchemaVariable__samSchemaVariables", None)
        self.__samSchemaVariables = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SAMStatusSchema76"):
                opp_val = getattr(old_value, "SAMStatusSchema76", None)
                if opp_val == self:
                    setattr(old_value, "SAMStatusSchema76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SAMStatusSchema76"):
                opp_val = getattr(value, "SAMStatusSchema76", None)
                setattr(value, "SAMStatusSchema76", self)

    @property
    def samSchemaVariable(self):
        return self.__samSchemaVariable

    @samSchemaVariable.setter
    def samSchemaVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_status_and_action_old_SAMSchemaVariable__samSchemaVariable", None)
        self.__samSchemaVariable = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SAMSchemaValue78"):
                    opp_val = getattr(item, "SAMSchemaValue78", None)
                    
                    if opp_val == self:
                        setattr(item, "SAMSchemaValue78", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SAMSchemaValue78"):
                    opp_val = getattr(item, "SAMSchemaValue78", None)
                    
                    setattr(item, "SAMSchemaValue78", self)
                    

    @property
    def samSourceSchemaVariables(self):
        return self.__samSourceSchemaVariables

    @samSourceSchemaVariables.setter
    def samSourceSchemaVariables(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_status_and_action_old_SAMSchemaVariable__samSourceSchemaVariables", None)
        self.__samSourceSchemaVariables = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SAMSchemaDerivator83"):
                    opp_val = getattr(item, "SAMSchemaDerivator83", None)
                    
                    if opp_val == self:
                        setattr(item, "SAMSchemaDerivator83", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SAMSchemaDerivator83"):
                    opp_val = getattr(item, "SAMSchemaDerivator83", None)
                    
                    setattr(item, "SAMSchemaDerivator83", self)
                    

    @property
    def samSchemaVariables80(self):
        return self.__samSchemaVariables80

    @samSchemaVariables80.setter
    def samSchemaVariables80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_status_and_action_old_SAMSchemaVariable__samSchemaVariables80", None)
        self.__samSchemaVariables80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SAMStatusVariable81"):
                opp_val = getattr(old_value, "SAMStatusVariable81", None)
                if opp_val == self:
                    setattr(old_value, "SAMStatusVariable81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SAMStatusVariable81"):
                opp_val = getattr(value, "SAMStatusVariable81", None)
                setattr(value, "SAMStatusVariable81", self)

    @property
    def samTargetSchemaVariable(self):
        return self.__samTargetSchemaVariable

    @samTargetSchemaVariable.setter
    def samTargetSchemaVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_status_and_action_old_SAMSchemaVariable__samTargetSchemaVariable", None)
        self.__samTargetSchemaVariable = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SAMSchemaDerivator85"):
                    opp_val = getattr(item, "SAMSchemaDerivator85", None)
                    
                    if opp_val == self:
                        setattr(item, "SAMSchemaDerivator85", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SAMSchemaDerivator85"):
                    opp_val = getattr(item, "SAMSchemaDerivator85", None)
                    
                    setattr(item, "SAMSchemaDerivator85", self)
                    

class SAMSchemaValue:

    pass
class behavioral_status_and_action_old_SAMAction:

    def __init__(self, name: str, isAgentAction: bool, samAction: set["SAMSchemaAction"] = None, samActions: "SapClass" = None):
        self.name = name
        self.isAgentAction = isAgentAction
        self.samAction = samAction if samAction is not None else set()
        self.samActions = samActions
        
        pass
    @property
    def isAgentAction(self):
        return self.__isAgentAction

    @isAgentAction.setter
    def isAgentAction(self, isAgentAction: bool):
        self.__isAgentAction = isAgentAction


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def samActions(self):
        return self.__samActions

    @samActions.setter
    def samActions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_status_and_action_old_SAMAction__samActions", None)
        self.__samActions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SapClass43"):
                opp_val = getattr(old_value, "SapClass43", None)
                if opp_val == self:
                    setattr(old_value, "SapClass43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SapClass43"):
                opp_val = getattr(value, "SapClass43", None)
                setattr(value, "SapClass43", self)

    @property
    def samAction(self):
        return self.__samAction

    @samAction.setter
    def samAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_status_and_action_old_SAMAction__samAction", None)
        self.__samAction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SAMSchemaAction"):
                    opp_val = getattr(item, "SAMSchemaAction", None)
                    
                    if opp_val == self:
                        setattr(item, "SAMSchemaAction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SAMSchemaAction"):
                    opp_val = getattr(item, "SAMSchemaAction", None)
                    
                    setattr(item, "SAMSchemaAction", self)
                    

class SAMOperator:

    pass
class behavioral_status_and_action_old_SAMStatusSchema:

    def __init__(self, name: str, samStatusSchema: "SapClass" = None, samStatusSchema56: set["SAMOperator"] = None, samStatusSchema58: set["SAMSchemaVariable"] = None, samStatusSchema61: set["SAMSchemaAction"] = None, samStatusSchema64: set["SAMSchemaDerivator"] = None):
        self.name = name
        self.samStatusSchema = samStatusSchema
        self.samStatusSchema56 = samStatusSchema56 if samStatusSchema56 is not None else set()
        self.samStatusSchema58 = samStatusSchema58 if samStatusSchema58 is not None else set()
        self.samStatusSchema61 = samStatusSchema61 if samStatusSchema61 is not None else set()
        self.samStatusSchema64 = samStatusSchema64 if samStatusSchema64 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def samStatusSchema58(self):
        return self.__samStatusSchema58

    @samStatusSchema58.setter
    def samStatusSchema58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_status_and_action_old_SAMStatusSchema__samStatusSchema58", None)
        self.__samStatusSchema58 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SAMSchemaVariable59"):
                    opp_val = getattr(item, "SAMSchemaVariable59", None)
                    
                    if opp_val == self:
                        setattr(item, "SAMSchemaVariable59", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SAMSchemaVariable59"):
                    opp_val = getattr(item, "SAMSchemaVariable59", None)
                    
                    setattr(item, "SAMSchemaVariable59", self)
                    

    @property
    def samStatusSchema64(self):
        return self.__samStatusSchema64

    @samStatusSchema64.setter
    def samStatusSchema64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_status_and_action_old_SAMStatusSchema__samStatusSchema64", None)
        self.__samStatusSchema64 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SAMSchemaDerivator65"):
                    opp_val = getattr(item, "SAMSchemaDerivator65", None)
                    
                    if opp_val == self:
                        setattr(item, "SAMSchemaDerivator65", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SAMSchemaDerivator65"):
                    opp_val = getattr(item, "SAMSchemaDerivator65", None)
                    
                    setattr(item, "SAMSchemaDerivator65", self)
                    

    @property
    def samStatusSchema(self):
        return self.__samStatusSchema

    @samStatusSchema.setter
    def samStatusSchema(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_status_and_action_old_SAMStatusSchema__samStatusSchema", None)
        self.__samStatusSchema = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SapClass54"):
                opp_val = getattr(old_value, "SapClass54", None)
                if opp_val == self:
                    setattr(old_value, "SapClass54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SapClass54"):
                opp_val = getattr(value, "SapClass54", None)
                setattr(value, "SapClass54", self)

    @property
    def samStatusSchema56(self):
        return self.__samStatusSchema56

    @samStatusSchema56.setter
    def samStatusSchema56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_status_and_action_old_SAMStatusSchema__samStatusSchema56", None)
        self.__samStatusSchema56 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SAMOperator"):
                    opp_val = getattr(item, "SAMOperator", None)
                    
                    if opp_val == self:
                        setattr(item, "SAMOperator", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SAMOperator"):
                    opp_val = getattr(item, "SAMOperator", None)
                    
                    setattr(item, "SAMOperator", self)
                    

    @property
    def samStatusSchema61(self):
        return self.__samStatusSchema61

    @samStatusSchema61.setter
    def samStatusSchema61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_status_and_action_old_SAMStatusSchema__samStatusSchema61", None)
        self.__samStatusSchema61 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SAMSchemaAction62"):
                    opp_val = getattr(item, "SAMSchemaAction62", None)
                    
                    if opp_val == self:
                        setattr(item, "SAMSchemaAction62", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SAMSchemaAction62"):
                    opp_val = getattr(item, "SAMSchemaAction62", None)
                    
                    setattr(item, "SAMSchemaAction62", self)
                    

class SAMStatusVariable:

    pass
class behavioral_status_and_action_old_SAMStatusValue:

    def __init__(self, name: str, samStatusValues: "SAMStatusVariable" = None):
        self.name = name
        self.samStatusValues = samStatusValues
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def samStatusValues(self):
        return self.__samStatusValues

    @samStatusValues.setter
    def samStatusValues(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_status_and_action_old_SAMStatusValue__samStatusValues", None)
        self.__samStatusValues = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SAMStatusVariable"):
                opp_val = getattr(old_value, "SAMStatusVariable", None)
                if opp_val == self:
                    setattr(old_value, "SAMStatusVariable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SAMStatusVariable"):
                opp_val = getattr(value, "SAMStatusVariable", None)
                setattr(value, "SAMStatusVariable", self)

class SAMSchemaDerivator:

    pass
class behavioral_status_and_action_old_SAMDerivator:

    def __init__(self, kind: str, samDerivators: "SapClass" = None, samDerivator: set["SAMSchemaDerivator"] = None):
        self.kind = kind
        self.samDerivators = samDerivators
        self.samDerivator = samDerivator if samDerivator is not None else set()
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def samDerivator(self):
        return self.__samDerivator

    @samDerivator.setter
    def samDerivator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_status_and_action_old_SAMDerivator__samDerivator", None)
        self.__samDerivator = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SAMSchemaDerivator"):
                    opp_val = getattr(item, "SAMSchemaDerivator", None)
                    
                    if opp_val == self:
                        setattr(item, "SAMSchemaDerivator", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SAMSchemaDerivator"):
                    opp_val = getattr(item, "SAMSchemaDerivator", None)
                    
                    setattr(item, "SAMSchemaDerivator", self)
                    

    @property
    def samDerivators(self):
        return self.__samDerivators

    @samDerivators.setter
    def samDerivators(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_status_and_action_old_SAMDerivator__samDerivators", None)
        self.__samDerivators = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SapClass50"):
                opp_val = getattr(old_value, "SapClass50", None)
                if opp_val == self:
                    setattr(old_value, "SapClass50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SapClass50"):
                opp_val = getattr(value, "SapClass50", None)
                setattr(value, "SapClass50", self)

class SAMSchemaVariable:

    pass
class SAMStatusValue:

    pass
class behavioral_status_and_action_old_SAMStatusVariable:

    def __init__(self, name: str, isAgentVariable: bool, samStatusVariables: "SapClass" = None, samStatusVariable: set["SAMStatusValue"] = None, samSchemaValue: set["SAMSchemaVariable"] = None):
        self.name = name
        self.isAgentVariable = isAgentVariable
        self.samStatusVariables = samStatusVariables
        self.samStatusVariable = samStatusVariable if samStatusVariable is not None else set()
        self.samSchemaValue = samSchemaValue if samSchemaValue is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def isAgentVariable(self):
        return self.__isAgentVariable

    @isAgentVariable.setter
    def isAgentVariable(self, isAgentVariable: bool):
        self.__isAgentVariable = isAgentVariable


    @property
    def samStatusVariables(self):
        return self.__samStatusVariables

    @samStatusVariables.setter
    def samStatusVariables(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_status_and_action_old_SAMStatusVariable__samStatusVariables", None)
        self.__samStatusVariables = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SapClass46"):
                opp_val = getattr(old_value, "SapClass46", None)
                if opp_val == self:
                    setattr(old_value, "SapClass46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SapClass46"):
                opp_val = getattr(value, "SapClass46", None)
                setattr(value, "SapClass46", self)

    @property
    def samStatusVariable(self):
        return self.__samStatusVariable

    @samStatusVariable.setter
    def samStatusVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_status_and_action_old_SAMStatusVariable__samStatusVariable", None)
        self.__samStatusVariable = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SAMStatusValue"):
                    opp_val = getattr(item, "SAMStatusValue", None)
                    
                    if opp_val == self:
                        setattr(item, "SAMStatusValue", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SAMStatusValue"):
                    opp_val = getattr(item, "SAMStatusValue", None)
                    
                    setattr(item, "SAMStatusValue", self)
                    

    @property
    def samSchemaValue(self):
        return self.__samSchemaValue

    @samSchemaValue.setter
    def samSchemaValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_status_and_action_old_SAMStatusVariable__samSchemaValue", None)
        self.__samSchemaValue = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SAMSchemaVariable"):
                    opp_val = getattr(item, "SAMSchemaVariable", None)
                    
                    if opp_val == self:
                        setattr(item, "SAMSchemaVariable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SAMSchemaVariable"):
                    opp_val = getattr(item, "SAMSchemaVariable", None)
                    
                    setattr(item, "SAMSchemaVariable", self)
                    

class SAMSchemaAction:

    pass
class behavioral_transactions_Dummy:

    pass
class behavioral_events_EventFilter:

    pass
class MethodSignature:

    pass
class Subscription:

    pass
class behavioral_events_EventProducer(ABC):

    pass
class SapClass:

    pass
class EventFilter:

    pass
class EventProducer:

    pass
class DimensionDefinition:

    pass
class NamedElement:

    pass
class behavioral_assembly_SchemaElement(NamedElement):

    pass
class behavioral_design_AbstractAction(NamedElement):

    def __init__(self, isAgent: bool, isPreconditionFixed: bool):
        self.isAgent = isAgent
        self.isPreconditionFixed = isPreconditionFixed
        
        pass
    @property
    def isPreconditionFixed(self):
        return self.__isPreconditionFixed

    @isPreconditionFixed.setter
    def isPreconditionFixed(self, isPreconditionFixed: bool):
        self.__isPreconditionFixed = isPreconditionFixed


    @property
    def isAgent(self):
        return self.__isAgent

    @isAgent.setter
    def isAgent(self, isAgent: bool):
        self.__isAgent = isAgent


class behavioral_design_AbstractStatusVariable(NamedElement):

    def __init__(self, isAgent: bool, isStateGuarded: bool, behavioral_design_AbstractStatusVariable: set["design_AbstractStatusValue"] = None):
        self.isAgent = isAgent
        self.isStateGuarded = isStateGuarded
        self.behavioral_design_AbstractStatusVariable = behavioral_design_AbstractStatusVariable if behavioral_design_AbstractStatusVariable is not None else set()
        
        pass
    @property
    def isStateGuarded(self):
        return self.__isStateGuarded

    @isStateGuarded.setter
    def isStateGuarded(self, isStateGuarded: bool):
        self.__isStateGuarded = isStateGuarded


    @property
    def isAgent(self):
        return self.__isAgent

    @isAgent.setter
    def isAgent(self, isAgent: bool):
        self.__isAgent = isAgent


    @property
    def behavioral_design_AbstractStatusVariable(self):
        return self.__behavioral_design_AbstractStatusVariable

    @behavioral_design_AbstractStatusVariable.setter
    def behavioral_design_AbstractStatusVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_design_AbstractStatusVariable__behavioral_design_AbstractStatusVariable", None)
        self.__behavioral_design_AbstractStatusVariable = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "design_AbstractStatusValue"):
                    opp_val = getattr(item, "design_AbstractStatusValue", None)
                    
                    if opp_val == self:
                        setattr(item, "design_AbstractStatusValue", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "design_AbstractStatusValue"):
                    opp_val = getattr(item, "design_AbstractStatusValue", None)
                    
                    setattr(item, "design_AbstractStatusValue", self)
                    

class behavioral_design_AbstractStatusValue(NamedElement):

    def __init__(self, isInitial: bool, isInhibiting: bool, isStateGuarded: bool):
        self.isInitial = isInitial
        self.isInhibiting = isInhibiting
        self.isStateGuarded = isStateGuarded
        
        pass
    @property
    def isInhibiting(self):
        return self.__isInhibiting

    @isInhibiting.setter
    def isInhibiting(self, isInhibiting: bool):
        self.__isInhibiting = isInhibiting


    @property
    def isStateGuarded(self):
        return self.__isStateGuarded

    @isStateGuarded.setter
    def isStateGuarded(self, isStateGuarded: bool):
        self.__isStateGuarded = isStateGuarded


    @property
    def isInitial(self):
        return self.__isInitial

    @isInitial.setter
    def isInitial(self, isInitial: bool):
        self.__isInitial = isInitial


class behavioral_assembly_StatusSchema(NamedElement):

    pass
class behavioral_design_BusinessObjectNode(NamedElement):

    pass
class behavioral_events_Subscription(NamedElement):

    pass
class behavioral_rules_Dummy:

    pass
class expressions_Conditional:

    pass
class NamedValueDeclaration:

    pass
class expressions_WithArgument:

    pass
class actions_Statement:

    pass
class behavioral_actions_ConditionalStatement(expressions_Conditional, actions_Statement):

    pass
class behavioral_actions_StatementWithArgument(expressions_WithArgument, actions_Statement):

    pass
class Association:

    pass
class GroupBy:

    pass
class FromClause:

    pass
class Selection:

    pass
class Foreach:

    pass
class Assignment:

    pass
class collectionexpressions_Iterate:

    pass
class NamedValueWithOptionalInitExpression:

    pass
class behavioral_actions_Variable(NamedValueWithOptionalInitExpression):

    def __init__(self, assignTo: set["Assignment"] = None, NamedValueWithOptionalInitExpression: "behavioral_actions_NamedValueDeclaration" = None):
        self.assignTo = assignTo if assignTo is not None else set()
        
        pass
    @property
    def assignTo(self):
        return self.__assignTo

    @assignTo.setter
    def assignTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_actions_Variable__assignTo", None)
        self.__assignTo = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Assignment"):
                    opp_val = getattr(item, "Assignment", None)
                    
                    if opp_val == self:
                        setattr(item, "Assignment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Assignment"):
                    opp_val = getattr(item, "Assignment", None)
                    
                    setattr(item, "Assignment", self)
                    

    def getCommonTypeOfAssignments(self):
        # TODO: Implement getCommonTypeOfAssignments method
        pass

class behavioral_actions_Constant(NamedValueWithOptionalInitExpression):

    pass
class behavioral_actions_QueryInvocation:

    pass
class behavioral_actions_Sort:

    pass
class LinkManipulationStatement:

    pass
class behavioral_actions_RemoveLink(LinkManipulationStatement):

    pass
class behavioral_actions_AddLink(LinkManipulationStatement):

    pass
class Iterator:

    pass
class Expression:

    pass
class SingleBlockStatement:

    pass
class behavioral_actions_Foreach(SingleBlockStatement):

    def __init__(self, parallel: bool, behavioral_actions_Foreach: "Expression" = None, boundToFor: "Iterator" = None):
        self.parallel = parallel
        self.behavioral_actions_Foreach = behavioral_actions_Foreach
        self.boundToFor = boundToFor
        
        pass
    @property
    def parallel(self):
        return self.__parallel

    @parallel.setter
    def parallel(self, parallel: bool):
        self.__parallel = parallel


    @property
    def boundToFor(self):
        return self.__boundToFor

    @boundToFor.setter
    def boundToFor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_actions_Foreach__boundToFor", None)
        self.__boundToFor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Iterator"):
                opp_val = getattr(old_value, "Iterator", None)
                if opp_val == self:
                    setattr(old_value, "Iterator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Iterator"):
                opp_val = getattr(value, "Iterator", None)
                setattr(value, "Iterator", self)

    @property
    def behavioral_actions_Foreach(self):
        return self.__behavioral_actions_Foreach

    @behavioral_actions_Foreach.setter
    def behavioral_actions_Foreach(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_actions_Foreach__behavioral_actions_Foreach", None)
        self.__behavioral_actions_Foreach = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression"):
                opp_val = getattr(old_value, "Expression", None)
                if opp_val == self:
                    setattr(old_value, "Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression"):
                opp_val = getattr(value, "Expression", None)
                setattr(value, "Expression", self)

class actions_SingleBlockStatement:

    pass
class Block:

    pass
class actions_StatementWithNestedBlocks:

    pass
class actions_ConditionalStatement:

    pass
class behavioral_actions_WhileLoop(actions_ConditionalStatement, actions_SingleBlockStatement):

    def __init__(self):
        
        pass
    def getLoopBody(self) :
        # TODO: Implement getLoopBody method
        pass

class behavioral_actions_IfElse(actions_StatementWithNestedBlocks, actions_ConditionalStatement):

    def __init__(self):
        
        pass
    def getElseBlock(self) :
        # TODO: Implement getElseBlock method
        pass

    def getIfBlock(self) :
        # TODO: Implement getIfBlock method
        pass

class StatementWithNestedBlocks:

    pass
class behavioral_actions_SingleBlockStatement(StatementWithNestedBlocks):

    pass
class NamedValue:

    pass
class behavioral_actions_NamedValueWithOptionalInitExpression(NamedValue):

    pass
class behavioral_actions_Iterator(NamedValue):

    pass
class Statement:

    pass
class behavioral_actions_NamedValueDeclaration(Statement):

    pass
class behavioral_actions_StatementWithNestedBlocks(Statement):

    pass
class behavioral_actions_ExpressionStatement(Statement):

    pass
class behavioral_actions_LinkManipulationStatement(Statement):

    def __init__(self, at: int, behavioral_actions_LinkManipulationStatement: "Association" = None, behavioral_actions_LinkManipulationStatement9: set["Expression"] = None, Statement: "behavioral_actions_Block" = None):
        self.at = at
        self.behavioral_actions_LinkManipulationStatement = behavioral_actions_LinkManipulationStatement
        self.behavioral_actions_LinkManipulationStatement9 = behavioral_actions_LinkManipulationStatement9 if behavioral_actions_LinkManipulationStatement9 is not None else set()
        
        pass
    @property
    def at(self):
        return self.__at

    @at.setter
    def at(self, at: int):
        self.__at = at


    @property
    def behavioral_actions_LinkManipulationStatement9(self):
        return self.__behavioral_actions_LinkManipulationStatement9

    @behavioral_actions_LinkManipulationStatement9.setter
    def behavioral_actions_LinkManipulationStatement9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_actions_LinkManipulationStatement__behavioral_actions_LinkManipulationStatement9", None)
        self.__behavioral_actions_LinkManipulationStatement9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Expression10"):
                    opp_val = getattr(item, "Expression10", None)
                    
                    if opp_val == self:
                        setattr(item, "Expression10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Expression10"):
                    opp_val = getattr(item, "Expression10", None)
                    
                    setattr(item, "Expression10", self)
                    

    @property
    def behavioral_actions_LinkManipulationStatement(self):
        return self.__behavioral_actions_LinkManipulationStatement

    @behavioral_actions_LinkManipulationStatement.setter
    def behavioral_actions_LinkManipulationStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_actions_LinkManipulationStatement__behavioral_actions_LinkManipulationStatement", None)
        self.__behavioral_actions_LinkManipulationStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Association"):
                opp_val = getattr(old_value, "Association", None)
                if opp_val == self:
                    setattr(old_value, "Association", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Association"):
                opp_val = getattr(value, "Association", None)
                setattr(value, "Association", self)

class classes_InScope:

    pass
class classes_FunctionSignatureImplementation:

    pass
class behavioral_actions_Block(classes_InScope, classes_FunctionSignatureImplementation):

    def __init__(self, block: set["Statement"] = None, owner: set["NamedValue"] = None, nestedBlocks: "StatementWithNestedBlocks" = None):
        self.block = block if block is not None else set()
        self.owner = owner if owner is not None else set()
        self.nestedBlocks = nestedBlocks
        
        pass
    @property
    def block(self):
        return self.__block

    @block.setter
    def block(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_actions_Block__block", None)
        self.__block = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Statement"):
                    opp_val = getattr(item, "Statement", None)
                    
                    if opp_val == self:
                        setattr(item, "Statement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Statement"):
                    opp_val = getattr(item, "Statement", None)
                    
                    setattr(item, "Statement", self)
                    

    @property
    def nestedBlocks(self):
        return self.__nestedBlocks

    @nestedBlocks.setter
    def nestedBlocks(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_actions_Block__nestedBlocks", None)
        self.__nestedBlocks = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StatementWithNestedBlocks"):
                opp_val = getattr(old_value, "StatementWithNestedBlocks", None)
                if opp_val == self:
                    setattr(old_value, "StatementWithNestedBlocks", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StatementWithNestedBlocks"):
                opp_val = getattr(value, "StatementWithNestedBlocks", None)
                setattr(value, "StatementWithNestedBlocks", self)

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_actions_Block__owner", None)
        self.__owner = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NamedValue"):
                    opp_val = getattr(item, "NamedValue", None)
                    
                    if opp_val == self:
                        setattr(item, "NamedValue", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NamedValue"):
                    opp_val = getattr(item, "NamedValue", None)
                    
                    setattr(item, "NamedValue", self)
                    

    def getNamedValuesInScope(self) :
        # TODO: Implement getNamedValuesInScope method
        pass

    def getOutermostBlock(self) :
        # TODO: Implement getOutermostBlock method
        pass

    def getOwningClass(self) :
        # TODO: Implement getOwningClass method
        pass

    def localIsSideEffectFree(self) :
        # TODO: Implement localIsSideEffectFree method
        pass

class behavioral_businesstasks_TaskAgent:

    pass
class InScope:

    pass
class behavioral_actions_Statement(InScope):

    def __init__(self, statements: "Block" = None):
        self.statements = statements
        
        pass
    @property
    def statements(self):
        return self.__statements

    @statements.setter
    def statements(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_actions_Statement__statements", None)
        self.__statements = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Block"):
                opp_val = getattr(old_value, "Block", None)
                if opp_val == self:
                    setattr(old_value, "Block", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Block"):
                opp_val = getattr(value, "Block", None)
                setattr(value, "Block", self)

    def getOutermostBlock(self) :
        # TODO: Implement getOutermostBlock method
        pass

    def isSideEffectFree(self) :
        # TODO: Implement isSideEffectFree method
        pass

    def getOwningClass(self) :
        # TODO: Implement getOwningClass method
        pass

    def getNamedValuesInScope(self) :
        # TODO: Implement getNamedValuesInScope method
        pass

    def isSideEffectFreeForBlock(self, behavioral_block) :
        # TODO: Implement isSideEffectFreeForBlock method
        pass

class Variable:

    pass
class StatementWithArgument:

    pass
class behavioral_actions_Return(StatementWithArgument):

    pass
class behavioral_actions_Assignment(StatementWithArgument):

    pass
class behavioral_bpdm_Dummy:

    pass