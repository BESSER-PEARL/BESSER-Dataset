from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class operators_QueryVariableQualifier(ABC):

    pass
class operators_EOperation:

    pass
class QueryVariableQualifier:

    pass
class operators_EReferenceQualifier(QueryVariableQualifier):

    pass
class operators_EOperationQualifier(QueryVariableQualifier):

    pass
class operators_StructuralFeatureSet:

    pass
class operators_EStructuralFeature:

    pass
class operators_Variable(ABC):

    def __init__(self, name: str, operators_Variable: "operators_VariableReference" = None):
        self.name = name
        self.operators_Variable = operators_Variable
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def operators_Variable(self):
        return self.__operators_Variable

    @operators_Variable.setter
    def operators_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_Variable__operators_Variable", None)
        self.__operators_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operators_VariableReference"):
                opp_val = getattr(old_value, "operators_VariableReference", None)
                if opp_val == self:
                    setattr(old_value, "operators_VariableReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operators_VariableReference"):
                opp_val = getattr(value, "operators_VariableReference", None)
                setattr(value, "operators_VariableReference", self)

class operators_EObject:

    pass
class operators_EClass:

    pass
class Variable:

    pass
class operators_QueryVariable(Variable):

    pass
class operators_EReference:

    pass
class operators_Referrable(ABC):

    pass
class Referrable:

    pass
class operators_VariableReference(Referrable):

    pass
class Result:

    pass
class operators_PrimitiveReference(Result):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class operators_EObjectReference(Result, Referrable):

    pass
class operators_EAttribute:

    pass
class operators_Result(ABC):

    pass
class operators_Operator(ABC):

    def __init__(self, executed: bool, operators_Operator: "operators_Result" = None):
        self.executed = executed
        self.operators_Operator = operators_Operator
        
        pass
    @property
    def executed(self):
        return self.__executed

    @executed.setter
    def executed(self, executed: bool):
        self.__executed = executed


    @property
    def operators_Operator(self):
        return self.__operators_Operator

    @operators_Operator.setter
    def operators_Operator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_Operator__operators_Operator", None)
        self.__operators_Operator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operators_Result"):
                opp_val = getattr(old_value, "operators_Result", None)
                if opp_val == self:
                    setattr(old_value, "operators_Result", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operators_Result"):
                opp_val = getattr(value, "operators_Result", None)
                setattr(value, "operators_Result", self)

    def execute(self):
        # TODO: Implement execute method
        pass

class operators_TypeVariable(Variable):

    pass
class Operator:

    pass
class operators_DELETE(Operator):

    def __init__(self, operators_DELETE: "operators_Referrable" = None):
        self.operators_DELETE = operators_DELETE
        
        pass
    @property
    def operators_DELETE(self):
        return self.__operators_DELETE

    @operators_DELETE.setter
    def operators_DELETE(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_DELETE__operators_DELETE", None)
        self.__operators_DELETE = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operators_Referrable11"):
                opp_val = getattr(old_value, "operators_Referrable11", None)
                if opp_val == self:
                    setattr(old_value, "operators_Referrable11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operators_Referrable11"):
                opp_val = getattr(value, "operators_Referrable11", None)
                setattr(value, "operators_Referrable11", self)

    def execute(self):
        # TODO: Implement execute method
        pass

class operators_MOVE(Operator):

    def __init__(self, operators_MOVE: "operators_Referrable" = None, operators_MOVE30: "operators_EReference" = None, operators_MOVE33: "operators_Referrable" = None):
        self.operators_MOVE = operators_MOVE
        self.operators_MOVE30 = operators_MOVE30
        self.operators_MOVE33 = operators_MOVE33
        
        pass
    @property
    def operators_MOVE33(self):
        return self.__operators_MOVE33

    @operators_MOVE33.setter
    def operators_MOVE33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_MOVE__operators_MOVE33", None)
        self.__operators_MOVE33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operators_Referrable34"):
                opp_val = getattr(old_value, "operators_Referrable34", None)
                if opp_val == self:
                    setattr(old_value, "operators_Referrable34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operators_Referrable34"):
                opp_val = getattr(value, "operators_Referrable34", None)
                setattr(value, "operators_Referrable34", self)

    @property
    def operators_MOVE(self):
        return self.__operators_MOVE

    @operators_MOVE.setter
    def operators_MOVE(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_MOVE__operators_MOVE", None)
        self.__operators_MOVE = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operators_Referrable28"):
                opp_val = getattr(old_value, "operators_Referrable28", None)
                if opp_val == self:
                    setattr(old_value, "operators_Referrable28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operators_Referrable28"):
                opp_val = getattr(value, "operators_Referrable28", None)
                setattr(value, "operators_Referrable28", self)

    @property
    def operators_MOVE30(self):
        return self.__operators_MOVE30

    @operators_MOVE30.setter
    def operators_MOVE30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_MOVE__operators_MOVE30", None)
        self.__operators_MOVE30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operators_EReference31"):
                opp_val = getattr(old_value, "operators_EReference31", None)
                if opp_val == self:
                    setattr(old_value, "operators_EReference31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operators_EReference31"):
                opp_val = getattr(value, "operators_EReference31", None)
                setattr(value, "operators_EReference31", self)

    def execute(self):
        # TODO: Implement execute method
        pass

class operators_ASSIGN(Operator):

    def __init__(self, value: str, operators_ASSIGN: "operators_EAttribute" = None, operators_ASSIGN14: "operators_Referrable" = None):
        self.value = value
        self.operators_ASSIGN = operators_ASSIGN
        self.operators_ASSIGN14 = operators_ASSIGN14
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def operators_ASSIGN14(self):
        return self.__operators_ASSIGN14

    @operators_ASSIGN14.setter
    def operators_ASSIGN14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_ASSIGN__operators_ASSIGN14", None)
        self.__operators_ASSIGN14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operators_Referrable15"):
                opp_val = getattr(old_value, "operators_Referrable15", None)
                if opp_val == self:
                    setattr(old_value, "operators_Referrable15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operators_Referrable15"):
                opp_val = getattr(value, "operators_Referrable15", None)
                setattr(value, "operators_Referrable15", self)

    @property
    def operators_ASSIGN(self):
        return self.__operators_ASSIGN

    @operators_ASSIGN.setter
    def operators_ASSIGN(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_ASSIGN__operators_ASSIGN", None)
        self.__operators_ASSIGN = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operators_EAttribute"):
                opp_val = getattr(old_value, "operators_EAttribute", None)
                if opp_val == self:
                    setattr(old_value, "operators_EAttribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operators_EAttribute"):
                opp_val = getattr(value, "operators_EAttribute", None)
                setattr(value, "operators_EAttribute", self)

    def execute(self):
        # TODO: Implement execute method
        pass

class operators_SET(Operator):

    def __init__(self, operators_SET: "operators_EReference" = None, operators_SET21: "operators_Referrable" = None, operators_SET24: "operators_Referrable" = None):
        self.operators_SET = operators_SET
        self.operators_SET21 = operators_SET21
        self.operators_SET24 = operators_SET24
        
        pass
    @property
    def operators_SET21(self):
        return self.__operators_SET21

    @operators_SET21.setter
    def operators_SET21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_SET__operators_SET21", None)
        self.__operators_SET21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operators_Referrable22"):
                opp_val = getattr(old_value, "operators_Referrable22", None)
                if opp_val == self:
                    setattr(old_value, "operators_Referrable22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operators_Referrable22"):
                opp_val = getattr(value, "operators_Referrable22", None)
                setattr(value, "operators_Referrable22", self)

    @property
    def operators_SET(self):
        return self.__operators_SET

    @operators_SET.setter
    def operators_SET(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_SET__operators_SET", None)
        self.__operators_SET = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operators_EReference19"):
                opp_val = getattr(old_value, "operators_EReference19", None)
                if opp_val == self:
                    setattr(old_value, "operators_EReference19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operators_EReference19"):
                opp_val = getattr(value, "operators_EReference19", None)
                setattr(value, "operators_EReference19", self)

    @property
    def operators_SET24(self):
        return self.__operators_SET24

    @operators_SET24.setter
    def operators_SET24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_SET__operators_SET24", None)
        self.__operators_SET24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operators_Referrable25"):
                opp_val = getattr(old_value, "operators_Referrable25", None)
                if opp_val == self:
                    setattr(old_value, "operators_Referrable25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operators_Referrable25"):
                opp_val = getattr(value, "operators_Referrable25", None)
                setattr(value, "operators_Referrable25", self)

    def execute(self):
        # TODO: Implement execute method
        pass

class operators_SPLIT(Operator):

    pass
class operators_VAR(Operator):

    def __init__(self, operators_VAR: "operators_QueryVariable" = None):
        self.operators_VAR = operators_VAR
        
        pass
    @property
    def operators_VAR(self):
        return self.__operators_VAR

    @operators_VAR.setter
    def operators_VAR(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_VAR__operators_VAR", None)
        self.__operators_VAR = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operators_QueryVariable"):
                opp_val = getattr(old_value, "operators_QueryVariable", None)
                if opp_val == self:
                    setattr(old_value, "operators_QueryVariable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operators_QueryVariable"):
                opp_val = getattr(value, "operators_QueryVariable", None)
                setattr(value, "operators_QueryVariable", self)

    def execute(self):
        # TODO: Implement execute method
        pass

class operators_MERGE(Operator):

    pass
class operators_CREATE(Operator):

    def __init__(self, operators_CREATE: "operators_TypeVariable" = None, operators_CREATE3: "operators_Referrable" = None, operators_CREATE5: "operators_EReference" = None):
        self.operators_CREATE = operators_CREATE
        self.operators_CREATE3 = operators_CREATE3
        self.operators_CREATE5 = operators_CREATE5
        
        pass
    @property
    def operators_CREATE3(self):
        return self.__operators_CREATE3

    @operators_CREATE3.setter
    def operators_CREATE3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_CREATE__operators_CREATE3", None)
        self.__operators_CREATE3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operators_Referrable"):
                opp_val = getattr(old_value, "operators_Referrable", None)
                if opp_val == self:
                    setattr(old_value, "operators_Referrable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operators_Referrable"):
                opp_val = getattr(value, "operators_Referrable", None)
                setattr(value, "operators_Referrable", self)

    @property
    def operators_CREATE(self):
        return self.__operators_CREATE

    @operators_CREATE.setter
    def operators_CREATE(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_CREATE__operators_CREATE", None)
        self.__operators_CREATE = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operators_TypeVariable"):
                opp_val = getattr(old_value, "operators_TypeVariable", None)
                if opp_val == self:
                    setattr(old_value, "operators_TypeVariable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operators_TypeVariable"):
                opp_val = getattr(value, "operators_TypeVariable", None)
                setattr(value, "operators_TypeVariable", self)

    @property
    def operators_CREATE5(self):
        return self.__operators_CREATE5

    @operators_CREATE5.setter
    def operators_CREATE5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_CREATE__operators_CREATE5", None)
        self.__operators_CREATE5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operators_EReference"):
                opp_val = getattr(old_value, "operators_EReference", None)
                if opp_val == self:
                    setattr(old_value, "operators_EReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operators_EReference"):
                opp_val = getattr(value, "operators_EReference", None)
                setattr(value, "operators_EReference", self)

    def execute(self):
        # TODO: Implement execute method
        pass
