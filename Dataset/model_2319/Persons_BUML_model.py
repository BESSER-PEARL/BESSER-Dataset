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
Persons_Persons = Class(name="Persons::Persons", is_abstract=True)
Persons_Male = Class(name="Persons::Male")
Persons = Class(name="Persons")
Persons_Female = Class(name="Persons::Female")

# Persons_Persons class attributes and methods
Persons_Persons_fullName: Property = Property(name="fullName", type=StringType)
Persons_Persons.attributes={Persons_Persons_fullName}

# Persons_Male class attributes and methods

# Persons class attributes and methods

# Persons_Female class attributes and methods

# Generalizations
gen_Persons_Male_Persons = Generalization(general=Persons, specific=Persons_Male)
gen_Persons_Female_Persons = Generalization(general=Persons, specific=Persons_Female)

# Domain Model
domain_model = DomainModel(
    name="Persons",
    types={Persons_Persons, Persons_Male, Persons, Persons_Female},
    associations={},
    generalizations={gen_Persons_Male_Persons, gen_Persons_Female_Persons},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)