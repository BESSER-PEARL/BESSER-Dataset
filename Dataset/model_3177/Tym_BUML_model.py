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
tym_Model = Class(name="tym::Model")
tym_EObject = Class(name="tym::EObject")
tym_AbstractElement = Class(name="tym::AbstractElement")
tym_Variable = Class(name="tym::Variable")
AbstractElement = Class(name="AbstractElement")
tym_Function = Class(name="tym::Function")
tym_FunctionBlock = Class(name="tym::FunctionBlock")
tym_PrintStatement = Class(name="tym::PrintStatement")
tym_TestStatement = Class(name="tym::TestStatement")
tym_Block = Class(name="tym::Block")
tym_Equality = Class(name="tym::Equality")
tym_LoopStatement = Class(name="tym::LoopStatement")
tym_Return = Class(name="tym::Return")
tym_FunctionCall = Class(name="tym::FunctionCall")
tym_Expression = Class(name="tym::Expression")
tym_Or = Class(name="tym::Or")
Expression = Class(name="Expression")
tym_And = Class(name="tym::And")
tym_Not = Class(name="tym::Not")
tym_Comparison = Class(name="tym::Comparison")
tym_Plus = Class(name="tym::Plus")
tym_Minus = Class(name="tym::Minus")
tym_MulOrDiv = Class(name="tym::MulOrDiv")
tym_IntConstant = Class(name="tym::IntConstant")
tym_StringConstant = Class(name="tym::StringConstant")
tym_BoolConstant = Class(name="tym::BoolConstant")
tym_VariableRef = Class(name="tym::VariableRef")

# tym_Model class attributes and methods

# tym_EObject class attributes and methods

# tym_AbstractElement class attributes and methods

# tym_Variable class attributes and methods
tym_Variable_vartype: Property = Property(name="vartype", type=StringType)
tym_Variable_name: Property = Property(name="name", type=StringType)
tym_Variable.attributes={tym_Variable_name, tym_Variable_vartype}

# AbstractElement class attributes and methods

# tym_Function class attributes and methods
tym_Function_return: Property = Property(name="return", type=StringType)
tym_Function_name: Property = Property(name="name", type=StringType)
tym_Function.attributes={tym_Function_name, tym_Function_return}

# tym_FunctionBlock class attributes and methods

# tym_PrintStatement class attributes and methods

# tym_TestStatement class attributes and methods

# tym_Block class attributes and methods

# tym_Equality class attributes and methods
tym_Equality_op: Property = Property(name="op", type=StringType)
tym_Equality.attributes={tym_Equality_op}

# tym_LoopStatement class attributes and methods

# tym_Return class attributes and methods

# tym_FunctionCall class attributes and methods

# tym_Expression class attributes and methods

# tym_Or class attributes and methods

# Expression class attributes and methods

# tym_And class attributes and methods

# tym_Not class attributes and methods

# tym_Comparison class attributes and methods
tym_Comparison_op: Property = Property(name="op", type=StringType)
tym_Comparison.attributes={tym_Comparison_op}

# tym_Plus class attributes and methods

# tym_Minus class attributes and methods

# tym_MulOrDiv class attributes and methods
tym_MulOrDiv_op: Property = Property(name="op", type=StringType)
tym_MulOrDiv.attributes={tym_MulOrDiv_op}

# tym_IntConstant class attributes and methods
tym_IntConstant_value: Property = Property(name="value", type=IntegerType)
tym_IntConstant.attributes={tym_IntConstant_value}

# tym_StringConstant class attributes and methods
tym_StringConstant_value: Property = Property(name="value", type=StringType)
tym_StringConstant.attributes={tym_StringConstant_value}

# tym_BoolConstant class attributes and methods
tym_BoolConstant_value: Property = Property(name="value", type=StringType)
tym_BoolConstant.attributes={tym_BoolConstant_value}

# tym_VariableRef class attributes and methods

# Relationships
thenBlock14: BinaryAssociation = BinaryAssociation(
    name="thenBlock14",
    ends={
        Property(name="tym_Block", type=tym_TestStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="tym_TestStatement15", type=tym_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseBlock16: BinaryAssociation = BinaryAssociation(
    name="elseBlock16",
    ends={
        Property(name="tym_Block18", type=tym_TestStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="tym_TestStatement17", type=tym_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elements19: BinaryAssociation = BinaryAssociation(
    name="elements19",
    ends={
        Property(name="tym_AbstractElement", type=tym_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="tym_Block20", type=tym_AbstractElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="tym_EObject", type=tym_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="tym_Model", type=tym_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable2: BinaryAssociation = BinaryAssociation(
    name="variable2",
    ends={
        Property(name="tym_Variable", type=tym_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="tym_Variable1", type=tym_Variable, multiplicity=Multiplicity(0, 1))
    }
)
expression3: BinaryAssociation = BinaryAssociation(
    name="expression3",
    ends={
        Property(name="tym_EObject5", type=tym_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="tym_Variable4", type=tym_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
params6: BinaryAssociation = BinaryAssociation(
    name="params6",
    ends={
        Property(name="tym_Variable7", type=tym_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="tym_Function", type=tym_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body8: BinaryAssociation = BinaryAssociation(
    name="body8",
    ends={
        Property(name="tym_FunctionBlock", type=tym_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="tym_Function9", type=tym_FunctionBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression10: BinaryAssociation = BinaryAssociation(
    name="expression10",
    ends={
        Property(name="tym_EObject11", type=tym_PrintStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="tym_PrintStatement", type=tym_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression12: BinaryAssociation = BinaryAssociation(
    name="expression12",
    ends={
        Property(name="tym_EObject13", type=tym_TestStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="tym_TestStatement", type=tym_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right42: BinaryAssociation = BinaryAssociation(
    name="right42",
    ends={
        Property(name="tym_And43", type=tym_Expression, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="tym_Expression44", type=tym_And, multiplicity=Multiplicity(1, 1))
    }
)
left45: BinaryAssociation = BinaryAssociation(
    name="left45",
    ends={
        Property(name="tym_Expression46", type=tym_Equality, multiplicity=Multiplicity(1, 1)),
        Property(name="tym_Equality", type=tym_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elements21: BinaryAssociation = BinaryAssociation(
    name="elements21",
    ends={
        Property(name="tym_AbstractElement23", type=tym_FunctionBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="tym_FunctionBlock22", type=tym_AbstractElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression24: BinaryAssociation = BinaryAssociation(
    name="expression24",
    ends={
        Property(name="tym_EObject25", type=tym_LoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="tym_LoopStatement", type=tym_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body26: BinaryAssociation = BinaryAssociation(
    name="body26",
    ends={
        Property(name="tym_Block28", type=tym_LoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="tym_LoopStatement27", type=tym_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression29: BinaryAssociation = BinaryAssociation(
    name="expression29",
    ends={
        Property(name="tym_EObject30", type=tym_Return, multiplicity=Multiplicity(1, 1)),
        Property(name="tym_Return", type=tym_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
funcname31: BinaryAssociation = BinaryAssociation(
    name="funcname31",
    ends={
        Property(name="tym_Function32", type=tym_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="tym_FunctionCall", type=tym_Function, multiplicity=Multiplicity(0, 1))
    }
)
params33: BinaryAssociation = BinaryAssociation(
    name="params33",
    ends={
        Property(name="tym_Expression", type=tym_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="tym_FunctionCall34", type=tym_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
left35: BinaryAssociation = BinaryAssociation(
    name="left35",
    ends={
        Property(name="tym_Expression36", type=tym_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="tym_Or", type=tym_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right37: BinaryAssociation = BinaryAssociation(
    name="right37",
    ends={
        Property(name="tym_Expression39", type=tym_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="tym_Or38", type=tym_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left40: BinaryAssociation = BinaryAssociation(
    name="left40",
    ends={
        Property(name="tym_Expression41", type=tym_And, multiplicity=Multiplicity(1, 1)),
        Property(name="tym_And", type=tym_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right67: BinaryAssociation = BinaryAssociation(
    name="right67",
    ends={
        Property(name="tym_Expression69", type=tym_MulOrDiv, multiplicity=Multiplicity(1, 1)),
        Property(name="tym_MulOrDiv68", type=tym_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right47: BinaryAssociation = BinaryAssociation(
    name="right47",
    ends={
        Property(name="tym_Expression49", type=tym_Equality, multiplicity=Multiplicity(1, 1)),
        Property(name="tym_Equality48", type=tym_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left50: BinaryAssociation = BinaryAssociation(
    name="left50",
    ends={
        Property(name="tym_Expression51", type=tym_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="tym_Comparison", type=tym_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right52: BinaryAssociation = BinaryAssociation(
    name="right52",
    ends={
        Property(name="tym_Expression54", type=tym_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="tym_Comparison53", type=tym_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left55: BinaryAssociation = BinaryAssociation(
    name="left55",
    ends={
        Property(name="tym_Expression56", type=tym_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="tym_Plus", type=tym_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right57: BinaryAssociation = BinaryAssociation(
    name="right57",
    ends={
        Property(name="tym_Expression59", type=tym_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="tym_Plus58", type=tym_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left60: BinaryAssociation = BinaryAssociation(
    name="left60",
    ends={
        Property(name="tym_Expression61", type=tym_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="tym_Minus", type=tym_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right62: BinaryAssociation = BinaryAssociation(
    name="right62",
    ends={
        Property(name="tym_Expression64", type=tym_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="tym_Minus63", type=tym_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left65: BinaryAssociation = BinaryAssociation(
    name="left65",
    ends={
        Property(name="tym_Expression66", type=tym_MulOrDiv, multiplicity=Multiplicity(1, 1)),
        Property(name="tym_MulOrDiv", type=tym_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression70: BinaryAssociation = BinaryAssociation(
    name="expression70",
    ends={
        Property(name="tym_Expression71", type=tym_Not, multiplicity=Multiplicity(1, 1)),
        Property(name="tym_Not", type=tym_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable72: BinaryAssociation = BinaryAssociation(
    name="variable72",
    ends={
        Property(name="tym_Variable73", type=tym_VariableRef, multiplicity=Multiplicity(1, 1)),
        Property(name="tym_VariableRef", type=tym_Variable, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_tym_Variable_AbstractElement = Generalization(general=AbstractElement, specific=tym_Variable)
gen_tym_PrintStatement_AbstractElement = Generalization(general=AbstractElement, specific=tym_PrintStatement)
gen_tym_TestStatement_AbstractElement = Generalization(general=AbstractElement, specific=tym_TestStatement)
gen_tym_Equality_Expression = Generalization(general=Expression, specific=tym_Equality)
gen_tym_LoopStatement_AbstractElement = Generalization(general=AbstractElement, specific=tym_LoopStatement)
gen_tym_Return_AbstractElement = Generalization(general=AbstractElement, specific=tym_Return)
gen_tym_FunctionCall_AbstractElement = Generalization(general=AbstractElement, specific=tym_FunctionCall)
gen_tym_Or_Expression = Generalization(general=Expression, specific=tym_Or)
gen_tym_And_Expression = Generalization(general=Expression, specific=tym_And)
gen_tym_Not_Expression = Generalization(general=Expression, specific=tym_Not)
gen_tym_Comparison_Expression = Generalization(general=Expression, specific=tym_Comparison)
gen_tym_Plus_Expression = Generalization(general=Expression, specific=tym_Plus)
gen_tym_Minus_Expression = Generalization(general=Expression, specific=tym_Minus)
gen_tym_MulOrDiv_Expression = Generalization(general=Expression, specific=tym_MulOrDiv)
gen_tym_IntConstant_Expression = Generalization(general=Expression, specific=tym_IntConstant)
gen_tym_StringConstant_Expression = Generalization(general=Expression, specific=tym_StringConstant)
gen_tym_BoolConstant_Expression = Generalization(general=Expression, specific=tym_BoolConstant)
gen_tym_VariableRef_Expression = Generalization(general=Expression, specific=tym_VariableRef)

# Domain Model
domain_model = DomainModel(
    name="tym",
    types={tym_Model, tym_EObject, tym_AbstractElement, tym_Variable, AbstractElement, tym_Function, tym_FunctionBlock, tym_PrintStatement, tym_TestStatement, tym_Block, tym_Equality, tym_LoopStatement, tym_Return, tym_FunctionCall, tym_Expression, tym_Or, Expression, tym_And, tym_Not, tym_Comparison, tym_Plus, tym_Minus, tym_MulOrDiv, tym_IntConstant, tym_StringConstant, tym_BoolConstant, tym_VariableRef},
    associations={thenBlock14, elseBlock16, elements19, elements0, variable2, expression3, params6, body8, expression10, expression12, right42, left45, elements21, expression24, body26, expression29, funcname31, params33, left35, right37, left40, right67, right47, left50, right52, left55, right57, left60, right62, left65, expression70, variable72},
    generalizations={gen_tym_Variable_AbstractElement, gen_tym_PrintStatement_AbstractElement, gen_tym_TestStatement_AbstractElement, gen_tym_Equality_Expression, gen_tym_LoopStatement_AbstractElement, gen_tym_Return_AbstractElement, gen_tym_FunctionCall_AbstractElement, gen_tym_Or_Expression, gen_tym_And_Expression, gen_tym_Not_Expression, gen_tym_Comparison_Expression, gen_tym_Plus_Expression, gen_tym_Minus_Expression, gen_tym_MulOrDiv_Expression, gen_tym_IntConstant_Expression, gen_tym_StringConstant_Expression, gen_tym_BoolConstant_Expression, gen_tym_VariableRef_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)