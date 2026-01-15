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
feature_FeatureModel = Class(name="feature::FeatureModel")
HybridDimension = Class(name="HybridDimension")
feature_RootRelationship = Class(name="feature::RootRelationship")
feature_Feature = Class(name="feature::Feature")
HybridElement = Class(name="HybridElement")
UUIDElement = Class(name="UUIDElement")
feature_FeatureGroup = Class(name="feature::FeatureGroup", is_abstract=True)
feature_GroupMembership = Class(name="feature::GroupMembership")
feature_FeatureDependency = Class(name="feature::FeatureDependency", is_abstract=True)
feature_Mandatory = Class(name="feature::Mandatory")
feature_Elimination = Class(name="feature::Elimination")
feature_Option = Class(name="feature::Option")
feature_DisplayName = Class(name="feature::DisplayName")
feature_ChildRelationship = Class(name="feature::ChildRelationship")
feature_Invariant = Class(name="feature::Invariant")
feature_OrFeatureGroup = Class(name="feature::OrFeatureGroup")
FeatureGroup = Class(name="FeatureGroup")
feature_XorFeatureGroup = Class(name="feature::XorFeatureGroup")
feature_FeatureRequirement = Class(name="feature::FeatureRequirement")
FeatureDependency = Class(name="FeatureDependency")
feature_FeatureExclusion = Class(name="feature::FeatureExclusion")
feature_Preference = Class(name="feature::Preference")
feature_DefaultBinding = Class(name="feature::DefaultBinding")

# feature_FeatureModel class attributes and methods

# HybridDimension class attributes and methods

# feature_RootRelationship class attributes and methods

# feature_Feature class attributes and methods
feature_Feature_transitiveEliminationState: Property = Property(name="transitiveEliminationState", type=StringType)
feature_Feature.attributes={feature_Feature_transitiveEliminationState}

# HybridElement class attributes and methods

# UUIDElement class attributes and methods

# feature_FeatureGroup class attributes and methods

# feature_GroupMembership class attributes and methods

# feature_FeatureDependency class attributes and methods

# feature_Mandatory class attributes and methods

# feature_Elimination class attributes and methods
feature_Elimination_defaultSelection: Property = Property(name="defaultSelection", type=StringType)
feature_Elimination.attributes={feature_Elimination_defaultSelection}

# feature_Option class attributes and methods

# feature_DisplayName class attributes and methods
feature_DisplayName_displayName: Property = Property(name="displayName", type=StringType)
feature_DisplayName.attributes={feature_DisplayName_displayName}

# feature_ChildRelationship class attributes and methods

# feature_Invariant class attributes and methods

# feature_OrFeatureGroup class attributes and methods

# FeatureGroup class attributes and methods

# feature_XorFeatureGroup class attributes and methods

# feature_FeatureRequirement class attributes and methods

# FeatureDependency class attributes and methods

# feature_FeatureExclusion class attributes and methods

# feature_Preference class attributes and methods

# feature_DefaultBinding class attributes and methods

# Relationships
roots0: BinaryAssociation = BinaryAssociation(
    name="roots0",
    ends={
        Property(name="feature_RootRelationship", type=feature_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="feature_FeatureModel", type=feature_RootRelationship, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
features1: BinaryAssociation = BinaryAssociation(
    name="features1",
    ends={
        Property(name="Feature", type=feature_FeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="featureModel", type=feature_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
featureModel2: BinaryAssociation = BinaryAssociation(
    name="featureModel2",
    ends={
        Property(name="FeatureModel", type=feature_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="features", type=feature_FeatureModel, multiplicity=Multiplicity(0, 1))
    }
)
parents6: BinaryAssociation = BinaryAssociation(
    name="parents6",
    ends={
        Property(name="ChildRelationship7", type=feature_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="child", type=feature_ChildRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
groups8: BinaryAssociation = BinaryAssociation(
    name="groups8",
    ends={
        Property(name="FeatureGroup", type=feature_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="parentFeature", type=feature_FeatureGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
groupedBy9: BinaryAssociation = BinaryAssociation(
    name="groupedBy9",
    ends={
        Property(name="GroupMembership", type=feature_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="groupedFeature", type=feature_GroupMembership, multiplicity=Multiplicity(0, 9999))
    }
)
incomingDependencies10: BinaryAssociation = BinaryAssociation(
    name="incomingDependencies10",
    ends={
        Property(name="FeatureDependency", type=feature_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="targetFeature", type=feature_FeatureDependency, multiplicity=Multiplicity(0, 9999))
    }
)
outgoingDependencies11: BinaryAssociation = BinaryAssociation(
    name="outgoingDependencies11",
    ends={
        Property(name="FeatureDependency12", type=feature_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="sourceFeature", type=feature_FeatureDependency, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mandatory13: BinaryAssociation = BinaryAssociation(
    name="mandatory13",
    ends={
        Property(name="Mandatory", type=feature_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="feature14", type=feature_Mandatory, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
featureOption3: BinaryAssociation = BinaryAssociation(
    name="featureOption3",
    ends={
        Property(name="feature_Option", type=feature_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="feature_Feature", type=feature_Option, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
names4: BinaryAssociation = BinaryAssociation(
    name="names4",
    ends={
        Property(name="DisplayName", type=feature_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="feature", type=feature_DisplayName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
children5: BinaryAssociation = BinaryAssociation(
    name="children5",
    ends={
        Property(name="ChildRelationship", type=feature_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=feature_ChildRelationship, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
feature22: BinaryAssociation = BinaryAssociation(
    name="feature22",
    ends={
        Property(name="Feature23", type=feature_DisplayName, multiplicity=Multiplicity(1, 1)),
        Property(name="names", type=feature_Feature, multiplicity=Multiplicity(0, 1))
    }
)
groupedFeatures24: BinaryAssociation = BinaryAssociation(
    name="groupedFeatures24",
    ends={
        Property(name="GroupMembership25", type=feature_FeatureGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="group", type=feature_GroupMembership, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
groupInvariant26: BinaryAssociation = BinaryAssociation(
    name="groupInvariant26",
    ends={
        Property(name="feature_Invariant", type=feature_FeatureGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="feature_FeatureGroup", type=feature_Invariant, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parentFeature27: BinaryAssociation = BinaryAssociation(
    name="parentFeature27",
    ends={
        Property(name="Feature28", type=feature_FeatureGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="groups", type=feature_Feature, multiplicity=Multiplicity(0, 1))
    }
)
eliminations15: BinaryAssociation = BinaryAssociation(
    name="eliminations15",
    ends={
        Property(name="Elimination", type=feature_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="feature16", type=feature_Elimination, multiplicity=Multiplicity(0, 2), is_composite=True)
    }
)
incomingRoots17: BinaryAssociation = BinaryAssociation(
    name="incomingRoots17",
    ends={
        Property(name="RootRelationship", type=feature_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="feature18", type=feature_RootRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
allChildFeatures20: BinaryAssociation = BinaryAssociation(
    name="allChildFeatures20",
    ends={
        Property(name="feature_Feature21", type=feature_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="feature_Feature19", type=feature_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
dependencyInvariant33: BinaryAssociation = BinaryAssociation(
    name="dependencyInvariant33",
    ends={
        Property(name="feature_Invariant34", type=feature_FeatureDependency, multiplicity=Multiplicity(1, 1)),
        Property(name="feature_FeatureDependency", type=feature_Invariant, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sourceFeature35: BinaryAssociation = BinaryAssociation(
    name="sourceFeature35",
    ends={
        Property(name="Feature36", type=feature_FeatureDependency, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingDependencies", type=feature_Feature, multiplicity=Multiplicity(0, 1))
    }
)
targetFeature37: BinaryAssociation = BinaryAssociation(
    name="targetFeature37",
    ends={
        Property(name="Feature38", type=feature_FeatureDependency, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingDependencies", type=feature_Feature, multiplicity=Multiplicity(0, 1))
    }
)
groupedFeature29: BinaryAssociation = BinaryAssociation(
    name="groupedFeature29",
    ends={
        Property(name="Feature30", type=feature_GroupMembership, multiplicity=Multiplicity(1, 1)),
        Property(name="groupedBy", type=feature_Feature, multiplicity=Multiplicity(0, 1))
    }
)
group31: BinaryAssociation = BinaryAssociation(
    name="group31",
    ends={
        Property(name="FeatureGroup32", type=feature_GroupMembership, multiplicity=Multiplicity(1, 1)),
        Property(name="groupedFeatures", type=feature_FeatureGroup, multiplicity=Multiplicity(0, 1))
    }
)
parent46: BinaryAssociation = BinaryAssociation(
    name="parent46",
    ends={
        Property(name="Feature47", type=feature_ChildRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=feature_Feature, multiplicity=Multiplicity(0, 1))
    }
)
child48: BinaryAssociation = BinaryAssociation(
    name="child48",
    ends={
        Property(name="Feature49", type=feature_ChildRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="parents", type=feature_Feature, multiplicity=Multiplicity(0, 1))
    }
)
parentInvariant50: BinaryAssociation = BinaryAssociation(
    name="parentInvariant50",
    ends={
        Property(name="feature_Invariant51", type=feature_ChildRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="feature_ChildRelationship", type=feature_Invariant, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parentPreference52: BinaryAssociation = BinaryAssociation(
    name="parentPreference52",
    ends={
        Property(name="feature_Preference", type=feature_ChildRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="feature_ChildRelationship53", type=feature_Preference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
feature54: BinaryAssociation = BinaryAssociation(
    name="feature54",
    ends={
        Property(name="Feature55", type=feature_Mandatory, multiplicity=Multiplicity(1, 1)),
        Property(name="mandatory", type=feature_Feature, multiplicity=Multiplicity(0, 1))
    }
)
rootInvariant39: BinaryAssociation = BinaryAssociation(
    name="rootInvariant39",
    ends={
        Property(name="feature_Invariant41", type=feature_RootRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="feature_RootRelationship40", type=feature_Invariant, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rootDefault42: BinaryAssociation = BinaryAssociation(
    name="rootDefault42",
    ends={
        Property(name="feature_DefaultBinding", type=feature_RootRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="feature_RootRelationship43", type=feature_DefaultBinding, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
feature44: BinaryAssociation = BinaryAssociation(
    name="feature44",
    ends={
        Property(name="Feature45", type=feature_RootRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingRoots", type=feature_Feature, multiplicity=Multiplicity(0, 1))
    }
)
eliminationDefault60: BinaryAssociation = BinaryAssociation(
    name="eliminationDefault60",
    ends={
        Property(name="feature_DefaultBinding62", type=feature_Elimination, multiplicity=Multiplicity(1, 1)),
        Property(name="feature_Elimination61", type=feature_DefaultBinding, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
feature56: BinaryAssociation = BinaryAssociation(
    name="feature56",
    ends={
        Property(name="Feature57", type=feature_Elimination, multiplicity=Multiplicity(1, 1)),
        Property(name="eliminations", type=feature_Feature, multiplicity=Multiplicity(0, 1))
    }
)
eliminationInvariant58: BinaryAssociation = BinaryAssociation(
    name="eliminationInvariant58",
    ends={
        Property(name="feature_Invariant59", type=feature_Elimination, multiplicity=Multiplicity(1, 1)),
        Property(name="feature_Elimination", type=feature_Invariant, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_feature_FeatureModel_HybridDimension = Generalization(general=HybridDimension, specific=feature_FeatureModel)
gen_feature_Feature_HybridElement = Generalization(general=HybridElement, specific=feature_Feature)
gen_feature_Feature_UUIDElement = Generalization(general=UUIDElement, specific=feature_Feature)
gen_feature_DisplayName_HybridElement = Generalization(general=HybridElement, specific=feature_DisplayName)
gen_feature_FeatureGroup_HybridElement = Generalization(general=HybridElement, specific=feature_FeatureGroup)
gen_feature_FeatureGroup_UUIDElement = Generalization(general=UUIDElement, specific=feature_FeatureGroup)
gen_feature_OrFeatureGroup_FeatureGroup = Generalization(general=FeatureGroup, specific=feature_OrFeatureGroup)
gen_feature_XorFeatureGroup_FeatureGroup = Generalization(general=FeatureGroup, specific=feature_XorFeatureGroup)
gen_feature_FeatureDependency_HybridElement = Generalization(general=HybridElement, specific=feature_FeatureDependency)
gen_feature_FeatureDependency_UUIDElement = Generalization(general=UUIDElement, specific=feature_FeatureDependency)
gen_feature_FeatureRequirement_FeatureDependency = Generalization(general=FeatureDependency, specific=feature_FeatureRequirement)
gen_feature_FeatureExclusion_FeatureDependency = Generalization(general=FeatureDependency, specific=feature_FeatureExclusion)
gen_feature_RootRelationship_HybridElement = Generalization(general=HybridElement, specific=feature_RootRelationship)
gen_feature_GroupMembership_HybridElement = Generalization(general=HybridElement, specific=feature_GroupMembership)
gen_feature_ChildRelationship_HybridElement = Generalization(general=HybridElement, specific=feature_ChildRelationship)
gen_feature_Mandatory_HybridElement = Generalization(general=HybridElement, specific=feature_Mandatory)
gen_feature_Elimination_HybridElement = Generalization(general=HybridElement, specific=feature_Elimination)

# Domain Model
domain_model = DomainModel(
    name="feature",
    types={feature_FeatureModel, HybridDimension, feature_RootRelationship, feature_Feature, HybridElement, UUIDElement, feature_FeatureGroup, feature_GroupMembership, feature_FeatureDependency, feature_Mandatory, feature_Elimination, feature_Option, feature_DisplayName, feature_ChildRelationship, feature_Invariant, feature_OrFeatureGroup, FeatureGroup, feature_XorFeatureGroup, feature_FeatureRequirement, FeatureDependency, feature_FeatureExclusion, feature_Preference, feature_DefaultBinding},
    associations={roots0, features1, featureModel2, parents6, groups8, groupedBy9, incomingDependencies10, outgoingDependencies11, mandatory13, featureOption3, names4, children5, feature22, groupedFeatures24, groupInvariant26, parentFeature27, eliminations15, incomingRoots17, allChildFeatures20, dependencyInvariant33, sourceFeature35, targetFeature37, groupedFeature29, group31, parent46, child48, parentInvariant50, parentPreference52, feature54, rootInvariant39, rootDefault42, feature44, eliminationDefault60, feature56, eliminationInvariant58},
    generalizations={gen_feature_FeatureModel_HybridDimension, gen_feature_Feature_HybridElement, gen_feature_Feature_UUIDElement, gen_feature_DisplayName_HybridElement, gen_feature_FeatureGroup_HybridElement, gen_feature_FeatureGroup_UUIDElement, gen_feature_OrFeatureGroup_FeatureGroup, gen_feature_XorFeatureGroup_FeatureGroup, gen_feature_FeatureDependency_HybridElement, gen_feature_FeatureDependency_UUIDElement, gen_feature_FeatureRequirement_FeatureDependency, gen_feature_FeatureExclusion_FeatureDependency, gen_feature_RootRelationship_HybridElement, gen_feature_GroupMembership_HybridElement, gen_feature_ChildRelationship_HybridElement, gen_feature_Mandatory_HybridElement, gen_feature_Elimination_HybridElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)