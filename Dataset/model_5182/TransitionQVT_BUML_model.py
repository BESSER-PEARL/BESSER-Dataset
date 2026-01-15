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
TransitionQVT_A = Class(name="TransitionQVT::A")
Element = Class(name="Element")
TransitionQVT_B = Class(name="TransitionQVT::B")
TransitionQVT_C = Class(name="TransitionQVT::C")
TransitionQVT_Root = Class(name="TransitionQVT::Root")
TransitionQVT_Element = Class(name="TransitionQVT::Element", is_abstract=True)

# TransitionQVT_A class attributes and methods
TransitionQVT_A_height: Property = Property(name="height", type=FloatType)
TransitionQVT_A_reduction: Property = Property(name="reduction", type=StringType)
TransitionQVT_A.attributes={TransitionQVT_A_height, TransitionQVT_A_reduction}

# Element class attributes and methods

# TransitionQVT_B class attributes and methods
TransitionQVT_B_boss: Property = Property(name="boss", type=StringType)
TransitionQVT_B.attributes={TransitionQVT_B_boss}

# TransitionQVT_C class attributes and methods
TransitionQVT_C_c: Property = Property(name="c", type=StringType)
TransitionQVT_C.attributes={TransitionQVT_C_c}

# TransitionQVT_Root class attributes and methods

# TransitionQVT_Element class attributes and methods
TransitionQVT_Element_id: Property = Property(name="id", type=IntegerType)
TransitionQVT_Element.attributes={TransitionQVT_Element_id}

# Relationships
abc2: BinaryAssociation = BinaryAssociation(
    name="abc2",
    ends={
        Property(name="TransitionQVT_Element3", type=TransitionQVT_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="TransitionQVT_Element1", type=TransitionQVT_Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
element0: BinaryAssociation = BinaryAssociation(
    name="element0",
    ends={
        Property(name="TransitionQVT_Element", type=TransitionQVT_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="TransitionQVT_Root", type=TransitionQVT_Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_TransitionQVT_A_Element = Generalization(general=Element, specific=TransitionQVT_A)
gen_TransitionQVT_B_Element = Generalization(general=Element, specific=TransitionQVT_B)
gen_TransitionQVT_C_Element = Generalization(general=Element, specific=TransitionQVT_C)

# Domain Model
domain_model = DomainModel(
    name="TransitionQVT",
    types={TransitionQVT_A, Element, TransitionQVT_B, TransitionQVT_C, TransitionQVT_Root, TransitionQVT_Element},
    associations={abc2, element0},
    generalizations={gen_TransitionQVT_A_Element, gen_TransitionQVT_B_Element, gen_TransitionQVT_C_Element},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)