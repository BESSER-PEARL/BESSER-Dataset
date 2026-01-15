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

# Enumerations
ADDITIVE_OPERATOR: Enumeration = Enumeration(
    name="ADDITIVE_OPERATOR",
    literals={
            EnumerationLiteral(name="plus"),
			EnumerationLiteral(name="minus")
    }
)

MULTIPLICATIVE_OPERATOR: Enumeration = Enumeration(
    name="MULTIPLICATIVE_OPERATOR",
    literals={
            EnumerationLiteral(name="mult"),
			EnumerationLiteral(name="div")
    }
)

# Classes
prolog_PrologProgram = Class(name="prolog::PrologProgram")
prolog_Clause = Class(name="prolog::Clause")
prolog_Predicate = Class(name="prolog::Predicate")
prolog_VariableReference = Class(name="prolog::VariableReference")
prolog_AnonymousVariable = Class(name="prolog::AnonymousVariable")
prolog_Assignment = Class(name="prolog::Assignment")
prolog_Part = Class(name="prolog::Part", is_abstract=True)
prolog_Conjunction = Class(name="prolog::Conjunction")
prolog_Term = Class(name="prolog::Term", is_abstract=True)
prolog_Numeral = Class(name="prolog::Numeral")
Term = Class(name="Term")
prolog_Variable = Class(name="prolog::Variable")
Tail = Class(name="Tail")
prolog_String = Class(name="prolog::String")
prolog_List = Class(name="prolog::List")
prolog_Tail = Class(name="prolog::Tail", is_abstract=True)
Part = Class(name="Part")
prolog_BracketExpression = Class(name="prolog::BracketExpression")
prolog_Additive = Class(name="prolog::Additive")
prolog_Multiplicative = Class(name="prolog::Multiplicative")
prolog_Power = Class(name="prolog::Power")
prolog_Negation = Class(name="prolog::Negation")

# prolog_PrologProgram class attributes and methods

# prolog_Clause class attributes and methods

# prolog_Predicate class attributes and methods
prolog_Predicate_name: Property = Property(name="name", type=StringType)
prolog_Predicate.attributes={prolog_Predicate_name}

# prolog_VariableReference class attributes and methods

# prolog_AnonymousVariable class attributes and methods
prolog_AnonymousVariable_text: Property = Property(name="text", type=StringType)
prolog_AnonymousVariable.attributes={prolog_AnonymousVariable_text}

# prolog_Assignment class attributes and methods

# prolog_Part class attributes and methods

# prolog_Conjunction class attributes and methods

# prolog_Term class attributes and methods

# prolog_Numeral class attributes and methods
prolog_Numeral_value: Property = Property(name="value", type=FloatType)
prolog_Numeral.attributes={prolog_Numeral_value}

# Term class attributes and methods

# prolog_Variable class attributes and methods
prolog_Variable_name: Property = Property(name="name", type=StringType)
prolog_Variable.attributes={prolog_Variable_name}

# Tail class attributes and methods

# prolog_String class attributes and methods
prolog_String_text: Property = Property(name="text", type=StringType)
prolog_String.attributes={prolog_String_text}

# prolog_List class attributes and methods

# prolog_Tail class attributes and methods

# Part class attributes and methods

# prolog_BracketExpression class attributes and methods

# prolog_Additive class attributes and methods
prolog_Additive_operator: Property = Property(name="operator", type=StringType)
prolog_Additive.attributes={prolog_Additive_operator}

# prolog_Multiplicative class attributes and methods
prolog_Multiplicative_operator: Property = Property(name="operator", type=StringType)
prolog_Multiplicative.attributes={prolog_Multiplicative_operator}

# prolog_Power class attributes and methods

# prolog_Negation class attributes and methods
prolog_Negation_operator: Property = Property(name="operator", type=StringType)
prolog_Negation.attributes={prolog_Negation_operator}

# Relationships
clauses0: BinaryAssociation = BinaryAssociation(
    name="clauses0",
    ends={
        Property(name="prolog_Clause", type=prolog_PrologProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="prolog_PrologProgram", type=prolog_Clause, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
predicate1: BinaryAssociation = BinaryAssociation(
    name="predicate1",
    ends={
        Property(name="prolog_Predicate", type=prolog_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="prolog_Clause2", type=prolog_Predicate, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable11: BinaryAssociation = BinaryAssociation(
    name="variable11",
    ends={
        Property(name="prolog_Variable", type=prolog_VariableReference, multiplicity=Multiplicity(1, 1)),
        Property(name="prolog_VariableReference", type=prolog_Variable, multiplicity=Multiplicity(1, 1))
    }
)
variable12: BinaryAssociation = BinaryAssociation(
    name="variable12",
    ends={
        Property(name="prolog_VariableReference13", type=prolog_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="prolog_Assignment", type=prolog_VariableReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
term14: BinaryAssociation = BinaryAssociation(
    name="term14",
    ends={
        Property(name="prolog_Term16", type=prolog_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="prolog_Assignment15", type=prolog_Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parts17: BinaryAssociation = BinaryAssociation(
    name="parts17",
    ends={
        Property(name="prolog_Part", type=prolog_Conjunction, multiplicity=Multiplicity(1, 1)),
        Property(name="prolog_Conjunction18", type=prolog_Part, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
conjunction3: BinaryAssociation = BinaryAssociation(
    name="conjunction3",
    ends={
        Property(name="prolog_Conjunction", type=prolog_Clause, multiplicity=Multiplicity(1, 1)),
        Property(name="prolog_Clause4", type=prolog_Conjunction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
headTerms5: BinaryAssociation = BinaryAssociation(
    name="headTerms5",
    ends={
        Property(name="prolog_Term", type=prolog_List, multiplicity=Multiplicity(1, 1)),
        Property(name="prolog_List", type=prolog_Term, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tail6: BinaryAssociation = BinaryAssociation(
    name="tail6",
    ends={
        Property(name="prolog_Tail", type=prolog_List, multiplicity=Multiplicity(1, 1)),
        Property(name="prolog_List7", type=prolog_Tail, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
terms8: BinaryAssociation = BinaryAssociation(
    name="terms8",
    ends={
        Property(name="prolog_Term10", type=prolog_Predicate, multiplicity=Multiplicity(1, 1)),
        Property(name="prolog_Predicate9", type=prolog_Term, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body34: BinaryAssociation = BinaryAssociation(
    name="body34",
    ends={
        Property(name="prolog_Term35", type=prolog_Negation, multiplicity=Multiplicity(1, 1)),
        Property(name="prolog_Negation", type=prolog_Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body36: BinaryAssociation = BinaryAssociation(
    name="body36",
    ends={
        Property(name="prolog_Term37", type=prolog_BracketExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="prolog_BracketExpression", type=prolog_Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
left19: BinaryAssociation = BinaryAssociation(
    name="left19",
    ends={
        Property(name="prolog_Term20", type=prolog_Additive, multiplicity=Multiplicity(1, 1)),
        Property(name="prolog_Additive", type=prolog_Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right21: BinaryAssociation = BinaryAssociation(
    name="right21",
    ends={
        Property(name="prolog_Term23", type=prolog_Additive, multiplicity=Multiplicity(1, 1)),
        Property(name="prolog_Additive22", type=prolog_Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
left24: BinaryAssociation = BinaryAssociation(
    name="left24",
    ends={
        Property(name="prolog_Term25", type=prolog_Multiplicative, multiplicity=Multiplicity(1, 1)),
        Property(name="prolog_Multiplicative", type=prolog_Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right26: BinaryAssociation = BinaryAssociation(
    name="right26",
    ends={
        Property(name="prolog_Term28", type=prolog_Multiplicative, multiplicity=Multiplicity(1, 1)),
        Property(name="prolog_Multiplicative27", type=prolog_Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
base29: BinaryAssociation = BinaryAssociation(
    name="base29",
    ends={
        Property(name="prolog_Term30", type=prolog_Power, multiplicity=Multiplicity(1, 1)),
        Property(name="prolog_Power", type=prolog_Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
exponent31: BinaryAssociation = BinaryAssociation(
    name="exponent31",
    ends={
        Property(name="prolog_Term33", type=prolog_Power, multiplicity=Multiplicity(1, 1)),
        Property(name="prolog_Power32", type=prolog_Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_prolog_VariableReference_Term = Generalization(general=Term, specific=prolog_VariableReference)
gen_prolog_AnonymousVariable_Term = Generalization(general=Term, specific=prolog_AnonymousVariable)
gen_prolog_Assignment_Part = Generalization(general=Part, specific=prolog_Assignment)
gen_prolog_Numeral_Term = Generalization(general=Term, specific=prolog_Numeral)
gen_prolog_Variable_Term = Generalization(general=Term, specific=prolog_Variable)
gen_prolog_Variable_Tail = Generalization(general=Tail, specific=prolog_Variable)
gen_prolog_String_Term = Generalization(general=Term, specific=prolog_String)
gen_prolog_List_Term = Generalization(general=Term, specific=prolog_List)
gen_prolog_List_Tail = Generalization(general=Tail, specific=prolog_List)
gen_prolog_Predicate_Part = Generalization(general=Part, specific=prolog_Predicate)
gen_prolog_Predicate_Term = Generalization(general=Term, specific=prolog_Predicate)
gen_prolog_BracketExpression_Term = Generalization(general=Term, specific=prolog_BracketExpression)
gen_prolog_Additive_Term = Generalization(general=Term, specific=prolog_Additive)
gen_prolog_Multiplicative_Term = Generalization(general=Term, specific=prolog_Multiplicative)
gen_prolog_Power_Term = Generalization(general=Term, specific=prolog_Power)
gen_prolog_Negation_Term = Generalization(general=Term, specific=prolog_Negation)

# Domain Model
domain_model = DomainModel(
    name="prolog",
    types={prolog_PrologProgram, prolog_Clause, prolog_Predicate, prolog_VariableReference, prolog_AnonymousVariable, prolog_Assignment, prolog_Part, prolog_Conjunction, prolog_Term, prolog_Numeral, Term, prolog_Variable, Tail, prolog_String, prolog_List, prolog_Tail, Part, prolog_BracketExpression, prolog_Additive, prolog_Multiplicative, prolog_Power, prolog_Negation, ADDITIVE_OPERATOR, MULTIPLICATIVE_OPERATOR},
    associations={clauses0, predicate1, variable11, variable12, term14, parts17, conjunction3, headTerms5, tail6, terms8, body34, body36, left19, right21, left24, right26, base29, exponent31},
    generalizations={gen_prolog_VariableReference_Term, gen_prolog_AnonymousVariable_Term, gen_prolog_Assignment_Part, gen_prolog_Numeral_Term, gen_prolog_Variable_Term, gen_prolog_Variable_Tail, gen_prolog_String_Term, gen_prolog_List_Term, gen_prolog_List_Tail, gen_prolog_Predicate_Part, gen_prolog_Predicate_Term, gen_prolog_BracketExpression_Term, gen_prolog_Additive_Term, gen_prolog_Multiplicative_Term, gen_prolog_Power_Term, gen_prolog_Negation_Term},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)