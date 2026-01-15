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
Named = Class(name="Named")
petrinet_PetriNet = Class(name="petrinet::PetriNet")
petrinet_Place = Class(name="petrinet::Place")
petrinet_InArc = Class(name="petrinet::InArc")
petrinet_OutArc = Class(name="petrinet::OutArc")
petrinet_Arc = Class(name="petrinet::Arc", is_abstract=True)
Arc = Class(name="Arc")
petrinet_Named = Class(name="petrinet::Named", is_abstract=True)

# petrinet_Transition class attributes and methods

# Named class attributes and methods

# petrinet_PetriNet class attributes and methods

# petrinet_Place class attributes and methods
petrinet_Place_token: Property = Property(name="token", type=IntegerType)
petrinet_Place.attributes={petrinet_Place_token}

# petrinet_InArc class attributes and methods

# petrinet_OutArc class attributes and methods

# petrinet_Arc class attributes and methods
petrinet_Arc_weight: Property = Property(name="weight", type=IntegerType)
petrinet_Arc.attributes={petrinet_Arc_weight}

# Arc class attributes and methods

# petrinet_Named class attributes and methods
petrinet_Named_name: Property = Property(name="name", type=StringType)
petrinet_Named.attributes={petrinet_Named_name}

# Relationships
places0: BinaryAssociation = BinaryAssociation(
    name="places0",
    ends={
        Property(name="petrinet_Place", type=petrinet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_PetriNet", type=petrinet_Place, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="petrinet_Transition", type=petrinet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_PetriNet2", type=petrinet_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inArc3: BinaryAssociation = BinaryAssociation(
    name="inArc3",
    ends={
        Property(name="petrinet_InArc", type=petrinet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Transition4", type=petrinet_InArc, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
outArc5: BinaryAssociation = BinaryAssociation(
    name="outArc5",
    ends={
        Property(name="petrinet_OutArc", type=petrinet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Transition6", type=petrinet_OutArc, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
targetPlace7: BinaryAssociation = BinaryAssociation(
    name="targetPlace7",
    ends={
        Property(name="petrinet_Place9", type=petrinet_InArc, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_InArc8", type=petrinet_Place, multiplicity=Multiplicity(1, 1))
    }
)
sourcePlace10: BinaryAssociation = BinaryAssociation(
    name="sourcePlace10",
    ends={
        Property(name="petrinet_Place12", type=petrinet_OutArc, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_OutArc11", type=petrinet_Place, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_petrinet_Place_Named = Generalization(general=Named, specific=petrinet_Place)
gen_petrinet_Transition_Named = Generalization(general=Named, specific=petrinet_Transition)
gen_petrinet_InArc_Arc = Generalization(general=Arc, specific=petrinet_InArc)
gen_petrinet_OutArc_Arc = Generalization(general=Arc, specific=petrinet_OutArc)

# Domain Model
domain_model = DomainModel(
    name="petrinet",
    types={petrinet_Transition, Named, petrinet_PetriNet, petrinet_Place, petrinet_InArc, petrinet_OutArc, petrinet_Arc, Arc, petrinet_Named},
    associations={places0, transitions1, inArc3, outArc5, targetPlace7, sourcePlace10},
    generalizations={gen_petrinet_Place_Named, gen_petrinet_Transition_Named, gen_petrinet_InArc_Arc, gen_petrinet_OutArc_Arc},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)