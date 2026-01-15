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
KindType: Enumeration = Enumeration(
    name="KindType",
    literals={
            EnumerationLiteral(name="synchronisation"),
			EnumerationLiteral(name="invariant"),
			EnumerationLiteral(name="assignment"),
			EnumerationLiteral(name="guard"),
			EnumerationLiteral(name="select"),
			EnumerationLiteral(name="comments")
    }
)

# Classes
flat11_InitType = Class(name="flat11::InitType")
flat11_CommittedType = Class(name="flat11::CommittedType")
flat11_DocumentRoot = Class(name="flat11::DocumentRoot")
flat11_EStringToStringMapEntry = Class(name="flat11::EStringToStringMapEntry")
flat11_LocationType = Class(name="flat11::LocationType")
flat11_SourceType = Class(name="flat11::SourceType")
flat11_NailType = Class(name="flat11::NailType")
flat11_NameType = Class(name="flat11::NameType")
flat11_NtaType = Class(name="flat11::NtaType")
flat11_LabelType = Class(name="flat11::LabelType")
flat11_ParameterType = Class(name="flat11::ParameterType")
flat11_TargetType = Class(name="flat11::TargetType")
flat11_TemplateType = Class(name="flat11::TemplateType")
flat11_TransitionType = Class(name="flat11::TransitionType")
flat11_UrgentType = Class(name="flat11::UrgentType")

# flat11_InitType class attributes and methods
flat11_InitType_ref: Property = Property(name="ref", type=StringType)
flat11_InitType.attributes={flat11_InitType_ref}

# flat11_CommittedType class attributes and methods

# flat11_DocumentRoot class attributes and methods
flat11_DocumentRoot_declaration: Property = Property(name="declaration", type=StringType)
flat11_DocumentRoot_imports: Property = Property(name="imports", type=StringType)
flat11_DocumentRoot_instantiation: Property = Property(name="instantiation", type=StringType)
flat11_DocumentRoot_mixed: Property = Property(name="mixed", type=StringType)
flat11_DocumentRoot_system: Property = Property(name="system", type=StringType)
flat11_DocumentRoot.attributes={flat11_DocumentRoot_mixed, flat11_DocumentRoot_imports, flat11_DocumentRoot_system, flat11_DocumentRoot_declaration, flat11_DocumentRoot_instantiation}

# flat11_EStringToStringMapEntry class attributes and methods

# flat11_LocationType class attributes and methods
flat11_LocationType_color: Property = Property(name="color", type=StringType)
flat11_LocationType_id: Property = Property(name="id", type=StringType)
flat11_LocationType_x: Property = Property(name="x", type=StringType)
flat11_LocationType_y: Property = Property(name="y", type=StringType)
flat11_LocationType.attributes={flat11_LocationType_color, flat11_LocationType_id, flat11_LocationType_y, flat11_LocationType_x}

# flat11_SourceType class attributes and methods
flat11_SourceType_ref: Property = Property(name="ref", type=StringType)
flat11_SourceType.attributes={flat11_SourceType_ref}

# flat11_NailType class attributes and methods
flat11_NailType_x: Property = Property(name="x", type=StringType)
flat11_NailType_y: Property = Property(name="y", type=StringType)
flat11_NailType.attributes={flat11_NailType_y, flat11_NailType_x}

# flat11_NameType class attributes and methods
flat11_NameType_value: Property = Property(name="value", type=StringType)
flat11_NameType_x: Property = Property(name="x", type=StringType)
flat11_NameType_y: Property = Property(name="y", type=StringType)
flat11_NameType.attributes={flat11_NameType_value, flat11_NameType_x, flat11_NameType_y}

# flat11_NtaType class attributes and methods
flat11_NtaType_instantiation: Property = Property(name="instantiation", type=StringType)
flat11_NtaType_system: Property = Property(name="system", type=StringType)
flat11_NtaType_imports: Property = Property(name="imports", type=StringType)
flat11_NtaType_declaration: Property = Property(name="declaration", type=StringType)
flat11_NtaType.attributes={flat11_NtaType_system, flat11_NtaType_declaration, flat11_NtaType_instantiation, flat11_NtaType_imports}

# flat11_LabelType class attributes and methods
flat11_LabelType_value: Property = Property(name="value", type=StringType)
flat11_LabelType_kind: Property = Property(name="kind", type=StringType)
flat11_LabelType_x: Property = Property(name="x", type=StringType)
flat11_LabelType_y: Property = Property(name="y", type=StringType)
flat11_LabelType.attributes={flat11_LabelType_y, flat11_LabelType_value, flat11_LabelType_x, flat11_LabelType_kind}

# flat11_ParameterType class attributes and methods
flat11_ParameterType_value: Property = Property(name="value", type=StringType)
flat11_ParameterType_x: Property = Property(name="x", type=StringType)
flat11_ParameterType_y: Property = Property(name="y", type=StringType)
flat11_ParameterType.attributes={flat11_ParameterType_y, flat11_ParameterType_value, flat11_ParameterType_x}

# flat11_TargetType class attributes and methods
flat11_TargetType_ref: Property = Property(name="ref", type=StringType)
flat11_TargetType.attributes={flat11_TargetType_ref}

# flat11_TemplateType class attributes and methods
flat11_TemplateType_declaration: Property = Property(name="declaration", type=StringType)
flat11_TemplateType.attributes={flat11_TemplateType_declaration}

# flat11_TransitionType class attributes and methods
flat11_TransitionType_y: Property = Property(name="y", type=StringType)
flat11_TransitionType_action: Property = Property(name="action", type=StringType)
flat11_TransitionType_color: Property = Property(name="color", type=StringType)
flat11_TransitionType_controllable: Property = Property(name="controllable", type=StringType)
flat11_TransitionType_id: Property = Property(name="id", type=StringType)
flat11_TransitionType_x: Property = Property(name="x", type=StringType)
flat11_TransitionType.attributes={flat11_TransitionType_x, flat11_TransitionType_controllable, flat11_TransitionType_color, flat11_TransitionType_id, flat11_TransitionType_action, flat11_TransitionType_y}

# flat11_UrgentType class attributes and methods

# Relationships
xSISchemaLocation1: BinaryAssociation = BinaryAssociation(
    name="xSISchemaLocation1",
    ends={
        Property(name="flat11_EStringToStringMapEntry3", type=flat11_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="flat11_DocumentRoot2", type=flat11_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
committed4: BinaryAssociation = BinaryAssociation(
    name="committed4",
    ends={
        Property(name="flat11_CommittedType", type=flat11_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="flat11_DocumentRoot5", type=flat11_CommittedType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
init6: BinaryAssociation = BinaryAssociation(
    name="init6",
    ends={
        Property(name="flat11_InitType", type=flat11_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="flat11_DocumentRoot7", type=flat11_InitType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xMLNSPrefixMap0: BinaryAssociation = BinaryAssociation(
    name="xMLNSPrefixMap0",
    ends={
        Property(name="flat11_EStringToStringMapEntry", type=flat11_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="flat11_DocumentRoot", type=flat11_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
location10: BinaryAssociation = BinaryAssociation(
    name="location10",
    ends={
        Property(name="flat11_LocationType", type=flat11_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="flat11_DocumentRoot11", type=flat11_LocationType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source20: BinaryAssociation = BinaryAssociation(
    name="source20",
    ends={
        Property(name="flat11_SourceType", type=flat11_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="flat11_DocumentRoot21", type=flat11_SourceType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nail12: BinaryAssociation = BinaryAssociation(
    name="nail12",
    ends={
        Property(name="flat11_NailType", type=flat11_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="flat11_DocumentRoot13", type=flat11_NailType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name14: BinaryAssociation = BinaryAssociation(
    name="name14",
    ends={
        Property(name="flat11_NameType", type=flat11_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="flat11_DocumentRoot15", type=flat11_NameType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nta16: BinaryAssociation = BinaryAssociation(
    name="nta16",
    ends={
        Property(name="flat11_NtaType", type=flat11_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="flat11_DocumentRoot17", type=flat11_NtaType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
label8: BinaryAssociation = BinaryAssociation(
    name="label8",
    ends={
        Property(name="flat11_LabelType", type=flat11_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="flat11_DocumentRoot9", type=flat11_LabelType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter18: BinaryAssociation = BinaryAssociation(
    name="parameter18",
    ends={
        Property(name="flat11_ParameterType", type=flat11_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="flat11_DocumentRoot19", type=flat11_ParameterType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target22: BinaryAssociation = BinaryAssociation(
    name="target22",
    ends={
        Property(name="flat11_TargetType", type=flat11_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="flat11_DocumentRoot23", type=flat11_TargetType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
template24: BinaryAssociation = BinaryAssociation(
    name="template24",
    ends={
        Property(name="flat11_TemplateType", type=flat11_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="flat11_DocumentRoot25", type=flat11_TemplateType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition26: BinaryAssociation = BinaryAssociation(
    name="transition26",
    ends={
        Property(name="flat11_TransitionType", type=flat11_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="flat11_DocumentRoot27", type=flat11_TransitionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
urgent28: BinaryAssociation = BinaryAssociation(
    name="urgent28",
    ends={
        Property(name="flat11_UrgentType", type=flat11_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="flat11_DocumentRoot29", type=flat11_UrgentType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name30: BinaryAssociation = BinaryAssociation(
    name="name30",
    ends={
        Property(name="flat11_NameType32", type=flat11_LocationType, multiplicity=Multiplicity(1, 1)),
        Property(name="flat11_LocationType31", type=flat11_NameType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
label33: BinaryAssociation = BinaryAssociation(
    name="label33",
    ends={
        Property(name="flat11_LabelType35", type=flat11_LocationType, multiplicity=Multiplicity(1, 1)),
        Property(name="flat11_LocationType34", type=flat11_LabelType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
urgent36: BinaryAssociation = BinaryAssociation(
    name="urgent36",
    ends={
        Property(name="flat11_UrgentType38", type=flat11_LocationType, multiplicity=Multiplicity(1, 1)),
        Property(name="flat11_LocationType37", type=flat11_UrgentType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
committed39: BinaryAssociation = BinaryAssociation(
    name="committed39",
    ends={
        Property(name="flat11_CommittedType41", type=flat11_LocationType, multiplicity=Multiplicity(1, 1)),
        Property(name="flat11_LocationType40", type=flat11_CommittedType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
template42: BinaryAssociation = BinaryAssociation(
    name="template42",
    ends={
        Property(name="flat11_TemplateType44", type=flat11_NtaType, multiplicity=Multiplicity(1, 1)),
        Property(name="flat11_NtaType43", type=flat11_TemplateType, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
name45: BinaryAssociation = BinaryAssociation(
    name="name45",
    ends={
        Property(name="flat11_NameType47", type=flat11_TemplateType, multiplicity=Multiplicity(1, 1)),
        Property(name="flat11_TemplateType46", type=flat11_NameType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameter48: BinaryAssociation = BinaryAssociation(
    name="parameter48",
    ends={
        Property(name="flat11_ParameterType50", type=flat11_TemplateType, multiplicity=Multiplicity(1, 1)),
        Property(name="flat11_TemplateType49", type=flat11_ParameterType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target63: BinaryAssociation = BinaryAssociation(
    name="target63",
    ends={
        Property(name="flat11_TargetType65", type=flat11_TransitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="flat11_TransitionType64", type=flat11_TargetType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
label66: BinaryAssociation = BinaryAssociation(
    name="label66",
    ends={
        Property(name="flat11_LabelType68", type=flat11_TransitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="flat11_TransitionType67", type=flat11_LabelType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
location51: BinaryAssociation = BinaryAssociation(
    name="location51",
    ends={
        Property(name="flat11_LocationType53", type=flat11_TemplateType, multiplicity=Multiplicity(1, 1)),
        Property(name="flat11_TemplateType52", type=flat11_LocationType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
init54: BinaryAssociation = BinaryAssociation(
    name="init54",
    ends={
        Property(name="flat11_InitType56", type=flat11_TemplateType, multiplicity=Multiplicity(1, 1)),
        Property(name="flat11_TemplateType55", type=flat11_InitType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
transition57: BinaryAssociation = BinaryAssociation(
    name="transition57",
    ends={
        Property(name="flat11_TransitionType59", type=flat11_TemplateType, multiplicity=Multiplicity(1, 1)),
        Property(name="flat11_TemplateType58", type=flat11_TransitionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source60: BinaryAssociation = BinaryAssociation(
    name="source60",
    ends={
        Property(name="flat11_SourceType62", type=flat11_TransitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="flat11_TransitionType61", type=flat11_SourceType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
nail69: BinaryAssociation = BinaryAssociation(
    name="nail69",
    ends={
        Property(name="flat11_NailType71", type=flat11_TransitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="flat11_TransitionType70", type=flat11_NailType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="flat11",
    types={flat11_InitType, flat11_CommittedType, flat11_DocumentRoot, flat11_EStringToStringMapEntry, flat11_LocationType, flat11_SourceType, flat11_NailType, flat11_NameType, flat11_NtaType, flat11_LabelType, flat11_ParameterType, flat11_TargetType, flat11_TemplateType, flat11_TransitionType, flat11_UrgentType, KindType},
    associations={xSISchemaLocation1, committed4, init6, xMLNSPrefixMap0, location10, source20, nail12, name14, nta16, label8, parameter18, target22, template24, transition26, urgent28, name30, label33, urgent36, committed39, template42, name45, parameter48, target63, label66, location51, init54, transition57, source60, nail69},
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