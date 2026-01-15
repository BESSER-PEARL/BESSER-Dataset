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
petrinet2_Node = Class(name="petrinet2::Node", is_abstract=True)
Element = Class(name="Element")
petrinet2_Place = Class(name="petrinet2::Place")
Node = Class(name="Node")
petrinet2_Transition = Class(name="petrinet2::Transition")
petrinet2_Petrinet = Class(name="petrinet2::Petrinet")
petrinet2_Element = Class(name="petrinet2::Element", is_abstract=True)
petrinet2_Arc = Class(name="petrinet2::Arc")

# petrinet2_Node class attributes and methods

# Element class attributes and methods

# petrinet2_Place class attributes and methods

# Node class attributes and methods

# petrinet2_Transition class attributes and methods
petrinet2_Transition_maxDelay: Property = Property(name="maxDelay", type=FloatType)
petrinet2_Transition_minDelay: Property = Property(name="minDelay", type=FloatType)
petrinet2_Transition.attributes={petrinet2_Transition_minDelay, petrinet2_Transition_maxDelay}

# petrinet2_Petrinet class attributes and methods

# petrinet2_Element class attributes and methods
petrinet2_Element_name: Property = Property(name="name", type=StringType)
petrinet2_Element.attributes={petrinet2_Element_name}

# petrinet2_Arc class attributes and methods

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="petrinet2_Element", type=petrinet2_Petrinet, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet2_Petrinet", type=petrinet2_Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
To1: BinaryAssociation = BinaryAssociation(
    name="To1",
    ends={
        Property(name="petrinet2_Node", type=petrinet2_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet2_Arc", type=petrinet2_Node, multiplicity=Multiplicity(1, 1))
    }
)
From2: BinaryAssociation = BinaryAssociation(
    name="From2",
    ends={
        Property(name="petrinet2_Node4", type=petrinet2_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet2_Arc3", type=petrinet2_Node, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_petrinet2_Node_Element = Generalization(general=Element, specific=petrinet2_Node)
gen_petrinet2_Place_Node = Generalization(general=Node, specific=petrinet2_Place)
gen_petrinet2_Transition_Node = Generalization(general=Node, specific=petrinet2_Transition)
gen_petrinet2_Arc_Element = Generalization(general=Element, specific=petrinet2_Arc)

# Domain Model
domain_model = DomainModel(
    name="petrinet2",
    types={petrinet2_Node, Element, petrinet2_Place, Node, petrinet2_Transition, petrinet2_Petrinet, petrinet2_Element, petrinet2_Arc},
    associations={elements0, To1, From2},
    generalizations={gen_petrinet2_Node_Element, gen_petrinet2_Place_Node, gen_petrinet2_Transition_Node, gen_petrinet2_Arc_Element},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)