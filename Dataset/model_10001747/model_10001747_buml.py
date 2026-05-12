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
Processor = Class(name="Processor")
Memory_Interface = Class(name="Memory_Interface")
Cache = Class(name="Cache")
RAM = Class(name="RAM")

# Processor class attributes and methods

# Memory_Interface class attributes and methods

# Cache class attributes and methods
Cache_chunck: Property = Property(name="chunck", type=StringType)
Cache.attributes={Cache_chunck}

# RAM class attributes and methods

# Relationships
Processor_Memory: BinaryAssociation = BinaryAssociation(
    name="Processor_Memory",
    ends={
        Property(name="memory0", type=Memory_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="processor1", type=Processor, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_SiRyIBJ7EeimSO_GhE8jew",
    types={Processor, Memory_Interface, Cache, RAM},
    associations={Processor_Memory},
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