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
persons_PersonRegister = Class(name="persons::PersonRegister")
persons_Person = Class(name="persons::Person", is_abstract=True)
persons_Male = Class(name="persons::Male")
Person = Class(name="Person")
persons_Female = Class(name="persons::Female")

# persons_PersonRegister class attributes and methods
persons_PersonRegister_id: Property = Property(name="id", type=StringType)
persons_PersonRegister.attributes={persons_PersonRegister_id}

# persons_Person class attributes and methods
persons_Person_fullName: Property = Property(name="fullName", type=StringType)
persons_Person_birthday: Property = Property(name="birthday", type=DateType)
persons_Person.attributes={persons_Person_fullName, persons_Person_birthday}

# persons_Male class attributes and methods

# Person class attributes and methods

# persons_Female class attributes and methods

# Relationships
persons0: BinaryAssociation = BinaryAssociation(
    name="persons0",
    ends={
        Property(name="persons_Person", type=persons_PersonRegister, multiplicity=Multiplicity(1, 1)),
        Property(name="persons_PersonRegister", type=persons_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_persons_Male_Person = Generalization(general=Person, specific=persons_Male)
gen_persons_Female_Person = Generalization(general=Person, specific=persons_Female)

# Domain Model
domain_model = DomainModel(
    name="persons",
    types={persons_PersonRegister, persons_Person, persons_Male, Person, persons_Female},
    associations={persons0},
    generalizations={gen_persons_Male_Person, gen_persons_Female_Person},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)