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
featureDiagram_FeatureDiagram = Class(name="featureDiagram::FeatureDiagram")
FeatureElement = Class(name="FeatureElement")
featureDiagram_Feature = Class(name="featureDiagram::Feature")
featureDiagram_ConstraintEdge = Class(name="featureDiagram::ConstraintEdge")
featureDiagram_Operator = Class(name="featureDiagram::Operator")
featureDiagram_Attribute = Class(name="featureDiagram::Attribute")
featureDiagram_EObject = Class(name="featureDiagram::EObject")
featureDiagram_PrimitiveFeature = Class(name="featureDiagram::PrimitiveFeature")
Feature = Class(name="Feature")
featureDiagram_Constraint = Class(name="featureDiagram::Constraint", is_abstract=True)
featureDiagram_Opt = Class(name="featureDiagram::Opt")
Operator = Class(name="Operator")
featureDiagram_Mandatory = Class(name="featureDiagram::Mandatory")
featureDiagram_Or = Class(name="featureDiagram::Or")
featureDiagram_Alternative = Class(name="featureDiagram::Alternative")
featureDiagram_Card = Class(name="featureDiagram::Card")
featureDiagram_Require = Class(name="featureDiagram::Require")
Constraint = Class(name="Constraint")
featureDiagram_Mutex = Class(name="featureDiagram::Mutex")
featureDiagram_FeatureElement = Class(name="featureDiagram::FeatureElement")

# featureDiagram_FeatureDiagram class attributes and methods
featureDiagram_FeatureDiagram_graphTypeTree: Property = Property(name="graphTypeTree", type=BooleanType)
featureDiagram_FeatureDiagram.attributes={featureDiagram_FeatureDiagram_graphTypeTree}

# FeatureElement class attributes and methods

# featureDiagram_Feature class attributes and methods
featureDiagram_Feature_name: Property = Property(name="name", type=StringType)
featureDiagram_Feature_selected: Property = Property(name="selected", type=BooleanType)
featureDiagram_Feature.attributes={featureDiagram_Feature_selected, featureDiagram_Feature_name}

# featureDiagram_ConstraintEdge class attributes and methods

# featureDiagram_Operator class attributes and methods
featureDiagram_Operator_name: Property = Property(name="name", type=StringType)
featureDiagram_Operator.attributes={featureDiagram_Operator_name}

# featureDiagram_Attribute class attributes and methods
featureDiagram_Attribute_name: Property = Property(name="name", type=StringType)
featureDiagram_Attribute_value: Property = Property(name="value", type=StringType)
featureDiagram_Attribute_type: Property = Property(name="type", type=StringType)
featureDiagram_Attribute.attributes={featureDiagram_Attribute_value, featureDiagram_Attribute_name, featureDiagram_Attribute_type}

# featureDiagram_EObject class attributes and methods

# featureDiagram_PrimitiveFeature class attributes and methods

# Feature class attributes and methods

# featureDiagram_Constraint class attributes and methods

# featureDiagram_Opt class attributes and methods

# Operator class attributes and methods

# featureDiagram_Mandatory class attributes and methods

# featureDiagram_Or class attributes and methods

# featureDiagram_Alternative class attributes and methods

# featureDiagram_Card class attributes and methods
featureDiagram_Card_min: Property = Property(name="min", type=IntegerType)
featureDiagram_Card_max: Property = Property(name="max", type=IntegerType)
featureDiagram_Card.attributes={featureDiagram_Card_max, featureDiagram_Card_min}

# featureDiagram_Require class attributes and methods

# Constraint class attributes and methods

# featureDiagram_Mutex class attributes and methods

# featureDiagram_FeatureElement class attributes and methods

# Relationships
owningFeatureDiagram4: BinaryAssociation = BinaryAssociation(
    name="owningFeatureDiagram4",
    ends={
        Property(name="FeatureDiagram", type=featureDiagram_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="features", type=featureDiagram_FeatureDiagram, multiplicity=Multiplicity(0, 1))
    }
)
features0: BinaryAssociation = BinaryAssociation(
    name="features0",
    ends={
        Property(name="Feature", type=featureDiagram_FeatureDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="owningFeatureDiagram", type=featureDiagram_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
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
operator5: BinaryAssociation = BinaryAssociation(
    name="operator5",
    ends={
        Property(name="Operator", type=featureDiagram_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="owningFeature", type=featureDiagram_Operator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes6: BinaryAssociation = BinaryAssociation(
    name="attributes6",
    ends={
        Property(name="Attribute", type=featureDiagram_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="owningFeature7", type=featureDiagram_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningOperator8: BinaryAssociation = BinaryAssociation(
    name="owningOperator8",
    ends={
        Property(name="Operator10", type=featureDiagram_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="features9", type=featureDiagram_Operator, multiplicity=Multiplicity(0, 9999))
    }
)
modelElements11: BinaryAssociation = BinaryAssociation(
    name="modelElements11",
    ends={
        Property(name="featureDiagram_EObject", type=featureDiagram_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="featureDiagram_Feature12", type=featureDiagram_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
target13: BinaryAssociation = BinaryAssociation(
    name="target13",
    ends={
        Property(name="featureDiagram_Feature15", type=featureDiagram_ConstraintEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="featureDiagram_ConstraintEdge14", type=featureDiagram_Feature, multiplicity=Multiplicity(0, 1))
    }
)
owningFeature20: BinaryAssociation = BinaryAssociation(
    name="owningFeature20",
    ends={
        Property(name="Feature21", type=featureDiagram_Operator, multiplicity=Multiplicity(1, 1)),
        Property(name="operator", type=featureDiagram_Feature, multiplicity=Multiplicity(0, 1))
    }
)
constraint16: BinaryAssociation = BinaryAssociation(
    name="constraint16",
    ends={
        Property(name="Constraint", type=featureDiagram_ConstraintEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="owningCE", type=featureDiagram_Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source17: BinaryAssociation = BinaryAssociation(
    name="source17",
    ends={
        Property(name="featureDiagram_Feature19", type=featureDiagram_ConstraintEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="featureDiagram_ConstraintEdge18", type=featureDiagram_Feature, multiplicity=Multiplicity(0, 1))
    }
)
features22: BinaryAssociation = BinaryAssociation(
    name="features22",
    ends={
        Property(name="Feature23", type=featureDiagram_Operator, multiplicity=Multiplicity(1, 1)),
        Property(name="owningOperator", type=featureDiagram_Feature, multiplicity=Multiplicity(1, 9999))
    }
)
owningCE24: BinaryAssociation = BinaryAssociation(
    name="owningCE24",
    ends={
        Property(name="ConstraintEdge", type=featureDiagram_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="constraint", type=featureDiagram_ConstraintEdge, multiplicity=Multiplicity(0, 1))
    }
)
owningFeature25: BinaryAssociation = BinaryAssociation(
    name="owningFeature25",
    ends={
        Property(name="Feature26", type=featureDiagram_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attributes", type=featureDiagram_Feature, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_featureDiagram_FeatureDiagram_FeatureElement = Generalization(general=FeatureElement, specific=featureDiagram_FeatureDiagram)
gen_featureDiagram_Feature_FeatureElement = Generalization(general=FeatureElement, specific=featureDiagram_Feature)
gen_featureDiagram_PrimitiveFeature_Feature = Generalization(general=Feature, specific=featureDiagram_PrimitiveFeature)
gen_featureDiagram_ConstraintEdge_FeatureElement = Generalization(general=FeatureElement, specific=featureDiagram_ConstraintEdge)
gen_featureDiagram_Operator_FeatureElement = Generalization(general=FeatureElement, specific=featureDiagram_Operator)
gen_featureDiagram_Attribute_FeatureElement = Generalization(general=FeatureElement, specific=featureDiagram_Attribute)
gen_featureDiagram_Opt_Operator = Generalization(general=Operator, specific=featureDiagram_Opt)
gen_featureDiagram_Mandatory_Operator = Generalization(general=Operator, specific=featureDiagram_Mandatory)
gen_featureDiagram_Or_Operator = Generalization(general=Operator, specific=featureDiagram_Or)
gen_featureDiagram_Alternative_Operator = Generalization(general=Operator, specific=featureDiagram_Alternative)
gen_featureDiagram_Card_Operator = Generalization(general=Operator, specific=featureDiagram_Card)
gen_featureDiagram_Constraint_FeatureElement = Generalization(general=FeatureElement, specific=featureDiagram_Constraint)
gen_featureDiagram_Require_Constraint = Generalization(general=Constraint, specific=featureDiagram_Require)
gen_featureDiagram_Mutex_Constraint = Generalization(general=Constraint, specific=featureDiagram_Mutex)

# Domain Model
domain_model = DomainModel(
    name="featureDiagram",
    types={featureDiagram_FeatureDiagram, FeatureElement, featureDiagram_Feature, featureDiagram_ConstraintEdge, featureDiagram_Operator, featureDiagram_Attribute, featureDiagram_EObject, featureDiagram_PrimitiveFeature, Feature, featureDiagram_Constraint, featureDiagram_Opt, Operator, featureDiagram_Mandatory, featureDiagram_Or, featureDiagram_Alternative, featureDiagram_Card, featureDiagram_Require, Constraint, featureDiagram_Mutex, featureDiagram_FeatureElement},
    associations={owningFeatureDiagram4, features0, root1, constraintEdges2, operator5, attributes6, owningOperator8, modelElements11, target13, owningFeature20, constraint16, source17, features22, owningCE24, owningFeature25},
    generalizations={gen_featureDiagram_FeatureDiagram_FeatureElement, gen_featureDiagram_Feature_FeatureElement, gen_featureDiagram_PrimitiveFeature_Feature, gen_featureDiagram_ConstraintEdge_FeatureElement, gen_featureDiagram_Operator_FeatureElement, gen_featureDiagram_Attribute_FeatureElement, gen_featureDiagram_Opt_Operator, gen_featureDiagram_Mandatory_Operator, gen_featureDiagram_Or_Operator, gen_featureDiagram_Alternative_Operator, gen_featureDiagram_Card_Operator, gen_featureDiagram_Constraint_FeatureElement, gen_featureDiagram_Require_Constraint, gen_featureDiagram_Mutex_Constraint},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)