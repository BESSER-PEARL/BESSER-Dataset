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
BooleanOperator: Enumeration = Enumeration(
    name="BooleanOperator",
    literals={
            EnumerationLiteral(name="And"),
			EnumerationLiteral(name="Or")
    }
)

ComparisionOperator: Enumeration = Enumeration(
    name="ComparisionOperator",
    literals={
            EnumerationLiteral(name="GreaterThan"),
			EnumerationLiteral(name="LessThan")
    }
)

# Classes
expression_Expression = Class(name="expression::Expression", is_abstract=True)
expression_Literal = Class(name="expression::Literal", is_abstract=True)
expression_NullLiteral = Class(name="expression::NullLiteral")
Literal = Class(name="Literal")
expression_BooleanLiteral = Class(name="expression::BooleanLiteral")
expression_IntegerLiteral = Class(name="expression::IntegerLiteral")
expression_StringLiteral = Class(name="expression::StringLiteral")
expression_TimeLiteral = Class(name="expression::TimeLiteral")
expression_Variable = Class(name="expression::Variable", is_abstract=True)
expression_Predicate = Class(name="expression::Predicate", is_abstract=True)
expression_PredicateBooleanOperator = Class(name="expression::PredicateBooleanOperator")
Predicate = Class(name="Predicate")
Expression = Class(name="Expression")
expression_PredicateEqualityOperator = Class(name="expression::PredicateEqualityOperator")
expression_PredicateComparisonOperator = Class(name="expression::PredicateComparisonOperator")
expression_PredicateInOperator = Class(name="expression::PredicateInOperator")
expression_PredicateIsOperator = Class(name="expression::PredicateIsOperator")
expression_PredicateLikeOperator = Class(name="expression::PredicateLikeOperator")
expression_PredicateIsEmpty = Class(name="expression::PredicateIsEmpty")
expression_PredicateIsNull = Class(name="expression::PredicateIsNull")

# expression_Expression class attributes and methods
expression_Expression_suffixes: Property = Property(name="suffixes", type=StringType)
expression_Expression.attributes={expression_Expression_suffixes}

# expression_Literal class attributes and methods

# expression_NullLiteral class attributes and methods

# Literal class attributes and methods

# expression_BooleanLiteral class attributes and methods
expression_BooleanLiteral_value: Property = Property(name="value", type=BooleanType)
expression_BooleanLiteral.attributes={expression_BooleanLiteral_value}

# expression_IntegerLiteral class attributes and methods
expression_IntegerLiteral_value: Property = Property(name="value", type=IntegerType)
expression_IntegerLiteral.attributes={expression_IntegerLiteral_value}

# expression_StringLiteral class attributes and methods
expression_StringLiteral_value: Property = Property(name="value", type=StringType)
expression_StringLiteral.attributes={expression_StringLiteral_value}

# expression_TimeLiteral class attributes and methods
expression_TimeLiteral_value: Property = Property(name="value", type=StringType)
expression_TimeLiteral.attributes={expression_TimeLiteral_value}

# expression_Variable class attributes and methods

# expression_Predicate class attributes and methods
expression_Predicate_negated: Property = Property(name="negated", type=BooleanType)
expression_Predicate.attributes={expression_Predicate_negated}

# expression_PredicateBooleanOperator class attributes and methods
expression_PredicateBooleanOperator_operator: Property = Property(name="operator", type=StringType)
expression_PredicateBooleanOperator.attributes={expression_PredicateBooleanOperator_operator}

# Predicate class attributes and methods

# Expression class attributes and methods

# expression_PredicateEqualityOperator class attributes and methods

# expression_PredicateComparisonOperator class attributes and methods
expression_PredicateComparisonOperator_operator: Property = Property(name="operator", type=StringType)
expression_PredicateComparisonOperator.attributes={expression_PredicateComparisonOperator_operator}

# expression_PredicateInOperator class attributes and methods

# expression_PredicateIsOperator class attributes and methods

# expression_PredicateLikeOperator class attributes and methods

# expression_PredicateIsEmpty class attributes and methods

# expression_PredicateIsNull class attributes and methods

# Relationships
expressions0: BinaryAssociation = BinaryAssociation(
    name="expressions0",
    ends={
        Property(name="expression_Predicate", type=expression_PredicateBooleanOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_PredicateBooleanOperator", type=expression_Predicate, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
left1: BinaryAssociation = BinaryAssociation(
    name="left1",
    ends={
        Property(name="expression_Expression", type=expression_PredicateEqualityOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_PredicateEqualityOperator", type=expression_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right2: BinaryAssociation = BinaryAssociation(
    name="right2",
    ends={
        Property(name="expression_Expression4", type=expression_PredicateEqualityOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_PredicateEqualityOperator3", type=expression_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
left5: BinaryAssociation = BinaryAssociation(
    name="left5",
    ends={
        Property(name="expression_Expression6", type=expression_PredicateComparisonOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_PredicateComparisonOperator", type=expression_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right7: BinaryAssociation = BinaryAssociation(
    name="right7",
    ends={
        Property(name="expression_Expression9", type=expression_PredicateComparisonOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_PredicateComparisonOperator8", type=expression_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
left10: BinaryAssociation = BinaryAssociation(
    name="left10",
    ends={
        Property(name="expression_Expression11", type=expression_PredicateInOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_PredicateInOperator", type=expression_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right12: BinaryAssociation = BinaryAssociation(
    name="right12",
    ends={
        Property(name="expression_Expression14", type=expression_PredicateInOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_PredicateInOperator13", type=expression_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
left15: BinaryAssociation = BinaryAssociation(
    name="left15",
    ends={
        Property(name="expression_PredicateIsOperator", type=expression_Expression, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="expression_Expression16", type=expression_PredicateIsOperator, multiplicity=Multiplicity(1, 1))
    }
)
right17: BinaryAssociation = BinaryAssociation(
    name="right17",
    ends={
        Property(name="expression_Expression19", type=expression_PredicateIsOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_PredicateIsOperator18", type=expression_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
left20: BinaryAssociation = BinaryAssociation(
    name="left20",
    ends={
        Property(name="expression_Expression21", type=expression_PredicateLikeOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_PredicateLikeOperator", type=expression_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right22: BinaryAssociation = BinaryAssociation(
    name="right22",
    ends={
        Property(name="expression_Expression24", type=expression_PredicateLikeOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_PredicateLikeOperator23", type=expression_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
feature25: BinaryAssociation = BinaryAssociation(
    name="feature25",
    ends={
        Property(name="expression_Variable", type=expression_PredicateIsEmpty, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_PredicateIsEmpty", type=expression_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
feature26: BinaryAssociation = BinaryAssociation(
    name="feature26",
    ends={
        Property(name="expression_Variable27", type=expression_PredicateIsNull, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_PredicateIsNull", type=expression_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_expression_NullLiteral_Literal = Generalization(general=Literal, specific=expression_NullLiteral)
gen_expression_BooleanLiteral_Literal = Generalization(general=Literal, specific=expression_BooleanLiteral)
gen_expression_IntegerLiteral_Literal = Generalization(general=Literal, specific=expression_IntegerLiteral)
gen_expression_StringLiteral_Literal = Generalization(general=Literal, specific=expression_StringLiteral)
gen_expression_TimeLiteral_Literal = Generalization(general=Literal, specific=expression_TimeLiteral)
gen_expression_Variable_Expression = Generalization(general=Expression, specific=expression_Variable)
gen_expression_Predicate_Expression = Generalization(general=Expression, specific=expression_Predicate)
gen_expression_PredicateBooleanOperator_Predicate = Generalization(general=Predicate, specific=expression_PredicateBooleanOperator)
gen_expression_Literal_Expression = Generalization(general=Expression, specific=expression_Literal)
gen_expression_PredicateEqualityOperator_Predicate = Generalization(general=Predicate, specific=expression_PredicateEqualityOperator)
gen_expression_PredicateComparisonOperator_Predicate = Generalization(general=Predicate, specific=expression_PredicateComparisonOperator)
gen_expression_PredicateInOperator_Predicate = Generalization(general=Predicate, specific=expression_PredicateInOperator)
gen_expression_PredicateIsOperator_Predicate = Generalization(general=Predicate, specific=expression_PredicateIsOperator)
gen_expression_PredicateLikeOperator_Predicate = Generalization(general=Predicate, specific=expression_PredicateLikeOperator)
gen_expression_PredicateIsEmpty_Predicate = Generalization(general=Predicate, specific=expression_PredicateIsEmpty)
gen_expression_PredicateIsNull_Predicate = Generalization(general=Predicate, specific=expression_PredicateIsNull)

# Domain Model
domain_model = DomainModel(
    name="expression",
    types={expression_Expression, expression_Literal, expression_NullLiteral, Literal, expression_BooleanLiteral, expression_IntegerLiteral, expression_StringLiteral, expression_TimeLiteral, expression_Variable, expression_Predicate, expression_PredicateBooleanOperator, Predicate, Expression, expression_PredicateEqualityOperator, expression_PredicateComparisonOperator, expression_PredicateInOperator, expression_PredicateIsOperator, expression_PredicateLikeOperator, expression_PredicateIsEmpty, expression_PredicateIsNull, BooleanOperator, ComparisionOperator},
    associations={expressions0, left1, right2, left5, right7, left10, right12, left15, right17, left20, right22, feature25, feature26},
    generalizations={gen_expression_NullLiteral_Literal, gen_expression_BooleanLiteral_Literal, gen_expression_IntegerLiteral_Literal, gen_expression_StringLiteral_Literal, gen_expression_TimeLiteral_Literal, gen_expression_Variable_Expression, gen_expression_Predicate_Expression, gen_expression_PredicateBooleanOperator_Predicate, gen_expression_Literal_Expression, gen_expression_PredicateEqualityOperator_Predicate, gen_expression_PredicateComparisonOperator_Predicate, gen_expression_PredicateInOperator_Predicate, gen_expression_PredicateIsOperator_Predicate, gen_expression_PredicateLikeOperator_Predicate, gen_expression_PredicateIsEmpty_Predicate, gen_expression_PredicateIsNull_Predicate},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)