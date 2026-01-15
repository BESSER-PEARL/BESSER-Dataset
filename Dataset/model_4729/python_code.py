from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class AggregateExpression:

    pass
class logiclanguage_ProjectedAggregateExpression(AggregateExpression):

    def __init__(self, projectionIndex: int):
        self.projectionIndex = projectionIndex
        
    @property
    def projectionIndex(self) -> int:
        return self.__projectionIndex

    @projectionIndex.setter
    def projectionIndex(self, projectionIndex: int):
        self.__projectionIndex = projectionIndex

class logiclanguage_Count(AggregateExpression):

    pass
class ProjectedAggregateExpression:

    pass
class logiclanguage_Max(ProjectedAggregateExpression):

    pass
class logiclanguage_Min(ProjectedAggregateExpression):

    pass
class logiclanguage_Sum(ProjectedAggregateExpression):

    pass
class logiclanguage_AggregatedParameterSubstitution:

    pass
class Function:

    pass
class logiclanguage_FunctionDefinition(Function):

    pass
class Relation:

    pass
class logiclanguage_RelationDeclaration(Relation):

    pass
class logiclanguage_RelationDefinition(Relation):

    pass
class Constant:

    pass
class logiclanguage_ConstantDeclaration(Constant):

    pass
class logiclanguage_ConstantDefinition(Constant):

    pass
class logiclanguage_ConstantAnnotation:

    pass
class logiclanguage_FunctionDeclaration(Function):

    pass
class NumericOperation:

    pass
class logiclanguage_Mod(NumericOperation):

    pass
class logiclanguage_Minus(NumericOperation):

    pass
class logiclanguage_Pow(NumericOperation):

    pass
class logiclanguage_Divison(NumericOperation):

    pass
class logiclanguage_Multiply(NumericOperation):

    pass
class logiclanguage_Plus(NumericOperation):

    pass
class logiclanguage_RelationAnnotation:

    pass
class logiclanguage_AssertionAnnotation:

    pass
class logiclanguage_Assertion:

    def __init__(self, name: str, logiclanguage_Assertion: "logiclanguage_Term" = None, target75: set["logiclanguage_AssertionAnnotation"] = None):
        self.name = name
        self.logiclanguage_Assertion = logiclanguage_Assertion
        self.target75 = target75 if target75 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def logiclanguage_Assertion(self):
        return self.__logiclanguage_Assertion

    @logiclanguage_Assertion.setter
    def logiclanguage_Assertion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_logiclanguage_Assertion__logiclanguage_Assertion", None)
        self.__logiclanguage_Assertion = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "logiclanguage_Term73"):
                opp_val = getattr(old_value, "logiclanguage_Term73", None)
                if opp_val == self:
                    setattr(old_value, "logiclanguage_Term73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "logiclanguage_Term73"):
                opp_val = getattr(value, "logiclanguage_Term73", None)
                setattr(value, "logiclanguage_Term73", self)

    @property
    def target75(self):
        return self.__target75

    @target75.setter
    def target75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_logiclanguage_Assertion__target75", None)
        self.__target75 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "logicproblem.ecoreAssertionAnnotation"):
                    opp_val = getattr(item, "logicproblem.ecoreAssertionAnnotation", None)
                    
                    if opp_val == self:
                        setattr(item, "logicproblem.ecoreAssertionAnnotation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "logicproblem.ecoreAssertionAnnotation"):
                    opp_val = getattr(item, "logicproblem.ecoreAssertionAnnotation", None)
                    
                    setattr(item, "logicproblem.ecoreAssertionAnnotation", self)
                    

class logiclanguage_TermDescription(ABC):

    pass
class logiclanguage_TypeDescriptor(ABC):

    pass
class PrimitiveRelation:

    pass
class logiclanguage_LessThan(PrimitiveRelation):

    pass
class logiclanguage_LessOrEqualThan(PrimitiveRelation):

    pass
class logiclanguage_MoreThan(PrimitiveRelation):

    pass
class logiclanguage_MoreOrEqualThan(PrimitiveRelation):

    pass
class logiclanguage_Distinct(PrimitiveRelation):

    pass
class logiclanguage_Equals(PrimitiveRelation):

    pass
class BoolOperation:

    pass
class logiclanguage_Iff(BoolOperation):

    pass
class logiclanguage_Not(BoolOperation):

    pass
class logiclanguage_Impl(BoolOperation):

    pass
class logiclanguage_Or(BoolOperation):

    pass
class logiclanguage_And(BoolOperation):

    pass
class QuantifiedExpression:

    pass
class logiclanguage_Forall(QuantifiedExpression):

    pass
class logiclanguage_Exists(QuantifiedExpression):

    pass
class AtomicTerm:

    pass
class logiclanguage_RealLiteral(AtomicTerm):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class logiclanguage_BoolLiteral(AtomicTerm):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class logiclanguage_StringLiteral(AtomicTerm):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class logiclanguage_IntLiteral(AtomicTerm):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class Term:

    pass
class logiclanguage_InstanceOf(Term):

    pass
class logiclanguage_TransitiveClosure(Term):

    pass
class logiclanguage_AggregateExpression(Term):

    pass
class logiclanguage_QuantifiedExpression(Term):

    pass
class logiclanguage_IfThenElse(Term):

    pass
class logiclanguage_AtomicTerm(Term):

    pass
class logiclanguage_NumericOperation(Term):

    pass
class logiclanguage_UnknownBecauseUninterpreted(Term):

    pass
class logiclanguage_PrimitiveRelation(Term):

    pass
class logiclanguage_BoolOperation(Term):

    pass
class logiclanguage_SymbolicValue(Term):

    pass
class TermDescription:

    pass
class logiclanguage_SymbolicDeclaration(TermDescription):

    def __init__(self, name: str, logiclanguage_SymbolicDeclaration: "logiclanguage_SymbolicValue" = None):
        self.name = name
        self.logiclanguage_SymbolicDeclaration = logiclanguage_SymbolicDeclaration
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def logiclanguage_SymbolicDeclaration(self):
        return self.__logiclanguage_SymbolicDeclaration

    @logiclanguage_SymbolicDeclaration.setter
    def logiclanguage_SymbolicDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_logiclanguage_SymbolicDeclaration__logiclanguage_SymbolicDeclaration", None)
        self.__logiclanguage_SymbolicDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "logiclanguage_SymbolicValue"):
                opp_val = getattr(old_value, "logiclanguage_SymbolicValue", None)
                if opp_val == self:
                    setattr(old_value, "logiclanguage_SymbolicValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "logiclanguage_SymbolicValue"):
                opp_val = getattr(value, "logiclanguage_SymbolicValue", None)
                setattr(value, "logiclanguage_SymbolicValue", self)

class logiclanguage_Term(TermDescription):

    pass
class logiclanguage_FunctionAnnotation:

    pass
class PrimitiveTypeReference:

    pass
class logiclanguage_BoolTypeReference(PrimitiveTypeReference):

    pass
class logiclanguage_StringTypeReference(PrimitiveTypeReference):

    pass
class logiclanguage_RealTypeReference(PrimitiveTypeReference):

    pass
class logiclanguage_IntTypeReference(PrimitiveTypeReference):

    pass
class TypeReference:

    pass
class logiclanguage_PrimitiveTypeReference(TypeReference):

    pass
class logiclanguage_ComplexTypeReference(TypeReference):

    pass
class Type:

    pass
class logiclanguage_TypeDeclaration(Type):

    pass
class logiclanguage_TypeDefinition(Type):

    pass
class SymbolicDeclaration:

    pass
class logiclanguage_Variable(SymbolicDeclaration):

    pass
class logiclanguage_Constant(SymbolicDeclaration):

    pass
class logiclanguage_Relation(SymbolicDeclaration):

    pass
class logiclanguage_Function(SymbolicDeclaration):

    pass
class logiclanguage_DefinedElement(SymbolicDeclaration):

    pass
class TypeDescriptor:

    pass
class logiclanguage_TypeReference(TypeDescriptor):

    pass
class logiclanguage_Type(TypeDescriptor):

    def __init__(self, name: str, isAbstract: bool, Type: "logiclanguage_Type" = None, supertypes: set["logiclanguage_Type"] = None, Type4: "logiclanguage_Type" = None, subtypes: set["logiclanguage_Type"] = None, logiclanguage_Type: "logiclanguage_ComplexTypeReference" = None):
        self.name = name
        self.isAbstract = isAbstract
        self.Type = Type
        self.supertypes = supertypes if supertypes is not None else set()
        self.Type4 = Type4
        self.subtypes = subtypes if subtypes is not None else set()
        self.logiclanguage_Type = logiclanguage_Type
        
    @property
    def isAbstract(self) -> bool:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def supertypes(self):
        return self.__supertypes

    @supertypes.setter
    def supertypes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_logiclanguage_Type__supertypes", None)
        self.__supertypes = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Type"):
                    opp_val = getattr(item, "Type", None)
                    
                    if opp_val == self:
                        setattr(item, "Type", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Type"):
                    opp_val = getattr(item, "Type", None)
                    
                    setattr(item, "Type", self)
                    

    @property
    def logiclanguage_Type(self):
        return self.__logiclanguage_Type

    @logiclanguage_Type.setter
    def logiclanguage_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_logiclanguage_Type__logiclanguage_Type", None)
        self.__logiclanguage_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "logiclanguage_ComplexTypeReference"):
                opp_val = getattr(old_value, "logiclanguage_ComplexTypeReference", None)
                if opp_val == self:
                    setattr(old_value, "logiclanguage_ComplexTypeReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "logiclanguage_ComplexTypeReference"):
                opp_val = getattr(value, "logiclanguage_ComplexTypeReference", None)
                setattr(value, "logiclanguage_ComplexTypeReference", self)

    @property
    def subtypes(self):
        return self.__subtypes

    @subtypes.setter
    def subtypes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_logiclanguage_Type__subtypes", None)
        self.__subtypes = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Type4"):
                    opp_val = getattr(item, "Type4", None)
                    
                    if opp_val == self:
                        setattr(item, "Type4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Type4"):
                    opp_val = getattr(item, "Type4", None)
                    
                    setattr(item, "Type4", self)
                    

    @property
    def Type(self):
        return self.__Type

    @Type.setter
    def Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_logiclanguage_Type__Type", None)
        self.__Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "supertypes"):
                opp_val = getattr(old_value, "supertypes", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "supertypes"):
                opp_val = getattr(value, "supertypes", None)
                if opp_val is None:
                    setattr(value, "supertypes", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Type4(self):
        return self.__Type4

    @Type4.setter
    def Type4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_logiclanguage_Type__Type4", None)
        self.__Type4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "subtypes"):
                opp_val = getattr(old_value, "subtypes", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "subtypes"):
                opp_val = getattr(value, "subtypes", None)
                if opp_val is None:
                    setattr(value, "subtypes", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
