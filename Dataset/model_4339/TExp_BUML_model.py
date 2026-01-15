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
tExp_Term = Class(name="tExp::Term")
tExp_Role = Class(name="tExp::Role")
tExp_Domainmodel = Class(name="tExp::Domainmodel")
tExp_TraceExpression = Class(name="tExp::TraceExpression")
tExp_PrologExpression = Class(name="tExp::PrologExpression")
tExp_EventType = Class(name="tExp::EventType")
tExp_Partition = Class(name="tExp::Partition")
tExp_Constraint = Class(name="tExp::Constraint")
tExp_Channel = Class(name="tExp::Channel")
tExp_Expression = Class(name="tExp::Expression")
tExp_Together = Class(name="tExp::Together")
tExp_Msg = Class(name="tExp::Msg")
tExp_UnionExpr = Class(name="tExp::UnionExpr")
tExp_AndExpr = Class(name="tExp::AndExpr")
tExp_AtomExpression = Class(name="tExp::AtomExpression")
PrologExpression = Class(name="PrologExpression")
tExp_VariableExpression = Class(name="tExp::VariableExpression")
tExp_StringExpression = Class(name="tExp::StringExpression")
tExp_NumberExpression = Class(name="tExp::NumberExpression")
tExp_ListExpression = Class(name="tExp::ListExpression")
tExp_ShuffleExpr = Class(name="tExp::ShuffleExpr")
Expression = Class(name="Expression")
tExp_Cardinality = Class(name="tExp::Cardinality")
tExp_CatExpr = Class(name="tExp::CatExpr")
tExp_SeqExpr = Class(name="tExp::SeqExpr")
tExp_FilterExpr = Class(name="tExp::FilterExpr")
tExp_VarExpr = Class(name="tExp::VarExpr")
tExp_TerminalExpr = Class(name="tExp::TerminalExpr")
tExp_Singletons = Class(name="tExp::Singletons")
Constraint = Class(name="Constraint")
tExp_Size = Class(name="tExp::Size")

# tExp_Term class attributes and methods
tExp_Term_name: Property = Property(name="name", type=StringType)
tExp_Term.attributes={tExp_Term_name}

# tExp_Role class attributes and methods
tExp_Role_name: Property = Property(name="name", type=StringType)
tExp_Role_class: Property = Property(name="class", type=StringType)
tExp_Role_args: Property = Property(name="args", type=StringType)
tExp_Role.attributes={tExp_Role_name, tExp_Role_args, tExp_Role_class}

# tExp_Domainmodel class attributes and methods

# tExp_TraceExpression class attributes and methods
tExp_TraceExpression_name: Property = Property(name="name", type=StringType)
tExp_TraceExpression_bodyL: Property = Property(name="bodyL", type=StringType)
tExp_TraceExpression_rolesL: Property = Property(name="rolesL", type=StringType)
tExp_TraceExpression_typesL: Property = Property(name="typesL", type=StringType)
tExp_TraceExpression_modulesL: Property = Property(name="modulesL", type=StringType)
tExp_TraceExpression_modules: Property = Property(name="modules", type=StringType)
tExp_TraceExpression_decentralizedL: Property = Property(name="decentralizedL", type=StringType)
tExp_TraceExpression_decentralized: Property = Property(name="decentralized", type=StringType)
tExp_TraceExpression_partitionL: Property = Property(name="partitionL", type=StringType)
tExp_TraceExpression_constraintsL: Property = Property(name="constraintsL", type=StringType)
tExp_TraceExpression_guiL: Property = Property(name="guiL", type=StringType)
tExp_TraceExpression_gui: Property = Property(name="gui", type=StringType)
tExp_TraceExpression_minimalL: Property = Property(name="minimalL", type=StringType)
tExp_TraceExpression_minimal: Property = Property(name="minimal", type=StringType)
tExp_TraceExpression_thresholdL: Property = Property(name="thresholdL", type=StringType)
tExp_TraceExpression_threshold: Property = Property(name="threshold", type=StringType)
tExp_TraceExpression_channelsL: Property = Property(name="channelsL", type=StringType)
tExp_TraceExpression.attributes={tExp_TraceExpression_modules, tExp_TraceExpression_rolesL, tExp_TraceExpression_constraintsL, tExp_TraceExpression_decentralized, tExp_TraceExpression_name, tExp_TraceExpression_gui, tExp_TraceExpression_thresholdL, tExp_TraceExpression_modulesL, tExp_TraceExpression_channelsL, tExp_TraceExpression_threshold, tExp_TraceExpression_decentralizedL, tExp_TraceExpression_partitionL, tExp_TraceExpression_bodyL, tExp_TraceExpression_minimal, tExp_TraceExpression_guiL, tExp_TraceExpression_minimalL, tExp_TraceExpression_typesL}

# tExp_PrologExpression class attributes and methods
tExp_PrologExpression_op: Property = Property(name="op", type=StringType)
tExp_PrologExpression.attributes={tExp_PrologExpression_op}

# tExp_EventType class attributes and methods
tExp_EventType_name: Property = Property(name="name", type=StringType)
tExp_EventType.attributes={tExp_EventType_name}

# tExp_Partition class attributes and methods

# tExp_Constraint class attributes and methods
tExp_Constraint_together: Property = Property(name="together", type=StringType)
tExp_Constraint_split: Property = Property(name="split", type=StringType)
tExp_Constraint_parMin: Property = Property(name="parMin", type=StringType)
tExp_Constraint_parMax: Property = Property(name="parMax", type=StringType)
tExp_Constraint.attributes={tExp_Constraint_split, tExp_Constraint_parMin, tExp_Constraint_together, tExp_Constraint_parMax}

# tExp_Channel class attributes and methods
tExp_Channel_name: Property = Property(name="name", type=StringType)
tExp_Channel_reliability: Property = Property(name="reliability", type=StringType)
tExp_Channel.attributes={tExp_Channel_reliability, tExp_Channel_name}

# tExp_Expression class attributes and methods
tExp_Expression_operator: Property = Property(name="operator", type=StringType)
tExp_Expression_variable: Property = Property(name="variable", type=StringType)
tExp_Expression_eps: Property = Property(name="eps", type=StringType)
tExp_Expression.attributes={tExp_Expression_variable, tExp_Expression_operator, tExp_Expression_eps}

# tExp_Together class attributes and methods

# tExp_Msg class attributes and methods
tExp_Msg_performative: Property = Property(name="performative", type=StringType)
tExp_Msg.attributes={tExp_Msg_performative}

# tExp_UnionExpr class attributes and methods

# tExp_AndExpr class attributes and methods

# tExp_AtomExpression class attributes and methods
tExp_AtomExpression_atom: Property = Property(name="atom", type=StringType)
tExp_AtomExpression.attributes={tExp_AtomExpression_atom}

# PrologExpression class attributes and methods

# tExp_VariableExpression class attributes and methods
tExp_VariableExpression_name: Property = Property(name="name", type=StringType)
tExp_VariableExpression.attributes={tExp_VariableExpression_name}

# tExp_StringExpression class attributes and methods
tExp_StringExpression_value: Property = Property(name="value", type=StringType)
tExp_StringExpression.attributes={tExp_StringExpression_value}

# tExp_NumberExpression class attributes and methods
tExp_NumberExpression_value: Property = Property(name="value", type=StringType)
tExp_NumberExpression.attributes={tExp_NumberExpression_value}

# tExp_ListExpression class attributes and methods

# tExp_ShuffleExpr class attributes and methods

# Expression class attributes and methods

# tExp_Cardinality class attributes and methods
tExp_Cardinality_minCardinality: Property = Property(name="minCardinality", type=IntegerType)
tExp_Cardinality_maxCardinality: Property = Property(name="maxCardinality", type=IntegerType)
tExp_Cardinality.attributes={tExp_Cardinality_maxCardinality, tExp_Cardinality_minCardinality}

# tExp_CatExpr class attributes and methods

# tExp_SeqExpr class attributes and methods

# tExp_FilterExpr class attributes and methods

# tExp_VarExpr class attributes and methods

# tExp_TerminalExpr class attributes and methods

# tExp_Singletons class attributes and methods
tExp_Singletons_minSingletons: Property = Property(name="minSingletons", type=IntegerType)
tExp_Singletons_maxSingletons: Property = Property(name="maxSingletons", type=IntegerType)
tExp_Singletons.attributes={tExp_Singletons_maxSingletons, tExp_Singletons_minSingletons}

# Constraint class attributes and methods

# tExp_Size class attributes and methods
tExp_Size_minSize: Property = Property(name="minSize", type=IntegerType)
tExp_Size_maxSize: Property = Property(name="maxSize", type=IntegerType)
tExp_Size.attributes={tExp_Size_minSize, tExp_Size_maxSize}

# Relationships
right4: BinaryAssociation = BinaryAssociation(
    name="right4",
    ends={
        Property(name="tExp_PrologExpression5", type=tExp_PrologExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="tExp_PrologExpression3", type=tExp_PrologExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
terms6: BinaryAssociation = BinaryAssociation(
    name="terms6",
    ends={
        Property(name="tExp_Term", type=tExp_TraceExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="tExp_TraceExpression7", type=tExp_Term, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
roles8: BinaryAssociation = BinaryAssociation(
    name="roles8",
    ends={
        Property(name="tExp_Role", type=tExp_TraceExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="tExp_TraceExpression9", type=tExp_Role, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="tExp_TraceExpression", type=tExp_Domainmodel, multiplicity=Multiplicity(1, 1)),
        Property(name="tExp_Domainmodel", type=tExp_TraceExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bodyVar21: BinaryAssociation = BinaryAssociation(
    name="bodyVar21",
    ends={
        Property(name="tExp_Expression22", type=tExp_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="tExp_Expression20", type=tExp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeFilter23: BinaryAssociation = BinaryAssociation(
    name="typeFilter23",
    ends={
        Property(name="tExp_EventType25", type=tExp_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="tExp_Expression24", type=tExp_EventType, multiplicity=Multiplicity(0, 1))
    }
)
left2: BinaryAssociation = BinaryAssociation(
    name="left2",
    ends={
        Property(name="tExp_PrologExpression", type=tExp_PrologExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="tExp_PrologExpression1", type=tExp_PrologExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
first26: BinaryAssociation = BinaryAssociation(
    name="first26",
    ends={
        Property(name="tExp_PrologExpression28", type=tExp_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="tExp_Expression27", type=tExp_PrologExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exprs29: BinaryAssociation = BinaryAssociation(
    name="exprs29",
    ends={
        Property(name="tExp_PrologExpression31", type=tExp_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="tExp_Expression30", type=tExp_PrologExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bodyFilter33: BinaryAssociation = BinaryAssociation(
    name="bodyFilter33",
    ends={
        Property(name="tExp_Expression34", type=tExp_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="tExp_Expression32", type=tExp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
types10: BinaryAssociation = BinaryAssociation(
    name="types10",
    ends={
        Property(name="tExp_EventType", type=tExp_TraceExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="tExp_TraceExpression11", type=tExp_EventType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
partition12: BinaryAssociation = BinaryAssociation(
    name="partition12",
    ends={
        Property(name="tExp_Partition", type=tExp_TraceExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="tExp_TraceExpression13", type=tExp_Partition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constraints14: BinaryAssociation = BinaryAssociation(
    name="constraints14",
    ends={
        Property(name="tExp_Constraint", type=tExp_TraceExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="tExp_TraceExpression15", type=tExp_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
channels16: BinaryAssociation = BinaryAssociation(
    name="channels16",
    ends={
        Property(name="tExp_Channel", type=tExp_TraceExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="tExp_TraceExpression17", type=tExp_Channel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr18: BinaryAssociation = BinaryAssociation(
    name="expr18",
    ends={
        Property(name="tExp_Expression", type=tExp_Term, multiplicity=Multiplicity(1, 1)),
        Property(name="tExp_Term19", type=tExp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constraints76: BinaryAssociation = BinaryAssociation(
    name="constraints76",
    ends={
        Property(name="tExp_Together", type=tExp_Partition, multiplicity=Multiplicity(1, 1)),
        Property(name="tExp_Partition77", type=tExp_Together, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
roles78: BinaryAssociation = BinaryAssociation(
    name="roles78",
    ends={
        Property(name="tExp_Role80", type=tExp_Together, multiplicity=Multiplicity(1, 1)),
        Property(name="tExp_Together79", type=tExp_Role, multiplicity=Multiplicity(0, 9999))
    }
)
typeSeq35: BinaryAssociation = BinaryAssociation(
    name="typeSeq35",
    ends={
        Property(name="tExp_EventType37", type=tExp_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="tExp_Expression36", type=tExp_EventType, multiplicity=Multiplicity(0, 1))
    }
)
bodySeq39: BinaryAssociation = BinaryAssociation(
    name="bodySeq39",
    ends={
        Property(name="tExp_Expression40", type=tExp_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="tExp_Expression38", type=tExp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
term41: BinaryAssociation = BinaryAssociation(
    name="term41",
    ends={
        Property(name="tExp_Term43", type=tExp_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="tExp_Expression42", type=tExp_Term, multiplicity=Multiplicity(0, 1))
    }
)
expr45: BinaryAssociation = BinaryAssociation(
    name="expr45",
    ends={
        Property(name="tExp_Expression46", type=tExp_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="tExp_Expression44", type=tExp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr47: BinaryAssociation = BinaryAssociation(
    name="expr47",
    ends={
        Property(name="tExp_PrologExpression49", type=tExp_EventType, multiplicity=Multiplicity(1, 1)),
        Property(name="tExp_EventType48", type=tExp_PrologExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exprs50: BinaryAssociation = BinaryAssociation(
    name="exprs50",
    ends={
        Property(name="tExp_PrologExpression52", type=tExp_EventType, multiplicity=Multiplicity(1, 1)),
        Property(name="tExp_EventType51", type=tExp_PrologExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
msgs53: BinaryAssociation = BinaryAssociation(
    name="msgs53",
    ends={
        Property(name="tExp_Msg", type=tExp_EventType, multiplicity=Multiplicity(1, 1)),
        Property(name="tExp_EventType54", type=tExp_Msg, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
channel55: BinaryAssociation = BinaryAssociation(
    name="channel55",
    ends={
        Property(name="tExp_Channel57", type=tExp_EventType, multiplicity=Multiplicity(1, 1)),
        Property(name="tExp_EventType56", type=tExp_Channel, multiplicity=Multiplicity(0, 1))
    }
)
async_sender58: BinaryAssociation = BinaryAssociation(
    name="async_sender58",
    ends={
        Property(name="tExp_Role60", type=tExp_Msg, multiplicity=Multiplicity(1, 1)),
        Property(name="tExp_Msg59", type=tExp_Role, multiplicity=Multiplicity(0, 1))
    }
)
receiver61: BinaryAssociation = BinaryAssociation(
    name="receiver61",
    ends={
        Property(name="tExp_Role63", type=tExp_Msg, multiplicity=Multiplicity(1, 1)),
        Property(name="tExp_Msg62", type=tExp_Role, multiplicity=Multiplicity(0, 1))
    }
)
sender64: BinaryAssociation = BinaryAssociation(
    name="sender64",
    ends={
        Property(name="tExp_Role66", type=tExp_Msg, multiplicity=Multiplicity(1, 1)),
        Property(name="tExp_Msg65", type=tExp_Role, multiplicity=Multiplicity(0, 1))
    }
)
async_receiver67: BinaryAssociation = BinaryAssociation(
    name="async_receiver67",
    ends={
        Property(name="tExp_Role69", type=tExp_Msg, multiplicity=Multiplicity(1, 1)),
        Property(name="tExp_Msg68", type=tExp_Role, multiplicity=Multiplicity(0, 1))
    }
)
content70: BinaryAssociation = BinaryAssociation(
    name="content70",
    ends={
        Property(name="tExp_PrologExpression72", type=tExp_Msg, multiplicity=Multiplicity(1, 1)),
        Property(name="tExp_Msg71", type=tExp_PrologExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conditions73: BinaryAssociation = BinaryAssociation(
    name="conditions73",
    ends={
        Property(name="tExp_PrologExpression75", type=tExp_Msg, multiplicity=Multiplicity(1, 1)),
        Property(name="tExp_Msg74", type=tExp_PrologExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right96: BinaryAssociation = BinaryAssociation(
    name="right96",
    ends={
        Property(name="tExp_Expression98", type=tExp_ShuffleExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="tExp_ShuffleExpr97", type=tExp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left99: BinaryAssociation = BinaryAssociation(
    name="left99",
    ends={
        Property(name="tExp_Expression100", type=tExp_UnionExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="tExp_UnionExpr", type=tExp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right101: BinaryAssociation = BinaryAssociation(
    name="right101",
    ends={
        Property(name="tExp_Expression103", type=tExp_UnionExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="tExp_UnionExpr102", type=tExp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left81: BinaryAssociation = BinaryAssociation(
    name="left81",
    ends={
        Property(name="tExp_Role83", type=tExp_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="tExp_Constraint82", type=tExp_Role, multiplicity=Multiplicity(0, 9999))
    }
)
right84: BinaryAssociation = BinaryAssociation(
    name="right84",
    ends={
        Property(name="tExp_Role86", type=tExp_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="tExp_Constraint85", type=tExp_Role, multiplicity=Multiplicity(0, 9999))
    }
)
terms87: BinaryAssociation = BinaryAssociation(
    name="terms87",
    ends={
        Property(name="tExp_PrologExpression88", type=tExp_AtomExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="tExp_AtomExpression", type=tExp_PrologExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
head89: BinaryAssociation = BinaryAssociation(
    name="head89",
    ends={
        Property(name="tExp_PrologExpression90", type=tExp_ListExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="tExp_ListExpression", type=tExp_PrologExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tail91: BinaryAssociation = BinaryAssociation(
    name="tail91",
    ends={
        Property(name="tExp_PrologExpression93", type=tExp_ListExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="tExp_ListExpression92", type=tExp_PrologExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left94: BinaryAssociation = BinaryAssociation(
    name="left94",
    ends={
        Property(name="tExp_Expression95", type=tExp_ShuffleExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="tExp_ShuffleExpr", type=tExp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left104: BinaryAssociation = BinaryAssociation(
    name="left104",
    ends={
        Property(name="tExp_Expression105", type=tExp_AndExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="tExp_AndExpr", type=tExp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right106: BinaryAssociation = BinaryAssociation(
    name="right106",
    ends={
        Property(name="tExp_Expression108", type=tExp_AndExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="tExp_AndExpr107", type=tExp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left109: BinaryAssociation = BinaryAssociation(
    name="left109",
    ends={
        Property(name="tExp_Expression110", type=tExp_CatExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="tExp_CatExpr", type=tExp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right111: BinaryAssociation = BinaryAssociation(
    name="right111",
    ends={
        Property(name="tExp_Expression113", type=tExp_CatExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="tExp_CatExpr112", type=tExp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
seqExpr114: BinaryAssociation = BinaryAssociation(
    name="seqExpr114",
    ends={
        Property(name="tExp_Expression115", type=tExp_SeqExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="tExp_SeqExpr", type=tExp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
filterExpr116: BinaryAssociation = BinaryAssociation(
    name="filterExpr116",
    ends={
        Property(name="tExp_Expression117", type=tExp_FilterExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="tExp_FilterExpr", type=tExp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
varExpr118: BinaryAssociation = BinaryAssociation(
    name="varExpr118",
    ends={
        Property(name="tExp_Expression119", type=tExp_VarExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="tExp_VarExpr", type=tExp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
terminalExpr120: BinaryAssociation = BinaryAssociation(
    name="terminalExpr120",
    ends={
        Property(name="tExp_Expression121", type=tExp_TerminalExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="tExp_TerminalExpr", type=tExp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_tExp_UnionExpr_Expression = Generalization(general=Expression, specific=tExp_UnionExpr)
gen_tExp_AndExpr_Expression = Generalization(general=Expression, specific=tExp_AndExpr)
gen_tExp_AtomExpression_PrologExpression = Generalization(general=PrologExpression, specific=tExp_AtomExpression)
gen_tExp_VariableExpression_PrologExpression = Generalization(general=PrologExpression, specific=tExp_VariableExpression)
gen_tExp_StringExpression_PrologExpression = Generalization(general=PrologExpression, specific=tExp_StringExpression)
gen_tExp_NumberExpression_PrologExpression = Generalization(general=PrologExpression, specific=tExp_NumberExpression)
gen_tExp_ListExpression_PrologExpression = Generalization(general=PrologExpression, specific=tExp_ListExpression)
gen_tExp_ShuffleExpr_Expression = Generalization(general=Expression, specific=tExp_ShuffleExpr)
gen_tExp_Cardinality_Constraint = Generalization(general=Constraint, specific=tExp_Cardinality)
gen_tExp_CatExpr_Expression = Generalization(general=Expression, specific=tExp_CatExpr)
gen_tExp_SeqExpr_Expression = Generalization(general=Expression, specific=tExp_SeqExpr)
gen_tExp_FilterExpr_Expression = Generalization(general=Expression, specific=tExp_FilterExpr)
gen_tExp_VarExpr_Expression = Generalization(general=Expression, specific=tExp_VarExpr)
gen_tExp_TerminalExpr_Expression = Generalization(general=Expression, specific=tExp_TerminalExpr)
gen_tExp_Singletons_Constraint = Generalization(general=Constraint, specific=tExp_Singletons)
gen_tExp_Size_Constraint = Generalization(general=Constraint, specific=tExp_Size)

# Domain Model
domain_model = DomainModel(
    name="tExp",
    types={tExp_Term, tExp_Role, tExp_Domainmodel, tExp_TraceExpression, tExp_PrologExpression, tExp_EventType, tExp_Partition, tExp_Constraint, tExp_Channel, tExp_Expression, tExp_Together, tExp_Msg, tExp_UnionExpr, tExp_AndExpr, tExp_AtomExpression, PrologExpression, tExp_VariableExpression, tExp_StringExpression, tExp_NumberExpression, tExp_ListExpression, tExp_ShuffleExpr, Expression, tExp_Cardinality, tExp_CatExpr, tExp_SeqExpr, tExp_FilterExpr, tExp_VarExpr, tExp_TerminalExpr, tExp_Singletons, Constraint, tExp_Size},
    associations={right4, terms6, roles8, elements0, bodyVar21, typeFilter23, left2, first26, exprs29, bodyFilter33, types10, partition12, constraints14, channels16, expr18, constraints76, roles78, typeSeq35, bodySeq39, term41, expr45, expr47, exprs50, msgs53, channel55, async_sender58, receiver61, sender64, async_receiver67, content70, conditions73, right96, left99, right101, left81, right84, terms87, head89, tail91, left94, left104, right106, left109, right111, seqExpr114, filterExpr116, varExpr118, terminalExpr120},
    generalizations={gen_tExp_UnionExpr_Expression, gen_tExp_AndExpr_Expression, gen_tExp_AtomExpression_PrologExpression, gen_tExp_VariableExpression_PrologExpression, gen_tExp_StringExpression_PrologExpression, gen_tExp_NumberExpression_PrologExpression, gen_tExp_ListExpression_PrologExpression, gen_tExp_ShuffleExpr_Expression, gen_tExp_Cardinality_Constraint, gen_tExp_CatExpr_Expression, gen_tExp_SeqExpr_Expression, gen_tExp_FilterExpr_Expression, gen_tExp_VarExpr_Expression, gen_tExp_TerminalExpr_Expression, gen_tExp_Singletons_Constraint, gen_tExp_Size_Constraint},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)