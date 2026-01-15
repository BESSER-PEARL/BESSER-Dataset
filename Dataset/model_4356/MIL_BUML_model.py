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
mil_Instruction = Class(name="mil::Instruction", is_abstract=True)
Statement = Class(name="Statement")
mil_LoadInstruction = Class(name="mil::LoadInstruction")
Instruction = Class(name="Instruction")
mil_Value = Class(name="mil::Value", is_abstract=True)
mil_StoreInstruction = Class(name="mil::StoreInstruction")
UnaryOperation = Class(name="UnaryOperation")
mil_RegisterReference = Class(name="mil::RegisterReference")
mil_AddInstruction = Class(name="mil::AddInstruction")
BinaryOperation = Class(name="BinaryOperation")
mil_ConstantInteger = Class(name="mil::ConstantInteger")
Value = Class(name="Value")
mil_MultInstruction = Class(name="mil::MultInstruction")
mil_SubInstruction = Class(name="mil::SubInstruction")
mil_DivInstruction = Class(name="mil::DivInstruction")
mil_BinaryOperation = Class(name="mil::BinaryOperation", is_abstract=True)
mil_MILModel = Class(name="mil::MILModel")
mil_Statement = Class(name="mil::Statement", is_abstract=True)
mil_LowerThanComparison = Class(name="mil::LowerThanComparison")
mil_LowerEqualsComparison = Class(name="mil::LowerEqualsComparison")
mil_GreaterThanComparison = Class(name="mil::GreaterThanComparison")
mil_GreaterEqualsComparison = Class(name="mil::GreaterEqualsComparison")
mil_YieldInstruction = Class(name="mil::YieldInstruction")
mil_PrintInstruction = Class(name="mil::PrintInstruction")
mil_JumpMarker = Class(name="mil::JumpMarker")
mil_Jumper = Class(name="mil::Jumper", is_abstract=True)
mil_CallInstruction = Class(name="mil::CallInstruction")
mil_ReturnInstruction = Class(name="mil::ReturnInstruction")
mil_UnaryOperation = Class(name="mil::UnaryOperation", is_abstract=True)
mil_NegateInstruction = Class(name="mil::NegateInstruction")
mil_JumpInstruction = Class(name="mil::JumpInstruction")
Jumper = Class(name="Jumper")
mil_ConditionalJumpInstruction = Class(name="mil::ConditionalJumpInstruction")
mil_Comparison = Class(name="mil::Comparison", is_abstract=True)
mil_EqualsComparison = Class(name="mil::EqualsComparison")
Comparison = Class(name="Comparison")
mil_NotEqualsComparison = Class(name="mil::NotEqualsComparison")

# mil_Instruction class attributes and methods

# Statement class attributes and methods

# mil_LoadInstruction class attributes and methods

# Instruction class attributes and methods

# mil_Value class attributes and methods

# mil_StoreInstruction class attributes and methods

# UnaryOperation class attributes and methods

# mil_RegisterReference class attributes and methods
mil_RegisterReference_address: Property = Property(name="address", type=StringType)
mil_RegisterReference.attributes={mil_RegisterReference_address}

# mil_AddInstruction class attributes and methods

# BinaryOperation class attributes and methods

# mil_ConstantInteger class attributes and methods
mil_ConstantInteger_rawValue: Property = Property(name="rawValue", type=IntegerType)
mil_ConstantInteger.attributes={mil_ConstantInteger_rawValue}

# Value class attributes and methods

# mil_MultInstruction class attributes and methods

# mil_SubInstruction class attributes and methods

# mil_DivInstruction class attributes and methods

# mil_BinaryOperation class attributes and methods

# mil_MILModel class attributes and methods

# mil_Statement class attributes and methods

# mil_LowerThanComparison class attributes and methods

# mil_LowerEqualsComparison class attributes and methods

# mil_GreaterThanComparison class attributes and methods

# mil_GreaterEqualsComparison class attributes and methods

# mil_YieldInstruction class attributes and methods

# mil_PrintInstruction class attributes and methods
mil_PrintInstruction_text: Property = Property(name="text", type=StringType)
mil_PrintInstruction.attributes={mil_PrintInstruction_text}

# mil_JumpMarker class attributes and methods
mil_JumpMarker_name: Property = Property(name="name", type=StringType)
mil_JumpMarker.attributes={mil_JumpMarker_name}

# mil_Jumper class attributes and methods

# mil_CallInstruction class attributes and methods

# mil_ReturnInstruction class attributes and methods

# mil_UnaryOperation class attributes and methods

# mil_NegateInstruction class attributes and methods

# mil_JumpInstruction class attributes and methods

# Jumper class attributes and methods

# mil_ConditionalJumpInstruction class attributes and methods

# mil_Comparison class attributes and methods

# mil_EqualsComparison class attributes and methods

# Comparison class attributes and methods

# mil_NotEqualsComparison class attributes and methods

# Relationships
value1: BinaryAssociation = BinaryAssociation(
    name="value1",
    ends={
        Property(name="mil_Value", type=mil_LoadInstruction, multiplicity=Multiplicity(1, 1)),
        Property(name="mil_LoadInstruction", type=mil_Value, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
registerReference2: BinaryAssociation = BinaryAssociation(
    name="registerReference2",
    ends={
        Property(name="mil_RegisterReference", type=mil_StoreInstruction, multiplicity=Multiplicity(1, 1)),
        Property(name="mil_StoreInstruction", type=mil_RegisterReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements0: BinaryAssociation = BinaryAssociation(
    name="statements0",
    ends={
        Property(name="mil_Statement", type=mil_MILModel, multiplicity=Multiplicity(1, 1)),
        Property(name="mil_MILModel", type=mil_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
jumpTarget3: BinaryAssociation = BinaryAssociation(
    name="jumpTarget3",
    ends={
        Property(name="mil_JumpMarker", type=mil_Jumper, multiplicity=Multiplicity(1, 1)),
        Property(name="mil_Jumper", type=mil_JumpMarker, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_mil_Instruction_Statement = Generalization(general=Statement, specific=mil_Instruction)
gen_mil_LoadInstruction_Instruction = Generalization(general=Instruction, specific=mil_LoadInstruction)
gen_mil_StoreInstruction_UnaryOperation = Generalization(general=UnaryOperation, specific=mil_StoreInstruction)
gen_mil_AddInstruction_BinaryOperation = Generalization(general=BinaryOperation, specific=mil_AddInstruction)
gen_mil_ConstantInteger_Value = Generalization(general=Value, specific=mil_ConstantInteger)
gen_mil_RegisterReference_Value = Generalization(general=Value, specific=mil_RegisterReference)
gen_mil_MultInstruction_BinaryOperation = Generalization(general=BinaryOperation, specific=mil_MultInstruction)
gen_mil_SubInstruction_BinaryOperation = Generalization(general=BinaryOperation, specific=mil_SubInstruction)
gen_mil_DivInstruction_BinaryOperation = Generalization(general=BinaryOperation, specific=mil_DivInstruction)
gen_mil_BinaryOperation_Instruction = Generalization(general=Instruction, specific=mil_BinaryOperation)
gen_mil_LowerThanComparison_Comparison = Generalization(general=Comparison, specific=mil_LowerThanComparison)
gen_mil_LowerEqualsComparison_Comparison = Generalization(general=Comparison, specific=mil_LowerEqualsComparison)
gen_mil_GreaterThanComparison_Comparison = Generalization(general=Comparison, specific=mil_GreaterThanComparison)
gen_mil_GreaterEqualsComparison_Comparison = Generalization(general=Comparison, specific=mil_GreaterEqualsComparison)
gen_mil_YieldInstruction_UnaryOperation = Generalization(general=UnaryOperation, specific=mil_YieldInstruction)
gen_mil_PrintInstruction_Instruction = Generalization(general=Instruction, specific=mil_PrintInstruction)
gen_mil_JumpMarker_Statement = Generalization(general=Statement, specific=mil_JumpMarker)
gen_mil_CallInstruction_Jumper = Generalization(general=Jumper, specific=mil_CallInstruction)
gen_mil_CallInstruction_Instruction = Generalization(general=Instruction, specific=mil_CallInstruction)
gen_mil_ReturnInstruction_Instruction = Generalization(general=Instruction, specific=mil_ReturnInstruction)
gen_mil_UnaryOperation_Instruction = Generalization(general=Instruction, specific=mil_UnaryOperation)
gen_mil_NegateInstruction_UnaryOperation = Generalization(general=UnaryOperation, specific=mil_NegateInstruction)
gen_mil_JumpInstruction_Instruction = Generalization(general=Instruction, specific=mil_JumpInstruction)
gen_mil_JumpInstruction_Jumper = Generalization(general=Jumper, specific=mil_JumpInstruction)
gen_mil_ConditionalJumpInstruction_UnaryOperation = Generalization(general=UnaryOperation, specific=mil_ConditionalJumpInstruction)
gen_mil_ConditionalJumpInstruction_Jumper = Generalization(general=Jumper, specific=mil_ConditionalJumpInstruction)
gen_mil_Comparison_BinaryOperation = Generalization(general=BinaryOperation, specific=mil_Comparison)
gen_mil_EqualsComparison_Comparison = Generalization(general=Comparison, specific=mil_EqualsComparison)
gen_mil_NotEqualsComparison_Comparison = Generalization(general=Comparison, specific=mil_NotEqualsComparison)

# Domain Model
domain_model = DomainModel(
    name="mil",
    types={mil_Instruction, Statement, mil_LoadInstruction, Instruction, mil_Value, mil_StoreInstruction, UnaryOperation, mil_RegisterReference, mil_AddInstruction, BinaryOperation, mil_ConstantInteger, Value, mil_MultInstruction, mil_SubInstruction, mil_DivInstruction, mil_BinaryOperation, mil_MILModel, mil_Statement, mil_LowerThanComparison, mil_LowerEqualsComparison, mil_GreaterThanComparison, mil_GreaterEqualsComparison, mil_YieldInstruction, mil_PrintInstruction, mil_JumpMarker, mil_Jumper, mil_CallInstruction, mil_ReturnInstruction, mil_UnaryOperation, mil_NegateInstruction, mil_JumpInstruction, Jumper, mil_ConditionalJumpInstruction, mil_Comparison, mil_EqualsComparison, Comparison, mil_NotEqualsComparison},
    associations={value1, registerReference2, statements0, jumpTarget3},
    generalizations={gen_mil_Instruction_Statement, gen_mil_LoadInstruction_Instruction, gen_mil_StoreInstruction_UnaryOperation, gen_mil_AddInstruction_BinaryOperation, gen_mil_ConstantInteger_Value, gen_mil_RegisterReference_Value, gen_mil_MultInstruction_BinaryOperation, gen_mil_SubInstruction_BinaryOperation, gen_mil_DivInstruction_BinaryOperation, gen_mil_BinaryOperation_Instruction, gen_mil_LowerThanComparison_Comparison, gen_mil_LowerEqualsComparison_Comparison, gen_mil_GreaterThanComparison_Comparison, gen_mil_GreaterEqualsComparison_Comparison, gen_mil_YieldInstruction_UnaryOperation, gen_mil_PrintInstruction_Instruction, gen_mil_JumpMarker_Statement, gen_mil_CallInstruction_Jumper, gen_mil_CallInstruction_Instruction, gen_mil_ReturnInstruction_Instruction, gen_mil_UnaryOperation_Instruction, gen_mil_NegateInstruction_UnaryOperation, gen_mil_JumpInstruction_Instruction, gen_mil_JumpInstruction_Jumper, gen_mil_ConditionalJumpInstruction_UnaryOperation, gen_mil_ConditionalJumpInstruction_Jumper, gen_mil_Comparison_BinaryOperation, gen_mil_EqualsComparison_Comparison, gen_mil_NotEqualsComparison_Comparison},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)