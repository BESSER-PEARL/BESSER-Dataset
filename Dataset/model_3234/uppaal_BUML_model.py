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
uppaal_CommittedType = Class(name="uppaal::CommittedType")
uppaal_DocumentRoot = Class(name="uppaal::DocumentRoot")
uppaal_EStringToStringMapEntry = Class(name="uppaal::EStringToStringMapEntry")
uppaal_LocationType = Class(name="uppaal::LocationType")
uppaal_NailType = Class(name="uppaal::NailType")
uppaal_NameType = Class(name="uppaal::NameType")
uppaal_InitType = Class(name="uppaal::InitType")
uppaal_LabelType = Class(name="uppaal::LabelType")
uppaal_TemplateType = Class(name="uppaal::TemplateType")
uppaal_TransitionType = Class(name="uppaal::TransitionType")
uppaal_UrgentType = Class(name="uppaal::UrgentType")
uppaal_NtaType = Class(name="uppaal::NtaType")
uppaal_ParameterType = Class(name="uppaal::ParameterType")
uppaal_SourceType = Class(name="uppaal::SourceType")
uppaal_TargetType = Class(name="uppaal::TargetType")

# uppaal_CommittedType class attributes and methods

# uppaal_DocumentRoot class attributes and methods
uppaal_DocumentRoot_mixed: Property = Property(name="mixed", type=StringType)
uppaal_DocumentRoot_declaration: Property = Property(name="declaration", type=StringType)
uppaal_DocumentRoot_imports: Property = Property(name="imports", type=StringType)
uppaal_DocumentRoot_instantiation: Property = Property(name="instantiation", type=StringType)
uppaal_DocumentRoot_system: Property = Property(name="system", type=StringType)
uppaal_DocumentRoot.attributes={uppaal_DocumentRoot_instantiation, uppaal_DocumentRoot_mixed, uppaal_DocumentRoot_imports, uppaal_DocumentRoot_declaration, uppaal_DocumentRoot_system}

# uppaal_EStringToStringMapEntry class attributes and methods

# uppaal_LocationType class attributes and methods
uppaal_LocationType_color: Property = Property(name="color", type=StringType)
uppaal_LocationType_id: Property = Property(name="id", type=StringType)
uppaal_LocationType_x: Property = Property(name="x", type=StringType)
uppaal_LocationType_y: Property = Property(name="y", type=StringType)
uppaal_LocationType.attributes={uppaal_LocationType_x, uppaal_LocationType_y, uppaal_LocationType_id, uppaal_LocationType_color}

# uppaal_NailType class attributes and methods
uppaal_NailType_x: Property = Property(name="x", type=StringType)
uppaal_NailType_y: Property = Property(name="y", type=StringType)
uppaal_NailType.attributes={uppaal_NailType_y, uppaal_NailType_x}

# uppaal_NameType class attributes and methods
uppaal_NameType_mixed: Property = Property(name="mixed", type=StringType)
uppaal_NameType_x: Property = Property(name="x", type=StringType)
uppaal_NameType_y: Property = Property(name="y", type=StringType)
uppaal_NameType.attributes={uppaal_NameType_y, uppaal_NameType_x, uppaal_NameType_mixed}

# uppaal_InitType class attributes and methods
uppaal_InitType_ref: Property = Property(name="ref", type=StringType)
uppaal_InitType.attributes={uppaal_InitType_ref}

# uppaal_LabelType class attributes and methods
uppaal_LabelType_mixed: Property = Property(name="mixed", type=StringType)
uppaal_LabelType_kind: Property = Property(name="kind", type=StringType)
uppaal_LabelType_x: Property = Property(name="x", type=StringType)
uppaal_LabelType_y: Property = Property(name="y", type=StringType)
uppaal_LabelType.attributes={uppaal_LabelType_x, uppaal_LabelType_kind, uppaal_LabelType_mixed, uppaal_LabelType_y}

# uppaal_TemplateType class attributes and methods
uppaal_TemplateType_declaration: Property = Property(name="declaration", type=StringType)
uppaal_TemplateType.attributes={uppaal_TemplateType_declaration}

# uppaal_TransitionType class attributes and methods
uppaal_TransitionType_x: Property = Property(name="x", type=StringType)
uppaal_TransitionType_y: Property = Property(name="y", type=StringType)
uppaal_TransitionType_color: Property = Property(name="color", type=StringType)
uppaal_TransitionType_id: Property = Property(name="id", type=StringType)
uppaal_TransitionType.attributes={uppaal_TransitionType_color, uppaal_TransitionType_id, uppaal_TransitionType_x, uppaal_TransitionType_y}

# uppaal_UrgentType class attributes and methods

# uppaal_NtaType class attributes and methods
uppaal_NtaType_declaration: Property = Property(name="declaration", type=StringType)
uppaal_NtaType_instantiation: Property = Property(name="instantiation", type=StringType)
uppaal_NtaType_system: Property = Property(name="system", type=StringType)
uppaal_NtaType_imports: Property = Property(name="imports", type=StringType)
uppaal_NtaType.attributes={uppaal_NtaType_system, uppaal_NtaType_instantiation, uppaal_NtaType_declaration, uppaal_NtaType_imports}

# uppaal_ParameterType class attributes and methods
uppaal_ParameterType_mixed: Property = Property(name="mixed", type=StringType)
uppaal_ParameterType_x: Property = Property(name="x", type=StringType)
uppaal_ParameterType_y: Property = Property(name="y", type=StringType)
uppaal_ParameterType.attributes={uppaal_ParameterType_x, uppaal_ParameterType_mixed, uppaal_ParameterType_y}

# uppaal_SourceType class attributes and methods
uppaal_SourceType_ref: Property = Property(name="ref", type=StringType)
uppaal_SourceType.attributes={uppaal_SourceType_ref}

# uppaal_TargetType class attributes and methods
uppaal_TargetType_ref: Property = Property(name="ref", type=StringType)
uppaal_TargetType.attributes={uppaal_TargetType_ref}

# Relationships
xMLNSPrefixMap0: BinaryAssociation = BinaryAssociation(
    name="xMLNSPrefixMap0",
    ends={
        Property(name="uppaal_EStringToStringMapEntry", type=uppaal_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_DocumentRoot", type=uppaal_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xSISchemaLocation1: BinaryAssociation = BinaryAssociation(
    name="xSISchemaLocation1",
    ends={
        Property(name="uppaal_EStringToStringMapEntry3", type=uppaal_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_DocumentRoot2", type=uppaal_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
location10: BinaryAssociation = BinaryAssociation(
    name="location10",
    ends={
        Property(name="uppaal_LocationType", type=uppaal_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_DocumentRoot11", type=uppaal_LocationType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nail12: BinaryAssociation = BinaryAssociation(
    name="nail12",
    ends={
        Property(name="uppaal_NailType", type=uppaal_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_DocumentRoot13", type=uppaal_NailType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name14: BinaryAssociation = BinaryAssociation(
    name="name14",
    ends={
        Property(name="uppaal_NameType", type=uppaal_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_DocumentRoot15", type=uppaal_NameType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
committed4: BinaryAssociation = BinaryAssociation(
    name="committed4",
    ends={
        Property(name="uppaal_CommittedType", type=uppaal_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_DocumentRoot5", type=uppaal_CommittedType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
init6: BinaryAssociation = BinaryAssociation(
    name="init6",
    ends={
        Property(name="uppaal_InitType", type=uppaal_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_DocumentRoot7", type=uppaal_InitType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
label8: BinaryAssociation = BinaryAssociation(
    name="label8",
    ends={
        Property(name="uppaal_LabelType", type=uppaal_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_DocumentRoot9", type=uppaal_LabelType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
template24: BinaryAssociation = BinaryAssociation(
    name="template24",
    ends={
        Property(name="uppaal_TemplateType", type=uppaal_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_DocumentRoot25", type=uppaal_TemplateType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition26: BinaryAssociation = BinaryAssociation(
    name="transition26",
    ends={
        Property(name="uppaal_TransitionType", type=uppaal_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_DocumentRoot27", type=uppaal_TransitionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
urgent28: BinaryAssociation = BinaryAssociation(
    name="urgent28",
    ends={
        Property(name="uppaal_UrgentType", type=uppaal_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_DocumentRoot29", type=uppaal_UrgentType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nta16: BinaryAssociation = BinaryAssociation(
    name="nta16",
    ends={
        Property(name="uppaal_NtaType", type=uppaal_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_DocumentRoot17", type=uppaal_NtaType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter18: BinaryAssociation = BinaryAssociation(
    name="parameter18",
    ends={
        Property(name="uppaal_ParameterType", type=uppaal_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_DocumentRoot19", type=uppaal_ParameterType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source20: BinaryAssociation = BinaryAssociation(
    name="source20",
    ends={
        Property(name="uppaal_SourceType", type=uppaal_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_DocumentRoot21", type=uppaal_SourceType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target22: BinaryAssociation = BinaryAssociation(
    name="target22",
    ends={
        Property(name="uppaal_TargetType", type=uppaal_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_DocumentRoot23", type=uppaal_TargetType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
urgent36: BinaryAssociation = BinaryAssociation(
    name="urgent36",
    ends={
        Property(name="uppaal_UrgentType38", type=uppaal_LocationType, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_LocationType37", type=uppaal_UrgentType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
committed39: BinaryAssociation = BinaryAssociation(
    name="committed39",
    ends={
        Property(name="uppaal_CommittedType41", type=uppaal_LocationType, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_LocationType40", type=uppaal_CommittedType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name30: BinaryAssociation = BinaryAssociation(
    name="name30",
    ends={
        Property(name="uppaal_NameType32", type=uppaal_LocationType, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_LocationType31", type=uppaal_NameType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
label33: BinaryAssociation = BinaryAssociation(
    name="label33",
    ends={
        Property(name="uppaal_LabelType35", type=uppaal_LocationType, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_LocationType34", type=uppaal_LabelType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
template42: BinaryAssociation = BinaryAssociation(
    name="template42",
    ends={
        Property(name="uppaal_TemplateType44", type=uppaal_NtaType, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_NtaType43", type=uppaal_TemplateType, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
parameter48: BinaryAssociation = BinaryAssociation(
    name="parameter48",
    ends={
        Property(name="uppaal_ParameterType50", type=uppaal_TemplateType, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_TemplateType49", type=uppaal_ParameterType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
location51: BinaryAssociation = BinaryAssociation(
    name="location51",
    ends={
        Property(name="uppaal_LocationType53", type=uppaal_TemplateType, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_TemplateType52", type=uppaal_LocationType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
init54: BinaryAssociation = BinaryAssociation(
    name="init54",
    ends={
        Property(name="uppaal_InitType56", type=uppaal_TemplateType, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_TemplateType55", type=uppaal_InitType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
transition57: BinaryAssociation = BinaryAssociation(
    name="transition57",
    ends={
        Property(name="uppaal_TransitionType59", type=uppaal_TemplateType, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_TemplateType58", type=uppaal_TransitionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name45: BinaryAssociation = BinaryAssociation(
    name="name45",
    ends={
        Property(name="uppaal_NameType47", type=uppaal_TemplateType, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_TemplateType46", type=uppaal_NameType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source60: BinaryAssociation = BinaryAssociation(
    name="source60",
    ends={
        Property(name="uppaal_SourceType62", type=uppaal_TransitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_TransitionType61", type=uppaal_SourceType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target63: BinaryAssociation = BinaryAssociation(
    name="target63",
    ends={
        Property(name="uppaal_TargetType65", type=uppaal_TransitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_TransitionType64", type=uppaal_TargetType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
label66: BinaryAssociation = BinaryAssociation(
    name="label66",
    ends={
        Property(name="uppaal_LabelType68", type=uppaal_TransitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_TransitionType67", type=uppaal_LabelType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nail69: BinaryAssociation = BinaryAssociation(
    name="nail69",
    ends={
        Property(name="uppaal_NailType71", type=uppaal_TransitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaal_TransitionType70", type=uppaal_NailType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="uppaal",
    types={uppaal_CommittedType, uppaal_DocumentRoot, uppaal_EStringToStringMapEntry, uppaal_LocationType, uppaal_NailType, uppaal_NameType, uppaal_InitType, uppaal_LabelType, uppaal_TemplateType, uppaal_TransitionType, uppaal_UrgentType, uppaal_NtaType, uppaal_ParameterType, uppaal_SourceType, uppaal_TargetType},
    associations={xMLNSPrefixMap0, xSISchemaLocation1, location10, nail12, name14, committed4, init6, label8, template24, transition26, urgent28, nta16, parameter18, source20, target22, urgent36, committed39, name30, label33, template42, parameter48, location51, init54, transition57, name45, source60, target63, label66, nail69},
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