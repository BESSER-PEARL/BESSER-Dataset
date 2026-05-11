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
Operator: Enumeration = Enumeration(
    name="Operator",
    literals={
            EnumerationLiteral(name="PLUS"),
			EnumerationLiteral(name="MINUS"),
			EnumerationLiteral(name="TIMES"),
			EnumerationLiteral(name="LESS_THAN_OR_EQUAL_TO"),
			EnumerationLiteral(name="GREATER_THAN_OR_EQUAL_TO"),
			EnumerationLiteral(name="EQUAL_TO")
    }
)

ILPDataType: Enumeration = Enumeration(
    name="ILPDataType",
    literals={
            EnumerationLiteral(name="BINARY"),
			EnumerationLiteral(name="INTEGER"),
			EnumerationLiteral(name="REAL")
    }
)

ObjectiveGoal: Enumeration = Enumeration(
    name="ObjectiveGoal",
    literals={
            EnumerationLiteral(name="MIN"),
			EnumerationLiteral(name="MAX")
    }
)

# Classes
ilp_IntegerLinearProgram = Class(name="ilp_IntegerLinearProgram")
ilp_LiteralExpression = Class(name="ilp_LiteralExpression")
Expression = Class(name="Expression")
ilp_BinaryExpression = Class(name="ilp_BinaryExpression", is_abstract=True)
ilp_Variable = Class(name="ilp_Variable")
ilp_ConstraintExpression = Class(name="ilp_ConstraintExpression")
ilp_ObjectiveFunctionExpression = Class(name="ilp_ObjectiveFunctionExpression")
ilp_Expression = Class(name="ilp_Expression", is_abstract=True)
BinaryExpression = Class(name="BinaryExpression")
ilp_ArithmeticExpression = Class(name="ilp_ArithmeticExpression")
ilp_VariableExpression = Class(name="ilp_VariableExpression")

# ilp_IntegerLinearProgram class attributes and methods

# ilp_LiteralExpression class attributes and methods
ilp_LiteralExpression_value: Property = Property(name="value", type=StringType)
ilp_LiteralExpression.attributes={ilp_LiteralExpression_value}

# Expression class attributes and methods

# ilp_BinaryExpression class attributes and methods
ilp_BinaryExpression_operator: Property = Property(name="operator", type=StringType)
ilp_BinaryExpression.attributes={ilp_BinaryExpression_operator}

# ilp_Variable class attributes and methods
ilp_Variable_dataType: Property = Property(name="dataType", type=StringType)
ilp_Variable_name: Property = Property(name="name", type=StringType)
ilp_Variable.attributes={ilp_Variable_dataType, ilp_Variable_name}

# ilp_ConstraintExpression class attributes and methods

# ilp_ObjectiveFunctionExpression class attributes and methods
ilp_ObjectiveFunctionExpression_goal: Property = Property(name="goal", type=StringType)
ilp_ObjectiveFunctionExpression.attributes={ilp_ObjectiveFunctionExpression_goal}

# ilp_Expression class attributes and methods
ilp_Expression_comment: Property = Property(name="comment", type=StringType)
ilp_Expression.attributes={ilp_Expression_comment}

# BinaryExpression class attributes and methods

# ilp_ArithmeticExpression class attributes and methods

# ilp_VariableExpression class attributes and methods

# Relationships
variables0: BinaryAssociation = BinaryAssociation(
    name="variables0",
    ends={
        Property(name="ilp_Variable", type=ilp_IntegerLinearProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="ilp_IntegerLinearProgram", type=ilp_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constraints1: BinaryAssociation = BinaryAssociation(
    name="constraints1",
    ends={
        Property(name="ilp_ConstraintExpression", type=ilp_IntegerLinearProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="ilp_IntegerLinearProgram2", type=ilp_ConstraintExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
objectiveFunction3: BinaryAssociation = BinaryAssociation(
    name="objectiveFunction3",
    ends={
        Property(name="ilp_ObjectiveFunctionExpression", type=ilp_IntegerLinearProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="ilp_IntegerLinearProgram4", type=ilp_ObjectiveFunctionExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
objectiveFunction11: BinaryAssociation = BinaryAssociation(
    name="objectiveFunction11",
    ends={
        Property(name="ilp_Expression13", type=ilp_ObjectiveFunctionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ilp_ObjectiveFunctionExpression12", type=ilp_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftExpression5: BinaryAssociation = BinaryAssociation(
    name="leftExpression5",
    ends={
        Property(name="ilp_Expression", type=ilp_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ilp_BinaryExpression", type=ilp_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightExpression6: BinaryAssociation = BinaryAssociation(
    name="rightExpression6",
    ends={
        Property(name="ilp_Expression8", type=ilp_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ilp_BinaryExpression7", type=ilp_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable9: BinaryAssociation = BinaryAssociation(
    name="variable9",
    ends={
        Property(name="ilp_Variable10", type=ilp_VariableExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ilp_VariableExpression", type=ilp_Variable, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_ilp_LiteralExpression_Expression = Generalization(general=Expression, specific=ilp_LiteralExpression)
gen_ilp_BinaryExpression_Expression = Generalization(general=Expression, specific=ilp_BinaryExpression)
gen_ilp_ConstraintExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=ilp_ConstraintExpression)
gen_ilp_ArithmeticExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=ilp_ArithmeticExpression)
gen_ilp_VariableExpression_Expression = Generalization(general=Expression, specific=ilp_VariableExpression)

# Domain Model
domain_model = DomainModel(
    name="ilp",
    types={ilp_IntegerLinearProgram, ilp_LiteralExpression, Expression, ilp_BinaryExpression, ilp_Variable, ilp_ConstraintExpression, ilp_ObjectiveFunctionExpression, ilp_Expression, BinaryExpression, ilp_ArithmeticExpression, ilp_VariableExpression, Operator, ILPDataType, ObjectiveGoal},
    associations={variables0, constraints1, objectiveFunction3, objectiveFunction11, leftExpression5, rightExpression6, variable9},
    generalizations={gen_ilp_LiteralExpression_Expression, gen_ilp_BinaryExpression_Expression, gen_ilp_ConstraintExpression_BinaryExpression, gen_ilp_ArithmeticExpression_BinaryExpression, gen_ilp_VariableExpression_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)