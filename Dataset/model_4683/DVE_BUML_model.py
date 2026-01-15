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
BinaryOperator: Enumeration = Enumeration(
    name="BinaryOperator",
    literals={
            EnumerationLiteral(name="IMPLY"),
			EnumerationLiteral(name="OR"),
			EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="BOR"),
			EnumerationLiteral(name="BAND"),
			EnumerationLiteral(name="BXOR"),
			EnumerationLiteral(name="EQ"),
			EnumerationLiteral(name="NEQ"),
			EnumerationLiteral(name="LT"),
			EnumerationLiteral(name="LEQ"),
			EnumerationLiteral(name="GT"),
			EnumerationLiteral(name="GEQ"),
			EnumerationLiteral(name="SHL"),
			EnumerationLiteral(name="SHR"),
			EnumerationLiteral(name="PLUS"),
			EnumerationLiteral(name="MINUS"),
			EnumerationLiteral(name="MULT"),
			EnumerationLiteral(name="DIV"),
			EnumerationLiteral(name="MOD")
    }
)

UnaryOperator: Enumeration = Enumeration(
    name="UnaryOperator",
    literals={
            EnumerationLiteral(name="MINUS"),
			EnumerationLiteral(name="BNOT"),
			EnumerationLiteral(name="NOT")
    }
)

# Classes
SystemProperties = Class(name="SystemProperties")
DVE_model_Type = Class(name="DVE::model::Type", is_abstract=True)
DVE_model_IntegerType = Class(name="DVE::model::IntegerType")
Type = Class(name="Type")
DVE_model_ByteType = Class(name="DVE::model::ByteType")
DVE_model_ArrayType = Class(name="DVE::model::ArrayType")
Expression = Class(name="Expression")
DVE_model_VariableDeclaration = Class(name="DVE::model::VariableDeclaration")
DVE_model_Element = Class(name="DVE::model::Element", is_abstract=True)
DVE_model_Declaration = Class(name="DVE::model::Declaration", is_abstract=True)
Element = Class(name="Element")
DVE_model_NamedDeclaration = Class(name="DVE::model::NamedDeclaration", is_abstract=True)
Declaration = Class(name="Declaration")
DVE_model_CompositeDeclaration = Class(name="DVE::model::CompositeDeclaration", is_abstract=True)
NamedDeclaration = Class(name="NamedDeclaration")
DVE_model_System = Class(name="DVE::model::System")
CompositeDeclaration = Class(name="CompositeDeclaration")
Process = Class(name="Process")
Transition = Class(name="Transition")
DVE_model_State = Class(name="DVE::model::State")
DVE_model_Transition = Class(name="DVE::model::Transition")
Synchronization = Class(name="Synchronization")
Assignment = Class(name="Assignment")
DVE_model_Synchronization = Class(name="DVE::model::Synchronization", is_abstract=True)
DVE_model_ConstantDeclaration = Class(name="DVE::model::ConstantDeclaration")
VariableDeclaration = Class(name="VariableDeclaration")
DVE_model_ChannelDeclaration = Class(name="DVE::model::ChannelDeclaration")
DVE_model_TypedChannelDeclaration = Class(name="DVE::model::TypedChannelDeclaration")
ChannelDeclaration = Class(name="ChannelDeclaration")
DVE_model_Process = Class(name="DVE::model::Process")
System = Class(name="System")
State = Class(name="State")
StateReference = Class(name="StateReference")
DVE_model_BinaryExpression = Class(name="DVE::model::BinaryExpression")
ChannelReference = Class(name="ChannelReference")
DVE_model_InputSynchronization = Class(name="DVE::model::InputSynchronization")
DVE_model_OutputSynchronization = Class(name="DVE::model::OutputSynchronization")
DVE_model_SystemProperties = Class(name="DVE::model::SystemProperties")
SystemType = Class(name="SystemType")
ProcessReference = Class(name="ProcessReference")
DVE_model_Assignment = Class(name="DVE::model::Assignment")
DVE_model_SystemType = Class(name="DVE::model::SystemType", is_abstract=True)
DVE_model_Synchronous = Class(name="DVE::model::Synchronous")
DVE_model_Asynchronous = Class(name="DVE::model::Asynchronous")
DVE_model_Expression = Class(name="DVE::model::Expression", is_abstract=True)
DVE_model_UnaryExpression = Class(name="DVE::model::UnaryExpression")
DVE_model_PrefixedReference = Class(name="DVE::model::PrefixedReference", is_abstract=True)
DVE_model_ProcessVariableReference = Class(name="DVE::model::ProcessVariableReference")
model_VariableReference = Class(name="model::VariableReference")
model_PrefixedReference = Class(name="model::PrefixedReference")
DVE_model_ProcessStateReference = Class(name="DVE::model::ProcessStateReference")
model_StateReference = Class(name="model::StateReference")
DVE_model_IndexedExpression = Class(name="DVE::model::IndexedExpression")
DVE_model_Reference = Class(name="DVE::model::Reference", is_abstract=True)
DVE_model_VariableReference = Class(name="DVE::model::VariableReference")
Reference = Class(name="Reference")
DVE_model_ChannelReference = Class(name="DVE::model::ChannelReference")
DVE_model_ProcessReference = Class(name="DVE::model::ProcessReference")
DVE_model_StateReference = Class(name="DVE::model::StateReference")
DVE_model_Literal = Class(name="DVE::model::Literal", is_abstract=True)
DVE_model_BooleanLiteral = Class(name="DVE::model::BooleanLiteral")
Literal = Class(name="Literal")
DVE_model_TrueLiteral = Class(name="DVE::model::TrueLiteral")
BooleanLiteral = Class(name="BooleanLiteral")
DVE_model_FalseLiteral = Class(name="DVE::model::FalseLiteral")
DVE_model_NumberLiteral = Class(name="DVE::model::NumberLiteral")
DVE_model_ArrayLiteral = Class(name="DVE::model::ArrayLiteral")

# SystemProperties class attributes and methods

# DVE_model_Type class attributes and methods

# DVE_model_IntegerType class attributes and methods

# Type class attributes and methods

# DVE_model_ByteType class attributes and methods

# DVE_model_ArrayType class attributes and methods

# Expression class attributes and methods

# DVE_model_VariableDeclaration class attributes and methods

# DVE_model_Element class attributes and methods

# DVE_model_Declaration class attributes and methods

# Element class attributes and methods

# DVE_model_NamedDeclaration class attributes and methods
DVE_model_NamedDeclaration_name: Property = Property(name="name", type=StringType)
DVE_model_NamedDeclaration.attributes={DVE_model_NamedDeclaration_name}

# Declaration class attributes and methods

# DVE_model_CompositeDeclaration class attributes and methods

# NamedDeclaration class attributes and methods

# DVE_model_System class attributes and methods

# CompositeDeclaration class attributes and methods

# Process class attributes and methods

# Transition class attributes and methods

# DVE_model_State class attributes and methods

# DVE_model_Transition class attributes and methods

# Synchronization class attributes and methods

# Assignment class attributes and methods

# DVE_model_Synchronization class attributes and methods

# DVE_model_ConstantDeclaration class attributes and methods

# VariableDeclaration class attributes and methods

# DVE_model_ChannelDeclaration class attributes and methods

# DVE_model_TypedChannelDeclaration class attributes and methods

# ChannelDeclaration class attributes and methods

# DVE_model_Process class attributes and methods

# System class attributes and methods

# State class attributes and methods

# StateReference class attributes and methods

# DVE_model_BinaryExpression class attributes and methods
DVE_model_BinaryExpression_operator: Property = Property(name="operator", type=StringType)
DVE_model_BinaryExpression.attributes={DVE_model_BinaryExpression_operator}

# ChannelReference class attributes and methods

# DVE_model_InputSynchronization class attributes and methods

# DVE_model_OutputSynchronization class attributes and methods

# DVE_model_SystemProperties class attributes and methods

# SystemType class attributes and methods

# ProcessReference class attributes and methods

# DVE_model_Assignment class attributes and methods

# DVE_model_SystemType class attributes and methods

# DVE_model_Synchronous class attributes and methods

# DVE_model_Asynchronous class attributes and methods

# DVE_model_Expression class attributes and methods

# DVE_model_UnaryExpression class attributes and methods
DVE_model_UnaryExpression_operator: Property = Property(name="operator", type=StringType)
DVE_model_UnaryExpression.attributes={DVE_model_UnaryExpression_operator}

# DVE_model_PrefixedReference class attributes and methods

# DVE_model_ProcessVariableReference class attributes and methods

# model_VariableReference class attributes and methods

# model_PrefixedReference class attributes and methods

# DVE_model_ProcessStateReference class attributes and methods

# model_StateReference class attributes and methods

# DVE_model_IndexedExpression class attributes and methods

# DVE_model_Reference class attributes and methods
DVE_model_Reference_refName: Property = Property(name="refName", type=StringType)
DVE_model_Reference.attributes={DVE_model_Reference_refName}

# DVE_model_VariableReference class attributes and methods

# Reference class attributes and methods

# DVE_model_ChannelReference class attributes and methods

# DVE_model_ProcessReference class attributes and methods

# DVE_model_StateReference class attributes and methods

# DVE_model_Literal class attributes and methods

# DVE_model_BooleanLiteral class attributes and methods

# Literal class attributes and methods

# DVE_model_TrueLiteral class attributes and methods

# BooleanLiteral class attributes and methods

# DVE_model_FalseLiteral class attributes and methods

# DVE_model_NumberLiteral class attributes and methods
DVE_model_NumberLiteral_value: Property = Property(name="value", type=StringType)
DVE_model_NumberLiteral.attributes={DVE_model_NumberLiteral_value}

# DVE_model_ArrayLiteral class attributes and methods

# Relationships
properties2: BinaryAssociation = BinaryAssociation(
    name="properties2",
    ends={
        Property(name="SystemProperties", type=DVE_model_System, multiplicity=Multiplicity(1, 1)),
        Property(name="DVE_model_System", type=SystemProperties, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elementType3: BinaryAssociation = BinaryAssociation(
    name="elementType3",
    ends={
        Property(name="Type", type=DVE_model_ArrayType, multiplicity=Multiplicity(1, 1)),
        Property(name="DVE_model_ArrayType", type=Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
size4: BinaryAssociation = BinaryAssociation(
    name="size4",
    ends={
        Property(name="Expression", type=DVE_model_ArrayType, multiplicity=Multiplicity(1, 1)),
        Property(name="DVE_model_ArrayType5", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
declarations0: BinaryAssociation = BinaryAssociation(
    name="declarations0",
    ends={
        Property(name="NamedDeclaration", type=DVE_model_CompositeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DVE_model_CompositeDeclaration", type=NamedDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
processes1: BinaryAssociation = BinaryAssociation(
    name="processes1",
    ends={
        Property(name="model", type=DVE_model_System, multiplicity=Multiplicity(1, 1)),
        Property(name="Process", type=Process, multiplicity=Multiplicity(0, 9999))
    }
)
transitions27: BinaryAssociation = BinaryAssociation(
    name="transitions27",
    ends={
        Property(name="Transition", type=DVE_model_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="DVE_model_Process28", type=Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
from29: BinaryAssociation = BinaryAssociation(
    name="from29",
    ends={
        Property(name="StateReference30", type=DVE_model_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="DVE_model_Transition", type=StateReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
to31: BinaryAssociation = BinaryAssociation(
    name="to31",
    ends={
        Property(name="StateReference33", type=DVE_model_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="DVE_model_Transition32", type=StateReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
guard34: BinaryAssociation = BinaryAssociation(
    name="guard34",
    ends={
        Property(name="Expression36", type=DVE_model_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="DVE_model_Transition35", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sync37: BinaryAssociation = BinaryAssociation(
    name="sync37",
    ends={
        Property(name="Synchronization", type=DVE_model_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="DVE_model_Transition38", type=Synchronization, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
effect39: BinaryAssociation = BinaryAssociation(
    name="effect39",
    ends={
        Property(name="Assignment", type=DVE_model_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="DVE_model_Transition40", type=Assignment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type6: BinaryAssociation = BinaryAssociation(
    name="type6",
    ends={
        Property(name="Type7", type=DVE_model_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DVE_model_VariableDeclaration", type=Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initial8: BinaryAssociation = BinaryAssociation(
    name="initial8",
    ends={
        Property(name="Expression10", type=DVE_model_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DVE_model_VariableDeclaration9", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
types11: BinaryAssociation = BinaryAssociation(
    name="types11",
    ends={
        Property(name="Type12", type=DVE_model_TypedChannelDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DVE_model_TypedChannelDeclaration", type=Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bufferSize13: BinaryAssociation = BinaryAssociation(
    name="bufferSize13",
    ends={
        Property(name="Expression15", type=DVE_model_TypedChannelDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="DVE_model_TypedChannelDeclaration14", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
system16: BinaryAssociation = BinaryAssociation(
    name="system16",
    ends={
        Property(name="model17", type=DVE_model_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="System", type=System, multiplicity=Multiplicity(1, 1))
    }
)
states18: BinaryAssociation = BinaryAssociation(
    name="states18",
    ends={
        Property(name="State", type=DVE_model_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="DVE_model_Process", type=State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
accepting19: BinaryAssociation = BinaryAssociation(
    name="accepting19",
    ends={
        Property(name="StateReference", type=DVE_model_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="DVE_model_Process20", type=StateReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
commited21: BinaryAssociation = BinaryAssociation(
    name="commited21",
    ends={
        Property(name="StateReference23", type=DVE_model_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="DVE_model_Process22", type=StateReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initial24: BinaryAssociation = BinaryAssociation(
    name="initial24",
    ends={
        Property(name="StateReference26", type=DVE_model_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="DVE_model_Process25", type=StateReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operand53: BinaryAssociation = BinaryAssociation(
    name="operand53",
    ends={
        Property(name="Expression54", type=DVE_model_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="DVE_model_UnaryExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operands55: BinaryAssociation = BinaryAssociation(
    name="operands55",
    ends={
        Property(name="Expression56", type=DVE_model_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="DVE_model_BinaryExpression", type=Expression, multiplicity=Multiplicity(2, 2), is_composite=True)
    }
)
channel41: BinaryAssociation = BinaryAssociation(
    name="channel41",
    ends={
        Property(name="ChannelReference", type=DVE_model_Synchronization, multiplicity=Multiplicity(1, 1)),
        Property(name="DVE_model_Synchronization", type=ChannelReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value42: BinaryAssociation = BinaryAssociation(
    name="value42",
    ends={
        Property(name="Expression44", type=DVE_model_Synchronization, multiplicity=Multiplicity(1, 1)),
        Property(name="DVE_model_Synchronization43", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
systemType45: BinaryAssociation = BinaryAssociation(
    name="systemType45",
    ends={
        Property(name="SystemType", type=DVE_model_SystemProperties, multiplicity=Multiplicity(1, 1)),
        Property(name="DVE_model_SystemProperties", type=SystemType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
property46: BinaryAssociation = BinaryAssociation(
    name="property46",
    ends={
        Property(name="ProcessReference", type=DVE_model_SystemProperties, multiplicity=Multiplicity(1, 1)),
        Property(name="DVE_model_SystemProperties47", type=ProcessReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lhs48: BinaryAssociation = BinaryAssociation(
    name="lhs48",
    ends={
        Property(name="Expression49", type=DVE_model_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="DVE_model_Assignment", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs50: BinaryAssociation = BinaryAssociation(
    name="rhs50",
    ends={
        Property(name="Expression52", type=DVE_model_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="DVE_model_Assignment51", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ref61: BinaryAssociation = BinaryAssociation(
    name="ref61",
    ends={
        Property(name="State62", type=DVE_model_StateReference, multiplicity=Multiplicity(1, 1)),
        Property(name="DVE_model_StateReference", type=State, multiplicity=Multiplicity(1, 1))
    }
)
prefix63: BinaryAssociation = BinaryAssociation(
    name="prefix63",
    ends={
        Property(name="ProcessReference64", type=DVE_model_PrefixedReference, multiplicity=Multiplicity(1, 1)),
        Property(name="DVE_model_PrefixedReference", type=ProcessReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
base65: BinaryAssociation = BinaryAssociation(
    name="base65",
    ends={
        Property(name="Expression66", type=DVE_model_IndexedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="DVE_model_IndexedExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ref57: BinaryAssociation = BinaryAssociation(
    name="ref57",
    ends={
        Property(name="VariableDeclaration", type=DVE_model_VariableReference, multiplicity=Multiplicity(1, 1)),
        Property(name="DVE_model_VariableReference", type=VariableDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
ref58: BinaryAssociation = BinaryAssociation(
    name="ref58",
    ends={
        Property(name="ChannelDeclaration", type=DVE_model_ChannelReference, multiplicity=Multiplicity(1, 1)),
        Property(name="DVE_model_ChannelReference", type=ChannelDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
ref59: BinaryAssociation = BinaryAssociation(
    name="ref59",
    ends={
        Property(name="Process60", type=DVE_model_ProcessReference, multiplicity=Multiplicity(1, 1)),
        Property(name="DVE_model_ProcessReference", type=Process, multiplicity=Multiplicity(1, 1))
    }
)
index67: BinaryAssociation = BinaryAssociation(
    name="index67",
    ends={
        Property(name="Expression69", type=DVE_model_IndexedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="DVE_model_IndexedExpression68", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
values70: BinaryAssociation = BinaryAssociation(
    name="values70",
    ends={
        Property(name="Expression71", type=DVE_model_ArrayLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="DVE_model_ArrayLiteral", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_DVE_model_Type_Element = Generalization(general=Element, specific=DVE_model_Type)
gen_DVE_model_IntegerType_Type = Generalization(general=Type, specific=DVE_model_IntegerType)
gen_DVE_model_ByteType_Type = Generalization(general=Type, specific=DVE_model_ByteType)
gen_DVE_model_ArrayType_Type = Generalization(general=Type, specific=DVE_model_ArrayType)
gen_DVE_model_VariableDeclaration_NamedDeclaration = Generalization(general=NamedDeclaration, specific=DVE_model_VariableDeclaration)
gen_DVE_model_Declaration_Element = Generalization(general=Element, specific=DVE_model_Declaration)
gen_DVE_model_NamedDeclaration_Declaration = Generalization(general=Declaration, specific=DVE_model_NamedDeclaration)
gen_DVE_model_CompositeDeclaration_NamedDeclaration = Generalization(general=NamedDeclaration, specific=DVE_model_CompositeDeclaration)
gen_DVE_model_System_CompositeDeclaration = Generalization(general=CompositeDeclaration, specific=DVE_model_System)
gen_DVE_model_State_NamedDeclaration = Generalization(general=NamedDeclaration, specific=DVE_model_State)
gen_DVE_model_Transition_Declaration = Generalization(general=Declaration, specific=DVE_model_Transition)
gen_DVE_model_Synchronization_Element = Generalization(general=Element, specific=DVE_model_Synchronization)
gen_DVE_model_ConstantDeclaration_VariableDeclaration = Generalization(general=VariableDeclaration, specific=DVE_model_ConstantDeclaration)
gen_DVE_model_ChannelDeclaration_NamedDeclaration = Generalization(general=NamedDeclaration, specific=DVE_model_ChannelDeclaration)
gen_DVE_model_TypedChannelDeclaration_ChannelDeclaration = Generalization(general=ChannelDeclaration, specific=DVE_model_TypedChannelDeclaration)
gen_DVE_model_Process_CompositeDeclaration = Generalization(general=CompositeDeclaration, specific=DVE_model_Process)
gen_DVE_model_BinaryExpression_Expression = Generalization(general=Expression, specific=DVE_model_BinaryExpression)
gen_DVE_model_InputSynchronization_Synchronization = Generalization(general=Synchronization, specific=DVE_model_InputSynchronization)
gen_DVE_model_OutputSynchronization_Synchronization = Generalization(general=Synchronization, specific=DVE_model_OutputSynchronization)
gen_DVE_model_SystemProperties_Element = Generalization(general=Element, specific=DVE_model_SystemProperties)
gen_DVE_model_Assignment_Element = Generalization(general=Element, specific=DVE_model_Assignment)
gen_DVE_model_SystemType_Element = Generalization(general=Element, specific=DVE_model_SystemType)
gen_DVE_model_Synchronous_SystemType = Generalization(general=SystemType, specific=DVE_model_Synchronous)
gen_DVE_model_Asynchronous_SystemType = Generalization(general=SystemType, specific=DVE_model_Asynchronous)
gen_DVE_model_Expression_Element = Generalization(general=Element, specific=DVE_model_Expression)
gen_DVE_model_UnaryExpression_Expression = Generalization(general=Expression, specific=DVE_model_UnaryExpression)
gen_DVE_model_PrefixedReference_Expression = Generalization(general=Expression, specific=DVE_model_PrefixedReference)
gen_DVE_model_ProcessVariableReference_model_VariableReference = Generalization(general=model_VariableReference, specific=DVE_model_ProcessVariableReference)
gen_DVE_model_ProcessVariableReference_model_PrefixedReference = Generalization(general=model_PrefixedReference, specific=DVE_model_ProcessVariableReference)
gen_DVE_model_ProcessStateReference_model_StateReference = Generalization(general=model_StateReference, specific=DVE_model_ProcessStateReference)
gen_DVE_model_ProcessStateReference_model_PrefixedReference = Generalization(general=model_PrefixedReference, specific=DVE_model_ProcessStateReference)
gen_DVE_model_IndexedExpression_Expression = Generalization(general=Expression, specific=DVE_model_IndexedExpression)
gen_DVE_model_Reference_Expression = Generalization(general=Expression, specific=DVE_model_Reference)
gen_DVE_model_VariableReference_Reference = Generalization(general=Reference, specific=DVE_model_VariableReference)
gen_DVE_model_ChannelReference_Reference = Generalization(general=Reference, specific=DVE_model_ChannelReference)
gen_DVE_model_ProcessReference_Reference = Generalization(general=Reference, specific=DVE_model_ProcessReference)
gen_DVE_model_StateReference_Reference = Generalization(general=Reference, specific=DVE_model_StateReference)
gen_DVE_model_Literal_Expression = Generalization(general=Expression, specific=DVE_model_Literal)
gen_DVE_model_BooleanLiteral_Literal = Generalization(general=Literal, specific=DVE_model_BooleanLiteral)
gen_DVE_model_TrueLiteral_BooleanLiteral = Generalization(general=BooleanLiteral, specific=DVE_model_TrueLiteral)
gen_DVE_model_FalseLiteral_BooleanLiteral = Generalization(general=BooleanLiteral, specific=DVE_model_FalseLiteral)
gen_DVE_model_NumberLiteral_Literal = Generalization(general=Literal, specific=DVE_model_NumberLiteral)
gen_DVE_model_ArrayLiteral_Literal = Generalization(general=Literal, specific=DVE_model_ArrayLiteral)

# Domain Model
domain_model = DomainModel(
    name="DVE",
    types={SystemProperties, DVE_model_Type, DVE_model_IntegerType, Type, DVE_model_ByteType, DVE_model_ArrayType, Expression, DVE_model_VariableDeclaration, DVE_model_Element, DVE_model_Declaration, Element, DVE_model_NamedDeclaration, Declaration, DVE_model_CompositeDeclaration, NamedDeclaration, DVE_model_System, CompositeDeclaration, Process, Transition, DVE_model_State, DVE_model_Transition, Synchronization, Assignment, DVE_model_Synchronization, DVE_model_ConstantDeclaration, VariableDeclaration, DVE_model_ChannelDeclaration, DVE_model_TypedChannelDeclaration, ChannelDeclaration, DVE_model_Process, System, State, StateReference, DVE_model_BinaryExpression, ChannelReference, DVE_model_InputSynchronization, DVE_model_OutputSynchronization, DVE_model_SystemProperties, SystemType, ProcessReference, DVE_model_Assignment, DVE_model_SystemType, DVE_model_Synchronous, DVE_model_Asynchronous, DVE_model_Expression, DVE_model_UnaryExpression, DVE_model_PrefixedReference, DVE_model_ProcessVariableReference, model_VariableReference, model_PrefixedReference, DVE_model_ProcessStateReference, model_StateReference, DVE_model_IndexedExpression, DVE_model_Reference, DVE_model_VariableReference, Reference, DVE_model_ChannelReference, DVE_model_ProcessReference, DVE_model_StateReference, DVE_model_Literal, DVE_model_BooleanLiteral, Literal, DVE_model_TrueLiteral, BooleanLiteral, DVE_model_FalseLiteral, DVE_model_NumberLiteral, DVE_model_ArrayLiteral, BinaryOperator, UnaryOperator},
    associations={properties2, elementType3, size4, declarations0, processes1, transitions27, from29, to31, guard34, sync37, effect39, type6, initial8, types11, bufferSize13, system16, states18, accepting19, commited21, initial24, operand53, operands55, channel41, value42, systemType45, property46, lhs48, rhs50, ref61, prefix63, base65, ref57, ref58, ref59, index67, values70},
    generalizations={gen_DVE_model_Type_Element, gen_DVE_model_IntegerType_Type, gen_DVE_model_ByteType_Type, gen_DVE_model_ArrayType_Type, gen_DVE_model_VariableDeclaration_NamedDeclaration, gen_DVE_model_Declaration_Element, gen_DVE_model_NamedDeclaration_Declaration, gen_DVE_model_CompositeDeclaration_NamedDeclaration, gen_DVE_model_System_CompositeDeclaration, gen_DVE_model_State_NamedDeclaration, gen_DVE_model_Transition_Declaration, gen_DVE_model_Synchronization_Element, gen_DVE_model_ConstantDeclaration_VariableDeclaration, gen_DVE_model_ChannelDeclaration_NamedDeclaration, gen_DVE_model_TypedChannelDeclaration_ChannelDeclaration, gen_DVE_model_Process_CompositeDeclaration, gen_DVE_model_BinaryExpression_Expression, gen_DVE_model_InputSynchronization_Synchronization, gen_DVE_model_OutputSynchronization_Synchronization, gen_DVE_model_SystemProperties_Element, gen_DVE_model_Assignment_Element, gen_DVE_model_SystemType_Element, gen_DVE_model_Synchronous_SystemType, gen_DVE_model_Asynchronous_SystemType, gen_DVE_model_Expression_Element, gen_DVE_model_UnaryExpression_Expression, gen_DVE_model_PrefixedReference_Expression, gen_DVE_model_ProcessVariableReference_model_VariableReference, gen_DVE_model_ProcessVariableReference_model_PrefixedReference, gen_DVE_model_ProcessStateReference_model_StateReference, gen_DVE_model_ProcessStateReference_model_PrefixedReference, gen_DVE_model_IndexedExpression_Expression, gen_DVE_model_Reference_Expression, gen_DVE_model_VariableReference_Reference, gen_DVE_model_ChannelReference_Reference, gen_DVE_model_ProcessReference_Reference, gen_DVE_model_StateReference_Reference, gen_DVE_model_Literal_Expression, gen_DVE_model_BooleanLiteral_Literal, gen_DVE_model_TrueLiteral_BooleanLiteral, gen_DVE_model_FalseLiteral_BooleanLiteral, gen_DVE_model_NumberLiteral_Literal, gen_DVE_model_ArrayLiteral_Literal},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)