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
arithmetic_Expression = Class(name="arithmetic::Expression")
arithmetic_AbstractDefinition = Class(name="arithmetic::AbstractDefinition")
arithmetic_Evaluation = Class(name="arithmetic::Evaluation")
arithmetic_SumExpression = Class(name="arithmetic::SumExpression")
Expression = Class(name="Expression")
arithmetic_Module = Class(name="arithmetic::Module")
arithmetic_Import = Class(name="arithmetic::Import")
arithmetic_Statement = Class(name="arithmetic::Statement")
arithmetic_Definition = Class(name="arithmetic::Definition")
Statement = Class(name="Statement")
AbstractDefinition = Class(name="AbstractDefinition")
arithmetic_DeclaredParameter = Class(name="arithmetic::DeclaredParameter")
arithmetic_Plus = Class(name="arithmetic::Plus")
arithmetic_Minus = Class(name="arithmetic::Minus")
arithmetic_Multi = Class(name="arithmetic::Multi")
arithmetic_Div = Class(name="arithmetic::Div")
arithmetic_NumberLiteral = Class(name="arithmetic::NumberLiteral")
arithmetic_FunctionCall = Class(name="arithmetic::FunctionCall")

# arithmetic_Expression class attributes and methods

# arithmetic_AbstractDefinition class attributes and methods
arithmetic_AbstractDefinition_name: Property = Property(name="name", type=StringType)
arithmetic_AbstractDefinition.attributes={arithmetic_AbstractDefinition_name}

# arithmetic_Evaluation class attributes and methods

# arithmetic_SumExpression class attributes and methods
arithmetic_SumExpression_lower: Property = Property(name="lower", type=IntegerType)
arithmetic_SumExpression_upper: Property = Property(name="upper", type=IntegerType)
arithmetic_SumExpression.attributes={arithmetic_SumExpression_upper, arithmetic_SumExpression_lower}

# Expression class attributes and methods

# arithmetic_Module class attributes and methods
arithmetic_Module_name: Property = Property(name="name", type=StringType)
arithmetic_Module.attributes={arithmetic_Module_name}

# arithmetic_Import class attributes and methods

# arithmetic_Statement class attributes and methods

# arithmetic_Definition class attributes and methods

# Statement class attributes and methods

# AbstractDefinition class attributes and methods

# arithmetic_DeclaredParameter class attributes and methods

# arithmetic_Plus class attributes and methods

# arithmetic_Minus class attributes and methods

# arithmetic_Multi class attributes and methods

# arithmetic_Div class attributes and methods

# arithmetic_NumberLiteral class attributes and methods
arithmetic_NumberLiteral_value: Property = Property(name="value", type=IntegerType)
arithmetic_NumberLiteral.attributes={arithmetic_NumberLiteral_value}

# arithmetic_FunctionCall class attributes and methods

# Relationships
args6: BinaryAssociation = BinaryAssociation(
    name="args6",
    ends={
        Property(name="arithmetic_DeclaredParameter", type=arithmetic_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="arithmetic_Definition", type=arithmetic_DeclaredParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr7: BinaryAssociation = BinaryAssociation(
    name="expr7",
    ends={
        Property(name="arithmetic_Expression", type=arithmetic_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="arithmetic_Definition8", type=arithmetic_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression9: BinaryAssociation = BinaryAssociation(
    name="expression9",
    ends={
        Property(name="arithmetic_Expression10", type=arithmetic_Evaluation, multiplicity=Multiplicity(1, 1)),
        Property(name="arithmetic_Evaluation", type=arithmetic_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
indexVariable11: BinaryAssociation = BinaryAssociation(
    name="indexVariable11",
    ends={
        Property(name="arithmetic_DeclaredParameter12", type=arithmetic_SumExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="arithmetic_SumExpression", type=arithmetic_DeclaredParameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr13: BinaryAssociation = BinaryAssociation(
    name="expr13",
    ends={
        Property(name="arithmetic_Expression15", type=arithmetic_SumExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="arithmetic_SumExpression14", type=arithmetic_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
imports0: BinaryAssociation = BinaryAssociation(
    name="imports0",
    ends={
        Property(name="arithmetic_Import", type=arithmetic_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="arithmetic_Module", type=arithmetic_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements1: BinaryAssociation = BinaryAssociation(
    name="statements1",
    ends={
        Property(name="arithmetic_Statement", type=arithmetic_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="arithmetic_Module2", type=arithmetic_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
module3: BinaryAssociation = BinaryAssociation(
    name="module3",
    ends={
        Property(name="arithmetic_Module5", type=arithmetic_Import, multiplicity=Multiplicity(1, 1)),
        Property(name="arithmetic_Import4", type=arithmetic_Module, multiplicity=Multiplicity(0, 1))
    }
)
func36: BinaryAssociation = BinaryAssociation(
    name="func36",
    ends={
        Property(name="arithmetic_AbstractDefinition", type=arithmetic_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="arithmetic_FunctionCall", type=arithmetic_AbstractDefinition, multiplicity=Multiplicity(0, 1))
    }
)
left16: BinaryAssociation = BinaryAssociation(
    name="left16",
    ends={
        Property(name="arithmetic_Expression17", type=arithmetic_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="arithmetic_Plus", type=arithmetic_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right18: BinaryAssociation = BinaryAssociation(
    name="right18",
    ends={
        Property(name="arithmetic_Expression20", type=arithmetic_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="arithmetic_Plus19", type=arithmetic_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left21: BinaryAssociation = BinaryAssociation(
    name="left21",
    ends={
        Property(name="arithmetic_Expression22", type=arithmetic_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="arithmetic_Minus", type=arithmetic_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right23: BinaryAssociation = BinaryAssociation(
    name="right23",
    ends={
        Property(name="arithmetic_Expression25", type=arithmetic_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="arithmetic_Minus24", type=arithmetic_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left26: BinaryAssociation = BinaryAssociation(
    name="left26",
    ends={
        Property(name="arithmetic_Expression27", type=arithmetic_Multi, multiplicity=Multiplicity(1, 1)),
        Property(name="arithmetic_Multi", type=arithmetic_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right28: BinaryAssociation = BinaryAssociation(
    name="right28",
    ends={
        Property(name="arithmetic_Expression30", type=arithmetic_Multi, multiplicity=Multiplicity(1, 1)),
        Property(name="arithmetic_Multi29", type=arithmetic_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left31: BinaryAssociation = BinaryAssociation(
    name="left31",
    ends={
        Property(name="arithmetic_Expression32", type=arithmetic_Div, multiplicity=Multiplicity(1, 1)),
        Property(name="arithmetic_Div", type=arithmetic_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right33: BinaryAssociation = BinaryAssociation(
    name="right33",
    ends={
        Property(name="arithmetic_Expression35", type=arithmetic_Div, multiplicity=Multiplicity(1, 1)),
        Property(name="arithmetic_Div34", type=arithmetic_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_arithmetic_DeclaredParameter_AbstractDefinition = Generalization(general=AbstractDefinition, specific=arithmetic_DeclaredParameter)
gen_arithmetic_Evaluation_Statement = Generalization(general=Statement, specific=arithmetic_Evaluation)
gen_arithmetic_SumExpression_Expression = Generalization(general=Expression, specific=arithmetic_SumExpression)
gen_arithmetic_Definition_Statement = Generalization(general=Statement, specific=arithmetic_Definition)
gen_arithmetic_Definition_AbstractDefinition = Generalization(general=AbstractDefinition, specific=arithmetic_Definition)
gen_arithmetic_Plus_Expression = Generalization(general=Expression, specific=arithmetic_Plus)
gen_arithmetic_Minus_Expression = Generalization(general=Expression, specific=arithmetic_Minus)
gen_arithmetic_Multi_Expression = Generalization(general=Expression, specific=arithmetic_Multi)
gen_arithmetic_Div_Expression = Generalization(general=Expression, specific=arithmetic_Div)
gen_arithmetic_NumberLiteral_Expression = Generalization(general=Expression, specific=arithmetic_NumberLiteral)
gen_arithmetic_FunctionCall_Expression = Generalization(general=Expression, specific=arithmetic_FunctionCall)

# Domain Model
domain_model = DomainModel(
    name="arithmetic",
    types={arithmetic_Expression, arithmetic_AbstractDefinition, arithmetic_Evaluation, arithmetic_SumExpression, Expression, arithmetic_Module, arithmetic_Import, arithmetic_Statement, arithmetic_Definition, Statement, AbstractDefinition, arithmetic_DeclaredParameter, arithmetic_Plus, arithmetic_Minus, arithmetic_Multi, arithmetic_Div, arithmetic_NumberLiteral, arithmetic_FunctionCall},
    associations={args6, expr7, expression9, indexVariable11, expr13, imports0, statements1, module3, func36, left16, right18, left21, right23, left26, right28, left31, right33},
    generalizations={gen_arithmetic_DeclaredParameter_AbstractDefinition, gen_arithmetic_Evaluation_Statement, gen_arithmetic_SumExpression_Expression, gen_arithmetic_Definition_Statement, gen_arithmetic_Definition_AbstractDefinition, gen_arithmetic_Plus_Expression, gen_arithmetic_Minus_Expression, gen_arithmetic_Multi_Expression, gen_arithmetic_Div_Expression, gen_arithmetic_NumberLiteral_Expression, gen_arithmetic_FunctionCall_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)