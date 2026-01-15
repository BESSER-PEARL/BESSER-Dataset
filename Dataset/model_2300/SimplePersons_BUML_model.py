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
SimplePersons_Person = Class(name="SimplePersons::Person", is_abstract=True)
SimplePersons_PersonRegister = Class(name="SimplePersons::PersonRegister")
SimplePersons_Male = Class(name="SimplePersons::Male")
Person = Class(name="Person")
SimplePersons_Female = Class(name="SimplePersons::Female")

# SimplePersons_Person class attributes and methods
SimplePersons_Person_name: Property = Property(name="name", type=StringType)
SimplePersons_Person.attributes={SimplePersons_Person_name}

# SimplePersons_PersonRegister class attributes and methods

# SimplePersons_Male class attributes and methods

# Person class attributes and methods

# SimplePersons_Female class attributes and methods

# Relationships
persons0: BinaryAssociation = BinaryAssociation(
    name="persons0",
    ends={
        Property(name="SimplePersons_Person", type=SimplePersons_PersonRegister, multiplicity=Multiplicity(1, 1)),
        Property(name="SimplePersons_PersonRegister", type=SimplePersons_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_SimplePersons_Male_Person = Generalization(general=Person, specific=SimplePersons_Male)
gen_SimplePersons_Female_Person = Generalization(general=Person, specific=SimplePersons_Female)

# Domain Model
domain_model = DomainModel(
    name="SimplePersons",
    types={SimplePersons_Person, SimplePersons_PersonRegister, SimplePersons_Male, Person, SimplePersons_Female},
    associations={persons0},
    generalizations={gen_SimplePersons_Male_Person, gen_SimplePersons_Female_Person},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)