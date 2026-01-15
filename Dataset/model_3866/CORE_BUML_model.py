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
core_COREImpactModelElement = Class(name="core::COREImpactModelElement")
core_LayoutContainerMap = Class(name="core::LayoutContainerMap")
core_COREContribution = Class(name="core::COREContribution")
core_COREInterface = Class(name="core::COREInterface")
core_COREFeatureModel = Class(name="core::COREFeatureModel")
COREModelElement = Class(name="COREModelElement")
core_COREReuse = Class(name="core::COREReuse")
core_COREBinding = Class(name="core::COREBinding", is_abstract=True)
core_CORECompositionSpecification = Class(name="core::CORECompositionSpecification", is_abstract=True)
core_COREMapping = Class(name="core::COREMapping", is_abstract=True)
core_CORENamedElement = Class(name="core::CORENamedElement", is_abstract=True)
core_COREConfiguration = Class(name="core::COREConfiguration")
core_COREPattern = Class(name="core::COREPattern", is_abstract=True)
core_LayoutMap = Class(name="core::LayoutMap")
core_EObject = Class(name="core::EObject")
core_LayoutElement = Class(name="core::LayoutElement")
core_COREFeatureImpact = Class(name="core::COREFeatureImpact")
COREImpactModelElement = Class(name="COREImpactModelElement")
core_COREModelCompositionSpecification = Class(name="core::COREModelCompositionSpecification", is_abstract=True)
core_COREWeightedMapping = Class(name="core::COREWeightedMapping")
core_COREImpactModelBinding = Class(name="core::COREImpactModelBinding")

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

# core_COREImpactModelElement class attributes and methods
core_COREImpactModelElement_scalingFactor: Property = Property(name="scalingFactor", type=FloatType)
core_COREImpactModelElement_offset: Property = Property(name="offset", type=FloatType)
core_COREImpactModelElement.attributes={core_COREImpactModelElement_offset, core_COREImpactModelElement_scalingFactor}

# core_LayoutContainerMap class attributes and methods

# core_COREContribution class attributes and methods
core_COREContribution_relativeWeight: Property = Property(name="relativeWeight", type=IntegerType)
core_COREContribution.attributes={core_COREContribution_relativeWeight}

# core_COREInterface class attributes and methods

# core_COREFeatureModel class attributes and methods

# COREModelElement class attributes and methods

# core_COREReuse class attributes and methods

# core_COREBinding class attributes and methods

# core_CORECompositionSpecification class attributes and methods

# core_COREMapping class attributes and methods

# core_CORENamedElement class attributes and methods
core_CORENamedElement_name: Property = Property(name="name", type=StringType)
core_CORENamedElement.attributes={core_CORENamedElement_name}

# core_COREConfiguration class attributes and methods

# core_COREPattern class attributes and methods

# core_LayoutMap class attributes and methods

# core_EObject class attributes and methods

# core_LayoutElement class attributes and methods
core_LayoutElement_x: Property = Property(name="x", type=FloatType)
core_LayoutElement_y: Property = Property(name="y", type=FloatType)
core_LayoutElement.attributes={core_LayoutElement_x, core_LayoutElement_y}

# core_COREFeatureImpact class attributes and methods
core_COREFeatureImpact_relativeFeatureWeight: Property = Property(name="relativeFeatureWeight", type=FloatType)
core_COREFeatureImpact.attributes={core_COREFeatureImpact_relativeFeatureWeight}

# COREImpactModelElement class attributes and methods

# core_COREModelCompositionSpecification class attributes and methods

# core_COREWeightedMapping class attributes and methods
core_COREWeightedMapping_weight: Property = Property(name="weight", type=IntegerType)
core_COREWeightedMapping.attributes={core_COREWeightedMapping_weight}

# core_COREImpactModelBinding class attributes and methods

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
contributions8: BinaryAssociation = BinaryAssociation(
    name="contributions8",
    ends={
        Property(name="core_COREContribution", type=core_COREImpactModel, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREImpactModel9", type=core_COREContribution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
concern4: BinaryAssociation = BinaryAssociation(
    name="concern4",
    ends={
        Property(name="COREConcern", type=core_COREModel, multiplicity=Multiplicity(1, 1)),
        Property(name="models", type=core_COREConcern, multiplicity=Multiplicity(1, 1))
    }
)
impactModelElements5: BinaryAssociation = BinaryAssociation(
    name="impactModelElements5",
    ends={
        Property(name="core_COREImpactModelElement", type=core_COREImpactModel, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREImpactModel", type=core_COREImpactModelElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
layouts6: BinaryAssociation = BinaryAssociation(
    name="layouts6",
    ends={
        Property(name="core_LayoutContainerMap", type=core_COREImpactModel, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREImpactModel7", type=core_LayoutContainerMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
models10: BinaryAssociation = BinaryAssociation(
    name="models10",
    ends={
        Property(name="COREModel", type=core_COREConcern, multiplicity=Multiplicity(1, 1)),
        Property(name="concern", type=core_COREModel, multiplicity=Multiplicity(1, 9999))
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
reusedConcern48: BinaryAssociation = BinaryAssociation(
    name="reusedConcern48",
    ends={
        Property(name="core_COREConcern50", type=core_COREReuse, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREReuse49", type=core_COREConcern, multiplicity=Multiplicity(1, 1))
    }
)
configurations51: BinaryAssociation = BinaryAssociation(
    name="configurations51",
    ends={
        Property(name="core_COREConfiguration53", type=core_COREReuse, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREReuse52", type=core_COREConfiguration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
selectedConfiguration54: BinaryAssociation = BinaryAssociation(
    name="selectedConfiguration54",
    ends={
        Property(name="core_COREConfiguration56", type=core_COREReuse, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREReuse55", type=core_COREConfiguration, multiplicity=Multiplicity(0, 1))
    }
)
reuse32: BinaryAssociation = BinaryAssociation(
    name="reuse32",
    ends={
        Property(name="core_COREReuse33", type=core_CORECompositionSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="core_CORECompositionSpecification", type=core_COREReuse, multiplicity=Multiplicity(1, 1))
    }
)
selectable34: BinaryAssociation = BinaryAssociation(
    name="selectable34",
    ends={
        Property(name="core_COREFeature36", type=core_COREInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREInterface35", type=core_COREFeature, multiplicity=Multiplicity(0, 9999))
    }
)
customizable37: BinaryAssociation = BinaryAssociation(
    name="customizable37",
    ends={
        Property(name="core_COREModelElement39", type=core_COREInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREInterface38", type=core_COREModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
usable40: BinaryAssociation = BinaryAssociation(
    name="usable40",
    ends={
        Property(name="core_COREModelElement42", type=core_COREInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREInterface41", type=core_COREModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
impacted43: BinaryAssociation = BinaryAssociation(
    name="impacted43",
    ends={
        Property(name="core_COREImpactModelElement45", type=core_COREInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREInterface44", type=core_COREImpactModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
defaults46: BinaryAssociation = BinaryAssociation(
    name="defaults46",
    ends={
        Property(name="core_COREConfiguration", type=core_COREInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREInterface47", type=core_COREConfiguration, multiplicity=Multiplicity(0, 9999))
    }
)
reuse79: BinaryAssociation = BinaryAssociation(
    name="reuse79",
    ends={
        Property(name="COREReuse", type=core_COREModelReuse, multiplicity=Multiplicity(1, 1)),
        Property(name="modelReuses", type=core_COREReuse, multiplicity=Multiplicity(1, 1))
    }
)
source80: BinaryAssociation = BinaryAssociation(
    name="source80",
    ends={
        Property(name="COREImpactModelElement", type=core_COREContribution, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=core_COREImpactModelElement, multiplicity=Multiplicity(1, 1))
    }
)
modelReuses57: BinaryAssociation = BinaryAssociation(
    name="modelReuses57",
    ends={
        Property(name="COREModelReuse", type=core_COREReuse, multiplicity=Multiplicity(1, 1)),
        Property(name="reuse", type=core_COREModelReuse, multiplicity=Multiplicity(0, 9999))
    }
)
extends59: BinaryAssociation = BinaryAssociation(
    name="extends59",
    ends={
        Property(name="core_COREReuse60", type=core_COREReuse, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREReuse58", type=core_COREReuse, multiplicity=Multiplicity(0, 1))
    }
)
outgoing61: BinaryAssociation = BinaryAssociation(
    name="outgoing61",
    ends={
        Property(name="COREContribution", type=core_COREImpactModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=core_COREContribution, multiplicity=Multiplicity(0, 9999))
    }
)
incoming62: BinaryAssociation = BinaryAssociation(
    name="incoming62",
    ends={
        Property(name="COREContribution63", type=core_COREImpactModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="impacts", type=core_COREContribution, multiplicity=Multiplicity(0, 9999))
    }
)
selected64: BinaryAssociation = BinaryAssociation(
    name="selected64",
    ends={
        Property(name="core_COREFeature66", type=core_COREConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREConfiguration65", type=core_COREFeature, multiplicity=Multiplicity(0, 9999))
    }
)
reexposed67: BinaryAssociation = BinaryAssociation(
    name="reexposed67",
    ends={
        Property(name="core_COREFeature69", type=core_COREConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREConfiguration68", type=core_COREFeature, multiplicity=Multiplicity(0, 9999))
    }
)
extendedConfigurations71: BinaryAssociation = BinaryAssociation(
    name="extendedConfigurations71",
    ends={
        Property(name="core_COREConfiguration72", type=core_COREConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREConfiguration70", type=core_COREConfiguration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
features73: BinaryAssociation = BinaryAssociation(
    name="features73",
    ends={
        Property(name="core_COREFeature75", type=core_COREFeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREFeatureModel74", type=core_COREFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
root76: BinaryAssociation = BinaryAssociation(
    name="root76",
    ends={
        Property(name="core_COREFeature78", type=core_COREFeatureModel, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREFeatureModel77", type=core_COREFeature, multiplicity=Multiplicity(1, 1))
    }
)
impacts81: BinaryAssociation = BinaryAssociation(
    name="impacts81",
    ends={
        Property(name="COREImpactModelElement82", type=core_COREContribution, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=core_COREImpactModelElement, multiplicity=Multiplicity(1, 1))
    }
)
key83: BinaryAssociation = BinaryAssociation(
    name="key83",
    ends={
        Property(name="core_EObject", type=core_LayoutMap, multiplicity=Multiplicity(1, 1)),
        Property(name="core_LayoutMap", type=core_EObject, multiplicity=Multiplicity(1, 1))
    }
)
value84: BinaryAssociation = BinaryAssociation(
    name="value84",
    ends={
        Property(name="core_LayoutElement", type=core_LayoutMap, multiplicity=Multiplicity(1, 1)),
        Property(name="core_LayoutMap85", type=core_LayoutElement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
key86: BinaryAssociation = BinaryAssociation(
    name="key86",
    ends={
        Property(name="core_EObject88", type=core_LayoutContainerMap, multiplicity=Multiplicity(1, 1)),
        Property(name="core_LayoutContainerMap87", type=core_EObject, multiplicity=Multiplicity(1, 1))
    }
)
value89: BinaryAssociation = BinaryAssociation(
    name="value89",
    ends={
        Property(name="core_LayoutMap91", type=core_LayoutContainerMap, multiplicity=Multiplicity(1, 1)),
        Property(name="core_LayoutContainerMap90", type=core_LayoutMap, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
represents92: BinaryAssociation = BinaryAssociation(
    name="represents92",
    ends={
        Property(name="core_COREFeature93", type=core_COREFeatureImpact, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREFeatureImpact", type=core_COREFeature, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_core_COREModel_CORENamedElement = Generalization(general=CORENamedElement, specific=core_COREModel)
gen_core_COREImpactModel_COREModel = Generalization(general=COREModel, specific=core_COREImpactModel)
gen_core_COREConcern_CORENamedElement = Generalization(general=CORENamedElement, specific=core_COREConcern)
gen_core_COREFeature_COREModelElement = Generalization(general=COREModelElement, specific=core_COREFeature)
gen_core_COREModelElement_CORENamedElement = Generalization(general=CORENamedElement, specific=core_COREModelElement)
gen_core_COREReuse_CORENamedElement = Generalization(general=CORENamedElement, specific=core_COREReuse)
gen_core_COREImpactModelElement_COREModelElement = Generalization(general=COREModelElement, specific=core_COREImpactModelElement)
gen_core_COREFeatureModel_COREModel = Generalization(general=COREModel, specific=core_COREFeatureModel)
gen_core_COREFeatureImpact_COREImpactModelElement = Generalization(general=COREImpactModelElement, specific=core_COREFeatureImpact)

# Domain Model
domain_model = DomainModel(
    name="core",
    types={core_COREModel, CORENamedElement, core_COREModelReuse, core_COREModelElement, core_COREFeature, core_COREConcern, core_COREImpactModel, COREModel, core_COREImpactModelElement, core_LayoutContainerMap, core_COREContribution, core_COREInterface, core_COREFeatureModel, COREModelElement, core_COREReuse, core_COREBinding, core_CORECompositionSpecification, core_COREMapping, core_CORENamedElement, core_COREConfiguration, core_COREPattern, core_LayoutMap, core_EObject, core_LayoutElement, core_COREFeatureImpact, COREImpactModelElement, core_COREModelCompositionSpecification, core_COREWeightedMapping, core_COREImpactModelBinding, COREFeatureRelationshipType, COREVisibilityType, COREPartialityType},
    associations={modelReuses0, modelElements1, realizes3, contributions8, concern4, impactModelElements5, layouts6, parent24, requires27, excludes30, models10, interface11, featureModel12, impactModel14, realizedBy17, reuses19, children21, reusedConcern48, configurations51, selectedConfiguration54, reuse32, selectable34, customizable37, usable40, impacted43, defaults46, reuse79, source80, modelReuses57, extends59, outgoing61, incoming62, selected64, reexposed67, extendedConfigurations71, features73, root76, impacts81, key83, value84, key86, value89, represents92},
    generalizations={gen_core_COREModel_CORENamedElement, gen_core_COREImpactModel_COREModel, gen_core_COREConcern_CORENamedElement, gen_core_COREFeature_COREModelElement, gen_core_COREModelElement_CORENamedElement, gen_core_COREReuse_CORENamedElement, gen_core_COREImpactModelElement_COREModelElement, gen_core_COREFeatureModel_COREModel, gen_core_COREFeatureImpact_COREImpactModelElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)