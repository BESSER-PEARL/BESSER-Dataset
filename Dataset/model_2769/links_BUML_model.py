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
links_ChildNodeA = Class(name="links::ChildNodeA")
links_ChildNodeB = Class(name="links::ChildNodeB")
links_Root = Class(name="links::Root")
links_Child_AB_Element_Link = Class(name="links::Child::AB::Element::Link")
links_RootNodeA = Class(name="links::RootNodeA")
links_RootNodeB = Class(name="links::RootNodeB")
links_Root_BA_Element_Link = Class(name="links::Root::BA::Element::Link")

# links_ChildNodeA class attributes and methods

# links_ChildNodeB class attributes and methods

# links_Root class attributes and methods

# links_Child_AB_Element_Link class attributes and methods

# links_RootNodeA class attributes and methods

# links_RootNodeB class attributes and methods

# links_Root_BA_Element_Link class attributes and methods
links_Root_BA_Element_Link_name: Property = Property(name="name", type=StringType)
links_Root_BA_Element_Link.attributes={links_Root_BA_Element_Link_name}

# Relationships
ChildrenNodeA7: BinaryAssociation = BinaryAssociation(
    name="ChildrenNodeA7",
    ends={
        Property(name="links_ChildNodeA", type=links_RootNodeA, multiplicity=Multiplicity(1, 1)),
        Property(name="links_RootNodeA8", type=links_ChildNodeA, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ChildrenB9: BinaryAssociation = BinaryAssociation(
    name="ChildrenB9",
    ends={
        Property(name="links_ChildNodeB", type=links_RootNodeB, multiplicity=Multiplicity(1, 1)),
        Property(name="links_RootNodeB10", type=links_ChildNodeB, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Root_BA_Feature_Link11: BinaryAssociation = BinaryAssociation(
    name="Root_BA_Feature_Link11",
    ends={
        Property(name="links_RootNodeA13", type=links_RootNodeB, multiplicity=Multiplicity(1, 1)),
        Property(name="links_RootNodeB12", type=links_RootNodeA, multiplicity=Multiplicity(0, 9999))
    }
)
Child_AB_Feature_Link14: BinaryAssociation = BinaryAssociation(
    name="Child_AB_Feature_Link14",
    ends={
        Property(name="links_ChildNodeB16", type=links_ChildNodeA, multiplicity=Multiplicity(1, 1)),
        Property(name="links_ChildNodeA15", type=links_ChildNodeB, multiplicity=Multiplicity(0, 9999))
    }
)
childABElementLinks0: BinaryAssociation = BinaryAssociation(
    name="childABElementLinks0",
    ends={
        Property(name="links_Child_AB_Element_Link", type=links_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="links_Root", type=links_Child_AB_Element_Link, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rootNodeAs1: BinaryAssociation = BinaryAssociation(
    name="rootNodeAs1",
    ends={
        Property(name="links_RootNodeA", type=links_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="links_Root2", type=links_RootNodeA, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rootNodeBs3: BinaryAssociation = BinaryAssociation(
    name="rootNodeBs3",
    ends={
        Property(name="links_RootNodeB", type=links_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="links_Root4", type=links_RootNodeB, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rootBALinks5: BinaryAssociation = BinaryAssociation(
    name="rootBALinks5",
    ends={
        Property(name="links_Root_BA_Element_Link", type=links_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="links_Root6", type=links_Root_BA_Element_Link, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source_A17: BinaryAssociation = BinaryAssociation(
    name="source_A17",
    ends={
        Property(name="links_ChildNodeA19", type=links_Child_AB_Element_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="links_Child_AB_Element_Link18", type=links_ChildNodeA, multiplicity=Multiplicity(0, 1))
    }
)
target_B20: BinaryAssociation = BinaryAssociation(
    name="target_B20",
    ends={
        Property(name="links_ChildNodeB22", type=links_Child_AB_Element_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="links_Child_AB_Element_Link21", type=links_ChildNodeB, multiplicity=Multiplicity(0, 1))
    }
)
b23: BinaryAssociation = BinaryAssociation(
    name="b23",
    ends={
        Property(name="links_RootNodeB25", type=links_Root_BA_Element_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="links_Root_BA_Element_Link24", type=links_RootNodeB, multiplicity=Multiplicity(0, 1))
    }
)
a26: BinaryAssociation = BinaryAssociation(
    name="a26",
    ends={
        Property(name="links_RootNodeA28", type=links_Root_BA_Element_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="links_Root_BA_Element_Link27", type=links_RootNodeA, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="links",
    types={links_ChildNodeA, links_ChildNodeB, links_Root, links_Child_AB_Element_Link, links_RootNodeA, links_RootNodeB, links_Root_BA_Element_Link},
    associations={ChildrenNodeA7, ChildrenB9, Root_BA_Feature_Link11, Child_AB_Feature_Link14, childABElementLinks0, rootNodeAs1, rootNodeBs3, rootBALinks5, source_A17, target_B20, b23, a26},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)