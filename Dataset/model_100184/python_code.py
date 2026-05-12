from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class sparqlas_TemplateBinding:

    pass
class sparqlas_TemplateableElement(ABC):

    pass
class sparqlas_TemplateParameterSubstitution:

    pass
class sparqlas_TemplateSignature:

    pass
class sparqlas_TemplateParameter:

    pass
class sparqlas_ParameterableElement(ABC):

    pass
class Declaration:

    pass
class sparqlas_ObjectPropertyDeclaration(Declaration):

    pass
class sparqlas_DatatypePropertyDeclaration(Declaration):

    pass
class sparqlas_ClassDeclaration(Declaration):

    pass
class sparqlas_IndividualDeclaration(Declaration):

    pass
class DataPropertyAtom:

    pass
class sparqlas_EquivalentDataProperties(DataPropertyAtom):

    pass
class sparqlas_DataPropertyDomain(DataPropertyAtom):

    pass
class sparqlas_FunctionalDataProperty(DataPropertyAtom):

    pass
class sparqlas_DataPropertyRange(DataPropertyAtom):

    pass
class sparqlas_DisjointDataProperties(DataPropertyAtom):

    pass
class sparqlas_SubDataPropertyOf(DataPropertyAtom):

    pass
class sparqlas_ObjectPropertyChain:

    pass
class ObjectPropertyAtom:

    pass
class sparqlas_InverseFunctionalObjectProperty(ObjectPropertyAtom):

    pass
class sparqlas_AsymmetricObjectProperty(ObjectPropertyAtom):

    pass
class sparqlas_SymmetricObjectProperty(ObjectPropertyAtom):

    pass
class sparqlas_FunctionalObjectProperty(ObjectPropertyAtom):

    pass
class sparqlas_EquivalentObjectProperties(ObjectPropertyAtom):

    pass
class sparqlas_IrreflexiveObjectProperty(ObjectPropertyAtom):

    pass
class sparqlas_ReflexiveObjectProperty(ObjectPropertyAtom):

    pass
class sparqlas_TransitiveObjectProperty(ObjectPropertyAtom):

    pass
class sparqlas_ObjectPropertyRange(ObjectPropertyAtom):

    pass
class sparqlas_InverseObjectPropertyAtom(ObjectPropertyAtom):

    pass
class sparqlas_ObjectPropertyDomain(ObjectPropertyAtom):

    pass
class sparqlas_DisjointObjectProperties(ObjectPropertyAtom):

    pass
class sparqlas_FacetRestriction:

    pass
class sparqlas_SubObjectPropertyOf(ObjectPropertyAtom):

    pass
class sparqlas_DataRange(ABC):

    pass
class Expression:

    pass
class ClassAtom:

    pass
class sparqlas_StrictSubClassOf(ClassAtom):

    pass
class sparqlas_DirectSubClassOf(ClassAtom):

    pass
class sparqlas_EquivalentClasses(ClassAtom):

    pass
class sparqlas_DisjointUnion(ClassAtom):

    pass
class sparqlas_SubClassOf(ClassAtom):

    pass
class sparqlas_DisjointClasses(ClassAtom):

    pass
class sparqlas_DataPropertyExpression(Expression):

    pass
class sparqlas_ClassExpression(Expression):

    pass
class Assertion:

    pass
class sparqlas_SameIndividual(Assertion):

    pass
class sparqlas_NegativeDataPropertyAssertion(Assertion):

    pass
class sparqlas_DifferentIndividuals(Assertion):

    pass
class sparqlas_DataPropertyAssertion(Assertion):

    pass
class sparqlas_NegativeObjectPropertyAssertion(Assertion):

    pass
class sparqlas_DirectClassAssertion(Assertion):

    pass
class sparqlas_ClassAssertion(Assertion):

    pass
class Atom:

    pass
class sparqlas_ClassAtom(Atom):

    pass
class sparqlas_HasKey(Atom):

    pass
class sparqlas_DataPropertyAtom(Atom):

    pass
class sparqlas_ObjectPropertyAtom(Atom):

    pass
class sparqlas_Declaration(Atom):

    pass
class sparqlas_Assertion(Atom):

    pass
class ParameterableElement:

    pass
class sparqlas_Expression(ParameterableElement):

    pass
class AbstractLiteral:

    pass
class sparqlas_Literal(AbstractLiteral):

    def __init__(self, lexicalForm: str, sparqlas_Literal: "sparqlas_Datatype" = None):
        self.lexicalForm = lexicalForm
        self.sparqlas_Literal = sparqlas_Literal
        
        pass
    @property
    def lexicalForm(self):
        return self.__lexicalForm

    @lexicalForm.setter
    def lexicalForm(self, lexicalForm: str):
        self.__lexicalForm = lexicalForm


    @property
    def sparqlas_Literal(self):
        return self.__sparqlas_Literal

    @sparqlas_Literal.setter
    def sparqlas_Literal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparqlas_Literal__sparqlas_Literal", None)
        self.__sparqlas_Literal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparqlas_Datatype"):
                opp_val = getattr(old_value, "sparqlas_Datatype", None)
                if opp_val == self:
                    setattr(old_value, "sparqlas_Datatype", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparqlas_Datatype"):
                opp_val = getattr(value, "sparqlas_Datatype", None)
                setattr(value, "sparqlas_Datatype", self)

class sparqlas_AbstractLiteral(ABC):

    pass
class sparqlas_Individual(ABC):

    pass
class DataRange:

    pass
class sparqlas_DataOneOf(DataRange):

    pass
class sparqlas_DatatypeRestriction(DataRange):

    pass
class sparqlas_DataUnionOf(DataRange):

    pass
class sparqlas_DataIntersectionOf(DataRange):

    pass
class sparqlas_DataComplementOf(DataRange):

    pass
class Constant:

    pass
class sparqlas_Datatype(Constant, DataRange):

    pass
class sparqlas_ObjectPropertyExpression(Expression):

    pass
class sparqlas_ObjectPropertyAssertion(Assertion):

    pass
class DataPropertyExpression:

    pass
class sparqlas_DataProperty(Constant, DataPropertyExpression):

    pass
class ObjectPropertyExpression:

    pass
class sparqlas_InverseObjectProperty(ObjectPropertyExpression):

    pass
class sparqlas_ObjectProperty(Constant, ObjectPropertyExpression):

    pass
class ClassExpression:

    pass
class sparqlas_ObjectHasValue(ClassExpression):

    pass
class sparqlas_ObjectComplementOf(ClassExpression):

    pass
class sparqlas_DataHasValue(ClassExpression):

    pass
class sparqlas_DataMaxCardinality(ClassExpression):

    def __init__(self, cardinality: int, sparqlas_DataMaxCardinality: "sparqlas_DataRange" = None, sparqlas_DataMaxCardinality141: "sparqlas_DataPropertyExpression" = None):
        self.cardinality = cardinality
        self.sparqlas_DataMaxCardinality = sparqlas_DataMaxCardinality
        self.sparqlas_DataMaxCardinality141 = sparqlas_DataMaxCardinality141
        
        pass
    @property
    def cardinality(self):
        return self.__cardinality

    @cardinality.setter
    def cardinality(self, cardinality: int):
        self.__cardinality = cardinality


    @property
    def sparqlas_DataMaxCardinality141(self):
        return self.__sparqlas_DataMaxCardinality141

    @sparqlas_DataMaxCardinality141.setter
    def sparqlas_DataMaxCardinality141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparqlas_DataMaxCardinality__sparqlas_DataMaxCardinality141", None)
        self.__sparqlas_DataMaxCardinality141 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparqlas_DataPropertyExpression142"):
                opp_val = getattr(old_value, "sparqlas_DataPropertyExpression142", None)
                if opp_val == self:
                    setattr(old_value, "sparqlas_DataPropertyExpression142", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparqlas_DataPropertyExpression142"):
                opp_val = getattr(value, "sparqlas_DataPropertyExpression142", None)
                setattr(value, "sparqlas_DataPropertyExpression142", self)

    @property
    def sparqlas_DataMaxCardinality(self):
        return self.__sparqlas_DataMaxCardinality

    @sparqlas_DataMaxCardinality.setter
    def sparqlas_DataMaxCardinality(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparqlas_DataMaxCardinality__sparqlas_DataMaxCardinality", None)
        self.__sparqlas_DataMaxCardinality = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparqlas_DataRange139"):
                opp_val = getattr(old_value, "sparqlas_DataRange139", None)
                if opp_val == self:
                    setattr(old_value, "sparqlas_DataRange139", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparqlas_DataRange139"):
                opp_val = getattr(value, "sparqlas_DataRange139", None)
                setattr(value, "sparqlas_DataRange139", self)

class sparqlas_ObjectAllValuesFrom(ClassExpression):

    pass
class sparqlas_ObjectIntersectionOf(ClassExpression):

    pass
class sparqlas_ObjectUnionOf(ClassExpression):

    pass
class sparqlas_DataMinCardinality(ClassExpression):

    def __init__(self, cardinality: int, sparqlas_DataMinCardinality136: "sparqlas_DataPropertyExpression" = None, sparqlas_DataMinCardinality: "sparqlas_DataRange" = None):
        self.cardinality = cardinality
        self.sparqlas_DataMinCardinality136 = sparqlas_DataMinCardinality136
        self.sparqlas_DataMinCardinality = sparqlas_DataMinCardinality
        
        pass
    @property
    def cardinality(self):
        return self.__cardinality

    @cardinality.setter
    def cardinality(self, cardinality: int):
        self.__cardinality = cardinality


    @property
    def sparqlas_DataMinCardinality(self):
        return self.__sparqlas_DataMinCardinality

    @sparqlas_DataMinCardinality.setter
    def sparqlas_DataMinCardinality(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparqlas_DataMinCardinality__sparqlas_DataMinCardinality", None)
        self.__sparqlas_DataMinCardinality = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparqlas_DataRange134"):
                opp_val = getattr(old_value, "sparqlas_DataRange134", None)
                if opp_val == self:
                    setattr(old_value, "sparqlas_DataRange134", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparqlas_DataRange134"):
                opp_val = getattr(value, "sparqlas_DataRange134", None)
                setattr(value, "sparqlas_DataRange134", self)

    @property
    def sparqlas_DataMinCardinality136(self):
        return self.__sparqlas_DataMinCardinality136

    @sparqlas_DataMinCardinality136.setter
    def sparqlas_DataMinCardinality136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparqlas_DataMinCardinality__sparqlas_DataMinCardinality136", None)
        self.__sparqlas_DataMinCardinality136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparqlas_DataPropertyExpression137"):
                opp_val = getattr(old_value, "sparqlas_DataPropertyExpression137", None)
                if opp_val == self:
                    setattr(old_value, "sparqlas_DataPropertyExpression137", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparqlas_DataPropertyExpression137"):
                opp_val = getattr(value, "sparqlas_DataPropertyExpression137", None)
                setattr(value, "sparqlas_DataPropertyExpression137", self)

class sparqlas_DataAllValuesFrom(ClassExpression):

    pass
class sparqlas_DataSomeValuesFrom(ClassExpression):

    pass
class sparqlas_DataExactCardinality(ClassExpression):

    def __init__(self, cardinality: int, sparqlas_DataExactCardinality: "sparqlas_DataRange" = None, sparqlas_DataExactCardinality146: "sparqlas_DataPropertyExpression" = None):
        self.cardinality = cardinality
        self.sparqlas_DataExactCardinality = sparqlas_DataExactCardinality
        self.sparqlas_DataExactCardinality146 = sparqlas_DataExactCardinality146
        
        pass
    @property
    def cardinality(self):
        return self.__cardinality

    @cardinality.setter
    def cardinality(self, cardinality: int):
        self.__cardinality = cardinality


    @property
    def sparqlas_DataExactCardinality(self):
        return self.__sparqlas_DataExactCardinality

    @sparqlas_DataExactCardinality.setter
    def sparqlas_DataExactCardinality(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparqlas_DataExactCardinality__sparqlas_DataExactCardinality", None)
        self.__sparqlas_DataExactCardinality = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparqlas_DataRange144"):
                opp_val = getattr(old_value, "sparqlas_DataRange144", None)
                if opp_val == self:
                    setattr(old_value, "sparqlas_DataRange144", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparqlas_DataRange144"):
                opp_val = getattr(value, "sparqlas_DataRange144", None)
                setattr(value, "sparqlas_DataRange144", self)

    @property
    def sparqlas_DataExactCardinality146(self):
        return self.__sparqlas_DataExactCardinality146

    @sparqlas_DataExactCardinality146.setter
    def sparqlas_DataExactCardinality146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparqlas_DataExactCardinality__sparqlas_DataExactCardinality146", None)
        self.__sparqlas_DataExactCardinality146 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparqlas_DataPropertyExpression147"):
                opp_val = getattr(old_value, "sparqlas_DataPropertyExpression147", None)
                if opp_val == self:
                    setattr(old_value, "sparqlas_DataPropertyExpression147", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparqlas_DataPropertyExpression147"):
                opp_val = getattr(value, "sparqlas_DataPropertyExpression147", None)
                setattr(value, "sparqlas_DataPropertyExpression147", self)

class sparqlas_ObjectOneOf(ClassExpression):

    pass
class sparqlas_ObjectSomeValuesFrom(ClassExpression):

    pass
class sparqlas_ObjectMaxCardinality(ClassExpression):

    def __init__(self, cardinality: int, sparqlas_ObjectMaxCardinality: "sparqlas_ClassExpression" = None, sparqlas_ObjectMaxCardinality112: "sparqlas_ObjectPropertyExpression" = None):
        self.cardinality = cardinality
        self.sparqlas_ObjectMaxCardinality = sparqlas_ObjectMaxCardinality
        self.sparqlas_ObjectMaxCardinality112 = sparqlas_ObjectMaxCardinality112
        
        pass
    @property
    def cardinality(self):
        return self.__cardinality

    @cardinality.setter
    def cardinality(self, cardinality: int):
        self.__cardinality = cardinality


    @property
    def sparqlas_ObjectMaxCardinality112(self):
        return self.__sparqlas_ObjectMaxCardinality112

    @sparqlas_ObjectMaxCardinality112.setter
    def sparqlas_ObjectMaxCardinality112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparqlas_ObjectMaxCardinality__sparqlas_ObjectMaxCardinality112", None)
        self.__sparqlas_ObjectMaxCardinality112 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparqlas_ObjectPropertyExpression113"):
                opp_val = getattr(old_value, "sparqlas_ObjectPropertyExpression113", None)
                if opp_val == self:
                    setattr(old_value, "sparqlas_ObjectPropertyExpression113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparqlas_ObjectPropertyExpression113"):
                opp_val = getattr(value, "sparqlas_ObjectPropertyExpression113", None)
                setattr(value, "sparqlas_ObjectPropertyExpression113", self)

    @property
    def sparqlas_ObjectMaxCardinality(self):
        return self.__sparqlas_ObjectMaxCardinality

    @sparqlas_ObjectMaxCardinality.setter
    def sparqlas_ObjectMaxCardinality(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparqlas_ObjectMaxCardinality__sparqlas_ObjectMaxCardinality", None)
        self.__sparqlas_ObjectMaxCardinality = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparqlas_ClassExpression110"):
                opp_val = getattr(old_value, "sparqlas_ClassExpression110", None)
                if opp_val == self:
                    setattr(old_value, "sparqlas_ClassExpression110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparqlas_ClassExpression110"):
                opp_val = getattr(value, "sparqlas_ClassExpression110", None)
                setattr(value, "sparqlas_ClassExpression110", self)

class sparqlas_ObjectExactCardinality(ClassExpression):

    def __init__(self, cardinality: int, sparqlas_ObjectExactCardinality: "sparqlas_ClassExpression" = None, sparqlas_ObjectExactCardinality117: "sparqlas_ObjectPropertyExpression" = None):
        self.cardinality = cardinality
        self.sparqlas_ObjectExactCardinality = sparqlas_ObjectExactCardinality
        self.sparqlas_ObjectExactCardinality117 = sparqlas_ObjectExactCardinality117
        
        pass
    @property
    def cardinality(self):
        return self.__cardinality

    @cardinality.setter
    def cardinality(self, cardinality: int):
        self.__cardinality = cardinality


    @property
    def sparqlas_ObjectExactCardinality117(self):
        return self.__sparqlas_ObjectExactCardinality117

    @sparqlas_ObjectExactCardinality117.setter
    def sparqlas_ObjectExactCardinality117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparqlas_ObjectExactCardinality__sparqlas_ObjectExactCardinality117", None)
        self.__sparqlas_ObjectExactCardinality117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparqlas_ObjectPropertyExpression118"):
                opp_val = getattr(old_value, "sparqlas_ObjectPropertyExpression118", None)
                if opp_val == self:
                    setattr(old_value, "sparqlas_ObjectPropertyExpression118", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparqlas_ObjectPropertyExpression118"):
                opp_val = getattr(value, "sparqlas_ObjectPropertyExpression118", None)
                setattr(value, "sparqlas_ObjectPropertyExpression118", self)

    @property
    def sparqlas_ObjectExactCardinality(self):
        return self.__sparqlas_ObjectExactCardinality

    @sparqlas_ObjectExactCardinality.setter
    def sparqlas_ObjectExactCardinality(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparqlas_ObjectExactCardinality__sparqlas_ObjectExactCardinality", None)
        self.__sparqlas_ObjectExactCardinality = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparqlas_ClassExpression115"):
                opp_val = getattr(old_value, "sparqlas_ClassExpression115", None)
                if opp_val == self:
                    setattr(old_value, "sparqlas_ClassExpression115", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparqlas_ClassExpression115"):
                opp_val = getattr(value, "sparqlas_ClassExpression115", None)
                setattr(value, "sparqlas_ClassExpression115", self)

class sparqlas_ObjectMinCardinality(ClassExpression):

    def __init__(self, cardinality: int, sparqlas_ObjectMinCardinality107: "sparqlas_ObjectPropertyExpression" = None, sparqlas_ObjectMinCardinality: "sparqlas_ClassExpression" = None):
        self.cardinality = cardinality
        self.sparqlas_ObjectMinCardinality107 = sparqlas_ObjectMinCardinality107
        self.sparqlas_ObjectMinCardinality = sparqlas_ObjectMinCardinality
        
        pass
    @property
    def cardinality(self):
        return self.__cardinality

    @cardinality.setter
    def cardinality(self, cardinality: int):
        self.__cardinality = cardinality


    @property
    def sparqlas_ObjectMinCardinality(self):
        return self.__sparqlas_ObjectMinCardinality

    @sparqlas_ObjectMinCardinality.setter
    def sparqlas_ObjectMinCardinality(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparqlas_ObjectMinCardinality__sparqlas_ObjectMinCardinality", None)
        self.__sparqlas_ObjectMinCardinality = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparqlas_ClassExpression105"):
                opp_val = getattr(old_value, "sparqlas_ClassExpression105", None)
                if opp_val == self:
                    setattr(old_value, "sparqlas_ClassExpression105", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparqlas_ClassExpression105"):
                opp_val = getattr(value, "sparqlas_ClassExpression105", None)
                setattr(value, "sparqlas_ClassExpression105", self)

    @property
    def sparqlas_ObjectMinCardinality107(self):
        return self.__sparqlas_ObjectMinCardinality107

    @sparqlas_ObjectMinCardinality107.setter
    def sparqlas_ObjectMinCardinality107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparqlas_ObjectMinCardinality__sparqlas_ObjectMinCardinality107", None)
        self.__sparqlas_ObjectMinCardinality107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparqlas_ObjectPropertyExpression108"):
                opp_val = getattr(old_value, "sparqlas_ObjectPropertyExpression108", None)
                if opp_val == self:
                    setattr(old_value, "sparqlas_ObjectPropertyExpression108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparqlas_ObjectPropertyExpression108"):
                opp_val = getattr(value, "sparqlas_ObjectPropertyExpression108", None)
                setattr(value, "sparqlas_ObjectPropertyExpression108", self)

class Variable:

    pass
class sparqlas_ObjectPropertyVariable(ObjectPropertyExpression, Variable):

    pass
class sparqlas_LiteralVariable(AbstractLiteral, Variable):

    pass
class sparqlas_DataPropertyVariable(DataPropertyExpression, Variable):

    pass
class sparqlas_ClassVariable(ClassExpression, Variable):

    pass
class Term:

    pass
class sparqlas_Term(ABC):

    pass
class IRI:

    pass
class sparqlas_AbbreviatedIRI(IRI):

    pass
class sparqlas_Class(Constant, ClassExpression):

    pass
class sparqlas_Constant(Term):

    pass
class Individual:

    pass
class sparqlas_NamedIndividual(Constant, Individual):

    pass
class sparqlas_AnonymousIndividual(Individual):

    def __init__(self, nodeID: str):
        self.nodeID = nodeID
        
        pass
    @property
    def nodeID(self):
        return self.__nodeID

    @nodeID.setter
    def nodeID(self, nodeID: str):
        self.__nodeID = nodeID


class sparqlas_IndividualVariable(Individual, Variable):

    pass
class sparqlas_Variable(Term):

    def __init__(self, symbol: str, sparqlas_Variable: "sparqlas_SelectQuery" = None):
        self.symbol = symbol
        self.sparqlas_Variable = sparqlas_Variable
        
        pass
    @property
    def symbol(self):
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol


    @property
    def sparqlas_Variable(self):
        return self.__sparqlas_Variable

    @sparqlas_Variable.setter
    def sparqlas_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparqlas_Variable__sparqlas_Variable", None)
        self.__sparqlas_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparqlas_SelectQuery14"):
                opp_val = getattr(old_value, "sparqlas_SelectQuery14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparqlas_SelectQuery14"):
                opp_val = getattr(value, "sparqlas_SelectQuery14", None)
                if opp_val is None:
                    setattr(value, "sparqlas_SelectQuery14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sparqlas_Atom(ABC):

    pass
class TemplateableElement:

    pass
class Query:

    pass
class sparqlas_ConstructQuery(TemplateableElement, Query):

    pass
class sparqlas_SelectQuery(TemplateableElement, Query):

    pass
class sparqlas_FullIRI(IRI):

    pass
class sparqlas_DescribeQuery(TemplateableElement, Query):

    pass
class sparqlas_AskQuery(TemplateableElement, Query):

    pass
class sparqlas_Import:

    pass
class sparqlas_IRI(ABC):

    def __init__(self, id: str, sparqlas_IRI: "sparqlas_OntologyDocument" = None, sparqlas_IRI23: "sparqlas_DescribeQuery" = None, sparqlas_IRI9: "sparqlas_Import" = None, sparqlas_IRI28: "sparqlas_Constant" = None, sparqlas_IRI162: "sparqlas_FacetRestriction" = None):
        self.id = id
        self.sparqlas_IRI = sparqlas_IRI
        self.sparqlas_IRI23 = sparqlas_IRI23
        self.sparqlas_IRI9 = sparqlas_IRI9
        self.sparqlas_IRI28 = sparqlas_IRI28
        self.sparqlas_IRI162 = sparqlas_IRI162
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def sparqlas_IRI28(self):
        return self.__sparqlas_IRI28

    @sparqlas_IRI28.setter
    def sparqlas_IRI28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparqlas_IRI__sparqlas_IRI28", None)
        self.__sparqlas_IRI28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparqlas_Constant"):
                opp_val = getattr(old_value, "sparqlas_Constant", None)
                if opp_val == self:
                    setattr(old_value, "sparqlas_Constant", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparqlas_Constant"):
                opp_val = getattr(value, "sparqlas_Constant", None)
                setattr(value, "sparqlas_Constant", self)

    @property
    def sparqlas_IRI(self):
        return self.__sparqlas_IRI

    @sparqlas_IRI.setter
    def sparqlas_IRI(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparqlas_IRI__sparqlas_IRI", None)
        self.__sparqlas_IRI = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparqlas_OntologyDocument"):
                opp_val = getattr(old_value, "sparqlas_OntologyDocument", None)
                if opp_val == self:
                    setattr(old_value, "sparqlas_OntologyDocument", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparqlas_OntologyDocument"):
                opp_val = getattr(value, "sparqlas_OntologyDocument", None)
                setattr(value, "sparqlas_OntologyDocument", self)

    @property
    def sparqlas_IRI9(self):
        return self.__sparqlas_IRI9

    @sparqlas_IRI9.setter
    def sparqlas_IRI9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparqlas_IRI__sparqlas_IRI9", None)
        self.__sparqlas_IRI9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparqlas_Import8"):
                opp_val = getattr(old_value, "sparqlas_Import8", None)
                if opp_val == self:
                    setattr(old_value, "sparqlas_Import8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparqlas_Import8"):
                opp_val = getattr(value, "sparqlas_Import8", None)
                setattr(value, "sparqlas_Import8", self)

    @property
    def sparqlas_IRI162(self):
        return self.__sparqlas_IRI162

    @sparqlas_IRI162.setter
    def sparqlas_IRI162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparqlas_IRI__sparqlas_IRI162", None)
        self.__sparqlas_IRI162 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparqlas_FacetRestriction161"):
                opp_val = getattr(old_value, "sparqlas_FacetRestriction161", None)
                if opp_val == self:
                    setattr(old_value, "sparqlas_FacetRestriction161", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparqlas_FacetRestriction161"):
                opp_val = getattr(value, "sparqlas_FacetRestriction161", None)
                setattr(value, "sparqlas_FacetRestriction161", self)

    @property
    def sparqlas_IRI23(self):
        return self.__sparqlas_IRI23

    @sparqlas_IRI23.setter
    def sparqlas_IRI23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparqlas_IRI__sparqlas_IRI23", None)
        self.__sparqlas_IRI23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparqlas_DescribeQuery"):
                opp_val = getattr(old_value, "sparqlas_DescribeQuery", None)
                if opp_val == self:
                    setattr(old_value, "sparqlas_DescribeQuery", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparqlas_DescribeQuery"):
                opp_val = getattr(value, "sparqlas_DescribeQuery", None)
                setattr(value, "sparqlas_DescribeQuery", self)

class sparqlas_OntologyDocument:

    pass
class sparqlas_Query(ABC):

    pass
class sparqlas_PrefixDefinition:

    def __init__(self, pref: str, sparqlas_PrefixDefinition: "sparqlas_OntologyDocument" = None, sparqlas_PrefixDefinition11: "sparqlas_FullIRI" = None):
        self.pref = pref
        self.sparqlas_PrefixDefinition = sparqlas_PrefixDefinition
        self.sparqlas_PrefixDefinition11 = sparqlas_PrefixDefinition11
        
        pass
    @property
    def pref(self):
        return self.__pref

    @pref.setter
    def pref(self, pref: str):
        self.__pref = pref


    @property
    def sparqlas_PrefixDefinition11(self):
        return self.__sparqlas_PrefixDefinition11

    @sparqlas_PrefixDefinition11.setter
    def sparqlas_PrefixDefinition11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparqlas_PrefixDefinition__sparqlas_PrefixDefinition11", None)
        self.__sparqlas_PrefixDefinition11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparqlas_FullIRI"):
                opp_val = getattr(old_value, "sparqlas_FullIRI", None)
                if opp_val == self:
                    setattr(old_value, "sparqlas_FullIRI", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparqlas_FullIRI"):
                opp_val = getattr(value, "sparqlas_FullIRI", None)
                setattr(value, "sparqlas_FullIRI", self)

    @property
    def sparqlas_PrefixDefinition(self):
        return self.__sparqlas_PrefixDefinition

    @sparqlas_PrefixDefinition.setter
    def sparqlas_PrefixDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparqlas_PrefixDefinition__sparqlas_PrefixDefinition", None)
        self.__sparqlas_PrefixDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparqlas_OntologyDocument4"):
                opp_val = getattr(old_value, "sparqlas_OntologyDocument4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparqlas_OntologyDocument4"):
                opp_val = getattr(value, "sparqlas_OntologyDocument4", None)
                if opp_val is None:
                    setattr(value, "sparqlas_OntologyDocument4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
