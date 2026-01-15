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
cal_AstTop = Class(name="cal::AstTop")
cal_AstPackage = Class(name="cal::AstPackage")
AstTop = Class(name="AstTop")
cal_AstUnit = Class(name="cal::AstUnit")
cal_AstNamespace = Class(name="cal::AstNamespace")
AstPackage = Class(name="AstPackage")
AstUnit = Class(name="AstUnit")
cal_AstEntity = Class(name="cal::AstEntity")
cal_Import = Class(name="cal::Import")
cal_AstFunction = Class(name="cal::AstFunction")
cal_EObject = Class(name="cal::EObject")
cal_AstAnnotation = Class(name="cal::AstAnnotation")
cal_AstTypeName = Class(name="cal::AstTypeName")
cal_AstAbstractActor = Class(name="cal::AstAbstractActor")
cal_AstPort = Class(name="cal::AstPort")
cal_AstVariable = Class(name="cal::AstVariable")
cal_AstNetwork = Class(name="cal::AstNetwork")
AstAbstractActor = Class(name="AstAbstractActor")
cal_AstActorVariable = Class(name="cal::AstActorVariable")
cal_AstStructure = Class(name="cal::AstStructure")
cal_AstAssignParameter = Class(name="cal::AstAssignParameter")
cal_AstExpression = Class(name="cal::AstExpression")
cal_AstConnection = Class(name="cal::AstConnection")
cal_AstActorVariableReference = Class(name="cal::AstActorVariableReference")
cal_AstConnectionAttribute = Class(name="cal::AstConnectionAttribute")
cal_AstType = Class(name="cal::AstType")
AstExternalFunction = Class(name="AstExternalFunction")
cal_AstTypeDefinitionParameter = Class(name="cal::AstTypeDefinitionParameter")
cal_AstActor = Class(name="cal::AstActor")
cal_AstProcedure = Class(name="cal::AstProcedure")
cal_AstAction = Class(name="cal::AstAction")
cal_AstSchedule = Class(name="cal::AstSchedule")
cal_AstPriority = Class(name="cal::AstPriority")
cal_AstExternalFunction = Class(name="cal::AstExternalFunction")
AstExternalProcedure = Class(name="AstExternalProcedure")
cal_AstStatement = Class(name="cal::AstStatement")
cal_AstExternalProcedure = Class(name="cal::AstExternalProcedure")
cal_AstTag = Class(name="cal::AstTag")
cal_AstExternalActor = Class(name="cal::AstExternalActor")
cal_AstInequality = Class(name="cal::AstInequality")
cal_AstState = Class(name="cal::AstState")
cal_AstTransition = Class(name="cal::AstTransition")
cal_AstInputPattern = Class(name="cal::AstInputPattern")
cal_AstOutputPattern = Class(name="cal::AstOutputPattern")
cal_AstStatementAssign = Class(name="cal::AstStatementAssign")
AstStatement = Class(name="AstStatement")
cal_AstVariableReference = Class(name="cal::AstVariableReference")
cal_AstMemberAccess = Class(name="cal::AstMemberAccess")
cal_AstStatementCall = Class(name="cal::AstStatementCall")
cal_AstStatementForeach = Class(name="cal::AstStatementForeach")
cal_AstForeachGenerator = Class(name="cal::AstForeachGenerator")
cal_AstStatementBlock = Class(name="cal::AstStatementBlock")
cal_AstStatementIf = Class(name="cal::AstStatementIf")
cal_AstStatementWhile = Class(name="cal::AstStatementWhile")
cal_AstExpressionCall = Class(name="cal::AstExpressionCall")
AstExpression = Class(name="AstExpression")
cal_AstExpressionIf = Class(name="cal::AstExpressionIf")
cal_AstExpressionList = Class(name="cal::AstExpressionList")
cal_AstExpressionVariable = Class(name="cal::AstExpressionVariable")
cal_AstExpressionLiteral = Class(name="cal::AstExpressionLiteral")
cal_AstExpressionBoolean = Class(name="cal::AstExpressionBoolean")
AstExpressionLiteral = Class(name="AstExpressionLiteral")
cal_AstExpressionFloat = Class(name="cal::AstExpressionFloat")
cal_AstExpressionInteger = Class(name="cal::AstExpressionInteger")
cal_AstExpressionString = Class(name="cal::AstExpressionString")
cal_AstTypeParameterList = Class(name="cal::AstTypeParameterList")
cal_AstGenerator = Class(name="cal::AstGenerator")
cal_AstAnnotationArgument = Class(name="cal::AstAnnotationArgument")
cal_AstInitialize = Class(name="cal::AstInitialize")
AstAction = Class(name="AstAction")
cal_AstExpressionBinary = Class(name="cal::AstExpressionBinary")
cal_AstExpressionUnary = Class(name="cal::AstExpressionUnary")
cal_AstTypeParam = Class(name="cal::AstTypeParam")

# cal_AstTop class attributes and methods

# cal_AstPackage class attributes and methods

# AstTop class attributes and methods

# cal_AstUnit class attributes and methods

# cal_AstNamespace class attributes and methods
cal_AstNamespace_name: Property = Property(name="name", type=StringType)
cal_AstNamespace.attributes={cal_AstNamespace_name}

# AstPackage class attributes and methods

# AstUnit class attributes and methods

# cal_AstEntity class attributes and methods

# cal_Import class attributes and methods
cal_Import_importedNamespace: Property = Property(name="importedNamespace", type=StringType)
cal_Import.attributes={cal_Import_importedNamespace}

# cal_AstFunction class attributes and methods
cal_AstFunction_name: Property = Property(name="name", type=StringType)
cal_AstFunction.attributes={cal_AstFunction_name}

# cal_EObject class attributes and methods

# cal_AstAnnotation class attributes and methods
cal_AstAnnotation_name: Property = Property(name="name", type=StringType)
cal_AstAnnotation.attributes={cal_AstAnnotation_name}

# cal_AstTypeName class attributes and methods
cal_AstTypeName_name: Property = Property(name="name", type=StringType)
cal_AstTypeName.attributes={cal_AstTypeName_name}

# cal_AstAbstractActor class attributes and methods
cal_AstAbstractActor_name: Property = Property(name="name", type=StringType)
cal_AstAbstractActor.attributes={cal_AstAbstractActor_name}

# cal_AstPort class attributes and methods
cal_AstPort_name: Property = Property(name="name", type=StringType)
cal_AstPort.attributes={cal_AstPort_name}

# cal_AstVariable class attributes and methods
cal_AstVariable_constant: Property = Property(name="constant", type=BooleanType)
cal_AstVariable_name: Property = Property(name="name", type=StringType)
cal_AstVariable.attributes={cal_AstVariable_constant, cal_AstVariable_name}

# cal_AstNetwork class attributes and methods

# AstAbstractActor class attributes and methods

# cal_AstActorVariable class attributes and methods
cal_AstActorVariable_name: Property = Property(name="name", type=StringType)
cal_AstActorVariable.attributes={cal_AstActorVariable_name}

# cal_AstStructure class attributes and methods

# cal_AstAssignParameter class attributes and methods
cal_AstAssignParameter_name: Property = Property(name="name", type=StringType)
cal_AstAssignParameter.attributes={cal_AstAssignParameter_name}

# cal_AstExpression class attributes and methods

# cal_AstConnection class attributes and methods
cal_AstConnection_outPort: Property = Property(name="outPort", type=StringType)
cal_AstConnection_inPort: Property = Property(name="inPort", type=StringType)
cal_AstConnection.attributes={cal_AstConnection_outPort, cal_AstConnection_inPort}

# cal_AstActorVariableReference class attributes and methods

# cal_AstConnectionAttribute class attributes and methods
cal_AstConnectionAttribute_name: Property = Property(name="name", type=StringType)
cal_AstConnectionAttribute.attributes={cal_AstConnectionAttribute_name}

# cal_AstType class attributes and methods
cal_AstType_builtin: Property = Property(name="builtin", type=StringType)
cal_AstType.attributes={cal_AstType_builtin}

# AstExternalFunction class attributes and methods

# cal_AstTypeDefinitionParameter class attributes and methods

# cal_AstActor class attributes and methods

# cal_AstProcedure class attributes and methods
cal_AstProcedure_name: Property = Property(name="name", type=StringType)
cal_AstProcedure.attributes={cal_AstProcedure_name}

# cal_AstAction class attributes and methods

# cal_AstSchedule class attributes and methods

# cal_AstPriority class attributes and methods

# cal_AstExternalFunction class attributes and methods

# AstExternalProcedure class attributes and methods

# cal_AstStatement class attributes and methods

# cal_AstExternalProcedure class attributes and methods

# cal_AstTag class attributes and methods
cal_AstTag_identifiers: Property = Property(name="identifiers", type=StringType)
cal_AstTag.attributes={cal_AstTag_identifiers}

# cal_AstExternalActor class attributes and methods

# cal_AstInequality class attributes and methods

# cal_AstState class attributes and methods
cal_AstState_name: Property = Property(name="name", type=StringType)
cal_AstState.attributes={cal_AstState_name}

# cal_AstTransition class attributes and methods

# cal_AstInputPattern class attributes and methods

# cal_AstOutputPattern class attributes and methods

# cal_AstStatementAssign class attributes and methods

# AstStatement class attributes and methods

# cal_AstVariableReference class attributes and methods

# cal_AstMemberAccess class attributes and methods
cal_AstMemberAccess_name: Property = Property(name="name", type=StringType)
cal_AstMemberAccess.attributes={cal_AstMemberAccess_name}

# cal_AstStatementCall class attributes and methods

# cal_AstStatementForeach class attributes and methods

# cal_AstForeachGenerator class attributes and methods

# cal_AstStatementBlock class attributes and methods

# cal_AstStatementIf class attributes and methods

# cal_AstStatementWhile class attributes and methods

# cal_AstExpressionCall class attributes and methods

# AstExpression class attributes and methods

# cal_AstExpressionIf class attributes and methods

# cal_AstExpressionList class attributes and methods

# cal_AstExpressionVariable class attributes and methods

# cal_AstExpressionLiteral class attributes and methods

# cal_AstExpressionBoolean class attributes and methods
cal_AstExpressionBoolean_value: Property = Property(name="value", type=BooleanType)
cal_AstExpressionBoolean.attributes={cal_AstExpressionBoolean_value}

# AstExpressionLiteral class attributes and methods

# cal_AstExpressionFloat class attributes and methods
cal_AstExpressionFloat_value: Property = Property(name="value", type=FloatType)
cal_AstExpressionFloat.attributes={cal_AstExpressionFloat_value}

# cal_AstExpressionInteger class attributes and methods
cal_AstExpressionInteger_value: Property = Property(name="value", type=StringType)
cal_AstExpressionInteger.attributes={cal_AstExpressionInteger_value}

# cal_AstExpressionString class attributes and methods
cal_AstExpressionString_value: Property = Property(name="value", type=StringType)
cal_AstExpressionString.attributes={cal_AstExpressionString_value}

# cal_AstTypeParameterList class attributes and methods

# cal_AstGenerator class attributes and methods

# cal_AstAnnotationArgument class attributes and methods
cal_AstAnnotationArgument_name: Property = Property(name="name", type=StringType)
cal_AstAnnotationArgument_value: Property = Property(name="value", type=StringType)
cal_AstAnnotationArgument.attributes={cal_AstAnnotationArgument_value, cal_AstAnnotationArgument_name}

# cal_AstInitialize class attributes and methods

# AstAction class attributes and methods

# cal_AstExpressionBinary class attributes and methods
cal_AstExpressionBinary_operator: Property = Property(name="operator", type=StringType)
cal_AstExpressionBinary.attributes={cal_AstExpressionBinary_operator}

# cal_AstExpressionUnary class attributes and methods
cal_AstExpressionUnary_unaryOperator: Property = Property(name="unaryOperator", type=StringType)
cal_AstExpressionUnary.attributes={cal_AstExpressionUnary_unaryOperator}

# cal_AstTypeParam class attributes and methods
cal_AstTypeParam_name: Property = Property(name="name", type=StringType)
cal_AstTypeParam.attributes={cal_AstTypeParam_name}

# Relationships
entities0: BinaryAssociation = BinaryAssociation(
    name="entities0",
    ends={
        Property(name="cal_AstEntity", type=cal_AstNamespace, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstNamespace", type=cal_AstEntity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
imports1: BinaryAssociation = BinaryAssociation(
    name="imports1",
    ends={
        Property(name="cal_Import", type=cal_AstNamespace, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstNamespace2", type=cal_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
units3: BinaryAssociation = BinaryAssociation(
    name="units3",
    ends={
        Property(name="cal_AstUnit", type=cal_AstNamespace, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstNamespace4", type=cal_AstUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
externals9: BinaryAssociation = BinaryAssociation(
    name="externals9",
    ends={
        Property(name="cal_EObject", type=cal_AstNamespace, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstNamespace10", type=cal_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotations11: BinaryAssociation = BinaryAssociation(
    name="annotations11",
    ends={
        Property(name="cal_AstAnnotation", type=cal_AstNamespace, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstNamespace12", type=cal_AstAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typedefs13: BinaryAssociation = BinaryAssociation(
    name="typedefs13",
    ends={
        Property(name="cal_AstTypeName", type=cal_AstNamespace, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstNamespace14", type=cal_AstTypeName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
namespaces16: BinaryAssociation = BinaryAssociation(
    name="namespaces16",
    ends={
        Property(name="cal_AstNamespace17", type=cal_AstNamespace, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstNamespace15", type=cal_AstNamespace, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotations18: BinaryAssociation = BinaryAssociation(
    name="annotations18",
    ends={
        Property(name="cal_AstAnnotation20", type=cal_AstEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstEntity19", type=cal_AstAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actor21: BinaryAssociation = BinaryAssociation(
    name="actor21",
    ends={
        Property(name="cal_AstAbstractActor", type=cal_AstEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstEntity22", type=cal_AstAbstractActor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters23: BinaryAssociation = BinaryAssociation(
    name="parameters23",
    ends={
        Property(name="cal_AstVariable25", type=cal_AstAbstractActor, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstAbstractActor24", type=cal_AstVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputs26: BinaryAssociation = BinaryAssociation(
    name="inputs26",
    ends={
        Property(name="cal_AstPort", type=cal_AstAbstractActor, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstAbstractActor27", type=cal_AstPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functions5: BinaryAssociation = BinaryAssociation(
    name="functions5",
    ends={
        Property(name="cal_AstFunction", type=cal_AstNamespace, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstNamespace6", type=cal_AstFunction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variables7: BinaryAssociation = BinaryAssociation(
    name="variables7",
    ends={
        Property(name="cal_AstVariable", type=cal_AstNamespace, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstNamespace8", type=cal_AstVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variables31: BinaryAssociation = BinaryAssociation(
    name="variables31",
    ends={
        Property(name="cal_AstVariable32", type=cal_AstNetwork, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstNetwork", type=cal_AstVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instances33: BinaryAssociation = BinaryAssociation(
    name="instances33",
    ends={
        Property(name="cal_AstActorVariable", type=cal_AstNetwork, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstNetwork34", type=cal_AstActorVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
structure35: BinaryAssociation = BinaryAssociation(
    name="structure35",
    ends={
        Property(name="cal_AstStructure", type=cal_AstNetwork, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstNetwork36", type=cal_AstStructure, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type37: BinaryAssociation = BinaryAssociation(
    name="type37",
    ends={
        Property(name="cal_AstEntity39", type=cal_AstActorVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstActorVariable38", type=cal_AstEntity, multiplicity=Multiplicity(0, 1))
    }
)
parameters40: BinaryAssociation = BinaryAssociation(
    name="parameters40",
    ends={
        Property(name="cal_AstAssignParameter", type=cal_AstActorVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstActorVariable41", type=cal_AstAssignParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value42: BinaryAssociation = BinaryAssociation(
    name="value42",
    ends={
        Property(name="cal_AstExpression", type=cal_AstAssignParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstAssignParameter43", type=cal_AstExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
connections44: BinaryAssociation = BinaryAssociation(
    name="connections44",
    ends={
        Property(name="cal_AstConnection", type=cal_AstStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstStructure45", type=cal_AstConnection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputs28: BinaryAssociation = BinaryAssociation(
    name="outputs28",
    ends={
        Property(name="cal_AstPort30", type=cal_AstAbstractActor, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstAbstractActor29", type=cal_AstPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
from46: BinaryAssociation = BinaryAssociation(
    name="from46",
    ends={
        Property(name="cal_AstActorVariableReference", type=cal_AstConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstConnection47", type=cal_AstActorVariableReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
to48: BinaryAssociation = BinaryAssociation(
    name="to48",
    ends={
        Property(name="cal_AstActorVariableReference50", type=cal_AstConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstConnection49", type=cal_AstActorVariableReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attribute51: BinaryAssociation = BinaryAssociation(
    name="attribute51",
    ends={
        Property(name="cal_AstConnectionAttribute", type=cal_AstConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstConnection52", type=cal_AstConnectionAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable53: BinaryAssociation = BinaryAssociation(
    name="variable53",
    ends={
        Property(name="cal_AstActorVariable55", type=cal_AstActorVariableReference, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstActorVariableReference54", type=cal_AstActorVariable, multiplicity=Multiplicity(0, 1))
    }
)
value56: BinaryAssociation = BinaryAssociation(
    name="value56",
    ends={
        Property(name="cal_AstExpression58", type=cal_AstConnectionAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstConnectionAttribute57", type=cal_AstExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value59: BinaryAssociation = BinaryAssociation(
    name="value59",
    ends={
        Property(name="cal_AstExpression61", type=cal_AstVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstVariable60", type=cal_AstExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotations62: BinaryAssociation = BinaryAssociation(
    name="annotations62",
    ends={
        Property(name="cal_AstAnnotation64", type=cal_AstVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstVariable63", type=cal_AstAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type65: BinaryAssociation = BinaryAssociation(
    name="type65",
    ends={
        Property(name="cal_AstType", type=cal_AstVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstVariable66", type=cal_AstType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dimensions67: BinaryAssociation = BinaryAssociation(
    name="dimensions67",
    ends={
        Property(name="cal_AstExpression69", type=cal_AstVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstVariable68", type=cal_AstExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters70: BinaryAssociation = BinaryAssociation(
    name="parameters70",
    ends={
        Property(name="cal_AstTypeDefinitionParameter", type=cal_AstTypeName, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstTypeName71", type=cal_AstTypeDefinitionParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constructor72: BinaryAssociation = BinaryAssociation(
    name="constructor72",
    ends={
        Property(name="cal_AstFunction74", type=cal_AstTypeName, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstTypeName73", type=cal_AstFunction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type75: BinaryAssociation = BinaryAssociation(
    name="type75",
    ends={
        Property(name="cal_AstType77", type=cal_AstTypeName, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstTypeName76", type=cal_AstType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value78: BinaryAssociation = BinaryAssociation(
    name="value78",
    ends={
        Property(name="cal_AstVariable80", type=cal_AstTypeDefinitionParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstTypeDefinitionParameter79", type=cal_AstVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type81: BinaryAssociation = BinaryAssociation(
    name="type81",
    ends={
        Property(name="cal_AstTypeName83", type=cal_AstTypeDefinitionParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstTypeDefinitionParameter82", type=cal_AstTypeName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
members84: BinaryAssociation = BinaryAssociation(
    name="members84",
    ends={
        Property(name="cal_AstVariable86", type=cal_AstFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstFunction85", type=cal_AstVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotations87: BinaryAssociation = BinaryAssociation(
    name="annotations87",
    ends={
        Property(name="cal_AstAnnotation89", type=cal_AstFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstFunction88", type=cal_AstAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters90: BinaryAssociation = BinaryAssociation(
    name="parameters90",
    ends={
        Property(name="cal_AstVariable92", type=cal_AstFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstFunction91", type=cal_AstVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type93: BinaryAssociation = BinaryAssociation(
    name="type93",
    ends={
        Property(name="cal_AstType95", type=cal_AstFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstFunction94", type=cal_AstType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variables96: BinaryAssociation = BinaryAssociation(
    name="variables96",
    ends={
        Property(name="cal_AstVariable98", type=cal_AstFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstFunction97", type=cal_AstVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression99: BinaryAssociation = BinaryAssociation(
    name="expression99",
    ends={
        Property(name="cal_AstExpression101", type=cal_AstFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstFunction100", type=cal_AstExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
functions102: BinaryAssociation = BinaryAssociation(
    name="functions102",
    ends={
        Property(name="cal_AstFunction103", type=cal_AstActor, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstActor", type=cal_AstFunction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
procedures104: BinaryAssociation = BinaryAssociation(
    name="procedures104",
    ends={
        Property(name="cal_AstProcedure", type=cal_AstActor, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstActor105", type=cal_AstProcedure, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actions106: BinaryAssociation = BinaryAssociation(
    name="actions106",
    ends={
        Property(name="cal_AstAction", type=cal_AstActor, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstActor107", type=cal_AstAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initializes108: BinaryAssociation = BinaryAssociation(
    name="initializes108",
    ends={
        Property(name="cal_AstAction110", type=cal_AstActor, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstActor109", type=cal_AstAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stateVariables111: BinaryAssociation = BinaryAssociation(
    name="stateVariables111",
    ends={
        Property(name="cal_AstVariable113", type=cal_AstActor, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstActor112", type=cal_AstVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
schedules114: BinaryAssociation = BinaryAssociation(
    name="schedules114",
    ends={
        Property(name="cal_AstSchedule", type=cal_AstActor, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstActor115", type=cal_AstSchedule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
priorities116: BinaryAssociation = BinaryAssociation(
    name="priorities116",
    ends={
        Property(name="cal_AstPriority", type=cal_AstActor, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstActor117", type=cal_AstPriority, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotations118: BinaryAssociation = BinaryAssociation(
    name="annotations118",
    ends={
        Property(name="cal_AstAnnotation120", type=cal_AstPort, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstPort119", type=cal_AstAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type121: BinaryAssociation = BinaryAssociation(
    name="type121",
    ends={
        Property(name="cal_AstType123", type=cal_AstPort, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstPort122", type=cal_AstType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotations124: BinaryAssociation = BinaryAssociation(
    name="annotations124",
    ends={
        Property(name="cal_AstAnnotation126", type=cal_AstProcedure, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstProcedure125", type=cal_AstAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters127: BinaryAssociation = BinaryAssociation(
    name="parameters127",
    ends={
        Property(name="cal_AstVariable129", type=cal_AstProcedure, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstProcedure128", type=cal_AstVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variables130: BinaryAssociation = BinaryAssociation(
    name="variables130",
    ends={
        Property(name="cal_AstVariable132", type=cal_AstProcedure, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstProcedure131", type=cal_AstVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements133: BinaryAssociation = BinaryAssociation(
    name="statements133",
    ends={
        Property(name="cal_AstStatement", type=cal_AstProcedure, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstProcedure134", type=cal_AstStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tags135: BinaryAssociation = BinaryAssociation(
    name="tags135",
    ends={
        Property(name="cal_AstTag", type=cal_AstInequality, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstInequality", type=cal_AstTag, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inequalities136: BinaryAssociation = BinaryAssociation(
    name="inequalities136",
    ends={
        Property(name="cal_AstInequality138", type=cal_AstPriority, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstPriority137", type=cal_AstInequality, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialState139: BinaryAssociation = BinaryAssociation(
    name="initialState139",
    ends={
        Property(name="cal_AstState", type=cal_AstSchedule, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstSchedule140", type=cal_AstState, multiplicity=Multiplicity(0, 1))
    }
)
transitions141: BinaryAssociation = BinaryAssociation(
    name="transitions141",
    ends={
        Property(name="cal_AstTransition", type=cal_AstSchedule, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstSchedule142", type=cal_AstTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source143: BinaryAssociation = BinaryAssociation(
    name="source143",
    ends={
        Property(name="cal_AstState145", type=cal_AstTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstTransition144", type=cal_AstState, multiplicity=Multiplicity(0, 1))
    }
)
tags146: BinaryAssociation = BinaryAssociation(
    name="tags146",
    ends={
        Property(name="cal_AstTag148", type=cal_AstTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstTransition147", type=cal_AstTag, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target149: BinaryAssociation = BinaryAssociation(
    name="target149",
    ends={
        Property(name="cal_AstState151", type=cal_AstTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstTransition150", type=cal_AstState, multiplicity=Multiplicity(0, 1))
    }
)
annotations152: BinaryAssociation = BinaryAssociation(
    name="annotations152",
    ends={
        Property(name="cal_AstAnnotation154", type=cal_AstAction, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstAction153", type=cal_AstAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tag155: BinaryAssociation = BinaryAssociation(
    name="tag155",
    ends={
        Property(name="cal_AstTag157", type=cal_AstAction, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstAction156", type=cal_AstTag, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inputs158: BinaryAssociation = BinaryAssociation(
    name="inputs158",
    ends={
        Property(name="cal_AstInputPattern", type=cal_AstAction, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstAction159", type=cal_AstInputPattern, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputs160: BinaryAssociation = BinaryAssociation(
    name="outputs160",
    ends={
        Property(name="cal_AstOutputPattern", type=cal_AstAction, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstAction161", type=cal_AstOutputPattern, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
guards162: BinaryAssociation = BinaryAssociation(
    name="guards162",
    ends={
        Property(name="cal_AstExpression164", type=cal_AstAction, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstAction163", type=cal_AstExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variables165: BinaryAssociation = BinaryAssociation(
    name="variables165",
    ends={
        Property(name="cal_AstVariable167", type=cal_AstAction, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstAction166", type=cal_AstVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements168: BinaryAssociation = BinaryAssociation(
    name="statements168",
    ends={
        Property(name="cal_AstStatement170", type=cal_AstAction, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstAction169", type=cal_AstStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
port171: BinaryAssociation = BinaryAssociation(
    name="port171",
    ends={
        Property(name="cal_AstPort173", type=cal_AstInputPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstInputPattern172", type=cal_AstPort, multiplicity=Multiplicity(0, 1))
    }
)
tokens174: BinaryAssociation = BinaryAssociation(
    name="tokens174",
    ends={
        Property(name="cal_AstVariable176", type=cal_AstInputPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstInputPattern175", type=cal_AstVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
repeat177: BinaryAssociation = BinaryAssociation(
    name="repeat177",
    ends={
        Property(name="cal_AstExpression179", type=cal_AstInputPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstInputPattern178", type=cal_AstExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
port180: BinaryAssociation = BinaryAssociation(
    name="port180",
    ends={
        Property(name="cal_AstPort182", type=cal_AstOutputPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstOutputPattern181", type=cal_AstPort, multiplicity=Multiplicity(0, 1))
    }
)
values183: BinaryAssociation = BinaryAssociation(
    name="values183",
    ends={
        Property(name="cal_AstExpression185", type=cal_AstOutputPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstOutputPattern184", type=cal_AstExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target189: BinaryAssociation = BinaryAssociation(
    name="target189",
    ends={
        Property(name="cal_AstVariableReference", type=cal_AstStatementAssign, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstStatementAssign", type=cal_AstVariableReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
indexes190: BinaryAssociation = BinaryAssociation(
    name="indexes190",
    ends={
        Property(name="cal_AstExpression192", type=cal_AstStatementAssign, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstStatementAssign191", type=cal_AstExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
member193: BinaryAssociation = BinaryAssociation(
    name="member193",
    ends={
        Property(name="cal_AstMemberAccess", type=cal_AstStatementAssign, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstStatementAssign194", type=cal_AstMemberAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value195: BinaryAssociation = BinaryAssociation(
    name="value195",
    ends={
        Property(name="cal_AstExpression197", type=cal_AstStatementAssign, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstStatementAssign196", type=cal_AstExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
procedure198: BinaryAssociation = BinaryAssociation(
    name="procedure198",
    ends={
        Property(name="cal_AstProcedure199", type=cal_AstStatementCall, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstStatementCall", type=cal_AstProcedure, multiplicity=Multiplicity(0, 1))
    }
)
parameters200: BinaryAssociation = BinaryAssociation(
    name="parameters200",
    ends={
        Property(name="cal_AstExpression202", type=cal_AstStatementCall, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstStatementCall201", type=cal_AstExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
generators203: BinaryAssociation = BinaryAssociation(
    name="generators203",
    ends={
        Property(name="cal_AstForeachGenerator", type=cal_AstStatementForeach, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstStatementForeach", type=cal_AstForeachGenerator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variables204: BinaryAssociation = BinaryAssociation(
    name="variables204",
    ends={
        Property(name="cal_AstVariable206", type=cal_AstStatementForeach, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstStatementForeach205", type=cal_AstVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements207: BinaryAssociation = BinaryAssociation(
    name="statements207",
    ends={
        Property(name="cal_AstStatement209", type=cal_AstStatementForeach, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstStatementForeach208", type=cal_AstStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable210: BinaryAssociation = BinaryAssociation(
    name="variable210",
    ends={
        Property(name="cal_AstVariable212", type=cal_AstForeachGenerator, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstForeachGenerator211", type=cal_AstVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression213: BinaryAssociation = BinaryAssociation(
    name="expression213",
    ends={
        Property(name="cal_AstExpression215", type=cal_AstForeachGenerator, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstForeachGenerator214", type=cal_AstExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variables216: BinaryAssociation = BinaryAssociation(
    name="variables216",
    ends={
        Property(name="cal_AstVariable217", type=cal_AstStatementBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstStatementBlock", type=cal_AstVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements218: BinaryAssociation = BinaryAssociation(
    name="statements218",
    ends={
        Property(name="cal_AstStatement220", type=cal_AstStatementBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstStatementBlock219", type=cal_AstStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition221: BinaryAssociation = BinaryAssociation(
    name="condition221",
    ends={
        Property(name="cal_AstExpression222", type=cal_AstStatementIf, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstStatementIf", type=cal_AstExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition229: BinaryAssociation = BinaryAssociation(
    name="condition229",
    ends={
        Property(name="cal_AstExpression230", type=cal_AstStatementWhile, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstStatementWhile", type=cal_AstExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
repeat186: BinaryAssociation = BinaryAssociation(
    name="repeat186",
    ends={
        Property(name="cal_AstExpression188", type=cal_AstOutputPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstOutputPattern187", type=cal_AstExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements231: BinaryAssociation = BinaryAssociation(
    name="statements231",
    ends={
        Property(name="cal_AstStatement233", type=cal_AstStatementWhile, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstStatementWhile232", type=cal_AstStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
function234: BinaryAssociation = BinaryAssociation(
    name="function234",
    ends={
        Property(name="cal_AstFunction235", type=cal_AstExpressionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstExpressionCall", type=cal_AstFunction, multiplicity=Multiplicity(0, 1))
    }
)
parameters236: BinaryAssociation = BinaryAssociation(
    name="parameters236",
    ends={
        Property(name="cal_AstExpression238", type=cal_AstExpressionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstExpressionCall237", type=cal_AstExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition239: BinaryAssociation = BinaryAssociation(
    name="condition239",
    ends={
        Property(name="cal_AstExpression240", type=cal_AstExpressionIf, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstExpressionIf", type=cal_AstExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
then241: BinaryAssociation = BinaryAssociation(
    name="then241",
    ends={
        Property(name="cal_AstExpression243", type=cal_AstExpressionIf, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstExpressionIf242", type=cal_AstExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
else244: BinaryAssociation = BinaryAssociation(
    name="else244",
    ends={
        Property(name="cal_AstExpression246", type=cal_AstExpressionIf, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstExpressionIf245", type=cal_AstExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
then223: BinaryAssociation = BinaryAssociation(
    name="then223",
    ends={
        Property(name="cal_AstStatement225", type=cal_AstStatementIf, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstStatementIf224", type=cal_AstStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
else226: BinaryAssociation = BinaryAssociation(
    name="else226",
    ends={
        Property(name="cal_AstStatement228", type=cal_AstStatementIf, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstStatementIf227", type=cal_AstStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable251: BinaryAssociation = BinaryAssociation(
    name="variable251",
    ends={
        Property(name="cal_AstVariable253", type=cal_AstGenerator, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstGenerator252", type=cal_AstVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression254: BinaryAssociation = BinaryAssociation(
    name="expression254",
    ends={
        Property(name="cal_AstExpression256", type=cal_AstGenerator, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstGenerator255", type=cal_AstExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value257: BinaryAssociation = BinaryAssociation(
    name="value257",
    ends={
        Property(name="cal_AstVariableReference258", type=cal_AstExpressionVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstExpressionVariable", type=cal_AstVariableReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
indexes259: BinaryAssociation = BinaryAssociation(
    name="indexes259",
    ends={
        Property(name="cal_AstExpression261", type=cal_AstExpressionVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstExpressionVariable260", type=cal_AstExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
member262: BinaryAssociation = BinaryAssociation(
    name="member262",
    ends={
        Property(name="cal_AstMemberAccess264", type=cal_AstExpressionVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstExpressionVariable263", type=cal_AstMemberAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeParams265: BinaryAssociation = BinaryAssociation(
    name="typeParams265",
    ends={
        Property(name="cal_AstTypeParameterList", type=cal_AstType, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstType266", type=cal_AstTypeParameterList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dimensions267: BinaryAssociation = BinaryAssociation(
    name="dimensions267",
    ends={
        Property(name="cal_AstExpression269", type=cal_AstType, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstType268", type=cal_AstExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name270: BinaryAssociation = BinaryAssociation(
    name="name270",
    ends={
        Property(name="cal_AstTypeName272", type=cal_AstType, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstType271", type=cal_AstTypeName, multiplicity=Multiplicity(0, 1))
    }
)
domain274: BinaryAssociation = BinaryAssociation(
    name="domain274",
    ends={
        Property(name="cal_AstType275", type=cal_AstType, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstType273", type=cal_AstType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
codomain277: BinaryAssociation = BinaryAssociation(
    name="codomain277",
    ends={
        Property(name="cal_AstType278", type=cal_AstType, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstType276", type=cal_AstType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
members279: BinaryAssociation = BinaryAssociation(
    name="members279",
    ends={
        Property(name="cal_AstVariable281", type=cal_AstType, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstType280", type=cal_AstVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expressions247: BinaryAssociation = BinaryAssociation(
    name="expressions247",
    ends={
        Property(name="cal_AstExpression248", type=cal_AstExpressionList, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstExpressionList", type=cal_AstExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
generators249: BinaryAssociation = BinaryAssociation(
    name="generators249",
    ends={
        Property(name="cal_AstGenerator", type=cal_AstExpressionList, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstExpressionList250", type=cal_AstGenerator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value284: BinaryAssociation = BinaryAssociation(
    name="value284",
    ends={
        Property(name="cal_AstExpression286", type=cal_AstTypeParam, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstTypeParam285", type=cal_AstExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type287: BinaryAssociation = BinaryAssociation(
    name="type287",
    ends={
        Property(name="cal_AstType289", type=cal_AstTypeParam, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstTypeParam288", type=cal_AstType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable290: BinaryAssociation = BinaryAssociation(
    name="variable290",
    ends={
        Property(name="cal_AstVariable292", type=cal_AstVariableReference, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstVariableReference291", type=cal_AstVariable, multiplicity=Multiplicity(0, 1))
    }
)
memberIndex293: BinaryAssociation = BinaryAssociation(
    name="memberIndex293",
    ends={
        Property(name="cal_AstExpression295", type=cal_AstMemberAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstMemberAccess294", type=cal_AstExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arguments296: BinaryAssociation = BinaryAssociation(
    name="arguments296",
    ends={
        Property(name="cal_AstAnnotationArgument", type=cal_AstAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstAnnotation297", type=cal_AstAnnotationArgument, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
left298: BinaryAssociation = BinaryAssociation(
    name="left298",
    ends={
        Property(name="cal_AstExpression299", type=cal_AstExpressionBinary, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstExpressionBinary", type=cal_AstExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right300: BinaryAssociation = BinaryAssociation(
    name="right300",
    ends={
        Property(name="cal_AstExpression302", type=cal_AstExpressionBinary, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstExpressionBinary301", type=cal_AstExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression303: BinaryAssociation = BinaryAssociation(
    name="expression303",
    ends={
        Property(name="cal_AstExpression304", type=cal_AstExpressionUnary, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstExpressionUnary", type=cal_AstExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
params282: BinaryAssociation = BinaryAssociation(
    name="params282",
    ends={
        Property(name="cal_AstTypeParam", type=cal_AstTypeParameterList, multiplicity=Multiplicity(1, 1)),
        Property(name="cal_AstTypeParameterList283", type=cal_AstTypeParam, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_cal_AstPackage_AstTop = Generalization(general=AstTop, specific=cal_AstPackage)
gen_cal_AstNamespace_AstTop = Generalization(general=AstTop, specific=cal_AstNamespace)
gen_cal_AstNamespace_AstPackage = Generalization(general=AstPackage, specific=cal_AstNamespace)
gen_cal_AstNamespace_AstUnit = Generalization(general=AstUnit, specific=cal_AstNamespace)
gen_cal_AstNetwork_AstAbstractActor = Generalization(general=AstAbstractActor, specific=cal_AstNetwork)
gen_cal_AstFunction_AstExternalFunction = Generalization(general=AstExternalFunction, specific=cal_AstFunction)
gen_cal_AstActor_AstAbstractActor = Generalization(general=AstAbstractActor, specific=cal_AstActor)
gen_cal_AstProcedure_AstExternalProcedure = Generalization(general=AstExternalProcedure, specific=cal_AstProcedure)
gen_cal_AstExternalActor_AstAbstractActor = Generalization(general=AstAbstractActor, specific=cal_AstExternalActor)
gen_cal_AstStatementAssign_AstStatement = Generalization(general=AstStatement, specific=cal_AstStatementAssign)
gen_cal_AstStatementCall_AstStatement = Generalization(general=AstStatement, specific=cal_AstStatementCall)
gen_cal_AstStatementForeach_AstStatement = Generalization(general=AstStatement, specific=cal_AstStatementForeach)
gen_cal_AstStatementBlock_AstStatement = Generalization(general=AstStatement, specific=cal_AstStatementBlock)
gen_cal_AstStatementIf_AstStatement = Generalization(general=AstStatement, specific=cal_AstStatementIf)
gen_cal_AstStatementWhile_AstStatement = Generalization(general=AstStatement, specific=cal_AstStatementWhile)
gen_cal_AstExpressionCall_AstExpression = Generalization(general=AstExpression, specific=cal_AstExpressionCall)
gen_cal_AstExpressionIf_AstExpression = Generalization(general=AstExpression, specific=cal_AstExpressionIf)
gen_cal_AstExpressionList_AstExpression = Generalization(general=AstExpression, specific=cal_AstExpressionList)
gen_cal_AstExpressionVariable_AstExpression = Generalization(general=AstExpression, specific=cal_AstExpressionVariable)
gen_cal_AstExpressionLiteral_AstExpression = Generalization(general=AstExpression, specific=cal_AstExpressionLiteral)
gen_cal_AstExpressionBoolean_AstExpressionLiteral = Generalization(general=AstExpressionLiteral, specific=cal_AstExpressionBoolean)
gen_cal_AstExpressionFloat_AstExpressionLiteral = Generalization(general=AstExpressionLiteral, specific=cal_AstExpressionFloat)
gen_cal_AstExpressionInteger_AstExpressionLiteral = Generalization(general=AstExpressionLiteral, specific=cal_AstExpressionInteger)
gen_cal_AstExpressionString_AstExpressionLiteral = Generalization(general=AstExpressionLiteral, specific=cal_AstExpressionString)
gen_cal_AstInitialize_AstAction = Generalization(general=AstAction, specific=cal_AstInitialize)
gen_cal_AstExpressionBinary_AstExpression = Generalization(general=AstExpression, specific=cal_AstExpressionBinary)
gen_cal_AstExpressionUnary_AstExpression = Generalization(general=AstExpression, specific=cal_AstExpressionUnary)

# Domain Model
domain_model = DomainModel(
    name="cal",
    types={cal_AstTop, cal_AstPackage, AstTop, cal_AstUnit, cal_AstNamespace, AstPackage, AstUnit, cal_AstEntity, cal_Import, cal_AstFunction, cal_EObject, cal_AstAnnotation, cal_AstTypeName, cal_AstAbstractActor, cal_AstPort, cal_AstVariable, cal_AstNetwork, AstAbstractActor, cal_AstActorVariable, cal_AstStructure, cal_AstAssignParameter, cal_AstExpression, cal_AstConnection, cal_AstActorVariableReference, cal_AstConnectionAttribute, cal_AstType, AstExternalFunction, cal_AstTypeDefinitionParameter, cal_AstActor, cal_AstProcedure, cal_AstAction, cal_AstSchedule, cal_AstPriority, cal_AstExternalFunction, AstExternalProcedure, cal_AstStatement, cal_AstExternalProcedure, cal_AstTag, cal_AstExternalActor, cal_AstInequality, cal_AstState, cal_AstTransition, cal_AstInputPattern, cal_AstOutputPattern, cal_AstStatementAssign, AstStatement, cal_AstVariableReference, cal_AstMemberAccess, cal_AstStatementCall, cal_AstStatementForeach, cal_AstForeachGenerator, cal_AstStatementBlock, cal_AstStatementIf, cal_AstStatementWhile, cal_AstExpressionCall, AstExpression, cal_AstExpressionIf, cal_AstExpressionList, cal_AstExpressionVariable, cal_AstExpressionLiteral, cal_AstExpressionBoolean, AstExpressionLiteral, cal_AstExpressionFloat, cal_AstExpressionInteger, cal_AstExpressionString, cal_AstTypeParameterList, cal_AstGenerator, cal_AstAnnotationArgument, cal_AstInitialize, AstAction, cal_AstExpressionBinary, cal_AstExpressionUnary, cal_AstTypeParam},
    associations={entities0, imports1, units3, externals9, annotations11, typedefs13, namespaces16, annotations18, actor21, parameters23, inputs26, functions5, variables7, variables31, instances33, structure35, type37, parameters40, value42, connections44, outputs28, from46, to48, attribute51, variable53, value56, value59, annotations62, type65, dimensions67, parameters70, constructor72, type75, value78, type81, members84, annotations87, parameters90, type93, variables96, expression99, functions102, procedures104, actions106, initializes108, stateVariables111, schedules114, priorities116, annotations118, type121, annotations124, parameters127, variables130, statements133, tags135, inequalities136, initialState139, transitions141, source143, tags146, target149, annotations152, tag155, inputs158, outputs160, guards162, variables165, statements168, port171, tokens174, repeat177, port180, values183, target189, indexes190, member193, value195, procedure198, parameters200, generators203, variables204, statements207, variable210, expression213, variables216, statements218, condition221, condition229, repeat186, statements231, function234, parameters236, condition239, then241, else244, then223, else226, variable251, expression254, value257, indexes259, member262, typeParams265, dimensions267, name270, domain274, codomain277, members279, expressions247, generators249, value284, type287, variable290, memberIndex293, arguments296, left298, right300, expression303, params282},
    generalizations={gen_cal_AstPackage_AstTop, gen_cal_AstNamespace_AstTop, gen_cal_AstNamespace_AstPackage, gen_cal_AstNamespace_AstUnit, gen_cal_AstNetwork_AstAbstractActor, gen_cal_AstFunction_AstExternalFunction, gen_cal_AstActor_AstAbstractActor, gen_cal_AstProcedure_AstExternalProcedure, gen_cal_AstExternalActor_AstAbstractActor, gen_cal_AstStatementAssign_AstStatement, gen_cal_AstStatementCall_AstStatement, gen_cal_AstStatementForeach_AstStatement, gen_cal_AstStatementBlock_AstStatement, gen_cal_AstStatementIf_AstStatement, gen_cal_AstStatementWhile_AstStatement, gen_cal_AstExpressionCall_AstExpression, gen_cal_AstExpressionIf_AstExpression, gen_cal_AstExpressionList_AstExpression, gen_cal_AstExpressionVariable_AstExpression, gen_cal_AstExpressionLiteral_AstExpression, gen_cal_AstExpressionBoolean_AstExpressionLiteral, gen_cal_AstExpressionFloat_AstExpressionLiteral, gen_cal_AstExpressionInteger_AstExpressionLiteral, gen_cal_AstExpressionString_AstExpressionLiteral, gen_cal_AstInitialize_AstAction, gen_cal_AstExpressionBinary_AstExpression, gen_cal_AstExpressionUnary_AstExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)