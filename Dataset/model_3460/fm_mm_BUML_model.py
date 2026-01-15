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
fm_FeatureCardinality = Class(name="fm::FeatureCardinality")
fm_Attribute = Class(name="fm::Attribute")
fm_FeatureModel = Class(name="fm::FeatureModel")
fm_Feature = Class(name="fm::Feature")
fm_Constraints = Class(name="fm::Constraints")
Cardinality = Class(name="Cardinality")
fm_CardExConstraint = Class(name="fm::CardExConstraint")
Constraints = Class(name="Constraints")
fm_OrFeature = Class(name="fm::OrFeature")
Feature = Class(name="Feature")
fm_GroupCardinality = Class(name="fm::GroupCardinality")
fm_XorFeature = Class(name="fm::XorFeature")
OrFeature = Class(name="OrFeature")
fm_Cardinality = Class(name="fm::Cardinality")
fm_BooleanConstraints = Class(name="fm::BooleanConstraints")
fm_Operation = Class(name="fm::Operation")
fm_Operator = Class(name="fm::Operator")
fm_AndOperator = Class(name="fm::AndOperator")
Operator = Class(name="Operator")
fm_OrOperator = Class(name="fm::OrOperator")

# fm_FeatureCardinality class attributes and methods

# fm_Attribute class attributes and methods
fm_Attribute_name: Property = Property(name="name", type=StringType)
fm_Attribute_value: Property = Property(name="value", type=StringType)
fm_Attribute.attributes={fm_Attribute_value, fm_Attribute_name}

# fm_FeatureModel class attributes and methods

# fm_Feature class attributes and methods
fm_Feature_name: Property = Property(name="name", type=StringType)
fm_Feature.attributes={fm_Feature_name}

# fm_Constraints class attributes and methods

# Cardinality class attributes and methods

# fm_CardExConstraint class attributes and methods

# Constraints class attributes and methods

# fm_OrFeature class attributes and methods

# Feature class attributes and methods

# fm_GroupCardinality class attributes and methods

# fm_XorFeature class attributes and methods

# OrFeature class attributes and methods

# fm_Cardinality class attributes and methods
fm_Cardinality_max: Property = Property(name="max", type=IntegerType)
fm_Cardinality_min: Property = Property(name="min", type=IntegerType)
fm_Cardinality.attributes={fm_Cardinality_max, fm_Cardinality_min}

# fm_BooleanConstraints class attributes and methods

# fm_Operation class attributes and methods
fm_Operation_value: Property = Property(name="value", type=IntegerType)
fm_Operation.attributes={fm_Operation_value}

# fm_Operator class attributes and methods

# fm_AndOperator class attributes and methods

# Operator class attributes and methods

# fm_OrOperator class attributes and methods

# Relationships
subFeatures4: BinaryAssociation = BinaryAssociation(
    name="subFeatures4",
    ends={
        Property(name="fm_Feature5", type=fm_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="fm_Feature3", type=fm_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
featureCardinality6: BinaryAssociation = BinaryAssociation(
    name="featureCardinality6",
    ends={
        Property(name="fm_FeatureCardinality", type=fm_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="fm_Feature7", type=fm_FeatureCardinality, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes8: BinaryAssociation = BinaryAssociation(
    name="attributes8",
    ends={
        Property(name="fm_Attribute", type=fm_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="fm_Feature9", type=fm_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
root0: BinaryAssociation = BinaryAssociation(
    name="root0",
    ends={
        Property(name="fm_Feature", type=fm_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="fm_FeatureModel", type=fm_Feature, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
constraints1: BinaryAssociation = BinaryAssociation(
    name="constraints1",
    ends={
        Property(name="fm_Constraints", type=fm_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="fm_FeatureModel2", type=fm_Constraints, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variants10: BinaryAssociation = BinaryAssociation(
    name="variants10",
    ends={
        Property(name="fm_Feature11", type=fm_OrFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="fm_OrFeature", type=fm_Feature, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
groupCardinality12: BinaryAssociation = BinaryAssociation(
    name="groupCardinality12",
    ends={
        Property(name="fm_GroupCardinality", type=fm_OrFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="fm_OrFeature13", type=fm_GroupCardinality, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
feature20: BinaryAssociation = BinaryAssociation(
    name="feature20",
    ends={
        Property(name="fm_Feature22", type=fm_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="fm_Operation21", type=fm_Feature, multiplicity=Multiplicity(1, 1))
    }
)
from23: BinaryAssociation = BinaryAssociation(
    name="from23",
    ends={
        Property(name="fm_Feature24", type=fm_BooleanConstraints, multiplicity=Multiplicity(1, 1)),
        Property(name="fm_BooleanConstraints", type=fm_Feature, multiplicity=Multiplicity(1, 1))
    }
)
to25: BinaryAssociation = BinaryAssociation(
    name="to25",
    ends={
        Property(name="fm_Feature27", type=fm_BooleanConstraints, multiplicity=Multiplicity(1, 1)),
        Property(name="fm_BooleanConstraints26", type=fm_Feature, multiplicity=Multiplicity(1, 1))
    }
)
action14: BinaryAssociation = BinaryAssociation(
    name="action14",
    ends={
        Property(name="fm_Operation", type=fm_CardExConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="fm_CardExConstraint", type=fm_Operation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition15: BinaryAssociation = BinaryAssociation(
    name="condition15",
    ends={
        Property(name="fm_Operation17", type=fm_CardExConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="fm_CardExConstraint16", type=fm_Operation, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
operator18: BinaryAssociation = BinaryAssociation(
    name="operator18",
    ends={
        Property(name="fm_Operator", type=fm_CardExConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="fm_CardExConstraint19", type=fm_Operator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_fm_FeatureCardinality_Cardinality = Generalization(general=Cardinality, specific=fm_FeatureCardinality)
gen_fm_GroupCardinality_Cardinality = Generalization(general=Cardinality, specific=fm_GroupCardinality)
gen_fm_CardExConstraint_Constraints = Generalization(general=Constraints, specific=fm_CardExConstraint)
gen_fm_OrFeature_Feature = Generalization(general=Feature, specific=fm_OrFeature)
gen_fm_XorFeature_OrFeature = Generalization(general=OrFeature, specific=fm_XorFeature)
gen_fm_BooleanConstraints_Constraints = Generalization(general=Constraints, specific=fm_BooleanConstraints)
gen_fm_AndOperator_Operator = Generalization(general=Operator, specific=fm_AndOperator)
gen_fm_OrOperator_Operator = Generalization(general=Operator, specific=fm_OrOperator)

# Domain Model
domain_model = DomainModel(
    name="fm",
    types={fm_FeatureCardinality, fm_Attribute, fm_FeatureModel, fm_Feature, fm_Constraints, Cardinality, fm_CardExConstraint, Constraints, fm_OrFeature, Feature, fm_GroupCardinality, fm_XorFeature, OrFeature, fm_Cardinality, fm_BooleanConstraints, fm_Operation, fm_Operator, fm_AndOperator, Operator, fm_OrOperator},
    associations={subFeatures4, featureCardinality6, attributes8, root0, constraints1, variants10, groupCardinality12, feature20, from23, to25, action14, condition15, operator18},
    generalizations={gen_fm_FeatureCardinality_Cardinality, gen_fm_GroupCardinality_Cardinality, gen_fm_CardExConstraint_Constraints, gen_fm_OrFeature_Feature, gen_fm_XorFeature_OrFeature, gen_fm_BooleanConstraints_Constraints, gen_fm_AndOperator_Operator, gen_fm_OrOperator_Operator},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)