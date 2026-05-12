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
GenericSound = Class(name="GenericSound")
Vendor1Adapter = Class(name="Vendor1Adapter")
Vendor2Adapter = Class(name="Vendor2Adapter")
Vendor1Sound = Class(name="Vendor1Sound")
Vendor2Sound = Class(name="Vendor2Sound")
ExtensionBoard = Class(name="ExtensionBoard")
FastCard = Class(name="FastCard")

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

# GenericSound class attributes and methods

# Vendor1Adapter class attributes and methods

# Vendor2Adapter class attributes and methods

# Vendor1Sound class attributes and methods

# Vendor2Sound class attributes and methods

# ExtensionBoard class attributes and methods

# FastCard class attributes and methods

# Relationships
Machine_Memory: BinaryAssociation = BinaryAssociation(
    name="Machine_Memory",
    ends={
        Property(name="machine0", type=Machine, multiplicity=Multiplicity(0, 9999)),
        Property(name="memory1", type=Memory_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
Processor_Memory: BinaryAssociation = BinaryAssociation(
    name="Processor_Memory",
    ends={
        Property(name="processor2", type=Processor, multiplicity=Multiplicity(0, 9999)),
        Property(name="memory3", type=Memory_Interface, multiplicity=Multiplicity(0, 9999))
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
        Property(name="processor7", type=Processor, multiplicity=Multiplicity(0, 9999))
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
        Property(name="ramProxy10", type=RAM, multiplicity=Multiplicity(1, 1)),
        Property(name="cache11", type=Cache, multiplicity=Multiplicity(0, 1))
    }
)
ExtensionBoard_Card: BinaryAssociation = BinaryAssociation(
    name="ExtensionBoard_Card",
    ends={
        Property(name="extensionBoard12", type=ExtensionBoard, multiplicity=Multiplicity(0, 9999)),
        Property(name="cards13", type=Card, multiplicity=Multiplicity(0, 9999))
    }
)
Vendor1Adapter_Vendor1Sound: BinaryAssociation = BinaryAssociation(
    name="Vendor1Adapter_Vendor1Sound",
    ends={
        Property(name="vendor1Adapter14", type=Vendor1Adapter, multiplicity=Multiplicity(0, 9999)),
        Property(name="vendor1Sound15", type=Vendor1Sound, multiplicity=Multiplicity(0, 9999))
    }
)
Vendor2Adapter_Vendor2Sound: BinaryAssociation = BinaryAssociation(
    name="Vendor2Adapter_Vendor2Sound",
    ends={
        Property(name="vendor2Adapter16", type=Vendor2Adapter, multiplicity=Multiplicity(0, 9999)),
        Property(name="vendor2Sound17", type=Vendor2Sound, multiplicity=Multiplicity(0, 9999))
    }
)
Machine_Card: BinaryAssociation = BinaryAssociation(
    name="Machine_Card",
    ends={
        Property(name="machine18", type=Machine, multiplicity=Multiplicity(0, 9999)),
        Property(name="cards19", type=Card, multiplicity=Multiplicity(0, 3))
    }
)
AcceleratorCard_CPU: BinaryAssociation = BinaryAssociation(
    name="AcceleratorCard_CPU",
    ends={
        Property(name="decoratedCPU20", type=CPU, multiplicity=Multiplicity(0, 1)),
        Property(name="acceleratorCard21", type=AcceleratorCard, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="b32e841d_6125_451c_848a_7de276a33ada",
    types={CPU, Processor, AcceleratorCard, Cache, RAM, Machine, Program, Instruction, Memory_Interface, DeviceCard, Card, Sound, GenericSound, Vendor1Adapter, Vendor2Adapter, Vendor1Sound, Vendor2Sound, ExtensionBoard, FastCard},
    associations={Machine_Memory, Processor_Memory, Program_Instruction, Machine_Processor, Processor_Program, Cache_RAM, ExtensionBoard_Card, Vendor1Adapter_Vendor1Sound, Vendor2Adapter_Vendor2Sound, Machine_Card, AcceleratorCard_CPU},
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