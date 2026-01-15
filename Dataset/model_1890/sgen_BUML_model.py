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
ParameterTypes: Enumeration = Enumeration(
    name="ParameterTypes",
    literals={
            EnumerationLiteral(name="STRING"),
			EnumerationLiteral(name="FLOAT"),
			EnumerationLiteral(name="BOOLEAN"),
			EnumerationLiteral(name="INTEGER")
    }
)

# Classes
sgen_GeneratorModel = Class(name="sgen::GeneratorModel")
sgen_GeneratorEntry = Class(name="sgen::GeneratorEntry")
sgen_Property = Class(name="sgen::Property")
sgen_GeneratorConfiguration = Class(name="sgen::GeneratorConfiguration")
sgen_FeatureConfiguration = Class(name="sgen::FeatureConfiguration")
sgen_FeatureParameterValue = Class(name="sgen::FeatureParameterValue")
sgen_FeatureType = Class(name="sgen::FeatureType")
NamedElement = Class(name="NamedElement")
DeprecatableElement = Class(name="DeprecatableElement")
sgen_FeatureParameter = Class(name="sgen::FeatureParameter")
sgen_FeatureTypeLibrary = Class(name="sgen::FeatureTypeLibrary")
sgen_EObject = Class(name="sgen::EObject")
sgen_DeprecatableElement = Class(name="sgen::DeprecatableElement")
sgen_Expression = Class(name="sgen::Expression")

# sgen_GeneratorModel class attributes and methods
sgen_GeneratorModel_generatorId: Property = Property(name="generatorId", type=StringType)
sgen_GeneratorModel.attributes={sgen_GeneratorModel_generatorId}

# sgen_GeneratorEntry class attributes and methods
sgen_GeneratorEntry_contentType: Property = Property(name="contentType", type=StringType)
sgen_GeneratorEntry_m_getFeatureConfiguration: Method = Method(name="getFeatureConfiguration", parameters={Parameter(name='featureName')}, type=StringType)
sgen_GeneratorEntry_m_getFeatureParameterValue: Method = Method(name="getFeatureParameterValue", parameters={Parameter(name='featureName'), Parameter(name='paramName')}, type=StringType)
sgen_GeneratorEntry.attributes={sgen_GeneratorEntry_contentType}
sgen_GeneratorEntry.methods={sgen_GeneratorEntry_m_getFeatureParameterValue, sgen_GeneratorEntry_m_getFeatureConfiguration}

# sgen_Property class attributes and methods

# sgen_GeneratorConfiguration class attributes and methods

# sgen_FeatureConfiguration class attributes and methods
sgen_FeatureConfiguration_m_getParameterValue: Method = Method(name="getParameterValue", parameters={Parameter(name='parameterName')}, type=StringType)
sgen_FeatureConfiguration.methods={sgen_FeatureConfiguration_m_getParameterValue}

# sgen_FeatureParameterValue class attributes and methods
sgen_FeatureParameterValue_m_setValue: Method = Method(name="setValue", parameters={Parameter(name='string')})
sgen_FeatureParameterValue_m_setValue: Method = Method(name="setValue", parameters={Parameter(name='boolean')})
sgen_FeatureParameterValue_m_getStringValue: Method = Method(name="getStringValue", parameters={}, type=StringType)
sgen_FeatureParameterValue_m_getBooleanValue: Method = Method(name="getBooleanValue", parameters={}, type=BooleanType)
sgen_FeatureParameterValue_m_setValue: Method = Method(name="setValue", parameters={Parameter(name='value')})
sgen_FeatureParameterValue_m_getIntegerValue: Method = Method(name="getIntegerValue", parameters={}, type=IntegerType)
sgen_FeatureParameterValue.methods={sgen_FeatureParameterValue_m_getIntegerValue, sgen_FeatureParameterValue_m_setValue, sgen_FeatureParameterValue_m_setValue, sgen_FeatureParameterValue_m_getStringValue, sgen_FeatureParameterValue_m_setValue, sgen_FeatureParameterValue_m_getBooleanValue}

# sgen_FeatureType class attributes and methods
sgen_FeatureType_optional: Property = Property(name="optional", type=BooleanType)
sgen_FeatureType.attributes={sgen_FeatureType_optional}

# NamedElement class attributes and methods

# DeprecatableElement class attributes and methods

# sgen_FeatureParameter class attributes and methods
sgen_FeatureParameter_optional: Property = Property(name="optional", type=BooleanType)
sgen_FeatureParameter_parameterType: Property = Property(name="parameterType", type=StringType)
sgen_FeatureParameter.attributes={sgen_FeatureParameter_optional, sgen_FeatureParameter_parameterType}

# sgen_FeatureTypeLibrary class attributes and methods
sgen_FeatureTypeLibrary_name: Property = Property(name="name", type=StringType)
sgen_FeatureTypeLibrary.attributes={sgen_FeatureTypeLibrary_name}

# sgen_EObject class attributes and methods

# sgen_DeprecatableElement class attributes and methods
sgen_DeprecatableElement_deprecated: Property = Property(name="deprecated", type=BooleanType)
sgen_DeprecatableElement_comment: Property = Property(name="comment", type=StringType)
sgen_DeprecatableElement.attributes={sgen_DeprecatableElement_deprecated, sgen_DeprecatableElement_comment}

# sgen_Expression class attributes and methods

# Relationships
entries0: BinaryAssociation = BinaryAssociation(
    name="entries0",
    ends={
        Property(name="sgen_GeneratorEntry", type=sgen_GeneratorModel, multiplicity=Multiplicity(1, 1)),
        Property(name="sgen_GeneratorModel", type=sgen_GeneratorEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties1: BinaryAssociation = BinaryAssociation(
    name="properties1",
    ends={
        Property(name="sgen_Property", type=sgen_GeneratorModel, multiplicity=Multiplicity(1, 1)),
        Property(name="sgen_GeneratorModel2", type=sgen_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
configurations3: BinaryAssociation = BinaryAssociation(
    name="configurations3",
    ends={
        Property(name="sgen_FeatureConfiguration", type=sgen_GeneratorConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="sgen_GeneratorConfiguration", type=sgen_FeatureConfiguration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
featureType6: BinaryAssociation = BinaryAssociation(
    name="featureType6",
    ends={
        Property(name="FeatureType", type=sgen_FeatureParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters", type=sgen_FeatureType, multiplicity=Multiplicity(0, 1))
    }
)
type7: BinaryAssociation = BinaryAssociation(
    name="type7",
    ends={
        Property(name="sgen_FeatureType9", type=sgen_FeatureConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="sgen_FeatureConfiguration8", type=sgen_FeatureType, multiplicity=Multiplicity(0, 1))
    }
)
parameterValues10: BinaryAssociation = BinaryAssociation(
    name="parameterValues10",
    ends={
        Property(name="FeatureParameterValue", type=sgen_FeatureConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="featureConfiguration", type=sgen_FeatureParameterValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters4: BinaryAssociation = BinaryAssociation(
    name="parameters4",
    ends={
        Property(name="FeatureParameter", type=sgen_FeatureType, multiplicity=Multiplicity(1, 1)),
        Property(name="featureType", type=sgen_FeatureParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
library5: BinaryAssociation = BinaryAssociation(
    name="library5",
    ends={
        Property(name="sgen_FeatureTypeLibrary", type=sgen_FeatureType, multiplicity=Multiplicity(1, 1)),
        Property(name="sgen_FeatureType", type=sgen_FeatureTypeLibrary, multiplicity=Multiplicity(1, 1))
    }
)
features13: BinaryAssociation = BinaryAssociation(
    name="features13",
    ends={
        Property(name="sgen_FeatureConfiguration15", type=sgen_GeneratorEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="sgen_GeneratorEntry14", type=sgen_FeatureConfiguration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter16: BinaryAssociation = BinaryAssociation(
    name="parameter16",
    ends={
        Property(name="sgen_FeatureParameter", type=sgen_FeatureParameterValue, multiplicity=Multiplicity(1, 1)),
        Property(name="sgen_FeatureParameterValue", type=sgen_FeatureParameter, multiplicity=Multiplicity(0, 1))
    }
)
elementRef11: BinaryAssociation = BinaryAssociation(
    name="elementRef11",
    ends={
        Property(name="sgen_EObject", type=sgen_GeneratorEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="sgen_GeneratorEntry12", type=sgen_EObject, multiplicity=Multiplicity(0, 1))
    }
)
featureConfiguration17: BinaryAssociation = BinaryAssociation(
    name="featureConfiguration17",
    ends={
        Property(name="FeatureConfiguration", type=sgen_FeatureParameterValue, multiplicity=Multiplicity(1, 1)),
        Property(name="parameterValues", type=sgen_FeatureConfiguration, multiplicity=Multiplicity(0, 1))
    }
)
expression18: BinaryAssociation = BinaryAssociation(
    name="expression18",
    ends={
        Property(name="sgen_Expression", type=sgen_FeatureParameterValue, multiplicity=Multiplicity(1, 1)),
        Property(name="sgen_FeatureParameterValue19", type=sgen_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
types20: BinaryAssociation = BinaryAssociation(
    name="types20",
    ends={
        Property(name="sgen_FeatureType22", type=sgen_FeatureTypeLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="sgen_FeatureTypeLibrary21", type=sgen_FeatureType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_sgen_FeatureParameter_NamedElement = Generalization(general=NamedElement, specific=sgen_FeatureParameter)
gen_sgen_FeatureParameter_DeprecatableElement = Generalization(general=DeprecatableElement, specific=sgen_FeatureParameter)
gen_sgen_FeatureType_NamedElement = Generalization(general=NamedElement, specific=sgen_FeatureType)
gen_sgen_FeatureType_DeprecatableElement = Generalization(general=DeprecatableElement, specific=sgen_FeatureType)

# Domain Model
domain_model = DomainModel(
    name="sgen",
    types={sgen_GeneratorModel, sgen_GeneratorEntry, sgen_Property, sgen_GeneratorConfiguration, sgen_FeatureConfiguration, sgen_FeatureParameterValue, sgen_FeatureType, NamedElement, DeprecatableElement, sgen_FeatureParameter, sgen_FeatureTypeLibrary, sgen_EObject, sgen_DeprecatableElement, sgen_Expression, ParameterTypes},
    associations={entries0, properties1, configurations3, featureType6, type7, parameterValues10, parameters4, library5, features13, parameter16, elementRef11, featureConfiguration17, expression18, types20},
    generalizations={gen_sgen_FeatureParameter_NamedElement, gen_sgen_FeatureParameter_DeprecatableElement, gen_sgen_FeatureType_NamedElement, gen_sgen_FeatureType_DeprecatableElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)