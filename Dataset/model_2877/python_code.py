from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class parameterizedExpressionsTestLanguage_Expression:

    pass
class Statement:

    pass
class parameterizedExpressionsTestLanguage_Block(Statement):

    pass
class parameterizedExpressionsTestLanguage_ExpressionStatement(Statement):

    pass
class parameterizedExpressionsTestLanguage_FunctionDeclaration(Statement):

    def __init__(self, generator: bool, name: str, parameterizedExpressionsTestLanguage_FunctionDeclaration: "parameterizedExpressionsTestLanguage_Block" = None):
        self.generator = generator
        self.name = name
        self.parameterizedExpressionsTestLanguage_FunctionDeclaration = parameterizedExpressionsTestLanguage_FunctionDeclaration
        
    @property
    def generator(self) -> bool:
        return self.__generator

    @generator.setter
    def generator(self, generator: bool):
        self.__generator = generator

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def parameterizedExpressionsTestLanguage_FunctionDeclaration(self):
        return self.__parameterizedExpressionsTestLanguage_FunctionDeclaration

    @parameterizedExpressionsTestLanguage_FunctionDeclaration.setter
    def parameterizedExpressionsTestLanguage_FunctionDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_parameterizedExpressionsTestLanguage_FunctionDeclaration__parameterizedExpressionsTestLanguage_FunctionDeclaration", None)
        self.__parameterizedExpressionsTestLanguage_FunctionDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parameterizedExpressionsTestLanguage_Block"):
                opp_val = getattr(old_value, "parameterizedExpressionsTestLanguage_Block", None)
                if opp_val == self:
                    setattr(old_value, "parameterizedExpressionsTestLanguage_Block", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parameterizedExpressionsTestLanguage_Block"):
                opp_val = getattr(value, "parameterizedExpressionsTestLanguage_Block", None)
                setattr(value, "parameterizedExpressionsTestLanguage_Block", self)

class parameterizedExpressionsTestLanguage_Statement:

    pass
class Expression:

    pass
class parameterizedExpressionsTestLanguage_AssignmentExpression(Expression):

    def __init__(self, op: str, parameterizedExpressionsTestLanguage_AssignmentExpression: "parameterizedExpressionsTestLanguage_Expression" = None, parameterizedExpressionsTestLanguage_AssignmentExpression26: "parameterizedExpressionsTestLanguage_Expression" = None):
        self.op = op
        self.parameterizedExpressionsTestLanguage_AssignmentExpression = parameterizedExpressionsTestLanguage_AssignmentExpression
        self.parameterizedExpressionsTestLanguage_AssignmentExpression26 = parameterizedExpressionsTestLanguage_AssignmentExpression26
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def parameterizedExpressionsTestLanguage_AssignmentExpression26(self):
        return self.__parameterizedExpressionsTestLanguage_AssignmentExpression26

    @parameterizedExpressionsTestLanguage_AssignmentExpression26.setter
    def parameterizedExpressionsTestLanguage_AssignmentExpression26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_parameterizedExpressionsTestLanguage_AssignmentExpression__parameterizedExpressionsTestLanguage_AssignmentExpression26", None)
        self.__parameterizedExpressionsTestLanguage_AssignmentExpression26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parameterizedExpressionsTestLanguage_Expression27"):
                opp_val = getattr(old_value, "parameterizedExpressionsTestLanguage_Expression27", None)
                if opp_val == self:
                    setattr(old_value, "parameterizedExpressionsTestLanguage_Expression27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parameterizedExpressionsTestLanguage_Expression27"):
                opp_val = getattr(value, "parameterizedExpressionsTestLanguage_Expression27", None)
                setattr(value, "parameterizedExpressionsTestLanguage_Expression27", self)

    @property
    def parameterizedExpressionsTestLanguage_AssignmentExpression(self):
        return self.__parameterizedExpressionsTestLanguage_AssignmentExpression

    @parameterizedExpressionsTestLanguage_AssignmentExpression.setter
    def parameterizedExpressionsTestLanguage_AssignmentExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_parameterizedExpressionsTestLanguage_AssignmentExpression__parameterizedExpressionsTestLanguage_AssignmentExpression", None)
        self.__parameterizedExpressionsTestLanguage_AssignmentExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parameterizedExpressionsTestLanguage_Expression24"):
                opp_val = getattr(old_value, "parameterizedExpressionsTestLanguage_Expression24", None)
                if opp_val == self:
                    setattr(old_value, "parameterizedExpressionsTestLanguage_Expression24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parameterizedExpressionsTestLanguage_Expression24"):
                opp_val = getattr(value, "parameterizedExpressionsTestLanguage_Expression24", None)
                setattr(value, "parameterizedExpressionsTestLanguage_Expression24", self)

class parameterizedExpressionsTestLanguage_YieldExpression(Expression):

    def __init__(self, many: bool, parameterizedExpressionsTestLanguage_YieldExpression: "parameterizedExpressionsTestLanguage_Expression" = None):
        self.many = many
        self.parameterizedExpressionsTestLanguage_YieldExpression = parameterizedExpressionsTestLanguage_YieldExpression
        
    @property
    def many(self) -> bool:
        return self.__many

    @many.setter
    def many(self, many: bool):
        self.__many = many

    @property
    def parameterizedExpressionsTestLanguage_YieldExpression(self):
        return self.__parameterizedExpressionsTestLanguage_YieldExpression

    @parameterizedExpressionsTestLanguage_YieldExpression.setter
    def parameterizedExpressionsTestLanguage_YieldExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_parameterizedExpressionsTestLanguage_YieldExpression__parameterizedExpressionsTestLanguage_YieldExpression", None)
        self.__parameterizedExpressionsTestLanguage_YieldExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parameterizedExpressionsTestLanguage_Expression29"):
                opp_val = getattr(old_value, "parameterizedExpressionsTestLanguage_Expression29", None)
                if opp_val == self:
                    setattr(old_value, "parameterizedExpressionsTestLanguage_Expression29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parameterizedExpressionsTestLanguage_Expression29"):
                opp_val = getattr(value, "parameterizedExpressionsTestLanguage_Expression29", None)
                setattr(value, "parameterizedExpressionsTestLanguage_Expression29", self)

class parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression(Expression):

    def __init__(self, property: str, parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression: "parameterizedExpressionsTestLanguage_Expression" = None):
        self.property = property
        self.parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression = parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression
        
    @property
    def property(self) -> str:
        return self.__property

    @property.setter
    def property(self, property: str):
        self.__property = property

    @property
    def parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression(self):
        return self.__parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression

    @parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression.setter
    def parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression__parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression", None)
        self.__parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parameterizedExpressionsTestLanguage_Expression12"):
                opp_val = getattr(old_value, "parameterizedExpressionsTestLanguage_Expression12", None)
                if opp_val == self:
                    setattr(old_value, "parameterizedExpressionsTestLanguage_Expression12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parameterizedExpressionsTestLanguage_Expression12"):
                opp_val = getattr(value, "parameterizedExpressionsTestLanguage_Expression12", None)
                setattr(value, "parameterizedExpressionsTestLanguage_Expression12", self)

class parameterizedExpressionsTestLanguage_CommaExpression(Expression):

    pass
class parameterizedExpressionsTestLanguage_ShiftExpression(Expression):

    def __init__(self, op: str, parameterizedExpressionsTestLanguage_ShiftExpression: "parameterizedExpressionsTestLanguage_Expression" = None, parameterizedExpressionsTestLanguage_ShiftExpression16: "parameterizedExpressionsTestLanguage_Expression" = None):
        self.op = op
        self.parameterizedExpressionsTestLanguage_ShiftExpression = parameterizedExpressionsTestLanguage_ShiftExpression
        self.parameterizedExpressionsTestLanguage_ShiftExpression16 = parameterizedExpressionsTestLanguage_ShiftExpression16
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def parameterizedExpressionsTestLanguage_ShiftExpression(self):
        return self.__parameterizedExpressionsTestLanguage_ShiftExpression

    @parameterizedExpressionsTestLanguage_ShiftExpression.setter
    def parameterizedExpressionsTestLanguage_ShiftExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_parameterizedExpressionsTestLanguage_ShiftExpression__parameterizedExpressionsTestLanguage_ShiftExpression", None)
        self.__parameterizedExpressionsTestLanguage_ShiftExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parameterizedExpressionsTestLanguage_Expression14"):
                opp_val = getattr(old_value, "parameterizedExpressionsTestLanguage_Expression14", None)
                if opp_val == self:
                    setattr(old_value, "parameterizedExpressionsTestLanguage_Expression14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parameterizedExpressionsTestLanguage_Expression14"):
                opp_val = getattr(value, "parameterizedExpressionsTestLanguage_Expression14", None)
                setattr(value, "parameterizedExpressionsTestLanguage_Expression14", self)

    @property
    def parameterizedExpressionsTestLanguage_ShiftExpression16(self):
        return self.__parameterizedExpressionsTestLanguage_ShiftExpression16

    @parameterizedExpressionsTestLanguage_ShiftExpression16.setter
    def parameterizedExpressionsTestLanguage_ShiftExpression16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_parameterizedExpressionsTestLanguage_ShiftExpression__parameterizedExpressionsTestLanguage_ShiftExpression16", None)
        self.__parameterizedExpressionsTestLanguage_ShiftExpression16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parameterizedExpressionsTestLanguage_Expression17"):
                opp_val = getattr(old_value, "parameterizedExpressionsTestLanguage_Expression17", None)
                if opp_val == self:
                    setattr(old_value, "parameterizedExpressionsTestLanguage_Expression17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parameterizedExpressionsTestLanguage_Expression17"):
                opp_val = getattr(value, "parameterizedExpressionsTestLanguage_Expression17", None)
                setattr(value, "parameterizedExpressionsTestLanguage_Expression17", self)

class parameterizedExpressionsTestLanguage_IndexedAccessExpression(Expression):

    pass
class parameterizedExpressionsTestLanguage_RelationalExpression(Expression):

    def __init__(self, op: str, parameterizedExpressionsTestLanguage_RelationalExpression: "parameterizedExpressionsTestLanguage_Expression" = None, parameterizedExpressionsTestLanguage_RelationalExpression21: "parameterizedExpressionsTestLanguage_Expression" = None):
        self.op = op
        self.parameterizedExpressionsTestLanguage_RelationalExpression = parameterizedExpressionsTestLanguage_RelationalExpression
        self.parameterizedExpressionsTestLanguage_RelationalExpression21 = parameterizedExpressionsTestLanguage_RelationalExpression21
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def parameterizedExpressionsTestLanguage_RelationalExpression21(self):
        return self.__parameterizedExpressionsTestLanguage_RelationalExpression21

    @parameterizedExpressionsTestLanguage_RelationalExpression21.setter
    def parameterizedExpressionsTestLanguage_RelationalExpression21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_parameterizedExpressionsTestLanguage_RelationalExpression__parameterizedExpressionsTestLanguage_RelationalExpression21", None)
        self.__parameterizedExpressionsTestLanguage_RelationalExpression21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parameterizedExpressionsTestLanguage_Expression22"):
                opp_val = getattr(old_value, "parameterizedExpressionsTestLanguage_Expression22", None)
                if opp_val == self:
                    setattr(old_value, "parameterizedExpressionsTestLanguage_Expression22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parameterizedExpressionsTestLanguage_Expression22"):
                opp_val = getattr(value, "parameterizedExpressionsTestLanguage_Expression22", None)
                setattr(value, "parameterizedExpressionsTestLanguage_Expression22", self)

    @property
    def parameterizedExpressionsTestLanguage_RelationalExpression(self):
        return self.__parameterizedExpressionsTestLanguage_RelationalExpression

    @parameterizedExpressionsTestLanguage_RelationalExpression.setter
    def parameterizedExpressionsTestLanguage_RelationalExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_parameterizedExpressionsTestLanguage_RelationalExpression__parameterizedExpressionsTestLanguage_RelationalExpression", None)
        self.__parameterizedExpressionsTestLanguage_RelationalExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parameterizedExpressionsTestLanguage_Expression19"):
                opp_val = getattr(old_value, "parameterizedExpressionsTestLanguage_Expression19", None)
                if opp_val == self:
                    setattr(old_value, "parameterizedExpressionsTestLanguage_Expression19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parameterizedExpressionsTestLanguage_Expression19"):
                opp_val = getattr(value, "parameterizedExpressionsTestLanguage_Expression19", None)
                setattr(value, "parameterizedExpressionsTestLanguage_Expression19", self)

class parameterizedExpressionsTestLanguage_IdentifierRef(Expression):

    def __init__(self, id: str):
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

class parameterizedExpressionsTestLanguage_LabelledStatement(Statement):

    def __init__(self, name: str, parameterizedExpressionsTestLanguage_LabelledStatement: "parameterizedExpressionsTestLanguage_Statement" = None):
        self.name = name
        self.parameterizedExpressionsTestLanguage_LabelledStatement = parameterizedExpressionsTestLanguage_LabelledStatement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def parameterizedExpressionsTestLanguage_LabelledStatement(self):
        return self.__parameterizedExpressionsTestLanguage_LabelledStatement

    @parameterizedExpressionsTestLanguage_LabelledStatement.setter
    def parameterizedExpressionsTestLanguage_LabelledStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_parameterizedExpressionsTestLanguage_LabelledStatement__parameterizedExpressionsTestLanguage_LabelledStatement", None)
        self.__parameterizedExpressionsTestLanguage_LabelledStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parameterizedExpressionsTestLanguage_Statement5"):
                opp_val = getattr(old_value, "parameterizedExpressionsTestLanguage_Statement5", None)
                if opp_val == self:
                    setattr(old_value, "parameterizedExpressionsTestLanguage_Statement5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parameterizedExpressionsTestLanguage_Statement5"):
                opp_val = getattr(value, "parameterizedExpressionsTestLanguage_Statement5", None)
                setattr(value, "parameterizedExpressionsTestLanguage_Statement5", self)
