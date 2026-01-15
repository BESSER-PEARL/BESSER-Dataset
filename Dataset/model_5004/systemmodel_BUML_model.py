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
systemmodel_SMElement = Class(name="systemmodel::SMElement", is_abstract=True)
systemmodel_SystemModel = Class(name="systemmodel::SystemModel")
SMElement = Class(name="SMElement")
systemmodel_Block = Class(name="systemmodel::Block", is_abstract=True)
systemmodel_Signal = Class(name="systemmodel::Signal")
systemmodel_DataType = Class(name="systemmodel::DataType", is_abstract=True)
Port = Class(name="Port")
systemmodel_UnitDelay = Class(name="systemmodel::UnitDelay")
Block = Class(name="Block")
systemmodel_Sum = Class(name="systemmodel::Sum")
systemmodel_InputBlock = Class(name="systemmodel::InputBlock")
InterfaceBlock = Class(name="InterfaceBlock")
systemmodel_Saturation = Class(name="systemmodel::Saturation")
systemmodel_OutputBlock = Class(name="systemmodel::OutputBlock")
systemmodel_InterfaceBlock = Class(name="systemmodel::InterfaceBlock", is_abstract=True)
systemmodel_GainBlock = Class(name="systemmodel::GainBlock")
systemmodel_Inport = Class(name="systemmodel::Inport")
systemmodel_Outport = Class(name="systemmodel::Outport")
systemmodel_Port = Class(name="systemmodel::Port", is_abstract=True)
systemmodel_MatrixType = Class(name="systemmodel::MatrixType")
DataType = Class(name="DataType")
systemmodel_VectorType = Class(name="systemmodel::VectorType")
systemmodel_ScalarType = Class(name="systemmodel::ScalarType")

# systemmodel_SMElement class attributes and methods
systemmodel_SMElement_name: Property = Property(name="name", type=StringType)
systemmodel_SMElement.attributes={systemmodel_SMElement_name}

# systemmodel_SystemModel class attributes and methods

# SMElement class attributes and methods

# systemmodel_Block class attributes and methods
systemmodel_Block_sequenceNumber: Property = Property(name="sequenceNumber", type=IntegerType)
systemmodel_Block.attributes={systemmodel_Block_sequenceNumber}

# systemmodel_Signal class attributes and methods

# systemmodel_DataType class attributes and methods
systemmodel_DataType_basetype: Property = Property(name="basetype", type=StringType)
systemmodel_DataType.attributes={systemmodel_DataType_basetype}

# Port class attributes and methods

# systemmodel_UnitDelay class attributes and methods
systemmodel_UnitDelay_initialCondition: Property = Property(name="initialCondition", type=StringType)
systemmodel_UnitDelay.attributes={systemmodel_UnitDelay_initialCondition}

# Block class attributes and methods

# systemmodel_Sum class attributes and methods

# systemmodel_InputBlock class attributes and methods

# InterfaceBlock class attributes and methods

# systemmodel_Saturation class attributes and methods
systemmodel_Saturation_lowerBound: Property = Property(name="lowerBound", type=StringType)
systemmodel_Saturation_upperBound: Property = Property(name="upperBound", type=StringType)
systemmodel_Saturation.attributes={systemmodel_Saturation_lowerBound, systemmodel_Saturation_upperBound}

# systemmodel_OutputBlock class attributes and methods

# systemmodel_InterfaceBlock class attributes and methods

# systemmodel_GainBlock class attributes and methods
systemmodel_GainBlock_gainfactor: Property = Property(name="gainfactor", type=StringType)
systemmodel_GainBlock.attributes={systemmodel_GainBlock_gainfactor}

# systemmodel_Inport class attributes and methods

# systemmodel_Outport class attributes and methods

# systemmodel_Port class attributes and methods

# systemmodel_MatrixType class attributes and methods
systemmodel_MatrixType_rows: Property = Property(name="rows", type=StringType)
systemmodel_MatrixType_columns: Property = Property(name="columns", type=StringType)
systemmodel_MatrixType.attributes={systemmodel_MatrixType_columns, systemmodel_MatrixType_rows}

# DataType class attributes and methods

# systemmodel_VectorType class attributes and methods
systemmodel_VectorType_size: Property = Property(name="size", type=StringType)
systemmodel_VectorType.attributes={systemmodel_VectorType_size}

# systemmodel_ScalarType class attributes and methods

# Relationships
blocks0: BinaryAssociation = BinaryAssociation(
    name="blocks0",
    ends={
        Property(name="systemmodel_Block", type=systemmodel_SystemModel, multiplicity=Multiplicity(1, 1)),
        Property(name="systemmodel_SystemModel", type=systemmodel_Block, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signals1: BinaryAssociation = BinaryAssociation(
    name="signals1",
    ends={
        Property(name="systemmodel_Signal", type=systemmodel_SystemModel, multiplicity=Multiplicity(1, 1)),
        Property(name="systemmodel_SystemModel2", type=systemmodel_Signal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataTypes3: BinaryAssociation = BinaryAssociation(
    name="dataTypes3",
    ends={
        Property(name="systemmodel_DataType", type=systemmodel_SystemModel, multiplicity=Multiplicity(1, 1)),
        Property(name="systemmodel_SystemModel4", type=systemmodel_DataType, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
srcPort8: BinaryAssociation = BinaryAssociation(
    name="srcPort8",
    ends={
        Property(name="Outport9", type=systemmodel_Signal, multiplicity=Multiplicity(1, 1)),
        Property(name="outSignals", type=systemmodel_Outport, multiplicity=Multiplicity(1, 1))
    }
)
dstPort10: BinaryAssociation = BinaryAssociation(
    name="dstPort10",
    ends={
        Property(name="Inport11", type=systemmodel_Signal, multiplicity=Multiplicity(1, 1)),
        Property(name="inSignal", type=systemmodel_Inport, multiplicity=Multiplicity(1, 1))
    }
)
inSignal12: BinaryAssociation = BinaryAssociation(
    name="inSignal12",
    ends={
        Property(name="Signal", type=systemmodel_Inport, multiplicity=Multiplicity(1, 1)),
        Property(name="dstPort", type=systemmodel_Signal, multiplicity=Multiplicity(0, 1))
    }
)
parentBlock13: BinaryAssociation = BinaryAssociation(
    name="parentBlock13",
    ends={
        Property(name="Block", type=systemmodel_Inport, multiplicity=Multiplicity(1, 1)),
        Property(name="inports", type=systemmodel_Block, multiplicity=Multiplicity(1, 1))
    }
)
outSignals14: BinaryAssociation = BinaryAssociation(
    name="outSignals14",
    ends={
        Property(name="Signal15", type=systemmodel_Outport, multiplicity=Multiplicity(1, 1)),
        Property(name="srcPort", type=systemmodel_Signal, multiplicity=Multiplicity(0, 9999))
    }
)
parentBlock16: BinaryAssociation = BinaryAssociation(
    name="parentBlock16",
    ends={
        Property(name="Block17", type=systemmodel_Outport, multiplicity=Multiplicity(1, 1)),
        Property(name="outports", type=systemmodel_Block, multiplicity=Multiplicity(1, 1))
    }
)
inports5: BinaryAssociation = BinaryAssociation(
    name="inports5",
    ends={
        Property(name="Inport", type=systemmodel_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="parentBlock", type=systemmodel_Inport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outports6: BinaryAssociation = BinaryAssociation(
    name="outports6",
    ends={
        Property(name="Outport", type=systemmodel_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="parentBlock7", type=systemmodel_Outport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type18: BinaryAssociation = BinaryAssociation(
    name="type18",
    ends={
        Property(name="systemmodel_DataType19", type=systemmodel_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="systemmodel_Port", type=systemmodel_DataType, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_systemmodel_SystemModel_SMElement = Generalization(general=SMElement, specific=systemmodel_SystemModel)
gen_systemmodel_Inport_Port = Generalization(general=Port, specific=systemmodel_Inport)
gen_systemmodel_Outport_Port = Generalization(general=Port, specific=systemmodel_Outport)
gen_systemmodel_UnitDelay_Block = Generalization(general=Block, specific=systemmodel_UnitDelay)
gen_systemmodel_Sum_Block = Generalization(general=Block, specific=systemmodel_Sum)
gen_systemmodel_InputBlock_InterfaceBlock = Generalization(general=InterfaceBlock, specific=systemmodel_InputBlock)
gen_systemmodel_Saturation_Block = Generalization(general=Block, specific=systemmodel_Saturation)
gen_systemmodel_OutputBlock_InterfaceBlock = Generalization(general=InterfaceBlock, specific=systemmodel_OutputBlock)
gen_systemmodel_InterfaceBlock_Block = Generalization(general=Block, specific=systemmodel_InterfaceBlock)
gen_systemmodel_GainBlock_Block = Generalization(general=Block, specific=systemmodel_GainBlock)
gen_systemmodel_Block_SMElement = Generalization(general=SMElement, specific=systemmodel_Block)
gen_systemmodel_Signal_SMElement = Generalization(general=SMElement, specific=systemmodel_Signal)
gen_systemmodel_ScalarType_DataType = Generalization(general=DataType, specific=systemmodel_ScalarType)
gen_systemmodel_Port_SMElement = Generalization(general=SMElement, specific=systemmodel_Port)
gen_systemmodel_DataType_SMElement = Generalization(general=SMElement, specific=systemmodel_DataType)
gen_systemmodel_MatrixType_DataType = Generalization(general=DataType, specific=systemmodel_MatrixType)
gen_systemmodel_VectorType_DataType = Generalization(general=DataType, specific=systemmodel_VectorType)

# Domain Model
domain_model = DomainModel(
    name="systemmodel",
    types={systemmodel_SMElement, systemmodel_SystemModel, SMElement, systemmodel_Block, systemmodel_Signal, systemmodel_DataType, Port, systemmodel_UnitDelay, Block, systemmodel_Sum, systemmodel_InputBlock, InterfaceBlock, systemmodel_Saturation, systemmodel_OutputBlock, systemmodel_InterfaceBlock, systemmodel_GainBlock, systemmodel_Inport, systemmodel_Outport, systemmodel_Port, systemmodel_MatrixType, DataType, systemmodel_VectorType, systemmodel_ScalarType},
    associations={blocks0, signals1, dataTypes3, srcPort8, dstPort10, inSignal12, parentBlock13, outSignals14, parentBlock16, inports5, outports6, type18},
    generalizations={gen_systemmodel_SystemModel_SMElement, gen_systemmodel_Inport_Port, gen_systemmodel_Outport_Port, gen_systemmodel_UnitDelay_Block, gen_systemmodel_Sum_Block, gen_systemmodel_InputBlock_InterfaceBlock, gen_systemmodel_Saturation_Block, gen_systemmodel_OutputBlock_InterfaceBlock, gen_systemmodel_InterfaceBlock_Block, gen_systemmodel_GainBlock_Block, gen_systemmodel_Block_SMElement, gen_systemmodel_Signal_SMElement, gen_systemmodel_ScalarType_DataType, gen_systemmodel_Port_SMElement, gen_systemmodel_DataType_SMElement, gen_systemmodel_MatrixType_DataType, gen_systemmodel_VectorType_DataType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)