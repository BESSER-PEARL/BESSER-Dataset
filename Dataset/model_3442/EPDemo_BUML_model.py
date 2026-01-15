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
epdemo_School = Class(name="epdemo::School")
epdemo_Clazz = Class(name="epdemo::Clazz")
epdemo_Student = Class(name="epdemo::Student")
epdemo_Teacher = Class(name="epdemo::Teacher")

# epdemo_School class attributes and methods
epdemo_School_Id: Property = Property(name="Id", type=StringType)
epdemo_School_Name: Property = Property(name="Name", type=StringType)
epdemo_School.attributes={epdemo_School_Name, epdemo_School_Id}

# epdemo_Clazz class attributes and methods
epdemo_Clazz_Id: Property = Property(name="Id", type=StringType)
epdemo_Clazz_Name: Property = Property(name="Name", type=StringType)
epdemo_Clazz.attributes={epdemo_Clazz_Id, epdemo_Clazz_Name}

# epdemo_Student class attributes and methods
epdemo_Student_Id: Property = Property(name="Id", type=StringType)
epdemo_Student_Name: Property = Property(name="Name", type=StringType)
epdemo_Student.attributes={epdemo_Student_Name, epdemo_Student_Id}

# epdemo_Teacher class attributes and methods
epdemo_Teacher_Id: Property = Property(name="Id", type=StringType)
epdemo_Teacher_Name: Property = Property(name="Name", type=StringType)
epdemo_Teacher.attributes={epdemo_Teacher_Name, epdemo_Teacher_Id}

# Relationships
teachers5: BinaryAssociation = BinaryAssociation(
    name="teachers5",
    ends={
        Property(name="epdemo_Teacher7", type=epdemo_Clazz, multiplicity=Multiplicity(1, 1)),
        Property(name="epdemo_Clazz6", type=epdemo_Teacher, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
students8: BinaryAssociation = BinaryAssociation(
    name="students8",
    ends={
        Property(name="epdemo_Student10", type=epdemo_Clazz, multiplicity=Multiplicity(1, 1)),
        Property(name="epdemo_Clazz9", type=epdemo_Student, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Clazzes0: BinaryAssociation = BinaryAssociation(
    name="Clazzes0",
    ends={
        Property(name="epdemo_Clazz", type=epdemo_School, multiplicity=Multiplicity(1, 1)),
        Property(name="epdemo_School", type=epdemo_Clazz, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
students1: BinaryAssociation = BinaryAssociation(
    name="students1",
    ends={
        Property(name="epdemo_Student", type=epdemo_School, multiplicity=Multiplicity(1, 1)),
        Property(name="epdemo_School2", type=epdemo_Student, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
teachers3: BinaryAssociation = BinaryAssociation(
    name="teachers3",
    ends={
        Property(name="epdemo_Teacher", type=epdemo_School, multiplicity=Multiplicity(1, 1)),
        Property(name="epdemo_School4", type=epdemo_Teacher, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="epdemo",
    types={epdemo_School, epdemo_Clazz, epdemo_Student, epdemo_Teacher},
    associations={teachers5, students8, Clazzes0, students1, teachers3},
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