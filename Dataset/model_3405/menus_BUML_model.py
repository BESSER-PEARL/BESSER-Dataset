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

# Enumerations
Gender: Enumeration = Enumeration(
    name="Gender",
    literals={
            EnumerationLiteral(name="MALE"),
			EnumerationLiteral(name="FEMALE"),
			EnumerationLiteral(name="UNSPECIFIED")
    }
)

# Classes
menus_Person = Class(name="menus::Person")
menus_PersonDirectory = Class(name="menus::PersonDirectory")

# menus_Person class attributes and methods
menus_Person_firstname: Property = Property(name="firstname", type=StringType)
menus_Person_lastname: Property = Property(name="lastname", type=StringType)
menus_Person_sex: Property = Property(name="sex", type=StringType)
menus_Person_pregnant: Property = Property(name="pregnant", type=BooleanType)
menus_Person_dateOfBirth: Property = Property(name="dateOfBirth", type=DateType)
menus_Person.attributes={menus_Person_sex, menus_Person_dateOfBirth, menus_Person_pregnant, menus_Person_firstname, menus_Person_lastname}

# menus_PersonDirectory class attributes and methods

# Relationships
entry2: BinaryAssociation = BinaryAssociation(
    name="entry2",
    ends={
        Property(name="menus_Person3", type=menus_PersonDirectory, multiplicity=Multiplicity(1, 1)),
        Property(name="menus_PersonDirectory", type=menus_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
partner1: BinaryAssociation = BinaryAssociation(
    name="partner1",
    ends={
        Property(name="menus_Person", type=menus_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="menus_Person0", type=menus_Person, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="menus",
    types={menus_Person, menus_PersonDirectory, Gender},
    associations={entry2, partner1},
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