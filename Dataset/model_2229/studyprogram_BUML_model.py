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
Season: Enumeration = Enumeration(
    name="Season",
    literals={
            EnumerationLiteral(name="Fall"),
			EnumerationLiteral(name="Spring"),
			EnumerationLiteral(name="Summer")
    }
)

# Classes
studyprogram_Program = Class(name="studyprogram::Program")
studyprogram_Semester = Class(name="studyprogram::Semester")
studyprogram_Specialization = Class(name="studyprogram::Specialization")
studyprogram_Course = Class(name="studyprogram::Course")
studyprogram_Department = Class(name="studyprogram::Department")
studyprogram_Slot = Class(name="studyprogram::Slot")

# studyprogram_Program class attributes and methods
studyprogram_Program_name: Property = Property(name="name", type=StringType)
studyprogram_Program.attributes={studyprogram_Program_name}

# studyprogram_Semester class attributes and methods
studyprogram_Semester_season: Property = Property(name="season", type=StringType)
studyprogram_Semester_year: Property = Property(name="year", type=IntegerType)
studyprogram_Semester.attributes={studyprogram_Semester_year, studyprogram_Semester_season}

# studyprogram_Specialization class attributes and methods
studyprogram_Specialization_name: Property = Property(name="name", type=StringType)
studyprogram_Specialization.attributes={studyprogram_Specialization_name}

# studyprogram_Course class attributes and methods
studyprogram_Course_name: Property = Property(name="name", type=StringType)
studyprogram_Course_credits: Property = Property(name="credits", type=FloatType)
studyprogram_Course.attributes={studyprogram_Course_name, studyprogram_Course_credits}

# studyprogram_Department class attributes and methods
studyprogram_Department_name: Property = Property(name="name", type=StringType)
studyprogram_Department.attributes={studyprogram_Department_name}

# studyprogram_Slot class attributes and methods

# Relationships
baseSemesters0: BinaryAssociation = BinaryAssociation(
    name="baseSemesters0",
    ends={
        Property(name="studyprogram_Semester", type=studyprogram_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="studyprogram_Program", type=studyprogram_Semester, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
specializations1: BinaryAssociation = BinaryAssociation(
    name="specializations1",
    ends={
        Property(name="studyprogram_Specialization", type=studyprogram_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="studyprogram_Program2", type=studyprogram_Specialization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specializationSemesters3: BinaryAssociation = BinaryAssociation(
    name="specializationSemesters3",
    ends={
        Property(name="studyprogram_Semester5", type=studyprogram_Specialization, multiplicity=Multiplicity(1, 1)),
        Property(name="studyprogram_Specialization4", type=studyprogram_Semester, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
additionalSpecializations7: BinaryAssociation = BinaryAssociation(
    name="additionalSpecializations7",
    ends={
        Property(name="studyprogram_Specialization8", type=studyprogram_Specialization, multiplicity=Multiplicity(1, 1)),
        Property(name="studyprogram_Specialization6", type=studyprogram_Specialization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
availableCourses11: BinaryAssociation = BinaryAssociation(
    name="availableCourses11",
    ends={
        Property(name="studyprogram_Course", type=studyprogram_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="studyprogram_Slot12", type=studyprogram_Course, multiplicity=Multiplicity(1, 9999))
    }
)
selectedCourse13: BinaryAssociation = BinaryAssociation(
    name="selectedCourse13",
    ends={
        Property(name="studyprogram_Course15", type=studyprogram_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="studyprogram_Slot14", type=studyprogram_Course, multiplicity=Multiplicity(1, 1))
    }
)
courses16: BinaryAssociation = BinaryAssociation(
    name="courses16",
    ends={
        Property(name="studyprogram_Course17", type=studyprogram_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="studyprogram_Department", type=studyprogram_Course, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
programs18: BinaryAssociation = BinaryAssociation(
    name="programs18",
    ends={
        Property(name="studyprogram_Program20", type=studyprogram_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="studyprogram_Department19", type=studyprogram_Program, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
slots9: BinaryAssociation = BinaryAssociation(
    name="slots9",
    ends={
        Property(name="studyprogram_Slot", type=studyprogram_Semester, multiplicity=Multiplicity(1, 1)),
        Property(name="studyprogram_Semester10", type=studyprogram_Slot, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="studyprogram",
    types={studyprogram_Program, studyprogram_Semester, studyprogram_Specialization, studyprogram_Course, studyprogram_Department, studyprogram_Slot, Season},
    associations={baseSemesters0, specializations1, specializationSemesters3, additionalSpecializations7, availableCourses11, selectedCourse13, courses16, programs18, slots9},
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