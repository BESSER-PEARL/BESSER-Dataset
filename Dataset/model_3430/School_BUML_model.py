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
school_SchoolStatistics = Class(name="school::SchoolStatistics")
school_Person = Class(name="school::Person", is_abstract=True)
school_Named = Class(name="school::Named", is_abstract=True)
school_Student = Class(name="school::Student")
Person = Class(name="Person")
school_Teacher = Class(name="school::Teacher")
school_SchoolModel = Class(name="school::SchoolModel")
school_School = Class(name="school::School")
Named = Class(name="Named")

# school_SchoolStatistics class attributes and methods
school_SchoolStatistics_studentsNumber: Property = Property(name="studentsNumber", type=IntegerType)
school_SchoolStatistics_teachersNumber: Property = Property(name="teachersNumber", type=IntegerType)
school_SchoolStatistics_studentsWithNoTeacher: Property = Property(name="studentsWithNoTeacher", type=StringType)
school_SchoolStatistics.attributes={school_SchoolStatistics_studentsWithNoTeacher, school_SchoolStatistics_teachersNumber, school_SchoolStatistics_studentsNumber}

# school_Person class attributes and methods

# school_Named class attributes and methods
school_Named_name: Property = Property(name="name", type=StringType)
school_Named.attributes={school_Named_name}

# school_Student class attributes and methods
school_Student_registrationNum: Property = Property(name="registrationNum", type=IntegerType)
school_Student.attributes={school_Student_registrationNum}

# Person class attributes and methods

# school_Teacher class attributes and methods

# school_SchoolModel class attributes and methods

# school_School class attributes and methods
school_School_m_getStudents: Method = Method(name="getStudents", parameters={})
school_School_m_getTeachers: Method = Method(name="getTeachers", parameters={})
school_School.methods={school_School_m_getTeachers, school_School_m_getStudents}

# Named class attributes and methods

# Relationships
statistics1: BinaryAssociation = BinaryAssociation(
    name="statistics1",
    ends={
        Property(name="school_SchoolStatistics", type=school_School, multiplicity=Multiplicity(1, 1)),
        Property(name="school_School2", type=school_SchoolStatistics, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
persons3: BinaryAssociation = BinaryAssociation(
    name="persons3",
    ends={
        Property(name="school_Person", type=school_School, multiplicity=Multiplicity(1, 1)),
        Property(name="school_School4", type=school_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
schools0: BinaryAssociation = BinaryAssociation(
    name="schools0",
    ends={
        Property(name="school_School", type=school_SchoolModel, multiplicity=Multiplicity(1, 1)),
        Property(name="school_SchoolModel", type=school_School, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
teachers5: BinaryAssociation = BinaryAssociation(
    name="teachers5",
    ends={
        Property(name="school_Teacher", type=school_Student, multiplicity=Multiplicity(1, 1)),
        Property(name="school_Student", type=school_Teacher, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_school_Person_Named = Generalization(general=Named, specific=school_Person)
gen_school_Student_Person = Generalization(general=Person, specific=school_Student)
gen_school_School_Named = Generalization(general=Named, specific=school_School)
gen_school_Teacher_Person = Generalization(general=Person, specific=school_Teacher)

# Domain Model
domain_model = DomainModel(
    name="school",
    types={school_SchoolStatistics, school_Person, school_Named, school_Student, Person, school_Teacher, school_SchoolModel, school_School, Named},
    associations={statistics1, persons3, schools0, teachers5},
    generalizations={gen_school_Person_Named, gen_school_Student_Person, gen_school_School_Named, gen_school_Teacher_Person},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)