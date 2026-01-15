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
education_Person = Class(name="education::Person")
education_Student = Class(name="education::Student")
Person = Class(name="Person")
education_Teacher = Class(name="education::Teacher")
education_Course = Class(name="education::Course")

# education_Person class attributes and methods
education_Person_firstname: Property = Property(name="firstname", type=StringType)
education_Person_lastname: Property = Property(name="lastname", type=StringType)
education_Person.attributes={education_Person_firstname, education_Person_lastname}

# education_Student class attributes and methods

# Person class attributes and methods

# education_Teacher class attributes and methods

# education_Course class attributes and methods
education_Course_name: Property = Property(name="name", type=StringType)
education_Course_m_start: Method = Method(name="start", parameters={Parameter(name='startdate')})
education_Course_m_finish: Method = Method(name="finish", parameters={Parameter(name='finishdate')})
education_Course.attributes={education_Course_name}
education_Course.methods={education_Course_m_finish, education_Course_m_start}

# Relationships
teacher1: BinaryAssociation = BinaryAssociation(
    name="teacher1",
    ends={
        Property(name="education_Teacher", type=education_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="education_Course2", type=education_Teacher, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
student0: BinaryAssociation = BinaryAssociation(
    name="student0",
    ends={
        Property(name="education_Student", type=education_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="education_Course", type=education_Student, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_education_Student_Person = Generalization(general=Person, specific=education_Student)
gen_education_Teacher_Person = Generalization(general=Person, specific=education_Teacher)

# Domain Model
domain_model = DomainModel(
    name="education",
    types={education_Person, education_Student, Person, education_Teacher, education_Course},
    associations={teacher1, student0},
    generalizations={gen_education_Student_Person, gen_education_Teacher_Person},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)