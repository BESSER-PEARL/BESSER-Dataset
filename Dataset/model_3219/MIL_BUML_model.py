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
mil_LabelInstruction = Class(name="mil::LabelInstruction")
Instruction = Class(name="Instruction")
mil_LoadInstruction = Class(name="mil::LoadInstruction")
mil_Value = Class(name="mil::Value", is_abstract=True)
mil_StoreInstruction = Class(name="mil::StoreInstruction")
mil_MILModel = Class(name="mil::MILModel")
mil_Instruction = Class(name="mil::Instruction", is_abstract=True)
mil_ConstantInteger = Class(name="mil::ConstantInteger")
Value = Class(name="Value")
mil_RegisterReference = Class(name="mil::RegisterReference")
mil_NegateInstruction = Class(name="mil::NegateInstruction")
mil_JumpInstruction = Class(name="mil::JumpInstruction", is_abstract=True)
mil_UnconditionalJumpInstruction = Class(name="mil::UnconditionalJumpInstruction")
JumpInstruction = Class(name="JumpInstruction")
mil_ConditionalJumpInstruction = Class(name="mil::ConditionalJumpInstruction")
mil_CompareInstruction = Class(name="mil::CompareInstruction", is_abstract=True)
mil_EqualInstruction = Class(name="mil::EqualInstruction")
CompareInstruction = Class(name="CompareInstruction")
mil_NotEqualInstruction = Class(name="mil::NotEqualInstruction")
mil_LessThanInstruction = Class(name="mil::LessThanInstruction")
mil_LessThanEqualInstruction = Class(name="mil::LessThanEqualInstruction")
mil_GreaterThanInstruction = Class(name="mil::GreaterThanInstruction")
mil_GreaterThanEqualInstruction = Class(name="mil::GreaterThanEqualInstruction")
mil_OutputInstruction = Class(name="mil::OutputInstruction", is_abstract=True)
mil_YieldInstruciton = Class(name="mil::YieldInstruciton")
OutputInstruction = Class(name="OutputInstruction")
mil_PrintInstruction = Class(name="mil::PrintInstruction")
mil_ArithmeticInstruction = Class(name="mil::ArithmeticInstruction", is_abstract=True)
mil_AddInstruction = Class(name="mil::AddInstruction")
ArithmeticInstruction = Class(name="ArithmeticInstruction")
mil_SubInstruction = Class(name="mil::SubInstruction")
mil_MulInstruction = Class(name="mil::MulInstruction")
mil_DivInstruction = Class(name="mil::DivInstruction")
mil_CallInstruction = Class(name="mil::CallInstruction")
mil_ReturnInstruction = Class(name="mil::ReturnInstruction")

# mil_LabelInstruction class attributes and methods
mil_LabelInstruction_name: Property = Property(name="name", type=StringType)
mil_LabelInstruction.attributes={mil_LabelInstruction_name}

# Instruction class attributes and methods

# mil_LoadInstruction class attributes and methods

# mil_Value class attributes and methods

# mil_StoreInstruction class attributes and methods

# mil_MILModel class attributes and methods

# mil_Instruction class attributes and methods

# mil_ConstantInteger class attributes and methods
mil_ConstantInteger_rawValue: Property = Property(name="rawValue", type=IntegerType)
mil_ConstantInteger.attributes={mil_ConstantInteger_rawValue}

# Value class attributes and methods

# mil_RegisterReference class attributes and methods
mil_RegisterReference_address: Property = Property(name="address", type=StringType)
mil_RegisterReference.attributes={mil_RegisterReference_address}

# mil_NegateInstruction class attributes and methods

# mil_JumpInstruction class attributes and methods

# mil_UnconditionalJumpInstruction class attributes and methods

# JumpInstruction class attributes and methods

# mil_ConditionalJumpInstruction class attributes and methods

# mil_CompareInstruction class attributes and methods

# mil_EqualInstruction class attributes and methods

# CompareInstruction class attributes and methods

# mil_NotEqualInstruction class attributes and methods

# mil_LessThanInstruction class attributes and methods

# mil_LessThanEqualInstruction class attributes and methods

# mil_GreaterThanInstruction class attributes and methods

# mil_GreaterThanEqualInstruction class attributes and methods

# mil_OutputInstruction class attributes and methods

# mil_YieldInstruciton class attributes and methods

# OutputInstruction class attributes and methods

# mil_PrintInstruction class attributes and methods
mil_PrintInstruction_output: Property = Property(name="output", type=StringType)
mil_PrintInstruction.attributes={mil_PrintInstruction_output}

# mil_ArithmeticInstruction class attributes and methods

# mil_AddInstruction class attributes and methods

# ArithmeticInstruction class attributes and methods

# mil_SubInstruction class attributes and methods

# mil_MulInstruction class attributes and methods

# mil_DivInstruction class attributes and methods

# mil_CallInstruction class attributes and methods

# mil_ReturnInstruction class attributes and methods

# Relationships
value1: BinaryAssociation = BinaryAssociation(
    name="value1",
    ends={
        Property(name="mil_Value", type=mil_LoadInstruction, multiplicity=Multiplicity(1, 1)),
        Property(name="mil_LoadInstruction", type=mil_Value, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
instructions0: BinaryAssociation = BinaryAssociation(
    name="instructions0",
    ends={
        Property(name="mil_Instruction", type=mil_MILModel, multiplicity=Multiplicity(1, 1)),
        Property(name="mil_MILModel", type=mil_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
registerReference2: BinaryAssociation = BinaryAssociation(
    name="registerReference2",
    ends={
        Property(name="mil_RegisterReference", type=mil_StoreInstruction, multiplicity=Multiplicity(1, 1)),
        Property(name="mil_StoreInstruction", type=mil_RegisterReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
jumpTo3: BinaryAssociation = BinaryAssociation(
    name="jumpTo3",
    ends={
        Property(name="mil_LabelInstruction", type=mil_JumpInstruction, multiplicity=Multiplicity(1, 1)),
        Property(name="mil_JumpInstruction", type=mil_LabelInstruction, multiplicity=Multiplicity(1, 1))
    }
)
operationName4: BinaryAssociation = BinaryAssociation(
    name="operationName4",
    ends={
        Property(name="mil_LabelInstruction5", type=mil_CallInstruction, multiplicity=Multiplicity(1, 1)),
        Property(name="mil_CallInstruction", type=mil_LabelInstruction, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_mil_LabelInstruction_Instruction = Generalization(general=Instruction, specific=mil_LabelInstruction)
gen_mil_LoadInstruction_Instruction = Generalization(general=Instruction, specific=mil_LoadInstruction)
gen_mil_StoreInstruction_Instruction = Generalization(general=Instruction, specific=mil_StoreInstruction)
gen_mil_ConstantInteger_Value = Generalization(general=Value, specific=mil_ConstantInteger)
gen_mil_RegisterReference_Value = Generalization(general=Value, specific=mil_RegisterReference)
gen_mil_NegateInstruction_Instruction = Generalization(general=Instruction, specific=mil_NegateInstruction)
gen_mil_JumpInstruction_Instruction = Generalization(general=Instruction, specific=mil_JumpInstruction)
gen_mil_UnconditionalJumpInstruction_JumpInstruction = Generalization(general=JumpInstruction, specific=mil_UnconditionalJumpInstruction)
gen_mil_ConditionalJumpInstruction_JumpInstruction = Generalization(general=JumpInstruction, specific=mil_ConditionalJumpInstruction)
gen_mil_CompareInstruction_Instruction = Generalization(general=Instruction, specific=mil_CompareInstruction)
gen_mil_EqualInstruction_CompareInstruction = Generalization(general=CompareInstruction, specific=mil_EqualInstruction)
gen_mil_NotEqualInstruction_CompareInstruction = Generalization(general=CompareInstruction, specific=mil_NotEqualInstruction)
gen_mil_LessThanInstruction_CompareInstruction = Generalization(general=CompareInstruction, specific=mil_LessThanInstruction)
gen_mil_LessThanEqualInstruction_CompareInstruction = Generalization(general=CompareInstruction, specific=mil_LessThanEqualInstruction)
gen_mil_GreaterThanInstruction_CompareInstruction = Generalization(general=CompareInstruction, specific=mil_GreaterThanInstruction)
gen_mil_GreaterThanEqualInstruction_CompareInstruction = Generalization(general=CompareInstruction, specific=mil_GreaterThanEqualInstruction)
gen_mil_OutputInstruction_Instruction = Generalization(general=Instruction, specific=mil_OutputInstruction)
gen_mil_YieldInstruciton_OutputInstruction = Generalization(general=OutputInstruction, specific=mil_YieldInstruciton)
gen_mil_PrintInstruction_OutputInstruction = Generalization(general=OutputInstruction, specific=mil_PrintInstruction)
gen_mil_ArithmeticInstruction_Instruction = Generalization(general=Instruction, specific=mil_ArithmeticInstruction)
gen_mil_AddInstruction_ArithmeticInstruction = Generalization(general=ArithmeticInstruction, specific=mil_AddInstruction)
gen_mil_SubInstruction_ArithmeticInstruction = Generalization(general=ArithmeticInstruction, specific=mil_SubInstruction)
gen_mil_MulInstruction_ArithmeticInstruction = Generalization(general=ArithmeticInstruction, specific=mil_MulInstruction)
gen_mil_DivInstruction_ArithmeticInstruction = Generalization(general=ArithmeticInstruction, specific=mil_DivInstruction)
gen_mil_CallInstruction_Instruction = Generalization(general=Instruction, specific=mil_CallInstruction)
gen_mil_ReturnInstruction_Instruction = Generalization(general=Instruction, specific=mil_ReturnInstruction)

# Domain Model
domain_model = DomainModel(
    name="mil",
    types={mil_LabelInstruction, Instruction, mil_LoadInstruction, mil_Value, mil_StoreInstruction, mil_MILModel, mil_Instruction, mil_ConstantInteger, Value, mil_RegisterReference, mil_NegateInstruction, mil_JumpInstruction, mil_UnconditionalJumpInstruction, JumpInstruction, mil_ConditionalJumpInstruction, mil_CompareInstruction, mil_EqualInstruction, CompareInstruction, mil_NotEqualInstruction, mil_LessThanInstruction, mil_LessThanEqualInstruction, mil_GreaterThanInstruction, mil_GreaterThanEqualInstruction, mil_OutputInstruction, mil_YieldInstruciton, OutputInstruction, mil_PrintInstruction, mil_ArithmeticInstruction, mil_AddInstruction, ArithmeticInstruction, mil_SubInstruction, mil_MulInstruction, mil_DivInstruction, mil_CallInstruction, mil_ReturnInstruction},
    associations={value1, instructions0, registerReference2, jumpTo3, operationName4},
    generalizations={gen_mil_LabelInstruction_Instruction, gen_mil_LoadInstruction_Instruction, gen_mil_StoreInstruction_Instruction, gen_mil_ConstantInteger_Value, gen_mil_RegisterReference_Value, gen_mil_NegateInstruction_Instruction, gen_mil_JumpInstruction_Instruction, gen_mil_UnconditionalJumpInstruction_JumpInstruction, gen_mil_ConditionalJumpInstruction_JumpInstruction, gen_mil_CompareInstruction_Instruction, gen_mil_EqualInstruction_CompareInstruction, gen_mil_NotEqualInstruction_CompareInstruction, gen_mil_LessThanInstruction_CompareInstruction, gen_mil_LessThanEqualInstruction_CompareInstruction, gen_mil_GreaterThanInstruction_CompareInstruction, gen_mil_GreaterThanEqualInstruction_CompareInstruction, gen_mil_OutputInstruction_Instruction, gen_mil_YieldInstruciton_OutputInstruction, gen_mil_PrintInstruction_OutputInstruction, gen_mil_ArithmeticInstruction_Instruction, gen_mil_AddInstruction_ArithmeticInstruction, gen_mil_SubInstruction_ArithmeticInstruction, gen_mil_MulInstruction_ArithmeticInstruction, gen_mil_DivInstruction_ArithmeticInstruction, gen_mil_CallInstruction_Instruction, gen_mil_ReturnInstruction_Instruction},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)