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
Sexe: Enumeration = Enumeration(
    name="Sexe",
    literals={
            EnumerationLiteral(name="FEMALE"),
			EnumerationLiteral(name="MALE")
    }
)

# Classes
family_WealthyFamily = Class(name="family::WealthyFamily")
Family = Class(name="Family")
family_Family = Class(name="family::Family")
family_Person = Class(name="family::Person")
family_Address = Class(name="family::Address")
family_Car = Class(name="family::Car")

# family_WealthyFamily class attributes and methods
family_WealthyFamily_forbesRanking: Property = Property(name="forbesRanking", type=IntegerType)
family_WealthyFamily.attributes={family_WealthyFamily_forbesRanking}

# Family class attributes and methods

# family_Family class attributes and methods
family_Family_surname: Property = Property(name="surname", type=StringType)
family_Family_numberOfPets: Property = Property(name="numberOfPets", type=IntegerType)
family_Family_hasASwimmingPool: Property = Property(name="hasASwimmingPool", type=BooleanType)
family_Family_favoriteHolidayDestinations: Property = Property(name="favoriteHolidayDestinations", type=StringType)
family_Family.attributes={family_Family_favoriteHolidayDestinations, family_Family_numberOfPets, family_Family_surname, family_Family_hasASwimmingPool}

# family_Person class attributes and methods
family_Person_firstName: Property = Property(name="firstName", type=StringType)
family_Person_sexe: Property = Property(name="sexe", type=StringType)
family_Person.attributes={family_Person_sexe, family_Person_firstName}

# family_Address class attributes and methods
family_Address_street: Property = Property(name="street", type=StringType)
family_Address.attributes={family_Address_street}

# family_Car class attributes and methods
family_Car_numberOfSeats: Property = Property(name="numberOfSeats", type=StringType)
family_Car.attributes={family_Car_numberOfSeats}

# Relationships
members0: BinaryAssociation = BinaryAssociation(
    name="members0",
    ends={
        Property(name="family_Person", type=family_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="family_Family", type=family_Person, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
address1: BinaryAssociation = BinaryAssociation(
    name="address1",
    ends={
        Property(name="family_Address", type=family_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="family_Family2", type=family_Address, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedCars3: BinaryAssociation = BinaryAssociation(
    name="ownedCars3",
    ends={
        Property(name="family_Car", type=family_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="family_Person4", type=family_Car, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_family_WealthyFamily_Family = Generalization(general=Family, specific=family_WealthyFamily)

# Domain Model
domain_model = DomainModel(
    name="family",
    types={family_WealthyFamily, Family, family_Family, family_Person, family_Address, family_Car, Sexe},
    associations={members0, address1, ownedCars3},
    generalizations={gen_family_WealthyFamily_Family},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)