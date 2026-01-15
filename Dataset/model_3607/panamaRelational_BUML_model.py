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
panamaRelational_PanamaOfficers = Class(name="panamaRelational::PanamaOfficers")

# panamaRelational_PanamaOfficers class attributes and methods
panamaRelational_PanamaOfficers_name: Property = Property(name="name", type=StringType)
panamaRelational_PanamaOfficers_company: Property = Property(name="company", type=StringType)
panamaRelational_PanamaOfficers.attributes={panamaRelational_PanamaOfficers_name, panamaRelational_PanamaOfficers_company}

# Domain Model
domain_model = DomainModel(
    name="panamaRelational",
    types={panamaRelational_PanamaOfficers},
    associations={},
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