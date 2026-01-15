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
family_family = Class(name="family::family")
family_Root = Class(name="family::Root")
family_university = Class(name="family::university")
family_studyprogramme = Class(name="family::studyprogramme")
family_person = Class(name="family::person")

# family_family class attributes and methods
family_family_name: Property = Property(name="name", type=StringType)
family_family.attributes={family_family_name}

# family_Root class attributes and methods

# family_university class attributes and methods
family_university_name: Property = Property(name="name", type=StringType)
family_university.attributes={family_university_name}

# family_studyprogramme class attributes and methods
family_studyprogramme_name: Property = Property(name="name", type=StringType)
family_studyprogramme.attributes={family_studyprogramme_name}

# family_person class attributes and methods
family_person_name: Property = Property(name="name", type=StringType)
family_person_age: Property = Property(name="age", type=StringType)
family_person_cpr: Property = Property(name="cpr", type=StringType)
family_person.attributes={family_person_age, family_person_cpr, family_person_name}

# Relationships
married2: BinaryAssociation = BinaryAssociation(
    name="married2",
    ends={
        Property(name="family_person", type=family_person, multiplicity=Multiplicity(1, 1)),
        Property(name="family_person1", type=family_person, multiplicity=Multiplicity(0, 1))
    }
)
children4: BinaryAssociation = BinaryAssociation(
    name="children4",
    ends={
        Property(name="family_person5", type=family_person, multiplicity=Multiplicity(1, 1)),
        Property(name="family_person3", type=family_person, multiplicity=Multiplicity(0, 9999))
    }
)
parents7: BinaryAssociation = BinaryAssociation(
    name="parents7",
    ends={
        Property(name="family_person8", type=family_person, multiplicity=Multiplicity(1, 1)),
        Property(name="family_person6", type=family_person, multiplicity=Multiplicity(0, 2))
    }
)
familymember9: BinaryAssociation = BinaryAssociation(
    name="familymember9",
    ends={
        Property(name="family_person10", type=family_family, multiplicity=Multiplicity(1, 1)),
        Property(name="family_family", type=family_person, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
enrolledStudents11: BinaryAssociation = BinaryAssociation(
    name="enrolledStudents11",
    ends={
        Property(name="family_person13", type=family_studyprogramme, multiplicity=Multiplicity(1, 1)),
        Property(name="family_studyprogramme12", type=family_person, multiplicity=Multiplicity(0, 9999))
    }
)
families14: BinaryAssociation = BinaryAssociation(
    name="families14",
    ends={
        Property(name="family_family15", type=family_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="family_Root", type=family_family, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
universities16: BinaryAssociation = BinaryAssociation(
    name="universities16",
    ends={
        Property(name="family_university18", type=family_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="family_Root17", type=family_university, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owns0: BinaryAssociation = BinaryAssociation(
    name="owns0",
    ends={
        Property(name="family_studyprogramme", type=family_university, multiplicity=Multiplicity(1, 1)),
        Property(name="family_university", type=family_studyprogramme, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="family",
    types={family_family, family_Root, family_university, family_studyprogramme, family_person},
    associations={married2, children4, parents7, familymember9, enrolledStudents11, families14, universities16, owns0},
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