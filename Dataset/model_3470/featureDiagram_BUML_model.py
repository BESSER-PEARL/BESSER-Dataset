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
featureDiagram_ConstraintEdge = Class(name="featureDiagram::ConstraintEdge")
featureDiagram_FeatureDiagram = Class(name="featureDiagram::FeatureDiagram")
featureDiagram_Feature = Class(name="featureDiagram::Feature")
featureDiagram_Constraint = Class(name="featureDiagram::Constraint", is_abstract=True)
featureDiagram_Operator = Class(name="featureDiagram::Operator", is_abstract=True)
featureDiagram_Model = Class(name="featureDiagram::Model")
featureDiagram_PrimitiveFeature = Class(name="featureDiagram::PrimitiveFeature")
Feature = Class(name="Feature")
featureDiagram_Opt = Class(name="featureDiagram::Opt")
Operator = Class(name="Operator")
featureDiagram_And = Class(name="featureDiagram::And")
featureDiagram_Or = Class(name="featureDiagram::Or")
featureDiagram_Xor = Class(name="featureDiagram::Xor")
featureDiagram_Card = Class(name="featureDiagram::Card")
featureDiagram_Require = Class(name="featureDiagram::Require")
Constraint = Class(name="Constraint")
featureDiagram_Mutex = Class(name="featureDiagram::Mutex")

# featureDiagram_ConstraintEdge class attributes and methods

# featureDiagram_FeatureDiagram class attributes and methods
featureDiagram_FeatureDiagram_graphTypeTree: Property = Property(name="graphTypeTree", type=StringType)
featureDiagram_FeatureDiagram.attributes={featureDiagram_FeatureDiagram_graphTypeTree}

# featureDiagram_Feature class attributes and methods
featureDiagram_Feature_name: Property = Property(name="name", type=StringType)
featureDiagram_Feature_selected: Property = Property(name="selected", type=StringType)
featureDiagram_Feature_optional: Property = Property(name="optional", type=StringType)
featureDiagram_Feature.attributes={featureDiagram_Feature_selected, featureDiagram_Feature_optional, featureDiagram_Feature_name}

# featureDiagram_Constraint class attributes and methods

# featureDiagram_Operator class attributes and methods

# featureDiagram_Model class attributes and methods
featureDiagram_Model_name: Property = Property(name="name", type=StringType)
featureDiagram_Model.attributes={featureDiagram_Model_name}

# featureDiagram_PrimitiveFeature class attributes and methods

# Feature class attributes and methods

# featureDiagram_Opt class attributes and methods

# Operator class attributes and methods

# featureDiagram_And class attributes and methods

# featureDiagram_Or class attributes and methods

# featureDiagram_Xor class attributes and methods

# featureDiagram_Card class attributes and methods

# featureDiagram_Require class attributes and methods

# Constraint class attributes and methods

# featureDiagram_Mutex class attributes and methods

# Relationships
root1: BinaryAssociation = BinaryAssociation(
    name="root1",
    ends={
        Property(name="featureDiagram_Feature", type=featureDiagram_FeatureDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="featureDiagram_FeatureDiagram", type=featureDiagram_Feature, multiplicity=Multiplicity(1, 1))
    }
)
constraintEdges2: BinaryAssociation = BinaryAssociation(
    name="constraintEdges2",
    ends={
        Property(name="featureDiagram_ConstraintEdge", type=featureDiagram_FeatureDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="featureDiagram_FeatureDiagram3", type=featureDiagram_ConstraintEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
features0: BinaryAssociation = BinaryAssociation(
    name="features0",
    ends={
        Property(name="Feature", type=featureDiagram_FeatureDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="owningFeatureDiagram", type=featureDiagram_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target14: BinaryAssociation = BinaryAssociation(
    name="target14",
    ends={
        Property(name="featureDiagram_Feature16", type=featureDiagram_ConstraintEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="featureDiagram_ConstraintEdge15", type=featureDiagram_Feature, multiplicity=Multiplicity(0, 1))
    }
)
constraint17: BinaryAssociation = BinaryAssociation(
    name="constraint17",
    ends={
        Property(name="Constraint", type=featureDiagram_ConstraintEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="owningCE", type=featureDiagram_Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source18: BinaryAssociation = BinaryAssociation(
    name="source18",
    ends={
        Property(name="featureDiagram_Feature20", type=featureDiagram_ConstraintEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="featureDiagram_ConstraintEdge19", type=featureDiagram_Feature, multiplicity=Multiplicity(0, 1))
    }
)
owningFeatureDiagram4: BinaryAssociation = BinaryAssociation(
    name="owningFeatureDiagram4",
    ends={
        Property(name="FeatureDiagram", type=featureDiagram_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="features", type=featureDiagram_FeatureDiagram, multiplicity=Multiplicity(1, 1))
    }
)
operator5: BinaryAssociation = BinaryAssociation(
    name="operator5",
    ends={
        Property(name="Operator", type=featureDiagram_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="owningFeature", type=featureDiagram_Operator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
models6: BinaryAssociation = BinaryAssociation(
    name="models6",
    ends={
        Property(name="featureDiagram_Model", type=featureDiagram_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="featureDiagram_Feature7", type=featureDiagram_Model, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
children9: BinaryAssociation = BinaryAssociation(
    name="children9",
    ends={
        Property(name="Feature10", type=featureDiagram_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="parents", type=featureDiagram_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
parents12: BinaryAssociation = BinaryAssociation(
    name="parents12",
    ends={
        Property(name="Feature13", type=featureDiagram_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=featureDiagram_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
owningFeature21: BinaryAssociation = BinaryAssociation(
    name="owningFeature21",
    ends={
        Property(name="Feature22", type=featureDiagram_Operator, multiplicity=Multiplicity(1, 1)),
        Property(name="operator", type=featureDiagram_Feature, multiplicity=Multiplicity(0, 1))
    }
)
owningCE23: BinaryAssociation = BinaryAssociation(
    name="owningCE23",
    ends={
        Property(name="ConstraintEdge", type=featureDiagram_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="constraint", type=featureDiagram_ConstraintEdge, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_featureDiagram_PrimitiveFeature_Feature = Generalization(general=Feature, specific=featureDiagram_PrimitiveFeature)
gen_featureDiagram_Opt_Operator = Generalization(general=Operator, specific=featureDiagram_Opt)
gen_featureDiagram_And_Operator = Generalization(general=Operator, specific=featureDiagram_And)
gen_featureDiagram_Or_Operator = Generalization(general=Operator, specific=featureDiagram_Or)
gen_featureDiagram_Xor_Operator = Generalization(general=Operator, specific=featureDiagram_Xor)
gen_featureDiagram_Card_Operator = Generalization(general=Operator, specific=featureDiagram_Card)
gen_featureDiagram_Require_Constraint = Generalization(general=Constraint, specific=featureDiagram_Require)
gen_featureDiagram_Mutex_Constraint = Generalization(general=Constraint, specific=featureDiagram_Mutex)

# Domain Model
domain_model = DomainModel(
    name="featureDiagram",
    types={featureDiagram_ConstraintEdge, featureDiagram_FeatureDiagram, featureDiagram_Feature, featureDiagram_Constraint, featureDiagram_Operator, featureDiagram_Model, featureDiagram_PrimitiveFeature, Feature, featureDiagram_Opt, Operator, featureDiagram_And, featureDiagram_Or, featureDiagram_Xor, featureDiagram_Card, featureDiagram_Require, Constraint, featureDiagram_Mutex},
    associations={root1, constraintEdges2, features0, target14, constraint17, source18, owningFeatureDiagram4, operator5, models6, children9, parents12, owningFeature21, owningCE23},
    generalizations={gen_featureDiagram_PrimitiveFeature_Feature, gen_featureDiagram_Opt_Operator, gen_featureDiagram_And_Operator, gen_featureDiagram_Or_Operator, gen_featureDiagram_Xor_Operator, gen_featureDiagram_Card_Operator, gen_featureDiagram_Require_Constraint, gen_featureDiagram_Mutex_Constraint},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)