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
petrinet_Petrinet = Class(name="petrinet::Petrinet")
petrinet_Arc = Class(name="petrinet::Arc")
petrinet_Token = Class(name="petrinet::Token")
petrinet_PTArc = Class(name="petrinet::PTArc")
petrinet_TPArc = Class(name="petrinet::TPArc")
petrinet_Place = Class(name="petrinet::Place")
petrinet_Transition = Class(name="petrinet::Transition")
Arc = Class(name="Arc")

# petrinet_Petrinet class attributes and methods
petrinet_Petrinet_name: Property = Property(name="name", type=StringType)
petrinet_Petrinet.attributes={petrinet_Petrinet_name}

# petrinet_Arc class attributes and methods
petrinet_Arc_weight: Property = Property(name="weight", type=IntegerType)
petrinet_Arc.attributes={petrinet_Arc_weight}

# petrinet_Token class attributes and methods

# petrinet_PTArc class attributes and methods

# petrinet_TPArc class attributes and methods

# petrinet_Place class attributes and methods
petrinet_Place_name: Property = Property(name="name", type=StringType)
petrinet_Place.attributes={petrinet_Place_name}

# petrinet_Transition class attributes and methods
petrinet_Transition_name: Property = Property(name="name", type=StringType)
petrinet_Transition.attributes={petrinet_Transition_name}

# Arc class attributes and methods

# Relationships
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="petrinet_Transition", type=petrinet_Petrinet, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Petrinet2", type=petrinet_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arcs3: BinaryAssociation = BinaryAssociation(
    name="arcs3",
    ends={
        Property(name="petrinet_Arc", type=petrinet_Petrinet, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Petrinet4", type=petrinet_Arc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tokens5: BinaryAssociation = BinaryAssociation(
    name="tokens5",
    ends={
        Property(name="petrinet_Token", type=petrinet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Place6", type=petrinet_Token, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
out7: BinaryAssociation = BinaryAssociation(
    name="out7",
    ends={
        Property(name="PTArc", type=petrinet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="src", type=petrinet_PTArc, multiplicity=Multiplicity(0, 9999))
    }
)
in8: BinaryAssociation = BinaryAssociation(
    name="in8",
    ends={
        Property(name="TPArc", type=petrinet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="trg", type=petrinet_TPArc, multiplicity=Multiplicity(0, 9999))
    }
)
places0: BinaryAssociation = BinaryAssociation(
    name="places0",
    ends={
        Property(name="petrinet_Place", type=petrinet_Petrinet, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Petrinet", type=petrinet_Place, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
out12: BinaryAssociation = BinaryAssociation(
    name="out12",
    ends={
        Property(name="TPArc14", type=petrinet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="src13", type=petrinet_TPArc, multiplicity=Multiplicity(0, 9999))
    }
)
src15: BinaryAssociation = BinaryAssociation(
    name="src15",
    ends={
        Property(name="Place", type=petrinet_PTArc, multiplicity=Multiplicity(1, 1)),
        Property(name="out", type=petrinet_Place, multiplicity=Multiplicity(0, 9999))
    }
)
trg16: BinaryAssociation = BinaryAssociation(
    name="trg16",
    ends={
        Property(name="Transition", type=petrinet_PTArc, multiplicity=Multiplicity(1, 1)),
        Property(name="in", type=petrinet_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
in9: BinaryAssociation = BinaryAssociation(
    name="in9",
    ends={
        Property(name="PTArc11", type=petrinet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="trg10", type=petrinet_PTArc, multiplicity=Multiplicity(0, 9999))
    }
)
src17: BinaryAssociation = BinaryAssociation(
    name="src17",
    ends={
        Property(name="Transition19", type=petrinet_TPArc, multiplicity=Multiplicity(1, 1)),
        Property(name="out18", type=petrinet_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
trg20: BinaryAssociation = BinaryAssociation(
    name="trg20",
    ends={
        Property(name="Place22", type=petrinet_TPArc, multiplicity=Multiplicity(1, 1)),
        Property(name="in21", type=petrinet_Place, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_petrinet_PTArc_Arc = Generalization(general=Arc, specific=petrinet_PTArc)
gen_petrinet_TPArc_Arc = Generalization(general=Arc, specific=petrinet_TPArc)

# Domain Model
domain_model = DomainModel(
    name="petrinet",
    types={petrinet_Petrinet, petrinet_Arc, petrinet_Token, petrinet_PTArc, petrinet_TPArc, petrinet_Place, petrinet_Transition, Arc},
    associations={transitions1, arcs3, tokens5, out7, in8, places0, out12, src15, trg16, in9, src17, trg20},
    generalizations={gen_petrinet_PTArc_Arc, gen_petrinet_TPArc_Arc},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)