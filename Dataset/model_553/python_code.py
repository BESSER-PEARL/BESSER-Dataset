from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class GlueType(Enum):
    before = "before"
    around = "around"
    after = "after"
class ArmaniSetTypes(Enum):
    Ports = "Ports"
    Representations = "Representations"
    Properties = "Properties"
    Elements = "Elements"
    Components = "Components"
    Connectors = "Connectors"
    Roles = "Roles"
class ArmaniQuantifier(Enum):
    forall = "forall"
    exists = "exists"
class ArmaniTypes(Enum):
    Component = "Component"
    Connector = "Connector"
    Role = "Role"
    Port = "Port"
    Representation = "Representation"
    Property = "Property"


############################################
# Definition of Classes
############################################

class ArmaniDesignRuleExpression:

    pass
class aspectualacme_ArmaniQuantifiedExpression(ArmaniDesignRuleExpression):

    def __init__(self, quantifier: str, aspectualacme_ArmaniQuantifiedExpression: "aspectualacme_ArmaniVariable" = None, aspectualacme_ArmaniQuantifiedExpression183: "aspectualacme_ArmaniSetExpression" = None, aspectualacme_ArmaniQuantifiedExpression186: "aspectualacme_ArmaniDesignRuleExpression" = None):
        self.quantifier = quantifier
        self.aspectualacme_ArmaniQuantifiedExpression = aspectualacme_ArmaniQuantifiedExpression
        self.aspectualacme_ArmaniQuantifiedExpression183 = aspectualacme_ArmaniQuantifiedExpression183
        self.aspectualacme_ArmaniQuantifiedExpression186 = aspectualacme_ArmaniQuantifiedExpression186
        
    @property
    def quantifier(self) -> str:
        return self.__quantifier

    @quantifier.setter
    def quantifier(self, quantifier: str):
        self.__quantifier = quantifier

    @property
    def aspectualacme_ArmaniQuantifiedExpression(self):
        return self.__aspectualacme_ArmaniQuantifiedExpression

    @aspectualacme_ArmaniQuantifiedExpression.setter
    def aspectualacme_ArmaniQuantifiedExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aspectualacme_ArmaniQuantifiedExpression__aspectualacme_ArmaniQuantifiedExpression", None)
        self.__aspectualacme_ArmaniQuantifiedExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aspectualacme_ArmaniVariable181"):
                opp_val = getattr(old_value, "aspectualacme_ArmaniVariable181", None)
                if opp_val == self:
                    setattr(old_value, "aspectualacme_ArmaniVariable181", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aspectualacme_ArmaniVariable181"):
                opp_val = getattr(value, "aspectualacme_ArmaniVariable181", None)
                setattr(value, "aspectualacme_ArmaniVariable181", self)

    @property
    def aspectualacme_ArmaniQuantifiedExpression183(self):
        return self.__aspectualacme_ArmaniQuantifiedExpression183

    @aspectualacme_ArmaniQuantifiedExpression183.setter
    def aspectualacme_ArmaniQuantifiedExpression183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aspectualacme_ArmaniQuantifiedExpression__aspectualacme_ArmaniQuantifiedExpression183", None)
        self.__aspectualacme_ArmaniQuantifiedExpression183 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aspectualacme_ArmaniSetExpression184"):
                opp_val = getattr(old_value, "aspectualacme_ArmaniSetExpression184", None)
                if opp_val == self:
                    setattr(old_value, "aspectualacme_ArmaniSetExpression184", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aspectualacme_ArmaniSetExpression184"):
                opp_val = getattr(value, "aspectualacme_ArmaniSetExpression184", None)
                setattr(value, "aspectualacme_ArmaniSetExpression184", self)

    @property
    def aspectualacme_ArmaniQuantifiedExpression186(self):
        return self.__aspectualacme_ArmaniQuantifiedExpression186

    @aspectualacme_ArmaniQuantifiedExpression186.setter
    def aspectualacme_ArmaniQuantifiedExpression186(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aspectualacme_ArmaniQuantifiedExpression__aspectualacme_ArmaniQuantifiedExpression186", None)
        self.__aspectualacme_ArmaniQuantifiedExpression186 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aspectualacme_ArmaniDesignRuleExpression187"):
                opp_val = getattr(old_value, "aspectualacme_ArmaniDesignRuleExpression187", None)
                if opp_val == self:
                    setattr(old_value, "aspectualacme_ArmaniDesignRuleExpression187", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aspectualacme_ArmaniDesignRuleExpression187"):
                opp_val = getattr(value, "aspectualacme_ArmaniDesignRuleExpression187", None)
                setattr(value, "aspectualacme_ArmaniDesignRuleExpression187", self)

class aspectualacme_ArmaniBooleanExpression(ArmaniDesignRuleExpression):

    pass
class ArmaniExpression:

    pass
class aspectualacme_ArmaniEqualityExpression(ArmaniExpression):

    def __init__(self, operators: str, aspectualacme_ArmaniEqualityExpression: set["aspectualacme_ArmaniRelationalExpression"] = None, aspectualacme_ArmaniEqualityExpression172: "aspectualacme_ArmaniIffExpression" = None):
        self.operators = operators
        self.aspectualacme_ArmaniEqualityExpression = aspectualacme_ArmaniEqualityExpression if aspectualacme_ArmaniEqualityExpression is not None else set()
        self.aspectualacme_ArmaniEqualityExpression172 = aspectualacme_ArmaniEqualityExpression172
        
    @property
    def operators(self) -> str:
        return self.__operators

    @operators.setter
    def operators(self, operators: str):
        self.__operators = operators

    @property
    def aspectualacme_ArmaniEqualityExpression172(self):
        return self.__aspectualacme_ArmaniEqualityExpression172

    @aspectualacme_ArmaniEqualityExpression172.setter
    def aspectualacme_ArmaniEqualityExpression172(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aspectualacme_ArmaniEqualityExpression__aspectualacme_ArmaniEqualityExpression172", None)
        self.__aspectualacme_ArmaniEqualityExpression172 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aspectualacme_ArmaniIffExpression"):
                opp_val = getattr(old_value, "aspectualacme_ArmaniIffExpression", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aspectualacme_ArmaniIffExpression"):
                opp_val = getattr(value, "aspectualacme_ArmaniIffExpression", None)
                if opp_val is None:
                    setattr(value, "aspectualacme_ArmaniIffExpression", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aspectualacme_ArmaniEqualityExpression(self):
        return self.__aspectualacme_ArmaniEqualityExpression

    @aspectualacme_ArmaniEqualityExpression.setter
    def aspectualacme_ArmaniEqualityExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aspectualacme_ArmaniEqualityExpression__aspectualacme_ArmaniEqualityExpression", None)
        self.__aspectualacme_ArmaniEqualityExpression = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aspectualacme_ArmaniRelationalExpression170"):
                    opp_val = getattr(item, "aspectualacme_ArmaniRelationalExpression170", None)
                    
                    if opp_val == self:
                        setattr(item, "aspectualacme_ArmaniRelationalExpression170", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aspectualacme_ArmaniRelationalExpression170"):
                    opp_val = getattr(item, "aspectualacme_ArmaniRelationalExpression170", None)
                    
                    setattr(item, "aspectualacme_ArmaniRelationalExpression170", self)
                    

class aspectualacme_ArmaniImpliesExpression(ArmaniExpression):

    pass
class aspectualacme_ArmaniIffExpression(ArmaniExpression):

    pass
class aspectualacme_ArmaniAdditiveExpression(ArmaniExpression):

    def __init__(self, operators: str, aspectualacme_ArmaniAdditiveExpression: set["aspectualacme_ArmaniMultiplicativeExpression"] = None, aspectualacme_ArmaniAdditiveExpression168: "aspectualacme_ArmaniRelationalExpression" = None):
        self.operators = operators
        self.aspectualacme_ArmaniAdditiveExpression = aspectualacme_ArmaniAdditiveExpression if aspectualacme_ArmaniAdditiveExpression is not None else set()
        self.aspectualacme_ArmaniAdditiveExpression168 = aspectualacme_ArmaniAdditiveExpression168
        
    @property
    def operators(self) -> str:
        return self.__operators

    @operators.setter
    def operators(self, operators: str):
        self.__operators = operators

    @property
    def aspectualacme_ArmaniAdditiveExpression168(self):
        return self.__aspectualacme_ArmaniAdditiveExpression168

    @aspectualacme_ArmaniAdditiveExpression168.setter
    def aspectualacme_ArmaniAdditiveExpression168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aspectualacme_ArmaniAdditiveExpression__aspectualacme_ArmaniAdditiveExpression168", None)
        self.__aspectualacme_ArmaniAdditiveExpression168 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aspectualacme_ArmaniRelationalExpression"):
                opp_val = getattr(old_value, "aspectualacme_ArmaniRelationalExpression", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aspectualacme_ArmaniRelationalExpression"):
                opp_val = getattr(value, "aspectualacme_ArmaniRelationalExpression", None)
                if opp_val is None:
                    setattr(value, "aspectualacme_ArmaniRelationalExpression", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aspectualacme_ArmaniAdditiveExpression(self):
        return self.__aspectualacme_ArmaniAdditiveExpression

    @aspectualacme_ArmaniAdditiveExpression.setter
    def aspectualacme_ArmaniAdditiveExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aspectualacme_ArmaniAdditiveExpression__aspectualacme_ArmaniAdditiveExpression", None)
        self.__aspectualacme_ArmaniAdditiveExpression = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aspectualacme_ArmaniMultiplicativeExpression166"):
                    opp_val = getattr(item, "aspectualacme_ArmaniMultiplicativeExpression166", None)
                    
                    if opp_val == self:
                        setattr(item, "aspectualacme_ArmaniMultiplicativeExpression166", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aspectualacme_ArmaniMultiplicativeExpression166"):
                    opp_val = getattr(item, "aspectualacme_ArmaniMultiplicativeExpression166", None)
                    
                    setattr(item, "aspectualacme_ArmaniMultiplicativeExpression166", self)
                    

class aspectualacme_ArmaniVariable(ArmaniExpression):

    def __init__(self, basicType: str, id: str, aspectualacme_ArmaniVariable: "aspectualacme_TypeDefinition" = None, aspectualacme_ArmaniVariable181: "aspectualacme_ArmaniQuantifiedExpression" = None):
        self.basicType = basicType
        self.id = id
        self.aspectualacme_ArmaniVariable = aspectualacme_ArmaniVariable
        self.aspectualacme_ArmaniVariable181 = aspectualacme_ArmaniVariable181
        
    @property
    def basicType(self) -> str:
        return self.__basicType

    @basicType.setter
    def basicType(self, basicType: str):
        self.__basicType = basicType

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def aspectualacme_ArmaniVariable181(self):
        return self.__aspectualacme_ArmaniVariable181

    @aspectualacme_ArmaniVariable181.setter
    def aspectualacme_ArmaniVariable181(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aspectualacme_ArmaniVariable__aspectualacme_ArmaniVariable181", None)
        self.__aspectualacme_ArmaniVariable181 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aspectualacme_ArmaniQuantifiedExpression"):
                opp_val = getattr(old_value, "aspectualacme_ArmaniQuantifiedExpression", None)
                if opp_val == self:
                    setattr(old_value, "aspectualacme_ArmaniQuantifiedExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aspectualacme_ArmaniQuantifiedExpression"):
                opp_val = getattr(value, "aspectualacme_ArmaniQuantifiedExpression", None)
                setattr(value, "aspectualacme_ArmaniQuantifiedExpression", self)

    @property
    def aspectualacme_ArmaniVariable(self):
        return self.__aspectualacme_ArmaniVariable

    @aspectualacme_ArmaniVariable.setter
    def aspectualacme_ArmaniVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aspectualacme_ArmaniVariable__aspectualacme_ArmaniVariable", None)
        self.__aspectualacme_ArmaniVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aspectualacme_TypeDefinition"):
                opp_val = getattr(old_value, "aspectualacme_TypeDefinition", None)
                if opp_val == self:
                    setattr(old_value, "aspectualacme_TypeDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aspectualacme_TypeDefinition"):
                opp_val = getattr(value, "aspectualacme_TypeDefinition", None)
                setattr(value, "aspectualacme_TypeDefinition", self)

class aspectualacme_ArmaniOrExpression(ArmaniExpression):

    def __init__(self, operators: str, aspectualacme_ArmaniOrExpression179: "aspectualacme_ArmaniBooleanExpression" = None, aspectualacme_ArmaniOrExpression: set["aspectualacme_ArmaniImpliesExpression"] = None):
        self.operators = operators
        self.aspectualacme_ArmaniOrExpression179 = aspectualacme_ArmaniOrExpression179
        self.aspectualacme_ArmaniOrExpression = aspectualacme_ArmaniOrExpression if aspectualacme_ArmaniOrExpression is not None else set()
        
    @property
    def operators(self) -> str:
        return self.__operators

    @operators.setter
    def operators(self, operators: str):
        self.__operators = operators

    @property
    def aspectualacme_ArmaniOrExpression(self):
        return self.__aspectualacme_ArmaniOrExpression

    @aspectualacme_ArmaniOrExpression.setter
    def aspectualacme_ArmaniOrExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aspectualacme_ArmaniOrExpression__aspectualacme_ArmaniOrExpression", None)
        self.__aspectualacme_ArmaniOrExpression = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aspectualacme_ArmaniImpliesExpression176"):
                    opp_val = getattr(item, "aspectualacme_ArmaniImpliesExpression176", None)
                    
                    if opp_val == self:
                        setattr(item, "aspectualacme_ArmaniImpliesExpression176", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aspectualacme_ArmaniImpliesExpression176"):
                    opp_val = getattr(item, "aspectualacme_ArmaniImpliesExpression176", None)
                    
                    setattr(item, "aspectualacme_ArmaniImpliesExpression176", self)
                    

    @property
    def aspectualacme_ArmaniOrExpression179(self):
        return self.__aspectualacme_ArmaniOrExpression179

    @aspectualacme_ArmaniOrExpression179.setter
    def aspectualacme_ArmaniOrExpression179(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aspectualacme_ArmaniOrExpression__aspectualacme_ArmaniOrExpression179", None)
        self.__aspectualacme_ArmaniOrExpression179 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aspectualacme_ArmaniBooleanExpression"):
                opp_val = getattr(old_value, "aspectualacme_ArmaniBooleanExpression", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aspectualacme_ArmaniBooleanExpression"):
                opp_val = getattr(value, "aspectualacme_ArmaniBooleanExpression", None)
                if opp_val is None:
                    setattr(value, "aspectualacme_ArmaniBooleanExpression", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class aspectualacme_ArmaniRelationalExpression(ArmaniExpression):

    def __init__(self, operators: str, aspectualacme_ArmaniRelationalExpression170: "aspectualacme_ArmaniEqualityExpression" = None, aspectualacme_ArmaniRelationalExpression: set["aspectualacme_ArmaniAdditiveExpression"] = None):
        self.operators = operators
        self.aspectualacme_ArmaniRelationalExpression170 = aspectualacme_ArmaniRelationalExpression170
        self.aspectualacme_ArmaniRelationalExpression = aspectualacme_ArmaniRelationalExpression if aspectualacme_ArmaniRelationalExpression is not None else set()
        
    @property
    def operators(self) -> str:
        return self.__operators

    @operators.setter
    def operators(self, operators: str):
        self.__operators = operators

    @property
    def aspectualacme_ArmaniRelationalExpression(self):
        return self.__aspectualacme_ArmaniRelationalExpression

    @aspectualacme_ArmaniRelationalExpression.setter
    def aspectualacme_ArmaniRelationalExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aspectualacme_ArmaniRelationalExpression__aspectualacme_ArmaniRelationalExpression", None)
        self.__aspectualacme_ArmaniRelationalExpression = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aspectualacme_ArmaniAdditiveExpression168"):
                    opp_val = getattr(item, "aspectualacme_ArmaniAdditiveExpression168", None)
                    
                    if opp_val == self:
                        setattr(item, "aspectualacme_ArmaniAdditiveExpression168", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aspectualacme_ArmaniAdditiveExpression168"):
                    opp_val = getattr(item, "aspectualacme_ArmaniAdditiveExpression168", None)
                    
                    setattr(item, "aspectualacme_ArmaniAdditiveExpression168", self)
                    

    @property
    def aspectualacme_ArmaniRelationalExpression170(self):
        return self.__aspectualacme_ArmaniRelationalExpression170

    @aspectualacme_ArmaniRelationalExpression170.setter
    def aspectualacme_ArmaniRelationalExpression170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aspectualacme_ArmaniRelationalExpression__aspectualacme_ArmaniRelationalExpression170", None)
        self.__aspectualacme_ArmaniRelationalExpression170 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aspectualacme_ArmaniEqualityExpression"):
                opp_val = getattr(old_value, "aspectualacme_ArmaniEqualityExpression", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aspectualacme_ArmaniEqualityExpression"):
                opp_val = getattr(value, "aspectualacme_ArmaniEqualityExpression", None)
                if opp_val is None:
                    setattr(value, "aspectualacme_ArmaniEqualityExpression", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class aspectualacme_ArmaniUnaryExpression(ArmaniExpression):

    def __init__(self, operator: str, aspectualacme_ArmaniUnaryExpression: "aspectualacme_ArmaniUnaryExpression" = None, aspectualacme_ArmaniUnaryExpression161: "aspectualacme_ArmaniUnaryExpression" = None, aspectualacme_ArmaniUnaryExpression164: "aspectualacme_ArmaniMultiplicativeExpression" = None):
        self.operator = operator
        self.aspectualacme_ArmaniUnaryExpression = aspectualacme_ArmaniUnaryExpression
        self.aspectualacme_ArmaniUnaryExpression161 = aspectualacme_ArmaniUnaryExpression161
        self.aspectualacme_ArmaniUnaryExpression164 = aspectualacme_ArmaniUnaryExpression164
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def aspectualacme_ArmaniUnaryExpression(self):
        return self.__aspectualacme_ArmaniUnaryExpression

    @aspectualacme_ArmaniUnaryExpression.setter
    def aspectualacme_ArmaniUnaryExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aspectualacme_ArmaniUnaryExpression__aspectualacme_ArmaniUnaryExpression", None)
        self.__aspectualacme_ArmaniUnaryExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aspectualacme_ArmaniUnaryExpression161"):
                opp_val = getattr(old_value, "aspectualacme_ArmaniUnaryExpression161", None)
                if opp_val == self:
                    setattr(old_value, "aspectualacme_ArmaniUnaryExpression161", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aspectualacme_ArmaniUnaryExpression161"):
                opp_val = getattr(value, "aspectualacme_ArmaniUnaryExpression161", None)
                setattr(value, "aspectualacme_ArmaniUnaryExpression161", self)

    @property
    def aspectualacme_ArmaniUnaryExpression161(self):
        return self.__aspectualacme_ArmaniUnaryExpression161

    @aspectualacme_ArmaniUnaryExpression161.setter
    def aspectualacme_ArmaniUnaryExpression161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aspectualacme_ArmaniUnaryExpression__aspectualacme_ArmaniUnaryExpression161", None)
        self.__aspectualacme_ArmaniUnaryExpression161 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aspectualacme_ArmaniUnaryExpression"):
                opp_val = getattr(old_value, "aspectualacme_ArmaniUnaryExpression", None)
                if opp_val == self:
                    setattr(old_value, "aspectualacme_ArmaniUnaryExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aspectualacme_ArmaniUnaryExpression"):
                opp_val = getattr(value, "aspectualacme_ArmaniUnaryExpression", None)
                setattr(value, "aspectualacme_ArmaniUnaryExpression", self)

    @property
    def aspectualacme_ArmaniUnaryExpression164(self):
        return self.__aspectualacme_ArmaniUnaryExpression164

    @aspectualacme_ArmaniUnaryExpression164.setter
    def aspectualacme_ArmaniUnaryExpression164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aspectualacme_ArmaniUnaryExpression__aspectualacme_ArmaniUnaryExpression164", None)
        self.__aspectualacme_ArmaniUnaryExpression164 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aspectualacme_ArmaniMultiplicativeExpression"):
                opp_val = getattr(old_value, "aspectualacme_ArmaniMultiplicativeExpression", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aspectualacme_ArmaniMultiplicativeExpression"):
                opp_val = getattr(value, "aspectualacme_ArmaniMultiplicativeExpression", None)
                if opp_val is None:
                    setattr(value, "aspectualacme_ArmaniMultiplicativeExpression", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ArmaniUnaryExpression:

    pass
class aspectualacme_ArmaniMultiplicativeExpression(ArmaniExpression):

    def __init__(self, operators: str, aspectualacme_ArmaniMultiplicativeExpression: set["aspectualacme_ArmaniUnaryExpression"] = None, aspectualacme_ArmaniMultiplicativeExpression166: "aspectualacme_ArmaniAdditiveExpression" = None):
        self.operators = operators
        self.aspectualacme_ArmaniMultiplicativeExpression = aspectualacme_ArmaniMultiplicativeExpression if aspectualacme_ArmaniMultiplicativeExpression is not None else set()
        self.aspectualacme_ArmaniMultiplicativeExpression166 = aspectualacme_ArmaniMultiplicativeExpression166
        
    @property
    def operators(self) -> str:
        return self.__operators

    @operators.setter
    def operators(self, operators: str):
        self.__operators = operators

    @property
    def aspectualacme_ArmaniMultiplicativeExpression(self):
        return self.__aspectualacme_ArmaniMultiplicativeExpression

    @aspectualacme_ArmaniMultiplicativeExpression.setter
    def aspectualacme_ArmaniMultiplicativeExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aspectualacme_ArmaniMultiplicativeExpression__aspectualacme_ArmaniMultiplicativeExpression", None)
        self.__aspectualacme_ArmaniMultiplicativeExpression = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aspectualacme_ArmaniUnaryExpression164"):
                    opp_val = getattr(item, "aspectualacme_ArmaniUnaryExpression164", None)
                    
                    if opp_val == self:
                        setattr(item, "aspectualacme_ArmaniUnaryExpression164", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aspectualacme_ArmaniUnaryExpression164"):
                    opp_val = getattr(item, "aspectualacme_ArmaniUnaryExpression164", None)
                    
                    setattr(item, "aspectualacme_ArmaniUnaryExpression164", self)
                    

    @property
    def aspectualacme_ArmaniMultiplicativeExpression166(self):
        return self.__aspectualacme_ArmaniMultiplicativeExpression166

    @aspectualacme_ArmaniMultiplicativeExpression166.setter
    def aspectualacme_ArmaniMultiplicativeExpression166(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aspectualacme_ArmaniMultiplicativeExpression__aspectualacme_ArmaniMultiplicativeExpression166", None)
        self.__aspectualacme_ArmaniMultiplicativeExpression166 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aspectualacme_ArmaniAdditiveExpression"):
                opp_val = getattr(old_value, "aspectualacme_ArmaniAdditiveExpression", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aspectualacme_ArmaniAdditiveExpression"):
                opp_val = getattr(value, "aspectualacme_ArmaniAdditiveExpression", None)
                if opp_val is None:
                    setattr(value, "aspectualacme_ArmaniAdditiveExpression", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ArmaniPrimitiveExpression:

    pass
class aspectualacme_ArmaniFunctionCall(ArmaniPrimitiveExpression):

    def __init__(self, functionId: str, aspectualacme_ArmaniFunctionCall: set["aspectualacme_ArmaniPrimitiveExpression"] = None):
        self.functionId = functionId
        self.aspectualacme_ArmaniFunctionCall = aspectualacme_ArmaniFunctionCall if aspectualacme_ArmaniFunctionCall is not None else set()
        
    @property
    def functionId(self) -> str:
        return self.__functionId

    @functionId.setter
    def functionId(self, functionId: str):
        self.__functionId = functionId

    @property
    def aspectualacme_ArmaniFunctionCall(self):
        return self.__aspectualacme_ArmaniFunctionCall

    @aspectualacme_ArmaniFunctionCall.setter
    def aspectualacme_ArmaniFunctionCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aspectualacme_ArmaniFunctionCall__aspectualacme_ArmaniFunctionCall", None)
        self.__aspectualacme_ArmaniFunctionCall = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aspectualacme_ArmaniPrimitiveExpression"):
                    opp_val = getattr(item, "aspectualacme_ArmaniPrimitiveExpression", None)
                    
                    if opp_val == self:
                        setattr(item, "aspectualacme_ArmaniPrimitiveExpression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aspectualacme_ArmaniPrimitiveExpression"):
                    opp_val = getattr(item, "aspectualacme_ArmaniPrimitiveExpression", None)
                    
                    setattr(item, "aspectualacme_ArmaniPrimitiveExpression", self)
                    

class aspectualacme_ArmaniExpression:

    pass
class aspectualacme_ArmaniDesignRuleExpression(ArmaniExpression):

    pass
class aspectualacme_ArmaniConstant(ArmaniPrimitiveExpression):

    pass
class aspectualacme_ArmaniSetExpression(ArmaniPrimitiveExpression):

    def __init__(self, reference: str, referenceType: str, aspectualacme_ArmaniSetExpression: set["aspectualacme_ArmaniConstant"] = None, aspectualacme_ArmaniSetExpression184: "aspectualacme_ArmaniQuantifiedExpression" = None):
        self.reference = reference
        self.referenceType = referenceType
        self.aspectualacme_ArmaniSetExpression = aspectualacme_ArmaniSetExpression if aspectualacme_ArmaniSetExpression is not None else set()
        self.aspectualacme_ArmaniSetExpression184 = aspectualacme_ArmaniSetExpression184
        
    @property
    def referenceType(self) -> str:
        return self.__referenceType

    @referenceType.setter
    def referenceType(self, referenceType: str):
        self.__referenceType = referenceType

    @property
    def reference(self) -> str:
        return self.__reference

    @reference.setter
    def reference(self, reference: str):
        self.__reference = reference

    @property
    def aspectualacme_ArmaniSetExpression(self):
        return self.__aspectualacme_ArmaniSetExpression

    @aspectualacme_ArmaniSetExpression.setter
    def aspectualacme_ArmaniSetExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aspectualacme_ArmaniSetExpression__aspectualacme_ArmaniSetExpression", None)
        self.__aspectualacme_ArmaniSetExpression = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aspectualacme_ArmaniConstant"):
                    opp_val = getattr(item, "aspectualacme_ArmaniConstant", None)
                    
                    if opp_val == self:
                        setattr(item, "aspectualacme_ArmaniConstant", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aspectualacme_ArmaniConstant"):
                    opp_val = getattr(item, "aspectualacme_ArmaniConstant", None)
                    
                    setattr(item, "aspectualacme_ArmaniConstant", self)
                    

    @property
    def aspectualacme_ArmaniSetExpression184(self):
        return self.__aspectualacme_ArmaniSetExpression184

    @aspectualacme_ArmaniSetExpression184.setter
    def aspectualacme_ArmaniSetExpression184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aspectualacme_ArmaniSetExpression__aspectualacme_ArmaniSetExpression184", None)
        self.__aspectualacme_ArmaniSetExpression184 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aspectualacme_ArmaniQuantifiedExpression183"):
                opp_val = getattr(old_value, "aspectualacme_ArmaniQuantifiedExpression183", None)
                if opp_val == self:
                    setattr(old_value, "aspectualacme_ArmaniQuantifiedExpression183", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aspectualacme_ArmaniQuantifiedExpression183"):
                opp_val = getattr(value, "aspectualacme_ArmaniQuantifiedExpression183", None)
                setattr(value, "aspectualacme_ArmaniQuantifiedExpression183", self)

class aspectualacme_ArmaniPrimitiveExpression(ArmaniUnaryExpression):

    pass
class aspectualacme_Binding:

    pass
class BindableElement:

    pass
class attachableElement:

    pass
class Role:

    pass
class aspectualacme_CrosscuttingRole(Role):

    pass
class aspectualacme_BaseRole(Role):

    pass
class aspectualacme_Glue:

    def __init__(self, glueType: str, aspectualacme_Glue: "aspectualacme_ConnectorType" = None, Glue: "aspectualacme_Connector" = None, aspectualacme_Glue125: "aspectualacme_BaseRole" = None, aspectualacme_Glue128: "aspectualacme_CrosscuttingRole" = None, glue: "aspectualacme_Connector" = None):
        self.glueType = glueType
        self.aspectualacme_Glue = aspectualacme_Glue
        self.Glue = Glue
        self.aspectualacme_Glue125 = aspectualacme_Glue125
        self.aspectualacme_Glue128 = aspectualacme_Glue128
        self.glue = glue
        
    @property
    def glueType(self) -> str:
        return self.__glueType

    @glueType.setter
    def glueType(self, glueType: str):
        self.__glueType = glueType

    @property
    def glue(self):
        return self.__glue

    @glue.setter
    def glue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aspectualacme_Glue__glue", None)
        self.__glue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Connector131"):
                opp_val = getattr(old_value, "Connector131", None)
                if opp_val == self:
                    setattr(old_value, "Connector131", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Connector131"):
                opp_val = getattr(value, "Connector131", None)
                setattr(value, "Connector131", self)

    @property
    def aspectualacme_Glue128(self):
        return self.__aspectualacme_Glue128

    @aspectualacme_Glue128.setter
    def aspectualacme_Glue128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aspectualacme_Glue__aspectualacme_Glue128", None)
        self.__aspectualacme_Glue128 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aspectualacme_CrosscuttingRole129"):
                opp_val = getattr(old_value, "aspectualacme_CrosscuttingRole129", None)
                if opp_val == self:
                    setattr(old_value, "aspectualacme_CrosscuttingRole129", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aspectualacme_CrosscuttingRole129"):
                opp_val = getattr(value, "aspectualacme_CrosscuttingRole129", None)
                setattr(value, "aspectualacme_CrosscuttingRole129", self)

    @property
    def aspectualacme_Glue(self):
        return self.__aspectualacme_Glue

    @aspectualacme_Glue.setter
    def aspectualacme_Glue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aspectualacme_Glue__aspectualacme_Glue", None)
        self.__aspectualacme_Glue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aspectualacme_ConnectorType44"):
                opp_val = getattr(old_value, "aspectualacme_ConnectorType44", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aspectualacme_ConnectorType44"):
                opp_val = getattr(value, "aspectualacme_ConnectorType44", None)
                if opp_val is None:
                    setattr(value, "aspectualacme_ConnectorType44", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Glue(self):
        return self.__Glue

    @Glue.setter
    def Glue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aspectualacme_Glue__Glue", None)
        self.__Glue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connector"):
                opp_val = getattr(old_value, "connector", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connector"):
                opp_val = getattr(value, "connector", None)
                if opp_val is None:
                    setattr(value, "connector", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aspectualacme_Glue125(self):
        return self.__aspectualacme_Glue125

    @aspectualacme_Glue125.setter
    def aspectualacme_Glue125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aspectualacme_Glue__aspectualacme_Glue125", None)
        self.__aspectualacme_Glue125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aspectualacme_BaseRole126"):
                opp_val = getattr(old_value, "aspectualacme_BaseRole126", None)
                if opp_val == self:
                    setattr(old_value, "aspectualacme_BaseRole126", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aspectualacme_BaseRole126"):
                opp_val = getattr(value, "aspectualacme_BaseRole126", None)
                setattr(value, "aspectualacme_BaseRole126", self)

class aspectualacme_Role(attachableElement, BindableElement):

    pass
class aspectualacme_Port(attachableElement, BindableElement):

    pass
class TypeDefinition:

    pass
class aspectualacme_PropertyType(TypeDefinition):

    def __init__(self, type: str, values: str, PropertyType: "aspectualacme_Family" = None, prtypes: "aspectualacme_Family" = None, aspectualacme_PropertyType: "aspectualacme_Property" = None):
        self.type = type
        self.values = values
        self.PropertyType = PropertyType
        self.prtypes = prtypes
        self.aspectualacme_PropertyType = aspectualacme_PropertyType
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def values(self) -> str:
        return self.__values

    @values.setter
    def values(self, values: str):
        self.__values = values

    @property
    def PropertyType(self):
        return self.__PropertyType

    @PropertyType.setter
    def PropertyType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aspectualacme_PropertyType__PropertyType", None)
        self.__PropertyType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parentFamily25"):
                opp_val = getattr(old_value, "parentFamily25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parentFamily25"):
                opp_val = getattr(value, "parentFamily25", None)
                if opp_val is None:
                    setattr(value, "parentFamily25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def prtypes(self):
        return self.__prtypes

    @prtypes.setter
    def prtypes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aspectualacme_PropertyType__prtypes", None)
        self.__prtypes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Family48"):
                opp_val = getattr(old_value, "Family48", None)
                if opp_val == self:
                    setattr(old_value, "Family48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Family48"):
                opp_val = getattr(value, "Family48", None)
                setattr(value, "Family48", self)

    @property
    def aspectualacme_PropertyType(self):
        return self.__aspectualacme_PropertyType

    @aspectualacme_PropertyType.setter
    def aspectualacme_PropertyType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aspectualacme_PropertyType__aspectualacme_PropertyType", None)
        self.__aspectualacme_PropertyType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aspectualacme_Property118"):
                opp_val = getattr(old_value, "aspectualacme_Property118", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aspectualacme_Property118"):
                opp_val = getattr(value, "aspectualacme_Property118", None)
                if opp_val is None:
                    setattr(value, "aspectualacme_Property118", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class aspectualacme_WildCard(attachableElement):

    def __init__(self, expression: str, aspectualacme_WildCard: "aspectualacme_Family" = None, aspectualacme_WildCard58: "aspectualacme_System" = None):
        self.expression = expression
        self.aspectualacme_WildCard = aspectualacme_WildCard
        self.aspectualacme_WildCard58 = aspectualacme_WildCard58
        
    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

    @property
    def aspectualacme_WildCard(self):
        return self.__aspectualacme_WildCard

    @aspectualacme_WildCard.setter
    def aspectualacme_WildCard(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aspectualacme_WildCard__aspectualacme_WildCard", None)
        self.__aspectualacme_WildCard = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aspectualacme_Family15"):
                opp_val = getattr(old_value, "aspectualacme_Family15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aspectualacme_Family15"):
                opp_val = getattr(value, "aspectualacme_Family15", None)
                if opp_val is None:
                    setattr(value, "aspectualacme_Family15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aspectualacme_WildCard58(self):
        return self.__aspectualacme_WildCard58

    @aspectualacme_WildCard58.setter
    def aspectualacme_WildCard58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aspectualacme_WildCard__aspectualacme_WildCard58", None)
        self.__aspectualacme_WildCard58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aspectualacme_System"):
                opp_val = getattr(old_value, "aspectualacme_System", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aspectualacme_System"):
                opp_val = getattr(value, "aspectualacme_System", None)
                if opp_val is None:
                    setattr(value, "aspectualacme_System", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class aspectualacme_Attachment:

    pass
class BasicElement:

    pass
class aspectualacme_System(BasicElement):

    pass
class aspectualacme_RoleType(TypeDefinition):

    pass
class aspectualacme_ConnectorType(TypeDefinition):

    pass
class aspectualacme_PortType(TypeDefinition):

    pass
class aspectualacme_ComponentType(TypeDefinition):

    pass
class aspectualacme_Representation:

    def __init__(self, name: str, Representation: "aspectualacme_Element" = None, Representation63: "aspectualacme_System" = None, parentRepresentation: "aspectualacme_System" = None, representation: set["aspectualacme_Binding"] = None, representations: "aspectualacme_Element" = None, Representation149: "aspectualacme_Binding" = None):
        self.name = name
        self.Representation = Representation
        self.Representation63 = Representation63
        self.parentRepresentation = parentRepresentation
        self.representation = representation if representation is not None else set()
        self.representations = representations
        self.Representation149 = Representation149
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Representation149(self):
        return self.__Representation149

    @Representation149.setter
    def Representation149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aspectualacme_Representation__Representation149", None)
        self.__Representation149 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bindings"):
                opp_val = getattr(old_value, "bindings", None)
                if opp_val == self:
                    setattr(old_value, "bindings", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bindings"):
                opp_val = getattr(value, "bindings", None)
                setattr(value, "bindings", self)

    @property
    def representations(self):
        return self.__representations

    @representations.setter
    def representations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aspectualacme_Representation__representations", None)
        self.__representations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Element"):
                opp_val = getattr(old_value, "Element", None)
                if opp_val == self:
                    setattr(old_value, "Element", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Element"):
                opp_val = getattr(value, "Element", None)
                setattr(value, "Element", self)

    @property
    def Representation63(self):
        return self.__Representation63

    @Representation63.setter
    def Representation63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aspectualacme_Representation__Representation63", None)
        self.__Representation63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "system"):
                opp_val = getattr(old_value, "system", None)
                if opp_val == self:
                    setattr(old_value, "system", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "system"):
                opp_val = getattr(value, "system", None)
                setattr(value, "system", self)

    @property
    def Representation(self):
        return self.__Representation

    @Representation.setter
    def Representation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aspectualacme_Representation__Representation", None)
        self.__Representation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "element"):
                opp_val = getattr(old_value, "element", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "element"):
                opp_val = getattr(value, "element", None)
                if opp_val is None:
                    setattr(value, "element", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def representation(self):
        return self.__representation

    @representation.setter
    def representation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aspectualacme_Representation__representation", None)
        self.__representation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Binding"):
                    opp_val = getattr(item, "Binding", None)
                    
                    if opp_val == self:
                        setattr(item, "Binding", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Binding"):
                    opp_val = getattr(item, "Binding", None)
                    
                    setattr(item, "Binding", self)
                    

    @property
    def parentRepresentation(self):
        return self.__parentRepresentation

    @parentRepresentation.setter
    def parentRepresentation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aspectualacme_Representation__parentRepresentation", None)
        self.__parentRepresentation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "System151"):
                opp_val = getattr(old_value, "System151", None)
                if opp_val == self:
                    setattr(old_value, "System151", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "System151"):
                opp_val = getattr(value, "System151", None)
                setattr(value, "System151", self)

class aspectualacme_Property:

    def __init__(self, name: str, value: str, aspectualacme_Property: "aspectualacme_Element" = None, Property: "aspectualacme_Family" = None, Property53: "aspectualacme_System" = None, aspectualacme_Property118: set["aspectualacme_PropertyType"] = None, properties: "aspectualacme_System" = None, properties122: "aspectualacme_Family" = None, aspectualacme_Property142: "aspectualacme_Binding" = None):
        self.name = name
        self.value = value
        self.aspectualacme_Property = aspectualacme_Property
        self.Property = Property
        self.Property53 = Property53
        self.aspectualacme_Property118 = aspectualacme_Property118 if aspectualacme_Property118 is not None else set()
        self.properties = properties
        self.properties122 = properties122
        self.aspectualacme_Property142 = aspectualacme_Property142
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def properties(self):
        return self.__properties

    @properties.setter
    def properties(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aspectualacme_Property__properties", None)
        self.__properties = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "System120"):
                opp_val = getattr(old_value, "System120", None)
                if opp_val == self:
                    setattr(old_value, "System120", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "System120"):
                opp_val = getattr(value, "System120", None)
                setattr(value, "System120", self)

    @property
    def Property53(self):
        return self.__Property53

    @Property53.setter
    def Property53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aspectualacme_Property__Property53", None)
        self.__Property53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parentSystem52"):
                opp_val = getattr(old_value, "parentSystem52", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parentSystem52"):
                opp_val = getattr(value, "parentSystem52", None)
                if opp_val is None:
                    setattr(value, "parentSystem52", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def properties122(self):
        return self.__properties122

    @properties122.setter
    def properties122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aspectualacme_Property__properties122", None)
        self.__properties122 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Family123"):
                opp_val = getattr(old_value, "Family123", None)
                if opp_val == self:
                    setattr(old_value, "Family123", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Family123"):
                opp_val = getattr(value, "Family123", None)
                setattr(value, "Family123", self)

    @property
    def aspectualacme_Property(self):
        return self.__aspectualacme_Property

    @aspectualacme_Property.setter
    def aspectualacme_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aspectualacme_Property__aspectualacme_Property", None)
        self.__aspectualacme_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aspectualacme_Element"):
                opp_val = getattr(old_value, "aspectualacme_Element", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aspectualacme_Element"):
                opp_val = getattr(value, "aspectualacme_Element", None)
                if opp_val is None:
                    setattr(value, "aspectualacme_Element", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aspectualacme_Property142(self):
        return self.__aspectualacme_Property142

    @aspectualacme_Property142.setter
    def aspectualacme_Property142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aspectualacme_Property__aspectualacme_Property142", None)
        self.__aspectualacme_Property142 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aspectualacme_Binding"):
                opp_val = getattr(old_value, "aspectualacme_Binding", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aspectualacme_Binding"):
                opp_val = getattr(value, "aspectualacme_Binding", None)
                if opp_val is None:
                    setattr(value, "aspectualacme_Binding", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aspectualacme_Property118(self):
        return self.__aspectualacme_Property118

    @aspectualacme_Property118.setter
    def aspectualacme_Property118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aspectualacme_Property__aspectualacme_Property118", None)
        self.__aspectualacme_Property118 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aspectualacme_PropertyType"):
                    opp_val = getattr(item, "aspectualacme_PropertyType", None)
                    
                    if opp_val == self:
                        setattr(item, "aspectualacme_PropertyType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aspectualacme_PropertyType"):
                    opp_val = getattr(item, "aspectualacme_PropertyType", None)
                    
                    setattr(item, "aspectualacme_PropertyType", self)
                    

    @property
    def Property(self):
        return self.__Property

    @Property.setter
    def Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aspectualacme_Property__Property", None)
        self.__Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parentFamily27"):
                opp_val = getattr(old_value, "parentFamily27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parentFamily27"):
                opp_val = getattr(value, "parentFamily27", None)
                if opp_val is None:
                    setattr(value, "parentFamily27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class aspectualacme_Element:

    def __init__(self, name: str, aspectualacme_Element: set["aspectualacme_Property"] = None, element: set["aspectualacme_Representation"] = None, Element: "aspectualacme_Representation" = None):
        self.name = name
        self.aspectualacme_Element = aspectualacme_Element if aspectualacme_Element is not None else set()
        self.element = element if element is not None else set()
        self.Element = Element
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def element(self):
        return self.__element

    @element.setter
    def element(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aspectualacme_Element__element", None)
        self.__element = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Representation"):
                    opp_val = getattr(item, "Representation", None)
                    
                    if opp_val == self:
                        setattr(item, "Representation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Representation"):
                    opp_val = getattr(item, "Representation", None)
                    
                    setattr(item, "Representation", self)
                    

    @property
    def aspectualacme_Element(self):
        return self.__aspectualacme_Element

    @aspectualacme_Element.setter
    def aspectualacme_Element(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aspectualacme_Element__aspectualacme_Element", None)
        self.__aspectualacme_Element = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aspectualacme_Property"):
                    opp_val = getattr(item, "aspectualacme_Property", None)
                    
                    if opp_val == self:
                        setattr(item, "aspectualacme_Property", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aspectualacme_Property"):
                    opp_val = getattr(item, "aspectualacme_Property", None)
                    
                    setattr(item, "aspectualacme_Property", self)
                    

    @property
    def Element(self):
        return self.__Element

    @Element.setter
    def Element(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aspectualacme_Element__Element", None)
        self.__Element = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "representations"):
                opp_val = getattr(old_value, "representations", None)
                if opp_val == self:
                    setattr(old_value, "representations", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "representations"):
                opp_val = getattr(value, "representations", None)
                setattr(value, "representations", self)

class aspectualacme_Family(BasicElement):

    pass
class aspectualacme_Armani:

    def __init__(self, modifiers: str, aspectualacme_Armani: "aspectualacme_BasicElement" = None, aspectualacme_Armani155: "aspectualacme_ArmaniDesignRuleExpression" = None):
        self.modifiers = modifiers
        self.aspectualacme_Armani = aspectualacme_Armani
        self.aspectualacme_Armani155 = aspectualacme_Armani155
        
    @property
    def modifiers(self) -> str:
        return self.__modifiers

    @modifiers.setter
    def modifiers(self, modifiers: str):
        self.__modifiers = modifiers

    @property
    def aspectualacme_Armani155(self):
        return self.__aspectualacme_Armani155

    @aspectualacme_Armani155.setter
    def aspectualacme_Armani155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aspectualacme_Armani__aspectualacme_Armani155", None)
        self.__aspectualacme_Armani155 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aspectualacme_ArmaniDesignRuleExpression"):
                opp_val = getattr(old_value, "aspectualacme_ArmaniDesignRuleExpression", None)
                if opp_val == self:
                    setattr(old_value, "aspectualacme_ArmaniDesignRuleExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aspectualacme_ArmaniDesignRuleExpression"):
                opp_val = getattr(value, "aspectualacme_ArmaniDesignRuleExpression", None)
                setattr(value, "aspectualacme_ArmaniDesignRuleExpression", self)

    @property
    def aspectualacme_Armani(self):
        return self.__aspectualacme_Armani

    @aspectualacme_Armani.setter
    def aspectualacme_Armani(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aspectualacme_Armani__aspectualacme_Armani", None)
        self.__aspectualacme_Armani = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aspectualacme_BasicElement6"):
                opp_val = getattr(old_value, "aspectualacme_BasicElement6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aspectualacme_BasicElement6"):
                opp_val = getattr(value, "aspectualacme_BasicElement6", None)
                if opp_val is None:
                    setattr(value, "aspectualacme_BasicElement6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Element:

    pass
class aspectualacme_Connector(Element):

    pass
class aspectualacme_BindableElement(Element):

    pass
class aspectualacme_Component(Element):

    pass
class aspectualacme_TypeDefinition(Element):

    pass
class aspectualacme_BasicElement(Element):

    pass
class aspectualacme_attachableElement(Element):

    pass
class aspectualacme_Import:

    def __init__(self, fileName: str, aspectualacme_Import: "aspectualacme_Root" = None):
        self.fileName = fileName
        self.aspectualacme_Import = aspectualacme_Import
        
    @property
    def fileName(self) -> str:
        return self.__fileName

    @fileName.setter
    def fileName(self, fileName: str):
        self.__fileName = fileName

    @property
    def aspectualacme_Import(self):
        return self.__aspectualacme_Import

    @aspectualacme_Import.setter
    def aspectualacme_Import(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_aspectualacme_Import__aspectualacme_Import", None)
        self.__aspectualacme_Import = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aspectualacme_Root"):
                opp_val = getattr(old_value, "aspectualacme_Root", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aspectualacme_Root"):
                opp_val = getattr(value, "aspectualacme_Root", None)
                if opp_val is None:
                    setattr(value, "aspectualacme_Root", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class aspectualacme_Root:

    pass