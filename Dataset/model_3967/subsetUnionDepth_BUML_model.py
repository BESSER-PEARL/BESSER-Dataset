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
subsetUnionDepth_Container = Class(name="subsetUnionDepth::Container")
subsetUnionDepth_Element = Class(name="subsetUnionDepth::Element")
subsetUnionDepth_Element_Level1 = Class(name="subsetUnionDepth::Element::Level1")
Element = Class(name="Element")
subsetUnionDepth_Container_Level1 = Class(name="subsetUnionDepth::Container::Level1")
Container = Class(name="Container")
subsetUnionDepth_Element_Level2 = Class(name="subsetUnionDepth::Element::Level2")
Element_Level1 = Class(name="Element::Level1")
subsetUnionDepth_Container_Level2 = Class(name="subsetUnionDepth::Container::Level2")
Container_Level1 = Class(name="Container::Level1")
subsetUnionDepth_Element_Level3 = Class(name="subsetUnionDepth::Element::Level3")
Element_Level2 = Class(name="Element::Level2")
subsetUnionDepth_Container_Level3 = Class(name="subsetUnionDepth::Container::Level3")
Container_Level2 = Class(name="Container::Level2")
subsetUnionDepth_Element_Level4 = Class(name="subsetUnionDepth::Element::Level4")
Element_Level3 = Class(name="Element::Level3")
subsetUnionDepth_Container_Level4 = Class(name="subsetUnionDepth::Container::Level4")
Container_Level3 = Class(name="Container::Level3")
subsetUnionDepth_Container_Level5 = Class(name="subsetUnionDepth::Container::Level5")
Container_Level4 = Class(name="Container::Level4")
subsetUnionDepth_Element_Level5 = Class(name="subsetUnionDepth::Element::Level5")
Element_Level4 = Class(name="Element::Level4")
subsetUnionDepth_Element_Level6 = Class(name="subsetUnionDepth::Element::Level6")
Element_Level5 = Class(name="Element::Level5")
subsetUnionDepth_Container_Level6 = Class(name="subsetUnionDepth::Container::Level6")
Container_Level5 = Class(name="Container::Level5")
subsetUnionDepth_Element_Level7 = Class(name="subsetUnionDepth::Element::Level7")
Element_Level6 = Class(name="Element::Level6")
subsetUnionDepth_Container_Level7 = Class(name="subsetUnionDepth::Container::Level7")
Container_Level6 = Class(name="Container::Level6")
subsetUnionDepth_Container_Level8 = Class(name="subsetUnionDepth::Container::Level8")
Container_Level7 = Class(name="Container::Level7")
subsetUnionDepth_Element_Level8 = Class(name="subsetUnionDepth::Element::Level8")
Element_Level7 = Class(name="Element::Level7")
subsetUnionDepth_Element_Level9 = Class(name="subsetUnionDepth::Element::Level9")
Element_Level8 = Class(name="Element::Level8")
subsetUnionDepth_Container_Level9 = Class(name="subsetUnionDepth::Container::Level9")
Container_Level8 = Class(name="Container::Level8")
subsetUnionDepth_Element_Level10 = Class(name="subsetUnionDepth::Element::Level10")
Element_Level9 = Class(name="Element::Level9")
subsetUnionDepth_Container_Level10 = Class(name="subsetUnionDepth::Container::Level10")
Container_Level9 = Class(name="Container::Level9")

# subsetUnionDepth_Container class attributes and methods
subsetUnionDepth_Container_name: Property = Property(name="name", type=StringType)
subsetUnionDepth_Container.attributes={subsetUnionDepth_Container_name}

# subsetUnionDepth_Element class attributes and methods
subsetUnionDepth_Element_name: Property = Property(name="name", type=StringType)
subsetUnionDepth_Element.attributes={subsetUnionDepth_Element_name}

# subsetUnionDepth_Element_Level1 class attributes and methods

# Element class attributes and methods

# subsetUnionDepth_Container_Level1 class attributes and methods

# Container class attributes and methods

# subsetUnionDepth_Element_Level2 class attributes and methods

# Element_Level1 class attributes and methods

# subsetUnionDepth_Container_Level2 class attributes and methods

# Container_Level1 class attributes and methods

# subsetUnionDepth_Element_Level3 class attributes and methods

# Element_Level2 class attributes and methods

# subsetUnionDepth_Container_Level3 class attributes and methods

# Container_Level2 class attributes and methods

# subsetUnionDepth_Element_Level4 class attributes and methods

# Element_Level3 class attributes and methods

# subsetUnionDepth_Container_Level4 class attributes and methods

# Container_Level3 class attributes and methods

# subsetUnionDepth_Container_Level5 class attributes and methods

# Container_Level4 class attributes and methods

# subsetUnionDepth_Element_Level5 class attributes and methods

# Element_Level4 class attributes and methods

# subsetUnionDepth_Element_Level6 class attributes and methods

# Element_Level5 class attributes and methods

# subsetUnionDepth_Container_Level6 class attributes and methods

# Container_Level5 class attributes and methods

# subsetUnionDepth_Element_Level7 class attributes and methods

# Element_Level6 class attributes and methods

# subsetUnionDepth_Container_Level7 class attributes and methods

# Container_Level6 class attributes and methods

# subsetUnionDepth_Container_Level8 class attributes and methods

# Container_Level7 class attributes and methods

# subsetUnionDepth_Element_Level8 class attributes and methods

# Element_Level7 class attributes and methods

# subsetUnionDepth_Element_Level9 class attributes and methods

# Element_Level8 class attributes and methods

# subsetUnionDepth_Container_Level9 class attributes and methods

# Container_Level8 class attributes and methods

# subsetUnionDepth_Element_Level10 class attributes and methods

# Element_Level9 class attributes and methods

# subsetUnionDepth_Container_Level10 class attributes and methods

# Container_Level9 class attributes and methods

# Relationships
unionBag0: BinaryAssociation = BinaryAssociation(
    name="unionBag0",
    ends={
        Property(name="subsetUnionDepth_Element", type=subsetUnionDepth_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="subsetUnionDepth_Container", type=subsetUnionDepth_Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subset11: BinaryAssociation = BinaryAssociation(
    name="subset11",
    ends={
        Property(name="subsetUnionDepth_Element_Level1", type=subsetUnionDepth_Container_Level1, multiplicity=Multiplicity(1, 1)),
        Property(name="subsetUnionDepth_Container_Level1", type=subsetUnionDepth_Element_Level1, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subset22: BinaryAssociation = BinaryAssociation(
    name="subset22",
    ends={
        Property(name="subsetUnionDepth_Element_Level2", type=subsetUnionDepth_Container_Level2, multiplicity=Multiplicity(1, 1)),
        Property(name="subsetUnionDepth_Container_Level2", type=subsetUnionDepth_Element_Level2, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subset33: BinaryAssociation = BinaryAssociation(
    name="subset33",
    ends={
        Property(name="subsetUnionDepth_Element_Level3", type=subsetUnionDepth_Container_Level3, multiplicity=Multiplicity(1, 1)),
        Property(name="subsetUnionDepth_Container_Level3", type=subsetUnionDepth_Element_Level3, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subset44: BinaryAssociation = BinaryAssociation(
    name="subset44",
    ends={
        Property(name="subsetUnionDepth_Element_Level4", type=subsetUnionDepth_Container_Level4, multiplicity=Multiplicity(1, 1)),
        Property(name="subsetUnionDepth_Container_Level4", type=subsetUnionDepth_Element_Level4, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subset55: BinaryAssociation = BinaryAssociation(
    name="subset55",
    ends={
        Property(name="subsetUnionDepth_Element_Level5", type=subsetUnionDepth_Container_Level5, multiplicity=Multiplicity(1, 1)),
        Property(name="subsetUnionDepth_Container_Level5", type=subsetUnionDepth_Element_Level5, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subset66: BinaryAssociation = BinaryAssociation(
    name="subset66",
    ends={
        Property(name="subsetUnionDepth_Element_Level6", type=subsetUnionDepth_Container_Level6, multiplicity=Multiplicity(1, 1)),
        Property(name="subsetUnionDepth_Container_Level6", type=subsetUnionDepth_Element_Level6, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subset77: BinaryAssociation = BinaryAssociation(
    name="subset77",
    ends={
        Property(name="subsetUnionDepth_Element_Level7", type=subsetUnionDepth_Container_Level7, multiplicity=Multiplicity(1, 1)),
        Property(name="subsetUnionDepth_Container_Level7", type=subsetUnionDepth_Element_Level7, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subset88: BinaryAssociation = BinaryAssociation(
    name="subset88",
    ends={
        Property(name="subsetUnionDepth_Element_Level8", type=subsetUnionDepth_Container_Level8, multiplicity=Multiplicity(1, 1)),
        Property(name="subsetUnionDepth_Container_Level8", type=subsetUnionDepth_Element_Level8, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subset99: BinaryAssociation = BinaryAssociation(
    name="subset99",
    ends={
        Property(name="subsetUnionDepth_Element_Level9", type=subsetUnionDepth_Container_Level9, multiplicity=Multiplicity(1, 1)),
        Property(name="subsetUnionDepth_Container_Level9", type=subsetUnionDepth_Element_Level9, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subset1010: BinaryAssociation = BinaryAssociation(
    name="subset1010",
    ends={
        Property(name="subsetUnionDepth_Element_Level10", type=subsetUnionDepth_Container_Level10, multiplicity=Multiplicity(1, 1)),
        Property(name="subsetUnionDepth_Container_Level10", type=subsetUnionDepth_Element_Level10, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_subsetUnionDepth_Element_Level1_Element = Generalization(general=Element, specific=subsetUnionDepth_Element_Level1)
gen_subsetUnionDepth_Container_Level1_Container = Generalization(general=Container, specific=subsetUnionDepth_Container_Level1)
gen_subsetUnionDepth_Element_Level2_Element_Level1 = Generalization(general=Element_Level1, specific=subsetUnionDepth_Element_Level2)
gen_subsetUnionDepth_Container_Level2_Container_Level1 = Generalization(general=Container_Level1, specific=subsetUnionDepth_Container_Level2)
gen_subsetUnionDepth_Element_Level3_Element_Level2 = Generalization(general=Element_Level2, specific=subsetUnionDepth_Element_Level3)
gen_subsetUnionDepth_Container_Level3_Container_Level2 = Generalization(general=Container_Level2, specific=subsetUnionDepth_Container_Level3)
gen_subsetUnionDepth_Element_Level4_Element_Level3 = Generalization(general=Element_Level3, specific=subsetUnionDepth_Element_Level4)
gen_subsetUnionDepth_Container_Level4_Container_Level3 = Generalization(general=Container_Level3, specific=subsetUnionDepth_Container_Level4)
gen_subsetUnionDepth_Container_Level5_Container_Level4 = Generalization(general=Container_Level4, specific=subsetUnionDepth_Container_Level5)
gen_subsetUnionDepth_Element_Level5_Element_Level4 = Generalization(general=Element_Level4, specific=subsetUnionDepth_Element_Level5)
gen_subsetUnionDepth_Element_Level6_Element_Level5 = Generalization(general=Element_Level5, specific=subsetUnionDepth_Element_Level6)
gen_subsetUnionDepth_Container_Level6_Container_Level5 = Generalization(general=Container_Level5, specific=subsetUnionDepth_Container_Level6)
gen_subsetUnionDepth_Element_Level7_Element_Level6 = Generalization(general=Element_Level6, specific=subsetUnionDepth_Element_Level7)
gen_subsetUnionDepth_Container_Level7_Container_Level6 = Generalization(general=Container_Level6, specific=subsetUnionDepth_Container_Level7)
gen_subsetUnionDepth_Container_Level8_Container_Level7 = Generalization(general=Container_Level7, specific=subsetUnionDepth_Container_Level8)
gen_subsetUnionDepth_Element_Level8_Element_Level7 = Generalization(general=Element_Level7, specific=subsetUnionDepth_Element_Level8)
gen_subsetUnionDepth_Element_Level9_Element_Level8 = Generalization(general=Element_Level8, specific=subsetUnionDepth_Element_Level9)
gen_subsetUnionDepth_Container_Level9_Container_Level8 = Generalization(general=Container_Level8, specific=subsetUnionDepth_Container_Level9)
gen_subsetUnionDepth_Element_Level10_Element_Level9 = Generalization(general=Element_Level9, specific=subsetUnionDepth_Element_Level10)
gen_subsetUnionDepth_Container_Level10_Container_Level9 = Generalization(general=Container_Level9, specific=subsetUnionDepth_Container_Level10)

# Domain Model
domain_model = DomainModel(
    name="subsetUnionDepth",
    types={subsetUnionDepth_Container, subsetUnionDepth_Element, subsetUnionDepth_Element_Level1, Element, subsetUnionDepth_Container_Level1, Container, subsetUnionDepth_Element_Level2, Element_Level1, subsetUnionDepth_Container_Level2, Container_Level1, subsetUnionDepth_Element_Level3, Element_Level2, subsetUnionDepth_Container_Level3, Container_Level2, subsetUnionDepth_Element_Level4, Element_Level3, subsetUnionDepth_Container_Level4, Container_Level3, subsetUnionDepth_Container_Level5, Container_Level4, subsetUnionDepth_Element_Level5, Element_Level4, subsetUnionDepth_Element_Level6, Element_Level5, subsetUnionDepth_Container_Level6, Container_Level5, subsetUnionDepth_Element_Level7, Element_Level6, subsetUnionDepth_Container_Level7, Container_Level6, subsetUnionDepth_Container_Level8, Container_Level7, subsetUnionDepth_Element_Level8, Element_Level7, subsetUnionDepth_Element_Level9, Element_Level8, subsetUnionDepth_Container_Level9, Container_Level8, subsetUnionDepth_Element_Level10, Element_Level9, subsetUnionDepth_Container_Level10, Container_Level9},
    associations={unionBag0, subset11, subset22, subset33, subset44, subset55, subset66, subset77, subset88, subset99, subset1010},
    generalizations={gen_subsetUnionDepth_Element_Level1_Element, gen_subsetUnionDepth_Container_Level1_Container, gen_subsetUnionDepth_Element_Level2_Element_Level1, gen_subsetUnionDepth_Container_Level2_Container_Level1, gen_subsetUnionDepth_Element_Level3_Element_Level2, gen_subsetUnionDepth_Container_Level3_Container_Level2, gen_subsetUnionDepth_Element_Level4_Element_Level3, gen_subsetUnionDepth_Container_Level4_Container_Level3, gen_subsetUnionDepth_Container_Level5_Container_Level4, gen_subsetUnionDepth_Element_Level5_Element_Level4, gen_subsetUnionDepth_Element_Level6_Element_Level5, gen_subsetUnionDepth_Container_Level6_Container_Level5, gen_subsetUnionDepth_Element_Level7_Element_Level6, gen_subsetUnionDepth_Container_Level7_Container_Level6, gen_subsetUnionDepth_Container_Level8_Container_Level7, gen_subsetUnionDepth_Element_Level8_Element_Level7, gen_subsetUnionDepth_Element_Level9_Element_Level8, gen_subsetUnionDepth_Container_Level9_Container_Level8, gen_subsetUnionDepth_Element_Level10_Element_Level9, gen_subsetUnionDepth_Container_Level10_Container_Level9},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)