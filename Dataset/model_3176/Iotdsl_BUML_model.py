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
iotdsl_Iot = Class(name="iotdsl::Iot")
iotdsl_Device = Class(name="iotdsl::Device")
iotdsl_Action = Class(name="iotdsl::Action")
iotdsl_Attribute = Class(name="iotdsl::Attribute")
iotdsl_State = Class(name="iotdsl::State")
iotdsl_Event = Class(name="iotdsl::Event")
iotdsl_Transition = Class(name="iotdsl::Transition")
iotdsl_IfStatement = Class(name="iotdsl::IfStatement")
Expression = Class(name="Expression")
iotdsl_Variable = Class(name="iotdsl::Variable")
Action = Class(name="Action")
iotdsl_Expression = Class(name="iotdsl::Expression")
iotdsl_IfBlock = Class(name="iotdsl::IfBlock")
iotdsl_Or = Class(name="iotdsl::Or")
iotdsl_And = Class(name="iotdsl::And")
iotdsl_Equality = Class(name="iotdsl::Equality")
iotdsl_Comparison = Class(name="iotdsl::Comparison")
iotdsl_Plus = Class(name="iotdsl::Plus")
iotdsl_Minus = Class(name="iotdsl::Minus")
iotdsl_Not = Class(name="iotdsl::Not")
iotdsl_MulOrDiv = Class(name="iotdsl::MulOrDiv")
iotdsl_BoolConstant = Class(name="iotdsl::BoolConstant")
iotdsl_IntConstant = Class(name="iotdsl::IntConstant")
iotdsl_StringConstant = Class(name="iotdsl::StringConstant")
iotdsl_VariableRef = Class(name="iotdsl::VariableRef")

# iotdsl_Iot class attributes and methods

# iotdsl_Device class attributes and methods
iotdsl_Device_name: Property = Property(name="name", type=StringType)
iotdsl_Device.attributes={iotdsl_Device_name}

# iotdsl_Action class attributes and methods

# iotdsl_Attribute class attributes and methods
iotdsl_Attribute_typeName: Property = Property(name="typeName", type=StringType)
iotdsl_Attribute_tag: Property = Property(name="tag", type=StringType)
iotdsl_Attribute_value: Property = Property(name="value", type=StringType)
iotdsl_Attribute.attributes={iotdsl_Attribute_tag, iotdsl_Attribute_typeName, iotdsl_Attribute_value}

# iotdsl_State class attributes and methods
iotdsl_State_name: Property = Property(name="name", type=StringType)
iotdsl_State.attributes={iotdsl_State_name}

# iotdsl_Event class attributes and methods
iotdsl_Event_name: Property = Property(name="name", type=StringType)
iotdsl_Event.attributes={iotdsl_Event_name}

# iotdsl_Transition class attributes and methods
iotdsl_Transition_name: Property = Property(name="name", type=StringType)
iotdsl_Transition.attributes={iotdsl_Transition_name}

# iotdsl_IfStatement class attributes and methods

# Expression class attributes and methods

# iotdsl_Variable class attributes and methods
iotdsl_Variable_name: Property = Property(name="name", type=StringType)
iotdsl_Variable.attributes={iotdsl_Variable_name}

# Action class attributes and methods

# iotdsl_Expression class attributes and methods

# iotdsl_IfBlock class attributes and methods

# iotdsl_Or class attributes and methods

# iotdsl_And class attributes and methods

# iotdsl_Equality class attributes and methods
iotdsl_Equality_op: Property = Property(name="op", type=StringType)
iotdsl_Equality.attributes={iotdsl_Equality_op}

# iotdsl_Comparison class attributes and methods
iotdsl_Comparison_op: Property = Property(name="op", type=StringType)
iotdsl_Comparison.attributes={iotdsl_Comparison_op}

# iotdsl_Plus class attributes and methods

# iotdsl_Minus class attributes and methods

# iotdsl_Not class attributes and methods

# iotdsl_MulOrDiv class attributes and methods
iotdsl_MulOrDiv_op: Property = Property(name="op", type=StringType)
iotdsl_MulOrDiv.attributes={iotdsl_MulOrDiv_op}

# iotdsl_BoolConstant class attributes and methods
iotdsl_BoolConstant_value: Property = Property(name="value", type=StringType)
iotdsl_BoolConstant.attributes={iotdsl_BoolConstant_value}

# iotdsl_IntConstant class attributes and methods
iotdsl_IntConstant_value: Property = Property(name="value", type=IntegerType)
iotdsl_IntConstant.attributes={iotdsl_IntConstant_value}

# iotdsl_StringConstant class attributes and methods
iotdsl_StringConstant_value: Property = Property(name="value", type=StringType)
iotdsl_StringConstant.attributes={iotdsl_StringConstant_value}

# iotdsl_VariableRef class attributes and methods

# Relationships
devices0: BinaryAssociation = BinaryAssociation(
    name="devices0",
    ends={
        Property(name="iotdsl_Device", type=iotdsl_Iot, multiplicity=Multiplicity(1, 1)),
        Property(name="iotdsl_Iot", type=iotdsl_Device, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements12: BinaryAssociation = BinaryAssociation(
    name="elements12",
    ends={
        Property(name="iotdsl_Action", type=iotdsl_State, multiplicity=Multiplicity(1, 1)),
        Property(name="iotdsl_State13", type=iotdsl_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superType2: BinaryAssociation = BinaryAssociation(
    name="superType2",
    ends={
        Property(name="iotdsl_Device3", type=iotdsl_Device, multiplicity=Multiplicity(1, 1)),
        Property(name="iotdsl_Device1", type=iotdsl_Device, multiplicity=Multiplicity(0, 1))
    }
)
attributes4: BinaryAssociation = BinaryAssociation(
    name="attributes4",
    ends={
        Property(name="iotdsl_Attribute", type=iotdsl_Device, multiplicity=Multiplicity(1, 1)),
        Property(name="iotdsl_Device5", type=iotdsl_Attribute, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
states6: BinaryAssociation = BinaryAssociation(
    name="states6",
    ends={
        Property(name="iotdsl_State", type=iotdsl_Device, multiplicity=Multiplicity(1, 1)),
        Property(name="iotdsl_Device7", type=iotdsl_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
events8: BinaryAssociation = BinaryAssociation(
    name="events8",
    ends={
        Property(name="iotdsl_Event", type=iotdsl_Device, multiplicity=Multiplicity(1, 1)),
        Property(name="iotdsl_Device9", type=iotdsl_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions10: BinaryAssociation = BinaryAssociation(
    name="transitions10",
    ends={
        Property(name="iotdsl_Transition", type=iotdsl_Device, multiplicity=Multiplicity(1, 1)),
        Property(name="iotdsl_Device11", type=iotdsl_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event14: BinaryAssociation = BinaryAssociation(
    name="event14",
    ends={
        Property(name="iotdsl_Event16", type=iotdsl_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="iotdsl_Transition15", type=iotdsl_Event, multiplicity=Multiplicity(0, 1))
    }
)
state17: BinaryAssociation = BinaryAssociation(
    name="state17",
    ends={
        Property(name="iotdsl_State19", type=iotdsl_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="iotdsl_Transition18", type=iotdsl_State, multiplicity=Multiplicity(0, 1))
    }
)
expression20: BinaryAssociation = BinaryAssociation(
    name="expression20",
    ends={
        Property(name="iotdsl_Expression", type=iotdsl_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="iotdsl_Variable", type=iotdsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements28: BinaryAssociation = BinaryAssociation(
    name="statements28",
    ends={
        Property(name="iotdsl_Action30", type=iotdsl_IfBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="iotdsl_IfBlock29", type=iotdsl_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression21: BinaryAssociation = BinaryAssociation(
    name="expression21",
    ends={
        Property(name="iotdsl_Expression22", type=iotdsl_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="iotdsl_IfStatement", type=iotdsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thenBlock23: BinaryAssociation = BinaryAssociation(
    name="thenBlock23",
    ends={
        Property(name="iotdsl_IfBlock", type=iotdsl_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="iotdsl_IfStatement24", type=iotdsl_IfBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseBlock25: BinaryAssociation = BinaryAssociation(
    name="elseBlock25",
    ends={
        Property(name="iotdsl_IfBlock27", type=iotdsl_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="iotdsl_IfStatement26", type=iotdsl_IfBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left36: BinaryAssociation = BinaryAssociation(
    name="left36",
    ends={
        Property(name="iotdsl_Expression37", type=iotdsl_And, multiplicity=Multiplicity(1, 1)),
        Property(name="iotdsl_And", type=iotdsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left31: BinaryAssociation = BinaryAssociation(
    name="left31",
    ends={
        Property(name="iotdsl_Expression32", type=iotdsl_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="iotdsl_Or", type=iotdsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right33: BinaryAssociation = BinaryAssociation(
    name="right33",
    ends={
        Property(name="iotdsl_Expression35", type=iotdsl_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="iotdsl_Or34", type=iotdsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right43: BinaryAssociation = BinaryAssociation(
    name="right43",
    ends={
        Property(name="iotdsl_Equality44", type=iotdsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="iotdsl_Expression45", type=iotdsl_Equality, multiplicity=Multiplicity(1, 1))
    }
)
right38: BinaryAssociation = BinaryAssociation(
    name="right38",
    ends={
        Property(name="iotdsl_Expression40", type=iotdsl_And, multiplicity=Multiplicity(1, 1)),
        Property(name="iotdsl_And39", type=iotdsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left41: BinaryAssociation = BinaryAssociation(
    name="left41",
    ends={
        Property(name="iotdsl_Expression42", type=iotdsl_Equality, multiplicity=Multiplicity(1, 1)),
        Property(name="iotdsl_Equality", type=iotdsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left46: BinaryAssociation = BinaryAssociation(
    name="left46",
    ends={
        Property(name="iotdsl_Expression47", type=iotdsl_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="iotdsl_Comparison", type=iotdsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right48: BinaryAssociation = BinaryAssociation(
    name="right48",
    ends={
        Property(name="iotdsl_Expression50", type=iotdsl_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="iotdsl_Comparison49", type=iotdsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left51: BinaryAssociation = BinaryAssociation(
    name="left51",
    ends={
        Property(name="iotdsl_Expression52", type=iotdsl_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="iotdsl_Plus", type=iotdsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right53: BinaryAssociation = BinaryAssociation(
    name="right53",
    ends={
        Property(name="iotdsl_Expression55", type=iotdsl_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="iotdsl_Plus54", type=iotdsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left56: BinaryAssociation = BinaryAssociation(
    name="left56",
    ends={
        Property(name="iotdsl_Expression57", type=iotdsl_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="iotdsl_Minus", type=iotdsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right58: BinaryAssociation = BinaryAssociation(
    name="right58",
    ends={
        Property(name="iotdsl_Expression60", type=iotdsl_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="iotdsl_Minus59", type=iotdsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left61: BinaryAssociation = BinaryAssociation(
    name="left61",
    ends={
        Property(name="iotdsl_Expression62", type=iotdsl_MulOrDiv, multiplicity=Multiplicity(1, 1)),
        Property(name="iotdsl_MulOrDiv", type=iotdsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right63: BinaryAssociation = BinaryAssociation(
    name="right63",
    ends={
        Property(name="iotdsl_Expression65", type=iotdsl_MulOrDiv, multiplicity=Multiplicity(1, 1)),
        Property(name="iotdsl_MulOrDiv64", type=iotdsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression66: BinaryAssociation = BinaryAssociation(
    name="expression66",
    ends={
        Property(name="iotdsl_Expression67", type=iotdsl_Not, multiplicity=Multiplicity(1, 1)),
        Property(name="iotdsl_Not", type=iotdsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable68: BinaryAssociation = BinaryAssociation(
    name="variable68",
    ends={
        Property(name="iotdsl_Variable69", type=iotdsl_VariableRef, multiplicity=Multiplicity(1, 1)),
        Property(name="iotdsl_VariableRef", type=iotdsl_Variable, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_iotdsl_Variable_Action = Generalization(general=Action, specific=iotdsl_Variable)
gen_iotdsl_Expression_Action = Generalization(general=Action, specific=iotdsl_Expression)
gen_iotdsl_IfStatement_Expression = Generalization(general=Expression, specific=iotdsl_IfStatement)
gen_iotdsl_Or_Expression = Generalization(general=Expression, specific=iotdsl_Or)
gen_iotdsl_And_Expression = Generalization(general=Expression, specific=iotdsl_And)
gen_iotdsl_Equality_Expression = Generalization(general=Expression, specific=iotdsl_Equality)
gen_iotdsl_Plus_Expression = Generalization(general=Expression, specific=iotdsl_Plus)
gen_iotdsl_Comparison_Expression = Generalization(general=Expression, specific=iotdsl_Comparison)
gen_iotdsl_Minus_Expression = Generalization(general=Expression, specific=iotdsl_Minus)
gen_iotdsl_Not_Expression = Generalization(general=Expression, specific=iotdsl_Not)
gen_iotdsl_MulOrDiv_Expression = Generalization(general=Expression, specific=iotdsl_MulOrDiv)
gen_iotdsl_BoolConstant_Expression = Generalization(general=Expression, specific=iotdsl_BoolConstant)
gen_iotdsl_IntConstant_Expression = Generalization(general=Expression, specific=iotdsl_IntConstant)
gen_iotdsl_StringConstant_Expression = Generalization(general=Expression, specific=iotdsl_StringConstant)
gen_iotdsl_VariableRef_Expression = Generalization(general=Expression, specific=iotdsl_VariableRef)

# Domain Model
domain_model = DomainModel(
    name="iotdsl",
    types={iotdsl_Iot, iotdsl_Device, iotdsl_Action, iotdsl_Attribute, iotdsl_State, iotdsl_Event, iotdsl_Transition, iotdsl_IfStatement, Expression, iotdsl_Variable, Action, iotdsl_Expression, iotdsl_IfBlock, iotdsl_Or, iotdsl_And, iotdsl_Equality, iotdsl_Comparison, iotdsl_Plus, iotdsl_Minus, iotdsl_Not, iotdsl_MulOrDiv, iotdsl_BoolConstant, iotdsl_IntConstant, iotdsl_StringConstant, iotdsl_VariableRef},
    associations={devices0, elements12, superType2, attributes4, states6, events8, transitions10, event14, state17, expression20, statements28, expression21, thenBlock23, elseBlock25, left36, left31, right33, right43, right38, left41, left46, right48, left51, right53, left56, right58, left61, right63, expression66, variable68},
    generalizations={gen_iotdsl_Variable_Action, gen_iotdsl_Expression_Action, gen_iotdsl_IfStatement_Expression, gen_iotdsl_Or_Expression, gen_iotdsl_And_Expression, gen_iotdsl_Equality_Expression, gen_iotdsl_Plus_Expression, gen_iotdsl_Comparison_Expression, gen_iotdsl_Minus_Expression, gen_iotdsl_Not_Expression, gen_iotdsl_MulOrDiv_Expression, gen_iotdsl_BoolConstant_Expression, gen_iotdsl_IntConstant_Expression, gen_iotdsl_StringConstant_Expression, gen_iotdsl_VariableRef_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)