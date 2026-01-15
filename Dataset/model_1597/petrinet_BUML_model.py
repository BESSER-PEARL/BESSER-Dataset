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
Petrinet_Node = Class(name="Petrinet::Node", is_abstract=True)
Element = Class(name="Element")
Petrinet_Arc = Class(name="Petrinet::Arc", is_abstract=True)
Petrinet_Element = Class(name="Petrinet::Element", is_abstract=True)
Petrinet_Petrinet = Class(name="Petrinet::Petrinet")
Petrinet_OutputArc = Class(name="Petrinet::OutputArc")
Arc = Class(name="Arc")
Petrinet_Transition = Class(name="Petrinet::Transition")
Petrinet_Place = Class(name="Petrinet::Place")
Petrinet_InputArc = Class(name="Petrinet::InputArc")
Node = Class(name="Node")

# Petrinet_Node class attributes and methods

# Element class attributes and methods

# Petrinet_Arc class attributes and methods

# Petrinet_Element class attributes and methods
Petrinet_Element_name: Property = Property(name="name", type=StringType)
Petrinet_Element.attributes={Petrinet_Element_name}

# Petrinet_Petrinet class attributes and methods

# Petrinet_OutputArc class attributes and methods

# Arc class attributes and methods

# Petrinet_Transition class attributes and methods
Petrinet_Transition_maxDelay: Property = Property(name="maxDelay", type=FloatType)
Petrinet_Transition_minDelay: Property = Property(name="minDelay", type=FloatType)
Petrinet_Transition.attributes={Petrinet_Transition_maxDelay, Petrinet_Transition_minDelay}

# Petrinet_Place class attributes and methods

# Petrinet_InputArc class attributes and methods

# Node class attributes and methods

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="Petrinet_Element", type=Petrinet_Petrinet, multiplicity=Multiplicity(1, 1)),
        Property(name="Petrinet_Petrinet", type=Petrinet_Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
src1: BinaryAssociation = BinaryAssociation(
    name="src1",
    ends={
        Property(name="Petrinet_Transition", type=Petrinet_OutputArc, multiplicity=Multiplicity(1, 1)),
        Property(name="Petrinet_OutputArc", type=Petrinet_Transition, multiplicity=Multiplicity(1, 1))
    }
)
dest2: BinaryAssociation = BinaryAssociation(
    name="dest2",
    ends={
        Property(name="Petrinet_Place", type=Petrinet_OutputArc, multiplicity=Multiplicity(1, 1)),
        Property(name="Petrinet_OutputArc3", type=Petrinet_Place, multiplicity=Multiplicity(1, 1))
    }
)
dest4: BinaryAssociation = BinaryAssociation(
    name="dest4",
    ends={
        Property(name="Petrinet_Transition5", type=Petrinet_InputArc, multiplicity=Multiplicity(1, 1)),
        Property(name="Petrinet_InputArc", type=Petrinet_Transition, multiplicity=Multiplicity(1, 1))
    }
)
src6: BinaryAssociation = BinaryAssociation(
    name="src6",
    ends={
        Property(name="Petrinet_Place8", type=Petrinet_InputArc, multiplicity=Multiplicity(1, 1)),
        Property(name="Petrinet_InputArc7", type=Petrinet_Place, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_Petrinet_Node_Element = Generalization(general=Element, specific=Petrinet_Node)
gen_Petrinet_Place_Node = Generalization(general=Node, specific=Petrinet_Place)
gen_Petrinet_Arc_Element = Generalization(general=Element, specific=Petrinet_Arc)
gen_Petrinet_OutputArc_Arc = Generalization(general=Arc, specific=Petrinet_OutputArc)
gen_Petrinet_InputArc_Arc = Generalization(general=Arc, specific=Petrinet_InputArc)
gen_Petrinet_Transition_Node = Generalization(general=Node, specific=Petrinet_Transition)

# Domain Model
domain_model = DomainModel(
    name="Petrinet",
    types={Petrinet_Node, Element, Petrinet_Arc, Petrinet_Element, Petrinet_Petrinet, Petrinet_OutputArc, Arc, Petrinet_Transition, Petrinet_Place, Petrinet_InputArc, Node},
    associations={elements0, src1, dest2, dest4, src6},
    generalizations={gen_Petrinet_Node_Element, gen_Petrinet_Place_Node, gen_Petrinet_Arc_Element, gen_Petrinet_OutputArc_Arc, gen_Petrinet_InputArc_Arc, gen_Petrinet_Transition_Node},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)