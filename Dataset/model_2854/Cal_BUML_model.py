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
cal_AstEntity = Class(name="cal::AstEntity")
cal_Import = Class(name="cal::Import")
cal_AstAnnotation = Class(name="cal::AstAnnotation")
cal_AstActor = Class(name="cal::AstActor")
cal_AstUnit = Class(name="cal::AstUnit")
cal_Function = Class(name="cal::Function")
cal_AstProcedure = Class(name="cal::AstProcedure")
cal_Variable = Class(name="cal::Variable")
cal_AstType = Class(name="cal::AstType")
cal_AstPort = Class(name="cal::AstPort")
cal_AstAction = Class(name="cal::AstAction")
cal_LocalFsm = Class(name="cal::LocalFsm")
cal_ScheduleFsm = Class(name="cal::ScheduleFsm")
cal_RegExp = Class(name="cal::RegExp")
cal_Priority = Class(name="cal::Priority")
cal_AstExpression = Class(name="cal::AstExpression")
cal_Statement = Class(name="cal::Statement")
cal_AstTag = Class(name="cal::AstTag")
cal_Inequality = Class(name="cal::Inequality")
cal_AstState = Class(name="cal::AstState")
cal_Fsm = Class(name="cal::Fsm")
cal_AstTransition = Class(name="cal::AstTransition")
cal_ExternalTarget = Class(name="cal::ExternalTarget")
cal_InputPattern = Class(name="cal::InputPattern")
cal_OutputPattern = Class(name="cal::OutputPattern")
cal_Guard = Class(name="cal::Guard")
Statement = Class(name="Statement")
cal_VariableReference = Class(name="cal::VariableReference")
cal_StatementCall = Class(name="cal::StatementCall")
cal_StatementAssign = Class(name="cal::StatementAssign")
cal_StatementIf = Class(name="cal::StatementIf")
cal_StatementElsif = Class(name="cal::StatementElsif")
cal_StatementForeach = Class(name="cal::StatementForeach")
cal_StatementWhile = Class(name="cal::StatementWhile")
cal_ExpressionElsif = Class(name="cal::ExpressionElsif")
cal_ExpressionCall = Class(name="cal::ExpressionCall")
AstExpression = Class(name="AstExpression")
cal_ExpressionIndex = Class(name="cal::ExpressionIndex")
cal_ExpressionIf = Class(name="cal::ExpressionIf")
cal_ExpressionVariable = Class(name="cal::ExpressionVariable")
cal_ExpressionLiteral = Class(name="cal::ExpressionLiteral")
cal_ExpressionBoolean = Class(name="cal::ExpressionBoolean")
ExpressionLiteral = Class(name="ExpressionLiteral")
cal_ExpressionFloat = Class(name="cal::ExpressionFloat")
cal_ExpressionInteger = Class(name="cal::ExpressionInteger")
cal_ExpressionList = Class(name="cal::ExpressionList")
cal_ExpressionString = Class(name="cal::ExpressionString")
cal_Generator = Class(name="cal::Generator")
cal_AstTypeList = Class(name="cal::AstTypeList")
cal_AstTypeString = Class(name="cal::AstTypeString")
cal_AstTypeUint = Class(name="cal::AstTypeUint")
cal_AstTypeBool = Class(name="cal::AstTypeBool")
AstType = Class(name="AstType")
cal_AstTypeFloat = Class(name="cal::AstTypeFloat")
cal_AstTypeHalf = Class(name="cal::AstTypeHalf")
cal_AstTypeDouble = Class(name="cal::AstTypeDouble")
cal_AstTypeInt = Class(name="cal::AstTypeInt")
cal_RegExpUnary = Class(name="cal::RegExpUnary")
cal_RegExpTag = Class(name="cal::RegExpTag")
cal_ExpressionBinary = Class(name="cal::ExpressionBinary")
cal_AnnotationArgument = Class(name="cal::AnnotationArgument")
cal_RegExpBinary = Class(name="cal::RegExpBinary")
RegExp = Class(name="RegExp")
cal_ExpressionUnary = Class(name="cal::ExpressionUnary")

# cal_AstEntity class attributes and methods
cal_AstEntity_package: Property = Property(name="package", type=StringType)
cal_AstEntity_name: Property = Property(name="name", type=StringType)
cal_AstEntity.attributes={cal_AstEntity_name, cal_AstEntity_package}

# cal_Import class attributes and methods
cal_Import_importedNamespace: Property = Property(name="importedNamespace", type=StringType)
cal_Import.attributes={cal_Import_importedNamespace}

# cal_AstAnnotation class attributes and methods
cal_AstAnnotation_name: Property = Property(name="name", type=StringType)
cal_AstAnnotation.attributes={cal_AstAnnotation_name}

# cal_AstActor class attributes and methods

# cal_AstUnit class attributes and methods

# cal_Function class attributes and methods
cal_Function_name: Property = Property(name="name", type=StringType)
cal_Function.attributes={cal_Function_name}

# cal_AstProcedure class attributes and methods
cal_AstProcedure_name: Property = Property(name="name", type=StringType)
cal_AstProcedure.attributes={cal_AstProcedure_name}

# cal_Variable class attributes and methods
cal_Variable_constant: Property = Property(name="constant", type=BooleanType)
cal_Variable_name: Property = Property(name="name", type=StringType)
cal_Variable.attributes={cal_Variable_constant, cal_Variable_name}

# cal_AstType class attributes and methods

# cal_AstPort class attributes and methods
cal_AstPort_name: Property = Property(name="name", type=StringType)
cal_AstPort.attributes={cal_AstPort_name}

# cal_AstAction class attributes and methods

# cal_LocalFsm class attributes and methods
cal_LocalFsm_name: Property = Property(name="name", type=StringType)
cal_LocalFsm.attributes={cal_LocalFsm_name}

# cal_ScheduleFsm class attributes and methods

# cal_RegExp class attributes and methods

# cal_Priority class attributes and methods

# cal_AstExpression class attributes and methods

# cal_Statement class attributes and methods

# cal_AstTag class attributes and methods
cal_AstTag_identifiers: Property = Property(name="identifiers", type=StringType)
cal_AstTag.attributes={cal_AstTag_identifiers}

# cal_Inequality class attributes and methods

# cal_AstState class attributes and methods
cal_AstState_name: Property = Property(name="name", type=StringType)
cal_AstState_node: Property = Property(name="node", type=StringType)
cal_AstState.attributes={cal_AstState_node, cal_AstState_name}

# cal_Fsm class attributes and methods

# cal_AstTransition class attributes and methods

# cal_ExternalTarget class attributes and methods

# cal_InputPattern class attributes and methods

# cal_OutputPattern class attributes and methods

# cal_Guard class attributes and methods

# Statement class attributes and methods

# cal_VariableReference class attributes and methods

# cal_StatementCall class attributes and methods

# cal_StatementAssign class attributes and methods

# cal_StatementIf class attributes and methods

# cal_StatementElsif class attributes and methods

# cal_StatementForeach class attributes and methods

# cal_StatementWhile class attributes and methods

# cal_ExpressionElsif class attributes and methods

# cal_ExpressionCall class attributes and methods

# AstExpression class attributes and methods

# cal_ExpressionIndex class attributes and methods

# cal_ExpressionIf class attributes and methods

# cal_ExpressionVariable class attributes and methods

# cal_ExpressionLiteral class attributes and methods

# cal_ExpressionBoolean class attributes and methods
cal_ExpressionBoolean_value: Property = Property(name="value", type=BooleanType)
cal_ExpressionBoolean.attributes={cal_ExpressionBoolean_value}

# ExpressionLiteral class attributes and methods

# cal_ExpressionFloat class attributes and methods
cal_ExpressionFloat_value: Property = Property(name="value", type=FloatType)
cal_ExpressionFloat.attributes={cal_ExpressionFloat_value}

# cal_ExpressionInteger class attributes and methods
cal_ExpressionInteger_value: Property = Property(name="value", type=StringType)
cal_ExpressionInteger.attributes={cal_ExpressionInteger_value}

# cal_ExpressionList class attributes and methods

# cal_ExpressionString class attributes and methods
cal_ExpressionString_value: Property = Property(name="value", type=StringType)
cal_ExpressionString.attributes={cal_ExpressionString_value}

# cal_Generator class attributes and methods

# cal_AstTypeList class attributes and methods

# cal_AstTypeString class attributes and methods

# cal_AstTypeUint class attributes and methods

# cal_AstTypeBool class attributes and methods

# AstType class attributes and methods

# cal_AstTypeFloat class attributes and methods

# cal_AstTypeHalf class attributes and methods

# cal_AstTypeDouble class attributes and methods

# cal_AstTypeInt class attributes and methods

# cal_RegExpUnary class attributes and methods
cal_RegExpUnary_unaryOperator: Property = Property(name="unaryOperator", type=StringType)
cal_RegExpUnary.attributes={cal_RegExpUnary_unaryOperator}

# cal_RegExpTag class attributes and methods

# cal_ExpressionBinary class attributes and methods
cal_ExpressionBinary_operator: Property = Property(name="operator", type=StringType)
cal_ExpressionBinary.attributes={cal_ExpressionBinary_operator}

# cal_AnnotationArgument class attributes and methods
cal_AnnotationArgument_name: Property = Property(name="name", type=StringType)
cal_AnnotationArgument_value: Property = Property(name="value", type=StringType)
cal_AnnotationArgument.attributes={cal_AnnotationArgument_name, cal_AnnotationArgument_value}

# cal_RegExpBinary class attributes and methods
cal_RegExpBinary_operator: Property = Property(name="operator", type=StringType)
cal_RegExpBinary.attributes={cal_RegExpBinary_operator}

# RegExp class attributes and methods

# cal_ExpressionUnary class attributes and methods
cal_ExpressionUnary_unaryOperator: Property = Property(name="unaryOperator", type=StringType)
cal_ExpressionUnary.attributes={cal_ExpressionUnary_unaryOperator}

# Relationships
imports0: BinaryAssociation = BinaryAssociation(
    name="imports0",
    ends={
        Property(name="cal_Import", type=cal_AstEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstEntity", type=cal_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotations1: BinaryAssociation = BinaryAssociation(
    name="annotations1",
    ends={
        Property(name="cal_AstAnnotation", type=cal_AstEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstEntity2", type=cal_AstAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actor3: BinaryAssociation = BinaryAssociation(
    name="actor3",
    ends={
        Property(name="cal_AstActor", type=cal_AstEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstEntity4", type=cal_AstActor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unit5: BinaryAssociation = BinaryAssociation(
    name="unit5",
    ends={
        Property(name="cal_AstUnit", type=cal_AstEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstEntity6", type=cal_AstUnit, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
functions7: BinaryAssociation = BinaryAssociation(
    name="functions7",
    ends={
        Property(name="cal_Function", type=cal_AstUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstUnit8", type=cal_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
procedures9: BinaryAssociation = BinaryAssociation(
    name="procedures9",
    ends={
        Property(name="cal_AstProcedure", type=cal_AstUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstUnit10", type=cal_AstProcedure, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variables11: BinaryAssociation = BinaryAssociation(
    name="variables11",
    ends={
        Property(name="cal_Variable", type=cal_AstUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstUnit12", type=cal_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type18: BinaryAssociation = BinaryAssociation(
    name="type18",
    ends={
        Property(name="cal_AstType", type=cal_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_Variable19", type=cal_AstType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dimensions20: BinaryAssociation = BinaryAssociation(
    name="dimensions20",
    ends={
        Property(name="cal_AstExpression22", type=cal_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_Variable21", type=cal_AstExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters23: BinaryAssociation = BinaryAssociation(
    name="parameters23",
    ends={
        Property(name="cal_Variable25", type=cal_AstActor, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstActor24", type=cal_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputs26: BinaryAssociation = BinaryAssociation(
    name="inputs26",
    ends={
        Property(name="cal_AstPort", type=cal_AstActor, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstActor27", type=cal_AstPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputs28: BinaryAssociation = BinaryAssociation(
    name="outputs28",
    ends={
        Property(name="cal_AstPort30", type=cal_AstActor, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstActor29", type=cal_AstPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functions31: BinaryAssociation = BinaryAssociation(
    name="functions31",
    ends={
        Property(name="cal_Function33", type=cal_AstActor, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstActor32", type=cal_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
procedures34: BinaryAssociation = BinaryAssociation(
    name="procedures34",
    ends={
        Property(name="cal_AstProcedure36", type=cal_AstActor, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstActor35", type=cal_AstProcedure, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actions37: BinaryAssociation = BinaryAssociation(
    name="actions37",
    ends={
        Property(name="cal_AstAction", type=cal_AstActor, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstActor38", type=cal_AstAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initializes39: BinaryAssociation = BinaryAssociation(
    name="initializes39",
    ends={
        Property(name="cal_AstAction41", type=cal_AstActor, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstActor40", type=cal_AstAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stateVariables42: BinaryAssociation = BinaryAssociation(
    name="stateVariables42",
    ends={
        Property(name="cal_Variable44", type=cal_AstActor, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstActor43", type=cal_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
localFsms45: BinaryAssociation = BinaryAssociation(
    name="localFsms45",
    ends={
        Property(name="cal_LocalFsm", type=cal_AstActor, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstActor46", type=cal_LocalFsm, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
scheduleFsm47: BinaryAssociation = BinaryAssociation(
    name="scheduleFsm47",
    ends={
        Property(name="cal_ScheduleFsm", type=cal_AstActor, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstActor48", type=cal_ScheduleFsm, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
scheduleRegExp49: BinaryAssociation = BinaryAssociation(
    name="scheduleRegExp49",
    ends={
        Property(name="cal_RegExp", type=cal_AstActor, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstActor50", type=cal_RegExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
priorities51: BinaryAssociation = BinaryAssociation(
    name="priorities51",
    ends={
        Property(name="cal_Priority", type=cal_AstActor, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstActor52", type=cal_Priority, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotations53: BinaryAssociation = BinaryAssociation(
    name="annotations53",
    ends={
        Property(name="cal_AstAnnotation55", type=cal_AstPort, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstPort54", type=cal_AstAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type56: BinaryAssociation = BinaryAssociation(
    name="type56",
    ends={
        Property(name="cal_AstType58", type=cal_AstPort, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstPort57", type=cal_AstType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotations59: BinaryAssociation = BinaryAssociation(
    name="annotations59",
    ends={
        Property(name="cal_AstAnnotation61", type=cal_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_Function60", type=cal_AstAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value13: BinaryAssociation = BinaryAssociation(
    name="value13",
    ends={
        Property(name="cal_AstExpression", type=cal_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_Variable14", type=cal_AstExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotations15: BinaryAssociation = BinaryAssociation(
    name="annotations15",
    ends={
        Property(name="cal_AstAnnotation17", type=cal_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_Variable16", type=cal_AstAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variables68: BinaryAssociation = BinaryAssociation(
    name="variables68",
    ends={
        Property(name="cal_Variable70", type=cal_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_Function69", type=cal_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression71: BinaryAssociation = BinaryAssociation(
    name="expression71",
    ends={
        Property(name="cal_AstExpression73", type=cal_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_Function72", type=cal_AstExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotations74: BinaryAssociation = BinaryAssociation(
    name="annotations74",
    ends={
        Property(name="cal_AstAnnotation76", type=cal_AstProcedure, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstProcedure75", type=cal_AstAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters77: BinaryAssociation = BinaryAssociation(
    name="parameters77",
    ends={
        Property(name="cal_Variable79", type=cal_AstProcedure, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstProcedure78", type=cal_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variables80: BinaryAssociation = BinaryAssociation(
    name="variables80",
    ends={
        Property(name="cal_Variable82", type=cal_AstProcedure, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstProcedure81", type=cal_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements83: BinaryAssociation = BinaryAssociation(
    name="statements83",
    ends={
        Property(name="cal_Statement", type=cal_AstProcedure, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstProcedure84", type=cal_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tags85: BinaryAssociation = BinaryAssociation(
    name="tags85",
    ends={
        Property(name="cal_AstTag", type=cal_Inequality, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_Inequality", type=cal_AstTag, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inequalities86: BinaryAssociation = BinaryAssociation(
    name="inequalities86",
    ends={
        Property(name="cal_Inequality88", type=cal_Priority, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_Priority87", type=cal_Inequality, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialState89: BinaryAssociation = BinaryAssociation(
    name="initialState89",
    ends={
        Property(name="cal_AstState", type=cal_ScheduleFsm, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_ScheduleFsm90", type=cal_AstState, multiplicity=Multiplicity(0, 1))
    }
)
contents91: BinaryAssociation = BinaryAssociation(
    name="contents91",
    ends={
        Property(name="cal_Fsm", type=cal_ScheduleFsm, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_ScheduleFsm92", type=cal_Fsm, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
transitions93: BinaryAssociation = BinaryAssociation(
    name="transitions93",
    ends={
        Property(name="cal_AstTransition", type=cal_Fsm, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_Fsm94", type=cal_AstTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
states95: BinaryAssociation = BinaryAssociation(
    name="states95",
    ends={
        Property(name="cal_AstState97", type=cal_Fsm, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_Fsm96", type=cal_AstState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source98: BinaryAssociation = BinaryAssociation(
    name="source98",
    ends={
        Property(name="cal_AstState100", type=cal_AstTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstTransition99", type=cal_AstState, multiplicity=Multiplicity(0, 1))
    }
)
tag101: BinaryAssociation = BinaryAssociation(
    name="tag101",
    ends={
        Property(name="cal_AstTag103", type=cal_AstTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstTransition102", type=cal_AstTag, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target104: BinaryAssociation = BinaryAssociation(
    name="target104",
    ends={
        Property(name="cal_AstState106", type=cal_AstTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstTransition105", type=cal_AstState, multiplicity=Multiplicity(0, 1))
    }
)
externalTarget107: BinaryAssociation = BinaryAssociation(
    name="externalTarget107",
    ends={
        Property(name="cal_ExternalTarget", type=cal_AstTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstTransition108", type=cal_ExternalTarget, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters62: BinaryAssociation = BinaryAssociation(
    name="parameters62",
    ends={
        Property(name="cal_Variable64", type=cal_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_Function63", type=cal_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type65: BinaryAssociation = BinaryAssociation(
    name="type65",
    ends={
        Property(name="cal_AstType67", type=cal_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_Function66", type=cal_AstType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
to118: BinaryAssociation = BinaryAssociation(
    name="to118",
    ends={
        Property(name="cal_AstState120", type=cal_ExternalTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_ExternalTarget119", type=cal_AstState, multiplicity=Multiplicity(0, 1))
    }
)
exp122: BinaryAssociation = BinaryAssociation(
    name="exp122",
    ends={
        Property(name="cal_RegExp123", type=cal_RegExp, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_RegExp121", type=cal_RegExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
contents124: BinaryAssociation = BinaryAssociation(
    name="contents124",
    ends={
        Property(name="cal_Fsm126", type=cal_LocalFsm, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_LocalFsm125", type=cal_Fsm, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotations127: BinaryAssociation = BinaryAssociation(
    name="annotations127",
    ends={
        Property(name="cal_AstAnnotation129", type=cal_AstAction, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstAction128", type=cal_AstAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tag130: BinaryAssociation = BinaryAssociation(
    name="tag130",
    ends={
        Property(name="cal_AstTag132", type=cal_AstAction, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstAction131", type=cal_AstTag, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inputs133: BinaryAssociation = BinaryAssociation(
    name="inputs133",
    ends={
        Property(name="cal_InputPattern", type=cal_AstAction, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstAction134", type=cal_InputPattern, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputs135: BinaryAssociation = BinaryAssociation(
    name="outputs135",
    ends={
        Property(name="cal_OutputPattern", type=cal_AstAction, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstAction136", type=cal_OutputPattern, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
guard137: BinaryAssociation = BinaryAssociation(
    name="guard137",
    ends={
        Property(name="cal_Guard", type=cal_AstAction, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstAction138", type=cal_Guard, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variables139: BinaryAssociation = BinaryAssociation(
    name="variables139",
    ends={
        Property(name="cal_Variable141", type=cal_AstAction, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstAction140", type=cal_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements142: BinaryAssociation = BinaryAssociation(
    name="statements142",
    ends={
        Property(name="cal_Statement144", type=cal_AstAction, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstAction143", type=cal_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
port145: BinaryAssociation = BinaryAssociation(
    name="port145",
    ends={
        Property(name="cal_AstPort147", type=cal_InputPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_InputPattern146", type=cal_AstPort, multiplicity=Multiplicity(0, 1))
    }
)
tokens148: BinaryAssociation = BinaryAssociation(
    name="tokens148",
    ends={
        Property(name="cal_Variable150", type=cal_InputPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_InputPattern149", type=cal_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
repeat151: BinaryAssociation = BinaryAssociation(
    name="repeat151",
    ends={
        Property(name="cal_AstExpression153", type=cal_InputPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_InputPattern152", type=cal_AstExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
port154: BinaryAssociation = BinaryAssociation(
    name="port154",
    ends={
        Property(name="cal_AstPort156", type=cal_OutputPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_OutputPattern155", type=cal_AstPort, multiplicity=Multiplicity(0, 1))
    }
)
values157: BinaryAssociation = BinaryAssociation(
    name="values157",
    ends={
        Property(name="cal_AstExpression159", type=cal_OutputPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_OutputPattern158", type=cal_AstExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fsm109: BinaryAssociation = BinaryAssociation(
    name="fsm109",
    ends={
        Property(name="cal_LocalFsm111", type=cal_ExternalTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_ExternalTarget110", type=cal_LocalFsm, multiplicity=Multiplicity(0, 1))
    }
)
state112: BinaryAssociation = BinaryAssociation(
    name="state112",
    ends={
        Property(name="cal_AstState114", type=cal_ExternalTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_ExternalTarget113", type=cal_AstState, multiplicity=Multiplicity(0, 1))
    }
)
from115: BinaryAssociation = BinaryAssociation(
    name="from115",
    ends={
        Property(name="cal_AstState117", type=cal_ExternalTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_ExternalTarget116", type=cal_AstState, multiplicity=Multiplicity(0, 1))
    }
)
target166: BinaryAssociation = BinaryAssociation(
    name="target166",
    ends={
        Property(name="cal_VariableReference", type=cal_StatementAssign, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_StatementAssign", type=cal_VariableReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
indexes167: BinaryAssociation = BinaryAssociation(
    name="indexes167",
    ends={
        Property(name="cal_AstExpression169", type=cal_StatementAssign, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_StatementAssign168", type=cal_AstExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value170: BinaryAssociation = BinaryAssociation(
    name="value170",
    ends={
        Property(name="cal_AstExpression172", type=cal_StatementAssign, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_StatementAssign171", type=cal_AstExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
procedure173: BinaryAssociation = BinaryAssociation(
    name="procedure173",
    ends={
        Property(name="cal_AstProcedure174", type=cal_StatementCall, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_StatementCall", type=cal_AstProcedure, multiplicity=Multiplicity(0, 1))
    }
)
arguments175: BinaryAssociation = BinaryAssociation(
    name="arguments175",
    ends={
        Property(name="cal_AstExpression177", type=cal_StatementCall, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_StatementCall176", type=cal_AstExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
repeat160: BinaryAssociation = BinaryAssociation(
    name="repeat160",
    ends={
        Property(name="cal_AstExpression162", type=cal_OutputPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_OutputPattern161", type=cal_AstExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressions163: BinaryAssociation = BinaryAssociation(
    name="expressions163",
    ends={
        Property(name="cal_AstExpression165", type=cal_Guard, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_Guard164", type=cal_AstExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable178: BinaryAssociation = BinaryAssociation(
    name="variable178",
    ends={
        Property(name="cal_Variable179", type=cal_StatementForeach, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_StatementForeach", type=cal_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lower180: BinaryAssociation = BinaryAssociation(
    name="lower180",
    ends={
        Property(name="cal_AstExpression182", type=cal_StatementForeach, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_StatementForeach181", type=cal_AstExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
higher183: BinaryAssociation = BinaryAssociation(
    name="higher183",
    ends={
        Property(name="cal_AstExpression185", type=cal_StatementForeach, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_StatementForeach184", type=cal_AstExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements186: BinaryAssociation = BinaryAssociation(
    name="statements186",
    ends={
        Property(name="cal_Statement188", type=cal_StatementForeach, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_StatementForeach187", type=cal_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition189: BinaryAssociation = BinaryAssociation(
    name="condition189",
    ends={
        Property(name="cal_AstExpression190", type=cal_StatementIf, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_StatementIf", type=cal_AstExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
then191: BinaryAssociation = BinaryAssociation(
    name="then191",
    ends={
        Property(name="cal_Statement193", type=cal_StatementIf, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_StatementIf192", type=cal_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elsifs194: BinaryAssociation = BinaryAssociation(
    name="elsifs194",
    ends={
        Property(name="cal_StatementElsif", type=cal_StatementIf, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_StatementIf195", type=cal_StatementElsif, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
else196: BinaryAssociation = BinaryAssociation(
    name="else196",
    ends={
        Property(name="cal_Statement198", type=cal_StatementIf, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_StatementIf197", type=cal_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition226: BinaryAssociation = BinaryAssociation(
    name="condition226",
    ends={
        Property(name="cal_AstExpression227", type=cal_ExpressionIf, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_ExpressionIf", type=cal_AstExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
then202: BinaryAssociation = BinaryAssociation(
    name="then202",
    ends={
        Property(name="cal_Statement204", type=cal_StatementElsif, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_StatementElsif203", type=cal_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
then228: BinaryAssociation = BinaryAssociation(
    name="then228",
    ends={
        Property(name="cal_AstExpression230", type=cal_ExpressionIf, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_ExpressionIf229", type=cal_AstExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition205: BinaryAssociation = BinaryAssociation(
    name="condition205",
    ends={
        Property(name="cal_AstExpression206", type=cal_StatementWhile, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_StatementWhile", type=cal_AstExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elsifs231: BinaryAssociation = BinaryAssociation(
    name="elsifs231",
    ends={
        Property(name="cal_ExpressionElsif", type=cal_ExpressionIf, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_ExpressionIf232", type=cal_ExpressionElsif, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements207: BinaryAssociation = BinaryAssociation(
    name="statements207",
    ends={
        Property(name="cal_Statement209", type=cal_StatementWhile, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_StatementWhile208", type=cal_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
else233: BinaryAssociation = BinaryAssociation(
    name="else233",
    ends={
        Property(name="cal_AstExpression235", type=cal_ExpressionIf, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_ExpressionIf234", type=cal_AstExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotations210: BinaryAssociation = BinaryAssociation(
    name="annotations210",
    ends={
        Property(name="cal_AstAnnotation212", type=cal_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_Statement211", type=cal_AstAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition236: BinaryAssociation = BinaryAssociation(
    name="condition236",
    ends={
        Property(name="cal_AstExpression238", type=cal_ExpressionElsif, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_ExpressionElsif237", type=cal_AstExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
then239: BinaryAssociation = BinaryAssociation(
    name="then239",
    ends={
        Property(name="cal_AstExpression241", type=cal_ExpressionElsif, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_ExpressionElsif240", type=cal_AstExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotations213: BinaryAssociation = BinaryAssociation(
    name="annotations213",
    ends={
        Property(name="cal_AstAnnotation214", type=cal_ExpressionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_ExpressionCall", type=cal_AstAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
function215: BinaryAssociation = BinaryAssociation(
    name="function215",
    ends={
        Property(name="cal_Function217", type=cal_ExpressionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_ExpressionCall216", type=cal_Function, multiplicity=Multiplicity(0, 1))
    }
)
parameters218: BinaryAssociation = BinaryAssociation(
    name="parameters218",
    ends={
        Property(name="cal_AstExpression220", type=cal_ExpressionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_ExpressionCall219", type=cal_AstExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source221: BinaryAssociation = BinaryAssociation(
    name="source221",
    ends={
        Property(name="cal_VariableReference222", type=cal_ExpressionIndex, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_ExpressionIndex", type=cal_VariableReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
indexes223: BinaryAssociation = BinaryAssociation(
    name="indexes223",
    ends={
        Property(name="cal_AstExpression225", type=cal_ExpressionIndex, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_ExpressionIndex224", type=cal_AstExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition199: BinaryAssociation = BinaryAssociation(
    name="condition199",
    ends={
        Property(name="cal_AstExpression201", type=cal_StatementElsif, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_StatementElsif200", type=cal_AstExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
higher252: BinaryAssociation = BinaryAssociation(
    name="higher252",
    ends={
        Property(name="cal_AstExpression254", type=cal_Generator, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_Generator253", type=cal_AstExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value255: BinaryAssociation = BinaryAssociation(
    name="value255",
    ends={
        Property(name="cal_VariableReference256", type=cal_ExpressionVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_ExpressionVariable", type=cal_VariableReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressions242: BinaryAssociation = BinaryAssociation(
    name="expressions242",
    ends={
        Property(name="cal_AstExpression243", type=cal_ExpressionList, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_ExpressionList", type=cal_AstExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
generators244: BinaryAssociation = BinaryAssociation(
    name="generators244",
    ends={
        Property(name="cal_Generator", type=cal_ExpressionList, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_ExpressionList245", type=cal_Generator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable246: BinaryAssociation = BinaryAssociation(
    name="variable246",
    ends={
        Property(name="cal_Variable248", type=cal_Generator, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_Generator247", type=cal_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lower249: BinaryAssociation = BinaryAssociation(
    name="lower249",
    ends={
        Property(name="cal_AstExpression251", type=cal_Generator, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_Generator250", type=cal_AstExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
size257: BinaryAssociation = BinaryAssociation(
    name="size257",
    ends={
        Property(name="cal_AstTypeInt", type=cal_AstExpression, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="cal_AstExpression258", type=cal_AstTypeInt, multiplicity=Multiplicity(1, 1))
    }
)
type259: BinaryAssociation = BinaryAssociation(
    name="type259",
    ends={
        Property(name="cal_AstType260", type=cal_AstTypeList, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstTypeList", type=cal_AstType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
size261: BinaryAssociation = BinaryAssociation(
    name="size261",
    ends={
        Property(name="cal_AstExpression263", type=cal_AstTypeList, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstTypeList262", type=cal_AstExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
size264: BinaryAssociation = BinaryAssociation(
    name="size264",
    ends={
        Property(name="cal_AstExpression265", type=cal_AstTypeUint, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstTypeUint", type=cal_AstExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable266: BinaryAssociation = BinaryAssociation(
    name="variable266",
    ends={
        Property(name="cal_Variable268", type=cal_VariableReference, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_VariableReference267", type=cal_Variable, multiplicity=Multiplicity(0, 1))
    }
)
left271: BinaryAssociation = BinaryAssociation(
    name="left271",
    ends={
        Property(name="cal_RegExp272", type=cal_RegExpBinary, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_RegExpBinary", type=cal_RegExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right273: BinaryAssociation = BinaryAssociation(
    name="right273",
    ends={
        Property(name="cal_RegExp275", type=cal_RegExpBinary, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_RegExpBinary274", type=cal_RegExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
child276: BinaryAssociation = BinaryAssociation(
    name="child276",
    ends={
        Property(name="cal_RegExp277", type=cal_RegExpUnary, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_RegExpUnary", type=cal_RegExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tag278: BinaryAssociation = BinaryAssociation(
    name="tag278",
    ends={
        Property(name="cal_AstTag279", type=cal_RegExpTag, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_RegExpTag", type=cal_AstTag, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left280: BinaryAssociation = BinaryAssociation(
    name="left280",
    ends={
        Property(name="cal_AstExpression281", type=cal_ExpressionBinary, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_ExpressionBinary", type=cal_AstExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments269: BinaryAssociation = BinaryAssociation(
    name="arguments269",
    ends={
        Property(name="cal_AnnotationArgument", type=cal_AstAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstAnnotation270", type=cal_AnnotationArgument, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
right282: BinaryAssociation = BinaryAssociation(
    name="right282",
    ends={
        Property(name="cal_AstExpression284", type=cal_ExpressionBinary, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_ExpressionBinary283", type=cal_AstExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression285: BinaryAssociation = BinaryAssociation(
    name="expression285",
    ends={
        Property(name="cal_AstExpression286", type=cal_ExpressionUnary, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_ExpressionUnary", type=cal_AstExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_cal_StatementAssign_Statement = Generalization(general=Statement, specific=cal_StatementAssign)
gen_cal_StatementCall_Statement = Generalization(general=Statement, specific=cal_StatementCall)
gen_cal_StatementIf_Statement = Generalization(general=Statement, specific=cal_StatementIf)
gen_cal_StatementForeach_Statement = Generalization(general=Statement, specific=cal_StatementForeach)
gen_cal_StatementWhile_Statement = Generalization(general=Statement, specific=cal_StatementWhile)
gen_cal_ExpressionCall_AstExpression = Generalization(general=AstExpression, specific=cal_ExpressionCall)
gen_cal_ExpressionIndex_AstExpression = Generalization(general=AstExpression, specific=cal_ExpressionIndex)
gen_cal_ExpressionIf_AstExpression = Generalization(general=AstExpression, specific=cal_ExpressionIf)
gen_cal_ExpressionVariable_AstExpression = Generalization(general=AstExpression, specific=cal_ExpressionVariable)
gen_cal_ExpressionLiteral_AstExpression = Generalization(general=AstExpression, specific=cal_ExpressionLiteral)
gen_cal_ExpressionBoolean_ExpressionLiteral = Generalization(general=ExpressionLiteral, specific=cal_ExpressionBoolean)
gen_cal_ExpressionFloat_ExpressionLiteral = Generalization(general=ExpressionLiteral, specific=cal_ExpressionFloat)
gen_cal_ExpressionInteger_ExpressionLiteral = Generalization(general=ExpressionLiteral, specific=cal_ExpressionInteger)
gen_cal_ExpressionList_AstExpression = Generalization(general=AstExpression, specific=cal_ExpressionList)
gen_cal_ExpressionString_ExpressionLiteral = Generalization(general=ExpressionLiteral, specific=cal_ExpressionString)
gen_cal_AstTypeList_AstType = Generalization(general=AstType, specific=cal_AstTypeList)
gen_cal_AstTypeString_AstType = Generalization(general=AstType, specific=cal_AstTypeString)
gen_cal_AstTypeUint_AstType = Generalization(general=AstType, specific=cal_AstTypeUint)
gen_cal_AstTypeBool_AstType = Generalization(general=AstType, specific=cal_AstTypeBool)
gen_cal_AstTypeFloat_AstType = Generalization(general=AstType, specific=cal_AstTypeFloat)
gen_cal_AstTypeHalf_AstType = Generalization(general=AstType, specific=cal_AstTypeHalf)
gen_cal_AstTypeDouble_AstType = Generalization(general=AstType, specific=cal_AstTypeDouble)
gen_cal_AstTypeInt_AstType = Generalization(general=AstType, specific=cal_AstTypeInt)
gen_cal_RegExpUnary_RegExp = Generalization(general=RegExp, specific=cal_RegExpUnary)
gen_cal_RegExpTag_RegExp = Generalization(general=RegExp, specific=cal_RegExpTag)
gen_cal_ExpressionBinary_AstExpression = Generalization(general=AstExpression, specific=cal_ExpressionBinary)
gen_cal_RegExpBinary_RegExp = Generalization(general=RegExp, specific=cal_RegExpBinary)
gen_cal_ExpressionUnary_AstExpression = Generalization(general=AstExpression, specific=cal_ExpressionUnary)

# Domain Model
domain_model = DomainModel(
    name="cal",
    types={cal_AstEntity, cal_Import, cal_AstAnnotation, cal_AstActor, cal_AstUnit, cal_Function, cal_AstProcedure, cal_Variable, cal_AstType, cal_AstPort, cal_AstAction, cal_LocalFsm, cal_ScheduleFsm, cal_RegExp, cal_Priority, cal_AstExpression, cal_Statement, cal_AstTag, cal_Inequality, cal_AstState, cal_Fsm, cal_AstTransition, cal_ExternalTarget, cal_InputPattern, cal_OutputPattern, cal_Guard, Statement, cal_VariableReference, cal_StatementCall, cal_StatementAssign, cal_StatementIf, cal_StatementElsif, cal_StatementForeach, cal_StatementWhile, cal_ExpressionElsif, cal_ExpressionCall, AstExpression, cal_ExpressionIndex, cal_ExpressionIf, cal_ExpressionVariable, cal_ExpressionLiteral, cal_ExpressionBoolean, ExpressionLiteral, cal_ExpressionFloat, cal_ExpressionInteger, cal_ExpressionList, cal_ExpressionString, cal_Generator, cal_AstTypeList, cal_AstTypeString, cal_AstTypeUint, cal_AstTypeBool, AstType, cal_AstTypeFloat, cal_AstTypeHalf, cal_AstTypeDouble, cal_AstTypeInt, cal_RegExpUnary, cal_RegExpTag, cal_ExpressionBinary, cal_AnnotationArgument, cal_RegExpBinary, RegExp, cal_ExpressionUnary},
    associations={imports0, annotations1, actor3, unit5, functions7, procedures9, variables11, type18, dimensions20, parameters23, inputs26, outputs28, functions31, procedures34, actions37, initializes39, stateVariables42, localFsms45, scheduleFsm47, scheduleRegExp49, priorities51, annotations53, type56, annotations59, value13, annotations15, variables68, expression71, annotations74, parameters77, variables80, statements83, tags85, inequalities86, initialState89, contents91, transitions93, states95, source98, tag101, target104, externalTarget107, parameters62, type65, to118, exp122, contents124, annotations127, tag130, inputs133, outputs135, guard137, variables139, statements142, port145, tokens148, repeat151, port154, values157, fsm109, state112, from115, target166, indexes167, value170, procedure173, arguments175, repeat160, expressions163, variable178, lower180, higher183, statements186, condition189, then191, elsifs194, else196, condition226, then202, then228, condition205, elsifs231, statements207, else233, annotations210, condition236, then239, annotations213, function215, parameters218, source221, indexes223, condition199, higher252, value255, expressions242, generators244, variable246, lower249, size257, type259, size261, size264, variable266, left271, right273, child276, tag278, left280, arguments269, right282, expression285},
    generalizations={gen_cal_StatementAssign_Statement, gen_cal_StatementCall_Statement, gen_cal_StatementIf_Statement, gen_cal_StatementForeach_Statement, gen_cal_StatementWhile_Statement, gen_cal_ExpressionCall_AstExpression, gen_cal_ExpressionIndex_AstExpression, gen_cal_ExpressionIf_AstExpression, gen_cal_ExpressionVariable_AstExpression, gen_cal_ExpressionLiteral_AstExpression, gen_cal_ExpressionBoolean_ExpressionLiteral, gen_cal_ExpressionFloat_ExpressionLiteral, gen_cal_ExpressionInteger_ExpressionLiteral, gen_cal_ExpressionList_AstExpression, gen_cal_ExpressionString_ExpressionLiteral, gen_cal_AstTypeList_AstType, gen_cal_AstTypeString_AstType, gen_cal_AstTypeUint_AstType, gen_cal_AstTypeBool_AstType, gen_cal_AstTypeFloat_AstType, gen_cal_AstTypeHalf_AstType, gen_cal_AstTypeDouble_AstType, gen_cal_AstTypeInt_AstType, gen_cal_RegExpUnary_RegExp, gen_cal_RegExpTag_RegExp, gen_cal_ExpressionBinary_AstExpression, gen_cal_RegExpBinary_RegExp, gen_cal_ExpressionUnary_AstExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)