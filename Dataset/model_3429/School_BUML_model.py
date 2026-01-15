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
school_SchoolModel = Class(name="school::SchoolModel")
school_School = Class(name="school::School")
Named = Class(name="Named")
school_Student = Class(name="school::Student")
Person = Class(name="Person")
school_Teacher = Class(name="school::Teacher")
school_Person = Class(name="school::Person", is_abstract=True)
school_Named = Class(name="school::Named", is_abstract=True)

# school_SchoolModel class attributes and methods

# school_School class attributes and methods

# Named class attributes and methods

# school_Student class attributes and methods
school_Student_registrationNum: Property = Property(name="registrationNum", type=IntegerType)
school_Student.attributes={school_Student_registrationNum}

# Person class attributes and methods

# school_Teacher class attributes and methods

# school_Person class attributes and methods

# school_Named class attributes and methods
school_Named_name: Property = Property(name="name", type=StringType)
school_Named.attributes={school_Named_name}

# Relationships
schools0: BinaryAssociation = BinaryAssociation(
    name="schools0",
    ends={
        Property(name="school_School", type=school_SchoolModel, multiplicity=Multiplicity(1, 1)),
        Property(name="school_SchoolModel", type=school_School, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
teachers3: BinaryAssociation = BinaryAssociation(
    name="teachers3",
    ends={
        Property(name="school_Teacher", type=school_Student, multiplicity=Multiplicity(1, 1)),
        Property(name="school_Student", type=school_Teacher, multiplicity=Multiplicity(0, 9999))
    }
)
persons1: BinaryAssociation = BinaryAssociation(
    name="persons1",
    ends={
        Property(name="school_Person", type=school_School, multiplicity=Multiplicity(1, 1)),
        Property(name="school_School2", type=school_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_school_School_Named = Generalization(general=Named, specific=school_School)
gen_school_Student_Person = Generalization(general=Person, specific=school_Student)
gen_school_Teacher_Person = Generalization(general=Person, specific=school_Teacher)
gen_school_Person_Named = Generalization(general=Named, specific=school_Person)

# Domain Model
domain_model = DomainModel(
    name="school",
    types={school_SchoolModel, school_School, Named, school_Student, Person, school_Teacher, school_Person, school_Named},
    associations={schools0, teachers3, persons1},
    generalizations={gen_school_School_Named, gen_school_Student_Person, gen_school_Teacher_Person, gen_school_Person_Named},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)