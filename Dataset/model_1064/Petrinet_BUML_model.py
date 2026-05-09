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
petrinet_NamedElement = Class(name="petrinet_NamedElement")
petrinet_Petrinet = Class(name="petrinet_Petrinet")
NamedElement = Class(name="NamedElement")
petrinet_Place = Class(name="petrinet_Place")
petrinet_Transition = Class(name="petrinet_Transition")
Arc = Class(name="Arc")
petrinet_Arc = Class(name="petrinet_Arc", is_abstract=True)
petrinet_PTArc = Class(name="petrinet_PTArc")
petrinet_TPArc = Class(name="petrinet_TPArc")

# petrinet_NamedElement class attributes and methods
petrinet_NamedElement_name: Property = Property(name="name", type=StringType)
petrinet_NamedElement.attributes={petrinet_NamedElement_name}

# petrinet_Petrinet class attributes and methods

# NamedElement class attributes and methods

# petrinet_Place class attributes and methods

# petrinet_Transition class attributes and methods

# Arc class attributes and methods

# petrinet_Arc class attributes and methods
petrinet_Arc_weight: Property = Property(name="weight", type=IntegerType)
petrinet_Arc.attributes={petrinet_Arc_weight}

# petrinet_PTArc class attributes and methods

# petrinet_TPArc class attributes and methods

# Relationships
places0: BinaryAssociation = BinaryAssociation(
    name="places0",
    ends={
        Property(name="Place", type=petrinet_Petrinet, multiplicity=Multiplicity(1, 1)),
        Property(name="net", type=petrinet_Place, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="Transition", type=petrinet_Petrinet, multiplicity=Multiplicity(1, 1)),
        Property(name="net2", type=petrinet_Transition, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
out8: BinaryAssociation = BinaryAssociation(
    name="out8",
    ends={
        Property(name="TPArc10", type=petrinet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="src9", type=petrinet_TPArc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
in_11: BinaryAssociation = BinaryAssociation(
    name="in_11",
    ends={
        Property(name="PTArc13", type=petrinet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="dst12", type=petrinet_PTArc, multiplicity=Multiplicity(0, 1))
    }
)
dst14: BinaryAssociation = BinaryAssociation(
    name="dst14",
    ends={
        Property(name="Transition15", type=petrinet_PTArc, multiplicity=Multiplicity(1, 1)),
        Property(name="in_", type=petrinet_Transition, multiplicity=Multiplicity(1, 1))
    }
)
src16: BinaryAssociation = BinaryAssociation(
    name="src16",
    ends={
        Property(name="Place17", type=petrinet_PTArc, multiplicity=Multiplicity(1, 1)),
        Property(name="out", type=petrinet_Place, multiplicity=Multiplicity(1, 1))
    }
)
dst18: BinaryAssociation = BinaryAssociation(
    name="dst18",
    ends={
        Property(name="Place20", type=petrinet_TPArc, multiplicity=Multiplicity(1, 1)),
        Property(name="in_19", type=petrinet_Place, multiplicity=Multiplicity(1, 1))
    }
)
src21: BinaryAssociation = BinaryAssociation(
    name="src21",
    ends={
        Property(name="Transition23", type=petrinet_TPArc, multiplicity=Multiplicity(1, 1)),
        Property(name="out22", type=petrinet_Transition, multiplicity=Multiplicity(1, 1))
    }
)
net3: BinaryAssociation = BinaryAssociation(
    name="net3",
    ends={
        Property(name="Petrinet", type=petrinet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="places", type=petrinet_Petrinet, multiplicity=Multiplicity(1, 1))
    }
)
out4: BinaryAssociation = BinaryAssociation(
    name="out4",
    ends={
        Property(name="PTArc", type=petrinet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="src", type=petrinet_PTArc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
in_5: BinaryAssociation = BinaryAssociation(
    name="in_5",
    ends={
        Property(name="TPArc", type=petrinet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="dst", type=petrinet_TPArc, multiplicity=Multiplicity(0, 1))
    }
)
net6: BinaryAssociation = BinaryAssociation(
    name="net6",
    ends={
        Property(name="Petrinet7", type=petrinet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transitions", type=petrinet_Petrinet, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_petrinet_Petrinet_NamedElement = Generalization(general=NamedElement, specific=petrinet_Petrinet)
gen_petrinet_PTArc_Arc = Generalization(general=Arc, specific=petrinet_PTArc)
gen_petrinet_TPArc_Arc = Generalization(general=Arc, specific=petrinet_TPArc)
gen_petrinet_Place_NamedElement = Generalization(general=NamedElement, specific=petrinet_Place)
gen_petrinet_Transition_NamedElement = Generalization(general=NamedElement, specific=petrinet_Transition)

# Domain Model
domain_model = DomainModel(
    name="petrinet",
    types={petrinet_NamedElement, petrinet_Petrinet, NamedElement, petrinet_Place, petrinet_Transition, Arc, petrinet_Arc, petrinet_PTArc, petrinet_TPArc},
    associations={places0, transitions1, out8, in_11, dst14, src16, dst18, src21, net3, out4, in_5, net6},
    generalizations={gen_petrinet_Petrinet_NamedElement, gen_petrinet_PTArc_Arc, gen_petrinet_TPArc_Arc, gen_petrinet_Place_NamedElement, gen_petrinet_Transition_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)