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
llp_LowLevelProgram = Class(name="llp_LowLevelProgram")
llp_Task = Class(name="llp_Task")
llp_DataAccessPattern = Class(name="llp_DataAccessPattern", is_abstract=True)
llp_ReadInstruction = Class(name="llp_ReadInstruction")
IOInstruction = Class(name="IOInstruction")
llp_WriteInstruction = Class(name="llp_WriteInstruction")
llp_IOInstruction = Class(name="llp_IOInstruction", is_abstract=True)
DataAccessPattern = Class(name="DataAccessPattern")
llp_MemoryReference = Class(name="llp_MemoryReference")
llp_CacheInstruction = Class(name="llp_CacheInstruction", is_abstract=True)
llp_CommitInstruction = Class(name="llp_CommitInstruction")
CacheInstruction = Class(name="CacheInstruction")
llp_LockInstruction = Class(name="llp_LockInstruction")
SynchronisationInstruction = Class(name="SynchronisationInstruction")
llp_UnlockInstruction = Class(name="llp_UnlockInstruction")
llp_SpawnInstruction = Class(name="llp_SpawnInstruction")
llp_ControlFlowBranchingInstruction = Class(name="llp_ControlFlowBranchingInstruction")
ControlFlowInstruction = Class(name="ControlFlowInstruction")
llp_RepetitionInstruction = Class(name="llp_RepetitionInstruction")
llp_ControlFlowInstruction = Class(name="llp_ControlFlowInstruction", is_abstract=True)
llp_SkipInstruction = Class(name="llp_SkipInstruction")
llp_SynchronisationInstruction = Class(name="llp_SynchronisationInstruction", is_abstract=True)
llp_ParenthesisInstruction = Class(name="llp_ParenthesisInstruction")
llp_Block = Class(name="llp_Block")

# llp_LowLevelProgram class attributes and methods

# llp_Task class attributes and methods
llp_Task_name: Property = Property(name="name", type=StringType)
llp_Task.attributes={llp_Task_name}

# llp_DataAccessPattern class attributes and methods

# llp_ReadInstruction class attributes and methods

# IOInstruction class attributes and methods

# llp_WriteInstruction class attributes and methods

# llp_IOInstruction class attributes and methods

# DataAccessPattern class attributes and methods

# llp_MemoryReference class attributes and methods
llp_MemoryReference_address: Property = Property(name="address", type=StringType)
llp_MemoryReference.attributes={llp_MemoryReference_address}

# llp_CacheInstruction class attributes and methods

# llp_CommitInstruction class attributes and methods

# CacheInstruction class attributes and methods

# llp_LockInstruction class attributes and methods

# SynchronisationInstruction class attributes and methods

# llp_UnlockInstruction class attributes and methods

# llp_SpawnInstruction class attributes and methods

# llp_ControlFlowBranchingInstruction class attributes and methods

# ControlFlowInstruction class attributes and methods

# llp_RepetitionInstruction class attributes and methods
llp_RepetitionInstruction_numberOfRepetitions: Property = Property(name="numberOfRepetitions", type=IntegerType)
llp_RepetitionInstruction.attributes={llp_RepetitionInstruction_numberOfRepetitions}

# llp_ControlFlowInstruction class attributes and methods

# llp_SkipInstruction class attributes and methods

# llp_SynchronisationInstruction class attributes and methods

# llp_ParenthesisInstruction class attributes and methods

# llp_Block class attributes and methods

# Relationships
tasks0: BinaryAssociation = BinaryAssociation(
    name="tasks0",
    ends={
        Property(name="llp_Task", type=llp_LowLevelProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="llp_LowLevelProgram", type=llp_Task, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
block3: BinaryAssociation = BinaryAssociation(
    name="block3",
    ends={
        Property(name="llp_Block5", type=llp_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="llp_Task4", type=llp_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
dataAccessPatterns6: BinaryAssociation = BinaryAssociation(
    name="dataAccessPatterns6",
    ends={
        Property(name="llp_DataAccessPattern", type=llp_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="llp_Block7", type=llp_DataAccessPattern, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
memoryReference8: BinaryAssociation = BinaryAssociation(
    name="memoryReference8",
    ends={
        Property(name="llp_MemoryReference", type=llp_IOInstruction, multiplicity=Multiplicity(1, 1)),
        Property(name="llp_IOInstruction", type=llp_MemoryReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
memoryReference9: BinaryAssociation = BinaryAssociation(
    name="memoryReference9",
    ends={
        Property(name="llp_MemoryReference10", type=llp_CommitInstruction, multiplicity=Multiplicity(1, 1)),
        Property(name="llp_CommitInstruction", type=llp_MemoryReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
task11: BinaryAssociation = BinaryAssociation(
    name="task11",
    ends={
        Property(name="llp_Task12", type=llp_SpawnInstruction, multiplicity=Multiplicity(1, 1)),
        Property(name="llp_SpawnInstruction", type=llp_Task, multiplicity=Multiplicity(1, 1))
    }
)
leftHandSideBlock13: BinaryAssociation = BinaryAssociation(
    name="leftHandSideBlock13",
    ends={
        Property(name="llp_Block14", type=llp_ControlFlowBranchingInstruction, multiplicity=Multiplicity(1, 1)),
        Property(name="llp_ControlFlowBranchingInstruction", type=llp_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightHandSideBlock15: BinaryAssociation = BinaryAssociation(
    name="rightHandSideBlock15",
    ends={
        Property(name="llp_Block17", type=llp_ControlFlowBranchingInstruction, multiplicity=Multiplicity(1, 1)),
        Property(name="llp_ControlFlowBranchingInstruction16", type=llp_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
block18: BinaryAssociation = BinaryAssociation(
    name="block18",
    ends={
        Property(name="llp_Block19", type=llp_RepetitionInstruction, multiplicity=Multiplicity(1, 1)),
        Property(name="llp_RepetitionInstruction", type=llp_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
memoryReference20: BinaryAssociation = BinaryAssociation(
    name="memoryReference20",
    ends={
        Property(name="llp_MemoryReference21", type=llp_SynchronisationInstruction, multiplicity=Multiplicity(1, 1)),
        Property(name="llp_SynchronisationInstruction", type=llp_MemoryReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
mainBlock1: BinaryAssociation = BinaryAssociation(
    name="mainBlock1",
    ends={
        Property(name="llp_Block", type=llp_LowLevelProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="llp_LowLevelProgram2", type=llp_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
block22: BinaryAssociation = BinaryAssociation(
    name="block22",
    ends={
        Property(name="llp_Block23", type=llp_ParenthesisInstruction, multiplicity=Multiplicity(1, 1)),
        Property(name="llp_ParenthesisInstruction", type=llp_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_llp_ReadInstruction_IOInstruction = Generalization(general=IOInstruction, specific=llp_ReadInstruction)
gen_llp_WriteInstruction_IOInstruction = Generalization(general=IOInstruction, specific=llp_WriteInstruction)
gen_llp_IOInstruction_DataAccessPattern = Generalization(general=DataAccessPattern, specific=llp_IOInstruction)
gen_llp_CacheInstruction_DataAccessPattern = Generalization(general=DataAccessPattern, specific=llp_CacheInstruction)
gen_llp_CommitInstruction_CacheInstruction = Generalization(general=CacheInstruction, specific=llp_CommitInstruction)
gen_llp_LockInstruction_SynchronisationInstruction = Generalization(general=SynchronisationInstruction, specific=llp_LockInstruction)
gen_llp_UnlockInstruction_SynchronisationInstruction = Generalization(general=SynchronisationInstruction, specific=llp_UnlockInstruction)
gen_llp_SpawnInstruction_DataAccessPattern = Generalization(general=DataAccessPattern, specific=llp_SpawnInstruction)
gen_llp_ControlFlowBranchingInstruction_ControlFlowInstruction = Generalization(general=ControlFlowInstruction, specific=llp_ControlFlowBranchingInstruction)
gen_llp_RepetitionInstruction_ControlFlowInstruction = Generalization(general=ControlFlowInstruction, specific=llp_RepetitionInstruction)
gen_llp_ControlFlowInstruction_DataAccessPattern = Generalization(general=DataAccessPattern, specific=llp_ControlFlowInstruction)
gen_llp_SkipInstruction_ControlFlowInstruction = Generalization(general=ControlFlowInstruction, specific=llp_SkipInstruction)
gen_llp_SynchronisationInstruction_DataAccessPattern = Generalization(general=DataAccessPattern, specific=llp_SynchronisationInstruction)
gen_llp_ParenthesisInstruction_ControlFlowInstruction = Generalization(general=ControlFlowInstruction, specific=llp_ParenthesisInstruction)

# Domain Model
domain_model = DomainModel(
    name="llp",
    types={llp_LowLevelProgram, llp_Task, llp_DataAccessPattern, llp_ReadInstruction, IOInstruction, llp_WriteInstruction, llp_IOInstruction, DataAccessPattern, llp_MemoryReference, llp_CacheInstruction, llp_CommitInstruction, CacheInstruction, llp_LockInstruction, SynchronisationInstruction, llp_UnlockInstruction, llp_SpawnInstruction, llp_ControlFlowBranchingInstruction, ControlFlowInstruction, llp_RepetitionInstruction, llp_ControlFlowInstruction, llp_SkipInstruction, llp_SynchronisationInstruction, llp_ParenthesisInstruction, llp_Block},
    associations={tasks0, block3, dataAccessPatterns6, memoryReference8, memoryReference9, task11, leftHandSideBlock13, rightHandSideBlock15, block18, memoryReference20, mainBlock1, block22},
    generalizations={gen_llp_ReadInstruction_IOInstruction, gen_llp_WriteInstruction_IOInstruction, gen_llp_IOInstruction_DataAccessPattern, gen_llp_CacheInstruction_DataAccessPattern, gen_llp_CommitInstruction_CacheInstruction, gen_llp_LockInstruction_SynchronisationInstruction, gen_llp_UnlockInstruction_SynchronisationInstruction, gen_llp_SpawnInstruction_DataAccessPattern, gen_llp_ControlFlowBranchingInstruction_ControlFlowInstruction, gen_llp_RepetitionInstruction_ControlFlowInstruction, gen_llp_ControlFlowInstruction_DataAccessPattern, gen_llp_SkipInstruction_ControlFlowInstruction, gen_llp_SynchronisationInstruction_DataAccessPattern, gen_llp_ParenthesisInstruction_ControlFlowInstruction},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)