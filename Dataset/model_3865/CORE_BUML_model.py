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
COREFeatureRelationshipType: Enumeration = Enumeration(
    name="COREFeatureRelationshipType",
    literals={
            EnumerationLiteral(name="None"),
			EnumerationLiteral(name="Optional"),
			EnumerationLiteral(name="Mandatory"),
			EnumerationLiteral(name="XOR"),
			EnumerationLiteral(name="OR")
    }
)

COREVisibilityType: Enumeration = Enumeration(
    name="COREVisibilityType",
    literals={
            EnumerationLiteral(name="public"),
			EnumerationLiteral(name="concern")
    }
)

COREPartialityType: Enumeration = Enumeration(
    name="COREPartialityType",
    literals={
            EnumerationLiteral(name="none"),
			EnumerationLiteral(name="public"),
			EnumerationLiteral(name="concern")
    }
)

# Classes
core_COREModel = Class(name="core::COREModel", is_abstract=True)
core_COREInterface = Class(name="core::COREInterface")
core_COREFeatureModel = Class(name="core::COREFeatureModel")
COREModelElement = Class(name="COREModelElement")
core_COREReuse = Class(name="core::COREReuse")
CORENamedElement = Class(name="CORENamedElement")
core_COREModelReuse = Class(name="core::COREModelReuse")
core_COREModelElement = Class(name="core::COREModelElement", is_abstract=True)
core_COREFeature = Class(name="core::COREFeature")
core_COREConcern = Class(name="core::COREConcern")
core_COREImpactModel = Class(name="core::COREImpactModel")
COREModel = Class(name="COREModel")
core_COREImpactNode = Class(name="core::COREImpactNode")
core_LayoutContainerMap = Class(name="core::LayoutContainerMap")
core_COREContribution = Class(name="core::COREContribution")
core_COREMapping = Class(name="core::COREMapping", is_abstract=True)
core_CORENamedElement = Class(name="core::CORENamedElement", is_abstract=True)
core_CORERelativity = Class(name="core::CORERelativity")
core_CORERelativity_Opt2 = Class(name="core::CORERelativity::Opt2")
core_COREBinding = Class(name="core::COREBinding", is_abstract=True)
core_CORECompositionSpecification = Class(name="core::CORECompositionSpecification", is_abstract=True)
core_COREConcernConfiguration = Class(name="core::COREConcernConfiguration")
core_COREConfiguration = Class(name="core::COREConfiguration", is_abstract=True)
core_COREReuseConfiguration = Class(name="core::COREReuseConfiguration")
core_COREPattern = Class(name="core::COREPattern", is_abstract=True)
core_COREFeatureImpactNode = Class(name="core::COREFeatureImpactNode")
COREImpactNode = Class(name="COREImpactNode")
core_COREWeightedMapping = Class(name="core::COREWeightedMapping")
core_COREModelCompositionSpecification = Class(name="core::COREModelCompositionSpecification", is_abstract=True)
core_LayoutMap = Class(name="core::LayoutMap")
core_EObject = Class(name="core::EObject")
core_LayoutElement = Class(name="core::LayoutElement")
core_COREImpactModelBinding = Class(name="core::COREImpactModelBinding")
COREConfiguration = Class(name="COREConfiguration")

# core_COREModel class attributes and methods

# core_COREInterface class attributes and methods

# core_COREFeatureModel class attributes and methods

# COREModelElement class attributes and methods

# core_COREReuse class attributes and methods

# CORENamedElement class attributes and methods

# core_COREModelReuse class attributes and methods

# core_COREModelElement class attributes and methods
core_COREModelElement_partiality: Property = Property(name="partiality", type=StringType)
core_COREModelElement_visibility: Property = Property(name="visibility", type=StringType)
core_COREModelElement.attributes={core_COREModelElement_visibility, core_COREModelElement_partiality}

# core_COREFeature class attributes and methods
core_COREFeature_parentRelationship: Property = Property(name="parentRelationship", type=StringType)
core_COREFeature.attributes={core_COREFeature_parentRelationship}

# core_COREConcern class attributes and methods

# core_COREImpactModel class attributes and methods

# COREModel class attributes and methods

# core_COREImpactNode class attributes and methods
core_COREImpactNode_scalingFactor: Property = Property(name="scalingFactor", type=FloatType)
core_COREImpactNode_offset: Property = Property(name="offset", type=FloatType)
core_COREImpactNode.attributes={core_COREImpactNode_offset, core_COREImpactNode_scalingFactor}

# core_LayoutContainerMap class attributes and methods

# core_COREContribution class attributes and methods
core_COREContribution_relativeWeight: Property = Property(name="relativeWeight", type=IntegerType)
core_COREContribution.attributes={core_COREContribution_relativeWeight}

# core_COREMapping class attributes and methods

# core_CORENamedElement class attributes and methods
core_CORENamedElement_name: Property = Property(name="name", type=StringType)
core_CORENamedElement.attributes={core_CORENamedElement_name}

# core_CORERelativity class attributes and methods
core_CORERelativity_probabilisticValue: Property = Property(name="probabilisticValue", type=FloatType)
core_CORERelativity.attributes={core_CORERelativity_probabilisticValue}

# core_CORERelativity_Opt2 class attributes and methods
core_CORERelativity_Opt2_probabilisticValue: Property = Property(name="probabilisticValue", type=FloatType)
core_CORERelativity_Opt2.attributes={core_CORERelativity_Opt2_probabilisticValue}

# core_COREBinding class attributes and methods

# core_CORECompositionSpecification class attributes and methods

# core_COREConcernConfiguration class attributes and methods

# core_COREConfiguration class attributes and methods

# core_COREReuseConfiguration class attributes and methods

# core_COREPattern class attributes and methods

# core_COREFeatureImpactNode class attributes and methods
core_COREFeatureImpactNode_relativeFeatureWeight: Property = Property(name="relativeFeatureWeight", type=IntegerType)
core_COREFeatureImpactNode.attributes={core_COREFeatureImpactNode_relativeFeatureWeight}

# COREImpactNode class attributes and methods

# core_COREWeightedMapping class attributes and methods
core_COREWeightedMapping_weight: Property = Property(name="weight", type=IntegerType)
core_COREWeightedMapping.attributes={core_COREWeightedMapping_weight}

# core_COREModelCompositionSpecification class attributes and methods

# core_LayoutMap class attributes and methods

# core_EObject class attributes and methods

# core_LayoutElement class attributes and methods
core_LayoutElement_x: Property = Property(name="x", type=FloatType)
core_LayoutElement_y: Property = Property(name="y", type=FloatType)
core_LayoutElement.attributes={core_LayoutElement_x, core_LayoutElement_y}

# core_COREImpactModelBinding class attributes and methods

# COREConfiguration class attributes and methods

# Relationships
interface11: BinaryAssociation = BinaryAssociation(
    name="interface11",
    ends={
        Property(name="core_COREInterface", type=core_COREConcern, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREConcern", type=core_COREInterface, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
featureModel12: BinaryAssociation = BinaryAssociation(
    name="featureModel12",
    ends={
        Property(name="core_COREFeatureModel", type=core_COREConcern, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREConcern13", type=core_COREFeatureModel, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
impactModel14: BinaryAssociation = BinaryAssociation(
    name="impactModel14",
    ends={
        Property(name="core_COREImpactModel16", type=core_COREConcern, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREConcern15", type=core_COREImpactModel, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
realizedBy17: BinaryAssociation = BinaryAssociation(
    name="realizedBy17",
    ends={
        Property(name="COREModel18", type=core_COREFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="realizes", type=core_COREModel, multiplicity=Multiplicity(0, 9999))
    }
)
reuses19: BinaryAssociation = BinaryAssociation(
    name="reuses19",
    ends={
        Property(name="core_COREReuse", type=core_COREFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREFeature", type=core_COREReuse, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modelReuses0: BinaryAssociation = BinaryAssociation(
    name="modelReuses0",
    ends={
        Property(name="core_COREModelReuse", type=core_COREModel, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREModel", type=core_COREModelReuse, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modelElements1: BinaryAssociation = BinaryAssociation(
    name="modelElements1",
    ends={
        Property(name="core_COREModelElement", type=core_COREModel, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREModel2", type=core_COREModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
realizes3: BinaryAssociation = BinaryAssociation(
    name="realizes3",
    ends={
        Property(name="COREFeature", type=core_COREModel, multiplicity=Multiplicity(1, 1)),
        Property(name="realizedBy", type=core_COREFeature, multiplicity=Multiplicity(0, 9999))
    }
)
coreConcern4: BinaryAssociation = BinaryAssociation(
    name="coreConcern4",
    ends={
        Property(name="COREConcern", type=core_COREModel, multiplicity=Multiplicity(1, 1)),
        Property(name="models", type=core_COREConcern, multiplicity=Multiplicity(1, 1))
    }
)
impactModelElements5: BinaryAssociation = BinaryAssociation(
    name="impactModelElements5",
    ends={
        Property(name="core_COREImpactNode", type=core_COREImpactModel, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREImpactModel", type=core_COREImpactNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
layouts6: BinaryAssociation = BinaryAssociation(
    name="layouts6",
    ends={
        Property(name="core_LayoutContainerMap", type=core_COREImpactModel, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREImpactModel7", type=core_LayoutContainerMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contributions8: BinaryAssociation = BinaryAssociation(
    name="contributions8",
    ends={
        Property(name="core_COREContribution", type=core_COREImpactModel, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREImpactModel9", type=core_COREContribution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
models10: BinaryAssociation = BinaryAssociation(
    name="models10",
    ends={
        Property(name="COREModel", type=core_COREConcern, multiplicity=Multiplicity(1, 1)),
        Property(name="coreConcern", type=core_COREModel, multiplicity=Multiplicity(1, 9999))
    }
)
selectable37: BinaryAssociation = BinaryAssociation(
    name="selectable37",
    ends={
        Property(name="core_COREFeature39", type=core_COREInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREInterface38", type=core_COREFeature, multiplicity=Multiplicity(0, 9999))
    }
)
customizable40: BinaryAssociation = BinaryAssociation(
    name="customizable40",
    ends={
        Property(name="core_COREModelElement42", type=core_COREInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREInterface41", type=core_COREModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
children21: BinaryAssociation = BinaryAssociation(
    name="children21",
    ends={
        Property(name="COREFeature22", type=core_COREFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=core_COREFeature, multiplicity=Multiplicity(0, 9999))
    }
)
parent24: BinaryAssociation = BinaryAssociation(
    name="parent24",
    ends={
        Property(name="COREFeature25", type=core_COREFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=core_COREFeature, multiplicity=Multiplicity(0, 1))
    }
)
requires27: BinaryAssociation = BinaryAssociation(
    name="requires27",
    ends={
        Property(name="core_COREFeature28", type=core_COREFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREFeature26", type=core_COREFeature, multiplicity=Multiplicity(0, 9999))
    }
)
excludes30: BinaryAssociation = BinaryAssociation(
    name="excludes30",
    ends={
        Property(name="core_COREFeature31", type=core_COREFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREFeature29", type=core_COREFeature, multiplicity=Multiplicity(0, 9999))
    }
)
relatedTo32: BinaryAssociation = BinaryAssociation(
    name="relatedTo32",
    ends={
        Property(name="core_CORERelativity", type=core_COREFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREFeature33", type=core_CORERelativity, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing34: BinaryAssociation = BinaryAssociation(
    name="outgoing34",
    ends={
        Property(name="CORERelativity_Opt2", type=core_COREFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=core_CORERelativity_Opt2, multiplicity=Multiplicity(0, 9999))
    }
)
incoming35: BinaryAssociation = BinaryAssociation(
    name="incoming35",
    ends={
        Property(name="CORERelativity_Opt236", type=core_COREFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="features", type=core_CORERelativity_Opt2, multiplicity=Multiplicity(0, 9999))
    }
)
reexposed69: BinaryAssociation = BinaryAssociation(
    name="reexposed69",
    ends={
        Property(name="core_COREFeature71", type=core_COREConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREConfiguration70", type=core_COREFeature, multiplicity=Multiplicity(0, 9999))
    }
)
extendingConfigurations72: BinaryAssociation = BinaryAssociation(
    name="extendingConfigurations72",
    ends={
        Property(name="core_COREReuseConfiguration74", type=core_COREConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREConfiguration73", type=core_COREReuseConfiguration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
features75: BinaryAssociation = BinaryAssociation(
    name="features75",
    ends={
        Property(name="core_COREFeature77", type=core_COREFeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREFeatureModel76", type=core_COREFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
root78: BinaryAssociation = BinaryAssociation(
    name="root78",
    ends={
        Property(name="core_COREFeature80", type=core_COREFeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREFeatureModel79", type=core_COREFeature, multiplicity=Multiplicity(1, 1))
    }
)
configurations81: BinaryAssociation = BinaryAssociation(
    name="configurations81",
    ends={
        Property(name="core_COREConcernConfiguration", type=core_COREFeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREFeatureModel82", type=core_COREConcernConfiguration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usable43: BinaryAssociation = BinaryAssociation(
    name="usable43",
    ends={
        Property(name="core_COREModelElement45", type=core_COREInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREInterface44", type=core_COREModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
impacted46: BinaryAssociation = BinaryAssociation(
    name="impacted46",
    ends={
        Property(name="core_COREImpactNode48", type=core_COREInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREInterface47", type=core_COREImpactNode, multiplicity=Multiplicity(0, 9999))
    }
)
defaults49: BinaryAssociation = BinaryAssociation(
    name="defaults49",
    ends={
        Property(name="core_COREConfiguration", type=core_COREInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREInterface50", type=core_COREConfiguration, multiplicity=Multiplicity(0, 9999))
    }
)
reusedConcern51: BinaryAssociation = BinaryAssociation(
    name="reusedConcern51",
    ends={
        Property(name="core_COREConcern53", type=core_COREReuse, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREReuse52", type=core_COREConcern, multiplicity=Multiplicity(1, 1))
    }
)
configurations54: BinaryAssociation = BinaryAssociation(
    name="configurations54",
    ends={
        Property(name="core_COREReuseConfiguration", type=core_COREReuse, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREReuse55", type=core_COREReuseConfiguration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
selectedConfiguration56: BinaryAssociation = BinaryAssociation(
    name="selectedConfiguration56",
    ends={
        Property(name="core_COREReuseConfiguration58", type=core_COREReuse, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREReuse57", type=core_COREReuseConfiguration, multiplicity=Multiplicity(0, 1))
    }
)
extends60: BinaryAssociation = BinaryAssociation(
    name="extends60",
    ends={
        Property(name="core_COREReuse61", type=core_COREReuse, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREReuse59", type=core_COREReuse, multiplicity=Multiplicity(0, 1))
    }
)
outgoing62: BinaryAssociation = BinaryAssociation(
    name="outgoing62",
    ends={
        Property(name="COREContribution", type=core_COREImpactNode, multiplicity=Multiplicity(1, 1)),
        Property(name="source63", type=core_COREContribution, multiplicity=Multiplicity(0, 9999))
    }
)
incoming64: BinaryAssociation = BinaryAssociation(
    name="incoming64",
    ends={
        Property(name="COREContribution65", type=core_COREImpactNode, multiplicity=Multiplicity(1, 1)),
        Property(name="impacts", type=core_COREContribution, multiplicity=Multiplicity(0, 9999))
    }
)
selected66: BinaryAssociation = BinaryAssociation(
    name="selected66",
    ends={
        Property(name="core_COREFeature68", type=core_COREConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREConfiguration67", type=core_COREFeature, multiplicity=Multiplicity(0, 9999))
    }
)
key97: BinaryAssociation = BinaryAssociation(
    name="key97",
    ends={
        Property(name="core_EObject99", type=core_LayoutContainerMap, multiplicity=Multiplicity(1, 1)),
        Property(name="core_LayoutContainerMap98", type=core_EObject, multiplicity=Multiplicity(1, 1))
    }
)
value100: BinaryAssociation = BinaryAssociation(
    name="value100",
    ends={
        Property(name="core_LayoutMap102", type=core_LayoutContainerMap, multiplicity=Multiplicity(1, 1)),
        Property(name="core_LayoutContainerMap101", type=core_LayoutMap, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
represents103: BinaryAssociation = BinaryAssociation(
    name="represents103",
    ends={
        Property(name="core_COREFeature104", type=core_COREFeatureImpactNode, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREFeatureImpactNode", type=core_COREFeature, multiplicity=Multiplicity(1, 1))
    }
)
weightedMappings105: BinaryAssociation = BinaryAssociation(
    name="weightedMappings105",
    ends={
        Property(name="core_COREWeightedMapping", type=core_COREFeatureImpactNode, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREFeatureImpactNode106", type=core_COREWeightedMapping, multiplicity=Multiplicity(0, 9999))
    }
)
defaultConfiguration83: BinaryAssociation = BinaryAssociation(
    name="defaultConfiguration83",
    ends={
        Property(name="core_COREConcernConfiguration85", type=core_COREFeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREFeatureModel84", type=core_COREConcernConfiguration, multiplicity=Multiplicity(0, 1))
    }
)
relatedFeatures86: BinaryAssociation = BinaryAssociation(
    name="relatedFeatures86",
    ends={
        Property(name="core_CORERelativity_Opt2", type=core_COREFeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREFeatureModel87", type=core_CORERelativity_Opt2, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reuse88: BinaryAssociation = BinaryAssociation(
    name="reuse88",
    ends={
        Property(name="core_COREReuse90", type=core_COREModelReuse, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREModelReuse89", type=core_COREReuse, multiplicity=Multiplicity(1, 1))
    }
)
source91: BinaryAssociation = BinaryAssociation(
    name="source91",
    ends={
        Property(name="COREImpactNode", type=core_COREContribution, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=core_COREImpactNode, multiplicity=Multiplicity(1, 1))
    }
)
impacts92: BinaryAssociation = BinaryAssociation(
    name="impacts92",
    ends={
        Property(name="COREImpactNode93", type=core_COREContribution, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=core_COREImpactNode, multiplicity=Multiplicity(1, 1))
    }
)
key94: BinaryAssociation = BinaryAssociation(
    name="key94",
    ends={
        Property(name="core_EObject", type=core_LayoutMap, multiplicity=Multiplicity(1, 1)),
        Property(name="core_LayoutMap", type=core_EObject, multiplicity=Multiplicity(1, 1))
    }
)
value95: BinaryAssociation = BinaryAssociation(
    name="value95",
    ends={
        Property(name="core_LayoutElement", type=core_LayoutMap, multiplicity=Multiplicity(1, 1)),
        Property(name="core_LayoutMap96", type=core_LayoutElement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
features119: BinaryAssociation = BinaryAssociation(
    name="features119",
    ends={
        Property(name="COREFeature121", type=core_CORERelativity_Opt2, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming120", type=core_COREFeature, multiplicity=Multiplicity(1, 1))
    }
)
reusedConfiguration107: BinaryAssociation = BinaryAssociation(
    name="reusedConfiguration107",
    ends={
        Property(name="core_COREConcernConfiguration109", type=core_COREReuseConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREReuseConfiguration108", type=core_COREConcernConfiguration, multiplicity=Multiplicity(0, 1))
    }
)
reuse110: BinaryAssociation = BinaryAssociation(
    name="reuse110",
    ends={
        Property(name="core_COREReuse112", type=core_COREReuseConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREReuseConfiguration111", type=core_COREReuse, multiplicity=Multiplicity(0, 1))
    }
)
relatedToFeature113: BinaryAssociation = BinaryAssociation(
    name="relatedToFeature113",
    ends={
        Property(name="core_COREFeature115", type=core_CORERelativity, multiplicity=Multiplicity(1, 1)),
        Property(name="core_CORERelativity114", type=core_COREFeature, multiplicity=Multiplicity(0, 1))
    }
)
source116: BinaryAssociation = BinaryAssociation(
    name="source116",
    ends={
        Property(name="COREFeature118", type=core_CORERelativity_Opt2, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing117", type=core_COREFeature, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_core_COREFeature_COREModelElement = Generalization(general=COREModelElement, specific=core_COREFeature)
gen_core_COREModel_CORENamedElement = Generalization(general=CORENamedElement, specific=core_COREModel)
gen_core_COREImpactModel_COREModel = Generalization(general=COREModel, specific=core_COREImpactModel)
gen_core_COREConcern_CORENamedElement = Generalization(general=CORENamedElement, specific=core_COREConcern)
gen_core_COREModelElement_CORENamedElement = Generalization(general=CORENamedElement, specific=core_COREModelElement)
gen_core_COREFeatureModel_COREModel = Generalization(general=COREModel, specific=core_COREFeatureModel)
gen_core_COREReuse_CORENamedElement = Generalization(general=CORENamedElement, specific=core_COREReuse)
gen_core_COREImpactNode_COREModelElement = Generalization(general=COREModelElement, specific=core_COREImpactNode)
gen_core_COREFeatureImpactNode_COREImpactNode = Generalization(general=COREImpactNode, specific=core_COREFeatureImpactNode)
gen_core_COREConcernConfiguration_COREConfiguration = Generalization(general=COREConfiguration, specific=core_COREConcernConfiguration)
gen_core_COREReuseConfiguration_COREConfiguration = Generalization(general=COREConfiguration, specific=core_COREReuseConfiguration)
gen_core_CORERelativity_COREModelElement = Generalization(general=COREModelElement, specific=core_CORERelativity)

# Domain Model
domain_model = DomainModel(
    name="core",
    types={core_COREModel, core_COREInterface, core_COREFeatureModel, COREModelElement, core_COREReuse, CORENamedElement, core_COREModelReuse, core_COREModelElement, core_COREFeature, core_COREConcern, core_COREImpactModel, COREModel, core_COREImpactNode, core_LayoutContainerMap, core_COREContribution, core_COREMapping, core_CORENamedElement, core_CORERelativity, core_CORERelativity_Opt2, core_COREBinding, core_CORECompositionSpecification, core_COREConcernConfiguration, core_COREConfiguration, core_COREReuseConfiguration, core_COREPattern, core_COREFeatureImpactNode, COREImpactNode, core_COREWeightedMapping, core_COREModelCompositionSpecification, core_LayoutMap, core_EObject, core_LayoutElement, core_COREImpactModelBinding, COREConfiguration, COREFeatureRelationshipType, COREVisibilityType, COREPartialityType},
    associations={interface11, featureModel12, impactModel14, realizedBy17, reuses19, modelReuses0, modelElements1, realizes3, coreConcern4, impactModelElements5, layouts6, contributions8, models10, selectable37, customizable40, children21, parent24, requires27, excludes30, relatedTo32, outgoing34, incoming35, reexposed69, extendingConfigurations72, features75, root78, configurations81, usable43, impacted46, defaults49, reusedConcern51, configurations54, selectedConfiguration56, extends60, outgoing62, incoming64, selected66, key97, value100, represents103, weightedMappings105, defaultConfiguration83, relatedFeatures86, reuse88, source91, impacts92, key94, value95, features119, reusedConfiguration107, reuse110, relatedToFeature113, source116},
    generalizations={gen_core_COREFeature_COREModelElement, gen_core_COREModel_CORENamedElement, gen_core_COREImpactModel_COREModel, gen_core_COREConcern_CORENamedElement, gen_core_COREModelElement_CORENamedElement, gen_core_COREFeatureModel_COREModel, gen_core_COREReuse_CORENamedElement, gen_core_COREImpactNode_COREModelElement, gen_core_COREFeatureImpactNode_COREImpactNode, gen_core_COREConcernConfiguration_COREConfiguration, gen_core_COREReuseConfiguration_COREConfiguration, gen_core_CORERelativity_COREModelElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)