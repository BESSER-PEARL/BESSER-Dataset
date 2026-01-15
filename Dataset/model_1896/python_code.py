from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Composition(Enum):
    Sequential = "Sequential"
    Atomic = "Atomic"
class SpecialEdgeEnum(Enum):
    Synchronize = "Synchronize"
    Reference = "Reference"
    Reversion = "Reversion"
    BranchKill = "BranchKill"
class BehaviorType(Enum):
    StateRealization = "StateRealization"
    Selection = "Selection"
    Guard = "Guard"
    InternalInput = "InternalInput"
    InternalOutput = "InternalOutput"
    ExternalOutput = "ExternalOutput"
    ExternalInput = "ExternalInput"
class Operator(Enum):
    Reference = "Reference"
    Reversion = "Reversion"
    BranchKill = "BranchKill"
    Synchronize = "Synchronize"
    Conjunction = "Conjunction"
    Disjunction = "Disjunction"
    ExclusiveOR = "ExclusiveOR"
    NoOperator = "NoOperator"
class Branch(Enum):
    Parallel = "Parallel"
    Alternative = "Alternative"
class TraceabilityStatus(Enum):
    Original = "Original"
    Implied = "Implied"
    Missing = "Missing"
    Updated = "Updated"
    Deleted = "Deleted"
    DesignRefinement = "DesignRefinement"
class EventType(Enum):
    InternalInput = "InternalInput"
    InternalOutput = "InternalOutput"
    ExternalInput = "ExternalInput"
    ExternalOutput = "ExternalOutput"


############################################
# Definition of Classes
############################################

class graphbt_Author:

    def __init__(self, name: str, contact: str, role: str, graphbt_Author: "graphbt_AuthorList" = None):
        self.name = name
        self.contact = contact
        self.role = role
        self.graphbt_Author = graphbt_Author
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def contact(self) -> str:
        return self.__contact

    @contact.setter
    def contact(self, contact: str):
        self.__contact = contact

    @property
    def role(self) -> str:
        return self.__role

    @role.setter
    def role(self, role: str):
        self.__role = role

    @property
    def graphbt_Author(self):
        return self.__graphbt_Author

    @graphbt_Author.setter
    def graphbt_Author(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphbt_Author__graphbt_Author", None)
        self.__graphbt_Author = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphbt_AuthorList84"):
                opp_val = getattr(old_value, "graphbt_AuthorList84", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphbt_AuthorList84"):
                opp_val = getattr(value, "graphbt_AuthorList84", None)
                if opp_val is None:
                    setattr(value, "graphbt_AuthorList84", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Layout:

    pass
class graphbt_Button(Layout):

    def __init__(self, label: str):
        self.label = label
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

class graphbt_Parameter:

    def __init__(self, name: str, type: str, graphbt_Parameter: "graphbt_MethodDeclaration" = None):
        self.name = name
        self.type = type
        self.graphbt_Parameter = graphbt_Parameter
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def graphbt_Parameter(self):
        return self.__graphbt_Parameter

    @graphbt_Parameter.setter
    def graphbt_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphbt_Parameter__graphbt_Parameter", None)
        self.__graphbt_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphbt_MethodDeclaration80"):
                opp_val = getattr(old_value, "graphbt_MethodDeclaration80", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphbt_MethodDeclaration80"):
                opp_val = getattr(value, "graphbt_MethodDeclaration80", None)
                if opp_val is None:
                    setattr(value, "graphbt_MethodDeclaration80", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class graphbt_Layout:

    def __init__(self, cRef: str, x: int, y: int, width: int, height: int, z: int, graphbt_Layout: "graphbt_LayoutList" = None):
        self.cRef = cRef
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.z = z
        self.graphbt_Layout = graphbt_Layout
        
    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, height: int):
        self.__height = height

    @property
    def z(self) -> int:
        return self.__z

    @z.setter
    def z(self, z: int):
        self.__z = z

    @property
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, y: int):
        self.__y = y

    @property
    def cRef(self) -> str:
        return self.__cRef

    @cRef.setter
    def cRef(self, cRef: str):
        self.__cRef = cRef

    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, width: int):
        self.__width = width

    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, x: int):
        self.__x = x

    @property
    def graphbt_Layout(self):
        return self.__graphbt_Layout

    @graphbt_Layout.setter
    def graphbt_Layout(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphbt_Layout__graphbt_Layout", None)
        self.__graphbt_Layout = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphbt_LayoutList82"):
                opp_val = getattr(old_value, "graphbt_LayoutList82", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphbt_LayoutList82"):
                opp_val = getattr(value, "graphbt_LayoutList82", None)
                if opp_val is None:
                    setattr(value, "graphbt_LayoutList82", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class graphbt_AlternativeClass:

    def __init__(self, alternativeAttribute: str):
        self.alternativeAttribute = alternativeAttribute
        
    @property
    def alternativeAttribute(self) -> str:
        return self.__alternativeAttribute

    @alternativeAttribute.setter
    def alternativeAttribute(self, alternativeAttribute: str):
        self.__alternativeAttribute = alternativeAttribute

class GUI:

    pass
class graphbt_OutputGUI(GUI):

    pass
class graphbt_InputGUI(GUI):

    pass
class graphbt_GUI:

    def __init__(self, identifier: str, codeImplementation: str):
        self.identifier = identifier
        self.codeImplementation = codeImplementation
        
    @property
    def codeImplementation(self) -> str:
        return self.__codeImplementation

    @codeImplementation.setter
    def codeImplementation(self, codeImplementation: str):
        self.__codeImplementation = codeImplementation

    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

class graphbt_GUIImplementable:

    pass
class GUIImplementable:

    pass
class graphbt_OutputType(GUIImplementable):

    pass
class graphbt_InputType(GUIImplementable):

    pass
class graphbt_Information:

    def __init__(self, key: str, value: str, graphbt_Information: "graphbt_MapInformation" = None):
        self.key = key
        self.value = value
        self.graphbt_Information = graphbt_Information
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def graphbt_Information(self):
        return self.__graphbt_Information

    @graphbt_Information.setter
    def graphbt_Information(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphbt_Information__graphbt_Information", None)
        self.__graphbt_Information = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphbt_MapInformation75"):
                opp_val = getattr(old_value, "graphbt_MapInformation75", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphbt_MapInformation75"):
                opp_val = getattr(value, "graphbt_MapInformation75", None)
                if opp_val is None:
                    setattr(value, "graphbt_MapInformation75", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class graphbt_TraceabilityStatusClass:

    def __init__(self, traceabilityStatusLiteral: str):
        self.traceabilityStatusLiteral = traceabilityStatusLiteral
        
    @property
    def traceabilityStatusLiteral(self) -> str:
        return self.__traceabilityStatusLiteral

    @traceabilityStatusLiteral.setter
    def traceabilityStatusLiteral(self, traceabilityStatusLiteral: str):
        self.__traceabilityStatusLiteral = traceabilityStatusLiteral

class graphbt_OperatorClass:

    def __init__(self, operatorLiteral: str):
        self.operatorLiteral = operatorLiteral
        
    @property
    def operatorLiteral(self) -> str:
        return self.__operatorLiteral

    @operatorLiteral.setter
    def operatorLiteral(self, operatorLiteral: str):
        self.__operatorLiteral = operatorLiteral

class graphbt_Formula:

    def __init__(self, formulaName: str, graphbt_Formula: "graphbt_FormulaList" = None):
        self.formulaName = formulaName
        self.graphbt_Formula = graphbt_Formula
        
    @property
    def formulaName(self) -> str:
        return self.__formulaName

    @formulaName.setter
    def formulaName(self, formulaName: str):
        self.__formulaName = formulaName

    @property
    def graphbt_Formula(self):
        return self.__graphbt_Formula

    @graphbt_Formula.setter
    def graphbt_Formula(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphbt_Formula__graphbt_Formula", None)
        self.__graphbt_Formula = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphbt_FormulaList67"):
                opp_val = getattr(old_value, "graphbt_FormulaList67", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphbt_FormulaList67"):
                opp_val = getattr(value, "graphbt_FormulaList67", None)
                if opp_val is None:
                    setattr(value, "graphbt_FormulaList67", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class graphbt_MethodDeclaration:

    def __init__(self, type: str, name: str, graphbt_MethodDeclaration: "graphbt_Library" = None, graphbt_MethodDeclaration80: set["graphbt_Parameter"] = None):
        self.type = type
        self.name = name
        self.graphbt_MethodDeclaration = graphbt_MethodDeclaration
        self.graphbt_MethodDeclaration80 = graphbt_MethodDeclaration80 if graphbt_MethodDeclaration80 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def graphbt_MethodDeclaration80(self):
        return self.__graphbt_MethodDeclaration80

    @graphbt_MethodDeclaration80.setter
    def graphbt_MethodDeclaration80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphbt_MethodDeclaration__graphbt_MethodDeclaration80", None)
        self.__graphbt_MethodDeclaration80 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graphbt_Parameter"):
                    opp_val = getattr(item, "graphbt_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "graphbt_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graphbt_Parameter"):
                    opp_val = getattr(item, "graphbt_Parameter", None)
                    
                    setattr(item, "graphbt_Parameter", self)
                    

    @property
    def graphbt_MethodDeclaration(self):
        return self.__graphbt_MethodDeclaration

    @graphbt_MethodDeclaration.setter
    def graphbt_MethodDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphbt_MethodDeclaration__graphbt_MethodDeclaration", None)
        self.__graphbt_MethodDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphbt_Library48"):
                opp_val = getattr(old_value, "graphbt_Library48", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphbt_Library48"):
                opp_val = getattr(value, "graphbt_Library48", None)
                if opp_val is None:
                    setattr(value, "graphbt_Library48", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class graphbt_Requirement:

    def __init__(self, Key: str, Requirement: str, Description: str, Id: str, graphbt_Requirement: set["graphbt_StandardNode"] = None, graphbt_Requirement65: "graphbt_RequirementList" = None):
        self.Key = Key
        self.Requirement = Requirement
        self.Description = Description
        self.Id = Id
        self.graphbt_Requirement = graphbt_Requirement if graphbt_Requirement is not None else set()
        self.graphbt_Requirement65 = graphbt_Requirement65
        
    @property
    def Requirement(self) -> str:
        return self.__Requirement

    @Requirement.setter
    def Requirement(self, Requirement: str):
        self.__Requirement = Requirement

    @property
    def Description(self) -> str:
        return self.__Description

    @Description.setter
    def Description(self, Description: str):
        self.__Description = Description

    @property
    def Key(self) -> str:
        return self.__Key

    @Key.setter
    def Key(self, Key: str):
        self.__Key = Key

    @property
    def Id(self) -> str:
        return self.__Id

    @Id.setter
    def Id(self, Id: str):
        self.__Id = Id

    @property
    def graphbt_Requirement(self):
        return self.__graphbt_Requirement

    @graphbt_Requirement.setter
    def graphbt_Requirement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphbt_Requirement__graphbt_Requirement", None)
        self.__graphbt_Requirement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graphbt_StandardNode59"):
                    opp_val = getattr(item, "graphbt_StandardNode59", None)
                    
                    if opp_val == self:
                        setattr(item, "graphbt_StandardNode59", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graphbt_StandardNode59"):
                    opp_val = getattr(item, "graphbt_StandardNode59", None)
                    
                    setattr(item, "graphbt_StandardNode59", self)
                    

    @property
    def graphbt_Requirement65(self):
        return self.__graphbt_Requirement65

    @graphbt_Requirement65.setter
    def graphbt_Requirement65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphbt_Requirement__graphbt_Requirement65", None)
        self.__graphbt_Requirement65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphbt_RequirementList64"):
                opp_val = getattr(old_value, "graphbt_RequirementList64", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphbt_RequirementList64"):
                opp_val = getattr(value, "graphbt_RequirementList64", None)
                if opp_val is None:
                    setattr(value, "graphbt_RequirementList64", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class graphbt_Library:

    def __init__(self, name: str, text: str, desc: str, location: str, id: str, graphbt_Library: "graphbt_Component" = None, graphbt_Library56: set["graphbt_Attribute"] = None, graphbt_Library48: set["graphbt_MethodDeclaration"] = None, graphbt_Library50: set["graphbt_State"] = None, graphbt_Library53: set["graphbt_Behavior"] = None, graphbt_Library78: "graphbt_Libraries" = None):
        self.name = name
        self.text = text
        self.desc = desc
        self.location = location
        self.id = id
        self.graphbt_Library = graphbt_Library
        self.graphbt_Library56 = graphbt_Library56 if graphbt_Library56 is not None else set()
        self.graphbt_Library48 = graphbt_Library48 if graphbt_Library48 is not None else set()
        self.graphbt_Library50 = graphbt_Library50 if graphbt_Library50 is not None else set()
        self.graphbt_Library53 = graphbt_Library53 if graphbt_Library53 is not None else set()
        self.graphbt_Library78 = graphbt_Library78
        
    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def desc(self) -> str:
        return self.__desc

    @desc.setter
    def desc(self, desc: str):
        self.__desc = desc

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
    def graphbt_Library53(self):
        return self.__graphbt_Library53

    @graphbt_Library53.setter
    def graphbt_Library53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphbt_Library__graphbt_Library53", None)
        self.__graphbt_Library53 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graphbt_Behavior54"):
                    opp_val = getattr(item, "graphbt_Behavior54", None)
                    
                    if opp_val == self:
                        setattr(item, "graphbt_Behavior54", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graphbt_Behavior54"):
                    opp_val = getattr(item, "graphbt_Behavior54", None)
                    
                    setattr(item, "graphbt_Behavior54", self)
                    

    @property
    def graphbt_Library50(self):
        return self.__graphbt_Library50

    @graphbt_Library50.setter
    def graphbt_Library50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphbt_Library__graphbt_Library50", None)
        self.__graphbt_Library50 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graphbt_State51"):
                    opp_val = getattr(item, "graphbt_State51", None)
                    
                    if opp_val == self:
                        setattr(item, "graphbt_State51", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graphbt_State51"):
                    opp_val = getattr(item, "graphbt_State51", None)
                    
                    setattr(item, "graphbt_State51", self)
                    

    @property
    def graphbt_Library48(self):
        return self.__graphbt_Library48

    @graphbt_Library48.setter
    def graphbt_Library48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphbt_Library__graphbt_Library48", None)
        self.__graphbt_Library48 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graphbt_MethodDeclaration"):
                    opp_val = getattr(item, "graphbt_MethodDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "graphbt_MethodDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graphbt_MethodDeclaration"):
                    opp_val = getattr(item, "graphbt_MethodDeclaration", None)
                    
                    setattr(item, "graphbt_MethodDeclaration", self)
                    

    @property
    def graphbt_Library56(self):
        return self.__graphbt_Library56

    @graphbt_Library56.setter
    def graphbt_Library56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphbt_Library__graphbt_Library56", None)
        self.__graphbt_Library56 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graphbt_Attribute57"):
                    opp_val = getattr(item, "graphbt_Attribute57", None)
                    
                    if opp_val == self:
                        setattr(item, "graphbt_Attribute57", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graphbt_Attribute57"):
                    opp_val = getattr(item, "graphbt_Attribute57", None)
                    
                    setattr(item, "graphbt_Attribute57", self)
                    

    @property
    def graphbt_Library78(self):
        return self.__graphbt_Library78

    @graphbt_Library78.setter
    def graphbt_Library78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphbt_Library__graphbt_Library78", None)
        self.__graphbt_Library78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphbt_Libraries77"):
                opp_val = getattr(old_value, "graphbt_Libraries77", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphbt_Libraries77"):
                opp_val = getattr(value, "graphbt_Libraries77", None)
                if opp_val is None:
                    setattr(value, "graphbt_Libraries77", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graphbt_Library(self):
        return self.__graphbt_Library

    @graphbt_Library.setter
    def graphbt_Library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphbt_Library__graphbt_Library", None)
        self.__graphbt_Library = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphbt_Component44"):
                opp_val = getattr(old_value, "graphbt_Component44", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphbt_Component44"):
                opp_val = getattr(value, "graphbt_Component44", None)
                if opp_val is None:
                    setattr(value, "graphbt_Component44", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class graphbt_MapInformation:

    def __init__(self, graphbt_MapInformation: "graphbt_State" = None, graphbt_MapInformation75: set["graphbt_Information"] = None):
        self.graphbt_MapInformation = graphbt_MapInformation
        self.graphbt_MapInformation75 = graphbt_MapInformation75 if graphbt_MapInformation75 is not None else set()
        
    @property
    def graphbt_MapInformation(self):
        return self.__graphbt_MapInformation

    @graphbt_MapInformation.setter
    def graphbt_MapInformation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphbt_MapInformation__graphbt_MapInformation", None)
        self.__graphbt_MapInformation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphbt_State46"):
                opp_val = getattr(old_value, "graphbt_State46", None)
                if opp_val == self:
                    setattr(old_value, "graphbt_State46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphbt_State46"):
                opp_val = getattr(value, "graphbt_State46", None)
                setattr(value, "graphbt_State46", self)

    @property
    def graphbt_MapInformation75(self):
        return self.__graphbt_MapInformation75

    @graphbt_MapInformation75.setter
    def graphbt_MapInformation75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphbt_MapInformation__graphbt_MapInformation75", None)
        self.__graphbt_MapInformation75 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graphbt_Information"):
                    opp_val = getattr(item, "graphbt_Information", None)
                    
                    if opp_val == self:
                        setattr(item, "graphbt_Information", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graphbt_Information"):
                    opp_val = getattr(item, "graphbt_Information", None)
                    
                    setattr(item, "graphbt_Information", self)
                    

    def setValue(self, value: str, key: str):
        # TODO: Implement setValue method
        pass

    def getValue(self, key: str) -> str:
        # TODO: Implement getValue method
        pass

class graphbt_CTEdge:

    pass
class graphbt_Component:

    def __init__(self, componentName: str, id: int, componentRef: str, componentDesc: str, enumerated: bool, graphbt_Component: set["graphbt_Attribute"] = None, graphbt_Component34: set["graphbt_State"] = None, graphbt_Component36: "graphbt_State" = None, graphbt_Component40: "graphbt_Component" = None, graphbt_Component38: set["graphbt_Component"] = None, graphbt_Component42: set["graphbt_Behavior"] = None, graphbt_Component44: set["graphbt_Library"] = None, graphbt_Component62: "graphbt_ComponentList" = None):
        self.componentName = componentName
        self.id = id
        self.componentRef = componentRef
        self.componentDesc = componentDesc
        self.enumerated = enumerated
        self.graphbt_Component = graphbt_Component if graphbt_Component is not None else set()
        self.graphbt_Component34 = graphbt_Component34 if graphbt_Component34 is not None else set()
        self.graphbt_Component36 = graphbt_Component36
        self.graphbt_Component40 = graphbt_Component40
        self.graphbt_Component38 = graphbt_Component38 if graphbt_Component38 is not None else set()
        self.graphbt_Component42 = graphbt_Component42 if graphbt_Component42 is not None else set()
        self.graphbt_Component44 = graphbt_Component44 if graphbt_Component44 is not None else set()
        self.graphbt_Component62 = graphbt_Component62
        
    @property
    def componentRef(self) -> str:
        return self.__componentRef

    @componentRef.setter
    def componentRef(self, componentRef: str):
        self.__componentRef = componentRef

    @property
    def componentDesc(self) -> str:
        return self.__componentDesc

    @componentDesc.setter
    def componentDesc(self, componentDesc: str):
        self.__componentDesc = componentDesc

    @property
    def enumerated(self) -> bool:
        return self.__enumerated

    @enumerated.setter
    def enumerated(self, enumerated: bool):
        self.__enumerated = enumerated

    @property
    def componentName(self) -> str:
        return self.__componentName

    @componentName.setter
    def componentName(self, componentName: str):
        self.__componentName = componentName

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def graphbt_Component42(self):
        return self.__graphbt_Component42

    @graphbt_Component42.setter
    def graphbt_Component42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphbt_Component__graphbt_Component42", None)
        self.__graphbt_Component42 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graphbt_Behavior"):
                    opp_val = getattr(item, "graphbt_Behavior", None)
                    
                    if opp_val == self:
                        setattr(item, "graphbt_Behavior", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graphbt_Behavior"):
                    opp_val = getattr(item, "graphbt_Behavior", None)
                    
                    setattr(item, "graphbt_Behavior", self)
                    

    @property
    def graphbt_Component62(self):
        return self.__graphbt_Component62

    @graphbt_Component62.setter
    def graphbt_Component62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphbt_Component__graphbt_Component62", None)
        self.__graphbt_Component62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphbt_ComponentList61"):
                opp_val = getattr(old_value, "graphbt_ComponentList61", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphbt_ComponentList61"):
                opp_val = getattr(value, "graphbt_ComponentList61", None)
                if opp_val is None:
                    setattr(value, "graphbt_ComponentList61", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graphbt_Component38(self):
        return self.__graphbt_Component38

    @graphbt_Component38.setter
    def graphbt_Component38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphbt_Component__graphbt_Component38", None)
        self.__graphbt_Component38 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graphbt_Component40"):
                    opp_val = getattr(item, "graphbt_Component40", None)
                    
                    if opp_val == self:
                        setattr(item, "graphbt_Component40", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graphbt_Component40"):
                    opp_val = getattr(item, "graphbt_Component40", None)
                    
                    setattr(item, "graphbt_Component40", self)
                    

    @property
    def graphbt_Component40(self):
        return self.__graphbt_Component40

    @graphbt_Component40.setter
    def graphbt_Component40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphbt_Component__graphbt_Component40", None)
        self.__graphbt_Component40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphbt_Component38"):
                opp_val = getattr(old_value, "graphbt_Component38", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphbt_Component38"):
                opp_val = getattr(value, "graphbt_Component38", None)
                if opp_val is None:
                    setattr(value, "graphbt_Component38", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graphbt_Component36(self):
        return self.__graphbt_Component36

    @graphbt_Component36.setter
    def graphbt_Component36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphbt_Component__graphbt_Component36", None)
        self.__graphbt_Component36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphbt_State37"):
                opp_val = getattr(old_value, "graphbt_State37", None)
                if opp_val == self:
                    setattr(old_value, "graphbt_State37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphbt_State37"):
                opp_val = getattr(value, "graphbt_State37", None)
                setattr(value, "graphbt_State37", self)

    @property
    def graphbt_Component(self):
        return self.__graphbt_Component

    @graphbt_Component.setter
    def graphbt_Component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphbt_Component__graphbt_Component", None)
        self.__graphbt_Component = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graphbt_Attribute"):
                    opp_val = getattr(item, "graphbt_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "graphbt_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graphbt_Attribute"):
                    opp_val = getattr(item, "graphbt_Attribute", None)
                    
                    setattr(item, "graphbt_Attribute", self)
                    

    @property
    def graphbt_Component44(self):
        return self.__graphbt_Component44

    @graphbt_Component44.setter
    def graphbt_Component44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphbt_Component__graphbt_Component44", None)
        self.__graphbt_Component44 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graphbt_Library"):
                    opp_val = getattr(item, "graphbt_Library", None)
                    
                    if opp_val == self:
                        setattr(item, "graphbt_Library", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graphbt_Library"):
                    opp_val = getattr(item, "graphbt_Library", None)
                    
                    setattr(item, "graphbt_Library", self)
                    

    @property
    def graphbt_Component34(self):
        return self.__graphbt_Component34

    @graphbt_Component34.setter
    def graphbt_Component34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphbt_Component__graphbt_Component34", None)
        self.__graphbt_Component34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graphbt_State"):
                    opp_val = getattr(item, "graphbt_State", None)
                    
                    if opp_val == self:
                        setattr(item, "graphbt_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graphbt_State"):
                    opp_val = getattr(item, "graphbt_State", None)
                    
                    setattr(item, "graphbt_State", self)
                    

    def getAttribute(self, name: str) -> str:
        # TODO: Implement getAttribute method
        pass

class graphbt_Behavior:

    def __init__(self, behaviorType: str, behaviorName: str, behaviorRef: str, behaviorDesc: str, technicalDetail: str, graphbt_Behavior: "graphbt_Component" = None, graphbt_Behavior54: "graphbt_Library" = None):
        self.behaviorType = behaviorType
        self.behaviorName = behaviorName
        self.behaviorRef = behaviorRef
        self.behaviorDesc = behaviorDesc
        self.technicalDetail = technicalDetail
        self.graphbt_Behavior = graphbt_Behavior
        self.graphbt_Behavior54 = graphbt_Behavior54
        
    @property
    def behaviorDesc(self) -> str:
        return self.__behaviorDesc

    @behaviorDesc.setter
    def behaviorDesc(self, behaviorDesc: str):
        self.__behaviorDesc = behaviorDesc

    @property
    def behaviorRef(self) -> str:
        return self.__behaviorRef

    @behaviorRef.setter
    def behaviorRef(self, behaviorRef: str):
        self.__behaviorRef = behaviorRef

    @property
    def behaviorType(self) -> str:
        return self.__behaviorType

    @behaviorType.setter
    def behaviorType(self, behaviorType: str):
        self.__behaviorType = behaviorType

    @property
    def behaviorName(self) -> str:
        return self.__behaviorName

    @behaviorName.setter
    def behaviorName(self, behaviorName: str):
        self.__behaviorName = behaviorName

    @property
    def technicalDetail(self) -> str:
        return self.__technicalDetail

    @technicalDetail.setter
    def technicalDetail(self, technicalDetail: str):
        self.__technicalDetail = technicalDetail

    @property
    def graphbt_Behavior54(self):
        return self.__graphbt_Behavior54

    @graphbt_Behavior54.setter
    def graphbt_Behavior54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphbt_Behavior__graphbt_Behavior54", None)
        self.__graphbt_Behavior54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphbt_Library53"):
                opp_val = getattr(old_value, "graphbt_Library53", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphbt_Library53"):
                opp_val = getattr(value, "graphbt_Library53", None)
                if opp_val is None:
                    setattr(value, "graphbt_Library53", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graphbt_Behavior(self):
        return self.__graphbt_Behavior

    @graphbt_Behavior.setter
    def graphbt_Behavior(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphbt_Behavior__graphbt_Behavior", None)
        self.__graphbt_Behavior = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphbt_Component42"):
                opp_val = getattr(old_value, "graphbt_Component42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphbt_Component42"):
                opp_val = getattr(value, "graphbt_Component42", None)
                if opp_val is None:
                    setattr(value, "graphbt_Component42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class graphbt_State:

    def __init__(self, name: str, ref: str, desc: str, graphbt_State: "graphbt_Component" = None, graphbt_State37: "graphbt_Component" = None, graphbt_State46: "graphbt_MapInformation" = None, graphbt_State51: "graphbt_Library" = None):
        self.name = name
        self.ref = ref
        self.desc = desc
        self.graphbt_State = graphbt_State
        self.graphbt_State37 = graphbt_State37
        self.graphbt_State46 = graphbt_State46
        self.graphbt_State51 = graphbt_State51
        
    @property
    def desc(self) -> str:
        return self.__desc

    @desc.setter
    def desc(self, desc: str):
        self.__desc = desc

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ref(self) -> str:
        return self.__ref

    @ref.setter
    def ref(self, ref: str):
        self.__ref = ref

    @property
    def graphbt_State(self):
        return self.__graphbt_State

    @graphbt_State.setter
    def graphbt_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphbt_State__graphbt_State", None)
        self.__graphbt_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphbt_Component34"):
                opp_val = getattr(old_value, "graphbt_Component34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphbt_Component34"):
                opp_val = getattr(value, "graphbt_Component34", None)
                if opp_val is None:
                    setattr(value, "graphbt_Component34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graphbt_State37(self):
        return self.__graphbt_State37

    @graphbt_State37.setter
    def graphbt_State37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphbt_State__graphbt_State37", None)
        self.__graphbt_State37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphbt_Component36"):
                opp_val = getattr(old_value, "graphbt_Component36", None)
                if opp_val == self:
                    setattr(old_value, "graphbt_Component36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphbt_Component36"):
                opp_val = getattr(value, "graphbt_Component36", None)
                setattr(value, "graphbt_Component36", self)

    @property
    def graphbt_State51(self):
        return self.__graphbt_State51

    @graphbt_State51.setter
    def graphbt_State51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphbt_State__graphbt_State51", None)
        self.__graphbt_State51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphbt_Library50"):
                opp_val = getattr(old_value, "graphbt_Library50", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphbt_Library50"):
                opp_val = getattr(value, "graphbt_Library50", None)
                if opp_val is None:
                    setattr(value, "graphbt_Library50", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graphbt_State46(self):
        return self.__graphbt_State46

    @graphbt_State46.setter
    def graphbt_State46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphbt_State__graphbt_State46", None)
        self.__graphbt_State46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphbt_MapInformation"):
                opp_val = getattr(old_value, "graphbt_MapInformation", None)
                if opp_val == self:
                    setattr(old_value, "graphbt_MapInformation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphbt_MapInformation"):
                opp_val = getattr(value, "graphbt_MapInformation", None)
                setattr(value, "graphbt_MapInformation", self)

class graphbt_Attribute:

    def __init__(self, name: str, value: str, type: str, graphbt_Attribute: "graphbt_Component" = None, graphbt_Attribute57: "graphbt_Library" = None):
        self.name = name
        self.value = value
        self.type = type
        self.graphbt_Attribute = graphbt_Attribute
        self.graphbt_Attribute57 = graphbt_Attribute57
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def graphbt_Attribute57(self):
        return self.__graphbt_Attribute57

    @graphbt_Attribute57.setter
    def graphbt_Attribute57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphbt_Attribute__graphbt_Attribute57", None)
        self.__graphbt_Attribute57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphbt_Library56"):
                opp_val = getattr(old_value, "graphbt_Library56", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphbt_Library56"):
                opp_val = getattr(value, "graphbt_Library56", None)
                if opp_val is None:
                    setattr(value, "graphbt_Library56", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graphbt_Attribute(self):
        return self.__graphbt_Attribute

    @graphbt_Attribute.setter
    def graphbt_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphbt_Attribute__graphbt_Attribute", None)
        self.__graphbt_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphbt_Component"):
                opp_val = getattr(old_value, "graphbt_Component", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphbt_Component"):
                opp_val = getattr(value, "graphbt_Component", None)
                if opp_val is None:
                    setattr(value, "graphbt_Component", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Node:

    pass
class graphbt_EmptyNode(Node):

    def __init__(self, label: str):
        self.label = label
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

class graphbt_Link:

    pass
class graphbt_AuthorList:

    pass
class graphbt_LayoutList:

    pass
class graphbt_SpecialEdge:

    def __init__(self, type: str, destination: int, graphbt_SpecialEdge: "graphbt_Node" = None):
        self.type = type
        self.destination = destination
        self.graphbt_SpecialEdge = graphbt_SpecialEdge
        
    @property
    def destination(self) -> int:
        return self.__destination

    @destination.setter
    def destination(self, destination: int):
        self.__destination = destination

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def graphbt_SpecialEdge(self):
        return self.__graphbt_SpecialEdge

    @graphbt_SpecialEdge.setter
    def graphbt_SpecialEdge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphbt_SpecialEdge__graphbt_SpecialEdge", None)
        self.__graphbt_SpecialEdge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphbt_Node23"):
                opp_val = getattr(old_value, "graphbt_Node23", None)
                if opp_val == self:
                    setattr(old_value, "graphbt_Node23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphbt_Node23"):
                opp_val = getattr(value, "graphbt_Node23", None)
                setattr(value, "graphbt_Node23", self)

class graphbt_Edge:

    def __init__(self, branch: str, composition: str, graphbt_Edge: "graphbt_Node" = None, graphbt_Edge25: set["graphbt_Link"] = None, graphbt_Edge27: "graphbt_Node" = None):
        self.branch = branch
        self.composition = composition
        self.graphbt_Edge = graphbt_Edge
        self.graphbt_Edge25 = graphbt_Edge25 if graphbt_Edge25 is not None else set()
        self.graphbt_Edge27 = graphbt_Edge27
        
    @property
    def branch(self) -> str:
        return self.__branch

    @branch.setter
    def branch(self, branch: str):
        self.__branch = branch

    @property
    def composition(self) -> str:
        return self.__composition

    @composition.setter
    def composition(self, composition: str):
        self.__composition = composition

    @property
    def graphbt_Edge(self):
        return self.__graphbt_Edge

    @graphbt_Edge.setter
    def graphbt_Edge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphbt_Edge__graphbt_Edge", None)
        self.__graphbt_Edge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphbt_Node21"):
                opp_val = getattr(old_value, "graphbt_Node21", None)
                if opp_val == self:
                    setattr(old_value, "graphbt_Node21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphbt_Node21"):
                opp_val = getattr(value, "graphbt_Node21", None)
                setattr(value, "graphbt_Node21", self)

    @property
    def graphbt_Edge27(self):
        return self.__graphbt_Edge27

    @graphbt_Edge27.setter
    def graphbt_Edge27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphbt_Edge__graphbt_Edge27", None)
        self.__graphbt_Edge27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphbt_Node28"):
                opp_val = getattr(old_value, "graphbt_Node28", None)
                if opp_val == self:
                    setattr(old_value, "graphbt_Node28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphbt_Node28"):
                opp_val = getattr(value, "graphbt_Node28", None)
                setattr(value, "graphbt_Node28", self)

    @property
    def graphbt_Edge25(self):
        return self.__graphbt_Edge25

    @graphbt_Edge25.setter
    def graphbt_Edge25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphbt_Edge__graphbt_Edge25", None)
        self.__graphbt_Edge25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graphbt_Link"):
                    opp_val = getattr(item, "graphbt_Link", None)
                    
                    if opp_val == self:
                        setattr(item, "graphbt_Link", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graphbt_Link"):
                    opp_val = getattr(item, "graphbt_Link", None)
                    
                    setattr(item, "graphbt_Link", self)
                    

class graphbt_Node:

    def __init__(self, index: int, id: str, graphbt_Node: "graphbt_BehaviorTree" = None, graphbt_Node21: "graphbt_Edge" = None, graphbt_Node23: "graphbt_SpecialEdge" = None, graphbt_Node28: "graphbt_Edge" = None, graphbt_Node70: "graphbt_Link" = None, graphbt_Node73: "graphbt_Link" = None):
        self.index = index
        self.id = id
        self.graphbt_Node = graphbt_Node
        self.graphbt_Node21 = graphbt_Node21
        self.graphbt_Node23 = graphbt_Node23
        self.graphbt_Node28 = graphbt_Node28
        self.graphbt_Node70 = graphbt_Node70
        self.graphbt_Node73 = graphbt_Node73
        
    @property
    def index(self) -> int:
        return self.__index

    @index.setter
    def index(self, index: int):
        self.__index = index

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def graphbt_Node73(self):
        return self.__graphbt_Node73

    @graphbt_Node73.setter
    def graphbt_Node73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphbt_Node__graphbt_Node73", None)
        self.__graphbt_Node73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphbt_Link72"):
                opp_val = getattr(old_value, "graphbt_Link72", None)
                if opp_val == self:
                    setattr(old_value, "graphbt_Link72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphbt_Link72"):
                opp_val = getattr(value, "graphbt_Link72", None)
                setattr(value, "graphbt_Link72", self)

    @property
    def graphbt_Node(self):
        return self.__graphbt_Node

    @graphbt_Node.setter
    def graphbt_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphbt_Node__graphbt_Node", None)
        self.__graphbt_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphbt_BehaviorTree19"):
                opp_val = getattr(old_value, "graphbt_BehaviorTree19", None)
                if opp_val == self:
                    setattr(old_value, "graphbt_BehaviorTree19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphbt_BehaviorTree19"):
                opp_val = getattr(value, "graphbt_BehaviorTree19", None)
                setattr(value, "graphbt_BehaviorTree19", self)

    @property
    def graphbt_Node23(self):
        return self.__graphbt_Node23

    @graphbt_Node23.setter
    def graphbt_Node23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphbt_Node__graphbt_Node23", None)
        self.__graphbt_Node23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphbt_SpecialEdge"):
                opp_val = getattr(old_value, "graphbt_SpecialEdge", None)
                if opp_val == self:
                    setattr(old_value, "graphbt_SpecialEdge", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphbt_SpecialEdge"):
                opp_val = getattr(value, "graphbt_SpecialEdge", None)
                setattr(value, "graphbt_SpecialEdge", self)

    @property
    def graphbt_Node21(self):
        return self.__graphbt_Node21

    @graphbt_Node21.setter
    def graphbt_Node21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphbt_Node__graphbt_Node21", None)
        self.__graphbt_Node21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphbt_Edge"):
                opp_val = getattr(old_value, "graphbt_Edge", None)
                if opp_val == self:
                    setattr(old_value, "graphbt_Edge", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphbt_Edge"):
                opp_val = getattr(value, "graphbt_Edge", None)
                setattr(value, "graphbt_Edge", self)

    @property
    def graphbt_Node70(self):
        return self.__graphbt_Node70

    @graphbt_Node70.setter
    def graphbt_Node70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphbt_Node__graphbt_Node70", None)
        self.__graphbt_Node70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphbt_Link69"):
                opp_val = getattr(old_value, "graphbt_Link69", None)
                if opp_val == self:
                    setattr(old_value, "graphbt_Link69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphbt_Link69"):
                opp_val = getattr(value, "graphbt_Link69", None)
                setattr(value, "graphbt_Link69", self)

    @property
    def graphbt_Node28(self):
        return self.__graphbt_Node28

    @graphbt_Node28.setter
    def graphbt_Node28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphbt_Node__graphbt_Node28", None)
        self.__graphbt_Node28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphbt_Edge27"):
                opp_val = getattr(old_value, "graphbt_Edge27", None)
                if opp_val == self:
                    setattr(old_value, "graphbt_Edge27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphbt_Edge27"):
                opp_val = getattr(value, "graphbt_Edge27", None)
                setattr(value, "graphbt_Edge27", self)

class graphbt_BehaviorTree:

    def __init__(self, name: str, graphbt_BehaviorTree: "graphbt_BEModel" = None, graphbt_BehaviorTree19: "graphbt_Node" = None):
        self.name = name
        self.graphbt_BehaviorTree = graphbt_BehaviorTree
        self.graphbt_BehaviorTree19 = graphbt_BehaviorTree19
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def graphbt_BehaviorTree(self):
        return self.__graphbt_BehaviorTree

    @graphbt_BehaviorTree.setter
    def graphbt_BehaviorTree(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphbt_BehaviorTree__graphbt_BehaviorTree", None)
        self.__graphbt_BehaviorTree = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphbt_BEModel"):
                opp_val = getattr(old_value, "graphbt_BEModel", None)
                if opp_val == self:
                    setattr(old_value, "graphbt_BEModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphbt_BEModel"):
                opp_val = getattr(value, "graphbt_BEModel", None)
                setattr(value, "graphbt_BEModel", self)

    @property
    def graphbt_BehaviorTree19(self):
        return self.__graphbt_BehaviorTree19

    @graphbt_BehaviorTree19.setter
    def graphbt_BehaviorTree19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphbt_BehaviorTree__graphbt_BehaviorTree19", None)
        self.__graphbt_BehaviorTree19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphbt_Node"):
                opp_val = getattr(old_value, "graphbt_Node", None)
                if opp_val == self:
                    setattr(old_value, "graphbt_Node", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphbt_Node"):
                opp_val = getattr(value, "graphbt_Node", None)
                setattr(value, "graphbt_Node", self)

class graphbt_BEModel:

    def __init__(self, name: str, subtitle: str, version: str, graphbt_BEModel2: "graphbt_ComponentList" = None, graphbt_BEModel4: "graphbt_RequirementList" = None, graphbt_BEModel6: "graphbt_FormulaList" = None, graphbt_BEModel8: "graphbt_Libraries" = None, graphbt_BEModel10: set["graphbt_StandardNode"] = None, graphbt_BEModel12: set["graphbt_StandardNode"] = None, graphbt_BEModel: "graphbt_BehaviorTree" = None, graphbt_BEModel15: "graphbt_LayoutList" = None, graphbt_BEModel17: "graphbt_AuthorList" = None):
        self.name = name
        self.subtitle = subtitle
        self.version = version
        self.graphbt_BEModel2 = graphbt_BEModel2
        self.graphbt_BEModel4 = graphbt_BEModel4
        self.graphbt_BEModel6 = graphbt_BEModel6
        self.graphbt_BEModel8 = graphbt_BEModel8
        self.graphbt_BEModel10 = graphbt_BEModel10 if graphbt_BEModel10 is not None else set()
        self.graphbt_BEModel12 = graphbt_BEModel12 if graphbt_BEModel12 is not None else set()
        self.graphbt_BEModel = graphbt_BEModel
        self.graphbt_BEModel15 = graphbt_BEModel15
        self.graphbt_BEModel17 = graphbt_BEModel17
        
    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def subtitle(self) -> str:
        return self.__subtitle

    @subtitle.setter
    def subtitle(self, subtitle: str):
        self.__subtitle = subtitle

    @property
    def graphbt_BEModel4(self):
        return self.__graphbt_BEModel4

    @graphbt_BEModel4.setter
    def graphbt_BEModel4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphbt_BEModel__graphbt_BEModel4", None)
        self.__graphbt_BEModel4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphbt_RequirementList"):
                opp_val = getattr(old_value, "graphbt_RequirementList", None)
                if opp_val == self:
                    setattr(old_value, "graphbt_RequirementList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphbt_RequirementList"):
                opp_val = getattr(value, "graphbt_RequirementList", None)
                setattr(value, "graphbt_RequirementList", self)

    @property
    def graphbt_BEModel(self):
        return self.__graphbt_BEModel

    @graphbt_BEModel.setter
    def graphbt_BEModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphbt_BEModel__graphbt_BEModel", None)
        self.__graphbt_BEModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphbt_BehaviorTree"):
                opp_val = getattr(old_value, "graphbt_BehaviorTree", None)
                if opp_val == self:
                    setattr(old_value, "graphbt_BehaviorTree", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphbt_BehaviorTree"):
                opp_val = getattr(value, "graphbt_BehaviorTree", None)
                setattr(value, "graphbt_BehaviorTree", self)

    @property
    def graphbt_BEModel8(self):
        return self.__graphbt_BEModel8

    @graphbt_BEModel8.setter
    def graphbt_BEModel8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphbt_BEModel__graphbt_BEModel8", None)
        self.__graphbt_BEModel8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphbt_Libraries"):
                opp_val = getattr(old_value, "graphbt_Libraries", None)
                if opp_val == self:
                    setattr(old_value, "graphbt_Libraries", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphbt_Libraries"):
                opp_val = getattr(value, "graphbt_Libraries", None)
                setattr(value, "graphbt_Libraries", self)

    @property
    def graphbt_BEModel6(self):
        return self.__graphbt_BEModel6

    @graphbt_BEModel6.setter
    def graphbt_BEModel6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphbt_BEModel__graphbt_BEModel6", None)
        self.__graphbt_BEModel6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphbt_FormulaList"):
                opp_val = getattr(old_value, "graphbt_FormulaList", None)
                if opp_val == self:
                    setattr(old_value, "graphbt_FormulaList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphbt_FormulaList"):
                opp_val = getattr(value, "graphbt_FormulaList", None)
                setattr(value, "graphbt_FormulaList", self)

    @property
    def graphbt_BEModel10(self):
        return self.__graphbt_BEModel10

    @graphbt_BEModel10.setter
    def graphbt_BEModel10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphbt_BEModel__graphbt_BEModel10", None)
        self.__graphbt_BEModel10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graphbt_StandardNode"):
                    opp_val = getattr(item, "graphbt_StandardNode", None)
                    
                    if opp_val == self:
                        setattr(item, "graphbt_StandardNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graphbt_StandardNode"):
                    opp_val = getattr(item, "graphbt_StandardNode", None)
                    
                    setattr(item, "graphbt_StandardNode", self)
                    

    @property
    def graphbt_BEModel2(self):
        return self.__graphbt_BEModel2

    @graphbt_BEModel2.setter
    def graphbt_BEModel2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphbt_BEModel__graphbt_BEModel2", None)
        self.__graphbt_BEModel2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphbt_ComponentList"):
                opp_val = getattr(old_value, "graphbt_ComponentList", None)
                if opp_val == self:
                    setattr(old_value, "graphbt_ComponentList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphbt_ComponentList"):
                opp_val = getattr(value, "graphbt_ComponentList", None)
                setattr(value, "graphbt_ComponentList", self)

    @property
    def graphbt_BEModel12(self):
        return self.__graphbt_BEModel12

    @graphbt_BEModel12.setter
    def graphbt_BEModel12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphbt_BEModel__graphbt_BEModel12", None)
        self.__graphbt_BEModel12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graphbt_StandardNode13"):
                    opp_val = getattr(item, "graphbt_StandardNode13", None)
                    
                    if opp_val == self:
                        setattr(item, "graphbt_StandardNode13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graphbt_StandardNode13"):
                    opp_val = getattr(item, "graphbt_StandardNode13", None)
                    
                    setattr(item, "graphbt_StandardNode13", self)
                    

    @property
    def graphbt_BEModel15(self):
        return self.__graphbt_BEModel15

    @graphbt_BEModel15.setter
    def graphbt_BEModel15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphbt_BEModel__graphbt_BEModel15", None)
        self.__graphbt_BEModel15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphbt_LayoutList"):
                opp_val = getattr(old_value, "graphbt_LayoutList", None)
                if opp_val == self:
                    setattr(old_value, "graphbt_LayoutList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphbt_LayoutList"):
                opp_val = getattr(value, "graphbt_LayoutList", None)
                setattr(value, "graphbt_LayoutList", self)

    @property
    def graphbt_BEModel17(self):
        return self.__graphbt_BEModel17

    @graphbt_BEModel17.setter
    def graphbt_BEModel17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphbt_BEModel__graphbt_BEModel17", None)
        self.__graphbt_BEModel17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphbt_AuthorList"):
                opp_val = getattr(old_value, "graphbt_AuthorList", None)
                if opp_val == self:
                    setattr(old_value, "graphbt_AuthorList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphbt_AuthorList"):
                opp_val = getattr(value, "graphbt_AuthorList", None)
                setattr(value, "graphbt_AuthorList", self)

class graphbt_StandardNode(Node):

    def __init__(self, traceabilityStatus: str, operator: str, label: str, componentRef: str, behaviorRef: str, traceabilityLink: str, leaf: bool, graphbt_StandardNode: "graphbt_BEModel" = None, graphbt_StandardNode13: "graphbt_BEModel" = None, graphbt_StandardNode31: "graphbt_StandardNode" = None, graphbt_StandardNode29: "graphbt_StandardNode" = None, graphbt_StandardNode59: "graphbt_Requirement" = None):
        self.traceabilityStatus = traceabilityStatus
        self.operator = operator
        self.label = label
        self.componentRef = componentRef
        self.behaviorRef = behaviorRef
        self.traceabilityLink = traceabilityLink
        self.leaf = leaf
        self.graphbt_StandardNode = graphbt_StandardNode
        self.graphbt_StandardNode13 = graphbt_StandardNode13
        self.graphbt_StandardNode31 = graphbt_StandardNode31
        self.graphbt_StandardNode29 = graphbt_StandardNode29
        self.graphbt_StandardNode59 = graphbt_StandardNode59
        
    @property
    def componentRef(self) -> str:
        return self.__componentRef

    @componentRef.setter
    def componentRef(self, componentRef: str):
        self.__componentRef = componentRef

    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def leaf(self) -> bool:
        return self.__leaf

    @leaf.setter
    def leaf(self, leaf: bool):
        self.__leaf = leaf

    @property
    def behaviorRef(self) -> str:
        return self.__behaviorRef

    @behaviorRef.setter
    def behaviorRef(self, behaviorRef: str):
        self.__behaviorRef = behaviorRef

    @property
    def traceabilityStatus(self) -> str:
        return self.__traceabilityStatus

    @traceabilityStatus.setter
    def traceabilityStatus(self, traceabilityStatus: str):
        self.__traceabilityStatus = traceabilityStatus

    @property
    def traceabilityLink(self) -> str:
        return self.__traceabilityLink

    @traceabilityLink.setter
    def traceabilityLink(self, traceabilityLink: str):
        self.__traceabilityLink = traceabilityLink

    @property
    def graphbt_StandardNode31(self):
        return self.__graphbt_StandardNode31

    @graphbt_StandardNode31.setter
    def graphbt_StandardNode31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphbt_StandardNode__graphbt_StandardNode31", None)
        self.__graphbt_StandardNode31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphbt_StandardNode29"):
                opp_val = getattr(old_value, "graphbt_StandardNode29", None)
                if opp_val == self:
                    setattr(old_value, "graphbt_StandardNode29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphbt_StandardNode29"):
                opp_val = getattr(value, "graphbt_StandardNode29", None)
                setattr(value, "graphbt_StandardNode29", self)

    @property
    def graphbt_StandardNode(self):
        return self.__graphbt_StandardNode

    @graphbt_StandardNode.setter
    def graphbt_StandardNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphbt_StandardNode__graphbt_StandardNode", None)
        self.__graphbt_StandardNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphbt_BEModel10"):
                opp_val = getattr(old_value, "graphbt_BEModel10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphbt_BEModel10"):
                opp_val = getattr(value, "graphbt_BEModel10", None)
                if opp_val is None:
                    setattr(value, "graphbt_BEModel10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graphbt_StandardNode29(self):
        return self.__graphbt_StandardNode29

    @graphbt_StandardNode29.setter
    def graphbt_StandardNode29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphbt_StandardNode__graphbt_StandardNode29", None)
        self.__graphbt_StandardNode29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphbt_StandardNode31"):
                opp_val = getattr(old_value, "graphbt_StandardNode31", None)
                if opp_val == self:
                    setattr(old_value, "graphbt_StandardNode31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphbt_StandardNode31"):
                opp_val = getattr(value, "graphbt_StandardNode31", None)
                setattr(value, "graphbt_StandardNode31", self)

    @property
    def graphbt_StandardNode59(self):
        return self.__graphbt_StandardNode59

    @graphbt_StandardNode59.setter
    def graphbt_StandardNode59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphbt_StandardNode__graphbt_StandardNode59", None)
        self.__graphbt_StandardNode59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphbt_Requirement"):
                opp_val = getattr(old_value, "graphbt_Requirement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphbt_Requirement"):
                opp_val = getattr(value, "graphbt_Requirement", None)
                if opp_val is None:
                    setattr(value, "graphbt_Requirement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graphbt_StandardNode13(self):
        return self.__graphbt_StandardNode13

    @graphbt_StandardNode13.setter
    def graphbt_StandardNode13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphbt_StandardNode__graphbt_StandardNode13", None)
        self.__graphbt_StandardNode13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphbt_BEModel12"):
                opp_val = getattr(old_value, "graphbt_BEModel12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphbt_BEModel12"):
                opp_val = getattr(value, "graphbt_BEModel12", None)
                if opp_val is None:
                    setattr(value, "graphbt_BEModel12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class graphbt_Libraries:

    pass
class graphbt_FormulaList:

    pass
class graphbt_RequirementList:

    def __init__(self, projectId: str, graphbt_RequirementList: "graphbt_BEModel" = None, graphbt_RequirementList64: set["graphbt_Requirement"] = None):
        self.projectId = projectId
        self.graphbt_RequirementList = graphbt_RequirementList
        self.graphbt_RequirementList64 = graphbt_RequirementList64 if graphbt_RequirementList64 is not None else set()
        
    @property
    def projectId(self) -> str:
        return self.__projectId

    @projectId.setter
    def projectId(self, projectId: str):
        self.__projectId = projectId

    @property
    def graphbt_RequirementList64(self):
        return self.__graphbt_RequirementList64

    @graphbt_RequirementList64.setter
    def graphbt_RequirementList64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphbt_RequirementList__graphbt_RequirementList64", None)
        self.__graphbt_RequirementList64 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graphbt_Requirement65"):
                    opp_val = getattr(item, "graphbt_Requirement65", None)
                    
                    if opp_val == self:
                        setattr(item, "graphbt_Requirement65", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graphbt_Requirement65"):
                    opp_val = getattr(item, "graphbt_Requirement65", None)
                    
                    setattr(item, "graphbt_Requirement65", self)
                    

    @property
    def graphbt_RequirementList(self):
        return self.__graphbt_RequirementList

    @graphbt_RequirementList.setter
    def graphbt_RequirementList(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphbt_RequirementList__graphbt_RequirementList", None)
        self.__graphbt_RequirementList = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphbt_BEModel4"):
                opp_val = getattr(old_value, "graphbt_BEModel4", None)
                if opp_val == self:
                    setattr(old_value, "graphbt_BEModel4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphbt_BEModel4"):
                opp_val = getattr(value, "graphbt_BEModel4", None)
                setattr(value, "graphbt_BEModel4", self)

class graphbt_ComponentList:

    pass