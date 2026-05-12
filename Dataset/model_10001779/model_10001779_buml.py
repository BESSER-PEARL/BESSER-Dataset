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
Room = Class(name="Room")
Teacher = Class(name="Teacher")
Class_ = Class(name="Class")
c = Class(name="c")
c1 = Class(name="c1")
Class2 = Class(name="Class2")
Class3 = Class(name="Class3")
Class4 = Class(name="Class4")

# Room class attributes and methods
Room_Name: Property = Property(name="Name", type=StringType)
Room.attributes={Room_Name}

# Teacher class attributes and methods
Teacher_Name: Property = Property(name="Name", type=StringType)
Teacher.attributes={Teacher_Name}

# Class class attributes and methods

# c class attributes and methods

# c1 class attributes and methods

# Class2 class attributes and methods

# Class3 class attributes and methods

# Class4 class attributes and methods

# Relationships
teaches: BinaryAssociation = BinaryAssociation(
    name="teaches",
    ends={
        Property(name="room0", type=Room, multiplicity=Multiplicity(1, 1)),
        Property(name="teacher1", type=Teacher, multiplicity=Multiplicity(0, 9999))
    }
)
Room_Class4: BinaryAssociation = BinaryAssociation(
    name="Room_Class4",
    ends={
        Property(name="class42", type=Class4, multiplicity=Multiplicity(0, 1)),
        Property(name="room3", type=Room, multiplicity=Multiplicity(0, 1))
    }
)
Class4_c: BinaryAssociation = BinaryAssociation(
    name="Class4_c",
    ends={
        Property(name="c4", type=c1, multiplicity=Multiplicity(0, 1)),
        Property(name="class45", type=Class4, multiplicity=Multiplicity(0, 1))
    }
)
c_Class: BinaryAssociation = BinaryAssociation(
    name="c_Class",
    ends={
        Property(name="class6", type=Class_, multiplicity=Multiplicity(0, 1)),
        Property(name="c7", type=c1, multiplicity=Multiplicity(0, 1))
    }
)
Class_c: BinaryAssociation = BinaryAssociation(
    name="Class_c",
    ends={
        Property(name="c8", type=c, multiplicity=Multiplicity(0, 1)),
        Property(name="class9", type=Class_, multiplicity=Multiplicity(0, 1))
    }
)
c_Class2: BinaryAssociation = BinaryAssociation(
    name="c_Class2",
    ends={
        Property(name="class210", type=Class2, multiplicity=Multiplicity(0, 1)),
        Property(name="c11", type=c, multiplicity=Multiplicity(0, 1))
    }
)
Class3_Class2: BinaryAssociation = BinaryAssociation(
    name="Class3_Class2",
    ends={
        Property(name="class212", type=Class2, multiplicity=Multiplicity(0, 1)),
        Property(name="class313", type=Class3, multiplicity=Multiplicity(0, 1))
    }
)
Class3_Class3: BinaryAssociation = BinaryAssociation(
    name="Class3_Class3",
    ends={
        Property(name="class314", type=Class3, multiplicity=Multiplicity(0, 1)),
        Property(name="class315", type=Class3, multiplicity=Multiplicity(0, 1))
    }
)
Class2_Class2: BinaryAssociation = BinaryAssociation(
    name="Class2_Class2",
    ends={
        Property(name="class216", type=Class2, multiplicity=Multiplicity(0, 1)),
        Property(name="class217", type=Class2, multiplicity=Multiplicity(0, 1))
    }
)
Class2_Class22: BinaryAssociation = BinaryAssociation(
    name="Class2_Class22",
    ends={
        Property(name="class218", type=Class2, multiplicity=Multiplicity(0, 1)),
        Property(name="class219", type=Class2, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_V1_cwGSnEeio56zSTH7puw",
    types={Room, Teacher, Class_, c, c1, Class2, Class3, Class4},
    associations={teaches, Room_Class4, Class4_c, c_Class, Class_c, c_Class2, Class3_Class2, Class3_Class3, Class2_Class2, Class2_Class22},
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