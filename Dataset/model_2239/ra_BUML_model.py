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

# Enumerations
SemesterKind: Enumeration = Enumeration(
    name="SemesterKind",
    literals={
            EnumerationLiteral(name="AUTUMN"),
			EnumerationLiteral(name="SPRING")
    }
)

# Classes
model_Department = Class(name="model::Department")
model_Person = Class(name="model::Person")
model_Course = Class(name="model::Course")
model_Role = Class(name="model::Role")
model_Semester = Class(name="model::Semester")
model_CourseAllocation = Class(name="model::CourseAllocation")
model_CourseInstance = Class(name="model::CourseInstance")

# model_Department class attributes and methods
model_Department_name: Property = Property(name="name", type=StringType)
model_Department.attributes={model_Department_name}

# model_Person class attributes and methods
model_Person_name: Property = Property(name="name", type=StringType)
model_Person_userName: Property = Property(name="userName", type=StringType)
model_Person_email: Property = Property(name="email", type=StringType)
model_Person_faceUrl: Property = Property(name="faceUrl", type=StringType)
model_Person_employmentFactor: Property = Property(name="employmentFactor", type=StringType)
model_Person.attributes={model_Person_email, model_Person_faceUrl, model_Person_name, model_Person_userName, model_Person_employmentFactor}

# model_Course class attributes and methods
model_Course_name: Property = Property(name="name", type=StringType)
model_Course_fullName: Property = Property(name="fullName", type=StringType)
model_Course.attributes={model_Course_fullName, model_Course_name}

# model_Role class attributes and methods
model_Role_name: Property = Property(name="name", type=StringType)
model_Role_factor: Property = Property(name="factor", type=StringType)
model_Role.attributes={model_Role_name, model_Role_factor}

# model_Semester class attributes and methods
model_Semester_year: Property = Property(name="year", type=StringType)
model_Semester_kind: Property = Property(name="kind", type=StringType)
model_Semester.attributes={model_Semester_year, model_Semester_kind}

# model_CourseAllocation class attributes and methods
model_CourseAllocation_factor: Property = Property(name="factor", type=StringType)
model_CourseAllocation_explicitFactor: Property = Property(name="explicitFactor", type=StringType)
model_CourseAllocation.attributes={model_CourseAllocation_explicitFactor, model_CourseAllocation_factor}

# model_CourseInstance class attributes and methods

# Relationships
employees0: BinaryAssociation = BinaryAssociation(
    name="employees0",
    ends={
        Property(name="model_Person", type=model_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Department", type=model_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
courses1: BinaryAssociation = BinaryAssociation(
    name="courses1",
    ends={
        Property(name="model_Course", type=model_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Department2", type=model_Course, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
roles3: BinaryAssociation = BinaryAssociation(
    name="roles3",
    ends={
        Property(name="model_Role", type=model_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Department4", type=model_Role, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
semesters5: BinaryAssociation = BinaryAssociation(
    name="semesters5",
    ends={
        Property(name="model_Semester", type=model_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Department6", type=model_Semester, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allocations7: BinaryAssociation = BinaryAssociation(
    name="allocations7",
    ends={
        Property(name="CourseAllocation", type=model_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="person", type=model_CourseAllocation, multiplicity=Multiplicity(0, 9999))
    }
)
requiredRoles8: BinaryAssociation = BinaryAssociation(
    name="requiredRoles8",
    ends={
        Property(name="model_Role10", type=model_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Course9", type=model_Role, multiplicity=Multiplicity(0, 9999))
    }
)
courses11: BinaryAssociation = BinaryAssociation(
    name="courses11",
    ends={
        Property(name="CourseInstance", type=model_Semester, multiplicity=Multiplicity(1, 1)),
        Property(name="semester", type=model_CourseInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
course12: BinaryAssociation = BinaryAssociation(
    name="course12",
    ends={
        Property(name="model_Course13", type=model_CourseInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="model_CourseInstance", type=model_Course, multiplicity=Multiplicity(0, 1))
    }
)
semester14: BinaryAssociation = BinaryAssociation(
    name="semester14",
    ends={
        Property(name="Semester", type=model_CourseInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="courses", type=model_Semester, multiplicity=Multiplicity(0, 1))
    }
)
allocations15: BinaryAssociation = BinaryAssociation(
    name="allocations15",
    ends={
        Property(name="CourseAllocation16", type=model_CourseInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="course", type=model_CourseAllocation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
person17: BinaryAssociation = BinaryAssociation(
    name="person17",
    ends={
        Property(name="Person", type=model_CourseAllocation, multiplicity=Multiplicity(1, 1)),
        Property(name="allocations", type=model_Person, multiplicity=Multiplicity(0, 1))
    }
)
role18: BinaryAssociation = BinaryAssociation(
    name="role18",
    ends={
        Property(name="model_Role19", type=model_CourseAllocation, multiplicity=Multiplicity(1, 1)),
        Property(name="model_CourseAllocation", type=model_Role, multiplicity=Multiplicity(0, 1))
    }
)
course20: BinaryAssociation = BinaryAssociation(
    name="course20",
    ends={
        Property(name="CourseInstance22", type=model_CourseAllocation, multiplicity=Multiplicity(1, 1)),
        Property(name="allocations21", type=model_CourseInstance, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="model",
    types={model_Department, model_Person, model_Course, model_Role, model_Semester, model_CourseAllocation, model_CourseInstance, SemesterKind},
    associations={employees0, courses1, roles3, semesters5, allocations7, requiredRoles8, courses11, course12, semester14, allocations15, person17, role18, course20},
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