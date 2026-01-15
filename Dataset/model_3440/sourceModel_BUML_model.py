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
SourceModel_Container = Class(name="SourceModel::Container")
SourceModel_Person = Class(name="SourceModel::Person")
SourceModel_Student = Class(name="SourceModel::Student")
Person = Class(name="Person")
SourceModel_Professor = Class(name="SourceModel::Professor")
SourceModel_MasterStudent = Class(name="SourceModel::MasterStudent")
Student = Class(name="Student")
SourceModel_BachelorStudent = Class(name="SourceModel::BachelorStudent")

# SourceModel_Container class attributes and methods

# SourceModel_Person class attributes and methods
SourceModel_Person_age: Property = Property(name="age", type=StringType)
SourceModel_Person.attributes={SourceModel_Person_age}

# SourceModel_Student class attributes and methods

# Person class attributes and methods

# SourceModel_Professor class attributes and methods

# SourceModel_MasterStudent class attributes and methods

# Student class attributes and methods

# SourceModel_BachelorStudent class attributes and methods

# Relationships
persons0: BinaryAssociation = BinaryAssociation(
    name="persons0",
    ends={
        Property(name="SourceModel_Person", type=SourceModel_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="SourceModel_Container", type=SourceModel_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
likes2: BinaryAssociation = BinaryAssociation(
    name="likes2",
    ends={
        Property(name="SourceModel_Person3", type=SourceModel_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="SourceModel_Person1", type=SourceModel_Person, multiplicity=Multiplicity(1, 1))
    }
)
teacher4: BinaryAssociation = BinaryAssociation(
    name="teacher4",
    ends={
        Property(name="Professor", type=SourceModel_Student, multiplicity=Multiplicity(1, 1)),
        Property(name="learner", type=SourceModel_Professor, multiplicity=Multiplicity(3, 5))
    }
)
learner5: BinaryAssociation = BinaryAssociation(
    name="learner5",
    ends={
        Property(name="Student", type=SourceModel_Professor, multiplicity=Multiplicity(1, 1)),
        Property(name="teacher", type=SourceModel_Student, multiplicity=Multiplicity(5, 9999))
    }
)

# Generalizations
gen_SourceModel_Student_Person = Generalization(general=Person, specific=SourceModel_Student)
gen_SourceModel_MasterStudent_Student = Generalization(general=Student, specific=SourceModel_MasterStudent)
gen_SourceModel_BachelorStudent_Student = Generalization(general=Student, specific=SourceModel_BachelorStudent)
gen_SourceModel_Professor_Person = Generalization(general=Person, specific=SourceModel_Professor)

# Domain Model
domain_model = DomainModel(
    name="SourceModel",
    types={SourceModel_Container, SourceModel_Person, SourceModel_Student, Person, SourceModel_Professor, SourceModel_MasterStudent, Student, SourceModel_BachelorStudent},
    associations={persons0, likes2, teacher4, learner5},
    generalizations={gen_SourceModel_Student_Person, gen_SourceModel_MasterStudent_Student, gen_SourceModel_BachelorStudent_Student, gen_SourceModel_Professor_Person},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)