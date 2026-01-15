from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class PrimitiveTypeKind(Enum):
    INTEGER = "INTEGER"
    BOOLEAN = "BOOLEAN"
class FlowKind(Enum):
    IN = "IN"
    OUT = "OUT"
    INOUT = "INOUT"


############################################
# Definition of Classes
############################################

class VariableRef:

    pass
class altarica_NestedQualifiedVariableRef(VariableRef):

    pass
class EventRef:

    pass
class altarica_NestedQualifiedEventRef(EventRef):

    pass
class altarica_EObject:

    pass
class Expression:

    pass
class altarica_And(Expression):

    pass
class altarica_Lower(Expression):

    pass
class altarica_EInteger(Expression):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class altarica_StrictUpper(Expression):

    pass
class altarica_Minus(Expression):

    pass
class altarica_StrictLower(Expression):

    pass
class altarica_Addition(Expression):

    pass
class altarica_Division(Expression):

    pass
class altarica_Upper(Expression):

    pass
class altarica_Or(Expression):

    pass
class altarica_Multiplication(Expression):

    pass
class altarica_Imply(Expression):

    pass
class altarica_NotEqual(Expression):

    pass
class altarica_EString(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class altarica_EBoolean(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class altarica_Equal(Expression):

    pass
class altarica_VariableRef(Expression):

    pass
class altarica_NavigableVariable:

    def __init__(self, name: str, altarica_NavigableVariable: "altarica_EventRef" = None, altarica_NavigableVariable106: "altarica_VariableRef" = None, altarica_NavigableVariable176: "altarica_NestedQualifiedEventRef" = None, altarica_NavigableVariable181: "altarica_NestedQualifiedVariableRef" = None):
        self.name = name
        self.altarica_NavigableVariable = altarica_NavigableVariable
        self.altarica_NavigableVariable106 = altarica_NavigableVariable106
        self.altarica_NavigableVariable176 = altarica_NavigableVariable176
        self.altarica_NavigableVariable181 = altarica_NavigableVariable181
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def altarica_NavigableVariable181(self):
        return self.__altarica_NavigableVariable181

    @altarica_NavigableVariable181.setter
    def altarica_NavigableVariable181(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_altarica_NavigableVariable__altarica_NavigableVariable181", None)
        self.__altarica_NavigableVariable181 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "altarica_NestedQualifiedVariableRef180"):
                opp_val = getattr(old_value, "altarica_NestedQualifiedVariableRef180", None)
                if opp_val == self:
                    setattr(old_value, "altarica_NestedQualifiedVariableRef180", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "altarica_NestedQualifiedVariableRef180"):
                opp_val = getattr(value, "altarica_NestedQualifiedVariableRef180", None)
                setattr(value, "altarica_NestedQualifiedVariableRef180", self)

    @property
    def altarica_NavigableVariable(self):
        return self.__altarica_NavigableVariable

    @altarica_NavigableVariable.setter
    def altarica_NavigableVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_altarica_NavigableVariable__altarica_NavigableVariable", None)
        self.__altarica_NavigableVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "altarica_EventRef104"):
                opp_val = getattr(old_value, "altarica_EventRef104", None)
                if opp_val == self:
                    setattr(old_value, "altarica_EventRef104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "altarica_EventRef104"):
                opp_val = getattr(value, "altarica_EventRef104", None)
                setattr(value, "altarica_EventRef104", self)

    @property
    def altarica_NavigableVariable176(self):
        return self.__altarica_NavigableVariable176

    @altarica_NavigableVariable176.setter
    def altarica_NavigableVariable176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_altarica_NavigableVariable__altarica_NavigableVariable176", None)
        self.__altarica_NavigableVariable176 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "altarica_NestedQualifiedEventRef175"):
                opp_val = getattr(old_value, "altarica_NestedQualifiedEventRef175", None)
                if opp_val == self:
                    setattr(old_value, "altarica_NestedQualifiedEventRef175", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "altarica_NestedQualifiedEventRef175"):
                opp_val = getattr(value, "altarica_NestedQualifiedEventRef175", None)
                setattr(value, "altarica_NestedQualifiedEventRef175", self)

    @property
    def altarica_NavigableVariable106(self):
        return self.__altarica_NavigableVariable106

    @altarica_NavigableVariable106.setter
    def altarica_NavigableVariable106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_altarica_NavigableVariable__altarica_NavigableVariable106", None)
        self.__altarica_NavigableVariable106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "altarica_VariableRef"):
                opp_val = getattr(old_value, "altarica_VariableRef", None)
                if opp_val == self:
                    setattr(old_value, "altarica_VariableRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "altarica_VariableRef"):
                opp_val = getattr(value, "altarica_VariableRef", None)
                setattr(value, "altarica_VariableRef", self)

class altarica_CaseExpression:

    pass
class AbstractBooleanExpression:

    pass
class AbstractExpression:

    pass
class altarica_IfThenElse(AbstractExpression, AbstractBooleanExpression):

    pass
class altarica_Switch(AbstractExpression, AbstractBooleanExpression):

    pass
class altarica_EventRef:

    pass
class altarica_Cardinality:

    pass
class altarica_Transition:

    pass
class altarica_VectorParameter:

    def __init__(self, isRequired: bool, altarica_VectorParameter: "altarica_Vector" = None, altarica_VectorParameter63: "altarica_EventRef" = None):
        self.isRequired = isRequired
        self.altarica_VectorParameter = altarica_VectorParameter
        self.altarica_VectorParameter63 = altarica_VectorParameter63
        
    @property
    def isRequired(self) -> bool:
        return self.__isRequired

    @isRequired.setter
    def isRequired(self, isRequired: bool):
        self.__isRequired = isRequired

    @property
    def altarica_VectorParameter(self):
        return self.__altarica_VectorParameter

    @altarica_VectorParameter.setter
    def altarica_VectorParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_altarica_VectorParameter__altarica_VectorParameter", None)
        self.__altarica_VectorParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "altarica_Vector59"):
                opp_val = getattr(old_value, "altarica_Vector59", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "altarica_Vector59"):
                opp_val = getattr(value, "altarica_Vector59", None)
                if opp_val is None:
                    setattr(value, "altarica_Vector59", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def altarica_VectorParameter63(self):
        return self.__altarica_VectorParameter63

    @altarica_VectorParameter63.setter
    def altarica_VectorParameter63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_altarica_VectorParameter__altarica_VectorParameter63", None)
        self.__altarica_VectorParameter63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "altarica_EventRef"):
                opp_val = getattr(old_value, "altarica_EventRef", None)
                if opp_val == self:
                    setattr(old_value, "altarica_EventRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "altarica_EventRef"):
                opp_val = getattr(value, "altarica_EventRef", None)
                setattr(value, "altarica_EventRef", self)

class altarica_Vector:

    pass
class altarica_AbstractBooleanExpression:

    pass
class altarica_Assert:

    pass
class altarica_NodeInstanceDeclaration:

    pass
class altarica_EventDeclaration:

    pass
class altarica_StateDeclaration:

    pass
class altarica_AbstractExpression:

    pass
class altarica_Priority:

    pass
class NavigableVariable:

    pass
class altarica_Event(NavigableVariable):

    pass
class altarica_NodeInstance(NavigableVariable):

    pass
class altarica_NonNavigableVariable(NavigableVariable):

    pass
class altarica_FlowDeclaration:

    def __init__(self, kind: str, altarica_FlowDeclaration22: set["altarica_Flow"] = None, altarica_FlowDeclaration24: "altarica_AbstractTypeRef" = None, altarica_FlowDeclaration26: "altarica_VariableAttribute" = None, altarica_FlowDeclaration: "altarica_FlowSpecification" = None):
        self.kind = kind
        self.altarica_FlowDeclaration22 = altarica_FlowDeclaration22 if altarica_FlowDeclaration22 is not None else set()
        self.altarica_FlowDeclaration24 = altarica_FlowDeclaration24
        self.altarica_FlowDeclaration26 = altarica_FlowDeclaration26
        self.altarica_FlowDeclaration = altarica_FlowDeclaration
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def altarica_FlowDeclaration22(self):
        return self.__altarica_FlowDeclaration22

    @altarica_FlowDeclaration22.setter
    def altarica_FlowDeclaration22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_altarica_FlowDeclaration__altarica_FlowDeclaration22", None)
        self.__altarica_FlowDeclaration22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "altarica_Flow"):
                    opp_val = getattr(item, "altarica_Flow", None)
                    
                    if opp_val == self:
                        setattr(item, "altarica_Flow", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "altarica_Flow"):
                    opp_val = getattr(item, "altarica_Flow", None)
                    
                    setattr(item, "altarica_Flow", self)
                    

    @property
    def altarica_FlowDeclaration(self):
        return self.__altarica_FlowDeclaration

    @altarica_FlowDeclaration.setter
    def altarica_FlowDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_altarica_FlowDeclaration__altarica_FlowDeclaration", None)
        self.__altarica_FlowDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "altarica_FlowSpecification"):
                opp_val = getattr(old_value, "altarica_FlowSpecification", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "altarica_FlowSpecification"):
                opp_val = getattr(value, "altarica_FlowSpecification", None)
                if opp_val is None:
                    setattr(value, "altarica_FlowSpecification", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def altarica_FlowDeclaration24(self):
        return self.__altarica_FlowDeclaration24

    @altarica_FlowDeclaration24.setter
    def altarica_FlowDeclaration24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_altarica_FlowDeclaration__altarica_FlowDeclaration24", None)
        self.__altarica_FlowDeclaration24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "altarica_AbstractTypeRef"):
                opp_val = getattr(old_value, "altarica_AbstractTypeRef", None)
                if opp_val == self:
                    setattr(old_value, "altarica_AbstractTypeRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "altarica_AbstractTypeRef"):
                opp_val = getattr(value, "altarica_AbstractTypeRef", None)
                setattr(value, "altarica_AbstractTypeRef", self)

    @property
    def altarica_FlowDeclaration26(self):
        return self.__altarica_FlowDeclaration26

    @altarica_FlowDeclaration26.setter
    def altarica_FlowDeclaration26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_altarica_FlowDeclaration__altarica_FlowDeclaration26", None)
        self.__altarica_FlowDeclaration26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "altarica_VariableAttribute"):
                opp_val = getattr(old_value, "altarica_VariableAttribute", None)
                if opp_val == self:
                    setattr(old_value, "altarica_VariableAttribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "altarica_VariableAttribute"):
                opp_val = getattr(value, "altarica_VariableAttribute", None)
                setattr(value, "altarica_VariableAttribute", self)

class altarica_AbstractTypeRef:

    pass
class altarica_AbstractSpecification:

    pass
class altarica_ExternalDirective:

    def __init__(self, directive: str, altarica_ExternalDirective: "altarica_ExternalSpecification" = None):
        self.directive = directive
        self.altarica_ExternalDirective = altarica_ExternalDirective
        
    @property
    def directive(self) -> str:
        return self.__directive

    @directive.setter
    def directive(self, directive: str):
        self.__directive = directive

    @property
    def altarica_ExternalDirective(self):
        return self.__altarica_ExternalDirective

    @altarica_ExternalDirective.setter
    def altarica_ExternalDirective(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_altarica_ExternalDirective__altarica_ExternalDirective", None)
        self.__altarica_ExternalDirective = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "altarica_ExternalSpecification"):
                opp_val = getattr(old_value, "altarica_ExternalSpecification", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "altarica_ExternalSpecification"):
                opp_val = getattr(value, "altarica_ExternalSpecification", None)
                if opp_val is None:
                    setattr(value, "altarica_ExternalSpecification", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class altarica_Affectation:

    pass
class altarica_InitStatement:

    pass
class AbstractSpecification:

    pass
class altarica_EventSpecification(AbstractSpecification):

    pass
class altarica_ExternalSpecification(AbstractSpecification):

    pass
class altarica_FlowSpecification(AbstractSpecification):

    pass
class altarica_AssertSpecification(AbstractSpecification):

    pass
class altarica_StateSpecification(AbstractSpecification):

    pass
class altarica_VectorSpecification(AbstractSpecification):

    pass
class altarica_TransitionSpecification(AbstractSpecification):

    pass
class altarica_NodeInstanceSpecification(AbstractSpecification):

    pass
class altarica_InitSpecification(AbstractSpecification):

    pass
class altarica_VariableAttribute:

    def __init__(self, name: str, altarica_VariableAttribute: "altarica_FlowDeclaration" = None, altarica_VariableAttribute32: "altarica_EventDeclaration" = None, altarica_VariableAttribute45: "altarica_StateDeclaration" = None):
        self.name = name
        self.altarica_VariableAttribute = altarica_VariableAttribute
        self.altarica_VariableAttribute32 = altarica_VariableAttribute32
        self.altarica_VariableAttribute45 = altarica_VariableAttribute45
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def altarica_VariableAttribute32(self):
        return self.__altarica_VariableAttribute32

    @altarica_VariableAttribute32.setter
    def altarica_VariableAttribute32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_altarica_VariableAttribute__altarica_VariableAttribute32", None)
        self.__altarica_VariableAttribute32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "altarica_EventDeclaration31"):
                opp_val = getattr(old_value, "altarica_EventDeclaration31", None)
                if opp_val == self:
                    setattr(old_value, "altarica_EventDeclaration31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "altarica_EventDeclaration31"):
                opp_val = getattr(value, "altarica_EventDeclaration31", None)
                setattr(value, "altarica_EventDeclaration31", self)

    @property
    def altarica_VariableAttribute(self):
        return self.__altarica_VariableAttribute

    @altarica_VariableAttribute.setter
    def altarica_VariableAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_altarica_VariableAttribute__altarica_VariableAttribute", None)
        self.__altarica_VariableAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "altarica_FlowDeclaration26"):
                opp_val = getattr(old_value, "altarica_FlowDeclaration26", None)
                if opp_val == self:
                    setattr(old_value, "altarica_FlowDeclaration26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "altarica_FlowDeclaration26"):
                opp_val = getattr(value, "altarica_FlowDeclaration26", None)
                setattr(value, "altarica_FlowDeclaration26", self)

    @property
    def altarica_VariableAttribute45(self):
        return self.__altarica_VariableAttribute45

    @altarica_VariableAttribute45.setter
    def altarica_VariableAttribute45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_altarica_VariableAttribute__altarica_VariableAttribute45", None)
        self.__altarica_VariableAttribute45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "altarica_StateDeclaration44"):
                opp_val = getattr(old_value, "altarica_StateDeclaration44", None)
                if opp_val == self:
                    setattr(old_value, "altarica_StateDeclaration44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "altarica_StateDeclaration44"):
                opp_val = getattr(value, "altarica_StateDeclaration44", None)
                setattr(value, "altarica_StateDeclaration44", self)

class AbstractDefinitionConstant:

    pass
class altarica_ExpressionConstant(AbstractDefinitionConstant):

    pass
class altarica_Expression(AbstractExpression, AbstractBooleanExpression):

    pass
class NonNavigableVariable:

    pass
class altarica_Flow(NonNavigableVariable):

    pass
class altarica_Literal(NonNavigableVariable):

    pass
class altarica_State(NonNavigableVariable):

    pass
class AbstractDomain:

    pass
class altarica_Enumeration(AbstractDomain):

    pass
class altarica_PrimitiveType(AbstractDomain):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class altarica_Range(AbstractDomain):

    pass
class AbstractTypeRef:

    pass
class altarica_DomainRef(AbstractTypeRef):

    pass
class altarica_AbstractDomain(AbstractTypeRef):

    pass
class altarica_DomainConstant(AbstractDefinitionConstant):

    pass
class altarica_AbstractDefinitionConstant:

    pass
class altarica_Constant(NonNavigableVariable):

    pass
class AbstractDeclaration:

    pass
class altarica_Domain(AbstractDeclaration):

    def __init__(self, name: str, altarica_Domain: "altarica_AbstractDomain" = None, altarica_Domain47: "altarica_DomainRef" = None):
        self.name = name
        self.altarica_Domain = altarica_Domain
        self.altarica_Domain47 = altarica_Domain47
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def altarica_Domain47(self):
        return self.__altarica_Domain47

    @altarica_Domain47.setter
    def altarica_Domain47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_altarica_Domain__altarica_Domain47", None)
        self.__altarica_Domain47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "altarica_DomainRef"):
                opp_val = getattr(old_value, "altarica_DomainRef", None)
                if opp_val == self:
                    setattr(old_value, "altarica_DomainRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "altarica_DomainRef"):
                opp_val = getattr(value, "altarica_DomainRef", None)
                setattr(value, "altarica_DomainRef", self)

    @property
    def altarica_Domain(self):
        return self.__altarica_Domain

    @altarica_Domain.setter
    def altarica_Domain(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_altarica_Domain__altarica_Domain", None)
        self.__altarica_Domain = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "altarica_AbstractDomain8"):
                opp_val = getattr(old_value, "altarica_AbstractDomain8", None)
                if opp_val == self:
                    setattr(old_value, "altarica_AbstractDomain8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "altarica_AbstractDomain8"):
                opp_val = getattr(value, "altarica_AbstractDomain8", None)
                setattr(value, "altarica_AbstractDomain8", self)

class altarica_Node(AbstractDeclaration):

    def __init__(self, isMain: bool, name: str, altarica_Node: set["altarica_AbstractSpecification"] = None, altarica_Node53: "altarica_NodeInstanceDeclaration" = None):
        self.isMain = isMain
        self.name = name
        self.altarica_Node = altarica_Node if altarica_Node is not None else set()
        self.altarica_Node53 = altarica_Node53
        
    @property
    def isMain(self) -> bool:
        return self.__isMain

    @isMain.setter
    def isMain(self, isMain: bool):
        self.__isMain = isMain

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def altarica_Node53(self):
        return self.__altarica_Node53

    @altarica_Node53.setter
    def altarica_Node53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_altarica_Node__altarica_Node53", None)
        self.__altarica_Node53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "altarica_NodeInstanceDeclaration52"):
                opp_val = getattr(old_value, "altarica_NodeInstanceDeclaration52", None)
                if opp_val == self:
                    setattr(old_value, "altarica_NodeInstanceDeclaration52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "altarica_NodeInstanceDeclaration52"):
                opp_val = getattr(value, "altarica_NodeInstanceDeclaration52", None)
                setattr(value, "altarica_NodeInstanceDeclaration52", self)

    @property
    def altarica_Node(self):
        return self.__altarica_Node

    @altarica_Node.setter
    def altarica_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_altarica_Node__altarica_Node", None)
        self.__altarica_Node = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "altarica_AbstractSpecification"):
                    opp_val = getattr(item, "altarica_AbstractSpecification", None)
                    
                    if opp_val == self:
                        setattr(item, "altarica_AbstractSpecification", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "altarica_AbstractSpecification"):
                    opp_val = getattr(item, "altarica_AbstractSpecification", None)
                    
                    setattr(item, "altarica_AbstractSpecification", self)
                    

class altarica_ConstantDefinition(AbstractDeclaration):

    pass
class altarica_AbstractDeclaration:

    pass
class altarica_System:

    pass