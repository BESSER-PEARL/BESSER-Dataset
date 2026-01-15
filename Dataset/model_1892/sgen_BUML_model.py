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
sgen_FeatureTypeLibrary = Class(name="sgen::FeatureTypeLibrary")
sgen_GeneratorModel = Class(name="sgen::GeneratorModel")
sgen_GeneratorEntry = Class(name="sgen::GeneratorEntry")
sgen_GeneratorConfiguration = Class(name="sgen::GeneratorConfiguration")
sgen_FeatureConfiguration = Class(name="sgen::FeatureConfiguration")
sgen_FeatureType = Class(name="sgen::FeatureType")
NamedElement = Class(name="NamedElement")
DeprecatableElement = Class(name="DeprecatableElement")
sgen_FeatureParameter = Class(name="sgen::FeatureParameter")
sgen_EObject = Class(name="sgen::EObject")
sgen_FeatureParameterValue = Class(name="sgen::FeatureParameterValue")
sgen_BoolLiteral = Class(name="sgen::BoolLiteral")
Literal = Class(name="Literal")
sgen_Literal = Class(name="sgen::Literal", is_abstract=True)
sgen_IntLiteral = Class(name="sgen::IntLiteral")
sgen_RealLiteral = Class(name="sgen::RealLiteral")
sgen_StringLiteral = Class(name="sgen::StringLiteral")
sgen_DeprecatableElement = Class(name="sgen::DeprecatableElement")

# sgen_FeatureTypeLibrary class attributes and methods
sgen_FeatureTypeLibrary_name: Property = Property(name="name", type=StringType)
sgen_FeatureTypeLibrary.attributes={sgen_FeatureTypeLibrary_name}

# sgen_GeneratorModel class attributes and methods
sgen_GeneratorModel_generatorId: Property = Property(name="generatorId", type=StringType)
sgen_GeneratorModel.attributes={sgen_GeneratorModel_generatorId}

# sgen_GeneratorEntry class attributes and methods
sgen_GeneratorEntry_contentType: Property = Property(name="contentType", type=StringType)
sgen_GeneratorEntry_m_getFeatureConfiguration: Method = Method(name="getFeatureConfiguration", parameters={Parameter(name='featureName')}, type=StringType)
sgen_GeneratorEntry_m_getFeatureParameterValue: Method = Method(name="getFeatureParameterValue", parameters={Parameter(name='paramName'), Parameter(name='featureName')}, type=StringType)
sgen_GeneratorEntry.attributes={sgen_GeneratorEntry_contentType}
sgen_GeneratorEntry.methods={sgen_GeneratorEntry_m_getFeatureConfiguration, sgen_GeneratorEntry_m_getFeatureParameterValue}

# sgen_GeneratorConfiguration class attributes and methods

# sgen_FeatureConfiguration class attributes and methods
sgen_FeatureConfiguration_m_getParameterValue: Method = Method(name="getParameterValue", parameters={Parameter(name='parameterName')}, type=StringType)
sgen_FeatureConfiguration.methods={sgen_FeatureConfiguration_m_getParameterValue}

# sgen_FeatureType class attributes and methods
sgen_FeatureType_optional: Property = Property(name="optional", type=BooleanType)
sgen_FeatureType.attributes={sgen_FeatureType_optional}

# NamedElement class attributes and methods

# DeprecatableElement class attributes and methods

# sgen_FeatureParameter class attributes and methods
sgen_FeatureParameter_optional: Property = Property(name="optional", type=BooleanType)
sgen_FeatureParameter_parameterType: Property = Property(name="parameterType", type=StringType)
sgen_FeatureParameter.attributes={sgen_FeatureParameter_parameterType, sgen_FeatureParameter_optional}

# sgen_EObject class attributes and methods

# sgen_FeatureParameterValue class attributes and methods
sgen_FeatureParameterValue_m_setValue: Method = Method(name="setValue", parameters={Parameter(name='string')})
sgen_FeatureParameterValue_m_setValue: Method = Method(name="setValue", parameters={Parameter(name='boolean')})
sgen_FeatureParameterValue_m_getStringValue: Method = Method(name="getStringValue", parameters={}, type=StringType)
sgen_FeatureParameterValue_m_getBooleanValue: Method = Method(name="getBooleanValue", parameters={}, type=BooleanType)
sgen_FeatureParameterValue.methods={sgen_FeatureParameterValue_m_getBooleanValue, sgen_FeatureParameterValue_m_setValue, sgen_FeatureParameterValue_m_setValue, sgen_FeatureParameterValue_m_getStringValue}

# sgen_BoolLiteral class attributes and methods
sgen_BoolLiteral_value: Property = Property(name="value", type=BooleanType)
sgen_BoolLiteral.attributes={sgen_BoolLiteral_value}

# Literal class attributes and methods

# sgen_Literal class attributes and methods

# sgen_IntLiteral class attributes and methods
sgen_IntLiteral_value: Property = Property(name="value", type=IntegerType)
sgen_IntLiteral.attributes={sgen_IntLiteral_value}

# sgen_RealLiteral class attributes and methods
sgen_RealLiteral_value: Property = Property(name="value", type=FloatType)
sgen_RealLiteral.attributes={sgen_RealLiteral_value}

# sgen_StringLiteral class attributes and methods
sgen_StringLiteral_value: Property = Property(name="value", type=StringType)
sgen_StringLiteral.attributes={sgen_StringLiteral_value}

# sgen_DeprecatableElement class attributes and methods
sgen_DeprecatableElement_deprecated: Property = Property(name="deprecated", type=BooleanType)
sgen_DeprecatableElement_comment: Property = Property(name="comment", type=StringType)
sgen_DeprecatableElement.attributes={sgen_DeprecatableElement_comment, sgen_DeprecatableElement_deprecated}

# Relationships
library3: BinaryAssociation = BinaryAssociation(
    name="library3",
    ends={
        Property(name="sgen_FeatureTypeLibrary", type=sgen_FeatureType, multiplicity=Multiplicity(1, 1)),
        Property(name="sgen_FeatureType", type=sgen_FeatureTypeLibrary, multiplicity=Multiplicity(1, 1))
    }
)
featureType4: BinaryAssociation = BinaryAssociation(
    name="featureType4",
    ends={
        Property(name="FeatureType", type=sgen_FeatureParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters", type=sgen_FeatureType, multiplicity=Multiplicity(0, 1))
    }
)
entries0: BinaryAssociation = BinaryAssociation(
    name="entries0",
    ends={
        Property(name="sgen_GeneratorEntry", type=sgen_GeneratorModel, multiplicity=Multiplicity(1, 1)),
        Property(name="sgen_GeneratorModel", type=sgen_GeneratorEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
configurations1: BinaryAssociation = BinaryAssociation(
    name="configurations1",
    ends={
        Property(name="sgen_FeatureConfiguration", type=sgen_GeneratorConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="sgen_GeneratorConfiguration", type=sgen_FeatureConfiguration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters2: BinaryAssociation = BinaryAssociation(
    name="parameters2",
    ends={
        Property(name="FeatureParameter", type=sgen_FeatureType, multiplicity=Multiplicity(1, 1)),
        Property(name="featureType", type=sgen_FeatureParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elementRef9: BinaryAssociation = BinaryAssociation(
    name="elementRef9",
    ends={
        Property(name="sgen_EObject", type=sgen_GeneratorEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="sgen_GeneratorEntry10", type=sgen_EObject, multiplicity=Multiplicity(0, 1))
    }
)
features11: BinaryAssociation = BinaryAssociation(
    name="features11",
    ends={
        Property(name="sgen_FeatureConfiguration13", type=sgen_GeneratorEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="sgen_GeneratorEntry12", type=sgen_FeatureConfiguration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type5: BinaryAssociation = BinaryAssociation(
    name="type5",
    ends={
        Property(name="sgen_FeatureType7", type=sgen_FeatureConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="sgen_FeatureConfiguration6", type=sgen_FeatureType, multiplicity=Multiplicity(0, 1))
    }
)
parameterValues8: BinaryAssociation = BinaryAssociation(
    name="parameterValues8",
    ends={
        Property(name="FeatureParameterValue", type=sgen_FeatureConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="featureConfiguration", type=sgen_FeatureParameterValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter14: BinaryAssociation = BinaryAssociation(
    name="parameter14",
    ends={
        Property(name="sgen_FeatureParameter", type=sgen_FeatureParameterValue, multiplicity=Multiplicity(1, 1)),
        Property(name="sgen_FeatureParameterValue", type=sgen_FeatureParameter, multiplicity=Multiplicity(0, 1))
    }
)
featureConfiguration15: BinaryAssociation = BinaryAssociation(
    name="featureConfiguration15",
    ends={
        Property(name="FeatureConfiguration", type=sgen_FeatureParameterValue, multiplicity=Multiplicity(1, 1)),
        Property(name="parameterValues", type=sgen_FeatureConfiguration, multiplicity=Multiplicity(0, 1))
    }
)
expression16: BinaryAssociation = BinaryAssociation(
    name="expression16",
    ends={
        Property(name="sgen_Literal", type=sgen_FeatureParameterValue, multiplicity=Multiplicity(1, 1)),
        Property(name="sgen_FeatureParameterValue17", type=sgen_Literal, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
types18: BinaryAssociation = BinaryAssociation(
    name="types18",
    ends={
        Property(name="sgen_FeatureType20", type=sgen_FeatureTypeLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="sgen_FeatureTypeLibrary19", type=sgen_FeatureType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_sgen_FeatureParameter_NamedElement = Generalization(general=NamedElement, specific=sgen_FeatureParameter)
gen_sgen_FeatureParameter_DeprecatableElement = Generalization(general=DeprecatableElement, specific=sgen_FeatureParameter)
gen_sgen_FeatureType_NamedElement = Generalization(general=NamedElement, specific=sgen_FeatureType)
gen_sgen_FeatureType_DeprecatableElement = Generalization(general=DeprecatableElement, specific=sgen_FeatureType)
gen_sgen_BoolLiteral_Literal = Generalization(general=Literal, specific=sgen_BoolLiteral)
gen_sgen_IntLiteral_Literal = Generalization(general=Literal, specific=sgen_IntLiteral)
gen_sgen_RealLiteral_Literal = Generalization(general=Literal, specific=sgen_RealLiteral)
gen_sgen_StringLiteral_Literal = Generalization(general=Literal, specific=sgen_StringLiteral)

# Domain Model
domain_model = DomainModel(
    name="sgen",
    types={sgen_FeatureTypeLibrary, sgen_GeneratorModel, sgen_GeneratorEntry, sgen_GeneratorConfiguration, sgen_FeatureConfiguration, sgen_FeatureType, NamedElement, DeprecatableElement, sgen_FeatureParameter, sgen_EObject, sgen_FeatureParameterValue, sgen_BoolLiteral, Literal, sgen_Literal, sgen_IntLiteral, sgen_RealLiteral, sgen_StringLiteral, sgen_DeprecatableElement, ParameterTypes},
    associations={library3, featureType4, entries0, configurations1, parameters2, elementRef9, features11, type5, parameterValues8, parameter14, featureConfiguration15, expression16, types18},
    generalizations={gen_sgen_FeatureParameter_NamedElement, gen_sgen_FeatureParameter_DeprecatableElement, gen_sgen_FeatureType_NamedElement, gen_sgen_FeatureType_DeprecatableElement, gen_sgen_BoolLiteral_Literal, gen_sgen_IntLiteral_Literal, gen_sgen_RealLiteral_Literal, gen_sgen_StringLiteral_Literal},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)