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
scxml_ScxmlSendType = Class(name="scxml::ScxmlSendType")
scxml_ScxmlOnexecuteType = Class(name="scxml::ScxmlOnexecuteType")
scxml_ScxmlScriptType = Class(name="scxml::ScxmlScriptType")
scxml_ScxmlParamType = Class(name="scxml::ScxmlParamType")
scxml_ScxmlScxmlType = Class(name="scxml::ScxmlScxmlType")
scxml_ScxmlStateType = Class(name="scxml::ScxmlStateType")
scxml_ScxmlTransitionType = Class(name="scxml::ScxmlTransitionType")
scxml_DocumentRoot = Class(name="scxml::DocumentRoot")
scxml_EStringToStringMapEntry = Class(name="scxml::EStringToStringMapEntry")

# scxml_ScxmlSendType class attributes and methods
scxml_ScxmlSendType_event: Property = Property(name="event", type=StringType)
scxml_ScxmlSendType.attributes={scxml_ScxmlSendType_event}

# scxml_ScxmlOnexecuteType class attributes and methods
scxml_ScxmlOnexecuteType_any: Property = Property(name="any", type=StringType)
scxml_ScxmlOnexecuteType_scxmlExecutablecontent: Property = Property(name="scxmlExecutablecontent", type=StringType)
scxml_ScxmlOnexecuteType_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
scxml_ScxmlOnexecuteType.attributes={scxml_ScxmlOnexecuteType_anyAttribute, scxml_ScxmlOnexecuteType_scxmlExecutablecontent, scxml_ScxmlOnexecuteType_any}

# scxml_ScxmlScriptType class attributes and methods
scxml_ScxmlScriptType_mixed: Property = Property(name="mixed", type=StringType)
scxml_ScxmlScriptType_scxmlExtraContent: Property = Property(name="scxmlExtraContent", type=StringType)
scxml_ScxmlScriptType_any: Property = Property(name="any", type=StringType)
scxml_ScxmlScriptType_src: Property = Property(name="src", type=StringType)
scxml_ScxmlScriptType_content: Property = Property(name="content", type=StringType)
scxml_ScxmlScriptType.attributes={scxml_ScxmlScriptType_mixed, scxml_ScxmlScriptType_content, scxml_ScxmlScriptType_scxmlExtraContent, scxml_ScxmlScriptType_src, scxml_ScxmlScriptType_any}

# scxml_ScxmlParamType class attributes and methods
scxml_ScxmlParamType_anyAttribute: Property = Property(name="anyAttribute", type=StringType)
scxml_ScxmlParamType_scxmlExtraContent: Property = Property(name="scxmlExtraContent", type=StringType)
scxml_ScxmlParamType_any: Property = Property(name="any", type=StringType)
scxml_ScxmlParamType_expr: Property = Property(name="expr", type=StringType)
scxml_ScxmlParamType_name: Property = Property(name="name", type=StringType)
scxml_ScxmlParamType.attributes={scxml_ScxmlParamType_expr, scxml_ScxmlParamType_scxmlExtraContent, scxml_ScxmlParamType_any, scxml_ScxmlParamType_anyAttribute, scxml_ScxmlParamType_name}

# scxml_ScxmlScxmlType class attributes and methods
scxml_ScxmlScxmlType_id: Property = Property(name="id", type=StringType)
scxml_ScxmlScxmlType_initial: Property = Property(name="initial", type=StringType)
scxml_ScxmlScxmlType_version: Property = Property(name="version", type=StringType)
scxml_ScxmlScxmlType.attributes={scxml_ScxmlScxmlType_version, scxml_ScxmlScxmlType_id, scxml_ScxmlScxmlType_initial}

# scxml_ScxmlStateType class attributes and methods
scxml_ScxmlStateType_id: Property = Property(name="id", type=StringType)
scxml_ScxmlStateType_initial: Property = Property(name="initial", type=StringType)
scxml_ScxmlStateType.attributes={scxml_ScxmlStateType_id, scxml_ScxmlStateType_initial}

# scxml_ScxmlTransitionType class attributes and methods
scxml_ScxmlTransitionType_target: Property = Property(name="target", type=StringType)
scxml_ScxmlTransitionType_scxmlExecutablecontent: Property = Property(name="scxmlExecutablecontent", type=StringType)
scxml_ScxmlTransitionType_any: Property = Property(name="any", type=StringType)
scxml_ScxmlTransitionType_cond: Property = Property(name="cond", type=StringType)
scxml_ScxmlTransitionType_event: Property = Property(name="event", type=StringType)
scxml_ScxmlTransitionType.attributes={scxml_ScxmlTransitionType_cond, scxml_ScxmlTransitionType_scxmlExecutablecontent, scxml_ScxmlTransitionType_target, scxml_ScxmlTransitionType_event, scxml_ScxmlTransitionType_any}

# scxml_DocumentRoot class attributes and methods
scxml_DocumentRoot_mixed: Property = Property(name="mixed", type=StringType)
scxml_DocumentRoot.attributes={scxml_DocumentRoot_mixed}

# scxml_EStringToStringMapEntry class attributes and methods

# Relationships
send0: BinaryAssociation = BinaryAssociation(
    name="send0",
    ends={
        Property(name="scxml_ScxmlSendType", type=scxml_ScxmlOnexecuteType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlOnexecuteType", type=scxml_ScxmlSendType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
script1: BinaryAssociation = BinaryAssociation(
    name="script1",
    ends={
        Property(name="scxml_ScxmlScriptType", type=scxml_ScxmlOnexecuteType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlOnexecuteType2", type=scxml_ScxmlScriptType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
script4: BinaryAssociation = BinaryAssociation(
    name="script4",
    ends={
        Property(name="scxml_ScxmlScxmlType5", type=scxml_ScxmlScriptType, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="scxml_ScxmlScriptType6", type=scxml_ScxmlScxmlType, multiplicity=Multiplicity(1, 1))
    }
)
state3: BinaryAssociation = BinaryAssociation(
    name="state3",
    ends={
        Property(name="scxml_ScxmlStateType", type=scxml_ScxmlScxmlType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlScxmlType", type=scxml_ScxmlStateType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
state18: BinaryAssociation = BinaryAssociation(
    name="state18",
    ends={
        Property(name="scxml_ScxmlStateType19", type=scxml_ScxmlStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlStateType17", type=scxml_ScxmlStateType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
param7: BinaryAssociation = BinaryAssociation(
    name="param7",
    ends={
        Property(name="scxml_ScxmlParamType", type=scxml_ScxmlSendType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlSendType8", type=scxml_ScxmlParamType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
onentry9: BinaryAssociation = BinaryAssociation(
    name="onentry9",
    ends={
        Property(name="scxml_ScxmlOnexecuteType11", type=scxml_ScxmlStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlStateType10", type=scxml_ScxmlOnexecuteType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
onexit12: BinaryAssociation = BinaryAssociation(
    name="onexit12",
    ends={
        Property(name="scxml_ScxmlOnexecuteType14", type=scxml_ScxmlStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlStateType13", type=scxml_ScxmlOnexecuteType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition15: BinaryAssociation = BinaryAssociation(
    name="transition15",
    ends={
        Property(name="scxml_ScxmlTransitionType", type=scxml_ScxmlStateType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlStateType16", type=scxml_ScxmlTransitionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xMLNSPrefixMap26: BinaryAssociation = BinaryAssociation(
    name="xMLNSPrefixMap26",
    ends={
        Property(name="scxml_EStringToStringMapEntry", type=scxml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_DocumentRoot", type=scxml_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
send20: BinaryAssociation = BinaryAssociation(
    name="send20",
    ends={
        Property(name="scxml_ScxmlSendType22", type=scxml_ScxmlTransitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlTransitionType21", type=scxml_ScxmlSendType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
script23: BinaryAssociation = BinaryAssociation(
    name="script23",
    ends={
        Property(name="scxml_ScxmlScriptType25", type=scxml_ScxmlTransitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_ScxmlTransitionType24", type=scxml_ScxmlScriptType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xSISchemaLocation27: BinaryAssociation = BinaryAssociation(
    name="xSISchemaLocation27",
    ends={
        Property(name="scxml_EStringToStringMapEntry29", type=scxml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_DocumentRoot28", type=scxml_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
scxml30: BinaryAssociation = BinaryAssociation(
    name="scxml30",
    ends={
        Property(name="scxml_ScxmlScxmlType32", type=scxml_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="scxml_DocumentRoot31", type=scxml_ScxmlScxmlType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="scxml",
    types={scxml_ScxmlSendType, scxml_ScxmlOnexecuteType, scxml_ScxmlScriptType, scxml_ScxmlParamType, scxml_ScxmlScxmlType, scxml_ScxmlStateType, scxml_ScxmlTransitionType, scxml_DocumentRoot, scxml_EStringToStringMapEntry},
    associations={send0, script1, script4, state3, state18, param7, onentry9, onexit12, transition15, xMLNSPrefixMap26, send20, script23, xSISchemaLocation27, scxml30},
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