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
Enumeration_: Enumeration = Enumeration(
    name="Enumeration",
    literals={
            
    }
)

# Classes
Person = Class(name="Person")
student = Class(name="student")
Admin = Class(name="Admin")
Interface_Interface = Class(name="Interface_Interface")
Class_ = Class(name="Class")
course = Class(name="course")
Department = Class(name="Department")
staff_member = Class(name="staff_member")
controller = Class(name="controller")
barcode = Class(name="barcode")

# Person class attributes and methods
Person_name: Property = Property(name="name", type=StringType)
Person_id: Property = Property(name="id", type=IntegerType)
Person_username: Property = Property(name="username", type=StringType)
Person_email: Property = Property(name="email", type=StringType)
Person_date_of_birth: Property = Property(name="date_of_birth", type=StringType)
Person_address: Property = Property(name="address", type=StringType)
Person_password: Property = Property(name="password", type=IntegerType)
Person_department: Property = Property(name="department", type=StringType)
Person.attributes={Person_date_of_birth, Person_department, Person_address, Person_name, Person_id, Person_email, Person_password, Person_username}

# student class attributes and methods
student_major_dept: Property = Property(name="major_dept", type=StringType)
student_minor_dept: Property = Property(name="minor_dept", type=StringType)
student.attributes={student_major_dept, student_minor_dept}

# Admin class attributes and methods

# Interface_Interface class attributes and methods

# Class class attributes and methods

# course class attributes and methods
course_course_name: Property = Property(name="course_name", type=StringType)
course_course_id: Property = Property(name="course_id", type=IntegerType)
course_course_preq: Property = Property(name="course_preq", type=StringType)
course_credit_hours: Property = Property(name="credit_hours", type=IntegerType)
course.attributes={course_credit_hours, course_course_preq, course_course_name, course_course_id}

# Department class attributes and methods
Department_dept_name: Property = Property(name="dept_name", type=StringType)
Department_dept_id: Property = Property(name="dept_id", type=IntegerType)
Department.attributes={Department_dept_name, Department_dept_id}

# staff_member class attributes and methods

# controller class attributes and methods

# barcode class attributes and methods

# Relationships
Department_student: BinaryAssociation = BinaryAssociation(
    name="Department_student",
    ends={
        Property(name="student0", type=student, multiplicity=Multiplicity(1, 9999)),
        Property(name="department1", type=Department, multiplicity=Multiplicity(1, 9999))
    }
)
student_course: BinaryAssociation = BinaryAssociation(
    name="student_course",
    ends={
        Property(name="course2", type=course, multiplicity=Multiplicity(1, 1)),
        Property(name="student3", type=student, multiplicity=Multiplicity(1, 9999))
    }
)
course_Admin: BinaryAssociation = BinaryAssociation(
    name="course_Admin",
    ends={
        Property(name="admin4", type=Admin, multiplicity=Multiplicity(1, 9999)),
        Property(name="course5", type=course, multiplicity=Multiplicity(1, 9999))
    }
)
student_barcode: BinaryAssociation = BinaryAssociation(
    name="student_barcode",
    ends={
        Property(name="barcode6", type=barcode, multiplicity=Multiplicity(1, 9999)),
        Property(name="student7", type=student, multiplicity=Multiplicity(1, 9999))
    }
)
course_Person: BinaryAssociation = BinaryAssociation(
    name="course_Person",
    ends={
        Property(name="person8", type=Person, multiplicity=Multiplicity(1, 9999)),
        Property(name="course9", type=course, multiplicity=Multiplicity(1, 9999))
    }
)
controller_staff_member: BinaryAssociation = BinaryAssociation(
    name="controller_staff_member",
    ends={
        Property(name="staff_member10", type=staff_member, multiplicity=Multiplicity(1, 9999)),
        Property(name="controller11", type=controller, multiplicity=Multiplicity(1, 9999))
    }
)
Admin_controller: BinaryAssociation = BinaryAssociation(
    name="Admin_controller",
    ends={
        Property(name="controller12", type=controller, multiplicity=Multiplicity(1, 9999)),
        Property(name="admin13", type=Admin, multiplicity=Multiplicity(1, 9999))
    }
)
Admin_staff_member: BinaryAssociation = BinaryAssociation(
    name="Admin_staff_member",
    ends={
        Property(name="staff_member14", type=staff_member, multiplicity=Multiplicity(1, 9999)),
        Property(name="admin15", type=Admin, multiplicity=Multiplicity(1, 9999))
    }
)
Department_course: BinaryAssociation = BinaryAssociation(
    name="Department_course",
    ends={
        Property(name="course16", type=course, multiplicity=Multiplicity(1, 9999)),
        Property(name="department17", type=Department, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_2RViYNILEeeLcIicqHdTUQ",
    types={Person, student, Admin, Interface_Interface, Class_, course, Department, staff_member, controller, barcode, Enumeration_},
    associations={Department_student, student_course, course_Admin, student_barcode, course_Person, controller_staff_member, Admin_controller, Admin_staff_member, Department_course},
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