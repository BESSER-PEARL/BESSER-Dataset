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
VHDLModel_AndGate = Class(name="VHDLModel::AndGate")
BinaryGate = Class(name="BinaryGate")
VHDLModel_BinaryGate = Class(name="VHDLModel::BinaryGate", is_abstract=True)
Block = Class(name="Block")
VHDLModel_InputPort = Class(name="VHDLModel::InputPort")
VHDLModel_Block = Class(name="VHDLModel::Block", is_abstract=True)
VHDLModel_BlockRef = Class(name="VHDLModel::BlockRef")
ComplexBlock = Class(name="ComplexBlock")
VHDLModel_CompositeBlock = Class(name="VHDLModel::CompositeBlock")
VHDLModel_ComplexBlock = Class(name="VHDLModel::ComplexBlock", is_abstract=True)
VHDLModel_Port = Class(name="VHDLModel::Port", is_abstract=True)
VHDLModel_OutputPort = Class(name="VHDLModel::OutputPort")
VHDLModel_NotGate = Class(name="VHDLModel::NotGate")
VHDLModel_OrGate = Class(name="VHDLModel::OrGate")
Port = Class(name="Port")
VHDLModel_Signal = Class(name="VHDLModel::Signal")
VHDLModel_VHDLSpecification = Class(name="VHDLModel::VHDLSpecification")

# VHDLModel_AndGate class attributes and methods

# BinaryGate class attributes and methods

# VHDLModel_BinaryGate class attributes and methods

# Block class attributes and methods

# VHDLModel_InputPort class attributes and methods

# VHDLModel_Block class attributes and methods
VHDLModel_Block_name: Property = Property(name="name", type=StringType)
VHDLModel_Block.attributes={VHDLModel_Block_name}

# VHDLModel_BlockRef class attributes and methods

# ComplexBlock class attributes and methods

# VHDLModel_CompositeBlock class attributes and methods

# VHDLModel_ComplexBlock class attributes and methods

# VHDLModel_Port class attributes and methods
VHDLModel_Port_name: Property = Property(name="name", type=StringType)
VHDLModel_Port_high: Property = Property(name="high", type=BooleanType)
VHDLModel_Port.attributes={VHDLModel_Port_name, VHDLModel_Port_high}

# VHDLModel_OutputPort class attributes and methods

# VHDLModel_NotGate class attributes and methods

# VHDLModel_OrGate class attributes and methods

# Port class attributes and methods

# VHDLModel_Signal class attributes and methods

# VHDLModel_VHDLSpecification class attributes and methods
VHDLModel_VHDLSpecification_name: Property = Property(name="name", type=StringType)
VHDLModel_VHDLSpecification.attributes={VHDLModel_VHDLSpecification_name}

# Relationships
inputport20: BinaryAssociation = BinaryAssociation(
    name="inputport20",
    ends={
        Property(name="VHDLModel_InputPort", type=VHDLModel_BinaryGate, multiplicity=Multiplicity(1, 1)),
        Property(name="VHDLModel_BinaryGate", type=VHDLModel_InputPort, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
inputs6: BinaryAssociation = BinaryAssociation(
    name="inputs6",
    ends={
        Property(name="VHDLModel_InputPort7", type=VHDLModel_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="VHDLModel_Block", type=VHDLModel_InputPort, multiplicity=Multiplicity(0, 9999))
    }
)
block8: BinaryAssociation = BinaryAssociation(
    name="block8",
    ends={
        Property(name="VHDLModel_CompositeBlock", type=VHDLModel_BlockRef, multiplicity=Multiplicity(1, 1)),
        Property(name="VHDLModel_BlockRef", type=VHDLModel_CompositeBlock, multiplicity=Multiplicity(1, 1))
    }
)
ports9: BinaryAssociation = BinaryAssociation(
    name="ports9",
    ends={
        Property(name="VHDLModel_Port", type=VHDLModel_ComplexBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="VHDLModel_ComplexBlock", type=VHDLModel_Port, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputport11: BinaryAssociation = BinaryAssociation(
    name="inputport11",
    ends={
        Property(name="VHDLModel_InputPort3", type=VHDLModel_BinaryGate, multiplicity=Multiplicity(1, 1)),
        Property(name="VHDLModel_BinaryGate2", type=VHDLModel_InputPort, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
outputport4: BinaryAssociation = BinaryAssociation(
    name="outputport4",
    ends={
        Property(name="VHDLModel_OutputPort", type=VHDLModel_BinaryGate, multiplicity=Multiplicity(1, 1)),
        Property(name="VHDLModel_BinaryGate5", type=VHDLModel_OutputPort, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
outputport13: BinaryAssociation = BinaryAssociation(
    name="outputport13",
    ends={
        Property(name="VHDLModel_OutputPort14", type=VHDLModel_NotGate, multiplicity=Multiplicity(1, 1)),
        Property(name="VHDLModel_NotGate", type=VHDLModel_OutputPort, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
inputport15: BinaryAssociation = BinaryAssociation(
    name="inputport15",
    ends={
        Property(name="VHDLModel_InputPort17", type=VHDLModel_NotGate, multiplicity=Multiplicity(1, 1)),
        Property(name="VHDLModel_NotGate16", type=VHDLModel_InputPort, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
src19: BinaryAssociation = BinaryAssociation(
    name="src19",
    ends={
        Property(name="VHDLModel_Port20", type=VHDLModel_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="VHDLModel_Port18", type=VHDLModel_Port, multiplicity=Multiplicity(0, 1))
    }
)
block21: BinaryAssociation = BinaryAssociation(
    name="block21",
    ends={
        Property(name="VHDLModel_Block23", type=VHDLModel_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="VHDLModel_Port22", type=VHDLModel_Block, multiplicity=Multiplicity(1, 1))
    }
)
blocks10: BinaryAssociation = BinaryAssociation(
    name="blocks10",
    ends={
        Property(name="VHDLModel_Block12", type=VHDLModel_CompositeBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="VHDLModel_CompositeBlock11", type=VHDLModel_Block, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
blocks24: BinaryAssociation = BinaryAssociation(
    name="blocks24",
    ends={
        Property(name="VHDLModel_CompositeBlock25", type=VHDLModel_VHDLSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="VHDLModel_VHDLSpecification", type=VHDLModel_CompositeBlock, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_VHDLModel_AndGate_BinaryGate = Generalization(general=BinaryGate, specific=VHDLModel_AndGate)
gen_VHDLModel_BinaryGate_Block = Generalization(general=Block, specific=VHDLModel_BinaryGate)
gen_VHDLModel_BlockRef_ComplexBlock = Generalization(general=ComplexBlock, specific=VHDLModel_BlockRef)
gen_VHDLModel_ComplexBlock_Block = Generalization(general=Block, specific=VHDLModel_ComplexBlock)
gen_VHDLModel_NotGate_Block = Generalization(general=Block, specific=VHDLModel_NotGate)
gen_VHDLModel_OrGate_BinaryGate = Generalization(general=BinaryGate, specific=VHDLModel_OrGate)
gen_VHDLModel_OutputPort_Port = Generalization(general=Port, specific=VHDLModel_OutputPort)
gen_VHDLModel_CompositeBlock_ComplexBlock = Generalization(general=ComplexBlock, specific=VHDLModel_CompositeBlock)
gen_VHDLModel_InputPort_Port = Generalization(general=Port, specific=VHDLModel_InputPort)
gen_VHDLModel_Signal_Port = Generalization(general=Port, specific=VHDLModel_Signal)

# Domain Model
domain_model = DomainModel(
    name="VHDLModel",
    types={VHDLModel_AndGate, BinaryGate, VHDLModel_BinaryGate, Block, VHDLModel_InputPort, VHDLModel_Block, VHDLModel_BlockRef, ComplexBlock, VHDLModel_CompositeBlock, VHDLModel_ComplexBlock, VHDLModel_Port, VHDLModel_OutputPort, VHDLModel_NotGate, VHDLModel_OrGate, Port, VHDLModel_Signal, VHDLModel_VHDLSpecification},
    associations={inputport20, inputs6, block8, ports9, inputport11, outputport4, outputport13, inputport15, src19, block21, blocks10, blocks24},
    generalizations={gen_VHDLModel_AndGate_BinaryGate, gen_VHDLModel_BinaryGate_Block, gen_VHDLModel_BlockRef_ComplexBlock, gen_VHDLModel_ComplexBlock_Block, gen_VHDLModel_NotGate_Block, gen_VHDLModel_OrGate_BinaryGate, gen_VHDLModel_OutputPort_Port, gen_VHDLModel_CompositeBlock_ComplexBlock, gen_VHDLModel_InputPort_Port, gen_VHDLModel_Signal_Port},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)