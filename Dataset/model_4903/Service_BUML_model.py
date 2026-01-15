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
Service_Tool = Class(name="Service::Tool")
Service_JavaService = Class(name="Service::JavaService")

# Service_Tool class attributes and methods
Service_Tool_name: Property = Property(name="name", type=StringType)
Service_Tool.attributes={Service_Tool_name}

# Service_JavaService class attributes and methods
Service_JavaService_name: Property = Property(name="name", type=StringType)
Service_JavaService_option: Property = Property(name="option", type=StringType)
Service_JavaService.attributes={Service_JavaService_name, Service_JavaService_option}

# Relationships
services0: BinaryAssociation = BinaryAssociation(
    name="services0",
    ends={
        Property(name="Service_JavaService", type=Service_Tool, multiplicity=Multiplicity(1, 1)),
        Property(name="Service_Tool", type=Service_JavaService, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="Service",
    types={Service_Tool, Service_JavaService},
    associations={services0},
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