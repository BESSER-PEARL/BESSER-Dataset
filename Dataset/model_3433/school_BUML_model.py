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
school_ClassGroup = Class(name="school::ClassGroup")
school_Student = Class(name="school::Student")
school_Teacher = Class(name="school::Teacher")
school_ClassLevel = Class(name="school::ClassLevel")
school_Room = Class(name="school::Room")
school_NewEClass7 = Class(name="school::NewEClass7")
school_store = Class(name="school::store")
school_SchoolYear = Class(name="school::SchoolYear")

# school_ClassGroup class attributes and methods
school_ClassGroup_name: Property = Property(name="name", type=StringType)
school_ClassGroup.attributes={school_ClassGroup_name}

# school_Student class attributes and methods
school_Student_name: Property = Property(name="name", type=StringType)
school_Student.attributes={school_Student_name}

# school_Teacher class attributes and methods
school_Teacher_name: Property = Property(name="name", type=StringType)
school_Teacher.attributes={school_Teacher_name}

# school_ClassLevel class attributes and methods
school_ClassLevel_level: Property = Property(name="level", type=IntegerType)
school_ClassLevel.attributes={school_ClassLevel_level}

# school_Room class attributes and methods
school_Room_location: Property = Property(name="location", type=StringType)
school_Room_m_AffectTeacher: Method = Method(name="AffectTeacher", parameters={Parameter(name='t')}, type=StringType)
school_Room.attributes={school_Room_location}
school_Room.methods={school_Room_m_AffectTeacher}

# school_NewEClass7 class attributes and methods

# school_store class attributes and methods
school_store_lastIn: Property = Property(name="lastIn", type=StringType)
school_store.attributes={school_store_lastIn}

# school_SchoolYear class attributes and methods
school_SchoolYear_year: Property = Property(name="year", type=DateType)
school_SchoolYear.attributes={school_SchoolYear_year}

# Relationships
eleves0: BinaryAssociation = BinaryAssociation(
    name="eleves0",
    ends={
        Property(name="school_Student", type=school_ClassGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="school_ClassGroup", type=school_Student, multiplicity=Multiplicity(0, 9999))
    }
)
room7: BinaryAssociation = BinaryAssociation(
    name="room7",
    ends={
        Property(name="school_Room9", type=school_Teacher, multiplicity=Multiplicity(1, 1)),
        Property(name="school_Teacher8", type=school_Room, multiplicity=Multiplicity(0, 1))
    }
)
prof1: BinaryAssociation = BinaryAssociation(
    name="prof1",
    ends={
        Property(name="school_Teacher", type=school_ClassGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="school_ClassGroup2", type=school_Teacher, multiplicity=Multiplicity(0, 9999))
    }
)
niveau3: BinaryAssociation = BinaryAssociation(
    name="niveau3",
    ends={
        Property(name="school_ClassLevel", type=school_ClassGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="school_ClassGroup4", type=school_ClassLevel, multiplicity=Multiplicity(1, 1))
    }
)
salle5: BinaryAssociation = BinaryAssociation(
    name="salle5",
    ends={
        Property(name="school_Room", type=school_ClassGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="school_ClassGroup6", type=school_Room, multiplicity=Multiplicity(0, 1))
    }
)
ecole10: BinaryAssociation = BinaryAssociation(
    name="ecole10",
    ends={
        Property(name="school_ClassGroup11", type=school_SchoolYear, multiplicity=Multiplicity(1, 1)),
        Property(name="school_SchoolYear", type=school_ClassGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eleves12: BinaryAssociation = BinaryAssociation(
    name="eleves12",
    ends={
        Property(name="school_Student14", type=school_SchoolYear, multiplicity=Multiplicity(1, 1)),
        Property(name="school_SchoolYear13", type=school_Student, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
niveau15: BinaryAssociation = BinaryAssociation(
    name="niveau15",
    ends={
        Property(name="school_ClassLevel17", type=school_SchoolYear, multiplicity=Multiplicity(1, 1)),
        Property(name="school_SchoolYear16", type=school_ClassLevel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="school",
    types={school_ClassGroup, school_Student, school_Teacher, school_ClassLevel, school_Room, school_NewEClass7, school_store, school_SchoolYear},
    associations={eleves0, room7, prof1, niveau3, salle5, ecole10, eleves12, niveau15},
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