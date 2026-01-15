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
kwas_Top = Class(name="kwas::Top")
kwas_Tree = Class(name="kwas::Tree", is_abstract=True)
kwas_Bin = Class(name="kwas::Bin")
Tree = Class(name="Tree")
kwas_Leaf = Class(name="kwas::Leaf")

# kwas_Top class attributes and methods

# kwas_Tree class attributes and methods
kwas_Tree_labelS: Property = Property(name="labelS", type=StringType)
kwas_Tree_labelI: Property = Property(name="labelI", type=StringType)
kwas_Tree_valsI: Property = Property(name="valsI", type=IntegerType)
kwas_Tree_valsS: Property = Property(name="valsS", type=IntegerType)
kwas_Tree.attributes={kwas_Tree_valsI, kwas_Tree_labelS, kwas_Tree_valsS, kwas_Tree_labelI}

# kwas_Bin class attributes and methods

# Tree class attributes and methods

# kwas_Leaf class attributes and methods
kwas_Leaf_val: Property = Property(name="val", type=IntegerType)
kwas_Leaf.attributes={kwas_Leaf_val}

# Relationships
node0: BinaryAssociation = BinaryAssociation(
    name="node0",
    ends={
        Property(name="kwas_Tree", type=kwas_Top, multiplicity=Multiplicity(1, 1)),
        Property(name="kwas_Top", type=kwas_Tree, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
left1: BinaryAssociation = BinaryAssociation(
    name="left1",
    ends={
        Property(name="kwas_Tree2", type=kwas_Bin, multiplicity=Multiplicity(1, 1)),
        Property(name="kwas_Bin", type=kwas_Tree, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right3: BinaryAssociation = BinaryAssociation(
    name="right3",
    ends={
        Property(name="kwas_Tree5", type=kwas_Bin, multiplicity=Multiplicity(1, 1)),
        Property(name="kwas_Bin4", type=kwas_Tree, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_kwas_Bin_Tree = Generalization(general=Tree, specific=kwas_Bin)
gen_kwas_Leaf_Tree = Generalization(general=Tree, specific=kwas_Leaf)

# Domain Model
domain_model = DomainModel(
    name="kwas",
    types={kwas_Top, kwas_Tree, kwas_Bin, Tree, kwas_Leaf},
    associations={node0, left1, right3},
    generalizations={gen_kwas_Bin_Tree, gen_kwas_Leaf_Tree},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)