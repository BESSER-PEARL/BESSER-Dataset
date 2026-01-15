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
rm_ResourceModel = Class(name="rm::ResourceModel")
rm_Device = Class(name="rm::Device")
rm_Memory = Class(name="rm::Memory")
rm_MemoryCellReference = Class(name="rm::MemoryCellReference")
rm_VariableReference = Class(name="rm::VariableReference")

# rm_ResourceModel class attributes and methods

# rm_Device class attributes and methods
rm_Device_cacheSize: Property = Property(name="cacheSize", type=IntegerType)
rm_Device.attributes={rm_Device_cacheSize}

# rm_Memory class attributes and methods
rm_Memory_size: Property = Property(name="size", type=IntegerType)
rm_Memory.attributes={rm_Memory_size}

# rm_MemoryCellReference class attributes and methods
rm_MemoryCellReference_startCellIndex: Property = Property(name="startCellIndex", type=IntegerType)
rm_MemoryCellReference_endCellIndex: Property = Property(name="endCellIndex", type=IntegerType)
rm_MemoryCellReference.attributes={rm_MemoryCellReference_endCellIndex, rm_MemoryCellReference_startCellIndex}

# rm_VariableReference class attributes and methods
rm_VariableReference_variable: Property = Property(name="variable", type=StringType)
rm_VariableReference_memoryCellIndex: Property = Property(name="memoryCellIndex", type=IntegerType)
rm_VariableReference.attributes={rm_VariableReference_memoryCellIndex, rm_VariableReference_variable}

# Relationships
devices0: BinaryAssociation = BinaryAssociation(
    name="devices0",
    ends={
        Property(name="rm_Device", type=rm_ResourceModel, multiplicity=Multiplicity(1, 1)),
        Property(name="rm_ResourceModel", type=rm_Device, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
memory1: BinaryAssociation = BinaryAssociation(
    name="memory1",
    ends={
        Property(name="rm_Memory", type=rm_ResourceModel, multiplicity=Multiplicity(1, 1)),
        Property(name="rm_ResourceModel2", type=rm_Memory, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
localMemoryCellReference3: BinaryAssociation = BinaryAssociation(
    name="localMemoryCellReference3",
    ends={
        Property(name="rm_MemoryCellReference", type=rm_Device, multiplicity=Multiplicity(1, 1)),
        Property(name="rm_Device4", type=rm_MemoryCellReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variableReferences5: BinaryAssociation = BinaryAssociation(
    name="variableReferences5",
    ends={
        Property(name="rm_VariableReference", type=rm_Memory, multiplicity=Multiplicity(1, 1)),
        Property(name="rm_Memory6", type=rm_VariableReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="rm",
    types={rm_ResourceModel, rm_Device, rm_Memory, rm_MemoryCellReference, rm_VariableReference},
    associations={devices0, memory1, localMemoryCellReference3, variableReferences5},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)