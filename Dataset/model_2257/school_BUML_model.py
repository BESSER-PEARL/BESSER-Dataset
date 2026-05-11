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
school_Grade2 = Class(name="school_Grade2")
Grade = Class(name="Grade")
school_School = Class(name="school_School")
school_Pupil = Class(name="school_Pupil")
school_Course = Class(name="school_Course")
school_Grade = Class(name="school_Grade")

# school_Grade2 class attributes and methods

# Grade class attributes and methods

# school_School class attributes and methods

# school_Pupil class attributes and methods
school_Pupil_name: Property = Property(name="name", type=StringType)
school_Pupil_inclass: Property = Property(name="inclass", type=StringType)
school_Pupil.attributes={school_Pupil_inclass, school_Pupil_name}

# school_Course class attributes and methods
school_Course_name: Property = Property(name="name", type=StringType)
school_Course.attributes={school_Course_name}

# school_Grade class attributes and methods
school_Grade_grade: Property = Property(name="grade", type=StringType)
school_Grade_year: Property = Property(name="year", type=StringType)
school_Grade.attributes={school_Grade_year, school_Grade_grade}

# Relationships
course5: BinaryAssociation = BinaryAssociation(
    name="course5",
    ends={
        Property(name="school_Course7", type=school_Grade, multiplicity=Multiplicity(1, 1)),
        Property(name="school_Grade6", type=school_Course, multiplicity=Multiplicity(0, 1))
    }
)
pupils0: BinaryAssociation = BinaryAssociation(
    name="pupils0",
    ends={
        Property(name="school_Pupil", type=school_School, multiplicity=Multiplicity(1, 1)),
        Property(name="school_School", type=school_Pupil, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
courses1: BinaryAssociation = BinaryAssociation(
    name="courses1",
    ends={
        Property(name="school_Course", type=school_School, multiplicity=Multiplicity(1, 1)),
        Property(name="school_School2", type=school_Course, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
grades3: BinaryAssociation = BinaryAssociation(
    name="grades3",
    ends={
        Property(name="school_Grade", type=school_Pupil, multiplicity=Multiplicity(1, 1)),
        Property(name="school_Pupil4", type=school_Grade, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_school_Grade2_Grade = Generalization(general=Grade, specific=school_Grade2)

# Domain Model
domain_model = DomainModel(
    name="school",
    types={school_Grade2, Grade, school_School, school_Pupil, school_Course, school_Grade},
    associations={course5, pupils0, courses1, grades3},
    generalizations={gen_school_Grade2_Grade},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)