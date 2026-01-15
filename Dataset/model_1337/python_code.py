from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class PrimitiveDataType(Enum):
    Boolean = "Boolean"
    Integer = "Integer"
    String = "String"
    Double = "Double"
    Date = "Date"
class ScopeType(Enum):
    instance = "instance"
    classifier = "classifier"
class OperatorType(Enum):
    multiply = "multiply"
    divide = "divide"
    module = "module"
    not = "not"
    or = "or"
    and = "and"
    lt = "lt"
    lte = "lte"
    gt = "gt"
    gte = "gte"
    equals = "equals"
    distinct = "distinct"
    negative = "negative"
    add = "add"
    subtract = "subtract"
class VisbilityType(Enum):
    private = "private"
    public = "public"
    protected = "protected"
    package = "package"


############################################
# Definition of Classes
############################################

class Relation:

    pass
class umlclassdiagram_Association(Relation):

    pass
class umlclassdiagram_Composition(Relation):

    pass
class umlclassdiagram_Aggregation(Relation):

    pass
class umlclassdiagram_Dependency(Relation):

    pass
class Feature:

    pass
class umlclassdiagram_Attribute(Feature):

    def __init__(self, derived: bool):
        self.derived = derived
        
    @property
    def derived(self) -> bool:
        return self.__derived

    @derived.setter
    def derived(self, derived: bool):
        self.__derived = derived

class Classifier:

    pass
class umlclassdiagram_AssociationClass(Classifier):

    pass
class umlclassdiagram_Class(Classifier):

    pass
class Modifier:

    pass
class umlclassdiagram_Operator:

    def __init__(self, operator: str, umlclassdiagram_Operator: "umlclassdiagram_Operation" = None):
        self.operator = operator
        self.umlclassdiagram_Operator = umlclassdiagram_Operator
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def umlclassdiagram_Operator(self):
        return self.__umlclassdiagram_Operator

    @umlclassdiagram_Operator.setter
    def umlclassdiagram_Operator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlclassdiagram_Operator__umlclassdiagram_Operator", None)
        self.__umlclassdiagram_Operator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umlclassdiagram_Operation114"):
                opp_val = getattr(old_value, "umlclassdiagram_Operation114", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umlclassdiagram_Operation114"):
                opp_val = getattr(value, "umlclassdiagram_Operation114", None)
                if opp_val is None:
                    setattr(value, "umlclassdiagram_Operation114", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class umlclassdiagram_Operation(Feature):

    pass
class NamedElement:

    pass
class umlclassdiagram_Parameter(NamedElement):

    pass
class umlclassdiagram_NamedElement(ABC):

    def __init__(self, name: str, umlclassdiagram_NamedElement96: "umlclassdiagram_Feature" = None, umlclassdiagram_NamedElement: "umlclassdiagram_Parameter" = None):
        self.name = name
        self.umlclassdiagram_NamedElement96 = umlclassdiagram_NamedElement96
        self.umlclassdiagram_NamedElement = umlclassdiagram_NamedElement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def umlclassdiagram_NamedElement96(self):
        return self.__umlclassdiagram_NamedElement96

    @umlclassdiagram_NamedElement96.setter
    def umlclassdiagram_NamedElement96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlclassdiagram_NamedElement__umlclassdiagram_NamedElement96", None)
        self.__umlclassdiagram_NamedElement96 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umlclassdiagram_Feature95"):
                opp_val = getattr(old_value, "umlclassdiagram_Feature95", None)
                if opp_val == self:
                    setattr(old_value, "umlclassdiagram_Feature95", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umlclassdiagram_Feature95"):
                opp_val = getattr(value, "umlclassdiagram_Feature95", None)
                setattr(value, "umlclassdiagram_Feature95", self)

    @property
    def umlclassdiagram_NamedElement(self):
        return self.__umlclassdiagram_NamedElement

    @umlclassdiagram_NamedElement.setter
    def umlclassdiagram_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlclassdiagram_NamedElement__umlclassdiagram_NamedElement", None)
        self.__umlclassdiagram_NamedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umlclassdiagram_Parameter"):
                opp_val = getattr(old_value, "umlclassdiagram_Parameter", None)
                if opp_val == self:
                    setattr(old_value, "umlclassdiagram_Parameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umlclassdiagram_Parameter"):
                opp_val = getattr(value, "umlclassdiagram_Parameter", None)
                setattr(value, "umlclassdiagram_Parameter", self)

class umlclassdiagram_Constraint:

    def __init__(self, id: str, umlclassdiagram_Constraint: "umlclassdiagram_ClassDiagram" = None, umlclassdiagram_Constraint106: "umlclassdiagram_Class" = None, umlclassdiagram_Constraint109: set["umlclassdiagram_RootCS"] = None):
        self.id = id
        self.umlclassdiagram_Constraint = umlclassdiagram_Constraint
        self.umlclassdiagram_Constraint106 = umlclassdiagram_Constraint106
        self.umlclassdiagram_Constraint109 = umlclassdiagram_Constraint109 if umlclassdiagram_Constraint109 is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def umlclassdiagram_Constraint109(self):
        return self.__umlclassdiagram_Constraint109

    @umlclassdiagram_Constraint109.setter
    def umlclassdiagram_Constraint109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlclassdiagram_Constraint__umlclassdiagram_Constraint109", None)
        self.__umlclassdiagram_Constraint109 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "umlclassdiagram_RootCS110"):
                    opp_val = getattr(item, "umlclassdiagram_RootCS110", None)
                    
                    if opp_val == self:
                        setattr(item, "umlclassdiagram_RootCS110", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "umlclassdiagram_RootCS110"):
                    opp_val = getattr(item, "umlclassdiagram_RootCS110", None)
                    
                    setattr(item, "umlclassdiagram_RootCS110", self)
                    

    @property
    def umlclassdiagram_Constraint(self):
        return self.__umlclassdiagram_Constraint

    @umlclassdiagram_Constraint.setter
    def umlclassdiagram_Constraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlclassdiagram_Constraint__umlclassdiagram_Constraint", None)
        self.__umlclassdiagram_Constraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umlclassdiagram_ClassDiagram92"):
                opp_val = getattr(old_value, "umlclassdiagram_ClassDiagram92", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umlclassdiagram_ClassDiagram92"):
                opp_val = getattr(value, "umlclassdiagram_ClassDiagram92", None)
                if opp_val is None:
                    setattr(value, "umlclassdiagram_ClassDiagram92", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def umlclassdiagram_Constraint106(self):
        return self.__umlclassdiagram_Constraint106

    @umlclassdiagram_Constraint106.setter
    def umlclassdiagram_Constraint106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlclassdiagram_Constraint__umlclassdiagram_Constraint106", None)
        self.__umlclassdiagram_Constraint106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umlclassdiagram_Class107"):
                opp_val = getattr(old_value, "umlclassdiagram_Class107", None)
                if opp_val == self:
                    setattr(old_value, "umlclassdiagram_Class107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umlclassdiagram_Class107"):
                opp_val = getattr(value, "umlclassdiagram_Class107", None)
                setattr(value, "umlclassdiagram_Class107", self)

class umlclassdiagram_PrimitiveElement(NamedElement):

    def __init__(self, type: str, umlclassdiagram_PrimitiveElement: "umlclassdiagram_ClassDiagram" = None):
        self.type = type
        self.umlclassdiagram_PrimitiveElement = umlclassdiagram_PrimitiveElement
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def umlclassdiagram_PrimitiveElement(self):
        return self.__umlclassdiagram_PrimitiveElement

    @umlclassdiagram_PrimitiveElement.setter
    def umlclassdiagram_PrimitiveElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlclassdiagram_PrimitiveElement__umlclassdiagram_PrimitiveElement", None)
        self.__umlclassdiagram_PrimitiveElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umlclassdiagram_ClassDiagram90"):
                opp_val = getattr(old_value, "umlclassdiagram_ClassDiagram90", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umlclassdiagram_ClassDiagram90"):
                opp_val = getattr(value, "umlclassdiagram_ClassDiagram90", None)
                if opp_val is None:
                    setattr(value, "umlclassdiagram_ClassDiagram90", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class umlclassdiagram_Relation(Modifier):

    def __init__(self, nsrc: str, ntar: str, derived: bool, umlclassdiagram_Relation: "umlclassdiagram_ClassDiagram" = None, umlclassdiagram_Relation116: "umlclassdiagram_Classifier" = None, umlclassdiagram_Relation119: "umlclassdiagram_Classifier" = None):
        self.nsrc = nsrc
        self.ntar = ntar
        self.derived = derived
        self.umlclassdiagram_Relation = umlclassdiagram_Relation
        self.umlclassdiagram_Relation116 = umlclassdiagram_Relation116
        self.umlclassdiagram_Relation119 = umlclassdiagram_Relation119
        
    @property
    def ntar(self) -> str:
        return self.__ntar

    @ntar.setter
    def ntar(self, ntar: str):
        self.__ntar = ntar

    @property
    def derived(self) -> bool:
        return self.__derived

    @derived.setter
    def derived(self, derived: bool):
        self.__derived = derived

    @property
    def nsrc(self) -> str:
        return self.__nsrc

    @nsrc.setter
    def nsrc(self, nsrc: str):
        self.__nsrc = nsrc

    @property
    def umlclassdiagram_Relation119(self):
        return self.__umlclassdiagram_Relation119

    @umlclassdiagram_Relation119.setter
    def umlclassdiagram_Relation119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlclassdiagram_Relation__umlclassdiagram_Relation119", None)
        self.__umlclassdiagram_Relation119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umlclassdiagram_Classifier120"):
                opp_val = getattr(old_value, "umlclassdiagram_Classifier120", None)
                if opp_val == self:
                    setattr(old_value, "umlclassdiagram_Classifier120", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umlclassdiagram_Classifier120"):
                opp_val = getattr(value, "umlclassdiagram_Classifier120", None)
                setattr(value, "umlclassdiagram_Classifier120", self)

    @property
    def umlclassdiagram_Relation(self):
        return self.__umlclassdiagram_Relation

    @umlclassdiagram_Relation.setter
    def umlclassdiagram_Relation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlclassdiagram_Relation__umlclassdiagram_Relation", None)
        self.__umlclassdiagram_Relation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umlclassdiagram_ClassDiagram88"):
                opp_val = getattr(old_value, "umlclassdiagram_ClassDiagram88", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umlclassdiagram_ClassDiagram88"):
                opp_val = getattr(value, "umlclassdiagram_ClassDiagram88", None)
                if opp_val is None:
                    setattr(value, "umlclassdiagram_ClassDiagram88", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def umlclassdiagram_Relation116(self):
        return self.__umlclassdiagram_Relation116

    @umlclassdiagram_Relation116.setter
    def umlclassdiagram_Relation116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlclassdiagram_Relation__umlclassdiagram_Relation116", None)
        self.__umlclassdiagram_Relation116 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umlclassdiagram_Classifier117"):
                opp_val = getattr(old_value, "umlclassdiagram_Classifier117", None)
                if opp_val == self:
                    setattr(old_value, "umlclassdiagram_Classifier117", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umlclassdiagram_Classifier117"):
                opp_val = getattr(value, "umlclassdiagram_Classifier117", None)
                setattr(value, "umlclassdiagram_Classifier117", self)

class umlclassdiagram_Classifier(Modifier):

    def __init__(self, abstract: bool, derived: bool, umlclassdiagram_Classifier: "umlclassdiagram_ClassDiagram" = None, umlclassdiagram_Classifier117: "umlclassdiagram_Relation" = None, umlclassdiagram_Classifier98: set["umlclassdiagram_Feature"] = None, umlclassdiagram_Classifier101: set["umlclassdiagram_Class"] = None, umlclassdiagram_Classifier103: set["umlclassdiagram_Class"] = None, umlclassdiagram_Classifier120: "umlclassdiagram_Relation" = None):
        self.abstract = abstract
        self.derived = derived
        self.umlclassdiagram_Classifier = umlclassdiagram_Classifier
        self.umlclassdiagram_Classifier117 = umlclassdiagram_Classifier117
        self.umlclassdiagram_Classifier98 = umlclassdiagram_Classifier98 if umlclassdiagram_Classifier98 is not None else set()
        self.umlclassdiagram_Classifier101 = umlclassdiagram_Classifier101 if umlclassdiagram_Classifier101 is not None else set()
        self.umlclassdiagram_Classifier103 = umlclassdiagram_Classifier103 if umlclassdiagram_Classifier103 is not None else set()
        self.umlclassdiagram_Classifier120 = umlclassdiagram_Classifier120
        
    @property
    def abstract(self) -> bool:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract

    @property
    def derived(self) -> bool:
        return self.__derived

    @derived.setter
    def derived(self, derived: bool):
        self.__derived = derived

    @property
    def umlclassdiagram_Classifier98(self):
        return self.__umlclassdiagram_Classifier98

    @umlclassdiagram_Classifier98.setter
    def umlclassdiagram_Classifier98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlclassdiagram_Classifier__umlclassdiagram_Classifier98", None)
        self.__umlclassdiagram_Classifier98 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "umlclassdiagram_Feature99"):
                    opp_val = getattr(item, "umlclassdiagram_Feature99", None)
                    
                    if opp_val == self:
                        setattr(item, "umlclassdiagram_Feature99", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "umlclassdiagram_Feature99"):
                    opp_val = getattr(item, "umlclassdiagram_Feature99", None)
                    
                    setattr(item, "umlclassdiagram_Feature99", self)
                    

    @property
    def umlclassdiagram_Classifier101(self):
        return self.__umlclassdiagram_Classifier101

    @umlclassdiagram_Classifier101.setter
    def umlclassdiagram_Classifier101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlclassdiagram_Classifier__umlclassdiagram_Classifier101", None)
        self.__umlclassdiagram_Classifier101 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "umlclassdiagram_Class"):
                    opp_val = getattr(item, "umlclassdiagram_Class", None)
                    
                    if opp_val == self:
                        setattr(item, "umlclassdiagram_Class", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "umlclassdiagram_Class"):
                    opp_val = getattr(item, "umlclassdiagram_Class", None)
                    
                    setattr(item, "umlclassdiagram_Class", self)
                    

    @property
    def umlclassdiagram_Classifier117(self):
        return self.__umlclassdiagram_Classifier117

    @umlclassdiagram_Classifier117.setter
    def umlclassdiagram_Classifier117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlclassdiagram_Classifier__umlclassdiagram_Classifier117", None)
        self.__umlclassdiagram_Classifier117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umlclassdiagram_Relation116"):
                opp_val = getattr(old_value, "umlclassdiagram_Relation116", None)
                if opp_val == self:
                    setattr(old_value, "umlclassdiagram_Relation116", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umlclassdiagram_Relation116"):
                opp_val = getattr(value, "umlclassdiagram_Relation116", None)
                setattr(value, "umlclassdiagram_Relation116", self)

    @property
    def umlclassdiagram_Classifier103(self):
        return self.__umlclassdiagram_Classifier103

    @umlclassdiagram_Classifier103.setter
    def umlclassdiagram_Classifier103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlclassdiagram_Classifier__umlclassdiagram_Classifier103", None)
        self.__umlclassdiagram_Classifier103 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "umlclassdiagram_Class104"):
                    opp_val = getattr(item, "umlclassdiagram_Class104", None)
                    
                    if opp_val == self:
                        setattr(item, "umlclassdiagram_Class104", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "umlclassdiagram_Class104"):
                    opp_val = getattr(item, "umlclassdiagram_Class104", None)
                    
                    setattr(item, "umlclassdiagram_Class104", self)
                    

    @property
    def umlclassdiagram_Classifier(self):
        return self.__umlclassdiagram_Classifier

    @umlclassdiagram_Classifier.setter
    def umlclassdiagram_Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlclassdiagram_Classifier__umlclassdiagram_Classifier", None)
        self.__umlclassdiagram_Classifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umlclassdiagram_ClassDiagram"):
                opp_val = getattr(old_value, "umlclassdiagram_ClassDiagram", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umlclassdiagram_ClassDiagram"):
                opp_val = getattr(value, "umlclassdiagram_ClassDiagram", None)
                if opp_val is None:
                    setattr(value, "umlclassdiagram_ClassDiagram", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def umlclassdiagram_Classifier120(self):
        return self.__umlclassdiagram_Classifier120

    @umlclassdiagram_Classifier120.setter
    def umlclassdiagram_Classifier120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlclassdiagram_Classifier__umlclassdiagram_Classifier120", None)
        self.__umlclassdiagram_Classifier120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umlclassdiagram_Relation119"):
                opp_val = getattr(old_value, "umlclassdiagram_Relation119", None)
                if opp_val == self:
                    setattr(old_value, "umlclassdiagram_Relation119", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umlclassdiagram_Relation119"):
                opp_val = getattr(value, "umlclassdiagram_Relation119", None)
                setattr(value, "umlclassdiagram_Relation119", self)

class umlclassdiagram_ClassDiagram:

    pass
class NavigationPathCS:

    pass
class umlclassdiagram_NavigationPathElementCS(NavigationPathCS):

    pass
class umlclassdiagram_NavigationPathVariableCS(NavigationPathCS):

    def __init__(self, varName: str):
        self.varName = varName
        
    @property
    def varName(self) -> str:
        return self.__varName

    @varName.setter
    def varName(self, varName: str):
        self.__varName = varName

class umlclassdiagram_Modifier(NamedElement):

    def __init__(self, visibility: str, scope: str):
        self.visibility = visibility
        self.scope = scope
        
    @property
    def scope(self) -> str:
        return self.__scope

    @scope.setter
    def scope(self, scope: str):
        self.__scope = scope

    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

class umlclassdiagram_NavigationPathNameCS:

    pass
class BooleanLiteralExpCS:

    pass
class umlclassdiagram_BooleanExpCS(BooleanLiteralExpCS):

    def __init__(self, boolSymbol: bool):
        self.boolSymbol = boolSymbol
        
    @property
    def boolSymbol(self) -> bool:
        return self.__boolSymbol

    @boolSymbol.setter
    def boolSymbol(self, boolSymbol: bool):
        self.__boolSymbol = boolSymbol

class umlclassdiagram_Feature(ABC):

    def __init__(self, name: str, visibility: str, scope: str, umlclassdiagram_Feature: "umlclassdiagram_PathElementCS" = None, umlclassdiagram_Feature95: "umlclassdiagram_NamedElement" = None, umlclassdiagram_Feature83: "umlclassdiagram_NavigationPathElementCS" = None, umlclassdiagram_Feature99: "umlclassdiagram_Classifier" = None):
        self.name = name
        self.visibility = visibility
        self.scope = scope
        self.umlclassdiagram_Feature = umlclassdiagram_Feature
        self.umlclassdiagram_Feature95 = umlclassdiagram_Feature95
        self.umlclassdiagram_Feature83 = umlclassdiagram_Feature83
        self.umlclassdiagram_Feature99 = umlclassdiagram_Feature99
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def scope(self) -> str:
        return self.__scope

    @scope.setter
    def scope(self, scope: str):
        self.__scope = scope

    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def umlclassdiagram_Feature(self):
        return self.__umlclassdiagram_Feature

    @umlclassdiagram_Feature.setter
    def umlclassdiagram_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlclassdiagram_Feature__umlclassdiagram_Feature", None)
        self.__umlclassdiagram_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umlclassdiagram_PathElementCS"):
                opp_val = getattr(old_value, "umlclassdiagram_PathElementCS", None)
                if opp_val == self:
                    setattr(old_value, "umlclassdiagram_PathElementCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umlclassdiagram_PathElementCS"):
                opp_val = getattr(value, "umlclassdiagram_PathElementCS", None)
                setattr(value, "umlclassdiagram_PathElementCS", self)

    @property
    def umlclassdiagram_Feature99(self):
        return self.__umlclassdiagram_Feature99

    @umlclassdiagram_Feature99.setter
    def umlclassdiagram_Feature99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlclassdiagram_Feature__umlclassdiagram_Feature99", None)
        self.__umlclassdiagram_Feature99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umlclassdiagram_Classifier98"):
                opp_val = getattr(old_value, "umlclassdiagram_Classifier98", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umlclassdiagram_Classifier98"):
                opp_val = getattr(value, "umlclassdiagram_Classifier98", None)
                if opp_val is None:
                    setattr(value, "umlclassdiagram_Classifier98", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def umlclassdiagram_Feature83(self):
        return self.__umlclassdiagram_Feature83

    @umlclassdiagram_Feature83.setter
    def umlclassdiagram_Feature83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlclassdiagram_Feature__umlclassdiagram_Feature83", None)
        self.__umlclassdiagram_Feature83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umlclassdiagram_NavigationPathElementCS"):
                opp_val = getattr(old_value, "umlclassdiagram_NavigationPathElementCS", None)
                if opp_val == self:
                    setattr(old_value, "umlclassdiagram_NavigationPathElementCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umlclassdiagram_NavigationPathElementCS"):
                opp_val = getattr(value, "umlclassdiagram_NavigationPathElementCS", None)
                setattr(value, "umlclassdiagram_NavigationPathElementCS", self)

    @property
    def umlclassdiagram_Feature95(self):
        return self.__umlclassdiagram_Feature95

    @umlclassdiagram_Feature95.setter
    def umlclassdiagram_Feature95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlclassdiagram_Feature__umlclassdiagram_Feature95", None)
        self.__umlclassdiagram_Feature95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umlclassdiagram_NamedElement96"):
                opp_val = getattr(old_value, "umlclassdiagram_NamedElement96", None)
                if opp_val == self:
                    setattr(old_value, "umlclassdiagram_NamedElement96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umlclassdiagram_NamedElement96"):
                opp_val = getattr(value, "umlclassdiagram_NamedElement96", None)
                setattr(value, "umlclassdiagram_NamedElement96", self)

class PathCS:

    pass
class umlclassdiagram_PathElementCS(PathCS):

    pass
class umlclassdiagram_PathVariableCS(PathCS):

    def __init__(self, varName: str):
        self.varName = varName
        
    @property
    def varName(self) -> str:
        return self.__varName

    @varName.setter
    def varName(self, varName: str):
        self.__varName = varName

class umlclassdiagram_PathCS:

    pass
class LiteralExpCS:

    pass
class umlclassdiagram_StringLiteralExpCS(LiteralExpCS):

    def __init__(self, stringSymbol: str):
        self.stringSymbol = stringSymbol
        
    @property
    def stringSymbol(self) -> str:
        return self.__stringSymbol

    @stringSymbol.setter
    def stringSymbol(self, stringSymbol: str):
        self.__stringSymbol = stringSymbol

class umlclassdiagram_BooleanLiteralExpCS(LiteralExpCS):

    pass
class umlclassdiagram_IntLiteralExpCS(LiteralExpCS):

    def __init__(self, intSymbol: int):
        self.intSymbol = intSymbol
        
    @property
    def intSymbol(self) -> int:
        return self.__intSymbol

    @intSymbol.setter
    def intSymbol(self, intSymbol: int):
        self.__intSymbol = intSymbol

class umlclassdiagram_NavigationPathCS:

    pass
class umlclassdiagram_AccVarCS:

    def __init__(self, accVarName: str, umlclassdiagram_AccVarCS60: "umlclassdiagram_PathNameCS" = None, umlclassdiagram_AccVarCS63: "umlclassdiagram_ExpCS" = None, umlclassdiagram_AccVarCS: "umlclassdiagram_IterateExpCS" = None, umlclassdiagram_AccVarCS72: "umlclassdiagram_ExistsExpCS" = None, umlclassdiagram_AccVarCS85: "umlclassdiagram_ForAllExpCS" = None):
        self.accVarName = accVarName
        self.umlclassdiagram_AccVarCS60 = umlclassdiagram_AccVarCS60
        self.umlclassdiagram_AccVarCS63 = umlclassdiagram_AccVarCS63
        self.umlclassdiagram_AccVarCS = umlclassdiagram_AccVarCS
        self.umlclassdiagram_AccVarCS72 = umlclassdiagram_AccVarCS72
        self.umlclassdiagram_AccVarCS85 = umlclassdiagram_AccVarCS85
        
    @property
    def accVarName(self) -> str:
        return self.__accVarName

    @accVarName.setter
    def accVarName(self, accVarName: str):
        self.__accVarName = accVarName

    @property
    def umlclassdiagram_AccVarCS63(self):
        return self.__umlclassdiagram_AccVarCS63

    @umlclassdiagram_AccVarCS63.setter
    def umlclassdiagram_AccVarCS63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlclassdiagram_AccVarCS__umlclassdiagram_AccVarCS63", None)
        self.__umlclassdiagram_AccVarCS63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umlclassdiagram_ExpCS64"):
                opp_val = getattr(old_value, "umlclassdiagram_ExpCS64", None)
                if opp_val == self:
                    setattr(old_value, "umlclassdiagram_ExpCS64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umlclassdiagram_ExpCS64"):
                opp_val = getattr(value, "umlclassdiagram_ExpCS64", None)
                setattr(value, "umlclassdiagram_ExpCS64", self)

    @property
    def umlclassdiagram_AccVarCS(self):
        return self.__umlclassdiagram_AccVarCS

    @umlclassdiagram_AccVarCS.setter
    def umlclassdiagram_AccVarCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlclassdiagram_AccVarCS__umlclassdiagram_AccVarCS", None)
        self.__umlclassdiagram_AccVarCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umlclassdiagram_IterateExpCS"):
                opp_val = getattr(old_value, "umlclassdiagram_IterateExpCS", None)
                if opp_val == self:
                    setattr(old_value, "umlclassdiagram_IterateExpCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umlclassdiagram_IterateExpCS"):
                opp_val = getattr(value, "umlclassdiagram_IterateExpCS", None)
                setattr(value, "umlclassdiagram_IterateExpCS", self)

    @property
    def umlclassdiagram_AccVarCS85(self):
        return self.__umlclassdiagram_AccVarCS85

    @umlclassdiagram_AccVarCS85.setter
    def umlclassdiagram_AccVarCS85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlclassdiagram_AccVarCS__umlclassdiagram_AccVarCS85", None)
        self.__umlclassdiagram_AccVarCS85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umlclassdiagram_ForAllExpCS"):
                opp_val = getattr(old_value, "umlclassdiagram_ForAllExpCS", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umlclassdiagram_ForAllExpCS"):
                opp_val = getattr(value, "umlclassdiagram_ForAllExpCS", None)
                if opp_val is None:
                    setattr(value, "umlclassdiagram_ForAllExpCS", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def umlclassdiagram_AccVarCS60(self):
        return self.__umlclassdiagram_AccVarCS60

    @umlclassdiagram_AccVarCS60.setter
    def umlclassdiagram_AccVarCS60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlclassdiagram_AccVarCS__umlclassdiagram_AccVarCS60", None)
        self.__umlclassdiagram_AccVarCS60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umlclassdiagram_PathNameCS61"):
                opp_val = getattr(old_value, "umlclassdiagram_PathNameCS61", None)
                if opp_val == self:
                    setattr(old_value, "umlclassdiagram_PathNameCS61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umlclassdiagram_PathNameCS61"):
                opp_val = getattr(value, "umlclassdiagram_PathNameCS61", None)
                setattr(value, "umlclassdiagram_PathNameCS61", self)

    @property
    def umlclassdiagram_AccVarCS72(self):
        return self.__umlclassdiagram_AccVarCS72

    @umlclassdiagram_AccVarCS72.setter
    def umlclassdiagram_AccVarCS72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlclassdiagram_AccVarCS__umlclassdiagram_AccVarCS72", None)
        self.__umlclassdiagram_AccVarCS72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umlclassdiagram_ExistsExpCS"):
                opp_val = getattr(old_value, "umlclassdiagram_ExistsExpCS", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umlclassdiagram_ExistsExpCS"):
                opp_val = getattr(value, "umlclassdiagram_ExistsExpCS", None)
                if opp_val is None:
                    setattr(value, "umlclassdiagram_ExistsExpCS", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class LoopExpCS:

    pass
class umlclassdiagram_ForAllExpCS(LoopExpCS):

    pass
class umlclassdiagram_IterateExpCS(LoopExpCS):

    pass
class umlclassdiagram_ExistsExpCS(LoopExpCS):

    pass
class umlclassdiagram_CollectExpCS(LoopExpCS):

    pass
class umlclassdiagram_IteratorVarCS:

    def __init__(self, itName: str, umlclassdiagram_IteratorVarCS: "umlclassdiagram_LoopExpCS" = None, umlclassdiagram_IteratorVarCS56: "umlclassdiagram_PathNameCS" = None):
        self.itName = itName
        self.umlclassdiagram_IteratorVarCS = umlclassdiagram_IteratorVarCS
        self.umlclassdiagram_IteratorVarCS56 = umlclassdiagram_IteratorVarCS56
        
    @property
    def itName(self) -> str:
        return self.__itName

    @itName.setter
    def itName(self, itName: str):
        self.__itName = itName

    @property
    def umlclassdiagram_IteratorVarCS56(self):
        return self.__umlclassdiagram_IteratorVarCS56

    @umlclassdiagram_IteratorVarCS56.setter
    def umlclassdiagram_IteratorVarCS56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlclassdiagram_IteratorVarCS__umlclassdiagram_IteratorVarCS56", None)
        self.__umlclassdiagram_IteratorVarCS56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umlclassdiagram_PathNameCS57"):
                opp_val = getattr(old_value, "umlclassdiagram_PathNameCS57", None)
                if opp_val == self:
                    setattr(old_value, "umlclassdiagram_PathNameCS57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umlclassdiagram_PathNameCS57"):
                opp_val = getattr(value, "umlclassdiagram_PathNameCS57", None)
                setattr(value, "umlclassdiagram_PathNameCS57", self)

    @property
    def umlclassdiagram_IteratorVarCS(self):
        return self.__umlclassdiagram_IteratorVarCS

    @umlclassdiagram_IteratorVarCS.setter
    def umlclassdiagram_IteratorVarCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlclassdiagram_IteratorVarCS__umlclassdiagram_IteratorVarCS", None)
        self.__umlclassdiagram_IteratorVarCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umlclassdiagram_LoopExpCS"):
                opp_val = getattr(old_value, "umlclassdiagram_LoopExpCS", None)
                if opp_val == self:
                    setattr(old_value, "umlclassdiagram_LoopExpCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umlclassdiagram_LoopExpCS"):
                opp_val = getattr(value, "umlclassdiagram_LoopExpCS", None)
                setattr(value, "umlclassdiagram_LoopExpCS", self)

class umlclassdiagram_RoundedBracketClauseCS:

    pass
class NavigationExpCS:

    pass
class umlclassdiagram_LoopExpCS(NavigationExpCS):

    def __init__(self, logicOp: str, umlclassdiagram_LoopExpCS: "umlclassdiagram_IteratorVarCS" = None, umlclassdiagram_LoopExpCS53: set["umlclassdiagram_ExpCS"] = None):
        self.logicOp = logicOp
        self.umlclassdiagram_LoopExpCS = umlclassdiagram_LoopExpCS
        self.umlclassdiagram_LoopExpCS53 = umlclassdiagram_LoopExpCS53 if umlclassdiagram_LoopExpCS53 is not None else set()
        
    @property
    def logicOp(self) -> str:
        return self.__logicOp

    @logicOp.setter
    def logicOp(self, logicOp: str):
        self.__logicOp = logicOp

    @property
    def umlclassdiagram_LoopExpCS53(self):
        return self.__umlclassdiagram_LoopExpCS53

    @umlclassdiagram_LoopExpCS53.setter
    def umlclassdiagram_LoopExpCS53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlclassdiagram_LoopExpCS__umlclassdiagram_LoopExpCS53", None)
        self.__umlclassdiagram_LoopExpCS53 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "umlclassdiagram_ExpCS54"):
                    opp_val = getattr(item, "umlclassdiagram_ExpCS54", None)
                    
                    if opp_val == self:
                        setattr(item, "umlclassdiagram_ExpCS54", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "umlclassdiagram_ExpCS54"):
                    opp_val = getattr(item, "umlclassdiagram_ExpCS54", None)
                    
                    setattr(item, "umlclassdiagram_ExpCS54", self)
                    

    @property
    def umlclassdiagram_LoopExpCS(self):
        return self.__umlclassdiagram_LoopExpCS

    @umlclassdiagram_LoopExpCS.setter
    def umlclassdiagram_LoopExpCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlclassdiagram_LoopExpCS__umlclassdiagram_LoopExpCS", None)
        self.__umlclassdiagram_LoopExpCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umlclassdiagram_IteratorVarCS"):
                opp_val = getattr(old_value, "umlclassdiagram_IteratorVarCS", None)
                if opp_val == self:
                    setattr(old_value, "umlclassdiagram_IteratorVarCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umlclassdiagram_IteratorVarCS"):
                opp_val = getattr(value, "umlclassdiagram_IteratorVarCS", None)
                setattr(value, "umlclassdiagram_IteratorVarCS", self)

class umlclassdiagram_NavigationNameExpCS(NavigationExpCS):

    pass
class umlclassdiagram_NameExpCS(NavigationExpCS):

    pass
class PrimaryExpCS:

    pass
class umlclassdiagram_LiteralExpCS(PrimaryExpCS):

    pass
class CallExpCS:

    pass
class umlclassdiagram_PrimaryExpCS(CallExpCS):

    pass
class umlclassdiagram_NavigationExpCS(PrimaryExpCS):

    pass
class ExpCS:

    pass
class umlclassdiagram_LogicExpCS(ExpCS):

    def __init__(self, op: str, umlclassdiagram_LogicExpCS38: "umlclassdiagram_CallExpCS" = None, umlclassdiagram_LogicExpCS: "umlclassdiagram_LogicExpCS" = None, umlclassdiagram_LogicExpCS35: "umlclassdiagram_LogicExpCS" = None):
        self.op = op
        self.umlclassdiagram_LogicExpCS38 = umlclassdiagram_LogicExpCS38
        self.umlclassdiagram_LogicExpCS = umlclassdiagram_LogicExpCS
        self.umlclassdiagram_LogicExpCS35 = umlclassdiagram_LogicExpCS35
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def umlclassdiagram_LogicExpCS(self):
        return self.__umlclassdiagram_LogicExpCS

    @umlclassdiagram_LogicExpCS.setter
    def umlclassdiagram_LogicExpCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlclassdiagram_LogicExpCS__umlclassdiagram_LogicExpCS", None)
        self.__umlclassdiagram_LogicExpCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umlclassdiagram_LogicExpCS35"):
                opp_val = getattr(old_value, "umlclassdiagram_LogicExpCS35", None)
                if opp_val == self:
                    setattr(old_value, "umlclassdiagram_LogicExpCS35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umlclassdiagram_LogicExpCS35"):
                opp_val = getattr(value, "umlclassdiagram_LogicExpCS35", None)
                setattr(value, "umlclassdiagram_LogicExpCS35", self)

    @property
    def umlclassdiagram_LogicExpCS38(self):
        return self.__umlclassdiagram_LogicExpCS38

    @umlclassdiagram_LogicExpCS38.setter
    def umlclassdiagram_LogicExpCS38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlclassdiagram_LogicExpCS__umlclassdiagram_LogicExpCS38", None)
        self.__umlclassdiagram_LogicExpCS38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umlclassdiagram_CallExpCS"):
                opp_val = getattr(old_value, "umlclassdiagram_CallExpCS", None)
                if opp_val == self:
                    setattr(old_value, "umlclassdiagram_CallExpCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umlclassdiagram_CallExpCS"):
                opp_val = getattr(value, "umlclassdiagram_CallExpCS", None)
                setattr(value, "umlclassdiagram_CallExpCS", self)

    @property
    def umlclassdiagram_LogicExpCS35(self):
        return self.__umlclassdiagram_LogicExpCS35

    @umlclassdiagram_LogicExpCS35.setter
    def umlclassdiagram_LogicExpCS35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlclassdiagram_LogicExpCS__umlclassdiagram_LogicExpCS35", None)
        self.__umlclassdiagram_LogicExpCS35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umlclassdiagram_LogicExpCS"):
                opp_val = getattr(old_value, "umlclassdiagram_LogicExpCS", None)
                if opp_val == self:
                    setattr(old_value, "umlclassdiagram_LogicExpCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umlclassdiagram_LogicExpCS"):
                opp_val = getattr(value, "umlclassdiagram_LogicExpCS", None)
                setattr(value, "umlclassdiagram_LogicExpCS", self)

class umlclassdiagram_InvariantCS:

    pass
class umlclassdiagram_ExpCS:

    pass
class umlclassdiagram_ParameterCS:

    def __init__(self, name: str, umlclassdiagram_ParameterCS: "umlclassdiagram_OperationCS" = None, umlclassdiagram_ParameterCS25: "umlclassdiagram_PathNameCS" = None):
        self.name = name
        self.umlclassdiagram_ParameterCS = umlclassdiagram_ParameterCS
        self.umlclassdiagram_ParameterCS25 = umlclassdiagram_ParameterCS25
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def umlclassdiagram_ParameterCS25(self):
        return self.__umlclassdiagram_ParameterCS25

    @umlclassdiagram_ParameterCS25.setter
    def umlclassdiagram_ParameterCS25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlclassdiagram_ParameterCS__umlclassdiagram_ParameterCS25", None)
        self.__umlclassdiagram_ParameterCS25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umlclassdiagram_PathNameCS26"):
                opp_val = getattr(old_value, "umlclassdiagram_PathNameCS26", None)
                if opp_val == self:
                    setattr(old_value, "umlclassdiagram_PathNameCS26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umlclassdiagram_PathNameCS26"):
                opp_val = getattr(value, "umlclassdiagram_PathNameCS26", None)
                setattr(value, "umlclassdiagram_PathNameCS26", self)

    @property
    def umlclassdiagram_ParameterCS(self):
        return self.__umlclassdiagram_ParameterCS

    @umlclassdiagram_ParameterCS.setter
    def umlclassdiagram_ParameterCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlclassdiagram_ParameterCS__umlclassdiagram_ParameterCS", None)
        self.__umlclassdiagram_ParameterCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umlclassdiagram_OperationCS18"):
                opp_val = getattr(old_value, "umlclassdiagram_OperationCS18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umlclassdiagram_OperationCS18"):
                opp_val = getattr(value, "umlclassdiagram_OperationCS18", None)
                if opp_val is None:
                    setattr(value, "umlclassdiagram_OperationCS18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class umlclassdiagram_OperationCS:

    def __init__(self, name: str, umlclassdiagram_OperationCS: "umlclassdiagram_ClassCS" = None, umlclassdiagram_OperationCS18: set["umlclassdiagram_ParameterCS"] = None, umlclassdiagram_OperationCS20: "umlclassdiagram_PathNameCS" = None, umlclassdiagram_OperationCS23: "umlclassdiagram_ExpCS" = None):
        self.name = name
        self.umlclassdiagram_OperationCS = umlclassdiagram_OperationCS
        self.umlclassdiagram_OperationCS18 = umlclassdiagram_OperationCS18 if umlclassdiagram_OperationCS18 is not None else set()
        self.umlclassdiagram_OperationCS20 = umlclassdiagram_OperationCS20
        self.umlclassdiagram_OperationCS23 = umlclassdiagram_OperationCS23
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def umlclassdiagram_OperationCS23(self):
        return self.__umlclassdiagram_OperationCS23

    @umlclassdiagram_OperationCS23.setter
    def umlclassdiagram_OperationCS23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlclassdiagram_OperationCS__umlclassdiagram_OperationCS23", None)
        self.__umlclassdiagram_OperationCS23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umlclassdiagram_ExpCS"):
                opp_val = getattr(old_value, "umlclassdiagram_ExpCS", None)
                if opp_val == self:
                    setattr(old_value, "umlclassdiagram_ExpCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umlclassdiagram_ExpCS"):
                opp_val = getattr(value, "umlclassdiagram_ExpCS", None)
                setattr(value, "umlclassdiagram_ExpCS", self)

    @property
    def umlclassdiagram_OperationCS20(self):
        return self.__umlclassdiagram_OperationCS20

    @umlclassdiagram_OperationCS20.setter
    def umlclassdiagram_OperationCS20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlclassdiagram_OperationCS__umlclassdiagram_OperationCS20", None)
        self.__umlclassdiagram_OperationCS20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umlclassdiagram_PathNameCS21"):
                opp_val = getattr(old_value, "umlclassdiagram_PathNameCS21", None)
                if opp_val == self:
                    setattr(old_value, "umlclassdiagram_PathNameCS21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umlclassdiagram_PathNameCS21"):
                opp_val = getattr(value, "umlclassdiagram_PathNameCS21", None)
                setattr(value, "umlclassdiagram_PathNameCS21", self)

    @property
    def umlclassdiagram_OperationCS(self):
        return self.__umlclassdiagram_OperationCS

    @umlclassdiagram_OperationCS.setter
    def umlclassdiagram_OperationCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlclassdiagram_OperationCS__umlclassdiagram_OperationCS", None)
        self.__umlclassdiagram_OperationCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umlclassdiagram_ClassCS13"):
                opp_val = getattr(old_value, "umlclassdiagram_ClassCS13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umlclassdiagram_ClassCS13"):
                opp_val = getattr(value, "umlclassdiagram_ClassCS13", None)
                if opp_val is None:
                    setattr(value, "umlclassdiagram_ClassCS13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def umlclassdiagram_OperationCS18(self):
        return self.__umlclassdiagram_OperationCS18

    @umlclassdiagram_OperationCS18.setter
    def umlclassdiagram_OperationCS18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlclassdiagram_OperationCS__umlclassdiagram_OperationCS18", None)
        self.__umlclassdiagram_OperationCS18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "umlclassdiagram_ParameterCS"):
                    opp_val = getattr(item, "umlclassdiagram_ParameterCS", None)
                    
                    if opp_val == self:
                        setattr(item, "umlclassdiagram_ParameterCS", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "umlclassdiagram_ParameterCS"):
                    opp_val = getattr(item, "umlclassdiagram_ParameterCS", None)
                    
                    setattr(item, "umlclassdiagram_ParameterCS", self)
                    

class LogicExpCS:

    pass
class umlclassdiagram_CallExpCS(LogicExpCS):

    pass
class umlclassdiagram_ClassCS:

    def __init__(self, name: str, umlclassdiagram_ClassCS9: "umlclassdiagram_PathNameCS" = None, umlclassdiagram_ClassCS11: set["umlclassdiagram_PropertyCS"] = None, umlclassdiagram_ClassCS: "umlclassdiagram_PackageCS" = None, umlclassdiagram_ClassCS13: set["umlclassdiagram_OperationCS"] = None):
        self.name = name
        self.umlclassdiagram_ClassCS9 = umlclassdiagram_ClassCS9
        self.umlclassdiagram_ClassCS11 = umlclassdiagram_ClassCS11 if umlclassdiagram_ClassCS11 is not None else set()
        self.umlclassdiagram_ClassCS = umlclassdiagram_ClassCS
        self.umlclassdiagram_ClassCS13 = umlclassdiagram_ClassCS13 if umlclassdiagram_ClassCS13 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def umlclassdiagram_ClassCS13(self):
        return self.__umlclassdiagram_ClassCS13

    @umlclassdiagram_ClassCS13.setter
    def umlclassdiagram_ClassCS13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlclassdiagram_ClassCS__umlclassdiagram_ClassCS13", None)
        self.__umlclassdiagram_ClassCS13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "umlclassdiagram_OperationCS"):
                    opp_val = getattr(item, "umlclassdiagram_OperationCS", None)
                    
                    if opp_val == self:
                        setattr(item, "umlclassdiagram_OperationCS", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "umlclassdiagram_OperationCS"):
                    opp_val = getattr(item, "umlclassdiagram_OperationCS", None)
                    
                    setattr(item, "umlclassdiagram_OperationCS", self)
                    

    @property
    def umlclassdiagram_ClassCS(self):
        return self.__umlclassdiagram_ClassCS

    @umlclassdiagram_ClassCS.setter
    def umlclassdiagram_ClassCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlclassdiagram_ClassCS__umlclassdiagram_ClassCS", None)
        self.__umlclassdiagram_ClassCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umlclassdiagram_PackageCS7"):
                opp_val = getattr(old_value, "umlclassdiagram_PackageCS7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umlclassdiagram_PackageCS7"):
                opp_val = getattr(value, "umlclassdiagram_PackageCS7", None)
                if opp_val is None:
                    setattr(value, "umlclassdiagram_PackageCS7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def umlclassdiagram_ClassCS9(self):
        return self.__umlclassdiagram_ClassCS9

    @umlclassdiagram_ClassCS9.setter
    def umlclassdiagram_ClassCS9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlclassdiagram_ClassCS__umlclassdiagram_ClassCS9", None)
        self.__umlclassdiagram_ClassCS9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umlclassdiagram_PathNameCS"):
                opp_val = getattr(old_value, "umlclassdiagram_PathNameCS", None)
                if opp_val == self:
                    setattr(old_value, "umlclassdiagram_PathNameCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umlclassdiagram_PathNameCS"):
                opp_val = getattr(value, "umlclassdiagram_PathNameCS", None)
                setattr(value, "umlclassdiagram_PathNameCS", self)

    @property
    def umlclassdiagram_ClassCS11(self):
        return self.__umlclassdiagram_ClassCS11

    @umlclassdiagram_ClassCS11.setter
    def umlclassdiagram_ClassCS11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlclassdiagram_ClassCS__umlclassdiagram_ClassCS11", None)
        self.__umlclassdiagram_ClassCS11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "umlclassdiagram_PropertyCS"):
                    opp_val = getattr(item, "umlclassdiagram_PropertyCS", None)
                    
                    if opp_val == self:
                        setattr(item, "umlclassdiagram_PropertyCS", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "umlclassdiagram_PropertyCS"):
                    opp_val = getattr(item, "umlclassdiagram_PropertyCS", None)
                    
                    setattr(item, "umlclassdiagram_PropertyCS", self)
                    

class umlclassdiagram_ConstraintCS:

    pass
class umlclassdiagram_PackageCS:

    def __init__(self, name: str, umlclassdiagram_PackageCS: "umlclassdiagram_RootCS" = None, umlclassdiagram_PackageCS5: "umlclassdiagram_PackageCS" = None, umlclassdiagram_PackageCS3: set["umlclassdiagram_PackageCS"] = None, umlclassdiagram_PackageCS7: set["umlclassdiagram_ClassCS"] = None):
        self.name = name
        self.umlclassdiagram_PackageCS = umlclassdiagram_PackageCS
        self.umlclassdiagram_PackageCS5 = umlclassdiagram_PackageCS5
        self.umlclassdiagram_PackageCS3 = umlclassdiagram_PackageCS3 if umlclassdiagram_PackageCS3 is not None else set()
        self.umlclassdiagram_PackageCS7 = umlclassdiagram_PackageCS7 if umlclassdiagram_PackageCS7 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def umlclassdiagram_PackageCS3(self):
        return self.__umlclassdiagram_PackageCS3

    @umlclassdiagram_PackageCS3.setter
    def umlclassdiagram_PackageCS3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlclassdiagram_PackageCS__umlclassdiagram_PackageCS3", None)
        self.__umlclassdiagram_PackageCS3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "umlclassdiagram_PackageCS5"):
                    opp_val = getattr(item, "umlclassdiagram_PackageCS5", None)
                    
                    if opp_val == self:
                        setattr(item, "umlclassdiagram_PackageCS5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "umlclassdiagram_PackageCS5"):
                    opp_val = getattr(item, "umlclassdiagram_PackageCS5", None)
                    
                    setattr(item, "umlclassdiagram_PackageCS5", self)
                    

    @property
    def umlclassdiagram_PackageCS(self):
        return self.__umlclassdiagram_PackageCS

    @umlclassdiagram_PackageCS.setter
    def umlclassdiagram_PackageCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlclassdiagram_PackageCS__umlclassdiagram_PackageCS", None)
        self.__umlclassdiagram_PackageCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umlclassdiagram_RootCS"):
                opp_val = getattr(old_value, "umlclassdiagram_RootCS", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umlclassdiagram_RootCS"):
                opp_val = getattr(value, "umlclassdiagram_RootCS", None)
                if opp_val is None:
                    setattr(value, "umlclassdiagram_RootCS", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def umlclassdiagram_PackageCS5(self):
        return self.__umlclassdiagram_PackageCS5

    @umlclassdiagram_PackageCS5.setter
    def umlclassdiagram_PackageCS5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlclassdiagram_PackageCS__umlclassdiagram_PackageCS5", None)
        self.__umlclassdiagram_PackageCS5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umlclassdiagram_PackageCS3"):
                opp_val = getattr(old_value, "umlclassdiagram_PackageCS3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umlclassdiagram_PackageCS3"):
                opp_val = getattr(value, "umlclassdiagram_PackageCS3", None)
                if opp_val is None:
                    setattr(value, "umlclassdiagram_PackageCS3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def umlclassdiagram_PackageCS7(self):
        return self.__umlclassdiagram_PackageCS7

    @umlclassdiagram_PackageCS7.setter
    def umlclassdiagram_PackageCS7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlclassdiagram_PackageCS__umlclassdiagram_PackageCS7", None)
        self.__umlclassdiagram_PackageCS7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "umlclassdiagram_ClassCS"):
                    opp_val = getattr(item, "umlclassdiagram_ClassCS", None)
                    
                    if opp_val == self:
                        setattr(item, "umlclassdiagram_ClassCS", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "umlclassdiagram_ClassCS"):
                    opp_val = getattr(item, "umlclassdiagram_ClassCS", None)
                    
                    setattr(item, "umlclassdiagram_ClassCS", self)
                    

class umlclassdiagram_RootCS:

    pass
class umlclassdiagram_PropertyCS:

    def __init__(self, name: str, umlclassdiagram_PropertyCS: "umlclassdiagram_ClassCS" = None, umlclassdiagram_PropertyCS15: "umlclassdiagram_PathNameCS" = None):
        self.name = name
        self.umlclassdiagram_PropertyCS = umlclassdiagram_PropertyCS
        self.umlclassdiagram_PropertyCS15 = umlclassdiagram_PropertyCS15
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def umlclassdiagram_PropertyCS(self):
        return self.__umlclassdiagram_PropertyCS

    @umlclassdiagram_PropertyCS.setter
    def umlclassdiagram_PropertyCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlclassdiagram_PropertyCS__umlclassdiagram_PropertyCS", None)
        self.__umlclassdiagram_PropertyCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umlclassdiagram_ClassCS11"):
                opp_val = getattr(old_value, "umlclassdiagram_ClassCS11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umlclassdiagram_ClassCS11"):
                opp_val = getattr(value, "umlclassdiagram_ClassCS11", None)
                if opp_val is None:
                    setattr(value, "umlclassdiagram_ClassCS11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def umlclassdiagram_PropertyCS15(self):
        return self.__umlclassdiagram_PropertyCS15

    @umlclassdiagram_PropertyCS15.setter
    def umlclassdiagram_PropertyCS15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlclassdiagram_PropertyCS__umlclassdiagram_PropertyCS15", None)
        self.__umlclassdiagram_PropertyCS15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umlclassdiagram_PathNameCS16"):
                opp_val = getattr(old_value, "umlclassdiagram_PathNameCS16", None)
                if opp_val == self:
                    setattr(old_value, "umlclassdiagram_PathNameCS16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umlclassdiagram_PathNameCS16"):
                opp_val = getattr(value, "umlclassdiagram_PathNameCS16", None)
                setattr(value, "umlclassdiagram_PathNameCS16", self)

class umlclassdiagram_PathNameCS:

    pass