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
school_Student = Class(name="school::Student")
school_Diagram = Class(name="school::Diagram")
school_School = Class(name="school::School")
school_Classroom = Class(name="school::Classroom")

# school_Student class attributes and methods
school_Student_name: Property = Property(name="name", type=StringType)
school_Student_nickname: Property = Property(name="nickname", type=StringType)
school_Student_age: Property = Property(name="age", type=IntegerType)
school_Student_m_validate: Method = Method(name="validate", parameters={Parameter(name='diagnostic'), Parameter(name='context')}, type=BooleanType)
school_Student.attributes={school_Student_nickname, school_Student_name, school_Student_age}
school_Student.methods={school_Student_m_validate}

# school_Diagram class attributes and methods

# school_School class attributes and methods
school_School_name: Property = Property(name="name", type=StringType)
school_School_director: Property = Property(name="director", type=StringType)
school_School_zipCode: Property = Property(name="zipCode", type=StringType)
school_School_city: Property = Property(name="city", type=StringType)
school_School.attributes={school_School_director, school_School_name, school_School_city, school_School_zipCode}

# school_Classroom class attributes and methods
school_Classroom_name: Property = Property(name="name", type=StringType)
school_Classroom_teacher: Property = Property(name="teacher", type=StringType)
school_Classroom_rank: Property = Property(name="rank", type=IntegerType)
school_Classroom_capacity: Property = Property(name="capacity", type=IntegerType)
school_Classroom_m_validate: Method = Method(name="validate", parameters={Parameter(name='diagnostic'), Parameter(name='context')}, type=BooleanType)
school_Classroom.attributes={school_Classroom_teacher, school_Classroom_capacity, school_Classroom_rank, school_Classroom_name}
school_Classroom.methods={school_Classroom_m_validate}

# Relationships
students0: BinaryAssociation = BinaryAssociation(
    name="students0",
    ends={
        Property(name="school_Student", type=school_Classroom, multiplicity=Multiplicity(1, 1)),
        Property(name="school_Classroom", type=school_Student, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
school1: BinaryAssociation = BinaryAssociation(
    name="school1",
    ends={
        Property(name="school_School", type=school_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="school_Diagram", type=school_School, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classrooms2: BinaryAssociation = BinaryAssociation(
    name="classrooms2",
    ends={
        Property(name="school_Classroom4", type=school_School, multiplicity=Multiplicity(1, 1)),
        Property(name="school_School3", type=school_Classroom, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
friends6: BinaryAssociation = BinaryAssociation(
    name="friends6",
    ends={
        Property(name="school_Student7", type=school_Student, multiplicity=Multiplicity(1, 1)),
        Property(name="school_Student5", type=school_Student, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="school",
    types={school_Student, school_Diagram, school_School, school_Classroom},
    associations={students0, school1, classrooms2, friends6},
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