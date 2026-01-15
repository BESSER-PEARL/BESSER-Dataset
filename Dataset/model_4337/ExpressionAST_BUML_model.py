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
ArithmeticOperator: Enumeration = Enumeration(
    name="ArithmeticOperator",
    literals={
            EnumerationLiteral(name="Add"),
			EnumerationLiteral(name="Subtract"),
			EnumerationLiteral(name="Multiply"),
			EnumerationLiteral(name="Divide")
    }
)

# Classes
ast_Model = Class(name="ast::Model")
ast_Expression = Class(name="ast::Expression", is_abstract=True)
ast_Operator = Class(name="ast::Operator")
Expression = Class(name="Expression")
ast_Operand = Class(name="ast::Operand", is_abstract=True)
ast_Variable = Class(name="ast::Variable")
Operand = Class(name="Operand")
ast_Number = Class(name="ast::Number")

# ast_Model class attributes and methods

# ast_Expression class attributes and methods
ast_Expression_incrementalID: Property = Property(name="incrementalID", type=StringType)
ast_Expression.attributes={ast_Expression_incrementalID}

# ast_Operator class attributes and methods
ast_Operator_op: Property = Property(name="op", type=StringType)
ast_Operator.attributes={ast_Operator_op}

# Expression class attributes and methods

# ast_Operand class attributes and methods

# ast_Variable class attributes and methods
ast_Variable_name: Property = Property(name="name", type=StringType)
ast_Variable.attributes={ast_Variable_name}

# Operand class attributes and methods

# ast_Number class attributes and methods
ast_Number_value: Property = Property(name="value", type=IntegerType)
ast_Number.attributes={ast_Number_value}

# Relationships
expr0: BinaryAssociation = BinaryAssociation(
    name="expr0",
    ends={
        Property(name="Expression", type=ast_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="model", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
model1: BinaryAssociation = BinaryAssociation(
    name="model1",
    ends={
        Property(name="Model", type=ast_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="expr", type=ast_Model, multiplicity=Multiplicity(0, 1))
    }
)
leftInverse2: BinaryAssociation = BinaryAssociation(
    name="leftInverse2",
    ends={
        Property(name="Operator", type=ast_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="left", type=ast_Operator, multiplicity=Multiplicity(0, 1))
    }
)
rightInverse3: BinaryAssociation = BinaryAssociation(
    name="rightInverse3",
    ends={
        Property(name="Operator4", type=ast_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="right", type=ast_Operator, multiplicity=Multiplicity(0, 1))
    }
)
left5: BinaryAssociation = BinaryAssociation(
    name="left5",
    ends={
        Property(name="Expression6", type=ast_Operator, multiplicity=Multiplicity(1, 1)),
        Property(name="leftInverse", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right7: BinaryAssociation = BinaryAssociation(
    name="right7",
    ends={
        Property(name="Expression8", type=ast_Operator, multiplicity=Multiplicity(1, 1)),
        Property(name="rightInverse", type=ast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_ast_Operator_Expression = Generalization(general=Expression, specific=ast_Operator)
gen_ast_Operand_Expression = Generalization(general=Expression, specific=ast_Operand)
gen_ast_Variable_Operand = Generalization(general=Operand, specific=ast_Variable)
gen_ast_Number_Operand = Generalization(general=Operand, specific=ast_Number)

# Domain Model
domain_model = DomainModel(
    name="ast",
    types={ast_Model, ast_Expression, ast_Operator, Expression, ast_Operand, ast_Variable, Operand, ast_Number, ArithmeticOperator},
    associations={expr0, model1, leftInverse2, rightInverse3, left5, right7},
    generalizations={gen_ast_Operator_Expression, gen_ast_Operand_Expression, gen_ast_Variable_Operand, gen_ast_Number_Operand},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)