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
petrinet_Place = Class(name="petrinet::Place")
petrinet_Transition = Class(name="petrinet::Transition")
Arc = Class(name="Arc")
petrinet_Arc = Class(name="petrinet::Arc")
petrinet_Token = Class(name="petrinet::Token")
petrinet_PTArc = Class(name="petrinet::PTArc")
petrinet_TPArc = Class(name="petrinet::TPArc")

# petrinet_Petrinet class attributes and methods
petrinet_Petrinet_name: Property = Property(name="name", type=StringType)
petrinet_Petrinet.attributes={petrinet_Petrinet_name}

# petrinet_Place class attributes and methods
petrinet_Place_name: Property = Property(name="name", type=StringType)
petrinet_Place.attributes={petrinet_Place_name}

# petrinet_Transition class attributes and methods
petrinet_Transition_name: Property = Property(name="name", type=StringType)
petrinet_Transition.attributes={petrinet_Transition_name}

# Arc class attributes and methods

# petrinet_Arc class attributes and methods
petrinet_Arc_name: Property = Property(name="name", type=StringType)
petrinet_Arc_weight: Property = Property(name="weight", type=IntegerType)
petrinet_Arc.attributes={petrinet_Arc_weight, petrinet_Arc_name}

# petrinet_Token class attributes and methods

# petrinet_PTArc class attributes and methods

# petrinet_TPArc class attributes and methods

# Relationships
places0: BinaryAssociation = BinaryAssociation(
    name="places0",
    ends={
        Property(name="petrinet_Place", type=petrinet_Petrinet, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Petrinet", type=petrinet_Place, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="petrinet_Transition", type=petrinet_Petrinet, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Petrinet2", type=petrinet_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
out11: BinaryAssociation = BinaryAssociation(
    name="out11",
    ends={
        Property(name="petrinet_TPArc13", type=petrinet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Transition12", type=petrinet_TPArc, multiplicity=Multiplicity(0, 9999))
    }
)
in14: BinaryAssociation = BinaryAssociation(
    name="in14",
    ends={
        Property(name="petrinet_PTArc16", type=petrinet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Transition15", type=petrinet_PTArc, multiplicity=Multiplicity(0, 9999))
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
        Property(name="petrinet_PTArc", type=petrinet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Place8", type=petrinet_PTArc, multiplicity=Multiplicity(0, 9999))
    }
)
in9: BinaryAssociation = BinaryAssociation(
    name="in9",
    ends={
        Property(name="petrinet_TPArc", type=petrinet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Place10", type=petrinet_TPArc, multiplicity=Multiplicity(0, 9999))
    }
)
source17: BinaryAssociation = BinaryAssociation(
    name="source17",
    ends={
        Property(name="petrinet_Place19", type=petrinet_PTArc, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_PTArc18", type=petrinet_Place, multiplicity=Multiplicity(0, 1))
    }
)
target20: BinaryAssociation = BinaryAssociation(
    name="target20",
    ends={
        Property(name="petrinet_Transition22", type=petrinet_PTArc, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_PTArc21", type=petrinet_Transition, multiplicity=Multiplicity(0, 1))
    }
)
source23: BinaryAssociation = BinaryAssociation(
    name="source23",
    ends={
        Property(name="petrinet_Transition25", type=petrinet_TPArc, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_TPArc24", type=petrinet_Transition, multiplicity=Multiplicity(0, 1))
    }
)
target26: BinaryAssociation = BinaryAssociation(
    name="target26",
    ends={
        Property(name="petrinet_Place28", type=petrinet_TPArc, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_TPArc27", type=petrinet_Place, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_petrinet_PTArc_Arc = Generalization(general=Arc, specific=petrinet_PTArc)
gen_petrinet_TPArc_Arc = Generalization(general=Arc, specific=petrinet_TPArc)

# Domain Model
domain_model = DomainModel(
    name="petrinet",
    types={petrinet_Petrinet, petrinet_Place, petrinet_Transition, Arc, petrinet_Arc, petrinet_Token, petrinet_PTArc, petrinet_TPArc},
    associations={places0, transitions1, out11, in14, arcs3, tokens5, out7, in9, source17, target20, source23, target26},
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