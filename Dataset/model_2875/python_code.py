from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Extension:

    pass
class xpand3_declaration_CreateExtension(Extension):

    pass
class AbstractAspect:

    pass
class xpand3_declaration_DefinitionAspect(AbstractAspect):

    pass
class xpand3_declaration_ExtensionAspect(AbstractAspect):

    pass
class AbstractNamedDeclaration:

    pass
class xpand3_declaration_JavaExtension(AbstractNamedDeclaration):

    pass
class xpand3_declaration_Definition(AbstractNamedDeclaration):

    pass
class declaration_xpand3_Identifier:

    pass
class declaration_xpand3_DeclaredParameter:

    pass
class declaration_xpand3_File:

    pass
class xpand3_declaration_Extension(AbstractNamedDeclaration):

    def __init__(self, cached: bool, xpand3_declaration_Extension: "AbstractExpression" = None, xpand3_declaration_Extension141: "declaration_xpand3_Identifier" = None):
        self.cached = cached
        self.xpand3_declaration_Extension = xpand3_declaration_Extension
        self.xpand3_declaration_Extension141 = xpand3_declaration_Extension141
        
    @property
    def cached(self) -> bool:
        return self.__cached

    @cached.setter
    def cached(self, cached: bool):
        self.__cached = cached

    @property
    def xpand3_declaration_Extension(self):
        return self.__xpand3_declaration_Extension

    @xpand3_declaration_Extension.setter
    def xpand3_declaration_Extension(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpand3_declaration_Extension__xpand3_declaration_Extension", None)
        self.__xpand3_declaration_Extension = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AbstractExpression139"):
                opp_val = getattr(old_value, "AbstractExpression139", None)
                if opp_val == self:
                    setattr(old_value, "AbstractExpression139", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AbstractExpression139"):
                opp_val = getattr(value, "AbstractExpression139", None)
                setattr(value, "AbstractExpression139", self)

    @property
    def xpand3_declaration_Extension141(self):
        return self.__xpand3_declaration_Extension141

    @xpand3_declaration_Extension141.setter
    def xpand3_declaration_Extension141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpand3_declaration_Extension__xpand3_declaration_Extension141", None)
        self.__xpand3_declaration_Extension141 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "declaration_xpand3_Identifier142"):
                opp_val = getattr(old_value, "declaration_xpand3_Identifier142", None)
                if opp_val == self:
                    setattr(old_value, "declaration_xpand3_Identifier142", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "declaration_xpand3_Identifier142"):
                opp_val = getattr(value, "declaration_xpand3_Identifier142", None)
                setattr(value, "declaration_xpand3_Identifier142", self)

class IfStatement:

    pass
class statement_xpand3_Identifier:

    pass
class AbstractStatementWithBody:

    pass
class xpand3_statement_ForEachStatement(AbstractStatementWithBody):

    pass
class xpand3_statement_ProtectStatement(AbstractStatementWithBody):

    def __init__(self, disable: bool, xpand3_statement_ProtectStatement: "AbstractExpression" = None, xpand3_statement_ProtectStatement124: "AbstractExpression" = None, xpand3_statement_ProtectStatement127: "AbstractExpression" = None):
        self.disable = disable
        self.xpand3_statement_ProtectStatement = xpand3_statement_ProtectStatement
        self.xpand3_statement_ProtectStatement124 = xpand3_statement_ProtectStatement124
        self.xpand3_statement_ProtectStatement127 = xpand3_statement_ProtectStatement127
        
    @property
    def disable(self) -> bool:
        return self.__disable

    @disable.setter
    def disable(self, disable: bool):
        self.__disable = disable

    @property
    def xpand3_statement_ProtectStatement127(self):
        return self.__xpand3_statement_ProtectStatement127

    @xpand3_statement_ProtectStatement127.setter
    def xpand3_statement_ProtectStatement127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpand3_statement_ProtectStatement__xpand3_statement_ProtectStatement127", None)
        self.__xpand3_statement_ProtectStatement127 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AbstractExpression128"):
                opp_val = getattr(old_value, "AbstractExpression128", None)
                if opp_val == self:
                    setattr(old_value, "AbstractExpression128", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AbstractExpression128"):
                opp_val = getattr(value, "AbstractExpression128", None)
                setattr(value, "AbstractExpression128", self)

    @property
    def xpand3_statement_ProtectStatement(self):
        return self.__xpand3_statement_ProtectStatement

    @xpand3_statement_ProtectStatement.setter
    def xpand3_statement_ProtectStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpand3_statement_ProtectStatement__xpand3_statement_ProtectStatement", None)
        self.__xpand3_statement_ProtectStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AbstractExpression122"):
                opp_val = getattr(old_value, "AbstractExpression122", None)
                if opp_val == self:
                    setattr(old_value, "AbstractExpression122", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AbstractExpression122"):
                opp_val = getattr(value, "AbstractExpression122", None)
                setattr(value, "AbstractExpression122", self)

    @property
    def xpand3_statement_ProtectStatement124(self):
        return self.__xpand3_statement_ProtectStatement124

    @xpand3_statement_ProtectStatement124.setter
    def xpand3_statement_ProtectStatement124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpand3_statement_ProtectStatement__xpand3_statement_ProtectStatement124", None)
        self.__xpand3_statement_ProtectStatement124 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AbstractExpression125"):
                opp_val = getattr(old_value, "AbstractExpression125", None)
                if opp_val == self:
                    setattr(old_value, "AbstractExpression125", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AbstractExpression125"):
                opp_val = getattr(value, "AbstractExpression125", None)
                setattr(value, "AbstractExpression125", self)

class xpand3_statement_LetStatement(AbstractStatementWithBody):

    pass
class xpand3_statement_IfStatement(AbstractStatementWithBody):

    pass
class xpand3_statement_FileStatement(AbstractStatementWithBody):

    def __init__(self, once: bool, xpand3_statement_FileStatement: "AbstractExpression" = None, xpand3_statement_FileStatement99: "statement_xpand3_Identifier" = None):
        self.once = once
        self.xpand3_statement_FileStatement = xpand3_statement_FileStatement
        self.xpand3_statement_FileStatement99 = xpand3_statement_FileStatement99
        
    @property
    def once(self) -> bool:
        return self.__once

    @once.setter
    def once(self, once: bool):
        self.__once = once

    @property
    def xpand3_statement_FileStatement99(self):
        return self.__xpand3_statement_FileStatement99

    @xpand3_statement_FileStatement99.setter
    def xpand3_statement_FileStatement99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpand3_statement_FileStatement__xpand3_statement_FileStatement99", None)
        self.__xpand3_statement_FileStatement99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statement_xpand3_Identifier100"):
                opp_val = getattr(old_value, "statement_xpand3_Identifier100", None)
                if opp_val == self:
                    setattr(old_value, "statement_xpand3_Identifier100", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statement_xpand3_Identifier100"):
                opp_val = getattr(value, "statement_xpand3_Identifier100", None)
                setattr(value, "statement_xpand3_Identifier100", self)

    @property
    def xpand3_statement_FileStatement(self):
        return self.__xpand3_statement_FileStatement

    @xpand3_statement_FileStatement.setter
    def xpand3_statement_FileStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpand3_statement_FileStatement__xpand3_statement_FileStatement", None)
        self.__xpand3_statement_FileStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AbstractExpression97"):
                opp_val = getattr(old_value, "AbstractExpression97", None)
                if opp_val == self:
                    setattr(old_value, "AbstractExpression97", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AbstractExpression97"):
                opp_val = getattr(value, "AbstractExpression97", None)
                setattr(value, "AbstractExpression97", self)

class AbstractStatement:

    pass
class xpand3_statement_ExpressionStatement(AbstractStatement):

    pass
class xpand3_statement_TextStatement(AbstractStatement):

    def __init__(self, value: str, deleteLine: bool, AbstractStatement: "xpand3_statement_AbstractStatementWithBody", AbstractStatement148: "xpand3_declaration_DefinitionAspect", AbstractStatement137: "xpand3_declaration_Definition"):
        self.value = value
        self.deleteLine = deleteLine
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def deleteLine(self) -> bool:
        return self.__deleteLine

    @deleteLine.setter
    def deleteLine(self, deleteLine: bool):
        self.__deleteLine = deleteLine

class xpand3_statement_ErrorStatement(AbstractStatement):

    pass
class xpand3_statement_AbstractStatementWithBody(AbstractStatement):

    pass
class xpand3_statement_ExpandStatement(AbstractStatement):

    def __init__(self, foreach: bool, xpand3_statement_ExpandStatement: set["AbstractExpression"] = None, xpand3_statement_ExpandStatement84: "AbstractExpression" = None, xpand3_statement_ExpandStatement87: "AbstractExpression" = None, xpand3_statement_ExpandStatement90: "statement_xpand3_Identifier" = None, AbstractStatement: "xpand3_statement_AbstractStatementWithBody", AbstractStatement148: "xpand3_declaration_DefinitionAspect", AbstractStatement137: "xpand3_declaration_Definition"):
        self.foreach = foreach
        self.xpand3_statement_ExpandStatement = xpand3_statement_ExpandStatement if xpand3_statement_ExpandStatement is not None else set()
        self.xpand3_statement_ExpandStatement84 = xpand3_statement_ExpandStatement84
        self.xpand3_statement_ExpandStatement87 = xpand3_statement_ExpandStatement87
        self.xpand3_statement_ExpandStatement90 = xpand3_statement_ExpandStatement90
        
    @property
    def foreach(self) -> bool:
        return self.__foreach

    @foreach.setter
    def foreach(self, foreach: bool):
        self.__foreach = foreach

    @property
    def xpand3_statement_ExpandStatement(self):
        return self.__xpand3_statement_ExpandStatement

    @xpand3_statement_ExpandStatement.setter
    def xpand3_statement_ExpandStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpand3_statement_ExpandStatement__xpand3_statement_ExpandStatement", None)
        self.__xpand3_statement_ExpandStatement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AbstractExpression82"):
                    opp_val = getattr(item, "AbstractExpression82", None)
                    
                    if opp_val == self:
                        setattr(item, "AbstractExpression82", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AbstractExpression82"):
                    opp_val = getattr(item, "AbstractExpression82", None)
                    
                    setattr(item, "AbstractExpression82", self)
                    

    @property
    def xpand3_statement_ExpandStatement84(self):
        return self.__xpand3_statement_ExpandStatement84

    @xpand3_statement_ExpandStatement84.setter
    def xpand3_statement_ExpandStatement84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpand3_statement_ExpandStatement__xpand3_statement_ExpandStatement84", None)
        self.__xpand3_statement_ExpandStatement84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AbstractExpression85"):
                opp_val = getattr(old_value, "AbstractExpression85", None)
                if opp_val == self:
                    setattr(old_value, "AbstractExpression85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AbstractExpression85"):
                opp_val = getattr(value, "AbstractExpression85", None)
                setattr(value, "AbstractExpression85", self)

    @property
    def xpand3_statement_ExpandStatement87(self):
        return self.__xpand3_statement_ExpandStatement87

    @xpand3_statement_ExpandStatement87.setter
    def xpand3_statement_ExpandStatement87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpand3_statement_ExpandStatement__xpand3_statement_ExpandStatement87", None)
        self.__xpand3_statement_ExpandStatement87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AbstractExpression88"):
                opp_val = getattr(old_value, "AbstractExpression88", None)
                if opp_val == self:
                    setattr(old_value, "AbstractExpression88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AbstractExpression88"):
                opp_val = getattr(value, "AbstractExpression88", None)
                setattr(value, "AbstractExpression88", self)

    @property
    def xpand3_statement_ExpandStatement90(self):
        return self.__xpand3_statement_ExpandStatement90

    @xpand3_statement_ExpandStatement90.setter
    def xpand3_statement_ExpandStatement90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpand3_statement_ExpandStatement__xpand3_statement_ExpandStatement90", None)
        self.__xpand3_statement_ExpandStatement90 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statement_xpand3_Identifier"):
                opp_val = getattr(old_value, "statement_xpand3_Identifier", None)
                if opp_val == self:
                    setattr(old_value, "statement_xpand3_Identifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statement_xpand3_Identifier"):
                opp_val = getattr(value, "statement_xpand3_Identifier", None)
                setattr(value, "statement_xpand3_Identifier", self)

class Case:

    pass
class Literal:

    pass
class xpand3_expression_StringLiteral(Literal):

    pass
class xpand3_expression_BooleanLiteral(Literal):

    pass
class xpand3_expression_RealLiteral(Literal):

    pass
class xpand3_expression_NullLiteral(Literal):

    pass
class xpand3_expression_IntegerLiteral(Literal):

    pass
class expression_xpand3_Identifier:

    pass
class FeatureCall:

    pass
class xpand3_expression_TypeSelectExpression(FeatureCall):

    pass
class xpand3_expression_OperationCall(FeatureCall):

    pass
class xpand3_expression_CollectionExpression(FeatureCall):

    pass
class AbstractDeclaration:

    pass
class xpand3_declaration_AbstractNamedDeclaration(AbstractDeclaration):

    pass
class xpand3_declaration_AbstractAspect(AbstractDeclaration):

    def __init__(self, wildparams: bool, xpand3_declaration_AbstractAspect: "declaration_xpand3_Identifier" = None, AbstractDeclaration: "xpand3_File"):
        self.wildparams = wildparams
        self.xpand3_declaration_AbstractAspect = xpand3_declaration_AbstractAspect
        
    @property
    def wildparams(self) -> bool:
        return self.__wildparams

    @wildparams.setter
    def wildparams(self, wildparams: bool):
        self.__wildparams = wildparams

    @property
    def xpand3_declaration_AbstractAspect(self):
        return self.__xpand3_declaration_AbstractAspect

    @xpand3_declaration_AbstractAspect.setter
    def xpand3_declaration_AbstractAspect(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpand3_declaration_AbstractAspect__xpand3_declaration_AbstractAspect", None)
        self.__xpand3_declaration_AbstractAspect = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "declaration_xpand3_Identifier144"):
                opp_val = getattr(old_value, "declaration_xpand3_Identifier144", None)
                if opp_val == self:
                    setattr(old_value, "declaration_xpand3_Identifier144", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "declaration_xpand3_Identifier144"):
                opp_val = getattr(value, "declaration_xpand3_Identifier144", None)
                setattr(value, "declaration_xpand3_Identifier144", self)

class xpand3_declaration_Check(AbstractDeclaration):

    def __init__(self, errorSeverity: bool, feature: str, xpand3_declaration_Check: "AbstractExpression" = None, xpand3_declaration_Check152: "AbstractExpression" = None, AbstractDeclaration: "xpand3_File"):
        self.errorSeverity = errorSeverity
        self.feature = feature
        self.xpand3_declaration_Check = xpand3_declaration_Check
        self.xpand3_declaration_Check152 = xpand3_declaration_Check152
        
    @property
    def feature(self) -> str:
        return self.__feature

    @feature.setter
    def feature(self, feature: str):
        self.__feature = feature

    @property
    def errorSeverity(self) -> bool:
        return self.__errorSeverity

    @errorSeverity.setter
    def errorSeverity(self, errorSeverity: bool):
        self.__errorSeverity = errorSeverity

    @property
    def xpand3_declaration_Check(self):
        return self.__xpand3_declaration_Check

    @xpand3_declaration_Check.setter
    def xpand3_declaration_Check(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpand3_declaration_Check__xpand3_declaration_Check", None)
        self.__xpand3_declaration_Check = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AbstractExpression150"):
                opp_val = getattr(old_value, "AbstractExpression150", None)
                if opp_val == self:
                    setattr(old_value, "AbstractExpression150", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AbstractExpression150"):
                opp_val = getattr(value, "AbstractExpression150", None)
                setattr(value, "AbstractExpression150", self)

    @property
    def xpand3_declaration_Check152(self):
        return self.__xpand3_declaration_Check152

    @xpand3_declaration_Check152.setter
    def xpand3_declaration_Check152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpand3_declaration_Check__xpand3_declaration_Check152", None)
        self.__xpand3_declaration_Check152 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AbstractExpression153"):
                opp_val = getattr(old_value, "AbstractExpression153", None)
                if opp_val == self:
                    setattr(old_value, "AbstractExpression153", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AbstractExpression153"):
                opp_val = getattr(value, "AbstractExpression153", None)
                setattr(value, "AbstractExpression153", self)

class AbstractExpression:

    pass
class xpand3_expression_ChainExpression(AbstractExpression):

    pass
class xpand3_expression_BinaryOperation(AbstractExpression):

    pass
class xpand3_expression_ConstructorCallExpression(AbstractExpression):

    pass
class xpand3_expression_IfExpression(AbstractExpression):

    pass
class xpand3_expression_SwitchExpression(AbstractExpression):

    pass
class xpand3_expression_LetExpression(AbstractExpression):

    pass
class xpand3_expression_UnaryOperation(AbstractExpression):

    pass
class xpand3_expression_FeatureCall(AbstractExpression):

    pass
class xpand3_expression_ListLiteral(AbstractExpression):

    pass
class xpand3_expression_GlobalVarExpression(AbstractExpression):

    pass
class xpand3_expression_Literal(AbstractExpression):

    pass
class xpand3_expression_Cast(AbstractExpression):

    pass
class BinaryOperation:

    pass
class xpand3_expression_BooleanOperation(BinaryOperation):

    pass
class xpand3_SyntaxElement(ABC):

    def __init__(self, start: int, end: int, fileName: str, line: int):
        self.start = start
        self.end = end
        self.fileName = fileName
        self.line = line
        
    @property
    def line(self) -> int:
        return self.__line

    @line.setter
    def line(self, line: int):
        self.__line = line

    @property
    def start(self) -> int:
        return self.__start

    @start.setter
    def start(self, start: int):
        self.__start = start

    @property
    def end(self) -> int:
        return self.__end

    @end.setter
    def end(self, end: int):
        self.__end = end

    @property
    def fileName(self) -> str:
        return self.__fileName

    @fileName.setter
    def fileName(self, fileName: str):
        self.__fileName = fileName

class SyntaxElement:

    pass
class xpand3_ImportStatement(SyntaxElement):

    def __init__(self, exported: bool, xpand3_ImportStatement: "xpand3_File" = None, xpand3_ImportStatement4: "xpand3_Identifier" = None):
        self.exported = exported
        self.xpand3_ImportStatement = xpand3_ImportStatement
        self.xpand3_ImportStatement4 = xpand3_ImportStatement4
        
    @property
    def exported(self) -> bool:
        return self.__exported

    @exported.setter
    def exported(self, exported: bool):
        self.__exported = exported

    @property
    def xpand3_ImportStatement4(self):
        return self.__xpand3_ImportStatement4

    @xpand3_ImportStatement4.setter
    def xpand3_ImportStatement4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpand3_ImportStatement__xpand3_ImportStatement4", None)
        self.__xpand3_ImportStatement4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpand3_Identifier"):
                opp_val = getattr(old_value, "xpand3_Identifier", None)
                if opp_val == self:
                    setattr(old_value, "xpand3_Identifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpand3_Identifier"):
                opp_val = getattr(value, "xpand3_Identifier", None)
                setattr(value, "xpand3_Identifier", self)

    @property
    def xpand3_ImportStatement(self):
        return self.__xpand3_ImportStatement

    @xpand3_ImportStatement.setter
    def xpand3_ImportStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpand3_ImportStatement__xpand3_ImportStatement", None)
        self.__xpand3_ImportStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpand3_File"):
                opp_val = getattr(old_value, "xpand3_File", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpand3_File"):
                opp_val = getattr(value, "xpand3_File", None)
                if opp_val is None:
                    setattr(value, "xpand3_File", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xpand3_DeclaredParameter(SyntaxElement):

    pass
class xpand3_statement_AbstractStatement(SyntaxElement):

    pass
class xpand3_Identifier(SyntaxElement):

    def __init__(self, value: str, xpand3_Identifier: "xpand3_ImportStatement" = None, xpand3_Identifier6: "xpand3_DeclaredParameter" = None, xpand3_Identifier9: "xpand3_DeclaredParameter" = None):
        self.value = value
        self.xpand3_Identifier = xpand3_Identifier
        self.xpand3_Identifier6 = xpand3_Identifier6
        self.xpand3_Identifier9 = xpand3_Identifier9
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def xpand3_Identifier9(self):
        return self.__xpand3_Identifier9

    @xpand3_Identifier9.setter
    def xpand3_Identifier9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpand3_Identifier__xpand3_Identifier9", None)
        self.__xpand3_Identifier9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpand3_DeclaredParameter8"):
                opp_val = getattr(old_value, "xpand3_DeclaredParameter8", None)
                if opp_val == self:
                    setattr(old_value, "xpand3_DeclaredParameter8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpand3_DeclaredParameter8"):
                opp_val = getattr(value, "xpand3_DeclaredParameter8", None)
                setattr(value, "xpand3_DeclaredParameter8", self)

    @property
    def xpand3_Identifier6(self):
        return self.__xpand3_Identifier6

    @xpand3_Identifier6.setter
    def xpand3_Identifier6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpand3_Identifier__xpand3_Identifier6", None)
        self.__xpand3_Identifier6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpand3_DeclaredParameter"):
                opp_val = getattr(old_value, "xpand3_DeclaredParameter", None)
                if opp_val == self:
                    setattr(old_value, "xpand3_DeclaredParameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpand3_DeclaredParameter"):
                opp_val = getattr(value, "xpand3_DeclaredParameter", None)
                setattr(value, "xpand3_DeclaredParameter", self)

    @property
    def xpand3_Identifier(self):
        return self.__xpand3_Identifier

    @xpand3_Identifier.setter
    def xpand3_Identifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpand3_Identifier__xpand3_Identifier", None)
        self.__xpand3_Identifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xpand3_ImportStatement4"):
                opp_val = getattr(old_value, "xpand3_ImportStatement4", None)
                if opp_val == self:
                    setattr(old_value, "xpand3_ImportStatement4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xpand3_ImportStatement4"):
                opp_val = getattr(value, "xpand3_ImportStatement4", None)
                setattr(value, "xpand3_ImportStatement4", self)

class xpand3_expression_Case(SyntaxElement):

    pass
class xpand3_declaration_AbstractDeclaration(SyntaxElement):

    def __init__(self, isPrivate: bool, xpand3_declaration_AbstractDeclaration: "declaration_xpand3_File" = None, xpand3_declaration_AbstractDeclaration131: set["declaration_xpand3_DeclaredParameter"] = None, xpand3_declaration_AbstractDeclaration133: "AbstractExpression" = None):
        self.isPrivate = isPrivate
        self.xpand3_declaration_AbstractDeclaration = xpand3_declaration_AbstractDeclaration
        self.xpand3_declaration_AbstractDeclaration131 = xpand3_declaration_AbstractDeclaration131 if xpand3_declaration_AbstractDeclaration131 is not None else set()
        self.xpand3_declaration_AbstractDeclaration133 = xpand3_declaration_AbstractDeclaration133
        
    @property
    def isPrivate(self) -> bool:
        return self.__isPrivate

    @isPrivate.setter
    def isPrivate(self, isPrivate: bool):
        self.__isPrivate = isPrivate

    @property
    def xpand3_declaration_AbstractDeclaration133(self):
        return self.__xpand3_declaration_AbstractDeclaration133

    @xpand3_declaration_AbstractDeclaration133.setter
    def xpand3_declaration_AbstractDeclaration133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpand3_declaration_AbstractDeclaration__xpand3_declaration_AbstractDeclaration133", None)
        self.__xpand3_declaration_AbstractDeclaration133 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AbstractExpression134"):
                opp_val = getattr(old_value, "AbstractExpression134", None)
                if opp_val == self:
                    setattr(old_value, "AbstractExpression134", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AbstractExpression134"):
                opp_val = getattr(value, "AbstractExpression134", None)
                setattr(value, "AbstractExpression134", self)

    @property
    def xpand3_declaration_AbstractDeclaration131(self):
        return self.__xpand3_declaration_AbstractDeclaration131

    @xpand3_declaration_AbstractDeclaration131.setter
    def xpand3_declaration_AbstractDeclaration131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpand3_declaration_AbstractDeclaration__xpand3_declaration_AbstractDeclaration131", None)
        self.__xpand3_declaration_AbstractDeclaration131 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "declaration_xpand3_DeclaredParameter"):
                    opp_val = getattr(item, "declaration_xpand3_DeclaredParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "declaration_xpand3_DeclaredParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "declaration_xpand3_DeclaredParameter"):
                    opp_val = getattr(item, "declaration_xpand3_DeclaredParameter", None)
                    
                    setattr(item, "declaration_xpand3_DeclaredParameter", self)
                    

    @property
    def xpand3_declaration_AbstractDeclaration(self):
        return self.__xpand3_declaration_AbstractDeclaration

    @xpand3_declaration_AbstractDeclaration.setter
    def xpand3_declaration_AbstractDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xpand3_declaration_AbstractDeclaration__xpand3_declaration_AbstractDeclaration", None)
        self.__xpand3_declaration_AbstractDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "declaration_xpand3_File"):
                opp_val = getattr(old_value, "declaration_xpand3_File", None)
                if opp_val == self:
                    setattr(old_value, "declaration_xpand3_File", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "declaration_xpand3_File"):
                opp_val = getattr(value, "declaration_xpand3_File", None)
                setattr(value, "declaration_xpand3_File", self)

class xpand3_expression_AbstractExpression(SyntaxElement):

    pass
class xpand3_File(SyntaxElement):

    pass