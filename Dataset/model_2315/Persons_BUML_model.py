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
Persons_Person = Class(name="Persons::Person", is_abstract=True)
Persons_Female = Class(name="Persons::Female")
Persons_Male = Class(name="Persons::Male")
Person = Class(name="Person")

# Persons_Person class attributes and methods
Persons_Person_fullName: Property = Property(name="fullName", type=StringType)
Persons_Person.attributes={Persons_Person_fullName}

# Persons_Female class attributes and methods

# Persons_Male class attributes and methods

# Person class attributes and methods

# Generalizations
gen_Persons_Female_Person = Generalization(general=Person, specific=Persons_Female)
gen_Persons_Male_Person = Generalization(general=Person, specific=Persons_Male)

# Domain Model
domain_model = DomainModel(
    name="Persons",
    types={Persons_Person, Persons_Female, Persons_Male, Person},
    associations={},
    generalizations={gen_Persons_Female_Person, gen_Persons_Male_Person},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)