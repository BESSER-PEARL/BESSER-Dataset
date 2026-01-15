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
FCORE_Softgoal = Class(name="FCORE::Softgoal")
FCORE_InfluenceFeature = Class(name="FCORE::InfluenceFeature")
FCORE_FeatureModel = Class(name="FCORE::FeatureModel")
FCORE_RootFeature = Class(name="FCORE::RootFeature")
FCORE_GroupFeature = Class(name="FCORE::GroupFeature")
FCORE_SolitaryFeature = Class(name="FCORE::SolitaryFeature")
FCORE_FeatureGroup = Class(name="FCORE::FeatureGroup")
FCORE_Attribute = Class(name="FCORE::Attribute")
FCORE_AttributeConstraint = Class(name="FCORE::AttributeConstraint")
FCORE_RequiresFeatureConstraint = Class(name="FCORE::RequiresFeatureConstraint")
FCORE_ExcludesFeatureConstraint = Class(name="FCORE::ExcludesFeatureConstraint")
FCORE_InfluenceAttribute = Class(name="FCORE::InfluenceAttribute")
FCORE_MandatoryConnection = Class(name="FCORE::MandatoryConnection")
FCORE_OptionalConnection = Class(name="FCORE::OptionalConnection")
FCORE_FeatureToGroupConnection = Class(name="FCORE::FeatureToGroupConnection")
FCORE_GroupToFeatureConnection = Class(name="FCORE::GroupToFeatureConnection")
FCORE_AttributeConstraintConnection = Class(name="FCORE::AttributeConstraintConnection")
FCORE_Feature = Class(name="FCORE::Feature", is_abstract=True)
FCORE_FeatureConstraint = Class(name="FCORE::FeatureConstraint", is_abstract=True)
FCORE_SingleFeatureConnection = Class(name="FCORE::SingleFeatureConnection", is_abstract=True)
Feature = Class(name="Feature")
FCORE_Influence = Class(name="FCORE::Influence", is_abstract=True)
FCORE_Conncection = Class(name="FCORE::Conncection", is_abstract=True)
Conncection = Class(name="Conncection")
FeatureConstraint = Class(name="FeatureConstraint")
Influence = Class(name="Influence")
FCORE_CardinalityConnection = Class(name="FCORE::CardinalityConnection")
SingleFeatureConnection = Class(name="SingleFeatureConnection")

# FCORE_Softgoal class attributes and methods
FCORE_Softgoal_name: Property = Property(name="name", type=StringType)
FCORE_Softgoal_weighting: Property = Property(name="weighting", type=StringType)
FCORE_Softgoal.attributes={FCORE_Softgoal_name, FCORE_Softgoal_weighting}

# FCORE_InfluenceFeature class attributes and methods

# FCORE_FeatureModel class attributes and methods

# FCORE_RootFeature class attributes and methods

# FCORE_GroupFeature class attributes and methods

# FCORE_SolitaryFeature class attributes and methods
FCORE_SolitaryFeature_min: Property = Property(name="min", type=IntegerType)
FCORE_SolitaryFeature_max: Property = Property(name="max", type=IntegerType)
FCORE_SolitaryFeature.attributes={FCORE_SolitaryFeature_max, FCORE_SolitaryFeature_min}

# FCORE_FeatureGroup class attributes and methods
FCORE_FeatureGroup_min: Property = Property(name="min", type=IntegerType)
FCORE_FeatureGroup_max: Property = Property(name="max", type=IntegerType)
FCORE_FeatureGroup.attributes={FCORE_FeatureGroup_max, FCORE_FeatureGroup_min}

# FCORE_Attribute class attributes and methods
FCORE_Attribute_name: Property = Property(name="name", type=StringType)
FCORE_Attribute_value: Property = Property(name="value", type=IntegerType)
FCORE_Attribute_min: Property = Property(name="min", type=IntegerType)
FCORE_Attribute_max: Property = Property(name="max", type=IntegerType)
FCORE_Attribute.attributes={FCORE_Attribute_value, FCORE_Attribute_name, FCORE_Attribute_min, FCORE_Attribute_max}

# FCORE_AttributeConstraint class attributes and methods
FCORE_AttributeConstraint_equation: Property = Property(name="equation", type=StringType)
FCORE_AttributeConstraint.attributes={FCORE_AttributeConstraint_equation}

# FCORE_RequiresFeatureConstraint class attributes and methods

# FCORE_ExcludesFeatureConstraint class attributes and methods

# FCORE_InfluenceAttribute class attributes and methods

# FCORE_MandatoryConnection class attributes and methods

# FCORE_OptionalConnection class attributes and methods

# FCORE_FeatureToGroupConnection class attributes and methods

# FCORE_GroupToFeatureConnection class attributes and methods

# FCORE_AttributeConstraintConnection class attributes and methods

# FCORE_Feature class attributes and methods
FCORE_Feature_selected: Property = Property(name="selected", type=BooleanType)
FCORE_Feature_name: Property = Property(name="name", type=StringType)
FCORE_Feature.attributes={FCORE_Feature_name, FCORE_Feature_selected}

# FCORE_FeatureConstraint class attributes and methods

# FCORE_SingleFeatureConnection class attributes and methods

# Feature class attributes and methods

# FCORE_Influence class attributes and methods
FCORE_Influence_contribution: Property = Property(name="contribution", type=FloatType)
FCORE_Influence.attributes={FCORE_Influence_contribution}

# FCORE_Conncection class attributes and methods

# Conncection class attributes and methods

# FeatureConstraint class attributes and methods

# Influence class attributes and methods

# FCORE_CardinalityConnection class attributes and methods
FCORE_CardinalityConnection_min: Property = Property(name="min", type=IntegerType)
FCORE_CardinalityConnection_max: Property = Property(name="max", type=IntegerType)
FCORE_CardinalityConnection.attributes={FCORE_CardinalityConnection_max, FCORE_CardinalityConnection_min}

# SingleFeatureConnection class attributes and methods

# Relationships
softgoals15: BinaryAssociation = BinaryAssociation(
    name="softgoals15",
    ends={
        Property(name="FCORE_Softgoal", type=FCORE_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="FCORE_FeatureModel16", type=FCORE_Softgoal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
featureInfluences17: BinaryAssociation = BinaryAssociation(
    name="featureInfluences17",
    ends={
        Property(name="FCORE_InfluenceFeature", type=FCORE_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="FCORE_FeatureModel18", type=FCORE_InfluenceFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rootFeature0: BinaryAssociation = BinaryAssociation(
    name="rootFeature0",
    ends={
        Property(name="FCORE_RootFeature", type=FCORE_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="FCORE_FeatureModel", type=FCORE_RootFeature, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
groupFeatures1: BinaryAssociation = BinaryAssociation(
    name="groupFeatures1",
    ends={
        Property(name="FCORE_GroupFeature", type=FCORE_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="FCORE_FeatureModel2", type=FCORE_GroupFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
solitaryFeatures3: BinaryAssociation = BinaryAssociation(
    name="solitaryFeatures3",
    ends={
        Property(name="FCORE_SolitaryFeature", type=FCORE_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="FCORE_FeatureModel4", type=FCORE_SolitaryFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
featureGroups5: BinaryAssociation = BinaryAssociation(
    name="featureGroups5",
    ends={
        Property(name="FCORE_FeatureGroup", type=FCORE_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="FCORE_FeatureModel6", type=FCORE_FeatureGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes7: BinaryAssociation = BinaryAssociation(
    name="attributes7",
    ends={
        Property(name="FCORE_Attribute", type=FCORE_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="FCORE_FeatureModel8", type=FCORE_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributeConstraints9: BinaryAssociation = BinaryAssociation(
    name="attributeConstraints9",
    ends={
        Property(name="FCORE_AttributeConstraint", type=FCORE_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="FCORE_FeatureModel10", type=FCORE_AttributeConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiresFeatureConstraints11: BinaryAssociation = BinaryAssociation(
    name="requiresFeatureConstraints11",
    ends={
        Property(name="FCORE_RequiresFeatureConstraint", type=FCORE_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="FCORE_FeatureModel12", type=FCORE_RequiresFeatureConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
excludesFeatureConstraints13: BinaryAssociation = BinaryAssociation(
    name="excludesFeatureConstraints13",
    ends={
        Property(name="FCORE_ExcludesFeatureConstraint", type=FCORE_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="FCORE_FeatureModel14", type=FCORE_ExcludesFeatureConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributeConstraints31: BinaryAssociation = BinaryAssociation(
    name="attributeConstraints31",
    ends={
        Property(name="AttributeConstraintConnection", type=FCORE_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=FCORE_AttributeConstraintConnection, multiplicity=Multiplicity(0, 9999))
    }
)
attributeInfluences19: BinaryAssociation = BinaryAssociation(
    name="attributeInfluences19",
    ends={
        Property(name="FCORE_InfluenceAttribute", type=FCORE_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="FCORE_FeatureModel20", type=FCORE_InfluenceAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mandatoryConnections21: BinaryAssociation = BinaryAssociation(
    name="mandatoryConnections21",
    ends={
        Property(name="FCORE_MandatoryConnection", type=FCORE_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="FCORE_FeatureModel22", type=FCORE_MandatoryConnection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
optionalConnections23: BinaryAssociation = BinaryAssociation(
    name="optionalConnections23",
    ends={
        Property(name="FCORE_OptionalConnection", type=FCORE_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="FCORE_FeatureModel24", type=FCORE_OptionalConnection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
featureToGroupConnections25: BinaryAssociation = BinaryAssociation(
    name="featureToGroupConnections25",
    ends={
        Property(name="FCORE_FeatureToGroupConnection", type=FCORE_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="FCORE_FeatureModel26", type=FCORE_FeatureToGroupConnection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
groupToFeatureConnections27: BinaryAssociation = BinaryAssociation(
    name="groupToFeatureConnections27",
    ends={
        Property(name="FCORE_GroupToFeatureConnection", type=FCORE_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="FCORE_FeatureModel28", type=FCORE_GroupToFeatureConnection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
AttributeConstraintConnections29: BinaryAssociation = BinaryAssociation(
    name="AttributeConstraintConnections29",
    ends={
        Property(name="FCORE_AttributeConstraintConnection", type=FCORE_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="FCORE_FeatureModel30", type=FCORE_AttributeConstraintConnection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
featureToGroupConnection46: BinaryAssociation = BinaryAssociation(
    name="featureToGroupConnection46",
    ends={
        Property(name="FeatureToGroupConnection48", type=FCORE_FeatureGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="target47", type=FCORE_FeatureToGroupConnection, multiplicity=Multiplicity(1, 1))
    }
)
attributes32: BinaryAssociation = BinaryAssociation(
    name="attributes32",
    ends={
        Property(name="FCORE_Attribute33", type=FCORE_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="FCORE_Feature", type=FCORE_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
featureConstraintsStarts34: BinaryAssociation = BinaryAssociation(
    name="featureConstraintsStarts34",
    ends={
        Property(name="FeatureConstraint", type=FCORE_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="featureStart", type=FCORE_FeatureConstraint, multiplicity=Multiplicity(0, 9999))
    }
)
featureConstraintsEnds35: BinaryAssociation = BinaryAssociation(
    name="featureConstraintsEnds35",
    ends={
        Property(name="FeatureConstraint36", type=FCORE_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="featureEnd", type=FCORE_FeatureConstraint, multiplicity=Multiplicity(0, 9999))
    }
)
influences37: BinaryAssociation = BinaryAssociation(
    name="influences37",
    ends={
        Property(name="InfluenceFeature", type=FCORE_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="feature", type=FCORE_InfluenceFeature, multiplicity=Multiplicity(0, 9999))
    }
)
outgoingSingleFeatureConnections38: BinaryAssociation = BinaryAssociation(
    name="outgoingSingleFeatureConnections38",
    ends={
        Property(name="SingleFeatureConnection", type=FCORE_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="source39", type=FCORE_SingleFeatureConnection, multiplicity=Multiplicity(0, 9999))
    }
)
featureToGroupConnections40: BinaryAssociation = BinaryAssociation(
    name="featureToGroupConnections40",
    ends={
        Property(name="FeatureToGroupConnection", type=FCORE_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="source41", type=FCORE_FeatureToGroupConnection, multiplicity=Multiplicity(0, 9999))
    }
)
incomingSingleFeatureConnection42: BinaryAssociation = BinaryAssociation(
    name="incomingSingleFeatureConnection42",
    ends={
        Property(name="SingleFeatureConnection43", type=FCORE_SolitaryFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=FCORE_SingleFeatureConnection, multiplicity=Multiplicity(1, 1))
    }
)
groupToFeatureConnection44: BinaryAssociation = BinaryAssociation(
    name="groupToFeatureConnection44",
    ends={
        Property(name="GroupToFeatureConnection", type=FCORE_GroupFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="target45", type=FCORE_GroupToFeatureConnection, multiplicity=Multiplicity(1, 1))
    }
)
featureStart57: BinaryAssociation = BinaryAssociation(
    name="featureStart57",
    ends={
        Property(name="Feature", type=FCORE_FeatureConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="featureConstraintsStarts", type=FCORE_Feature, multiplicity=Multiplicity(1, 1))
    }
)
groupToFeatureConnections49: BinaryAssociation = BinaryAssociation(
    name="groupToFeatureConnections49",
    ends={
        Property(name="GroupToFeatureConnection51", type=FCORE_FeatureGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="source50", type=FCORE_GroupToFeatureConnection, multiplicity=Multiplicity(2, 9999))
    }
)
featureEnd58: BinaryAssociation = BinaryAssociation(
    name="featureEnd58",
    ends={
        Property(name="Feature59", type=FCORE_FeatureConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="featureConstraintsEnds", type=FCORE_Feature, multiplicity=Multiplicity(1, 1))
    }
)
influences52: BinaryAssociation = BinaryAssociation(
    name="influences52",
    ends={
        Property(name="InfluenceAttribute", type=FCORE_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attribute", type=FCORE_InfluenceAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
attributeConstraintConnection53: BinaryAssociation = BinaryAssociation(
    name="attributeConstraintConnection53",
    ends={
        Property(name="AttributeConstraintConnection55", type=FCORE_AttributeConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="target54", type=FCORE_AttributeConstraintConnection, multiplicity=Multiplicity(0, 1))
    }
)
influence56: BinaryAssociation = BinaryAssociation(
    name="influence56",
    ends={
        Property(name="Influence", type=FCORE_Softgoal, multiplicity=Multiplicity(1, 1)),
        Property(name="softgoal", type=FCORE_Influence, multiplicity=Multiplicity(0, 9999))
    }
)
source65: BinaryAssociation = BinaryAssociation(
    name="source65",
    ends={
        Property(name="Feature66", type=FCORE_SingleFeatureConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingSingleFeatureConnections", type=FCORE_Feature, multiplicity=Multiplicity(1, 1))
    }
)
softgoal60: BinaryAssociation = BinaryAssociation(
    name="softgoal60",
    ends={
        Property(name="Softgoal", type=FCORE_Influence, multiplicity=Multiplicity(1, 1)),
        Property(name="influence", type=FCORE_Softgoal, multiplicity=Multiplicity(1, 1))
    }
)
feature61: BinaryAssociation = BinaryAssociation(
    name="feature61",
    ends={
        Property(name="Feature62", type=FCORE_InfluenceFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="influences", type=FCORE_Feature, multiplicity=Multiplicity(1, 1))
    }
)
attribute63: BinaryAssociation = BinaryAssociation(
    name="attribute63",
    ends={
        Property(name="Attribute", type=FCORE_InfluenceAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="influences64", type=FCORE_Attribute, multiplicity=Multiplicity(1, 1))
    }
)
source71: BinaryAssociation = BinaryAssociation(
    name="source71",
    ends={
        Property(name="groupToFeatureConnections", type=FCORE_FeatureGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="FeatureGroup72", type=FCORE_GroupToFeatureConnection, multiplicity=Multiplicity(1, 1))
    }
)
target67: BinaryAssociation = BinaryAssociation(
    name="target67",
    ends={
        Property(name="SolitaryFeature", type=FCORE_SingleFeatureConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingSingleFeatureConnection", type=FCORE_SolitaryFeature, multiplicity=Multiplicity(1, 1))
    }
)
source68: BinaryAssociation = BinaryAssociation(
    name="source68",
    ends={
        Property(name="Feature69", type=FCORE_FeatureToGroupConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="featureToGroupConnections", type=FCORE_Feature, multiplicity=Multiplicity(1, 1))
    }
)
target70: BinaryAssociation = BinaryAssociation(
    name="target70",
    ends={
        Property(name="FeatureGroup", type=FCORE_FeatureToGroupConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="featureToGroupConnection", type=FCORE_FeatureGroup, multiplicity=Multiplicity(1, 1))
    }
)
target73: BinaryAssociation = BinaryAssociation(
    name="target73",
    ends={
        Property(name="GroupFeature", type=FCORE_GroupToFeatureConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="groupToFeatureConnection", type=FCORE_GroupFeature, multiplicity=Multiplicity(1, 1))
    }
)
source74: BinaryAssociation = BinaryAssociation(
    name="source74",
    ends={
        Property(name="Feature75", type=FCORE_AttributeConstraintConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="attributeConstraints", type=FCORE_Feature, multiplicity=Multiplicity(1, 1))
    }
)
target76: BinaryAssociation = BinaryAssociation(
    name="target76",
    ends={
        Property(name="AttributeConstraint", type=FCORE_AttributeConstraintConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="attributeConstraintConnection", type=FCORE_AttributeConstraint, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_FCORE_RootFeature_Feature = Generalization(general=Feature, specific=FCORE_RootFeature)
gen_FCORE_SolitaryFeature_Feature = Generalization(general=Feature, specific=FCORE_SolitaryFeature)
gen_FCORE_GroupFeature_Feature = Generalization(general=Feature, specific=FCORE_GroupFeature)
gen_FCORE_FeatureConstraint_Conncection = Generalization(general=Conncection, specific=FCORE_FeatureConstraint)
gen_FCORE_SingleFeatureConnection_Conncection = Generalization(general=Conncection, specific=FCORE_SingleFeatureConnection)
gen_FCORE_RequiresFeatureConstraint_FeatureConstraint = Generalization(general=FeatureConstraint, specific=FCORE_RequiresFeatureConstraint)
gen_FCORE_ExcludesFeatureConstraint_FeatureConstraint = Generalization(general=FeatureConstraint, specific=FCORE_ExcludesFeatureConstraint)
gen_FCORE_Influence_Conncection = Generalization(general=Conncection, specific=FCORE_Influence)
gen_FCORE_InfluenceFeature_Influence = Generalization(general=Influence, specific=FCORE_InfluenceFeature)
gen_FCORE_InfluenceAttribute_Influence = Generalization(general=Influence, specific=FCORE_InfluenceAttribute)
gen_FCORE_CardinalityConnection_SingleFeatureConnection = Generalization(general=SingleFeatureConnection, specific=FCORE_CardinalityConnection)
gen_FCORE_MandatoryConnection_SingleFeatureConnection = Generalization(general=SingleFeatureConnection, specific=FCORE_MandatoryConnection)
gen_FCORE_OptionalConnection_SingleFeatureConnection = Generalization(general=SingleFeatureConnection, specific=FCORE_OptionalConnection)
gen_FCORE_FeatureToGroupConnection_Conncection = Generalization(general=Conncection, specific=FCORE_FeatureToGroupConnection)
gen_FCORE_GroupToFeatureConnection_Conncection = Generalization(general=Conncection, specific=FCORE_GroupToFeatureConnection)
gen_FCORE_AttributeConstraintConnection_Conncection = Generalization(general=Conncection, specific=FCORE_AttributeConstraintConnection)

# Domain Model
domain_model = DomainModel(
    name="FCORE",
    types={FCORE_Softgoal, FCORE_InfluenceFeature, FCORE_FeatureModel, FCORE_RootFeature, FCORE_GroupFeature, FCORE_SolitaryFeature, FCORE_FeatureGroup, FCORE_Attribute, FCORE_AttributeConstraint, FCORE_RequiresFeatureConstraint, FCORE_ExcludesFeatureConstraint, FCORE_InfluenceAttribute, FCORE_MandatoryConnection, FCORE_OptionalConnection, FCORE_FeatureToGroupConnection, FCORE_GroupToFeatureConnection, FCORE_AttributeConstraintConnection, FCORE_Feature, FCORE_FeatureConstraint, FCORE_SingleFeatureConnection, Feature, FCORE_Influence, FCORE_Conncection, Conncection, FeatureConstraint, Influence, FCORE_CardinalityConnection, SingleFeatureConnection},
    associations={softgoals15, featureInfluences17, rootFeature0, groupFeatures1, solitaryFeatures3, featureGroups5, attributes7, attributeConstraints9, requiresFeatureConstraints11, excludesFeatureConstraints13, attributeConstraints31, attributeInfluences19, mandatoryConnections21, optionalConnections23, featureToGroupConnections25, groupToFeatureConnections27, AttributeConstraintConnections29, featureToGroupConnection46, attributes32, featureConstraintsStarts34, featureConstraintsEnds35, influences37, outgoingSingleFeatureConnections38, featureToGroupConnections40, incomingSingleFeatureConnection42, groupToFeatureConnection44, featureStart57, groupToFeatureConnections49, featureEnd58, influences52, attributeConstraintConnection53, influence56, source65, softgoal60, feature61, attribute63, source71, target67, source68, target70, target73, source74, target76},
    generalizations={gen_FCORE_RootFeature_Feature, gen_FCORE_SolitaryFeature_Feature, gen_FCORE_GroupFeature_Feature, gen_FCORE_FeatureConstraint_Conncection, gen_FCORE_SingleFeatureConnection_Conncection, gen_FCORE_RequiresFeatureConstraint_FeatureConstraint, gen_FCORE_ExcludesFeatureConstraint_FeatureConstraint, gen_FCORE_Influence_Conncection, gen_FCORE_InfluenceFeature_Influence, gen_FCORE_InfluenceAttribute_Influence, gen_FCORE_CardinalityConnection_SingleFeatureConnection, gen_FCORE_MandatoryConnection_SingleFeatureConnection, gen_FCORE_OptionalConnection_SingleFeatureConnection, gen_FCORE_FeatureToGroupConnection_Conncection, gen_FCORE_GroupToFeatureConnection_Conncection, gen_FCORE_AttributeConstraintConnection_Conncection},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)