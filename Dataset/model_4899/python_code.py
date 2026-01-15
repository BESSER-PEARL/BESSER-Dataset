from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class ComparisonOperator:

    pass
class behaviour_Equals(ComparisonOperator):

    pass
class ArithmeticOperation:

    pass
class behaviour_Plus(ArithmeticOperation):

    pass
class BinaryExpression:

    pass
class behaviour_ComparisonOperator(BinaryExpression):

    pass
class behaviour_ArithmeticOperation(BinaryExpression):

    pass
class Expression:

    pass
class behaviour_ReadLine(Expression):

    pass
class behaviour_BinaryExpression(Expression):

    pass
class behaviour_Variable(Expression):

    def __init__(self, varName: str):
        self.varName = varName
        
    @property
    def varName(self) -> str:
        return self.__varName

    @varName.setter
    def varName(self, varName: str):
        self.__varName = varName

class behaviour_FunctionCall(Expression):

    def __init__(self, funcName: str, behaviour_FunctionCall: set["behaviour_Expression"] = None):
        self.funcName = funcName
        self.behaviour_FunctionCall = behaviour_FunctionCall if behaviour_FunctionCall is not None else set()
        
    @property
    def funcName(self) -> str:
        return self.__funcName

    @funcName.setter
    def funcName(self, funcName: str):
        self.__funcName = funcName

    @property
    def behaviour_FunctionCall(self):
        return self.__behaviour_FunctionCall

    @behaviour_FunctionCall.setter
    def behaviour_FunctionCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_FunctionCall__behaviour_FunctionCall", None)
        self.__behaviour_FunctionCall = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "behaviour_Expression34"):
                    opp_val = getattr(item, "behaviour_Expression34", None)
                    
                    if opp_val == self:
                        setattr(item, "behaviour_Expression34", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "behaviour_Expression34"):
                    opp_val = getattr(item, "behaviour_Expression34", None)
                    
                    setattr(item, "behaviour_Expression34", self)
                    

class behaviour_Literal(Expression):

    def __init__(self, vlaue: str):
        self.vlaue = vlaue
        
    @property
    def vlaue(self) -> str:
        return self.__vlaue

    @vlaue.setter
    def vlaue(self, vlaue: str):
        self.__vlaue = vlaue

class behaviour_Expression(ABC):

    pass
class Statement:

    pass
class behaviour_TryCatchStatement(Statement):

    pass
class behaviour_ReturnStatement(Statement):

    pass
class behaviour_DeclarationStatement(Statement):

    def __init__(self, varName: str, varType: str, behaviour_DeclarationStatement: "behaviour_Expression" = None):
        self.varName = varName
        self.varType = varType
        self.behaviour_DeclarationStatement = behaviour_DeclarationStatement
        
    @property
    def varType(self) -> str:
        return self.__varType

    @varType.setter
    def varType(self, varType: str):
        self.__varType = varType

    @property
    def varName(self) -> str:
        return self.__varName

    @varName.setter
    def varName(self, varName: str):
        self.__varName = varName

    @property
    def behaviour_DeclarationStatement(self):
        return self.__behaviour_DeclarationStatement

    @behaviour_DeclarationStatement.setter
    def behaviour_DeclarationStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_DeclarationStatement__behaviour_DeclarationStatement", None)
        self.__behaviour_DeclarationStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviour_Expression21"):
                opp_val = getattr(old_value, "behaviour_Expression21", None)
                if opp_val == self:
                    setattr(old_value, "behaviour_Expression21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviour_Expression21"):
                opp_val = getattr(value, "behaviour_Expression21", None)
                setattr(value, "behaviour_Expression21", self)

class behaviour_ExceptionStatement(Statement):

    pass
class behaviour_CallFunctionStatement(Statement):

    def __init__(self, nameFunc: str, behaviour_CallFunctionStatement: set["behaviour_Expression"] = None):
        self.nameFunc = nameFunc
        self.behaviour_CallFunctionStatement = behaviour_CallFunctionStatement if behaviour_CallFunctionStatement is not None else set()
        
    @property
    def nameFunc(self) -> str:
        return self.__nameFunc

    @nameFunc.setter
    def nameFunc(self, nameFunc: str):
        self.__nameFunc = nameFunc

    @property
    def behaviour_CallFunctionStatement(self):
        return self.__behaviour_CallFunctionStatement

    @behaviour_CallFunctionStatement.setter
    def behaviour_CallFunctionStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_CallFunctionStatement__behaviour_CallFunctionStatement", None)
        self.__behaviour_CallFunctionStatement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "behaviour_Expression25"):
                    opp_val = getattr(item, "behaviour_Expression25", None)
                    
                    if opp_val == self:
                        setattr(item, "behaviour_Expression25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "behaviour_Expression25"):
                    opp_val = getattr(item, "behaviour_Expression25", None)
                    
                    setattr(item, "behaviour_Expression25", self)
                    

class behaviour_LoopStatement(Statement):

    pass
class behaviour_AssignmentStatement(Statement):

    def __init__(self, varName: str, behaviour_AssignmentStatement: "behaviour_Expression" = None):
        self.varName = varName
        self.behaviour_AssignmentStatement = behaviour_AssignmentStatement
        
    @property
    def varName(self) -> str:
        return self.__varName

    @varName.setter
    def varName(self, varName: str):
        self.__varName = varName

    @property
    def behaviour_AssignmentStatement(self):
        return self.__behaviour_AssignmentStatement

    @behaviour_AssignmentStatement.setter
    def behaviour_AssignmentStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_AssignmentStatement__behaviour_AssignmentStatement", None)
        self.__behaviour_AssignmentStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviour_Expression19"):
                opp_val = getattr(old_value, "behaviour_Expression19", None)
                if opp_val == self:
                    setattr(old_value, "behaviour_Expression19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviour_Expression19"):
                opp_val = getattr(value, "behaviour_Expression19", None)
                setattr(value, "behaviour_Expression19", self)

class behaviour_CondionalStatement(Statement):

    pass
class behaviour_Statement(ABC):

    pass
class behaviour_Function:

    def __init__(self, name: str, behaviour_Function: "behaviour_Behaviour" = None, behaviour_Function3: "behaviour_Behaviour" = None, behaviour_Function5: set["behaviour_Statement"] = None):
        self.name = name
        self.behaviour_Function = behaviour_Function
        self.behaviour_Function3 = behaviour_Function3
        self.behaviour_Function5 = behaviour_Function5 if behaviour_Function5 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def behaviour_Function5(self):
        return self.__behaviour_Function5

    @behaviour_Function5.setter
    def behaviour_Function5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_Function__behaviour_Function5", None)
        self.__behaviour_Function5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "behaviour_Statement"):
                    opp_val = getattr(item, "behaviour_Statement", None)
                    
                    if opp_val == self:
                        setattr(item, "behaviour_Statement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "behaviour_Statement"):
                    opp_val = getattr(item, "behaviour_Statement", None)
                    
                    setattr(item, "behaviour_Statement", self)
                    

    @property
    def behaviour_Function(self):
        return self.__behaviour_Function

    @behaviour_Function.setter
    def behaviour_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_Function__behaviour_Function", None)
        self.__behaviour_Function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviour_Behaviour"):
                opp_val = getattr(old_value, "behaviour_Behaviour", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviour_Behaviour"):
                opp_val = getattr(value, "behaviour_Behaviour", None)
                if opp_val is None:
                    setattr(value, "behaviour_Behaviour", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def behaviour_Function3(self):
        return self.__behaviour_Function3

    @behaviour_Function3.setter
    def behaviour_Function3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_Function__behaviour_Function3", None)
        self.__behaviour_Function3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviour_Behaviour2"):
                opp_val = getattr(old_value, "behaviour_Behaviour2", None)
                if opp_val == self:
                    setattr(old_value, "behaviour_Behaviour2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviour_Behaviour2"):
                opp_val = getattr(value, "behaviour_Behaviour2", None)
                setattr(value, "behaviour_Behaviour2", self)

class behaviour_Behaviour:

    pass