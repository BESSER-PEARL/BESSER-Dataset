from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class If:

    pass
class Call:

    pass
class mt_core_Parameter:

    def __init__(self, type: str):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class Parameter:

    pass
class mt_core_Method:

    def __init__(self, name: str, return: str, mt_core_Method: set["Parameter"] = None):
        self.name = name
        self.return = return
        self.mt_core_Method = mt_core_Method if mt_core_Method is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def return(self) -> str:
        return self.__return

    @return.setter
    def return(self, return: str):
        self.__return = return

    @property
    def mt_core_Method(self):
        return self.__mt_core_Method

    @mt_core_Method.setter
    def mt_core_Method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mt_core_Method__mt_core_Method", None)
        self.__mt_core_Method = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Parameter"):
                    opp_val = getattr(item, "Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Parameter"):
                    opp_val = getattr(item, "Parameter", None)
                    
                    setattr(item, "Parameter", self)
                    

class Method:

    pass
class Literal:

    pass
class mt_expressions_NullLiteral(Literal):

    pass
class mt_expressions_BooleanLiteral(Literal):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class mt_expressions_DoubleLiteral(Literal):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class mt_expressions_IntegerLiteral(Literal):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class mt_expressions_StringLiteral(Literal):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class Statement:

    pass
class mt_statements_If(Statement):

    pass
class mt_statements_Comment(Statement):

    def __init__(self, value: str, Statement30: "mt_statements_If", Statement33: "mt_statements_If", Statement11: "mt_core_FilePath", Statement40: "mt_statements_For", Statement: "mt_core_Script"):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class mt_statements_Text(Statement):

    def __init__(self, value: str, Statement30: "mt_statements_If", Statement33: "mt_statements_If", Statement11: "mt_core_FilePath", Statement40: "mt_statements_For", Statement: "mt_core_Script"):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class mt_statements_For(Statement):

    pass
class mt_statements_Feature(Statement):

    pass
class ScriptDescriptor:

    pass
class ASTNode:

    pass
class mt_expressions_Expression(ASTNode):

    pass
class mt_statements_Statement(ASTNode):

    pass
class mt_core_ScriptDescriptor(ASTNode):

    def __init__(self, type: str, description: str, name: str, mt_core_ScriptDescriptor: "FilePath" = None, mt_core_ScriptDescriptor9: "Expression" = None):
        self.type = type
        self.description = description
        self.name = name
        self.mt_core_ScriptDescriptor = mt_core_ScriptDescriptor
        self.mt_core_ScriptDescriptor9 = mt_core_ScriptDescriptor9
        
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
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mt_core_ScriptDescriptor9(self):
        return self.__mt_core_ScriptDescriptor9

    @mt_core_ScriptDescriptor9.setter
    def mt_core_ScriptDescriptor9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mt_core_ScriptDescriptor__mt_core_ScriptDescriptor9", None)
        self.__mt_core_ScriptDescriptor9 = value
        
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

    @property
    def mt_core_ScriptDescriptor(self):
        return self.__mt_core_ScriptDescriptor

    @mt_core_ScriptDescriptor.setter
    def mt_core_ScriptDescriptor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mt_core_ScriptDescriptor__mt_core_ScriptDescriptor", None)
        self.__mt_core_ScriptDescriptor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FilePath"):
                opp_val = getattr(old_value, "FilePath", None)
                if opp_val == self:
                    setattr(old_value, "FilePath", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FilePath"):
                opp_val = getattr(value, "FilePath", None)
                setattr(value, "FilePath", self)

class mt_expressions_Call(ASTNode):

    def __init__(self, name: str, prefix: str, mt_expressions_Call: set["Expression"] = None, mt_expressions_Call18: "Expression" = None):
        self.name = name
        self.prefix = prefix
        self.mt_expressions_Call = mt_expressions_Call if mt_expressions_Call is not None else set()
        self.mt_expressions_Call18 = mt_expressions_Call18
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def prefix(self) -> str:
        return self.__prefix

    @prefix.setter
    def prefix(self, prefix: str):
        self.__prefix = prefix

    @property
    def mt_expressions_Call(self):
        return self.__mt_expressions_Call

    @mt_expressions_Call.setter
    def mt_expressions_Call(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mt_expressions_Call__mt_expressions_Call", None)
        self.__mt_expressions_Call = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Expression16"):
                    opp_val = getattr(item, "Expression16", None)
                    
                    if opp_val == self:
                        setattr(item, "Expression16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Expression16"):
                    opp_val = getattr(item, "Expression16", None)
                    
                    setattr(item, "Expression16", self)
                    

    @property
    def mt_expressions_Call18(self):
        return self.__mt_expressions_Call18

    @mt_expressions_Call18.setter
    def mt_expressions_Call18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mt_expressions_Call__mt_expressions_Call18", None)
        self.__mt_expressions_Call18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression19"):
                opp_val = getattr(old_value, "Expression19", None)
                if opp_val == self:
                    setattr(old_value, "Expression19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression19"):
                opp_val = getattr(value, "Expression19", None)
                setattr(value, "Expression19", self)

class mt_core_Script(ASTNode):

    pass
class Script:

    pass
class core_mt_Resource:

    pass
class Resource:

    pass
class mt_core_Service(Resource):

    pass
class mt_core_Template(Resource):

    def __init__(self, beginTag: str, endTag: str, mt_core_Template: set["core_mt_Resource"] = None, mt_core_Template3: set["Script"] = None):
        self.beginTag = beginTag
        self.endTag = endTag
        self.mt_core_Template = mt_core_Template if mt_core_Template is not None else set()
        self.mt_core_Template3 = mt_core_Template3 if mt_core_Template3 is not None else set()
        
    @property
    def endTag(self) -> str:
        return self.__endTag

    @endTag.setter
    def endTag(self, endTag: str):
        self.__endTag = endTag

    @property
    def beginTag(self) -> str:
        return self.__beginTag

    @beginTag.setter
    def beginTag(self, beginTag: str):
        self.__beginTag = beginTag

    @property
    def mt_core_Template3(self):
        return self.__mt_core_Template3

    @mt_core_Template3.setter
    def mt_core_Template3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mt_core_Template__mt_core_Template3", None)
        self.__mt_core_Template3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Script"):
                    opp_val = getattr(item, "Script", None)
                    
                    if opp_val == self:
                        setattr(item, "Script", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Script"):
                    opp_val = getattr(item, "Script", None)
                    
                    setattr(item, "Script", self)
                    

    @property
    def mt_core_Template(self):
        return self.__mt_core_Template

    @mt_core_Template.setter
    def mt_core_Template(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mt_core_Template__mt_core_Template", None)
        self.__mt_core_Template = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "core_mt_Resource"):
                    opp_val = getattr(item, "core_mt_Resource", None)
                    
                    if opp_val == self:
                        setattr(item, "core_mt_Resource", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "core_mt_Resource"):
                    opp_val = getattr(item, "core_mt_Resource", None)
                    
                    setattr(item, "core_mt_Resource", self)
                    

class mt_core_ASTNode(ABC):

    def __init__(self, begin: int, end: int):
        self.begin = begin
        self.end = end
        
    @property
    def end(self) -> int:
        return self.__end

    @end.setter
    def end(self, end: int):
        self.__end = end

    @property
    def begin(self) -> int:
        return self.__begin

    @begin.setter
    def begin(self, begin: int):
        self.__begin = begin

    def getTemplate(self) -> str:
        # TODO: Implement getTemplate method
        pass

class mt_Resource(ABC):

    def __init__(self, name: str, mt_Resource: "mt_ResourceSet" = None):
        self.name = name
        self.mt_Resource = mt_Resource
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mt_Resource(self):
        return self.__mt_Resource

    @mt_Resource.setter
    def mt_Resource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mt_Resource__mt_Resource", None)
        self.__mt_Resource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mt_ResourceSet"):
                opp_val = getattr(old_value, "mt_ResourceSet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mt_ResourceSet"):
                opp_val = getattr(value, "mt_ResourceSet", None)
                if opp_val is None:
                    setattr(value, "mt_ResourceSet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mt_ResourceSet:

    pass
class mt_core_Metamodel(Resource):

    def __init__(self, packageClass: str):
        self.packageClass = packageClass
        
    @property
    def packageClass(self) -> str:
        return self.__packageClass

    @packageClass.setter
    def packageClass(self, packageClass: str):
        self.__packageClass = packageClass

class mt_core_FilePath(ASTNode):

    pass
class Expression:

    pass
class mt_expressions_CallSet(Expression):

    pass
class mt_expressions_Literal(Expression):

    pass
class mt_expressions_Parenthesis(Expression):

    pass
class mt_expressions_Not(Expression):

    pass
class mt_expressions_Operator(Expression):

    def __init__(self, operator: str, mt_expressions_Operator: set["Expression"] = None, Expression27: "mt_statements_If", Expression21: "mt_expressions_Not", Expression23: "mt_expressions_Operator", Expression25: "mt_expressions_Parenthesis", Expression37: "mt_statements_For", Expression19: "mt_expressions_Call", Expression42: "mt_statements_Feature", Expression16: "mt_expressions_Call", Expression: "mt_core_ScriptDescriptor"):
        self.operator = operator
        self.mt_expressions_Operator = mt_expressions_Operator if mt_expressions_Operator is not None else set()
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def mt_expressions_Operator(self):
        return self.__mt_expressions_Operator

    @mt_expressions_Operator.setter
    def mt_expressions_Operator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mt_expressions_Operator__mt_expressions_Operator", None)
        self.__mt_expressions_Operator = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Expression23"):
                    opp_val = getattr(item, "Expression23", None)
                    
                    if opp_val == self:
                        setattr(item, "Expression23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Expression23"):
                    opp_val = getattr(item, "Expression23", None)
                    
                    setattr(item, "Expression23", self)
                    

class FilePath:

    pass