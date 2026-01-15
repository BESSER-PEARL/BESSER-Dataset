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
petrinet_Net = Class(name="petrinet::Net")
petrinet_Place = Class(name="petrinet::Place")
petrinet_Transition = Class(name="petrinet::Transition")
petrinet_NamedElement = Class(name="petrinet::NamedElement", is_abstract=True)
NamedElement = Class(name="NamedElement")

# petrinet_Net class attributes and methods

# petrinet_Place class attributes and methods

# petrinet_Transition class attributes and methods

# petrinet_NamedElement class attributes and methods
petrinet_NamedElement_name: Property = Property(name="name", type=StringType)
petrinet_NamedElement.attributes={petrinet_NamedElement_name}

# NamedElement class attributes and methods

# Relationships
places0: BinaryAssociation = BinaryAssociation(
    name="places0",
    ends={
        Property(name="Place", type=petrinet_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="cnet", type=petrinet_Place, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="Transition", type=petrinet_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="cnet2", type=petrinet_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pret5: BinaryAssociation = BinaryAssociation(
    name="pret5",
    ends={
        Property(name="Transition6", type=petrinet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="postp", type=petrinet_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
cnet7: BinaryAssociation = BinaryAssociation(
    name="cnet7",
    ends={
        Property(name="Net", type=petrinet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="places", type=petrinet_Net, multiplicity=Multiplicity(1, 1))
    }
)
postt3: BinaryAssociation = BinaryAssociation(
    name="postt3",
    ends={
        Property(name="Transition4", type=petrinet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="prep", type=petrinet_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
prep8: BinaryAssociation = BinaryAssociation(
    name="prep8",
    ends={
        Property(name="Place9", type=petrinet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="postt", type=petrinet_Place, multiplicity=Multiplicity(0, 9999))
    }
)
postp10: BinaryAssociation = BinaryAssociation(
    name="postp10",
    ends={
        Property(name="Place11", type=petrinet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="pret", type=petrinet_Place, multiplicity=Multiplicity(0, 9999))
    }
)
cnet12: BinaryAssociation = BinaryAssociation(
    name="cnet12",
    ends={
        Property(name="Net13", type=petrinet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transitions", type=petrinet_Net, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_petrinet_Place_NamedElement = Generalization(general=NamedElement, specific=petrinet_Place)
gen_petrinet_Transition_NamedElement = Generalization(general=NamedElement, specific=petrinet_Transition)

# Domain Model
domain_model = DomainModel(
    name="petrinet",
    types={petrinet_Net, petrinet_Place, petrinet_Transition, petrinet_NamedElement, NamedElement},
    associations={places0, transitions1, pret5, cnet7, postt3, prep8, postp10, cnet12},
    generalizations={gen_petrinet_Place_NamedElement, gen_petrinet_Transition_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)