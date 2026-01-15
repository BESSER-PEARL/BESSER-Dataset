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
petrinet_Transition = Class(name="petrinet::Transition")
petrinet_NamedElement = Class(name="petrinet::NamedElement")
petrinet_Net = Class(name="petrinet::Net")
NamedElement = Class(name="NamedElement")
petrinet_Place = Class(name="petrinet::Place")

# petrinet_Transition class attributes and methods

# petrinet_NamedElement class attributes and methods
petrinet_NamedElement_name: Property = Property(name="name", type=StringType)
petrinet_NamedElement.attributes={petrinet_NamedElement_name}

# petrinet_Net class attributes and methods

# NamedElement class attributes and methods

# petrinet_Place class attributes and methods

# Relationships
places0: BinaryAssociation = BinaryAssociation(
    name="places0",
    ends={
        Property(name="Place", type=petrinet_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="net", type=petrinet_Place, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="Transition", type=petrinet_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="net2", type=petrinet_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
net3: BinaryAssociation = BinaryAssociation(
    name="net3",
    ends={
        Property(name="Net", type=petrinet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="places", type=petrinet_Net, multiplicity=Multiplicity(1, 1))
    }
)
dst4: BinaryAssociation = BinaryAssociation(
    name="dst4",
    ends={
        Property(name="Transition5", type=petrinet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="src", type=petrinet_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
src6: BinaryAssociation = BinaryAssociation(
    name="src6",
    ends={
        Property(name="Transition7", type=petrinet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="dst", type=petrinet_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
net8: BinaryAssociation = BinaryAssociation(
    name="net8",
    ends={
        Property(name="Net9", type=petrinet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transitions", type=petrinet_Net, multiplicity=Multiplicity(1, 1))
    }
)
src10: BinaryAssociation = BinaryAssociation(
    name="src10",
    ends={
        Property(name="Place12", type=petrinet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="dst11", type=petrinet_Place, multiplicity=Multiplicity(0, 9999))
    }
)
dst13: BinaryAssociation = BinaryAssociation(
    name="dst13",
    ends={
        Property(name="Place15", type=petrinet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="src14", type=petrinet_Place, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_petrinet_Place_NamedElement = Generalization(general=NamedElement, specific=petrinet_Place)
gen_petrinet_Net_NamedElement = Generalization(general=NamedElement, specific=petrinet_Net)
gen_petrinet_Transition_NamedElement = Generalization(general=NamedElement, specific=petrinet_Transition)

# Domain Model
domain_model = DomainModel(
    name="petrinet",
    types={petrinet_Transition, petrinet_NamedElement, petrinet_Net, NamedElement, petrinet_Place},
    associations={places0, transitions1, net3, dst4, src6, net8, src10, dst13},
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