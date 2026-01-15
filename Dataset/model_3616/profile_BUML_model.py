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
BindingKind: Enumeration = Enumeration(
    name="BindingKind",
    literals={
            EnumerationLiteral(name="Static"),
			EnumerationLiteral(name="Dynamic")
    }
)

ValueSetType: Enumeration = Enumeration(
    name="ValueSetType",
    literals={
            EnumerationLiteral(name="Extensional"),
			EnumerationLiteral(name="Intensional")
    }
)

StatusKind: Enumeration = Enumeration(
    name="StatusKind",
    literals={
            EnumerationLiteral(name="Active"),
			EnumerationLiteral(name="Inactive")
    }
)

Extensibility: Enumeration = Enumeration(
    name="Extensibility",
    literals={
            EnumerationLiteral(name="NEA"),
			EnumerationLiteral(name="CEA")
    }
)

Guidance: Enumeration = Enumeration(
    name="Guidance",
    literals={
            EnumerationLiteral(name="FIXED"),
			EnumerationLiteral(name="CLOSED"),
			EnumerationLiteral(name="EXTEND"),
			EnumerationLiteral(name="RESTRICT"),
			EnumerationLiteral(name="OPEN")
    }
)

ValueSetBinding: Enumeration = Enumeration(
    name="ValueSetBinding",
    literals={
            EnumerationLiteral(name="Direct"),
			EnumerationLiteral(name="Indirect")
    }
)

# Classes
profile_CD = Class(name="profile::CD")
profile_CR = Class(name="profile::CR")
profile_ConceptDomainConstraint = Class(name="profile::ConceptDomainConstraint")
profile_ConceptDomain = Class(name="profile::ConceptDomain")
profile_Property = Class(name="profile::Property")
profile_Class = Class(name="profile::Class")
profile_CodeSystemConstraint = Class(name="profile::CodeSystemConstraint")
profile_CodeSystemVersion = Class(name="profile::CodeSystemVersion")
profile_Enumeration = Class(name="profile::Enumeration")
profile_ValueSetConstraint = Class(name="profile::ValueSetConstraint")
profile_ValueSetVersion = Class(name="profile::ValueSetVersion")
profile_ValueSetCode = Class(name="profile::ValueSetCode")
profile_ValueSetConstraints = Class(name="profile::ValueSetConstraints")
profile_ContextToValueSet = Class(name="profile::ContextToValueSet")
profile_EnumerationLiteral = Class(name="profile::EnumerationLiteral")
profile_ValueSetContextBinding = Class(name="profile::ValueSetContextBinding")
profile_UsageContext = Class(name="profile::UsageContext")
profile_Context = Class(name="profile::Context")
profile_CodedType = Class(name="profile::CodedType")
profile_Classifier = Class(name="profile::Classifier")
profile_NullValueSetConstraint = Class(name="profile::NullValueSetConstraint")

# profile_CD class attributes and methods
profile_CD_code: Property = Property(name="code", type=StringType)
profile_CD_codeSystem: Property = Property(name="codeSystem", type=StringType)
profile_CD_codeSystemName: Property = Property(name="codeSystemName", type=StringType)
profile_CD_codeSystemVersion: Property = Property(name="codeSystemVersion", type=StringType)
profile_CD_displayName: Property = Property(name="displayName", type=StringType)
profile_CD.attributes={profile_CD_codeSystemVersion, profile_CD_codeSystem, profile_CD_codeSystemName, profile_CD_code, profile_CD_displayName}

# profile_CR class attributes and methods
profile_CR_inverted: Property = Property(name="inverted", type=StringType)
profile_CR.attributes={profile_CR_inverted}

# profile_ConceptDomainConstraint class attributes and methods
profile_ConceptDomainConstraint_identifier: Property = Property(name="identifier", type=StringType)
profile_ConceptDomainConstraint_name: Property = Property(name="name", type=StringType)
profile_ConceptDomainConstraint.attributes={profile_ConceptDomainConstraint_name, profile_ConceptDomainConstraint_identifier}

# profile_ConceptDomain class attributes and methods
profile_ConceptDomain_identifier: Property = Property(name="identifier", type=StringType)
profile_ConceptDomain_fullName: Property = Property(name="fullName", type=StringType)
profile_ConceptDomain_status: Property = Property(name="status", type=StringType)
profile_ConceptDomain_statusDate: Property = Property(name="statusDate", type=StringType)
profile_ConceptDomain.attributes={profile_ConceptDomain_identifier, profile_ConceptDomain_fullName, profile_ConceptDomain_status, profile_ConceptDomain_statusDate}

# profile_Property class attributes and methods

# profile_Class class attributes and methods

# profile_CodeSystemConstraint class attributes and methods
profile_CodeSystemConstraint_identifier: Property = Property(name="identifier", type=StringType)
profile_CodeSystemConstraint_name: Property = Property(name="name", type=StringType)
profile_CodeSystemConstraint_version: Property = Property(name="version", type=StringType)
profile_CodeSystemConstraint_binding: Property = Property(name="binding", type=StringType)
profile_CodeSystemConstraint_code: Property = Property(name="code", type=StringType)
profile_CodeSystemConstraint_displayName: Property = Property(name="displayName", type=StringType)
profile_CodeSystemConstraint.attributes={profile_CodeSystemConstraint_displayName, profile_CodeSystemConstraint_code, profile_CodeSystemConstraint_name, profile_CodeSystemConstraint_binding, profile_CodeSystemConstraint_identifier, profile_CodeSystemConstraint_version}

# profile_CodeSystemVersion class attributes and methods
profile_CodeSystemVersion_identifier: Property = Property(name="identifier", type=StringType)
profile_CodeSystemVersion_version: Property = Property(name="version", type=StringType)
profile_CodeSystemVersion_fullName: Property = Property(name="fullName", type=StringType)
profile_CodeSystemVersion_source: Property = Property(name="source", type=StringType)
profile_CodeSystemVersion_url: Property = Property(name="url", type=StringType)
profile_CodeSystemVersion_effectiveDate: Property = Property(name="effectiveDate", type=StringType)
profile_CodeSystemVersion_releaseDate: Property = Property(name="releaseDate", type=StringType)
profile_CodeSystemVersion_status: Property = Property(name="status", type=StringType)
profile_CodeSystemVersion_statusDate: Property = Property(name="statusDate", type=StringType)
profile_CodeSystemVersion_m_getEnumerationName: Method = Method(name="getEnumerationName", parameters={}, type=StringType)
profile_CodeSystemVersion_m_setEnumerationName: Method = Method(name="setEnumerationName", parameters={Parameter(name='name')})
profile_CodeSystemVersion_m_getEnumerationQualifiedName: Method = Method(name="getEnumerationQualifiedName", parameters={}, type=StringType)
profile_CodeSystemVersion.attributes={profile_CodeSystemVersion_status, profile_CodeSystemVersion_effectiveDate, profile_CodeSystemVersion_source, profile_CodeSystemVersion_identifier, profile_CodeSystemVersion_statusDate, profile_CodeSystemVersion_version, profile_CodeSystemVersion_url, profile_CodeSystemVersion_releaseDate, profile_CodeSystemVersion_fullName}
profile_CodeSystemVersion.methods={profile_CodeSystemVersion_m_getEnumerationQualifiedName, profile_CodeSystemVersion_m_setEnumerationName, profile_CodeSystemVersion_m_getEnumerationName}

# profile_Enumeration class attributes and methods

# profile_ValueSetConstraint class attributes and methods
profile_ValueSetConstraint_identifier: Property = Property(name="identifier", type=StringType)
profile_ValueSetConstraint_name: Property = Property(name="name", type=StringType)
profile_ValueSetConstraint_version: Property = Property(name="version", type=StringType)
profile_ValueSetConstraint_binding: Property = Property(name="binding", type=StringType)
profile_ValueSetConstraint_extensibility: Property = Property(name="extensibility", type=StringType)
profile_ValueSetConstraint_guidance: Property = Property(name="guidance", type=StringType)
profile_ValueSetConstraint_uri: Property = Property(name="uri", type=StringType)
profile_ValueSetConstraint.attributes={profile_ValueSetConstraint_extensibility, profile_ValueSetConstraint_version, profile_ValueSetConstraint_name, profile_ValueSetConstraint_identifier, profile_ValueSetConstraint_guidance, profile_ValueSetConstraint_uri, profile_ValueSetConstraint_binding}

# profile_ValueSetVersion class attributes and methods
profile_ValueSetVersion_identifier: Property = Property(name="identifier", type=StringType)
profile_ValueSetVersion_version: Property = Property(name="version", type=StringType)
profile_ValueSetVersion_fullName: Property = Property(name="fullName", type=StringType)
profile_ValueSetVersion_source: Property = Property(name="source", type=StringType)
profile_ValueSetVersion_url: Property = Property(name="url", type=StringType)
profile_ValueSetVersion_definition: Property = Property(name="definition", type=StringType)
profile_ValueSetVersion_effectiveDate: Property = Property(name="effectiveDate", type=StringType)
profile_ValueSetVersion_expirationDate: Property = Property(name="expirationDate", type=StringType)
profile_ValueSetVersion_releaseDate: Property = Property(name="releaseDate", type=StringType)
profile_ValueSetVersion_revisionDate: Property = Property(name="revisionDate", type=StringType)
profile_ValueSetVersion_status: Property = Property(name="status", type=StringType)
profile_ValueSetVersion_statusDate: Property = Property(name="statusDate", type=StringType)
profile_ValueSetVersion_type: Property = Property(name="type", type=StringType)
profile_ValueSetVersion_binding: Property = Property(name="binding", type=StringType)
profile_ValueSetVersion_m_getEnumerationName: Method = Method(name="getEnumerationName", parameters={}, type=StringType)
profile_ValueSetVersion_m_setEnumerationName: Method = Method(name="setEnumerationName", parameters={Parameter(name='name')})
profile_ValueSetVersion_m_getEnumerationQualifiedName: Method = Method(name="getEnumerationQualifiedName", parameters={}, type=StringType)
profile_ValueSetVersion.attributes={profile_ValueSetVersion_type, profile_ValueSetVersion_effectiveDate, profile_ValueSetVersion_binding, profile_ValueSetVersion_source, profile_ValueSetVersion_url, profile_ValueSetVersion_identifier, profile_ValueSetVersion_version, profile_ValueSetVersion_fullName, profile_ValueSetVersion_releaseDate, profile_ValueSetVersion_statusDate, profile_ValueSetVersion_expirationDate, profile_ValueSetVersion_revisionDate, profile_ValueSetVersion_status, profile_ValueSetVersion_definition}
profile_ValueSetVersion.methods={profile_ValueSetVersion_m_getEnumerationQualifiedName, profile_ValueSetVersion_m_getEnumerationName, profile_ValueSetVersion_m_setEnumerationName}

# profile_ValueSetCode class attributes and methods
profile_ValueSetCode_conceptName: Property = Property(name="conceptName", type=StringType)
profile_ValueSetCode_usageNote: Property = Property(name="usageNote", type=StringType)
profile_ValueSetCode.attributes={profile_ValueSetCode_usageNote, profile_ValueSetCode_conceptName}

# profile_ValueSetConstraints class attributes and methods

# profile_ContextToValueSet class attributes and methods
profile_ContextToValueSet_key: Property = Property(name="key", type=StringType)
profile_ContextToValueSet_value: Property = Property(name="value", type=StringType)
profile_ContextToValueSet.attributes={profile_ContextToValueSet_key, profile_ContextToValueSet_value}

# profile_EnumerationLiteral class attributes and methods

# profile_ValueSetContextBinding class attributes and methods
profile_ValueSetContextBinding_effectiveDate: Property = Property(name="effectiveDate", type=StringType)
profile_ValueSetContextBinding.attributes={profile_ValueSetContextBinding_effectiveDate}

# profile_UsageContext class attributes and methods
profile_UsageContext_identifier: Property = Property(name="identifier", type=StringType)
profile_UsageContext_status: Property = Property(name="status", type=StringType)
profile_UsageContext_statusDate: Property = Property(name="statusDate", type=StringType)
profile_UsageContext.attributes={profile_UsageContext_identifier, profile_UsageContext_status, profile_UsageContext_statusDate}

# profile_Context class attributes and methods

# profile_CodedType class attributes and methods

# profile_Classifier class attributes and methods

# profile_NullValueSetConstraint class attributes and methods
profile_NullValueSetConstraint_version: Property = Property(name="version", type=StringType)
profile_NullValueSetConstraint_binding: Property = Property(name="binding", type=StringType)
profile_NullValueSetConstraint_identifier: Property = Property(name="identifier", type=StringType)
profile_NullValueSetConstraint_name: Property = Property(name="name", type=StringType)
profile_NullValueSetConstraint.attributes={profile_NullValueSetConstraint_version, profile_NullValueSetConstraint_name, profile_NullValueSetConstraint_identifier, profile_NullValueSetConstraint_binding}

# Relationships
qualifier0: BinaryAssociation = BinaryAssociation(
    name="qualifier0",
    ends={
        Property(name="profile_CR", type=profile_CD, multiplicity=Multiplicity(1, 1)),
        Property(name="profile_CD", type=profile_CR, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
translation2: BinaryAssociation = BinaryAssociation(
    name="translation2",
    ends={
        Property(name="profile_CD3", type=profile_CD, multiplicity=Multiplicity(1, 1)),
        Property(name="profile_CD1", type=profile_CD, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name4: BinaryAssociation = BinaryAssociation(
    name="name4",
    ends={
        Property(name="profile_CD6", type=profile_CR, multiplicity=Multiplicity(1, 1)),
        Property(name="profile_CR5", type=profile_CD, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value7: BinaryAssociation = BinaryAssociation(
    name="value7",
    ends={
        Property(name="profile_CD9", type=profile_CR, multiplicity=Multiplicity(1, 1)),
        Property(name="profile_CR8", type=profile_CD, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
reference10: BinaryAssociation = BinaryAssociation(
    name="reference10",
    ends={
        Property(name="profile_ConceptDomain", type=profile_ConceptDomainConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="profile_ConceptDomainConstraint", type=profile_ConceptDomain, multiplicity=Multiplicity(0, 1))
    }
)
base_Property11: BinaryAssociation = BinaryAssociation(
    name="base_Property11",
    ends={
        Property(name="profile_Property", type=profile_ConceptDomainConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="profile_ConceptDomainConstraint12", type=profile_Property, multiplicity=Multiplicity(1, 1))
    }
)
base_Class13: BinaryAssociation = BinaryAssociation(
    name="base_Class13",
    ends={
        Property(name="profile_Class", type=profile_ConceptDomain, multiplicity=Multiplicity(1, 1)),
        Property(name="profile_ConceptDomain14", type=profile_Class, multiplicity=Multiplicity(1, 1))
    }
)
reference15: BinaryAssociation = BinaryAssociation(
    name="reference15",
    ends={
        Property(name="profile_CodeSystemVersion", type=profile_CodeSystemConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="profile_CodeSystemConstraint", type=profile_CodeSystemVersion, multiplicity=Multiplicity(0, 1))
    }
)
qualifier16: BinaryAssociation = BinaryAssociation(
    name="qualifier16",
    ends={
        Property(name="profile_CR18", type=profile_CodeSystemConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="profile_CodeSystemConstraint17", type=profile_CR, multiplicity=Multiplicity(0, 9999))
    }
)
base_Property19: BinaryAssociation = BinaryAssociation(
    name="base_Property19",
    ends={
        Property(name="profile_Property21", type=profile_CodeSystemConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="profile_CodeSystemConstraint20", type=profile_Property, multiplicity=Multiplicity(1, 1))
    }
)
base_Enumeration22: BinaryAssociation = BinaryAssociation(
    name="base_Enumeration22",
    ends={
        Property(name="profile_Enumeration", type=profile_CodeSystemVersion, multiplicity=Multiplicity(1, 1)),
        Property(name="profile_CodeSystemVersion23", type=profile_Enumeration, multiplicity=Multiplicity(1, 1))
    }
)
reference24: BinaryAssociation = BinaryAssociation(
    name="reference24",
    ends={
        Property(name="profile_ValueSetVersion", type=profile_ValueSetConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="profile_ValueSetConstraint", type=profile_ValueSetVersion, multiplicity=Multiplicity(0, 1))
    }
)
base_Property25: BinaryAssociation = BinaryAssociation(
    name="base_Property25",
    ends={
        Property(name="profile_Property27", type=profile_ValueSetConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="profile_ValueSetConstraint26", type=profile_Property, multiplicity=Multiplicity(1, 1))
    }
)
codeSystem28: BinaryAssociation = BinaryAssociation(
    name="codeSystem28",
    ends={
        Property(name="profile_CodeSystemVersion30", type=profile_ValueSetVersion, multiplicity=Multiplicity(1, 1)),
        Property(name="profile_ValueSetVersion29", type=profile_CodeSystemVersion, multiplicity=Multiplicity(0, 1))
    }
)
base_Enumeration31: BinaryAssociation = BinaryAssociation(
    name="base_Enumeration31",
    ends={
        Property(name="profile_Enumeration33", type=profile_ValueSetVersion, multiplicity=Multiplicity(1, 1)),
        Property(name="profile_ValueSetVersion32", type=profile_Enumeration, multiplicity=Multiplicity(1, 1))
    }
)
base_Class45: BinaryAssociation = BinaryAssociation(
    name="base_Class45",
    ends={
        Property(name="profile_Class47", type=profile_ValueSetContextBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="profile_ValueSetContextBinding46", type=profile_Class, multiplicity=Multiplicity(1, 1))
    }
)
base_Class48: BinaryAssociation = BinaryAssociation(
    name="base_Class48",
    ends={
        Property(name="profile_Class50", type=profile_UsageContext, multiplicity=Multiplicity(1, 1)),
        Property(name="profile_UsageContext49", type=profile_Class, multiplicity=Multiplicity(1, 1))
    }
)
base_Property51: BinaryAssociation = BinaryAssociation(
    name="base_Property51",
    ends={
        Property(name="profile_Property52", type=profile_ValueSetConstraints, multiplicity=Multiplicity(1, 1)),
        Property(name="profile_ValueSetConstraints", type=profile_Property, multiplicity=Multiplicity(1, 1))
    }
)
codeSystem34: BinaryAssociation = BinaryAssociation(
    name="codeSystem34",
    ends={
        Property(name="profile_CodeSystemVersion35", type=profile_ValueSetCode, multiplicity=Multiplicity(1, 1)),
        Property(name="profile_ValueSetCode", type=profile_CodeSystemVersion, multiplicity=Multiplicity(0, 1))
    }
)
constraints53: BinaryAssociation = BinaryAssociation(
    name="constraints53",
    ends={
        Property(name="profile_ContextToValueSet", type=profile_ValueSetConstraints, multiplicity=Multiplicity(1, 1)),
        Property(name="profile_ValueSetConstraints54", type=profile_ContextToValueSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
base_EnumerationLiteral36: BinaryAssociation = BinaryAssociation(
    name="base_EnumerationLiteral36",
    ends={
        Property(name="profile_EnumerationLiteral", type=profile_ValueSetCode, multiplicity=Multiplicity(1, 1)),
        Property(name="profile_ValueSetCode37", type=profile_EnumerationLiteral, multiplicity=Multiplicity(1, 1))
    }
)
conceptDomain38: BinaryAssociation = BinaryAssociation(
    name="conceptDomain38",
    ends={
        Property(name="profile_ConceptDomain39", type=profile_ValueSetContextBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="profile_ValueSetContextBinding", type=profile_ConceptDomain, multiplicity=Multiplicity(1, 1))
    }
)
valueSet40: BinaryAssociation = BinaryAssociation(
    name="valueSet40",
    ends={
        Property(name="profile_ValueSetVersion42", type=profile_ValueSetContextBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="profile_ValueSetContextBinding41", type=profile_ValueSetVersion, multiplicity=Multiplicity(1, 1))
    }
)
usageContext43: BinaryAssociation = BinaryAssociation(
    name="usageContext43",
    ends={
        Property(name="profile_UsageContext", type=profile_ValueSetContextBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="profile_ValueSetContextBinding44", type=profile_UsageContext, multiplicity=Multiplicity(1, 1))
    }
)
base_Property57: BinaryAssociation = BinaryAssociation(
    name="base_Property57",
    ends={
        Property(name="profile_Property59", type=profile_NullValueSetConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="profile_NullValueSetConstraint58", type=profile_Property, multiplicity=Multiplicity(1, 1))
    }
)
base_Enumeration60: BinaryAssociation = BinaryAssociation(
    name="base_Enumeration60",
    ends={
        Property(name="profile_Enumeration61", type=profile_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="profile_Context", type=profile_Enumeration, multiplicity=Multiplicity(1, 1))
    }
)
base_Classifier62: BinaryAssociation = BinaryAssociation(
    name="base_Classifier62",
    ends={
        Property(name="profile_Classifier", type=profile_CodedType, multiplicity=Multiplicity(1, 1)),
        Property(name="profile_CodedType", type=profile_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
reference55: BinaryAssociation = BinaryAssociation(
    name="reference55",
    ends={
        Property(name="profile_ValueSetVersion56", type=profile_NullValueSetConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="profile_NullValueSetConstraint", type=profile_ValueSetVersion, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="profile",
    types={profile_CD, profile_CR, profile_ConceptDomainConstraint, profile_ConceptDomain, profile_Property, profile_Class, profile_CodeSystemConstraint, profile_CodeSystemVersion, profile_Enumeration, profile_ValueSetConstraint, profile_ValueSetVersion, profile_ValueSetCode, profile_ValueSetConstraints, profile_ContextToValueSet, profile_EnumerationLiteral, profile_ValueSetContextBinding, profile_UsageContext, profile_Context, profile_CodedType, profile_Classifier, profile_NullValueSetConstraint, BindingKind, ValueSetType, StatusKind, Extensibility, Guidance, ValueSetBinding},
    associations={qualifier0, translation2, name4, value7, reference10, base_Property11, base_Class13, reference15, qualifier16, base_Property19, base_Enumeration22, reference24, base_Property25, codeSystem28, base_Enumeration31, base_Class45, base_Class48, base_Property51, codeSystem34, constraints53, base_EnumerationLiteral36, conceptDomain38, valueSet40, usageContext43, base_Property57, base_Enumeration60, base_Classifier62, reference55},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)