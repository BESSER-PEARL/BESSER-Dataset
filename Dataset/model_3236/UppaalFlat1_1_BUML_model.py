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
UppaalFlat11_EStringToStringMapEntry = Class(name="UppaalFlat11::EStringToStringMapEntry")
UppaalFlat11_CommittedType = Class(name="UppaalFlat11::CommittedType")
UppaalFlat11_DocumentRoot = Class(name="UppaalFlat11::DocumentRoot")
UppaalFlat11_InitType = Class(name="UppaalFlat11::InitType")
UppaalFlat11_LabelType = Class(name="UppaalFlat11::LabelType")
UppaalFlat11_LocationType = Class(name="UppaalFlat11::LocationType")
UppaalFlat11_NailType = Class(name="UppaalFlat11::NailType")
UppaalFlat11_NtaType = Class(name="UppaalFlat11::NtaType")
UppaalFlat11_ParameterType = Class(name="UppaalFlat11::ParameterType")
UppaalFlat11_SourceType = Class(name="UppaalFlat11::SourceType")
UppaalFlat11_NameType = Class(name="UppaalFlat11::NameType")
UppaalFlat11_TemplateType = Class(name="UppaalFlat11::TemplateType")
UppaalFlat11_TransitionType = Class(name="UppaalFlat11::TransitionType")
UppaalFlat11_UrgentType = Class(name="UppaalFlat11::UrgentType")
UppaalFlat11_TargetType = Class(name="UppaalFlat11::TargetType")

# UppaalFlat11_EStringToStringMapEntry class attributes and methods

# UppaalFlat11_CommittedType class attributes and methods

# UppaalFlat11_DocumentRoot class attributes and methods
UppaalFlat11_DocumentRoot_mixed: Property = Property(name="mixed", type=StringType)
UppaalFlat11_DocumentRoot_declaration: Property = Property(name="declaration", type=StringType)
UppaalFlat11_DocumentRoot_instantiation: Property = Property(name="instantiation", type=StringType)
UppaalFlat11_DocumentRoot_imports: Property = Property(name="imports", type=StringType)
UppaalFlat11_DocumentRoot_system: Property = Property(name="system", type=StringType)
UppaalFlat11_DocumentRoot.attributes={UppaalFlat11_DocumentRoot_declaration, UppaalFlat11_DocumentRoot_mixed, UppaalFlat11_DocumentRoot_imports, UppaalFlat11_DocumentRoot_system, UppaalFlat11_DocumentRoot_instantiation}

# UppaalFlat11_InitType class attributes and methods
UppaalFlat11_InitType_ref: Property = Property(name="ref", type=StringType)
UppaalFlat11_InitType.attributes={UppaalFlat11_InitType_ref}

# UppaalFlat11_LabelType class attributes and methods
UppaalFlat11_LabelType_x: Property = Property(name="x", type=StringType)
UppaalFlat11_LabelType_y: Property = Property(name="y", type=StringType)
UppaalFlat11_LabelType_mixed: Property = Property(name="mixed", type=StringType)
UppaalFlat11_LabelType_kind: Property = Property(name="kind", type=StringType)
UppaalFlat11_LabelType.attributes={UppaalFlat11_LabelType_mixed, UppaalFlat11_LabelType_y, UppaalFlat11_LabelType_kind, UppaalFlat11_LabelType_x}

# UppaalFlat11_LocationType class attributes and methods
UppaalFlat11_LocationType_color: Property = Property(name="color", type=StringType)
UppaalFlat11_LocationType_id: Property = Property(name="id", type=StringType)
UppaalFlat11_LocationType_x: Property = Property(name="x", type=StringType)
UppaalFlat11_LocationType_y: Property = Property(name="y", type=StringType)
UppaalFlat11_LocationType.attributes={UppaalFlat11_LocationType_color, UppaalFlat11_LocationType_y, UppaalFlat11_LocationType_x, UppaalFlat11_LocationType_id}

# UppaalFlat11_NailType class attributes and methods
UppaalFlat11_NailType_x: Property = Property(name="x", type=StringType)
UppaalFlat11_NailType_y: Property = Property(name="y", type=StringType)
UppaalFlat11_NailType.attributes={UppaalFlat11_NailType_y, UppaalFlat11_NailType_x}

# UppaalFlat11_NtaType class attributes and methods
UppaalFlat11_NtaType_declaration: Property = Property(name="declaration", type=StringType)
UppaalFlat11_NtaType_imports: Property = Property(name="imports", type=StringType)
UppaalFlat11_NtaType_instantiation: Property = Property(name="instantiation", type=StringType)
UppaalFlat11_NtaType_system: Property = Property(name="system", type=StringType)
UppaalFlat11_NtaType.attributes={UppaalFlat11_NtaType_system, UppaalFlat11_NtaType_instantiation, UppaalFlat11_NtaType_imports, UppaalFlat11_NtaType_declaration}

# UppaalFlat11_ParameterType class attributes and methods
UppaalFlat11_ParameterType_mixed: Property = Property(name="mixed", type=StringType)
UppaalFlat11_ParameterType_x: Property = Property(name="x", type=StringType)
UppaalFlat11_ParameterType_y: Property = Property(name="y", type=StringType)
UppaalFlat11_ParameterType.attributes={UppaalFlat11_ParameterType_mixed, UppaalFlat11_ParameterType_x, UppaalFlat11_ParameterType_y}

# UppaalFlat11_SourceType class attributes and methods
UppaalFlat11_SourceType_ref: Property = Property(name="ref", type=StringType)
UppaalFlat11_SourceType.attributes={UppaalFlat11_SourceType_ref}

# UppaalFlat11_NameType class attributes and methods
UppaalFlat11_NameType_mixed: Property = Property(name="mixed", type=StringType)
UppaalFlat11_NameType_x: Property = Property(name="x", type=StringType)
UppaalFlat11_NameType_y: Property = Property(name="y", type=StringType)
UppaalFlat11_NameType.attributes={UppaalFlat11_NameType_mixed, UppaalFlat11_NameType_y, UppaalFlat11_NameType_x}

# UppaalFlat11_TemplateType class attributes and methods
UppaalFlat11_TemplateType_declaration: Property = Property(name="declaration", type=StringType)
UppaalFlat11_TemplateType.attributes={UppaalFlat11_TemplateType_declaration}

# UppaalFlat11_TransitionType class attributes and methods
UppaalFlat11_TransitionType_x: Property = Property(name="x", type=StringType)
UppaalFlat11_TransitionType_y: Property = Property(name="y", type=StringType)
UppaalFlat11_TransitionType_color: Property = Property(name="color", type=StringType)
UppaalFlat11_TransitionType_id: Property = Property(name="id", type=StringType)
UppaalFlat11_TransitionType.attributes={UppaalFlat11_TransitionType_x, UppaalFlat11_TransitionType_y, UppaalFlat11_TransitionType_id, UppaalFlat11_TransitionType_color}

# UppaalFlat11_UrgentType class attributes and methods

# UppaalFlat11_TargetType class attributes and methods
UppaalFlat11_TargetType_ref: Property = Property(name="ref", type=StringType)
UppaalFlat11_TargetType.attributes={UppaalFlat11_TargetType_ref}

# Relationships
xMLNSPrefixMap0: BinaryAssociation = BinaryAssociation(
    name="xMLNSPrefixMap0",
    ends={
        Property(name="UppaalFlat11_EStringToStringMapEntry", type=UppaalFlat11_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="UppaalFlat11_DocumentRoot", type=UppaalFlat11_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xSISchemaLocation1: BinaryAssociation = BinaryAssociation(
    name="xSISchemaLocation1",
    ends={
        Property(name="UppaalFlat11_EStringToStringMapEntry3", type=UppaalFlat11_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="UppaalFlat11_DocumentRoot2", type=UppaalFlat11_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
committed4: BinaryAssociation = BinaryAssociation(
    name="committed4",
    ends={
        Property(name="UppaalFlat11_CommittedType", type=UppaalFlat11_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="UppaalFlat11_DocumentRoot5", type=UppaalFlat11_CommittedType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
init6: BinaryAssociation = BinaryAssociation(
    name="init6",
    ends={
        Property(name="UppaalFlat11_InitType", type=UppaalFlat11_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="UppaalFlat11_DocumentRoot7", type=UppaalFlat11_InitType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
label8: BinaryAssociation = BinaryAssociation(
    name="label8",
    ends={
        Property(name="UppaalFlat11_LabelType", type=UppaalFlat11_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="UppaalFlat11_DocumentRoot9", type=UppaalFlat11_LabelType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
location10: BinaryAssociation = BinaryAssociation(
    name="location10",
    ends={
        Property(name="UppaalFlat11_LocationType", type=UppaalFlat11_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="UppaalFlat11_DocumentRoot11", type=UppaalFlat11_LocationType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nta16: BinaryAssociation = BinaryAssociation(
    name="nta16",
    ends={
        Property(name="UppaalFlat11_NtaType", type=UppaalFlat11_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="UppaalFlat11_DocumentRoot17", type=UppaalFlat11_NtaType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter18: BinaryAssociation = BinaryAssociation(
    name="parameter18",
    ends={
        Property(name="UppaalFlat11_ParameterType", type=UppaalFlat11_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="UppaalFlat11_DocumentRoot19", type=UppaalFlat11_ParameterType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source20: BinaryAssociation = BinaryAssociation(
    name="source20",
    ends={
        Property(name="UppaalFlat11_SourceType", type=UppaalFlat11_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="UppaalFlat11_DocumentRoot21", type=UppaalFlat11_SourceType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nail12: BinaryAssociation = BinaryAssociation(
    name="nail12",
    ends={
        Property(name="UppaalFlat11_NailType", type=UppaalFlat11_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="UppaalFlat11_DocumentRoot13", type=UppaalFlat11_NailType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name14: BinaryAssociation = BinaryAssociation(
    name="name14",
    ends={
        Property(name="UppaalFlat11_NameType", type=UppaalFlat11_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="UppaalFlat11_DocumentRoot15", type=UppaalFlat11_NameType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
template24: BinaryAssociation = BinaryAssociation(
    name="template24",
    ends={
        Property(name="UppaalFlat11_TemplateType", type=UppaalFlat11_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="UppaalFlat11_DocumentRoot25", type=UppaalFlat11_TemplateType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition26: BinaryAssociation = BinaryAssociation(
    name="transition26",
    ends={
        Property(name="UppaalFlat11_TransitionType", type=UppaalFlat11_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="UppaalFlat11_DocumentRoot27", type=UppaalFlat11_TransitionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
urgent28: BinaryAssociation = BinaryAssociation(
    name="urgent28",
    ends={
        Property(name="UppaalFlat11_UrgentType", type=UppaalFlat11_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="UppaalFlat11_DocumentRoot29", type=UppaalFlat11_UrgentType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target22: BinaryAssociation = BinaryAssociation(
    name="target22",
    ends={
        Property(name="UppaalFlat11_TargetType", type=UppaalFlat11_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="UppaalFlat11_DocumentRoot23", type=UppaalFlat11_TargetType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
urgent36: BinaryAssociation = BinaryAssociation(
    name="urgent36",
    ends={
        Property(name="UppaalFlat11_LocationType37", type=UppaalFlat11_UrgentType, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="UppaalFlat11_UrgentType38", type=UppaalFlat11_LocationType, multiplicity=Multiplicity(1, 1))
    }
)
committed39: BinaryAssociation = BinaryAssociation(
    name="committed39",
    ends={
        Property(name="UppaalFlat11_CommittedType41", type=UppaalFlat11_LocationType, multiplicity=Multiplicity(1, 1)),
        Property(name="UppaalFlat11_LocationType40", type=UppaalFlat11_CommittedType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name30: BinaryAssociation = BinaryAssociation(
    name="name30",
    ends={
        Property(name="UppaalFlat11_NameType32", type=UppaalFlat11_LocationType, multiplicity=Multiplicity(1, 1)),
        Property(name="UppaalFlat11_LocationType31", type=UppaalFlat11_NameType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
label33: BinaryAssociation = BinaryAssociation(
    name="label33",
    ends={
        Property(name="UppaalFlat11_LabelType35", type=UppaalFlat11_LocationType, multiplicity=Multiplicity(1, 1)),
        Property(name="UppaalFlat11_LocationType34", type=UppaalFlat11_LabelType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
template42: BinaryAssociation = BinaryAssociation(
    name="template42",
    ends={
        Property(name="UppaalFlat11_TemplateType44", type=UppaalFlat11_NtaType, multiplicity=Multiplicity(1, 1)),
        Property(name="UppaalFlat11_NtaType43", type=UppaalFlat11_TemplateType, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
location51: BinaryAssociation = BinaryAssociation(
    name="location51",
    ends={
        Property(name="UppaalFlat11_LocationType53", type=UppaalFlat11_TemplateType, multiplicity=Multiplicity(1, 1)),
        Property(name="UppaalFlat11_TemplateType52", type=UppaalFlat11_LocationType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name45: BinaryAssociation = BinaryAssociation(
    name="name45",
    ends={
        Property(name="UppaalFlat11_NameType47", type=UppaalFlat11_TemplateType, multiplicity=Multiplicity(1, 1)),
        Property(name="UppaalFlat11_TemplateType46", type=UppaalFlat11_NameType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameter48: BinaryAssociation = BinaryAssociation(
    name="parameter48",
    ends={
        Property(name="UppaalFlat11_ParameterType50", type=UppaalFlat11_TemplateType, multiplicity=Multiplicity(1, 1)),
        Property(name="UppaalFlat11_TemplateType49", type=UppaalFlat11_ParameterType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
init54: BinaryAssociation = BinaryAssociation(
    name="init54",
    ends={
        Property(name="UppaalFlat11_InitType56", type=UppaalFlat11_TemplateType, multiplicity=Multiplicity(1, 1)),
        Property(name="UppaalFlat11_TemplateType55", type=UppaalFlat11_InitType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
transition57: BinaryAssociation = BinaryAssociation(
    name="transition57",
    ends={
        Property(name="UppaalFlat11_TransitionType59", type=UppaalFlat11_TemplateType, multiplicity=Multiplicity(1, 1)),
        Property(name="UppaalFlat11_TemplateType58", type=UppaalFlat11_TransitionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source60: BinaryAssociation = BinaryAssociation(
    name="source60",
    ends={
        Property(name="UppaalFlat11_SourceType62", type=UppaalFlat11_TransitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="UppaalFlat11_TransitionType61", type=UppaalFlat11_SourceType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target63: BinaryAssociation = BinaryAssociation(
    name="target63",
    ends={
        Property(name="UppaalFlat11_TargetType65", type=UppaalFlat11_TransitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="UppaalFlat11_TransitionType64", type=UppaalFlat11_TargetType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
label66: BinaryAssociation = BinaryAssociation(
    name="label66",
    ends={
        Property(name="UppaalFlat11_LabelType68", type=UppaalFlat11_TransitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="UppaalFlat11_TransitionType67", type=UppaalFlat11_LabelType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nail69: BinaryAssociation = BinaryAssociation(
    name="nail69",
    ends={
        Property(name="UppaalFlat11_NailType71", type=UppaalFlat11_TransitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="UppaalFlat11_TransitionType70", type=UppaalFlat11_NailType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="UppaalFlat11",
    types={UppaalFlat11_EStringToStringMapEntry, UppaalFlat11_CommittedType, UppaalFlat11_DocumentRoot, UppaalFlat11_InitType, UppaalFlat11_LabelType, UppaalFlat11_LocationType, UppaalFlat11_NailType, UppaalFlat11_NtaType, UppaalFlat11_ParameterType, UppaalFlat11_SourceType, UppaalFlat11_NameType, UppaalFlat11_TemplateType, UppaalFlat11_TransitionType, UppaalFlat11_UrgentType, UppaalFlat11_TargetType},
    associations={xMLNSPrefixMap0, xSISchemaLocation1, committed4, init6, label8, location10, nta16, parameter18, source20, nail12, name14, template24, transition26, urgent28, target22, urgent36, committed39, name30, label33, template42, location51, name45, parameter48, init54, transition57, source60, target63, label66, nail69},
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