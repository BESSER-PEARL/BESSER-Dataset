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
Uppaal_ImportsType = Class(name="Uppaal::ImportsType")
Uppaal_DeclarationType = Class(name="Uppaal::DeclarationType")
Uppaal_DocumentRoot = Class(name="Uppaal::DocumentRoot")
Uppaal_EStringToStringMapEntry = Class(name="Uppaal::EStringToStringMapEntry")
Uppaal_InstantiationType = Class(name="Uppaal::InstantiationType")
Uppaal_InitType = Class(name="Uppaal::InitType")
Uppaal_ParameterType = Class(name="Uppaal::ParameterType")
Uppaal_LabelType = Class(name="Uppaal::LabelType")
Uppaal_LocationType = Class(name="Uppaal::LocationType")
Uppaal_NailType = Class(name="Uppaal::NailType")
Uppaal_NameType = Class(name="Uppaal::NameType")
Uppaal_NtaType = Class(name="Uppaal::NtaType")
Uppaal_SourceType = Class(name="Uppaal::SourceType")
Uppaal_SystemType = Class(name="Uppaal::SystemType")
Uppaal_TargetType = Class(name="Uppaal::TargetType")
Uppaal_TemplateType = Class(name="Uppaal::TemplateType")
Uppaal_TransitionType = Class(name="Uppaal::TransitionType")

# Uppaal_ImportsType class attributes and methods
Uppaal_ImportsType_mixed: Property = Property(name="mixed", type=StringType)
Uppaal_ImportsType.attributes={Uppaal_ImportsType_mixed}

# Uppaal_DeclarationType class attributes and methods
Uppaal_DeclarationType_mixed: Property = Property(name="mixed", type=StringType)
Uppaal_DeclarationType.attributes={Uppaal_DeclarationType_mixed}

# Uppaal_DocumentRoot class attributes and methods
Uppaal_DocumentRoot_mixed: Property = Property(name="mixed", type=StringType)
Uppaal_DocumentRoot_committed: Property = Property(name="committed", type=StringType)
Uppaal_DocumentRoot_urgent: Property = Property(name="urgent", type=StringType)
Uppaal_DocumentRoot.attributes={Uppaal_DocumentRoot_urgent, Uppaal_DocumentRoot_mixed, Uppaal_DocumentRoot_committed}

# Uppaal_EStringToStringMapEntry class attributes and methods

# Uppaal_InstantiationType class attributes and methods
Uppaal_InstantiationType_mixed: Property = Property(name="mixed", type=StringType)
Uppaal_InstantiationType.attributes={Uppaal_InstantiationType_mixed}

# Uppaal_InitType class attributes and methods
Uppaal_InitType_ref: Property = Property(name="ref", type=StringType)
Uppaal_InitType.attributes={Uppaal_InitType_ref}

# Uppaal_ParameterType class attributes and methods
Uppaal_ParameterType_y: Property = Property(name="y", type=StringType)
Uppaal_ParameterType_mixed: Property = Property(name="mixed", type=StringType)
Uppaal_ParameterType_x: Property = Property(name="x", type=StringType)
Uppaal_ParameterType.attributes={Uppaal_ParameterType_y, Uppaal_ParameterType_mixed, Uppaal_ParameterType_x}

# Uppaal_LabelType class attributes and methods
Uppaal_LabelType_mixed: Property = Property(name="mixed", type=StringType)
Uppaal_LabelType_kind: Property = Property(name="kind", type=StringType)
Uppaal_LabelType_x: Property = Property(name="x", type=StringType)
Uppaal_LabelType_y: Property = Property(name="y", type=StringType)
Uppaal_LabelType.attributes={Uppaal_LabelType_x, Uppaal_LabelType_kind, Uppaal_LabelType_y, Uppaal_LabelType_mixed}

# Uppaal_LocationType class attributes and methods
Uppaal_LocationType_committed: Property = Property(name="committed", type=StringType)
Uppaal_LocationType_color: Property = Property(name="color", type=StringType)
Uppaal_LocationType_urgent: Property = Property(name="urgent", type=StringType)
Uppaal_LocationType_id: Property = Property(name="id", type=StringType)
Uppaal_LocationType_x: Property = Property(name="x", type=StringType)
Uppaal_LocationType_y: Property = Property(name="y", type=StringType)
Uppaal_LocationType.attributes={Uppaal_LocationType_y, Uppaal_LocationType_id, Uppaal_LocationType_x, Uppaal_LocationType_urgent, Uppaal_LocationType_color, Uppaal_LocationType_committed}

# Uppaal_NailType class attributes and methods
Uppaal_NailType_x: Property = Property(name="x", type=StringType)
Uppaal_NailType_y: Property = Property(name="y", type=StringType)
Uppaal_NailType.attributes={Uppaal_NailType_y, Uppaal_NailType_x}

# Uppaal_NameType class attributes and methods
Uppaal_NameType_mixed: Property = Property(name="mixed", type=StringType)
Uppaal_NameType_x: Property = Property(name="x", type=StringType)
Uppaal_NameType_y: Property = Property(name="y", type=StringType)
Uppaal_NameType.attributes={Uppaal_NameType_y, Uppaal_NameType_mixed, Uppaal_NameType_x}

# Uppaal_NtaType class attributes and methods

# Uppaal_SourceType class attributes and methods
Uppaal_SourceType_ref: Property = Property(name="ref", type=StringType)
Uppaal_SourceType.attributes={Uppaal_SourceType_ref}

# Uppaal_SystemType class attributes and methods
Uppaal_SystemType_mixed: Property = Property(name="mixed", type=StringType)
Uppaal_SystemType.attributes={Uppaal_SystemType_mixed}

# Uppaal_TargetType class attributes and methods
Uppaal_TargetType_ref: Property = Property(name="ref", type=StringType)
Uppaal_TargetType.attributes={Uppaal_TargetType_ref}

# Uppaal_TemplateType class attributes and methods

# Uppaal_TransitionType class attributes and methods
Uppaal_TransitionType_color: Property = Property(name="color", type=StringType)
Uppaal_TransitionType_id: Property = Property(name="id", type=StringType)
Uppaal_TransitionType_x: Property = Property(name="x", type=StringType)
Uppaal_TransitionType_y: Property = Property(name="y", type=StringType)
Uppaal_TransitionType.attributes={Uppaal_TransitionType_x, Uppaal_TransitionType_y, Uppaal_TransitionType_color, Uppaal_TransitionType_id}

# Relationships
imports6: BinaryAssociation = BinaryAssociation(
    name="imports6",
    ends={
        Property(name="Uppaal_ImportsType", type=Uppaal_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Uppaal_DocumentRoot7", type=Uppaal_ImportsType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xMLNSPrefixMap0: BinaryAssociation = BinaryAssociation(
    name="xMLNSPrefixMap0",
    ends={
        Property(name="Uppaal_EStringToStringMapEntry", type=Uppaal_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Uppaal_DocumentRoot", type=Uppaal_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xSISchemaLocation1: BinaryAssociation = BinaryAssociation(
    name="xSISchemaLocation1",
    ends={
        Property(name="Uppaal_EStringToStringMapEntry3", type=Uppaal_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Uppaal_DocumentRoot2", type=Uppaal_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declaration4: BinaryAssociation = BinaryAssociation(
    name="declaration4",
    ends={
        Property(name="Uppaal_DeclarationType", type=Uppaal_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Uppaal_DocumentRoot5", type=Uppaal_DeclarationType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instantiation10: BinaryAssociation = BinaryAssociation(
    name="instantiation10",
    ends={
        Property(name="Uppaal_InstantiationType", type=Uppaal_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Uppaal_DocumentRoot11", type=Uppaal_InstantiationType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
init8: BinaryAssociation = BinaryAssociation(
    name="init8",
    ends={
        Property(name="Uppaal_InitType", type=Uppaal_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Uppaal_DocumentRoot9", type=Uppaal_InitType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter22: BinaryAssociation = BinaryAssociation(
    name="parameter22",
    ends={
        Property(name="Uppaal_ParameterType", type=Uppaal_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Uppaal_DocumentRoot23", type=Uppaal_ParameterType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
label12: BinaryAssociation = BinaryAssociation(
    name="label12",
    ends={
        Property(name="Uppaal_LabelType", type=Uppaal_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Uppaal_DocumentRoot13", type=Uppaal_LabelType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
location14: BinaryAssociation = BinaryAssociation(
    name="location14",
    ends={
        Property(name="Uppaal_LocationType", type=Uppaal_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Uppaal_DocumentRoot15", type=Uppaal_LocationType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nail16: BinaryAssociation = BinaryAssociation(
    name="nail16",
    ends={
        Property(name="Uppaal_NailType", type=Uppaal_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Uppaal_DocumentRoot17", type=Uppaal_NailType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name18: BinaryAssociation = BinaryAssociation(
    name="name18",
    ends={
        Property(name="Uppaal_NameType", type=Uppaal_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Uppaal_DocumentRoot19", type=Uppaal_NameType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nta20: BinaryAssociation = BinaryAssociation(
    name="nta20",
    ends={
        Property(name="Uppaal_NtaType", type=Uppaal_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Uppaal_DocumentRoot21", type=Uppaal_NtaType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition32: BinaryAssociation = BinaryAssociation(
    name="transition32",
    ends={
        Property(name="Uppaal_TransitionType", type=Uppaal_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Uppaal_DocumentRoot33", type=Uppaal_TransitionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source24: BinaryAssociation = BinaryAssociation(
    name="source24",
    ends={
        Property(name="Uppaal_SourceType", type=Uppaal_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Uppaal_DocumentRoot25", type=Uppaal_SourceType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
system26: BinaryAssociation = BinaryAssociation(
    name="system26",
    ends={
        Property(name="Uppaal_SystemType", type=Uppaal_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Uppaal_DocumentRoot27", type=Uppaal_SystemType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target28: BinaryAssociation = BinaryAssociation(
    name="target28",
    ends={
        Property(name="Uppaal_TargetType", type=Uppaal_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Uppaal_DocumentRoot29", type=Uppaal_TargetType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
template30: BinaryAssociation = BinaryAssociation(
    name="template30",
    ends={
        Property(name="Uppaal_TemplateType", type=Uppaal_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Uppaal_DocumentRoot31", type=Uppaal_TemplateType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name34: BinaryAssociation = BinaryAssociation(
    name="name34",
    ends={
        Property(name="Uppaal_NameType36", type=Uppaal_LocationType, multiplicity=Multiplicity(1, 1)),
        Property(name="Uppaal_LocationType35", type=Uppaal_NameType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
label37: BinaryAssociation = BinaryAssociation(
    name="label37",
    ends={
        Property(name="Uppaal_LabelType39", type=Uppaal_LocationType, multiplicity=Multiplicity(1, 1)),
        Property(name="Uppaal_LocationType38", type=Uppaal_LabelType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declaration43: BinaryAssociation = BinaryAssociation(
    name="declaration43",
    ends={
        Property(name="Uppaal_DeclarationType45", type=Uppaal_NtaType, multiplicity=Multiplicity(1, 1)),
        Property(name="Uppaal_NtaType44", type=Uppaal_DeclarationType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
imports40: BinaryAssociation = BinaryAssociation(
    name="imports40",
    ends={
        Property(name="Uppaal_ImportsType42", type=Uppaal_NtaType, multiplicity=Multiplicity(1, 1)),
        Property(name="Uppaal_NtaType41", type=Uppaal_ImportsType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
system52: BinaryAssociation = BinaryAssociation(
    name="system52",
    ends={
        Property(name="Uppaal_SystemType54", type=Uppaal_NtaType, multiplicity=Multiplicity(1, 1)),
        Property(name="Uppaal_NtaType53", type=Uppaal_SystemType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
template46: BinaryAssociation = BinaryAssociation(
    name="template46",
    ends={
        Property(name="Uppaal_TemplateType48", type=Uppaal_NtaType, multiplicity=Multiplicity(1, 1)),
        Property(name="Uppaal_NtaType47", type=Uppaal_TemplateType, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
instantiation49: BinaryAssociation = BinaryAssociation(
    name="instantiation49",
    ends={
        Property(name="Uppaal_InstantiationType51", type=Uppaal_NtaType, multiplicity=Multiplicity(1, 1)),
        Property(name="Uppaal_NtaType50", type=Uppaal_InstantiationType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
location64: BinaryAssociation = BinaryAssociation(
    name="location64",
    ends={
        Property(name="Uppaal_LocationType66", type=Uppaal_TemplateType, multiplicity=Multiplicity(1, 1)),
        Property(name="Uppaal_TemplateType65", type=Uppaal_LocationType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
init67: BinaryAssociation = BinaryAssociation(
    name="init67",
    ends={
        Property(name="Uppaal_InitType69", type=Uppaal_TemplateType, multiplicity=Multiplicity(1, 1)),
        Property(name="Uppaal_TemplateType68", type=Uppaal_InitType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name55: BinaryAssociation = BinaryAssociation(
    name="name55",
    ends={
        Property(name="Uppaal_NameType57", type=Uppaal_TemplateType, multiplicity=Multiplicity(1, 1)),
        Property(name="Uppaal_TemplateType56", type=Uppaal_NameType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameter58: BinaryAssociation = BinaryAssociation(
    name="parameter58",
    ends={
        Property(name="Uppaal_ParameterType60", type=Uppaal_TemplateType, multiplicity=Multiplicity(1, 1)),
        Property(name="Uppaal_TemplateType59", type=Uppaal_ParameterType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaration61: BinaryAssociation = BinaryAssociation(
    name="declaration61",
    ends={
        Property(name="Uppaal_DeclarationType63", type=Uppaal_TemplateType, multiplicity=Multiplicity(1, 1)),
        Property(name="Uppaal_TemplateType62", type=Uppaal_DeclarationType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nail82: BinaryAssociation = BinaryAssociation(
    name="nail82",
    ends={
        Property(name="Uppaal_NailType84", type=Uppaal_TransitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="Uppaal_TransitionType83", type=Uppaal_NailType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition70: BinaryAssociation = BinaryAssociation(
    name="transition70",
    ends={
        Property(name="Uppaal_TransitionType72", type=Uppaal_TemplateType, multiplicity=Multiplicity(1, 1)),
        Property(name="Uppaal_TemplateType71", type=Uppaal_TransitionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source73: BinaryAssociation = BinaryAssociation(
    name="source73",
    ends={
        Property(name="Uppaal_SourceType75", type=Uppaal_TransitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="Uppaal_TransitionType74", type=Uppaal_SourceType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target76: BinaryAssociation = BinaryAssociation(
    name="target76",
    ends={
        Property(name="Uppaal_TargetType78", type=Uppaal_TransitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="Uppaal_TransitionType77", type=Uppaal_TargetType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
label79: BinaryAssociation = BinaryAssociation(
    name="label79",
    ends={
        Property(name="Uppaal_LabelType81", type=Uppaal_TransitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="Uppaal_TransitionType80", type=Uppaal_LabelType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="Uppaal",
    types={Uppaal_ImportsType, Uppaal_DeclarationType, Uppaal_DocumentRoot, Uppaal_EStringToStringMapEntry, Uppaal_InstantiationType, Uppaal_InitType, Uppaal_ParameterType, Uppaal_LabelType, Uppaal_LocationType, Uppaal_NailType, Uppaal_NameType, Uppaal_NtaType, Uppaal_SourceType, Uppaal_SystemType, Uppaal_TargetType, Uppaal_TemplateType, Uppaal_TransitionType},
    associations={imports6, xMLNSPrefixMap0, xSISchemaLocation1, declaration4, instantiation10, init8, parameter22, label12, location14, nail16, name18, nta20, transition32, source24, system26, target28, template30, name34, label37, declaration43, imports40, system52, template46, instantiation49, location64, init67, name55, parameter58, declaration61, nail82, transition70, source73, target76, label79},
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