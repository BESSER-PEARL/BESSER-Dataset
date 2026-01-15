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
            EnumerationLiteral(name="Optional"),
			EnumerationLiteral(name="Mandatory"),
			EnumerationLiteral(name="XOR"),
			EnumerationLiteral(name="OR")
    }
)

COREFeatureSelectionStatus: Enumeration = Enumeration(
    name="COREFeatureSelectionStatus",
    literals={
            EnumerationLiteral(name="NOT_SELECTED_NO_ACTION"),
			EnumerationLiteral(name="USER_SELECTED"),
			EnumerationLiteral(name="AUTO_SELECTED"),
			EnumerationLiteral(name="NOT_SELECTED_ACTION_REQUIRED"),
			EnumerationLiteral(name="WARNING_USER_SELECTED"),
			EnumerationLiteral(name="WARNING_AUTO_SELECTED"),
			EnumerationLiteral(name="REEXPOSE_USER_SELECTED"),
			EnumerationLiteral(name="REEXPOSE_AUTO_SELECTED")
    }
)

# Classes
core_COREModelElement = Class(name="core::COREModelElement", is_abstract=True)
core_COREFeature = Class(name="core::COREFeature", is_abstract=True)
core_COREImpactModel = Class(name="core::COREImpactModel", is_abstract=True)
COREModel = Class(name="COREModel")
core_COREConcern = Class(name="core::COREConcern")
core_COREInterface = Class(name="core::COREInterface")
COREModelElement = Class(name="COREModelElement")
core_COREModel = Class(name="core::COREModel", is_abstract=True)
CORENamedElement = Class(name="CORENamedElement")
core_COREModelReuse = Class(name="core::COREModelReuse")
core_COREReuse = Class(name="core::COREReuse")
core_COREBinding = Class(name="core::COREBinding", is_abstract=True)
CORECompositionSpecification = Class(name="CORECompositionSpecification")
core_COREMapping = Class(name="core::COREMapping", is_abstract=True)
core_CORECompositionSpecification = Class(name="core::CORECompositionSpecification", is_abstract=True)
core_CORENamedElement = Class(name="core::CORENamedElement", is_abstract=True)
core_COREPattern = Class(name="core::COREPattern", is_abstract=True)
core_COREFeatureModel = Class(name="core::COREFeatureModel", is_abstract=True)
core_COREImpactModelElement = Class(name="core::COREImpactModelElement", is_abstract=True)
core_COREConfiguration = Class(name="core::COREConfiguration")

# core_COREModelElement class attributes and methods

# core_COREFeature class attributes and methods
core_COREFeature_m_addFeature: Method = Method(name="addFeature", parameters={Parameter(name='child_name'), Parameter(name='association'), Parameter(name='position')}, type=BooleanType)
core_COREFeature_m_delete: Method = Method(name="delete", parameters={}, type=BooleanType)
core_COREFeature_m_rename: Method = Method(name="rename", parameters={Parameter(name='core_feature_name')})
core_COREFeature_m_changeLink: Method = Method(name="changeLink", parameters={Parameter(name='new_association')}, type=BooleanType)
core_COREFeature_m_changeParent: Method = Method(name="changeParent", parameters={Parameter(name='feature'), Parameter(name='new_association')}, type=BooleanType)
core_COREFeature_m_requires: Method = Method(name="requires", parameters={Parameter(name='feature')}, type=BooleanType)
core_COREFeature_m_excludes: Method = Method(name="excludes", parameters={Parameter(name='feature')}, type=BooleanType)
core_COREFeature_m_removeConstraint: Method = Method(name="removeConstraint", parameters={Parameter(name='feature')}, type=BooleanType)
core_COREFeature_m_addRealizedBy: Method = Method(name="addRealizedBy", parameters={Parameter(name='model')}, type=BooleanType)
core_COREFeature_m_AssociateReuse: Method = Method(name="AssociateReuse", parameters={Parameter(name='selected'), Parameter(name='reexposed'), Parameter(name='reuse')}, type=BooleanType)
core_COREFeature.methods={core_COREFeature_m_removeConstraint, core_COREFeature_m_changeLink, core_COREFeature_m_requires, core_COREFeature_m_addRealizedBy, core_COREFeature_m_addFeature, core_COREFeature_m_delete, core_COREFeature_m_rename, core_COREFeature_m_changeParent, core_COREFeature_m_excludes, core_COREFeature_m_AssociateReuse}

# core_COREImpactModel class attributes and methods

# COREModel class attributes and methods

# core_COREConcern class attributes and methods

# core_COREInterface class attributes and methods

# COREModelElement class attributes and methods

# core_COREModel class attributes and methods

# CORENamedElement class attributes and methods

# core_COREModelReuse class attributes and methods

# core_COREReuse class attributes and methods

# core_COREBinding class attributes and methods

# CORECompositionSpecification class attributes and methods

# core_COREMapping class attributes and methods

# core_CORECompositionSpecification class attributes and methods

# core_CORENamedElement class attributes and methods
core_CORENamedElement_name: Property = Property(name="name", type=StringType)
core_CORENamedElement.attributes={core_CORENamedElement_name}

# core_COREPattern class attributes and methods

# core_COREFeatureModel class attributes and methods
core_COREFeatureModel_m_getGlobalRoot: Method = Method(name="getGlobalRoot", parameters={}, type=StringType)
core_COREFeatureModel_m_getLocalRoot: Method = Method(name="getLocalRoot", parameters={}, type=StringType)
core_COREFeatureModel.methods={core_COREFeatureModel_m_getLocalRoot, core_COREFeatureModel_m_getGlobalRoot}

# core_COREImpactModelElement class attributes and methods

# core_COREConfiguration class attributes and methods

# Relationships
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
models4: BinaryAssociation = BinaryAssociation(
    name="models4",
    ends={
        Property(name="core_COREModel5", type=core_COREConcern, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREConcern", type=core_COREModel, multiplicity=Multiplicity(2, 9999))
    }
)
interface6: BinaryAssociation = BinaryAssociation(
    name="interface6",
    ends={
        Property(name="core_COREInterface", type=core_COREConcern, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREConcern7", type=core_COREInterface, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
modelReuse0: BinaryAssociation = BinaryAssociation(
    name="modelReuse0",
    ends={
        Property(name="core_COREModelReuse", type=core_COREModel, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREModel", type=core_COREModelReuse, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
realizedBy8: BinaryAssociation = BinaryAssociation(
    name="realizedBy8",
    ends={
        Property(name="COREModel", type=core_COREFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="realizes", type=core_COREModel, multiplicity=Multiplicity(0, 9999))
    }
)
reuses9: BinaryAssociation = BinaryAssociation(
    name="reuses9",
    ends={
        Property(name="core_COREReuse", type=core_COREFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREFeature", type=core_COREReuse, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
coreMappings10: BinaryAssociation = BinaryAssociation(
    name="coreMappings10",
    ends={
        Property(name="core_COREMapping", type=core_COREBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREBinding", type=core_COREMapping, multiplicity=Multiplicity(0, 9999))
    }
)
source11: BinaryAssociation = BinaryAssociation(
    name="source11",
    ends={
        Property(name="core_COREModel12", type=core_CORECompositionSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="core_CORECompositionSpecification", type=core_COREModel, multiplicity=Multiplicity(1, 1))
    }
)
mappedTo13: BinaryAssociation = BinaryAssociation(
    name="mappedTo13",
    ends={
        Property(name="core_COREModelElement15", type=core_COREMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREMapping14", type=core_COREModelElement, multiplicity=Multiplicity(1, 1))
    }
)
mappedFrom16: BinaryAssociation = BinaryAssociation(
    name="mappedFrom16",
    ends={
        Property(name="core_COREModelElement18", type=core_COREMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREMapping17", type=core_COREModelElement, multiplicity=Multiplicity(1, 1))
    }
)
selectable19: BinaryAssociation = BinaryAssociation(
    name="selectable19",
    ends={
        Property(name="core_COREFeature21", type=core_COREInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREInterface20", type=core_COREFeature, multiplicity=Multiplicity(0, 9999))
    }
)
customizable22: BinaryAssociation = BinaryAssociation(
    name="customizable22",
    ends={
        Property(name="core_COREModelElement24", type=core_COREInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREInterface23", type=core_COREModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
configurations35: BinaryAssociation = BinaryAssociation(
    name="configurations35",
    ends={
        Property(name="core_COREConfiguration37", type=core_COREReuse, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREReuse36", type=core_COREConfiguration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
selected38: BinaryAssociation = BinaryAssociation(
    name="selected38",
    ends={
        Property(name="core_COREConfiguration40", type=core_COREReuse, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREReuse39", type=core_COREConfiguration, multiplicity=Multiplicity(0, 1))
    }
)
selected41: BinaryAssociation = BinaryAssociation(
    name="selected41",
    ends={
        Property(name="core_COREFeature43", type=core_COREConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREConfiguration42", type=core_COREFeature, multiplicity=Multiplicity(0, 9999))
    }
)
reexposed44: BinaryAssociation = BinaryAssociation(
    name="reexposed44",
    ends={
        Property(name="core_COREFeature46", type=core_COREConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREConfiguration45", type=core_COREFeature, multiplicity=Multiplicity(0, 9999))
    }
)
compositions47: BinaryAssociation = BinaryAssociation(
    name="compositions47",
    ends={
        Property(name="core_CORECompositionSpecification49", type=core_COREModelReuse, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREModelReuse48", type=core_CORECompositionSpecification, multiplicity=Multiplicity(0, 9999))
    }
)
usable25: BinaryAssociation = BinaryAssociation(
    name="usable25",
    ends={
        Property(name="core_COREModelElement27", type=core_COREInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREInterface26", type=core_COREModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
impacted28: BinaryAssociation = BinaryAssociation(
    name="impacted28",
    ends={
        Property(name="core_COREImpactModelElement", type=core_COREInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREInterface29", type=core_COREImpactModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
defaults30: BinaryAssociation = BinaryAssociation(
    name="defaults30",
    ends={
        Property(name="core_COREConfiguration", type=core_COREInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREInterface31", type=core_COREConfiguration, multiplicity=Multiplicity(0, 9999))
    }
)
reusedConcern32: BinaryAssociation = BinaryAssociation(
    name="reusedConcern32",
    ends={
        Property(name="core_COREConcern34", type=core_COREReuse, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREReuse33", type=core_COREConcern, multiplicity=Multiplicity(1, 1))
    }
)
modelReuse50: BinaryAssociation = BinaryAssociation(
    name="modelReuse50",
    ends={
        Property(name="core_COREReuse52", type=core_COREModelReuse, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREModelReuse51", type=core_COREReuse, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_core_COREImpactModel_COREModel = Generalization(general=COREModel, specific=core_COREImpactModel)
gen_core_COREConcern_CORENamedElement = Generalization(general=CORENamedElement, specific=core_COREConcern)
gen_core_COREFeature_COREModelElement = Generalization(general=COREModelElement, specific=core_COREFeature)
gen_core_COREModel_CORENamedElement = Generalization(general=CORENamedElement, specific=core_COREModel)
gen_core_COREBinding_CORECompositionSpecification = Generalization(general=CORECompositionSpecification, specific=core_COREBinding)
gen_core_COREModelElement_CORENamedElement = Generalization(general=CORENamedElement, specific=core_COREModelElement)
gen_core_COREPattern_CORECompositionSpecification = Generalization(general=CORECompositionSpecification, specific=core_COREPattern)
gen_core_COREImpactModelElement_COREModelElement = Generalization(general=COREModelElement, specific=core_COREImpactModelElement)
gen_core_COREConfiguration_CORENamedElement = Generalization(general=CORENamedElement, specific=core_COREConfiguration)
gen_core_COREFeatureModel_COREModel = Generalization(general=COREModel, specific=core_COREFeatureModel)

# Domain Model
domain_model = DomainModel(
    name="core",
    types={core_COREModelElement, core_COREFeature, core_COREImpactModel, COREModel, core_COREConcern, core_COREInterface, COREModelElement, core_COREModel, CORENamedElement, core_COREModelReuse, core_COREReuse, core_COREBinding, CORECompositionSpecification, core_COREMapping, core_CORECompositionSpecification, core_CORENamedElement, core_COREPattern, core_COREFeatureModel, core_COREImpactModelElement, core_COREConfiguration, COREFeatureRelationshipType, COREFeatureSelectionStatus},
    associations={modelElements1, realizes3, models4, interface6, modelReuse0, realizedBy8, reuses9, coreMappings10, source11, mappedTo13, mappedFrom16, selectable19, customizable22, configurations35, selected38, selected41, reexposed44, compositions47, usable25, impacted28, defaults30, reusedConcern32, modelReuse50},
    generalizations={gen_core_COREImpactModel_COREModel, gen_core_COREConcern_CORENamedElement, gen_core_COREFeature_COREModelElement, gen_core_COREModel_CORENamedElement, gen_core_COREBinding_CORECompositionSpecification, gen_core_COREModelElement_CORENamedElement, gen_core_COREPattern_CORECompositionSpecification, gen_core_COREImpactModelElement_COREModelElement, gen_core_COREConfiguration_CORENamedElement, gen_core_COREFeatureModel_COREModel},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)