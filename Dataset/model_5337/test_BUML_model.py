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
root_Test = Class(name="root::Test")

# root_Test class attributes and methods
root_Test_att1: Property = Property(name="att1", type=IntegerType)
root_Test_att2: Property = Property(name="att2", type=IntegerType)
root_Test_name: Property = Property(name="name", type=StringType)
root_Test.attributes={root_Test_att1, root_Test_name, root_Test_att2}

# Domain Model
domain_model = DomainModel(
    name="root",
    types={root_Test},
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