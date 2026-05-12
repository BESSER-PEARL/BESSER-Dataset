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
PetriNetMM2_PetriNet = Class(name="PetriNetMM2_PetriNet")
Place = Class(name="Place")
Transition = Class(name="Transition")
Arc = Class(name="Arc")
PetriNetMM2_PetriNetModel = Class(name="PetriNetMM2_PetriNetModel")
PetriNetModelElement = Class(name="PetriNetModelElement")
PetriNetMM2_PetriNetModelElement = Class(name="PetriNetMM2_PetriNetModelElement")
PetriNetModel = Class(name="PetriNetModel")
PetriNetMM2_Place = Class(name="PetriNetMM2_Place")
GenericPT = Class(name="GenericPT")
PetriNet = Class(name="PetriNet")
PTArc = Class(name="PTArc")
TPArc = Class(name="TPArc")
PetriNetMM2_Transition = Class(name="PetriNetMM2_Transition")
PetriNetMM2_GenericPT = Class(name="PetriNetMM2_GenericPT")
PetriNetMM2_Arc = Class(name="PetriNetMM2_Arc")
PetriNetMM2_PTArc = Class(name="PetriNetMM2_PTArc")
PetriNetMM2_TPArc = Class(name="PetriNetMM2_TPArc")

# PetriNetMM2_PetriNet class attributes and methods
PetriNetMM2_PetriNet_name: Property = Property(name="name", type=StringType)
PetriNetMM2_PetriNet.attributes={PetriNetMM2_PetriNet_name}

# Place class attributes and methods

# Transition class attributes and methods

# Arc class attributes and methods

# PetriNetMM2_PetriNetModel class attributes and methods

# PetriNetModelElement class attributes and methods

# PetriNetMM2_PetriNetModelElement class attributes and methods

# PetriNetModel class attributes and methods

# PetriNetMM2_Place class attributes and methods
PetriNetMM2_Place_name: Property = Property(name="name", type=StringType)
PetriNetMM2_Place_relevance: Property = Property(name="relevance", type=IntegerType)
PetriNetMM2_Place.attributes={PetriNetMM2_Place_name, PetriNetMM2_Place_relevance}

# GenericPT class attributes and methods

# PetriNet class attributes and methods

# PTArc class attributes and methods

# TPArc class attributes and methods

# PetriNetMM2_Transition class attributes and methods
PetriNetMM2_Transition_name: Property = Property(name="name", type=StringType)
PetriNetMM2_Transition_relevance: Property = Property(name="relevance", type=IntegerType)
PetriNetMM2_Transition.attributes={PetriNetMM2_Transition_name, PetriNetMM2_Transition_relevance}

# PetriNetMM2_GenericPT class attributes and methods
PetriNetMM2_GenericPT_label: Property = Property(name="label", type=StringType)
PetriNetMM2_GenericPT.attributes={PetriNetMM2_GenericPT_label}

# PetriNetMM2_Arc class attributes and methods
PetriNetMM2_Arc_weight: Property = Property(name="weight", type=IntegerType)
PetriNetMM2_Arc.attributes={PetriNetMM2_Arc_weight}

# PetriNetMM2_PTArc class attributes and methods

# PetriNetMM2_TPArc class attributes and methods

# Relationships
places2: BinaryAssociation = BinaryAssociation(
    name="places2",
    ends={
        Property(name="Place", type=PetriNetMM2_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="net", type=Place, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions3: BinaryAssociation = BinaryAssociation(
    name="transitions3",
    ends={
        Property(name="Transition", type=PetriNetMM2_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="net4", type=Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arcs5: BinaryAssociation = BinaryAssociation(
    name="arcs5",
    ends={
        Property(name="Arc", type=PetriNetMM2_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNetMM2_PetriNet", type=Arc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="PetriNetModelElement", type=PetriNetMM2_PetriNetModel, multiplicity=Multiplicity(1, 1)),
        Property(name="modelContainer", type=PetriNetModelElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modelContainer1: BinaryAssociation = BinaryAssociation(
    name="modelContainer1",
    ends={
        Property(name="PetriNetModel", type=PetriNetMM2_PetriNetModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements", type=PetriNetModel, multiplicity=Multiplicity(1, 1))
    }
)
net9: BinaryAssociation = BinaryAssociation(
    name="net9",
    ends={
        Property(name="PetriNet10", type=PetriNetMM2_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transitions", type=PetriNet, multiplicity=Multiplicity(1, 1))
    }
)
in_11: BinaryAssociation = BinaryAssociation(
    name="in_11",
    ends={
        Property(name="PTArc13", type=PetriNetMM2_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="dst12", type=PTArc, multiplicity=Multiplicity(1, 9999))
    }
)
out14: BinaryAssociation = BinaryAssociation(
    name="out14",
    ends={
        Property(name="TPArc16", type=PetriNetMM2_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="src15", type=TPArc, multiplicity=Multiplicity(1, 9999))
    }
)
net6: BinaryAssociation = BinaryAssociation(
    name="net6",
    ends={
        Property(name="PetriNet", type=PetriNetMM2_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="places", type=PetriNet, multiplicity=Multiplicity(1, 1))
    }
)
out7: BinaryAssociation = BinaryAssociation(
    name="out7",
    ends={
        Property(name="PTArc", type=PetriNetMM2_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="src", type=PTArc, multiplicity=Multiplicity(0, 9999))
    }
)
in_8: BinaryAssociation = BinaryAssociation(
    name="in_8",
    ends={
        Property(name="TPArc", type=PetriNetMM2_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="dst", type=TPArc, multiplicity=Multiplicity(0, 9999))
    }
)
dst24: BinaryAssociation = BinaryAssociation(
    name="dst24",
    ends={
        Property(name="Place26", type=PetriNetMM2_TPArc, multiplicity=Multiplicity(1, 1)),
        Property(name="in_25", type=Place, multiplicity=Multiplicity(0, 9999))
    }
)
src17: BinaryAssociation = BinaryAssociation(
    name="src17",
    ends={
        Property(name="Place18", type=PetriNetMM2_PTArc, multiplicity=Multiplicity(1, 1)),
        Property(name="out", type=Place, multiplicity=Multiplicity(1, 1))
    }
)
dst19: BinaryAssociation = BinaryAssociation(
    name="dst19",
    ends={
        Property(name="Transition20", type=PetriNetMM2_PTArc, multiplicity=Multiplicity(1, 1)),
        Property(name="in_", type=Transition, multiplicity=Multiplicity(0, 9999))
    }
)
src21: BinaryAssociation = BinaryAssociation(
    name="src21",
    ends={
        Property(name="Transition23", type=PetriNetMM2_TPArc, multiplicity=Multiplicity(1, 1)),
        Property(name="out22", type=Transition, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_PetriNetMM2_PetriNet_PetriNetModelElement = Generalization(general=PetriNetModelElement, specific=PetriNetMM2_PetriNet)
gen_PetriNetMM2_Place_GenericPT = Generalization(general=GenericPT, specific=PetriNetMM2_Place)
gen_PetriNetMM2_Transition_GenericPT = Generalization(general=GenericPT, specific=PetriNetMM2_Transition)
gen_PetriNetMM2_GenericPT_PetriNetModelElement = Generalization(general=PetriNetModelElement, specific=PetriNetMM2_GenericPT)
gen_PetriNetMM2_Arc_PetriNetModelElement = Generalization(general=PetriNetModelElement, specific=PetriNetMM2_Arc)
gen_PetriNetMM2_PTArc_Arc = Generalization(general=Arc, specific=PetriNetMM2_PTArc)
gen_PetriNetMM2_TPArc_Arc = Generalization(general=Arc, specific=PetriNetMM2_TPArc)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={PetriNetMM2_PetriNet, Place, Transition, Arc, PetriNetMM2_PetriNetModel, PetriNetModelElement, PetriNetMM2_PetriNetModelElement, PetriNetModel, PetriNetMM2_Place, GenericPT, PetriNet, PTArc, TPArc, PetriNetMM2_Transition, PetriNetMM2_GenericPT, PetriNetMM2_Arc, PetriNetMM2_PTArc, PetriNetMM2_TPArc},
    associations={places2, transitions3, arcs5, elements0, modelContainer1, net9, in_11, out14, net6, out7, in_8, dst24, src17, dst19, src21},
    generalizations={gen_PetriNetMM2_PetriNet_PetriNetModelElement, gen_PetriNetMM2_Place_GenericPT, gen_PetriNetMM2_Transition_GenericPT, gen_PetriNetMM2_GenericPT_PetriNetModelElement, gen_PetriNetMM2_Arc_PetriNetModelElement, gen_PetriNetMM2_PTArc_Arc, gen_PetriNetMM2_TPArc_Arc},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)