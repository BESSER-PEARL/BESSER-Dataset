from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class PositionEnum(Enum):
    left = "left"
    top = "top"
    right = "right"
    group = "group"
    none = "none"
    defaultpos = "defaultpos"
class TWEvol(Enum):
    twFinal = "twFinal"
    twTransient = "twTransient"
    twMutable = "twMutable"
    twImmutable = "twImmutable"
class TWUpdateKind(Enum):
    none = "none"
    merge = "merge"
    compute = "compute"
class TWCommitKind(Enum):
    none = "none"
    conflict = "conflict"
    reconcile = "reconcile"
class TWDestEvol(Enum):
    mutable = "mutable"
    immutable = "immutable"
    effective = "effective"
    finalDest = "finalDest"
    branch = "branch"


############################################
# Definition of Classes
############################################

class ccore_DBObject:

    def __init__(self, uuid_lsb: str, objectId: int, uuid_msb: str, ccore_DBObject: "ccore_ItemType" = None):
        self.uuid_lsb = uuid_lsb
        self.objectId = objectId
        self.uuid_msb = uuid_msb
        self.ccore_DBObject = ccore_DBObject
        
    @property
    def uuid_lsb(self) -> str:
        return self.__uuid_lsb

    @uuid_lsb.setter
    def uuid_lsb(self, uuid_lsb: str):
        self.__uuid_lsb = uuid_lsb

    @property
    def uuid_msb(self) -> str:
        return self.__uuid_msb

    @uuid_msb.setter
    def uuid_msb(self, uuid_msb: str):
        self.__uuid_msb = uuid_msb

    @property
    def objectId(self) -> int:
        return self.__objectId

    @objectId.setter
    def objectId(self, objectId: int):
        self.__objectId = objectId

    @property
    def ccore_DBObject(self):
        return self.__ccore_DBObject

    @ccore_DBObject.setter
    def ccore_DBObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_DBObject__ccore_DBObject", None)
        self.__ccore_DBObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccore_ItemType172"):
                opp_val = getattr(old_value, "ccore_ItemType172", None)
                if opp_val == self:
                    setattr(old_value, "ccore_ItemType172", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccore_ItemType172"):
                opp_val = getattr(value, "ccore_ItemType172", None)
                setattr(value, "ccore_ItemType172", self)

class RuntimeItemType:

    pass
class ccore_ViewModel:

    pass
class ccore_ExtItem(ABC):

    pass
class ccore_View:

    def __init__(self, icon: str, ccore_View: set["ccore_ViewItemType"] = None, ccore_View161: "ccore_ViewModel" = None):
        self.icon = icon
        self.ccore_View = ccore_View if ccore_View is not None else set()
        self.ccore_View161 = ccore_View161
        
    @property
    def icon(self) -> str:
        return self.__icon

    @icon.setter
    def icon(self, icon: str):
        self.__icon = icon

    @property
    def ccore_View(self):
        return self.__ccore_View

    @ccore_View.setter
    def ccore_View(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_View__ccore_View", None)
        self.__ccore_View = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ccore_ViewItemType159"):
                    opp_val = getattr(item, "ccore_ViewItemType159", None)
                    
                    if opp_val == self:
                        setattr(item, "ccore_ViewItemType159", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ccore_ViewItemType159"):
                    opp_val = getattr(item, "ccore_ViewItemType159", None)
                    
                    setattr(item, "ccore_ViewItemType159", self)
                    

    @property
    def ccore_View161(self):
        return self.__ccore_View161

    @ccore_View161.setter
    def ccore_View161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_View__ccore_View161", None)
        self.__ccore_View161 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccore_ViewModel"):
                opp_val = getattr(old_value, "ccore_ViewModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccore_ViewModel"):
                opp_val = getattr(value, "ccore_ViewModel", None)
                if opp_val is None:
                    setattr(value, "ccore_ViewModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ccore_ComputedString(ABC):

    def __init__(self, expression: str):
        self.expression = expression
        
    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

class ccore_EEnum:

    pass
class EEnum:

    pass
class ccore_ComposerLink:

    pass
class ccore_MenuGroup:

    pass
class ccore_MenuAction:

    pass
class ccore_GroupExtItem:

    pass
class ccore_ExportedContent:

    def __init__(self):
        
    def hasChildren(self) -> bool:
        # TODO: Implement hasChildren method
        pass

class EReference:

    pass
class ccore_EnumType(EEnum):

    def __init__(self, mustBeGenerated: bool, javaClass: str, values: str, ccore_EnumType: "ccore_Enum" = None, ccore_EnumType127: "ccore_EEnum" = None):
        self.mustBeGenerated = mustBeGenerated
        self.javaClass = javaClass
        self.values = values
        self.ccore_EnumType = ccore_EnumType
        self.ccore_EnumType127 = ccore_EnumType127
        
    @property
    def values(self) -> str:
        return self.__values

    @values.setter
    def values(self, values: str):
        self.__values = values

    @property
    def javaClass(self) -> str:
        return self.__javaClass

    @javaClass.setter
    def javaClass(self, javaClass: str):
        self.__javaClass = javaClass

    @property
    def mustBeGenerated(self) -> bool:
        return self.__mustBeGenerated

    @mustBeGenerated.setter
    def mustBeGenerated(self, mustBeGenerated: bool):
        self.__mustBeGenerated = mustBeGenerated

    @property
    def ccore_EnumType(self):
        return self.__ccore_EnumType

    @ccore_EnumType.setter
    def ccore_EnumType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_EnumType__ccore_EnumType", None)
        self.__ccore_EnumType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccore_Enum"):
                opp_val = getattr(old_value, "ccore_Enum", None)
                if opp_val == self:
                    setattr(old_value, "ccore_Enum", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccore_Enum"):
                opp_val = getattr(value, "ccore_Enum", None)
                setattr(value, "ccore_Enum", self)

    @property
    def ccore_EnumType127(self):
        return self.__ccore_EnumType127

    @ccore_EnumType127.setter
    def ccore_EnumType127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_EnumType__ccore_EnumType127", None)
        self.__ccore_EnumType127 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccore_EEnum"):
                opp_val = getattr(old_value, "ccore_EEnum", None)
                if opp_val == self:
                    setattr(old_value, "ccore_EEnum", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccore_EEnum"):
                opp_val = getattr(value, "ccore_EEnum", None)
                setattr(value, "ccore_EEnum", self)

class ccore_MenuAbstract(ABC):

    def __init__(self, label: str, icon: str, path: str, ccore_MenuAbstract: "ccore_Menu" = None):
        self.label = label
        self.icon = icon
        self.path = path
        self.ccore_MenuAbstract = ccore_MenuAbstract
        
    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path

    @property
    def icon(self) -> str:
        return self.__icon

    @icon.setter
    def icon(self, icon: str):
        self.__icon = icon

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def ccore_MenuAbstract(self):
        return self.__ccore_MenuAbstract

    @ccore_MenuAbstract.setter
    def ccore_MenuAbstract(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_MenuAbstract__ccore_MenuAbstract", None)
        self.__ccore_MenuAbstract = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccore_Menu92"):
                opp_val = getattr(old_value, "ccore_Menu92", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccore_Menu92"):
                opp_val = getattr(value, "ccore_Menu92", None)
                if opp_val is None:
                    setattr(value, "ccore_Menu92", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ccore_Menu:

    pass
class ccore_ActionExtItemType:

    pass
class ccore_DynamicActions:

    pass
class BindingDesc:

    pass
class ccore_BindExt(BindingDesc):

    pass
class ccore_UnresolvedAttributeType(ABC):

    pass
class LongAttribute:

    pass
class ccore_TimeAttribute(LongAttribute):

    def __init__(self, initWithTheCurrentTime: bool):
        self.initWithTheCurrentTime = initWithTheCurrentTime
        
    @property
    def initWithTheCurrentTime(self) -> bool:
        return self.__initWithTheCurrentTime

    @initWithTheCurrentTime.setter
    def initWithTheCurrentTime(self, initWithTheCurrentTime: bool):
        self.__initWithTheCurrentTime = initWithTheCurrentTime

class Attribute:

    pass
class ccore_IntegerAttribute(Attribute):

    pass
class ccore_DateAttribute(Attribute):

    pass
class ccore_LinkType(EReference, Attribute):

    def __init__(self, annotation: bool, aggregation: bool, composition: bool, selection: str, mapping: bool, linkManager: str, twDestEvol: str, twCoupled: bool, hidden: bool, min: int, max: int, kind: int, group: bool, ccore_LinkType: "ccore_TypeDefinition" = None, ccore_LinkType103: "ccore_TypeDefinition" = None, ccore_LinkType143: "ccore_Composer" = None, ccore_LinkType136: "ccore_ViewLinkType" = None, ccore_LinkType157: "ccore_ComposerLink" = None, ccore_LinkType170: "ccore_BindingDesc" = None):
        self.annotation = annotation
        self.aggregation = aggregation
        self.composition = composition
        self.selection = selection
        self.mapping = mapping
        self.linkManager = linkManager
        self.twDestEvol = twDestEvol
        self.twCoupled = twCoupled
        self.hidden = hidden
        self.min = min
        self.max = max
        self.kind = kind
        self.group = group
        self.ccore_LinkType = ccore_LinkType
        self.ccore_LinkType103 = ccore_LinkType103
        self.ccore_LinkType143 = ccore_LinkType143
        self.ccore_LinkType136 = ccore_LinkType136
        self.ccore_LinkType157 = ccore_LinkType157
        self.ccore_LinkType170 = ccore_LinkType170
        
    @property
    def group(self) -> bool:
        return self.__group

    @group.setter
    def group(self, group: bool):
        self.__group = group

    @property
    def mapping(self) -> bool:
        return self.__mapping

    @mapping.setter
    def mapping(self, mapping: bool):
        self.__mapping = mapping

    @property
    def max(self) -> int:
        return self.__max

    @max.setter
    def max(self, max: int):
        self.__max = max

    @property
    def twDestEvol(self) -> str:
        return self.__twDestEvol

    @twDestEvol.setter
    def twDestEvol(self, twDestEvol: str):
        self.__twDestEvol = twDestEvol

    @property
    def linkManager(self) -> str:
        return self.__linkManager

    @linkManager.setter
    def linkManager(self, linkManager: str):
        self.__linkManager = linkManager

    @property
    def min(self) -> int:
        return self.__min

    @min.setter
    def min(self, min: int):
        self.__min = min

    @property
    def kind(self) -> int:
        return self.__kind

    @kind.setter
    def kind(self, kind: int):
        self.__kind = kind

    @property
    def aggregation(self) -> bool:
        return self.__aggregation

    @aggregation.setter
    def aggregation(self, aggregation: bool):
        self.__aggregation = aggregation

    @property
    def selection(self) -> str:
        return self.__selection

    @selection.setter
    def selection(self, selection: str):
        self.__selection = selection

    @property
    def hidden(self) -> bool:
        return self.__hidden

    @hidden.setter
    def hidden(self, hidden: bool):
        self.__hidden = hidden

    @property
    def annotation(self) -> bool:
        return self.__annotation

    @annotation.setter
    def annotation(self, annotation: bool):
        self.__annotation = annotation

    @property
    def composition(self) -> bool:
        return self.__composition

    @composition.setter
    def composition(self, composition: bool):
        self.__composition = composition

    @property
    def twCoupled(self) -> bool:
        return self.__twCoupled

    @twCoupled.setter
    def twCoupled(self, twCoupled: bool):
        self.__twCoupled = twCoupled

    @property
    def ccore_LinkType103(self):
        return self.__ccore_LinkType103

    @ccore_LinkType103.setter
    def ccore_LinkType103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_LinkType__ccore_LinkType103", None)
        self.__ccore_LinkType103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccore_TypeDefinition104"):
                opp_val = getattr(old_value, "ccore_TypeDefinition104", None)
                if opp_val == self:
                    setattr(old_value, "ccore_TypeDefinition104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccore_TypeDefinition104"):
                opp_val = getattr(value, "ccore_TypeDefinition104", None)
                setattr(value, "ccore_TypeDefinition104", self)

    @property
    def ccore_LinkType136(self):
        return self.__ccore_LinkType136

    @ccore_LinkType136.setter
    def ccore_LinkType136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_LinkType__ccore_LinkType136", None)
        self.__ccore_LinkType136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccore_ViewLinkType135"):
                opp_val = getattr(old_value, "ccore_ViewLinkType135", None)
                if opp_val == self:
                    setattr(old_value, "ccore_ViewLinkType135", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccore_ViewLinkType135"):
                opp_val = getattr(value, "ccore_ViewLinkType135", None)
                setattr(value, "ccore_ViewLinkType135", self)

    @property
    def ccore_LinkType157(self):
        return self.__ccore_LinkType157

    @ccore_LinkType157.setter
    def ccore_LinkType157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_LinkType__ccore_LinkType157", None)
        self.__ccore_LinkType157 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccore_ComposerLink156"):
                opp_val = getattr(old_value, "ccore_ComposerLink156", None)
                if opp_val == self:
                    setattr(old_value, "ccore_ComposerLink156", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccore_ComposerLink156"):
                opp_val = getattr(value, "ccore_ComposerLink156", None)
                setattr(value, "ccore_ComposerLink156", self)

    @property
    def ccore_LinkType170(self):
        return self.__ccore_LinkType170

    @ccore_LinkType170.setter
    def ccore_LinkType170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_LinkType__ccore_LinkType170", None)
        self.__ccore_LinkType170 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccore_BindingDesc169"):
                opp_val = getattr(old_value, "ccore_BindingDesc169", None)
                if opp_val == self:
                    setattr(old_value, "ccore_BindingDesc169", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccore_BindingDesc169"):
                opp_val = getattr(value, "ccore_BindingDesc169", None)
                setattr(value, "ccore_BindingDesc169", self)

    @property
    def ccore_LinkType143(self):
        return self.__ccore_LinkType143

    @ccore_LinkType143.setter
    def ccore_LinkType143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_LinkType__ccore_LinkType143", None)
        self.__ccore_LinkType143 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccore_Composer"):
                opp_val = getattr(old_value, "ccore_Composer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccore_Composer"):
                opp_val = getattr(value, "ccore_Composer", None)
                if opp_val is None:
                    setattr(value, "ccore_Composer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ccore_LinkType(self):
        return self.__ccore_LinkType

    @ccore_LinkType.setter
    def ccore_LinkType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_LinkType__ccore_LinkType", None)
        self.__ccore_LinkType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccore_TypeDefinition101"):
                opp_val = getattr(old_value, "ccore_TypeDefinition101", None)
                if opp_val == self:
                    setattr(old_value, "ccore_TypeDefinition101", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccore_TypeDefinition101"):
                opp_val = getattr(value, "ccore_TypeDefinition101", None)
                setattr(value, "ccore_TypeDefinition101", self)

class ccore_LongAttribute(Attribute):

    pass
class ccore_UUIDAttribute(Attribute):

    pass
class ccore_BooleanAttribute(Attribute):

    pass
class ccore_DoubleAttribute(Attribute):

    pass
class ccore_StringAttribute(Attribute):

    def __init__(self, notEmpty: bool):
        self.notEmpty = notEmpty
        
    @property
    def notEmpty(self) -> bool:
        return self.__notEmpty

    @notEmpty.setter
    def notEmpty(self, notEmpty: bool):
        self.__notEmpty = notEmpty

class ccore_Enum(Attribute):

    def __init__(self, enumClazz: str, values: str, ccore_Enum: "ccore_EnumType" = None):
        self.enumClazz = enumClazz
        self.values = values
        self.ccore_Enum = ccore_Enum
        
    @property
    def enumClazz(self) -> str:
        return self.__enumClazz

    @enumClazz.setter
    def enumClazz(self, enumClazz: str):
        self.__enumClazz = enumClazz

    @property
    def values(self) -> str:
        return self.__values

    @values.setter
    def values(self, values: str):
        self.__values = values

    @property
    def ccore_Enum(self):
        return self.__ccore_Enum

    @ccore_Enum.setter
    def ccore_Enum(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_Enum__ccore_Enum", None)
        self.__ccore_Enum = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccore_EnumType"):
                opp_val = getattr(old_value, "ccore_EnumType", None)
                if opp_val == self:
                    setattr(old_value, "ccore_EnumType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccore_EnumType"):
                opp_val = getattr(value, "ccore_EnumType", None)
                setattr(value, "ccore_EnumType", self)

class RuntimeItem:

    pass
class ccore_ModelController(RuntimeItem):

    pass
class ccore_InteractionController(RuntimeItem):

    pass
class ccore_Display(RuntimeItem):

    def __init__(self, extendsIC: bool, extendsMC: bool, extendsUI: bool, ccore_Display: "ccore_Field" = None):
        self.extendsIC = extendsIC
        self.extendsMC = extendsMC
        self.extendsUI = extendsUI
        self.ccore_Display = ccore_Display
        
    @property
    def extendsIC(self) -> bool:
        return self.__extendsIC

    @extendsIC.setter
    def extendsIC(self, extendsIC: bool):
        self.__extendsIC = extendsIC

    @property
    def extendsMC(self) -> bool:
        return self.__extendsMC

    @extendsMC.setter
    def extendsMC(self, extendsMC: bool):
        self.__extendsMC = extendsMC

    @property
    def extendsUI(self) -> bool:
        return self.__extendsUI

    @extendsUI.setter
    def extendsUI(self, extendsUI: bool):
        self.__extendsUI = extendsUI

    @property
    def ccore_Display(self):
        return self.__ccore_Display

    @ccore_Display.setter
    def ccore_Display(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_Display__ccore_Display", None)
        self.__ccore_Display = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccore_Field119"):
                opp_val = getattr(old_value, "ccore_Field119", None)
                if opp_val == self:
                    setattr(old_value, "ccore_Field119", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccore_Field119"):
                opp_val = getattr(value, "ccore_Field119", None)
                setattr(value, "ccore_Field119", self)

class ccore_ViewItemType:

    def __init__(self, ref: bool, isRootElement: bool, ccore_ViewItemType: "ccore_ItemType" = None, ccore_ViewItemType82: set["ccore_ViewLinkType"] = None, ccore_ViewItemType159: "ccore_View" = None):
        self.ref = ref
        self.isRootElement = isRootElement
        self.ccore_ViewItemType = ccore_ViewItemType
        self.ccore_ViewItemType82 = ccore_ViewItemType82 if ccore_ViewItemType82 is not None else set()
        self.ccore_ViewItemType159 = ccore_ViewItemType159
        
    @property
    def isRootElement(self) -> bool:
        return self.__isRootElement

    @isRootElement.setter
    def isRootElement(self, isRootElement: bool):
        self.__isRootElement = isRootElement

    @property
    def ref(self) -> bool:
        return self.__ref

    @ref.setter
    def ref(self, ref: bool):
        self.__ref = ref

    @property
    def ccore_ViewItemType(self):
        return self.__ccore_ViewItemType

    @ccore_ViewItemType.setter
    def ccore_ViewItemType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_ViewItemType__ccore_ViewItemType", None)
        self.__ccore_ViewItemType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccore_ItemType80"):
                opp_val = getattr(old_value, "ccore_ItemType80", None)
                if opp_val == self:
                    setattr(old_value, "ccore_ItemType80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccore_ItemType80"):
                opp_val = getattr(value, "ccore_ItemType80", None)
                setattr(value, "ccore_ItemType80", self)

    @property
    def ccore_ViewItemType82(self):
        return self.__ccore_ViewItemType82

    @ccore_ViewItemType82.setter
    def ccore_ViewItemType82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_ViewItemType__ccore_ViewItemType82", None)
        self.__ccore_ViewItemType82 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ccore_ViewLinkType"):
                    opp_val = getattr(item, "ccore_ViewLinkType", None)
                    
                    if opp_val == self:
                        setattr(item, "ccore_ViewLinkType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ccore_ViewLinkType"):
                    opp_val = getattr(item, "ccore_ViewLinkType", None)
                    
                    setattr(item, "ccore_ViewLinkType", self)
                    

    @property
    def ccore_ViewItemType159(self):
        return self.__ccore_ViewItemType159

    @ccore_ViewItemType159.setter
    def ccore_ViewItemType159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_ViewItemType__ccore_ViewItemType159", None)
        self.__ccore_ViewItemType159 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccore_View"):
                opp_val = getattr(old_value, "ccore_View", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccore_View"):
                opp_val = getattr(value, "ccore_View", None)
                if opp_val is None:
                    setattr(value, "ccore_View", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ccore_GenInformation:

    def __init__(self, cSTName: str):
        self.cSTName = cSTName
        
    @property
    def cSTName(self) -> str:
        return self.__cSTName

    @cSTName.setter
    def cSTName(self, cSTName: str):
        self.__cSTName = cSTName

class ItemType:

    pass
class ccore_RuntimeItemType(ItemType):

    pass
class ccore_EStructuralFeature:

    pass
class ccore_ViewDescription:

    pass
class ccore_ViewLinkType:

    def __init__(self, canCreateItem: bool, canCreateLink: bool, displayCreate: str, aggregation: bool, ccore_ViewLinkType: "ccore_ViewItemType" = None, ccore_ViewLinkType135: "ccore_LinkType" = None):
        self.canCreateItem = canCreateItem
        self.canCreateLink = canCreateLink
        self.displayCreate = displayCreate
        self.aggregation = aggregation
        self.ccore_ViewLinkType = ccore_ViewLinkType
        self.ccore_ViewLinkType135 = ccore_ViewLinkType135
        
    @property
    def aggregation(self) -> bool:
        return self.__aggregation

    @aggregation.setter
    def aggregation(self, aggregation: bool):
        self.__aggregation = aggregation

    @property
    def canCreateItem(self) -> bool:
        return self.__canCreateItem

    @canCreateItem.setter
    def canCreateItem(self, canCreateItem: bool):
        self.__canCreateItem = canCreateItem

    @property
    def canCreateLink(self) -> bool:
        return self.__canCreateLink

    @canCreateLink.setter
    def canCreateLink(self, canCreateLink: bool):
        self.__canCreateLink = canCreateLink

    @property
    def displayCreate(self) -> str:
        return self.__displayCreate

    @displayCreate.setter
    def displayCreate(self, displayCreate: str):
        self.__displayCreate = displayCreate

    @property
    def ccore_ViewLinkType135(self):
        return self.__ccore_ViewLinkType135

    @ccore_ViewLinkType135.setter
    def ccore_ViewLinkType135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_ViewLinkType__ccore_ViewLinkType135", None)
        self.__ccore_ViewLinkType135 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccore_LinkType136"):
                opp_val = getattr(old_value, "ccore_LinkType136", None)
                if opp_val == self:
                    setattr(old_value, "ccore_LinkType136", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccore_LinkType136"):
                opp_val = getattr(value, "ccore_LinkType136", None)
                setattr(value, "ccore_LinkType136", self)

    @property
    def ccore_ViewLinkType(self):
        return self.__ccore_ViewLinkType

    @ccore_ViewLinkType.setter
    def ccore_ViewLinkType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_ViewLinkType__ccore_ViewLinkType", None)
        self.__ccore_ViewLinkType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccore_ViewItemType82"):
                opp_val = getattr(old_value, "ccore_ViewItemType82", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccore_ViewItemType82"):
                opp_val = getattr(value, "ccore_ViewItemType82", None)
                if opp_val is None:
                    setattr(value, "ccore_ViewItemType82", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class EAttribute:

    pass
class ccore_Composer(RuntimeItem):

    def __init__(self, types: str, Composer: "ccore_Item" = None, ccore_Composer: set["ccore_LinkType"] = None, ccore_Composer145: set["ccore_ComposerLink"] = None, composers: "ccore_Item" = None):
        self.types = types
        self.Composer = Composer
        self.ccore_Composer = ccore_Composer if ccore_Composer is not None else set()
        self.ccore_Composer145 = ccore_Composer145 if ccore_Composer145 is not None else set()
        self.composers = composers
        
    @property
    def types(self) -> str:
        return self.__types

    @types.setter
    def types(self, types: str):
        self.__types = types

    @property
    def ccore_Composer145(self):
        return self.__ccore_Composer145

    @ccore_Composer145.setter
    def ccore_Composer145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_Composer__ccore_Composer145", None)
        self.__ccore_Composer145 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ccore_ComposerLink"):
                    opp_val = getattr(item, "ccore_ComposerLink", None)
                    
                    if opp_val == self:
                        setattr(item, "ccore_ComposerLink", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ccore_ComposerLink"):
                    opp_val = getattr(item, "ccore_ComposerLink", None)
                    
                    setattr(item, "ccore_ComposerLink", self)
                    

    @property
    def composers(self):
        return self.__composers

    @composers.setter
    def composers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_Composer__composers", None)
        self.__composers = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Item"):
                opp_val = getattr(old_value, "Item", None)
                if opp_val == self:
                    setattr(old_value, "Item", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Item"):
                opp_val = getattr(value, "Item", None)
                setattr(value, "Item", self)

    @property
    def Composer(self):
        return self.__Composer

    @Composer.setter
    def Composer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_Composer__Composer", None)
        self.__Composer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownerItem70"):
                opp_val = getattr(old_value, "ownerItem70", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownerItem70"):
                opp_val = getattr(value, "ownerItem70", None)
                if opp_val is None:
                    setattr(value, "ownerItem70", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ccore_Composer(self):
        return self.__ccore_Composer

    @ccore_Composer.setter
    def ccore_Composer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_Composer__ccore_Composer", None)
        self.__ccore_Composer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ccore_LinkType143"):
                    opp_val = getattr(item, "ccore_LinkType143", None)
                    
                    if opp_val == self:
                        setattr(item, "ccore_LinkType143", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ccore_LinkType143"):
                    opp_val = getattr(item, "ccore_LinkType143", None)
                    
                    setattr(item, "ccore_LinkType143", self)
                    

class ccore_Exporter(RuntimeItem):

    def __init__(self, types: str, Exporter: "ccore_Item" = None, exporters: "ccore_Item" = None, ccore_Exporter: "ccore_ComposerLink" = None):
        self.types = types
        self.Exporter = Exporter
        self.exporters = exporters
        self.ccore_Exporter = ccore_Exporter
        
    @property
    def types(self) -> str:
        return self.__types

    @types.setter
    def types(self, types: str):
        self.__types = types

    @property
    def Exporter(self):
        return self.__Exporter

    @Exporter.setter
    def Exporter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_Exporter__Exporter", None)
        self.__Exporter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownerItem68"):
                opp_val = getattr(old_value, "ownerItem68", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownerItem68"):
                opp_val = getattr(value, "ownerItem68", None)
                if opp_val is None:
                    setattr(value, "ownerItem68", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ccore_Exporter(self):
        return self.__ccore_Exporter

    @ccore_Exporter.setter
    def ccore_Exporter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_Exporter__ccore_Exporter", None)
        self.__ccore_Exporter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccore_ComposerLink154"):
                opp_val = getattr(old_value, "ccore_ComposerLink154", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccore_ComposerLink154"):
                opp_val = getattr(value, "ccore_ComposerLink154", None)
                if opp_val is None:
                    setattr(value, "ccore_ComposerLink154", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def exporters(self):
        return self.__exporters

    @exporters.setter
    def exporters(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_Exporter__exporters", None)
        self.__exporters = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Item148"):
                opp_val = getattr(old_value, "Item148", None)
                if opp_val == self:
                    setattr(old_value, "Item148", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Item148"):
                opp_val = getattr(value, "Item148", None)
                setattr(value, "Item148", self)

class ccore_ContentItem:

    pass
class DBObject:

    pass
class ENamedElement:

    pass
class ccore_Item(ENamedElement, DBObject):

    def __init__(self, committedBy: str, displayName: str, itemHidden: bool, itemReadonly: bool, qualifiedName: str, twRequireNewRev: bool, twVersion: int, twRevModified: bool, twCommittedDate: str, isvalid: bool, ccore_Item59: "ccore_Item" = None, ccore_Item57: "ccore_Item" = None, ccore_Item61: set["ccore_Attribute"] = None, ccore_Item: "ccore_Cadse" = None, ccore_Item55: set["ccore_ItemType"] = None, ownerItem: set["ccore_ContentItem"] = None, ccore_Item65: "ccore_Cadse" = None, ownerItem68: set["ccore_Exporter"] = None, ownerItem70: set["ccore_Composer"] = None, ccore_Item138: "ccore_GroupExtItem" = None, ccore_Item141: "ccore_GroupExtItem" = None, Item: "ccore_Composer" = None, Item148: "ccore_Exporter" = None, Item150: "ccore_ContentItem" = None, ccore_Item164: "ccore_BindingDesc" = None, ccore_Item167: "ccore_BindingDesc" = None):
        self.committedBy = committedBy
        self.displayName = displayName
        self.itemHidden = itemHidden
        self.itemReadonly = itemReadonly
        self.qualifiedName = qualifiedName
        self.twRequireNewRev = twRequireNewRev
        self.twVersion = twVersion
        self.twRevModified = twRevModified
        self.twCommittedDate = twCommittedDate
        self.isvalid = isvalid
        self.ccore_Item59 = ccore_Item59
        self.ccore_Item57 = ccore_Item57
        self.ccore_Item61 = ccore_Item61 if ccore_Item61 is not None else set()
        self.ccore_Item = ccore_Item
        self.ccore_Item55 = ccore_Item55 if ccore_Item55 is not None else set()
        self.ownerItem = ownerItem if ownerItem is not None else set()
        self.ccore_Item65 = ccore_Item65
        self.ownerItem68 = ownerItem68 if ownerItem68 is not None else set()
        self.ownerItem70 = ownerItem70 if ownerItem70 is not None else set()
        self.ccore_Item138 = ccore_Item138
        self.ccore_Item141 = ccore_Item141
        self.Item = Item
        self.Item148 = Item148
        self.Item150 = Item150
        self.ccore_Item164 = ccore_Item164
        self.ccore_Item167 = ccore_Item167
        
    @property
    def twRevModified(self) -> bool:
        return self.__twRevModified

    @twRevModified.setter
    def twRevModified(self, twRevModified: bool):
        self.__twRevModified = twRevModified

    @property
    def displayName(self) -> str:
        return self.__displayName

    @displayName.setter
    def displayName(self, displayName: str):
        self.__displayName = displayName

    @property
    def qualifiedName(self) -> str:
        return self.__qualifiedName

    @qualifiedName.setter
    def qualifiedName(self, qualifiedName: str):
        self.__qualifiedName = qualifiedName

    @property
    def twCommittedDate(self) -> str:
        return self.__twCommittedDate

    @twCommittedDate.setter
    def twCommittedDate(self, twCommittedDate: str):
        self.__twCommittedDate = twCommittedDate

    @property
    def twRequireNewRev(self) -> bool:
        return self.__twRequireNewRev

    @twRequireNewRev.setter
    def twRequireNewRev(self, twRequireNewRev: bool):
        self.__twRequireNewRev = twRequireNewRev

    @property
    def itemReadonly(self) -> bool:
        return self.__itemReadonly

    @itemReadonly.setter
    def itemReadonly(self, itemReadonly: bool):
        self.__itemReadonly = itemReadonly

    @property
    def isvalid(self) -> bool:
        return self.__isvalid

    @isvalid.setter
    def isvalid(self, isvalid: bool):
        self.__isvalid = isvalid

    @property
    def itemHidden(self) -> bool:
        return self.__itemHidden

    @itemHidden.setter
    def itemHidden(self, itemHidden: bool):
        self.__itemHidden = itemHidden

    @property
    def committedBy(self) -> str:
        return self.__committedBy

    @committedBy.setter
    def committedBy(self, committedBy: str):
        self.__committedBy = committedBy

    @property
    def twVersion(self) -> int:
        return self.__twVersion

    @twVersion.setter
    def twVersion(self, twVersion: int):
        self.__twVersion = twVersion

    @property
    def Item148(self):
        return self.__Item148

    @Item148.setter
    def Item148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_Item__Item148", None)
        self.__Item148 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "exporters"):
                opp_val = getattr(old_value, "exporters", None)
                if opp_val == self:
                    setattr(old_value, "exporters", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "exporters"):
                opp_val = getattr(value, "exporters", None)
                setattr(value, "exporters", self)

    @property
    def ccore_Item55(self):
        return self.__ccore_Item55

    @ccore_Item55.setter
    def ccore_Item55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_Item__ccore_Item55", None)
        self.__ccore_Item55 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ccore_ItemType56"):
                    opp_val = getattr(item, "ccore_ItemType56", None)
                    
                    if opp_val == self:
                        setattr(item, "ccore_ItemType56", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ccore_ItemType56"):
                    opp_val = getattr(item, "ccore_ItemType56", None)
                    
                    setattr(item, "ccore_ItemType56", self)
                    

    @property
    def ccore_Item61(self):
        return self.__ccore_Item61

    @ccore_Item61.setter
    def ccore_Item61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_Item__ccore_Item61", None)
        self.__ccore_Item61 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ccore_Attribute62"):
                    opp_val = getattr(item, "ccore_Attribute62", None)
                    
                    if opp_val == self:
                        setattr(item, "ccore_Attribute62", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ccore_Attribute62"):
                    opp_val = getattr(item, "ccore_Attribute62", None)
                    
                    setattr(item, "ccore_Attribute62", self)
                    

    @property
    def ownerItem70(self):
        return self.__ownerItem70

    @ownerItem70.setter
    def ownerItem70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_Item__ownerItem70", None)
        self.__ownerItem70 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Composer"):
                    opp_val = getattr(item, "Composer", None)
                    
                    if opp_val == self:
                        setattr(item, "Composer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Composer"):
                    opp_val = getattr(item, "Composer", None)
                    
                    setattr(item, "Composer", self)
                    

    @property
    def ccore_Item164(self):
        return self.__ccore_Item164

    @ccore_Item164.setter
    def ccore_Item164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_Item__ccore_Item164", None)
        self.__ccore_Item164 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccore_BindingDesc163"):
                opp_val = getattr(old_value, "ccore_BindingDesc163", None)
                if opp_val == self:
                    setattr(old_value, "ccore_BindingDesc163", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccore_BindingDesc163"):
                opp_val = getattr(value, "ccore_BindingDesc163", None)
                setattr(value, "ccore_BindingDesc163", self)

    @property
    def ownerItem(self):
        return self.__ownerItem

    @ownerItem.setter
    def ownerItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_Item__ownerItem", None)
        self.__ownerItem = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ContentItem"):
                    opp_val = getattr(item, "ContentItem", None)
                    
                    if opp_val == self:
                        setattr(item, "ContentItem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ContentItem"):
                    opp_val = getattr(item, "ContentItem", None)
                    
                    setattr(item, "ContentItem", self)
                    

    @property
    def ccore_Item57(self):
        return self.__ccore_Item57

    @ccore_Item57.setter
    def ccore_Item57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_Item__ccore_Item57", None)
        self.__ccore_Item57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccore_Item59"):
                opp_val = getattr(old_value, "ccore_Item59", None)
                if opp_val == self:
                    setattr(old_value, "ccore_Item59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccore_Item59"):
                opp_val = getattr(value, "ccore_Item59", None)
                setattr(value, "ccore_Item59", self)

    @property
    def ownerItem68(self):
        return self.__ownerItem68

    @ownerItem68.setter
    def ownerItem68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_Item__ownerItem68", None)
        self.__ownerItem68 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Exporter"):
                    opp_val = getattr(item, "Exporter", None)
                    
                    if opp_val == self:
                        setattr(item, "Exporter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Exporter"):
                    opp_val = getattr(item, "Exporter", None)
                    
                    setattr(item, "Exporter", self)
                    

    @property
    def ccore_Item(self):
        return self.__ccore_Item

    @ccore_Item.setter
    def ccore_Item(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_Item__ccore_Item", None)
        self.__ccore_Item = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccore_Cadse53"):
                opp_val = getattr(old_value, "ccore_Cadse53", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccore_Cadse53"):
                opp_val = getattr(value, "ccore_Cadse53", None)
                if opp_val is None:
                    setattr(value, "ccore_Cadse53", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ccore_Item138(self):
        return self.__ccore_Item138

    @ccore_Item138.setter
    def ccore_Item138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_Item__ccore_Item138", None)
        self.__ccore_Item138 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccore_GroupExtItem"):
                opp_val = getattr(old_value, "ccore_GroupExtItem", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccore_GroupExtItem"):
                opp_val = getattr(value, "ccore_GroupExtItem", None)
                if opp_val is None:
                    setattr(value, "ccore_GroupExtItem", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Item150(self):
        return self.__Item150

    @Item150.setter
    def Item150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_Item__Item150", None)
        self.__Item150 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contents"):
                opp_val = getattr(old_value, "contents", None)
                if opp_val == self:
                    setattr(old_value, "contents", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contents"):
                opp_val = getattr(value, "contents", None)
                setattr(value, "contents", self)

    @property
    def ccore_Item59(self):
        return self.__ccore_Item59

    @ccore_Item59.setter
    def ccore_Item59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_Item__ccore_Item59", None)
        self.__ccore_Item59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccore_Item57"):
                opp_val = getattr(old_value, "ccore_Item57", None)
                if opp_val == self:
                    setattr(old_value, "ccore_Item57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccore_Item57"):
                opp_val = getattr(value, "ccore_Item57", None)
                setattr(value, "ccore_Item57", self)

    @property
    def ccore_Item65(self):
        return self.__ccore_Item65

    @ccore_Item65.setter
    def ccore_Item65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_Item__ccore_Item65", None)
        self.__ccore_Item65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccore_Cadse66"):
                opp_val = getattr(old_value, "ccore_Cadse66", None)
                if opp_val == self:
                    setattr(old_value, "ccore_Cadse66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccore_Cadse66"):
                opp_val = getattr(value, "ccore_Cadse66", None)
                setattr(value, "ccore_Cadse66", self)

    @property
    def ccore_Item167(self):
        return self.__ccore_Item167

    @ccore_Item167.setter
    def ccore_Item167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_Item__ccore_Item167", None)
        self.__ccore_Item167 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccore_BindingDesc166"):
                opp_val = getattr(old_value, "ccore_BindingDesc166", None)
                if opp_val == self:
                    setattr(old_value, "ccore_BindingDesc166", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccore_BindingDesc166"):
                opp_val = getattr(value, "ccore_BindingDesc166", None)
                setattr(value, "ccore_BindingDesc166", self)

    @property
    def Item(self):
        return self.__Item

    @Item.setter
    def Item(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_Item__Item", None)
        self.__Item = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composers"):
                opp_val = getattr(old_value, "composers", None)
                if opp_val == self:
                    setattr(old_value, "composers", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composers"):
                opp_val = getattr(value, "composers", None)
                setattr(value, "composers", self)

    @property
    def ccore_Item141(self):
        return self.__ccore_Item141

    @ccore_Item141.setter
    def ccore_Item141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_Item__ccore_Item141", None)
        self.__ccore_Item141 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccore_GroupExtItem140"):
                opp_val = getattr(old_value, "ccore_GroupExtItem140", None)
                if opp_val == self:
                    setattr(old_value, "ccore_GroupExtItem140", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccore_GroupExtItem140"):
                opp_val = getattr(value, "ccore_GroupExtItem140", None)
                setattr(value, "ccore_GroupExtItem140", self)

class ccore_BindingDesc(DBObject):

    pass
class ccore_EPackage:

    pass
class EPackage:

    pass
class ccore_ComposerType(RuntimeItemType):

    pass
class ccore_ExporterType(RuntimeItemType):

    pass
class ccore_ContentItemType(ItemType):

    def __init__(self, extendsClass: bool, ccore_ContentItemType: "ccore_ItemType" = None, ccore_ContentItemType36: "ccore_ItemType" = None):
        self.extendsClass = extendsClass
        self.ccore_ContentItemType = ccore_ContentItemType
        self.ccore_ContentItemType36 = ccore_ContentItemType36
        
    @property
    def extendsClass(self) -> bool:
        return self.__extendsClass

    @extendsClass.setter
    def extendsClass(self, extendsClass: bool):
        self.__extendsClass = extendsClass

    @property
    def ccore_ContentItemType(self):
        return self.__ccore_ContentItemType

    @ccore_ContentItemType.setter
    def ccore_ContentItemType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_ContentItemType__ccore_ContentItemType", None)
        self.__ccore_ContentItemType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccore_ItemType29"):
                opp_val = getattr(old_value, "ccore_ItemType29", None)
                if opp_val == self:
                    setattr(old_value, "ccore_ItemType29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccore_ItemType29"):
                opp_val = getattr(value, "ccore_ItemType29", None)
                setattr(value, "ccore_ItemType29", self)

    @property
    def ccore_ContentItemType36(self):
        return self.__ccore_ContentItemType36

    @ccore_ContentItemType36.setter
    def ccore_ContentItemType36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_ContentItemType__ccore_ContentItemType36", None)
        self.__ccore_ContentItemType36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccore_ItemType35"):
                opp_val = getattr(old_value, "ccore_ItemType35", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccore_ItemType35"):
                opp_val = getattr(value, "ccore_ItemType35", None)
                if opp_val is None:
                    setattr(value, "ccore_ItemType35", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class TypeDefinition:

    pass
class ccore_ItemType(TypeDefinition):

    def __init__(self, hasUniqueName: bool, isMetaItemType: bool, isInstanceHidden: bool, overwriteDefaultPages: bool, icon: str, itemFactoryClass: str, hasContent: bool, isRootElement: bool, isInstanceAbstract: bool, hasShortName: bool, itemManagerClass: str, packageName: str, customManager: bool, managerClass: str, qualifiedNameTemplate: str, messageErrorId: str, validateNameRe: str, displayNameTemplate: str, humanName: str, ccore_ItemType19: set["ccore_WCListener"] = None, ccore_ItemType: "ccore_ExtentedType" = None, ccore_ItemType17: "ccore_ItemType" = None, ccore_ItemType15: set["ccore_ItemType"] = None, ccore_ItemType41: "ccore_Cadse" = None, ccore_ItemType22: "ccore_ItemType" = None, ccore_ItemType20: set["ccore_ItemType"] = None, ccore_ItemType24: set["ccore_ExtentedType"] = None, ccore_ItemType27: "ccore_KeyDefinition" = None, ccore_ItemType29: "ccore_ContentItemType" = None, ccore_ItemType31: set["ccore_ExporterType"] = None, ccore_ItemType33: set["ccore_ComposerType"] = None, ccore_ItemType35: set["ccore_ContentItemType"] = None, ccore_ItemType56: "ccore_Item" = None, ccore_ItemType80: "ccore_ViewItemType" = None, ccore_ItemType86: "ccore_BindExt" = None, ccore_ItemType107: "ccore_WCListener" = None, ccore_ItemType172: "ccore_DBObject" = None):
        self.hasUniqueName = hasUniqueName
        self.isMetaItemType = isMetaItemType
        self.isInstanceHidden = isInstanceHidden
        self.overwriteDefaultPages = overwriteDefaultPages
        self.icon = icon
        self.itemFactoryClass = itemFactoryClass
        self.hasContent = hasContent
        self.isRootElement = isRootElement
        self.isInstanceAbstract = isInstanceAbstract
        self.hasShortName = hasShortName
        self.itemManagerClass = itemManagerClass
        self.packageName = packageName
        self.customManager = customManager
        self.managerClass = managerClass
        self.qualifiedNameTemplate = qualifiedNameTemplate
        self.messageErrorId = messageErrorId
        self.validateNameRe = validateNameRe
        self.displayNameTemplate = displayNameTemplate
        self.humanName = humanName
        self.ccore_ItemType19 = ccore_ItemType19 if ccore_ItemType19 is not None else set()
        self.ccore_ItemType = ccore_ItemType
        self.ccore_ItemType17 = ccore_ItemType17
        self.ccore_ItemType15 = ccore_ItemType15 if ccore_ItemType15 is not None else set()
        self.ccore_ItemType41 = ccore_ItemType41
        self.ccore_ItemType22 = ccore_ItemType22
        self.ccore_ItemType20 = ccore_ItemType20 if ccore_ItemType20 is not None else set()
        self.ccore_ItemType24 = ccore_ItemType24 if ccore_ItemType24 is not None else set()
        self.ccore_ItemType27 = ccore_ItemType27
        self.ccore_ItemType29 = ccore_ItemType29
        self.ccore_ItemType31 = ccore_ItemType31 if ccore_ItemType31 is not None else set()
        self.ccore_ItemType33 = ccore_ItemType33 if ccore_ItemType33 is not None else set()
        self.ccore_ItemType35 = ccore_ItemType35 if ccore_ItemType35 is not None else set()
        self.ccore_ItemType56 = ccore_ItemType56
        self.ccore_ItemType80 = ccore_ItemType80
        self.ccore_ItemType86 = ccore_ItemType86
        self.ccore_ItemType107 = ccore_ItemType107
        self.ccore_ItemType172 = ccore_ItemType172
        
    @property
    def isRootElement(self) -> bool:
        return self.__isRootElement

    @isRootElement.setter
    def isRootElement(self, isRootElement: bool):
        self.__isRootElement = isRootElement

    @property
    def hasUniqueName(self) -> bool:
        return self.__hasUniqueName

    @hasUniqueName.setter
    def hasUniqueName(self, hasUniqueName: bool):
        self.__hasUniqueName = hasUniqueName

    @property
    def isMetaItemType(self) -> bool:
        return self.__isMetaItemType

    @isMetaItemType.setter
    def isMetaItemType(self, isMetaItemType: bool):
        self.__isMetaItemType = isMetaItemType

    @property
    def customManager(self) -> bool:
        return self.__customManager

    @customManager.setter
    def customManager(self, customManager: bool):
        self.__customManager = customManager

    @property
    def validateNameRe(self) -> str:
        return self.__validateNameRe

    @validateNameRe.setter
    def validateNameRe(self, validateNameRe: str):
        self.__validateNameRe = validateNameRe

    @property
    def packageName(self) -> str:
        return self.__packageName

    @packageName.setter
    def packageName(self, packageName: str):
        self.__packageName = packageName

    @property
    def itemFactoryClass(self) -> str:
        return self.__itemFactoryClass

    @itemFactoryClass.setter
    def itemFactoryClass(self, itemFactoryClass: str):
        self.__itemFactoryClass = itemFactoryClass

    @property
    def icon(self) -> str:
        return self.__icon

    @icon.setter
    def icon(self, icon: str):
        self.__icon = icon

    @property
    def isInstanceHidden(self) -> bool:
        return self.__isInstanceHidden

    @isInstanceHidden.setter
    def isInstanceHidden(self, isInstanceHidden: bool):
        self.__isInstanceHidden = isInstanceHidden

    @property
    def isInstanceAbstract(self) -> bool:
        return self.__isInstanceAbstract

    @isInstanceAbstract.setter
    def isInstanceAbstract(self, isInstanceAbstract: bool):
        self.__isInstanceAbstract = isInstanceAbstract

    @property
    def displayNameTemplate(self) -> str:
        return self.__displayNameTemplate

    @displayNameTemplate.setter
    def displayNameTemplate(self, displayNameTemplate: str):
        self.__displayNameTemplate = displayNameTemplate

    @property
    def messageErrorId(self) -> str:
        return self.__messageErrorId

    @messageErrorId.setter
    def messageErrorId(self, messageErrorId: str):
        self.__messageErrorId = messageErrorId

    @property
    def managerClass(self) -> str:
        return self.__managerClass

    @managerClass.setter
    def managerClass(self, managerClass: str):
        self.__managerClass = managerClass

    @property
    def overwriteDefaultPages(self) -> bool:
        return self.__overwriteDefaultPages

    @overwriteDefaultPages.setter
    def overwriteDefaultPages(self, overwriteDefaultPages: bool):
        self.__overwriteDefaultPages = overwriteDefaultPages

    @property
    def hasShortName(self) -> bool:
        return self.__hasShortName

    @hasShortName.setter
    def hasShortName(self, hasShortName: bool):
        self.__hasShortName = hasShortName

    @property
    def hasContent(self) -> bool:
        return self.__hasContent

    @hasContent.setter
    def hasContent(self, hasContent: bool):
        self.__hasContent = hasContent

    @property
    def itemManagerClass(self) -> str:
        return self.__itemManagerClass

    @itemManagerClass.setter
    def itemManagerClass(self, itemManagerClass: str):
        self.__itemManagerClass = itemManagerClass

    @property
    def humanName(self) -> str:
        return self.__humanName

    @humanName.setter
    def humanName(self, humanName: str):
        self.__humanName = humanName

    @property
    def qualifiedNameTemplate(self) -> str:
        return self.__qualifiedNameTemplate

    @qualifiedNameTemplate.setter
    def qualifiedNameTemplate(self, qualifiedNameTemplate: str):
        self.__qualifiedNameTemplate = qualifiedNameTemplate

    @property
    def ccore_ItemType19(self):
        return self.__ccore_ItemType19

    @ccore_ItemType19.setter
    def ccore_ItemType19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_ItemType__ccore_ItemType19", None)
        self.__ccore_ItemType19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ccore_WCListener"):
                    opp_val = getattr(item, "ccore_WCListener", None)
                    
                    if opp_val == self:
                        setattr(item, "ccore_WCListener", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ccore_WCListener"):
                    opp_val = getattr(item, "ccore_WCListener", None)
                    
                    setattr(item, "ccore_WCListener", self)
                    

    @property
    def ccore_ItemType22(self):
        return self.__ccore_ItemType22

    @ccore_ItemType22.setter
    def ccore_ItemType22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_ItemType__ccore_ItemType22", None)
        self.__ccore_ItemType22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccore_ItemType20"):
                opp_val = getattr(old_value, "ccore_ItemType20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccore_ItemType20"):
                opp_val = getattr(value, "ccore_ItemType20", None)
                if opp_val is None:
                    setattr(value, "ccore_ItemType20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ccore_ItemType35(self):
        return self.__ccore_ItemType35

    @ccore_ItemType35.setter
    def ccore_ItemType35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_ItemType__ccore_ItemType35", None)
        self.__ccore_ItemType35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ccore_ContentItemType36"):
                    opp_val = getattr(item, "ccore_ContentItemType36", None)
                    
                    if opp_val == self:
                        setattr(item, "ccore_ContentItemType36", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ccore_ContentItemType36"):
                    opp_val = getattr(item, "ccore_ContentItemType36", None)
                    
                    setattr(item, "ccore_ContentItemType36", self)
                    

    @property
    def ccore_ItemType27(self):
        return self.__ccore_ItemType27

    @ccore_ItemType27.setter
    def ccore_ItemType27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_ItemType__ccore_ItemType27", None)
        self.__ccore_ItemType27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccore_KeyDefinition"):
                opp_val = getattr(old_value, "ccore_KeyDefinition", None)
                if opp_val == self:
                    setattr(old_value, "ccore_KeyDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccore_KeyDefinition"):
                opp_val = getattr(value, "ccore_KeyDefinition", None)
                setattr(value, "ccore_KeyDefinition", self)

    @property
    def ccore_ItemType(self):
        return self.__ccore_ItemType

    @ccore_ItemType.setter
    def ccore_ItemType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_ItemType__ccore_ItemType", None)
        self.__ccore_ItemType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccore_ExtentedType"):
                opp_val = getattr(old_value, "ccore_ExtentedType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccore_ExtentedType"):
                opp_val = getattr(value, "ccore_ExtentedType", None)
                if opp_val is None:
                    setattr(value, "ccore_ExtentedType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ccore_ItemType31(self):
        return self.__ccore_ItemType31

    @ccore_ItemType31.setter
    def ccore_ItemType31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_ItemType__ccore_ItemType31", None)
        self.__ccore_ItemType31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ccore_ExporterType"):
                    opp_val = getattr(item, "ccore_ExporterType", None)
                    
                    if opp_val == self:
                        setattr(item, "ccore_ExporterType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ccore_ExporterType"):
                    opp_val = getattr(item, "ccore_ExporterType", None)
                    
                    setattr(item, "ccore_ExporterType", self)
                    

    @property
    def ccore_ItemType20(self):
        return self.__ccore_ItemType20

    @ccore_ItemType20.setter
    def ccore_ItemType20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_ItemType__ccore_ItemType20", None)
        self.__ccore_ItemType20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ccore_ItemType22"):
                    opp_val = getattr(item, "ccore_ItemType22", None)
                    
                    if opp_val == self:
                        setattr(item, "ccore_ItemType22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ccore_ItemType22"):
                    opp_val = getattr(item, "ccore_ItemType22", None)
                    
                    setattr(item, "ccore_ItemType22", self)
                    

    @property
    def ccore_ItemType172(self):
        return self.__ccore_ItemType172

    @ccore_ItemType172.setter
    def ccore_ItemType172(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_ItemType__ccore_ItemType172", None)
        self.__ccore_ItemType172 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccore_DBObject"):
                opp_val = getattr(old_value, "ccore_DBObject", None)
                if opp_val == self:
                    setattr(old_value, "ccore_DBObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccore_DBObject"):
                opp_val = getattr(value, "ccore_DBObject", None)
                setattr(value, "ccore_DBObject", self)

    @property
    def ccore_ItemType41(self):
        return self.__ccore_ItemType41

    @ccore_ItemType41.setter
    def ccore_ItemType41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_ItemType__ccore_ItemType41", None)
        self.__ccore_ItemType41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccore_Cadse40"):
                opp_val = getattr(old_value, "ccore_Cadse40", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccore_Cadse40"):
                opp_val = getattr(value, "ccore_Cadse40", None)
                if opp_val is None:
                    setattr(value, "ccore_Cadse40", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ccore_ItemType107(self):
        return self.__ccore_ItemType107

    @ccore_ItemType107.setter
    def ccore_ItemType107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_ItemType__ccore_ItemType107", None)
        self.__ccore_ItemType107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccore_WCListener106"):
                opp_val = getattr(old_value, "ccore_WCListener106", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccore_WCListener106"):
                opp_val = getattr(value, "ccore_WCListener106", None)
                if opp_val is None:
                    setattr(value, "ccore_WCListener106", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ccore_ItemType56(self):
        return self.__ccore_ItemType56

    @ccore_ItemType56.setter
    def ccore_ItemType56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_ItemType__ccore_ItemType56", None)
        self.__ccore_ItemType56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccore_Item55"):
                opp_val = getattr(old_value, "ccore_Item55", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccore_Item55"):
                opp_val = getattr(value, "ccore_Item55", None)
                if opp_val is None:
                    setattr(value, "ccore_Item55", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ccore_ItemType15(self):
        return self.__ccore_ItemType15

    @ccore_ItemType15.setter
    def ccore_ItemType15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_ItemType__ccore_ItemType15", None)
        self.__ccore_ItemType15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ccore_ItemType17"):
                    opp_val = getattr(item, "ccore_ItemType17", None)
                    
                    if opp_val == self:
                        setattr(item, "ccore_ItemType17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ccore_ItemType17"):
                    opp_val = getattr(item, "ccore_ItemType17", None)
                    
                    setattr(item, "ccore_ItemType17", self)
                    

    @property
    def ccore_ItemType86(self):
        return self.__ccore_ItemType86

    @ccore_ItemType86.setter
    def ccore_ItemType86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_ItemType__ccore_ItemType86", None)
        self.__ccore_ItemType86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccore_BindExt"):
                opp_val = getattr(old_value, "ccore_BindExt", None)
                if opp_val == self:
                    setattr(old_value, "ccore_BindExt", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccore_BindExt"):
                opp_val = getattr(value, "ccore_BindExt", None)
                setattr(value, "ccore_BindExt", self)

    @property
    def ccore_ItemType29(self):
        return self.__ccore_ItemType29

    @ccore_ItemType29.setter
    def ccore_ItemType29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_ItemType__ccore_ItemType29", None)
        self.__ccore_ItemType29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccore_ContentItemType"):
                opp_val = getattr(old_value, "ccore_ContentItemType", None)
                if opp_val == self:
                    setattr(old_value, "ccore_ContentItemType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccore_ContentItemType"):
                opp_val = getattr(value, "ccore_ContentItemType", None)
                setattr(value, "ccore_ContentItemType", self)

    @property
    def ccore_ItemType80(self):
        return self.__ccore_ItemType80

    @ccore_ItemType80.setter
    def ccore_ItemType80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_ItemType__ccore_ItemType80", None)
        self.__ccore_ItemType80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccore_ViewItemType"):
                opp_val = getattr(old_value, "ccore_ViewItemType", None)
                if opp_val == self:
                    setattr(old_value, "ccore_ViewItemType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccore_ViewItemType"):
                opp_val = getattr(value, "ccore_ViewItemType", None)
                setattr(value, "ccore_ViewItemType", self)

    @property
    def ccore_ItemType33(self):
        return self.__ccore_ItemType33

    @ccore_ItemType33.setter
    def ccore_ItemType33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_ItemType__ccore_ItemType33", None)
        self.__ccore_ItemType33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ccore_ComposerType"):
                    opp_val = getattr(item, "ccore_ComposerType", None)
                    
                    if opp_val == self:
                        setattr(item, "ccore_ComposerType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ccore_ComposerType"):
                    opp_val = getattr(item, "ccore_ComposerType", None)
                    
                    setattr(item, "ccore_ComposerType", self)
                    

    @property
    def ccore_ItemType17(self):
        return self.__ccore_ItemType17

    @ccore_ItemType17.setter
    def ccore_ItemType17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_ItemType__ccore_ItemType17", None)
        self.__ccore_ItemType17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccore_ItemType15"):
                opp_val = getattr(old_value, "ccore_ItemType15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccore_ItemType15"):
                opp_val = getattr(value, "ccore_ItemType15", None)
                if opp_val is None:
                    setattr(value, "ccore_ItemType15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ccore_ItemType24(self):
        return self.__ccore_ItemType24

    @ccore_ItemType24.setter
    def ccore_ItemType24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_ItemType__ccore_ItemType24", None)
        self.__ccore_ItemType24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ccore_ExtentedType25"):
                    opp_val = getattr(item, "ccore_ExtentedType25", None)
                    
                    if opp_val == self:
                        setattr(item, "ccore_ExtentedType25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ccore_ExtentedType25"):
                    opp_val = getattr(item, "ccore_ExtentedType25", None)
                    
                    setattr(item, "ccore_ExtentedType25", self)
                    

class ccore_ExtentedType(TypeDefinition):

    pass
class ccore_EClass:

    pass
class ccore_GroupOfAttributes:

    def __init__(self, column: int, ccore_GroupOfAttributes: "ccore_TypeDefinition" = None, ccore_GroupOfAttributes129: set["ccore_Attribute"] = None, ccore_GroupOfAttributes133: "ccore_GroupOfAttributes" = None, ccore_GroupOfAttributes131: "ccore_GroupOfAttributes" = None):
        self.column = column
        self.ccore_GroupOfAttributes = ccore_GroupOfAttributes
        self.ccore_GroupOfAttributes129 = ccore_GroupOfAttributes129 if ccore_GroupOfAttributes129 is not None else set()
        self.ccore_GroupOfAttributes133 = ccore_GroupOfAttributes133
        self.ccore_GroupOfAttributes131 = ccore_GroupOfAttributes131
        
    @property
    def column(self) -> int:
        return self.__column

    @column.setter
    def column(self, column: int):
        self.__column = column

    @property
    def ccore_GroupOfAttributes133(self):
        return self.__ccore_GroupOfAttributes133

    @ccore_GroupOfAttributes133.setter
    def ccore_GroupOfAttributes133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_GroupOfAttributes__ccore_GroupOfAttributes133", None)
        self.__ccore_GroupOfAttributes133 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccore_GroupOfAttributes131"):
                opp_val = getattr(old_value, "ccore_GroupOfAttributes131", None)
                if opp_val == self:
                    setattr(old_value, "ccore_GroupOfAttributes131", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccore_GroupOfAttributes131"):
                opp_val = getattr(value, "ccore_GroupOfAttributes131", None)
                setattr(value, "ccore_GroupOfAttributes131", self)

    @property
    def ccore_GroupOfAttributes(self):
        return self.__ccore_GroupOfAttributes

    @ccore_GroupOfAttributes.setter
    def ccore_GroupOfAttributes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_GroupOfAttributes__ccore_GroupOfAttributes", None)
        self.__ccore_GroupOfAttributes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccore_TypeDefinition11"):
                opp_val = getattr(old_value, "ccore_TypeDefinition11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccore_TypeDefinition11"):
                opp_val = getattr(value, "ccore_TypeDefinition11", None)
                if opp_val is None:
                    setattr(value, "ccore_TypeDefinition11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ccore_GroupOfAttributes131(self):
        return self.__ccore_GroupOfAttributes131

    @ccore_GroupOfAttributes131.setter
    def ccore_GroupOfAttributes131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_GroupOfAttributes__ccore_GroupOfAttributes131", None)
        self.__ccore_GroupOfAttributes131 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccore_GroupOfAttributes133"):
                opp_val = getattr(old_value, "ccore_GroupOfAttributes133", None)
                if opp_val == self:
                    setattr(old_value, "ccore_GroupOfAttributes133", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccore_GroupOfAttributes133"):
                opp_val = getattr(value, "ccore_GroupOfAttributes133", None)
                setattr(value, "ccore_GroupOfAttributes133", self)

    @property
    def ccore_GroupOfAttributes129(self):
        return self.__ccore_GroupOfAttributes129

    @ccore_GroupOfAttributes129.setter
    def ccore_GroupOfAttributes129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_GroupOfAttributes__ccore_GroupOfAttributes129", None)
        self.__ccore_GroupOfAttributes129 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ccore_Attribute130"):
                    opp_val = getattr(item, "ccore_Attribute130", None)
                    
                    if opp_val == self:
                        setattr(item, "ccore_Attribute130", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ccore_Attribute130"):
                    opp_val = getattr(item, "ccore_Attribute130", None)
                    
                    setattr(item, "ccore_Attribute130", self)
                    

class ccore_UIValidator:

    pass
class ccore_Page:

    def __init__(self, title: str, description: str, label: str, idRuntime: str, ccore_Page: "ccore_TypeDefinition" = None, ccore_Page9: "ccore_TypeDefinition" = None, ccore_Page121: set["ccore_Attribute"] = None, ccore_Page125: "ccore_Page" = None, ccore_Page123: set["ccore_Page"] = None):
        self.title = title
        self.description = description
        self.label = label
        self.idRuntime = idRuntime
        self.ccore_Page = ccore_Page
        self.ccore_Page9 = ccore_Page9
        self.ccore_Page121 = ccore_Page121 if ccore_Page121 is not None else set()
        self.ccore_Page125 = ccore_Page125
        self.ccore_Page123 = ccore_Page123 if ccore_Page123 is not None else set()
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def idRuntime(self) -> str:
        return self.__idRuntime

    @idRuntime.setter
    def idRuntime(self, idRuntime: str):
        self.__idRuntime = idRuntime

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def ccore_Page(self):
        return self.__ccore_Page

    @ccore_Page.setter
    def ccore_Page(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_Page__ccore_Page", None)
        self.__ccore_Page = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccore_TypeDefinition4"):
                opp_val = getattr(old_value, "ccore_TypeDefinition4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccore_TypeDefinition4"):
                opp_val = getattr(value, "ccore_TypeDefinition4", None)
                if opp_val is None:
                    setattr(value, "ccore_TypeDefinition4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ccore_Page121(self):
        return self.__ccore_Page121

    @ccore_Page121.setter
    def ccore_Page121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_Page__ccore_Page121", None)
        self.__ccore_Page121 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ccore_Attribute122"):
                    opp_val = getattr(item, "ccore_Attribute122", None)
                    
                    if opp_val == self:
                        setattr(item, "ccore_Attribute122", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ccore_Attribute122"):
                    opp_val = getattr(item, "ccore_Attribute122", None)
                    
                    setattr(item, "ccore_Attribute122", self)
                    

    @property
    def ccore_Page9(self):
        return self.__ccore_Page9

    @ccore_Page9.setter
    def ccore_Page9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_Page__ccore_Page9", None)
        self.__ccore_Page9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccore_TypeDefinition8"):
                opp_val = getattr(old_value, "ccore_TypeDefinition8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccore_TypeDefinition8"):
                opp_val = getattr(value, "ccore_TypeDefinition8", None)
                if opp_val is None:
                    setattr(value, "ccore_TypeDefinition8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ccore_Page125(self):
        return self.__ccore_Page125

    @ccore_Page125.setter
    def ccore_Page125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_Page__ccore_Page125", None)
        self.__ccore_Page125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccore_Page123"):
                opp_val = getattr(old_value, "ccore_Page123", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccore_Page123"):
                opp_val = getattr(value, "ccore_Page123", None)
                if opp_val is None:
                    setattr(value, "ccore_Page123", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ccore_Page123(self):
        return self.__ccore_Page123

    @ccore_Page123.setter
    def ccore_Page123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_Page__ccore_Page123", None)
        self.__ccore_Page123 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ccore_Page125"):
                    opp_val = getattr(item, "ccore_Page125", None)
                    
                    if opp_val == self:
                        setattr(item, "ccore_Page125", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ccore_Page125"):
                    opp_val = getattr(item, "ccore_Page125", None)
                    
                    setattr(item, "ccore_Page125", self)
                    

class EClass:

    pass
class Item:

    pass
class ccore_KeyDefinition(Item):

    pass
class ccore_Cadse(Item, EPackage):

    def __init__(self, itemRepoURL: str, idDefinition: str, description: str, defaultContentRepoURL: str, executed: bool, itemRepoLogin: str, itemRepoPasswd: str, ccore_Cadse40: set["ccore_ItemType"] = None, ccore_Cadse43: set["ccore_KeyDefinition"] = None, ccore_Cadse: "ccore_Cadse" = None, ccore_Cadse37: set["ccore_Cadse"] = None, ccore_Cadse46: set["ccore_ExtentedType"] = None, ccore_Cadse49: "ccore_EPackage" = None, ccore_Cadse51: set["ccore_BindingDesc"] = None, ccore_Cadse53: set["ccore_Item"] = None, ccore_Cadse66: "ccore_Item" = None):
        self.itemRepoURL = itemRepoURL
        self.idDefinition = idDefinition
        self.description = description
        self.defaultContentRepoURL = defaultContentRepoURL
        self.executed = executed
        self.itemRepoLogin = itemRepoLogin
        self.itemRepoPasswd = itemRepoPasswd
        self.ccore_Cadse40 = ccore_Cadse40 if ccore_Cadse40 is not None else set()
        self.ccore_Cadse43 = ccore_Cadse43 if ccore_Cadse43 is not None else set()
        self.ccore_Cadse = ccore_Cadse
        self.ccore_Cadse37 = ccore_Cadse37 if ccore_Cadse37 is not None else set()
        self.ccore_Cadse46 = ccore_Cadse46 if ccore_Cadse46 is not None else set()
        self.ccore_Cadse49 = ccore_Cadse49
        self.ccore_Cadse51 = ccore_Cadse51 if ccore_Cadse51 is not None else set()
        self.ccore_Cadse53 = ccore_Cadse53 if ccore_Cadse53 is not None else set()
        self.ccore_Cadse66 = ccore_Cadse66
        
    @property
    def itemRepoURL(self) -> str:
        return self.__itemRepoURL

    @itemRepoURL.setter
    def itemRepoURL(self, itemRepoURL: str):
        self.__itemRepoURL = itemRepoURL

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def itemRepoPasswd(self) -> str:
        return self.__itemRepoPasswd

    @itemRepoPasswd.setter
    def itemRepoPasswd(self, itemRepoPasswd: str):
        self.__itemRepoPasswd = itemRepoPasswd

    @property
    def executed(self) -> bool:
        return self.__executed

    @executed.setter
    def executed(self, executed: bool):
        self.__executed = executed

    @property
    def itemRepoLogin(self) -> str:
        return self.__itemRepoLogin

    @itemRepoLogin.setter
    def itemRepoLogin(self, itemRepoLogin: str):
        self.__itemRepoLogin = itemRepoLogin

    @property
    def defaultContentRepoURL(self) -> str:
        return self.__defaultContentRepoURL

    @defaultContentRepoURL.setter
    def defaultContentRepoURL(self, defaultContentRepoURL: str):
        self.__defaultContentRepoURL = defaultContentRepoURL

    @property
    def idDefinition(self) -> str:
        return self.__idDefinition

    @idDefinition.setter
    def idDefinition(self, idDefinition: str):
        self.__idDefinition = idDefinition

    @property
    def ccore_Cadse49(self):
        return self.__ccore_Cadse49

    @ccore_Cadse49.setter
    def ccore_Cadse49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_Cadse__ccore_Cadse49", None)
        self.__ccore_Cadse49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccore_EPackage"):
                opp_val = getattr(old_value, "ccore_EPackage", None)
                if opp_val == self:
                    setattr(old_value, "ccore_EPackage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccore_EPackage"):
                opp_val = getattr(value, "ccore_EPackage", None)
                setattr(value, "ccore_EPackage", self)

    @property
    def ccore_Cadse51(self):
        return self.__ccore_Cadse51

    @ccore_Cadse51.setter
    def ccore_Cadse51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_Cadse__ccore_Cadse51", None)
        self.__ccore_Cadse51 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ccore_BindingDesc"):
                    opp_val = getattr(item, "ccore_BindingDesc", None)
                    
                    if opp_val == self:
                        setattr(item, "ccore_BindingDesc", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ccore_BindingDesc"):
                    opp_val = getattr(item, "ccore_BindingDesc", None)
                    
                    setattr(item, "ccore_BindingDesc", self)
                    

    @property
    def ccore_Cadse(self):
        return self.__ccore_Cadse

    @ccore_Cadse.setter
    def ccore_Cadse(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_Cadse__ccore_Cadse", None)
        self.__ccore_Cadse = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccore_Cadse37"):
                opp_val = getattr(old_value, "ccore_Cadse37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccore_Cadse37"):
                opp_val = getattr(value, "ccore_Cadse37", None)
                if opp_val is None:
                    setattr(value, "ccore_Cadse37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ccore_Cadse37(self):
        return self.__ccore_Cadse37

    @ccore_Cadse37.setter
    def ccore_Cadse37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_Cadse__ccore_Cadse37", None)
        self.__ccore_Cadse37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ccore_Cadse"):
                    opp_val = getattr(item, "ccore_Cadse", None)
                    
                    if opp_val == self:
                        setattr(item, "ccore_Cadse", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ccore_Cadse"):
                    opp_val = getattr(item, "ccore_Cadse", None)
                    
                    setattr(item, "ccore_Cadse", self)
                    

    @property
    def ccore_Cadse53(self):
        return self.__ccore_Cadse53

    @ccore_Cadse53.setter
    def ccore_Cadse53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_Cadse__ccore_Cadse53", None)
        self.__ccore_Cadse53 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ccore_Item"):
                    opp_val = getattr(item, "ccore_Item", None)
                    
                    if opp_val == self:
                        setattr(item, "ccore_Item", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ccore_Item"):
                    opp_val = getattr(item, "ccore_Item", None)
                    
                    setattr(item, "ccore_Item", self)
                    

    @property
    def ccore_Cadse46(self):
        return self.__ccore_Cadse46

    @ccore_Cadse46.setter
    def ccore_Cadse46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_Cadse__ccore_Cadse46", None)
        self.__ccore_Cadse46 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ccore_ExtentedType47"):
                    opp_val = getattr(item, "ccore_ExtentedType47", None)
                    
                    if opp_val == self:
                        setattr(item, "ccore_ExtentedType47", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ccore_ExtentedType47"):
                    opp_val = getattr(item, "ccore_ExtentedType47", None)
                    
                    setattr(item, "ccore_ExtentedType47", self)
                    

    @property
    def ccore_Cadse43(self):
        return self.__ccore_Cadse43

    @ccore_Cadse43.setter
    def ccore_Cadse43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_Cadse__ccore_Cadse43", None)
        self.__ccore_Cadse43 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ccore_KeyDefinition44"):
                    opp_val = getattr(item, "ccore_KeyDefinition44", None)
                    
                    if opp_val == self:
                        setattr(item, "ccore_KeyDefinition44", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ccore_KeyDefinition44"):
                    opp_val = getattr(item, "ccore_KeyDefinition44", None)
                    
                    setattr(item, "ccore_KeyDefinition44", self)
                    

    @property
    def ccore_Cadse40(self):
        return self.__ccore_Cadse40

    @ccore_Cadse40.setter
    def ccore_Cadse40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_Cadse__ccore_Cadse40", None)
        self.__ccore_Cadse40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ccore_ItemType41"):
                    opp_val = getattr(item, "ccore_ItemType41", None)
                    
                    if opp_val == self:
                        setattr(item, "ccore_ItemType41", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ccore_ItemType41"):
                    opp_val = getattr(item, "ccore_ItemType41", None)
                    
                    setattr(item, "ccore_ItemType41", self)
                    

    @property
    def ccore_Cadse66(self):
        return self.__ccore_Cadse66

    @ccore_Cadse66.setter
    def ccore_Cadse66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_Cadse__ccore_Cadse66", None)
        self.__ccore_Cadse66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccore_Item65"):
                opp_val = getattr(old_value, "ccore_Item65", None)
                if opp_val == self:
                    setattr(old_value, "ccore_Item65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccore_Item65"):
                opp_val = getattr(value, "ccore_Item65", None)
                setattr(value, "ccore_Item65", self)

class ccore_Field(Item):

    def __init__(self, label: str, position: str, editable: bool, ccore_Field: "ccore_TypeDefinition" = None, ccore_Field112: "ccore_Attribute" = None, ccore_Field115: "ccore_InteractionController" = None, ccore_Field117: "ccore_ModelController" = None, ccore_Field119: "ccore_Display" = None):
        self.label = label
        self.position = position
        self.editable = editable
        self.ccore_Field = ccore_Field
        self.ccore_Field112 = ccore_Field112
        self.ccore_Field115 = ccore_Field115
        self.ccore_Field117 = ccore_Field117
        self.ccore_Field119 = ccore_Field119
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def editable(self) -> bool:
        return self.__editable

    @editable.setter
    def editable(self, editable: bool):
        self.__editable = editable

    @property
    def position(self) -> str:
        return self.__position

    @position.setter
    def position(self, position: str):
        self.__position = position

    @property
    def ccore_Field(self):
        return self.__ccore_Field

    @ccore_Field.setter
    def ccore_Field(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_Field__ccore_Field", None)
        self.__ccore_Field = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccore_TypeDefinition2"):
                opp_val = getattr(old_value, "ccore_TypeDefinition2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccore_TypeDefinition2"):
                opp_val = getattr(value, "ccore_TypeDefinition2", None)
                if opp_val is None:
                    setattr(value, "ccore_TypeDefinition2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ccore_Field112(self):
        return self.__ccore_Field112

    @ccore_Field112.setter
    def ccore_Field112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_Field__ccore_Field112", None)
        self.__ccore_Field112 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccore_Attribute113"):
                opp_val = getattr(old_value, "ccore_Attribute113", None)
                if opp_val == self:
                    setattr(old_value, "ccore_Attribute113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccore_Attribute113"):
                opp_val = getattr(value, "ccore_Attribute113", None)
                setattr(value, "ccore_Attribute113", self)

    @property
    def ccore_Field115(self):
        return self.__ccore_Field115

    @ccore_Field115.setter
    def ccore_Field115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_Field__ccore_Field115", None)
        self.__ccore_Field115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccore_InteractionController"):
                opp_val = getattr(old_value, "ccore_InteractionController", None)
                if opp_val == self:
                    setattr(old_value, "ccore_InteractionController", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccore_InteractionController"):
                opp_val = getattr(value, "ccore_InteractionController", None)
                setattr(value, "ccore_InteractionController", self)

    @property
    def ccore_Field119(self):
        return self.__ccore_Field119

    @ccore_Field119.setter
    def ccore_Field119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_Field__ccore_Field119", None)
        self.__ccore_Field119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccore_Display"):
                opp_val = getattr(old_value, "ccore_Display", None)
                if opp_val == self:
                    setattr(old_value, "ccore_Display", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccore_Display"):
                opp_val = getattr(value, "ccore_Display", None)
                setattr(value, "ccore_Display", self)

    @property
    def ccore_Field117(self):
        return self.__ccore_Field117

    @ccore_Field117.setter
    def ccore_Field117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_Field__ccore_Field117", None)
        self.__ccore_Field117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccore_ModelController"):
                opp_val = getattr(old_value, "ccore_ModelController", None)
                if opp_val == self:
                    setattr(old_value, "ccore_ModelController", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccore_ModelController"):
                opp_val = getattr(value, "ccore_ModelController", None)
                setattr(value, "ccore_ModelController", self)

class ccore_Attribute(Item, EAttribute):

    def __init__(self, isList: bool, require: bool, cannotBeUndefined: bool, natif: bool, _final: bool, mustBeInitialized: bool, tWRevSpecific: bool, tWEvol: str, tWUpdateKind: str, tWCommitKind: str, devGenerated: bool, idRuntime: str, hiddenInComputedPages: bool, ccore_Attribute: "ccore_TypeDefinition" = None, ccore_Attribute62: "ccore_Item" = None, ccore_Attribute72: set["ccore_WCListener"] = None, ccore_Attribute98: "ccore_UIValidator" = None, ccore_Attribute113: "ccore_Field" = None, ccore_Attribute110: "ccore_WCListener" = None, ccore_Attribute122: "ccore_Page" = None, ccore_Attribute130: "ccore_GroupOfAttributes" = None):
        self.isList = isList
        self.require = require
        self.cannotBeUndefined = cannotBeUndefined
        self.natif = natif
        self._final = _final
        self.mustBeInitialized = mustBeInitialized
        self.tWRevSpecific = tWRevSpecific
        self.tWEvol = tWEvol
        self.tWUpdateKind = tWUpdateKind
        self.tWCommitKind = tWCommitKind
        self.devGenerated = devGenerated
        self.idRuntime = idRuntime
        self.hiddenInComputedPages = hiddenInComputedPages
        self.ccore_Attribute = ccore_Attribute
        self.ccore_Attribute62 = ccore_Attribute62
        self.ccore_Attribute72 = ccore_Attribute72 if ccore_Attribute72 is not None else set()
        self.ccore_Attribute98 = ccore_Attribute98
        self.ccore_Attribute113 = ccore_Attribute113
        self.ccore_Attribute110 = ccore_Attribute110
        self.ccore_Attribute122 = ccore_Attribute122
        self.ccore_Attribute130 = ccore_Attribute130
        
    @property
    def cannotBeUndefined(self) -> bool:
        return self.__cannotBeUndefined

    @cannotBeUndefined.setter
    def cannotBeUndefined(self, cannotBeUndefined: bool):
        self.__cannotBeUndefined = cannotBeUndefined

    @property
    def tWEvol(self) -> str:
        return self.__tWEvol

    @tWEvol.setter
    def tWEvol(self, tWEvol: str):
        self.__tWEvol = tWEvol

    @property
    def _final(self) -> bool:
        return self.___final

    @_final.setter
    def _final(self, _final: bool):
        self.___final = _final

    @property
    def tWUpdateKind(self) -> str:
        return self.__tWUpdateKind

    @tWUpdateKind.setter
    def tWUpdateKind(self, tWUpdateKind: str):
        self.__tWUpdateKind = tWUpdateKind

    @property
    def devGenerated(self) -> bool:
        return self.__devGenerated

    @devGenerated.setter
    def devGenerated(self, devGenerated: bool):
        self.__devGenerated = devGenerated

    @property
    def idRuntime(self) -> str:
        return self.__idRuntime

    @idRuntime.setter
    def idRuntime(self, idRuntime: str):
        self.__idRuntime = idRuntime

    @property
    def mustBeInitialized(self) -> bool:
        return self.__mustBeInitialized

    @mustBeInitialized.setter
    def mustBeInitialized(self, mustBeInitialized: bool):
        self.__mustBeInitialized = mustBeInitialized

    @property
    def require(self) -> bool:
        return self.__require

    @require.setter
    def require(self, require: bool):
        self.__require = require

    @property
    def natif(self) -> bool:
        return self.__natif

    @natif.setter
    def natif(self, natif: bool):
        self.__natif = natif

    @property
    def tWRevSpecific(self) -> bool:
        return self.__tWRevSpecific

    @tWRevSpecific.setter
    def tWRevSpecific(self, tWRevSpecific: bool):
        self.__tWRevSpecific = tWRevSpecific

    @property
    def hiddenInComputedPages(self) -> bool:
        return self.__hiddenInComputedPages

    @hiddenInComputedPages.setter
    def hiddenInComputedPages(self, hiddenInComputedPages: bool):
        self.__hiddenInComputedPages = hiddenInComputedPages

    @property
    def isList(self) -> bool:
        return self.__isList

    @isList.setter
    def isList(self, isList: bool):
        self.__isList = isList

    @property
    def tWCommitKind(self) -> str:
        return self.__tWCommitKind

    @tWCommitKind.setter
    def tWCommitKind(self, tWCommitKind: str):
        self.__tWCommitKind = tWCommitKind

    @property
    def ccore_Attribute(self):
        return self.__ccore_Attribute

    @ccore_Attribute.setter
    def ccore_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_Attribute__ccore_Attribute", None)
        self.__ccore_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccore_TypeDefinition"):
                opp_val = getattr(old_value, "ccore_TypeDefinition", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccore_TypeDefinition"):
                opp_val = getattr(value, "ccore_TypeDefinition", None)
                if opp_val is None:
                    setattr(value, "ccore_TypeDefinition", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ccore_Attribute98(self):
        return self.__ccore_Attribute98

    @ccore_Attribute98.setter
    def ccore_Attribute98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_Attribute__ccore_Attribute98", None)
        self.__ccore_Attribute98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccore_UIValidator97"):
                opp_val = getattr(old_value, "ccore_UIValidator97", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccore_UIValidator97"):
                opp_val = getattr(value, "ccore_UIValidator97", None)
                if opp_val is None:
                    setattr(value, "ccore_UIValidator97", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ccore_Attribute130(self):
        return self.__ccore_Attribute130

    @ccore_Attribute130.setter
    def ccore_Attribute130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_Attribute__ccore_Attribute130", None)
        self.__ccore_Attribute130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccore_GroupOfAttributes129"):
                opp_val = getattr(old_value, "ccore_GroupOfAttributes129", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccore_GroupOfAttributes129"):
                opp_val = getattr(value, "ccore_GroupOfAttributes129", None)
                if opp_val is None:
                    setattr(value, "ccore_GroupOfAttributes129", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ccore_Attribute113(self):
        return self.__ccore_Attribute113

    @ccore_Attribute113.setter
    def ccore_Attribute113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_Attribute__ccore_Attribute113", None)
        self.__ccore_Attribute113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccore_Field112"):
                opp_val = getattr(old_value, "ccore_Field112", None)
                if opp_val == self:
                    setattr(old_value, "ccore_Field112", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccore_Field112"):
                opp_val = getattr(value, "ccore_Field112", None)
                setattr(value, "ccore_Field112", self)

    @property
    def ccore_Attribute110(self):
        return self.__ccore_Attribute110

    @ccore_Attribute110.setter
    def ccore_Attribute110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_Attribute__ccore_Attribute110", None)
        self.__ccore_Attribute110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccore_WCListener109"):
                opp_val = getattr(old_value, "ccore_WCListener109", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccore_WCListener109"):
                opp_val = getattr(value, "ccore_WCListener109", None)
                if opp_val is None:
                    setattr(value, "ccore_WCListener109", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ccore_Attribute72(self):
        return self.__ccore_Attribute72

    @ccore_Attribute72.setter
    def ccore_Attribute72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_Attribute__ccore_Attribute72", None)
        self.__ccore_Attribute72 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ccore_WCListener73"):
                    opp_val = getattr(item, "ccore_WCListener73", None)
                    
                    if opp_val == self:
                        setattr(item, "ccore_WCListener73", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ccore_WCListener73"):
                    opp_val = getattr(item, "ccore_WCListener73", None)
                    
                    setattr(item, "ccore_WCListener73", self)
                    

    @property
    def ccore_Attribute122(self):
        return self.__ccore_Attribute122

    @ccore_Attribute122.setter
    def ccore_Attribute122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_Attribute__ccore_Attribute122", None)
        self.__ccore_Attribute122 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccore_Page121"):
                opp_val = getattr(old_value, "ccore_Page121", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccore_Page121"):
                opp_val = getattr(value, "ccore_Page121", None)
                if opp_val is None:
                    setattr(value, "ccore_Page121", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ccore_Attribute62(self):
        return self.__ccore_Attribute62

    @ccore_Attribute62.setter
    def ccore_Attribute62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_Attribute__ccore_Attribute62", None)
        self.__ccore_Attribute62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccore_Item61"):
                opp_val = getattr(old_value, "ccore_Item61", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccore_Item61"):
                opp_val = getattr(value, "ccore_Item61", None)
                if opp_val is None:
                    setattr(value, "ccore_Item61", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ccore_RuntimeItem(Item):

    def __init__(self, className: str, extendsClass: bool):
        self.className = className
        self.extendsClass = extendsClass
        
    @property
    def extendsClass(self) -> bool:
        return self.__extendsClass

    @extendsClass.setter
    def extendsClass(self, extendsClass: bool):
        self.__extendsClass = extendsClass

    @property
    def className(self) -> str:
        return self.__className

    @className.setter
    def className(self, className: str):
        self.__className = className

class ccore_TypeDefinition(Item, EClass):

    def __init__(self, idRuntime: str, ccore_TypeDefinition: set["ccore_Attribute"] = None, ccore_TypeDefinition2: set["ccore_Field"] = None, ccore_TypeDefinition4: set["ccore_Page"] = None, ccore_TypeDefinition6: set["ccore_UIValidator"] = None, ccore_TypeDefinition8: set["ccore_Page"] = None, ccore_TypeDefinition11: set["ccore_GroupOfAttributes"] = None, ccore_TypeDefinition13: "ccore_EClass" = None, ccore_TypeDefinition84: "ccore_ViewDescription" = None, ccore_TypeDefinition101: "ccore_LinkType" = None, ccore_TypeDefinition104: "ccore_LinkType" = None):
        self.idRuntime = idRuntime
        self.ccore_TypeDefinition = ccore_TypeDefinition if ccore_TypeDefinition is not None else set()
        self.ccore_TypeDefinition2 = ccore_TypeDefinition2 if ccore_TypeDefinition2 is not None else set()
        self.ccore_TypeDefinition4 = ccore_TypeDefinition4 if ccore_TypeDefinition4 is not None else set()
        self.ccore_TypeDefinition6 = ccore_TypeDefinition6 if ccore_TypeDefinition6 is not None else set()
        self.ccore_TypeDefinition8 = ccore_TypeDefinition8 if ccore_TypeDefinition8 is not None else set()
        self.ccore_TypeDefinition11 = ccore_TypeDefinition11 if ccore_TypeDefinition11 is not None else set()
        self.ccore_TypeDefinition13 = ccore_TypeDefinition13
        self.ccore_TypeDefinition84 = ccore_TypeDefinition84
        self.ccore_TypeDefinition101 = ccore_TypeDefinition101
        self.ccore_TypeDefinition104 = ccore_TypeDefinition104
        
    @property
    def idRuntime(self) -> str:
        return self.__idRuntime

    @idRuntime.setter
    def idRuntime(self, idRuntime: str):
        self.__idRuntime = idRuntime

    @property
    def ccore_TypeDefinition4(self):
        return self.__ccore_TypeDefinition4

    @ccore_TypeDefinition4.setter
    def ccore_TypeDefinition4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_TypeDefinition__ccore_TypeDefinition4", None)
        self.__ccore_TypeDefinition4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ccore_Page"):
                    opp_val = getattr(item, "ccore_Page", None)
                    
                    if opp_val == self:
                        setattr(item, "ccore_Page", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ccore_Page"):
                    opp_val = getattr(item, "ccore_Page", None)
                    
                    setattr(item, "ccore_Page", self)
                    

    @property
    def ccore_TypeDefinition104(self):
        return self.__ccore_TypeDefinition104

    @ccore_TypeDefinition104.setter
    def ccore_TypeDefinition104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_TypeDefinition__ccore_TypeDefinition104", None)
        self.__ccore_TypeDefinition104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccore_LinkType103"):
                opp_val = getattr(old_value, "ccore_LinkType103", None)
                if opp_val == self:
                    setattr(old_value, "ccore_LinkType103", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccore_LinkType103"):
                opp_val = getattr(value, "ccore_LinkType103", None)
                setattr(value, "ccore_LinkType103", self)

    @property
    def ccore_TypeDefinition6(self):
        return self.__ccore_TypeDefinition6

    @ccore_TypeDefinition6.setter
    def ccore_TypeDefinition6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_TypeDefinition__ccore_TypeDefinition6", None)
        self.__ccore_TypeDefinition6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ccore_UIValidator"):
                    opp_val = getattr(item, "ccore_UIValidator", None)
                    
                    if opp_val == self:
                        setattr(item, "ccore_UIValidator", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ccore_UIValidator"):
                    opp_val = getattr(item, "ccore_UIValidator", None)
                    
                    setattr(item, "ccore_UIValidator", self)
                    

    @property
    def ccore_TypeDefinition8(self):
        return self.__ccore_TypeDefinition8

    @ccore_TypeDefinition8.setter
    def ccore_TypeDefinition8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_TypeDefinition__ccore_TypeDefinition8", None)
        self.__ccore_TypeDefinition8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ccore_Page9"):
                    opp_val = getattr(item, "ccore_Page9", None)
                    
                    if opp_val == self:
                        setattr(item, "ccore_Page9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ccore_Page9"):
                    opp_val = getattr(item, "ccore_Page9", None)
                    
                    setattr(item, "ccore_Page9", self)
                    

    @property
    def ccore_TypeDefinition2(self):
        return self.__ccore_TypeDefinition2

    @ccore_TypeDefinition2.setter
    def ccore_TypeDefinition2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_TypeDefinition__ccore_TypeDefinition2", None)
        self.__ccore_TypeDefinition2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ccore_Field"):
                    opp_val = getattr(item, "ccore_Field", None)
                    
                    if opp_val == self:
                        setattr(item, "ccore_Field", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ccore_Field"):
                    opp_val = getattr(item, "ccore_Field", None)
                    
                    setattr(item, "ccore_Field", self)
                    

    @property
    def ccore_TypeDefinition84(self):
        return self.__ccore_TypeDefinition84

    @ccore_TypeDefinition84.setter
    def ccore_TypeDefinition84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_TypeDefinition__ccore_TypeDefinition84", None)
        self.__ccore_TypeDefinition84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccore_ViewDescription"):
                opp_val = getattr(old_value, "ccore_ViewDescription", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccore_ViewDescription"):
                opp_val = getattr(value, "ccore_ViewDescription", None)
                if opp_val is None:
                    setattr(value, "ccore_ViewDescription", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ccore_TypeDefinition101(self):
        return self.__ccore_TypeDefinition101

    @ccore_TypeDefinition101.setter
    def ccore_TypeDefinition101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_TypeDefinition__ccore_TypeDefinition101", None)
        self.__ccore_TypeDefinition101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccore_LinkType"):
                opp_val = getattr(old_value, "ccore_LinkType", None)
                if opp_val == self:
                    setattr(old_value, "ccore_LinkType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccore_LinkType"):
                opp_val = getattr(value, "ccore_LinkType", None)
                setattr(value, "ccore_LinkType", self)

    @property
    def ccore_TypeDefinition11(self):
        return self.__ccore_TypeDefinition11

    @ccore_TypeDefinition11.setter
    def ccore_TypeDefinition11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_TypeDefinition__ccore_TypeDefinition11", None)
        self.__ccore_TypeDefinition11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ccore_GroupOfAttributes"):
                    opp_val = getattr(item, "ccore_GroupOfAttributes", None)
                    
                    if opp_val == self:
                        setattr(item, "ccore_GroupOfAttributes", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ccore_GroupOfAttributes"):
                    opp_val = getattr(item, "ccore_GroupOfAttributes", None)
                    
                    setattr(item, "ccore_GroupOfAttributes", self)
                    

    @property
    def ccore_TypeDefinition(self):
        return self.__ccore_TypeDefinition

    @ccore_TypeDefinition.setter
    def ccore_TypeDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_TypeDefinition__ccore_TypeDefinition", None)
        self.__ccore_TypeDefinition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ccore_Attribute"):
                    opp_val = getattr(item, "ccore_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "ccore_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ccore_Attribute"):
                    opp_val = getattr(item, "ccore_Attribute", None)
                    
                    setattr(item, "ccore_Attribute", self)
                    

    @property
    def ccore_TypeDefinition13(self):
        return self.__ccore_TypeDefinition13

    @ccore_TypeDefinition13.setter
    def ccore_TypeDefinition13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ccore_TypeDefinition__ccore_TypeDefinition13", None)
        self.__ccore_TypeDefinition13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ccore_EClass"):
                opp_val = getattr(old_value, "ccore_EClass", None)
                if opp_val == self:
                    setattr(old_value, "ccore_EClass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ccore_EClass"):
                opp_val = getattr(value, "ccore_EClass", None)
                setattr(value, "ccore_EClass", self)

class ccore_WCListener(ABC):

    pass