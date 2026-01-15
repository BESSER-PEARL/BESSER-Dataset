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
ABC_Root = Class(name="ABC::Root")
ABC_Element = Class(name="ABC::Element", is_abstract=True)
ABC_A = Class(name="ABC::A")
Element = Class(name="Element")
ABC_B = Class(name="ABC::B")
ABC_C = Class(name="ABC::C")

# ABC_Root class attributes and methods

# ABC_Element class attributes and methods
ABC_Element_id: Property = Property(name="id", type=IntegerType)
ABC_Element.attributes={ABC_Element_id}

# ABC_A class attributes and methods
ABC_A_a: Property = Property(name="a", type=StringType)
ABC_A.attributes={ABC_A_a}

# Element class attributes and methods

# ABC_B class attributes and methods
ABC_B_b: Property = Property(name="b", type=StringType)
ABC_B.attributes={ABC_B_b}

# ABC_C class attributes and methods
ABC_C_c: Property = Property(name="c", type=StringType)
ABC_C.attributes={ABC_C_c}

# Relationships
element0: BinaryAssociation = BinaryAssociation(
    name="element0",
    ends={
        Property(name="ABC_Element", type=ABC_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="ABC_Root", type=ABC_Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
abc2: BinaryAssociation = BinaryAssociation(
    name="abc2",
    ends={
        Property(name="ABC_Element3", type=ABC_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="ABC_Element1", type=ABC_Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_ABC_A_Element = Generalization(general=Element, specific=ABC_A)
gen_ABC_B_Element = Generalization(general=Element, specific=ABC_B)
gen_ABC_C_Element = Generalization(general=Element, specific=ABC_C)

# Domain Model
domain_model = DomainModel(
    name="ABC",
    types={ABC_Root, ABC_Element, ABC_A, Element, ABC_B, ABC_C},
    associations={element0, abc2},
    generalizations={gen_ABC_A_Element, gen_ABC_B_Element, gen_ABC_C_Element},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)