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
ADMIN = Class(name="ADMIN")
EMPLOYEE = Class(name="EMPLOYEE")
STUDENT = Class(name="STUDENT")
VALIDATE = Class(name="VALIDATE")

# ADMIN class attributes and methods
ADMIN_NAME: Property = Property(name="NAME", type=StringType)
ADMIN_PASSWORD: Property = Property(name="PASSWORD", type=StringType)
ADMIN.attributes={ADMIN_NAME, ADMIN_PASSWORD}

# EMPLOYEE class attributes and methods
EMPLOYEE_NAME: Property = Property(name="NAME", type=StringType)
EMPLOYEE_EMP_ID: Property = Property(name="EMP_ID", type=IntegerType)
EMPLOYEE_QULIFICATION: Property = Property(name="QULIFICATION", type=StringType)
EMPLOYEE_EMAIL_ID: Property = Property(name="EMAIL_ID", type=StringType)
EMPLOYEE_CONTACT_NO: Property = Property(name="CONTACT_NO", type=IntegerType)
EMPLOYEE.attributes={EMPLOYEE_QULIFICATION, EMPLOYEE_EMAIL_ID, EMPLOYEE_CONTACT_NO, EMPLOYEE_NAME, EMPLOYEE_EMP_ID}

# STUDENT class attributes and methods
STUDENT_NAME: Property = Property(name="NAME", type=StringType)
STUDENT_STUD_ID: Property = Property(name="STUD_ID", type=IntegerType)
STUDENT_COURSE: Property = Property(name="COURSE", type=StringType)
STUDENT_QUALIFICATION: Property = Property(name="QUALIFICATION", type=StringType)
STUDENT_EMAIL_ID: Property = Property(name="EMAIL_ID", type=StringType)
STUDENT_CONTACT_NO: Property = Property(name="CONTACT_NO", type=IntegerType)
STUDENT.attributes={STUDENT_CONTACT_NO, STUDENT_QUALIFICATION, STUDENT_STUD_ID, STUDENT_NAME, STUDENT_EMAIL_ID, STUDENT_COURSE}

# VALIDATE class attributes and methods
VALIDATE_USERNAME: Property = Property(name="USERNAME", type=StringType)
VALIDATE_PASSWORD: Property = Property(name="PASSWORD", type=StringType)
VALIDATE.attributes={VALIDATE_PASSWORD, VALIDATE_USERNAME}

# Relationships
EMPLOYEE_STUDENT: BinaryAssociation = BinaryAssociation(
    name="EMPLOYEE_STUDENT",
    ends={
        Property(name="sTUDENT0", type=STUDENT, multiplicity=Multiplicity(0, 9999)),
        Property(name="eMPLOYEE1", type=EMPLOYEE, multiplicity=Multiplicity(0, 9999))
    }
)
ADMIN_EMPLOYEE: BinaryAssociation = BinaryAssociation(
    name="ADMIN_EMPLOYEE",
    ends={
        Property(name="eMPLOYEE2", type=EMPLOYEE, multiplicity=Multiplicity(0, 9999)),
        Property(name="aDMIN3", type=ADMIN, multiplicity=Multiplicity(1, 1))
    }
)
ADMIN_STUDENT: BinaryAssociation = BinaryAssociation(
    name="ADMIN_STUDENT",
    ends={
        Property(name="sTUDENT4", type=STUDENT, multiplicity=Multiplicity(0, 9999)),
        Property(name="aDMIN5", type=ADMIN, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_CulacK5jEee6S77dw3LIvQ",
    types={ADMIN, EMPLOYEE, STUDENT, VALIDATE},
    associations={EMPLOYEE_STUDENT, ADMIN_EMPLOYEE, ADMIN_STUDENT},
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