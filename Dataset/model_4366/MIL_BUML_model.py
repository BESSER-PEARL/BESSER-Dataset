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
mil_LoadInstruction = Class(name="mil_LoadInstruction")
Instruction = Class(name="Instruction")
mil_Value = Class(name="mil_Value", is_abstract=True)
mil_StoreInstruction = Class(name="mil_StoreInstruction")
mil_RegisterReference = Class(name="mil_RegisterReference")
mil_AddInstruction = Class(name="mil_AddInstruction")
mil_SubInstruction = Class(name="mil_SubInstruction")
mil_MulInstruction = Class(name="mil_MulInstruction")
mil_DivInstruction = Class(name="mil_DivInstruction")
mil_MILModel = Class(name="mil_MILModel")
mil_Instruction = Class(name="mil_Instruction", is_abstract=True)
mil_NegInstruction = Class(name="mil_NegInstruction")
mil_EqInstruction = Class(name="mil_EqInstruction")
mil_NeqInstruction = Class(name="mil_NeqInstruction")
mil_LtInstruction = Class(name="mil_LtInstruction")
mil_LeqInstruction = Class(name="mil_LeqInstruction")
mil_GtInstruction = Class(name="mil_GtInstruction")
mil_GeqInstruction = Class(name="mil_GeqInstruction")
mil_JumpInstruction = Class(name="mil_JumpInstruction", is_abstract=True)
mil_LabelInstruction = Class(name="mil_LabelInstruction")
mil_JmpInstruction = Class(name="mil_JmpInstruction")
JumpInstruction = Class(name="JumpInstruction")
mil_JpcInstruction = Class(name="mil_JpcInstruction")
mil_CalInstruction = Class(name="mil_CalInstruction")
mil_RetInstruction = Class(name="mil_RetInstruction")
mil_YldInstruction = Class(name="mil_YldInstruction")
mil_PrtInstruction = Class(name="mil_PrtInstruction")
mil_InpInstruction = Class(name="mil_InpInstruction")
mil_ConstantInteger = Class(name="mil_ConstantInteger")
mil_ErrInstruction = Class(name="mil_ErrInstruction")
PrtInstruction = Class(name="PrtInstruction")
Value = Class(name="Value")

# mil_LoadInstruction class attributes and methods

# Instruction class attributes and methods

# mil_Value class attributes and methods

# mil_StoreInstruction class attributes and methods

# mil_RegisterReference class attributes and methods
mil_RegisterReference_address: Property = Property(name="address", type=StringType)
mil_RegisterReference.attributes={mil_RegisterReference_address}

# mil_AddInstruction class attributes and methods

# mil_SubInstruction class attributes and methods

# mil_MulInstruction class attributes and methods

# mil_DivInstruction class attributes and methods

# mil_MILModel class attributes and methods

# mil_Instruction class attributes and methods

# mil_NegInstruction class attributes and methods

# mil_EqInstruction class attributes and methods

# mil_NeqInstruction class attributes and methods

# mil_LtInstruction class attributes and methods

# mil_LeqInstruction class attributes and methods

# mil_GtInstruction class attributes and methods

# mil_GeqInstruction class attributes and methods

# mil_JumpInstruction class attributes and methods

# mil_LabelInstruction class attributes and methods
mil_LabelInstruction_name: Property = Property(name="name", type=StringType)
mil_LabelInstruction.attributes={mil_LabelInstruction_name}

# mil_JmpInstruction class attributes and methods

# JumpInstruction class attributes and methods

# mil_JpcInstruction class attributes and methods

# mil_CalInstruction class attributes and methods

# mil_RetInstruction class attributes and methods

# mil_YldInstruction class attributes and methods

# mil_PrtInstruction class attributes and methods
mil_PrtInstruction_value: Property = Property(name="value", type=StringType)
mil_PrtInstruction.attributes={mil_PrtInstruction_value}

# mil_InpInstruction class attributes and methods

# mil_ConstantInteger class attributes and methods
mil_ConstantInteger_rawValue: Property = Property(name="rawValue", type=IntegerType)
mil_ConstantInteger.attributes={mil_ConstantInteger_rawValue}

# mil_ErrInstruction class attributes and methods

# PrtInstruction class attributes and methods

# Value class attributes and methods

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
instructions0: BinaryAssociation = BinaryAssociation(
    name="instructions0",
    ends={
        Property(name="mil_Instruction", type=mil_MILModel, multiplicity=Multiplicity(1, 1)),
        Property(name="mil_MILModel", type=mil_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
label3: BinaryAssociation = BinaryAssociation(
    name="label3",
    ends={
        Property(name="mil_LabelInstruction", type=mil_JumpInstruction, multiplicity=Multiplicity(1, 1)),
        Property(name="mil_JumpInstruction", type=mil_LabelInstruction, multiplicity=Multiplicity(1, 1))
    }
)
lowerBound4: BinaryAssociation = BinaryAssociation(
    name="lowerBound4",
    ends={
        Property(name="mil_ConstantInteger", type=mil_InpInstruction, multiplicity=Multiplicity(1, 1)),
        Property(name="mil_InpInstruction", type=mil_ConstantInteger, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
upperBound5: BinaryAssociation = BinaryAssociation(
    name="upperBound5",
    ends={
        Property(name="mil_ConstantInteger7", type=mil_InpInstruction, multiplicity=Multiplicity(1, 1)),
        Property(name="mil_InpInstruction6", type=mil_ConstantInteger, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_mil_LoadInstruction_Instruction = Generalization(general=Instruction, specific=mil_LoadInstruction)
gen_mil_StoreInstruction_Instruction = Generalization(general=Instruction, specific=mil_StoreInstruction)
gen_mil_AddInstruction_Instruction = Generalization(general=Instruction, specific=mil_AddInstruction)
gen_mil_SubInstruction_Instruction = Generalization(general=Instruction, specific=mil_SubInstruction)
gen_mil_MulInstruction_Instruction = Generalization(general=Instruction, specific=mil_MulInstruction)
gen_mil_DivInstruction_Instruction = Generalization(general=Instruction, specific=mil_DivInstruction)
gen_mil_RegisterReference_Value = Generalization(general=Value, specific=mil_RegisterReference)
gen_mil_NegInstruction_Instruction = Generalization(general=Instruction, specific=mil_NegInstruction)
gen_mil_EqInstruction_Instruction = Generalization(general=Instruction, specific=mil_EqInstruction)
gen_mil_NeqInstruction_Instruction = Generalization(general=Instruction, specific=mil_NeqInstruction)
gen_mil_LtInstruction_Instruction = Generalization(general=Instruction, specific=mil_LtInstruction)
gen_mil_LeqInstruction_Instruction = Generalization(general=Instruction, specific=mil_LeqInstruction)
gen_mil_GtInstruction_Instruction = Generalization(general=Instruction, specific=mil_GtInstruction)
gen_mil_GeqInstruction_Instruction = Generalization(general=Instruction, specific=mil_GeqInstruction)
gen_mil_JumpInstruction_Instruction = Generalization(general=Instruction, specific=mil_JumpInstruction)
gen_mil_JmpInstruction_JumpInstruction = Generalization(general=JumpInstruction, specific=mil_JmpInstruction)
gen_mil_JpcInstruction_JumpInstruction = Generalization(general=JumpInstruction, specific=mil_JpcInstruction)
gen_mil_CalInstruction_JumpInstruction = Generalization(general=JumpInstruction, specific=mil_CalInstruction)
gen_mil_RetInstruction_Instruction = Generalization(general=Instruction, specific=mil_RetInstruction)
gen_mil_LabelInstruction_Instruction = Generalization(general=Instruction, specific=mil_LabelInstruction)
gen_mil_YldInstruction_Instruction = Generalization(general=Instruction, specific=mil_YldInstruction)
gen_mil_PrtInstruction_Instruction = Generalization(general=Instruction, specific=mil_PrtInstruction)
gen_mil_InpInstruction_Instruction = Generalization(general=Instruction, specific=mil_InpInstruction)
gen_mil_ErrInstruction_PrtInstruction = Generalization(general=PrtInstruction, specific=mil_ErrInstruction)
gen_mil_ConstantInteger_Value = Generalization(general=Value, specific=mil_ConstantInteger)

# Domain Model
domain_model = DomainModel(
    name="mil",
    types={mil_LoadInstruction, Instruction, mil_Value, mil_StoreInstruction, mil_RegisterReference, mil_AddInstruction, mil_SubInstruction, mil_MulInstruction, mil_DivInstruction, mil_MILModel, mil_Instruction, mil_NegInstruction, mil_EqInstruction, mil_NeqInstruction, mil_LtInstruction, mil_LeqInstruction, mil_GtInstruction, mil_GeqInstruction, mil_JumpInstruction, mil_LabelInstruction, mil_JmpInstruction, JumpInstruction, mil_JpcInstruction, mil_CalInstruction, mil_RetInstruction, mil_YldInstruction, mil_PrtInstruction, mil_InpInstruction, mil_ConstantInteger, mil_ErrInstruction, PrtInstruction, Value},
    associations={value1, registerReference2, instructions0, label3, lowerBound4, upperBound5},
    generalizations={gen_mil_LoadInstruction_Instruction, gen_mil_StoreInstruction_Instruction, gen_mil_AddInstruction_Instruction, gen_mil_SubInstruction_Instruction, gen_mil_MulInstruction_Instruction, gen_mil_DivInstruction_Instruction, gen_mil_RegisterReference_Value, gen_mil_NegInstruction_Instruction, gen_mil_EqInstruction_Instruction, gen_mil_NeqInstruction_Instruction, gen_mil_LtInstruction_Instruction, gen_mil_LeqInstruction_Instruction, gen_mil_GtInstruction_Instruction, gen_mil_GeqInstruction_Instruction, gen_mil_JumpInstruction_Instruction, gen_mil_JmpInstruction_JumpInstruction, gen_mil_JpcInstruction_JumpInstruction, gen_mil_CalInstruction_JumpInstruction, gen_mil_RetInstruction_Instruction, gen_mil_LabelInstruction_Instruction, gen_mil_YldInstruction_Instruction, gen_mil_PrtInstruction_Instruction, gen_mil_InpInstruction_Instruction, gen_mil_ErrInstruction_PrtInstruction, gen_mil_ConstantInteger_Value},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)