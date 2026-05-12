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
CPU = Class(name="CPU")
Processor = Class(name="Processor", is_abstract=True)
AcceleratorCard = Class(name="AcceleratorCard", is_abstract=True)
Cache = Class(name="Cache")
RAM = Class(name="RAM")
Machine = Class(name="Machine")
Program = Class(name="Program")
Instruction = Class(name="Instruction")
Memory_Interface = Class(name="Memory_Interface")
DeviceCard = Class(name="DeviceCard", is_abstract=True)
Card = Class(name="Card", is_abstract=True)
Sound = Class(name="Sound", is_abstract=True)
ExtensionBoard = Class(name="ExtensionBoard")

# CPU class attributes and methods

# Processor class attributes and methods

# AcceleratorCard class attributes and methods

# Cache class attributes and methods
Cache_chunck: Property = Property(name="chunck", type=StringType)
Cache.attributes={Cache_chunck}

# RAM class attributes and methods

# Machine class attributes and methods

# Program class attributes and methods
Program_name: Property = Property(name="name", type=StringType)
Program.attributes={Program_name}

# Instruction class attributes and methods

# Memory_Interface class attributes and methods

# DeviceCard class attributes and methods

# Card class attributes and methods

# Sound class attributes and methods

# ExtensionBoard class attributes and methods

# Relationships
Machine_Memory: BinaryAssociation = BinaryAssociation(
    name="Machine_Memory",
    ends={
        Property(name="machine0", type=Machine, multiplicity=Multiplicity(0, 9999)),
        Property(name="memory1", type=Cache, multiplicity=Multiplicity(0, 9999))
    }
)
Processor_Memory: BinaryAssociation = BinaryAssociation(
    name="Processor_Memory",
    ends={
        Property(name="processor2", type=Processor, multiplicity=Multiplicity(0, 9999)),
        Property(name="memory3", type=Cache, multiplicity=Multiplicity(0, 9999))
    }
)
Program_Instruction: BinaryAssociation = BinaryAssociation(
    name="Program_Instruction",
    ends={
        Property(name="program4", type=Program, multiplicity=Multiplicity(0, 9999)),
        Property(name="instructions5", type=Instruction, multiplicity=Multiplicity(0, 9999))
    }
)
Machine_Processor: BinaryAssociation = BinaryAssociation(
    name="Machine_Processor",
    ends={
        Property(name="machine6", type=Machine, multiplicity=Multiplicity(0, 9999)),
        Property(name="processor7", type=AcceleratorCard, multiplicity=Multiplicity(0, 9999))
    }
)
Processor_Program: BinaryAssociation = BinaryAssociation(
    name="Processor_Program",
    ends={
        Property(name="processor8", type=Processor, multiplicity=Multiplicity(0, 9999)),
        Property(name="program9", type=Program, multiplicity=Multiplicity(0, 9999))
    }
)
Cache_RAM: BinaryAssociation = BinaryAssociation(
    name="Cache_RAM",
    ends={
        Property(name="ramProxy10", type=RAM, multiplicity=Multiplicity(0, 1)),
        Property(name="cache11", type=Cache, multiplicity=Multiplicity(0, 1))
    }
)
ExtensionBoard_Card: BinaryAssociation = BinaryAssociation(
    name="ExtensionBoard_Card",
    ends={
        Property(name="extensionBoard12", type=ExtensionBoard, multiplicity=Multiplicity(0, 9999)),
        Property(name="cards13", type=Card, multiplicity=Multiplicity(0, 3))
    }
)
Machine_Card: BinaryAssociation = BinaryAssociation(
    name="Machine_Card",
    ends={
        Property(name="machine14", type=Machine, multiplicity=Multiplicity(0, 9999)),
        Property(name="cards15", type=Card, multiplicity=Multiplicity(0, 3))
    }
)
AcceleratorCard_CPU: BinaryAssociation = BinaryAssociation(
    name="AcceleratorCard_CPU",
    ends={
        Property(name="decoratedCPU16", type=CPU, multiplicity=Multiplicity(1, 1)),
        Property(name="acceleratorCard17", type=AcceleratorCard, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="c60f6c29_a7df_477c_bd8b_610ede23db37",
    types={CPU, Processor, AcceleratorCard, Cache, RAM, Machine, Program, Instruction, Memory_Interface, DeviceCard, Card, Sound, ExtensionBoard},
    associations={Machine_Memory, Processor_Memory, Program_Instruction, Machine_Processor, Processor_Program, Cache_RAM, ExtensionBoard_Card, Machine_Card, AcceleratorCard_CPU},
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