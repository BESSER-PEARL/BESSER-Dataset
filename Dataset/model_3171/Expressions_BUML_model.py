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
expressions_AbstractElement = Class(name="expressions::AbstractElement")
expressions_Variable = Class(name="expressions::Variable")
AbstractElement = Class(name="AbstractElement")
expressions_Expression = Class(name="expressions::Expression")
expressions_Or = Class(name="expressions::Or")
Expression = Class(name="Expression")
expressions_And = Class(name="expressions::And")
expressions_Minus = Class(name="expressions::Minus")
expressions_Equality = Class(name="expressions::Equality")
expressions_Comparison = Class(name="expressions::Comparison")
expressions_Plus = Class(name="expressions::Plus")
expressions_BoolConstant = Class(name="expressions::BoolConstant")
expressions_MulOrDiv = Class(name="expressions::MulOrDiv")
expressions_Not = Class(name="expressions::Not")
expressions_IntConstant = Class(name="expressions::IntConstant")
expressions_StringConstant = Class(name="expressions::StringConstant")
expressions_VariableRef = Class(name="expressions::VariableRef")

# expressions_ExpressionsModel class attributes and methods

# expressions_AbstractElement class attributes and methods

# expressions_Variable class attributes and methods
expressions_Variable_name: Property = Property(name="name", type=StringType)
expressions_Variable.attributes={expressions_Variable_name}

# AbstractElement class attributes and methods

# expressions_Expression class attributes and methods

# expressions_Or class attributes and methods

# Expression class attributes and methods

# expressions_And class attributes and methods

# expressions_Minus class attributes and methods

# expressions_Equality class attributes and methods
expressions_Equality_op: Property = Property(name="op", type=StringType)
expressions_Equality.attributes={expressions_Equality_op}

# expressions_Comparison class attributes and methods
expressions_Comparison_op: Property = Property(name="op", type=StringType)
expressions_Comparison.attributes={expressions_Comparison_op}

# expressions_Plus class attributes and methods

# expressions_BoolConstant class attributes and methods
expressions_BoolConstant_value: Property = Property(name="value", type=StringType)
expressions_BoolConstant.attributes={expressions_BoolConstant_value}

# expressions_MulOrDiv class attributes and methods
expressions_MulOrDiv_op: Property = Property(name="op", type=StringType)
expressions_MulOrDiv.attributes={expressions_MulOrDiv_op}

# expressions_Not class attributes and methods

# expressions_IntConstant class attributes and methods
expressions_IntConstant_value: Property = Property(name="value", type=IntegerType)
expressions_IntConstant.attributes={expressions_IntConstant_value}

# expressions_StringConstant class attributes and methods
expressions_StringConstant_value: Property = Property(name="value", type=StringType)
expressions_StringConstant.attributes={expressions_StringConstant_value}

# expressions_VariableRef class attributes and methods

# Relationships
right9: BinaryAssociation = BinaryAssociation(
    name="right9",
    ends={
        Property(name="expressions_Expression11", type=expressions_And, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_And10", type=expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
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
        Property(name="expressions_Expression", type=expressions_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_Variable", type=expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left2: BinaryAssociation = BinaryAssociation(
    name="left2",
    ends={
        Property(name="expressions_Expression3", type=expressions_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_Or", type=expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right4: BinaryAssociation = BinaryAssociation(
    name="right4",
    ends={
        Property(name="expressions_Expression6", type=expressions_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_Or5", type=expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left7: BinaryAssociation = BinaryAssociation(
    name="left7",
    ends={
        Property(name="expressions_Expression8", type=expressions_And, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_And", type=expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left27: BinaryAssociation = BinaryAssociation(
    name="left27",
    ends={
        Property(name="expressions_Expression28", type=expressions_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_Minus", type=expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left12: BinaryAssociation = BinaryAssociation(
    name="left12",
    ends={
        Property(name="expressions_Expression13", type=expressions_Equality, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_Equality", type=expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right14: BinaryAssociation = BinaryAssociation(
    name="right14",
    ends={
        Property(name="expressions_Expression16", type=expressions_Equality, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_Equality15", type=expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left17: BinaryAssociation = BinaryAssociation(
    name="left17",
    ends={
        Property(name="expressions_Expression18", type=expressions_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_Comparison", type=expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right19: BinaryAssociation = BinaryAssociation(
    name="right19",
    ends={
        Property(name="expressions_Expression21", type=expressions_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_Comparison20", type=expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left22: BinaryAssociation = BinaryAssociation(
    name="left22",
    ends={
        Property(name="expressions_Expression23", type=expressions_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_Plus", type=expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right24: BinaryAssociation = BinaryAssociation(
    name="right24",
    ends={
        Property(name="expressions_Expression26", type=expressions_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_Plus25", type=expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right29: BinaryAssociation = BinaryAssociation(
    name="right29",
    ends={
        Property(name="expressions_Expression31", type=expressions_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_Minus30", type=expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left32: BinaryAssociation = BinaryAssociation(
    name="left32",
    ends={
        Property(name="expressions_Expression33", type=expressions_MulOrDiv, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_MulOrDiv", type=expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right34: BinaryAssociation = BinaryAssociation(
    name="right34",
    ends={
        Property(name="expressions_Expression36", type=expressions_MulOrDiv, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_MulOrDiv35", type=expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression37: BinaryAssociation = BinaryAssociation(
    name="expression37",
    ends={
        Property(name="expressions_Expression38", type=expressions_Not, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_Not", type=expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable39: BinaryAssociation = BinaryAssociation(
    name="variable39",
    ends={
        Property(name="expressions_Variable40", type=expressions_VariableRef, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_VariableRef", type=expressions_Variable, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_expressions_Variable_AbstractElement = Generalization(general=AbstractElement, specific=expressions_Variable)
gen_expressions_Expression_AbstractElement = Generalization(general=AbstractElement, specific=expressions_Expression)
gen_expressions_Or_Expression = Generalization(general=Expression, specific=expressions_Or)
gen_expressions_And_Expression = Generalization(general=Expression, specific=expressions_And)
gen_expressions_Minus_Expression = Generalization(general=Expression, specific=expressions_Minus)
gen_expressions_Equality_Expression = Generalization(general=Expression, specific=expressions_Equality)
gen_expressions_Comparison_Expression = Generalization(general=Expression, specific=expressions_Comparison)
gen_expressions_Plus_Expression = Generalization(general=Expression, specific=expressions_Plus)
gen_expressions_BoolConstant_Expression = Generalization(general=Expression, specific=expressions_BoolConstant)
gen_expressions_MulOrDiv_Expression = Generalization(general=Expression, specific=expressions_MulOrDiv)
gen_expressions_Not_Expression = Generalization(general=Expression, specific=expressions_Not)
gen_expressions_IntConstant_Expression = Generalization(general=Expression, specific=expressions_IntConstant)
gen_expressions_StringConstant_Expression = Generalization(general=Expression, specific=expressions_StringConstant)
gen_expressions_VariableRef_Expression = Generalization(general=Expression, specific=expressions_VariableRef)

# Domain Model
domain_model = DomainModel(
    name="expressions",
    types={expressions_ExpressionsModel, expressions_AbstractElement, expressions_Variable, AbstractElement, expressions_Expression, expressions_Or, Expression, expressions_And, expressions_Minus, expressions_Equality, expressions_Comparison, expressions_Plus, expressions_BoolConstant, expressions_MulOrDiv, expressions_Not, expressions_IntConstant, expressions_StringConstant, expressions_VariableRef},
    associations={right9, elements0, expression1, left2, right4, left7, left27, left12, right14, left17, right19, left22, right24, right29, left32, right34, expression37, variable39},
    generalizations={gen_expressions_Variable_AbstractElement, gen_expressions_Expression_AbstractElement, gen_expressions_Or_Expression, gen_expressions_And_Expression, gen_expressions_Minus_Expression, gen_expressions_Equality_Expression, gen_expressions_Comparison_Expression, gen_expressions_Plus_Expression, gen_expressions_BoolConstant_Expression, gen_expressions_MulOrDiv_Expression, gen_expressions_Not_Expression, gen_expressions_IntConstant_Expression, gen_expressions_StringConstant_Expression, gen_expressions_VariableRef_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)