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
persons_Female = Class(name="persons::Female")
persons_Person = Class(name="persons::Person", is_abstract=True)
persons_Male = Class(name="persons::Male")
Person = Class(name="Person")

# persons_Female class attributes and methods

# persons_Person class attributes and methods
persons_Person_fullName: Property = Property(name="fullName", type=StringType)
persons_Person.attributes={persons_Person_fullName}

# persons_Male class attributes and methods

# Person class attributes and methods

# Generalizations
gen_persons_Female_Person = Generalization(general=Person, specific=persons_Female)
gen_persons_Male_Person = Generalization(general=Person, specific=persons_Male)

# Domain Model
domain_model = DomainModel(
    name="persons",
    types={persons_Female, persons_Person, persons_Male, Person},
    associations={},
    generalizations={gen_persons_Female_Person, gen_persons_Male_Person},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)