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
NamedElement = Class(name="NamedElement")
PetriNet_Net = Class(name="PetriNet::Net")
PetriNet_Place = Class(name="PetriNet::Place")
PetriNet_Transition = Class(name="PetriNet::Transition")
PetriNet_NamedElement = Class(name="PetriNet::NamedElement", is_abstract=True)

# NamedElement class attributes and methods

# PetriNet_Net class attributes and methods

# PetriNet_Place class attributes and methods

# PetriNet_Transition class attributes and methods

# PetriNet_NamedElement class attributes and methods
PetriNet_NamedElement_name: Property = Property(name="name", type=StringType)
PetriNet_NamedElement.attributes={PetriNet_NamedElement_name}

# Relationships
places0: BinaryAssociation = BinaryAssociation(
    name="places0",
    ends={
        Property(name="Place", type=PetriNet_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="cnet", type=PetriNet_Place, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="Transition", type=PetriNet_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="cnet2", type=PetriNet_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
postp10: BinaryAssociation = BinaryAssociation(
    name="postp10",
    ends={
        Property(name="pret", type=PetriNet_Place, multiplicity=Multiplicity(0, 9999)),
        Property(name="Place11", type=PetriNet_Transition, multiplicity=Multiplicity(1, 1))
    }
)
cnet12: BinaryAssociation = BinaryAssociation(
    name="cnet12",
    ends={
        Property(name="Net13", type=PetriNet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transitions", type=PetriNet_Net, multiplicity=Multiplicity(1, 1))
    }
)
postt3: BinaryAssociation = BinaryAssociation(
    name="postt3",
    ends={
        Property(name="Transition4", type=PetriNet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="prep", type=PetriNet_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
pret5: BinaryAssociation = BinaryAssociation(
    name="pret5",
    ends={
        Property(name="Transition6", type=PetriNet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="postp", type=PetriNet_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
cnet7: BinaryAssociation = BinaryAssociation(
    name="cnet7",
    ends={
        Property(name="Net", type=PetriNet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="places", type=PetriNet_Net, multiplicity=Multiplicity(1, 1))
    }
)
prep8: BinaryAssociation = BinaryAssociation(
    name="prep8",
    ends={
        Property(name="Place9", type=PetriNet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="postt", type=PetriNet_Place, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_PetriNet_Place_NamedElement = Generalization(general=NamedElement, specific=PetriNet_Place)
gen_PetriNet_Transition_NamedElement = Generalization(general=NamedElement, specific=PetriNet_Transition)

# Domain Model
domain_model = DomainModel(
    name="PetriNet",
    types={NamedElement, PetriNet_Net, PetriNet_Place, PetriNet_Transition, PetriNet_NamedElement},
    associations={places0, transitions1, postp10, cnet12, postt3, pret5, cnet7, prep8},
    generalizations={gen_PetriNet_Place_NamedElement, gen_PetriNet_Transition_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)