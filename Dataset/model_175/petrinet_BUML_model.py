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
NamedElement = Class(name="NamedElement")
petrinet_Place = Class(name="petrinet::Place")
petrinet_Transition = Class(name="petrinet::Transition")
petrinet_NamedElement = Class(name="petrinet::NamedElement")

# petrinet_Net class attributes and methods

# NamedElement class attributes and methods

# petrinet_Place class attributes and methods
petrinet_Place_tokens: Property = Property(name="tokens", type=IntegerType)
petrinet_Place.attributes={petrinet_Place_tokens}

# petrinet_Transition class attributes and methods

# petrinet_NamedElement class attributes and methods
petrinet_NamedElement_name: Property = Property(name="name", type=StringType)
petrinet_NamedElement.attributes={petrinet_NamedElement_name}

# Relationships
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="petrinet_Transition", type=petrinet_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Net2", type=petrinet_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
first3: BinaryAssociation = BinaryAssociation(
    name="first3",
    ends={
        Property(name="petrinet_Place5", type=petrinet_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Net4", type=petrinet_Place, multiplicity=Multiplicity(1, 1))
    }
)
places0: BinaryAssociation = BinaryAssociation(
    name="places0",
    ends={
        Property(name="petrinet_Place", type=petrinet_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Net", type=petrinet_Place, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
to6: BinaryAssociation = BinaryAssociation(
    name="to6",
    ends={
        Property(name="petrinet_Transition8", type=petrinet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Place7", type=petrinet_Transition, multiplicity=Multiplicity(0, 1))
    }
)
input9: BinaryAssociation = BinaryAssociation(
    name="input9",
    ends={
        Property(name="petrinet_Place11", type=petrinet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Transition10", type=petrinet_Place, multiplicity=Multiplicity(0, 9999))
    }
)
output12: BinaryAssociation = BinaryAssociation(
    name="output12",
    ends={
        Property(name="petrinet_Place14", type=petrinet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Transition13", type=petrinet_Place, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_petrinet_Place_NamedElement = Generalization(general=NamedElement, specific=petrinet_Place)
gen_petrinet_Net_NamedElement = Generalization(general=NamedElement, specific=petrinet_Net)
gen_petrinet_Transition_NamedElement = Generalization(general=NamedElement, specific=petrinet_Transition)

# Domain Model
domain_model = DomainModel(
    name="petrinet",
    types={petrinet_Net, NamedElement, petrinet_Place, petrinet_Transition, petrinet_NamedElement},
    associations={transitions1, first3, places0, to6, input9, output12},
    generalizations={gen_petrinet_Place_NamedElement, gen_petrinet_Net_NamedElement, gen_petrinet_Transition_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)