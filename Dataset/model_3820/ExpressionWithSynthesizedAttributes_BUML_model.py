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
Expression = Class(name="Expression")
expression_Expression = Class(name="expression::Expression", is_abstract=True)
expression_IntegerExpression = Class(name="expression::IntegerExpression")
expression_UnaryExpression = Class(name="expression::UnaryExpression")
expression_ExpressionStatement = Class(name="expression::ExpressionStatement")
expression_BinaryExpression = Class(name="expression::BinaryExpression")

# Expression class attributes and methods

# expression_Expression class attributes and methods
expression_Expression_calculatedValue: Property = Property(name="calculatedValue", type=FloatType)
expression_Expression.attributes={expression_Expression_calculatedValue}

# expression_IntegerExpression class attributes and methods
expression_IntegerExpression_value: Property = Property(name="value", type=FloatType)
expression_IntegerExpression.attributes={expression_IntegerExpression_value}

# expression_UnaryExpression class attributes and methods

# expression_ExpressionStatement class attributes and methods

# expression_BinaryExpression class attributes and methods

# Relationships
leftSide0: BinaryAssociation = BinaryAssociation(
    name="leftSide0",
    ends={
        Property(name="expression_Expression", type=expression_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_BinaryExpression", type=expression_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightSide1: BinaryAssociation = BinaryAssociation(
    name="rightSide1",
    ends={
        Property(name="expression_Expression3", type=expression_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_BinaryExpression2", type=expression_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression4: BinaryAssociation = BinaryAssociation(
    name="expression4",
    ends={
        Property(name="expression_Expression5", type=expression_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_UnaryExpression", type=expression_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression6: BinaryAssociation = BinaryAssociation(
    name="expression6",
    ends={
        Property(name="expression_Expression7", type=expression_ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_ExpressionStatement", type=expression_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_expression_BinaryExpression_Expression = Generalization(general=Expression, specific=expression_BinaryExpression)
gen_expression_IntegerExpression_Expression = Generalization(general=Expression, specific=expression_IntegerExpression)
gen_expression_UnaryExpression_Expression = Generalization(general=Expression, specific=expression_UnaryExpression)

# Domain Model
domain_model = DomainModel(
    name="expression",
    types={Expression, expression_Expression, expression_IntegerExpression, expression_UnaryExpression, expression_ExpressionStatement, expression_BinaryExpression},
    associations={leftSide0, rightSide1, expression4, expression6},
    generalizations={gen_expression_BinaryExpression_Expression, gen_expression_IntegerExpression_Expression, gen_expression_UnaryExpression_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)