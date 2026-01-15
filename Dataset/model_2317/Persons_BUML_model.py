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
Persons_Male = Class(name="Persons::Male")
Person = Class(name="Person")
Persons_Female = Class(name="Persons::Female")

# Persons_Person class attributes and methods
Persons_Person_fullName: Property = Property(name="fullName", type=StringType)
Persons_Person.attributes={Persons_Person_fullName}

# Persons_Male class attributes and methods

# Person class attributes and methods

# Persons_Female class attributes and methods

# Generalizations
gen_Persons_Male_Person = Generalization(general=Person, specific=Persons_Male)
gen_Persons_Female_Person = Generalization(general=Person, specific=Persons_Female)

# Domain Model
domain_model = DomainModel(
    name="Persons",
    types={Persons_Person, Persons_Male, Person, Persons_Female},
    associations={},
    generalizations={gen_Persons_Male_Person, gen_Persons_Female_Person},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)