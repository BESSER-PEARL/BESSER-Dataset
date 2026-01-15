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
pn_NamedElement = Class(name="pn::NamedElement", is_abstract=True)
pn_Net = Class(name="pn::Net")
NamedElement = Class(name="NamedElement")
pn_NetElement = Class(name="pn::NetElement", is_abstract=True)
pn_Transition = Class(name="pn::Transition")
NetElement = Class(name="NetElement")
pn_Place = Class(name="pn::Place")

# pn_NamedElement class attributes and methods
pn_NamedElement_name: Property = Property(name="name", type=StringType)
pn_NamedElement.attributes={pn_NamedElement_name}

# pn_Net class attributes and methods
pn_Net_incrementalID: Property = Property(name="incrementalID", type=StringType)
pn_Net.attributes={pn_Net_incrementalID}

# NamedElement class attributes and methods

# pn_NetElement class attributes and methods

# pn_Transition class attributes and methods

# NetElement class attributes and methods

# pn_Place class attributes and methods
pn_Place_noOfTokens: Property = Property(name="noOfTokens", type=IntegerType)
pn_Place.attributes={pn_Place_noOfTokens}

# Relationships
trgT2P2: BinaryAssociation = BinaryAssociation(
    name="trgT2P2",
    ends={
        Property(name="Place", type=pn_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="srcT2P", type=pn_Place, multiplicity=Multiplicity(0, 9999))
    }
)
srcP2T3: BinaryAssociation = BinaryAssociation(
    name="srcP2T3",
    ends={
        Property(name="Place4", type=pn_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="trgP2T", type=pn_Place, multiplicity=Multiplicity(0, 9999))
    }
)
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="NetElement", type=pn_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="net", type=pn_NetElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
net1: BinaryAssociation = BinaryAssociation(
    name="net1",
    ends={
        Property(name="Net", type=pn_NetElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements", type=pn_Net, multiplicity=Multiplicity(1, 1))
    }
)
trgP2T5: BinaryAssociation = BinaryAssociation(
    name="trgP2T5",
    ends={
        Property(name="Transition", type=pn_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="srcP2T", type=pn_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
srcT2P6: BinaryAssociation = BinaryAssociation(
    name="srcT2P6",
    ends={
        Property(name="Transition7", type=pn_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="trgT2P", type=pn_Transition, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_pn_Net_NamedElement = Generalization(general=NamedElement, specific=pn_Net)
gen_pn_Transition_NetElement = Generalization(general=NetElement, specific=pn_Transition)
gen_pn_Place_NetElement = Generalization(general=NetElement, specific=pn_Place)
gen_pn_NetElement_NamedElement = Generalization(general=NamedElement, specific=pn_NetElement)
gen_pn_Place_NamedElement = Generalization(general=NamedElement, specific=pn_Place)

# Domain Model
domain_model = DomainModel(
    name="pn",
    types={pn_NamedElement, pn_Net, NamedElement, pn_NetElement, pn_Transition, NetElement, pn_Place},
    associations={trgT2P2, srcP2T3, elements0, net1, trgP2T5, srcT2P6},
    generalizations={gen_pn_Net_NamedElement, gen_pn_Transition_NetElement, gen_pn_Place_NetElement, gen_pn_NetElement_NamedElement, gen_pn_Place_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)