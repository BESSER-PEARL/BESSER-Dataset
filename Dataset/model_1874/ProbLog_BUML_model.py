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
problog_LHS = Class(name="problog::LHS")
problog_RHS = Class(name="problog::RHS")
problog_Evidence = Class(name="problog::Evidence")
ProbLogStatement = Class(name="ProbLogStatement")
problog_Query = Class(name="problog::Query")
problog_ProbLogProgram = Class(name="problog::ProbLogProgram")
problog_Statement = Class(name="problog::Statement", is_abstract=True)
problog_Term = Class(name="problog::Term")
problog_Rule = Class(name="problog::Rule")
Statement = Class(name="Statement")
problog_Variable = Class(name="problog::Variable")
problog_AnnotatedReferable = Class(name="problog::AnnotatedReferable")
Proposition = Class(name="Proposition")
problog_ProbabilityMeasure = Class(name="problog::ProbabilityMeasure", is_abstract=True)
problog_Proposition = Class(name="problog::Proposition", is_abstract=True)
problog_Referable = Class(name="problog::Referable", is_abstract=True)
problog_Atom = Class(name="problog::Atom")
Referable = Class(name="Referable")
Annotatable = Class(name="Annotatable")
problog_ProbLogStatement = Class(name="problog::ProbLogStatement", is_abstract=True)
problog_Annotatable = Class(name="problog::Annotatable", is_abstract=True)
problog_ProbabilityLiteral = Class(name="problog::ProbabilityLiteral")
ProbabilityMeasure = Class(name="ProbabilityMeasure")
problog_ProbabilityFraction = Class(name="problog::ProbabilityFraction")
problog_ImportLibrary = Class(name="problog::ImportLibrary")
problog_Collection = Class(name="problog::Collection", is_abstract=True)
problog_PLList = Class(name="problog::PLList")
Collection = Class(name="Collection")
problog_TermInstance = Class(name="problog::TermInstance")
problog_Comment = Class(name="problog::Comment")
problog_Cheat = Class(name="problog::Cheat")
problog_PLTuple = Class(name="problog::PLTuple")

# problog_LHS class attributes and methods

# problog_RHS class attributes and methods

# problog_Evidence class attributes and methods
problog_Evidence_value: Property = Property(name="value", type=StringType)
problog_Evidence.attributes={problog_Evidence_value}

# ProbLogStatement class attributes and methods

# problog_Query class attributes and methods

# problog_ProbLogProgram class attributes and methods

# problog_Statement class attributes and methods

# problog_Term class attributes and methods
problog_Term_name: Property = Property(name="name", type=StringType)
problog_Term_arguments: Property = Property(name="arguments", type=IntegerType)
problog_Term.attributes={problog_Term_name, problog_Term_arguments}

# problog_Rule class attributes and methods

# Statement class attributes and methods

# problog_Variable class attributes and methods
problog_Variable_name: Property = Property(name="name", type=StringType)
problog_Variable.attributes={problog_Variable_name}

# problog_AnnotatedReferable class attributes and methods

# Proposition class attributes and methods

# problog_ProbabilityMeasure class attributes and methods

# problog_Proposition class attributes and methods

# problog_Referable class attributes and methods

# problog_Atom class attributes and methods
problog_Atom_name: Property = Property(name="name", type=StringType)
problog_Atom.attributes={problog_Atom_name}

# Referable class attributes and methods

# Annotatable class attributes and methods

# problog_ProbLogStatement class attributes and methods

# problog_Annotatable class attributes and methods

# problog_ProbabilityLiteral class attributes and methods
problog_ProbabilityLiteral_value: Property = Property(name="value", type=FloatType)
problog_ProbabilityLiteral.attributes={problog_ProbabilityLiteral_value}

# ProbabilityMeasure class attributes and methods

# problog_ProbabilityFraction class attributes and methods
problog_ProbabilityFraction_nominator: Property = Property(name="nominator", type=IntegerType)
problog_ProbabilityFraction_denominator: Property = Property(name="denominator", type=IntegerType)
problog_ProbabilityFraction.attributes={problog_ProbabilityFraction_nominator, problog_ProbabilityFraction_denominator}

# problog_ImportLibrary class attributes and methods
problog_ImportLibrary_name: Property = Property(name="name", type=StringType)
problog_ImportLibrary.attributes={problog_ImportLibrary_name}

# problog_Collection class attributes and methods

# problog_PLList class attributes and methods

# Collection class attributes and methods

# problog_TermInstance class attributes and methods

# problog_Comment class attributes and methods
problog_Comment_text: Property = Property(name="text", type=StringType)
problog_Comment.attributes={problog_Comment_text}

# problog_Cheat class attributes and methods
problog_Cheat_contents: Property = Property(name="contents", type=StringType)
problog_Cheat.attributes={problog_Cheat_contents}

# problog_PLTuple class attributes and methods

# Relationships
lhs3: BinaryAssociation = BinaryAssociation(
    name="lhs3",
    ends={
        Property(name="problog_LHS", type=problog_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="problog_Rule", type=problog_LHS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs4: BinaryAssociation = BinaryAssociation(
    name="rhs4",
    ends={
        Property(name="problog_RHS", type=problog_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="problog_Rule5", type=problog_RHS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements0: BinaryAssociation = BinaryAssociation(
    name="statements0",
    ends={
        Property(name="problog_Statement", type=problog_ProbLogProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="problog_ProbLogProgram", type=problog_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
terms1: BinaryAssociation = BinaryAssociation(
    name="terms1",
    ends={
        Property(name="problog_Term", type=problog_ProbLogProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="problog_ProbLogProgram2", type=problog_Term, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
probabilitymeasure10: BinaryAssociation = BinaryAssociation(
    name="probabilitymeasure10",
    ends={
        Property(name="problog_ProbabilityMeasure", type=problog_AnnotatedReferable, multiplicity=Multiplicity(1, 1)),
        Property(name="problog_AnnotatedReferable", type=problog_ProbabilityMeasure, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
propositions6: BinaryAssociation = BinaryAssociation(
    name="propositions6",
    ends={
        Property(name="problog_Proposition", type=problog_LHS, multiplicity=Multiplicity(1, 1)),
        Property(name="problog_LHS7", type=problog_Proposition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conjunction8: BinaryAssociation = BinaryAssociation(
    name="conjunction8",
    ends={
        Property(name="problog_Referable", type=problog_RHS, multiplicity=Multiplicity(1, 1)),
        Property(name="problog_RHS9", type=problog_Referable, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
subject13: BinaryAssociation = BinaryAssociation(
    name="subject13",
    ends={
        Property(name="problog_Referable14", type=problog_ProbLogStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="problog_ProbLogStatement", type=problog_Referable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
annotates11: BinaryAssociation = BinaryAssociation(
    name="annotates11",
    ends={
        Property(name="problog_Annotatable", type=problog_AnnotatedReferable, multiplicity=Multiplicity(1, 1)),
        Property(name="problog_AnnotatedReferable12", type=problog_Annotatable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
contents20: BinaryAssociation = BinaryAssociation(
    name="contents20",
    ends={
        Property(name="problog_Referable21", type=problog_Collection, multiplicity=Multiplicity(1, 1)),
        Property(name="problog_Collection", type=problog_Referable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
template15: BinaryAssociation = BinaryAssociation(
    name="template15",
    ends={
        Property(name="problog_Term16", type=problog_TermInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="problog_TermInstance", type=problog_Term, multiplicity=Multiplicity(1, 1))
    }
)
arguments17: BinaryAssociation = BinaryAssociation(
    name="arguments17",
    ends={
        Property(name="problog_Referable19", type=problog_TermInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="problog_TermInstance18", type=problog_Referable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_problog_Rule_Statement = Generalization(general=Statement, specific=problog_Rule)
gen_problog_Evidence_ProbLogStatement = Generalization(general=ProbLogStatement, specific=problog_Evidence)
gen_problog_Variable_Referable = Generalization(general=Referable, specific=problog_Variable)
gen_problog_AnnotatedReferable_Proposition = Generalization(general=Proposition, specific=problog_AnnotatedReferable)
gen_problog_Query_ProbLogStatement = Generalization(general=ProbLogStatement, specific=problog_Query)
gen_problog_Atom_Referable = Generalization(general=Referable, specific=problog_Atom)
gen_problog_Atom_Annotatable = Generalization(general=Annotatable, specific=problog_Atom)
gen_problog_Annotatable_Proposition = Generalization(general=Proposition, specific=problog_Annotatable)
gen_problog_ProbLogStatement_Statement = Generalization(general=Statement, specific=problog_ProbLogStatement)
gen_problog_ProbabilityLiteral_ProbabilityMeasure = Generalization(general=ProbabilityMeasure, specific=problog_ProbabilityLiteral)
gen_problog_ProbabilityFraction_ProbabilityMeasure = Generalization(general=ProbabilityMeasure, specific=problog_ProbabilityFraction)
gen_problog_ImportLibrary_Statement = Generalization(general=Statement, specific=problog_ImportLibrary)
gen_problog_Collection_Referable = Generalization(general=Referable, specific=problog_Collection)
gen_problog_PLList_Collection = Generalization(general=Collection, specific=problog_PLList)
gen_problog_TermInstance_Annotatable = Generalization(general=Annotatable, specific=problog_TermInstance)
gen_problog_TermInstance_Referable = Generalization(general=Referable, specific=problog_TermInstance)
gen_problog_Comment_Statement = Generalization(general=Statement, specific=problog_Comment)
gen_problog_Cheat_Statement = Generalization(general=Statement, specific=problog_Cheat)
gen_problog_PLTuple_Collection = Generalization(general=Collection, specific=problog_PLTuple)

# Domain Model
domain_model = DomainModel(
    name="problog",
    types={problog_LHS, problog_RHS, problog_Evidence, ProbLogStatement, problog_Query, problog_ProbLogProgram, problog_Statement, problog_Term, problog_Rule, Statement, problog_Variable, problog_AnnotatedReferable, Proposition, problog_ProbabilityMeasure, problog_Proposition, problog_Referable, problog_Atom, Referable, Annotatable, problog_ProbLogStatement, problog_Annotatable, problog_ProbabilityLiteral, ProbabilityMeasure, problog_ProbabilityFraction, problog_ImportLibrary, problog_Collection, problog_PLList, Collection, problog_TermInstance, problog_Comment, problog_Cheat, problog_PLTuple},
    associations={lhs3, rhs4, statements0, terms1, probabilitymeasure10, propositions6, conjunction8, subject13, annotates11, contents20, template15, arguments17},
    generalizations={gen_problog_Rule_Statement, gen_problog_Evidence_ProbLogStatement, gen_problog_Variable_Referable, gen_problog_AnnotatedReferable_Proposition, gen_problog_Query_ProbLogStatement, gen_problog_Atom_Referable, gen_problog_Atom_Annotatable, gen_problog_Annotatable_Proposition, gen_problog_ProbLogStatement_Statement, gen_problog_ProbabilityLiteral_ProbabilityMeasure, gen_problog_ProbabilityFraction_ProbabilityMeasure, gen_problog_ImportLibrary_Statement, gen_problog_Collection_Referable, gen_problog_PLList_Collection, gen_problog_TermInstance_Annotatable, gen_problog_TermInstance_Referable, gen_problog_Comment_Statement, gen_problog_Cheat_Statement, gen_problog_PLTuple_Collection},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)