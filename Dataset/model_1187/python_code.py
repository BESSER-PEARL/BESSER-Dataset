from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class CollectionExp:

    pass
class superimposed_SetExp(CollectionExp):

    pass
class superimposed_OclModel:

    def __init__(self, name: str, superimposed_OclModel: "superimposed_OclModelElement" = None):
        self.name = name
        self.superimposed_OclModel = superimposed_OclModel
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def superimposed_OclModel(self):
        return self.__superimposed_OclModel

    @superimposed_OclModel.setter
    def superimposed_OclModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_superimposed_OclModel__superimposed_OclModel", None)
        self.__superimposed_OclModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "superimposed_OclModelElement"):
                opp_val = getattr(old_value, "superimposed_OclModelElement", None)
                if opp_val == self:
                    setattr(old_value, "superimposed_OclModelElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "superimposed_OclModelElement"):
                opp_val = getattr(value, "superimposed_OclModelElement", None)
                setattr(value, "superimposed_OclModelElement", self)

class NumericExp:

    pass
class superimposed_IntegerExp(NumericExp):

    def __init__(self, integerSymbol: str):
        self.integerSymbol = integerSymbol
        
    @property
    def integerSymbol(self) -> str:
        return self.__integerSymbol

    @integerSymbol.setter
    def integerSymbol(self, integerSymbol: str):
        self.__integerSymbol = integerSymbol

class superimposed_RealExp(NumericExp):

    def __init__(self, realSymbol: str):
        self.realSymbol = realSymbol
        
    @property
    def realSymbol(self) -> str:
        return self.__realSymbol

    @realSymbol.setter
    def realSymbol(self, realSymbol: str):
        self.__realSymbol = realSymbol

class PrimitiveExp:

    pass
class superimposed_BooleanExp(PrimitiveExp):

    def __init__(self, booleanSymbol: str):
        self.booleanSymbol = booleanSymbol
        
    @property
    def booleanSymbol(self) -> str:
        return self.__booleanSymbol

    @booleanSymbol.setter
    def booleanSymbol(self, booleanSymbol: str):
        self.__booleanSymbol = booleanSymbol

class superimposed_NumericExp(PrimitiveExp):

    pass
class superimposed_StringExp(PrimitiveExp):

    def __init__(self, stringSymbol: str):
        self.stringSymbol = stringSymbol
        
    @property
    def stringSymbol(self) -> str:
        return self.__stringSymbol

    @stringSymbol.setter
    def stringSymbol(self, stringSymbol: str):
        self.__stringSymbol = stringSymbol

class VariableDeclaration:

    pass
class superimposed_Iterator(VariableDeclaration):

    pass
class LoopExp:

    pass
class superimposed_IteratorExp(LoopExp):

    def __init__(self, name: str, superimposed_IteratorExp: "superimposed_Iterator" = None):
        self.name = name
        self.superimposed_IteratorExp = superimposed_IteratorExp
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def superimposed_IteratorExp(self):
        return self.__superimposed_IteratorExp

    @superimposed_IteratorExp.setter
    def superimposed_IteratorExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_superimposed_IteratorExp__superimposed_IteratorExp", None)
        self.__superimposed_IteratorExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "superimposed_Iterator"):
                opp_val = getattr(old_value, "superimposed_Iterator", None)
                if opp_val == self:
                    setattr(old_value, "superimposed_Iterator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "superimposed_Iterator"):
                opp_val = getattr(value, "superimposed_Iterator", None)
                setattr(value, "superimposed_Iterator", self)

class OclType:

    pass
class superimposed_OclModelElement(OclType):

    def __init__(self, name: str, superimposed_OclModelElement: "superimposed_OclModel" = None):
        self.name = name
        self.superimposed_OclModelElement = superimposed_OclModelElement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def superimposed_OclModelElement(self):
        return self.__superimposed_OclModelElement

    @superimposed_OclModelElement.setter
    def superimposed_OclModelElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_superimposed_OclModelElement__superimposed_OclModelElement", None)
        self.__superimposed_OclModelElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "superimposed_OclModel"):
                opp_val = getattr(old_value, "superimposed_OclModel", None)
                if opp_val == self:
                    setattr(old_value, "superimposed_OclModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "superimposed_OclModel"):
                opp_val = getattr(value, "superimposed_OclModel", None)
                setattr(value, "superimposed_OclModel", self)

class OperationCallExp:

    pass
class superimposed_CollectionOperationCallExp(OperationCallExp):

    pass
class PropertyCallExp:

    pass
class superimposed_LoopExp(PropertyCallExp):

    pass
class superimposed_NavigationCallExp(PropertyCallExp):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class superimposed_OperationCallExp(PropertyCallExp):

    def __init__(self, name: str, superimposed_OperationCallExp: set["superimposed_OclExpression"] = None):
        self.name = name
        self.superimposed_OperationCallExp = superimposed_OperationCallExp if superimposed_OperationCallExp is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def superimposed_OperationCallExp(self):
        return self.__superimposed_OperationCallExp

    @superimposed_OperationCallExp.setter
    def superimposed_OperationCallExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_superimposed_OperationCallExp__superimposed_OperationCallExp", None)
        self.__superimposed_OperationCallExp = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "superimposed_OclExpression11"):
                    opp_val = getattr(item, "superimposed_OclExpression11", None)
                    
                    if opp_val == self:
                        setattr(item, "superimposed_OclExpression11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "superimposed_OclExpression11"):
                    opp_val = getattr(item, "superimposed_OclExpression11", None)
                    
                    setattr(item, "superimposed_OclExpression11", self)
                    

class OclExpression:

    pass
class superimposed_OclUndefinedExp(OclExpression):

    pass
class superimposed_PropertyCallExp(OclExpression):

    pass
class superimposed_LetExp(OclExpression):

    pass
class superimposed_IfExp(OclExpression):

    pass
class superimposed_PrimitiveExp(OclExpression):

    pass
class superimposed_CollectionExp(OclExpression):

    pass
class superimposed_OperatorCallExp(OclExpression):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class superimposed_VariableExp(OclExpression):

    pass
class superimposed_OclType(OclExpression):

    pass
class OperatorCallExp:

    pass
class superimposed_BinaryOperatorCallExp(OperatorCallExp):

    pass
class superimposed_UnaryOperatorCallExp(OperatorCallExp):

    pass
class superimposed_OclExpression(ABC):

    pass
class superimposed_VariableDeclaration:

    def __init__(self, name: str, superimposed_VariableDeclaration: "superimposed_OclExpression" = None, superimposed_VariableDeclaration2: "superimposed_OclType" = None, superimposed_VariableDeclaration4: "superimposed_VariableExp" = None, superimposed_VariableDeclaration6: "superimposed_LetExp" = None):
        self.name = name
        self.superimposed_VariableDeclaration = superimposed_VariableDeclaration
        self.superimposed_VariableDeclaration2 = superimposed_VariableDeclaration2
        self.superimposed_VariableDeclaration4 = superimposed_VariableDeclaration4
        self.superimposed_VariableDeclaration6 = superimposed_VariableDeclaration6
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def superimposed_VariableDeclaration2(self):
        return self.__superimposed_VariableDeclaration2

    @superimposed_VariableDeclaration2.setter
    def superimposed_VariableDeclaration2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_superimposed_VariableDeclaration__superimposed_VariableDeclaration2", None)
        self.__superimposed_VariableDeclaration2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "superimposed_OclType"):
                opp_val = getattr(old_value, "superimposed_OclType", None)
                if opp_val == self:
                    setattr(old_value, "superimposed_OclType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "superimposed_OclType"):
                opp_val = getattr(value, "superimposed_OclType", None)
                setattr(value, "superimposed_OclType", self)

    @property
    def superimposed_VariableDeclaration4(self):
        return self.__superimposed_VariableDeclaration4

    @superimposed_VariableDeclaration4.setter
    def superimposed_VariableDeclaration4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_superimposed_VariableDeclaration__superimposed_VariableDeclaration4", None)
        self.__superimposed_VariableDeclaration4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "superimposed_VariableExp"):
                opp_val = getattr(old_value, "superimposed_VariableExp", None)
                if opp_val == self:
                    setattr(old_value, "superimposed_VariableExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "superimposed_VariableExp"):
                opp_val = getattr(value, "superimposed_VariableExp", None)
                setattr(value, "superimposed_VariableExp", self)

    @property
    def superimposed_VariableDeclaration(self):
        return self.__superimposed_VariableDeclaration

    @superimposed_VariableDeclaration.setter
    def superimposed_VariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_superimposed_VariableDeclaration__superimposed_VariableDeclaration", None)
        self.__superimposed_VariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "superimposed_OclExpression"):
                opp_val = getattr(old_value, "superimposed_OclExpression", None)
                if opp_val == self:
                    setattr(old_value, "superimposed_OclExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "superimposed_OclExpression"):
                opp_val = getattr(value, "superimposed_OclExpression", None)
                setattr(value, "superimposed_OclExpression", self)

    @property
    def superimposed_VariableDeclaration6(self):
        return self.__superimposed_VariableDeclaration6

    @superimposed_VariableDeclaration6.setter
    def superimposed_VariableDeclaration6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_superimposed_VariableDeclaration__superimposed_VariableDeclaration6", None)
        self.__superimposed_VariableDeclaration6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "superimposed_LetExp"):
                opp_val = getattr(old_value, "superimposed_LetExp", None)
                if opp_val == self:
                    setattr(old_value, "superimposed_LetExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "superimposed_LetExp"):
                opp_val = getattr(value, "superimposed_LetExp", None)
                setattr(value, "superimposed_LetExp", self)
