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
systemmodel_Outport = Class(name="systemmodel::Outport")
systemmodel_SMElement = Class(name="systemmodel::SMElement", is_abstract=True)
systemmodel_SystemModel = Class(name="systemmodel::SystemModel")
SMElement = Class(name="SMElement")
systemmodel_Block = Class(name="systemmodel::Block", is_abstract=True)
systemmodel_Signal = Class(name="systemmodel::Signal")
systemmodel_Inport = Class(name="systemmodel::Inport")
systemmodel_UnitDelay = Class(name="systemmodel::UnitDelay")
Block = Class(name="Block")
systemmodel_Sum = Class(name="systemmodel::Sum")
systemmodel_SrcBlock = Class(name="systemmodel::SrcBlock")
systemmodel_Sum1 = Class(name="systemmodel::Sum1")
systemmodel_ModelElement = Class(name="systemmodel::ModelElement", is_abstract=True)
Sum = Class(name="Sum")
systemmodel_Sum2 = Class(name="systemmodel::Sum2")
systemmodel_Test = Class(name="systemmodel::Test")
systemmodel_A = Class(name="systemmodel::A")
ModelElement = Class(name="ModelElement")
systemmodel_B = Class(name="systemmodel::B")
systemmodel_C = Class(name="systemmodel::C")
A = Class(name="A")
systemmodel_Root = Class(name="systemmodel::Root")

# systemmodel_Outport class attributes and methods

# systemmodel_SMElement class attributes and methods

# systemmodel_SystemModel class attributes and methods

# SMElement class attributes and methods

# systemmodel_Block class attributes and methods

# systemmodel_Signal class attributes and methods

# systemmodel_Inport class attributes and methods

# systemmodel_UnitDelay class attributes and methods

# Block class attributes and methods

# systemmodel_Sum class attributes and methods

# systemmodel_SrcBlock class attributes and methods

# systemmodel_Sum1 class attributes and methods

# systemmodel_ModelElement class attributes and methods

# Sum class attributes and methods

# systemmodel_Sum2 class attributes and methods

# systemmodel_Test class attributes and methods

# systemmodel_A class attributes and methods
systemmodel_A_name: Property = Property(name="name", type=StringType)
systemmodel_A_multiValAtt: Property = Property(name="multiValAtt", type=StringType)
systemmodel_A.attributes={systemmodel_A_multiValAtt, systemmodel_A_name}

# ModelElement class attributes and methods

# systemmodel_B class attributes and methods

# systemmodel_C class attributes and methods
systemmodel_C_name: Property = Property(name="name", type=StringType)
systemmodel_C.attributes={systemmodel_C_name}

# A class attributes and methods

# systemmodel_Root class attributes and methods

# Relationships
outports5: BinaryAssociation = BinaryAssociation(
    name="outports5",
    ends={
        Property(name="Outport", type=systemmodel_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="parentBlock", type=systemmodel_Outport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
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
inports3: BinaryAssociation = BinaryAssociation(
    name="inports3",
    ends={
        Property(name="systemmodel_Inport", type=systemmodel_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="systemmodel_Block4", type=systemmodel_Inport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentBlock12: BinaryAssociation = BinaryAssociation(
    name="parentBlock12",
    ends={
        Property(name="Block", type=systemmodel_Outport, multiplicity=Multiplicity(1, 1)),
        Property(name="outports", type=systemmodel_Block, multiplicity=Multiplicity(1, 1))
    }
)
srcPort6: BinaryAssociation = BinaryAssociation(
    name="srcPort6",
    ends={
        Property(name="Outport7", type=systemmodel_Signal, multiplicity=Multiplicity(1, 1)),
        Property(name="outSignals", type=systemmodel_Outport, multiplicity=Multiplicity(1, 1))
    }
)
dstPort8: BinaryAssociation = BinaryAssociation(
    name="dstPort8",
    ends={
        Property(name="Inport", type=systemmodel_Signal, multiplicity=Multiplicity(1, 1)),
        Property(name="inSignal", type=systemmodel_Inport, multiplicity=Multiplicity(1, 1))
    }
)
inSignal9: BinaryAssociation = BinaryAssociation(
    name="inSignal9",
    ends={
        Property(name="Signal", type=systemmodel_Inport, multiplicity=Multiplicity(1, 1)),
        Property(name="dstPort", type=systemmodel_Signal, multiplicity=Multiplicity(0, 1))
    }
)
outSignals10: BinaryAssociation = BinaryAssociation(
    name="outSignals10",
    ends={
        Property(name="Signal11", type=systemmodel_Outport, multiplicity=Multiplicity(1, 1)),
        Property(name="srcPort", type=systemmodel_Signal, multiplicity=Multiplicity(0, 9999))
    }
)
elements18: BinaryAssociation = BinaryAssociation(
    name="elements18",
    ends={
        Property(name="systemmodel_ModelElement", type=systemmodel_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="systemmodel_Root", type=systemmodel_ModelElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nonUniqueOrderedRef13: BinaryAssociation = BinaryAssociation(
    name="nonUniqueOrderedRef13",
    ends={
        Property(name="systemmodel_Block14", type=systemmodel_Test, multiplicity=Multiplicity(1, 1)),
        Property(name="systemmodel_Test", type=systemmodel_Block, multiplicity=Multiplicity(0, 9999))
    }
)
refB15: BinaryAssociation = BinaryAssociation(
    name="refB15",
    ends={
        Property(name="systemmodel_B", type=systemmodel_A, multiplicity=Multiplicity(1, 1)),
        Property(name="systemmodel_A", type=systemmodel_B, multiplicity=Multiplicity(0, 9999))
    }
)
refC16: BinaryAssociation = BinaryAssociation(
    name="refC16",
    ends={
        Property(name="systemmodel_C", type=systemmodel_A, multiplicity=Multiplicity(1, 1)),
        Property(name="systemmodel_A17", type=systemmodel_C, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_systemmodel_Signal_SMElement = Generalization(general=SMElement, specific=systemmodel_Signal)
gen_systemmodel_SystemModel_SMElement = Generalization(general=SMElement, specific=systemmodel_SystemModel)
gen_systemmodel_Block_SMElement = Generalization(general=SMElement, specific=systemmodel_Block)
gen_systemmodel_UnitDelay_Block = Generalization(general=Block, specific=systemmodel_UnitDelay)
gen_systemmodel_Sum_Block = Generalization(general=Block, specific=systemmodel_Sum)
gen_systemmodel_SrcBlock_Block = Generalization(general=Block, specific=systemmodel_SrcBlock)
gen_systemmodel_Inport_SMElement = Generalization(general=SMElement, specific=systemmodel_Inport)
gen_systemmodel_Outport_SMElement = Generalization(general=SMElement, specific=systemmodel_Outport)
gen_systemmodel_Root_SMElement = Generalization(general=SMElement, specific=systemmodel_Root)
gen_systemmodel_ModelElement_SMElement = Generalization(general=SMElement, specific=systemmodel_ModelElement)
gen_systemmodel_Sum1_Sum = Generalization(general=Sum, specific=systemmodel_Sum1)
gen_systemmodel_Sum2_Sum = Generalization(general=Sum, specific=systemmodel_Sum2)
gen_systemmodel_Test_Block = Generalization(general=Block, specific=systemmodel_Test)
gen_systemmodel_A_ModelElement = Generalization(general=ModelElement, specific=systemmodel_A)
gen_systemmodel_B_A = Generalization(general=A, specific=systemmodel_B)
gen_systemmodel_C_ModelElement = Generalization(general=ModelElement, specific=systemmodel_C)

# Domain Model
domain_model = DomainModel(
    name="systemmodel",
    types={systemmodel_Outport, systemmodel_SMElement, systemmodel_SystemModel, SMElement, systemmodel_Block, systemmodel_Signal, systemmodel_Inport, systemmodel_UnitDelay, Block, systemmodel_Sum, systemmodel_SrcBlock, systemmodel_Sum1, systemmodel_ModelElement, Sum, systemmodel_Sum2, systemmodel_Test, systemmodel_A, ModelElement, systemmodel_B, systemmodel_C, A, systemmodel_Root},
    associations={outports5, blocks0, signals1, inports3, parentBlock12, srcPort6, dstPort8, inSignal9, outSignals10, elements18, nonUniqueOrderedRef13, refB15, refC16},
    generalizations={gen_systemmodel_Signal_SMElement, gen_systemmodel_SystemModel_SMElement, gen_systemmodel_Block_SMElement, gen_systemmodel_UnitDelay_Block, gen_systemmodel_Sum_Block, gen_systemmodel_SrcBlock_Block, gen_systemmodel_Inport_SMElement, gen_systemmodel_Outport_SMElement, gen_systemmodel_Root_SMElement, gen_systemmodel_ModelElement_SMElement, gen_systemmodel_Sum1_Sum, gen_systemmodel_Sum2_Sum, gen_systemmodel_Test_Block, gen_systemmodel_A_ModelElement, gen_systemmodel_B_A, gen_systemmodel_C_ModelElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)