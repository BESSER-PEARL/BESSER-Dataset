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
PersonList_Person = Class(name="PersonList::Person", is_abstract=True)
PersonList_Place = Class(name="PersonList::Place", is_abstract=True)
PersonList_LivingPlace = Class(name="PersonList::LivingPlace")
PersonList_WorkPlace = Class(name="PersonList::WorkPlace")
Place = Class(name="Place")
PersonList_WorkingPosition = Class(name="PersonList::WorkingPosition")
PersonList_Male = Class(name="PersonList::Male")
Person = Class(name="Person")
PersonList_Female = Class(name="PersonList::Female")

# PersonList_List class attributes and methods

# PersonList_Person class attributes and methods
PersonList_Person_name: Property = Property(name="name", type=StringType)
PersonList_Person.attributes={PersonList_Person_name}

# PersonList_Place class attributes and methods
PersonList_Place_address: Property = Property(name="address", type=StringType)
PersonList_Place.attributes={PersonList_Place_address}

# PersonList_LivingPlace class attributes and methods

# PersonList_WorkPlace class attributes and methods

# Place class attributes and methods

# PersonList_WorkingPosition class attributes and methods
PersonList_WorkingPosition_description: Property = Property(name="description", type=StringType)
PersonList_WorkingPosition.attributes={PersonList_WorkingPosition_description}

# PersonList_Male class attributes and methods

# Person class attributes and methods

# PersonList_Female class attributes and methods

# Relationships
members0: BinaryAssociation = BinaryAssociation(
    name="members0",
    ends={
        Property(name="Person", type=PersonList_List, multiplicity=Multiplicity(1, 1)),
        Property(name="list", type=PersonList_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
list2: BinaryAssociation = BinaryAssociation(
    name="list2",
    ends={
        Property(name="List", type=PersonList_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="members", type=PersonList_List, multiplicity=Multiplicity(1, 1))
    }
)
places1: BinaryAssociation = BinaryAssociation(
    name="places1",
    ends={
        Property(name="PersonList_Place", type=PersonList_List, multiplicity=Multiplicity(1, 1)),
        Property(name="PersonList_List", type=PersonList_Place, multiplicity=Multiplicity(0, 1))
    }
)
home4: BinaryAssociation = BinaryAssociation(
    name="home4",
    ends={
        Property(name="LivingPlace", type=PersonList_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="persons5", type=PersonList_LivingPlace, multiplicity=Multiplicity(1, 1))
    }
)
position6: BinaryAssociation = BinaryAssociation(
    name="position6",
    ends={
        Property(name="WorkingPosition7", type=PersonList_WorkPlace, multiplicity=Multiplicity(1, 1)),
        Property(name="works", type=PersonList_WorkingPosition, multiplicity=Multiplicity(0, 1))
    }
)
persons8: BinaryAssociation = BinaryAssociation(
    name="persons8",
    ends={
        Property(name="Person9", type=PersonList_LivingPlace, multiplicity=Multiplicity(1, 1)),
        Property(name="home", type=PersonList_Person, multiplicity=Multiplicity(0, 9999))
    }
)
works3: BinaryAssociation = BinaryAssociation(
    name="works3",
    ends={
        Property(name="WorkingPosition", type=PersonList_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="persons", type=PersonList_WorkingPosition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
works10: BinaryAssociation = BinaryAssociation(
    name="works10",
    ends={
        Property(name="WorkPlace", type=PersonList_WorkingPosition, multiplicity=Multiplicity(1, 1)),
        Property(name="position", type=PersonList_WorkPlace, multiplicity=Multiplicity(1, 1))
    }
)
persons11: BinaryAssociation = BinaryAssociation(
    name="persons11",
    ends={
        Property(name="Person13", type=PersonList_WorkingPosition, multiplicity=Multiplicity(1, 1)),
        Property(name="works12", type=PersonList_Person, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_PersonList_WorkPlace_Place = Generalization(general=Place, specific=PersonList_WorkPlace)
gen_PersonList_LivingPlace_Place = Generalization(general=Place, specific=PersonList_LivingPlace)
gen_PersonList_Male_Person = Generalization(general=Person, specific=PersonList_Male)
gen_PersonList_Female_Person = Generalization(general=Person, specific=PersonList_Female)

# Domain Model
domain_model = DomainModel(
    name="PersonList",
    types={PersonList_List, PersonList_Person, PersonList_Place, PersonList_LivingPlace, PersonList_WorkPlace, Place, PersonList_WorkingPosition, PersonList_Male, Person, PersonList_Female, Gender},
    associations={members0, list2, places1, home4, position6, persons8, works3, works10, persons11},
    generalizations={gen_PersonList_WorkPlace_Place, gen_PersonList_LivingPlace_Place, gen_PersonList_Male_Person, gen_PersonList_Female_Person},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)