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
university_Course = Class(name="university::Course")
university_University = Class(name="university::University")
university_Professor = Class(name="university::Professor")
university_Certificate = Class(name="university::Certificate")
university_Student = Class(name="university::Student")

# university_Course class attributes and methods
university_Course_name: Property = Property(name="name", type=StringType)
university_Course_gradeAverage: Property = Property(name="gradeAverage", type=FloatType)
university_Course_numberOfAttendants: Property = Property(name="numberOfAttendants", type=IntegerType)
university_Course.attributes={university_Course_gradeAverage, university_Course_numberOfAttendants, university_Course_name}

# university_University class attributes and methods
university_University_name: Property = Property(name="name", type=StringType)
university_University_averageLength: Property = Property(name="averageLength", type=FloatType)
university_University_numberOfStudents: Property = Property(name="numberOfStudents", type=IntegerType)
university_University.attributes={university_University_averageLength, university_University_name, university_University_numberOfStudents}

# university_Professor class attributes and methods
university_Professor_name: Property = Property(name="name", type=StringType)
university_Professor.attributes={university_Professor_name}

# university_Certificate class attributes and methods
university_Certificate_note: Property = Property(name="note", type=IntegerType)
university_Certificate.attributes={university_Certificate_note}

# university_Student class attributes and methods
university_Student_semester: Property = Property(name="semester", type=IntegerType)
university_Student_MNR: Property = Property(name="MNR", type=StringType)
university_Student.attributes={university_Student_semester, university_Student_MNR}

# Relationships
courses2: BinaryAssociation = BinaryAssociation(
    name="courses2",
    ends={
        Property(name="Course", type=university_Professor, multiplicity=Multiplicity(1, 1)),
        Property(name="professor", type=university_Course, multiplicity=Multiplicity(0, 9999))
    }
)
professors3: BinaryAssociation = BinaryAssociation(
    name="professors3",
    ends={
        Property(name="university_Professor", type=university_University, multiplicity=Multiplicity(1, 1)),
        Property(name="university_University", type=university_Professor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
courses4: BinaryAssociation = BinaryAssociation(
    name="courses4",
    ends={
        Property(name="university_Course", type=university_University, multiplicity=Multiplicity(1, 1)),
        Property(name="university_University5", type=university_Course, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
professor0: BinaryAssociation = BinaryAssociation(
    name="professor0",
    ends={
        Property(name="Professor", type=university_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="courses", type=university_Professor, multiplicity=Multiplicity(0, 1))
    }
)
courseCertificates1: BinaryAssociation = BinaryAssociation(
    name="courseCertificates1",
    ends={
        Property(name="Certificate", type=university_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="course", type=university_Certificate, multiplicity=Multiplicity(0, 9999))
    }
)
student12: BinaryAssociation = BinaryAssociation(
    name="student12",
    ends={
        Property(name="Student", type=university_Certificate, multiplicity=Multiplicity(1, 1)),
        Property(name="studentCertificates", type=university_Student, multiplicity=Multiplicity(0, 1))
    }
)
course13: BinaryAssociation = BinaryAssociation(
    name="course13",
    ends={
        Property(name="Course14", type=university_Certificate, multiplicity=Multiplicity(1, 1)),
        Property(name="courseCertificates", type=university_Course, multiplicity=Multiplicity(0, 1))
    }
)
students6: BinaryAssociation = BinaryAssociation(
    name="students6",
    ends={
        Property(name="university_Student", type=university_University, multiplicity=Multiplicity(1, 1)),
        Property(name="university_University7", type=university_Student, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
certificates8: BinaryAssociation = BinaryAssociation(
    name="certificates8",
    ends={
        Property(name="university_Certificate", type=university_University, multiplicity=Multiplicity(1, 1)),
        Property(name="university_University9", type=university_Certificate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
studentCertificates10: BinaryAssociation = BinaryAssociation(
    name="studentCertificates10",
    ends={
        Property(name="Certificate11", type=university_Student, multiplicity=Multiplicity(1, 1)),
        Property(name="student", type=university_Certificate, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="university",
    types={university_Course, university_University, university_Professor, university_Certificate, university_Student},
    associations={courses2, professors3, courses4, professor0, courseCertificates1, student12, course13, students6, certificates8, studentCertificates10},
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