from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class BooleanOperator(Enum):
    and = "and"
    or = "or"
    less_than = "less_than"
    greater_than = "greater_than"
    less_than_equal = "less_than_equal"
    greater_than_equal = "greater_than_equal"
    equivalent = "equivalent"
    not_equivalent = "not_equivalent"
class Operator(Enum):
    add = "add"
    subtract = "subtract"
    assign = "assign"
    bitwise_or = "bitwise_or"
    bitwise_and = "bitwise_and"
    assign_add = "assign_add"
class CVQualifier(Enum):
    const = "const"
    volatile = "volatile"
    unqualified = "unqualified"
class PrimitiveType(Enum):
    int8 = "int8"
    int16 = "int16"
    int32 = "int32"
    uint8 = "uint8"
    uint16 = "uint16"
    uint32 = "uint32"
    char = "char"
    float = "float"
    double = "double"
    void = "void"
    long = "long"
class LinkageSpec(Enum):
    unspecified = "unspecified"
    extern = "extern"
    static = "static"
class ElementKind(Enum):
    default = "default"
    headerOnly = "headerOnly"
    implOnly = "implOnly"
class Pointer(Enum):
    pointer = "pointer"
    const_pointer = "const_pointer"
    invalid = "invalid"
    volatile_pointer = "volatile_pointer"
    const_volatile_pointer = "const_volatile_pointer"


############################################
# Definition of Classes
############################################

class langc_LinkableArtifact:

    def __init__(self, name: str, langc_LinkableArtifact: "langc_System" = None, langc_LinkableArtifact149: set["langc_FunctionImplementation"] = None, langc_LinkableArtifact152: set["langc_UserElement"] = None):
        self.name = name
        self.langc_LinkableArtifact = langc_LinkableArtifact
        self.langc_LinkableArtifact149 = langc_LinkableArtifact149 if langc_LinkableArtifact149 is not None else set()
        self.langc_LinkableArtifact152 = langc_LinkableArtifact152 if langc_LinkableArtifact152 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def langc_LinkableArtifact152(self):
        return self.__langc_LinkableArtifact152

    @langc_LinkableArtifact152.setter
    def langc_LinkableArtifact152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_LinkableArtifact__langc_LinkableArtifact152", None)
        self.__langc_LinkableArtifact152 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "langc_UserElement153"):
                    opp_val = getattr(item, "langc_UserElement153", None)
                    
                    if opp_val == self:
                        setattr(item, "langc_UserElement153", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "langc_UserElement153"):
                    opp_val = getattr(item, "langc_UserElement153", None)
                    
                    setattr(item, "langc_UserElement153", self)
                    

    @property
    def langc_LinkableArtifact(self):
        return self.__langc_LinkableArtifact

    @langc_LinkableArtifact.setter
    def langc_LinkableArtifact(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_LinkableArtifact__langc_LinkableArtifact", None)
        self.__langc_LinkableArtifact = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_System146"):
                opp_val = getattr(old_value, "langc_System146", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_System146"):
                opp_val = getattr(value, "langc_System146", None)
                if opp_val is None:
                    setattr(value, "langc_System146", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def langc_LinkableArtifact149(self):
        return self.__langc_LinkableArtifact149

    @langc_LinkableArtifact149.setter
    def langc_LinkableArtifact149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_LinkableArtifact__langc_LinkableArtifact149", None)
        self.__langc_LinkableArtifact149 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "langc_FunctionImplementation150"):
                    opp_val = getattr(item, "langc_FunctionImplementation150", None)
                    
                    if opp_val == self:
                        setattr(item, "langc_FunctionImplementation150", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "langc_FunctionImplementation150"):
                    opp_val = getattr(item, "langc_FunctionImplementation150", None)
                    
                    setattr(item, "langc_FunctionImplementation150", self)
                    

class langc_System:

    pass
class langc_BindableValue(ABC):

    pass
class Sizeof:

    pass
class langc_SizeofExpr(Sizeof):

    pass
class langc_SizeofType(Sizeof):

    pass
class Directive:

    pass
class SwitchClause:

    pass
class langc_LabeledClause(SwitchClause):

    pass
class CodeBlock:

    pass
class langc_CodeBlob(CodeBlock):

    def __init__(self, markerComment: str, text: str, langc_CodeBlob: "langc_DependencyBlob" = None):
        self.markerComment = markerComment
        self.text = text
        self.langc_CodeBlob = langc_CodeBlob
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def markerComment(self) -> str:
        return self.__markerComment

    @markerComment.setter
    def markerComment(self, markerComment: str):
        self.__markerComment = markerComment

    @property
    def langc_CodeBlob(self):
        return self.__langc_CodeBlob

    @langc_CodeBlob.setter
    def langc_CodeBlob(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_CodeBlob__langc_CodeBlob", None)
        self.__langc_CodeBlob = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_DependencyBlob"):
                opp_val = getattr(old_value, "langc_DependencyBlob", None)
                if opp_val == self:
                    setattr(old_value, "langc_DependencyBlob", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_DependencyBlob"):
                opp_val = getattr(value, "langc_DependencyBlob", None)
                setattr(value, "langc_DependencyBlob", self)

class langc_WhileStatement(CodeBlock):

    pass
class langc_ConditionalStatement(CodeBlock):

    pass
class langc_SwitchClause(CodeBlock):

    def __init__(self, fallthrough: bool, langc_SwitchClause: "langc_SwitchStatement" = None):
        self.fallthrough = fallthrough
        self.langc_SwitchClause = langc_SwitchClause
        
    @property
    def fallthrough(self) -> bool:
        return self.__fallthrough

    @fallthrough.setter
    def fallthrough(self, fallthrough: bool):
        self.__fallthrough = fallthrough

    @property
    def langc_SwitchClause(self):
        return self.__langc_SwitchClause

    @langc_SwitchClause.setter
    def langc_SwitchClause(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_SwitchClause__langc_SwitchClause", None)
        self.__langc_SwitchClause = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_SwitchStatement"):
                opp_val = getattr(old_value, "langc_SwitchStatement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_SwitchStatement"):
                opp_val = getattr(value, "langc_SwitchStatement", None)
                if opp_val is None:
                    setattr(value, "langc_SwitchStatement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class FileName:

    pass
class langc_SystemFileName(FileName):

    pass
class langc_SubSystem:

    def __init__(self, name: str, langc_SubSystem: set["langc_ElementList"] = None, langc_SubSystem74: set["langc_FolderName"] = None, langc_SubSystem76: set["langc_FolderName"] = None, langc_SubSystem141: "langc_System" = None):
        self.name = name
        self.langc_SubSystem = langc_SubSystem if langc_SubSystem is not None else set()
        self.langc_SubSystem74 = langc_SubSystem74 if langc_SubSystem74 is not None else set()
        self.langc_SubSystem76 = langc_SubSystem76 if langc_SubSystem76 is not None else set()
        self.langc_SubSystem141 = langc_SubSystem141
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def langc_SubSystem(self):
        return self.__langc_SubSystem

    @langc_SubSystem.setter
    def langc_SubSystem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_SubSystem__langc_SubSystem", None)
        self.__langc_SubSystem = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "langc_ElementList72"):
                    opp_val = getattr(item, "langc_ElementList72", None)
                    
                    if opp_val == self:
                        setattr(item, "langc_ElementList72", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "langc_ElementList72"):
                    opp_val = getattr(item, "langc_ElementList72", None)
                    
                    setattr(item, "langc_ElementList72", self)
                    

    @property
    def langc_SubSystem76(self):
        return self.__langc_SubSystem76

    @langc_SubSystem76.setter
    def langc_SubSystem76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_SubSystem__langc_SubSystem76", None)
        self.__langc_SubSystem76 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "langc_FolderName77"):
                    opp_val = getattr(item, "langc_FolderName77", None)
                    
                    if opp_val == self:
                        setattr(item, "langc_FolderName77", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "langc_FolderName77"):
                    opp_val = getattr(item, "langc_FolderName77", None)
                    
                    setattr(item, "langc_FolderName77", self)
                    

    @property
    def langc_SubSystem141(self):
        return self.__langc_SubSystem141

    @langc_SubSystem141.setter
    def langc_SubSystem141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_SubSystem__langc_SubSystem141", None)
        self.__langc_SubSystem141 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_System"):
                opp_val = getattr(old_value, "langc_System", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_System"):
                opp_val = getattr(value, "langc_System", None)
                if opp_val is None:
                    setattr(value, "langc_System", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def langc_SubSystem74(self):
        return self.__langc_SubSystem74

    @langc_SubSystem74.setter
    def langc_SubSystem74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_SubSystem__langc_SubSystem74", None)
        self.__langc_SubSystem74 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "langc_FolderName"):
                    opp_val = getattr(item, "langc_FolderName", None)
                    
                    if opp_val == self:
                        setattr(item, "langc_FolderName", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "langc_FolderName"):
                    opp_val = getattr(item, "langc_FolderName", None)
                    
                    setattr(item, "langc_FolderName", self)
                    

class langc_Dependency(ABC):

    pass
class Name:

    pass
class FileDependency:

    pass
class langc_UserInclude(FileDependency):

    pass
class langc_SystemInclude(FileDependency):

    pass
class Dependency:

    pass
class langc_DependencyBlob(Dependency):

    def __init__(self, text: str, markerComment: str, langc_DependencyBlob: "langc_CodeBlob" = None):
        self.text = text
        self.markerComment = markerComment
        self.langc_DependencyBlob = langc_DependencyBlob
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def markerComment(self) -> str:
        return self.__markerComment

    @markerComment.setter
    def markerComment(self, markerComment: str):
        self.__markerComment = markerComment

    @property
    def langc_DependencyBlob(self):
        return self.__langc_DependencyBlob

    @langc_DependencyBlob.setter
    def langc_DependencyBlob(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_DependencyBlob__langc_DependencyBlob", None)
        self.__langc_DependencyBlob = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_CodeBlob"):
                opp_val = getattr(old_value, "langc_CodeBlob", None)
                if opp_val == self:
                    setattr(old_value, "langc_CodeBlob", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_CodeBlob"):
                opp_val = getattr(value, "langc_CodeBlob", None)
                setattr(value, "langc_CodeBlob", self)

class langc_FileDependency(Dependency):

    pass
class langc_FolderName(Name):

    def __init__(self, api: bool, langc_FolderName: "langc_SubSystem" = None, langc_FolderName77: "langc_SubSystem" = None, langc_FolderName144: "langc_System" = None):
        self.api = api
        self.langc_FolderName = langc_FolderName
        self.langc_FolderName77 = langc_FolderName77
        self.langc_FolderName144 = langc_FolderName144
        
    @property
    def api(self) -> bool:
        return self.__api

    @api.setter
    def api(self, api: bool):
        self.__api = api

    @property
    def langc_FolderName144(self):
        return self.__langc_FolderName144

    @langc_FolderName144.setter
    def langc_FolderName144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_FolderName__langc_FolderName144", None)
        self.__langc_FolderName144 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_System143"):
                opp_val = getattr(old_value, "langc_System143", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_System143"):
                opp_val = getattr(value, "langc_System143", None)
                if opp_val is None:
                    setattr(value, "langc_System143", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def langc_FolderName77(self):
        return self.__langc_FolderName77

    @langc_FolderName77.setter
    def langc_FolderName77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_FolderName__langc_FolderName77", None)
        self.__langc_FolderName77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_SubSystem76"):
                opp_val = getattr(old_value, "langc_SubSystem76", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_SubSystem76"):
                opp_val = getattr(value, "langc_SubSystem76", None)
                if opp_val is None:
                    setattr(value, "langc_SubSystem76", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def langc_FolderName(self):
        return self.__langc_FolderName

    @langc_FolderName.setter
    def langc_FolderName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_FolderName__langc_FolderName", None)
        self.__langc_FolderName = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_SubSystem74"):
                opp_val = getattr(old_value, "langc_SubSystem74", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_SubSystem74"):
                opp_val = getattr(value, "langc_SubSystem74", None)
                if opp_val is None:
                    setattr(value, "langc_SubSystem74", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ElementAccess:

    pass
class langc_MemberAccess(ElementAccess):

    pass
class langc_DependencyList:

    pass
class langc_FileName(Name):

    def __init__(self, hasObjectCode: bool, langc_FileName: "langc_ElementList" = None, langc_FileName85: "langc_FileDependency" = None, langc_FileName93: "langc_UserElement" = None):
        self.hasObjectCode = hasObjectCode
        self.langc_FileName = langc_FileName
        self.langc_FileName85 = langc_FileName85
        self.langc_FileName93 = langc_FileName93
        
    @property
    def hasObjectCode(self) -> bool:
        return self.__hasObjectCode

    @hasObjectCode.setter
    def hasObjectCode(self, hasObjectCode: bool):
        self.__hasObjectCode = hasObjectCode

    @property
    def langc_FileName93(self):
        return self.__langc_FileName93

    @langc_FileName93.setter
    def langc_FileName93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_FileName__langc_FileName93", None)
        self.__langc_FileName93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_UserElement92"):
                opp_val = getattr(old_value, "langc_UserElement92", None)
                if opp_val == self:
                    setattr(old_value, "langc_UserElement92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_UserElement92"):
                opp_val = getattr(value, "langc_UserElement92", None)
                setattr(value, "langc_UserElement92", self)

    @property
    def langc_FileName(self):
        return self.__langc_FileName

    @langc_FileName.setter
    def langc_FileName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_FileName__langc_FileName", None)
        self.__langc_FileName = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_ElementList31"):
                opp_val = getattr(old_value, "langc_ElementList31", None)
                if opp_val == self:
                    setattr(old_value, "langc_ElementList31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_ElementList31"):
                opp_val = getattr(value, "langc_ElementList31", None)
                setattr(value, "langc_ElementList31", self)

    @property
    def langc_FileName85(self):
        return self.__langc_FileName85

    @langc_FileName85.setter
    def langc_FileName85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_FileName__langc_FileName85", None)
        self.__langc_FileName85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_FileDependency"):
                opp_val = getattr(old_value, "langc_FileDependency", None)
                if opp_val == self:
                    setattr(old_value, "langc_FileDependency", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_FileDependency"):
                opp_val = getattr(value, "langc_FileDependency", None)
                setattr(value, "langc_FileDependency", self)

class ExpressionStatement:

    pass
class langc_ReturnStatement(ExpressionStatement):

    pass
class Statement:

    pass
class langc_VariableDeclarationStatement(Statement):

    pass
class langc_SwitchStatement(Statement):

    pass
class langc_BreakStatement(Statement):

    pass
class langc_CodeBlock(Statement):

    def __init__(self, forceBraces: bool, langc_CodeBlock: set["langc_Statement"] = None, langc_CodeBlock136: "langc_FunctionImplementation" = None):
        self.forceBraces = forceBraces
        self.langc_CodeBlock = langc_CodeBlock if langc_CodeBlock is not None else set()
        self.langc_CodeBlock136 = langc_CodeBlock136
        
    @property
    def forceBraces(self) -> bool:
        return self.__forceBraces

    @forceBraces.setter
    def forceBraces(self, forceBraces: bool):
        self.__forceBraces = forceBraces

    @property
    def langc_CodeBlock(self):
        return self.__langc_CodeBlock

    @langc_CodeBlock.setter
    def langc_CodeBlock(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_CodeBlock__langc_CodeBlock", None)
        self.__langc_CodeBlock = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "langc_Statement"):
                    opp_val = getattr(item, "langc_Statement", None)
                    
                    if opp_val == self:
                        setattr(item, "langc_Statement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "langc_Statement"):
                    opp_val = getattr(item, "langc_Statement", None)
                    
                    setattr(item, "langc_Statement", self)
                    

    @property
    def langc_CodeBlock136(self):
        return self.__langc_CodeBlock136

    @langc_CodeBlock136.setter
    def langc_CodeBlock136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_CodeBlock__langc_CodeBlock136", None)
        self.__langc_CodeBlock136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_FunctionImplementation135"):
                opp_val = getattr(old_value, "langc_FunctionImplementation135", None)
                if opp_val == self:
                    setattr(old_value, "langc_FunctionImplementation135", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_FunctionImplementation135"):
                opp_val = getattr(value, "langc_FunctionImplementation135", None)
                setattr(value, "langc_FunctionImplementation135", self)

class langc_ExpressionStatement(Statement):

    pass
class langc_Statement(ABC):

    pass
class Literal:

    pass
class langc_CharacterLiteral(Literal):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class langc_FloatingLiteral(Literal):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class langc_IntegralLiteral(Literal):

    def __init__(self, value: str, bytes: str, signed: bool, langc_IntegralLiteral: "langc_Enumerator" = None):
        self.value = value
        self.bytes = bytes
        self.signed = signed
        self.langc_IntegralLiteral = langc_IntegralLiteral
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def signed(self) -> bool:
        return self.__signed

    @signed.setter
    def signed(self, signed: bool):
        self.__signed = signed

    @property
    def bytes(self) -> str:
        return self.__bytes

    @bytes.setter
    def bytes(self, bytes: str):
        self.__bytes = bytes

    @property
    def langc_IntegralLiteral(self):
        return self.__langc_IntegralLiteral

    @langc_IntegralLiteral.setter
    def langc_IntegralLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_IntegralLiteral__langc_IntegralLiteral", None)
        self.__langc_IntegralLiteral = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_Enumerator80"):
                opp_val = getattr(old_value, "langc_Enumerator80", None)
                if opp_val == self:
                    setattr(old_value, "langc_Enumerator80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_Enumerator80"):
                opp_val = getattr(value, "langc_Enumerator80", None)
                setattr(value, "langc_Enumerator80", self)

class langc_Directive(ABC):

    pass
class Structure:

    pass
class langc_Union(Structure):

    pass
class langc_Struct(Structure):

    pass
class langc_ElementList:

    pass
class Expression:

    pass
class langc_FunctionAddress(Expression):

    pass
class langc_BinaryOperation(Expression):

    def __init__(self, operator: str, langc_BinaryOperation51: "langc_Expression" = None, langc_BinaryOperation: "langc_Expression" = None):
        self.operator = operator
        self.langc_BinaryOperation51 = langc_BinaryOperation51
        self.langc_BinaryOperation = langc_BinaryOperation
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def langc_BinaryOperation51(self):
        return self.__langc_BinaryOperation51

    @langc_BinaryOperation51.setter
    def langc_BinaryOperation51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_BinaryOperation__langc_BinaryOperation51", None)
        self.__langc_BinaryOperation51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_Expression52"):
                opp_val = getattr(old_value, "langc_Expression52", None)
                if opp_val == self:
                    setattr(old_value, "langc_Expression52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_Expression52"):
                opp_val = getattr(value, "langc_Expression52", None)
                setattr(value, "langc_Expression52", self)

    @property
    def langc_BinaryOperation(self):
        return self.__langc_BinaryOperation

    @langc_BinaryOperation.setter
    def langc_BinaryOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_BinaryOperation__langc_BinaryOperation", None)
        self.__langc_BinaryOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_Expression49"):
                opp_val = getattr(old_value, "langc_Expression49", None)
                if opp_val == self:
                    setattr(old_value, "langc_Expression49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_Expression49"):
                opp_val = getattr(value, "langc_Expression49", None)
                setattr(value, "langc_Expression49", self)

class langc_Sizeof(Expression):

    pass
class langc_BlockInitializer(Expression):

    pass
class langc_AddressOfExpr(Expression):

    pass
class langc_CastExpr(Expression):

    pass
class langc_LogicalComparison(Expression):

    def __init__(self, operator: str, langc_LogicalComparison: "langc_Expression" = None, langc_LogicalComparison130: "langc_Expression" = None):
        self.operator = operator
        self.langc_LogicalComparison = langc_LogicalComparison
        self.langc_LogicalComparison130 = langc_LogicalComparison130
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def langc_LogicalComparison130(self):
        return self.__langc_LogicalComparison130

    @langc_LogicalComparison130.setter
    def langc_LogicalComparison130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_LogicalComparison__langc_LogicalComparison130", None)
        self.__langc_LogicalComparison130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_Expression131"):
                opp_val = getattr(old_value, "langc_Expression131", None)
                if opp_val == self:
                    setattr(old_value, "langc_Expression131", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_Expression131"):
                opp_val = getattr(value, "langc_Expression131", None)
                setattr(value, "langc_Expression131", self)

    @property
    def langc_LogicalComparison(self):
        return self.__langc_LogicalComparison

    @langc_LogicalComparison.setter
    def langc_LogicalComparison(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_LogicalComparison__langc_LogicalComparison", None)
        self.__langc_LogicalComparison = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_Expression128"):
                opp_val = getattr(old_value, "langc_Expression128", None)
                if opp_val == self:
                    setattr(old_value, "langc_Expression128", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_Expression128"):
                opp_val = getattr(value, "langc_Expression128", None)
                setattr(value, "langc_Expression128", self)

class langc_DereferenceExpr(Expression):

    pass
class langc_IndexExpr(Expression):

    pass
class langc_Literal(Expression):

    def __init__(self, primitiveType: str):
        self.primitiveType = primitiveType
        
    @property
    def primitiveType(self) -> str:
        return self.__primitiveType

    @primitiveType.setter
    def primitiveType(self, primitiveType: str):
        self.__primitiveType = primitiveType

class langc_StringLiteral(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class langc_ExpressionBlob(Expression):

    def __init__(self, text: str):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class langc_ElementAccess(Expression):

    pass
class langc_FunctionCall(Expression):

    pass
class langc_Expression:

    def __init__(self, precendence: int, langc_Expression: "langc_ElementReference" = None, langc_Expression20: "langc_ElementReference" = None, langc_Expression26: "langc_FunctionCall" = None, langc_Expression46: "langc_ExpressionStatement" = None, langc_Expression52: "langc_BinaryOperation" = None, langc_Expression66: "langc_VariableDeclaration" = None, langc_Expression70: "langc_MemberAccess" = None, langc_Expression49: "langc_BinaryOperation" = None, langc_Expression90: "langc_CastExpr" = None, langc_Expression99: "langc_LabeledClause" = None, langc_Expression103: "langc_SwitchStatement" = None, langc_Expression105: "langc_AddressOfExpr" = None, langc_Expression107: "langc_DereferenceExpr" = None, langc_Expression109: "langc_WhileStatement" = None, langc_Expression114: "langc_Macro" = None, langc_Expression123: "langc_IndexExpr" = None, langc_Expression126: "langc_IndexExpr" = None, langc_Expression128: "langc_LogicalComparison" = None, langc_Expression131: "langc_LogicalComparison" = None, langc_Expression133: "langc_SizeofExpr" = None, langc_Expression121: "langc_BlockInitializer" = None, langc_Expression155: "langc_ConditionalStatement" = None):
        self.precendence = precendence
        self.langc_Expression = langc_Expression
        self.langc_Expression20 = langc_Expression20
        self.langc_Expression26 = langc_Expression26
        self.langc_Expression46 = langc_Expression46
        self.langc_Expression52 = langc_Expression52
        self.langc_Expression66 = langc_Expression66
        self.langc_Expression70 = langc_Expression70
        self.langc_Expression49 = langc_Expression49
        self.langc_Expression90 = langc_Expression90
        self.langc_Expression99 = langc_Expression99
        self.langc_Expression103 = langc_Expression103
        self.langc_Expression105 = langc_Expression105
        self.langc_Expression107 = langc_Expression107
        self.langc_Expression109 = langc_Expression109
        self.langc_Expression114 = langc_Expression114
        self.langc_Expression123 = langc_Expression123
        self.langc_Expression126 = langc_Expression126
        self.langc_Expression128 = langc_Expression128
        self.langc_Expression131 = langc_Expression131
        self.langc_Expression133 = langc_Expression133
        self.langc_Expression121 = langc_Expression121
        self.langc_Expression155 = langc_Expression155
        
    @property
    def precendence(self) -> int:
        return self.__precendence

    @precendence.setter
    def precendence(self, precendence: int):
        self.__precendence = precendence

    @property
    def langc_Expression99(self):
        return self.__langc_Expression99

    @langc_Expression99.setter
    def langc_Expression99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_Expression__langc_Expression99", None)
        self.__langc_Expression99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_LabeledClause"):
                opp_val = getattr(old_value, "langc_LabeledClause", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_LabeledClause"):
                opp_val = getattr(value, "langc_LabeledClause", None)
                if opp_val is None:
                    setattr(value, "langc_LabeledClause", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def langc_Expression46(self):
        return self.__langc_Expression46

    @langc_Expression46.setter
    def langc_Expression46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_Expression__langc_Expression46", None)
        self.__langc_Expression46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_ExpressionStatement"):
                opp_val = getattr(old_value, "langc_ExpressionStatement", None)
                if opp_val == self:
                    setattr(old_value, "langc_ExpressionStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_ExpressionStatement"):
                opp_val = getattr(value, "langc_ExpressionStatement", None)
                setattr(value, "langc_ExpressionStatement", self)

    @property
    def langc_Expression20(self):
        return self.__langc_Expression20

    @langc_Expression20.setter
    def langc_Expression20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_Expression__langc_Expression20", None)
        self.__langc_Expression20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_ElementReference21"):
                opp_val = getattr(old_value, "langc_ElementReference21", None)
                if opp_val == self:
                    setattr(old_value, "langc_ElementReference21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_ElementReference21"):
                opp_val = getattr(value, "langc_ElementReference21", None)
                setattr(value, "langc_ElementReference21", self)

    @property
    def langc_Expression90(self):
        return self.__langc_Expression90

    @langc_Expression90.setter
    def langc_Expression90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_Expression__langc_Expression90", None)
        self.__langc_Expression90 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_CastExpr89"):
                opp_val = getattr(old_value, "langc_CastExpr89", None)
                if opp_val == self:
                    setattr(old_value, "langc_CastExpr89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_CastExpr89"):
                opp_val = getattr(value, "langc_CastExpr89", None)
                setattr(value, "langc_CastExpr89", self)

    @property
    def langc_Expression155(self):
        return self.__langc_Expression155

    @langc_Expression155.setter
    def langc_Expression155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_Expression__langc_Expression155", None)
        self.__langc_Expression155 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_ConditionalStatement"):
                opp_val = getattr(old_value, "langc_ConditionalStatement", None)
                if opp_val == self:
                    setattr(old_value, "langc_ConditionalStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_ConditionalStatement"):
                opp_val = getattr(value, "langc_ConditionalStatement", None)
                setattr(value, "langc_ConditionalStatement", self)

    @property
    def langc_Expression26(self):
        return self.__langc_Expression26

    @langc_Expression26.setter
    def langc_Expression26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_Expression__langc_Expression26", None)
        self.__langc_Expression26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_FunctionCall25"):
                opp_val = getattr(old_value, "langc_FunctionCall25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_FunctionCall25"):
                opp_val = getattr(value, "langc_FunctionCall25", None)
                if opp_val is None:
                    setattr(value, "langc_FunctionCall25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def langc_Expression128(self):
        return self.__langc_Expression128

    @langc_Expression128.setter
    def langc_Expression128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_Expression__langc_Expression128", None)
        self.__langc_Expression128 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_LogicalComparison"):
                opp_val = getattr(old_value, "langc_LogicalComparison", None)
                if opp_val == self:
                    setattr(old_value, "langc_LogicalComparison", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_LogicalComparison"):
                opp_val = getattr(value, "langc_LogicalComparison", None)
                setattr(value, "langc_LogicalComparison", self)

    @property
    def langc_Expression(self):
        return self.__langc_Expression

    @langc_Expression.setter
    def langc_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_Expression__langc_Expression", None)
        self.__langc_Expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_ElementReference18"):
                opp_val = getattr(old_value, "langc_ElementReference18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_ElementReference18"):
                opp_val = getattr(value, "langc_ElementReference18", None)
                if opp_val is None:
                    setattr(value, "langc_ElementReference18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def langc_Expression105(self):
        return self.__langc_Expression105

    @langc_Expression105.setter
    def langc_Expression105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_Expression__langc_Expression105", None)
        self.__langc_Expression105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_AddressOfExpr"):
                opp_val = getattr(old_value, "langc_AddressOfExpr", None)
                if opp_val == self:
                    setattr(old_value, "langc_AddressOfExpr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_AddressOfExpr"):
                opp_val = getattr(value, "langc_AddressOfExpr", None)
                setattr(value, "langc_AddressOfExpr", self)

    @property
    def langc_Expression107(self):
        return self.__langc_Expression107

    @langc_Expression107.setter
    def langc_Expression107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_Expression__langc_Expression107", None)
        self.__langc_Expression107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_DereferenceExpr"):
                opp_val = getattr(old_value, "langc_DereferenceExpr", None)
                if opp_val == self:
                    setattr(old_value, "langc_DereferenceExpr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_DereferenceExpr"):
                opp_val = getattr(value, "langc_DereferenceExpr", None)
                setattr(value, "langc_DereferenceExpr", self)

    @property
    def langc_Expression52(self):
        return self.__langc_Expression52

    @langc_Expression52.setter
    def langc_Expression52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_Expression__langc_Expression52", None)
        self.__langc_Expression52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_BinaryOperation51"):
                opp_val = getattr(old_value, "langc_BinaryOperation51", None)
                if opp_val == self:
                    setattr(old_value, "langc_BinaryOperation51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_BinaryOperation51"):
                opp_val = getattr(value, "langc_BinaryOperation51", None)
                setattr(value, "langc_BinaryOperation51", self)

    @property
    def langc_Expression131(self):
        return self.__langc_Expression131

    @langc_Expression131.setter
    def langc_Expression131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_Expression__langc_Expression131", None)
        self.__langc_Expression131 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_LogicalComparison130"):
                opp_val = getattr(old_value, "langc_LogicalComparison130", None)
                if opp_val == self:
                    setattr(old_value, "langc_LogicalComparison130", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_LogicalComparison130"):
                opp_val = getattr(value, "langc_LogicalComparison130", None)
                setattr(value, "langc_LogicalComparison130", self)

    @property
    def langc_Expression121(self):
        return self.__langc_Expression121

    @langc_Expression121.setter
    def langc_Expression121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_Expression__langc_Expression121", None)
        self.__langc_Expression121 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_BlockInitializer"):
                opp_val = getattr(old_value, "langc_BlockInitializer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_BlockInitializer"):
                opp_val = getattr(value, "langc_BlockInitializer", None)
                if opp_val is None:
                    setattr(value, "langc_BlockInitializer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def langc_Expression133(self):
        return self.__langc_Expression133

    @langc_Expression133.setter
    def langc_Expression133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_Expression__langc_Expression133", None)
        self.__langc_Expression133 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_SizeofExpr"):
                opp_val = getattr(old_value, "langc_SizeofExpr", None)
                if opp_val == self:
                    setattr(old_value, "langc_SizeofExpr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_SizeofExpr"):
                opp_val = getattr(value, "langc_SizeofExpr", None)
                setattr(value, "langc_SizeofExpr", self)

    @property
    def langc_Expression49(self):
        return self.__langc_Expression49

    @langc_Expression49.setter
    def langc_Expression49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_Expression__langc_Expression49", None)
        self.__langc_Expression49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_BinaryOperation"):
                opp_val = getattr(old_value, "langc_BinaryOperation", None)
                if opp_val == self:
                    setattr(old_value, "langc_BinaryOperation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_BinaryOperation"):
                opp_val = getattr(value, "langc_BinaryOperation", None)
                setattr(value, "langc_BinaryOperation", self)

    @property
    def langc_Expression109(self):
        return self.__langc_Expression109

    @langc_Expression109.setter
    def langc_Expression109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_Expression__langc_Expression109", None)
        self.__langc_Expression109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_WhileStatement"):
                opp_val = getattr(old_value, "langc_WhileStatement", None)
                if opp_val == self:
                    setattr(old_value, "langc_WhileStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_WhileStatement"):
                opp_val = getattr(value, "langc_WhileStatement", None)
                setattr(value, "langc_WhileStatement", self)

    @property
    def langc_Expression103(self):
        return self.__langc_Expression103

    @langc_Expression103.setter
    def langc_Expression103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_Expression__langc_Expression103", None)
        self.__langc_Expression103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_SwitchStatement102"):
                opp_val = getattr(old_value, "langc_SwitchStatement102", None)
                if opp_val == self:
                    setattr(old_value, "langc_SwitchStatement102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_SwitchStatement102"):
                opp_val = getattr(value, "langc_SwitchStatement102", None)
                setattr(value, "langc_SwitchStatement102", self)

    @property
    def langc_Expression123(self):
        return self.__langc_Expression123

    @langc_Expression123.setter
    def langc_Expression123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_Expression__langc_Expression123", None)
        self.__langc_Expression123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_IndexExpr"):
                opp_val = getattr(old_value, "langc_IndexExpr", None)
                if opp_val == self:
                    setattr(old_value, "langc_IndexExpr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_IndexExpr"):
                opp_val = getattr(value, "langc_IndexExpr", None)
                setattr(value, "langc_IndexExpr", self)

    @property
    def langc_Expression66(self):
        return self.__langc_Expression66

    @langc_Expression66.setter
    def langc_Expression66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_Expression__langc_Expression66", None)
        self.__langc_Expression66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_VariableDeclaration65"):
                opp_val = getattr(old_value, "langc_VariableDeclaration65", None)
                if opp_val == self:
                    setattr(old_value, "langc_VariableDeclaration65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_VariableDeclaration65"):
                opp_val = getattr(value, "langc_VariableDeclaration65", None)
                setattr(value, "langc_VariableDeclaration65", self)

    @property
    def langc_Expression70(self):
        return self.__langc_Expression70

    @langc_Expression70.setter
    def langc_Expression70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_Expression__langc_Expression70", None)
        self.__langc_Expression70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_MemberAccess"):
                opp_val = getattr(old_value, "langc_MemberAccess", None)
                if opp_val == self:
                    setattr(old_value, "langc_MemberAccess", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_MemberAccess"):
                opp_val = getattr(value, "langc_MemberAccess", None)
                setattr(value, "langc_MemberAccess", self)

    @property
    def langc_Expression114(self):
        return self.__langc_Expression114

    @langc_Expression114.setter
    def langc_Expression114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_Expression__langc_Expression114", None)
        self.__langc_Expression114 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_Macro113"):
                opp_val = getattr(old_value, "langc_Macro113", None)
                if opp_val == self:
                    setattr(old_value, "langc_Macro113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_Macro113"):
                opp_val = getattr(value, "langc_Macro113", None)
                setattr(value, "langc_Macro113", self)

    @property
    def langc_Expression126(self):
        return self.__langc_Expression126

    @langc_Expression126.setter
    def langc_Expression126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_Expression__langc_Expression126", None)
        self.__langc_Expression126 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_IndexExpr125"):
                opp_val = getattr(old_value, "langc_IndexExpr125", None)
                if opp_val == self:
                    setattr(old_value, "langc_IndexExpr125", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_IndexExpr125"):
                opp_val = getattr(value, "langc_IndexExpr125", None)
                setattr(value, "langc_IndexExpr125", self)

class langc_Element(ABC):

    pass
class langc_NamedReference:

    pass
class NamedElement:

    pass
class langc_Typedef(NamedElement):

    pass
class langc_VariableDeclaration(NamedElement):

    def __init__(self, linkage: str, langc_VariableDeclaration: "langc_ElementReference" = None, langc_VariableDeclaration65: "langc_Expression" = None, langc_VariableDeclaration119: "langc_VariableDeclarationStatement" = None):
        self.linkage = linkage
        self.langc_VariableDeclaration = langc_VariableDeclaration
        self.langc_VariableDeclaration65 = langc_VariableDeclaration65
        self.langc_VariableDeclaration119 = langc_VariableDeclaration119
        
    @property
    def linkage(self) -> str:
        return self.__linkage

    @linkage.setter
    def linkage(self, linkage: str):
        self.__linkage = linkage

    @property
    def langc_VariableDeclaration(self):
        return self.__langc_VariableDeclaration

    @langc_VariableDeclaration.setter
    def langc_VariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_VariableDeclaration__langc_VariableDeclaration", None)
        self.__langc_VariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_ElementReference63"):
                opp_val = getattr(old_value, "langc_ElementReference63", None)
                if opp_val == self:
                    setattr(old_value, "langc_ElementReference63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_ElementReference63"):
                opp_val = getattr(value, "langc_ElementReference63", None)
                setattr(value, "langc_ElementReference63", self)

    @property
    def langc_VariableDeclaration65(self):
        return self.__langc_VariableDeclaration65

    @langc_VariableDeclaration65.setter
    def langc_VariableDeclaration65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_VariableDeclaration__langc_VariableDeclaration65", None)
        self.__langc_VariableDeclaration65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_Expression66"):
                opp_val = getattr(old_value, "langc_Expression66", None)
                if opp_val == self:
                    setattr(old_value, "langc_Expression66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_Expression66"):
                opp_val = getattr(value, "langc_Expression66", None)
                setattr(value, "langc_Expression66", self)

    @property
    def langc_VariableDeclaration119(self):
        return self.__langc_VariableDeclaration119

    @langc_VariableDeclaration119.setter
    def langc_VariableDeclaration119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_VariableDeclaration__langc_VariableDeclaration119", None)
        self.__langc_VariableDeclaration119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_VariableDeclarationStatement"):
                opp_val = getattr(old_value, "langc_VariableDeclarationStatement", None)
                if opp_val == self:
                    setattr(old_value, "langc_VariableDeclarationStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_VariableDeclarationStatement"):
                opp_val = getattr(value, "langc_VariableDeclarationStatement", None)
                setattr(value, "langc_VariableDeclarationStatement", self)

class langc_Enum(NamedElement):

    pass
class langc_Structure(NamedElement):

    pass
class langc_Function(NamedElement):

    def __init__(self, linkage: str, langc_Function: "langc_ElementReference" = None, langc_Function6: set["langc_NamedReference"] = None, langc_Function8: "langc_FunctionImplementation" = None, langc_Function23: "langc_FunctionCall" = None, langc_Function61: "langc_FunctionAddress" = None, langc_Function139: "langc_FunctionImplementation" = None):
        self.linkage = linkage
        self.langc_Function = langc_Function
        self.langc_Function6 = langc_Function6 if langc_Function6 is not None else set()
        self.langc_Function8 = langc_Function8
        self.langc_Function23 = langc_Function23
        self.langc_Function61 = langc_Function61
        self.langc_Function139 = langc_Function139
        
    @property
    def linkage(self) -> str:
        return self.__linkage

    @linkage.setter
    def linkage(self, linkage: str):
        self.__linkage = linkage

    @property
    def langc_Function(self):
        return self.__langc_Function

    @langc_Function.setter
    def langc_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_Function__langc_Function", None)
        self.__langc_Function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_ElementReference"):
                opp_val = getattr(old_value, "langc_ElementReference", None)
                if opp_val == self:
                    setattr(old_value, "langc_ElementReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_ElementReference"):
                opp_val = getattr(value, "langc_ElementReference", None)
                setattr(value, "langc_ElementReference", self)

    @property
    def langc_Function23(self):
        return self.__langc_Function23

    @langc_Function23.setter
    def langc_Function23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_Function__langc_Function23", None)
        self.__langc_Function23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_FunctionCall"):
                opp_val = getattr(old_value, "langc_FunctionCall", None)
                if opp_val == self:
                    setattr(old_value, "langc_FunctionCall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_FunctionCall"):
                opp_val = getattr(value, "langc_FunctionCall", None)
                setattr(value, "langc_FunctionCall", self)

    @property
    def langc_Function139(self):
        return self.__langc_Function139

    @langc_Function139.setter
    def langc_Function139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_Function__langc_Function139", None)
        self.__langc_Function139 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_FunctionImplementation138"):
                opp_val = getattr(old_value, "langc_FunctionImplementation138", None)
                if opp_val == self:
                    setattr(old_value, "langc_FunctionImplementation138", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_FunctionImplementation138"):
                opp_val = getattr(value, "langc_FunctionImplementation138", None)
                setattr(value, "langc_FunctionImplementation138", self)

    @property
    def langc_Function6(self):
        return self.__langc_Function6

    @langc_Function6.setter
    def langc_Function6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_Function__langc_Function6", None)
        self.__langc_Function6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "langc_NamedReference"):
                    opp_val = getattr(item, "langc_NamedReference", None)
                    
                    if opp_val == self:
                        setattr(item, "langc_NamedReference", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "langc_NamedReference"):
                    opp_val = getattr(item, "langc_NamedReference", None)
                    
                    setattr(item, "langc_NamedReference", self)
                    

    @property
    def langc_Function61(self):
        return self.__langc_Function61

    @langc_Function61.setter
    def langc_Function61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_Function__langc_Function61", None)
        self.__langc_Function61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_FunctionAddress"):
                opp_val = getattr(old_value, "langc_FunctionAddress", None)
                if opp_val == self:
                    setattr(old_value, "langc_FunctionAddress", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_FunctionAddress"):
                opp_val = getattr(value, "langc_FunctionAddress", None)
                setattr(value, "langc_FunctionAddress", self)

    @property
    def langc_Function8(self):
        return self.__langc_Function8

    @langc_Function8.setter
    def langc_Function8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_Function__langc_Function8", None)
        self.__langc_Function8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_FunctionImplementation"):
                opp_val = getattr(old_value, "langc_FunctionImplementation", None)
                if opp_val == self:
                    setattr(old_value, "langc_FunctionImplementation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_FunctionImplementation"):
                opp_val = getattr(value, "langc_FunctionImplementation", None)
                setattr(value, "langc_FunctionImplementation", self)

class Element:

    pass
class langc_UserElement(Element):

    def __init__(self, kind: str, langc_UserElement: "langc_ElementList" = None, langc_UserElement92: "langc_FileName" = None, langc_UserElement153: "langc_LinkableArtifact" = None):
        self.kind = kind
        self.langc_UserElement = langc_UserElement
        self.langc_UserElement92 = langc_UserElement92
        self.langc_UserElement153 = langc_UserElement153
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def langc_UserElement153(self):
        return self.__langc_UserElement153

    @langc_UserElement153.setter
    def langc_UserElement153(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_UserElement__langc_UserElement153", None)
        self.__langc_UserElement153 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_LinkableArtifact152"):
                opp_val = getattr(old_value, "langc_LinkableArtifact152", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_LinkableArtifact152"):
                opp_val = getattr(value, "langc_LinkableArtifact152", None)
                if opp_val is None:
                    setattr(value, "langc_LinkableArtifact152", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def langc_UserElement92(self):
        return self.__langc_UserElement92

    @langc_UserElement92.setter
    def langc_UserElement92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_UserElement__langc_UserElement92", None)
        self.__langc_UserElement92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_FileName93"):
                opp_val = getattr(old_value, "langc_FileName93", None)
                if opp_val == self:
                    setattr(old_value, "langc_FileName93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_FileName93"):
                opp_val = getattr(value, "langc_FileName93", None)
                setattr(value, "langc_FileName93", self)

    @property
    def langc_UserElement(self):
        return self.__langc_UserElement

    @langc_UserElement.setter
    def langc_UserElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_UserElement__langc_UserElement", None)
        self.__langc_UserElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_ElementList"):
                opp_val = getattr(old_value, "langc_ElementList", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_ElementList"):
                opp_val = getattr(value, "langc_ElementList", None)
                if opp_val is None:
                    setattr(value, "langc_ElementList", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class langc_BuiltInType(Element):

    def __init__(self, type: str):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class langc_Name:

    def __init__(self, name: str, langc_Name: "langc_NamedElement" = None, langc_Name3: "langc_Name" = None, langc_Name1: "langc_Name" = None, langc_Name11: "langc_NamedReference" = None, langc_Name28: "langc_ElementAccess" = None, langc_Name83: "langc_Enumerator" = None, langc_Name111: "langc_Macro" = None, langc_Name117: "langc_Macro" = None):
        self.name = name
        self.langc_Name = langc_Name
        self.langc_Name3 = langc_Name3
        self.langc_Name1 = langc_Name1
        self.langc_Name11 = langc_Name11
        self.langc_Name28 = langc_Name28
        self.langc_Name83 = langc_Name83
        self.langc_Name111 = langc_Name111
        self.langc_Name117 = langc_Name117
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def langc_Name1(self):
        return self.__langc_Name1

    @langc_Name1.setter
    def langc_Name1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_Name__langc_Name1", None)
        self.__langc_Name1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_Name3"):
                opp_val = getattr(old_value, "langc_Name3", None)
                if opp_val == self:
                    setattr(old_value, "langc_Name3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_Name3"):
                opp_val = getattr(value, "langc_Name3", None)
                setattr(value, "langc_Name3", self)

    @property
    def langc_Name28(self):
        return self.__langc_Name28

    @langc_Name28.setter
    def langc_Name28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_Name__langc_Name28", None)
        self.__langc_Name28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_ElementAccess"):
                opp_val = getattr(old_value, "langc_ElementAccess", None)
                if opp_val == self:
                    setattr(old_value, "langc_ElementAccess", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_ElementAccess"):
                opp_val = getattr(value, "langc_ElementAccess", None)
                setattr(value, "langc_ElementAccess", self)

    @property
    def langc_Name111(self):
        return self.__langc_Name111

    @langc_Name111.setter
    def langc_Name111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_Name__langc_Name111", None)
        self.__langc_Name111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_Macro"):
                opp_val = getattr(old_value, "langc_Macro", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_Macro"):
                opp_val = getattr(value, "langc_Macro", None)
                if opp_val is None:
                    setattr(value, "langc_Macro", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def langc_Name11(self):
        return self.__langc_Name11

    @langc_Name11.setter
    def langc_Name11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_Name__langc_Name11", None)
        self.__langc_Name11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_NamedReference10"):
                opp_val = getattr(old_value, "langc_NamedReference10", None)
                if opp_val == self:
                    setattr(old_value, "langc_NamedReference10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_NamedReference10"):
                opp_val = getattr(value, "langc_NamedReference10", None)
                setattr(value, "langc_NamedReference10", self)

    @property
    def langc_Name83(self):
        return self.__langc_Name83

    @langc_Name83.setter
    def langc_Name83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_Name__langc_Name83", None)
        self.__langc_Name83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_Enumerator82"):
                opp_val = getattr(old_value, "langc_Enumerator82", None)
                if opp_val == self:
                    setattr(old_value, "langc_Enumerator82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_Enumerator82"):
                opp_val = getattr(value, "langc_Enumerator82", None)
                setattr(value, "langc_Enumerator82", self)

    @property
    def langc_Name117(self):
        return self.__langc_Name117

    @langc_Name117.setter
    def langc_Name117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_Name__langc_Name117", None)
        self.__langc_Name117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_Macro116"):
                opp_val = getattr(old_value, "langc_Macro116", None)
                if opp_val == self:
                    setattr(old_value, "langc_Macro116", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_Macro116"):
                opp_val = getattr(value, "langc_Macro116", None)
                setattr(value, "langc_Macro116", self)

    @property
    def langc_Name(self):
        return self.__langc_Name

    @langc_Name.setter
    def langc_Name(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_Name__langc_Name", None)
        self.__langc_Name = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_NamedElement"):
                opp_val = getattr(old_value, "langc_NamedElement", None)
                if opp_val == self:
                    setattr(old_value, "langc_NamedElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_NamedElement"):
                opp_val = getattr(value, "langc_NamedElement", None)
                setattr(value, "langc_NamedElement", self)

    @property
    def langc_Name3(self):
        return self.__langc_Name3

    @langc_Name3.setter
    def langc_Name3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_Name__langc_Name3", None)
        self.__langc_Name3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_Name1"):
                opp_val = getattr(old_value, "langc_Name1", None)
                if opp_val == self:
                    setattr(old_value, "langc_Name1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_Name1"):
                opp_val = getattr(value, "langc_Name1", None)
                setattr(value, "langc_Name1", self)

class BindableValue:

    pass
class langc_Macro(BindableValue, Directive):

    pass
class langc_Enumerator(BindableValue):

    pass
class langc_ElementReference(BindableValue):

    def __init__(self, cvQualifier: str, pointerSpec: str, langc_ElementReference: "langc_Function" = None, langc_ElementReference14: "langc_NamedReference" = None, langc_ElementReference16: "langc_Element" = None, langc_ElementReference18: set["langc_Expression"] = None, langc_ElementReference21: "langc_Expression" = None, langc_ElementReference56: "langc_FunctionPointer" = None, langc_ElementReference59: "langc_FunctionPointer" = None, langc_ElementReference63: "langc_VariableDeclaration" = None, langc_ElementReference68: "langc_Typedef" = None, langc_ElementReference87: "langc_CastExpr" = None, langc_ElementReference97: "langc_SizeofType" = None):
        self.cvQualifier = cvQualifier
        self.pointerSpec = pointerSpec
        self.langc_ElementReference = langc_ElementReference
        self.langc_ElementReference14 = langc_ElementReference14
        self.langc_ElementReference16 = langc_ElementReference16
        self.langc_ElementReference18 = langc_ElementReference18 if langc_ElementReference18 is not None else set()
        self.langc_ElementReference21 = langc_ElementReference21
        self.langc_ElementReference56 = langc_ElementReference56
        self.langc_ElementReference59 = langc_ElementReference59
        self.langc_ElementReference63 = langc_ElementReference63
        self.langc_ElementReference68 = langc_ElementReference68
        self.langc_ElementReference87 = langc_ElementReference87
        self.langc_ElementReference97 = langc_ElementReference97
        
    @property
    def cvQualifier(self) -> str:
        return self.__cvQualifier

    @cvQualifier.setter
    def cvQualifier(self, cvQualifier: str):
        self.__cvQualifier = cvQualifier

    @property
    def pointerSpec(self) -> str:
        return self.__pointerSpec

    @pointerSpec.setter
    def pointerSpec(self, pointerSpec: str):
        self.__pointerSpec = pointerSpec

    @property
    def langc_ElementReference14(self):
        return self.__langc_ElementReference14

    @langc_ElementReference14.setter
    def langc_ElementReference14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_ElementReference__langc_ElementReference14", None)
        self.__langc_ElementReference14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_NamedReference13"):
                opp_val = getattr(old_value, "langc_NamedReference13", None)
                if opp_val == self:
                    setattr(old_value, "langc_NamedReference13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_NamedReference13"):
                opp_val = getattr(value, "langc_NamedReference13", None)
                setattr(value, "langc_NamedReference13", self)

    @property
    def langc_ElementReference(self):
        return self.__langc_ElementReference

    @langc_ElementReference.setter
    def langc_ElementReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_ElementReference__langc_ElementReference", None)
        self.__langc_ElementReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_Function"):
                opp_val = getattr(old_value, "langc_Function", None)
                if opp_val == self:
                    setattr(old_value, "langc_Function", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_Function"):
                opp_val = getattr(value, "langc_Function", None)
                setattr(value, "langc_Function", self)

    @property
    def langc_ElementReference63(self):
        return self.__langc_ElementReference63

    @langc_ElementReference63.setter
    def langc_ElementReference63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_ElementReference__langc_ElementReference63", None)
        self.__langc_ElementReference63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_VariableDeclaration"):
                opp_val = getattr(old_value, "langc_VariableDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "langc_VariableDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_VariableDeclaration"):
                opp_val = getattr(value, "langc_VariableDeclaration", None)
                setattr(value, "langc_VariableDeclaration", self)

    @property
    def langc_ElementReference97(self):
        return self.__langc_ElementReference97

    @langc_ElementReference97.setter
    def langc_ElementReference97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_ElementReference__langc_ElementReference97", None)
        self.__langc_ElementReference97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_SizeofType"):
                opp_val = getattr(old_value, "langc_SizeofType", None)
                if opp_val == self:
                    setattr(old_value, "langc_SizeofType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_SizeofType"):
                opp_val = getattr(value, "langc_SizeofType", None)
                setattr(value, "langc_SizeofType", self)

    @property
    def langc_ElementReference21(self):
        return self.__langc_ElementReference21

    @langc_ElementReference21.setter
    def langc_ElementReference21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_ElementReference__langc_ElementReference21", None)
        self.__langc_ElementReference21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_Expression20"):
                opp_val = getattr(old_value, "langc_Expression20", None)
                if opp_val == self:
                    setattr(old_value, "langc_Expression20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_Expression20"):
                opp_val = getattr(value, "langc_Expression20", None)
                setattr(value, "langc_Expression20", self)

    @property
    def langc_ElementReference16(self):
        return self.__langc_ElementReference16

    @langc_ElementReference16.setter
    def langc_ElementReference16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_ElementReference__langc_ElementReference16", None)
        self.__langc_ElementReference16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_Element"):
                opp_val = getattr(old_value, "langc_Element", None)
                if opp_val == self:
                    setattr(old_value, "langc_Element", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_Element"):
                opp_val = getattr(value, "langc_Element", None)
                setattr(value, "langc_Element", self)

    @property
    def langc_ElementReference68(self):
        return self.__langc_ElementReference68

    @langc_ElementReference68.setter
    def langc_ElementReference68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_ElementReference__langc_ElementReference68", None)
        self.__langc_ElementReference68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_Typedef"):
                opp_val = getattr(old_value, "langc_Typedef", None)
                if opp_val == self:
                    setattr(old_value, "langc_Typedef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_Typedef"):
                opp_val = getattr(value, "langc_Typedef", None)
                setattr(value, "langc_Typedef", self)

    @property
    def langc_ElementReference59(self):
        return self.__langc_ElementReference59

    @langc_ElementReference59.setter
    def langc_ElementReference59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_ElementReference__langc_ElementReference59", None)
        self.__langc_ElementReference59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_FunctionPointer58"):
                opp_val = getattr(old_value, "langc_FunctionPointer58", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_FunctionPointer58"):
                opp_val = getattr(value, "langc_FunctionPointer58", None)
                if opp_val is None:
                    setattr(value, "langc_FunctionPointer58", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def langc_ElementReference87(self):
        return self.__langc_ElementReference87

    @langc_ElementReference87.setter
    def langc_ElementReference87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_ElementReference__langc_ElementReference87", None)
        self.__langc_ElementReference87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_CastExpr"):
                opp_val = getattr(old_value, "langc_CastExpr", None)
                if opp_val == self:
                    setattr(old_value, "langc_CastExpr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_CastExpr"):
                opp_val = getattr(value, "langc_CastExpr", None)
                setattr(value, "langc_CastExpr", self)

    @property
    def langc_ElementReference18(self):
        return self.__langc_ElementReference18

    @langc_ElementReference18.setter
    def langc_ElementReference18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_ElementReference__langc_ElementReference18", None)
        self.__langc_ElementReference18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "langc_Expression"):
                    opp_val = getattr(item, "langc_Expression", None)
                    
                    if opp_val == self:
                        setattr(item, "langc_Expression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "langc_Expression"):
                    opp_val = getattr(item, "langc_Expression", None)
                    
                    setattr(item, "langc_Expression", self)
                    

    @property
    def langc_ElementReference56(self):
        return self.__langc_ElementReference56

    @langc_ElementReference56.setter
    def langc_ElementReference56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_langc_ElementReference__langc_ElementReference56", None)
        self.__langc_ElementReference56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "langc_FunctionPointer"):
                opp_val = getattr(old_value, "langc_FunctionPointer", None)
                if opp_val == self:
                    setattr(old_value, "langc_FunctionPointer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "langc_FunctionPointer"):
                opp_val = getattr(value, "langc_FunctionPointer", None)
                setattr(value, "langc_FunctionPointer", self)

class UserElement:

    pass
class langc_FunctionPointer(UserElement):

    pass
class langc_FunctionImplementation(UserElement):

    pass
class langc_NamedElement(UserElement, BindableValue):

    pass