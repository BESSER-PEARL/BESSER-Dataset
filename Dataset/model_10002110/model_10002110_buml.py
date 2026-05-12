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
teachers = Class(name="teachers")
subjects = Class(name="subjects")
classrooms = Class(name="classrooms")
conflictCheck = Class(name="conflictCheck")
constraints = Class(name="constraints")
leftOuts = Class(name="leftOuts")

# teachers class attributes and methods
teachers_name: Property = Property(name="name", type=StringType)
teachers_subject: Property = Property(name="subject", type=StringType)
teachers_classroom: Property = Property(name="classroom", type=IntegerType)
teachers_section: Property = Property(name="section", type=StringType)
teachers.attributes={teachers_subject, teachers_section, teachers_classroom, teachers_name}

# subjects class attributes and methods
subjects_classroom: Property = Property(name="classroom", type=IntegerType)
subjects_teacher: Property = Property(name="teacher", type=StringType)
subjects_Section: Property = Property(name="Section", type=StringType)
subjects_name: Property = Property(name="name", type=StringType)
subjects.attributes={subjects_teacher, subjects_classroom, subjects_Section, subjects_name}

# classrooms class attributes and methods
classrooms_number: Property = Property(name="number", type=IntegerType)
classrooms_teacher: Property = Property(name="teacher", type=StringType)
classrooms_subject: Property = Property(name="subject", type=StringType)
classrooms.attributes={classrooms_number, classrooms_subject, classrooms_teacher}

# conflictCheck class attributes and methods
conflictCheck_conflict: Property = Property(name="conflict", type=BooleanType)
conflictCheck_subjects: Property = Property(name="subjects", type=StringType)
conflictCheck.attributes={conflictCheck_conflict, conflictCheck_subjects}

# constraints class attributes and methods
constraints_singletons: Property = Property(name="singletons", type=subjects)
constraints_doubletons: Property = Property(name="doubletons", type=subjects)
constraints.attributes={constraints_doubletons, constraints_singletons}

# leftOuts class attributes and methods
leftOuts_subject: Property = Property(name="subject", type=subjects)
leftOuts_classroom: Property = Property(name="classroom", type=classrooms)
leftOuts_teachers: Property = Property(name="teachers", type=teachers)
leftOuts_students: Property = Property(name="students", type=StringType)
leftOuts.attributes={leftOuts_classroom, leftOuts_students, leftOuts_subject, leftOuts_teachers}

# Domain Model
domain_model = DomainModel(
    name="_ovAIgODiEee1VcqWCkiVQg",
    types={teachers, subjects, classrooms, conflictCheck, constraints, leftOuts},
    associations={},
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