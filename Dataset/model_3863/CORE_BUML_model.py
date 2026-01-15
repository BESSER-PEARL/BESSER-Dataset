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
core_COREReuse = Class(name="core::COREReuse")
core_COREModelElement = Class(name="core::COREModelElement", is_abstract=True)
core_COREFeature = Class(name="core::COREFeature", is_abstract=True)
core_COREImpactModel = Class(name="core::COREImpactModel", is_abstract=True)
COREModel = Class(name="COREModel")
core_COREConcern = Class(name="core::COREConcern")
core_COREInterface = Class(name="core::COREInterface")
COREModelElement = Class(name="COREModelElement")
core_COREModel = Class(name="core::COREModel", is_abstract=True)
CORENamedElement = Class(name="CORENamedElement")
core_CORENamedElement = Class(name="core::CORENamedElement", is_abstract=True)
core_COREImpactModelElement = Class(name="core::COREImpactModelElement", is_abstract=True)
core_COREStrategy = Class(name="core::COREStrategy", is_abstract=True)
core_COREConfiguration = Class(name="core::COREConfiguration", is_abstract=True)
core_COREBinding = Class(name="core::COREBinding", is_abstract=True)
CORECompositionSpecification = Class(name="CORECompositionSpecification")
core_COREMapping = Class(name="core::COREMapping")
core_CORECompositionSpecification = Class(name="core::CORECompositionSpecification", is_abstract=True)
core_COREPattern = Class(name="core::COREPattern", is_abstract=True)
core_COREFeatureModel = Class(name="core::COREFeatureModel", is_abstract=True)

# core_COREReuse class attributes and methods

# core_COREModelElement class attributes and methods

# core_COREFeature class attributes and methods

# core_COREImpactModel class attributes and methods

# COREModel class attributes and methods

# core_COREConcern class attributes and methods

# core_COREInterface class attributes and methods

# COREModelElement class attributes and methods

# core_COREModel class attributes and methods

# CORENamedElement class attributes and methods

# core_CORENamedElement class attributes and methods
core_CORENamedElement_name: Property = Property(name="name", type=StringType)
core_CORENamedElement.attributes={core_CORENamedElement_name}

# core_COREImpactModelElement class attributes and methods

# core_COREStrategy class attributes and methods

# core_COREConfiguration class attributes and methods

# core_COREBinding class attributes and methods

# CORECompositionSpecification class attributes and methods

# core_COREMapping class attributes and methods

# core_CORECompositionSpecification class attributes and methods

# core_COREPattern class attributes and methods

# core_COREFeatureModel class attributes and methods

# Relationships
reuses0: BinaryAssociation = BinaryAssociation(
    name="reuses0",
    ends={
        Property(name="core_COREReuse", type=core_COREModel, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREModel", type=core_COREReuse, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
realizedBy8: BinaryAssociation = BinaryAssociation(
    name="realizedBy8",
    ends={
        Property(name="COREModel", type=core_COREFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="realizes", type=core_COREModel, multiplicity=Multiplicity(0, 9999))
    }
)
configurations21: BinaryAssociation = BinaryAssociation(
    name="configurations21",
    ends={
        Property(name="core_COREConfiguration23", type=core_COREStrategy, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREStrategy22", type=core_COREConfiguration, multiplicity=Multiplicity(0, 9999))
    }
)
selectable24: BinaryAssociation = BinaryAssociation(
    name="selectable24",
    ends={
        Property(name="core_COREFeature26", type=core_COREInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREInterface25", type=core_COREFeature, multiplicity=Multiplicity(0, 9999))
    }
)
customizable27: BinaryAssociation = BinaryAssociation(
    name="customizable27",
    ends={
        Property(name="core_COREModelElement29", type=core_COREInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREInterface28", type=core_COREModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
usable30: BinaryAssociation = BinaryAssociation(
    name="usable30",
    ends={
        Property(name="core_COREModelElement32", type=core_COREInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREInterface31", type=core_COREModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
impacted33: BinaryAssociation = BinaryAssociation(
    name="impacted33",
    ends={
        Property(name="core_COREImpactModelElement", type=core_COREInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREInterface34", type=core_COREImpactModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
reusedConcern35: BinaryAssociation = BinaryAssociation(
    name="reusedConcern35",
    ends={
        Property(name="core_COREConcern37", type=core_COREReuse, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREReuse36", type=core_COREConcern, multiplicity=Multiplicity(1, 1))
    }
)
compositions38: BinaryAssociation = BinaryAssociation(
    name="compositions38",
    ends={
        Property(name="core_CORECompositionSpecification40", type=core_COREReuse, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREReuse39", type=core_CORECompositionSpecification, multiplicity=Multiplicity(0, 9999))
    }
)
strategies9: BinaryAssociation = BinaryAssociation(
    name="strategies9",
    ends={
        Property(name="core_COREStrategy", type=core_COREFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREFeature", type=core_COREStrategy, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
configurations10: BinaryAssociation = BinaryAssociation(
    name="configurations10",
    ends={
        Property(name="core_COREConfiguration", type=core_COREFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREFeature11", type=core_COREConfiguration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
coreMappings12: BinaryAssociation = BinaryAssociation(
    name="coreMappings12",
    ends={
        Property(name="core_COREMapping", type=core_COREBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREBinding", type=core_COREMapping, multiplicity=Multiplicity(0, 9999))
    }
)
source13: BinaryAssociation = BinaryAssociation(
    name="source13",
    ends={
        Property(name="core_COREModel14", type=core_CORECompositionSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="core_CORECompositionSpecification", type=core_COREModel, multiplicity=Multiplicity(1, 1))
    }
)
mappedTo15: BinaryAssociation = BinaryAssociation(
    name="mappedTo15",
    ends={
        Property(name="core_COREModelElement17", type=core_COREMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREMapping16", type=core_COREModelElement, multiplicity=Multiplicity(1, 1))
    }
)
mappedFrom18: BinaryAssociation = BinaryAssociation(
    name="mappedFrom18",
    ends={
        Property(name="core_COREModelElement20", type=core_COREMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREMapping19", type=core_COREModelElement, multiplicity=Multiplicity(1, 1))
    }
)
selected41: BinaryAssociation = BinaryAssociation(
    name="selected41",
    ends={
        Property(name="core_COREFeature43", type=core_COREReuse, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREReuse42", type=core_COREFeature, multiplicity=Multiplicity(1, 9999))
    }
)
reusedConcern44: BinaryAssociation = BinaryAssociation(
    name="reusedConcern44",
    ends={
        Property(name="core_COREConcern46", type=core_COREConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREConfiguration45", type=core_COREConcern, multiplicity=Multiplicity(0, 9999))
    }
)
selected47: BinaryAssociation = BinaryAssociation(
    name="selected47",
    ends={
        Property(name="core_COREFeature49", type=core_COREConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="core_COREConfiguration48", type=core_COREFeature, multiplicity=Multiplicity(1, 9999))
    }
)

# Generalizations
gen_core_COREImpactModel_COREModel = Generalization(general=COREModel, specific=core_COREImpactModel)
gen_core_COREConcern_CORENamedElement = Generalization(general=CORENamedElement, specific=core_COREConcern)
gen_core_COREFeature_COREModelElement = Generalization(general=COREModelElement, specific=core_COREFeature)
gen_core_COREModel_CORENamedElement = Generalization(general=CORENamedElement, specific=core_COREModel)
gen_core_COREStrategy_CORENamedElement = Generalization(general=CORENamedElement, specific=core_COREStrategy)
gen_core_COREBinding_CORECompositionSpecification = Generalization(general=CORECompositionSpecification, specific=core_COREBinding)
gen_core_COREModelElement_CORENamedElement = Generalization(general=CORENamedElement, specific=core_COREModelElement)
gen_core_COREPattern_CORECompositionSpecification = Generalization(general=CORECompositionSpecification, specific=core_COREPattern)
gen_core_COREImpactModelElement_COREModelElement = Generalization(general=COREModelElement, specific=core_COREImpactModelElement)
gen_core_COREConfiguration_CORENamedElement = Generalization(general=CORENamedElement, specific=core_COREConfiguration)
gen_core_COREFeatureModel_COREModel = Generalization(general=COREModel, specific=core_COREFeatureModel)

# Domain Model
domain_model = DomainModel(
    name="core",
    types={core_COREReuse, core_COREModelElement, core_COREFeature, core_COREImpactModel, COREModel, core_COREConcern, core_COREInterface, COREModelElement, core_COREModel, CORENamedElement, core_CORENamedElement, core_COREImpactModelElement, core_COREStrategy, core_COREConfiguration, core_COREBinding, CORECompositionSpecification, core_COREMapping, core_CORECompositionSpecification, core_COREPattern, core_COREFeatureModel},
    associations={reuses0, modelElements1, realizes3, models4, interface6, realizedBy8, configurations21, selectable24, customizable27, usable30, impacted33, reusedConcern35, compositions38, strategies9, configurations10, coreMappings12, source13, mappedTo15, mappedFrom18, selected41, reusedConcern44, selected47},
    generalizations={gen_core_COREImpactModel_COREModel, gen_core_COREConcern_CORENamedElement, gen_core_COREFeature_COREModelElement, gen_core_COREModel_CORENamedElement, gen_core_COREStrategy_CORENamedElement, gen_core_COREBinding_CORECompositionSpecification, gen_core_COREModelElement_CORENamedElement, gen_core_COREPattern_CORECompositionSpecification, gen_core_COREImpactModelElement_COREModelElement, gen_core_COREConfiguration_CORENamedElement, gen_core_COREFeatureModel_COREModel},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)