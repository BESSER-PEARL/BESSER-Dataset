from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class VisibilityKind(Enum):
    none = "none"
    public = "public"
    private = "private"
    protected = "protected"
class InheritanceKind(Enum):
    abstract = "abstract"
    final = "final"


############################################
# Definition of Classes
############################################

class PrimitiveType:

    pass
class Java5_PrimitiveTypeShort(PrimitiveType):

    pass
class Java5_PrimitiveTypeByte(PrimitiveType):

    pass
class Java5_PrimitiveTypeFloat(PrimitiveType):

    pass
class Java5_PrimitiveTypeChar(PrimitiveType):

    pass
class Java5_PrimitiveTypeInt(PrimitiveType):

    pass
class Java5_PrimitiveTypeDouble(PrimitiveType):

    pass
class Java5_PrimitiveTypeLong(PrimitiveType):

    pass
class Java5_PrimitiveTypeBoolean(PrimitiveType):

    pass
class VariableDeclaration:

    pass
class Java5_PrimitiveTypeVoid(PrimitiveType):

    pass
class Java5_Model:

    def __init__(self, name: str, Java5_Model: set["Java5_PackageDeclaration"] = None, Java5_Model216: set["Java5_OrphanType"] = None, Java5_Model218: set["Java5_UnresolvedItem"] = None, Java5_Model220: set["Java5_CompilationUnit"] = None):
        self.name = name
        self.Java5_Model = Java5_Model if Java5_Model is not None else set()
        self.Java5_Model216 = Java5_Model216 if Java5_Model216 is not None else set()
        self.Java5_Model218 = Java5_Model218 if Java5_Model218 is not None else set()
        self.Java5_Model220 = Java5_Model220 if Java5_Model220 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Java5_Model220(self):
        return self.__Java5_Model220

    @Java5_Model220.setter
    def Java5_Model220(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_Model__Java5_Model220", None)
        self.__Java5_Model220 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Java5_CompilationUnit221"):
                    opp_val = getattr(item, "Java5_CompilationUnit221", None)
                    
                    if opp_val == self:
                        setattr(item, "Java5_CompilationUnit221", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Java5_CompilationUnit221"):
                    opp_val = getattr(item, "Java5_CompilationUnit221", None)
                    
                    setattr(item, "Java5_CompilationUnit221", self)
                    

    @property
    def Java5_Model(self):
        return self.__Java5_Model

    @Java5_Model.setter
    def Java5_Model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_Model__Java5_Model", None)
        self.__Java5_Model = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Java5_PackageDeclaration214"):
                    opp_val = getattr(item, "Java5_PackageDeclaration214", None)
                    
                    if opp_val == self:
                        setattr(item, "Java5_PackageDeclaration214", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Java5_PackageDeclaration214"):
                    opp_val = getattr(item, "Java5_PackageDeclaration214", None)
                    
                    setattr(item, "Java5_PackageDeclaration214", self)
                    

    @property
    def Java5_Model218(self):
        return self.__Java5_Model218

    @Java5_Model218.setter
    def Java5_Model218(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_Model__Java5_Model218", None)
        self.__Java5_Model218 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Java5_UnresolvedItem"):
                    opp_val = getattr(item, "Java5_UnresolvedItem", None)
                    
                    if opp_val == self:
                        setattr(item, "Java5_UnresolvedItem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Java5_UnresolvedItem"):
                    opp_val = getattr(item, "Java5_UnresolvedItem", None)
                    
                    setattr(item, "Java5_UnresolvedItem", self)
                    

    @property
    def Java5_Model216(self):
        return self.__Java5_Model216

    @Java5_Model216.setter
    def Java5_Model216(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_Model__Java5_Model216", None)
        self.__Java5_Model216 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Java5_OrphanType"):
                    opp_val = getattr(item, "Java5_OrphanType", None)
                    
                    if opp_val == self:
                        setattr(item, "Java5_OrphanType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Java5_OrphanType"):
                    opp_val = getattr(item, "Java5_OrphanType", None)
                    
                    setattr(item, "Java5_OrphanType", self)
                    

class Java5_VariableDeclarationFragment(VariableDeclaration):

    pass
class Java5_SingleVariableDeclaration(VariableDeclaration):

    def __init__(self, varargs: bool, SingleVariableDeclaration: "Java5_CatchClause" = None, SingleVariableDeclaration123: "Java5_EnhancedForStatement" = None, SingleVariableDeclaration194: "Java5_MethodDeclaration" = None, SingleVariableDeclaration226: "Java5_Modifier" = None, SingleVariableDeclaration255: set["Java5_Modifier"] = None, Java5_SingleVariableDeclaration: "Java5_NamedElementRef" = None, parameters: "Java5_MethodDeclaration" = None, exception: "Java5_CatchClause" = None, parameter: "Java5_EnhancedForStatement" = None):
        self.varargs = varargs
        self.SingleVariableDeclaration = SingleVariableDeclaration
        self.SingleVariableDeclaration123 = SingleVariableDeclaration123
        self.SingleVariableDeclaration194 = SingleVariableDeclaration194
        self.SingleVariableDeclaration226 = SingleVariableDeclaration226
        self.SingleVariableDeclaration255 = SingleVariableDeclaration255 if SingleVariableDeclaration255 is not None else set()
        self.Java5_SingleVariableDeclaration = Java5_SingleVariableDeclaration
        self.parameters = parameters
        self.exception = exception
        self.parameter = parameter
        
    @property
    def varargs(self) -> bool:
        return self.__varargs

    @varargs.setter
    def varargs(self, varargs: bool):
        self.__varargs = varargs

    @property
    def SingleVariableDeclaration(self):
        return self.__SingleVariableDeclaration

    @SingleVariableDeclaration.setter
    def SingleVariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_SingleVariableDeclaration__SingleVariableDeclaration", None)
        self.__SingleVariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "catchClause"):
                opp_val = getattr(old_value, "catchClause", None)
                if opp_val == self:
                    setattr(old_value, "catchClause", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "catchClause"):
                opp_val = getattr(value, "catchClause", None)
                setattr(value, "catchClause", self)

    @property
    def SingleVariableDeclaration194(self):
        return self.__SingleVariableDeclaration194

    @SingleVariableDeclaration194.setter
    def SingleVariableDeclaration194(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_SingleVariableDeclaration__SingleVariableDeclaration194", None)
        self.__SingleVariableDeclaration194 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "methodDeclaration"):
                opp_val = getattr(old_value, "methodDeclaration", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "methodDeclaration"):
                opp_val = getattr(value, "methodDeclaration", None)
                if opp_val is None:
                    setattr(value, "methodDeclaration", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Java5_SingleVariableDeclaration(self):
        return self.__Java5_SingleVariableDeclaration

    @Java5_SingleVariableDeclaration.setter
    def Java5_SingleVariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_SingleVariableDeclaration__Java5_SingleVariableDeclaration", None)
        self.__Java5_SingleVariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Java5_NamedElementRef258"):
                opp_val = getattr(old_value, "Java5_NamedElementRef258", None)
                if opp_val == self:
                    setattr(old_value, "Java5_NamedElementRef258", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Java5_NamedElementRef258"):
                opp_val = getattr(value, "Java5_NamedElementRef258", None)
                setattr(value, "Java5_NamedElementRef258", self)

    @property
    def SingleVariableDeclaration226(self):
        return self.__SingleVariableDeclaration226

    @SingleVariableDeclaration226.setter
    def SingleVariableDeclaration226(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_SingleVariableDeclaration__SingleVariableDeclaration226", None)
        self.__SingleVariableDeclaration226 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modifiers225"):
                opp_val = getattr(old_value, "modifiers225", None)
                if opp_val == self:
                    setattr(old_value, "modifiers225", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modifiers225"):
                opp_val = getattr(value, "modifiers225", None)
                setattr(value, "modifiers225", self)

    @property
    def parameters(self):
        return self.__parameters

    @parameters.setter
    def parameters(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_SingleVariableDeclaration__parameters", None)
        self.__parameters = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MethodDeclaration260"):
                opp_val = getattr(old_value, "MethodDeclaration260", None)
                if opp_val == self:
                    setattr(old_value, "MethodDeclaration260", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MethodDeclaration260"):
                opp_val = getattr(value, "MethodDeclaration260", None)
                setattr(value, "MethodDeclaration260", self)

    @property
    def SingleVariableDeclaration255(self):
        return self.__SingleVariableDeclaration255

    @SingleVariableDeclaration255.setter
    def SingleVariableDeclaration255(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_SingleVariableDeclaration__SingleVariableDeclaration255", None)
        self.__SingleVariableDeclaration255 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Modifier256"):
                    opp_val = getattr(item, "Modifier256", None)
                    
                    if opp_val == self:
                        setattr(item, "Modifier256", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Modifier256"):
                    opp_val = getattr(item, "Modifier256", None)
                    
                    setattr(item, "Modifier256", self)
                    

    @property
    def exception(self):
        return self.__exception

    @exception.setter
    def exception(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_SingleVariableDeclaration__exception", None)
        self.__exception = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CatchClause"):
                opp_val = getattr(old_value, "CatchClause", None)
                if opp_val == self:
                    setattr(old_value, "CatchClause", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CatchClause"):
                opp_val = getattr(value, "CatchClause", None)
                setattr(value, "CatchClause", self)

    @property
    def SingleVariableDeclaration123(self):
        return self.__SingleVariableDeclaration123

    @SingleVariableDeclaration123.setter
    def SingleVariableDeclaration123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_SingleVariableDeclaration__SingleVariableDeclaration123", None)
        self.__SingleVariableDeclaration123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "enhancedForStatement"):
                opp_val = getattr(old_value, "enhancedForStatement", None)
                if opp_val == self:
                    setattr(old_value, "enhancedForStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "enhancedForStatement"):
                opp_val = getattr(value, "enhancedForStatement", None)
                setattr(value, "enhancedForStatement", self)

    @property
    def parameter(self):
        return self.__parameter

    @parameter.setter
    def parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_SingleVariableDeclaration__parameter", None)
        self.__parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EnhancedForStatement"):
                opp_val = getattr(old_value, "EnhancedForStatement", None)
                if opp_val == self:
                    setattr(old_value, "EnhancedForStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EnhancedForStatement"):
                opp_val = getattr(value, "EnhancedForStatement", None)
                setattr(value, "EnhancedForStatement", self)

class TypeDeclaration:

    pass
class Java5_InterfaceDeclaration(TypeDeclaration):

    pass
class Java5_ClassDeclaration(TypeDeclaration):

    pass
class Java5_ASTNode(ABC):

    pass
class Statement:

    pass
class Java5_BreakStatement(Statement):

    pass
class Java5_SwitchStatement(Statement):

    pass
class Java5_EmptyStatement(Statement):

    pass
class Java5_ExpressionStatement(Statement):

    pass
class Java5_WhileStatement(Statement):

    pass
class Java5_TypeDeclarationStatement(Statement):

    pass
class Java5_CatchClause(Statement):

    pass
class Java5_ConstructorInvocation(Statement):

    pass
class Java5_DoStatement(Statement):

    pass
class Java5_TryStatement(Statement):

    pass
class Java5_SwitchCase(Statement):

    def __init__(self, default: bool, Java5_SwitchCase: "Java5_Expression" = None):
        self.default = default
        self.Java5_SwitchCase = Java5_SwitchCase
        
    @property
    def default(self) -> bool:
        return self.__default

    @default.setter
    def default(self, default: bool):
        self.__default = default

    @property
    def Java5_SwitchCase(self):
        return self.__Java5_SwitchCase

    @Java5_SwitchCase.setter
    def Java5_SwitchCase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_SwitchCase__Java5_SwitchCase", None)
        self.__Java5_SwitchCase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Java5_Expression285"):
                opp_val = getattr(old_value, "Java5_Expression285", None)
                if opp_val == self:
                    setattr(old_value, "Java5_Expression285", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Java5_Expression285"):
                opp_val = getattr(value, "Java5_Expression285", None)
                setattr(value, "Java5_Expression285", self)

class Java5_ReturnStatement(Statement):

    pass
class Java5_EnhancedForStatement(Statement):

    pass
class Java5_SuperConstructorInvocation(Statement):

    pass
class Java5_SynchronizedStatement(Statement):

    pass
class Java5_Block(Statement):

    pass
class Java5_ThrowStatement(Statement):

    pass
class Java5_VariableDeclarationStatement(Statement):

    def __init__(self, extraArrayDimensions: int, VariableDeclarationStatement: "Java5_Modifier" = None, VariableDeclarationStatement330: "Java5_VariableDeclarationFragment" = None, Java5_VariableDeclarationStatement: "Java5_NamedElementRef" = None, variableDeclarationStatement: set["Java5_VariableDeclarationFragment"] = None, VariableDeclarationStatement339: set["Java5_Modifier"] = None):
        self.extraArrayDimensions = extraArrayDimensions
        self.VariableDeclarationStatement = VariableDeclarationStatement
        self.VariableDeclarationStatement330 = VariableDeclarationStatement330
        self.Java5_VariableDeclarationStatement = Java5_VariableDeclarationStatement
        self.variableDeclarationStatement = variableDeclarationStatement if variableDeclarationStatement is not None else set()
        self.VariableDeclarationStatement339 = VariableDeclarationStatement339 if VariableDeclarationStatement339 is not None else set()
        
    @property
    def extraArrayDimensions(self) -> int:
        return self.__extraArrayDimensions

    @extraArrayDimensions.setter
    def extraArrayDimensions(self, extraArrayDimensions: int):
        self.__extraArrayDimensions = extraArrayDimensions

    @property
    def variableDeclarationStatement(self):
        return self.__variableDeclarationStatement

    @variableDeclarationStatement.setter
    def variableDeclarationStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_VariableDeclarationStatement__variableDeclarationStatement", None)
        self.__variableDeclarationStatement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VariableDeclarationFragment337"):
                    opp_val = getattr(item, "VariableDeclarationFragment337", None)
                    
                    if opp_val == self:
                        setattr(item, "VariableDeclarationFragment337", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VariableDeclarationFragment337"):
                    opp_val = getattr(item, "VariableDeclarationFragment337", None)
                    
                    setattr(item, "VariableDeclarationFragment337", self)
                    

    @property
    def VariableDeclarationStatement330(self):
        return self.__VariableDeclarationStatement330

    @VariableDeclarationStatement330.setter
    def VariableDeclarationStatement330(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_VariableDeclarationStatement__VariableDeclarationStatement330", None)
        self.__VariableDeclarationStatement330 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fragments329"):
                opp_val = getattr(old_value, "fragments329", None)
                if opp_val == self:
                    setattr(old_value, "fragments329", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fragments329"):
                opp_val = getattr(value, "fragments329", None)
                setattr(value, "fragments329", self)

    @property
    def VariableDeclarationStatement339(self):
        return self.__VariableDeclarationStatement339

    @VariableDeclarationStatement339.setter
    def VariableDeclarationStatement339(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_VariableDeclarationStatement__VariableDeclarationStatement339", None)
        self.__VariableDeclarationStatement339 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Modifier340"):
                    opp_val = getattr(item, "Modifier340", None)
                    
                    if opp_val == self:
                        setattr(item, "Modifier340", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Modifier340"):
                    opp_val = getattr(item, "Modifier340", None)
                    
                    setattr(item, "Modifier340", self)
                    

    @property
    def Java5_VariableDeclarationStatement(self):
        return self.__Java5_VariableDeclarationStatement

    @Java5_VariableDeclarationStatement.setter
    def Java5_VariableDeclarationStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_VariableDeclarationStatement__Java5_VariableDeclarationStatement", None)
        self.__Java5_VariableDeclarationStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Java5_NamedElementRef335"):
                opp_val = getattr(old_value, "Java5_NamedElementRef335", None)
                if opp_val == self:
                    setattr(old_value, "Java5_NamedElementRef335", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Java5_NamedElementRef335"):
                opp_val = getattr(value, "Java5_NamedElementRef335", None)
                setattr(value, "Java5_NamedElementRef335", self)

    @property
    def VariableDeclarationStatement(self):
        return self.__VariableDeclarationStatement

    @VariableDeclarationStatement.setter
    def VariableDeclarationStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_VariableDeclarationStatement__VariableDeclarationStatement", None)
        self.__VariableDeclarationStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modifiers228"):
                opp_val = getattr(old_value, "modifiers228", None)
                if opp_val == self:
                    setattr(old_value, "modifiers228", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modifiers228"):
                opp_val = getattr(value, "modifiers228", None)
                setattr(value, "modifiers228", self)

class Java5_ContinueStatement(Statement):

    pass
class Java5_ForStatement(Statement):

    pass
class Java5_IfStatement(Statement):

    pass
class Java5_AssertStatement(Statement):

    pass
class OrphanType:

    pass
class Java5_ParameterizedType(OrphanType):

    pass
class Java5_PrimitiveType(OrphanType):

    pass
class Java5_WildCardType(OrphanType):

    def __init__(self, isUpperBound: str, Java5_WildCardType: "Java5_NamedElementRef" = None):
        self.isUpperBound = isUpperBound
        self.Java5_WildCardType = Java5_WildCardType
        
    @property
    def isUpperBound(self) -> str:
        return self.__isUpperBound

    @isUpperBound.setter
    def isUpperBound(self, isUpperBound: str):
        self.__isUpperBound = isUpperBound

    @property
    def Java5_WildCardType(self):
        return self.__Java5_WildCardType

    @Java5_WildCardType.setter
    def Java5_WildCardType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_WildCardType__Java5_WildCardType", None)
        self.__Java5_WildCardType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Java5_NamedElementRef347"):
                opp_val = getattr(old_value, "Java5_NamedElementRef347", None)
                if opp_val == self:
                    setattr(old_value, "Java5_NamedElementRef347", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Java5_NamedElementRef347"):
                opp_val = getattr(value, "Java5_NamedElementRef347", None)
                setattr(value, "Java5_NamedElementRef347", self)

class Java5_ArrayType(OrphanType):

    def __init__(self, dimensions: int, originalName: str, Java5_ArrayType: "Java5_NamedElementRef" = None):
        self.dimensions = dimensions
        self.originalName = originalName
        self.Java5_ArrayType = Java5_ArrayType
        
    @property
    def originalName(self) -> str:
        return self.__originalName

    @originalName.setter
    def originalName(self, originalName: str):
        self.__originalName = originalName

    @property
    def dimensions(self) -> int:
        return self.__dimensions

    @dimensions.setter
    def dimensions(self, dimensions: int):
        self.__dimensions = dimensions

    @property
    def Java5_ArrayType(self):
        return self.__Java5_ArrayType

    @Java5_ArrayType.setter
    def Java5_ArrayType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_ArrayType__Java5_ArrayType", None)
        self.__Java5_ArrayType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Java5_NamedElementRef40"):
                opp_val = getattr(old_value, "Java5_NamedElementRef40", None)
                if opp_val == self:
                    setattr(old_value, "Java5_NamedElementRef40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Java5_NamedElementRef40"):
                opp_val = getattr(value, "Java5_NamedElementRef40", None)
                setattr(value, "Java5_NamedElementRef40", self)

class ASTNode:

    pass
class Java5_TagElement(ASTNode):

    def __init__(self, tagName: str, Java5_TagElement: set["Java5_ASTNode"] = None):
        self.tagName = tagName
        self.Java5_TagElement = Java5_TagElement if Java5_TagElement is not None else set()
        
    @property
    def tagName(self) -> str:
        return self.__tagName

    @tagName.setter
    def tagName(self, tagName: str):
        self.__tagName = tagName

    @property
    def Java5_TagElement(self):
        return self.__Java5_TagElement

    @Java5_TagElement.setter
    def Java5_TagElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_TagElement__Java5_TagElement", None)
        self.__Java5_TagElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Java5_ASTNode"):
                    opp_val = getattr(item, "Java5_ASTNode", None)
                    
                    if opp_val == self:
                        setattr(item, "Java5_ASTNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Java5_ASTNode"):
                    opp_val = getattr(item, "Java5_ASTNode", None)
                    
                    setattr(item, "Java5_ASTNode", self)
                    

class Java5_TextElement(ASTNode):

    def __init__(self, text: str):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class Java5_MethodRef(ASTNode):

    pass
class Java5_MemberRef(ASTNode):

    pass
class Java5_Statement(ASTNode):

    pass
class Java5_Modifier(ASTNode):

    def __init__(self, visibility: str, inheritance: str, static: bool, transient: bool, volatile: bool, native: bool, strictfp: bool, synchronized: bool, Modifier: "Java5_BodyDeclaration" = None, modifiers: "Java5_BodyDeclaration" = None, modifiers225: "Java5_SingleVariableDeclaration" = None, modifiers228: "Java5_VariableDeclarationStatement" = None, modifiers230: "Java5_VariableDeclarationExpression" = None, Modifier256: "Java5_SingleVariableDeclaration" = None, Modifier326: "Java5_VariableDeclarationExpression" = None, Modifier340: "Java5_VariableDeclarationStatement" = None):
        self.visibility = visibility
        self.inheritance = inheritance
        self.static = static
        self.transient = transient
        self.volatile = volatile
        self.native = native
        self.strictfp = strictfp
        self.synchronized = synchronized
        self.Modifier = Modifier
        self.modifiers = modifiers
        self.modifiers225 = modifiers225
        self.modifiers228 = modifiers228
        self.modifiers230 = modifiers230
        self.Modifier256 = Modifier256
        self.Modifier326 = Modifier326
        self.Modifier340 = Modifier340
        
    @property
    def static(self) -> bool:
        return self.__static

    @static.setter
    def static(self, static: bool):
        self.__static = static

    @property
    def transient(self) -> bool:
        return self.__transient

    @transient.setter
    def transient(self, transient: bool):
        self.__transient = transient

    @property
    def volatile(self) -> bool:
        return self.__volatile

    @volatile.setter
    def volatile(self, volatile: bool):
        self.__volatile = volatile

    @property
    def synchronized(self) -> bool:
        return self.__synchronized

    @synchronized.setter
    def synchronized(self, synchronized: bool):
        self.__synchronized = synchronized

    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def strictfp(self) -> bool:
        return self.__strictfp

    @strictfp.setter
    def strictfp(self, strictfp: bool):
        self.__strictfp = strictfp

    @property
    def inheritance(self) -> str:
        return self.__inheritance

    @inheritance.setter
    def inheritance(self, inheritance: str):
        self.__inheritance = inheritance

    @property
    def native(self) -> bool:
        return self.__native

    @native.setter
    def native(self, native: bool):
        self.__native = native

    @property
    def modifiers228(self):
        return self.__modifiers228

    @modifiers228.setter
    def modifiers228(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_Modifier__modifiers228", None)
        self.__modifiers228 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VariableDeclarationStatement"):
                opp_val = getattr(old_value, "VariableDeclarationStatement", None)
                if opp_val == self:
                    setattr(old_value, "VariableDeclarationStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VariableDeclarationStatement"):
                opp_val = getattr(value, "VariableDeclarationStatement", None)
                setattr(value, "VariableDeclarationStatement", self)

    @property
    def Modifier256(self):
        return self.__Modifier256

    @Modifier256.setter
    def Modifier256(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_Modifier__Modifier256", None)
        self.__Modifier256 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SingleVariableDeclaration255"):
                opp_val = getattr(old_value, "SingleVariableDeclaration255", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SingleVariableDeclaration255"):
                opp_val = getattr(value, "SingleVariableDeclaration255", None)
                if opp_val is None:
                    setattr(value, "SingleVariableDeclaration255", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Modifier326(self):
        return self.__Modifier326

    @Modifier326.setter
    def Modifier326(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_Modifier__Modifier326", None)
        self.__Modifier326 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VariableDeclarationExpression325"):
                opp_val = getattr(old_value, "VariableDeclarationExpression325", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VariableDeclarationExpression325"):
                opp_val = getattr(value, "VariableDeclarationExpression325", None)
                if opp_val is None:
                    setattr(value, "VariableDeclarationExpression325", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def modifiers230(self):
        return self.__modifiers230

    @modifiers230.setter
    def modifiers230(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_Modifier__modifiers230", None)
        self.__modifiers230 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VariableDeclarationExpression"):
                opp_val = getattr(old_value, "VariableDeclarationExpression", None)
                if opp_val == self:
                    setattr(old_value, "VariableDeclarationExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VariableDeclarationExpression"):
                opp_val = getattr(value, "VariableDeclarationExpression", None)
                setattr(value, "VariableDeclarationExpression", self)

    @property
    def Modifier(self):
        return self.__Modifier

    @Modifier.setter
    def Modifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_Modifier__Modifier", None)
        self.__Modifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BodyDeclaration58"):
                opp_val = getattr(old_value, "BodyDeclaration58", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BodyDeclaration58"):
                opp_val = getattr(value, "BodyDeclaration58", None)
                if opp_val is None:
                    setattr(value, "BodyDeclaration58", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Modifier340(self):
        return self.__Modifier340

    @Modifier340.setter
    def Modifier340(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_Modifier__Modifier340", None)
        self.__Modifier340 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VariableDeclarationStatement339"):
                opp_val = getattr(old_value, "VariableDeclarationStatement339", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VariableDeclarationStatement339"):
                opp_val = getattr(value, "VariableDeclarationStatement339", None)
                if opp_val is None:
                    setattr(value, "VariableDeclarationStatement339", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def modifiers225(self):
        return self.__modifiers225

    @modifiers225.setter
    def modifiers225(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_Modifier__modifiers225", None)
        self.__modifiers225 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SingleVariableDeclaration226"):
                opp_val = getattr(old_value, "SingleVariableDeclaration226", None)
                if opp_val == self:
                    setattr(old_value, "SingleVariableDeclaration226", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SingleVariableDeclaration226"):
                opp_val = getattr(value, "SingleVariableDeclaration226", None)
                setattr(value, "SingleVariableDeclaration226", self)

    @property
    def modifiers(self):
        return self.__modifiers

    @modifiers.setter
    def modifiers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_Modifier__modifiers", None)
        self.__modifiers = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BodyDeclaration223"):
                opp_val = getattr(old_value, "BodyDeclaration223", None)
                if opp_val == self:
                    setattr(old_value, "BodyDeclaration223", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BodyDeclaration223"):
                opp_val = getattr(value, "BodyDeclaration223", None)
                setattr(value, "BodyDeclaration223", self)

class Java5_MethodRefParameter(ASTNode):

    def __init__(self, name: str, isVarargs: str, Java5_MethodRefParameter: "Java5_MethodRef" = None, Java5_MethodRefParameter211: "Java5_NamedElementRef" = None):
        self.name = name
        self.isVarargs = isVarargs
        self.Java5_MethodRefParameter = Java5_MethodRefParameter
        self.Java5_MethodRefParameter211 = Java5_MethodRefParameter211
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def isVarargs(self) -> str:
        return self.__isVarargs

    @isVarargs.setter
    def isVarargs(self, isVarargs: str):
        self.__isVarargs = isVarargs

    @property
    def Java5_MethodRefParameter(self):
        return self.__Java5_MethodRefParameter

    @Java5_MethodRefParameter.setter
    def Java5_MethodRefParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_MethodRefParameter__Java5_MethodRefParameter", None)
        self.__Java5_MethodRefParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Java5_MethodRef209"):
                opp_val = getattr(old_value, "Java5_MethodRef209", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Java5_MethodRef209"):
                opp_val = getattr(value, "Java5_MethodRef209", None)
                if opp_val is None:
                    setattr(value, "Java5_MethodRef209", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Java5_MethodRefParameter211(self):
        return self.__Java5_MethodRefParameter211

    @Java5_MethodRefParameter211.setter
    def Java5_MethodRefParameter211(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_MethodRefParameter__Java5_MethodRefParameter211", None)
        self.__Java5_MethodRefParameter211 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Java5_NamedElementRef212"):
                opp_val = getattr(old_value, "Java5_NamedElementRef212", None)
                if opp_val == self:
                    setattr(old_value, "Java5_NamedElementRef212", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Java5_NamedElementRef212"):
                opp_val = getattr(value, "Java5_NamedElementRef212", None)
                setattr(value, "Java5_NamedElementRef212", self)

class Java5_NamedElement(ASTNode):

    def __init__(self, name: str, proxy: bool, Java5_NamedElement: "Java5_NamedElementRef" = None):
        self.name = name
        self.proxy = proxy
        self.Java5_NamedElement = Java5_NamedElement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def proxy(self) -> bool:
        return self.__proxy

    @proxy.setter
    def proxy(self, proxy: bool):
        self.__proxy = proxy

    @property
    def Java5_NamedElement(self):
        return self.__Java5_NamedElement

    @Java5_NamedElement.setter
    def Java5_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_NamedElement__Java5_NamedElement", None)
        self.__Java5_NamedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Java5_NamedElementRef235"):
                opp_val = getattr(old_value, "Java5_NamedElementRef235", None)
                if opp_val == self:
                    setattr(old_value, "Java5_NamedElementRef235", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Java5_NamedElementRef235"):
                opp_val = getattr(value, "Java5_NamedElementRef235", None)
                setattr(value, "Java5_NamedElementRef235", self)

class Java5_AnonymousClassDeclaration(ASTNode):

    pass
class AbstractTypeDeclaration:

    pass
class Java5_EnumDeclaration(AbstractTypeDeclaration):

    pass
class Java5_TypeDeclaration(AbstractTypeDeclaration):

    pass
class Java5_AnnotationTypeDeclaration(AbstractTypeDeclaration):

    pass
class Java5_Expression(ASTNode):

    pass
class NamedElement:

    pass
class Java5_PackageDeclaration(NamedElement):

    def __init__(self, qualifiedName: str, PackageDeclaration: "Java5_AbstractTypeDeclaration" = None, Java5_PackageDeclaration: "Java5_CompilationUnit" = None, Java5_PackageDeclaration214: "Java5_Model" = None, package: set["Java5_AbstractTypeDeclaration"] = None, Java5_PackageDeclaration240: "Java5_PackageDeclaration" = None, Java5_PackageDeclaration238: set["Java5_PackageDeclaration"] = None):
        self.qualifiedName = qualifiedName
        self.PackageDeclaration = PackageDeclaration
        self.Java5_PackageDeclaration = Java5_PackageDeclaration
        self.Java5_PackageDeclaration214 = Java5_PackageDeclaration214
        self.package = package if package is not None else set()
        self.Java5_PackageDeclaration240 = Java5_PackageDeclaration240
        self.Java5_PackageDeclaration238 = Java5_PackageDeclaration238 if Java5_PackageDeclaration238 is not None else set()
        
    @property
    def qualifiedName(self) -> str:
        return self.__qualifiedName

    @qualifiedName.setter
    def qualifiedName(self, qualifiedName: str):
        self.__qualifiedName = qualifiedName

    @property
    def Java5_PackageDeclaration240(self):
        return self.__Java5_PackageDeclaration240

    @Java5_PackageDeclaration240.setter
    def Java5_PackageDeclaration240(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_PackageDeclaration__Java5_PackageDeclaration240", None)
        self.__Java5_PackageDeclaration240 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Java5_PackageDeclaration238"):
                opp_val = getattr(old_value, "Java5_PackageDeclaration238", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Java5_PackageDeclaration238"):
                opp_val = getattr(value, "Java5_PackageDeclaration238", None)
                if opp_val is None:
                    setattr(value, "Java5_PackageDeclaration238", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def package(self):
        return self.__package

    @package.setter
    def package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_PackageDeclaration__package", None)
        self.__package = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AbstractTypeDeclaration237"):
                    opp_val = getattr(item, "AbstractTypeDeclaration237", None)
                    
                    if opp_val == self:
                        setattr(item, "AbstractTypeDeclaration237", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AbstractTypeDeclaration237"):
                    opp_val = getattr(item, "AbstractTypeDeclaration237", None)
                    
                    setattr(item, "AbstractTypeDeclaration237", self)
                    

    @property
    def Java5_PackageDeclaration238(self):
        return self.__Java5_PackageDeclaration238

    @Java5_PackageDeclaration238.setter
    def Java5_PackageDeclaration238(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_PackageDeclaration__Java5_PackageDeclaration238", None)
        self.__Java5_PackageDeclaration238 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Java5_PackageDeclaration240"):
                    opp_val = getattr(item, "Java5_PackageDeclaration240", None)
                    
                    if opp_val == self:
                        setattr(item, "Java5_PackageDeclaration240", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Java5_PackageDeclaration240"):
                    opp_val = getattr(item, "Java5_PackageDeclaration240", None)
                    
                    setattr(item, "Java5_PackageDeclaration240", self)
                    

    @property
    def PackageDeclaration(self):
        return self.__PackageDeclaration

    @PackageDeclaration.setter
    def PackageDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_PackageDeclaration__PackageDeclaration", None)
        self.__PackageDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedElements"):
                opp_val = getattr(old_value, "ownedElements", None)
                if opp_val == self:
                    setattr(old_value, "ownedElements", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedElements"):
                opp_val = getattr(value, "ownedElements", None)
                setattr(value, "ownedElements", self)

    @property
    def Java5_PackageDeclaration214(self):
        return self.__Java5_PackageDeclaration214

    @Java5_PackageDeclaration214.setter
    def Java5_PackageDeclaration214(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_PackageDeclaration__Java5_PackageDeclaration214", None)
        self.__Java5_PackageDeclaration214 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Java5_Model"):
                opp_val = getattr(old_value, "Java5_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Java5_Model"):
                opp_val = getattr(value, "Java5_Model", None)
                if opp_val is None:
                    setattr(value, "Java5_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Java5_PackageDeclaration(self):
        return self.__Java5_PackageDeclaration

    @Java5_PackageDeclaration.setter
    def Java5_PackageDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_PackageDeclaration__Java5_PackageDeclaration", None)
        self.__Java5_PackageDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Java5_CompilationUnit87"):
                opp_val = getattr(old_value, "Java5_CompilationUnit87", None)
                if opp_val == self:
                    setattr(old_value, "Java5_CompilationUnit87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Java5_CompilationUnit87"):
                opp_val = getattr(value, "Java5_CompilationUnit87", None)
                setattr(value, "Java5_CompilationUnit87", self)

class Java5_CompilationUnit(NamedElement):

    def __init__(self, originalFilePath: str, Java5_CompilationUnit: set["Java5_ImportDeclaration"] = None, Java5_CompilationUnit89: set["Java5_AbstractTypeDeclaration"] = None, Java5_CompilationUnit87: "Java5_PackageDeclaration" = None, Java5_CompilationUnit221: "Java5_Model" = None):
        self.originalFilePath = originalFilePath
        self.Java5_CompilationUnit = Java5_CompilationUnit if Java5_CompilationUnit is not None else set()
        self.Java5_CompilationUnit89 = Java5_CompilationUnit89 if Java5_CompilationUnit89 is not None else set()
        self.Java5_CompilationUnit87 = Java5_CompilationUnit87
        self.Java5_CompilationUnit221 = Java5_CompilationUnit221
        
    @property
    def originalFilePath(self) -> str:
        return self.__originalFilePath

    @originalFilePath.setter
    def originalFilePath(self, originalFilePath: str):
        self.__originalFilePath = originalFilePath

    @property
    def Java5_CompilationUnit221(self):
        return self.__Java5_CompilationUnit221

    @Java5_CompilationUnit221.setter
    def Java5_CompilationUnit221(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_CompilationUnit__Java5_CompilationUnit221", None)
        self.__Java5_CompilationUnit221 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Java5_Model220"):
                opp_val = getattr(old_value, "Java5_Model220", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Java5_Model220"):
                opp_val = getattr(value, "Java5_Model220", None)
                if opp_val is None:
                    setattr(value, "Java5_Model220", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Java5_CompilationUnit87(self):
        return self.__Java5_CompilationUnit87

    @Java5_CompilationUnit87.setter
    def Java5_CompilationUnit87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_CompilationUnit__Java5_CompilationUnit87", None)
        self.__Java5_CompilationUnit87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Java5_PackageDeclaration"):
                opp_val = getattr(old_value, "Java5_PackageDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "Java5_PackageDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Java5_PackageDeclaration"):
                opp_val = getattr(value, "Java5_PackageDeclaration", None)
                setattr(value, "Java5_PackageDeclaration", self)

    @property
    def Java5_CompilationUnit(self):
        return self.__Java5_CompilationUnit

    @Java5_CompilationUnit.setter
    def Java5_CompilationUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_CompilationUnit__Java5_CompilationUnit", None)
        self.__Java5_CompilationUnit = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Java5_ImportDeclaration85"):
                    opp_val = getattr(item, "Java5_ImportDeclaration85", None)
                    
                    if opp_val == self:
                        setattr(item, "Java5_ImportDeclaration85", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Java5_ImportDeclaration85"):
                    opp_val = getattr(item, "Java5_ImportDeclaration85", None)
                    
                    setattr(item, "Java5_ImportDeclaration85", self)
                    

    @property
    def Java5_CompilationUnit89(self):
        return self.__Java5_CompilationUnit89

    @Java5_CompilationUnit89.setter
    def Java5_CompilationUnit89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_CompilationUnit__Java5_CompilationUnit89", None)
        self.__Java5_CompilationUnit89 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Java5_AbstractTypeDeclaration90"):
                    opp_val = getattr(item, "Java5_AbstractTypeDeclaration90", None)
                    
                    if opp_val == self:
                        setattr(item, "Java5_AbstractTypeDeclaration90", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Java5_AbstractTypeDeclaration90"):
                    opp_val = getattr(item, "Java5_AbstractTypeDeclaration90", None)
                    
                    setattr(item, "Java5_AbstractTypeDeclaration90", self)
                    

class Java5_VariableDeclaration(NamedElement):

    def __init__(self, extraArrayDimensions: int, Java5_VariableDeclaration: "Java5_Expression" = None):
        self.extraArrayDimensions = extraArrayDimensions
        self.Java5_VariableDeclaration = Java5_VariableDeclaration
        
    @property
    def extraArrayDimensions(self) -> int:
        return self.__extraArrayDimensions

    @extraArrayDimensions.setter
    def extraArrayDimensions(self, extraArrayDimensions: int):
        self.__extraArrayDimensions = extraArrayDimensions

    @property
    def Java5_VariableDeclaration(self):
        return self.__Java5_VariableDeclaration

    @Java5_VariableDeclaration.setter
    def Java5_VariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_VariableDeclaration__Java5_VariableDeclaration", None)
        self.__Java5_VariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Java5_Expression319"):
                opp_val = getattr(old_value, "Java5_Expression319", None)
                if opp_val == self:
                    setattr(old_value, "Java5_Expression319", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Java5_Expression319"):
                opp_val = getattr(value, "Java5_Expression319", None)
                setattr(value, "Java5_Expression319", self)

class Java5_UnresolvedItem(NamedElement):

    pass
class Java5_LabeledStatement(Statement, NamedElement):

    pass
class Java5_OrphanType(NamedElement):

    pass
class Java5_TypeParameter(NamedElement):

    pass
class Java5_AnnotationMemberValuePair(NamedElement):

    pass
class Expression:

    pass
class Java5_Assignment(Expression):

    def __init__(self, operator: str, Java5_Assignment: "Java5_Expression" = None, Java5_Assignment49: "Java5_Expression" = None):
        self.operator = operator
        self.Java5_Assignment = Java5_Assignment
        self.Java5_Assignment49 = Java5_Assignment49
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def Java5_Assignment49(self):
        return self.__Java5_Assignment49

    @Java5_Assignment49.setter
    def Java5_Assignment49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_Assignment__Java5_Assignment49", None)
        self.__Java5_Assignment49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Java5_Expression50"):
                opp_val = getattr(old_value, "Java5_Expression50", None)
                if opp_val == self:
                    setattr(old_value, "Java5_Expression50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Java5_Expression50"):
                opp_val = getattr(value, "Java5_Expression50", None)
                setattr(value, "Java5_Expression50", self)

    @property
    def Java5_Assignment(self):
        return self.__Java5_Assignment

    @Java5_Assignment.setter
    def Java5_Assignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_Assignment__Java5_Assignment", None)
        self.__Java5_Assignment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Java5_Expression47"):
                opp_val = getattr(old_value, "Java5_Expression47", None)
                if opp_val == self:
                    setattr(old_value, "Java5_Expression47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Java5_Expression47"):
                opp_val = getattr(value, "Java5_Expression47", None)
                setattr(value, "Java5_Expression47", self)

class Java5_ClassInstanceCreation(Expression):

    pass
class Java5_MethodInvocation(Expression):

    pass
class Java5_NamedElementRef(Expression):

    pass
class Java5_PostfixExpression(Expression):

    def __init__(self, operator: str, Java5_PostfixExpression: "Java5_Expression" = None):
        self.operator = operator
        self.Java5_PostfixExpression = Java5_PostfixExpression
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def Java5_PostfixExpression(self):
        return self.__Java5_PostfixExpression

    @Java5_PostfixExpression.setter
    def Java5_PostfixExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_PostfixExpression__Java5_PostfixExpression", None)
        self.__Java5_PostfixExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Java5_Expression249"):
                opp_val = getattr(old_value, "Java5_Expression249", None)
                if opp_val == self:
                    setattr(old_value, "Java5_Expression249", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Java5_Expression249"):
                opp_val = getattr(value, "Java5_Expression249", None)
                setattr(value, "Java5_Expression249", self)

class Java5_TypeLiteral(Expression):

    pass
class Java5_FieldAccess(Expression):

    pass
class Java5_VariableDeclarationExpression(Expression):

    pass
class Java5_ArrayLengthAccess(Expression):

    pass
class Java5_ParenthesizedExpression(Expression):

    pass
class Java5_BooleanLiteral(Expression):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class Java5_CastExpression(Expression):

    pass
class Java5_NullLiteral(Expression):

    pass
class Java5_SuperFieldAccess(Expression):

    pass
class Java5_ThisExpression(Expression):

    pass
class Java5_ArrayAccess(Expression):

    pass
class Java5_StringLiteral(Expression):

    def __init__(self, escapedValue: str, value: str):
        self.escapedValue = escapedValue
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def escapedValue(self) -> str:
        return self.__escapedValue

    @escapedValue.setter
    def escapedValue(self, escapedValue: str):
        self.__escapedValue = escapedValue

class Java5_SuperMethodInvocation(Expression):

    pass
class Java5_ArrayInitializer(Expression):

    pass
class Java5_CharacterLiteral(Expression):

    def __init__(self, escapedValue: str, value: str):
        self.escapedValue = escapedValue
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def escapedValue(self) -> str:
        return self.__escapedValue

    @escapedValue.setter
    def escapedValue(self, escapedValue: str):
        self.__escapedValue = escapedValue

class Java5_Annotation(Expression):

    pass
class Java5_InfixExpression(Expression):

    def __init__(self, operator: str, Java5_InfixExpression162: set["Java5_Expression"] = None, Java5_InfixExpression: "Java5_Expression" = None, Java5_InfixExpression159: "Java5_Expression" = None):
        self.operator = operator
        self.Java5_InfixExpression162 = Java5_InfixExpression162 if Java5_InfixExpression162 is not None else set()
        self.Java5_InfixExpression = Java5_InfixExpression
        self.Java5_InfixExpression159 = Java5_InfixExpression159
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def Java5_InfixExpression159(self):
        return self.__Java5_InfixExpression159

    @Java5_InfixExpression159.setter
    def Java5_InfixExpression159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_InfixExpression__Java5_InfixExpression159", None)
        self.__Java5_InfixExpression159 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Java5_Expression160"):
                opp_val = getattr(old_value, "Java5_Expression160", None)
                if opp_val == self:
                    setattr(old_value, "Java5_Expression160", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Java5_Expression160"):
                opp_val = getattr(value, "Java5_Expression160", None)
                setattr(value, "Java5_Expression160", self)

    @property
    def Java5_InfixExpression(self):
        return self.__Java5_InfixExpression

    @Java5_InfixExpression.setter
    def Java5_InfixExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_InfixExpression__Java5_InfixExpression", None)
        self.__Java5_InfixExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Java5_Expression157"):
                opp_val = getattr(old_value, "Java5_Expression157", None)
                if opp_val == self:
                    setattr(old_value, "Java5_Expression157", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Java5_Expression157"):
                opp_val = getattr(value, "Java5_Expression157", None)
                setattr(value, "Java5_Expression157", self)

    @property
    def Java5_InfixExpression162(self):
        return self.__Java5_InfixExpression162

    @Java5_InfixExpression162.setter
    def Java5_InfixExpression162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_InfixExpression__Java5_InfixExpression162", None)
        self.__Java5_InfixExpression162 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Java5_Expression163"):
                    opp_val = getattr(item, "Java5_Expression163", None)
                    
                    if opp_val == self:
                        setattr(item, "Java5_Expression163", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Java5_Expression163"):
                    opp_val = getattr(item, "Java5_Expression163", None)
                    
                    setattr(item, "Java5_Expression163", self)
                    

class Java5_InstanceofExpression(Expression):

    pass
class Java5_NumberLiteral(Expression):

    def __init__(self, tokenValue: str):
        self.tokenValue = tokenValue
        
    @property
    def tokenValue(self) -> str:
        return self.__tokenValue

    @tokenValue.setter
    def tokenValue(self, tokenValue: str):
        self.__tokenValue = tokenValue

class Java5_PrefixExpression(Expression):

    def __init__(self, operator: str, Java5_PrefixExpression: "Java5_Expression" = None):
        self.operator = operator
        self.Java5_PrefixExpression = Java5_PrefixExpression
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def Java5_PrefixExpression(self):
        return self.__Java5_PrefixExpression

    @Java5_PrefixExpression.setter
    def Java5_PrefixExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_PrefixExpression__Java5_PrefixExpression", None)
        self.__Java5_PrefixExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Java5_Expression251"):
                opp_val = getattr(old_value, "Java5_Expression251", None)
                if opp_val == self:
                    setattr(old_value, "Java5_Expression251", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Java5_Expression251"):
                opp_val = getattr(value, "Java5_Expression251", None)
                setattr(value, "Java5_Expression251", self)

class Java5_ArrayCreation(Expression):

    pass
class Java5_ConditionalExpression(Expression):

    pass
class Java5_ImportDeclaration(ASTNode):

    def __init__(self, static: bool, Java5_ImportDeclaration: "Java5_AbstractTypeDeclaration" = None, Java5_ImportDeclaration85: "Java5_CompilationUnit" = None, Java5_ImportDeclaration154: "Java5_NamedElementRef" = None):
        self.static = static
        self.Java5_ImportDeclaration = Java5_ImportDeclaration
        self.Java5_ImportDeclaration85 = Java5_ImportDeclaration85
        self.Java5_ImportDeclaration154 = Java5_ImportDeclaration154
        
    @property
    def static(self) -> bool:
        return self.__static

    @static.setter
    def static(self, static: bool):
        self.__static = static

    @property
    def Java5_ImportDeclaration154(self):
        return self.__Java5_ImportDeclaration154

    @Java5_ImportDeclaration154.setter
    def Java5_ImportDeclaration154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_ImportDeclaration__Java5_ImportDeclaration154", None)
        self.__Java5_ImportDeclaration154 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Java5_NamedElementRef155"):
                opp_val = getattr(old_value, "Java5_NamedElementRef155", None)
                if opp_val == self:
                    setattr(old_value, "Java5_NamedElementRef155", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Java5_NamedElementRef155"):
                opp_val = getattr(value, "Java5_NamedElementRef155", None)
                setattr(value, "Java5_NamedElementRef155", self)

    @property
    def Java5_ImportDeclaration85(self):
        return self.__Java5_ImportDeclaration85

    @Java5_ImportDeclaration85.setter
    def Java5_ImportDeclaration85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_ImportDeclaration__Java5_ImportDeclaration85", None)
        self.__Java5_ImportDeclaration85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Java5_CompilationUnit"):
                opp_val = getattr(old_value, "Java5_CompilationUnit", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Java5_CompilationUnit"):
                opp_val = getattr(value, "Java5_CompilationUnit", None)
                if opp_val is None:
                    setattr(value, "Java5_CompilationUnit", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Java5_ImportDeclaration(self):
        return self.__Java5_ImportDeclaration

    @Java5_ImportDeclaration.setter
    def Java5_ImportDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_ImportDeclaration__Java5_ImportDeclaration", None)
        self.__Java5_ImportDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Java5_AbstractTypeDeclaration"):
                opp_val = getattr(old_value, "Java5_AbstractTypeDeclaration", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Java5_AbstractTypeDeclaration"):
                opp_val = getattr(value, "Java5_AbstractTypeDeclaration", None)
                if opp_val is None:
                    setattr(value, "Java5_AbstractTypeDeclaration", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Java5_BodyDeclaration(NamedElement):

    pass
class BodyDeclaration:

    pass
class Java5_AnnotationTypeMemberDeclaration(BodyDeclaration):

    pass
class Java5_Initializer(BodyDeclaration):

    pass
class Java5_EnumConstantDeclaration(BodyDeclaration):

    pass
class Java5_FieldDeclaration(BodyDeclaration):

    pass
class Java5_MethodDeclaration(BodyDeclaration):

    def __init__(self, extraArrayDimensions: int, constructor: bool, varargs: bool, Java5_MethodDeclaration184: "Java5_NamedElementRef" = None, Java5_MethodDeclaration187: set["Java5_TypeParameter"] = None, MethodDeclaration: "Java5_MethodDeclaration" = None, redefinitions: "Java5_MethodDeclaration" = None, MethodDeclaration192: "Java5_MethodDeclaration" = None, redefinedMethodDeclaration: set["Java5_MethodDeclaration"] = None, methodDeclaration: set["Java5_SingleVariableDeclaration"] = None, Java5_MethodDeclaration: "Java5_Block" = None, Java5_MethodDeclaration181: set["Java5_NamedElementRef"] = None, MethodDeclaration260: "Java5_SingleVariableDeclaration" = None):
        self.extraArrayDimensions = extraArrayDimensions
        self.constructor = constructor
        self.varargs = varargs
        self.Java5_MethodDeclaration184 = Java5_MethodDeclaration184
        self.Java5_MethodDeclaration187 = Java5_MethodDeclaration187 if Java5_MethodDeclaration187 is not None else set()
        self.MethodDeclaration = MethodDeclaration
        self.redefinitions = redefinitions
        self.MethodDeclaration192 = MethodDeclaration192
        self.redefinedMethodDeclaration = redefinedMethodDeclaration if redefinedMethodDeclaration is not None else set()
        self.methodDeclaration = methodDeclaration if methodDeclaration is not None else set()
        self.Java5_MethodDeclaration = Java5_MethodDeclaration
        self.Java5_MethodDeclaration181 = Java5_MethodDeclaration181 if Java5_MethodDeclaration181 is not None else set()
        self.MethodDeclaration260 = MethodDeclaration260
        
    @property
    def constructor(self) -> bool:
        return self.__constructor

    @constructor.setter
    def constructor(self, constructor: bool):
        self.__constructor = constructor

    @property
    def extraArrayDimensions(self) -> int:
        return self.__extraArrayDimensions

    @extraArrayDimensions.setter
    def extraArrayDimensions(self, extraArrayDimensions: int):
        self.__extraArrayDimensions = extraArrayDimensions

    @property
    def varargs(self) -> bool:
        return self.__varargs

    @varargs.setter
    def varargs(self, varargs: bool):
        self.__varargs = varargs

    @property
    def redefinedMethodDeclaration(self):
        return self.__redefinedMethodDeclaration

    @redefinedMethodDeclaration.setter
    def redefinedMethodDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_MethodDeclaration__redefinedMethodDeclaration", None)
        self.__redefinedMethodDeclaration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MethodDeclaration192"):
                    opp_val = getattr(item, "MethodDeclaration192", None)
                    
                    if opp_val == self:
                        setattr(item, "MethodDeclaration192", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MethodDeclaration192"):
                    opp_val = getattr(item, "MethodDeclaration192", None)
                    
                    setattr(item, "MethodDeclaration192", self)
                    

    @property
    def redefinitions(self):
        return self.__redefinitions

    @redefinitions.setter
    def redefinitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_MethodDeclaration__redefinitions", None)
        self.__redefinitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MethodDeclaration"):
                opp_val = getattr(old_value, "MethodDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "MethodDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MethodDeclaration"):
                opp_val = getattr(value, "MethodDeclaration", None)
                setattr(value, "MethodDeclaration", self)

    @property
    def MethodDeclaration(self):
        return self.__MethodDeclaration

    @MethodDeclaration.setter
    def MethodDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_MethodDeclaration__MethodDeclaration", None)
        self.__MethodDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "redefinitions"):
                opp_val = getattr(old_value, "redefinitions", None)
                if opp_val == self:
                    setattr(old_value, "redefinitions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "redefinitions"):
                opp_val = getattr(value, "redefinitions", None)
                setattr(value, "redefinitions", self)

    @property
    def methodDeclaration(self):
        return self.__methodDeclaration

    @methodDeclaration.setter
    def methodDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_MethodDeclaration__methodDeclaration", None)
        self.__methodDeclaration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SingleVariableDeclaration194"):
                    opp_val = getattr(item, "SingleVariableDeclaration194", None)
                    
                    if opp_val == self:
                        setattr(item, "SingleVariableDeclaration194", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SingleVariableDeclaration194"):
                    opp_val = getattr(item, "SingleVariableDeclaration194", None)
                    
                    setattr(item, "SingleVariableDeclaration194", self)
                    

    @property
    def Java5_MethodDeclaration184(self):
        return self.__Java5_MethodDeclaration184

    @Java5_MethodDeclaration184.setter
    def Java5_MethodDeclaration184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_MethodDeclaration__Java5_MethodDeclaration184", None)
        self.__Java5_MethodDeclaration184 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Java5_NamedElementRef185"):
                opp_val = getattr(old_value, "Java5_NamedElementRef185", None)
                if opp_val == self:
                    setattr(old_value, "Java5_NamedElementRef185", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Java5_NamedElementRef185"):
                opp_val = getattr(value, "Java5_NamedElementRef185", None)
                setattr(value, "Java5_NamedElementRef185", self)

    @property
    def Java5_MethodDeclaration(self):
        return self.__Java5_MethodDeclaration

    @Java5_MethodDeclaration.setter
    def Java5_MethodDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_MethodDeclaration__Java5_MethodDeclaration", None)
        self.__Java5_MethodDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Java5_Block179"):
                opp_val = getattr(old_value, "Java5_Block179", None)
                if opp_val == self:
                    setattr(old_value, "Java5_Block179", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Java5_Block179"):
                opp_val = getattr(value, "Java5_Block179", None)
                setattr(value, "Java5_Block179", self)

    @property
    def MethodDeclaration260(self):
        return self.__MethodDeclaration260

    @MethodDeclaration260.setter
    def MethodDeclaration260(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_MethodDeclaration__MethodDeclaration260", None)
        self.__MethodDeclaration260 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parameters"):
                opp_val = getattr(old_value, "parameters", None)
                if opp_val == self:
                    setattr(old_value, "parameters", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parameters"):
                opp_val = getattr(value, "parameters", None)
                setattr(value, "parameters", self)

    @property
    def Java5_MethodDeclaration181(self):
        return self.__Java5_MethodDeclaration181

    @Java5_MethodDeclaration181.setter
    def Java5_MethodDeclaration181(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_MethodDeclaration__Java5_MethodDeclaration181", None)
        self.__Java5_MethodDeclaration181 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Java5_NamedElementRef182"):
                    opp_val = getattr(item, "Java5_NamedElementRef182", None)
                    
                    if opp_val == self:
                        setattr(item, "Java5_NamedElementRef182", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Java5_NamedElementRef182"):
                    opp_val = getattr(item, "Java5_NamedElementRef182", None)
                    
                    setattr(item, "Java5_NamedElementRef182", self)
                    

    @property
    def MethodDeclaration192(self):
        return self.__MethodDeclaration192

    @MethodDeclaration192.setter
    def MethodDeclaration192(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_MethodDeclaration__MethodDeclaration192", None)
        self.__MethodDeclaration192 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "redefinedMethodDeclaration"):
                opp_val = getattr(old_value, "redefinedMethodDeclaration", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "redefinedMethodDeclaration"):
                opp_val = getattr(value, "redefinedMethodDeclaration", None)
                if opp_val is None:
                    setattr(value, "redefinedMethodDeclaration", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Java5_MethodDeclaration187(self):
        return self.__Java5_MethodDeclaration187

    @Java5_MethodDeclaration187.setter
    def Java5_MethodDeclaration187(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_MethodDeclaration__Java5_MethodDeclaration187", None)
        self.__Java5_MethodDeclaration187 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Java5_TypeParameter"):
                    opp_val = getattr(item, "Java5_TypeParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "Java5_TypeParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Java5_TypeParameter"):
                    opp_val = getattr(item, "Java5_TypeParameter", None)
                    
                    setattr(item, "Java5_TypeParameter", self)
                    

class Java5_AbstractTypeDeclaration(BodyDeclaration):

    def __init__(self, qualifiedName: str, abstractTypeDeclaration: set["Java5_BodyDeclaration"] = None, Java5_AbstractTypeDeclaration: set["Java5_ImportDeclaration"] = None, ownedElements: "Java5_PackageDeclaration" = None, Java5_AbstractTypeDeclaration4: set["Java5_NamedElementRef"] = None, AbstractTypeDeclaration: "Java5_BodyDeclaration" = None, Java5_AbstractTypeDeclaration90: "Java5_CompilationUnit" = None, AbstractTypeDeclaration237: "Java5_PackageDeclaration" = None, Java5_AbstractTypeDeclaration304: "Java5_TypeDeclarationStatement" = None):
        self.qualifiedName = qualifiedName
        self.abstractTypeDeclaration = abstractTypeDeclaration if abstractTypeDeclaration is not None else set()
        self.Java5_AbstractTypeDeclaration = Java5_AbstractTypeDeclaration if Java5_AbstractTypeDeclaration is not None else set()
        self.ownedElements = ownedElements
        self.Java5_AbstractTypeDeclaration4 = Java5_AbstractTypeDeclaration4 if Java5_AbstractTypeDeclaration4 is not None else set()
        self.AbstractTypeDeclaration = AbstractTypeDeclaration
        self.Java5_AbstractTypeDeclaration90 = Java5_AbstractTypeDeclaration90
        self.AbstractTypeDeclaration237 = AbstractTypeDeclaration237
        self.Java5_AbstractTypeDeclaration304 = Java5_AbstractTypeDeclaration304
        
    @property
    def qualifiedName(self) -> str:
        return self.__qualifiedName

    @qualifiedName.setter
    def qualifiedName(self, qualifiedName: str):
        self.__qualifiedName = qualifiedName

    @property
    def Java5_AbstractTypeDeclaration90(self):
        return self.__Java5_AbstractTypeDeclaration90

    @Java5_AbstractTypeDeclaration90.setter
    def Java5_AbstractTypeDeclaration90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_AbstractTypeDeclaration__Java5_AbstractTypeDeclaration90", None)
        self.__Java5_AbstractTypeDeclaration90 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Java5_CompilationUnit89"):
                opp_val = getattr(old_value, "Java5_CompilationUnit89", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Java5_CompilationUnit89"):
                opp_val = getattr(value, "Java5_CompilationUnit89", None)
                if opp_val is None:
                    setattr(value, "Java5_CompilationUnit89", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def AbstractTypeDeclaration(self):
        return self.__AbstractTypeDeclaration

    @AbstractTypeDeclaration.setter
    def AbstractTypeDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_AbstractTypeDeclaration__AbstractTypeDeclaration", None)
        self.__AbstractTypeDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bodyDeclarations"):
                opp_val = getattr(old_value, "bodyDeclarations", None)
                if opp_val == self:
                    setattr(old_value, "bodyDeclarations", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bodyDeclarations"):
                opp_val = getattr(value, "bodyDeclarations", None)
                setattr(value, "bodyDeclarations", self)

    @property
    def ownedElements(self):
        return self.__ownedElements

    @ownedElements.setter
    def ownedElements(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_AbstractTypeDeclaration__ownedElements", None)
        self.__ownedElements = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PackageDeclaration"):
                opp_val = getattr(old_value, "PackageDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "PackageDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PackageDeclaration"):
                opp_val = getattr(value, "PackageDeclaration", None)
                setattr(value, "PackageDeclaration", self)

    @property
    def abstractTypeDeclaration(self):
        return self.__abstractTypeDeclaration

    @abstractTypeDeclaration.setter
    def abstractTypeDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_AbstractTypeDeclaration__abstractTypeDeclaration", None)
        self.__abstractTypeDeclaration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BodyDeclaration"):
                    opp_val = getattr(item, "BodyDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "BodyDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BodyDeclaration"):
                    opp_val = getattr(item, "BodyDeclaration", None)
                    
                    setattr(item, "BodyDeclaration", self)
                    

    @property
    def Java5_AbstractTypeDeclaration4(self):
        return self.__Java5_AbstractTypeDeclaration4

    @Java5_AbstractTypeDeclaration4.setter
    def Java5_AbstractTypeDeclaration4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_AbstractTypeDeclaration__Java5_AbstractTypeDeclaration4", None)
        self.__Java5_AbstractTypeDeclaration4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Java5_NamedElementRef"):
                    opp_val = getattr(item, "Java5_NamedElementRef", None)
                    
                    if opp_val == self:
                        setattr(item, "Java5_NamedElementRef", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Java5_NamedElementRef"):
                    opp_val = getattr(item, "Java5_NamedElementRef", None)
                    
                    setattr(item, "Java5_NamedElementRef", self)
                    

    @property
    def AbstractTypeDeclaration237(self):
        return self.__AbstractTypeDeclaration237

    @AbstractTypeDeclaration237.setter
    def AbstractTypeDeclaration237(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_AbstractTypeDeclaration__AbstractTypeDeclaration237", None)
        self.__AbstractTypeDeclaration237 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "package"):
                opp_val = getattr(old_value, "package", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "package"):
                opp_val = getattr(value, "package", None)
                if opp_val is None:
                    setattr(value, "package", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Java5_AbstractTypeDeclaration304(self):
        return self.__Java5_AbstractTypeDeclaration304

    @Java5_AbstractTypeDeclaration304.setter
    def Java5_AbstractTypeDeclaration304(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_AbstractTypeDeclaration__Java5_AbstractTypeDeclaration304", None)
        self.__Java5_AbstractTypeDeclaration304 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Java5_TypeDeclarationStatement"):
                opp_val = getattr(old_value, "Java5_TypeDeclarationStatement", None)
                if opp_val == self:
                    setattr(old_value, "Java5_TypeDeclarationStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Java5_TypeDeclarationStatement"):
                opp_val = getattr(value, "Java5_TypeDeclarationStatement", None)
                setattr(value, "Java5_TypeDeclarationStatement", self)

    @property
    def Java5_AbstractTypeDeclaration(self):
        return self.__Java5_AbstractTypeDeclaration

    @Java5_AbstractTypeDeclaration.setter
    def Java5_AbstractTypeDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Java5_AbstractTypeDeclaration__Java5_AbstractTypeDeclaration", None)
        self.__Java5_AbstractTypeDeclaration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Java5_ImportDeclaration"):
                    opp_val = getattr(item, "Java5_ImportDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "Java5_ImportDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Java5_ImportDeclaration"):
                    opp_val = getattr(item, "Java5_ImportDeclaration", None)
                    
                    setattr(item, "Java5_ImportDeclaration", self)
                    
