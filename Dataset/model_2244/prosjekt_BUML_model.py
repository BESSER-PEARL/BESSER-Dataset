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
prosjekt_Institute = Class(name="prosjekt::Institute")
prosjekt_Course = Class(name="prosjekt::Course")
prosjekt_CourseCoordinator = Class(name="prosjekt::CourseCoordinator")
prosjekt_Semester = Class(name="prosjekt::Semester")

# prosjekt_Institute class attributes and methods
prosjekt_Institute_name: Property = Property(name="name", type=StringType)
prosjekt_Institute_shortName: Property = Property(name="shortName", type=StringType)
prosjekt_Institute.attributes={prosjekt_Institute_name, prosjekt_Institute_shortName}

# prosjekt_Course class attributes and methods
prosjekt_Course_name: Property = Property(name="name", type=StringType)
prosjekt_Course_code: Property = Property(name="code", type=StringType)
prosjekt_Course_avgGrade: Property = Property(name="avgGrade", type=IntegerType)
prosjekt_Course_studyPoints: Property = Property(name="studyPoints", type=FloatType)
prosjekt_Course.attributes={prosjekt_Course_studyPoints, prosjekt_Course_avgGrade, prosjekt_Course_code, prosjekt_Course_name}

# prosjekt_CourseCoordinator class attributes and methods
prosjekt_CourseCoordinator_name: Property = Property(name="name", type=StringType)
prosjekt_CourseCoordinator.attributes={prosjekt_CourseCoordinator_name}

# prosjekt_Semester class attributes and methods
prosjekt_Semester_name: Property = Property(name="name", type=StringType)
prosjekt_Semester.attributes={prosjekt_Semester_name}

# Relationships
course0: BinaryAssociation = BinaryAssociation(
    name="course0",
    ends={
        Property(name="Course", type=prosjekt_Institute, multiplicity=Multiplicity(1, 1)),
        Property(name="institute", type=prosjekt_Course, multiplicity=Multiplicity(0, 1))
    }
)
courseCoordinator1: BinaryAssociation = BinaryAssociation(
    name="courseCoordinator1",
    ends={
        Property(name="CourseCoordinator", type=prosjekt_Institute, multiplicity=Multiplicity(1, 1)),
        Property(name="institute2", type=prosjekt_CourseCoordinator, multiplicity=Multiplicity(0, 9999))
    }
)
institute3: BinaryAssociation = BinaryAssociation(
    name="institute3",
    ends={
        Property(name="Institute", type=prosjekt_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="course", type=prosjekt_Institute, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
semester4: BinaryAssociation = BinaryAssociation(
    name="semester4",
    ends={
        Property(name="Semester", type=prosjekt_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="course5", type=prosjekt_Semester, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
courseCoordinator6: BinaryAssociation = BinaryAssociation(
    name="courseCoordinator6",
    ends={
        Property(name="CourseCoordinator8", type=prosjekt_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="course7", type=prosjekt_CourseCoordinator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
course9: BinaryAssociation = BinaryAssociation(
    name="course9",
    ends={
        Property(name="Course10", type=prosjekt_Semester, multiplicity=Multiplicity(1, 1)),
        Property(name="semester", type=prosjekt_Course, multiplicity=Multiplicity(0, 1))
    }
)
course11: BinaryAssociation = BinaryAssociation(
    name="course11",
    ends={
        Property(name="Course12", type=prosjekt_CourseCoordinator, multiplicity=Multiplicity(1, 1)),
        Property(name="courseCoordinator", type=prosjekt_Course, multiplicity=Multiplicity(0, 1))
    }
)
institute13: BinaryAssociation = BinaryAssociation(
    name="institute13",
    ends={
        Property(name="Institute15", type=prosjekt_CourseCoordinator, multiplicity=Multiplicity(1, 1)),
        Property(name="courseCoordinator14", type=prosjekt_Institute, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="prosjekt",
    types={prosjekt_Institute, prosjekt_Course, prosjekt_CourseCoordinator, prosjekt_Semester},
    associations={course0, courseCoordinator1, institute3, semester4, courseCoordinator6, course9, course11, institute13},
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