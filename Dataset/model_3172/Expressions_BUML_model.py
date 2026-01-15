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
expressions_ExpressionsModel = Class(name="expressions::ExpressionsModel")
expressions_And = Class(name="expressions::And")
expressions_Equality = Class(name="expressions::Equality")
expressions_AbstractElement = Class(name="expressions::AbstractElement")
expressions_Expression = Class(name="expressions::Expression")
expressions_Variable = Class(name="expressions::Variable")
AbstractElement = Class(name="AbstractElement")
expressions_EvalExpression = Class(name="expressions::EvalExpression")
expressions_Or = Class(name="expressions::Or")
Expression = Class(name="Expression")
expressions_Minus = Class(name="expressions::Minus")
expressions_MulOrDiv = Class(name="expressions::MulOrDiv")
expressions_Comparison = Class(name="expressions::Comparison")
expressions_Plus = Class(name="expressions::Plus")
expressions_VariableRef = Class(name="expressions::VariableRef")
expressions_Not = Class(name="expressions::Not")
expressions_IntConstant = Class(name="expressions::IntConstant")
expressions_StringConstant = Class(name="expressions::StringConstant")
expressions_BoolConstant = Class(name="expressions::BoolConstant")

# expressions_ExpressionsModel class attributes and methods

# expressions_And class attributes and methods

# expressions_Equality class attributes and methods
expressions_Equality_op: Property = Property(name="op", type=StringType)
expressions_Equality.attributes={expressions_Equality_op}

# expressions_AbstractElement class attributes and methods

# expressions_Expression class attributes and methods

# expressions_Variable class attributes and methods
expressions_Variable_name: Property = Property(name="name", type=StringType)
expressions_Variable.attributes={expressions_Variable_name}

# AbstractElement class attributes and methods

# expressions_EvalExpression class attributes and methods

# expressions_Or class attributes and methods

# Expression class attributes and methods

# expressions_Minus class attributes and methods

# expressions_MulOrDiv class attributes and methods
expressions_MulOrDiv_op: Property = Property(name="op", type=StringType)
expressions_MulOrDiv.attributes={expressions_MulOrDiv_op}

# expressions_Comparison class attributes and methods
expressions_Comparison_op: Property = Property(name="op", type=StringType)
expressions_Comparison.attributes={expressions_Comparison_op}

# expressions_Plus class attributes and methods

# expressions_VariableRef class attributes and methods

# expressions_Not class attributes and methods

# expressions_IntConstant class attributes and methods
expressions_IntConstant_value: Property = Property(name="value", type=IntegerType)
expressions_IntConstant.attributes={expressions_IntConstant_value}

# expressions_StringConstant class attributes and methods
expressions_StringConstant_value: Property = Property(name="value", type=StringType)
expressions_StringConstant.attributes={expressions_StringConstant_value}

# expressions_BoolConstant class attributes and methods
expressions_BoolConstant_value: Property = Property(name="value", type=StringType)
expressions_BoolConstant.attributes={expressions_BoolConstant_value}

# Relationships
right5: BinaryAssociation = BinaryAssociation(
    name="right5",
    ends={
        Property(name="expressions_Or6", type=expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="expressions_Expression7", type=expressions_Or, multiplicity=Multiplicity(1, 1))
    }
)
left8: BinaryAssociation = BinaryAssociation(
    name="left8",
    ends={
        Property(name="expressions_Expression9", type=expressions_And, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_And", type=expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right10: BinaryAssociation = BinaryAssociation(
    name="right10",
    ends={
        Property(name="expressions_Expression12", type=expressions_And, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_And11", type=expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="expressions_AbstractElement", type=expressions_ExpressionsModel, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_ExpressionsModel", type=expressions_AbstractElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression1: BinaryAssociation = BinaryAssociation(
    name="expression1",
    ends={
        Property(name="expressions_Expression", type=expressions_AbstractElement, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_AbstractElement2", type=expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left3: BinaryAssociation = BinaryAssociation(
    name="left3",
    ends={
        Property(name="expressions_Expression4", type=expressions_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_Or", type=expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right25: BinaryAssociation = BinaryAssociation(
    name="right25",
    ends={
        Property(name="expressions_Expression27", type=expressions_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_Plus26", type=expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left28: BinaryAssociation = BinaryAssociation(
    name="left28",
    ends={
        Property(name="expressions_Expression29", type=expressions_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_Minus", type=expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right30: BinaryAssociation = BinaryAssociation(
    name="right30",
    ends={
        Property(name="expressions_Expression32", type=expressions_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_Minus31", type=expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left13: BinaryAssociation = BinaryAssociation(
    name="left13",
    ends={
        Property(name="expressions_Expression14", type=expressions_Equality, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_Equality", type=expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right15: BinaryAssociation = BinaryAssociation(
    name="right15",
    ends={
        Property(name="expressions_Expression17", type=expressions_Equality, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_Equality16", type=expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left18: BinaryAssociation = BinaryAssociation(
    name="left18",
    ends={
        Property(name="expressions_Expression19", type=expressions_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_Comparison", type=expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right20: BinaryAssociation = BinaryAssociation(
    name="right20",
    ends={
        Property(name="expressions_Expression22", type=expressions_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_Comparison21", type=expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left23: BinaryAssociation = BinaryAssociation(
    name="left23",
    ends={
        Property(name="expressions_Expression24", type=expressions_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_Plus", type=expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable40: BinaryAssociation = BinaryAssociation(
    name="variable40",
    ends={
        Property(name="expressions_Variable", type=expressions_VariableRef, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_VariableRef", type=expressions_Variable, multiplicity=Multiplicity(0, 1))
    }
)
left33: BinaryAssociation = BinaryAssociation(
    name="left33",
    ends={
        Property(name="expressions_Expression34", type=expressions_MulOrDiv, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_MulOrDiv", type=expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right35: BinaryAssociation = BinaryAssociation(
    name="right35",
    ends={
        Property(name="expressions_Expression37", type=expressions_MulOrDiv, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_MulOrDiv36", type=expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression38: BinaryAssociation = BinaryAssociation(
    name="expression38",
    ends={
        Property(name="expressions_Expression39", type=expressions_Not, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_Not", type=expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_expressions_And_Expression = Generalization(general=Expression, specific=expressions_And)
gen_expressions_Equality_Expression = Generalization(general=Expression, specific=expressions_Equality)
gen_expressions_Variable_AbstractElement = Generalization(general=AbstractElement, specific=expressions_Variable)
gen_expressions_EvalExpression_AbstractElement = Generalization(general=AbstractElement, specific=expressions_EvalExpression)
gen_expressions_Or_Expression = Generalization(general=Expression, specific=expressions_Or)
gen_expressions_Minus_Expression = Generalization(general=Expression, specific=expressions_Minus)
gen_expressions_MulOrDiv_Expression = Generalization(general=Expression, specific=expressions_MulOrDiv)
gen_expressions_Comparison_Expression = Generalization(general=Expression, specific=expressions_Comparison)
gen_expressions_Plus_Expression = Generalization(general=Expression, specific=expressions_Plus)
gen_expressions_VariableRef_Expression = Generalization(general=Expression, specific=expressions_VariableRef)
gen_expressions_Not_Expression = Generalization(general=Expression, specific=expressions_Not)
gen_expressions_IntConstant_Expression = Generalization(general=Expression, specific=expressions_IntConstant)
gen_expressions_StringConstant_Expression = Generalization(general=Expression, specific=expressions_StringConstant)
gen_expressions_BoolConstant_Expression = Generalization(general=Expression, specific=expressions_BoolConstant)

# Domain Model
domain_model = DomainModel(
    name="expressions",
    types={expressions_ExpressionsModel, expressions_And, expressions_Equality, expressions_AbstractElement, expressions_Expression, expressions_Variable, AbstractElement, expressions_EvalExpression, expressions_Or, Expression, expressions_Minus, expressions_MulOrDiv, expressions_Comparison, expressions_Plus, expressions_VariableRef, expressions_Not, expressions_IntConstant, expressions_StringConstant, expressions_BoolConstant},
    associations={right5, left8, right10, elements0, expression1, left3, right25, left28, right30, left13, right15, left18, right20, left23, variable40, left33, right35, expression38},
    generalizations={gen_expressions_And_Expression, gen_expressions_Equality_Expression, gen_expressions_Variable_AbstractElement, gen_expressions_EvalExpression_AbstractElement, gen_expressions_Or_Expression, gen_expressions_Minus_Expression, gen_expressions_MulOrDiv_Expression, gen_expressions_Comparison_Expression, gen_expressions_Plus_Expression, gen_expressions_VariableRef_Expression, gen_expressions_Not_Expression, gen_expressions_IntConstant_Expression, gen_expressions_StringConstant_Expression, gen_expressions_BoolConstant_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)