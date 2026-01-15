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
classmate_Classroom = Class(name="classmate::Classroom")
classmate_Student = Class(name="classmate::Student")
classmate_ClassmateSystem = Class(name="classmate::ClassmateSystem")
classmate_School = Class(name="classmate::School")
classmate_Friend = Class(name="classmate::Friend")

# classmate_Classroom class attributes and methods
classmate_Classroom_name: Property = Property(name="name", type=StringType)
classmate_Classroom.attributes={classmate_Classroom_name}

# classmate_Student class attributes and methods
classmate_Student_name: Property = Property(name="name", type=StringType)
classmate_Student.attributes={classmate_Student_name}

# classmate_ClassmateSystem class attributes and methods

# classmate_School class attributes and methods
classmate_School_name: Property = Property(name="name", type=StringType)
classmate_School.attributes={classmate_School_name}

# classmate_Friend class attributes and methods
classmate_Friend_fromDate: Property = Property(name="fromDate", type=StringType)
classmate_Friend_toDate: Property = Property(name="toDate", type=StringType)
classmate_Friend.attributes={classmate_Friend_toDate, classmate_Friend_fromDate}

# Relationships
classrooms4: BinaryAssociation = BinaryAssociation(
    name="classrooms4",
    ends={
        Property(name="classmate_Classroom6", type=classmate_School, multiplicity=Multiplicity(1, 1)),
        Property(name="classmate_School5", type=classmate_Classroom, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
students0: BinaryAssociation = BinaryAssociation(
    name="students0",
    ends={
        Property(name="classmate_Student", type=classmate_Classroom, multiplicity=Multiplicity(1, 1)),
        Property(name="classmate_Classroom", type=classmate_Student, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
school1: BinaryAssociation = BinaryAssociation(
    name="school1",
    ends={
        Property(name="classmate_School", type=classmate_ClassmateSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="classmate_ClassmateSystem", type=classmate_School, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
friends2: BinaryAssociation = BinaryAssociation(
    name="friends2",
    ends={
        Property(name="classmate_Friend", type=classmate_ClassmateSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="classmate_ClassmateSystem3", type=classmate_Friend, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fromStudent7: BinaryAssociation = BinaryAssociation(
    name="fromStudent7",
    ends={
        Property(name="classmate_Student9", type=classmate_Friend, multiplicity=Multiplicity(1, 1)),
        Property(name="classmate_Friend8", type=classmate_Student, multiplicity=Multiplicity(0, 1))
    }
)
toStudent10: BinaryAssociation = BinaryAssociation(
    name="toStudent10",
    ends={
        Property(name="classmate_Student12", type=classmate_Friend, multiplicity=Multiplicity(1, 1)),
        Property(name="classmate_Friend11", type=classmate_Student, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="classmate",
    types={classmate_Classroom, classmate_Student, classmate_ClassmateSystem, classmate_School, classmate_Friend},
    associations={classrooms4, students0, school1, friends2, fromStudent7, toStudent10},
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