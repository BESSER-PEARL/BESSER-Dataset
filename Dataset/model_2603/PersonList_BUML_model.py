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
            EnumerationLiteral(name="Male"),
			EnumerationLiteral(name="Female")
    }
)

# Classes
PersonList_List = Class(name="PersonList::List")
PersonList_Person = Class(name="PersonList::Person")
PersonList_WorkPlace = Class(name="PersonList::WorkPlace")
PersonList_LivingPlace = Class(name="PersonList::LivingPlace")

# PersonList_List class attributes and methods

# PersonList_Person class attributes and methods
PersonList_Person_firstname: Property = Property(name="firstname", type=StringType)
PersonList_Person_lastname: Property = Property(name="lastname", type=StringType)
PersonList_Person_gender: Property = Property(name="gender", type=StringType)
PersonList_Person.attributes={PersonList_Person_firstname, PersonList_Person_lastname, PersonList_Person_gender}

# PersonList_WorkPlace class attributes and methods
PersonList_WorkPlace_address: Property = Property(name="address", type=StringType)
PersonList_WorkPlace.attributes={PersonList_WorkPlace_address}

# PersonList_LivingPlace class attributes and methods
PersonList_LivingPlace_address: Property = Property(name="address", type=StringType)
PersonList_LivingPlace.attributes={PersonList_LivingPlace_address}

# Relationships
members0: BinaryAssociation = BinaryAssociation(
    name="members0",
    ends={
        Property(name="Person", type=PersonList_List, multiplicity=Multiplicity(1, 1)),
        Property(name="list", type=PersonList_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
persons10: BinaryAssociation = BinaryAssociation(
    name="persons10",
    ends={
        Property(name="Person11", type=PersonList_LivingPlace, multiplicity=Multiplicity(1, 1)),
        Property(name="home", type=PersonList_Person, multiplicity=Multiplicity(0, 9999))
    }
)
wplaces1: BinaryAssociation = BinaryAssociation(
    name="wplaces1",
    ends={
        Property(name="PersonList_WorkPlace", type=PersonList_List, multiplicity=Multiplicity(1, 1)),
        Property(name="PersonList_List", type=PersonList_WorkPlace, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lplaces2: BinaryAssociation = BinaryAssociation(
    name="lplaces2",
    ends={
        Property(name="PersonList_LivingPlace", type=PersonList_List, multiplicity=Multiplicity(1, 1)),
        Property(name="PersonList_List3", type=PersonList_LivingPlace, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
list4: BinaryAssociation = BinaryAssociation(
    name="list4",
    ends={
        Property(name="List", type=PersonList_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="members", type=PersonList_List, multiplicity=Multiplicity(1, 1))
    }
)
works5: BinaryAssociation = BinaryAssociation(
    name="works5",
    ends={
        Property(name="WorkPlace", type=PersonList_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="persons", type=PersonList_WorkPlace, multiplicity=Multiplicity(1, 1))
    }
)
home6: BinaryAssociation = BinaryAssociation(
    name="home6",
    ends={
        Property(name="LivingPlace", type=PersonList_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="persons7", type=PersonList_LivingPlace, multiplicity=Multiplicity(1, 1))
    }
)
persons8: BinaryAssociation = BinaryAssociation(
    name="persons8",
    ends={
        Property(name="Person9", type=PersonList_WorkPlace, multiplicity=Multiplicity(1, 1)),
        Property(name="works", type=PersonList_Person, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="PersonList",
    types={PersonList_List, PersonList_Person, PersonList_WorkPlace, PersonList_LivingPlace, Gender},
    associations={members0, persons10, wplaces1, lplaces2, list4, works5, home6, persons8},
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