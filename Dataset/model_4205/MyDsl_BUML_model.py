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
myDsl_Import = Class(name="myDsl::Import")
myDsl_Model = Class(name="myDsl::Model")
myDsl_Greeting = Class(name="myDsl::Greeting")

# myDsl_Import class attributes and methods
myDsl_Import_Import_type: Property = Property(name="Import_type", type=StringType)
myDsl_Import_import_num: Property = Property(name="import_num", type=IntegerType)
myDsl_Import.attributes={myDsl_Import_import_num, myDsl_Import_Import_type}

# myDsl_Model class attributes and methods

# myDsl_Greeting class attributes and methods
myDsl_Greeting_name: Property = Property(name="name", type=StringType)
myDsl_Greeting.attributes={myDsl_Greeting_name}

# Relationships
imports1: BinaryAssociation = BinaryAssociation(
    name="imports1",
    ends={
        Property(name="myDsl_Import", type=myDsl_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Model2", type=myDsl_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
greetings0: BinaryAssociation = BinaryAssociation(
    name="greetings0",
    ends={
        Property(name="myDsl_Greeting", type=myDsl_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Model", type=myDsl_Greeting, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="myDsl",
    types={myDsl_Import, myDsl_Model, myDsl_Greeting},
    associations={imports1, greetings0},
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