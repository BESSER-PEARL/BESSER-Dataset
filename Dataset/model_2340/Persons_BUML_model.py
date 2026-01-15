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
Persons_Person = Class(name="Persons::Person", is_abstract=True)
Persons_Community = Class(name="Persons::Community")
Persons_Man = Class(name="Persons::Man")
Person = Class(name="Person")
Persons_TownHall = Class(name="Persons::TownHall")
Persons_Association = Class(name="Persons::Association")
Persons_Woman = Class(name="Persons::Woman")
NamedElement = Class(name="NamedElement")
Persons_District = Class(name="Persons::District")
Persons_Committee = Class(name="Persons::Committee")
Persons_Facility = Class(name="Persons::Facility", is_abstract=True)
Persons_NamedElement = Class(name="Persons::NamedElement", is_abstract=True)
Facility = Class(name="Facility")
Persons_OrdinaryFacility = Class(name="Persons::OrdinaryFacility")
Persons_SpecialFacility = Class(name="Persons::SpecialFacility")

# Persons_Person class attributes and methods
Persons_Person_fullName: Property = Property(name="fullName", type=StringType)
Persons_Person.attributes={Persons_Person_fullName}

# Persons_Community class attributes and methods

# Persons_Man class attributes and methods

# Person class attributes and methods

# Persons_TownHall class attributes and methods

# Persons_Association class attributes and methods

# Persons_Woman class attributes and methods

# NamedElement class attributes and methods

# Persons_District class attributes and methods

# Persons_Committee class attributes and methods

# Persons_Facility class attributes and methods

# Persons_NamedElement class attributes and methods
Persons_NamedElement_name: Property = Property(name="name", type=StringType)
Persons_NamedElement.attributes={Persons_NamedElement_name}

# Facility class attributes and methods

# Persons_OrdinaryFacility class attributes and methods

# Persons_SpecialFacility class attributes and methods

# Relationships
persons0: BinaryAssociation = BinaryAssociation(
    name="persons0",
    ends={
        Property(name="Persons_Person", type=Persons_Community, multiplicity=Multiplicity(1, 1)),
        Property(name="Persons_Community", type=Persons_Person, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
townHalls1: BinaryAssociation = BinaryAssociation(
    name="townHalls1",
    ends={
        Property(name="Persons_TownHall", type=Persons_Community, multiplicity=Multiplicity(1, 1)),
        Property(name="Persons_Community2", type=Persons_TownHall, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
associations3: BinaryAssociation = BinaryAssociation(
    name="associations3",
    ends={
        Property(name="Persons_Association", type=Persons_Community, multiplicity=Multiplicity(1, 1)),
        Property(name="Persons_Community4", type=Persons_Association, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
districts10: BinaryAssociation = BinaryAssociation(
    name="districts10",
    ends={
        Property(name="Persons_District", type=Persons_TownHall, multiplicity=Multiplicity(1, 1)),
        Property(name="Persons_TownHall11", type=Persons_District, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
workers5: BinaryAssociation = BinaryAssociation(
    name="workers5",
    ends={
        Property(name="Persons_Person7", type=Persons_TownHall, multiplicity=Multiplicity(1, 1)),
        Property(name="Persons_TownHall6", type=Persons_Person, multiplicity=Multiplicity(0, 9999))
    }
)
committee8: BinaryAssociation = BinaryAssociation(
    name="committee8",
    ends={
        Property(name="Persons_Committee", type=Persons_TownHall, multiplicity=Multiplicity(1, 1)),
        Property(name="Persons_TownHall9", type=Persons_Committee, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
facilities15: BinaryAssociation = BinaryAssociation(
    name="facilities15",
    ends={
        Property(name="Persons_Facility", type=Persons_District, multiplicity=Multiplicity(1, 1)),
        Property(name="Persons_District16", type=Persons_Facility, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
committee12: BinaryAssociation = BinaryAssociation(
    name="committee12",
    ends={
        Property(name="Persons_Committee14", type=Persons_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="Persons_Association13", type=Persons_Committee, multiplicity=Multiplicity(0, 1))
    }
)
members17: BinaryAssociation = BinaryAssociation(
    name="members17",
    ends={
        Property(name="Persons_Person19", type=Persons_Facility, multiplicity=Multiplicity(1, 1)),
        Property(name="Persons_Facility18", type=Persons_Person, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_Persons_Man_Person = Generalization(general=Person, specific=Persons_Man)
gen_Persons_Woman_Person = Generalization(general=Person, specific=Persons_Woman)
gen_Persons_TownHall_NamedElement = Generalization(general=NamedElement, specific=Persons_TownHall)
gen_Persons_Association_NamedElement = Generalization(general=NamedElement, specific=Persons_Association)
gen_Persons_District_NamedElement = Generalization(general=NamedElement, specific=Persons_District)
gen_Persons_Committee_NamedElement = Generalization(general=NamedElement, specific=Persons_Committee)
gen_Persons_SpecialFacility_Facility = Generalization(general=Facility, specific=Persons_SpecialFacility)
gen_Persons_OrdinaryFacility_Facility = Generalization(general=Facility, specific=Persons_OrdinaryFacility)
gen_Persons_Facility_NamedElement = Generalization(general=NamedElement, specific=Persons_Facility)

# Domain Model
domain_model = DomainModel(
    name="Persons",
    types={Persons_Person, Persons_Community, Persons_Man, Person, Persons_TownHall, Persons_Association, Persons_Woman, NamedElement, Persons_District, Persons_Committee, Persons_Facility, Persons_NamedElement, Facility, Persons_OrdinaryFacility, Persons_SpecialFacility},
    associations={persons0, townHalls1, associations3, districts10, workers5, committee8, facilities15, committee12, members17},
    generalizations={gen_Persons_Man_Person, gen_Persons_Woman_Person, gen_Persons_TownHall_NamedElement, gen_Persons_Association_NamedElement, gen_Persons_District_NamedElement, gen_Persons_Committee_NamedElement, gen_Persons_SpecialFacility_Facility, gen_Persons_OrdinaryFacility_Facility, gen_Persons_Facility_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)