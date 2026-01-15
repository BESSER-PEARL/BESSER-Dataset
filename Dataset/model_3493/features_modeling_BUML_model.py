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
Feature = Class(name="Feature")
features_modeling_Feature = Class(name="features::modeling::Feature")
features_modeling_F = Class(name="features::modeling::F")
features_modeling_G = Class(name="features::modeling::G")
features_modeling_R = Class(name="features::modeling::R")
features_modeling_E = Class(name="features::modeling::E")
features_modeling_EMAND = Class(name="features::modeling::EMAND")
E = Class(name="E")
features_modeling_GXOR = Class(name="features::modeling::GXOR")
Group = Class(name="Group")
features_modeling_GOR = Class(name="features::modeling::GOR")
features_modeling_Edge = Class(name="features::modeling::Edge")
features_modeling_Constraints = Class(name="features::modeling::Constraints")
features_modeling_PropFormulaCNF = Class(name="features::modeling::PropFormulaCNF")
features_modeling_PropositionOR = Class(name="features::modeling::PropositionOR")
features_modeling_I = Class(name="features::modeling::I")
Constraint = Class(name="Constraint")
features_modeling_EX = Class(name="features::modeling::EX")
features_modeling_Constraint = Class(name="features::modeling::Constraint", is_abstract=True)
features_modeling_Group = Class(name="features::modeling::Group", is_abstract=True)
features_modeling_AND = Class(name="features::modeling::AND")
features_modeling_NOT = Class(name="features::modeling::NOT")

# Feature class attributes and methods

# features_modeling_Feature class attributes and methods
features_modeling_Feature_ID: Property = Property(name="ID", type=StringType)
features_modeling_Feature.attributes={features_modeling_Feature_ID}

# features_modeling_F class attributes and methods

# features_modeling_G class attributes and methods

# features_modeling_R class attributes and methods

# features_modeling_E class attributes and methods

# features_modeling_EMAND class attributes and methods

# E class attributes and methods

# features_modeling_GXOR class attributes and methods

# Group class attributes and methods

# features_modeling_GOR class attributes and methods

# features_modeling_Edge class attributes and methods

# features_modeling_Constraints class attributes and methods

# features_modeling_PropFormulaCNF class attributes and methods

# features_modeling_PropositionOR class attributes and methods

# features_modeling_I class attributes and methods

# Constraint class attributes and methods

# features_modeling_EX class attributes and methods

# features_modeling_Constraint class attributes and methods

# features_modeling_Group class attributes and methods

# features_modeling_AND class attributes and methods

# features_modeling_NOT class attributes and methods

# Relationships
children2: BinaryAssociation = BinaryAssociation(
    name="children2",
    ends={
        Property(name="features_modeling_Feature", type=features_modeling_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="features_modeling_Feature1", type=features_modeling_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
r0: BinaryAssociation = BinaryAssociation(
    name="r0",
    ends={
        Property(name="features_modeling_R", type=features_modeling_G, multiplicity=Multiplicity(1, 1)),
        Property(name="features_modeling_G", type=features_modeling_R, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
edge10: BinaryAssociation = BinaryAssociation(
    name="edge10",
    ends={
        Property(name="features_modeling_Edge11", type=features_modeling_E, multiplicity=Multiplicity(1, 1)),
        Property(name="features_modeling_E", type=features_modeling_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
feature3: BinaryAssociation = BinaryAssociation(
    name="feature3",
    ends={
        Property(name="features_modeling_Feature4", type=features_modeling_F, multiplicity=Multiplicity(1, 1)),
        Property(name="features_modeling_F", type=features_modeling_Feature, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
r5: BinaryAssociation = BinaryAssociation(
    name="r5",
    ends={
        Property(name="features_modeling_R7", type=features_modeling_F, multiplicity=Multiplicity(1, 1)),
        Property(name="features_modeling_F6", type=features_modeling_R, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
feature8: BinaryAssociation = BinaryAssociation(
    name="feature8",
    ends={
        Property(name="features_modeling_Feature9", type=features_modeling_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="features_modeling_Edge", type=features_modeling_Feature, multiplicity=Multiplicity(2, 2), is_composite=True)
    }
)
feature14: BinaryAssociation = BinaryAssociation(
    name="feature14",
    ends={
        Property(name="features_modeling_Feature15", type=features_modeling_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="features_modeling_Group", type=features_modeling_Feature, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
constraint16: BinaryAssociation = BinaryAssociation(
    name="constraint16",
    ends={
        Property(name="features_modeling_Constraint17", type=features_modeling_Constraints, multiplicity=Multiplicity(1, 1)),
        Property(name="features_modeling_Constraints", type=features_modeling_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
proposition18: BinaryAssociation = BinaryAssociation(
    name="proposition18",
    ends={
        Property(name="features_modeling_PropositionOR", type=features_modeling_PropFormulaCNF, multiplicity=Multiplicity(1, 1)),
        Property(name="features_modeling_PropFormulaCNF", type=features_modeling_PropositionOR, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
feature12: BinaryAssociation = BinaryAssociation(
    name="feature12",
    ends={
        Property(name="features_modeling_Feature13", type=features_modeling_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="features_modeling_Constraint", type=features_modeling_Feature, multiplicity=Multiplicity(2, 2), is_composite=True)
    }
)
feature24: BinaryAssociation = BinaryAssociation(
    name="feature24",
    ends={
        Property(name="features_modeling_NOT25", type=features_modeling_Feature, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="features_modeling_Feature26", type=features_modeling_NOT, multiplicity=Multiplicity(1, 1))
    }
)
feature19: BinaryAssociation = BinaryAssociation(
    name="feature19",
    ends={
        Property(name="features_modeling_Feature21", type=features_modeling_PropositionOR, multiplicity=Multiplicity(1, 1)),
        Property(name="features_modeling_PropositionOR20", type=features_modeling_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
not22: BinaryAssociation = BinaryAssociation(
    name="not22",
    ends={
        Property(name="features_modeling_NOT", type=features_modeling_PropositionOR, multiplicity=Multiplicity(1, 1)),
        Property(name="features_modeling_PropositionOR23", type=features_modeling_NOT, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_features_modeling_R_Feature = Generalization(general=Feature, specific=features_modeling_R)
gen_features_modeling_EMAND_E = Generalization(general=E, specific=features_modeling_EMAND)
gen_features_modeling_GXOR_Group = Generalization(general=Group, specific=features_modeling_GXOR)
gen_features_modeling_GOR_Group = Generalization(general=Group, specific=features_modeling_GOR)
gen_features_modeling_I_Constraint = Generalization(general=Constraint, specific=features_modeling_I)
gen_features_modeling_EX_Constraint = Generalization(general=Constraint, specific=features_modeling_EX)

# Domain Model
domain_model = DomainModel(
    name="features_modeling",
    types={Feature, features_modeling_Feature, features_modeling_F, features_modeling_G, features_modeling_R, features_modeling_E, features_modeling_EMAND, E, features_modeling_GXOR, Group, features_modeling_GOR, features_modeling_Edge, features_modeling_Constraints, features_modeling_PropFormulaCNF, features_modeling_PropositionOR, features_modeling_I, Constraint, features_modeling_EX, features_modeling_Constraint, features_modeling_Group, features_modeling_AND, features_modeling_NOT},
    associations={children2, r0, edge10, feature3, r5, feature8, feature14, constraint16, proposition18, feature12, feature24, feature19, not22},
    generalizations={gen_features_modeling_R_Feature, gen_features_modeling_EMAND_E, gen_features_modeling_GXOR_Group, gen_features_modeling_GOR_Group, gen_features_modeling_I_Constraint, gen_features_modeling_EX_Constraint},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)