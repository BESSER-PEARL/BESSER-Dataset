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
prosjekt_Department = Class(name="prosjekt::Department")
prosjekt_University = Class(name="prosjekt::University")
prosjekt_Course = Class(name="prosjekt::Course")
prosjekt_Person = Class(name="prosjekt::Person")
prosjekt_Semester = Class(name="prosjekt::Semester")
prosjekt_CourseCoordinator = Class(name="prosjekt::CourseCoordinator")

# prosjekt_Department class attributes and methods
prosjekt_Department_name: Property = Property(name="name", type=StringType)
prosjekt_Department_shortName: Property = Property(name="shortName", type=StringType)
prosjekt_Department.attributes={prosjekt_Department_name, prosjekt_Department_shortName}

# prosjekt_University class attributes and methods
prosjekt_University_shortName: Property = Property(name="shortName", type=StringType)
prosjekt_University_name: Property = Property(name="name", type=StringType)
prosjekt_University.attributes={prosjekt_University_name, prosjekt_University_shortName}

# prosjekt_Course class attributes and methods
prosjekt_Course_name: Property = Property(name="name", type=StringType)
prosjekt_Course_code: Property = Property(name="code", type=StringType)
prosjekt_Course_studyPoints: Property = Property(name="studyPoints", type=FloatType)
prosjekt_Course.attributes={prosjekt_Course_name, prosjekt_Course_code, prosjekt_Course_studyPoints}

# prosjekt_Person class attributes and methods
prosjekt_Person_name: Property = Property(name="name", type=StringType)
prosjekt_Person.attributes={prosjekt_Person_name}

# prosjekt_Semester class attributes and methods
prosjekt_Semester_name: Property = Property(name="name", type=StringType)
prosjekt_Semester_averageGrade: Property = Property(name="averageGrade", type=FloatType)
prosjekt_Semester_amountA: Property = Property(name="amountA", type=IntegerType)
prosjekt_Semester_amountB: Property = Property(name="amountB", type=IntegerType)
prosjekt_Semester_amountC: Property = Property(name="amountC", type=IntegerType)
prosjekt_Semester_amountD: Property = Property(name="amountD", type=IntegerType)
prosjekt_Semester_amountE: Property = Property(name="amountE", type=IntegerType)
prosjekt_Semester_amountF: Property = Property(name="amountF", type=IntegerType)
prosjekt_Semester.attributes={prosjekt_Semester_averageGrade, prosjekt_Semester_amountE, prosjekt_Semester_amountF, prosjekt_Semester_amountB, prosjekt_Semester_amountA, prosjekt_Semester_amountD, prosjekt_Semester_name, prosjekt_Semester_amountC}

# prosjekt_CourseCoordinator class attributes and methods

# Relationships
departments0: BinaryAssociation = BinaryAssociation(
    name="departments0",
    ends={
        Property(name="Department", type=prosjekt_University, multiplicity=Multiplicity(1, 1)),
        Property(name="university", type=prosjekt_Department, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
university1: BinaryAssociation = BinaryAssociation(
    name="university1",
    ends={
        Property(name="University", type=prosjekt_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="departments", type=prosjekt_University, multiplicity=Multiplicity(1, 1))
    }
)
course2: BinaryAssociation = BinaryAssociation(
    name="course2",
    ends={
        Property(name="Course", type=prosjekt_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="department", type=prosjekt_Course, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
staff3: BinaryAssociation = BinaryAssociation(
    name="staff3",
    ends={
        Property(name="Person", type=prosjekt_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="worksForDepartment", type=prosjekt_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
semester6: BinaryAssociation = BinaryAssociation(
    name="semester6",
    ends={
        Property(name="course7", type=prosjekt_Semester, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="Semester", type=prosjekt_Course, multiplicity=Multiplicity(1, 1))
    }
)
department4: BinaryAssociation = BinaryAssociation(
    name="department4",
    ends={
        Property(name="Department5", type=prosjekt_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="course", type=prosjekt_Department, multiplicity=Multiplicity(1, 1))
    }
)
worksForDepartment10: BinaryAssociation = BinaryAssociation(
    name="worksForDepartment10",
    ends={
        Property(name="Department11", type=prosjekt_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="staff", type=prosjekt_Department, multiplicity=Multiplicity(0, 1))
    }
)
roles12: BinaryAssociation = BinaryAssociation(
    name="roles12",
    ends={
        Property(name="CourseCoordinator", type=prosjekt_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="person", type=prosjekt_CourseCoordinator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
course8: BinaryAssociation = BinaryAssociation(
    name="course8",
    ends={
        Property(name="Course9", type=prosjekt_Semester, multiplicity=Multiplicity(1, 1)),
        Property(name="semester", type=prosjekt_Course, multiplicity=Multiplicity(0, 1))
    }
)
course13: BinaryAssociation = BinaryAssociation(
    name="course13",
    ends={
        Property(name="prosjekt_Course", type=prosjekt_CourseCoordinator, multiplicity=Multiplicity(1, 1)),
        Property(name="prosjekt_CourseCoordinator", type=prosjekt_Course, multiplicity=Multiplicity(0, 1))
    }
)
person14: BinaryAssociation = BinaryAssociation(
    name="person14",
    ends={
        Property(name="Person15", type=prosjekt_CourseCoordinator, multiplicity=Multiplicity(1, 1)),
        Property(name="roles", type=prosjekt_Person, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="prosjekt",
    types={prosjekt_Department, prosjekt_University, prosjekt_Course, prosjekt_Person, prosjekt_Semester, prosjekt_CourseCoordinator},
    associations={departments0, university1, course2, staff3, semester6, department4, worksForDepartment10, roles12, course8, course13, person14},
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