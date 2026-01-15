from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class AggregationKind(Enum):
    none = "none"
    aggregate = "aggregate"
    composite = "composite"
class PseudostateKind(Enum):
    choice = "choice"
    deepHistory = "deepHistory"
    fork = "fork"
    initial = "initial"
    join = "join"
    junction = "junction"
    shallowHistory = "shallowHistory"
class ScopeKind(Enum):
    instance = "instance"
    classifier = "classifier"
class OrderingKind(Enum):
    unordered = "unordered"
    ordered = "ordered"
class ParameterDirectionKind(Enum):
    in = "in"
    inout = "inout"
    out = "out"
    return = "return"
class CallConcurrencyKind(Enum):
    sequential = "sequential"
    guarded = "guarded"
    concurrent = "concurrent"
class ChangeableKind(Enum):
    changeable = "changeable"
    frozen = "frozen"
    addOnly = "addOnly"
class VisibilityKind(Enum):
    public = "public"
    protected = "protected"
    private = "private"
    package = "package"


############################################
# Definition of Classes
############################################

class Binding:

    pass
class foundation_core_TemplateArgument:

    pass
class TypeExpression:

    pass
class Enumeration:

    pass
class TagDefinition:

    pass
class foundation_core_ElementResidence:

    def __init__(self, visibility: str, Component156: "Component" = None, ModelElement153: "ModelElement" = None):
        self.visibility = visibility
        self.Component156 = Component156
        self.ModelElement153 = ModelElement153
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def ModelElement153(self):
        return self.__ModelElement153

    @ModelElement153.setter
    def ModelElement153(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_ElementResidence__ModelElement153", None)
        self.__ModelElement153 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core154"):
                opp_val = getattr(old_value, "core154", None)
                if opp_val == self:
                    setattr(old_value, "core154", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core154"):
                opp_val = getattr(value, "core154", None)
                setattr(value, "core154", self)

    @property
    def Component156(self):
        return self.__Component156

    @Component156.setter
    def Component156(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_ElementResidence__Component156", None)
        self.__Component156 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core157"):
                opp_val = getattr(old_value, "core157", None)
                if opp_val == self:
                    setattr(old_value, "core157", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core157"):
                opp_val = getattr(value, "core157", None)
                setattr(value, "core157", self)

class EnumerationLiteral:

    pass
class DataType:

    pass
class foundation_core_ProgrammingLanguageDataType(DataType):

    pass
class foundation_core_Enumeration(DataType):

    pass
class foundation_core_Primitive(DataType):

    pass
class foundation_core_TemplateParameter:

    pass
class Artifact:

    pass
class Component:

    pass
class Node:

    pass
class TemplateArgument:

    pass
class MappingExpression:

    pass
class ProcedureExpression:

    pass
class core_Association:

    pass
class core_Class:

    pass
class foundation_core_AssociationClass(core_Association, core_Class):

    pass
class GeneralizableElement:

    pass
class foundation_core_Stereotype(GeneralizableElement):

    def __init__(self, icon: str, baseClass: str, TagDefinition: set["TagDefinition"] = None, ModelElement173: set["ModelElement"] = None, Constraint176: set["Constraint"] = None, core118: "foundation_core_Generalization", core115: "foundation_core_Generalization"):
        self.icon = icon
        self.baseClass = baseClass
        self.TagDefinition = TagDefinition if TagDefinition is not None else set()
        self.ModelElement173 = ModelElement173 if ModelElement173 is not None else set()
        self.Constraint176 = Constraint176 if Constraint176 is not None else set()
        
    @property
    def icon(self) -> str:
        return self.__icon

    @icon.setter
    def icon(self, icon: str):
        self.__icon = icon

    @property
    def baseClass(self) -> str:
        return self.__baseClass

    @baseClass.setter
    def baseClass(self, baseClass: str):
        self.__baseClass = baseClass

    @property
    def TagDefinition(self):
        return self.__TagDefinition

    @TagDefinition.setter
    def TagDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_Stereotype__TagDefinition", None)
        self.__TagDefinition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core171"):
                    opp_val = getattr(item, "core171", None)
                    
                    if opp_val == self:
                        setattr(item, "core171", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core171"):
                    opp_val = getattr(item, "core171", None)
                    
                    setattr(item, "core171", self)
                    

    @property
    def Constraint176(self):
        return self.__Constraint176

    @Constraint176.setter
    def Constraint176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_Stereotype__Constraint176", None)
        self.__Constraint176 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core177"):
                    opp_val = getattr(item, "core177", None)
                    
                    if opp_val == self:
                        setattr(item, "core177", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core177"):
                    opp_val = getattr(item, "core177", None)
                    
                    setattr(item, "core177", self)
                    

    @property
    def ModelElement173(self):
        return self.__ModelElement173

    @ModelElement173.setter
    def ModelElement173(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_Stereotype__ModelElement173", None)
        self.__ModelElement173 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core174"):
                    opp_val = getattr(item, "core174", None)
                    
                    if opp_val == self:
                        setattr(item, "core174", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core174"):
                    opp_val = getattr(item, "core174", None)
                    
                    setattr(item, "core174", self)
                    

class Relationship:

    pass
class foundation_core_Flow(Relationship):

    pass
class foundation_core_Dependency(Relationship):

    pass
class foundation_core_Generalization(Relationship):

    def __init__(self, discriminator: str, GeneralizableElement: "GeneralizableElement" = None, GeneralizableElement117: "GeneralizableElement" = None, Classifier120: "Classifier" = None):
        self.discriminator = discriminator
        self.GeneralizableElement = GeneralizableElement
        self.GeneralizableElement117 = GeneralizableElement117
        self.Classifier120 = Classifier120
        
    @property
    def discriminator(self) -> str:
        return self.__discriminator

    @discriminator.setter
    def discriminator(self, discriminator: str):
        self.__discriminator = discriminator

    @property
    def GeneralizableElement117(self):
        return self.__GeneralizableElement117

    @GeneralizableElement117.setter
    def GeneralizableElement117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_Generalization__GeneralizableElement117", None)
        self.__GeneralizableElement117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core118"):
                opp_val = getattr(old_value, "core118", None)
                if opp_val == self:
                    setattr(old_value, "core118", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core118"):
                opp_val = getattr(value, "core118", None)
                setattr(value, "core118", self)

    @property
    def GeneralizableElement(self):
        return self.__GeneralizableElement

    @GeneralizableElement.setter
    def GeneralizableElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_Generalization__GeneralizableElement", None)
        self.__GeneralizableElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core115"):
                opp_val = getattr(old_value, "core115", None)
                if opp_val == self:
                    setattr(old_value, "core115", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core115"):
                opp_val = getattr(value, "core115", None)
                setattr(value, "core115", self)

    @property
    def Classifier120(self):
        return self.__Classifier120

    @Classifier120.setter
    def Classifier120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_Generalization__Classifier120", None)
        self.__Classifier120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core121"):
                opp_val = getattr(old_value, "core121", None)
                if opp_val == self:
                    setattr(old_value, "core121", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core121"):
                opp_val = getattr(value, "core121", None)
                setattr(value, "core121", self)

class Operation:

    pass
class Method:

    pass
class BehavioralFeature:

    pass
class foundation_core_Method(BehavioralFeature):

    pass
class foundation_core_Operation(BehavioralFeature):

    def __init__(self, concurrency: str, isRoot: str, isLeaf: str, isAbstract: str, specification: str, CallAction: set["CallAction"] = None, CallEvent: set["CallEvent"] = None, Collaboration102: set["Collaboration"] = None, Method: set["Method"] = None, core107: "foundation_core_Parameter"):
        self.concurrency = concurrency
        self.isRoot = isRoot
        self.isLeaf = isLeaf
        self.isAbstract = isAbstract
        self.specification = specification
        self.CallAction = CallAction if CallAction is not None else set()
        self.CallEvent = CallEvent if CallEvent is not None else set()
        self.Collaboration102 = Collaboration102 if Collaboration102 is not None else set()
        self.Method = Method if Method is not None else set()
        
    @property
    def isRoot(self) -> str:
        return self.__isRoot

    @isRoot.setter
    def isRoot(self, isRoot: str):
        self.__isRoot = isRoot

    @property
    def isLeaf(self) -> str:
        return self.__isLeaf

    @isLeaf.setter
    def isLeaf(self, isLeaf: str):
        self.__isLeaf = isLeaf

    @property
    def specification(self) -> str:
        return self.__specification

    @specification.setter
    def specification(self, specification: str):
        self.__specification = specification

    @property
    def isAbstract(self) -> str:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract

    @property
    def concurrency(self) -> str:
        return self.__concurrency

    @concurrency.setter
    def concurrency(self, concurrency: str):
        self.__concurrency = concurrency

    @property
    def CallEvent(self):
        return self.__CallEvent

    @CallEvent.setter
    def CallEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_Operation__CallEvent", None)
        self.__CallEvent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "behavioral_elements.ecorestate_machines100"):
                    opp_val = getattr(item, "behavioral_elements.ecorestate_machines100", None)
                    
                    if opp_val == self:
                        setattr(item, "behavioral_elements.ecorestate_machines100", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "behavioral_elements.ecorestate_machines100"):
                    opp_val = getattr(item, "behavioral_elements.ecorestate_machines100", None)
                    
                    setattr(item, "behavioral_elements.ecorestate_machines100", self)
                    

    @property
    def Method(self):
        return self.__Method

    @Method.setter
    def Method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_Operation__Method", None)
        self.__Method = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core96"):
                    opp_val = getattr(item, "core96", None)
                    
                    if opp_val == self:
                        setattr(item, "core96", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core96"):
                    opp_val = getattr(item, "core96", None)
                    
                    setattr(item, "core96", self)
                    

    @property
    def Collaboration102(self):
        return self.__Collaboration102

    @Collaboration102.setter
    def Collaboration102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_Operation__Collaboration102", None)
        self.__Collaboration102 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "behavioral_elements.ecorecollaborations103"):
                    opp_val = getattr(item, "behavioral_elements.ecorecollaborations103", None)
                    
                    if opp_val == self:
                        setattr(item, "behavioral_elements.ecorecollaborations103", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "behavioral_elements.ecorecollaborations103"):
                    opp_val = getattr(item, "behavioral_elements.ecorecollaborations103", None)
                    
                    setattr(item, "behavioral_elements.ecorecollaborations103", self)
                    

    @property
    def CallAction(self):
        return self.__CallAction

    @CallAction.setter
    def CallAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_Operation__CallAction", None)
        self.__CallAction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "behavioral_elements.ecorecommon_behavior98"):
                    opp_val = getattr(item, "behavioral_elements.ecorecommon_behavior98", None)
                    
                    if opp_val == self:
                        setattr(item, "behavioral_elements.ecorecommon_behavior98", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "behavioral_elements.ecorecommon_behavior98"):
                    opp_val = getattr(item, "behavioral_elements.ecorecommon_behavior98", None)
                    
                    setattr(item, "behavioral_elements.ecorecommon_behavior98", self)
                    

class CallEvent:

    pass
class CallAction:

    pass
class core_Relationship:

    pass
class Signal:

    pass
class AssociationEndRole:

    pass
class Association:

    pass
class BooleanExpression:

    pass
class Attribute:

    pass
class Classifier:

    pass
class foundation_core_Artifact(Classifier):

    pass
class foundation_core_Component(Classifier):

    pass
class foundation_core_Node(Classifier):

    pass
class foundation_core_DataType(Classifier):

    pass
class foundation_core_Interface(Classifier):

    pass
class foundation_core_Class(Classifier):

    def __init__(self, isActive: str, core61: "foundation_core_StructuralFeature", core56: "foundation_core_Feature", core110: "foundation_core_Parameter", core70: "foundation_core_AssociationEnd", core73: "foundation_core_AssociationEnd", core121: "foundation_core_Generalization"):
        self.isActive = isActive
        
    @property
    def isActive(self) -> str:
        return self.__isActive

    @isActive.setter
    def isActive(self, isActive: str):
        self.__isActive = isActive

class Feature:

    pass
class foundation_core_StructuralFeature(Feature):

    def __init__(self, changeability: str, targetScope: str, ordering: str, foundation_core_StructuralFeature: "Multiplicity" = None, Classifier60: "Classifier" = None, core40: "foundation_core_Classifier"):
        self.changeability = changeability
        self.targetScope = targetScope
        self.ordering = ordering
        self.foundation_core_StructuralFeature = foundation_core_StructuralFeature
        self.Classifier60 = Classifier60
        
    @property
    def changeability(self) -> str:
        return self.__changeability

    @changeability.setter
    def changeability(self, changeability: str):
        self.__changeability = changeability

    @property
    def ordering(self) -> str:
        return self.__ordering

    @ordering.setter
    def ordering(self, ordering: str):
        self.__ordering = ordering

    @property
    def targetScope(self) -> str:
        return self.__targetScope

    @targetScope.setter
    def targetScope(self, targetScope: str):
        self.__targetScope = targetScope

    @property
    def foundation_core_StructuralFeature(self):
        return self.__foundation_core_StructuralFeature

    @foundation_core_StructuralFeature.setter
    def foundation_core_StructuralFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_StructuralFeature__foundation_core_StructuralFeature", None)
        self.__foundation_core_StructuralFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Multiplicity58"):
                opp_val = getattr(old_value, "Multiplicity58", None)
                if opp_val == self:
                    setattr(old_value, "Multiplicity58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Multiplicity58"):
                opp_val = getattr(value, "Multiplicity58", None)
                setattr(value, "Multiplicity58", self)

    @property
    def Classifier60(self):
        return self.__Classifier60

    @Classifier60.setter
    def Classifier60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_StructuralFeature__Classifier60", None)
        self.__Classifier60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core61"):
                opp_val = getattr(old_value, "core61", None)
                if opp_val == self:
                    setattr(old_value, "core61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core61"):
                opp_val = getattr(value, "core61", None)
                setattr(value, "core61", self)

class foundation_core_BehavioralFeature(Feature):

    def __init__(self, isQuery: str, Parameter91: set["Parameter"] = None, Signal: set["Signal"] = None, core40: "foundation_core_Classifier"):
        self.isQuery = isQuery
        self.Parameter91 = Parameter91 if Parameter91 is not None else set()
        self.Signal = Signal if Signal is not None else set()
        
    @property
    def isQuery(self) -> str:
        return self.__isQuery

    @isQuery.setter
    def isQuery(self, isQuery: str):
        self.__isQuery = isQuery

    @property
    def Parameter91(self):
        return self.__Parameter91

    @Parameter91.setter
    def Parameter91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_BehavioralFeature__Parameter91", None)
        self.__Parameter91 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core92"):
                    opp_val = getattr(item, "core92", None)
                    
                    if opp_val == self:
                        setattr(item, "core92", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core92"):
                    opp_val = getattr(item, "core92", None)
                    
                    setattr(item, "core92", self)
                    

    @property
    def Signal(self):
        return self.__Signal

    @Signal.setter
    def Signal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_BehavioralFeature__Signal", None)
        self.__Signal = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "behavioral_elements.ecorecommon_behavior94"):
                    opp_val = getattr(item, "behavioral_elements.ecorecommon_behavior94", None)
                    
                    if opp_val == self:
                        setattr(item, "behavioral_elements.ecorecommon_behavior94", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "behavioral_elements.ecorecommon_behavior94"):
                    opp_val = getattr(item, "behavioral_elements.ecorecommon_behavior94", None)
                    
                    setattr(item, "behavioral_elements.ecorecommon_behavior94", self)
                    

class core_Namespace:

    pass
class core_GeneralizableElement:

    pass
class foundation_core_Association(core_Relationship, core_GeneralizableElement):

    pass
class foundation_core_Classifier(core_Namespace, core_GeneralizableElement):

    pass
class Collaboration:

    pass
class CreateAction:

    pass
class AssociationEnd:

    pass
class Parameter:

    pass
class StructuralFeature:

    pass
class foundation_core_Attribute(StructuralFeature):

    pass
class TaggedValue:

    pass
class Stereotype:

    pass
class TemplateParameter:

    pass
class Generalization:

    pass
class ModelElement:

    pass
class foundation_core_TaggedValue(ModelElement):

    def __init__(self, dataValue: str, TagDefinition190: "TagDefinition" = None, ModelElement193: set["ModelElement"] = None, ModelElement187: "ModelElement" = None, core194: "foundation_core_TaggedValue", ModelElement165: "foundation_core_TemplateParameter", core131: "foundation_core_PresentationElement", core174: "foundation_core_Stereotype", ModelElement202: "foundation_core_TemplateArgument", core77: "foundation_core_Constraint", ModelElement159: "foundation_core_TemplateParameter", core145: "foundation_core_Comment", core162: "foundation_core_TemplateParameter", core127: "foundation_core_Dependency", core124: "foundation_core_Dependency", core148: "foundation_core_Flow", core188: "foundation_core_TaggedValue", core154: "foundation_core_ElementResidence", core38: "foundation_core_Namespace", core151: "foundation_core_Flow"):
        self.dataValue = dataValue
        self.TagDefinition190 = TagDefinition190
        self.ModelElement193 = ModelElement193 if ModelElement193 is not None else set()
        self.ModelElement187 = ModelElement187
        
    @property
    def dataValue(self) -> str:
        return self.__dataValue

    @dataValue.setter
    def dataValue(self, dataValue: str):
        self.__dataValue = dataValue

    @property
    def ModelElement187(self):
        return self.__ModelElement187

    @ModelElement187.setter
    def ModelElement187(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_TaggedValue__ModelElement187", None)
        self.__ModelElement187 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core188"):
                opp_val = getattr(old_value, "core188", None)
                if opp_val == self:
                    setattr(old_value, "core188", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core188"):
                opp_val = getattr(value, "core188", None)
                setattr(value, "core188", self)

    @property
    def TagDefinition190(self):
        return self.__TagDefinition190

    @TagDefinition190.setter
    def TagDefinition190(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_TaggedValue__TagDefinition190", None)
        self.__TagDefinition190 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core191"):
                opp_val = getattr(old_value, "core191", None)
                if opp_val == self:
                    setattr(old_value, "core191", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core191"):
                opp_val = getattr(value, "core191", None)
                setattr(value, "core191", self)

    @property
    def ModelElement193(self):
        return self.__ModelElement193

    @ModelElement193.setter
    def ModelElement193(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_TaggedValue__ModelElement193", None)
        self.__ModelElement193 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core194"):
                    opp_val = getattr(item, "core194", None)
                    
                    if opp_val == self:
                        setattr(item, "core194", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core194"):
                    opp_val = getattr(item, "core194", None)
                    
                    setattr(item, "core194", self)
                    

class foundation_core_Namespace(ModelElement):

    pass
class foundation_core_Constraint(ModelElement):

    pass
class foundation_core_Parameter(ModelElement):

    def __init__(self, kind: str, foundation_core_Parameter: "Expression" = None, BehavioralFeature: "BehavioralFeature" = None, Classifier109: "Classifier" = None, core194: "foundation_core_TaggedValue", ModelElement165: "foundation_core_TemplateParameter", core131: "foundation_core_PresentationElement", core174: "foundation_core_Stereotype", ModelElement202: "foundation_core_TemplateArgument", core77: "foundation_core_Constraint", ModelElement159: "foundation_core_TemplateParameter", core145: "foundation_core_Comment", core162: "foundation_core_TemplateParameter", core127: "foundation_core_Dependency", core124: "foundation_core_Dependency", core148: "foundation_core_Flow", core188: "foundation_core_TaggedValue", core154: "foundation_core_ElementResidence", core38: "foundation_core_Namespace", core151: "foundation_core_Flow"):
        self.kind = kind
        self.foundation_core_Parameter = foundation_core_Parameter
        self.BehavioralFeature = BehavioralFeature
        self.Classifier109 = Classifier109
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def Classifier109(self):
        return self.__Classifier109

    @Classifier109.setter
    def Classifier109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_Parameter__Classifier109", None)
        self.__Classifier109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core110"):
                opp_val = getattr(old_value, "core110", None)
                if opp_val == self:
                    setattr(old_value, "core110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core110"):
                opp_val = getattr(value, "core110", None)
                setattr(value, "core110", self)

    @property
    def BehavioralFeature(self):
        return self.__BehavioralFeature

    @BehavioralFeature.setter
    def BehavioralFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_Parameter__BehavioralFeature", None)
        self.__BehavioralFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core107"):
                opp_val = getattr(old_value, "core107", None)
                if opp_val == self:
                    setattr(old_value, "core107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core107"):
                opp_val = getattr(value, "core107", None)
                setattr(value, "core107", self)

    @property
    def foundation_core_Parameter(self):
        return self.__foundation_core_Parameter

    @foundation_core_Parameter.setter
    def foundation_core_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_Parameter__foundation_core_Parameter", None)
        self.__foundation_core_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression105"):
                opp_val = getattr(old_value, "Expression105", None)
                if opp_val == self:
                    setattr(old_value, "Expression105", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression105"):
                opp_val = getattr(value, "Expression105", None)
                setattr(value, "Expression105", self)

class foundation_core_AssociationEnd(ModelElement):

    def __init__(self, isNavigable: str, ordering: str, aggregation: str, targetScope: str, changeability: str, Attribute: set["Attribute"] = None, Classifier69: "Classifier" = None, Classifier72: set["Classifier"] = None, foundation_core_AssociationEnd: "Multiplicity" = None, Association: "Association" = None, core194: "foundation_core_TaggedValue", ModelElement165: "foundation_core_TemplateParameter", core131: "foundation_core_PresentationElement", core174: "foundation_core_Stereotype", ModelElement202: "foundation_core_TemplateArgument", core77: "foundation_core_Constraint", ModelElement159: "foundation_core_TemplateParameter", core145: "foundation_core_Comment", core162: "foundation_core_TemplateParameter", core127: "foundation_core_Dependency", core124: "foundation_core_Dependency", core148: "foundation_core_Flow", core188: "foundation_core_TaggedValue", core154: "foundation_core_ElementResidence", core38: "foundation_core_Namespace", core151: "foundation_core_Flow"):
        self.isNavigable = isNavigable
        self.ordering = ordering
        self.aggregation = aggregation
        self.targetScope = targetScope
        self.changeability = changeability
        self.Attribute = Attribute if Attribute is not None else set()
        self.Classifier69 = Classifier69
        self.Classifier72 = Classifier72 if Classifier72 is not None else set()
        self.foundation_core_AssociationEnd = foundation_core_AssociationEnd
        self.Association = Association
        
    @property
    def isNavigable(self) -> str:
        return self.__isNavigable

    @isNavigable.setter
    def isNavigable(self, isNavigable: str):
        self.__isNavigable = isNavigable

    @property
    def targetScope(self) -> str:
        return self.__targetScope

    @targetScope.setter
    def targetScope(self, targetScope: str):
        self.__targetScope = targetScope

    @property
    def aggregation(self) -> str:
        return self.__aggregation

    @aggregation.setter
    def aggregation(self, aggregation: str):
        self.__aggregation = aggregation

    @property
    def ordering(self) -> str:
        return self.__ordering

    @ordering.setter
    def ordering(self, ordering: str):
        self.__ordering = ordering

    @property
    def changeability(self) -> str:
        return self.__changeability

    @changeability.setter
    def changeability(self, changeability: str):
        self.__changeability = changeability

    @property
    def Classifier72(self):
        return self.__Classifier72

    @Classifier72.setter
    def Classifier72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_AssociationEnd__Classifier72", None)
        self.__Classifier72 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core73"):
                    opp_val = getattr(item, "core73", None)
                    
                    if opp_val == self:
                        setattr(item, "core73", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core73"):
                    opp_val = getattr(item, "core73", None)
                    
                    setattr(item, "core73", self)
                    

    @property
    def Classifier69(self):
        return self.__Classifier69

    @Classifier69.setter
    def Classifier69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_AssociationEnd__Classifier69", None)
        self.__Classifier69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core70"):
                opp_val = getattr(old_value, "core70", None)
                if opp_val == self:
                    setattr(old_value, "core70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core70"):
                opp_val = getattr(value, "core70", None)
                setattr(value, "core70", self)

    @property
    def foundation_core_AssociationEnd(self):
        return self.__foundation_core_AssociationEnd

    @foundation_core_AssociationEnd.setter
    def foundation_core_AssociationEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_AssociationEnd__foundation_core_AssociationEnd", None)
        self.__foundation_core_AssociationEnd = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Multiplicity63"):
                opp_val = getattr(old_value, "Multiplicity63", None)
                if opp_val == self:
                    setattr(old_value, "Multiplicity63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Multiplicity63"):
                opp_val = getattr(value, "Multiplicity63", None)
                setattr(value, "Multiplicity63", self)

    @property
    def Association(self):
        return self.__Association

    @Association.setter
    def Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_AssociationEnd__Association", None)
        self.__Association = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core65"):
                opp_val = getattr(old_value, "core65", None)
                if opp_val == self:
                    setattr(old_value, "core65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core65"):
                opp_val = getattr(value, "core65", None)
                setattr(value, "core65", self)

    @property
    def Attribute(self):
        return self.__Attribute

    @Attribute.setter
    def Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_AssociationEnd__Attribute", None)
        self.__Attribute = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core67"):
                    opp_val = getattr(item, "core67", None)
                    
                    if opp_val == self:
                        setattr(item, "core67", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core67"):
                    opp_val = getattr(item, "core67", None)
                    
                    setattr(item, "core67", self)
                    

class foundation_core_TagDefinition(ModelElement):

    def __init__(self, tagType: str, foundation_core_TagDefinition: "Multiplicity" = None, Stereotype181: "Stereotype" = None, TaggedValue184: set["TaggedValue"] = None, core194: "foundation_core_TaggedValue", ModelElement165: "foundation_core_TemplateParameter", core131: "foundation_core_PresentationElement", core174: "foundation_core_Stereotype", ModelElement202: "foundation_core_TemplateArgument", core77: "foundation_core_Constraint", ModelElement159: "foundation_core_TemplateParameter", core145: "foundation_core_Comment", core162: "foundation_core_TemplateParameter", core127: "foundation_core_Dependency", core124: "foundation_core_Dependency", core148: "foundation_core_Flow", core188: "foundation_core_TaggedValue", core154: "foundation_core_ElementResidence", core38: "foundation_core_Namespace", core151: "foundation_core_Flow"):
        self.tagType = tagType
        self.foundation_core_TagDefinition = foundation_core_TagDefinition
        self.Stereotype181 = Stereotype181
        self.TaggedValue184 = TaggedValue184 if TaggedValue184 is not None else set()
        
    @property
    def tagType(self) -> str:
        return self.__tagType

    @tagType.setter
    def tagType(self, tagType: str):
        self.__tagType = tagType

    @property
    def TaggedValue184(self):
        return self.__TaggedValue184

    @TaggedValue184.setter
    def TaggedValue184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_TagDefinition__TaggedValue184", None)
        self.__TaggedValue184 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core185"):
                    opp_val = getattr(item, "core185", None)
                    
                    if opp_val == self:
                        setattr(item, "core185", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core185"):
                    opp_val = getattr(item, "core185", None)
                    
                    setattr(item, "core185", self)
                    

    @property
    def Stereotype181(self):
        return self.__Stereotype181

    @Stereotype181.setter
    def Stereotype181(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_TagDefinition__Stereotype181", None)
        self.__Stereotype181 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core182"):
                opp_val = getattr(old_value, "core182", None)
                if opp_val == self:
                    setattr(old_value, "core182", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core182"):
                opp_val = getattr(value, "core182", None)
                setattr(value, "core182", self)

    @property
    def foundation_core_TagDefinition(self):
        return self.__foundation_core_TagDefinition

    @foundation_core_TagDefinition.setter
    def foundation_core_TagDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_TagDefinition__foundation_core_TagDefinition", None)
        self.__foundation_core_TagDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Multiplicity179"):
                opp_val = getattr(old_value, "Multiplicity179", None)
                if opp_val == self:
                    setattr(old_value, "Multiplicity179", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Multiplicity179"):
                opp_val = getattr(value, "Multiplicity179", None)
                setattr(value, "Multiplicity179", self)

class foundation_core_Feature(ModelElement):

    def __init__(self, ownerScope: str, Classifier: "Classifier" = None, core194: "foundation_core_TaggedValue", ModelElement165: "foundation_core_TemplateParameter", core131: "foundation_core_PresentationElement", core174: "foundation_core_Stereotype", ModelElement202: "foundation_core_TemplateArgument", core77: "foundation_core_Constraint", ModelElement159: "foundation_core_TemplateParameter", core145: "foundation_core_Comment", core162: "foundation_core_TemplateParameter", core127: "foundation_core_Dependency", core124: "foundation_core_Dependency", core148: "foundation_core_Flow", core188: "foundation_core_TaggedValue", core154: "foundation_core_ElementResidence", core38: "foundation_core_Namespace", core151: "foundation_core_Flow"):
        self.ownerScope = ownerScope
        self.Classifier = Classifier
        
    @property
    def ownerScope(self) -> str:
        return self.__ownerScope

    @ownerScope.setter
    def ownerScope(self, ownerScope: str):
        self.__ownerScope = ownerScope

    @property
    def Classifier(self):
        return self.__Classifier

    @Classifier.setter
    def Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_Feature__Classifier", None)
        self.__Classifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core56"):
                opp_val = getattr(old_value, "core56", None)
                if opp_val == self:
                    setattr(old_value, "core56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core56"):
                opp_val = getattr(value, "core56", None)
                setattr(value, "core56", self)

class foundation_core_EnumerationLiteral(ModelElement):

    pass
class foundation_core_Relationship(ModelElement):

    pass
class foundation_core_Comment(ModelElement):

    def __init__(self, body: str, ModelElement144: set["ModelElement"] = None, core194: "foundation_core_TaggedValue", ModelElement165: "foundation_core_TemplateParameter", core131: "foundation_core_PresentationElement", core174: "foundation_core_Stereotype", ModelElement202: "foundation_core_TemplateArgument", core77: "foundation_core_Constraint", ModelElement159: "foundation_core_TemplateParameter", core145: "foundation_core_Comment", core162: "foundation_core_TemplateParameter", core127: "foundation_core_Dependency", core124: "foundation_core_Dependency", core148: "foundation_core_Flow", core188: "foundation_core_TaggedValue", core154: "foundation_core_ElementResidence", core38: "foundation_core_Namespace", core151: "foundation_core_Flow"):
        self.body = body
        self.ModelElement144 = ModelElement144 if ModelElement144 is not None else set()
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def ModelElement144(self):
        return self.__ModelElement144

    @ModelElement144.setter
    def ModelElement144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_Comment__ModelElement144", None)
        self.__ModelElement144 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core145"):
                    opp_val = getattr(item, "core145", None)
                    
                    if opp_val == self:
                        setattr(item, "core145", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core145"):
                    opp_val = getattr(item, "core145", None)
                    
                    setattr(item, "core145", self)
                    

class foundation_core_GeneralizableElement(ModelElement):

    def __init__(self, isRoot: str, isLeaf: str, isAbstract: str, Generalization: set["Generalization"] = None, Generalization35: set["Generalization"] = None, core194: "foundation_core_TaggedValue", ModelElement165: "foundation_core_TemplateParameter", core131: "foundation_core_PresentationElement", core174: "foundation_core_Stereotype", ModelElement202: "foundation_core_TemplateArgument", core77: "foundation_core_Constraint", ModelElement159: "foundation_core_TemplateParameter", core145: "foundation_core_Comment", core162: "foundation_core_TemplateParameter", core127: "foundation_core_Dependency", core124: "foundation_core_Dependency", core148: "foundation_core_Flow", core188: "foundation_core_TaggedValue", core154: "foundation_core_ElementResidence", core38: "foundation_core_Namespace", core151: "foundation_core_Flow"):
        self.isRoot = isRoot
        self.isLeaf = isLeaf
        self.isAbstract = isAbstract
        self.Generalization = Generalization if Generalization is not None else set()
        self.Generalization35 = Generalization35 if Generalization35 is not None else set()
        
    @property
    def isRoot(self) -> str:
        return self.__isRoot

    @isRoot.setter
    def isRoot(self, isRoot: str):
        self.__isRoot = isRoot

    @property
    def isAbstract(self) -> str:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract

    @property
    def isLeaf(self) -> str:
        return self.__isLeaf

    @isLeaf.setter
    def isLeaf(self, isLeaf: str):
        self.__isLeaf = isLeaf

    @property
    def Generalization35(self):
        return self.__Generalization35

    @Generalization35.setter
    def Generalization35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_GeneralizableElement__Generalization35", None)
        self.__Generalization35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core36"):
                    opp_val = getattr(item, "core36", None)
                    
                    if opp_val == self:
                        setattr(item, "core36", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core36"):
                    opp_val = getattr(item, "core36", None)
                    
                    setattr(item, "core36", self)
                    

    @property
    def Generalization(self):
        return self.__Generalization

    @Generalization.setter
    def Generalization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_GeneralizableElement__Generalization", None)
        self.__Generalization = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core33"):
                    opp_val = getattr(item, "core33", None)
                    
                    if opp_val == self:
                        setattr(item, "core33", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core33"):
                    opp_val = getattr(item, "core33", None)
                    
                    setattr(item, "core33", self)
                    

class StateMachine:

    pass
class Constraint:

    pass
class Dependency:

    pass
class foundation_core_Binding(Dependency):

    pass
class foundation_core_Abstraction(Dependency):

    pass
class foundation_core_Permission(Dependency):

    pass
class foundation_core_Usage(Dependency):

    pass
class Namespace:

    pass
class ElementResidence:

    pass
class Comment:

    pass
class Flow:

    pass
class PresentationElement:

    pass
class Expression:

    pass
class foundation_data_types_ProcedureExpression(Expression):

    pass
class foundation_data_types_ObjectSetExpression(Expression):

    pass
class foundation_data_types_TypeExpression(Expression):

    pass
class foundation_data_types_MappingExpression(Expression):

    pass
class foundation_data_types_BooleanExpression(Expression):

    pass
class foundation_data_types_Expression:

    def __init__(self, language: str, body: str):
        self.language = language
        self.body = body
        
    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

class Element:

    pass
class foundation_core_PresentationElement(Element):

    pass
class foundation_core_ModelElement(Element):

    def __init__(self, name: str, visibility: str, isSpecification: str, Dependency9: set["Dependency"] = None, PresentationElement: set["PresentationElement"] = None, Flow: set["Flow"] = None, Flow16: set["Flow"] = None, Comment: set["Comment"] = None, ElementResidence: set["ElementResidence"] = None, Namespace: "Namespace" = None, Dependency: set["Dependency"] = None, Constraint: set["Constraint"] = None, TaggedValue29: set["TaggedValue"] = None, StateMachine: set["StateMachine"] = None, TemplateParameter: set["TemplateParameter"] = None, Stereotype: set["Stereotype"] = None, TaggedValue: set["TaggedValue"] = None):
        self.name = name
        self.visibility = visibility
        self.isSpecification = isSpecification
        self.Dependency9 = Dependency9 if Dependency9 is not None else set()
        self.PresentationElement = PresentationElement if PresentationElement is not None else set()
        self.Flow = Flow if Flow is not None else set()
        self.Flow16 = Flow16 if Flow16 is not None else set()
        self.Comment = Comment if Comment is not None else set()
        self.ElementResidence = ElementResidence if ElementResidence is not None else set()
        self.Namespace = Namespace
        self.Dependency = Dependency if Dependency is not None else set()
        self.Constraint = Constraint if Constraint is not None else set()
        self.TaggedValue29 = TaggedValue29 if TaggedValue29 is not None else set()
        self.StateMachine = StateMachine if StateMachine is not None else set()
        self.TemplateParameter = TemplateParameter if TemplateParameter is not None else set()
        self.Stereotype = Stereotype if Stereotype is not None else set()
        self.TaggedValue = TaggedValue if TaggedValue is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def isSpecification(self) -> str:
        return self.__isSpecification

    @isSpecification.setter
    def isSpecification(self, isSpecification: str):
        self.__isSpecification = isSpecification

    @property
    def PresentationElement(self):
        return self.__PresentationElement

    @PresentationElement.setter
    def PresentationElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_ModelElement__PresentationElement", None)
        self.__PresentationElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core12"):
                    opp_val = getattr(item, "core12", None)
                    
                    if opp_val == self:
                        setattr(item, "core12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core12"):
                    opp_val = getattr(item, "core12", None)
                    
                    setattr(item, "core12", self)
                    

    @property
    def Flow16(self):
        return self.__Flow16

    @Flow16.setter
    def Flow16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_ModelElement__Flow16", None)
        self.__Flow16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core17"):
                    opp_val = getattr(item, "core17", None)
                    
                    if opp_val == self:
                        setattr(item, "core17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core17"):
                    opp_val = getattr(item, "core17", None)
                    
                    setattr(item, "core17", self)
                    

    @property
    def Namespace(self):
        return self.__Namespace

    @Namespace.setter
    def Namespace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_ModelElement__Namespace", None)
        self.__Namespace = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "core"):
                opp_val = getattr(old_value, "core", None)
                if opp_val == self:
                    setattr(old_value, "core", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "core"):
                opp_val = getattr(value, "core", None)
                setattr(value, "core", self)

    @property
    def Dependency(self):
        return self.__Dependency

    @Dependency.setter
    def Dependency(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_ModelElement__Dependency", None)
        self.__Dependency = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core5"):
                    opp_val = getattr(item, "core5", None)
                    
                    if opp_val == self:
                        setattr(item, "core5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core5"):
                    opp_val = getattr(item, "core5", None)
                    
                    setattr(item, "core5", self)
                    

    @property
    def TaggedValue29(self):
        return self.__TaggedValue29

    @TaggedValue29.setter
    def TaggedValue29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_ModelElement__TaggedValue29", None)
        self.__TaggedValue29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core30"):
                    opp_val = getattr(item, "core30", None)
                    
                    if opp_val == self:
                        setattr(item, "core30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core30"):
                    opp_val = getattr(item, "core30", None)
                    
                    setattr(item, "core30", self)
                    

    @property
    def Constraint(self):
        return self.__Constraint

    @Constraint.setter
    def Constraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_ModelElement__Constraint", None)
        self.__Constraint = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core7"):
                    opp_val = getattr(item, "core7", None)
                    
                    if opp_val == self:
                        setattr(item, "core7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core7"):
                    opp_val = getattr(item, "core7", None)
                    
                    setattr(item, "core7", self)
                    

    @property
    def Dependency9(self):
        return self.__Dependency9

    @Dependency9.setter
    def Dependency9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_ModelElement__Dependency9", None)
        self.__Dependency9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core10"):
                    opp_val = getattr(item, "core10", None)
                    
                    if opp_val == self:
                        setattr(item, "core10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core10"):
                    opp_val = getattr(item, "core10", None)
                    
                    setattr(item, "core10", self)
                    

    @property
    def TaggedValue(self):
        return self.__TaggedValue

    @TaggedValue.setter
    def TaggedValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_ModelElement__TaggedValue", None)
        self.__TaggedValue = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core27"):
                    opp_val = getattr(item, "core27", None)
                    
                    if opp_val == self:
                        setattr(item, "core27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core27"):
                    opp_val = getattr(item, "core27", None)
                    
                    setattr(item, "core27", self)
                    

    @property
    def Flow(self):
        return self.__Flow

    @Flow.setter
    def Flow(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_ModelElement__Flow", None)
        self.__Flow = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core14"):
                    opp_val = getattr(item, "core14", None)
                    
                    if opp_val == self:
                        setattr(item, "core14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core14"):
                    opp_val = getattr(item, "core14", None)
                    
                    setattr(item, "core14", self)
                    

    @property
    def ElementResidence(self):
        return self.__ElementResidence

    @ElementResidence.setter
    def ElementResidence(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_ModelElement__ElementResidence", None)
        self.__ElementResidence = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core21"):
                    opp_val = getattr(item, "core21", None)
                    
                    if opp_val == self:
                        setattr(item, "core21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core21"):
                    opp_val = getattr(item, "core21", None)
                    
                    setattr(item, "core21", self)
                    

    @property
    def Comment(self):
        return self.__Comment

    @Comment.setter
    def Comment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_ModelElement__Comment", None)
        self.__Comment = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core19"):
                    opp_val = getattr(item, "core19", None)
                    
                    if opp_val == self:
                        setattr(item, "core19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core19"):
                    opp_val = getattr(item, "core19", None)
                    
                    setattr(item, "core19", self)
                    

    @property
    def StateMachine(self):
        return self.__StateMachine

    @StateMachine.setter
    def StateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_ModelElement__StateMachine", None)
        self.__StateMachine = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "behavioral_elements.ecorestate_machines"):
                    opp_val = getattr(item, "behavioral_elements.ecorestate_machines", None)
                    
                    if opp_val == self:
                        setattr(item, "behavioral_elements.ecorestate_machines", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "behavioral_elements.ecorestate_machines"):
                    opp_val = getattr(item, "behavioral_elements.ecorestate_machines", None)
                    
                    setattr(item, "behavioral_elements.ecorestate_machines", self)
                    

    @property
    def Stereotype(self):
        return self.__Stereotype

    @Stereotype.setter
    def Stereotype(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_ModelElement__Stereotype", None)
        self.__Stereotype = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core25"):
                    opp_val = getattr(item, "core25", None)
                    
                    if opp_val == self:
                        setattr(item, "core25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core25"):
                    opp_val = getattr(item, "core25", None)
                    
                    setattr(item, "core25", self)
                    

    @property
    def TemplateParameter(self):
        return self.__TemplateParameter

    @TemplateParameter.setter
    def TemplateParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_ModelElement__TemplateParameter", None)
        self.__TemplateParameter = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core23"):
                    opp_val = getattr(item, "core23", None)
                    
                    if opp_val == self:
                        setattr(item, "core23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core23"):
                    opp_val = getattr(item, "core23", None)
                    
                    setattr(item, "core23", self)
                    

class foundation_core_Element(ABC):

    pass
class foundation_data_types_ArgListsExpression(Expression):

    pass
class foundation_data_types_TimeExpression(Expression):

    pass
class foundation_data_types_IterationExpression(Expression):

    pass
class foundation_data_types_ActionExpression(Expression):

    pass
class Multiplicity:

    pass
class foundation_data_types_MultiplicityRange:

    def __init__(self, lower: str, upper: str, Multiplicity: "Multiplicity" = None):
        self.lower = lower
        self.upper = upper
        self.Multiplicity = Multiplicity
        
    @property
    def lower(self) -> str:
        return self.__lower

    @lower.setter
    def lower(self, lower: str):
        self.__lower = lower

    @property
    def upper(self) -> str:
        return self.__upper

    @upper.setter
    def upper(self, upper: str):
        self.__upper = upper

    @property
    def Multiplicity(self):
        return self.__Multiplicity

    @Multiplicity.setter
    def Multiplicity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_data_types_MultiplicityRange__Multiplicity", None)
        self.__Multiplicity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "data_types2"):
                opp_val = getattr(old_value, "data_types2", None)
                if opp_val == self:
                    setattr(old_value, "data_types2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "data_types2"):
                opp_val = getattr(value, "data_types2", None)
                setattr(value, "data_types2", self)

class MultiplicityRange:

    pass
class foundation_data_types_Multiplicity:

    pass