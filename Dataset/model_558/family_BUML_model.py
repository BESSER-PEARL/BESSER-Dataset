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
family_person = Class(name="family::person")
family_course = Class(name="family::course")
family_university = Class(name="family::university")
family_Family = Class(name="family::Family")

# family_person class attributes and methods
family_person_name: Property = Property(name="name", type=StringType)
family_person_age: Property = Property(name="age", type=IntegerType)
family_person_CPR: Property = Property(name="CPR", type=StringType)
family_person.attributes={family_person_CPR, family_person_name, family_person_age}

# family_course class attributes and methods
family_course_name: Property = Property(name="name", type=StringType)
family_course.attributes={family_course_name}

# family_university class attributes and methods
family_university_name: Property = Property(name="name", type=StringType)
family_university.attributes={family_university_name}

# family_Family class attributes and methods

# Relationships
spouse1: BinaryAssociation = BinaryAssociation(
    name="spouse1",
    ends={
        Property(name="family_person", type=family_person, multiplicity=Multiplicity(1, 1)),
        Property(name="family_person0", type=family_person, multiplicity=Multiplicity(0, 1))
    }
)
courses10: BinaryAssociation = BinaryAssociation(
    name="courses10",
    ends={
        Property(name="family_course", type=family_university, multiplicity=Multiplicity(1, 1)),
        Property(name="family_university11", type=family_course, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent3: BinaryAssociation = BinaryAssociation(
    name="parent3",
    ends={
        Property(name="family_person4", type=family_person, multiplicity=Multiplicity(1, 1)),
        Property(name="family_person2", type=family_person, multiplicity=Multiplicity(0, 1))
    }
)
children6: BinaryAssociation = BinaryAssociation(
    name="children6",
    ends={
        Property(name="family_person7", type=family_person, multiplicity=Multiplicity(1, 1)),
        Property(name="family_person5", type=family_person, multiplicity=Multiplicity(0, 9999))
    }
)
enrollment8: BinaryAssociation = BinaryAssociation(
    name="enrollment8",
    ends={
        Property(name="family_university", type=family_person, multiplicity=Multiplicity(1, 1)),
        Property(name="family_person9", type=family_university, multiplicity=Multiplicity(0, 9999))
    }
)
students12: BinaryAssociation = BinaryAssociation(
    name="students12",
    ends={
        Property(name="family_person14", type=family_course, multiplicity=Multiplicity(1, 1)),
        Property(name="family_course13", type=family_person, multiplicity=Multiplicity(0, 9999))
    }
)
members16: BinaryAssociation = BinaryAssociation(
    name="members16",
    ends={
        Property(name="family_Family", type=family_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="family_Family15", type=family_Family, multiplicity=Multiplicity(0, 1))
    }
)
Members17: BinaryAssociation = BinaryAssociation(
    name="Members17",
    ends={
        Property(name="family_person19", type=family_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="family_Family18", type=family_person, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="family",
    types={family_person, family_course, family_university, family_Family},
    associations={spouse1, courses10, parent3, children6, enrollment8, students12, members16, Members17},
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