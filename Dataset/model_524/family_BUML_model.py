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
Month: Enumeration = Enumeration(
    name="Month",
    literals={
            EnumerationLiteral(name="January"),
			EnumerationLiteral(name="February"),
			EnumerationLiteral(name="March"),
			EnumerationLiteral(name="April"),
			EnumerationLiteral(name="May"),
			EnumerationLiteral(name="June"),
			EnumerationLiteral(name="July"),
			EnumerationLiteral(name="August"),
			EnumerationLiteral(name="September"),
			EnumerationLiteral(name="October"),
			EnumerationLiteral(name="November"),
			EnumerationLiteral(name="December")
    }
)

# Classes
family_Family = Class(name="family::Family")
EModelElement = Class(name="EModelElement")
family_Man = Class(name="family::Man")
family_Woman = Class(name="family::Woman")
family_Person = Class(name="family::Person", is_abstract=True)
Person = Class(name="Person")

# family_Family class attributes and methods
family_Family_name: Property = Property(name="name", type=StringType)
family_Family.attributes={family_Family_name}

# EModelElement class attributes and methods

# family_Man class attributes and methods

# family_Woman class attributes and methods

# family_Person class attributes and methods
family_Person_firstName: Property = Property(name="firstName", type=StringType)
family_Person_lastName: Property = Property(name="lastName", type=StringType)
family_Person_birthDay: Property = Property(name="birthDay", type=IntegerType)
family_Person_birthMonth: Property = Property(name="birthMonth", type=StringType)
family_Person_birthYear: Property = Property(name="birthYear", type=IntegerType)
family_Person_birthCity: Property = Property(name="birthCity", type=StringType)
family_Person.attributes={family_Person_birthMonth, family_Person_birthDay, family_Person_lastName, family_Person_birthYear, family_Person_birthCity, family_Person_firstName}

# Person class attributes and methods

# Relationships
men0: BinaryAssociation = BinaryAssociation(
    name="men0",
    ends={
        Property(name="family_Man", type=family_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="family_Family", type=family_Man, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
women1: BinaryAssociation = BinaryAssociation(
    name="women1",
    ends={
        Property(name="family_Woman", type=family_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="family_Family2", type=family_Woman, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
families4: BinaryAssociation = BinaryAssociation(
    name="families4",
    ends={
        Property(name="family_Family5", type=family_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="family_Family3", type=family_Family, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
father6: BinaryAssociation = BinaryAssociation(
    name="father6",
    ends={
        Property(name="family_Man7", type=family_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="family_Person", type=family_Man, multiplicity=Multiplicity(0, 1))
    }
)
mother8: BinaryAssociation = BinaryAssociation(
    name="mother8",
    ends={
        Property(name="family_Woman10", type=family_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="family_Person9", type=family_Woman, multiplicity=Multiplicity(0, 1))
    }
)
children12: BinaryAssociation = BinaryAssociation(
    name="children12",
    ends={
        Property(name="family_Person11", type=family_Person, multiplicity=Multiplicity(0, 9999)),
        Property(name="family_Person13", type=family_Person, multiplicity=Multiplicity(1, 1))
    }
)
wife14: BinaryAssociation = BinaryAssociation(
    name="wife14",
    ends={
        Property(name="family_Woman16", type=family_Man, multiplicity=Multiplicity(1, 1)),
        Property(name="family_Man15", type=family_Woman, multiplicity=Multiplicity(0, 1))
    }
)
husband17: BinaryAssociation = BinaryAssociation(
    name="husband17",
    ends={
        Property(name="family_Man19", type=family_Woman, multiplicity=Multiplicity(1, 1)),
        Property(name="family_Woman18", type=family_Man, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_family_Family_EModelElement = Generalization(general=EModelElement, specific=family_Family)
gen_family_Person_EModelElement = Generalization(general=EModelElement, specific=family_Person)
gen_family_Man_Person = Generalization(general=Person, specific=family_Man)
gen_family_Woman_Person = Generalization(general=Person, specific=family_Woman)

# Domain Model
domain_model = DomainModel(
    name="family",
    types={family_Family, EModelElement, family_Man, family_Woman, family_Person, Person, Month},
    associations={men0, women1, families4, father6, mother8, children12, wife14, husband17},
    generalizations={gen_family_Family_EModelElement, gen_family_Person_EModelElement, gen_family_Man_Person, gen_family_Woman_Person},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)