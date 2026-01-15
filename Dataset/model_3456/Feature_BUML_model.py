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

# Enumerations
HyFeatureTypeEnum: Enumeration = Enumeration(
    name="HyFeatureTypeEnum",
    literals={
            EnumerationLiteral(name="OPTIONAL"),
			EnumerationLiteral(name="MANDATORY")
    }
)

HyGroupTypeEnum: Enumeration = Enumeration(
    name="HyGroupTypeEnum",
    literals={
            EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="OR"),
			EnumerationLiteral(name="ALTERNATIVE")
    }
)

# Classes
feature_HyFeatureModel = Class(name="feature::HyFeatureModel")
feature_HyRootFeature = Class(name="feature::HyRootFeature")
feature_HyFeature = Class(name="feature::HyFeature")
feature_HyEnum = Class(name="feature::HyEnum")
feature_HyContextModel = Class(name="feature::HyContextModel")
HyTemporalElement = Class(name="HyTemporalElement")
HyNamedElement = Class(name="HyNamedElement")
feature_HyVersion = Class(name="feature::HyVersion")
feature_HyGroupComposition = Class(name="feature::HyGroupComposition")
feature_HyFeatureChild = Class(name="feature::HyFeatureChild")
feature_HyFeatureAttribute = Class(name="feature::HyFeatureAttribute", is_abstract=True)
feature_HyGroup = Class(name="feature::HyGroup")
feature_HyGroupType = Class(name="feature::HyGroupType")
feature_HyFeatureType = Class(name="feature::HyFeatureType")
feature_HyNumberAttribute = Class(name="feature::HyNumberAttribute")
HyFeatureAttribute = Class(name="HyFeatureAttribute")
feature_HyBooleanAttribute = Class(name="feature::HyBooleanAttribute")
feature_HyStringAttribute = Class(name="feature::HyStringAttribute")
feature_HyEnumAttribute = Class(name="feature::HyEnumAttribute")
feature_HyEnumLiteral = Class(name="feature::HyEnumLiteral")
HyLinearTemporalElement = Class(name="HyLinearTemporalElement")

# feature_HyFeatureModel class attributes and methods

# feature_HyRootFeature class attributes and methods

# feature_HyFeature class attributes and methods
feature_HyFeature_deprecatedSince: Property = Property(name="deprecatedSince", type=DateType)
feature_HyFeature_m_isOptional: Method = Method(name="isOptional", parameters={Parameter(name='date')}, type=BooleanType)
feature_HyFeature_m_isMandatory: Method = Method(name="isMandatory", parameters={Parameter(name='date')}, type=BooleanType)
feature_HyFeature.attributes={feature_HyFeature_deprecatedSince}
feature_HyFeature.methods={feature_HyFeature_m_isMandatory, feature_HyFeature_m_isOptional}

# feature_HyEnum class attributes and methods

# feature_HyContextModel class attributes and methods

# HyTemporalElement class attributes and methods

# HyNamedElement class attributes and methods

# feature_HyVersion class attributes and methods
feature_HyVersion_number: Property = Property(name="number", type=StringType)
feature_HyVersion.attributes={feature_HyVersion_number}

# feature_HyGroupComposition class attributes and methods

# feature_HyFeatureChild class attributes and methods

# feature_HyFeatureAttribute class attributes and methods

# feature_HyGroup class attributes and methods
feature_HyGroup_m_isAlternative: Method = Method(name="isAlternative", parameters={Parameter(name='date')}, type=BooleanType)
feature_HyGroup_m_isOr: Method = Method(name="isOr", parameters={Parameter(name='date')}, type=BooleanType)
feature_HyGroup_m_isAnd: Method = Method(name="isAnd", parameters={Parameter(name='date')}, type=BooleanType)
feature_HyGroup.methods={feature_HyGroup_m_isOr, feature_HyGroup_m_isAlternative, feature_HyGroup_m_isAnd}

# feature_HyGroupType class attributes and methods
feature_HyGroupType_type: Property = Property(name="type", type=StringType)
feature_HyGroupType.attributes={feature_HyGroupType_type}

# feature_HyFeatureType class attributes and methods
feature_HyFeatureType_type: Property = Property(name="type", type=StringType)
feature_HyFeatureType.attributes={feature_HyFeatureType_type}

# feature_HyNumberAttribute class attributes and methods
feature_HyNumberAttribute_min: Property = Property(name="min", type=IntegerType)
feature_HyNumberAttribute_max: Property = Property(name="max", type=IntegerType)
feature_HyNumberAttribute_default: Property = Property(name="default", type=IntegerType)
feature_HyNumberAttribute.attributes={feature_HyNumberAttribute_min, feature_HyNumberAttribute_max, feature_HyNumberAttribute_default}

# HyFeatureAttribute class attributes and methods

# feature_HyBooleanAttribute class attributes and methods
feature_HyBooleanAttribute_default: Property = Property(name="default", type=BooleanType)
feature_HyBooleanAttribute.attributes={feature_HyBooleanAttribute_default}

# feature_HyStringAttribute class attributes and methods
feature_HyStringAttribute_default: Property = Property(name="default", type=StringType)
feature_HyStringAttribute.attributes={feature_HyStringAttribute_default}

# feature_HyEnumAttribute class attributes and methods

# feature_HyEnumLiteral class attributes and methods

# HyLinearTemporalElement class attributes and methods

# Relationships
rootFeature0: BinaryAssociation = BinaryAssociation(
    name="rootFeature0",
    ends={
        Property(name="feature_HyRootFeature", type=feature_HyFeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="feature_HyFeatureModel", type=feature_HyRootFeature, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
features1: BinaryAssociation = BinaryAssociation(
    name="features1",
    ends={
        Property(name="HyFeature", type=feature_HyFeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="featureModel", type=feature_HyFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enums4: BinaryAssociation = BinaryAssociation(
    name="enums4",
    ends={
        Property(name="feature_HyEnum", type=feature_HyFeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="feature_HyFeatureModel5", type=feature_HyEnum, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contexts6: BinaryAssociation = BinaryAssociation(
    name="contexts6",
    ends={
        Property(name="feature_HyContextModel", type=feature_HyFeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="feature_HyFeatureModel7", type=feature_HyContextModel, multiplicity=Multiplicity(0, 9999))
    }
)
versions8: BinaryAssociation = BinaryAssociation(
    name="versions8",
    ends={
        Property(name="HyVersion", type=feature_HyFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="feature", type=feature_HyVersion, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
groupMembership9: BinaryAssociation = BinaryAssociation(
    name="groupMembership9",
    ends={
        Property(name="HyGroupComposition", type=feature_HyFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="features", type=feature_HyGroupComposition, multiplicity=Multiplicity(0, 9999))
    }
)
parentOf10: BinaryAssociation = BinaryAssociation(
    name="parentOf10",
    ends={
        Property(name="HyFeatureChild", type=feature_HyFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=feature_HyFeatureChild, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes11: BinaryAssociation = BinaryAssociation(
    name="attributes11",
    ends={
        Property(name="HyFeatureAttribute", type=feature_HyFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="feature12", type=feature_HyFeatureAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
groups2: BinaryAssociation = BinaryAssociation(
    name="groups2",
    ends={
        Property(name="HyGroup", type=feature_HyFeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="featureModel3", type=feature_HyGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
types13: BinaryAssociation = BinaryAssociation(
    name="types13",
    ends={
        Property(name="feature_HyFeature", type=feature_HyFeatureType, multiplicity=Multiplicity(1, 9999), is_composite=True),
        Property(name="feature_HyFeatureType", type=feature_HyFeature, multiplicity=Multiplicity(1, 1))
    }
)
featureModel14: BinaryAssociation = BinaryAssociation(
    name="featureModel14",
    ends={
        Property(name="HyFeatureModel", type=feature_HyFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="features15", type=feature_HyFeatureModel, multiplicity=Multiplicity(1, 1))
    }
)
parentOf16: BinaryAssociation = BinaryAssociation(
    name="parentOf16",
    ends={
        Property(name="HyGroupComposition17", type=feature_HyGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="compositionOf", type=feature_HyGroupComposition, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
childOf18: BinaryAssociation = BinaryAssociation(
    name="childOf18",
    ends={
        Property(name="HyFeatureChild19", type=feature_HyGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="childGroup", type=feature_HyFeatureChild, multiplicity=Multiplicity(1, 9999))
    }
)
types20: BinaryAssociation = BinaryAssociation(
    name="types20",
    ends={
        Property(name="feature_HyGroupType", type=feature_HyGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="feature_HyGroup", type=feature_HyGroupType, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
featureModel21: BinaryAssociation = BinaryAssociation(
    name="featureModel21",
    ends={
        Property(name="HyFeatureModel22", type=feature_HyGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="groups", type=feature_HyFeatureModel, multiplicity=Multiplicity(1, 1))
    }
)
supersedingVersions26: BinaryAssociation = BinaryAssociation(
    name="supersedingVersions26",
    ends={
        Property(name="HyVersion27", type=feature_HyVersion, multiplicity=Multiplicity(1, 1)),
        Property(name="supersededVersion", type=feature_HyVersion, multiplicity=Multiplicity(0, 9999))
    }
)
supersededVersion29: BinaryAssociation = BinaryAssociation(
    name="supersededVersion29",
    ends={
        Property(name="HyVersion30", type=feature_HyVersion, multiplicity=Multiplicity(1, 1)),
        Property(name="supersedingVersions", type=feature_HyVersion, multiplicity=Multiplicity(0, 1))
    }
)
enumType31: BinaryAssociation = BinaryAssociation(
    name="enumType31",
    ends={
        Property(name="feature_HyEnum32", type=feature_HyEnumAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="feature_HyEnumAttribute", type=feature_HyEnum, multiplicity=Multiplicity(1, 1))
    }
)
feature23: BinaryAssociation = BinaryAssociation(
    name="feature23",
    ends={
        Property(name="HyFeature24", type=feature_HyVersion, multiplicity=Multiplicity(1, 1)),
        Property(name="versions", type=feature_HyFeature, multiplicity=Multiplicity(1, 1))
    }
)
feature37: BinaryAssociation = BinaryAssociation(
    name="feature37",
    ends={
        Property(name="feature_HyFeature39", type=feature_HyRootFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="feature_HyRootFeature38", type=feature_HyFeature, multiplicity=Multiplicity(1, 1))
    }
)
compositionOf40: BinaryAssociation = BinaryAssociation(
    name="compositionOf40",
    ends={
        Property(name="HyGroup41", type=feature_HyGroupComposition, multiplicity=Multiplicity(1, 1)),
        Property(name="parentOf", type=feature_HyGroup, multiplicity=Multiplicity(1, 1))
    }
)
features42: BinaryAssociation = BinaryAssociation(
    name="features42",
    ends={
        Property(name="HyFeature43", type=feature_HyGroupComposition, multiplicity=Multiplicity(1, 1)),
        Property(name="groupMembership", type=feature_HyFeature, multiplicity=Multiplicity(1, 9999))
    }
)
parent44: BinaryAssociation = BinaryAssociation(
    name="parent44",
    ends={
        Property(name="HyFeature46", type=feature_HyFeatureChild, multiplicity=Multiplicity(1, 1)),
        Property(name="parentOf45", type=feature_HyFeature, multiplicity=Multiplicity(1, 1))
    }
)
childGroup47: BinaryAssociation = BinaryAssociation(
    name="childGroup47",
    ends={
        Property(name="HyGroup48", type=feature_HyFeatureChild, multiplicity=Multiplicity(1, 1)),
        Property(name="childOf", type=feature_HyGroup, multiplicity=Multiplicity(1, 1))
    }
)
default33: BinaryAssociation = BinaryAssociation(
    name="default33",
    ends={
        Property(name="feature_HyEnumLiteral", type=feature_HyEnumAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="feature_HyEnumAttribute34", type=feature_HyEnumLiteral, multiplicity=Multiplicity(1, 1))
    }
)
feature35: BinaryAssociation = BinaryAssociation(
    name="feature35",
    ends={
        Property(name="HyFeature36", type=feature_HyFeatureAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attributes", type=feature_HyFeature, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_feature_HyFeature_HyTemporalElement = Generalization(general=HyTemporalElement, specific=feature_HyFeature)
gen_feature_HyFeature_HyNamedElement = Generalization(general=HyNamedElement, specific=feature_HyFeature)
gen_feature_HyGroup_HyTemporalElement = Generalization(general=HyTemporalElement, specific=feature_HyGroup)
gen_feature_HyVersion_HyTemporalElement = Generalization(general=HyTemporalElement, specific=feature_HyVersion)
gen_feature_HyNumberAttribute_HyFeatureAttribute = Generalization(general=HyFeatureAttribute, specific=feature_HyNumberAttribute)
gen_feature_HyBooleanAttribute_HyFeatureAttribute = Generalization(general=HyFeatureAttribute, specific=feature_HyBooleanAttribute)
gen_feature_HyStringAttribute_HyFeatureAttribute = Generalization(general=HyFeatureAttribute, specific=feature_HyStringAttribute)
gen_feature_HyEnumAttribute_HyFeatureAttribute = Generalization(general=HyFeatureAttribute, specific=feature_HyEnumAttribute)
gen_feature_HyRootFeature_HyLinearTemporalElement = Generalization(general=HyLinearTemporalElement, specific=feature_HyRootFeature)
gen_feature_HyGroupComposition_HyLinearTemporalElement = Generalization(general=HyLinearTemporalElement, specific=feature_HyGroupComposition)
gen_feature_HyFeatureChild_HyLinearTemporalElement = Generalization(general=HyLinearTemporalElement, specific=feature_HyFeatureChild)
gen_feature_HyFeatureAttribute_HyTemporalElement = Generalization(general=HyTemporalElement, specific=feature_HyFeatureAttribute)
gen_feature_HyFeatureAttribute_HyNamedElement = Generalization(general=HyNamedElement, specific=feature_HyFeatureAttribute)
gen_feature_HyFeatureType_HyLinearTemporalElement = Generalization(general=HyLinearTemporalElement, specific=feature_HyFeatureType)
gen_feature_HyGroupType_HyLinearTemporalElement = Generalization(general=HyLinearTemporalElement, specific=feature_HyGroupType)

# Domain Model
domain_model = DomainModel(
    name="feature",
    types={feature_HyFeatureModel, feature_HyRootFeature, feature_HyFeature, feature_HyEnum, feature_HyContextModel, HyTemporalElement, HyNamedElement, feature_HyVersion, feature_HyGroupComposition, feature_HyFeatureChild, feature_HyFeatureAttribute, feature_HyGroup, feature_HyGroupType, feature_HyFeatureType, feature_HyNumberAttribute, HyFeatureAttribute, feature_HyBooleanAttribute, feature_HyStringAttribute, feature_HyEnumAttribute, feature_HyEnumLiteral, HyLinearTemporalElement, HyFeatureTypeEnum, HyGroupTypeEnum},
    associations={rootFeature0, features1, enums4, contexts6, versions8, groupMembership9, parentOf10, attributes11, groups2, types13, featureModel14, parentOf16, childOf18, types20, featureModel21, supersedingVersions26, supersededVersion29, enumType31, feature23, feature37, compositionOf40, features42, parent44, childGroup47, default33, feature35},
    generalizations={gen_feature_HyFeature_HyTemporalElement, gen_feature_HyFeature_HyNamedElement, gen_feature_HyGroup_HyTemporalElement, gen_feature_HyVersion_HyTemporalElement, gen_feature_HyNumberAttribute_HyFeatureAttribute, gen_feature_HyBooleanAttribute_HyFeatureAttribute, gen_feature_HyStringAttribute_HyFeatureAttribute, gen_feature_HyEnumAttribute_HyFeatureAttribute, gen_feature_HyRootFeature_HyLinearTemporalElement, gen_feature_HyGroupComposition_HyLinearTemporalElement, gen_feature_HyFeatureChild_HyLinearTemporalElement, gen_feature_HyFeatureAttribute_HyTemporalElement, gen_feature_HyFeatureAttribute_HyNamedElement, gen_feature_HyFeatureType_HyLinearTemporalElement, gen_feature_HyGroupType_HyLinearTemporalElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)