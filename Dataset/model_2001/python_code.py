from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class TokenType(Enum):
    Basic = "Basic"
    External = "External"
    Undeveloped = "Undeveloped"
    Intermediate = "Intermediate"
    Component = "Component"
    System = "System"
    Unhandled = "Unhandled"
    Sink = "Sink"
class TokenTraceType(Enum):
    TokenGraph = "TokenGraph"
    TokenTrace = "TokenTrace"
    CompositeParts = "CompositeParts"
    MinimalCutSet = "MinimalCutSet"


############################################
# Definition of Classes
############################################

class MultiLiteralConstraint:

    pass
class TokenTrace_Literal:

    pass
class TokenTrace_EObject:

    pass
class TokenTrace_Token(MultiLiteralConstraint):

    def __init__(self, name: str, message: str, tokenType: str, referenceCount: int, assignedProbability: str, computedProbability: str, scale: str, TokenTrace_Token: "TokenTrace_TokenTrace" = None, TokenTrace_Token5: "TokenTrace_TokenTrace" = None, TokenTrace_Token10: "TokenTrace_Token" = None, TokenTrace_Token8: set["TokenTrace_Token"] = None, TokenTrace_Token12: "TokenTrace_EObject" = None, TokenTrace_Token15: "TokenTrace_Literal" = None, TokenTrace_Token18: set["TokenTrace_Literal"] = None):
        self.name = name
        self.message = message
        self.tokenType = tokenType
        self.referenceCount = referenceCount
        self.assignedProbability = assignedProbability
        self.computedProbability = computedProbability
        self.scale = scale
        self.TokenTrace_Token = TokenTrace_Token
        self.TokenTrace_Token5 = TokenTrace_Token5
        self.TokenTrace_Token10 = TokenTrace_Token10
        self.TokenTrace_Token8 = TokenTrace_Token8 if TokenTrace_Token8 is not None else set()
        self.TokenTrace_Token12 = TokenTrace_Token12
        self.TokenTrace_Token15 = TokenTrace_Token15
        self.TokenTrace_Token18 = TokenTrace_Token18 if TokenTrace_Token18 is not None else set()
        
    @property
    def tokenType(self) -> str:
        return self.__tokenType

    @tokenType.setter
    def tokenType(self, tokenType: str):
        self.__tokenType = tokenType

    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message

    @property
    def scale(self) -> str:
        return self.__scale

    @scale.setter
    def scale(self, scale: str):
        self.__scale = scale

    @property
    def referenceCount(self) -> int:
        return self.__referenceCount

    @referenceCount.setter
    def referenceCount(self, referenceCount: int):
        self.__referenceCount = referenceCount

    @property
    def assignedProbability(self) -> str:
        return self.__assignedProbability

    @assignedProbability.setter
    def assignedProbability(self, assignedProbability: str):
        self.__assignedProbability = assignedProbability

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def computedProbability(self) -> str:
        return self.__computedProbability

    @computedProbability.setter
    def computedProbability(self, computedProbability: str):
        self.__computedProbability = computedProbability

    @property
    def TokenTrace_Token15(self):
        return self.__TokenTrace_Token15

    @TokenTrace_Token15.setter
    def TokenTrace_Token15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TokenTrace_Token__TokenTrace_Token15", None)
        self.__TokenTrace_Token15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TokenTrace_Literal16"):
                opp_val = getattr(old_value, "TokenTrace_Literal16", None)
                if opp_val == self:
                    setattr(old_value, "TokenTrace_Literal16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TokenTrace_Literal16"):
                opp_val = getattr(value, "TokenTrace_Literal16", None)
                setattr(value, "TokenTrace_Literal16", self)

    @property
    def TokenTrace_Token10(self):
        return self.__TokenTrace_Token10

    @TokenTrace_Token10.setter
    def TokenTrace_Token10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TokenTrace_Token__TokenTrace_Token10", None)
        self.__TokenTrace_Token10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TokenTrace_Token8"):
                opp_val = getattr(old_value, "TokenTrace_Token8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TokenTrace_Token8"):
                opp_val = getattr(value, "TokenTrace_Token8", None)
                if opp_val is None:
                    setattr(value, "TokenTrace_Token8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def TokenTrace_Token8(self):
        return self.__TokenTrace_Token8

    @TokenTrace_Token8.setter
    def TokenTrace_Token8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TokenTrace_Token__TokenTrace_Token8", None)
        self.__TokenTrace_Token8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TokenTrace_Token10"):
                    opp_val = getattr(item, "TokenTrace_Token10", None)
                    
                    if opp_val == self:
                        setattr(item, "TokenTrace_Token10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TokenTrace_Token10"):
                    opp_val = getattr(item, "TokenTrace_Token10", None)
                    
                    setattr(item, "TokenTrace_Token10", self)
                    

    @property
    def TokenTrace_Token(self):
        return self.__TokenTrace_Token

    @TokenTrace_Token.setter
    def TokenTrace_Token(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TokenTrace_Token__TokenTrace_Token", None)
        self.__TokenTrace_Token = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TokenTrace_TokenTrace"):
                opp_val = getattr(old_value, "TokenTrace_TokenTrace", None)
                if opp_val == self:
                    setattr(old_value, "TokenTrace_TokenTrace", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TokenTrace_TokenTrace"):
                opp_val = getattr(value, "TokenTrace_TokenTrace", None)
                setattr(value, "TokenTrace_TokenTrace", self)

    @property
    def TokenTrace_Token18(self):
        return self.__TokenTrace_Token18

    @TokenTrace_Token18.setter
    def TokenTrace_Token18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TokenTrace_Token__TokenTrace_Token18", None)
        self.__TokenTrace_Token18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TokenTrace_Literal19"):
                    opp_val = getattr(item, "TokenTrace_Literal19", None)
                    
                    if opp_val == self:
                        setattr(item, "TokenTrace_Literal19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TokenTrace_Literal19"):
                    opp_val = getattr(item, "TokenTrace_Literal19", None)
                    
                    setattr(item, "TokenTrace_Literal19", self)
                    

    @property
    def TokenTrace_Token12(self):
        return self.__TokenTrace_Token12

    @TokenTrace_Token12.setter
    def TokenTrace_Token12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TokenTrace_Token__TokenTrace_Token12", None)
        self.__TokenTrace_Token12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TokenTrace_EObject13"):
                opp_val = getattr(old_value, "TokenTrace_EObject13", None)
                if opp_val == self:
                    setattr(old_value, "TokenTrace_EObject13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TokenTrace_EObject13"):
                opp_val = getattr(value, "TokenTrace_EObject13", None)
                setattr(value, "TokenTrace_EObject13", self)

    @property
    def TokenTrace_Token5(self):
        return self.__TokenTrace_Token5

    @TokenTrace_Token5.setter
    def TokenTrace_Token5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TokenTrace_Token__TokenTrace_Token5", None)
        self.__TokenTrace_Token5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TokenTrace_TokenTrace4"):
                opp_val = getattr(old_value, "TokenTrace_TokenTrace4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TokenTrace_TokenTrace4"):
                opp_val = getattr(value, "TokenTrace_TokenTrace4", None)
                if opp_val is None:
                    setattr(value, "TokenTrace_TokenTrace4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getProbability(self) -> str:
        # TODO: Implement getProbability method
        pass

class TokenTrace_TokenTrace:

    def __init__(self, name: str, message: str, tokenTraceType: str, TokenTrace_TokenTrace: "TokenTrace_Token" = None, TokenTrace_TokenTrace2: "TokenTrace_EObject" = None, TokenTrace_TokenTrace4: set["TokenTrace_Token"] = None, TokenTrace_TokenTrace7: "TokenTrace_Literal" = None):
        self.name = name
        self.message = message
        self.tokenTraceType = tokenTraceType
        self.TokenTrace_TokenTrace = TokenTrace_TokenTrace
        self.TokenTrace_TokenTrace2 = TokenTrace_TokenTrace2
        self.TokenTrace_TokenTrace4 = TokenTrace_TokenTrace4 if TokenTrace_TokenTrace4 is not None else set()
        self.TokenTrace_TokenTrace7 = TokenTrace_TokenTrace7
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message

    @property
    def tokenTraceType(self) -> str:
        return self.__tokenTraceType

    @tokenTraceType.setter
    def tokenTraceType(self, tokenTraceType: str):
        self.__tokenTraceType = tokenTraceType

    @property
    def TokenTrace_TokenTrace(self):
        return self.__TokenTrace_TokenTrace

    @TokenTrace_TokenTrace.setter
    def TokenTrace_TokenTrace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TokenTrace_TokenTrace__TokenTrace_TokenTrace", None)
        self.__TokenTrace_TokenTrace = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TokenTrace_Token"):
                opp_val = getattr(old_value, "TokenTrace_Token", None)
                if opp_val == self:
                    setattr(old_value, "TokenTrace_Token", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TokenTrace_Token"):
                opp_val = getattr(value, "TokenTrace_Token", None)
                setattr(value, "TokenTrace_Token", self)

    @property
    def TokenTrace_TokenTrace2(self):
        return self.__TokenTrace_TokenTrace2

    @TokenTrace_TokenTrace2.setter
    def TokenTrace_TokenTrace2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TokenTrace_TokenTrace__TokenTrace_TokenTrace2", None)
        self.__TokenTrace_TokenTrace2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TokenTrace_EObject"):
                opp_val = getattr(old_value, "TokenTrace_EObject", None)
                if opp_val == self:
                    setattr(old_value, "TokenTrace_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TokenTrace_EObject"):
                opp_val = getattr(value, "TokenTrace_EObject", None)
                setattr(value, "TokenTrace_EObject", self)

    @property
    def TokenTrace_TokenTrace7(self):
        return self.__TokenTrace_TokenTrace7

    @TokenTrace_TokenTrace7.setter
    def TokenTrace_TokenTrace7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TokenTrace_TokenTrace__TokenTrace_TokenTrace7", None)
        self.__TokenTrace_TokenTrace7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TokenTrace_Literal"):
                opp_val = getattr(old_value, "TokenTrace_Literal", None)
                if opp_val == self:
                    setattr(old_value, "TokenTrace_Literal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TokenTrace_Literal"):
                opp_val = getattr(value, "TokenTrace_Literal", None)
                setattr(value, "TokenTrace_Literal", self)

    @property
    def TokenTrace_TokenTrace4(self):
        return self.__TokenTrace_TokenTrace4

    @TokenTrace_TokenTrace4.setter
    def TokenTrace_TokenTrace4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TokenTrace_TokenTrace__TokenTrace_TokenTrace4", None)
        self.__TokenTrace_TokenTrace4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TokenTrace_Token5"):
                    opp_val = getattr(item, "TokenTrace_Token5", None)
                    
                    if opp_val == self:
                        setattr(item, "TokenTrace_Token5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TokenTrace_Token5"):
                    opp_val = getattr(item, "TokenTrace_Token5", None)
                    
                    setattr(item, "TokenTrace_Token5", self)
                    
