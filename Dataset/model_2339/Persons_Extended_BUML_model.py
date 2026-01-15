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
persons_TownHall = Class(name="persons::TownHall")
persons_Association = Class(name="persons::Association")
persons_Man = Class(name="persons::Man")
Person = Class(name="Person")
persons_Woman = Class(name="persons::Woman")
NamedElement = Class(name="NamedElement")
persons_Community = Class(name="persons::Community")
persons_Person = Class(name="persons::Person", is_abstract=True)
persons_Facility = Class(name="persons::Facility", is_abstract=True)
persons_SpecialFacility = Class(name="persons::SpecialFacility")
Facility = Class(name="Facility")
persons_OrdinaryFacility = Class(name="persons::OrdinaryFacility")
persons_Committee = Class(name="persons::Committee")
persons_District = Class(name="persons::District")
persons_NamedElement = Class(name="persons::NamedElement", is_abstract=True)

# persons_TownHall class attributes and methods

# persons_Association class attributes and methods

# persons_Man class attributes and methods

# Person class attributes and methods

# persons_Woman class attributes and methods

# NamedElement class attributes and methods

# persons_Community class attributes and methods

# persons_Person class attributes and methods
persons_Person_fullName: Property = Property(name="fullName", type=StringType)
persons_Person.attributes={persons_Person_fullName}

# persons_Facility class attributes and methods

# persons_SpecialFacility class attributes and methods

# Facility class attributes and methods

# persons_OrdinaryFacility class attributes and methods

# persons_Committee class attributes and methods

# persons_District class attributes and methods

# persons_NamedElement class attributes and methods
persons_NamedElement_name: Property = Property(name="name", type=StringType)
persons_NamedElement.attributes={persons_NamedElement_name}

# Relationships
persons0: BinaryAssociation = BinaryAssociation(
    name="persons0",
    ends={
        Property(name="persons_Community", type=persons_Person, multiplicity=Multiplicity(1, 9999), is_composite=True),
        Property(name="persons_Person", type=persons_Community, multiplicity=Multiplicity(1, 1))
    }
)
townHalls1: BinaryAssociation = BinaryAssociation(
    name="townHalls1",
    ends={
        Property(name="persons_TownHall", type=persons_Community, multiplicity=Multiplicity(1, 1)),
        Property(name="persons_Community2", type=persons_TownHall, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
associations3: BinaryAssociation = BinaryAssociation(
    name="associations3",
    ends={
        Property(name="persons_Association", type=persons_Community, multiplicity=Multiplicity(1, 1)),
        Property(name="persons_Community4", type=persons_Association, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
facilities12: BinaryAssociation = BinaryAssociation(
    name="facilities12",
    ends={
        Property(name="persons_Facility", type=persons_District, multiplicity=Multiplicity(1, 1)),
        Property(name="persons_District13", type=persons_Facility, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
members14: BinaryAssociation = BinaryAssociation(
    name="members14",
    ends={
        Property(name="persons_Person16", type=persons_Facility, multiplicity=Multiplicity(1, 1)),
        Property(name="persons_Facility15", type=persons_Person, multiplicity=Multiplicity(0, 9999))
    }
)
workers5: BinaryAssociation = BinaryAssociation(
    name="workers5",
    ends={
        Property(name="persons_Person7", type=persons_TownHall, multiplicity=Multiplicity(1, 1)),
        Property(name="persons_TownHall6", type=persons_Person, multiplicity=Multiplicity(0, 9999))
    }
)
committee8: BinaryAssociation = BinaryAssociation(
    name="committee8",
    ends={
        Property(name="persons_Committee", type=persons_TownHall, multiplicity=Multiplicity(1, 1)),
        Property(name="persons_TownHall9", type=persons_Committee, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
districts10: BinaryAssociation = BinaryAssociation(
    name="districts10",
    ends={
        Property(name="persons_District", type=persons_TownHall, multiplicity=Multiplicity(1, 1)),
        Property(name="persons_TownHall11", type=persons_District, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Generalizations
gen_persons_Man_Person = Generalization(general=Person, specific=persons_Man)
gen_persons_Woman_Person = Generalization(general=Person, specific=persons_Woman)
gen_persons_TownHall_NamedElement = Generalization(general=NamedElement, specific=persons_TownHall)
gen_persons_Committee_NamedElement = Generalization(general=NamedElement, specific=persons_Committee)
gen_persons_District_NamedElement = Generalization(general=NamedElement, specific=persons_District)
gen_persons_Facility_NamedElement = Generalization(general=NamedElement, specific=persons_Facility)
gen_persons_SpecialFacility_Facility = Generalization(general=Facility, specific=persons_SpecialFacility)
gen_persons_OrdinaryFacility_Facility = Generalization(general=Facility, specific=persons_OrdinaryFacility)
gen_persons_Association_NamedElement = Generalization(general=NamedElement, specific=persons_Association)

# Domain Model
domain_model = DomainModel(
    name="persons",
    types={persons_TownHall, persons_Association, persons_Man, Person, persons_Woman, NamedElement, persons_Community, persons_Person, persons_Facility, persons_SpecialFacility, Facility, persons_OrdinaryFacility, persons_Committee, persons_District, persons_NamedElement},
    associations={persons0, townHalls1, associations3, facilities12, members14, workers5, committee8, districts10},
    generalizations={gen_persons_Man_Person, gen_persons_Woman_Person, gen_persons_TownHall_NamedElement, gen_persons_Committee_NamedElement, gen_persons_District_NamedElement, gen_persons_Facility_NamedElement, gen_persons_SpecialFacility_Facility, gen_persons_OrdinaryFacility_Facility, gen_persons_Association_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)