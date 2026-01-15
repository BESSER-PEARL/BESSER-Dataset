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
subsetUnion_Container = Class(name="subsetUnion::Container")
subsetUnion_Element = Class(name="subsetUnion::Element")
subsetUnion_Element_Level1 = Class(name="subsetUnion::Element::Level1")
subsetUnion_Element_Level2 = Class(name="subsetUnion::Element::Level2")
subsetUnion_Element_Level3 = Class(name="subsetUnion::Element::Level3")
subsetUnion_Element_Level4 = Class(name="subsetUnion::Element::Level4")
subsetUnion_Element_Level5 = Class(name="subsetUnion::Element::Level5")
subsetUnion_Element_Level6 = Class(name="subsetUnion::Element::Level6")
subsetUnion_Element_Level7 = Class(name="subsetUnion::Element::Level7")
subsetUnion_Element_Level8 = Class(name="subsetUnion::Element::Level8")
subsetUnion_Element_Level9 = Class(name="subsetUnion::Element::Level9")
subsetUnion_Element_Level10 = Class(name="subsetUnion::Element::Level10")
Element = Class(name="Element")

# subsetUnion_Container class attributes and methods
subsetUnion_Container_name: Property = Property(name="name", type=StringType)
subsetUnion_Container.attributes={subsetUnion_Container_name}

# subsetUnion_Element class attributes and methods
subsetUnion_Element_name: Property = Property(name="name", type=StringType)
subsetUnion_Element.attributes={subsetUnion_Element_name}

# subsetUnion_Element_Level1 class attributes and methods

# subsetUnion_Element_Level2 class attributes and methods

# subsetUnion_Element_Level3 class attributes and methods

# subsetUnion_Element_Level4 class attributes and methods

# subsetUnion_Element_Level5 class attributes and methods

# subsetUnion_Element_Level6 class attributes and methods

# subsetUnion_Element_Level7 class attributes and methods

# subsetUnion_Element_Level8 class attributes and methods

# subsetUnion_Element_Level9 class attributes and methods

# subsetUnion_Element_Level10 class attributes and methods

# Element class attributes and methods

# Relationships
unionBag0: BinaryAssociation = BinaryAssociation(
    name="unionBag0",
    ends={
        Property(name="subsetUnion_Element", type=subsetUnion_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="subsetUnion_Container", type=subsetUnion_Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subset11: BinaryAssociation = BinaryAssociation(
    name="subset11",
    ends={
        Property(name="subsetUnion_Element_Level1", type=subsetUnion_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="subsetUnion_Container2", type=subsetUnion_Element_Level1, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subset23: BinaryAssociation = BinaryAssociation(
    name="subset23",
    ends={
        Property(name="subsetUnion_Element_Level2", type=subsetUnion_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="subsetUnion_Container4", type=subsetUnion_Element_Level2, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subset35: BinaryAssociation = BinaryAssociation(
    name="subset35",
    ends={
        Property(name="subsetUnion_Element_Level3", type=subsetUnion_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="subsetUnion_Container6", type=subsetUnion_Element_Level3, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subset47: BinaryAssociation = BinaryAssociation(
    name="subset47",
    ends={
        Property(name="subsetUnion_Element_Level4", type=subsetUnion_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="subsetUnion_Container8", type=subsetUnion_Element_Level4, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subset59: BinaryAssociation = BinaryAssociation(
    name="subset59",
    ends={
        Property(name="subsetUnion_Element_Level5", type=subsetUnion_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="subsetUnion_Container10", type=subsetUnion_Element_Level5, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subset611: BinaryAssociation = BinaryAssociation(
    name="subset611",
    ends={
        Property(name="subsetUnion_Element_Level6", type=subsetUnion_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="subsetUnion_Container12", type=subsetUnion_Element_Level6, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subset713: BinaryAssociation = BinaryAssociation(
    name="subset713",
    ends={
        Property(name="subsetUnion_Element_Level7", type=subsetUnion_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="subsetUnion_Container14", type=subsetUnion_Element_Level7, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subset815: BinaryAssociation = BinaryAssociation(
    name="subset815",
    ends={
        Property(name="subsetUnion_Element_Level8", type=subsetUnion_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="subsetUnion_Container16", type=subsetUnion_Element_Level8, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subset917: BinaryAssociation = BinaryAssociation(
    name="subset917",
    ends={
        Property(name="subsetUnion_Element_Level9", type=subsetUnion_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="subsetUnion_Container18", type=subsetUnion_Element_Level9, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subset1019: BinaryAssociation = BinaryAssociation(
    name="subset1019",
    ends={
        Property(name="subsetUnion_Element_Level10", type=subsetUnion_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="subsetUnion_Container20", type=subsetUnion_Element_Level10, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_subsetUnion_Element_Level1_Element = Generalization(general=Element, specific=subsetUnion_Element_Level1)
gen_subsetUnion_Element_Level2_Element = Generalization(general=Element, specific=subsetUnion_Element_Level2)
gen_subsetUnion_Element_Level3_Element = Generalization(general=Element, specific=subsetUnion_Element_Level3)
gen_subsetUnion_Element_Level4_Element = Generalization(general=Element, specific=subsetUnion_Element_Level4)
gen_subsetUnion_Element_Level5_Element = Generalization(general=Element, specific=subsetUnion_Element_Level5)
gen_subsetUnion_Element_Level6_Element = Generalization(general=Element, specific=subsetUnion_Element_Level6)
gen_subsetUnion_Element_Level7_Element = Generalization(general=Element, specific=subsetUnion_Element_Level7)
gen_subsetUnion_Element_Level8_Element = Generalization(general=Element, specific=subsetUnion_Element_Level8)
gen_subsetUnion_Element_Level9_Element = Generalization(general=Element, specific=subsetUnion_Element_Level9)
gen_subsetUnion_Element_Level10_Element = Generalization(general=Element, specific=subsetUnion_Element_Level10)

# Domain Model
domain_model = DomainModel(
    name="subsetUnion",
    types={subsetUnion_Container, subsetUnion_Element, subsetUnion_Element_Level1, subsetUnion_Element_Level2, subsetUnion_Element_Level3, subsetUnion_Element_Level4, subsetUnion_Element_Level5, subsetUnion_Element_Level6, subsetUnion_Element_Level7, subsetUnion_Element_Level8, subsetUnion_Element_Level9, subsetUnion_Element_Level10, Element},
    associations={unionBag0, subset11, subset23, subset35, subset47, subset59, subset611, subset713, subset815, subset917, subset1019},
    generalizations={gen_subsetUnion_Element_Level1_Element, gen_subsetUnion_Element_Level2_Element, gen_subsetUnion_Element_Level3_Element, gen_subsetUnion_Element_Level4_Element, gen_subsetUnion_Element_Level5_Element, gen_subsetUnion_Element_Level6_Element, gen_subsetUnion_Element_Level7_Element, gen_subsetUnion_Element_Level8_Element, gen_subsetUnion_Element_Level9_Element, gen_subsetUnion_Element_Level10_Element},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)