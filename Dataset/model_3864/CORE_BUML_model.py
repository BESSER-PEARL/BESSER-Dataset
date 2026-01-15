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
CORENamedElement = Class(name="CORENamedElement")
core_COREModelReuse = Class(name="core::COREModelReuse")
core_COREModelElement = Class(name="core::COREModelElement", is_abstract=True)
core_COREFeature = Class(name="core::COREFeature")
core_COREConcern = Class(name="core::COREConcern")
core_COREImpactModel = Class(name="core::COREImpactModel")
COREModel = Class(name="COREModel")
COREModelElement = Class(name="COREModelElement")
core_COREReuse = Class(name="core::COREReuse")
core_COREBinding = Class(name="core::COREBinding", is_abstract=True)
core_COREImpactNode = Class(name="core::COREImpactNode")
core_LayoutContainerMap = Class(name="core::LayoutContainerMap")
core_COREContribution = Class(name="core::COREContribution")
core_COREInterface = Class(name="core::COREInterface")
core_COREFeatureModel = Class(name="core::COREFeatureModel")
core_CORENamedElement = Class(name="core::CORENamedElement", is_abstract=True)
core_COREConfiguration = Class(name="core::COREConfiguration", is_abstract=True)
core_CORECompositionSpecification = Class(name="core::CORECompositionSpecification", is_abstract=True)
core_COREMapping = Class(name="core::COREMapping", is_abstract=True)
core_COREConcernConfiguration = Class(name="core::COREConcernConfiguration")
core_COREReuseConfiguration = Class(name="core::COREReuseConfiguration")
core_COREPattern = Class(name="core::COREPattern", is_abstract=True)
core_LayoutMap = Class(name="core::LayoutMap")
core_EObject = Class(name="core::EObject")
core_LayoutElement = Class(name="core::LayoutElement")
core_COREFeatureImpactNode = Class(name="core::COREFeatureImpactNode")
COREImpactNode = Class(name="COREImpactNode")
core_COREWeightedMapping = Class(name="core::COREWeightedMapping")
core_COREModelCompositionSpecification = Class(name="core::COREModelCompositionSpecification", is_abstract=True)
core_COREImpactModelBinding = Class(name="core::COREImpactModelBinding")
COREConfiguration = Class(name="COREConfiguration")

# core_COREModel class attributes and methods

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

# COREModelElement class attributes and methods

# core_COREReuse class attributes and methods

# core_COREBinding class attributes and methods

# core_COREImpactNode class attributes and methods
core_COREImpactNode_scalingFactor: Property = Property(name="scalingFactor", type=FloatType)
core_COREImpactNode_offset: Property = Property(name="offset", type=FloatType)
core_COREImpactNode.attributes={core_COREImpactNode_scalingFactor, core_COREImpactNode_offset}

# core_LayoutContainerMap class attributes and methods

# core_COREContribution class attributes and methods
core_COREContribution_relativeWeight: Property = Property(name="relativeWeight", type=IntegerType)
core_COREContribution.attributes={core_COREContribution_relativeWeight}

# core_COREInterface class attributes and methods

# core_COREFeatureModel class attributes and methods

# core_CORENamedElement class attributes and methods
core_CORENamedElement_name: Property = Property(name="name", type=StringType)
core_CORENamedElement.attributes={core_CORENamedElement_name}

# core_COREConfiguration class attributes and methods

# core_CORECompositionSpecification class attributes and methods

# core_COREMapping class attributes and methods

# core_COREConcernConfiguration class attributes and methods

# core_COREReuseConfiguration class attributes and methods

# core_COREPattern class attributes and methods

# core_LayoutMap class attributes and methods

# core_EObject class attributes and methods

# core_LayoutElement class attributes and methods
core_LayoutElement_x: Property = Property(name="x", type=FloatType)
core_LayoutElement_y: Property = Property(name="y", type=FloatType)
core_LayoutElement.attributes={core_LayoutElement_x, core_LayoutElement_y}

# core_COREFeatureImpactNode class attributes and methods
core_COREFeatureImpactNode_relativeFeatureWeight: Property = Property(name="relativeFeatureWeight", type=IntegerType)
core_COREFeatureImpactNode.attributes={core_COREFeatureImpactNode_relativeFeatureWeight}

# COREImpactNode class attributes and methods

# core_COREWeightedMapping class attributes and methods
core_COREWeightedMapping_weight: Property = Property(name="weight", type=IntegerType)
core_COREWeightedMapping.attributes={core_COREWeightedMapping_weight}

# core_COREModelCompositionSpecification class attributes and methods

# core_COREImpactModelBinding class attributes and methods

# COREConfiguration class attributes and methods

# Relationships
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
selectable32: BinaryAssociation = BinaryAssociation(
    name="selectable32",
    ends={
        Property(name="core_COREFeature34", type=core_COREInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREInterface33", type=core_COREFeature, multiplicity=Multiplicity(0, 9999))
    }
)
customizable35: BinaryAssociation = BinaryAssociation(
    name="customizable35",
    ends={
        Property(name="core_COREModelElement37", type=core_COREInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREInterface36", type=core_COREModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
usable38: BinaryAssociation = BinaryAssociation(
    name="usable38",
    ends={
        Property(name="core_COREModelElement40", type=core_COREInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREInterface39", type=core_COREModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
impacted41: BinaryAssociation = BinaryAssociation(
    name="impacted41",
    ends={
        Property(name="core_COREImpactNode43", type=core_COREInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREInterface42", type=core_COREImpactNode, multiplicity=Multiplicity(0, 9999))
    }
)
defaults44: BinaryAssociation = BinaryAssociation(
    name="defaults44",
    ends={
        Property(name="core_COREConfiguration", type=core_COREInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREInterface45", type=core_COREConfiguration, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing54: BinaryAssociation = BinaryAssociation(
    name="outgoing54",
    ends={
        Property(name="COREContribution", type=core_COREImpactNode, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=core_COREContribution, multiplicity=Multiplicity(0, 9999))
    }
)
incoming55: BinaryAssociation = BinaryAssociation(
    name="incoming55",
    ends={
        Property(name="COREContribution56", type=core_COREImpactNode, multiplicity=Multiplicity(1, 1)),
        Property(name="impacts", type=core_COREContribution, multiplicity=Multiplicity(0, 9999))
    }
)
selected57: BinaryAssociation = BinaryAssociation(
    name="selected57",
    ends={
        Property(name="core_COREFeature59", type=core_COREConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREConfiguration58", type=core_COREFeature, multiplicity=Multiplicity(0, 9999))
    }
)
features60: BinaryAssociation = BinaryAssociation(
    name="features60",
    ends={
        Property(name="core_COREFeature62", type=core_COREFeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREFeatureModel61", type=core_COREFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
root63: BinaryAssociation = BinaryAssociation(
    name="root63",
    ends={
        Property(name="core_COREFeature65", type=core_COREFeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREFeatureModel64", type=core_COREFeature, multiplicity=Multiplicity(1, 1))
    }
)
configurations66: BinaryAssociation = BinaryAssociation(
    name="configurations66",
    ends={
        Property(name="core_COREConcernConfiguration", type=core_COREFeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREFeatureModel67", type=core_COREConcernConfiguration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defaultConfiguration68: BinaryAssociation = BinaryAssociation(
    name="defaultConfiguration68",
    ends={
        Property(name="core_COREConcernConfiguration70", type=core_COREFeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREFeatureModel69", type=core_COREConcernConfiguration, multiplicity=Multiplicity(0, 1))
    }
)
reusedConcern46: BinaryAssociation = BinaryAssociation(
    name="reusedConcern46",
    ends={
        Property(name="core_COREConcern48", type=core_COREReuse, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREReuse47", type=core_COREConcern, multiplicity=Multiplicity(1, 1))
    }
)
configurations49: BinaryAssociation = BinaryAssociation(
    name="configurations49",
    ends={
        Property(name="core_COREReuseConfiguration", type=core_COREReuse, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREReuse50", type=core_COREReuseConfiguration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
selectedConfiguration51: BinaryAssociation = BinaryAssociation(
    name="selectedConfiguration51",
    ends={
        Property(name="core_COREReuseConfiguration53", type=core_COREReuse, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREReuse52", type=core_COREReuseConfiguration, multiplicity=Multiplicity(0, 1))
    }
)
key77: BinaryAssociation = BinaryAssociation(
    name="key77",
    ends={
        Property(name="core_EObject", type=core_LayoutMap, multiplicity=Multiplicity(1, 1)),
        Property(name="core_LayoutMap", type=core_EObject, multiplicity=Multiplicity(1, 1))
    }
)
value78: BinaryAssociation = BinaryAssociation(
    name="value78",
    ends={
        Property(name="core_LayoutElement", type=core_LayoutMap, multiplicity=Multiplicity(1, 1)),
        Property(name="core_LayoutMap79", type=core_LayoutElement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
key80: BinaryAssociation = BinaryAssociation(
    name="key80",
    ends={
        Property(name="core_EObject82", type=core_LayoutContainerMap, multiplicity=Multiplicity(1, 1)),
        Property(name="core_LayoutContainerMap81", type=core_EObject, multiplicity=Multiplicity(1, 1))
    }
)
value83: BinaryAssociation = BinaryAssociation(
    name="value83",
    ends={
        Property(name="core_LayoutMap85", type=core_LayoutContainerMap, multiplicity=Multiplicity(1, 1)),
        Property(name="core_LayoutContainerMap84", type=core_LayoutMap, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
represents86: BinaryAssociation = BinaryAssociation(
    name="represents86",
    ends={
        Property(name="core_COREFeature87", type=core_COREFeatureImpactNode, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREFeatureImpactNode", type=core_COREFeature, multiplicity=Multiplicity(1, 1))
    }
)
weightedMappings88: BinaryAssociation = BinaryAssociation(
    name="weightedMappings88",
    ends={
        Property(name="core_COREWeightedMapping", type=core_COREFeatureImpactNode, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREFeatureImpactNode89", type=core_COREWeightedMapping, multiplicity=Multiplicity(0, 9999))
    }
)
reuse71: BinaryAssociation = BinaryAssociation(
    name="reuse71",
    ends={
        Property(name="core_COREReuse73", type=core_COREModelReuse, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREModelReuse72", type=core_COREReuse, multiplicity=Multiplicity(1, 1))
    }
)
source74: BinaryAssociation = BinaryAssociation(
    name="source74",
    ends={
        Property(name="COREImpactNode", type=core_COREContribution, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=core_COREImpactNode, multiplicity=Multiplicity(1, 1))
    }
)
impacts75: BinaryAssociation = BinaryAssociation(
    name="impacts75",
    ends={
        Property(name="COREImpactNode76", type=core_COREContribution, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=core_COREImpactNode, multiplicity=Multiplicity(1, 1))
    }
)
reuse93: BinaryAssociation = BinaryAssociation(
    name="reuse93",
    ends={
        Property(name="core_COREReuse95", type=core_COREReuseConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREReuseConfiguration94", type=core_COREReuse, multiplicity=Multiplicity(0, 1))
    }
)
reusedConfiguration90: BinaryAssociation = BinaryAssociation(
    name="reusedConfiguration90",
    ends={
        Property(name="core_COREConcernConfiguration92", type=core_COREReuseConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREReuseConfiguration91", type=core_COREConcernConfiguration, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_core_COREModel_CORENamedElement = Generalization(general=CORENamedElement, specific=core_COREModel)
gen_core_COREImpactModel_COREModel = Generalization(general=COREModel, specific=core_COREImpactModel)
gen_core_COREFeature_COREModelElement = Generalization(general=COREModelElement, specific=core_COREFeature)
gen_core_COREConcern_CORENamedElement = Generalization(general=CORENamedElement, specific=core_COREConcern)
gen_core_COREReuse_CORENamedElement = Generalization(general=CORENamedElement, specific=core_COREReuse)
gen_core_COREModelElement_CORENamedElement = Generalization(general=CORENamedElement, specific=core_COREModelElement)
gen_core_COREFeatureModel_COREModel = Generalization(general=COREModel, specific=core_COREFeatureModel)
gen_core_COREImpactNode_COREModelElement = Generalization(general=COREModelElement, specific=core_COREImpactNode)
gen_core_COREFeatureImpactNode_COREImpactNode = Generalization(general=COREImpactNode, specific=core_COREFeatureImpactNode)
gen_core_COREConcernConfiguration_COREConfiguration = Generalization(general=COREConfiguration, specific=core_COREConcernConfiguration)
gen_core_COREReuseConfiguration_COREConfiguration = Generalization(general=COREConfiguration, specific=core_COREReuseConfiguration)

# Domain Model
domain_model = DomainModel(
    name="core",
    types={core_COREModel, CORENamedElement, core_COREModelReuse, core_COREModelElement, core_COREFeature, core_COREConcern, core_COREImpactModel, COREModel, COREModelElement, core_COREReuse, core_COREBinding, core_COREImpactNode, core_LayoutContainerMap, core_COREContribution, core_COREInterface, core_COREFeatureModel, core_CORENamedElement, core_COREConfiguration, core_CORECompositionSpecification, core_COREMapping, core_COREConcernConfiguration, core_COREReuseConfiguration, core_COREPattern, core_LayoutMap, core_EObject, core_LayoutElement, core_COREFeatureImpactNode, COREImpactNode, core_COREWeightedMapping, core_COREModelCompositionSpecification, core_COREImpactModelBinding, COREConfiguration, COREFeatureRelationshipType, COREVisibilityType, COREPartialityType},
    associations={modelReuses0, modelElements1, realizes3, coreConcern4, impactModel14, realizedBy17, reuses19, children21, parent24, requires27, excludes30, impactModelElements5, layouts6, contributions8, models10, interface11, featureModel12, selectable32, customizable35, usable38, impacted41, defaults44, outgoing54, incoming55, selected57, features60, root63, configurations66, defaultConfiguration68, reusedConcern46, configurations49, selectedConfiguration51, key77, value78, key80, value83, represents86, weightedMappings88, reuse71, source74, impacts75, reuse93, reusedConfiguration90},
    generalizations={gen_core_COREModel_CORENamedElement, gen_core_COREImpactModel_COREModel, gen_core_COREFeature_COREModelElement, gen_core_COREConcern_CORENamedElement, gen_core_COREReuse_CORENamedElement, gen_core_COREModelElement_CORENamedElement, gen_core_COREFeatureModel_COREModel, gen_core_COREImpactNode_COREModelElement, gen_core_COREFeatureImpactNode_COREImpactNode, gen_core_COREConcernConfiguration_COREConfiguration, gen_core_COREReuseConfiguration_COREConfiguration},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)