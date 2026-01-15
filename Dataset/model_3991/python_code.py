from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class TypeType3(Enum):
    STRING = "STRING"
    FLOAT = "FLOAT"
    INTEGER = "INTEGER"
    REFERENCE = "REFERENCE"
    DATETIME = "DATETIME"
    BOOLEAN = "BOOLEAN"
    PERFORMER = "PERFORMER"
class ExecutionType(Enum):
    ASYNCHR = "ASYNCHR"
    SYNCHR = "SYNCHR"
class IsArrayType(Enum):
    TRUE = "TRUE"
    FALSE = "FALSE"
class InstantiationType(Enum):
    ONCE = "ONCE"
    MULTIPLE = "MULTIPLE"
class DurationUnitType(Enum):
    Y = "Y"
    M = "M"
    D = "D"
    h = "h"
    m1 = "m1"
    s = "s"
class TypeType(Enum):
    AND = "AND"
    XOR = "XOR"
class TypeType1(Enum):
    RESOURCESET = "RESOURCESET"
    RESOURCE = "RESOURCE"
    ROLE = "ROLE"
    ORGANIZATIONALUNIT = "ORGANIZATIONALUNIT"
    HUMAN = "HUMAN"
    SYSTEM = "SYSTEM"
class AccessLevelType(Enum):
    PUBLIC = "PUBLIC"
    PRIVATE = "PRIVATE"
class TypeType4(Enum):
    AND = "AND"
    XOR = "XOR"
class GraphConformanceType(Enum):
    FULLBLOCKED = "FULLBLOCKED"
    LOOPBLOCKED = "LOOPBLOCKED"
    NONBLOCKED = "NONBLOCKED"
class ModeType(Enum):
    IN = "IN"
    OUT = "OUT"
    INOUT = "INOUT"
class TypeType2(Enum):
    CONDITION = "CONDITION"
    OTHERWISE = "OTHERWISE"
    EXCEPTION = "EXCEPTION"
    DEFAULTEXCEPTION = "DEFAULTEXCEPTION"
class ExecutionType1(Enum):
    ASYNCHR = "ASYNCHR"
    SYNCHR = "SYNCHR"
class TypeType5(Enum):
    APPLICATION = "APPLICATION"
    PROCEDURE = "PROCEDURE"
class PublicationStatusType(Enum):
    UNDERREVISION = "UNDERREVISION"
    RELEASED = "RELEASED"
    UNDERTEST = "UNDERTEST"


############################################
# Definition of Classes
############################################

class xpdl1_WorkflowProcessesType:

    pass
class xpdl1_WorkflowProcessType:

    def __init__(self, accessLevel: str, id: str, name: str, xpdl1_WorkflowProcessType: "xpdl1_DocumentRoot" = None, xpdl1_WorkflowProcessType475: "xpdl1_WorkflowProcessesType" = None, xpdl1_WorkflowProcessType477: "xpdl1_ProcessHeaderType" = None, xpdl1_WorkflowProcessType480: "xpdl1_RedefinableHeaderType" = None, xpdl1_WorkflowProcessType483: "xpdl1_FormalParametersType" = None, xpdl1_WorkflowProcessType486: "xpdl1_DataFieldsType" = None, xpdl1_WorkflowProcessType489: "xpdl1_ParticipantsType" = None, xpdl1_WorkflowProcessType492: "xpdl1_ApplicationsType" = None, xpdl1_WorkflowProcessType498: "xpdl1_ActivitiesType" = None, xpdl1_WorkflowProcessType501: "xpdl1_TransitionsType" = None, xpdl1_WorkflowProcessType504: "xpdl1_ExtendedAttributesType" = None, xpdl1_WorkflowProcessType495: "xpdl1_ActivitySetsType" = None):
        self.accessLevel = accessLevel
        self.id = id
        self.name = name
        self.xpdl1_WorkflowProcessType = xpdl1_WorkflowProcessType
        self.xpdl1_WorkflowProcessType475 = xpdl1_WorkflowProcessType475
        self.xpdl1_WorkflowProcessType477 = xpdl1_WorkflowProcessType477
        self.xpdl1_WorkflowProcessType480 = xpdl1_WorkflowProcessType480
        self.xpdl1_WorkflowProcessType483 = xpdl1_WorkflowProcessType483
        self.xpdl1_WorkflowProcessType486 = xpdl1_WorkflowProcessType486
        self.xpdl1_WorkflowProcessType489 = xpdl1_WorkflowProcessType489
        self.xpdl1_WorkflowProcessType492 = xpdl1_WorkflowProcessType492
        self.xpdl1_WorkflowProcessType498 = xpdl1_WorkflowProcessType498
        self.xpdl1_WorkflowProcessType501 = xpdl1_WorkflowProcessType501
        self.xpdl1_WorkflowProcessType504 = xpdl1_WorkflowProcessType504
        self.xpdl1_WorkflowProcessType495 = xpdl1_WorkflowProcessType495
        
    @property
    def accessLevel(self) -> str:
        return self.__accessLevel

    @accessLevel.setter
    def accessLevel(self, accessLevel: str):
        self.__accessLevel = accessLevel

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
    def xpdl1_WorkflowProcessType483(self):
        return self.__xpdl1_WorkflowProcessType483

    @xpdl1_WorkflowProcessType483.setter
    def xpdl1_WorkflowProcessType483(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_WorkflowProcessType__xpdl1_WorkflowProcessType483", None)
        self.__xpdl1_WorkflowProcessType483 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_FormalParametersType484"):
                opp_val = getattr(old_value, "xpdl1_FormalParametersType484", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_FormalParametersType484", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_FormalParametersType484"):
                opp_val = getattr(value, "xpdl1_FormalParametersType484", None)
                setattr(value, "xpdl1_FormalParametersType484", self)

    @property
    def xpdl1_WorkflowProcessType480(self):
        return self.__xpdl1_WorkflowProcessType480

    @xpdl1_WorkflowProcessType480.setter
    def xpdl1_WorkflowProcessType480(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_WorkflowProcessType__xpdl1_WorkflowProcessType480", None)
        self.__xpdl1_WorkflowProcessType480 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_RedefinableHeaderType481"):
                opp_val = getattr(old_value, "xpdl1_RedefinableHeaderType481", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_RedefinableHeaderType481", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_RedefinableHeaderType481"):
                opp_val = getattr(value, "xpdl1_RedefinableHeaderType481", None)
                setattr(value, "xpdl1_RedefinableHeaderType481", self)

    @property
    def xpdl1_WorkflowProcessType504(self):
        return self.__xpdl1_WorkflowProcessType504

    @xpdl1_WorkflowProcessType504.setter
    def xpdl1_WorkflowProcessType504(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_WorkflowProcessType__xpdl1_WorkflowProcessType504", None)
        self.__xpdl1_WorkflowProcessType504 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_ExtendedAttributesType505"):
                opp_val = getattr(old_value, "xpdl1_ExtendedAttributesType505", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_ExtendedAttributesType505", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_ExtendedAttributesType505"):
                opp_val = getattr(value, "xpdl1_ExtendedAttributesType505", None)
                setattr(value, "xpdl1_ExtendedAttributesType505", self)

    @property
    def xpdl1_WorkflowProcessType486(self):
        return self.__xpdl1_WorkflowProcessType486

    @xpdl1_WorkflowProcessType486.setter
    def xpdl1_WorkflowProcessType486(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_WorkflowProcessType__xpdl1_WorkflowProcessType486", None)
        self.__xpdl1_WorkflowProcessType486 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_DataFieldsType487"):
                opp_val = getattr(old_value, "xpdl1_DataFieldsType487", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_DataFieldsType487", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_DataFieldsType487"):
                opp_val = getattr(value, "xpdl1_DataFieldsType487", None)
                setattr(value, "xpdl1_DataFieldsType487", self)

    @property
    def xpdl1_WorkflowProcessType501(self):
        return self.__xpdl1_WorkflowProcessType501

    @xpdl1_WorkflowProcessType501.setter
    def xpdl1_WorkflowProcessType501(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_WorkflowProcessType__xpdl1_WorkflowProcessType501", None)
        self.__xpdl1_WorkflowProcessType501 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_TransitionsType502"):
                opp_val = getattr(old_value, "xpdl1_TransitionsType502", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_TransitionsType502", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_TransitionsType502"):
                opp_val = getattr(value, "xpdl1_TransitionsType502", None)
                setattr(value, "xpdl1_TransitionsType502", self)

    @property
    def xpdl1_WorkflowProcessType475(self):
        return self.__xpdl1_WorkflowProcessType475

    @xpdl1_WorkflowProcessType475.setter
    def xpdl1_WorkflowProcessType475(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_WorkflowProcessType__xpdl1_WorkflowProcessType475", None)
        self.__xpdl1_WorkflowProcessType475 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_WorkflowProcessesType474"):
                opp_val = getattr(old_value, "xpdl1_WorkflowProcessesType474", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_WorkflowProcessesType474"):
                opp_val = getattr(value, "xpdl1_WorkflowProcessesType474", None)
                if opp_val is None:
                    setattr(value, "xpdl1_WorkflowProcessesType474", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xpdl1_WorkflowProcessType492(self):
        return self.__xpdl1_WorkflowProcessType492

    @xpdl1_WorkflowProcessType492.setter
    def xpdl1_WorkflowProcessType492(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_WorkflowProcessType__xpdl1_WorkflowProcessType492", None)
        self.__xpdl1_WorkflowProcessType492 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_ApplicationsType493"):
                opp_val = getattr(old_value, "xpdl1_ApplicationsType493", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_ApplicationsType493", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_ApplicationsType493"):
                opp_val = getattr(value, "xpdl1_ApplicationsType493", None)
                setattr(value, "xpdl1_ApplicationsType493", self)

    @property
    def xpdl1_WorkflowProcessType495(self):
        return self.__xpdl1_WorkflowProcessType495

    @xpdl1_WorkflowProcessType495.setter
    def xpdl1_WorkflowProcessType495(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_WorkflowProcessType__xpdl1_WorkflowProcessType495", None)
        self.__xpdl1_WorkflowProcessType495 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_ActivitySetsType496"):
                opp_val = getattr(old_value, "xpdl1_ActivitySetsType496", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_ActivitySetsType496", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_ActivitySetsType496"):
                opp_val = getattr(value, "xpdl1_ActivitySetsType496", None)
                setattr(value, "xpdl1_ActivitySetsType496", self)

    @property
    def xpdl1_WorkflowProcessType489(self):
        return self.__xpdl1_WorkflowProcessType489

    @xpdl1_WorkflowProcessType489.setter
    def xpdl1_WorkflowProcessType489(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_WorkflowProcessType__xpdl1_WorkflowProcessType489", None)
        self.__xpdl1_WorkflowProcessType489 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_ParticipantsType490"):
                opp_val = getattr(old_value, "xpdl1_ParticipantsType490", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_ParticipantsType490", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_ParticipantsType490"):
                opp_val = getattr(value, "xpdl1_ParticipantsType490", None)
                setattr(value, "xpdl1_ParticipantsType490", self)

    @property
    def xpdl1_WorkflowProcessType477(self):
        return self.__xpdl1_WorkflowProcessType477

    @xpdl1_WorkflowProcessType477.setter
    def xpdl1_WorkflowProcessType477(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_WorkflowProcessType__xpdl1_WorkflowProcessType477", None)
        self.__xpdl1_WorkflowProcessType477 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_ProcessHeaderType478"):
                opp_val = getattr(old_value, "xpdl1_ProcessHeaderType478", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_ProcessHeaderType478", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_ProcessHeaderType478"):
                opp_val = getattr(value, "xpdl1_ProcessHeaderType478", None)
                setattr(value, "xpdl1_ProcessHeaderType478", self)

    @property
    def xpdl1_WorkflowProcessType(self):
        return self.__xpdl1_WorkflowProcessType

    @xpdl1_WorkflowProcessType.setter
    def xpdl1_WorkflowProcessType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_WorkflowProcessType__xpdl1_WorkflowProcessType", None)
        self.__xpdl1_WorkflowProcessType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_DocumentRoot248"):
                opp_val = getattr(old_value, "xpdl1_DocumentRoot248", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_DocumentRoot248"):
                opp_val = getattr(value, "xpdl1_DocumentRoot248", None)
                if opp_val is None:
                    setattr(value, "xpdl1_DocumentRoot248", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xpdl1_WorkflowProcessType498(self):
        return self.__xpdl1_WorkflowProcessType498

    @xpdl1_WorkflowProcessType498.setter
    def xpdl1_WorkflowProcessType498(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_WorkflowProcessType__xpdl1_WorkflowProcessType498", None)
        self.__xpdl1_WorkflowProcessType498 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_ActivitiesType499"):
                opp_val = getattr(old_value, "xpdl1_ActivitiesType499", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_ActivitiesType499", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_ActivitiesType499"):
                opp_val = getattr(value, "xpdl1_ActivitiesType499", None)
                setattr(value, "xpdl1_ActivitiesType499", self)

class xpdl1_TypeDeclarationType:

    def __init__(self, description: str, id: str, name: str, xpdl1_TypeDeclarationType: "xpdl1_DocumentRoot" = None, xpdl1_TypeDeclarationType439: "xpdl1_TypeDeclarationsType" = None, xpdl1_TypeDeclarationType441: "xpdl1_BasicTypeType" = None, xpdl1_TypeDeclarationType444: "xpdl1_DeclaredTypeType" = None, xpdl1_TypeDeclarationType447: "xpdl1_SchemaTypeType" = None, xpdl1_TypeDeclarationType453: "xpdl1_RecordTypeType" = None, xpdl1_TypeDeclarationType456: "xpdl1_UnionTypeType" = None, xpdl1_TypeDeclarationType459: "xpdl1_EnumerationTypeType" = None, xpdl1_TypeDeclarationType462: "xpdl1_ArrayTypeType" = None, xpdl1_TypeDeclarationType465: "xpdl1_ListTypeType" = None, xpdl1_TypeDeclarationType450: "xpdl1_ExternalReferenceType" = None, xpdl1_TypeDeclarationType468: "xpdl1_ExtendedAttributesType" = None):
        self.description = description
        self.id = id
        self.name = name
        self.xpdl1_TypeDeclarationType = xpdl1_TypeDeclarationType
        self.xpdl1_TypeDeclarationType439 = xpdl1_TypeDeclarationType439
        self.xpdl1_TypeDeclarationType441 = xpdl1_TypeDeclarationType441
        self.xpdl1_TypeDeclarationType444 = xpdl1_TypeDeclarationType444
        self.xpdl1_TypeDeclarationType447 = xpdl1_TypeDeclarationType447
        self.xpdl1_TypeDeclarationType453 = xpdl1_TypeDeclarationType453
        self.xpdl1_TypeDeclarationType456 = xpdl1_TypeDeclarationType456
        self.xpdl1_TypeDeclarationType459 = xpdl1_TypeDeclarationType459
        self.xpdl1_TypeDeclarationType462 = xpdl1_TypeDeclarationType462
        self.xpdl1_TypeDeclarationType465 = xpdl1_TypeDeclarationType465
        self.xpdl1_TypeDeclarationType450 = xpdl1_TypeDeclarationType450
        self.xpdl1_TypeDeclarationType468 = xpdl1_TypeDeclarationType468
        
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
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def xpdl1_TypeDeclarationType439(self):
        return self.__xpdl1_TypeDeclarationType439

    @xpdl1_TypeDeclarationType439.setter
    def xpdl1_TypeDeclarationType439(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_TypeDeclarationType__xpdl1_TypeDeclarationType439", None)
        self.__xpdl1_TypeDeclarationType439 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_TypeDeclarationsType438"):
                opp_val = getattr(old_value, "xpdl1_TypeDeclarationsType438", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_TypeDeclarationsType438"):
                opp_val = getattr(value, "xpdl1_TypeDeclarationsType438", None)
                if opp_val is None:
                    setattr(value, "xpdl1_TypeDeclarationsType438", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xpdl1_TypeDeclarationType450(self):
        return self.__xpdl1_TypeDeclarationType450

    @xpdl1_TypeDeclarationType450.setter
    def xpdl1_TypeDeclarationType450(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_TypeDeclarationType__xpdl1_TypeDeclarationType450", None)
        self.__xpdl1_TypeDeclarationType450 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_ExternalReferenceType451"):
                opp_val = getattr(old_value, "xpdl1_ExternalReferenceType451", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_ExternalReferenceType451", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_ExternalReferenceType451"):
                opp_val = getattr(value, "xpdl1_ExternalReferenceType451", None)
                setattr(value, "xpdl1_ExternalReferenceType451", self)

    @property
    def xpdl1_TypeDeclarationType441(self):
        return self.__xpdl1_TypeDeclarationType441

    @xpdl1_TypeDeclarationType441.setter
    def xpdl1_TypeDeclarationType441(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_TypeDeclarationType__xpdl1_TypeDeclarationType441", None)
        self.__xpdl1_TypeDeclarationType441 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_BasicTypeType442"):
                opp_val = getattr(old_value, "xpdl1_BasicTypeType442", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_BasicTypeType442", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_BasicTypeType442"):
                opp_val = getattr(value, "xpdl1_BasicTypeType442", None)
                setattr(value, "xpdl1_BasicTypeType442", self)

    @property
    def xpdl1_TypeDeclarationType462(self):
        return self.__xpdl1_TypeDeclarationType462

    @xpdl1_TypeDeclarationType462.setter
    def xpdl1_TypeDeclarationType462(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_TypeDeclarationType__xpdl1_TypeDeclarationType462", None)
        self.__xpdl1_TypeDeclarationType462 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_ArrayTypeType463"):
                opp_val = getattr(old_value, "xpdl1_ArrayTypeType463", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_ArrayTypeType463", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_ArrayTypeType463"):
                opp_val = getattr(value, "xpdl1_ArrayTypeType463", None)
                setattr(value, "xpdl1_ArrayTypeType463", self)

    @property
    def xpdl1_TypeDeclarationType456(self):
        return self.__xpdl1_TypeDeclarationType456

    @xpdl1_TypeDeclarationType456.setter
    def xpdl1_TypeDeclarationType456(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_TypeDeclarationType__xpdl1_TypeDeclarationType456", None)
        self.__xpdl1_TypeDeclarationType456 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_UnionTypeType457"):
                opp_val = getattr(old_value, "xpdl1_UnionTypeType457", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_UnionTypeType457", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_UnionTypeType457"):
                opp_val = getattr(value, "xpdl1_UnionTypeType457", None)
                setattr(value, "xpdl1_UnionTypeType457", self)

    @property
    def xpdl1_TypeDeclarationType444(self):
        return self.__xpdl1_TypeDeclarationType444

    @xpdl1_TypeDeclarationType444.setter
    def xpdl1_TypeDeclarationType444(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_TypeDeclarationType__xpdl1_TypeDeclarationType444", None)
        self.__xpdl1_TypeDeclarationType444 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_DeclaredTypeType445"):
                opp_val = getattr(old_value, "xpdl1_DeclaredTypeType445", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_DeclaredTypeType445", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_DeclaredTypeType445"):
                opp_val = getattr(value, "xpdl1_DeclaredTypeType445", None)
                setattr(value, "xpdl1_DeclaredTypeType445", self)

    @property
    def xpdl1_TypeDeclarationType465(self):
        return self.__xpdl1_TypeDeclarationType465

    @xpdl1_TypeDeclarationType465.setter
    def xpdl1_TypeDeclarationType465(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_TypeDeclarationType__xpdl1_TypeDeclarationType465", None)
        self.__xpdl1_TypeDeclarationType465 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_ListTypeType466"):
                opp_val = getattr(old_value, "xpdl1_ListTypeType466", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_ListTypeType466", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_ListTypeType466"):
                opp_val = getattr(value, "xpdl1_ListTypeType466", None)
                setattr(value, "xpdl1_ListTypeType466", self)

    @property
    def xpdl1_TypeDeclarationType459(self):
        return self.__xpdl1_TypeDeclarationType459

    @xpdl1_TypeDeclarationType459.setter
    def xpdl1_TypeDeclarationType459(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_TypeDeclarationType__xpdl1_TypeDeclarationType459", None)
        self.__xpdl1_TypeDeclarationType459 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_EnumerationTypeType460"):
                opp_val = getattr(old_value, "xpdl1_EnumerationTypeType460", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_EnumerationTypeType460", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_EnumerationTypeType460"):
                opp_val = getattr(value, "xpdl1_EnumerationTypeType460", None)
                setattr(value, "xpdl1_EnumerationTypeType460", self)

    @property
    def xpdl1_TypeDeclarationType468(self):
        return self.__xpdl1_TypeDeclarationType468

    @xpdl1_TypeDeclarationType468.setter
    def xpdl1_TypeDeclarationType468(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_TypeDeclarationType__xpdl1_TypeDeclarationType468", None)
        self.__xpdl1_TypeDeclarationType468 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_ExtendedAttributesType469"):
                opp_val = getattr(old_value, "xpdl1_ExtendedAttributesType469", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_ExtendedAttributesType469", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_ExtendedAttributesType469"):
                opp_val = getattr(value, "xpdl1_ExtendedAttributesType469", None)
                setattr(value, "xpdl1_ExtendedAttributesType469", self)

    @property
    def xpdl1_TypeDeclarationType453(self):
        return self.__xpdl1_TypeDeclarationType453

    @xpdl1_TypeDeclarationType453.setter
    def xpdl1_TypeDeclarationType453(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_TypeDeclarationType__xpdl1_TypeDeclarationType453", None)
        self.__xpdl1_TypeDeclarationType453 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_RecordTypeType454"):
                opp_val = getattr(old_value, "xpdl1_RecordTypeType454", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_RecordTypeType454", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_RecordTypeType454"):
                opp_val = getattr(value, "xpdl1_RecordTypeType454", None)
                setattr(value, "xpdl1_RecordTypeType454", self)

    @property
    def xpdl1_TypeDeclarationType447(self):
        return self.__xpdl1_TypeDeclarationType447

    @xpdl1_TypeDeclarationType447.setter
    def xpdl1_TypeDeclarationType447(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_TypeDeclarationType__xpdl1_TypeDeclarationType447", None)
        self.__xpdl1_TypeDeclarationType447 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_SchemaTypeType448"):
                opp_val = getattr(old_value, "xpdl1_SchemaTypeType448", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_SchemaTypeType448", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_SchemaTypeType448"):
                opp_val = getattr(value, "xpdl1_SchemaTypeType448", None)
                setattr(value, "xpdl1_SchemaTypeType448", self)

    @property
    def xpdl1_TypeDeclarationType(self):
        return self.__xpdl1_TypeDeclarationType

    @xpdl1_TypeDeclarationType.setter
    def xpdl1_TypeDeclarationType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_TypeDeclarationType__xpdl1_TypeDeclarationType", None)
        self.__xpdl1_TypeDeclarationType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_DocumentRoot241"):
                opp_val = getattr(old_value, "xpdl1_DocumentRoot241", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_DocumentRoot241"):
                opp_val = getattr(value, "xpdl1_DocumentRoot241", None)
                if opp_val is None:
                    setattr(value, "xpdl1_DocumentRoot241", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xpdl1_TypeDeclarationsType:

    pass
class xpdl1_TransitionRestrictionType:

    pass
class xpdl1_TimeEstimationType:

    def __init__(self, waitingTime: str, workingTime: str, duration: str, xpdl1_TimeEstimationType: "xpdl1_DocumentRoot" = None, xpdl1_TimeEstimationType388: "xpdl1_ProcessHeaderType" = None, xpdl1_TimeEstimationType397: "xpdl1_SimulationInformationType" = None):
        self.waitingTime = waitingTime
        self.workingTime = workingTime
        self.duration = duration
        self.xpdl1_TimeEstimationType = xpdl1_TimeEstimationType
        self.xpdl1_TimeEstimationType388 = xpdl1_TimeEstimationType388
        self.xpdl1_TimeEstimationType397 = xpdl1_TimeEstimationType397
        
    @property
    def workingTime(self) -> str:
        return self.__workingTime

    @workingTime.setter
    def workingTime(self, workingTime: str):
        self.__workingTime = workingTime

    @property
    def waitingTime(self) -> str:
        return self.__waitingTime

    @waitingTime.setter
    def waitingTime(self, waitingTime: str):
        self.__waitingTime = waitingTime

    @property
    def duration(self) -> str:
        return self.__duration

    @duration.setter
    def duration(self, duration: str):
        self.__duration = duration

    @property
    def xpdl1_TimeEstimationType388(self):
        return self.__xpdl1_TimeEstimationType388

    @xpdl1_TimeEstimationType388.setter
    def xpdl1_TimeEstimationType388(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_TimeEstimationType__xpdl1_TimeEstimationType388", None)
        self.__xpdl1_TimeEstimationType388 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_ProcessHeaderType387"):
                opp_val = getattr(old_value, "xpdl1_ProcessHeaderType387", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_ProcessHeaderType387", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_ProcessHeaderType387"):
                opp_val = getattr(value, "xpdl1_ProcessHeaderType387", None)
                setattr(value, "xpdl1_ProcessHeaderType387", self)

    @property
    def xpdl1_TimeEstimationType(self):
        return self.__xpdl1_TimeEstimationType

    @xpdl1_TimeEstimationType.setter
    def xpdl1_TimeEstimationType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_TimeEstimationType__xpdl1_TimeEstimationType", None)
        self.__xpdl1_TimeEstimationType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_DocumentRoot223"):
                opp_val = getattr(old_value, "xpdl1_DocumentRoot223", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_DocumentRoot223"):
                opp_val = getattr(value, "xpdl1_DocumentRoot223", None)
                if opp_val is None:
                    setattr(value, "xpdl1_DocumentRoot223", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xpdl1_TimeEstimationType397(self):
        return self.__xpdl1_TimeEstimationType397

    @xpdl1_TimeEstimationType397.setter
    def xpdl1_TimeEstimationType397(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_TimeEstimationType__xpdl1_TimeEstimationType397", None)
        self.__xpdl1_TimeEstimationType397 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_SimulationInformationType396"):
                opp_val = getattr(old_value, "xpdl1_SimulationInformationType396", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_SimulationInformationType396", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_SimulationInformationType396"):
                opp_val = getattr(value, "xpdl1_SimulationInformationType396", None)
                setattr(value, "xpdl1_SimulationInformationType396", self)

class xpdl1_TransitionRefsType:

    pass
class xpdl1_TransitionRefType:

    def __init__(self, id: str, xpdl1_TransitionRefType: "xpdl1_DocumentRoot" = None, xpdl1_TransitionRefType418: "xpdl1_TransitionRefsType" = None):
        self.id = id
        self.xpdl1_TransitionRefType = xpdl1_TransitionRefType
        self.xpdl1_TransitionRefType418 = xpdl1_TransitionRefType418
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def xpdl1_TransitionRefType(self):
        return self.__xpdl1_TransitionRefType

    @xpdl1_TransitionRefType.setter
    def xpdl1_TransitionRefType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_TransitionRefType__xpdl1_TransitionRefType", None)
        self.__xpdl1_TransitionRefType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_DocumentRoot229"):
                opp_val = getattr(old_value, "xpdl1_DocumentRoot229", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_DocumentRoot229"):
                opp_val = getattr(value, "xpdl1_DocumentRoot229", None)
                if opp_val is None:
                    setattr(value, "xpdl1_DocumentRoot229", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xpdl1_TransitionRefType418(self):
        return self.__xpdl1_TransitionRefType418

    @xpdl1_TransitionRefType418.setter
    def xpdl1_TransitionRefType418(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_TransitionRefType__xpdl1_TransitionRefType418", None)
        self.__xpdl1_TransitionRefType418 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_TransitionRefsType417"):
                opp_val = getattr(old_value, "xpdl1_TransitionRefsType417", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_TransitionRefsType417"):
                opp_val = getattr(value, "xpdl1_TransitionRefsType417", None)
                if opp_val is None:
                    setattr(value, "xpdl1_TransitionRefsType417", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xpdl1_TransitionType:

    def __init__(self, description: str, name: str, to: str, from: str, id: str, xpdl1_TransitionType: "xpdl1_DocumentRoot" = None, xpdl1_TransitionType430: "xpdl1_TransitionsType" = None, xpdl1_TransitionType432: "xpdl1_ConditionType" = None, xpdl1_TransitionType435: "xpdl1_ExtendedAttributesType" = None):
        self.description = description
        self.name = name
        self.to = to
        self.from = from
        self.id = id
        self.xpdl1_TransitionType = xpdl1_TransitionType
        self.xpdl1_TransitionType430 = xpdl1_TransitionType430
        self.xpdl1_TransitionType432 = xpdl1_TransitionType432
        self.xpdl1_TransitionType435 = xpdl1_TransitionType435
        
    @property
    def from(self) -> str:
        return self.__from

    @from.setter
    def from(self, from: str):
        self.__from = from

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def to(self) -> str:
        return self.__to

    @to.setter
    def to(self, to: str):
        self.__to = to

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def xpdl1_TransitionType430(self):
        return self.__xpdl1_TransitionType430

    @xpdl1_TransitionType430.setter
    def xpdl1_TransitionType430(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_TransitionType__xpdl1_TransitionType430", None)
        self.__xpdl1_TransitionType430 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_TransitionsType429"):
                opp_val = getattr(old_value, "xpdl1_TransitionsType429", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_TransitionsType429"):
                opp_val = getattr(value, "xpdl1_TransitionsType429", None)
                if opp_val is None:
                    setattr(value, "xpdl1_TransitionsType429", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xpdl1_TransitionType(self):
        return self.__xpdl1_TransitionType

    @xpdl1_TransitionType.setter
    def xpdl1_TransitionType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_TransitionType__xpdl1_TransitionType", None)
        self.__xpdl1_TransitionType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_DocumentRoot227"):
                opp_val = getattr(old_value, "xpdl1_DocumentRoot227", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_DocumentRoot227"):
                opp_val = getattr(value, "xpdl1_DocumentRoot227", None)
                if opp_val is None:
                    setattr(value, "xpdl1_DocumentRoot227", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xpdl1_TransitionType432(self):
        return self.__xpdl1_TransitionType432

    @xpdl1_TransitionType432.setter
    def xpdl1_TransitionType432(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_TransitionType__xpdl1_TransitionType432", None)
        self.__xpdl1_TransitionType432 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_ConditionType433"):
                opp_val = getattr(old_value, "xpdl1_ConditionType433", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_ConditionType433", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_ConditionType433"):
                opp_val = getattr(value, "xpdl1_ConditionType433", None)
                setattr(value, "xpdl1_ConditionType433", self)

    @property
    def xpdl1_TransitionType435(self):
        return self.__xpdl1_TransitionType435

    @xpdl1_TransitionType435.setter
    def xpdl1_TransitionType435(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_TransitionType__xpdl1_TransitionType435", None)
        self.__xpdl1_TransitionType435 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_ExtendedAttributesType436"):
                opp_val = getattr(old_value, "xpdl1_ExtendedAttributesType436", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_ExtendedAttributesType436", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_ExtendedAttributesType436"):
                opp_val = getattr(value, "xpdl1_ExtendedAttributesType436", None)
                setattr(value, "xpdl1_ExtendedAttributesType436", self)

class xpdl1_ToolType:

    def __init__(self, id: str, type: str, description: str, xpdl1_ToolType: "xpdl1_DocumentRoot" = None, xpdl1_ToolType283: "xpdl1_ImplementationType" = None, xpdl1_ToolType414: "xpdl1_ExtendedAttributesType" = None, xpdl1_ToolType411: "xpdl1_ActualParametersType" = None):
        self.id = id
        self.type = type
        self.description = description
        self.xpdl1_ToolType = xpdl1_ToolType
        self.xpdl1_ToolType283 = xpdl1_ToolType283
        self.xpdl1_ToolType414 = xpdl1_ToolType414
        self.xpdl1_ToolType411 = xpdl1_ToolType411
        
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
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def xpdl1_ToolType283(self):
        return self.__xpdl1_ToolType283

    @xpdl1_ToolType283.setter
    def xpdl1_ToolType283(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ToolType__xpdl1_ToolType283", None)
        self.__xpdl1_ToolType283 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_ImplementationType282"):
                opp_val = getattr(old_value, "xpdl1_ImplementationType282", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_ImplementationType282"):
                opp_val = getattr(value, "xpdl1_ImplementationType282", None)
                if opp_val is None:
                    setattr(value, "xpdl1_ImplementationType282", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xpdl1_ToolType(self):
        return self.__xpdl1_ToolType

    @xpdl1_ToolType.setter
    def xpdl1_ToolType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ToolType__xpdl1_ToolType", None)
        self.__xpdl1_ToolType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_DocumentRoot225"):
                opp_val = getattr(old_value, "xpdl1_DocumentRoot225", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_DocumentRoot225"):
                opp_val = getattr(value, "xpdl1_DocumentRoot225", None)
                if opp_val is None:
                    setattr(value, "xpdl1_DocumentRoot225", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xpdl1_ToolType411(self):
        return self.__xpdl1_ToolType411

    @xpdl1_ToolType411.setter
    def xpdl1_ToolType411(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ToolType__xpdl1_ToolType411", None)
        self.__xpdl1_ToolType411 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_ActualParametersType412"):
                opp_val = getattr(old_value, "xpdl1_ActualParametersType412", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_ActualParametersType412", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_ActualParametersType412"):
                opp_val = getattr(value, "xpdl1_ActualParametersType412", None)
                setattr(value, "xpdl1_ActualParametersType412", self)

    @property
    def xpdl1_ToolType414(self):
        return self.__xpdl1_ToolType414

    @xpdl1_ToolType414.setter
    def xpdl1_ToolType414(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ToolType__xpdl1_ToolType414", None)
        self.__xpdl1_ToolType414 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_ExtendedAttributesType415"):
                opp_val = getattr(old_value, "xpdl1_ExtendedAttributesType415", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_ExtendedAttributesType415", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_ExtendedAttributesType415"):
                opp_val = getattr(value, "xpdl1_ExtendedAttributesType415", None)
                setattr(value, "xpdl1_ExtendedAttributesType415", self)

class xpdl1_ScriptType:

    def __init__(self, grammar: str, type: str, version: str, xpdl1_ScriptType: "xpdl1_DocumentRoot" = None, xpdl1_ScriptType352: "xpdl1_PackageType" = None):
        self.grammar = grammar
        self.type = type
        self.version = version
        self.xpdl1_ScriptType = xpdl1_ScriptType
        self.xpdl1_ScriptType352 = xpdl1_ScriptType352
        
    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def grammar(self) -> str:
        return self.__grammar

    @grammar.setter
    def grammar(self, grammar: str):
        self.__grammar = grammar

    @property
    def xpdl1_ScriptType(self):
        return self.__xpdl1_ScriptType

    @xpdl1_ScriptType.setter
    def xpdl1_ScriptType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ScriptType__xpdl1_ScriptType", None)
        self.__xpdl1_ScriptType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_DocumentRoot211"):
                opp_val = getattr(old_value, "xpdl1_DocumentRoot211", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_DocumentRoot211"):
                opp_val = getattr(value, "xpdl1_DocumentRoot211", None)
                if opp_val is None:
                    setattr(value, "xpdl1_DocumentRoot211", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xpdl1_ScriptType352(self):
        return self.__xpdl1_ScriptType352

    @xpdl1_ScriptType352.setter
    def xpdl1_ScriptType352(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ScriptType__xpdl1_ScriptType352", None)
        self.__xpdl1_ScriptType352 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_PackageType351"):
                opp_val = getattr(old_value, "xpdl1_PackageType351", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_PackageType351", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_PackageType351"):
                opp_val = getattr(value, "xpdl1_PackageType351", None)
                setattr(value, "xpdl1_PackageType351", self)

class xpdl1_SubFlowType:

    def __init__(self, execution: str, id: str, xpdl1_SubFlowType: "xpdl1_DocumentRoot" = None, xpdl1_SubFlowType286: "xpdl1_ImplementationType" = None, xpdl1_SubFlowType408: "xpdl1_ActualParametersType" = None):
        self.execution = execution
        self.id = id
        self.xpdl1_SubFlowType = xpdl1_SubFlowType
        self.xpdl1_SubFlowType286 = xpdl1_SubFlowType286
        self.xpdl1_SubFlowType408 = xpdl1_SubFlowType408
        
    @property
    def execution(self) -> str:
        return self.__execution

    @execution.setter
    def execution(self, execution: str):
        self.__execution = execution

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def xpdl1_SubFlowType408(self):
        return self.__xpdl1_SubFlowType408

    @xpdl1_SubFlowType408.setter
    def xpdl1_SubFlowType408(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_SubFlowType__xpdl1_SubFlowType408", None)
        self.__xpdl1_SubFlowType408 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_ActualParametersType409"):
                opp_val = getattr(old_value, "xpdl1_ActualParametersType409", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_ActualParametersType409", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_ActualParametersType409"):
                opp_val = getattr(value, "xpdl1_ActualParametersType409", None)
                setattr(value, "xpdl1_ActualParametersType409", self)

    @property
    def xpdl1_SubFlowType(self):
        return self.__xpdl1_SubFlowType

    @xpdl1_SubFlowType.setter
    def xpdl1_SubFlowType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_SubFlowType__xpdl1_SubFlowType", None)
        self.__xpdl1_SubFlowType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_DocumentRoot221"):
                opp_val = getattr(old_value, "xpdl1_DocumentRoot221", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_DocumentRoot221"):
                opp_val = getattr(value, "xpdl1_DocumentRoot221", None)
                if opp_val is None:
                    setattr(value, "xpdl1_DocumentRoot221", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xpdl1_SubFlowType286(self):
        return self.__xpdl1_SubFlowType286

    @xpdl1_SubFlowType286.setter
    def xpdl1_SubFlowType286(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_SubFlowType__xpdl1_SubFlowType286", None)
        self.__xpdl1_SubFlowType286 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_ImplementationType285"):
                opp_val = getattr(old_value, "xpdl1_ImplementationType285", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_ImplementationType285", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_ImplementationType285"):
                opp_val = getattr(value, "xpdl1_ImplementationType285", None)
                setattr(value, "xpdl1_ImplementationType285", self)

class xpdl1_SplitType:

    def __init__(self, type: str, xpdl1_SplitType: "xpdl1_DocumentRoot" = None, xpdl1_SplitType399: "xpdl1_TransitionRefsType" = None, xpdl1_SplitType427: "xpdl1_TransitionRestrictionType" = None):
        self.type = type
        self.xpdl1_SplitType = xpdl1_SplitType
        self.xpdl1_SplitType399 = xpdl1_SplitType399
        self.xpdl1_SplitType427 = xpdl1_SplitType427
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def xpdl1_SplitType399(self):
        return self.__xpdl1_SplitType399

    @xpdl1_SplitType399.setter
    def xpdl1_SplitType399(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_SplitType__xpdl1_SplitType399", None)
        self.__xpdl1_SplitType399 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_TransitionRefsType400"):
                opp_val = getattr(old_value, "xpdl1_TransitionRefsType400", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_TransitionRefsType400", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_TransitionRefsType400"):
                opp_val = getattr(value, "xpdl1_TransitionRefsType400", None)
                setattr(value, "xpdl1_TransitionRefsType400", self)

    @property
    def xpdl1_SplitType(self):
        return self.__xpdl1_SplitType

    @xpdl1_SplitType.setter
    def xpdl1_SplitType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_SplitType__xpdl1_SplitType", None)
        self.__xpdl1_SplitType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_DocumentRoot216"):
                opp_val = getattr(old_value, "xpdl1_DocumentRoot216", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_DocumentRoot216"):
                opp_val = getattr(value, "xpdl1_DocumentRoot216", None)
                if opp_val is None:
                    setattr(value, "xpdl1_DocumentRoot216", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xpdl1_SplitType427(self):
        return self.__xpdl1_SplitType427

    @xpdl1_SplitType427.setter
    def xpdl1_SplitType427(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_SplitType__xpdl1_SplitType427", None)
        self.__xpdl1_SplitType427 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_TransitionRestrictionType426"):
                opp_val = getattr(old_value, "xpdl1_TransitionRestrictionType426", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_TransitionRestrictionType426", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_TransitionRestrictionType426"):
                opp_val = getattr(value, "xpdl1_TransitionRestrictionType426", None)
                setattr(value, "xpdl1_TransitionRestrictionType426", self)

class xpdl1_RedefinableHeaderType:

    def __init__(self, author: str, version: str, publicationStatus: str, codepage: str, countrykey: str, xpdl1_RedefinableHeaderType: "xpdl1_DocumentRoot" = None, xpdl1_RedefinableHeaderType346: "xpdl1_PackageType" = None, xpdl1_RedefinableHeaderType393: "xpdl1_ResponsiblesType" = None, xpdl1_RedefinableHeaderType481: "xpdl1_WorkflowProcessType" = None):
        self.author = author
        self.version = version
        self.publicationStatus = publicationStatus
        self.codepage = codepage
        self.countrykey = countrykey
        self.xpdl1_RedefinableHeaderType = xpdl1_RedefinableHeaderType
        self.xpdl1_RedefinableHeaderType346 = xpdl1_RedefinableHeaderType346
        self.xpdl1_RedefinableHeaderType393 = xpdl1_RedefinableHeaderType393
        self.xpdl1_RedefinableHeaderType481 = xpdl1_RedefinableHeaderType481
        
    @property
    def publicationStatus(self) -> str:
        return self.__publicationStatus

    @publicationStatus.setter
    def publicationStatus(self, publicationStatus: str):
        self.__publicationStatus = publicationStatus

    @property
    def codepage(self) -> str:
        return self.__codepage

    @codepage.setter
    def codepage(self, codepage: str):
        self.__codepage = codepage

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def countrykey(self) -> str:
        return self.__countrykey

    @countrykey.setter
    def countrykey(self, countrykey: str):
        self.__countrykey = countrykey

    @property
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author

    @property
    def xpdl1_RedefinableHeaderType393(self):
        return self.__xpdl1_RedefinableHeaderType393

    @xpdl1_RedefinableHeaderType393.setter
    def xpdl1_RedefinableHeaderType393(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_RedefinableHeaderType__xpdl1_RedefinableHeaderType393", None)
        self.__xpdl1_RedefinableHeaderType393 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_ResponsiblesType394"):
                opp_val = getattr(old_value, "xpdl1_ResponsiblesType394", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_ResponsiblesType394", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_ResponsiblesType394"):
                opp_val = getattr(value, "xpdl1_ResponsiblesType394", None)
                setattr(value, "xpdl1_ResponsiblesType394", self)

    @property
    def xpdl1_RedefinableHeaderType481(self):
        return self.__xpdl1_RedefinableHeaderType481

    @xpdl1_RedefinableHeaderType481.setter
    def xpdl1_RedefinableHeaderType481(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_RedefinableHeaderType__xpdl1_RedefinableHeaderType481", None)
        self.__xpdl1_RedefinableHeaderType481 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_WorkflowProcessType480"):
                opp_val = getattr(old_value, "xpdl1_WorkflowProcessType480", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_WorkflowProcessType480", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_WorkflowProcessType480"):
                opp_val = getattr(value, "xpdl1_WorkflowProcessType480", None)
                setattr(value, "xpdl1_WorkflowProcessType480", self)

    @property
    def xpdl1_RedefinableHeaderType(self):
        return self.__xpdl1_RedefinableHeaderType

    @xpdl1_RedefinableHeaderType.setter
    def xpdl1_RedefinableHeaderType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_RedefinableHeaderType__xpdl1_RedefinableHeaderType", None)
        self.__xpdl1_RedefinableHeaderType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_DocumentRoot201"):
                opp_val = getattr(old_value, "xpdl1_DocumentRoot201", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_DocumentRoot201"):
                opp_val = getattr(value, "xpdl1_DocumentRoot201", None)
                if opp_val is None:
                    setattr(value, "xpdl1_DocumentRoot201", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xpdl1_RedefinableHeaderType346(self):
        return self.__xpdl1_RedefinableHeaderType346

    @xpdl1_RedefinableHeaderType346.setter
    def xpdl1_RedefinableHeaderType346(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_RedefinableHeaderType__xpdl1_RedefinableHeaderType346", None)
        self.__xpdl1_RedefinableHeaderType346 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_PackageType345"):
                opp_val = getattr(old_value, "xpdl1_PackageType345", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_PackageType345", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_PackageType345"):
                opp_val = getattr(value, "xpdl1_PackageType345", None)
                setattr(value, "xpdl1_PackageType345", self)

class xpdl1_ResponsiblesType:

    def __init__(self, responsible: str, xpdl1_ResponsiblesType: "xpdl1_DocumentRoot" = None, xpdl1_ResponsiblesType394: "xpdl1_RedefinableHeaderType" = None):
        self.responsible = responsible
        self.xpdl1_ResponsiblesType = xpdl1_ResponsiblesType
        self.xpdl1_ResponsiblesType394 = xpdl1_ResponsiblesType394
        
    @property
    def responsible(self) -> str:
        return self.__responsible

    @responsible.setter
    def responsible(self, responsible: str):
        self.__responsible = responsible

    @property
    def xpdl1_ResponsiblesType394(self):
        return self.__xpdl1_ResponsiblesType394

    @xpdl1_ResponsiblesType394.setter
    def xpdl1_ResponsiblesType394(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ResponsiblesType__xpdl1_ResponsiblesType394", None)
        self.__xpdl1_ResponsiblesType394 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_RedefinableHeaderType393"):
                opp_val = getattr(old_value, "xpdl1_RedefinableHeaderType393", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_RedefinableHeaderType393", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_RedefinableHeaderType393"):
                opp_val = getattr(value, "xpdl1_RedefinableHeaderType393", None)
                setattr(value, "xpdl1_RedefinableHeaderType393", self)

    @property
    def xpdl1_ResponsiblesType(self):
        return self.__xpdl1_ResponsiblesType

    @xpdl1_ResponsiblesType.setter
    def xpdl1_ResponsiblesType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ResponsiblesType__xpdl1_ResponsiblesType", None)
        self.__xpdl1_ResponsiblesType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_DocumentRoot203"):
                opp_val = getattr(old_value, "xpdl1_DocumentRoot203", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_DocumentRoot203"):
                opp_val = getattr(value, "xpdl1_DocumentRoot203", None)
                if opp_val is None:
                    setattr(value, "xpdl1_DocumentRoot203", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xpdl1_ParticipantTypeType:

    def __init__(self, type: str, xpdl1_ParticipantTypeType: "xpdl1_DocumentRoot" = None, xpdl1_ParticipantTypeType379: "xpdl1_ParticipantType" = None):
        self.type = type
        self.xpdl1_ParticipantTypeType = xpdl1_ParticipantTypeType
        self.xpdl1_ParticipantTypeType379 = xpdl1_ParticipantTypeType379
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def xpdl1_ParticipantTypeType(self):
        return self.__xpdl1_ParticipantTypeType

    @xpdl1_ParticipantTypeType.setter
    def xpdl1_ParticipantTypeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ParticipantTypeType__xpdl1_ParticipantTypeType", None)
        self.__xpdl1_ParticipantTypeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_DocumentRoot194"):
                opp_val = getattr(old_value, "xpdl1_DocumentRoot194", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_DocumentRoot194"):
                opp_val = getattr(value, "xpdl1_DocumentRoot194", None)
                if opp_val is None:
                    setattr(value, "xpdl1_DocumentRoot194", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xpdl1_ParticipantTypeType379(self):
        return self.__xpdl1_ParticipantTypeType379

    @xpdl1_ParticipantTypeType379.setter
    def xpdl1_ParticipantTypeType379(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ParticipantTypeType__xpdl1_ParticipantTypeType379", None)
        self.__xpdl1_ParticipantTypeType379 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_ParticipantType378"):
                opp_val = getattr(old_value, "xpdl1_ParticipantType378", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_ParticipantType378", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_ParticipantType378"):
                opp_val = getattr(value, "xpdl1_ParticipantType378", None)
                setattr(value, "xpdl1_ParticipantType378", self)

class xpdl1_ParticipantsType:

    pass
class xpdl1_ProcessHeaderType:

    def __init__(self, created: str, description: str, priority: str, limit: str, validFrom: str, validTo: str, durationUnit: str, xpdl1_ProcessHeaderType: "xpdl1_DocumentRoot" = None, xpdl1_ProcessHeaderType387: "xpdl1_TimeEstimationType" = None, xpdl1_ProcessHeaderType478: "xpdl1_WorkflowProcessType" = None):
        self.created = created
        self.description = description
        self.priority = priority
        self.limit = limit
        self.validFrom = validFrom
        self.validTo = validTo
        self.durationUnit = durationUnit
        self.xpdl1_ProcessHeaderType = xpdl1_ProcessHeaderType
        self.xpdl1_ProcessHeaderType387 = xpdl1_ProcessHeaderType387
        self.xpdl1_ProcessHeaderType478 = xpdl1_ProcessHeaderType478
        
    @property
    def validFrom(self) -> str:
        return self.__validFrom

    @validFrom.setter
    def validFrom(self, validFrom: str):
        self.__validFrom = validFrom

    @property
    def priority(self) -> str:
        return self.__priority

    @priority.setter
    def priority(self, priority: str):
        self.__priority = priority

    @property
    def validTo(self) -> str:
        return self.__validTo

    @validTo.setter
    def validTo(self, validTo: str):
        self.__validTo = validTo

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def durationUnit(self) -> str:
        return self.__durationUnit

    @durationUnit.setter
    def durationUnit(self, durationUnit: str):
        self.__durationUnit = durationUnit

    @property
    def limit(self) -> str:
        return self.__limit

    @limit.setter
    def limit(self, limit: str):
        self.__limit = limit

    @property
    def created(self) -> str:
        return self.__created

    @created.setter
    def created(self, created: str):
        self.__created = created

    @property
    def xpdl1_ProcessHeaderType(self):
        return self.__xpdl1_ProcessHeaderType

    @xpdl1_ProcessHeaderType.setter
    def xpdl1_ProcessHeaderType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ProcessHeaderType__xpdl1_ProcessHeaderType", None)
        self.__xpdl1_ProcessHeaderType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_DocumentRoot196"):
                opp_val = getattr(old_value, "xpdl1_DocumentRoot196", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_DocumentRoot196"):
                opp_val = getattr(value, "xpdl1_DocumentRoot196", None)
                if opp_val is None:
                    setattr(value, "xpdl1_DocumentRoot196", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xpdl1_ProcessHeaderType478(self):
        return self.__xpdl1_ProcessHeaderType478

    @xpdl1_ProcessHeaderType478.setter
    def xpdl1_ProcessHeaderType478(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ProcessHeaderType__xpdl1_ProcessHeaderType478", None)
        self.__xpdl1_ProcessHeaderType478 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_WorkflowProcessType477"):
                opp_val = getattr(old_value, "xpdl1_WorkflowProcessType477", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_WorkflowProcessType477", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_WorkflowProcessType477"):
                opp_val = getattr(value, "xpdl1_WorkflowProcessType477", None)
                setattr(value, "xpdl1_WorkflowProcessType477", self)

    @property
    def xpdl1_ProcessHeaderType387(self):
        return self.__xpdl1_ProcessHeaderType387

    @xpdl1_ProcessHeaderType387.setter
    def xpdl1_ProcessHeaderType387(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ProcessHeaderType__xpdl1_ProcessHeaderType387", None)
        self.__xpdl1_ProcessHeaderType387 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_TimeEstimationType388"):
                opp_val = getattr(old_value, "xpdl1_TimeEstimationType388", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_TimeEstimationType388", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_TimeEstimationType388"):
                opp_val = getattr(value, "xpdl1_TimeEstimationType388", None)
                setattr(value, "xpdl1_TimeEstimationType388", self)

class xpdl1_PackageType:

    def __init__(self, id: str, name: str, xpdl1_PackageType: "xpdl1_DocumentRoot" = None, xpdl1_PackageType342: "xpdl1_PackageHeaderType" = None, xpdl1_PackageType345: "xpdl1_RedefinableHeaderType" = None, xpdl1_PackageType348: "xpdl1_ConformanceClassType" = None, xpdl1_PackageType351: "xpdl1_ScriptType" = None, xpdl1_PackageType354: "xpdl1_ExternalPackagesType" = None, xpdl1_PackageType357: "xpdl1_TypeDeclarationsType" = None, xpdl1_PackageType360: "xpdl1_ParticipantsType" = None, xpdl1_PackageType363: "xpdl1_ApplicationsType" = None, xpdl1_PackageType366: "xpdl1_DataFieldsType" = None, xpdl1_PackageType369: "xpdl1_WorkflowProcessesType" = None, xpdl1_PackageType372: "xpdl1_ExtendedAttributesType" = None):
        self.id = id
        self.name = name
        self.xpdl1_PackageType = xpdl1_PackageType
        self.xpdl1_PackageType342 = xpdl1_PackageType342
        self.xpdl1_PackageType345 = xpdl1_PackageType345
        self.xpdl1_PackageType348 = xpdl1_PackageType348
        self.xpdl1_PackageType351 = xpdl1_PackageType351
        self.xpdl1_PackageType354 = xpdl1_PackageType354
        self.xpdl1_PackageType357 = xpdl1_PackageType357
        self.xpdl1_PackageType360 = xpdl1_PackageType360
        self.xpdl1_PackageType363 = xpdl1_PackageType363
        self.xpdl1_PackageType366 = xpdl1_PackageType366
        self.xpdl1_PackageType369 = xpdl1_PackageType369
        self.xpdl1_PackageType372 = xpdl1_PackageType372
        
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
    def xpdl1_PackageType351(self):
        return self.__xpdl1_PackageType351

    @xpdl1_PackageType351.setter
    def xpdl1_PackageType351(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_PackageType__xpdl1_PackageType351", None)
        self.__xpdl1_PackageType351 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_ScriptType352"):
                opp_val = getattr(old_value, "xpdl1_ScriptType352", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_ScriptType352", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_ScriptType352"):
                opp_val = getattr(value, "xpdl1_ScriptType352", None)
                setattr(value, "xpdl1_ScriptType352", self)

    @property
    def xpdl1_PackageType(self):
        return self.__xpdl1_PackageType

    @xpdl1_PackageType.setter
    def xpdl1_PackageType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_PackageType__xpdl1_PackageType", None)
        self.__xpdl1_PackageType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_DocumentRoot186"):
                opp_val = getattr(old_value, "xpdl1_DocumentRoot186", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_DocumentRoot186"):
                opp_val = getattr(value, "xpdl1_DocumentRoot186", None)
                if opp_val is None:
                    setattr(value, "xpdl1_DocumentRoot186", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xpdl1_PackageType354(self):
        return self.__xpdl1_PackageType354

    @xpdl1_PackageType354.setter
    def xpdl1_PackageType354(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_PackageType__xpdl1_PackageType354", None)
        self.__xpdl1_PackageType354 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_ExternalPackagesType355"):
                opp_val = getattr(old_value, "xpdl1_ExternalPackagesType355", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_ExternalPackagesType355", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_ExternalPackagesType355"):
                opp_val = getattr(value, "xpdl1_ExternalPackagesType355", None)
                setattr(value, "xpdl1_ExternalPackagesType355", self)

    @property
    def xpdl1_PackageType348(self):
        return self.__xpdl1_PackageType348

    @xpdl1_PackageType348.setter
    def xpdl1_PackageType348(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_PackageType__xpdl1_PackageType348", None)
        self.__xpdl1_PackageType348 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_ConformanceClassType349"):
                opp_val = getattr(old_value, "xpdl1_ConformanceClassType349", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_ConformanceClassType349", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_ConformanceClassType349"):
                opp_val = getattr(value, "xpdl1_ConformanceClassType349", None)
                setattr(value, "xpdl1_ConformanceClassType349", self)

    @property
    def xpdl1_PackageType372(self):
        return self.__xpdl1_PackageType372

    @xpdl1_PackageType372.setter
    def xpdl1_PackageType372(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_PackageType__xpdl1_PackageType372", None)
        self.__xpdl1_PackageType372 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_ExtendedAttributesType373"):
                opp_val = getattr(old_value, "xpdl1_ExtendedAttributesType373", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_ExtendedAttributesType373", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_ExtendedAttributesType373"):
                opp_val = getattr(value, "xpdl1_ExtendedAttributesType373", None)
                setattr(value, "xpdl1_ExtendedAttributesType373", self)

    @property
    def xpdl1_PackageType366(self):
        return self.__xpdl1_PackageType366

    @xpdl1_PackageType366.setter
    def xpdl1_PackageType366(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_PackageType__xpdl1_PackageType366", None)
        self.__xpdl1_PackageType366 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_DataFieldsType367"):
                opp_val = getattr(old_value, "xpdl1_DataFieldsType367", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_DataFieldsType367", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_DataFieldsType367"):
                opp_val = getattr(value, "xpdl1_DataFieldsType367", None)
                setattr(value, "xpdl1_DataFieldsType367", self)

    @property
    def xpdl1_PackageType342(self):
        return self.__xpdl1_PackageType342

    @xpdl1_PackageType342.setter
    def xpdl1_PackageType342(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_PackageType__xpdl1_PackageType342", None)
        self.__xpdl1_PackageType342 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_PackageHeaderType343"):
                opp_val = getattr(old_value, "xpdl1_PackageHeaderType343", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_PackageHeaderType343", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_PackageHeaderType343"):
                opp_val = getattr(value, "xpdl1_PackageHeaderType343", None)
                setattr(value, "xpdl1_PackageHeaderType343", self)

    @property
    def xpdl1_PackageType360(self):
        return self.__xpdl1_PackageType360

    @xpdl1_PackageType360.setter
    def xpdl1_PackageType360(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_PackageType__xpdl1_PackageType360", None)
        self.__xpdl1_PackageType360 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_ParticipantsType361"):
                opp_val = getattr(old_value, "xpdl1_ParticipantsType361", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_ParticipantsType361", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_ParticipantsType361"):
                opp_val = getattr(value, "xpdl1_ParticipantsType361", None)
                setattr(value, "xpdl1_ParticipantsType361", self)

    @property
    def xpdl1_PackageType357(self):
        return self.__xpdl1_PackageType357

    @xpdl1_PackageType357.setter
    def xpdl1_PackageType357(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_PackageType__xpdl1_PackageType357", None)
        self.__xpdl1_PackageType357 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_TypeDeclarationsType358"):
                opp_val = getattr(old_value, "xpdl1_TypeDeclarationsType358", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_TypeDeclarationsType358", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_TypeDeclarationsType358"):
                opp_val = getattr(value, "xpdl1_TypeDeclarationsType358", None)
                setattr(value, "xpdl1_TypeDeclarationsType358", self)

    @property
    def xpdl1_PackageType363(self):
        return self.__xpdl1_PackageType363

    @xpdl1_PackageType363.setter
    def xpdl1_PackageType363(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_PackageType__xpdl1_PackageType363", None)
        self.__xpdl1_PackageType363 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_ApplicationsType364"):
                opp_val = getattr(old_value, "xpdl1_ApplicationsType364", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_ApplicationsType364", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_ApplicationsType364"):
                opp_val = getattr(value, "xpdl1_ApplicationsType364", None)
                setattr(value, "xpdl1_ApplicationsType364", self)

    @property
    def xpdl1_PackageType369(self):
        return self.__xpdl1_PackageType369

    @xpdl1_PackageType369.setter
    def xpdl1_PackageType369(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_PackageType__xpdl1_PackageType369", None)
        self.__xpdl1_PackageType369 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_WorkflowProcessesType370"):
                opp_val = getattr(old_value, "xpdl1_WorkflowProcessesType370", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_WorkflowProcessesType370", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_WorkflowProcessesType370"):
                opp_val = getattr(value, "xpdl1_WorkflowProcessesType370", None)
                setattr(value, "xpdl1_WorkflowProcessesType370", self)

    @property
    def xpdl1_PackageType345(self):
        return self.__xpdl1_PackageType345

    @xpdl1_PackageType345.setter
    def xpdl1_PackageType345(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_PackageType__xpdl1_PackageType345", None)
        self.__xpdl1_PackageType345 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_RedefinableHeaderType346"):
                opp_val = getattr(old_value, "xpdl1_RedefinableHeaderType346", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_RedefinableHeaderType346", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_RedefinableHeaderType346"):
                opp_val = getattr(value, "xpdl1_RedefinableHeaderType346", None)
                setattr(value, "xpdl1_RedefinableHeaderType346", self)

class xpdl1_NoType:

    pass
class xpdl1_MemberType:

    pass
class xpdl1_ParticipantType:

    def __init__(self, description: str, id: str, name: str, xpdl1_ParticipantType: "xpdl1_DocumentRoot" = None, xpdl1_ParticipantType376: "xpdl1_ParticipantsType" = None, xpdl1_ParticipantType378: "xpdl1_ParticipantTypeType" = None, xpdl1_ParticipantType381: "xpdl1_ExternalReferenceType" = None, xpdl1_ParticipantType384: "xpdl1_ExtendedAttributesType" = None):
        self.description = description
        self.id = id
        self.name = name
        self.xpdl1_ParticipantType = xpdl1_ParticipantType
        self.xpdl1_ParticipantType376 = xpdl1_ParticipantType376
        self.xpdl1_ParticipantType378 = xpdl1_ParticipantType378
        self.xpdl1_ParticipantType381 = xpdl1_ParticipantType381
        self.xpdl1_ParticipantType384 = xpdl1_ParticipantType384
        
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
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def xpdl1_ParticipantType(self):
        return self.__xpdl1_ParticipantType

    @xpdl1_ParticipantType.setter
    def xpdl1_ParticipantType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ParticipantType__xpdl1_ParticipantType", None)
        self.__xpdl1_ParticipantType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_DocumentRoot190"):
                opp_val = getattr(old_value, "xpdl1_DocumentRoot190", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_DocumentRoot190"):
                opp_val = getattr(value, "xpdl1_DocumentRoot190", None)
                if opp_val is None:
                    setattr(value, "xpdl1_DocumentRoot190", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xpdl1_ParticipantType378(self):
        return self.__xpdl1_ParticipantType378

    @xpdl1_ParticipantType378.setter
    def xpdl1_ParticipantType378(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ParticipantType__xpdl1_ParticipantType378", None)
        self.__xpdl1_ParticipantType378 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_ParticipantTypeType379"):
                opp_val = getattr(old_value, "xpdl1_ParticipantTypeType379", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_ParticipantTypeType379", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_ParticipantTypeType379"):
                opp_val = getattr(value, "xpdl1_ParticipantTypeType379", None)
                setattr(value, "xpdl1_ParticipantTypeType379", self)

    @property
    def xpdl1_ParticipantType381(self):
        return self.__xpdl1_ParticipantType381

    @xpdl1_ParticipantType381.setter
    def xpdl1_ParticipantType381(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ParticipantType__xpdl1_ParticipantType381", None)
        self.__xpdl1_ParticipantType381 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_ExternalReferenceType382"):
                opp_val = getattr(old_value, "xpdl1_ExternalReferenceType382", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_ExternalReferenceType382", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_ExternalReferenceType382"):
                opp_val = getattr(value, "xpdl1_ExternalReferenceType382", None)
                setattr(value, "xpdl1_ExternalReferenceType382", self)

    @property
    def xpdl1_ParticipantType376(self):
        return self.__xpdl1_ParticipantType376

    @xpdl1_ParticipantType376.setter
    def xpdl1_ParticipantType376(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ParticipantType__xpdl1_ParticipantType376", None)
        self.__xpdl1_ParticipantType376 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_ParticipantsType375"):
                opp_val = getattr(old_value, "xpdl1_ParticipantsType375", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_ParticipantsType375"):
                opp_val = getattr(value, "xpdl1_ParticipantsType375", None)
                if opp_val is None:
                    setattr(value, "xpdl1_ParticipantsType375", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xpdl1_ParticipantType384(self):
        return self.__xpdl1_ParticipantType384

    @xpdl1_ParticipantType384.setter
    def xpdl1_ParticipantType384(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ParticipantType__xpdl1_ParticipantType384", None)
        self.__xpdl1_ParticipantType384 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_ExtendedAttributesType385"):
                opp_val = getattr(old_value, "xpdl1_ExtendedAttributesType385", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_ExtendedAttributesType385", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_ExtendedAttributesType385"):
                opp_val = getattr(value, "xpdl1_ExtendedAttributesType385", None)
                setattr(value, "xpdl1_ExtendedAttributesType385", self)

class xpdl1_PackageHeaderType:

    def __init__(self, vendor: str, created: str, description: str, documentation: str, priorityUnit: str, costUnit: str, xPDLVersion: str, xpdl1_PackageHeaderType: "xpdl1_DocumentRoot" = None, xpdl1_PackageHeaderType343: "xpdl1_PackageType" = None):
        self.vendor = vendor
        self.created = created
        self.description = description
        self.documentation = documentation
        self.priorityUnit = priorityUnit
        self.costUnit = costUnit
        self.xPDLVersion = xPDLVersion
        self.xpdl1_PackageHeaderType = xpdl1_PackageHeaderType
        self.xpdl1_PackageHeaderType343 = xpdl1_PackageHeaderType343
        
    @property
    def created(self) -> str:
        return self.__created

    @created.setter
    def created(self, created: str):
        self.__created = created

    @property
    def xPDLVersion(self) -> str:
        return self.__xPDLVersion

    @xPDLVersion.setter
    def xPDLVersion(self, xPDLVersion: str):
        self.__xPDLVersion = xPDLVersion

    @property
    def vendor(self) -> str:
        return self.__vendor

    @vendor.setter
    def vendor(self, vendor: str):
        self.__vendor = vendor

    @property
    def priorityUnit(self) -> str:
        return self.__priorityUnit

    @priorityUnit.setter
    def priorityUnit(self, priorityUnit: str):
        self.__priorityUnit = priorityUnit

    @property
    def costUnit(self) -> str:
        return self.__costUnit

    @costUnit.setter
    def costUnit(self, costUnit: str):
        self.__costUnit = costUnit

    @property
    def documentation(self) -> str:
        return self.__documentation

    @documentation.setter
    def documentation(self, documentation: str):
        self.__documentation = documentation

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def xpdl1_PackageHeaderType343(self):
        return self.__xpdl1_PackageHeaderType343

    @xpdl1_PackageHeaderType343.setter
    def xpdl1_PackageHeaderType343(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_PackageHeaderType__xpdl1_PackageHeaderType343", None)
        self.__xpdl1_PackageHeaderType343 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_PackageType342"):
                opp_val = getattr(old_value, "xpdl1_PackageType342", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_PackageType342", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_PackageType342"):
                opp_val = getattr(value, "xpdl1_PackageType342", None)
                setattr(value, "xpdl1_PackageType342", self)

    @property
    def xpdl1_PackageHeaderType(self):
        return self.__xpdl1_PackageHeaderType

    @xpdl1_PackageHeaderType.setter
    def xpdl1_PackageHeaderType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_PackageHeaderType__xpdl1_PackageHeaderType", None)
        self.__xpdl1_PackageHeaderType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_DocumentRoot188"):
                opp_val = getattr(old_value, "xpdl1_DocumentRoot188", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_DocumentRoot188"):
                opp_val = getattr(value, "xpdl1_DocumentRoot188", None)
                if opp_val is None:
                    setattr(value, "xpdl1_DocumentRoot188", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xpdl1_JoinType:

    def __init__(self, type: str, xpdl1_JoinType: "xpdl1_DocumentRoot" = None, xpdl1_JoinType424: "xpdl1_TransitionRestrictionType" = None):
        self.type = type
        self.xpdl1_JoinType = xpdl1_JoinType
        self.xpdl1_JoinType424 = xpdl1_JoinType424
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def xpdl1_JoinType424(self):
        return self.__xpdl1_JoinType424

    @xpdl1_JoinType424.setter
    def xpdl1_JoinType424(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_JoinType__xpdl1_JoinType424", None)
        self.__xpdl1_JoinType424 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_TransitionRestrictionType423"):
                opp_val = getattr(old_value, "xpdl1_TransitionRestrictionType423", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_TransitionRestrictionType423", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_TransitionRestrictionType423"):
                opp_val = getattr(value, "xpdl1_TransitionRestrictionType423", None)
                setattr(value, "xpdl1_TransitionRestrictionType423", self)

    @property
    def xpdl1_JoinType(self):
        return self.__xpdl1_JoinType

    @xpdl1_JoinType.setter
    def xpdl1_JoinType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_JoinType__xpdl1_JoinType", None)
        self.__xpdl1_JoinType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_DocumentRoot175"):
                opp_val = getattr(old_value, "xpdl1_DocumentRoot175", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_DocumentRoot175"):
                opp_val = getattr(value, "xpdl1_DocumentRoot175", None)
                if opp_val is None:
                    setattr(value, "xpdl1_DocumentRoot175", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xpdl1_ManualType:

    pass
class xpdl1_FormalParameterType:

    def __init__(self, description: str, id: str, index: str, mode: str, xpdl1_FormalParameterType: "xpdl1_DocumentRoot" = None, xpdl1_FormalParameterType276: "xpdl1_DataTypeType" = None, xpdl1_FormalParameterType274: "xpdl1_FormalParametersType" = None):
        self.description = description
        self.id = id
        self.index = index
        self.mode = mode
        self.xpdl1_FormalParameterType = xpdl1_FormalParameterType
        self.xpdl1_FormalParameterType276 = xpdl1_FormalParameterType276
        self.xpdl1_FormalParameterType274 = xpdl1_FormalParameterType274
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def mode(self) -> str:
        return self.__mode

    @mode.setter
    def mode(self, mode: str):
        self.__mode = mode

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def index(self) -> str:
        return self.__index

    @index.setter
    def index(self, index: str):
        self.__index = index

    @property
    def xpdl1_FormalParameterType274(self):
        return self.__xpdl1_FormalParameterType274

    @xpdl1_FormalParameterType274.setter
    def xpdl1_FormalParameterType274(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_FormalParameterType__xpdl1_FormalParameterType274", None)
        self.__xpdl1_FormalParameterType274 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_FormalParametersType273"):
                opp_val = getattr(old_value, "xpdl1_FormalParametersType273", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_FormalParametersType273"):
                opp_val = getattr(value, "xpdl1_FormalParametersType273", None)
                if opp_val is None:
                    setattr(value, "xpdl1_FormalParametersType273", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xpdl1_FormalParameterType276(self):
        return self.__xpdl1_FormalParameterType276

    @xpdl1_FormalParameterType276.setter
    def xpdl1_FormalParameterType276(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_FormalParameterType__xpdl1_FormalParameterType276", None)
        self.__xpdl1_FormalParameterType276 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_DataTypeType277"):
                opp_val = getattr(old_value, "xpdl1_DataTypeType277", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_DataTypeType277", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_DataTypeType277"):
                opp_val = getattr(value, "xpdl1_DataTypeType277", None)
                setattr(value, "xpdl1_DataTypeType277", self)

    @property
    def xpdl1_FormalParameterType(self):
        return self.__xpdl1_FormalParameterType

    @xpdl1_FormalParameterType.setter
    def xpdl1_FormalParameterType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_FormalParameterType__xpdl1_FormalParameterType", None)
        self.__xpdl1_FormalParameterType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_DocumentRoot167"):
                opp_val = getattr(old_value, "xpdl1_DocumentRoot167", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_DocumentRoot167"):
                opp_val = getattr(value, "xpdl1_DocumentRoot167", None)
                if opp_val is None:
                    setattr(value, "xpdl1_DocumentRoot167", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xpdl1_ExtendedAttributeType:

    def __init__(self, mixed: str, group: str, any: str, name: str, value: str, xpdl1_ExtendedAttributeType: "xpdl1_DocumentRoot" = None, xpdl1_ExtendedAttributeType259: "xpdl1_ExtendedAttributesType" = None):
        self.mixed = mixed
        self.group = group
        self.any = any
        self.name = name
        self.value = value
        self.xpdl1_ExtendedAttributeType = xpdl1_ExtendedAttributeType
        self.xpdl1_ExtendedAttributeType259 = xpdl1_ExtendedAttributeType259
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def xpdl1_ExtendedAttributeType(self):
        return self.__xpdl1_ExtendedAttributeType

    @xpdl1_ExtendedAttributeType.setter
    def xpdl1_ExtendedAttributeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ExtendedAttributeType__xpdl1_ExtendedAttributeType", None)
        self.__xpdl1_ExtendedAttributeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_DocumentRoot152"):
                opp_val = getattr(old_value, "xpdl1_DocumentRoot152", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_DocumentRoot152"):
                opp_val = getattr(value, "xpdl1_DocumentRoot152", None)
                if opp_val is None:
                    setattr(value, "xpdl1_DocumentRoot152", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xpdl1_ExtendedAttributeType259(self):
        return self.__xpdl1_ExtendedAttributeType259

    @xpdl1_ExtendedAttributeType259.setter
    def xpdl1_ExtendedAttributeType259(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ExtendedAttributeType__xpdl1_ExtendedAttributeType259", None)
        self.__xpdl1_ExtendedAttributeType259 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_ExtendedAttributesType258"):
                opp_val = getattr(old_value, "xpdl1_ExtendedAttributesType258", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_ExtendedAttributesType258"):
                opp_val = getattr(value, "xpdl1_ExtendedAttributesType258", None)
                if opp_val is None:
                    setattr(value, "xpdl1_ExtendedAttributesType258", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xpdl1_EnumerationValueType:

    def __init__(self, name: str, xpdl1_EnumerationValueType: "xpdl1_DocumentRoot" = None, xpdl1_EnumerationValueType256: "xpdl1_EnumerationTypeType" = None):
        self.name = name
        self.xpdl1_EnumerationValueType = xpdl1_EnumerationValueType
        self.xpdl1_EnumerationValueType256 = xpdl1_EnumerationValueType256
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def xpdl1_EnumerationValueType256(self):
        return self.__xpdl1_EnumerationValueType256

    @xpdl1_EnumerationValueType256.setter
    def xpdl1_EnumerationValueType256(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_EnumerationValueType__xpdl1_EnumerationValueType256", None)
        self.__xpdl1_EnumerationValueType256 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_EnumerationTypeType255"):
                opp_val = getattr(old_value, "xpdl1_EnumerationTypeType255", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_EnumerationTypeType255"):
                opp_val = getattr(value, "xpdl1_EnumerationTypeType255", None)
                if opp_val is None:
                    setattr(value, "xpdl1_EnumerationTypeType255", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xpdl1_EnumerationValueType(self):
        return self.__xpdl1_EnumerationValueType

    @xpdl1_EnumerationValueType.setter
    def xpdl1_EnumerationValueType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_EnumerationValueType__xpdl1_EnumerationValueType", None)
        self.__xpdl1_EnumerationValueType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_DocumentRoot150"):
                opp_val = getattr(old_value, "xpdl1_DocumentRoot150", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_DocumentRoot150"):
                opp_val = getattr(value, "xpdl1_DocumentRoot150", None)
                if opp_val is None:
                    setattr(value, "xpdl1_DocumentRoot150", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xpdl1_ExternalPackagesType:

    pass
class xpdl1_ExternalPackageType:

    def __init__(self, href: str, xpdl1_ExternalPackageType: "xpdl1_DocumentRoot" = None, xpdl1_ExternalPackageType262: "xpdl1_ExternalPackagesType" = None, xpdl1_ExternalPackageType264: "xpdl1_ExtendedAttributesType" = None):
        self.href = href
        self.xpdl1_ExternalPackageType = xpdl1_ExternalPackageType
        self.xpdl1_ExternalPackageType262 = xpdl1_ExternalPackageType262
        self.xpdl1_ExternalPackageType264 = xpdl1_ExternalPackageType264
        
    @property
    def href(self) -> str:
        return self.__href

    @href.setter
    def href(self, href: str):
        self.__href = href

    @property
    def xpdl1_ExternalPackageType264(self):
        return self.__xpdl1_ExternalPackageType264

    @xpdl1_ExternalPackageType264.setter
    def xpdl1_ExternalPackageType264(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ExternalPackageType__xpdl1_ExternalPackageType264", None)
        self.__xpdl1_ExternalPackageType264 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_ExtendedAttributesType265"):
                opp_val = getattr(old_value, "xpdl1_ExtendedAttributesType265", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_ExtendedAttributesType265", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_ExtendedAttributesType265"):
                opp_val = getattr(value, "xpdl1_ExtendedAttributesType265", None)
                setattr(value, "xpdl1_ExtendedAttributesType265", self)

    @property
    def xpdl1_ExternalPackageType(self):
        return self.__xpdl1_ExternalPackageType

    @xpdl1_ExternalPackageType.setter
    def xpdl1_ExternalPackageType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ExternalPackageType__xpdl1_ExternalPackageType", None)
        self.__xpdl1_ExternalPackageType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_DocumentRoot157"):
                opp_val = getattr(old_value, "xpdl1_DocumentRoot157", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_DocumentRoot157"):
                opp_val = getattr(value, "xpdl1_DocumentRoot157", None)
                if opp_val is None:
                    setattr(value, "xpdl1_DocumentRoot157", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xpdl1_ExternalPackageType262(self):
        return self.__xpdl1_ExternalPackageType262

    @xpdl1_ExternalPackageType262.setter
    def xpdl1_ExternalPackageType262(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ExternalPackageType__xpdl1_ExternalPackageType262", None)
        self.__xpdl1_ExternalPackageType262 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_ExternalPackagesType261"):
                opp_val = getattr(old_value, "xpdl1_ExternalPackagesType261", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_ExternalPackagesType261"):
                opp_val = getattr(value, "xpdl1_ExternalPackagesType261", None)
                if opp_val is None:
                    setattr(value, "xpdl1_ExternalPackagesType261", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xpdl1_EStringToStringMapEntry:

    pass
class xpdl1_DocumentRoot:

    def __init__(self, mixed: str, author: str, actualParameter: str, codepage: str, cost: str, costUnit: str, countrykey: str, created: str, description: str, documentation: str, duration: str, icon: str, initialValue: str, length: str, limit: str, performer: str, priority: str, priorityUnit: str, responsible: str, validTo: str, vendor: str, version: str, waitingTime: str, validFrom: str, xPDLVersion: str, workingTime: str, xpdl1_DocumentRoot: set["xpdl1_EStringToStringMapEntry"] = None, xpdl1_DocumentRoot93: set["xpdl1_EStringToStringMapEntry"] = None, xpdl1_DocumentRoot96: set["xpdl1_ActivitiesType"] = None, xpdl1_DocumentRoot99: set["xpdl1_ActivityType"] = None, xpdl1_DocumentRoot102: set["xpdl1_ActivitySetType"] = None, xpdl1_DocumentRoot105: set["xpdl1_ActivitySetsType"] = None, xpdl1_DocumentRoot108: set["xpdl1_ActualParametersType"] = None, xpdl1_DocumentRoot110: set["xpdl1_ApplicationType"] = None, xpdl1_DocumentRoot113: set["xpdl1_ApplicationsType"] = None, xpdl1_DocumentRoot116: set["xpdl1_ArrayTypeType"] = None, xpdl1_DocumentRoot119: set["xpdl1_AutomaticType"] = None, xpdl1_DocumentRoot124: set["xpdl1_BlockActivityType"] = None, xpdl1_DocumentRoot127: set["xpdl1_ConditionType"] = None, xpdl1_DocumentRoot130: set["xpdl1_ConformanceClassType"] = None, xpdl1_DocumentRoot121: set["xpdl1_BasicTypeType"] = None, xpdl1_DocumentRoot144: set["xpdl1_DeclaredTypeType"] = None, xpdl1_DocumentRoot132: set["xpdl1_DataFieldType"] = None, xpdl1_DocumentRoot135: set["xpdl1_DataFieldsType"] = None, xpdl1_DocumentRoot138: set["xpdl1_DataTypeType"] = None, xpdl1_DocumentRoot141: set["xpdl1_DeadlineType"] = None, xpdl1_DocumentRoot147: set["xpdl1_EnumerationTypeType"] = None, xpdl1_DocumentRoot157: set["xpdl1_ExternalPackageType"] = None, xpdl1_DocumentRoot150: set["xpdl1_EnumerationValueType"] = None, xpdl1_DocumentRoot152: set["xpdl1_ExtendedAttributeType"] = None, xpdl1_DocumentRoot154: set["xpdl1_ExtendedAttributesType"] = None, xpdl1_DocumentRoot169: set["xpdl1_FormalParametersType"] = None, xpdl1_DocumentRoot172: set["xpdl1_ImplementationType"] = None, xpdl1_DocumentRoot159: set["xpdl1_ExternalPackagesType"] = None, xpdl1_DocumentRoot161: set["xpdl1_ExternalReferenceType"] = None, xpdl1_DocumentRoot164: set["xpdl1_FinishModeType"] = None, xpdl1_DocumentRoot167: set["xpdl1_FormalParameterType"] = None, xpdl1_DocumentRoot177: set["xpdl1_ListTypeType"] = None, xpdl1_DocumentRoot180: set["xpdl1_ManualType"] = None, xpdl1_DocumentRoot175: set["xpdl1_JoinType"] = None, xpdl1_DocumentRoot188: set["xpdl1_PackageHeaderType"] = None, xpdl1_DocumentRoot190: set["xpdl1_ParticipantType"] = None, xpdl1_DocumentRoot182: set["xpdl1_MemberType"] = None, xpdl1_DocumentRoot184: set["xpdl1_NoType"] = None, xpdl1_DocumentRoot186: set["xpdl1_PackageType"] = None, xpdl1_DocumentRoot196: set["xpdl1_ProcessHeaderType"] = None, xpdl1_DocumentRoot198: set["xpdl1_RecordTypeType"] = None, xpdl1_DocumentRoot192: set["xpdl1_ParticipantsType"] = None, xpdl1_DocumentRoot194: set["xpdl1_ParticipantTypeType"] = None, xpdl1_DocumentRoot203: set["xpdl1_ResponsiblesType"] = None, xpdl1_DocumentRoot205: set["xpdl1_RouteType"] = None, xpdl1_DocumentRoot208: set["xpdl1_SchemaTypeType"] = None, xpdl1_DocumentRoot201: set["xpdl1_RedefinableHeaderType"] = None, xpdl1_DocumentRoot213: set["xpdl1_SimulationInformationType"] = None, xpdl1_DocumentRoot216: set["xpdl1_SplitType"] = None, xpdl1_DocumentRoot218: set["xpdl1_StartModeType"] = None, xpdl1_DocumentRoot221: set["xpdl1_SubFlowType"] = None, xpdl1_DocumentRoot211: set["xpdl1_ScriptType"] = None, xpdl1_DocumentRoot225: set["xpdl1_ToolType"] = None, xpdl1_DocumentRoot227: set["xpdl1_TransitionType"] = None, xpdl1_DocumentRoot229: set["xpdl1_TransitionRefType"] = None, xpdl1_DocumentRoot231: set["xpdl1_TransitionRefsType"] = None, xpdl1_DocumentRoot223: set["xpdl1_TimeEstimationType"] = None, xpdl1_DocumentRoot235: set["xpdl1_TransitionRestrictionsType"] = None, xpdl1_DocumentRoot238: set["xpdl1_TransitionsType"] = None, xpdl1_DocumentRoot233: set["xpdl1_TransitionRestrictionType"] = None, xpdl1_DocumentRoot243: set["xpdl1_TypeDeclarationsType"] = None, xpdl1_DocumentRoot245: set["xpdl1_UnionTypeType"] = None, xpdl1_DocumentRoot241: set["xpdl1_TypeDeclarationType"] = None, xpdl1_DocumentRoot248: set["xpdl1_WorkflowProcessType"] = None, xpdl1_DocumentRoot250: set["xpdl1_WorkflowProcessesType"] = None, xpdl1_DocumentRoot252: set["xpdl1_XpressionType"] = None):
        self.mixed = mixed
        self.author = author
        self.actualParameter = actualParameter
        self.codepage = codepage
        self.cost = cost
        self.costUnit = costUnit
        self.countrykey = countrykey
        self.created = created
        self.description = description
        self.documentation = documentation
        self.duration = duration
        self.icon = icon
        self.initialValue = initialValue
        self.length = length
        self.limit = limit
        self.performer = performer
        self.priority = priority
        self.priorityUnit = priorityUnit
        self.responsible = responsible
        self.validTo = validTo
        self.vendor = vendor
        self.version = version
        self.waitingTime = waitingTime
        self.validFrom = validFrom
        self.xPDLVersion = xPDLVersion
        self.workingTime = workingTime
        self.xpdl1_DocumentRoot = xpdl1_DocumentRoot if xpdl1_DocumentRoot is not None else set()
        self.xpdl1_DocumentRoot93 = xpdl1_DocumentRoot93 if xpdl1_DocumentRoot93 is not None else set()
        self.xpdl1_DocumentRoot96 = xpdl1_DocumentRoot96 if xpdl1_DocumentRoot96 is not None else set()
        self.xpdl1_DocumentRoot99 = xpdl1_DocumentRoot99 if xpdl1_DocumentRoot99 is not None else set()
        self.xpdl1_DocumentRoot102 = xpdl1_DocumentRoot102 if xpdl1_DocumentRoot102 is not None else set()
        self.xpdl1_DocumentRoot105 = xpdl1_DocumentRoot105 if xpdl1_DocumentRoot105 is not None else set()
        self.xpdl1_DocumentRoot108 = xpdl1_DocumentRoot108 if xpdl1_DocumentRoot108 is not None else set()
        self.xpdl1_DocumentRoot110 = xpdl1_DocumentRoot110 if xpdl1_DocumentRoot110 is not None else set()
        self.xpdl1_DocumentRoot113 = xpdl1_DocumentRoot113 if xpdl1_DocumentRoot113 is not None else set()
        self.xpdl1_DocumentRoot116 = xpdl1_DocumentRoot116 if xpdl1_DocumentRoot116 is not None else set()
        self.xpdl1_DocumentRoot119 = xpdl1_DocumentRoot119 if xpdl1_DocumentRoot119 is not None else set()
        self.xpdl1_DocumentRoot124 = xpdl1_DocumentRoot124 if xpdl1_DocumentRoot124 is not None else set()
        self.xpdl1_DocumentRoot127 = xpdl1_DocumentRoot127 if xpdl1_DocumentRoot127 is not None else set()
        self.xpdl1_DocumentRoot130 = xpdl1_DocumentRoot130 if xpdl1_DocumentRoot130 is not None else set()
        self.xpdl1_DocumentRoot121 = xpdl1_DocumentRoot121 if xpdl1_DocumentRoot121 is not None else set()
        self.xpdl1_DocumentRoot144 = xpdl1_DocumentRoot144 if xpdl1_DocumentRoot144 is not None else set()
        self.xpdl1_DocumentRoot132 = xpdl1_DocumentRoot132 if xpdl1_DocumentRoot132 is not None else set()
        self.xpdl1_DocumentRoot135 = xpdl1_DocumentRoot135 if xpdl1_DocumentRoot135 is not None else set()
        self.xpdl1_DocumentRoot138 = xpdl1_DocumentRoot138 if xpdl1_DocumentRoot138 is not None else set()
        self.xpdl1_DocumentRoot141 = xpdl1_DocumentRoot141 if xpdl1_DocumentRoot141 is not None else set()
        self.xpdl1_DocumentRoot147 = xpdl1_DocumentRoot147 if xpdl1_DocumentRoot147 is not None else set()
        self.xpdl1_DocumentRoot157 = xpdl1_DocumentRoot157 if xpdl1_DocumentRoot157 is not None else set()
        self.xpdl1_DocumentRoot150 = xpdl1_DocumentRoot150 if xpdl1_DocumentRoot150 is not None else set()
        self.xpdl1_DocumentRoot152 = xpdl1_DocumentRoot152 if xpdl1_DocumentRoot152 is not None else set()
        self.xpdl1_DocumentRoot154 = xpdl1_DocumentRoot154 if xpdl1_DocumentRoot154 is not None else set()
        self.xpdl1_DocumentRoot169 = xpdl1_DocumentRoot169 if xpdl1_DocumentRoot169 is not None else set()
        self.xpdl1_DocumentRoot172 = xpdl1_DocumentRoot172 if xpdl1_DocumentRoot172 is not None else set()
        self.xpdl1_DocumentRoot159 = xpdl1_DocumentRoot159 if xpdl1_DocumentRoot159 is not None else set()
        self.xpdl1_DocumentRoot161 = xpdl1_DocumentRoot161 if xpdl1_DocumentRoot161 is not None else set()
        self.xpdl1_DocumentRoot164 = xpdl1_DocumentRoot164 if xpdl1_DocumentRoot164 is not None else set()
        self.xpdl1_DocumentRoot167 = xpdl1_DocumentRoot167 if xpdl1_DocumentRoot167 is not None else set()
        self.xpdl1_DocumentRoot177 = xpdl1_DocumentRoot177 if xpdl1_DocumentRoot177 is not None else set()
        self.xpdl1_DocumentRoot180 = xpdl1_DocumentRoot180 if xpdl1_DocumentRoot180 is not None else set()
        self.xpdl1_DocumentRoot175 = xpdl1_DocumentRoot175 if xpdl1_DocumentRoot175 is not None else set()
        self.xpdl1_DocumentRoot188 = xpdl1_DocumentRoot188 if xpdl1_DocumentRoot188 is not None else set()
        self.xpdl1_DocumentRoot190 = xpdl1_DocumentRoot190 if xpdl1_DocumentRoot190 is not None else set()
        self.xpdl1_DocumentRoot182 = xpdl1_DocumentRoot182 if xpdl1_DocumentRoot182 is not None else set()
        self.xpdl1_DocumentRoot184 = xpdl1_DocumentRoot184 if xpdl1_DocumentRoot184 is not None else set()
        self.xpdl1_DocumentRoot186 = xpdl1_DocumentRoot186 if xpdl1_DocumentRoot186 is not None else set()
        self.xpdl1_DocumentRoot196 = xpdl1_DocumentRoot196 if xpdl1_DocumentRoot196 is not None else set()
        self.xpdl1_DocumentRoot198 = xpdl1_DocumentRoot198 if xpdl1_DocumentRoot198 is not None else set()
        self.xpdl1_DocumentRoot192 = xpdl1_DocumentRoot192 if xpdl1_DocumentRoot192 is not None else set()
        self.xpdl1_DocumentRoot194 = xpdl1_DocumentRoot194 if xpdl1_DocumentRoot194 is not None else set()
        self.xpdl1_DocumentRoot203 = xpdl1_DocumentRoot203 if xpdl1_DocumentRoot203 is not None else set()
        self.xpdl1_DocumentRoot205 = xpdl1_DocumentRoot205 if xpdl1_DocumentRoot205 is not None else set()
        self.xpdl1_DocumentRoot208 = xpdl1_DocumentRoot208 if xpdl1_DocumentRoot208 is not None else set()
        self.xpdl1_DocumentRoot201 = xpdl1_DocumentRoot201 if xpdl1_DocumentRoot201 is not None else set()
        self.xpdl1_DocumentRoot213 = xpdl1_DocumentRoot213 if xpdl1_DocumentRoot213 is not None else set()
        self.xpdl1_DocumentRoot216 = xpdl1_DocumentRoot216 if xpdl1_DocumentRoot216 is not None else set()
        self.xpdl1_DocumentRoot218 = xpdl1_DocumentRoot218 if xpdl1_DocumentRoot218 is not None else set()
        self.xpdl1_DocumentRoot221 = xpdl1_DocumentRoot221 if xpdl1_DocumentRoot221 is not None else set()
        self.xpdl1_DocumentRoot211 = xpdl1_DocumentRoot211 if xpdl1_DocumentRoot211 is not None else set()
        self.xpdl1_DocumentRoot225 = xpdl1_DocumentRoot225 if xpdl1_DocumentRoot225 is not None else set()
        self.xpdl1_DocumentRoot227 = xpdl1_DocumentRoot227 if xpdl1_DocumentRoot227 is not None else set()
        self.xpdl1_DocumentRoot229 = xpdl1_DocumentRoot229 if xpdl1_DocumentRoot229 is not None else set()
        self.xpdl1_DocumentRoot231 = xpdl1_DocumentRoot231 if xpdl1_DocumentRoot231 is not None else set()
        self.xpdl1_DocumentRoot223 = xpdl1_DocumentRoot223 if xpdl1_DocumentRoot223 is not None else set()
        self.xpdl1_DocumentRoot235 = xpdl1_DocumentRoot235 if xpdl1_DocumentRoot235 is not None else set()
        self.xpdl1_DocumentRoot238 = xpdl1_DocumentRoot238 if xpdl1_DocumentRoot238 is not None else set()
        self.xpdl1_DocumentRoot233 = xpdl1_DocumentRoot233 if xpdl1_DocumentRoot233 is not None else set()
        self.xpdl1_DocumentRoot243 = xpdl1_DocumentRoot243 if xpdl1_DocumentRoot243 is not None else set()
        self.xpdl1_DocumentRoot245 = xpdl1_DocumentRoot245 if xpdl1_DocumentRoot245 is not None else set()
        self.xpdl1_DocumentRoot241 = xpdl1_DocumentRoot241 if xpdl1_DocumentRoot241 is not None else set()
        self.xpdl1_DocumentRoot248 = xpdl1_DocumentRoot248 if xpdl1_DocumentRoot248 is not None else set()
        self.xpdl1_DocumentRoot250 = xpdl1_DocumentRoot250 if xpdl1_DocumentRoot250 is not None else set()
        self.xpdl1_DocumentRoot252 = xpdl1_DocumentRoot252 if xpdl1_DocumentRoot252 is not None else set()
        
    @property
    def workingTime(self) -> str:
        return self.__workingTime

    @workingTime.setter
    def workingTime(self, workingTime: str):
        self.__workingTime = workingTime

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def initialValue(self) -> str:
        return self.__initialValue

    @initialValue.setter
    def initialValue(self, initialValue: str):
        self.__initialValue = initialValue

    @property
    def xPDLVersion(self) -> str:
        return self.__xPDLVersion

    @xPDLVersion.setter
    def xPDLVersion(self, xPDLVersion: str):
        self.__xPDLVersion = xPDLVersion

    @property
    def priority(self) -> str:
        return self.__priority

    @priority.setter
    def priority(self, priority: str):
        self.__priority = priority

    @property
    def responsible(self) -> str:
        return self.__responsible

    @responsible.setter
    def responsible(self, responsible: str):
        self.__responsible = responsible

    @property
    def created(self) -> str:
        return self.__created

    @created.setter
    def created(self, created: str):
        self.__created = created

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def validTo(self) -> str:
        return self.__validTo

    @validTo.setter
    def validTo(self, validTo: str):
        self.__validTo = validTo

    @property
    def documentation(self) -> str:
        return self.__documentation

    @documentation.setter
    def documentation(self, documentation: str):
        self.__documentation = documentation

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def vendor(self) -> str:
        return self.__vendor

    @vendor.setter
    def vendor(self, vendor: str):
        self.__vendor = vendor

    @property
    def duration(self) -> str:
        return self.__duration

    @duration.setter
    def duration(self, duration: str):
        self.__duration = duration

    @property
    def countrykey(self) -> str:
        return self.__countrykey

    @countrykey.setter
    def countrykey(self, countrykey: str):
        self.__countrykey = countrykey

    @property
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author

    @property
    def length(self) -> str:
        return self.__length

    @length.setter
    def length(self, length: str):
        self.__length = length

    @property
    def limit(self) -> str:
        return self.__limit

    @limit.setter
    def limit(self, limit: str):
        self.__limit = limit

    @property
    def priorityUnit(self) -> str:
        return self.__priorityUnit

    @priorityUnit.setter
    def priorityUnit(self, priorityUnit: str):
        self.__priorityUnit = priorityUnit

    @property
    def codepage(self) -> str:
        return self.__codepage

    @codepage.setter
    def codepage(self, codepage: str):
        self.__codepage = codepage

    @property
    def waitingTime(self) -> str:
        return self.__waitingTime

    @waitingTime.setter
    def waitingTime(self, waitingTime: str):
        self.__waitingTime = waitingTime

    @property
    def validFrom(self) -> str:
        return self.__validFrom

    @validFrom.setter
    def validFrom(self, validFrom: str):
        self.__validFrom = validFrom

    @property
    def actualParameter(self) -> str:
        return self.__actualParameter

    @actualParameter.setter
    def actualParameter(self, actualParameter: str):
        self.__actualParameter = actualParameter

    @property
    def costUnit(self) -> str:
        return self.__costUnit

    @costUnit.setter
    def costUnit(self, costUnit: str):
        self.__costUnit = costUnit

    @property
    def cost(self) -> str:
        return self.__cost

    @cost.setter
    def cost(self, cost: str):
        self.__cost = cost

    @property
    def performer(self) -> str:
        return self.__performer

    @performer.setter
    def performer(self, performer: str):
        self.__performer = performer

    @property
    def icon(self) -> str:
        return self.__icon

    @icon.setter
    def icon(self, icon: str):
        self.__icon = icon

    @property
    def xpdl1_DocumentRoot229(self):
        return self.__xpdl1_DocumentRoot229

    @xpdl1_DocumentRoot229.setter
    def xpdl1_DocumentRoot229(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot229", None)
        self.__xpdl1_DocumentRoot229 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_TransitionRefType"):
                    opp_val = getattr(item, "xpdl1_TransitionRefType", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_TransitionRefType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_TransitionRefType"):
                    opp_val = getattr(item, "xpdl1_TransitionRefType", None)
                    
                    setattr(item, "xpdl1_TransitionRefType", self)
                    

    @property
    def xpdl1_DocumentRoot198(self):
        return self.__xpdl1_DocumentRoot198

    @xpdl1_DocumentRoot198.setter
    def xpdl1_DocumentRoot198(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot198", None)
        self.__xpdl1_DocumentRoot198 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_RecordTypeType199"):
                    opp_val = getattr(item, "xpdl1_RecordTypeType199", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_RecordTypeType199", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_RecordTypeType199"):
                    opp_val = getattr(item, "xpdl1_RecordTypeType199", None)
                    
                    setattr(item, "xpdl1_RecordTypeType199", self)
                    

    @property
    def xpdl1_DocumentRoot177(self):
        return self.__xpdl1_DocumentRoot177

    @xpdl1_DocumentRoot177.setter
    def xpdl1_DocumentRoot177(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot177", None)
        self.__xpdl1_DocumentRoot177 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_ListTypeType178"):
                    opp_val = getattr(item, "xpdl1_ListTypeType178", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_ListTypeType178", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_ListTypeType178"):
                    opp_val = getattr(item, "xpdl1_ListTypeType178", None)
                    
                    setattr(item, "xpdl1_ListTypeType178", self)
                    

    @property
    def xpdl1_DocumentRoot218(self):
        return self.__xpdl1_DocumentRoot218

    @xpdl1_DocumentRoot218.setter
    def xpdl1_DocumentRoot218(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot218", None)
        self.__xpdl1_DocumentRoot218 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_StartModeType219"):
                    opp_val = getattr(item, "xpdl1_StartModeType219", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_StartModeType219", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_StartModeType219"):
                    opp_val = getattr(item, "xpdl1_StartModeType219", None)
                    
                    setattr(item, "xpdl1_StartModeType219", self)
                    

    @property
    def xpdl1_DocumentRoot161(self):
        return self.__xpdl1_DocumentRoot161

    @xpdl1_DocumentRoot161.setter
    def xpdl1_DocumentRoot161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot161", None)
        self.__xpdl1_DocumentRoot161 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_ExternalReferenceType162"):
                    opp_val = getattr(item, "xpdl1_ExternalReferenceType162", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_ExternalReferenceType162", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_ExternalReferenceType162"):
                    opp_val = getattr(item, "xpdl1_ExternalReferenceType162", None)
                    
                    setattr(item, "xpdl1_ExternalReferenceType162", self)
                    

    @property
    def xpdl1_DocumentRoot182(self):
        return self.__xpdl1_DocumentRoot182

    @xpdl1_DocumentRoot182.setter
    def xpdl1_DocumentRoot182(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot182", None)
        self.__xpdl1_DocumentRoot182 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_MemberType"):
                    opp_val = getattr(item, "xpdl1_MemberType", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_MemberType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_MemberType"):
                    opp_val = getattr(item, "xpdl1_MemberType", None)
                    
                    setattr(item, "xpdl1_MemberType", self)
                    

    @property
    def xpdl1_DocumentRoot169(self):
        return self.__xpdl1_DocumentRoot169

    @xpdl1_DocumentRoot169.setter
    def xpdl1_DocumentRoot169(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot169", None)
        self.__xpdl1_DocumentRoot169 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_FormalParametersType170"):
                    opp_val = getattr(item, "xpdl1_FormalParametersType170", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_FormalParametersType170", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_FormalParametersType170"):
                    opp_val = getattr(item, "xpdl1_FormalParametersType170", None)
                    
                    setattr(item, "xpdl1_FormalParametersType170", self)
                    

    @property
    def xpdl1_DocumentRoot208(self):
        return self.__xpdl1_DocumentRoot208

    @xpdl1_DocumentRoot208.setter
    def xpdl1_DocumentRoot208(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot208", None)
        self.__xpdl1_DocumentRoot208 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_SchemaTypeType209"):
                    opp_val = getattr(item, "xpdl1_SchemaTypeType209", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_SchemaTypeType209", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_SchemaTypeType209"):
                    opp_val = getattr(item, "xpdl1_SchemaTypeType209", None)
                    
                    setattr(item, "xpdl1_SchemaTypeType209", self)
                    

    @property
    def xpdl1_DocumentRoot135(self):
        return self.__xpdl1_DocumentRoot135

    @xpdl1_DocumentRoot135.setter
    def xpdl1_DocumentRoot135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot135", None)
        self.__xpdl1_DocumentRoot135 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_DataFieldsType136"):
                    opp_val = getattr(item, "xpdl1_DataFieldsType136", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_DataFieldsType136", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_DataFieldsType136"):
                    opp_val = getattr(item, "xpdl1_DataFieldsType136", None)
                    
                    setattr(item, "xpdl1_DataFieldsType136", self)
                    

    @property
    def xpdl1_DocumentRoot159(self):
        return self.__xpdl1_DocumentRoot159

    @xpdl1_DocumentRoot159.setter
    def xpdl1_DocumentRoot159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot159", None)
        self.__xpdl1_DocumentRoot159 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_ExternalPackagesType"):
                    opp_val = getattr(item, "xpdl1_ExternalPackagesType", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_ExternalPackagesType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_ExternalPackagesType"):
                    opp_val = getattr(item, "xpdl1_ExternalPackagesType", None)
                    
                    setattr(item, "xpdl1_ExternalPackagesType", self)
                    

    @property
    def xpdl1_DocumentRoot231(self):
        return self.__xpdl1_DocumentRoot231

    @xpdl1_DocumentRoot231.setter
    def xpdl1_DocumentRoot231(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot231", None)
        self.__xpdl1_DocumentRoot231 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_TransitionRefsType"):
                    opp_val = getattr(item, "xpdl1_TransitionRefsType", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_TransitionRefsType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_TransitionRefsType"):
                    opp_val = getattr(item, "xpdl1_TransitionRefsType", None)
                    
                    setattr(item, "xpdl1_TransitionRefsType", self)
                    

    @property
    def xpdl1_DocumentRoot110(self):
        return self.__xpdl1_DocumentRoot110

    @xpdl1_DocumentRoot110.setter
    def xpdl1_DocumentRoot110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot110", None)
        self.__xpdl1_DocumentRoot110 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_ApplicationType111"):
                    opp_val = getattr(item, "xpdl1_ApplicationType111", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_ApplicationType111", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_ApplicationType111"):
                    opp_val = getattr(item, "xpdl1_ApplicationType111", None)
                    
                    setattr(item, "xpdl1_ApplicationType111", self)
                    

    @property
    def xpdl1_DocumentRoot192(self):
        return self.__xpdl1_DocumentRoot192

    @xpdl1_DocumentRoot192.setter
    def xpdl1_DocumentRoot192(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot192", None)
        self.__xpdl1_DocumentRoot192 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_ParticipantsType"):
                    opp_val = getattr(item, "xpdl1_ParticipantsType", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_ParticipantsType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_ParticipantsType"):
                    opp_val = getattr(item, "xpdl1_ParticipantsType", None)
                    
                    setattr(item, "xpdl1_ParticipantsType", self)
                    

    @property
    def xpdl1_DocumentRoot238(self):
        return self.__xpdl1_DocumentRoot238

    @xpdl1_DocumentRoot238.setter
    def xpdl1_DocumentRoot238(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot238", None)
        self.__xpdl1_DocumentRoot238 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_TransitionsType239"):
                    opp_val = getattr(item, "xpdl1_TransitionsType239", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_TransitionsType239", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_TransitionsType239"):
                    opp_val = getattr(item, "xpdl1_TransitionsType239", None)
                    
                    setattr(item, "xpdl1_TransitionsType239", self)
                    

    @property
    def xpdl1_DocumentRoot164(self):
        return self.__xpdl1_DocumentRoot164

    @xpdl1_DocumentRoot164.setter
    def xpdl1_DocumentRoot164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot164", None)
        self.__xpdl1_DocumentRoot164 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_FinishModeType165"):
                    opp_val = getattr(item, "xpdl1_FinishModeType165", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_FinishModeType165", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_FinishModeType165"):
                    opp_val = getattr(item, "xpdl1_FinishModeType165", None)
                    
                    setattr(item, "xpdl1_FinishModeType165", self)
                    

    @property
    def xpdl1_DocumentRoot188(self):
        return self.__xpdl1_DocumentRoot188

    @xpdl1_DocumentRoot188.setter
    def xpdl1_DocumentRoot188(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot188", None)
        self.__xpdl1_DocumentRoot188 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_PackageHeaderType"):
                    opp_val = getattr(item, "xpdl1_PackageHeaderType", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_PackageHeaderType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_PackageHeaderType"):
                    opp_val = getattr(item, "xpdl1_PackageHeaderType", None)
                    
                    setattr(item, "xpdl1_PackageHeaderType", self)
                    

    @property
    def xpdl1_DocumentRoot241(self):
        return self.__xpdl1_DocumentRoot241

    @xpdl1_DocumentRoot241.setter
    def xpdl1_DocumentRoot241(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot241", None)
        self.__xpdl1_DocumentRoot241 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_TypeDeclarationType"):
                    opp_val = getattr(item, "xpdl1_TypeDeclarationType", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_TypeDeclarationType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_TypeDeclarationType"):
                    opp_val = getattr(item, "xpdl1_TypeDeclarationType", None)
                    
                    setattr(item, "xpdl1_TypeDeclarationType", self)
                    

    @property
    def xpdl1_DocumentRoot124(self):
        return self.__xpdl1_DocumentRoot124

    @xpdl1_DocumentRoot124.setter
    def xpdl1_DocumentRoot124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot124", None)
        self.__xpdl1_DocumentRoot124 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_BlockActivityType125"):
                    opp_val = getattr(item, "xpdl1_BlockActivityType125", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_BlockActivityType125", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_BlockActivityType125"):
                    opp_val = getattr(item, "xpdl1_BlockActivityType125", None)
                    
                    setattr(item, "xpdl1_BlockActivityType125", self)
                    

    @property
    def xpdl1_DocumentRoot235(self):
        return self.__xpdl1_DocumentRoot235

    @xpdl1_DocumentRoot235.setter
    def xpdl1_DocumentRoot235(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot235", None)
        self.__xpdl1_DocumentRoot235 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_TransitionRestrictionsType236"):
                    opp_val = getattr(item, "xpdl1_TransitionRestrictionsType236", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_TransitionRestrictionsType236", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_TransitionRestrictionsType236"):
                    opp_val = getattr(item, "xpdl1_TransitionRestrictionsType236", None)
                    
                    setattr(item, "xpdl1_TransitionRestrictionsType236", self)
                    

    @property
    def xpdl1_DocumentRoot190(self):
        return self.__xpdl1_DocumentRoot190

    @xpdl1_DocumentRoot190.setter
    def xpdl1_DocumentRoot190(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot190", None)
        self.__xpdl1_DocumentRoot190 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_ParticipantType"):
                    opp_val = getattr(item, "xpdl1_ParticipantType", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_ParticipantType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_ParticipantType"):
                    opp_val = getattr(item, "xpdl1_ParticipantType", None)
                    
                    setattr(item, "xpdl1_ParticipantType", self)
                    

    @property
    def xpdl1_DocumentRoot184(self):
        return self.__xpdl1_DocumentRoot184

    @xpdl1_DocumentRoot184.setter
    def xpdl1_DocumentRoot184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot184", None)
        self.__xpdl1_DocumentRoot184 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_NoType"):
                    opp_val = getattr(item, "xpdl1_NoType", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_NoType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_NoType"):
                    opp_val = getattr(item, "xpdl1_NoType", None)
                    
                    setattr(item, "xpdl1_NoType", self)
                    

    @property
    def xpdl1_DocumentRoot203(self):
        return self.__xpdl1_DocumentRoot203

    @xpdl1_DocumentRoot203.setter
    def xpdl1_DocumentRoot203(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot203", None)
        self.__xpdl1_DocumentRoot203 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_ResponsiblesType"):
                    opp_val = getattr(item, "xpdl1_ResponsiblesType", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_ResponsiblesType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_ResponsiblesType"):
                    opp_val = getattr(item, "xpdl1_ResponsiblesType", None)
                    
                    setattr(item, "xpdl1_ResponsiblesType", self)
                    

    @property
    def xpdl1_DocumentRoot147(self):
        return self.__xpdl1_DocumentRoot147

    @xpdl1_DocumentRoot147.setter
    def xpdl1_DocumentRoot147(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot147", None)
        self.__xpdl1_DocumentRoot147 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_EnumerationTypeType148"):
                    opp_val = getattr(item, "xpdl1_EnumerationTypeType148", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_EnumerationTypeType148", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_EnumerationTypeType148"):
                    opp_val = getattr(item, "xpdl1_EnumerationTypeType148", None)
                    
                    setattr(item, "xpdl1_EnumerationTypeType148", self)
                    

    @property
    def xpdl1_DocumentRoot93(self):
        return self.__xpdl1_DocumentRoot93

    @xpdl1_DocumentRoot93.setter
    def xpdl1_DocumentRoot93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot93", None)
        self.__xpdl1_DocumentRoot93 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_EStringToStringMapEntry94"):
                    opp_val = getattr(item, "xpdl1_EStringToStringMapEntry94", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_EStringToStringMapEntry94", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_EStringToStringMapEntry94"):
                    opp_val = getattr(item, "xpdl1_EStringToStringMapEntry94", None)
                    
                    setattr(item, "xpdl1_EStringToStringMapEntry94", self)
                    

    @property
    def xpdl1_DocumentRoot194(self):
        return self.__xpdl1_DocumentRoot194

    @xpdl1_DocumentRoot194.setter
    def xpdl1_DocumentRoot194(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot194", None)
        self.__xpdl1_DocumentRoot194 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_ParticipantTypeType"):
                    opp_val = getattr(item, "xpdl1_ParticipantTypeType", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_ParticipantTypeType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_ParticipantTypeType"):
                    opp_val = getattr(item, "xpdl1_ParticipantTypeType", None)
                    
                    setattr(item, "xpdl1_ParticipantTypeType", self)
                    

    @property
    def xpdl1_DocumentRoot167(self):
        return self.__xpdl1_DocumentRoot167

    @xpdl1_DocumentRoot167.setter
    def xpdl1_DocumentRoot167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot167", None)
        self.__xpdl1_DocumentRoot167 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_FormalParameterType"):
                    opp_val = getattr(item, "xpdl1_FormalParameterType", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_FormalParameterType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_FormalParameterType"):
                    opp_val = getattr(item, "xpdl1_FormalParameterType", None)
                    
                    setattr(item, "xpdl1_FormalParameterType", self)
                    

    @property
    def xpdl1_DocumentRoot138(self):
        return self.__xpdl1_DocumentRoot138

    @xpdl1_DocumentRoot138.setter
    def xpdl1_DocumentRoot138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot138", None)
        self.__xpdl1_DocumentRoot138 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_DataTypeType139"):
                    opp_val = getattr(item, "xpdl1_DataTypeType139", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_DataTypeType139", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_DataTypeType139"):
                    opp_val = getattr(item, "xpdl1_DataTypeType139", None)
                    
                    setattr(item, "xpdl1_DataTypeType139", self)
                    

    @property
    def xpdl1_DocumentRoot175(self):
        return self.__xpdl1_DocumentRoot175

    @xpdl1_DocumentRoot175.setter
    def xpdl1_DocumentRoot175(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot175", None)
        self.__xpdl1_DocumentRoot175 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_JoinType"):
                    opp_val = getattr(item, "xpdl1_JoinType", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_JoinType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_JoinType"):
                    opp_val = getattr(item, "xpdl1_JoinType", None)
                    
                    setattr(item, "xpdl1_JoinType", self)
                    

    @property
    def xpdl1_DocumentRoot157(self):
        return self.__xpdl1_DocumentRoot157

    @xpdl1_DocumentRoot157.setter
    def xpdl1_DocumentRoot157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot157", None)
        self.__xpdl1_DocumentRoot157 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_ExternalPackageType"):
                    opp_val = getattr(item, "xpdl1_ExternalPackageType", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_ExternalPackageType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_ExternalPackageType"):
                    opp_val = getattr(item, "xpdl1_ExternalPackageType", None)
                    
                    setattr(item, "xpdl1_ExternalPackageType", self)
                    

    @property
    def xpdl1_DocumentRoot116(self):
        return self.__xpdl1_DocumentRoot116

    @xpdl1_DocumentRoot116.setter
    def xpdl1_DocumentRoot116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot116", None)
        self.__xpdl1_DocumentRoot116 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_ArrayTypeType117"):
                    opp_val = getattr(item, "xpdl1_ArrayTypeType117", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_ArrayTypeType117", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_ArrayTypeType117"):
                    opp_val = getattr(item, "xpdl1_ArrayTypeType117", None)
                    
                    setattr(item, "xpdl1_ArrayTypeType117", self)
                    

    @property
    def xpdl1_DocumentRoot108(self):
        return self.__xpdl1_DocumentRoot108

    @xpdl1_DocumentRoot108.setter
    def xpdl1_DocumentRoot108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot108", None)
        self.__xpdl1_DocumentRoot108 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_ActualParametersType"):
                    opp_val = getattr(item, "xpdl1_ActualParametersType", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_ActualParametersType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_ActualParametersType"):
                    opp_val = getattr(item, "xpdl1_ActualParametersType", None)
                    
                    setattr(item, "xpdl1_ActualParametersType", self)
                    

    @property
    def xpdl1_DocumentRoot113(self):
        return self.__xpdl1_DocumentRoot113

    @xpdl1_DocumentRoot113.setter
    def xpdl1_DocumentRoot113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot113", None)
        self.__xpdl1_DocumentRoot113 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_ApplicationsType114"):
                    opp_val = getattr(item, "xpdl1_ApplicationsType114", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_ApplicationsType114", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_ApplicationsType114"):
                    opp_val = getattr(item, "xpdl1_ApplicationsType114", None)
                    
                    setattr(item, "xpdl1_ApplicationsType114", self)
                    

    @property
    def xpdl1_DocumentRoot225(self):
        return self.__xpdl1_DocumentRoot225

    @xpdl1_DocumentRoot225.setter
    def xpdl1_DocumentRoot225(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot225", None)
        self.__xpdl1_DocumentRoot225 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_ToolType"):
                    opp_val = getattr(item, "xpdl1_ToolType", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_ToolType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_ToolType"):
                    opp_val = getattr(item, "xpdl1_ToolType", None)
                    
                    setattr(item, "xpdl1_ToolType", self)
                    

    @property
    def xpdl1_DocumentRoot152(self):
        return self.__xpdl1_DocumentRoot152

    @xpdl1_DocumentRoot152.setter
    def xpdl1_DocumentRoot152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot152", None)
        self.__xpdl1_DocumentRoot152 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_ExtendedAttributeType"):
                    opp_val = getattr(item, "xpdl1_ExtendedAttributeType", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_ExtendedAttributeType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_ExtendedAttributeType"):
                    opp_val = getattr(item, "xpdl1_ExtendedAttributeType", None)
                    
                    setattr(item, "xpdl1_ExtendedAttributeType", self)
                    

    @property
    def xpdl1_DocumentRoot121(self):
        return self.__xpdl1_DocumentRoot121

    @xpdl1_DocumentRoot121.setter
    def xpdl1_DocumentRoot121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot121", None)
        self.__xpdl1_DocumentRoot121 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_BasicTypeType122"):
                    opp_val = getattr(item, "xpdl1_BasicTypeType122", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_BasicTypeType122", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_BasicTypeType122"):
                    opp_val = getattr(item, "xpdl1_BasicTypeType122", None)
                    
                    setattr(item, "xpdl1_BasicTypeType122", self)
                    

    @property
    def xpdl1_DocumentRoot127(self):
        return self.__xpdl1_DocumentRoot127

    @xpdl1_DocumentRoot127.setter
    def xpdl1_DocumentRoot127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot127", None)
        self.__xpdl1_DocumentRoot127 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_ConditionType128"):
                    opp_val = getattr(item, "xpdl1_ConditionType128", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_ConditionType128", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_ConditionType128"):
                    opp_val = getattr(item, "xpdl1_ConditionType128", None)
                    
                    setattr(item, "xpdl1_ConditionType128", self)
                    

    @property
    def xpdl1_DocumentRoot243(self):
        return self.__xpdl1_DocumentRoot243

    @xpdl1_DocumentRoot243.setter
    def xpdl1_DocumentRoot243(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot243", None)
        self.__xpdl1_DocumentRoot243 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_TypeDeclarationsType"):
                    opp_val = getattr(item, "xpdl1_TypeDeclarationsType", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_TypeDeclarationsType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_TypeDeclarationsType"):
                    opp_val = getattr(item, "xpdl1_TypeDeclarationsType", None)
                    
                    setattr(item, "xpdl1_TypeDeclarationsType", self)
                    

    @property
    def xpdl1_DocumentRoot132(self):
        return self.__xpdl1_DocumentRoot132

    @xpdl1_DocumentRoot132.setter
    def xpdl1_DocumentRoot132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot132", None)
        self.__xpdl1_DocumentRoot132 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_DataFieldType133"):
                    opp_val = getattr(item, "xpdl1_DataFieldType133", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_DataFieldType133", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_DataFieldType133"):
                    opp_val = getattr(item, "xpdl1_DataFieldType133", None)
                    
                    setattr(item, "xpdl1_DataFieldType133", self)
                    

    @property
    def xpdl1_DocumentRoot141(self):
        return self.__xpdl1_DocumentRoot141

    @xpdl1_DocumentRoot141.setter
    def xpdl1_DocumentRoot141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot141", None)
        self.__xpdl1_DocumentRoot141 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_DeadlineType142"):
                    opp_val = getattr(item, "xpdl1_DeadlineType142", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_DeadlineType142", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_DeadlineType142"):
                    opp_val = getattr(item, "xpdl1_DeadlineType142", None)
                    
                    setattr(item, "xpdl1_DeadlineType142", self)
                    

    @property
    def xpdl1_DocumentRoot96(self):
        return self.__xpdl1_DocumentRoot96

    @xpdl1_DocumentRoot96.setter
    def xpdl1_DocumentRoot96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot96", None)
        self.__xpdl1_DocumentRoot96 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_ActivitiesType97"):
                    opp_val = getattr(item, "xpdl1_ActivitiesType97", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_ActivitiesType97", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_ActivitiesType97"):
                    opp_val = getattr(item, "xpdl1_ActivitiesType97", None)
                    
                    setattr(item, "xpdl1_ActivitiesType97", self)
                    

    @property
    def xpdl1_DocumentRoot233(self):
        return self.__xpdl1_DocumentRoot233

    @xpdl1_DocumentRoot233.setter
    def xpdl1_DocumentRoot233(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot233", None)
        self.__xpdl1_DocumentRoot233 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_TransitionRestrictionType"):
                    opp_val = getattr(item, "xpdl1_TransitionRestrictionType", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_TransitionRestrictionType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_TransitionRestrictionType"):
                    opp_val = getattr(item, "xpdl1_TransitionRestrictionType", None)
                    
                    setattr(item, "xpdl1_TransitionRestrictionType", self)
                    

    @property
    def xpdl1_DocumentRoot144(self):
        return self.__xpdl1_DocumentRoot144

    @xpdl1_DocumentRoot144.setter
    def xpdl1_DocumentRoot144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot144", None)
        self.__xpdl1_DocumentRoot144 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_DeclaredTypeType145"):
                    opp_val = getattr(item, "xpdl1_DeclaredTypeType145", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_DeclaredTypeType145", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_DeclaredTypeType145"):
                    opp_val = getattr(item, "xpdl1_DeclaredTypeType145", None)
                    
                    setattr(item, "xpdl1_DeclaredTypeType145", self)
                    

    @property
    def xpdl1_DocumentRoot245(self):
        return self.__xpdl1_DocumentRoot245

    @xpdl1_DocumentRoot245.setter
    def xpdl1_DocumentRoot245(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot245", None)
        self.__xpdl1_DocumentRoot245 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_UnionTypeType246"):
                    opp_val = getattr(item, "xpdl1_UnionTypeType246", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_UnionTypeType246", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_UnionTypeType246"):
                    opp_val = getattr(item, "xpdl1_UnionTypeType246", None)
                    
                    setattr(item, "xpdl1_UnionTypeType246", self)
                    

    @property
    def xpdl1_DocumentRoot180(self):
        return self.__xpdl1_DocumentRoot180

    @xpdl1_DocumentRoot180.setter
    def xpdl1_DocumentRoot180(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot180", None)
        self.__xpdl1_DocumentRoot180 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_ManualType"):
                    opp_val = getattr(item, "xpdl1_ManualType", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_ManualType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_ManualType"):
                    opp_val = getattr(item, "xpdl1_ManualType", None)
                    
                    setattr(item, "xpdl1_ManualType", self)
                    

    @property
    def xpdl1_DocumentRoot172(self):
        return self.__xpdl1_DocumentRoot172

    @xpdl1_DocumentRoot172.setter
    def xpdl1_DocumentRoot172(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot172", None)
        self.__xpdl1_DocumentRoot172 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_ImplementationType173"):
                    opp_val = getattr(item, "xpdl1_ImplementationType173", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_ImplementationType173", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_ImplementationType173"):
                    opp_val = getattr(item, "xpdl1_ImplementationType173", None)
                    
                    setattr(item, "xpdl1_ImplementationType173", self)
                    

    @property
    def xpdl1_DocumentRoot196(self):
        return self.__xpdl1_DocumentRoot196

    @xpdl1_DocumentRoot196.setter
    def xpdl1_DocumentRoot196(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot196", None)
        self.__xpdl1_DocumentRoot196 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_ProcessHeaderType"):
                    opp_val = getattr(item, "xpdl1_ProcessHeaderType", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_ProcessHeaderType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_ProcessHeaderType"):
                    opp_val = getattr(item, "xpdl1_ProcessHeaderType", None)
                    
                    setattr(item, "xpdl1_ProcessHeaderType", self)
                    

    @property
    def xpdl1_DocumentRoot119(self):
        return self.__xpdl1_DocumentRoot119

    @xpdl1_DocumentRoot119.setter
    def xpdl1_DocumentRoot119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot119", None)
        self.__xpdl1_DocumentRoot119 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_AutomaticType"):
                    opp_val = getattr(item, "xpdl1_AutomaticType", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_AutomaticType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_AutomaticType"):
                    opp_val = getattr(item, "xpdl1_AutomaticType", None)
                    
                    setattr(item, "xpdl1_AutomaticType", self)
                    

    @property
    def xpdl1_DocumentRoot221(self):
        return self.__xpdl1_DocumentRoot221

    @xpdl1_DocumentRoot221.setter
    def xpdl1_DocumentRoot221(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot221", None)
        self.__xpdl1_DocumentRoot221 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_SubFlowType"):
                    opp_val = getattr(item, "xpdl1_SubFlowType", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_SubFlowType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_SubFlowType"):
                    opp_val = getattr(item, "xpdl1_SubFlowType", None)
                    
                    setattr(item, "xpdl1_SubFlowType", self)
                    

    @property
    def xpdl1_DocumentRoot248(self):
        return self.__xpdl1_DocumentRoot248

    @xpdl1_DocumentRoot248.setter
    def xpdl1_DocumentRoot248(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot248", None)
        self.__xpdl1_DocumentRoot248 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_WorkflowProcessType"):
                    opp_val = getattr(item, "xpdl1_WorkflowProcessType", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_WorkflowProcessType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_WorkflowProcessType"):
                    opp_val = getattr(item, "xpdl1_WorkflowProcessType", None)
                    
                    setattr(item, "xpdl1_WorkflowProcessType", self)
                    

    @property
    def xpdl1_DocumentRoot205(self):
        return self.__xpdl1_DocumentRoot205

    @xpdl1_DocumentRoot205.setter
    def xpdl1_DocumentRoot205(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot205", None)
        self.__xpdl1_DocumentRoot205 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_RouteType206"):
                    opp_val = getattr(item, "xpdl1_RouteType206", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_RouteType206", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_RouteType206"):
                    opp_val = getattr(item, "xpdl1_RouteType206", None)
                    
                    setattr(item, "xpdl1_RouteType206", self)
                    

    @property
    def xpdl1_DocumentRoot105(self):
        return self.__xpdl1_DocumentRoot105

    @xpdl1_DocumentRoot105.setter
    def xpdl1_DocumentRoot105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot105", None)
        self.__xpdl1_DocumentRoot105 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_ActivitySetsType106"):
                    opp_val = getattr(item, "xpdl1_ActivitySetsType106", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_ActivitySetsType106", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_ActivitySetsType106"):
                    opp_val = getattr(item, "xpdl1_ActivitySetsType106", None)
                    
                    setattr(item, "xpdl1_ActivitySetsType106", self)
                    

    @property
    def xpdl1_DocumentRoot223(self):
        return self.__xpdl1_DocumentRoot223

    @xpdl1_DocumentRoot223.setter
    def xpdl1_DocumentRoot223(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot223", None)
        self.__xpdl1_DocumentRoot223 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_TimeEstimationType"):
                    opp_val = getattr(item, "xpdl1_TimeEstimationType", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_TimeEstimationType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_TimeEstimationType"):
                    opp_val = getattr(item, "xpdl1_TimeEstimationType", None)
                    
                    setattr(item, "xpdl1_TimeEstimationType", self)
                    

    @property
    def xpdl1_DocumentRoot213(self):
        return self.__xpdl1_DocumentRoot213

    @xpdl1_DocumentRoot213.setter
    def xpdl1_DocumentRoot213(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot213", None)
        self.__xpdl1_DocumentRoot213 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_SimulationInformationType214"):
                    opp_val = getattr(item, "xpdl1_SimulationInformationType214", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_SimulationInformationType214", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_SimulationInformationType214"):
                    opp_val = getattr(item, "xpdl1_SimulationInformationType214", None)
                    
                    setattr(item, "xpdl1_SimulationInformationType214", self)
                    

    @property
    def xpdl1_DocumentRoot201(self):
        return self.__xpdl1_DocumentRoot201

    @xpdl1_DocumentRoot201.setter
    def xpdl1_DocumentRoot201(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot201", None)
        self.__xpdl1_DocumentRoot201 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_RedefinableHeaderType"):
                    opp_val = getattr(item, "xpdl1_RedefinableHeaderType", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_RedefinableHeaderType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_RedefinableHeaderType"):
                    opp_val = getattr(item, "xpdl1_RedefinableHeaderType", None)
                    
                    setattr(item, "xpdl1_RedefinableHeaderType", self)
                    

    @property
    def xpdl1_DocumentRoot252(self):
        return self.__xpdl1_DocumentRoot252

    @xpdl1_DocumentRoot252.setter
    def xpdl1_DocumentRoot252(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot252", None)
        self.__xpdl1_DocumentRoot252 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_XpressionType253"):
                    opp_val = getattr(item, "xpdl1_XpressionType253", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_XpressionType253", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_XpressionType253"):
                    opp_val = getattr(item, "xpdl1_XpressionType253", None)
                    
                    setattr(item, "xpdl1_XpressionType253", self)
                    

    @property
    def xpdl1_DocumentRoot211(self):
        return self.__xpdl1_DocumentRoot211

    @xpdl1_DocumentRoot211.setter
    def xpdl1_DocumentRoot211(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot211", None)
        self.__xpdl1_DocumentRoot211 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_ScriptType"):
                    opp_val = getattr(item, "xpdl1_ScriptType", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_ScriptType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_ScriptType"):
                    opp_val = getattr(item, "xpdl1_ScriptType", None)
                    
                    setattr(item, "xpdl1_ScriptType", self)
                    

    @property
    def xpdl1_DocumentRoot130(self):
        return self.__xpdl1_DocumentRoot130

    @xpdl1_DocumentRoot130.setter
    def xpdl1_DocumentRoot130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot130", None)
        self.__xpdl1_DocumentRoot130 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_ConformanceClassType"):
                    opp_val = getattr(item, "xpdl1_ConformanceClassType", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_ConformanceClassType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_ConformanceClassType"):
                    opp_val = getattr(item, "xpdl1_ConformanceClassType", None)
                    
                    setattr(item, "xpdl1_ConformanceClassType", self)
                    

    @property
    def xpdl1_DocumentRoot216(self):
        return self.__xpdl1_DocumentRoot216

    @xpdl1_DocumentRoot216.setter
    def xpdl1_DocumentRoot216(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot216", None)
        self.__xpdl1_DocumentRoot216 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_SplitType"):
                    opp_val = getattr(item, "xpdl1_SplitType", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_SplitType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_SplitType"):
                    opp_val = getattr(item, "xpdl1_SplitType", None)
                    
                    setattr(item, "xpdl1_SplitType", self)
                    

    @property
    def xpdl1_DocumentRoot227(self):
        return self.__xpdl1_DocumentRoot227

    @xpdl1_DocumentRoot227.setter
    def xpdl1_DocumentRoot227(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot227", None)
        self.__xpdl1_DocumentRoot227 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_TransitionType"):
                    opp_val = getattr(item, "xpdl1_TransitionType", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_TransitionType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_TransitionType"):
                    opp_val = getattr(item, "xpdl1_TransitionType", None)
                    
                    setattr(item, "xpdl1_TransitionType", self)
                    

    @property
    def xpdl1_DocumentRoot102(self):
        return self.__xpdl1_DocumentRoot102

    @xpdl1_DocumentRoot102.setter
    def xpdl1_DocumentRoot102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot102", None)
        self.__xpdl1_DocumentRoot102 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_ActivitySetType103"):
                    opp_val = getattr(item, "xpdl1_ActivitySetType103", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_ActivitySetType103", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_ActivitySetType103"):
                    opp_val = getattr(item, "xpdl1_ActivitySetType103", None)
                    
                    setattr(item, "xpdl1_ActivitySetType103", self)
                    

    @property
    def xpdl1_DocumentRoot250(self):
        return self.__xpdl1_DocumentRoot250

    @xpdl1_DocumentRoot250.setter
    def xpdl1_DocumentRoot250(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot250", None)
        self.__xpdl1_DocumentRoot250 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_WorkflowProcessesType"):
                    opp_val = getattr(item, "xpdl1_WorkflowProcessesType", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_WorkflowProcessesType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_WorkflowProcessesType"):
                    opp_val = getattr(item, "xpdl1_WorkflowProcessesType", None)
                    
                    setattr(item, "xpdl1_WorkflowProcessesType", self)
                    

    @property
    def xpdl1_DocumentRoot186(self):
        return self.__xpdl1_DocumentRoot186

    @xpdl1_DocumentRoot186.setter
    def xpdl1_DocumentRoot186(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot186", None)
        self.__xpdl1_DocumentRoot186 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_PackageType"):
                    opp_val = getattr(item, "xpdl1_PackageType", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_PackageType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_PackageType"):
                    opp_val = getattr(item, "xpdl1_PackageType", None)
                    
                    setattr(item, "xpdl1_PackageType", self)
                    

    @property
    def xpdl1_DocumentRoot154(self):
        return self.__xpdl1_DocumentRoot154

    @xpdl1_DocumentRoot154.setter
    def xpdl1_DocumentRoot154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot154", None)
        self.__xpdl1_DocumentRoot154 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_ExtendedAttributesType155"):
                    opp_val = getattr(item, "xpdl1_ExtendedAttributesType155", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_ExtendedAttributesType155", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_ExtendedAttributesType155"):
                    opp_val = getattr(item, "xpdl1_ExtendedAttributesType155", None)
                    
                    setattr(item, "xpdl1_ExtendedAttributesType155", self)
                    

    @property
    def xpdl1_DocumentRoot99(self):
        return self.__xpdl1_DocumentRoot99

    @xpdl1_DocumentRoot99.setter
    def xpdl1_DocumentRoot99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot99", None)
        self.__xpdl1_DocumentRoot99 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_ActivityType100"):
                    opp_val = getattr(item, "xpdl1_ActivityType100", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_ActivityType100", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_ActivityType100"):
                    opp_val = getattr(item, "xpdl1_ActivityType100", None)
                    
                    setattr(item, "xpdl1_ActivityType100", self)
                    

    @property
    def xpdl1_DocumentRoot150(self):
        return self.__xpdl1_DocumentRoot150

    @xpdl1_DocumentRoot150.setter
    def xpdl1_DocumentRoot150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot150", None)
        self.__xpdl1_DocumentRoot150 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_EnumerationValueType"):
                    opp_val = getattr(item, "xpdl1_EnumerationValueType", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_EnumerationValueType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_EnumerationValueType"):
                    opp_val = getattr(item, "xpdl1_EnumerationValueType", None)
                    
                    setattr(item, "xpdl1_EnumerationValueType", self)
                    

    @property
    def xpdl1_DocumentRoot(self):
        return self.__xpdl1_DocumentRoot

    @xpdl1_DocumentRoot.setter
    def xpdl1_DocumentRoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DocumentRoot__xpdl1_DocumentRoot", None)
        self.__xpdl1_DocumentRoot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_EStringToStringMapEntry"):
                    opp_val = getattr(item, "xpdl1_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_EStringToStringMapEntry"):
                    opp_val = getattr(item, "xpdl1_EStringToStringMapEntry", None)
                    
                    setattr(item, "xpdl1_EStringToStringMapEntry", self)
                    

class xpdl1_EObject:

    pass
class xpdl1_DataTypeType:

    pass
class xpdl1_DataFieldType:

    def __init__(self, initialValue: str, length: str, description: str, id: str, isArray: str, name: str, xpdl1_DataFieldType: "xpdl1_DataFieldsType" = None, xpdl1_DataFieldType55: "xpdl1_DataTypeType" = None, xpdl1_DataFieldType57: "xpdl1_ExtendedAttributesType" = None, xpdl1_DataFieldType133: "xpdl1_DocumentRoot" = None):
        self.initialValue = initialValue
        self.length = length
        self.description = description
        self.id = id
        self.isArray = isArray
        self.name = name
        self.xpdl1_DataFieldType = xpdl1_DataFieldType
        self.xpdl1_DataFieldType55 = xpdl1_DataFieldType55
        self.xpdl1_DataFieldType57 = xpdl1_DataFieldType57
        self.xpdl1_DataFieldType133 = xpdl1_DataFieldType133
        
    @property
    def isArray(self) -> str:
        return self.__isArray

    @isArray.setter
    def isArray(self, isArray: str):
        self.__isArray = isArray

    @property
    def length(self) -> str:
        return self.__length

    @length.setter
    def length(self, length: str):
        self.__length = length

    @property
    def initialValue(self) -> str:
        return self.__initialValue

    @initialValue.setter
    def initialValue(self, initialValue: str):
        self.__initialValue = initialValue

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
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def xpdl1_DataFieldType57(self):
        return self.__xpdl1_DataFieldType57

    @xpdl1_DataFieldType57.setter
    def xpdl1_DataFieldType57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DataFieldType__xpdl1_DataFieldType57", None)
        self.__xpdl1_DataFieldType57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_ExtendedAttributesType58"):
                opp_val = getattr(old_value, "xpdl1_ExtendedAttributesType58", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_ExtendedAttributesType58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_ExtendedAttributesType58"):
                opp_val = getattr(value, "xpdl1_ExtendedAttributesType58", None)
                setattr(value, "xpdl1_ExtendedAttributesType58", self)

    @property
    def xpdl1_DataFieldType(self):
        return self.__xpdl1_DataFieldType

    @xpdl1_DataFieldType.setter
    def xpdl1_DataFieldType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DataFieldType__xpdl1_DataFieldType", None)
        self.__xpdl1_DataFieldType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_DataFieldsType"):
                opp_val = getattr(old_value, "xpdl1_DataFieldsType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_DataFieldsType"):
                opp_val = getattr(value, "xpdl1_DataFieldsType", None)
                if opp_val is None:
                    setattr(value, "xpdl1_DataFieldsType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xpdl1_DataFieldType133(self):
        return self.__xpdl1_DataFieldType133

    @xpdl1_DataFieldType133.setter
    def xpdl1_DataFieldType133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DataFieldType__xpdl1_DataFieldType133", None)
        self.__xpdl1_DataFieldType133 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_DocumentRoot132"):
                opp_val = getattr(old_value, "xpdl1_DocumentRoot132", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_DocumentRoot132"):
                opp_val = getattr(value, "xpdl1_DocumentRoot132", None)
                if opp_val is None:
                    setattr(value, "xpdl1_DocumentRoot132", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xpdl1_DataFieldType55(self):
        return self.__xpdl1_DataFieldType55

    @xpdl1_DataFieldType55.setter
    def xpdl1_DataFieldType55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DataFieldType__xpdl1_DataFieldType55", None)
        self.__xpdl1_DataFieldType55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_DataTypeType"):
                opp_val = getattr(old_value, "xpdl1_DataTypeType", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_DataTypeType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_DataTypeType"):
                opp_val = getattr(value, "xpdl1_DataTypeType", None)
                setattr(value, "xpdl1_DataTypeType", self)

class xpdl1_DataFieldsType:

    pass
class xpdl1_ConformanceClassType:

    def __init__(self, graphConformance: str, xpdl1_ConformanceClassType: "xpdl1_DocumentRoot" = None, xpdl1_ConformanceClassType349: "xpdl1_PackageType" = None):
        self.graphConformance = graphConformance
        self.xpdl1_ConformanceClassType = xpdl1_ConformanceClassType
        self.xpdl1_ConformanceClassType349 = xpdl1_ConformanceClassType349
        
    @property
    def graphConformance(self) -> str:
        return self.__graphConformance

    @graphConformance.setter
    def graphConformance(self, graphConformance: str):
        self.__graphConformance = graphConformance

    @property
    def xpdl1_ConformanceClassType(self):
        return self.__xpdl1_ConformanceClassType

    @xpdl1_ConformanceClassType.setter
    def xpdl1_ConformanceClassType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ConformanceClassType__xpdl1_ConformanceClassType", None)
        self.__xpdl1_ConformanceClassType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_DocumentRoot130"):
                opp_val = getattr(old_value, "xpdl1_DocumentRoot130", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_DocumentRoot130"):
                opp_val = getattr(value, "xpdl1_DocumentRoot130", None)
                if opp_val is None:
                    setattr(value, "xpdl1_DocumentRoot130", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xpdl1_ConformanceClassType349(self):
        return self.__xpdl1_ConformanceClassType349

    @xpdl1_ConformanceClassType349.setter
    def xpdl1_ConformanceClassType349(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ConformanceClassType__xpdl1_ConformanceClassType349", None)
        self.__xpdl1_ConformanceClassType349 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_PackageType348"):
                opp_val = getattr(old_value, "xpdl1_PackageType348", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_PackageType348", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_PackageType348"):
                opp_val = getattr(value, "xpdl1_PackageType348", None)
                setattr(value, "xpdl1_PackageType348", self)

class xpdl1_XpressionType:

    def __init__(self, mixed: str, any: str, group: str, xpdl1_XpressionType: "xpdl1_ConditionType" = None, xpdl1_XpressionType253: "xpdl1_DocumentRoot" = None):
        self.mixed = mixed
        self.any = any
        self.group = group
        self.xpdl1_XpressionType = xpdl1_XpressionType
        self.xpdl1_XpressionType253 = xpdl1_XpressionType253
        
    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

    @property
    def xpdl1_XpressionType(self):
        return self.__xpdl1_XpressionType

    @xpdl1_XpressionType.setter
    def xpdl1_XpressionType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_XpressionType__xpdl1_XpressionType", None)
        self.__xpdl1_XpressionType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_ConditionType"):
                opp_val = getattr(old_value, "xpdl1_ConditionType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_ConditionType"):
                opp_val = getattr(value, "xpdl1_ConditionType", None)
                if opp_val is None:
                    setattr(value, "xpdl1_ConditionType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xpdl1_XpressionType253(self):
        return self.__xpdl1_XpressionType253

    @xpdl1_XpressionType253.setter
    def xpdl1_XpressionType253(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_XpressionType__xpdl1_XpressionType253", None)
        self.__xpdl1_XpressionType253 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_DocumentRoot252"):
                opp_val = getattr(old_value, "xpdl1_DocumentRoot252", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_DocumentRoot252"):
                opp_val = getattr(value, "xpdl1_DocumentRoot252", None)
                if opp_val is None:
                    setattr(value, "xpdl1_DocumentRoot252", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xpdl1_ConditionType:

    def __init__(self, mixed: str, group: str, type: str, xpdl1_ConditionType: set["xpdl1_XpressionType"] = None, xpdl1_ConditionType128: "xpdl1_DocumentRoot" = None, xpdl1_ConditionType433: "xpdl1_TransitionType" = None):
        self.mixed = mixed
        self.group = group
        self.type = type
        self.xpdl1_ConditionType = xpdl1_ConditionType if xpdl1_ConditionType is not None else set()
        self.xpdl1_ConditionType128 = xpdl1_ConditionType128
        self.xpdl1_ConditionType433 = xpdl1_ConditionType433
        
    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def xpdl1_ConditionType(self):
        return self.__xpdl1_ConditionType

    @xpdl1_ConditionType.setter
    def xpdl1_ConditionType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ConditionType__xpdl1_ConditionType", None)
        self.__xpdl1_ConditionType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_XpressionType"):
                    opp_val = getattr(item, "xpdl1_XpressionType", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_XpressionType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_XpressionType"):
                    opp_val = getattr(item, "xpdl1_XpressionType", None)
                    
                    setattr(item, "xpdl1_XpressionType", self)
                    

    @property
    def xpdl1_ConditionType433(self):
        return self.__xpdl1_ConditionType433

    @xpdl1_ConditionType433.setter
    def xpdl1_ConditionType433(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ConditionType__xpdl1_ConditionType433", None)
        self.__xpdl1_ConditionType433 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_TransitionType432"):
                opp_val = getattr(old_value, "xpdl1_TransitionType432", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_TransitionType432", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_TransitionType432"):
                opp_val = getattr(value, "xpdl1_TransitionType432", None)
                setattr(value, "xpdl1_TransitionType432", self)

    @property
    def xpdl1_ConditionType128(self):
        return self.__xpdl1_ConditionType128

    @xpdl1_ConditionType128.setter
    def xpdl1_ConditionType128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ConditionType__xpdl1_ConditionType128", None)
        self.__xpdl1_ConditionType128 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_DocumentRoot127"):
                opp_val = getattr(old_value, "xpdl1_DocumentRoot127", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_DocumentRoot127"):
                opp_val = getattr(value, "xpdl1_DocumentRoot127", None)
                if opp_val is None:
                    setattr(value, "xpdl1_DocumentRoot127", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xpdl1_AutomaticType:

    pass
class xpdl1_ListTypeType:

    pass
class xpdl1_EnumerationTypeType:

    pass
class xpdl1_UnionTypeType:

    pass
class xpdl1_RecordTypeType:

    pass
class xpdl1_SchemaTypeType:

    def __init__(self, any: str, xpdl1_SchemaTypeType: "xpdl1_ArrayTypeType" = None, xpdl1_SchemaTypeType67: "xpdl1_DataTypeType" = None, xpdl1_SchemaTypeType209: "xpdl1_DocumentRoot" = None, xpdl1_SchemaTypeType295: "xpdl1_ListTypeType" = None, xpdl1_SchemaTypeType322: "xpdl1_MemberType" = None, xpdl1_SchemaTypeType448: "xpdl1_TypeDeclarationType" = None):
        self.any = any
        self.xpdl1_SchemaTypeType = xpdl1_SchemaTypeType
        self.xpdl1_SchemaTypeType67 = xpdl1_SchemaTypeType67
        self.xpdl1_SchemaTypeType209 = xpdl1_SchemaTypeType209
        self.xpdl1_SchemaTypeType295 = xpdl1_SchemaTypeType295
        self.xpdl1_SchemaTypeType322 = xpdl1_SchemaTypeType322
        self.xpdl1_SchemaTypeType448 = xpdl1_SchemaTypeType448
        
    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

    @property
    def xpdl1_SchemaTypeType(self):
        return self.__xpdl1_SchemaTypeType

    @xpdl1_SchemaTypeType.setter
    def xpdl1_SchemaTypeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_SchemaTypeType__xpdl1_SchemaTypeType", None)
        self.__xpdl1_SchemaTypeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_ArrayTypeType37"):
                opp_val = getattr(old_value, "xpdl1_ArrayTypeType37", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_ArrayTypeType37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_ArrayTypeType37"):
                opp_val = getattr(value, "xpdl1_ArrayTypeType37", None)
                setattr(value, "xpdl1_ArrayTypeType37", self)

    @property
    def xpdl1_SchemaTypeType448(self):
        return self.__xpdl1_SchemaTypeType448

    @xpdl1_SchemaTypeType448.setter
    def xpdl1_SchemaTypeType448(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_SchemaTypeType__xpdl1_SchemaTypeType448", None)
        self.__xpdl1_SchemaTypeType448 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_TypeDeclarationType447"):
                opp_val = getattr(old_value, "xpdl1_TypeDeclarationType447", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_TypeDeclarationType447", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_TypeDeclarationType447"):
                opp_val = getattr(value, "xpdl1_TypeDeclarationType447", None)
                setattr(value, "xpdl1_TypeDeclarationType447", self)

    @property
    def xpdl1_SchemaTypeType295(self):
        return self.__xpdl1_SchemaTypeType295

    @xpdl1_SchemaTypeType295.setter
    def xpdl1_SchemaTypeType295(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_SchemaTypeType__xpdl1_SchemaTypeType295", None)
        self.__xpdl1_SchemaTypeType295 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_ListTypeType294"):
                opp_val = getattr(old_value, "xpdl1_ListTypeType294", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_ListTypeType294", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_ListTypeType294"):
                opp_val = getattr(value, "xpdl1_ListTypeType294", None)
                setattr(value, "xpdl1_ListTypeType294", self)

    @property
    def xpdl1_SchemaTypeType209(self):
        return self.__xpdl1_SchemaTypeType209

    @xpdl1_SchemaTypeType209.setter
    def xpdl1_SchemaTypeType209(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_SchemaTypeType__xpdl1_SchemaTypeType209", None)
        self.__xpdl1_SchemaTypeType209 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_DocumentRoot208"):
                opp_val = getattr(old_value, "xpdl1_DocumentRoot208", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_DocumentRoot208"):
                opp_val = getattr(value, "xpdl1_DocumentRoot208", None)
                if opp_val is None:
                    setattr(value, "xpdl1_DocumentRoot208", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xpdl1_SchemaTypeType322(self):
        return self.__xpdl1_SchemaTypeType322

    @xpdl1_SchemaTypeType322.setter
    def xpdl1_SchemaTypeType322(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_SchemaTypeType__xpdl1_SchemaTypeType322", None)
        self.__xpdl1_SchemaTypeType322 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_MemberType321"):
                opp_val = getattr(old_value, "xpdl1_MemberType321", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_MemberType321", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_MemberType321"):
                opp_val = getattr(value, "xpdl1_MemberType321", None)
                setattr(value, "xpdl1_MemberType321", self)

    @property
    def xpdl1_SchemaTypeType67(self):
        return self.__xpdl1_SchemaTypeType67

    @xpdl1_SchemaTypeType67.setter
    def xpdl1_SchemaTypeType67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_SchemaTypeType__xpdl1_SchemaTypeType67", None)
        self.__xpdl1_SchemaTypeType67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_DataTypeType66"):
                opp_val = getattr(old_value, "xpdl1_DataTypeType66", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_DataTypeType66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_DataTypeType66"):
                opp_val = getattr(value, "xpdl1_DataTypeType66", None)
                setattr(value, "xpdl1_DataTypeType66", self)

class xpdl1_DeclaredTypeType:

    def __init__(self, id: str, xpdl1_DeclaredTypeType: "xpdl1_ArrayTypeType" = None, xpdl1_DeclaredTypeType64: "xpdl1_DataTypeType" = None, xpdl1_DeclaredTypeType145: "xpdl1_DocumentRoot" = None, xpdl1_DeclaredTypeType292: "xpdl1_ListTypeType" = None, xpdl1_DeclaredTypeType319: "xpdl1_MemberType" = None, xpdl1_DeclaredTypeType445: "xpdl1_TypeDeclarationType" = None):
        self.id = id
        self.xpdl1_DeclaredTypeType = xpdl1_DeclaredTypeType
        self.xpdl1_DeclaredTypeType64 = xpdl1_DeclaredTypeType64
        self.xpdl1_DeclaredTypeType145 = xpdl1_DeclaredTypeType145
        self.xpdl1_DeclaredTypeType292 = xpdl1_DeclaredTypeType292
        self.xpdl1_DeclaredTypeType319 = xpdl1_DeclaredTypeType319
        self.xpdl1_DeclaredTypeType445 = xpdl1_DeclaredTypeType445
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def xpdl1_DeclaredTypeType319(self):
        return self.__xpdl1_DeclaredTypeType319

    @xpdl1_DeclaredTypeType319.setter
    def xpdl1_DeclaredTypeType319(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DeclaredTypeType__xpdl1_DeclaredTypeType319", None)
        self.__xpdl1_DeclaredTypeType319 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_MemberType318"):
                opp_val = getattr(old_value, "xpdl1_MemberType318", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_MemberType318", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_MemberType318"):
                opp_val = getattr(value, "xpdl1_MemberType318", None)
                setattr(value, "xpdl1_MemberType318", self)

    @property
    def xpdl1_DeclaredTypeType(self):
        return self.__xpdl1_DeclaredTypeType

    @xpdl1_DeclaredTypeType.setter
    def xpdl1_DeclaredTypeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DeclaredTypeType__xpdl1_DeclaredTypeType", None)
        self.__xpdl1_DeclaredTypeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_ArrayTypeType35"):
                opp_val = getattr(old_value, "xpdl1_ArrayTypeType35", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_ArrayTypeType35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_ArrayTypeType35"):
                opp_val = getattr(value, "xpdl1_ArrayTypeType35", None)
                setattr(value, "xpdl1_ArrayTypeType35", self)

    @property
    def xpdl1_DeclaredTypeType292(self):
        return self.__xpdl1_DeclaredTypeType292

    @xpdl1_DeclaredTypeType292.setter
    def xpdl1_DeclaredTypeType292(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DeclaredTypeType__xpdl1_DeclaredTypeType292", None)
        self.__xpdl1_DeclaredTypeType292 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_ListTypeType291"):
                opp_val = getattr(old_value, "xpdl1_ListTypeType291", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_ListTypeType291", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_ListTypeType291"):
                opp_val = getattr(value, "xpdl1_ListTypeType291", None)
                setattr(value, "xpdl1_ListTypeType291", self)

    @property
    def xpdl1_DeclaredTypeType145(self):
        return self.__xpdl1_DeclaredTypeType145

    @xpdl1_DeclaredTypeType145.setter
    def xpdl1_DeclaredTypeType145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DeclaredTypeType__xpdl1_DeclaredTypeType145", None)
        self.__xpdl1_DeclaredTypeType145 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_DocumentRoot144"):
                opp_val = getattr(old_value, "xpdl1_DocumentRoot144", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_DocumentRoot144"):
                opp_val = getattr(value, "xpdl1_DocumentRoot144", None)
                if opp_val is None:
                    setattr(value, "xpdl1_DocumentRoot144", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xpdl1_DeclaredTypeType64(self):
        return self.__xpdl1_DeclaredTypeType64

    @xpdl1_DeclaredTypeType64.setter
    def xpdl1_DeclaredTypeType64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DeclaredTypeType__xpdl1_DeclaredTypeType64", None)
        self.__xpdl1_DeclaredTypeType64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_DataTypeType63"):
                opp_val = getattr(old_value, "xpdl1_DataTypeType63", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_DataTypeType63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_DataTypeType63"):
                opp_val = getattr(value, "xpdl1_DataTypeType63", None)
                setattr(value, "xpdl1_DataTypeType63", self)

    @property
    def xpdl1_DeclaredTypeType445(self):
        return self.__xpdl1_DeclaredTypeType445

    @xpdl1_DeclaredTypeType445.setter
    def xpdl1_DeclaredTypeType445(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DeclaredTypeType__xpdl1_DeclaredTypeType445", None)
        self.__xpdl1_DeclaredTypeType445 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_TypeDeclarationType444"):
                opp_val = getattr(old_value, "xpdl1_TypeDeclarationType444", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_TypeDeclarationType444", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_TypeDeclarationType444"):
                opp_val = getattr(value, "xpdl1_TypeDeclarationType444", None)
                setattr(value, "xpdl1_TypeDeclarationType444", self)

class xpdl1_BasicTypeType:

    def __init__(self, type: str, xpdl1_BasicTypeType: "xpdl1_ArrayTypeType" = None, xpdl1_BasicTypeType61: "xpdl1_DataTypeType" = None, xpdl1_BasicTypeType122: "xpdl1_DocumentRoot" = None, xpdl1_BasicTypeType289: "xpdl1_ListTypeType" = None, xpdl1_BasicTypeType316: "xpdl1_MemberType" = None, xpdl1_BasicTypeType442: "xpdl1_TypeDeclarationType" = None):
        self.type = type
        self.xpdl1_BasicTypeType = xpdl1_BasicTypeType
        self.xpdl1_BasicTypeType61 = xpdl1_BasicTypeType61
        self.xpdl1_BasicTypeType122 = xpdl1_BasicTypeType122
        self.xpdl1_BasicTypeType289 = xpdl1_BasicTypeType289
        self.xpdl1_BasicTypeType316 = xpdl1_BasicTypeType316
        self.xpdl1_BasicTypeType442 = xpdl1_BasicTypeType442
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def xpdl1_BasicTypeType316(self):
        return self.__xpdl1_BasicTypeType316

    @xpdl1_BasicTypeType316.setter
    def xpdl1_BasicTypeType316(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_BasicTypeType__xpdl1_BasicTypeType316", None)
        self.__xpdl1_BasicTypeType316 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_MemberType315"):
                opp_val = getattr(old_value, "xpdl1_MemberType315", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_MemberType315", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_MemberType315"):
                opp_val = getattr(value, "xpdl1_MemberType315", None)
                setattr(value, "xpdl1_MemberType315", self)

    @property
    def xpdl1_BasicTypeType(self):
        return self.__xpdl1_BasicTypeType

    @xpdl1_BasicTypeType.setter
    def xpdl1_BasicTypeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_BasicTypeType__xpdl1_BasicTypeType", None)
        self.__xpdl1_BasicTypeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_ArrayTypeType"):
                opp_val = getattr(old_value, "xpdl1_ArrayTypeType", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_ArrayTypeType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_ArrayTypeType"):
                opp_val = getattr(value, "xpdl1_ArrayTypeType", None)
                setattr(value, "xpdl1_ArrayTypeType", self)

    @property
    def xpdl1_BasicTypeType442(self):
        return self.__xpdl1_BasicTypeType442

    @xpdl1_BasicTypeType442.setter
    def xpdl1_BasicTypeType442(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_BasicTypeType__xpdl1_BasicTypeType442", None)
        self.__xpdl1_BasicTypeType442 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_TypeDeclarationType441"):
                opp_val = getattr(old_value, "xpdl1_TypeDeclarationType441", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_TypeDeclarationType441", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_TypeDeclarationType441"):
                opp_val = getattr(value, "xpdl1_TypeDeclarationType441", None)
                setattr(value, "xpdl1_TypeDeclarationType441", self)

    @property
    def xpdl1_BasicTypeType122(self):
        return self.__xpdl1_BasicTypeType122

    @xpdl1_BasicTypeType122.setter
    def xpdl1_BasicTypeType122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_BasicTypeType__xpdl1_BasicTypeType122", None)
        self.__xpdl1_BasicTypeType122 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_DocumentRoot121"):
                opp_val = getattr(old_value, "xpdl1_DocumentRoot121", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_DocumentRoot121"):
                opp_val = getattr(value, "xpdl1_DocumentRoot121", None)
                if opp_val is None:
                    setattr(value, "xpdl1_DocumentRoot121", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xpdl1_BasicTypeType61(self):
        return self.__xpdl1_BasicTypeType61

    @xpdl1_BasicTypeType61.setter
    def xpdl1_BasicTypeType61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_BasicTypeType__xpdl1_BasicTypeType61", None)
        self.__xpdl1_BasicTypeType61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_DataTypeType60"):
                opp_val = getattr(old_value, "xpdl1_DataTypeType60", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_DataTypeType60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_DataTypeType60"):
                opp_val = getattr(value, "xpdl1_DataTypeType60", None)
                setattr(value, "xpdl1_DataTypeType60", self)

    @property
    def xpdl1_BasicTypeType289(self):
        return self.__xpdl1_BasicTypeType289

    @xpdl1_BasicTypeType289.setter
    def xpdl1_BasicTypeType289(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_BasicTypeType__xpdl1_BasicTypeType289", None)
        self.__xpdl1_BasicTypeType289 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_ListTypeType288"):
                opp_val = getattr(old_value, "xpdl1_ListTypeType288", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_ListTypeType288", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_ListTypeType288"):
                opp_val = getattr(value, "xpdl1_ListTypeType288", None)
                setattr(value, "xpdl1_ListTypeType288", self)

class xpdl1_ArrayTypeType:

    def __init__(self, lowerIndex: str, upperIndex: str, xpdl1_ArrayTypeType: "xpdl1_BasicTypeType" = None, xpdl1_ArrayTypeType35: "xpdl1_DeclaredTypeType" = None, xpdl1_ArrayTypeType37: "xpdl1_SchemaTypeType" = None, xpdl1_ArrayTypeType42: "xpdl1_RecordTypeType" = None, xpdl1_ArrayTypeType44: "xpdl1_UnionTypeType" = None, xpdl1_ArrayTypeType46: "xpdl1_EnumerationTypeType" = None, xpdl1_ArrayTypeType49: "xpdl1_ArrayTypeType" = None, xpdl1_ArrayTypeType47: "xpdl1_ArrayTypeType" = None, xpdl1_ArrayTypeType51: "xpdl1_ListTypeType" = None, xpdl1_ArrayTypeType39: "xpdl1_ExternalReferenceType" = None, xpdl1_ArrayTypeType82: "xpdl1_DataTypeType" = None, xpdl1_ArrayTypeType117: "xpdl1_DocumentRoot" = None, xpdl1_ArrayTypeType310: "xpdl1_ListTypeType" = None, xpdl1_ArrayTypeType337: "xpdl1_MemberType" = None, xpdl1_ArrayTypeType463: "xpdl1_TypeDeclarationType" = None):
        self.lowerIndex = lowerIndex
        self.upperIndex = upperIndex
        self.xpdl1_ArrayTypeType = xpdl1_ArrayTypeType
        self.xpdl1_ArrayTypeType35 = xpdl1_ArrayTypeType35
        self.xpdl1_ArrayTypeType37 = xpdl1_ArrayTypeType37
        self.xpdl1_ArrayTypeType42 = xpdl1_ArrayTypeType42
        self.xpdl1_ArrayTypeType44 = xpdl1_ArrayTypeType44
        self.xpdl1_ArrayTypeType46 = xpdl1_ArrayTypeType46
        self.xpdl1_ArrayTypeType49 = xpdl1_ArrayTypeType49
        self.xpdl1_ArrayTypeType47 = xpdl1_ArrayTypeType47
        self.xpdl1_ArrayTypeType51 = xpdl1_ArrayTypeType51
        self.xpdl1_ArrayTypeType39 = xpdl1_ArrayTypeType39
        self.xpdl1_ArrayTypeType82 = xpdl1_ArrayTypeType82
        self.xpdl1_ArrayTypeType117 = xpdl1_ArrayTypeType117
        self.xpdl1_ArrayTypeType310 = xpdl1_ArrayTypeType310
        self.xpdl1_ArrayTypeType337 = xpdl1_ArrayTypeType337
        self.xpdl1_ArrayTypeType463 = xpdl1_ArrayTypeType463
        
    @property
    def lowerIndex(self) -> str:
        return self.__lowerIndex

    @lowerIndex.setter
    def lowerIndex(self, lowerIndex: str):
        self.__lowerIndex = lowerIndex

    @property
    def upperIndex(self) -> str:
        return self.__upperIndex

    @upperIndex.setter
    def upperIndex(self, upperIndex: str):
        self.__upperIndex = upperIndex

    @property
    def xpdl1_ArrayTypeType46(self):
        return self.__xpdl1_ArrayTypeType46

    @xpdl1_ArrayTypeType46.setter
    def xpdl1_ArrayTypeType46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ArrayTypeType__xpdl1_ArrayTypeType46", None)
        self.__xpdl1_ArrayTypeType46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_EnumerationTypeType"):
                opp_val = getattr(old_value, "xpdl1_EnumerationTypeType", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_EnumerationTypeType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_EnumerationTypeType"):
                opp_val = getattr(value, "xpdl1_EnumerationTypeType", None)
                setattr(value, "xpdl1_EnumerationTypeType", self)

    @property
    def xpdl1_ArrayTypeType37(self):
        return self.__xpdl1_ArrayTypeType37

    @xpdl1_ArrayTypeType37.setter
    def xpdl1_ArrayTypeType37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ArrayTypeType__xpdl1_ArrayTypeType37", None)
        self.__xpdl1_ArrayTypeType37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_SchemaTypeType"):
                opp_val = getattr(old_value, "xpdl1_SchemaTypeType", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_SchemaTypeType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_SchemaTypeType"):
                opp_val = getattr(value, "xpdl1_SchemaTypeType", None)
                setattr(value, "xpdl1_SchemaTypeType", self)

    @property
    def xpdl1_ArrayTypeType49(self):
        return self.__xpdl1_ArrayTypeType49

    @xpdl1_ArrayTypeType49.setter
    def xpdl1_ArrayTypeType49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ArrayTypeType__xpdl1_ArrayTypeType49", None)
        self.__xpdl1_ArrayTypeType49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_ArrayTypeType47"):
                opp_val = getattr(old_value, "xpdl1_ArrayTypeType47", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_ArrayTypeType47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_ArrayTypeType47"):
                opp_val = getattr(value, "xpdl1_ArrayTypeType47", None)
                setattr(value, "xpdl1_ArrayTypeType47", self)

    @property
    def xpdl1_ArrayTypeType44(self):
        return self.__xpdl1_ArrayTypeType44

    @xpdl1_ArrayTypeType44.setter
    def xpdl1_ArrayTypeType44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ArrayTypeType__xpdl1_ArrayTypeType44", None)
        self.__xpdl1_ArrayTypeType44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_UnionTypeType"):
                opp_val = getattr(old_value, "xpdl1_UnionTypeType", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_UnionTypeType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_UnionTypeType"):
                opp_val = getattr(value, "xpdl1_UnionTypeType", None)
                setattr(value, "xpdl1_UnionTypeType", self)

    @property
    def xpdl1_ArrayTypeType47(self):
        return self.__xpdl1_ArrayTypeType47

    @xpdl1_ArrayTypeType47.setter
    def xpdl1_ArrayTypeType47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ArrayTypeType__xpdl1_ArrayTypeType47", None)
        self.__xpdl1_ArrayTypeType47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_ArrayTypeType49"):
                opp_val = getattr(old_value, "xpdl1_ArrayTypeType49", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_ArrayTypeType49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_ArrayTypeType49"):
                opp_val = getattr(value, "xpdl1_ArrayTypeType49", None)
                setattr(value, "xpdl1_ArrayTypeType49", self)

    @property
    def xpdl1_ArrayTypeType82(self):
        return self.__xpdl1_ArrayTypeType82

    @xpdl1_ArrayTypeType82.setter
    def xpdl1_ArrayTypeType82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ArrayTypeType__xpdl1_ArrayTypeType82", None)
        self.__xpdl1_ArrayTypeType82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_DataTypeType81"):
                opp_val = getattr(old_value, "xpdl1_DataTypeType81", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_DataTypeType81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_DataTypeType81"):
                opp_val = getattr(value, "xpdl1_DataTypeType81", None)
                setattr(value, "xpdl1_DataTypeType81", self)

    @property
    def xpdl1_ArrayTypeType310(self):
        return self.__xpdl1_ArrayTypeType310

    @xpdl1_ArrayTypeType310.setter
    def xpdl1_ArrayTypeType310(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ArrayTypeType__xpdl1_ArrayTypeType310", None)
        self.__xpdl1_ArrayTypeType310 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_ListTypeType309"):
                opp_val = getattr(old_value, "xpdl1_ListTypeType309", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_ListTypeType309", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_ListTypeType309"):
                opp_val = getattr(value, "xpdl1_ListTypeType309", None)
                setattr(value, "xpdl1_ListTypeType309", self)

    @property
    def xpdl1_ArrayTypeType117(self):
        return self.__xpdl1_ArrayTypeType117

    @xpdl1_ArrayTypeType117.setter
    def xpdl1_ArrayTypeType117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ArrayTypeType__xpdl1_ArrayTypeType117", None)
        self.__xpdl1_ArrayTypeType117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_DocumentRoot116"):
                opp_val = getattr(old_value, "xpdl1_DocumentRoot116", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_DocumentRoot116"):
                opp_val = getattr(value, "xpdl1_DocumentRoot116", None)
                if opp_val is None:
                    setattr(value, "xpdl1_DocumentRoot116", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xpdl1_ArrayTypeType(self):
        return self.__xpdl1_ArrayTypeType

    @xpdl1_ArrayTypeType.setter
    def xpdl1_ArrayTypeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ArrayTypeType__xpdl1_ArrayTypeType", None)
        self.__xpdl1_ArrayTypeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_BasicTypeType"):
                opp_val = getattr(old_value, "xpdl1_BasicTypeType", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_BasicTypeType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_BasicTypeType"):
                opp_val = getattr(value, "xpdl1_BasicTypeType", None)
                setattr(value, "xpdl1_BasicTypeType", self)

    @property
    def xpdl1_ArrayTypeType42(self):
        return self.__xpdl1_ArrayTypeType42

    @xpdl1_ArrayTypeType42.setter
    def xpdl1_ArrayTypeType42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ArrayTypeType__xpdl1_ArrayTypeType42", None)
        self.__xpdl1_ArrayTypeType42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_RecordTypeType"):
                opp_val = getattr(old_value, "xpdl1_RecordTypeType", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_RecordTypeType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_RecordTypeType"):
                opp_val = getattr(value, "xpdl1_RecordTypeType", None)
                setattr(value, "xpdl1_RecordTypeType", self)

    @property
    def xpdl1_ArrayTypeType51(self):
        return self.__xpdl1_ArrayTypeType51

    @xpdl1_ArrayTypeType51.setter
    def xpdl1_ArrayTypeType51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ArrayTypeType__xpdl1_ArrayTypeType51", None)
        self.__xpdl1_ArrayTypeType51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_ListTypeType"):
                opp_val = getattr(old_value, "xpdl1_ListTypeType", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_ListTypeType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_ListTypeType"):
                opp_val = getattr(value, "xpdl1_ListTypeType", None)
                setattr(value, "xpdl1_ListTypeType", self)

    @property
    def xpdl1_ArrayTypeType337(self):
        return self.__xpdl1_ArrayTypeType337

    @xpdl1_ArrayTypeType337.setter
    def xpdl1_ArrayTypeType337(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ArrayTypeType__xpdl1_ArrayTypeType337", None)
        self.__xpdl1_ArrayTypeType337 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_MemberType336"):
                opp_val = getattr(old_value, "xpdl1_MemberType336", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_MemberType336", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_MemberType336"):
                opp_val = getattr(value, "xpdl1_MemberType336", None)
                setattr(value, "xpdl1_MemberType336", self)

    @property
    def xpdl1_ArrayTypeType463(self):
        return self.__xpdl1_ArrayTypeType463

    @xpdl1_ArrayTypeType463.setter
    def xpdl1_ArrayTypeType463(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ArrayTypeType__xpdl1_ArrayTypeType463", None)
        self.__xpdl1_ArrayTypeType463 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_TypeDeclarationType462"):
                opp_val = getattr(old_value, "xpdl1_TypeDeclarationType462", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_TypeDeclarationType462", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_TypeDeclarationType462"):
                opp_val = getattr(value, "xpdl1_TypeDeclarationType462", None)
                setattr(value, "xpdl1_TypeDeclarationType462", self)

    @property
    def xpdl1_ArrayTypeType39(self):
        return self.__xpdl1_ArrayTypeType39

    @xpdl1_ArrayTypeType39.setter
    def xpdl1_ArrayTypeType39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ArrayTypeType__xpdl1_ArrayTypeType39", None)
        self.__xpdl1_ArrayTypeType39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_ExternalReferenceType40"):
                opp_val = getattr(old_value, "xpdl1_ExternalReferenceType40", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_ExternalReferenceType40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_ExternalReferenceType40"):
                opp_val = getattr(value, "xpdl1_ExternalReferenceType40", None)
                setattr(value, "xpdl1_ExternalReferenceType40", self)

    @property
    def xpdl1_ArrayTypeType35(self):
        return self.__xpdl1_ArrayTypeType35

    @xpdl1_ArrayTypeType35.setter
    def xpdl1_ArrayTypeType35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ArrayTypeType__xpdl1_ArrayTypeType35", None)
        self.__xpdl1_ArrayTypeType35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_DeclaredTypeType"):
                opp_val = getattr(old_value, "xpdl1_DeclaredTypeType", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_DeclaredTypeType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_DeclaredTypeType"):
                opp_val = getattr(value, "xpdl1_DeclaredTypeType", None)
                setattr(value, "xpdl1_DeclaredTypeType", self)

class xpdl1_ExternalReferenceType:

    def __init__(self, location: str, namespace: str, xref: str, xpdl1_ExternalReferenceType: "xpdl1_ApplicationType" = None, xpdl1_ExternalReferenceType40: "xpdl1_ArrayTypeType" = None, xpdl1_ExternalReferenceType70: "xpdl1_DataTypeType" = None, xpdl1_ExternalReferenceType162: "xpdl1_DocumentRoot" = None, xpdl1_ExternalReferenceType298: "xpdl1_ListTypeType" = None, xpdl1_ExternalReferenceType325: "xpdl1_MemberType" = None, xpdl1_ExternalReferenceType382: "xpdl1_ParticipantType" = None, xpdl1_ExternalReferenceType451: "xpdl1_TypeDeclarationType" = None):
        self.location = location
        self.namespace = namespace
        self.xref = xref
        self.xpdl1_ExternalReferenceType = xpdl1_ExternalReferenceType
        self.xpdl1_ExternalReferenceType40 = xpdl1_ExternalReferenceType40
        self.xpdl1_ExternalReferenceType70 = xpdl1_ExternalReferenceType70
        self.xpdl1_ExternalReferenceType162 = xpdl1_ExternalReferenceType162
        self.xpdl1_ExternalReferenceType298 = xpdl1_ExternalReferenceType298
        self.xpdl1_ExternalReferenceType325 = xpdl1_ExternalReferenceType325
        self.xpdl1_ExternalReferenceType382 = xpdl1_ExternalReferenceType382
        self.xpdl1_ExternalReferenceType451 = xpdl1_ExternalReferenceType451
        
    @property
    def namespace(self) -> str:
        return self.__namespace

    @namespace.setter
    def namespace(self, namespace: str):
        self.__namespace = namespace

    @property
    def xref(self) -> str:
        return self.__xref

    @xref.setter
    def xref(self, xref: str):
        self.__xref = xref

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def xpdl1_ExternalReferenceType325(self):
        return self.__xpdl1_ExternalReferenceType325

    @xpdl1_ExternalReferenceType325.setter
    def xpdl1_ExternalReferenceType325(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ExternalReferenceType__xpdl1_ExternalReferenceType325", None)
        self.__xpdl1_ExternalReferenceType325 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_MemberType324"):
                opp_val = getattr(old_value, "xpdl1_MemberType324", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_MemberType324", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_MemberType324"):
                opp_val = getattr(value, "xpdl1_MemberType324", None)
                setattr(value, "xpdl1_MemberType324", self)

    @property
    def xpdl1_ExternalReferenceType382(self):
        return self.__xpdl1_ExternalReferenceType382

    @xpdl1_ExternalReferenceType382.setter
    def xpdl1_ExternalReferenceType382(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ExternalReferenceType__xpdl1_ExternalReferenceType382", None)
        self.__xpdl1_ExternalReferenceType382 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_ParticipantType381"):
                opp_val = getattr(old_value, "xpdl1_ParticipantType381", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_ParticipantType381", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_ParticipantType381"):
                opp_val = getattr(value, "xpdl1_ParticipantType381", None)
                setattr(value, "xpdl1_ParticipantType381", self)

    @property
    def xpdl1_ExternalReferenceType(self):
        return self.__xpdl1_ExternalReferenceType

    @xpdl1_ExternalReferenceType.setter
    def xpdl1_ExternalReferenceType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ExternalReferenceType__xpdl1_ExternalReferenceType", None)
        self.__xpdl1_ExternalReferenceType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_ApplicationType29"):
                opp_val = getattr(old_value, "xpdl1_ApplicationType29", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_ApplicationType29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_ApplicationType29"):
                opp_val = getattr(value, "xpdl1_ApplicationType29", None)
                setattr(value, "xpdl1_ApplicationType29", self)

    @property
    def xpdl1_ExternalReferenceType298(self):
        return self.__xpdl1_ExternalReferenceType298

    @xpdl1_ExternalReferenceType298.setter
    def xpdl1_ExternalReferenceType298(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ExternalReferenceType__xpdl1_ExternalReferenceType298", None)
        self.__xpdl1_ExternalReferenceType298 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_ListTypeType297"):
                opp_val = getattr(old_value, "xpdl1_ListTypeType297", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_ListTypeType297", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_ListTypeType297"):
                opp_val = getattr(value, "xpdl1_ListTypeType297", None)
                setattr(value, "xpdl1_ListTypeType297", self)

    @property
    def xpdl1_ExternalReferenceType451(self):
        return self.__xpdl1_ExternalReferenceType451

    @xpdl1_ExternalReferenceType451.setter
    def xpdl1_ExternalReferenceType451(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ExternalReferenceType__xpdl1_ExternalReferenceType451", None)
        self.__xpdl1_ExternalReferenceType451 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_TypeDeclarationType450"):
                opp_val = getattr(old_value, "xpdl1_TypeDeclarationType450", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_TypeDeclarationType450", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_TypeDeclarationType450"):
                opp_val = getattr(value, "xpdl1_TypeDeclarationType450", None)
                setattr(value, "xpdl1_TypeDeclarationType450", self)

    @property
    def xpdl1_ExternalReferenceType70(self):
        return self.__xpdl1_ExternalReferenceType70

    @xpdl1_ExternalReferenceType70.setter
    def xpdl1_ExternalReferenceType70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ExternalReferenceType__xpdl1_ExternalReferenceType70", None)
        self.__xpdl1_ExternalReferenceType70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_DataTypeType69"):
                opp_val = getattr(old_value, "xpdl1_DataTypeType69", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_DataTypeType69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_DataTypeType69"):
                opp_val = getattr(value, "xpdl1_DataTypeType69", None)
                setattr(value, "xpdl1_DataTypeType69", self)

    @property
    def xpdl1_ExternalReferenceType162(self):
        return self.__xpdl1_ExternalReferenceType162

    @xpdl1_ExternalReferenceType162.setter
    def xpdl1_ExternalReferenceType162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ExternalReferenceType__xpdl1_ExternalReferenceType162", None)
        self.__xpdl1_ExternalReferenceType162 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_DocumentRoot161"):
                opp_val = getattr(old_value, "xpdl1_DocumentRoot161", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_DocumentRoot161"):
                opp_val = getattr(value, "xpdl1_DocumentRoot161", None)
                if opp_val is None:
                    setattr(value, "xpdl1_DocumentRoot161", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xpdl1_ExternalReferenceType40(self):
        return self.__xpdl1_ExternalReferenceType40

    @xpdl1_ExternalReferenceType40.setter
    def xpdl1_ExternalReferenceType40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ExternalReferenceType__xpdl1_ExternalReferenceType40", None)
        self.__xpdl1_ExternalReferenceType40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_ArrayTypeType39"):
                opp_val = getattr(old_value, "xpdl1_ArrayTypeType39", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_ArrayTypeType39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_ArrayTypeType39"):
                opp_val = getattr(value, "xpdl1_ArrayTypeType39", None)
                setattr(value, "xpdl1_ArrayTypeType39", self)

class xpdl1_FormalParametersType:

    pass
class xpdl1_ApplicationType:

    def __init__(self, description: str, id: str, name: str, xpdl1_ApplicationType: "xpdl1_ApplicationsType" = None, xpdl1_ApplicationType27: "xpdl1_FormalParametersType" = None, xpdl1_ApplicationType29: "xpdl1_ExternalReferenceType" = None, xpdl1_ApplicationType31: "xpdl1_ExtendedAttributesType" = None, xpdl1_ApplicationType111: "xpdl1_DocumentRoot" = None):
        self.description = description
        self.id = id
        self.name = name
        self.xpdl1_ApplicationType = xpdl1_ApplicationType
        self.xpdl1_ApplicationType27 = xpdl1_ApplicationType27
        self.xpdl1_ApplicationType29 = xpdl1_ApplicationType29
        self.xpdl1_ApplicationType31 = xpdl1_ApplicationType31
        self.xpdl1_ApplicationType111 = xpdl1_ApplicationType111
        
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
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def xpdl1_ApplicationType27(self):
        return self.__xpdl1_ApplicationType27

    @xpdl1_ApplicationType27.setter
    def xpdl1_ApplicationType27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ApplicationType__xpdl1_ApplicationType27", None)
        self.__xpdl1_ApplicationType27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_FormalParametersType"):
                opp_val = getattr(old_value, "xpdl1_FormalParametersType", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_FormalParametersType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_FormalParametersType"):
                opp_val = getattr(value, "xpdl1_FormalParametersType", None)
                setattr(value, "xpdl1_FormalParametersType", self)

    @property
    def xpdl1_ApplicationType31(self):
        return self.__xpdl1_ApplicationType31

    @xpdl1_ApplicationType31.setter
    def xpdl1_ApplicationType31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ApplicationType__xpdl1_ApplicationType31", None)
        self.__xpdl1_ApplicationType31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_ExtendedAttributesType32"):
                opp_val = getattr(old_value, "xpdl1_ExtendedAttributesType32", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_ExtendedAttributesType32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_ExtendedAttributesType32"):
                opp_val = getattr(value, "xpdl1_ExtendedAttributesType32", None)
                setattr(value, "xpdl1_ExtendedAttributesType32", self)

    @property
    def xpdl1_ApplicationType111(self):
        return self.__xpdl1_ApplicationType111

    @xpdl1_ApplicationType111.setter
    def xpdl1_ApplicationType111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ApplicationType__xpdl1_ApplicationType111", None)
        self.__xpdl1_ApplicationType111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_DocumentRoot110"):
                opp_val = getattr(old_value, "xpdl1_DocumentRoot110", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_DocumentRoot110"):
                opp_val = getattr(value, "xpdl1_DocumentRoot110", None)
                if opp_val is None:
                    setattr(value, "xpdl1_DocumentRoot110", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xpdl1_ApplicationType29(self):
        return self.__xpdl1_ApplicationType29

    @xpdl1_ApplicationType29.setter
    def xpdl1_ApplicationType29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ApplicationType__xpdl1_ApplicationType29", None)
        self.__xpdl1_ApplicationType29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_ExternalReferenceType"):
                opp_val = getattr(old_value, "xpdl1_ExternalReferenceType", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_ExternalReferenceType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_ExternalReferenceType"):
                opp_val = getattr(value, "xpdl1_ExternalReferenceType", None)
                setattr(value, "xpdl1_ExternalReferenceType", self)

    @property
    def xpdl1_ApplicationType(self):
        return self.__xpdl1_ApplicationType

    @xpdl1_ApplicationType.setter
    def xpdl1_ApplicationType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ApplicationType__xpdl1_ApplicationType", None)
        self.__xpdl1_ApplicationType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_ApplicationsType"):
                opp_val = getattr(old_value, "xpdl1_ApplicationsType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_ApplicationsType"):
                opp_val = getattr(value, "xpdl1_ApplicationsType", None)
                if opp_val is None:
                    setattr(value, "xpdl1_ApplicationsType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xpdl1_ApplicationsType:

    pass
class xpdl1_ActualParametersType:

    def __init__(self, actualParameter: str, xpdl1_ActualParametersType: "xpdl1_DocumentRoot" = None, xpdl1_ActualParametersType409: "xpdl1_SubFlowType" = None, xpdl1_ActualParametersType412: "xpdl1_ToolType" = None):
        self.actualParameter = actualParameter
        self.xpdl1_ActualParametersType = xpdl1_ActualParametersType
        self.xpdl1_ActualParametersType409 = xpdl1_ActualParametersType409
        self.xpdl1_ActualParametersType412 = xpdl1_ActualParametersType412
        
    @property
    def actualParameter(self) -> str:
        return self.__actualParameter

    @actualParameter.setter
    def actualParameter(self, actualParameter: str):
        self.__actualParameter = actualParameter

    @property
    def xpdl1_ActualParametersType(self):
        return self.__xpdl1_ActualParametersType

    @xpdl1_ActualParametersType.setter
    def xpdl1_ActualParametersType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ActualParametersType__xpdl1_ActualParametersType", None)
        self.__xpdl1_ActualParametersType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_DocumentRoot108"):
                opp_val = getattr(old_value, "xpdl1_DocumentRoot108", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_DocumentRoot108"):
                opp_val = getattr(value, "xpdl1_DocumentRoot108", None)
                if opp_val is None:
                    setattr(value, "xpdl1_DocumentRoot108", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xpdl1_ActualParametersType409(self):
        return self.__xpdl1_ActualParametersType409

    @xpdl1_ActualParametersType409.setter
    def xpdl1_ActualParametersType409(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ActualParametersType__xpdl1_ActualParametersType409", None)
        self.__xpdl1_ActualParametersType409 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_SubFlowType408"):
                opp_val = getattr(old_value, "xpdl1_SubFlowType408", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_SubFlowType408", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_SubFlowType408"):
                opp_val = getattr(value, "xpdl1_SubFlowType408", None)
                setattr(value, "xpdl1_SubFlowType408", self)

    @property
    def xpdl1_ActualParametersType412(self):
        return self.__xpdl1_ActualParametersType412

    @xpdl1_ActualParametersType412.setter
    def xpdl1_ActualParametersType412(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ActualParametersType__xpdl1_ActualParametersType412", None)
        self.__xpdl1_ActualParametersType412 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_ToolType411"):
                opp_val = getattr(old_value, "xpdl1_ToolType411", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_ToolType411", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_ToolType411"):
                opp_val = getattr(value, "xpdl1_ToolType411", None)
                setattr(value, "xpdl1_ToolType411", self)

class xpdl1_ExtendedAttributesType:

    pass
class xpdl1_TransitionRestrictionsType:

    pass
class xpdl1_SimulationInformationType:

    def __init__(self, cost: str, instantiation: str, xpdl1_SimulationInformationType: "xpdl1_ActivityType" = None, xpdl1_SimulationInformationType214: "xpdl1_DocumentRoot" = None, xpdl1_SimulationInformationType396: "xpdl1_TimeEstimationType" = None):
        self.cost = cost
        self.instantiation = instantiation
        self.xpdl1_SimulationInformationType = xpdl1_SimulationInformationType
        self.xpdl1_SimulationInformationType214 = xpdl1_SimulationInformationType214
        self.xpdl1_SimulationInformationType396 = xpdl1_SimulationInformationType396
        
    @property
    def instantiation(self) -> str:
        return self.__instantiation

    @instantiation.setter
    def instantiation(self, instantiation: str):
        self.__instantiation = instantiation

    @property
    def cost(self) -> str:
        return self.__cost

    @cost.setter
    def cost(self, cost: str):
        self.__cost = cost

    @property
    def xpdl1_SimulationInformationType(self):
        return self.__xpdl1_SimulationInformationType

    @xpdl1_SimulationInformationType.setter
    def xpdl1_SimulationInformationType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_SimulationInformationType__xpdl1_SimulationInformationType", None)
        self.__xpdl1_SimulationInformationType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_ActivityType20"):
                opp_val = getattr(old_value, "xpdl1_ActivityType20", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_ActivityType20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_ActivityType20"):
                opp_val = getattr(value, "xpdl1_ActivityType20", None)
                setattr(value, "xpdl1_ActivityType20", self)

    @property
    def xpdl1_SimulationInformationType214(self):
        return self.__xpdl1_SimulationInformationType214

    @xpdl1_SimulationInformationType214.setter
    def xpdl1_SimulationInformationType214(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_SimulationInformationType__xpdl1_SimulationInformationType214", None)
        self.__xpdl1_SimulationInformationType214 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_DocumentRoot213"):
                opp_val = getattr(old_value, "xpdl1_DocumentRoot213", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_DocumentRoot213"):
                opp_val = getattr(value, "xpdl1_DocumentRoot213", None)
                if opp_val is None:
                    setattr(value, "xpdl1_DocumentRoot213", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xpdl1_SimulationInformationType396(self):
        return self.__xpdl1_SimulationInformationType396

    @xpdl1_SimulationInformationType396.setter
    def xpdl1_SimulationInformationType396(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_SimulationInformationType__xpdl1_SimulationInformationType396", None)
        self.__xpdl1_SimulationInformationType396 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_TimeEstimationType397"):
                opp_val = getattr(old_value, "xpdl1_TimeEstimationType397", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_TimeEstimationType397", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_TimeEstimationType397"):
                opp_val = getattr(value, "xpdl1_TimeEstimationType397", None)
                setattr(value, "xpdl1_TimeEstimationType397", self)

class xpdl1_DeadlineType:

    def __init__(self, execution: str, xpdl1_DeadlineType: "xpdl1_ActivityType" = None, xpdl1_DeadlineType87: "xpdl1_EObject" = None, xpdl1_DeadlineType89: "xpdl1_EObject" = None, xpdl1_DeadlineType142: "xpdl1_DocumentRoot" = None):
        self.execution = execution
        self.xpdl1_DeadlineType = xpdl1_DeadlineType
        self.xpdl1_DeadlineType87 = xpdl1_DeadlineType87
        self.xpdl1_DeadlineType89 = xpdl1_DeadlineType89
        self.xpdl1_DeadlineType142 = xpdl1_DeadlineType142
        
    @property
    def execution(self) -> str:
        return self.__execution

    @execution.setter
    def execution(self, execution: str):
        self.__execution = execution

    @property
    def xpdl1_DeadlineType89(self):
        return self.__xpdl1_DeadlineType89

    @xpdl1_DeadlineType89.setter
    def xpdl1_DeadlineType89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DeadlineType__xpdl1_DeadlineType89", None)
        self.__xpdl1_DeadlineType89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_EObject90"):
                opp_val = getattr(old_value, "xpdl1_EObject90", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_EObject90", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_EObject90"):
                opp_val = getattr(value, "xpdl1_EObject90", None)
                setattr(value, "xpdl1_EObject90", self)

    @property
    def xpdl1_DeadlineType(self):
        return self.__xpdl1_DeadlineType

    @xpdl1_DeadlineType.setter
    def xpdl1_DeadlineType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DeadlineType__xpdl1_DeadlineType", None)
        self.__xpdl1_DeadlineType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_ActivityType18"):
                opp_val = getattr(old_value, "xpdl1_ActivityType18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_ActivityType18"):
                opp_val = getattr(value, "xpdl1_ActivityType18", None)
                if opp_val is None:
                    setattr(value, "xpdl1_ActivityType18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xpdl1_DeadlineType87(self):
        return self.__xpdl1_DeadlineType87

    @xpdl1_DeadlineType87.setter
    def xpdl1_DeadlineType87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DeadlineType__xpdl1_DeadlineType87", None)
        self.__xpdl1_DeadlineType87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_EObject"):
                opp_val = getattr(old_value, "xpdl1_EObject", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_EObject"):
                opp_val = getattr(value, "xpdl1_EObject", None)
                setattr(value, "xpdl1_EObject", self)

    @property
    def xpdl1_DeadlineType142(self):
        return self.__xpdl1_DeadlineType142

    @xpdl1_DeadlineType142.setter
    def xpdl1_DeadlineType142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_DeadlineType__xpdl1_DeadlineType142", None)
        self.__xpdl1_DeadlineType142 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_DocumentRoot141"):
                opp_val = getattr(old_value, "xpdl1_DocumentRoot141", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_DocumentRoot141"):
                opp_val = getattr(value, "xpdl1_DocumentRoot141", None)
                if opp_val is None:
                    setattr(value, "xpdl1_DocumentRoot141", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xpdl1_FinishModeType:

    pass
class xpdl1_StartModeType:

    pass
class xpdl1_BlockActivityType:

    def __init__(self, blockId: str, xpdl1_BlockActivityType: "xpdl1_ActivityType" = None, xpdl1_BlockActivityType125: "xpdl1_DocumentRoot" = None):
        self.blockId = blockId
        self.xpdl1_BlockActivityType = xpdl1_BlockActivityType
        self.xpdl1_BlockActivityType125 = xpdl1_BlockActivityType125
        
    @property
    def blockId(self) -> str:
        return self.__blockId

    @blockId.setter
    def blockId(self, blockId: str):
        self.__blockId = blockId

    @property
    def xpdl1_BlockActivityType125(self):
        return self.__xpdl1_BlockActivityType125

    @xpdl1_BlockActivityType125.setter
    def xpdl1_BlockActivityType125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_BlockActivityType__xpdl1_BlockActivityType125", None)
        self.__xpdl1_BlockActivityType125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_DocumentRoot124"):
                opp_val = getattr(old_value, "xpdl1_DocumentRoot124", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_DocumentRoot124"):
                opp_val = getattr(value, "xpdl1_DocumentRoot124", None)
                if opp_val is None:
                    setattr(value, "xpdl1_DocumentRoot124", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xpdl1_BlockActivityType(self):
        return self.__xpdl1_BlockActivityType

    @xpdl1_BlockActivityType.setter
    def xpdl1_BlockActivityType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_BlockActivityType__xpdl1_BlockActivityType", None)
        self.__xpdl1_BlockActivityType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_ActivityType12"):
                opp_val = getattr(old_value, "xpdl1_ActivityType12", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_ActivityType12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_ActivityType12"):
                opp_val = getattr(value, "xpdl1_ActivityType12", None)
                setattr(value, "xpdl1_ActivityType12", self)

class xpdl1_ImplementationType:

    pass
class xpdl1_RouteType:

    pass
class xpdl1_TransitionsType:

    pass
class xpdl1_ActivitySetType:

    def __init__(self, id: str, xpdl1_ActivitySetType: "xpdl1_ActivitySetsType" = None, xpdl1_ActivitySetType3: "xpdl1_ActivitiesType" = None, xpdl1_ActivitySetType6: "xpdl1_TransitionsType" = None, xpdl1_ActivitySetType103: "xpdl1_DocumentRoot" = None):
        self.id = id
        self.xpdl1_ActivitySetType = xpdl1_ActivitySetType
        self.xpdl1_ActivitySetType3 = xpdl1_ActivitySetType3
        self.xpdl1_ActivitySetType6 = xpdl1_ActivitySetType6
        self.xpdl1_ActivitySetType103 = xpdl1_ActivitySetType103
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def xpdl1_ActivitySetType103(self):
        return self.__xpdl1_ActivitySetType103

    @xpdl1_ActivitySetType103.setter
    def xpdl1_ActivitySetType103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ActivitySetType__xpdl1_ActivitySetType103", None)
        self.__xpdl1_ActivitySetType103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_DocumentRoot102"):
                opp_val = getattr(old_value, "xpdl1_DocumentRoot102", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_DocumentRoot102"):
                opp_val = getattr(value, "xpdl1_DocumentRoot102", None)
                if opp_val is None:
                    setattr(value, "xpdl1_DocumentRoot102", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xpdl1_ActivitySetType6(self):
        return self.__xpdl1_ActivitySetType6

    @xpdl1_ActivitySetType6.setter
    def xpdl1_ActivitySetType6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ActivitySetType__xpdl1_ActivitySetType6", None)
        self.__xpdl1_ActivitySetType6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_TransitionsType"):
                opp_val = getattr(old_value, "xpdl1_TransitionsType", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_TransitionsType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_TransitionsType"):
                opp_val = getattr(value, "xpdl1_TransitionsType", None)
                setattr(value, "xpdl1_TransitionsType", self)

    @property
    def xpdl1_ActivitySetType3(self):
        return self.__xpdl1_ActivitySetType3

    @xpdl1_ActivitySetType3.setter
    def xpdl1_ActivitySetType3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ActivitySetType__xpdl1_ActivitySetType3", None)
        self.__xpdl1_ActivitySetType3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_ActivitiesType4"):
                opp_val = getattr(old_value, "xpdl1_ActivitiesType4", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_ActivitiesType4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_ActivitiesType4"):
                opp_val = getattr(value, "xpdl1_ActivitiesType4", None)
                setattr(value, "xpdl1_ActivitiesType4", self)

    @property
    def xpdl1_ActivitySetType(self):
        return self.__xpdl1_ActivitySetType

    @xpdl1_ActivitySetType.setter
    def xpdl1_ActivitySetType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ActivitySetType__xpdl1_ActivitySetType", None)
        self.__xpdl1_ActivitySetType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_ActivitySetsType"):
                opp_val = getattr(old_value, "xpdl1_ActivitySetsType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_ActivitySetsType"):
                opp_val = getattr(value, "xpdl1_ActivitySetsType", None)
                if opp_val is None:
                    setattr(value, "xpdl1_ActivitySetsType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xpdl1_ActivitySetsType:

    pass
class xpdl1_ActivityType:

    def __init__(self, description: str, limit: str, performer: str, priority: str, icon: str, documentation: str, id: str, name: str, xpdl1_ActivityType: "xpdl1_ActivitiesType" = None, xpdl1_ActivityType8: "xpdl1_RouteType" = None, xpdl1_ActivityType10: "xpdl1_ImplementationType" = None, xpdl1_ActivityType12: "xpdl1_BlockActivityType" = None, xpdl1_ActivityType14: "xpdl1_StartModeType" = None, xpdl1_ActivityType16: "xpdl1_FinishModeType" = None, xpdl1_ActivityType18: set["xpdl1_DeadlineType"] = None, xpdl1_ActivityType20: "xpdl1_SimulationInformationType" = None, xpdl1_ActivityType24: "xpdl1_ExtendedAttributesType" = None, xpdl1_ActivityType22: "xpdl1_TransitionRestrictionsType" = None, xpdl1_ActivityType100: "xpdl1_DocumentRoot" = None):
        self.description = description
        self.limit = limit
        self.performer = performer
        self.priority = priority
        self.icon = icon
        self.documentation = documentation
        self.id = id
        self.name = name
        self.xpdl1_ActivityType = xpdl1_ActivityType
        self.xpdl1_ActivityType8 = xpdl1_ActivityType8
        self.xpdl1_ActivityType10 = xpdl1_ActivityType10
        self.xpdl1_ActivityType12 = xpdl1_ActivityType12
        self.xpdl1_ActivityType14 = xpdl1_ActivityType14
        self.xpdl1_ActivityType16 = xpdl1_ActivityType16
        self.xpdl1_ActivityType18 = xpdl1_ActivityType18 if xpdl1_ActivityType18 is not None else set()
        self.xpdl1_ActivityType20 = xpdl1_ActivityType20
        self.xpdl1_ActivityType24 = xpdl1_ActivityType24
        self.xpdl1_ActivityType22 = xpdl1_ActivityType22
        self.xpdl1_ActivityType100 = xpdl1_ActivityType100
        
    @property
    def priority(self) -> str:
        return self.__priority

    @priority.setter
    def priority(self, priority: str):
        self.__priority = priority

    @property
    def performer(self) -> str:
        return self.__performer

    @performer.setter
    def performer(self, performer: str):
        self.__performer = performer

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
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def limit(self) -> str:
        return self.__limit

    @limit.setter
    def limit(self, limit: str):
        self.__limit = limit

    @property
    def documentation(self) -> str:
        return self.__documentation

    @documentation.setter
    def documentation(self, documentation: str):
        self.__documentation = documentation

    @property
    def icon(self) -> str:
        return self.__icon

    @icon.setter
    def icon(self, icon: str):
        self.__icon = icon

    @property
    def xpdl1_ActivityType8(self):
        return self.__xpdl1_ActivityType8

    @xpdl1_ActivityType8.setter
    def xpdl1_ActivityType8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ActivityType__xpdl1_ActivityType8", None)
        self.__xpdl1_ActivityType8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_RouteType"):
                opp_val = getattr(old_value, "xpdl1_RouteType", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_RouteType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_RouteType"):
                opp_val = getattr(value, "xpdl1_RouteType", None)
                setattr(value, "xpdl1_RouteType", self)

    @property
    def xpdl1_ActivityType(self):
        return self.__xpdl1_ActivityType

    @xpdl1_ActivityType.setter
    def xpdl1_ActivityType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ActivityType__xpdl1_ActivityType", None)
        self.__xpdl1_ActivityType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_ActivitiesType"):
                opp_val = getattr(old_value, "xpdl1_ActivitiesType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_ActivitiesType"):
                opp_val = getattr(value, "xpdl1_ActivitiesType", None)
                if opp_val is None:
                    setattr(value, "xpdl1_ActivitiesType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xpdl1_ActivityType12(self):
        return self.__xpdl1_ActivityType12

    @xpdl1_ActivityType12.setter
    def xpdl1_ActivityType12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ActivityType__xpdl1_ActivityType12", None)
        self.__xpdl1_ActivityType12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_BlockActivityType"):
                opp_val = getattr(old_value, "xpdl1_BlockActivityType", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_BlockActivityType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_BlockActivityType"):
                opp_val = getattr(value, "xpdl1_BlockActivityType", None)
                setattr(value, "xpdl1_BlockActivityType", self)

    @property
    def xpdl1_ActivityType14(self):
        return self.__xpdl1_ActivityType14

    @xpdl1_ActivityType14.setter
    def xpdl1_ActivityType14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ActivityType__xpdl1_ActivityType14", None)
        self.__xpdl1_ActivityType14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_StartModeType"):
                opp_val = getattr(old_value, "xpdl1_StartModeType", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_StartModeType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_StartModeType"):
                opp_val = getattr(value, "xpdl1_StartModeType", None)
                setattr(value, "xpdl1_StartModeType", self)

    @property
    def xpdl1_ActivityType16(self):
        return self.__xpdl1_ActivityType16

    @xpdl1_ActivityType16.setter
    def xpdl1_ActivityType16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ActivityType__xpdl1_ActivityType16", None)
        self.__xpdl1_ActivityType16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_FinishModeType"):
                opp_val = getattr(old_value, "xpdl1_FinishModeType", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_FinishModeType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_FinishModeType"):
                opp_val = getattr(value, "xpdl1_FinishModeType", None)
                setattr(value, "xpdl1_FinishModeType", self)

    @property
    def xpdl1_ActivityType18(self):
        return self.__xpdl1_ActivityType18

    @xpdl1_ActivityType18.setter
    def xpdl1_ActivityType18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ActivityType__xpdl1_ActivityType18", None)
        self.__xpdl1_ActivityType18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xpdl1_DeadlineType"):
                    opp_val = getattr(item, "xpdl1_DeadlineType", None)
                    
                    if opp_val == self:
                        setattr(item, "xpdl1_DeadlineType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xpdl1_DeadlineType"):
                    opp_val = getattr(item, "xpdl1_DeadlineType", None)
                    
                    setattr(item, "xpdl1_DeadlineType", self)
                    

    @property
    def xpdl1_ActivityType24(self):
        return self.__xpdl1_ActivityType24

    @xpdl1_ActivityType24.setter
    def xpdl1_ActivityType24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ActivityType__xpdl1_ActivityType24", None)
        self.__xpdl1_ActivityType24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_ExtendedAttributesType"):
                opp_val = getattr(old_value, "xpdl1_ExtendedAttributesType", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_ExtendedAttributesType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_ExtendedAttributesType"):
                opp_val = getattr(value, "xpdl1_ExtendedAttributesType", None)
                setattr(value, "xpdl1_ExtendedAttributesType", self)

    @property
    def xpdl1_ActivityType100(self):
        return self.__xpdl1_ActivityType100

    @xpdl1_ActivityType100.setter
    def xpdl1_ActivityType100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ActivityType__xpdl1_ActivityType100", None)
        self.__xpdl1_ActivityType100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_DocumentRoot99"):
                opp_val = getattr(old_value, "xpdl1_DocumentRoot99", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_DocumentRoot99"):
                opp_val = getattr(value, "xpdl1_DocumentRoot99", None)
                if opp_val is None:
                    setattr(value, "xpdl1_DocumentRoot99", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xpdl1_ActivityType20(self):
        return self.__xpdl1_ActivityType20

    @xpdl1_ActivityType20.setter
    def xpdl1_ActivityType20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ActivityType__xpdl1_ActivityType20", None)
        self.__xpdl1_ActivityType20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_SimulationInformationType"):
                opp_val = getattr(old_value, "xpdl1_SimulationInformationType", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_SimulationInformationType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_SimulationInformationType"):
                opp_val = getattr(value, "xpdl1_SimulationInformationType", None)
                setattr(value, "xpdl1_SimulationInformationType", self)

    @property
    def xpdl1_ActivityType22(self):
        return self.__xpdl1_ActivityType22

    @xpdl1_ActivityType22.setter
    def xpdl1_ActivityType22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ActivityType__xpdl1_ActivityType22", None)
        self.__xpdl1_ActivityType22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_TransitionRestrictionsType"):
                opp_val = getattr(old_value, "xpdl1_TransitionRestrictionsType", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_TransitionRestrictionsType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_TransitionRestrictionsType"):
                opp_val = getattr(value, "xpdl1_TransitionRestrictionsType", None)
                setattr(value, "xpdl1_TransitionRestrictionsType", self)

    @property
    def xpdl1_ActivityType10(self):
        return self.__xpdl1_ActivityType10

    @xpdl1_ActivityType10.setter
    def xpdl1_ActivityType10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpdl1_ActivityType__xpdl1_ActivityType10", None)
        self.__xpdl1_ActivityType10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpdl1_ImplementationType"):
                opp_val = getattr(old_value, "xpdl1_ImplementationType", None)
                if opp_val == self:
                    setattr(old_value, "xpdl1_ImplementationType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpdl1_ImplementationType"):
                opp_val = getattr(value, "xpdl1_ImplementationType", None)
                setattr(value, "xpdl1_ImplementationType", self)

class xpdl1_ActivitiesType:

    pass