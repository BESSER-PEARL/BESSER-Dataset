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
petriNetz_Petrinet = Class(name="petriNetz::Petrinet")
petriNetz_Transition = Class(name="petriNetz::Transition")
petriNetz_Arc = Class(name="petriNetz::Arc")
petriNetz_Token = Class(name="petriNetz::Token")
petriNetz_PTArc = Class(name="petriNetz::PTArc")
petriNetz_Place = Class(name="petriNetz::Place")
Arc = Class(name="Arc")
petriNetz_TPArc = Class(name="petriNetz::TPArc")

# petriNetz_Petrinet class attributes and methods
petriNetz_Petrinet_name: Property = Property(name="name", type=StringType)
petriNetz_Petrinet.attributes={petriNetz_Petrinet_name}

# petriNetz_Transition class attributes and methods
petriNetz_Transition_name: Property = Property(name="name", type=StringType)
petriNetz_Transition.attributes={petriNetz_Transition_name}

# petriNetz_Arc class attributes and methods
petriNetz_Arc_weight: Property = Property(name="weight", type=IntegerType)
petriNetz_Arc.attributes={petriNetz_Arc_weight}

# petriNetz_Token class attributes and methods

# petriNetz_PTArc class attributes and methods

# petriNetz_Place class attributes and methods
petriNetz_Place_name: Property = Property(name="name", type=StringType)
petriNetz_Place.attributes={petriNetz_Place_name}

# Arc class attributes and methods

# petriNetz_TPArc class attributes and methods

# Relationships
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="petriNetz_Transition", type=petriNetz_Petrinet, multiplicity=Multiplicity(1, 1)),
        Property(name="petriNetz_Petrinet2", type=petriNetz_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arcs3: BinaryAssociation = BinaryAssociation(
    name="arcs3",
    ends={
        Property(name="petriNetz_Arc", type=petriNetz_Petrinet, multiplicity=Multiplicity(1, 1)),
        Property(name="petriNetz_Petrinet4", type=petriNetz_Arc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tokens5: BinaryAssociation = BinaryAssociation(
    name="tokens5",
    ends={
        Property(name="petriNetz_Token", type=petriNetz_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="petriNetz_Place6", type=petriNetz_Token, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
out7: BinaryAssociation = BinaryAssociation(
    name="out7",
    ends={
        Property(name="petriNetz_PTArc", type=petriNetz_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="petriNetz_Place8", type=petriNetz_PTArc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
places0: BinaryAssociation = BinaryAssociation(
    name="places0",
    ends={
        Property(name="petriNetz_Place", type=petriNetz_Petrinet, multiplicity=Multiplicity(1, 1)),
        Property(name="petriNetz_Petrinet", type=petriNetz_Place, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
in11: BinaryAssociation = BinaryAssociation(
    name="in11",
    ends={
        Property(name="petriNetz_PTArc13", type=petriNetz_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="petriNetz_Transition12", type=petriNetz_PTArc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
out14: BinaryAssociation = BinaryAssociation(
    name="out14",
    ends={
        Property(name="petriNetz_TPArc16", type=petriNetz_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="petriNetz_Transition15", type=petriNetz_TPArc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
src17: BinaryAssociation = BinaryAssociation(
    name="src17",
    ends={
        Property(name="petriNetz_Place19", type=petriNetz_PTArc, multiplicity=Multiplicity(1, 1)),
        Property(name="petriNetz_PTArc18", type=petriNetz_Place, multiplicity=Multiplicity(0, 1))
    }
)
trg20: BinaryAssociation = BinaryAssociation(
    name="trg20",
    ends={
        Property(name="petriNetz_Transition22", type=petriNetz_PTArc, multiplicity=Multiplicity(1, 1)),
        Property(name="petriNetz_PTArc21", type=petriNetz_Transition, multiplicity=Multiplicity(0, 1))
    }
)
in9: BinaryAssociation = BinaryAssociation(
    name="in9",
    ends={
        Property(name="petriNetz_TPArc", type=petriNetz_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="petriNetz_Place10", type=petriNetz_TPArc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
trg23: BinaryAssociation = BinaryAssociation(
    name="trg23",
    ends={
        Property(name="petriNetz_Place25", type=petriNetz_TPArc, multiplicity=Multiplicity(1, 1)),
        Property(name="petriNetz_TPArc24", type=petriNetz_Place, multiplicity=Multiplicity(0, 1))
    }
)
src26: BinaryAssociation = BinaryAssociation(
    name="src26",
    ends={
        Property(name="petriNetz_Transition28", type=petriNetz_TPArc, multiplicity=Multiplicity(1, 1)),
        Property(name="petriNetz_TPArc27", type=petriNetz_Transition, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_petriNetz_PTArc_Arc = Generalization(general=Arc, specific=petriNetz_PTArc)
gen_petriNetz_TPArc_Arc = Generalization(general=Arc, specific=petriNetz_TPArc)

# Domain Model
domain_model = DomainModel(
    name="petriNetz",
    types={petriNetz_Petrinet, petriNetz_Transition, petriNetz_Arc, petriNetz_Token, petriNetz_PTArc, petriNetz_Place, Arc, petriNetz_TPArc},
    associations={transitions1, arcs3, tokens5, out7, places0, in11, out14, src17, trg20, in9, trg23, src26},
    generalizations={gen_petriNetz_PTArc_Arc, gen_petriNetz_TPArc_Arc},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)