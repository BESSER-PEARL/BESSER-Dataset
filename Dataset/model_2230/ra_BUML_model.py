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
programmeCode: Enumeration = Enumeration(
    name="programmeCode",
    literals={
            EnumerationLiteral(name="Datateknologi5"),
			EnumerationLiteral(name="Informatikk"),
			EnumerationLiteral(name="Datateknologi2")
    }
)

# Classes
ra_Department = Class(name="ra::Department")
ra_Programme = Class(name="ra::Programme")
ra_Course = Class(name="ra::Course")
ra_StudyPlan = Class(name="ra::StudyPlan")
ra_Specialization = Class(name="ra::Specialization")
ra_MandatoryCourse = Class(name="ra::MandatoryCourse")
ra_Semester = Class(name="ra::Semester")

# ra_Department class attributes and methods

# ra_Programme class attributes and methods
ra_Programme_name: Property = Property(name="name", type=StringType)
ra_Programme_mCode: Property = Property(name="mCode", type=StringType)
ra_Programme.attributes={ra_Programme_mCode, ra_Programme_name}

# ra_Course class attributes and methods
ra_Course_name: Property = Property(name="name", type=StringType)
ra_Course_code: Property = Property(name="code", type=StringType)
ra_Course.attributes={ra_Course_code, ra_Course_name}

# ra_StudyPlan class attributes and methods

# ra_Specialization class attributes and methods
ra_Specialization_name: Property = Property(name="name", type=StringType)
ra_Specialization.attributes={ra_Specialization_name}

# ra_MandatoryCourse class attributes and methods
ra_MandatoryCourse_mandatory: Property = Property(name="mandatory", type=BooleanType)
ra_MandatoryCourse_credit: Property = Property(name="credit", type=FloatType)
ra_MandatoryCourse.attributes={ra_MandatoryCourse_mandatory, ra_MandatoryCourse_credit}

# ra_Semester class attributes and methods
ra_Semester_totalPoints: Property = Property(name="totalPoints", type=FloatType)
ra_Semester_semesterNumber: Property = Property(name="semesterNumber", type=IntegerType)
ra_Semester.attributes={ra_Semester_totalPoints, ra_Semester_semesterNumber}

# Relationships
programme0: BinaryAssociation = BinaryAssociation(
    name="programme0",
    ends={
        Property(name="ra_Programme", type=ra_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="ra_Department", type=ra_Programme, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
course1: BinaryAssociation = BinaryAssociation(
    name="course1",
    ends={
        Property(name="ra_Course", type=ra_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="ra_Department2", type=ra_Course, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
studyPlan3: BinaryAssociation = BinaryAssociation(
    name="studyPlan3",
    ends={
        Property(name="ra_StudyPlan", type=ra_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="ra_Department4", type=ra_StudyPlan, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
spesialization5: BinaryAssociation = BinaryAssociation(
    name="spesialization5",
    ends={
        Property(name="ra_Specialization", type=ra_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="ra_Department6", type=ra_Specialization, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mandatoryCourse7: BinaryAssociation = BinaryAssociation(
    name="mandatoryCourse7",
    ends={
        Property(name="MandatoryCourse", type=ra_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="course", type=ra_MandatoryCourse, multiplicity=Multiplicity(0, 1))
    }
)
programme9: BinaryAssociation = BinaryAssociation(
    name="programme9",
    ends={
        Property(name="Programme", type=ra_StudyPlan, multiplicity=Multiplicity(1, 1)),
        Property(name="studyPlan", type=ra_Programme, multiplicity=Multiplicity(0, 1))
    }
)
studyPlan8: BinaryAssociation = BinaryAssociation(
    name="studyPlan8",
    ends={
        Property(name="StudyPlan", type=ra_Programme, multiplicity=Multiplicity(1, 1)),
        Property(name="programme", type=ra_StudyPlan, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
spesialization10: BinaryAssociation = BinaryAssociation(
    name="spesialization10",
    ends={
        Property(name="ra_Specialization12", type=ra_StudyPlan, multiplicity=Multiplicity(1, 1)),
        Property(name="ra_StudyPlan11", type=ra_Specialization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
semester13: BinaryAssociation = BinaryAssociation(
    name="semester13",
    ends={
        Property(name="ra_Semester", type=ra_StudyPlan, multiplicity=Multiplicity(1, 1)),
        Property(name="ra_StudyPlan14", type=ra_Semester, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mandatoryCourse15: BinaryAssociation = BinaryAssociation(
    name="mandatoryCourse15",
    ends={
        Property(name="ra_MandatoryCourse", type=ra_StudyPlan, multiplicity=Multiplicity(1, 1)),
        Property(name="ra_StudyPlan16", type=ra_MandatoryCourse, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
semester17: BinaryAssociation = BinaryAssociation(
    name="semester17",
    ends={
        Property(name="ra_Semester19", type=ra_Specialization, multiplicity=Multiplicity(1, 1)),
        Property(name="ra_Specialization18", type=ra_Semester, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
courseSlot20: BinaryAssociation = BinaryAssociation(
    name="courseSlot20",
    ends={
        Property(name="ra_Course22", type=ra_Semester, multiplicity=Multiplicity(1, 1)),
        Property(name="ra_Semester21", type=ra_Course, multiplicity=Multiplicity(0, 9999))
    }
)
mandatoryCourse23: BinaryAssociation = BinaryAssociation(
    name="mandatoryCourse23",
    ends={
        Property(name="MandatoryCourse24", type=ra_Semester, multiplicity=Multiplicity(1, 1)),
        Property(name="semester", type=ra_MandatoryCourse, multiplicity=Multiplicity(0, 9999))
    }
)
semester25: BinaryAssociation = BinaryAssociation(
    name="semester25",
    ends={
        Property(name="Semester", type=ra_MandatoryCourse, multiplicity=Multiplicity(1, 1)),
        Property(name="mandatoryCourse", type=ra_Semester, multiplicity=Multiplicity(0, 1))
    }
)
course26: BinaryAssociation = BinaryAssociation(
    name="course26",
    ends={
        Property(name="Course", type=ra_MandatoryCourse, multiplicity=Multiplicity(1, 1)),
        Property(name="mandatoryCourse27", type=ra_Course, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="ra",
    types={ra_Department, ra_Programme, ra_Course, ra_StudyPlan, ra_Specialization, ra_MandatoryCourse, ra_Semester, programmeCode},
    associations={programme0, course1, studyPlan3, spesialization5, mandatoryCourse7, programme9, studyPlan8, spesialization10, semester13, mandatoryCourse15, semester17, courseSlot20, mandatoryCourse23, semester25, course26},
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