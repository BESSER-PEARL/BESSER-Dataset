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
incomeLevel: Enumeration = Enumeration(
    name="incomeLevel",
    literals={
            EnumerationLiteral(name="UnderGrad"),
			EnumerationLiteral(name="PreDoc"),
			EnumerationLiteral(name="PostDoc"),
			EnumerationLiteral(name="Professor")
    }
)

Grade: Enumeration = Enumeration(
    name="Grade",
    literals={
            EnumerationLiteral(name="None"),
			EnumerationLiteral(name="BSC"),
			EnumerationLiteral(name="MSC"),
			EnumerationLiteral(name="PHD"),
			EnumerationLiteral(name="Professor")
    }
)

EEnum0: Enumeration = Enumeration(
    name="EEnum0",
    literals={
            
    }
)

# Classes
test_Student = Class(name="test::Student")
Person = Class(name="Person")
test_Employee = Class(name="test::Employee")
test_Person = Class(name="test::Person")
test_University = Class(name="test::University")

# test_Student class attributes and methods
test_Student_regNo: Property = Property(name="regNo", type=StringType)
test_Student.attributes={test_Student_regNo}

# Person class attributes and methods

# test_Employee class attributes and methods
test_Employee_incomeLevel: Property = Property(name="incomeLevel", type=StringType)
test_Employee.attributes={test_Employee_incomeLevel}

# test_Person class attributes and methods
test_Person_lastname: Property = Property(name="lastname", type=StringType)
test_Person_firstame: Property = Property(name="firstame", type=StringType)
test_Person_Grade: Property = Property(name="Grade", type=StringType)
test_Person.attributes={test_Person_firstame, test_Person_lastname, test_Person_Grade}

# test_University class attributes and methods
test_University_name: Property = Property(name="name", type=StringType)
test_University.attributes={test_University_name}

# Relationships
supervisor1: BinaryAssociation = BinaryAssociation(
    name="supervisor1",
    ends={
        Property(name="test_Person", type=test_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="test_Person0", type=test_Person, multiplicity=Multiplicity(0, 1))
    }
)
supervised3: BinaryAssociation = BinaryAssociation(
    name="supervised3",
    ends={
        Property(name="test_Person4", type=test_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="test_Person2", type=test_Person, multiplicity=Multiplicity(0, 9999))
    }
)
persons5: BinaryAssociation = BinaryAssociation(
    name="persons5",
    ends={
        Property(name="test_Person6", type=test_University, multiplicity=Multiplicity(1, 1)),
        Property(name="test_University", type=test_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_test_Student_Person = Generalization(general=Person, specific=test_Student)
gen_test_Employee_Person = Generalization(general=Person, specific=test_Employee)

# Domain Model
domain_model = DomainModel(
    name="test",
    types={test_Student, Person, test_Employee, test_Person, test_University, incomeLevel, Grade, EEnum0},
    associations={supervisor1, supervised3, persons5},
    generalizations={gen_test_Student_Person, gen_test_Employee_Person},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)