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
school_School = Class(name="school::School")
school_Academy = Class(name="school::Academy")
school_Teacher = Class(name="school::Teacher")
school_Notation = Class(name="school::Notation")
school_ClassRoom = Class(name="school::ClassRoom")
school_Matter = Class(name="school::Matter")
school_Math = Class(name="school::Math")
Matter = Class(name="Matter")

# school_Student class attributes and methods
school_Student_name: Property = Property(name="name", type=StringType)
school_Student_age: Property = Property(name="age", type=IntegerType)
school_Student.attributes={school_Student_name, school_Student_age}

# school_School class attributes and methods
school_School_name: Property = Property(name="name", type=StringType)
school_School_rank: Property = Property(name="rank", type=IntegerType)
school_School.attributes={school_School_name, school_School_rank}

# school_Academy class attributes and methods
school_Academy_name: Property = Property(name="name", type=StringType)
school_Academy.attributes={school_Academy_name}

# school_Teacher class attributes and methods
school_Teacher_name: Property = Property(name="name", type=StringType)
school_Teacher_m_evaluate: Method = Method(name="evaluate", parameters={Parameter(name='student')}, type=StringType)
school_Teacher.attributes={school_Teacher_name}
school_Teacher.methods={school_Teacher_m_evaluate}

# school_Notation class attributes and methods
school_Notation_value: Property = Property(name="value", type=IntegerType)
school_Notation.attributes={school_Notation_value}

# school_ClassRoom class attributes and methods
school_ClassRoom_number: Property = Property(name="number", type=IntegerType)
school_ClassRoom.attributes={school_ClassRoom_number}

# school_Matter class attributes and methods

# school_Math class attributes and methods

# Matter class attributes and methods

# Relationships
students1: BinaryAssociation = BinaryAssociation(
    name="students1",
    ends={
        Property(name="school_Student", type=school_Academy, multiplicity=Multiplicity(1, 1)),
        Property(name="school_Academy2", type=school_Student, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
schools3: BinaryAssociation = BinaryAssociation(
    name="schools3",
    ends={
        Property(name="school_School", type=school_Academy, multiplicity=Multiplicity(1, 1)),
        Property(name="school_Academy4", type=school_School, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
teachers0: BinaryAssociation = BinaryAssociation(
    name="teachers0",
    ends={
        Property(name="school_Teacher", type=school_Academy, multiplicity=Multiplicity(1, 1)),
        Property(name="school_Academy", type=school_Teacher, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
notations19: BinaryAssociation = BinaryAssociation(
    name="notations19",
    ends={
        Property(name="school_Notation", type=school_Student, multiplicity=Multiplicity(1, 1)),
        Property(name="school_Student20", type=school_Notation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rooms5: BinaryAssociation = BinaryAssociation(
    name="rooms5",
    ends={
        Property(name="school_ClassRoom", type=school_School, multiplicity=Multiplicity(1, 1)),
        Property(name="school_School6", type=school_ClassRoom, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
teachers7: BinaryAssociation = BinaryAssociation(
    name="teachers7",
    ends={
        Property(name="school_Teacher9", type=school_School, multiplicity=Multiplicity(1, 1)),
        Property(name="school_School8", type=school_Teacher, multiplicity=Multiplicity(1, 9999))
    }
)
students10: BinaryAssociation = BinaryAssociation(
    name="students10",
    ends={
        Property(name="school_Student12", type=school_School, multiplicity=Multiplicity(1, 1)),
        Property(name="school_School11", type=school_Student, multiplicity=Multiplicity(1, 9999))
    }
)
teacher13: BinaryAssociation = BinaryAssociation(
    name="teacher13",
    ends={
        Property(name="school_Teacher15", type=school_ClassRoom, multiplicity=Multiplicity(1, 1)),
        Property(name="school_ClassRoom14", type=school_Teacher, multiplicity=Multiplicity(1, 1))
    }
)
children16: BinaryAssociation = BinaryAssociation(
    name="children16",
    ends={
        Property(name="school_Student18", type=school_ClassRoom, multiplicity=Multiplicity(1, 1)),
        Property(name="school_ClassRoom17", type=school_Student, multiplicity=Multiplicity(1, 9999))
    }
)

# Generalizations
gen_school_Math_Matter = Generalization(general=Matter, specific=school_Math)

# Domain Model
domain_model = DomainModel(
    name="school",
    types={school_Student, school_School, school_Academy, school_Teacher, school_Notation, school_ClassRoom, school_Matter, school_Math, Matter},
    associations={students1, schools3, teachers0, notations19, rooms5, teachers7, students10, teacher13, children16},
    generalizations={gen_school_Math_Matter},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)