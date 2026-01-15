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
Friends_Person = Class(name="Friends::Person", is_abstract=True)
Friends_Classroom = Class(name="Friends::Classroom")
Friends_Man = Class(name="Friends::Man")
Person = Class(name="Person")
Friends_Woman = Class(name="Friends::Woman")

# Friends_Person class attributes and methods
Friends_Person_name: Property = Property(name="name", type=StringType)
Friends_Person.attributes={Friends_Person_name}

# Friends_Classroom class attributes and methods
Friends_Classroom_id: Property = Property(name="id", type=IntegerType)
Friends_Classroom.attributes={Friends_Classroom_id}

# Friends_Man class attributes and methods

# Person class attributes and methods

# Friends_Woman class attributes and methods

# Relationships
friend_with1: BinaryAssociation = BinaryAssociation(
    name="friend_with1",
    ends={
        Property(name="Friends_Person", type=Friends_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="Friends_Person0", type=Friends_Person, multiplicity=Multiplicity(0, 9999))
    }
)
teacher_of2: BinaryAssociation = BinaryAssociation(
    name="teacher_of2",
    ends={
        Property(name="Friends_Classroom", type=Friends_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="Friends_Person3", type=Friends_Classroom, multiplicity=Multiplicity(0, 1))
    }
)
person4: BinaryAssociation = BinaryAssociation(
    name="person4",
    ends={
        Property(name="Friends_Person6", type=Friends_Classroom, multiplicity=Multiplicity(1, 1)),
        Property(name="Friends_Classroom5", type=Friends_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_Friends_Man_Person = Generalization(general=Person, specific=Friends_Man)
gen_Friends_Woman_Person = Generalization(general=Person, specific=Friends_Woman)

# Domain Model
domain_model = DomainModel(
    name="Friends",
    types={Friends_Person, Friends_Classroom, Friends_Man, Person, Friends_Woman},
    associations={friend_with1, teacher_of2, person4},
    generalizations={gen_Friends_Man_Person, gen_Friends_Woman_Person},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)