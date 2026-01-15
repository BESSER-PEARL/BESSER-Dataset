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
simpleExpressions_IfCondition = Class(name="simpleExpressions::IfCondition")
simpleExpressions_Expression = Class(name="simpleExpressions::Expression")
simpleExpressions_NumberLiteral = Class(name="simpleExpressions::NumberLiteral")
Expression = Class(name="Expression")
simpleExpressions_MethodCall = Class(name="simpleExpressions::MethodCall")
simpleExpressions_OrExpression = Class(name="simpleExpressions::OrExpression")
simpleExpressions_Comparison = Class(name="simpleExpressions::Comparison")
simpleExpressions_NotExpression = Class(name="simpleExpressions::NotExpression")
simpleExpressions_AndExpression = Class(name="simpleExpressions::AndExpression")

# simpleExpressions_IfCondition class attributes and methods
simpleExpressions_IfCondition_elseif: Property = Property(name="elseif", type=BooleanType)
simpleExpressions_IfCondition.attributes={simpleExpressions_IfCondition_elseif}

# simpleExpressions_Expression class attributes and methods

# simpleExpressions_NumberLiteral class attributes and methods
simpleExpressions_NumberLiteral_value: Property = Property(name="value", type=IntegerType)
simpleExpressions_NumberLiteral.attributes={simpleExpressions_NumberLiteral_value}

# Expression class attributes and methods

# simpleExpressions_MethodCall class attributes and methods
simpleExpressions_MethodCall_value: Property = Property(name="value", type=StringType)
simpleExpressions_MethodCall.attributes={simpleExpressions_MethodCall_value}

# simpleExpressions_OrExpression class attributes and methods

# simpleExpressions_Comparison class attributes and methods
simpleExpressions_Comparison_operator: Property = Property(name="operator", type=StringType)
simpleExpressions_Comparison.attributes={simpleExpressions_Comparison_operator}

# simpleExpressions_NotExpression class attributes and methods

# simpleExpressions_AndExpression class attributes and methods

# Relationships
condition0: BinaryAssociation = BinaryAssociation(
    name="condition0",
    ends={
        Property(name="simpleExpressions_Expression", type=simpleExpressions_IfCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleExpressions_IfCondition", type=simpleExpressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left6: BinaryAssociation = BinaryAssociation(
    name="left6",
    ends={
        Property(name="simpleExpressions_Expression7", type=simpleExpressions_AndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleExpressions_AndExpression", type=simpleExpressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right8: BinaryAssociation = BinaryAssociation(
    name="right8",
    ends={
        Property(name="simpleExpressions_Expression10", type=simpleExpressions_AndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleExpressions_AndExpression9", type=simpleExpressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left11: BinaryAssociation = BinaryAssociation(
    name="left11",
    ends={
        Property(name="simpleExpressions_Expression12", type=simpleExpressions_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleExpressions_Comparison", type=simpleExpressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right13: BinaryAssociation = BinaryAssociation(
    name="right13",
    ends={
        Property(name="simpleExpressions_Expression15", type=simpleExpressions_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleExpressions_Comparison14", type=simpleExpressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression16: BinaryAssociation = BinaryAssociation(
    name="expression16",
    ends={
        Property(name="simpleExpressions_Expression17", type=simpleExpressions_NotExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleExpressions_NotExpression", type=simpleExpressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left1: BinaryAssociation = BinaryAssociation(
    name="left1",
    ends={
        Property(name="simpleExpressions_Expression2", type=simpleExpressions_OrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleExpressions_OrExpression", type=simpleExpressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right3: BinaryAssociation = BinaryAssociation(
    name="right3",
    ends={
        Property(name="simpleExpressions_Expression5", type=simpleExpressions_OrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleExpressions_OrExpression4", type=simpleExpressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_simpleExpressions_NumberLiteral_Expression = Generalization(general=Expression, specific=simpleExpressions_NumberLiteral)
gen_simpleExpressions_MethodCall_Expression = Generalization(general=Expression, specific=simpleExpressions_MethodCall)
gen_simpleExpressions_OrExpression_Expression = Generalization(general=Expression, specific=simpleExpressions_OrExpression)
gen_simpleExpressions_Comparison_Expression = Generalization(general=Expression, specific=simpleExpressions_Comparison)
gen_simpleExpressions_NotExpression_Expression = Generalization(general=Expression, specific=simpleExpressions_NotExpression)
gen_simpleExpressions_AndExpression_Expression = Generalization(general=Expression, specific=simpleExpressions_AndExpression)

# Domain Model
domain_model = DomainModel(
    name="simpleExpressions",
    types={simpleExpressions_IfCondition, simpleExpressions_Expression, simpleExpressions_NumberLiteral, Expression, simpleExpressions_MethodCall, simpleExpressions_OrExpression, simpleExpressions_Comparison, simpleExpressions_NotExpression, simpleExpressions_AndExpression},
    associations={condition0, left6, right8, left11, right13, expression16, left1, right3},
    generalizations={gen_simpleExpressions_NumberLiteral_Expression, gen_simpleExpressions_MethodCall_Expression, gen_simpleExpressions_OrExpression_Expression, gen_simpleExpressions_Comparison_Expression, gen_simpleExpressions_NotExpression_Expression, gen_simpleExpressions_AndExpression_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)