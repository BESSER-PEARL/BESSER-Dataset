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
class PreconditionKindEnum(Enum):
    ENABLE = "ENABLE"
    REQUIRED = "REQUIRED"
    INHIBIT = "INHIBIT"
    NEUTEAL = "NEUTEAL"
class SAMOperatorKindEnum(Enum):
    OR = "OR"
    AND = "AND"


############################################
# Definition of Classes
############################################

class Strategy:

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
class behavioral_assembly_Strategy(ABC):

    pass
class behavioral_assembly_InhibitingStrategy(Strategy):

    pass
class behavioral_assembly_EnablingStrategy(Strategy):

    pass
class design_AbstractStatusVariable:

    pass
class assembly_Strategy:

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
class design_AbstractStatusValue:

    pass
class behavioral_assembly_StatusValueProxy(assembly_ConnectableElement, design_AbstractStatusValue, design_StatusValue):

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
class behavioral_assembly_ActionProxy(assembly_ConnectableElement, design_Action, design_AbstractAction):

    pass
class design_StatusVariable:

    pass
class behavioral_assembly_StatusVariableProxy(assembly_ConnectableElement, design_AbstractStatusVariable, design_StatusVariable):

    pass
class design_BusinessObjectNode:

    pass
class behavioral_design_BusinessObject:

    pass
class SAMDerivator:

    pass
class behavioral_status_and_action_old_SAMSchemaDerivator:

    pass
class SAMAction:

    pass
class behavioral_status_and_action_old_SAMSchemaAction:

    pass
class SAMStatusVariable:

    pass
class behavioral_status_and_action_old_SAMSchemaValue:

    def __init__(self, isInitial: bool, isInhibiting: bool, SAMSchemaAction123: set["SAMSchemaAction"] = None, SAMSchemaValue126: set["SAMSchemaValue"] = None, SAMSchemaValue129: set["SAMSchemaValue"] = None, SAMOperator132: set["SAMOperator"] = None, SAMSchemaAction135: set["SAMSchemaAction"] = None, SAMSchemaVariable120: "SAMSchemaVariable" = None):
        self.isInitial = isInitial
        self.isInhibiting = isInhibiting
        self.SAMSchemaAction123 = SAMSchemaAction123 if SAMSchemaAction123 is not None else set()
        self.SAMSchemaValue126 = SAMSchemaValue126 if SAMSchemaValue126 is not None else set()
        self.SAMSchemaValue129 = SAMSchemaValue129 if SAMSchemaValue129 is not None else set()
        self.SAMOperator132 = SAMOperator132 if SAMOperator132 is not None else set()
        self.SAMSchemaAction135 = SAMSchemaAction135 if SAMSchemaAction135 is not None else set()
        self.SAMSchemaVariable120 = SAMSchemaVariable120
        
    @property
    def isInhibiting(self) -> bool:
        return self.__isInhibiting

    @isInhibiting.setter
    def isInhibiting(self, isInhibiting: bool):
        self.__isInhibiting = isInhibiting

    @property
    def isInitial(self) -> bool:
        return self.__isInitial

    @isInitial.setter
    def isInitial(self, isInitial: bool):
        self.__isInitial = isInitial

    @property
    def SAMSchemaVariable120(self):
        return self.__SAMSchemaVariable120

    @SAMSchemaVariable120.setter
    def SAMSchemaVariable120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_status_and_action_old_SAMSchemaValue__SAMSchemaVariable120", None)
        self.__SAMSchemaVariable120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "status_and_action_old121"):
                opp_val = getattr(old_value, "status_and_action_old121", None)
                if opp_val == self:
                    setattr(old_value, "status_and_action_old121", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "status_and_action_old121"):
                opp_val = getattr(value, "status_and_action_old121", None)
                setattr(value, "status_and_action_old121", self)

    @property
    def SAMSchemaAction123(self):
        return self.__SAMSchemaAction123

    @SAMSchemaAction123.setter
    def SAMSchemaAction123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_status_and_action_old_SAMSchemaValue__SAMSchemaAction123", None)
        self.__SAMSchemaAction123 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "status_and_action_old124"):
                    opp_val = getattr(item, "status_and_action_old124", None)
                    
                    if opp_val == self:
                        setattr(item, "status_and_action_old124", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "status_and_action_old124"):
                    opp_val = getattr(item, "status_and_action_old124", None)
                    
                    setattr(item, "status_and_action_old124", self)
                    

    @property
    def SAMSchemaValue126(self):
        return self.__SAMSchemaValue126

    @SAMSchemaValue126.setter
    def SAMSchemaValue126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_status_and_action_old_SAMSchemaValue__SAMSchemaValue126", None)
        self.__SAMSchemaValue126 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "status_and_action_old127"):
                    opp_val = getattr(item, "status_and_action_old127", None)
                    
                    if opp_val == self:
                        setattr(item, "status_and_action_old127", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "status_and_action_old127"):
                    opp_val = getattr(item, "status_and_action_old127", None)
                    
                    setattr(item, "status_and_action_old127", self)
                    

    @property
    def SAMSchemaAction135(self):
        return self.__SAMSchemaAction135

    @SAMSchemaAction135.setter
    def SAMSchemaAction135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_status_and_action_old_SAMSchemaValue__SAMSchemaAction135", None)
        self.__SAMSchemaAction135 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "status_and_action_old136"):
                    opp_val = getattr(item, "status_and_action_old136", None)
                    
                    if opp_val == self:
                        setattr(item, "status_and_action_old136", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "status_and_action_old136"):
                    opp_val = getattr(item, "status_and_action_old136", None)
                    
                    setattr(item, "status_and_action_old136", self)
                    

    @property
    def SAMSchemaValue129(self):
        return self.__SAMSchemaValue129

    @SAMSchemaValue129.setter
    def SAMSchemaValue129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_status_and_action_old_SAMSchemaValue__SAMSchemaValue129", None)
        self.__SAMSchemaValue129 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "status_and_action_old130"):
                    opp_val = getattr(item, "status_and_action_old130", None)
                    
                    if opp_val == self:
                        setattr(item, "status_and_action_old130", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "status_and_action_old130"):
                    opp_val = getattr(item, "status_and_action_old130", None)
                    
                    setattr(item, "status_and_action_old130", self)
                    

    @property
    def SAMOperator132(self):
        return self.__SAMOperator132

    @SAMOperator132.setter
    def SAMOperator132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_status_and_action_old_SAMSchemaValue__SAMOperator132", None)
        self.__SAMOperator132 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "status_and_action_old133"):
                    opp_val = getattr(item, "status_and_action_old133", None)
                    
                    if opp_val == self:
                        setattr(item, "status_and_action_old133", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "status_and_action_old133"):
                    opp_val = getattr(item, "status_and_action_old133", None)
                    
                    setattr(item, "status_and_action_old133", self)
                    

class behavioral_status_and_action_old_SAMSchemaVariable:

    def __init__(self, hasStateGuard: bool, SAMStatusSchema105: "SAMStatusSchema" = None, SAMSchemaValue108: set["SAMSchemaValue"] = None, SAMStatusVariable111: "SAMStatusVariable" = None, SAMSchemaDerivator114: set["SAMSchemaDerivator"] = None, SAMSchemaDerivator117: set["SAMSchemaDerivator"] = None):
        self.hasStateGuard = hasStateGuard
        self.SAMStatusSchema105 = SAMStatusSchema105
        self.SAMSchemaValue108 = SAMSchemaValue108 if SAMSchemaValue108 is not None else set()
        self.SAMStatusVariable111 = SAMStatusVariable111
        self.SAMSchemaDerivator114 = SAMSchemaDerivator114 if SAMSchemaDerivator114 is not None else set()
        self.SAMSchemaDerivator117 = SAMSchemaDerivator117 if SAMSchemaDerivator117 is not None else set()
        
    @property
    def hasStateGuard(self) -> bool:
        return self.__hasStateGuard

    @hasStateGuard.setter
    def hasStateGuard(self, hasStateGuard: bool):
        self.__hasStateGuard = hasStateGuard

    @property
    def SAMSchemaValue108(self):
        return self.__SAMSchemaValue108

    @SAMSchemaValue108.setter
    def SAMSchemaValue108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_status_and_action_old_SAMSchemaVariable__SAMSchemaValue108", None)
        self.__SAMSchemaValue108 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "status_and_action_old109"):
                    opp_val = getattr(item, "status_and_action_old109", None)
                    
                    if opp_val == self:
                        setattr(item, "status_and_action_old109", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "status_and_action_old109"):
                    opp_val = getattr(item, "status_and_action_old109", None)
                    
                    setattr(item, "status_and_action_old109", self)
                    

    @property
    def SAMStatusSchema105(self):
        return self.__SAMStatusSchema105

    @SAMStatusSchema105.setter
    def SAMStatusSchema105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_status_and_action_old_SAMSchemaVariable__SAMStatusSchema105", None)
        self.__SAMStatusSchema105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "status_and_action_old106"):
                opp_val = getattr(old_value, "status_and_action_old106", None)
                if opp_val == self:
                    setattr(old_value, "status_and_action_old106", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "status_and_action_old106"):
                opp_val = getattr(value, "status_and_action_old106", None)
                setattr(value, "status_and_action_old106", self)

    @property
    def SAMSchemaDerivator117(self):
        return self.__SAMSchemaDerivator117

    @SAMSchemaDerivator117.setter
    def SAMSchemaDerivator117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_status_and_action_old_SAMSchemaVariable__SAMSchemaDerivator117", None)
        self.__SAMSchemaDerivator117 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "status_and_action_old118"):
                    opp_val = getattr(item, "status_and_action_old118", None)
                    
                    if opp_val == self:
                        setattr(item, "status_and_action_old118", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "status_and_action_old118"):
                    opp_val = getattr(item, "status_and_action_old118", None)
                    
                    setattr(item, "status_and_action_old118", self)
                    

    @property
    def SAMStatusVariable111(self):
        return self.__SAMStatusVariable111

    @SAMStatusVariable111.setter
    def SAMStatusVariable111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_status_and_action_old_SAMSchemaVariable__SAMStatusVariable111", None)
        self.__SAMStatusVariable111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "status_and_action_old112"):
                opp_val = getattr(old_value, "status_and_action_old112", None)
                if opp_val == self:
                    setattr(old_value, "status_and_action_old112", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "status_and_action_old112"):
                opp_val = getattr(value, "status_and_action_old112", None)
                setattr(value, "status_and_action_old112", self)

    @property
    def SAMSchemaDerivator114(self):
        return self.__SAMSchemaDerivator114

    @SAMSchemaDerivator114.setter
    def SAMSchemaDerivator114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_status_and_action_old_SAMSchemaVariable__SAMSchemaDerivator114", None)
        self.__SAMSchemaDerivator114 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "status_and_action_old115"):
                    opp_val = getattr(item, "status_and_action_old115", None)
                    
                    if opp_val == self:
                        setattr(item, "status_and_action_old115", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "status_and_action_old115"):
                    opp_val = getattr(item, "status_and_action_old115", None)
                    
                    setattr(item, "status_and_action_old115", self)
                    

class SAMSchemaValue:

    pass
class SAMStatusSchema:

    pass
class behavioral_status_and_action_old_SAMOperator:

    def __init__(self, kind: str, SAMStatusSchema: "SAMStatusSchema" = None, SAMSchemaValue: set["SAMSchemaValue"] = None, SAMOperator96: set["SAMOperator"] = None, SAMOperator99: set["SAMOperator"] = None, SAMSchemaAction102: set["SAMSchemaAction"] = None):
        self.kind = kind
        self.SAMStatusSchema = SAMStatusSchema
        self.SAMSchemaValue = SAMSchemaValue if SAMSchemaValue is not None else set()
        self.SAMOperator96 = SAMOperator96 if SAMOperator96 is not None else set()
        self.SAMOperator99 = SAMOperator99 if SAMOperator99 is not None else set()
        self.SAMSchemaAction102 = SAMSchemaAction102 if SAMSchemaAction102 is not None else set()
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def SAMOperator99(self):
        return self.__SAMOperator99

    @SAMOperator99.setter
    def SAMOperator99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_status_and_action_old_SAMOperator__SAMOperator99", None)
        self.__SAMOperator99 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "status_and_action_old100"):
                    opp_val = getattr(item, "status_and_action_old100", None)
                    
                    if opp_val == self:
                        setattr(item, "status_and_action_old100", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "status_and_action_old100"):
                    opp_val = getattr(item, "status_and_action_old100", None)
                    
                    setattr(item, "status_and_action_old100", self)
                    

    @property
    def SAMSchemaValue(self):
        return self.__SAMSchemaValue

    @SAMSchemaValue.setter
    def SAMSchemaValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_status_and_action_old_SAMOperator__SAMSchemaValue", None)
        self.__SAMSchemaValue = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "status_and_action_old94"):
                    opp_val = getattr(item, "status_and_action_old94", None)
                    
                    if opp_val == self:
                        setattr(item, "status_and_action_old94", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "status_and_action_old94"):
                    opp_val = getattr(item, "status_and_action_old94", None)
                    
                    setattr(item, "status_and_action_old94", self)
                    

    @property
    def SAMStatusSchema(self):
        return self.__SAMStatusSchema

    @SAMStatusSchema.setter
    def SAMStatusSchema(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_status_and_action_old_SAMOperator__SAMStatusSchema", None)
        self.__SAMStatusSchema = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "status_and_action_old92"):
                opp_val = getattr(old_value, "status_and_action_old92", None)
                if opp_val == self:
                    setattr(old_value, "status_and_action_old92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "status_and_action_old92"):
                opp_val = getattr(value, "status_and_action_old92", None)
                setattr(value, "status_and_action_old92", self)

    @property
    def SAMOperator96(self):
        return self.__SAMOperator96

    @SAMOperator96.setter
    def SAMOperator96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_status_and_action_old_SAMOperator__SAMOperator96", None)
        self.__SAMOperator96 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "status_and_action_old97"):
                    opp_val = getattr(item, "status_and_action_old97", None)
                    
                    if opp_val == self:
                        setattr(item, "status_and_action_old97", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "status_and_action_old97"):
                    opp_val = getattr(item, "status_and_action_old97", None)
                    
                    setattr(item, "status_and_action_old97", self)
                    

    @property
    def SAMSchemaAction102(self):
        return self.__SAMSchemaAction102

    @SAMSchemaAction102.setter
    def SAMSchemaAction102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_status_and_action_old_SAMOperator__SAMSchemaAction102", None)
        self.__SAMSchemaAction102 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "status_and_action_old103"):
                    opp_val = getattr(item, "status_and_action_old103", None)
                    
                    if opp_val == self:
                        setattr(item, "status_and_action_old103", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "status_and_action_old103"):
                    opp_val = getattr(item, "status_and_action_old103", None)
                    
                    setattr(item, "status_and_action_old103", self)
                    

class SAMOperator:

    pass
class behavioral_status_and_action_old_SAMStatusSchema:

    def __init__(self, name: str, SapClass78: "SapClass" = None, SAMOperator: set["SAMOperator"] = None, SAMSchemaVariable83: set["SAMSchemaVariable"] = None, SAMSchemaAction86: set["SAMSchemaAction"] = None, SAMSchemaDerivator89: set["SAMSchemaDerivator"] = None):
        self.name = name
        self.SapClass78 = SapClass78
        self.SAMOperator = SAMOperator if SAMOperator is not None else set()
        self.SAMSchemaVariable83 = SAMSchemaVariable83 if SAMSchemaVariable83 is not None else set()
        self.SAMSchemaAction86 = SAMSchemaAction86 if SAMSchemaAction86 is not None else set()
        self.SAMSchemaDerivator89 = SAMSchemaDerivator89 if SAMSchemaDerivator89 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def SAMSchemaDerivator89(self):
        return self.__SAMSchemaDerivator89

    @SAMSchemaDerivator89.setter
    def SAMSchemaDerivator89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_status_and_action_old_SAMStatusSchema__SAMSchemaDerivator89", None)
        self.__SAMSchemaDerivator89 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "status_and_action_old90"):
                    opp_val = getattr(item, "status_and_action_old90", None)
                    
                    if opp_val == self:
                        setattr(item, "status_and_action_old90", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "status_and_action_old90"):
                    opp_val = getattr(item, "status_and_action_old90", None)
                    
                    setattr(item, "status_and_action_old90", self)
                    

    @property
    def SAMSchemaAction86(self):
        return self.__SAMSchemaAction86

    @SAMSchemaAction86.setter
    def SAMSchemaAction86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_status_and_action_old_SAMStatusSchema__SAMSchemaAction86", None)
        self.__SAMSchemaAction86 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "status_and_action_old87"):
                    opp_val = getattr(item, "status_and_action_old87", None)
                    
                    if opp_val == self:
                        setattr(item, "status_and_action_old87", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "status_and_action_old87"):
                    opp_val = getattr(item, "status_and_action_old87", None)
                    
                    setattr(item, "status_and_action_old87", self)
                    

    @property
    def SapClass78(self):
        return self.__SapClass78

    @SapClass78.setter
    def SapClass78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_status_and_action_old_SAMStatusSchema__SapClass78", None)
        self.__SapClass78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "data.ecoreclasses79"):
                opp_val = getattr(old_value, "data.ecoreclasses79", None)
                if opp_val == self:
                    setattr(old_value, "data.ecoreclasses79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "data.ecoreclasses79"):
                opp_val = getattr(value, "data.ecoreclasses79", None)
                setattr(value, "data.ecoreclasses79", self)

    @property
    def SAMSchemaVariable83(self):
        return self.__SAMSchemaVariable83

    @SAMSchemaVariable83.setter
    def SAMSchemaVariable83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_status_and_action_old_SAMStatusSchema__SAMSchemaVariable83", None)
        self.__SAMSchemaVariable83 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "status_and_action_old84"):
                    opp_val = getattr(item, "status_and_action_old84", None)
                    
                    if opp_val == self:
                        setattr(item, "status_and_action_old84", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "status_and_action_old84"):
                    opp_val = getattr(item, "status_and_action_old84", None)
                    
                    setattr(item, "status_and_action_old84", self)
                    

    @property
    def SAMOperator(self):
        return self.__SAMOperator

    @SAMOperator.setter
    def SAMOperator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_status_and_action_old_SAMStatusSchema__SAMOperator", None)
        self.__SAMOperator = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "status_and_action_old81"):
                    opp_val = getattr(item, "status_and_action_old81", None)
                    
                    if opp_val == self:
                        setattr(item, "status_and_action_old81", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "status_and_action_old81"):
                    opp_val = getattr(item, "status_and_action_old81", None)
                    
                    setattr(item, "status_and_action_old81", self)
                    

class behavioral_events_EventFilter:

    pass
class MethodSignature:

    pass
class behavioral_status_and_action_old_SAMStatusValue:

    def __init__(self, name: str, SAMStatusVariable: "SAMStatusVariable" = None):
        self.name = name
        self.SAMStatusVariable = SAMStatusVariable
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def SAMStatusVariable(self):
        return self.__SAMStatusVariable

    @SAMStatusVariable.setter
    def SAMStatusVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_status_and_action_old_SAMStatusValue__SAMStatusVariable", None)
        self.__SAMStatusVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "status_and_action_old76"):
                opp_val = getattr(old_value, "status_and_action_old76", None)
                if opp_val == self:
                    setattr(old_value, "status_and_action_old76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "status_and_action_old76"):
                opp_val = getattr(value, "status_and_action_old76", None)
                setattr(value, "status_and_action_old76", self)

class SAMSchemaDerivator:

    pass
class behavioral_status_and_action_old_SAMDerivator:

    def __init__(self, kind: str, SapClass71: "SapClass" = None, SAMSchemaDerivator: set["SAMSchemaDerivator"] = None):
        self.kind = kind
        self.SapClass71 = SapClass71
        self.SAMSchemaDerivator = SAMSchemaDerivator if SAMSchemaDerivator is not None else set()
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def SapClass71(self):
        return self.__SapClass71

    @SapClass71.setter
    def SapClass71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_status_and_action_old_SAMDerivator__SapClass71", None)
        self.__SapClass71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "data.ecoreclasses72"):
                opp_val = getattr(old_value, "data.ecoreclasses72", None)
                if opp_val == self:
                    setattr(old_value, "data.ecoreclasses72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "data.ecoreclasses72"):
                opp_val = getattr(value, "data.ecoreclasses72", None)
                setattr(value, "data.ecoreclasses72", self)

    @property
    def SAMSchemaDerivator(self):
        return self.__SAMSchemaDerivator

    @SAMSchemaDerivator.setter
    def SAMSchemaDerivator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_status_and_action_old_SAMDerivator__SAMSchemaDerivator", None)
        self.__SAMSchemaDerivator = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "status_and_action_old74"):
                    opp_val = getattr(item, "status_and_action_old74", None)
                    
                    if opp_val == self:
                        setattr(item, "status_and_action_old74", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "status_and_action_old74"):
                    opp_val = getattr(item, "status_and_action_old74", None)
                    
                    setattr(item, "status_and_action_old74", self)
                    

class SAMSchemaVariable:

    pass
class SAMStatusValue:

    pass
class behavioral_status_and_action_old_SAMStatusVariable:

    def __init__(self, name: str, isAgentVariable: bool, SapClass64: "SapClass" = None, SAMStatusValue: set["SAMStatusValue"] = None, SAMSchemaVariable: set["SAMSchemaVariable"] = None):
        self.name = name
        self.isAgentVariable = isAgentVariable
        self.SapClass64 = SapClass64
        self.SAMStatusValue = SAMStatusValue if SAMStatusValue is not None else set()
        self.SAMSchemaVariable = SAMSchemaVariable if SAMSchemaVariable is not None else set()
        
    @property
    def isAgentVariable(self) -> bool:
        return self.__isAgentVariable

    @isAgentVariable.setter
    def isAgentVariable(self, isAgentVariable: bool):
        self.__isAgentVariable = isAgentVariable

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def SapClass64(self):
        return self.__SapClass64

    @SapClass64.setter
    def SapClass64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_status_and_action_old_SAMStatusVariable__SapClass64", None)
        self.__SapClass64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "data.ecoreclasses65"):
                opp_val = getattr(old_value, "data.ecoreclasses65", None)
                if opp_val == self:
                    setattr(old_value, "data.ecoreclasses65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "data.ecoreclasses65"):
                opp_val = getattr(value, "data.ecoreclasses65", None)
                setattr(value, "data.ecoreclasses65", self)

    @property
    def SAMSchemaVariable(self):
        return self.__SAMSchemaVariable

    @SAMSchemaVariable.setter
    def SAMSchemaVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_status_and_action_old_SAMStatusVariable__SAMSchemaVariable", None)
        self.__SAMSchemaVariable = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "status_and_action_old69"):
                    opp_val = getattr(item, "status_and_action_old69", None)
                    
                    if opp_val == self:
                        setattr(item, "status_and_action_old69", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "status_and_action_old69"):
                    opp_val = getattr(item, "status_and_action_old69", None)
                    
                    setattr(item, "status_and_action_old69", self)
                    

    @property
    def SAMStatusValue(self):
        return self.__SAMStatusValue

    @SAMStatusValue.setter
    def SAMStatusValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_status_and_action_old_SAMStatusVariable__SAMStatusValue", None)
        self.__SAMStatusValue = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "status_and_action_old67"):
                    opp_val = getattr(item, "status_and_action_old67", None)
                    
                    if opp_val == self:
                        setattr(item, "status_and_action_old67", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "status_and_action_old67"):
                    opp_val = getattr(item, "status_and_action_old67", None)
                    
                    setattr(item, "status_and_action_old67", self)
                    

class SAMSchemaAction:

    pass
class behavioral_status_and_action_old_SAMAction:

    def __init__(self, name: str, isAgentAction: bool, SapClass60: "SapClass" = None, SAMSchemaAction: set["SAMSchemaAction"] = None):
        self.name = name
        self.isAgentAction = isAgentAction
        self.SapClass60 = SapClass60
        self.SAMSchemaAction = SAMSchemaAction if SAMSchemaAction is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def isAgentAction(self) -> bool:
        return self.__isAgentAction

    @isAgentAction.setter
    def isAgentAction(self, isAgentAction: bool):
        self.__isAgentAction = isAgentAction

    @property
    def SAMSchemaAction(self):
        return self.__SAMSchemaAction

    @SAMSchemaAction.setter
    def SAMSchemaAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_status_and_action_old_SAMAction__SAMSchemaAction", None)
        self.__SAMSchemaAction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "status_and_action_old"):
                    opp_val = getattr(item, "status_and_action_old", None)
                    
                    if opp_val == self:
                        setattr(item, "status_and_action_old", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "status_and_action_old"):
                    opp_val = getattr(item, "status_and_action_old", None)
                    
                    setattr(item, "status_and_action_old", self)
                    

    @property
    def SapClass60(self):
        return self.__SapClass60

    @SapClass60.setter
    def SapClass60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_status_and_action_old_SAMAction__SapClass60", None)
        self.__SapClass60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "data.ecoreclasses61"):
                opp_val = getattr(old_value, "data.ecoreclasses61", None)
                if opp_val == self:
                    setattr(old_value, "data.ecoreclasses61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "data.ecoreclasses61"):
                opp_val = getattr(value, "data.ecoreclasses61", None)
                setattr(value, "data.ecoreclasses61", self)

class behavioral_transactions_Dummy:

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
class NamedElement:

    pass
class behavioral_design_BusinessObjectNode(NamedElement):

    pass
class behavioral_design_AbstractAction(NamedElement):

    def __init__(self, isAgent: bool, isPreconditionFixed: bool):
        self.isAgent = isAgent
        self.isPreconditionFixed = isPreconditionFixed
        
    @property
    def isAgent(self) -> bool:
        return self.__isAgent

    @isAgent.setter
    def isAgent(self, isAgent: bool):
        self.__isAgent = isAgent

    @property
    def isPreconditionFixed(self) -> bool:
        return self.__isPreconditionFixed

    @isPreconditionFixed.setter
    def isPreconditionFixed(self, isPreconditionFixed: bool):
        self.__isPreconditionFixed = isPreconditionFixed

class behavioral_design_AbstractStatusValue(NamedElement):

    def __init__(self, isInitial: bool, isInhibiting: bool, isStateGuarded: bool):
        self.isInitial = isInitial
        self.isInhibiting = isInhibiting
        self.isStateGuarded = isStateGuarded
        
    @property
    def isInhibiting(self) -> bool:
        return self.__isInhibiting

    @isInhibiting.setter
    def isInhibiting(self, isInhibiting: bool):
        self.__isInhibiting = isInhibiting

    @property
    def isInitial(self) -> bool:
        return self.__isInitial

    @isInitial.setter
    def isInitial(self, isInitial: bool):
        self.__isInitial = isInitial

    @property
    def isStateGuarded(self) -> bool:
        return self.__isStateGuarded

    @isStateGuarded.setter
    def isStateGuarded(self, isStateGuarded: bool):
        self.__isStateGuarded = isStateGuarded

class behavioral_assembly_SchemaElement(NamedElement):

    pass
class behavioral_assembly_StatusSchema(NamedElement):

    pass
class behavioral_design_AbstractStatusVariable(NamedElement):

    def __init__(self, isAgent: bool, isStateGuarded: bool, behavioral_design_AbstractStatusVariable: set["design_AbstractStatusValue"] = None):
        self.isAgent = isAgent
        self.isStateGuarded = isStateGuarded
        self.behavioral_design_AbstractStatusVariable = behavioral_design_AbstractStatusVariable if behavioral_design_AbstractStatusVariable is not None else set()
        
    @property
    def isAgent(self) -> bool:
        return self.__isAgent

    @isAgent.setter
    def isAgent(self, isAgent: bool):
        self.__isAgent = isAgent

    @property
    def isStateGuarded(self) -> bool:
        return self.__isStateGuarded

    @isStateGuarded.setter
    def isStateGuarded(self, isStateGuarded: bool):
        self.__isStateGuarded = isStateGuarded

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
class behavioral_actions_ConditionalStatement(actions_Statement, expressions_Conditional):

    pass
class behavioral_actions_StatementWithArgument(actions_Statement, expressions_WithArgument):

    pass
class NamedValueWithOptionalInitExpression:

    pass
class behavioral_actions_Constant(NamedValueWithOptionalInitExpression):

    pass
class DimensionDefinition:

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
class behavioral_actions_Variable(NamedValueWithOptionalInitExpression):

    def __init__(self, Assignment: set["Assignment"] = None, actions36: "behavioral_actions_NamedValueDeclaration"):
        self.Assignment = Assignment if Assignment is not None else set()
        
    @property
    def Assignment(self):
        return self.__Assignment

    @Assignment.setter
    def Assignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_actions_Variable__Assignment", None)
        self.__Assignment = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "actions20"):
                    opp_val = getattr(item, "actions20", None)
                    
                    if opp_val == self:
                        setattr(item, "actions20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "actions20"):
                    opp_val = getattr(item, "actions20", None)
                    
                    setattr(item, "actions20", self)
                    

    def getCommonTypeOfAssignments(self):
        # TODO: Implement getCommonTypeOfAssignments method
        pass

class collectionexpressions_Iterate:

    pass
class actions_SingleBlockStatement:

    pass
class behavioral_actions_QueryInvocation:

    pass
class behavioral_actions_Sort:

    pass
class Association:

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

    def __init__(self, parallel: bool, behavioral_actions_Foreach: "Expression" = None, Iterator: "Iterator" = None):
        self.parallel = parallel
        self.behavioral_actions_Foreach = behavioral_actions_Foreach
        self.Iterator = Iterator
        
    @property
    def parallel(self) -> bool:
        return self.__parallel

    @parallel.setter
    def parallel(self, parallel: bool):
        self.__parallel = parallel

    @property
    def Iterator(self):
        return self.__Iterator

    @Iterator.setter
    def Iterator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_actions_Foreach__Iterator", None)
        self.__Iterator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "actions10"):
                opp_val = getattr(old_value, "actions10", None)
                if opp_val == self:
                    setattr(old_value, "actions10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "actions10"):
                opp_val = getattr(value, "actions10", None)
                setattr(value, "actions10", self)

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

class actions_StatementWithNestedBlocks:

    pass
class actions_ConditionalStatement:

    pass
class behavioral_actions_WhileLoop(actions_SingleBlockStatement, actions_ConditionalStatement):

    def __init__(self):
        
    def getLoopBody(self) -> str:
        # TODO: Implement getLoopBody method
        pass

class behavioral_actions_IfElse(actions_StatementWithNestedBlocks, actions_ConditionalStatement):

    def __init__(self):
        
    def getIfBlock(self) -> str:
        # TODO: Implement getIfBlock method
        pass

    def getElseBlock(self) -> str:
        # TODO: Implement getElseBlock method
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
class behavioral_actions_LinkManipulationStatement(Statement):

    def __init__(self, at: int, behavioral_actions_LinkManipulationStatement: "Association" = None, behavioral_actions_LinkManipulationStatement13: set["Expression"] = None, actions4: "behavioral_actions_Block"):
        self.at = at
        self.behavioral_actions_LinkManipulationStatement = behavioral_actions_LinkManipulationStatement
        self.behavioral_actions_LinkManipulationStatement13 = behavioral_actions_LinkManipulationStatement13 if behavioral_actions_LinkManipulationStatement13 is not None else set()
        
    @property
    def at(self) -> int:
        return self.__at

    @at.setter
    def at(self, at: int):
        self.__at = at

    @property
    def behavioral_actions_LinkManipulationStatement13(self):
        return self.__behavioral_actions_LinkManipulationStatement13

    @behavioral_actions_LinkManipulationStatement13.setter
    def behavioral_actions_LinkManipulationStatement13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_actions_LinkManipulationStatement__behavioral_actions_LinkManipulationStatement13", None)
        self.__behavioral_actions_LinkManipulationStatement13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Expression14"):
                    opp_val = getattr(item, "Expression14", None)
                    
                    if opp_val == self:
                        setattr(item, "Expression14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Expression14"):
                    opp_val = getattr(item, "Expression14", None)
                    
                    setattr(item, "Expression14", self)
                    

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

class behavioral_actions_ExpressionStatement(Statement):

    pass
class behavioral_actions_StatementWithNestedBlocks(Statement):

    pass
class classes_InScope:

    pass
class classes_FunctionSignatureImplementation:

    pass
class behavioral_actions_Block(classes_FunctionSignatureImplementation, classes_InScope):

    def __init__(self, Statement: set["Statement"] = None, NamedValue: set["NamedValue"] = None, StatementWithNestedBlocks: "StatementWithNestedBlocks" = None):
        self.Statement = Statement if Statement is not None else set()
        self.NamedValue = NamedValue if NamedValue is not None else set()
        self.StatementWithNestedBlocks = StatementWithNestedBlocks
        
    @property
    def StatementWithNestedBlocks(self):
        return self.__StatementWithNestedBlocks

    @StatementWithNestedBlocks.setter
    def StatementWithNestedBlocks(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_actions_Block__StatementWithNestedBlocks", None)
        self.__StatementWithNestedBlocks = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "actions7"):
                opp_val = getattr(old_value, "actions7", None)
                if opp_val == self:
                    setattr(old_value, "actions7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "actions7"):
                opp_val = getattr(value, "actions7", None)
                setattr(value, "actions7", self)

    @property
    def Statement(self):
        return self.__Statement

    @Statement.setter
    def Statement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_actions_Block__Statement", None)
        self.__Statement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "actions4"):
                    opp_val = getattr(item, "actions4", None)
                    
                    if opp_val == self:
                        setattr(item, "actions4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "actions4"):
                    opp_val = getattr(item, "actions4", None)
                    
                    setattr(item, "actions4", self)
                    

    @property
    def NamedValue(self):
        return self.__NamedValue

    @NamedValue.setter
    def NamedValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_actions_Block__NamedValue", None)
        self.__NamedValue = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "data.ecoreclasses"):
                    opp_val = getattr(item, "data.ecoreclasses", None)
                    
                    if opp_val == self:
                        setattr(item, "data.ecoreclasses", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "data.ecoreclasses"):
                    opp_val = getattr(item, "data.ecoreclasses", None)
                    
                    setattr(item, "data.ecoreclasses", self)
                    

    def getOutermostBlock(self) -> str:
        # TODO: Implement getOutermostBlock method
        pass

    def getNamedValuesInScope(self) -> str:
        # TODO: Implement getNamedValuesInScope method
        pass

    def localIsSideEffectFree(self) -> bool:
        # TODO: Implement localIsSideEffectFree method
        pass

    def getOwningClass(self) -> str:
        # TODO: Implement getOwningClass method
        pass

class Block:

    pass
class InScope:

    pass
class behavioral_actions_Statement(InScope):

    def __init__(self, Block: "Block" = None):
        self.Block = Block
        
    @property
    def Block(self):
        return self.__Block

    @Block.setter
    def Block(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behavioral_actions_Statement__Block", None)
        self.__Block = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "actions2"):
                opp_val = getattr(old_value, "actions2", None)
                if opp_val == self:
                    setattr(old_value, "actions2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "actions2"):
                opp_val = getattr(value, "actions2", None)
                setattr(value, "actions2", self)

    def getOwningClass(self) -> str:
        # TODO: Implement getOwningClass method
        pass

    def getOutermostBlock(self) -> str:
        # TODO: Implement getOutermostBlock method
        pass

    def getNamedValuesInScope(self) -> str:
        # TODO: Implement getNamedValuesInScope method
        pass

    def isSideEffectFree(self) -> bool:
        # TODO: Implement isSideEffectFree method
        pass

    def isSideEffectFreeForBlock(self, block: str) -> bool:
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
class behavioral_businesstasks_TaskAgent:

    pass
class behavioral_bpdm_Dummy:

    pass