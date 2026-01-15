####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Classes
mprologTermReference_Model = Class(name="mprologTermReference::Model")
mprologTermReference_QuotedAtom = Class(name="mprologTermReference::QuotedAtom")
mprologTermReference_List = Class(name="mprologTermReference::List")
mprologTermReference_InfixExpression = Class(name="mprologTermReference::InfixExpression")
mprologTermReference_Operator = Class(name="mprologTermReference::Operator")
mprologTermReference_TermReference = Class(name="mprologTermReference::TermReference", is_abstract=True)
mprologTermReference_FunctorReference = Class(name="mprologTermReference::FunctorReference")
TermReference = Class(name="TermReference")
mprologTermReference_Clause = Class(name="mprologTermReference::Clause")
mprologTermReference_Head = Class(name="mprologTermReference::Head")
mprologTermReference_Body = Class(name="mprologTermReference::Body")
mprologTermReference_Functor = Class(name="mprologTermReference::Functor")
mprologTermReference_Term = Class(name="mprologTermReference::Term", is_abstract=True)
mprologTermReference_Variable = Class(name="mprologTermReference::Variable")
Term = Class(name="Term")
mprologTermReference_VariableReference = Class(name="mprologTermReference::VariableReference")
mprologTermReference_Parenthesis = Class(name="mprologTermReference::Parenthesis")

# mprologTermReference_Model class attributes and methods
mprologTermReference_Model_name: Property = Property(name="name", type=StringType)
mprologTermReference_Model.attributes={mprologTermReference_Model_name}

# mprologTermReference_QuotedAtom class attributes and methods
mprologTermReference_QuotedAtom_text: Property = Property(name="text", type=StringType)
mprologTermReference_QuotedAtom.attributes={mprologTermReference_QuotedAtom_text}

# mprologTermReference_List class attributes and methods

# mprologTermReference_InfixExpression class attributes and methods

# mprologTermReference_Operator class attributes and methods
mprologTermReference_Operator_symbol: Property = Property(name="symbol", type=StringType)
mprologTermReference_Operator.attributes={mprologTermReference_Operator_symbol}

# mprologTermReference_TermReference class attributes and methods

# mprologTermReference_FunctorReference class attributes and methods

# TermReference class attributes and methods

# mprologTermReference_Clause class attributes and methods

# mprologTermReference_Head class attributes and methods

# mprologTermReference_Body class attributes and methods

# mprologTermReference_Functor class attributes and methods
mprologTermReference_Functor_text: Property = Property(name="text", type=StringType)
mprologTermReference_Functor.attributes={mprologTermReference_Functor_text}

# mprologTermReference_Term class attributes and methods

# mprologTermReference_Variable class attributes and methods
mprologTermReference_Variable_name: Property = Property(name="name", type=StringType)
mprologTermReference_Variable.attributes={mprologTermReference_Variable_name}

# Term class attributes and methods

# mprologTermReference_VariableReference class attributes and methods

# mprologTermReference_Parenthesis class attributes and methods

# Relationships
ownedTerm12: BinaryAssociation = BinaryAssociation(
    name="ownedTerm12",
    ends={
        Property(name="mprologTermReference_Term14", type=mprologTermReference_Functor, multiplicity=Multiplicity(1, 1)),
        Property(name="mprologTermReference_Functor13", type=mprologTermReference_Term, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedHeadTerms15: BinaryAssociation = BinaryAssociation(
    name="ownedHeadTerms15",
    ends={
        Property(name="mprologTermReference_Term16", type=mprologTermReference_List, multiplicity=Multiplicity(1, 1)),
        Property(name="mprologTermReference_List", type=mprologTermReference_Term, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedTailTerms17: BinaryAssociation = BinaryAssociation(
    name="ownedTailTerms17",
    ends={
        Property(name="mprologTermReference_Term19", type=mprologTermReference_List, multiplicity=Multiplicity(1, 1)),
        Property(name="mprologTermReference_List18", type=mprologTermReference_Term, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftTerm20: BinaryAssociation = BinaryAssociation(
    name="leftTerm20",
    ends={
        Property(name="mprologTermReference_Term21", type=mprologTermReference_InfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mprologTermReference_InfixExpression", type=mprologTermReference_Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightTerm22: BinaryAssociation = BinaryAssociation(
    name="rightTerm22",
    ends={
        Property(name="mprologTermReference_Term24", type=mprologTermReference_InfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mprologTermReference_InfixExpression23", type=mprologTermReference_Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ownedOperator25: BinaryAssociation = BinaryAssociation(
    name="ownedOperator25",
    ends={
        Property(name="mprologTermReference_Operator", type=mprologTermReference_InfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mprologTermReference_InfixExpression26", type=mprologTermReference_Operator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
idReference27: BinaryAssociation = BinaryAssociation(
    name="idReference27",
    ends={
        Property(name="mprologTermReference_Functor28", type=mprologTermReference_FunctorReference, multiplicity=Multiplicity(1, 1)),
        Property(name="mprologTermReference_FunctorReference", type=mprologTermReference_Functor, multiplicity=Multiplicity(0, 1))
    }
)
ownedTerm29: BinaryAssociation = BinaryAssociation(
    name="ownedTerm29",
    ends={
        Property(name="mprologTermReference_Term31", type=mprologTermReference_FunctorReference, multiplicity=Multiplicity(1, 1)),
        Property(name="mprologTermReference_FunctorReference30", type=mprologTermReference_Term, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedClause0: BinaryAssociation = BinaryAssociation(
    name="ownedClause0",
    ends={
        Property(name="mprologTermReference_Clause", type=mprologTermReference_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="mprologTermReference_Model", type=mprologTermReference_Clause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedHead1: BinaryAssociation = BinaryAssociation(
    name="ownedHead1",
    ends={
        Property(name="mprologTermReference_Head", type=mprologTermReference_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="mprologTermReference_Clause2", type=mprologTermReference_Head, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedBody3: BinaryAssociation = BinaryAssociation(
    name="ownedBody3",
    ends={
        Property(name="mprologTermReference_Body", type=mprologTermReference_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="mprologTermReference_Clause4", type=mprologTermReference_Body, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedFunctor5: BinaryAssociation = BinaryAssociation(
    name="ownedFunctor5",
    ends={
        Property(name="mprologTermReference_Functor", type=mprologTermReference_Head, multiplicity=Multiplicity(1, 1)),
        Property(name="mprologTermReference_Head6", type=mprologTermReference_Functor, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
nextTerm8: BinaryAssociation = BinaryAssociation(
    name="nextTerm8",
    ends={
        Property(name="mprologTermReference_Term", type=mprologTermReference_Term, multiplicity=Multiplicity(1, 1)),
        Property(name="mprologTermReference_Term7", type=mprologTermReference_Term, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedTerm9: BinaryAssociation = BinaryAssociation(
    name="ownedTerm9",
    ends={
        Property(name="mprologTermReference_Term11", type=mprologTermReference_Body, multiplicity=Multiplicity(1, 1)),
        Property(name="mprologTermReference_Body10", type=mprologTermReference_Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
idReference32: BinaryAssociation = BinaryAssociation(
    name="idReference32",
    ends={
        Property(name="mprologTermReference_Variable", type=mprologTermReference_VariableReference, multiplicity=Multiplicity(1, 1)),
        Property(name="mprologTermReference_VariableReference", type=mprologTermReference_Variable, multiplicity=Multiplicity(0, 1))
    }
)
ownedTerm33: BinaryAssociation = BinaryAssociation(
    name="ownedTerm33",
    ends={
        Property(name="mprologTermReference_Term34", type=mprologTermReference_Parenthesis, multiplicity=Multiplicity(1, 1)),
        Property(name="mprologTermReference_Parenthesis", type=mprologTermReference_Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_mprologTermReference_Variable_Term = Generalization(general=Term, specific=mprologTermReference_Variable)
gen_mprologTermReference_Functor_Term = Generalization(general=Term, specific=mprologTermReference_Functor)
gen_mprologTermReference_QuotedAtom_Term = Generalization(general=Term, specific=mprologTermReference_QuotedAtom)
gen_mprologTermReference_List_Term = Generalization(general=Term, specific=mprologTermReference_List)
gen_mprologTermReference_InfixExpression_Term = Generalization(general=Term, specific=mprologTermReference_InfixExpression)
gen_mprologTermReference_TermReference_Term = Generalization(general=Term, specific=mprologTermReference_TermReference)
gen_mprologTermReference_FunctorReference_TermReference = Generalization(general=TermReference, specific=mprologTermReference_FunctorReference)
gen_mprologTermReference_VariableReference_TermReference = Generalization(general=TermReference, specific=mprologTermReference_VariableReference)
gen_mprologTermReference_Parenthesis_Term = Generalization(general=Term, specific=mprologTermReference_Parenthesis)

# Domain Model
domain_model = DomainModel(
    name="mprologTermReference",
    types={mprologTermReference_Model, mprologTermReference_QuotedAtom, mprologTermReference_List, mprologTermReference_InfixExpression, mprologTermReference_Operator, mprologTermReference_TermReference, mprologTermReference_FunctorReference, TermReference, mprologTermReference_Clause, mprologTermReference_Head, mprologTermReference_Body, mprologTermReference_Functor, mprologTermReference_Term, mprologTermReference_Variable, Term, mprologTermReference_VariableReference, mprologTermReference_Parenthesis},
    associations={ownedTerm12, ownedHeadTerms15, ownedTailTerms17, leftTerm20, rightTerm22, ownedOperator25, idReference27, ownedTerm29, ownedClause0, ownedHead1, ownedBody3, ownedFunctor5, nextTerm8, ownedTerm9, idReference32, ownedTerm33},
    generalizations={gen_mprologTermReference_Variable_Term, gen_mprologTermReference_Functor_Term, gen_mprologTermReference_QuotedAtom_Term, gen_mprologTermReference_List_Term, gen_mprologTermReference_InfixExpression_Term, gen_mprologTermReference_TermReference_Term, gen_mprologTermReference_FunctorReference_TermReference, gen_mprologTermReference_VariableReference_TermReference, gen_mprologTermReference_Parenthesis_Term},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)