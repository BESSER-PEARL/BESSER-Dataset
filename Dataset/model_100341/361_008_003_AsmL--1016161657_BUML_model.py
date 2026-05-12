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
AsmL_LocatedElement = Class(name="AsmL_LocatedElement", is_abstract=True)
AsmL_Body = Class(name="AsmL_Body")
LocatedElement = Class(name="LocatedElement")
Rule = Class(name="Rule")
AsmL_InWhereHolds = Class(name="AsmL_InWhereHolds")
Term = Class(name="Term")
AsmL_AsmLFile = Class(name="AsmL_AsmLFile")
AsmLElement = Class(name="AsmLElement")
Main = Class(name="Main")
AsmL_AsmLElement = Class(name="AsmL_AsmLElement", is_abstract=True)
AsmLFile = Class(name="AsmLFile")
AsmL_VarDeclaration = Class(name="AsmL_VarDeclaration")
VarOrCase = Class(name="VarOrCase")
VarOrMethod = Class(name="VarOrMethod")
Type = Class(name="Type")
AsmL_Namespace = Class(name="AsmL_Namespace")
AsmL_Structure = Class(name="AsmL_Structure")
AsmL_Case = Class(name="AsmL_Case")
VarDeclaration = Class(name="VarDeclaration")
AsmL_Class = Class(name="AsmL_Class")
AsmL_VarOrCase = Class(name="AsmL_VarOrCase", is_abstract=True)
Structure = Class(name="Structure")
AsmL_Enumeration = Class(name="AsmL_Enumeration")
Enumerator = Class(name="Enumerator")
AsmL_Enumerator = Class(name="AsmL_Enumerator")
AsmL_Function = Class(name="AsmL_Function", is_abstract=True)
AsmL_VarOrMethod = Class(name="AsmL_VarOrMethod")
Class_ = Class(name="Class")
AsmL_Method = Class(name="AsmL_Method")
Function = Class(name="Function")
Parameter_ = Class(name="Parameter")
AsmL_Parameter = Class(name="AsmL_Parameter")
Body = Class(name="Body")
AsmL_Main = Class(name="AsmL_Main")
Initially = Class(name="Initially")
AsmL_Initially = Class(name="AsmL_Initially")
VarTerm = Class(name="VarTerm")
AsmL_Rule = Class(name="AsmL_Rule", is_abstract=True)
Method_ = Class(name="Method")
AsmL_SkipRule = Class(name="AsmL_SkipRule")
AsmL_Step = Class(name="AsmL_Step", is_abstract=True)
AsmL_StepUntilFixPoint = Class(name="AsmL_StepUntilFixPoint")
Step = Class(name="Step")
AsmL_StepExpression = Class(name="AsmL_StepExpression", is_abstract=True)
AsmL_StepWhile = Class(name="AsmL_StepWhile")
StepExpression = Class(name="StepExpression")
AsmL_StepUntil = Class(name="AsmL_StepUntil")
AsmL_StepForEach = Class(name="AsmL_StepForEach")
InWhereHolds = Class(name="InWhereHolds")
MethodCallTerm = Class(name="MethodCallTerm")
AsmL_UpdateRule = Class(name="AsmL_UpdateRule", is_abstract=True)
AsmL_UpdateVarRule = Class(name="AsmL_UpdateVarRule")
UpdateRule = Class(name="UpdateRule")
AsmL_UpdateFieldRule = Class(name="AsmL_UpdateFieldRule")
AsmL_MethodInvocation = Class(name="AsmL_MethodInvocation")
AsmL_ChooseRule = Class(name="AsmL_ChooseRule")
AsmL_ForallRule = Class(name="AsmL_ForallRule")
AsmL_UpdateMapRule = Class(name="AsmL_UpdateMapRule")
AsmL_ConditionalRule = Class(name="AsmL_ConditionalRule")
ElseIf = Class(name="ElseIf")
AsmL_ElseIf = Class(name="AsmL_ElseIf")
ConditionalRule = Class(name="ConditionalRule")
AsmL_ReturnRule = Class(name="AsmL_ReturnRule")
AsmL_AddRule = Class(name="AsmL_AddRule")
AsmL_RemoveRule = Class(name="AsmL_RemoveRule")
AsmL_Type = Class(name="AsmL_Type", is_abstract=True)
AsmL_NamedType = Class(name="AsmL_NamedType")
AsmL_MapType = Class(name="AsmL_MapType")
AsmL_SetType = Class(name="AsmL_SetType")
AsmL_SequenceType = Class(name="AsmL_SequenceType")
AsmL_Term = Class(name="AsmL_Term", is_abstract=True)
AsmL_VarTerm = Class(name="AsmL_VarTerm")
AsmL_TupletType = Class(name="AsmL_TupletType")
AsmL_MapTerm = Class(name="AsmL_MapTerm")
AsmL_Operator = Class(name="AsmL_Operator")
AsmL_TulpletTerm = Class(name="AsmL_TulpletTerm")
AsmL_MethodCallTerm = Class(name="AsmL_MethodCallTerm")
AsmL_ForAllTerm = Class(name="AsmL_ForAllTerm")
PredicateTerm = Class(name="PredicateTerm")
AsmL_ExistsTerm = Class(name="AsmL_ExistsTerm")
AsmL_AnyIn = Class(name="AsmL_AnyIn")
AsmL_SetTerm = Class(name="AsmL_SetTerm", is_abstract=True)
AsmL_EnumerateSet = Class(name="AsmL_EnumerateSet")
SetTerm = Class(name="SetTerm")
AsmL_NewInstance = Class(name="AsmL_NewInstance")
AsmL_PredicateTerm = Class(name="AsmL_PredicateTerm")
AsmL_AlgorithmSet = Class(name="AsmL_AlgorithmSet")
AsmL_SequenceTerm = Class(name="AsmL_SequenceTerm", is_abstract=True)
AsmL_EnumerateSequence = Class(name="AsmL_EnumerateSequence")
SequenceTerm = Class(name="SequenceTerm")
AsmL_RangeSet = Class(name="AsmL_RangeSet")
AsmL_RangeSequence = Class(name="AsmL_RangeSequence")
AsmL_Constant = Class(name="AsmL_Constant", is_abstract=True)
AsmL_BooleanConstant = Class(name="AsmL_BooleanConstant")
Constant = Class(name="Constant")
AsmL_StringConstant = Class(name="AsmL_StringConstant")
AsmL_NullConstant = Class(name="AsmL_NullConstant")
AsmL_IntegerConstant = Class(name="AsmL_IntegerConstant")

# AsmL_LocatedElement class attributes and methods
AsmL_LocatedElement_commentsAfter: Property = Property(name="commentsAfter", type=StringType)
AsmL_LocatedElement_location: Property = Property(name="location", type=StringType)
AsmL_LocatedElement_commentsBefore: Property = Property(name="commentsBefore", type=StringType)
AsmL_LocatedElement.attributes={AsmL_LocatedElement_location, AsmL_LocatedElement_commentsBefore, AsmL_LocatedElement_commentsAfter}

# AsmL_Body class attributes and methods

# LocatedElement class attributes and methods

# Rule class attributes and methods

# AsmL_InWhereHolds class attributes and methods

# Term class attributes and methods

# AsmL_AsmLFile class attributes and methods

# AsmLElement class attributes and methods

# Main class attributes and methods

# AsmL_AsmLElement class attributes and methods

# AsmLFile class attributes and methods

# AsmL_VarDeclaration class attributes and methods
AsmL_VarDeclaration_isLocal: Property = Property(name="isLocal", type=StringType)
AsmL_VarDeclaration_name: Property = Property(name="name", type=StringType)
AsmL_VarDeclaration_isConstant: Property = Property(name="isConstant", type=StringType)
AsmL_VarDeclaration_isDeclaration: Property = Property(name="isDeclaration", type=StringType)
AsmL_VarDeclaration.attributes={AsmL_VarDeclaration_name, AsmL_VarDeclaration_isConstant, AsmL_VarDeclaration_isDeclaration, AsmL_VarDeclaration_isLocal}

# VarOrCase class attributes and methods

# VarOrMethod class attributes and methods

# Type class attributes and methods

# AsmL_Namespace class attributes and methods
AsmL_Namespace_name: Property = Property(name="name", type=StringType)
AsmL_Namespace.attributes={AsmL_Namespace_name}

# AsmL_Structure class attributes and methods
AsmL_Structure_name: Property = Property(name="name", type=StringType)
AsmL_Structure_superStructureName: Property = Property(name="superStructureName", type=StringType)
AsmL_Structure.attributes={AsmL_Structure_superStructureName, AsmL_Structure_name}

# AsmL_Case class attributes and methods
AsmL_Case_name: Property = Property(name="name", type=StringType)
AsmL_Case.attributes={AsmL_Case_name}

# VarDeclaration class attributes and methods

# AsmL_Class class attributes and methods
AsmL_Class_name: Property = Property(name="name", type=StringType)
AsmL_Class_isAbstract: Property = Property(name="isAbstract", type=StringType)
AsmL_Class_superClassName: Property = Property(name="superClassName", type=StringType)
AsmL_Class.attributes={AsmL_Class_isAbstract, AsmL_Class_name, AsmL_Class_superClassName}

# AsmL_VarOrCase class attributes and methods

# Structure class attributes and methods

# AsmL_Enumeration class attributes and methods
AsmL_Enumeration_name: Property = Property(name="name", type=StringType)
AsmL_Enumeration.attributes={AsmL_Enumeration_name}

# Enumerator class attributes and methods

# AsmL_Enumerator class attributes and methods
AsmL_Enumerator_name: Property = Property(name="name", type=StringType)
AsmL_Enumerator.attributes={AsmL_Enumerator_name}

# AsmL_Function class attributes and methods
AsmL_Function_name: Property = Property(name="name", type=StringType)
AsmL_Function.attributes={AsmL_Function_name}

# AsmL_VarOrMethod class attributes and methods

# Class class attributes and methods

# AsmL_Method class attributes and methods
AsmL_Method_isAbstract: Property = Property(name="isAbstract", type=StringType)
AsmL_Method_isShared: Property = Property(name="isShared", type=StringType)
AsmL_Method_isEntryPoint: Property = Property(name="isEntryPoint", type=StringType)
AsmL_Method_isOverride: Property = Property(name="isOverride", type=StringType)
AsmL_Method.attributes={AsmL_Method_isEntryPoint, AsmL_Method_isShared, AsmL_Method_isOverride, AsmL_Method_isAbstract}

# Function class attributes and methods

# Parameter class attributes and methods

# AsmL_Parameter class attributes and methods
AsmL_Parameter_name: Property = Property(name="name", type=StringType)
AsmL_Parameter.attributes={AsmL_Parameter_name}

# Body class attributes and methods

# AsmL_Main class attributes and methods

# Initially class attributes and methods

# AsmL_Initially class attributes and methods

# VarTerm class attributes and methods

# AsmL_Rule class attributes and methods

# Method class attributes and methods

# AsmL_SkipRule class attributes and methods

# AsmL_Step class attributes and methods
AsmL_Step_name: Property = Property(name="name", type=StringType)
AsmL_Step.attributes={AsmL_Step_name}

# AsmL_StepUntilFixPoint class attributes and methods

# Step class attributes and methods

# AsmL_StepExpression class attributes and methods

# AsmL_StepWhile class attributes and methods

# StepExpression class attributes and methods

# AsmL_StepUntil class attributes and methods

# AsmL_StepForEach class attributes and methods

# InWhereHolds class attributes and methods

# MethodCallTerm class attributes and methods

# AsmL_UpdateRule class attributes and methods

# AsmL_UpdateVarRule class attributes and methods

# UpdateRule class attributes and methods

# AsmL_UpdateFieldRule class attributes and methods

# AsmL_MethodInvocation class attributes and methods

# AsmL_ChooseRule class attributes and methods

# AsmL_ForallRule class attributes and methods

# AsmL_UpdateMapRule class attributes and methods

# AsmL_ConditionalRule class attributes and methods

# ElseIf class attributes and methods

# AsmL_ElseIf class attributes and methods

# ConditionalRule class attributes and methods

# AsmL_ReturnRule class attributes and methods

# AsmL_AddRule class attributes and methods

# AsmL_RemoveRule class attributes and methods

# AsmL_Type class attributes and methods
AsmL_Type_withNull: Property = Property(name="withNull", type=StringType)
AsmL_Type.attributes={AsmL_Type_withNull}

# AsmL_NamedType class attributes and methods
AsmL_NamedType_name: Property = Property(name="name", type=StringType)
AsmL_NamedType.attributes={AsmL_NamedType_name}

# AsmL_MapType class attributes and methods

# AsmL_SetType class attributes and methods

# AsmL_SequenceType class attributes and methods

# AsmL_Term class attributes and methods

# AsmL_VarTerm class attributes and methods
AsmL_VarTerm_name: Property = Property(name="name", type=StringType)
AsmL_VarTerm.attributes={AsmL_VarTerm_name}

# AsmL_TupletType class attributes and methods

# AsmL_MapTerm class attributes and methods
AsmL_MapTerm_separator: Property = Property(name="separator", type=StringType)
AsmL_MapTerm.attributes={AsmL_MapTerm_separator}

# AsmL_Operator class attributes and methods
AsmL_Operator_opName: Property = Property(name="opName", type=StringType)
AsmL_Operator.attributes={AsmL_Operator_opName}

# AsmL_TulpletTerm class attributes and methods

# AsmL_MethodCallTerm class attributes and methods
AsmL_MethodCallTerm_name: Property = Property(name="name", type=StringType)
AsmL_MethodCallTerm.attributes={AsmL_MethodCallTerm_name}

# AsmL_ForAllTerm class attributes and methods

# PredicateTerm class attributes and methods

# AsmL_ExistsTerm class attributes and methods
AsmL_ExistsTerm_isUnique: Property = Property(name="isUnique", type=StringType)
AsmL_ExistsTerm.attributes={AsmL_ExistsTerm_isUnique}

# AsmL_AnyIn class attributes and methods

# AsmL_SetTerm class attributes and methods

# AsmL_EnumerateSet class attributes and methods

# SetTerm class attributes and methods

# AsmL_NewInstance class attributes and methods

# AsmL_PredicateTerm class attributes and methods

# AsmL_AlgorithmSet class attributes and methods

# AsmL_SequenceTerm class attributes and methods

# AsmL_EnumerateSequence class attributes and methods

# SequenceTerm class attributes and methods

# AsmL_RangeSet class attributes and methods

# AsmL_RangeSequence class attributes and methods

# AsmL_Constant class attributes and methods

# AsmL_BooleanConstant class attributes and methods
AsmL_BooleanConstant_val: Property = Property(name="val", type=StringType)
AsmL_BooleanConstant.attributes={AsmL_BooleanConstant_val}

# Constant class attributes and methods

# AsmL_StringConstant class attributes and methods
AsmL_StringConstant_val: Property = Property(name="val", type=StringType)
AsmL_StringConstant.attributes={AsmL_StringConstant_val}

# AsmL_NullConstant class attributes and methods

# AsmL_IntegerConstant class attributes and methods
AsmL_IntegerConstant_val: Property = Property(name="val", type=StringType)
AsmL_IntegerConstant.attributes={AsmL_IntegerConstant_val}

# Relationships
rules0: BinaryAssociation = BinaryAssociation(
    name="rules0",
    ends={
        Property(name="Rule", type=AsmL_Body, multiplicity=Multiplicity(1, 1)),
        Property(name="ownerBody", type=Rule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
var1: BinaryAssociation = BinaryAssociation(
    name="var1",
    ends={
        Property(name="Term", type=AsmL_InWhereHolds, multiplicity=Multiplicity(1, 1)),
        Property(name="AsmL_InWhereHolds", type=Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
in_2: BinaryAssociation = BinaryAssociation(
    name="in_2",
    ends={
        Property(name="Term4", type=AsmL_InWhereHolds, multiplicity=Multiplicity(1, 1)),
        Property(name="AsmL_InWhereHolds3", type=Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
holds8: BinaryAssociation = BinaryAssociation(
    name="holds8",
    ends={
        Property(name="AsmL_InWhereHolds9", type=Term, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="Term10", type=AsmL_InWhereHolds, multiplicity=Multiplicity(1, 1))
    }
)
elements11: BinaryAssociation = BinaryAssociation(
    name="elements11",
    ends={
        Property(name="AsmLElement", type=AsmL_AsmLFile, multiplicity=Multiplicity(1, 1)),
        Property(name="file", type=AsmLElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
main12: BinaryAssociation = BinaryAssociation(
    name="main12",
    ends={
        Property(name="Main", type=AsmL_AsmLFile, multiplicity=Multiplicity(1, 1)),
        Property(name="mainFile", type=Main, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
file13: BinaryAssociation = BinaryAssociation(
    name="file13",
    ends={
        Property(name="AsmLFile", type=AsmL_AsmLElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements", type=AsmLFile, multiplicity=Multiplicity(1, 1))
    }
)
where5: BinaryAssociation = BinaryAssociation(
    name="where5",
    ends={
        Property(name="Term7", type=AsmL_InWhereHolds, multiplicity=Multiplicity(1, 1)),
        Property(name="AsmL_InWhereHolds6", type=Term, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type14: BinaryAssociation = BinaryAssociation(
    name="type14",
    ends={
        Property(name="Type", type=AsmL_VarDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ownerDeclaration", type=Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
varOrCase15: BinaryAssociation = BinaryAssociation(
    name="varOrCase15",
    ends={
        Property(name="VarOrCase", type=AsmL_Structure, multiplicity=Multiplicity(1, 1)),
        Property(name="ownerStructure", type=VarOrCase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownerStructure16: BinaryAssociation = BinaryAssociation(
    name="ownerStructure16",
    ends={
        Property(name="varOrCase", type=Structure, multiplicity=Multiplicity(1, 1)),
        Property(name="Structure", type=AsmL_VarOrCase, multiplicity=Multiplicity(1, 1))
    }
)
variables17: BinaryAssociation = BinaryAssociation(
    name="variables17",
    ends={
        Property(name="VarDeclaration", type=AsmL_Case, multiplicity=Multiplicity(1, 1)),
        Property(name="AsmL_Case", type=VarDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
varOrMethod18: BinaryAssociation = BinaryAssociation(
    name="varOrMethod18",
    ends={
        Property(name="VarOrMethod", type=AsmL_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="ownerClass", type=VarOrMethod, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownerClass19: BinaryAssociation = BinaryAssociation(
    name="ownerClass19",
    ends={
        Property(name="Class", type=AsmL_VarOrMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="varOrMethod", type=Class_, multiplicity=Multiplicity(1, 1))
    }
)
enumerators20: BinaryAssociation = BinaryAssociation(
    name="enumerators20",
    ends={
        Property(name="Enumerator", type=AsmL_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="AsmL_Enumeration", type=Enumerator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value21: BinaryAssociation = BinaryAssociation(
    name="value21",
    ends={
        Property(name="Term22", type=AsmL_Enumerator, multiplicity=Multiplicity(1, 1)),
        Property(name="AsmL_Enumerator", type=Term, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnType24: BinaryAssociation = BinaryAssociation(
    name="returnType24",
    ends={
        Property(name="Type25", type=AsmL_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="ownerMethod", type=Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters26: BinaryAssociation = BinaryAssociation(
    name="parameters26",
    ends={
        Property(name="Parameter", type=AsmL_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="ownerMethod27", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type28: BinaryAssociation = BinaryAssociation(
    name="type28",
    ends={
        Property(name="Type29", type=AsmL_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ownerParameter", type=Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body23: BinaryAssociation = BinaryAssociation(
    name="body23",
    ends={
        Property(name="Body", type=AsmL_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="AsmL_Function", type=Body, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ownerMethod30: BinaryAssociation = BinaryAssociation(
    name="ownerMethod30",
    ends={
        Property(name="Method", type=AsmL_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters", type=Method_, multiplicity=Multiplicity(1, 1))
    }
)
mainFile31: BinaryAssociation = BinaryAssociation(
    name="mainFile31",
    ends={
        Property(name="AsmLFile32", type=AsmL_Main, multiplicity=Multiplicity(1, 1)),
        Property(name="main", type=AsmLFile, multiplicity=Multiplicity(1, 1))
    }
)
initialisations33: BinaryAssociation = BinaryAssociation(
    name="initialisations33",
    ends={
        Property(name="Initially", type=AsmL_Main, multiplicity=Multiplicity(1, 1)),
        Property(name="AsmL_Main", type=Initially, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
id34: BinaryAssociation = BinaryAssociation(
    name="id34",
    ends={
        Property(name="VarTerm", type=AsmL_Initially, multiplicity=Multiplicity(1, 1)),
        Property(name="AsmL_Initially", type=VarTerm, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
val35: BinaryAssociation = BinaryAssociation(
    name="val35",
    ends={
        Property(name="Term37", type=AsmL_Initially, multiplicity=Multiplicity(1, 1)),
        Property(name="AsmL_Initially36", type=Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression40: BinaryAssociation = BinaryAssociation(
    name="expression40",
    ends={
        Property(name="Term41", type=AsmL_StepExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="AsmL_StepExpression", type=Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ownerBody38: BinaryAssociation = BinaryAssociation(
    name="ownerBody38",
    ends={
        Property(name="Body39", type=AsmL_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="rules", type=Body, multiplicity=Multiplicity(1, 1))
    }
)
called43: BinaryAssociation = BinaryAssociation(
    name="called43",
    ends={
        Property(name="MethodCallTerm", type=AsmL_MethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="AsmL_MethodInvocation", type=MethodCallTerm, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
term44: BinaryAssociation = BinaryAssociation(
    name="term44",
    ends={
        Property(name="Term45", type=AsmL_UpdateRule, multiplicity=Multiplicity(1, 1)),
        Property(name="AsmL_UpdateRule", type=Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
updateVar46: BinaryAssociation = BinaryAssociation(
    name="updateVar46",
    ends={
        Property(name="Term47", type=AsmL_UpdateVarRule, multiplicity=Multiplicity(1, 1)),
        Property(name="AsmL_UpdateVarRule", type=Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
path48: BinaryAssociation = BinaryAssociation(
    name="path48",
    ends={
        Property(name="VarTerm49", type=AsmL_UpdateFieldRule, multiplicity=Multiplicity(1, 1)),
        Property(name="AsmL_UpdateFieldRule", type=VarTerm, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
expressions42: BinaryAssociation = BinaryAssociation(
    name="expressions42",
    ends={
        Property(name="InWhereHolds", type=AsmL_StepForEach, multiplicity=Multiplicity(1, 1)),
        Property(name="AsmL_StepForEach", type=InWhereHolds, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
updateMap50: BinaryAssociation = BinaryAssociation(
    name="updateMap50",
    ends={
        Property(name="VarTerm51", type=AsmL_UpdateMapRule, multiplicity=Multiplicity(1, 1)),
        Property(name="AsmL_UpdateMapRule", type=VarTerm, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters52: BinaryAssociation = BinaryAssociation(
    name="parameters52",
    ends={
        Property(name="Term54", type=AsmL_UpdateMapRule, multiplicity=Multiplicity(1, 1)),
        Property(name="AsmL_UpdateMapRule53", type=Term, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
expressions55: BinaryAssociation = BinaryAssociation(
    name="expressions55",
    ends={
        Property(name="InWhereHolds56", type=AsmL_ChooseRule, multiplicity=Multiplicity(1, 1)),
        Property(name="AsmL_ChooseRule", type=InWhereHolds, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ifChoosenRules57: BinaryAssociation = BinaryAssociation(
    name="ifChoosenRules57",
    ends={
        Property(name="Body59", type=AsmL_ChooseRule, multiplicity=Multiplicity(1, 1)),
        Property(name="AsmL_ChooseRule58", type=Body, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ifNotChoosenRule60: BinaryAssociation = BinaryAssociation(
    name="ifNotChoosenRule60",
    ends={
        Property(name="Body62", type=AsmL_ChooseRule, multiplicity=Multiplicity(1, 1)),
        Property(name="AsmL_ChooseRule61", type=Body, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
doRule65: BinaryAssociation = BinaryAssociation(
    name="doRule65",
    ends={
        Property(name="AsmL_ForallRule66", type=Body, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Body67", type=AsmL_ForallRule, multiplicity=Multiplicity(1, 1))
    }
)
condition68: BinaryAssociation = BinaryAssociation(
    name="condition68",
    ends={
        Property(name="Term69", type=AsmL_ConditionalRule, multiplicity=Multiplicity(1, 1)),
        Property(name="AsmL_ConditionalRule", type=Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenRule70: BinaryAssociation = BinaryAssociation(
    name="thenRule70",
    ends={
        Property(name="Body72", type=AsmL_ConditionalRule, multiplicity=Multiplicity(1, 1)),
        Property(name="AsmL_ConditionalRule71", type=Body, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseRule73: BinaryAssociation = BinaryAssociation(
    name="elseRule73",
    ends={
        Property(name="Body75", type=AsmL_ConditionalRule, multiplicity=Multiplicity(1, 1)),
        Property(name="AsmL_ConditionalRule74", type=Body, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseIfRule76: BinaryAssociation = BinaryAssociation(
    name="elseIfRule76",
    ends={
        Property(name="ElseIf", type=AsmL_ConditionalRule, multiplicity=Multiplicity(1, 1)),
        Property(name="AsmL_ConditionalRule77", type=ElseIf, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressions63: BinaryAssociation = BinaryAssociation(
    name="expressions63",
    ends={
        Property(name="InWhereHolds64", type=AsmL_ForallRule, multiplicity=Multiplicity(1, 1)),
        Property(name="AsmL_ForallRule", type=InWhereHolds, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
val80: BinaryAssociation = BinaryAssociation(
    name="val80",
    ends={
        Property(name="Term81", type=AsmL_AddRule, multiplicity=Multiplicity(1, 1)),
        Property(name="AsmL_AddRule", type=Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
set82: BinaryAssociation = BinaryAssociation(
    name="set82",
    ends={
        Property(name="VarTerm84", type=AsmL_AddRule, multiplicity=Multiplicity(1, 1)),
        Property(name="AsmL_AddRule83", type=VarTerm, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
val85: BinaryAssociation = BinaryAssociation(
    name="val85",
    ends={
        Property(name="Term86", type=AsmL_RemoveRule, multiplicity=Multiplicity(1, 1)),
        Property(name="AsmL_RemoveRule", type=Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
set87: BinaryAssociation = BinaryAssociation(
    name="set87",
    ends={
        Property(name="VarTerm89", type=AsmL_RemoveRule, multiplicity=Multiplicity(1, 1)),
        Property(name="AsmL_RemoveRule88", type=VarTerm, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
term78: BinaryAssociation = BinaryAssociation(
    name="term78",
    ends={
        Property(name="Term79", type=AsmL_ReturnRule, multiplicity=Multiplicity(1, 1)),
        Property(name="AsmL_ReturnRule", type=Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ownerDeclaration90: BinaryAssociation = BinaryAssociation(
    name="ownerDeclaration90",
    ends={
        Property(name="VarDeclaration91", type=AsmL_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="type", type=VarDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
ownerMethod92: BinaryAssociation = BinaryAssociation(
    name="ownerMethod92",
    ends={
        Property(name="Method93", type=AsmL_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="returnType", type=Method_, multiplicity=Multiplicity(0, 1))
    }
)
ownerParameter94: BinaryAssociation = BinaryAssociation(
    name="ownerParameter94",
    ends={
        Property(name="Parameter96", type=AsmL_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="type95", type=Parameter_, multiplicity=Multiplicity(0, 1))
    }
)
ofType97: BinaryAssociation = BinaryAssociation(
    name="ofType97",
    ends={
        Property(name="Type98", type=AsmL_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="AsmL_MapType", type=Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
toType99: BinaryAssociation = BinaryAssociation(
    name="toType99",
    ends={
        Property(name="Type101", type=AsmL_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="AsmL_MapType100", type=Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
types102: BinaryAssociation = BinaryAssociation(
    name="types102",
    ends={
        Property(name="Type103", type=AsmL_TupletType, multiplicity=Multiplicity(1, 1)),
        Property(name="AsmL_TupletType", type=Type, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
of104: BinaryAssociation = BinaryAssociation(
    name="of104",
    ends={
        Property(name="Type105", type=AsmL_SetType, multiplicity=Multiplicity(1, 1)),
        Property(name="AsmL_SetType", type=Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
of106: BinaryAssociation = BinaryAssociation(
    name="of106",
    ends={
        Property(name="Type107", type=AsmL_SequenceType, multiplicity=Multiplicity(1, 1)),
        Property(name="AsmL_SequenceType", type=Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftExp108: BinaryAssociation = BinaryAssociation(
    name="leftExp108",
    ends={
        Property(name="Term109", type=AsmL_Operator, multiplicity=Multiplicity(1, 1)),
        Property(name="AsmL_Operator", type=Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightExp110: BinaryAssociation = BinaryAssociation(
    name="rightExp110",
    ends={
        Property(name="Term112", type=AsmL_Operator, multiplicity=Multiplicity(1, 1)),
        Property(name="AsmL_Operator111", type=Term, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ofTerm113: BinaryAssociation = BinaryAssociation(
    name="ofTerm113",
    ends={
        Property(name="Term114", type=AsmL_MapTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="AsmL_MapTerm", type=Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
toTerm115: BinaryAssociation = BinaryAssociation(
    name="toTerm115",
    ends={
        Property(name="Term117", type=AsmL_MapTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="AsmL_MapTerm116", type=Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
terms118: BinaryAssociation = BinaryAssociation(
    name="terms118",
    ends={
        Property(name="Term119", type=AsmL_TulpletTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="AsmL_TulpletTerm", type=Term, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
parameters120: BinaryAssociation = BinaryAssociation(
    name="parameters120",
    ends={
        Property(name="Term121", type=AsmL_MethodCallTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="AsmL_MethodCallTerm", type=Term, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expressions122: BinaryAssociation = BinaryAssociation(
    name="expressions122",
    ends={
        Property(name="InWhereHolds123", type=AsmL_PredicateTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="AsmL_PredicateTerm", type=InWhereHolds, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
vals124: BinaryAssociation = BinaryAssociation(
    name="vals124",
    ends={
        Property(name="Term125", type=AsmL_EnumerateSet, multiplicity=Multiplicity(1, 1)),
        Property(name="AsmL_EnumerateSet", type=Term, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
minval126: BinaryAssociation = BinaryAssociation(
    name="minval126",
    ends={
        Property(name="Term127", type=AsmL_RangeSet, multiplicity=Multiplicity(1, 1)),
        Property(name="AsmL_RangeSet", type=Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
maxval128: BinaryAssociation = BinaryAssociation(
    name="maxval128",
    ends={
        Property(name="Term130", type=AsmL_RangeSet, multiplicity=Multiplicity(1, 1)),
        Property(name="AsmL_RangeSet129", type=Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expressions131: BinaryAssociation = BinaryAssociation(
    name="expressions131",
    ends={
        Property(name="InWhereHolds132", type=AsmL_AlgorithmSet, multiplicity=Multiplicity(1, 1)),
        Property(name="AsmL_AlgorithmSet", type=InWhereHolds, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
minval135: BinaryAssociation = BinaryAssociation(
    name="minval135",
    ends={
        Property(name="Term136", type=AsmL_RangeSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="AsmL_RangeSequence", type=Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
maxval137: BinaryAssociation = BinaryAssociation(
    name="maxval137",
    ends={
        Property(name="Term139", type=AsmL_RangeSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="AsmL_RangeSequence138", type=Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
vals133: BinaryAssociation = BinaryAssociation(
    name="vals133",
    ends={
        Property(name="Term134", type=AsmL_EnumerateSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="AsmL_EnumerateSequence", type=Term, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_AsmL_Body_LocatedElement = Generalization(general=LocatedElement, specific=AsmL_Body)
gen_AsmL_InWhereHolds_LocatedElement = Generalization(general=LocatedElement, specific=AsmL_InWhereHolds)
gen_AsmL_AsmLFile_LocatedElement = Generalization(general=LocatedElement, specific=AsmL_AsmLFile)
gen_AsmL_AsmLElement_LocatedElement = Generalization(general=LocatedElement, specific=AsmL_AsmLElement)
gen_AsmL_VarDeclaration_AsmLElement = Generalization(general=AsmLElement, specific=AsmL_VarDeclaration)
gen_AsmL_VarDeclaration_VarOrCase = Generalization(general=VarOrCase, specific=AsmL_VarDeclaration)
gen_AsmL_Namespace_AsmLElement = Generalization(general=AsmLElement, specific=AsmL_Namespace)
gen_AsmL_Structure_AsmLElement = Generalization(general=AsmLElement, specific=AsmL_Structure)
gen_AsmL_VarDeclaration_VarOrMethod = Generalization(general=VarOrMethod, specific=AsmL_VarDeclaration)
gen_AsmL_Case_VarOrCase = Generalization(general=VarOrCase, specific=AsmL_Case)
gen_AsmL_Class_AsmLElement = Generalization(general=AsmLElement, specific=AsmL_Class)
gen_AsmL_VarOrCase_LocatedElement = Generalization(general=LocatedElement, specific=AsmL_VarOrCase)
gen_AsmL_Enumeration_AsmLElement = Generalization(general=AsmLElement, specific=AsmL_Enumeration)
gen_AsmL_Enumerator_LocatedElement = Generalization(general=LocatedElement, specific=AsmL_Enumerator)
gen_AsmL_Function_AsmLElement = Generalization(general=AsmLElement, specific=AsmL_Function)
gen_AsmL_VarOrMethod_LocatedElement = Generalization(general=LocatedElement, specific=AsmL_VarOrMethod)
gen_AsmL_Method_Function = Generalization(general=Function, specific=AsmL_Method)
gen_AsmL_Method_VarOrMethod = Generalization(general=VarOrMethod, specific=AsmL_Method)
gen_AsmL_Parameter_LocatedElement = Generalization(general=LocatedElement, specific=AsmL_Parameter)
gen_AsmL_Main_Function = Generalization(general=Function, specific=AsmL_Main)
gen_AsmL_Initially_LocatedElement = Generalization(general=LocatedElement, specific=AsmL_Initially)
gen_AsmL_Rule_LocatedElement = Generalization(general=LocatedElement, specific=AsmL_Rule)
gen_AsmL_SkipRule_Rule = Generalization(general=Rule, specific=AsmL_SkipRule)
gen_AsmL_Step_Rule = Generalization(general=Rule, specific=AsmL_Step)
gen_AsmL_StepUntilFixPoint_Step = Generalization(general=Step, specific=AsmL_StepUntilFixPoint)
gen_AsmL_StepExpression_Step = Generalization(general=Step, specific=AsmL_StepExpression)
gen_AsmL_StepWhile_StepExpression = Generalization(general=StepExpression, specific=AsmL_StepWhile)
gen_AsmL_StepUntil_StepExpression = Generalization(general=StepExpression, specific=AsmL_StepUntil)
gen_AsmL_StepForEach_Step = Generalization(general=Step, specific=AsmL_StepForEach)
gen_AsmL_MethodInvocation_Rule = Generalization(general=Rule, specific=AsmL_MethodInvocation)
gen_AsmL_UpdateRule_Rule = Generalization(general=Rule, specific=AsmL_UpdateRule)
gen_AsmL_UpdateVarRule_UpdateRule = Generalization(general=UpdateRule, specific=AsmL_UpdateVarRule)
gen_AsmL_UpdateFieldRule_UpdateRule = Generalization(general=UpdateRule, specific=AsmL_UpdateFieldRule)
gen_AsmL_ChooseRule_Rule = Generalization(general=Rule, specific=AsmL_ChooseRule)
gen_AsmL_ForallRule_Rule = Generalization(general=Rule, specific=AsmL_ForallRule)
gen_AsmL_UpdateMapRule_UpdateRule = Generalization(general=UpdateRule, specific=AsmL_UpdateMapRule)
gen_AsmL_ConditionalRule_Rule = Generalization(general=Rule, specific=AsmL_ConditionalRule)
gen_AsmL_ElseIf_ConditionalRule = Generalization(general=ConditionalRule, specific=AsmL_ElseIf)
gen_AsmL_ReturnRule_Rule = Generalization(general=Rule, specific=AsmL_ReturnRule)
gen_AsmL_AddRule_Rule = Generalization(general=Rule, specific=AsmL_AddRule)
gen_AsmL_RemoveRule_Rule = Generalization(general=Rule, specific=AsmL_RemoveRule)
gen_AsmL_Type_AsmLElement = Generalization(general=AsmLElement, specific=AsmL_Type)
gen_AsmL_NamedType_Type = Generalization(general=Type, specific=AsmL_NamedType)
gen_AsmL_MapType_Type = Generalization(general=Type, specific=AsmL_MapType)
gen_AsmL_SetType_Type = Generalization(general=Type, specific=AsmL_SetType)
gen_AsmL_SequenceType_Type = Generalization(general=Type, specific=AsmL_SequenceType)
gen_AsmL_Term_LocatedElement = Generalization(general=LocatedElement, specific=AsmL_Term)
gen_AsmL_VarTerm_Term = Generalization(general=Term, specific=AsmL_VarTerm)
gen_AsmL_TupletType_Type = Generalization(general=Type, specific=AsmL_TupletType)
gen_AsmL_MapTerm_Term = Generalization(general=Term, specific=AsmL_MapTerm)
gen_AsmL_Operator_Term = Generalization(general=Term, specific=AsmL_Operator)
gen_AsmL_TulpletTerm_Term = Generalization(general=Term, specific=AsmL_TulpletTerm)
gen_AsmL_MethodCallTerm_Term = Generalization(general=Term, specific=AsmL_MethodCallTerm)
gen_AsmL_ForAllTerm_PredicateTerm = Generalization(general=PredicateTerm, specific=AsmL_ForAllTerm)
gen_AsmL_ExistsTerm_PredicateTerm = Generalization(general=PredicateTerm, specific=AsmL_ExistsTerm)
gen_AsmL_AnyIn_PredicateTerm = Generalization(general=PredicateTerm, specific=AsmL_AnyIn)
gen_AsmL_SetTerm_Term = Generalization(general=Term, specific=AsmL_SetTerm)
gen_AsmL_EnumerateSet_SetTerm = Generalization(general=SetTerm, specific=AsmL_EnumerateSet)
gen_AsmL_NewInstance_MethodCallTerm = Generalization(general=MethodCallTerm, specific=AsmL_NewInstance)
gen_AsmL_PredicateTerm_Term = Generalization(general=Term, specific=AsmL_PredicateTerm)
gen_AsmL_AlgorithmSet_SetTerm = Generalization(general=SetTerm, specific=AsmL_AlgorithmSet)
gen_AsmL_SequenceTerm_Term = Generalization(general=Term, specific=AsmL_SequenceTerm)
gen_AsmL_EnumerateSequence_SequenceTerm = Generalization(general=SequenceTerm, specific=AsmL_EnumerateSequence)
gen_AsmL_RangeSet_SetTerm = Generalization(general=SetTerm, specific=AsmL_RangeSet)
gen_AsmL_RangeSequence_SequenceTerm = Generalization(general=SequenceTerm, specific=AsmL_RangeSequence)
gen_AsmL_Constant_Term = Generalization(general=Term, specific=AsmL_Constant)
gen_AsmL_BooleanConstant_Constant = Generalization(general=Constant, specific=AsmL_BooleanConstant)
gen_AsmL_StringConstant_Constant = Generalization(general=Constant, specific=AsmL_StringConstant)
gen_AsmL_NullConstant_Constant = Generalization(general=Constant, specific=AsmL_NullConstant)
gen_AsmL_IntegerConstant_Constant = Generalization(general=Constant, specific=AsmL_IntegerConstant)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={AsmL_LocatedElement, AsmL_Body, LocatedElement, Rule, AsmL_InWhereHolds, Term, AsmL_AsmLFile, AsmLElement, Main, AsmL_AsmLElement, AsmLFile, AsmL_VarDeclaration, VarOrCase, VarOrMethod, Type, AsmL_Namespace, AsmL_Structure, AsmL_Case, VarDeclaration, AsmL_Class, AsmL_VarOrCase, Structure, AsmL_Enumeration, Enumerator, AsmL_Enumerator, AsmL_Function, AsmL_VarOrMethod, Class_, AsmL_Method, Function, Parameter_, AsmL_Parameter, Body, AsmL_Main, Initially, AsmL_Initially, VarTerm, AsmL_Rule, Method_, AsmL_SkipRule, AsmL_Step, AsmL_StepUntilFixPoint, Step, AsmL_StepExpression, AsmL_StepWhile, StepExpression, AsmL_StepUntil, AsmL_StepForEach, InWhereHolds, MethodCallTerm, AsmL_UpdateRule, AsmL_UpdateVarRule, UpdateRule, AsmL_UpdateFieldRule, AsmL_MethodInvocation, AsmL_ChooseRule, AsmL_ForallRule, AsmL_UpdateMapRule, AsmL_ConditionalRule, ElseIf, AsmL_ElseIf, ConditionalRule, AsmL_ReturnRule, AsmL_AddRule, AsmL_RemoveRule, AsmL_Type, AsmL_NamedType, AsmL_MapType, AsmL_SetType, AsmL_SequenceType, AsmL_Term, AsmL_VarTerm, AsmL_TupletType, AsmL_MapTerm, AsmL_Operator, AsmL_TulpletTerm, AsmL_MethodCallTerm, AsmL_ForAllTerm, PredicateTerm, AsmL_ExistsTerm, AsmL_AnyIn, AsmL_SetTerm, AsmL_EnumerateSet, SetTerm, AsmL_NewInstance, AsmL_PredicateTerm, AsmL_AlgorithmSet, AsmL_SequenceTerm, AsmL_EnumerateSequence, SequenceTerm, AsmL_RangeSet, AsmL_RangeSequence, AsmL_Constant, AsmL_BooleanConstant, Constant, AsmL_StringConstant, AsmL_NullConstant, AsmL_IntegerConstant},
    associations={rules0, var1, in_2, holds8, elements11, main12, file13, where5, type14, varOrCase15, ownerStructure16, variables17, varOrMethod18, ownerClass19, enumerators20, value21, returnType24, parameters26, type28, body23, ownerMethod30, mainFile31, initialisations33, id34, val35, expression40, ownerBody38, called43, term44, updateVar46, path48, expressions42, updateMap50, parameters52, expressions55, ifChoosenRules57, ifNotChoosenRule60, doRule65, condition68, thenRule70, elseRule73, elseIfRule76, expressions63, val80, set82, val85, set87, term78, ownerDeclaration90, ownerMethod92, ownerParameter94, ofType97, toType99, types102, of104, of106, leftExp108, rightExp110, ofTerm113, toTerm115, terms118, parameters120, expressions122, vals124, minval126, maxval128, expressions131, minval135, maxval137, vals133},
    generalizations={gen_AsmL_Body_LocatedElement, gen_AsmL_InWhereHolds_LocatedElement, gen_AsmL_AsmLFile_LocatedElement, gen_AsmL_AsmLElement_LocatedElement, gen_AsmL_VarDeclaration_AsmLElement, gen_AsmL_VarDeclaration_VarOrCase, gen_AsmL_Namespace_AsmLElement, gen_AsmL_Structure_AsmLElement, gen_AsmL_VarDeclaration_VarOrMethod, gen_AsmL_Case_VarOrCase, gen_AsmL_Class_AsmLElement, gen_AsmL_VarOrCase_LocatedElement, gen_AsmL_Enumeration_AsmLElement, gen_AsmL_Enumerator_LocatedElement, gen_AsmL_Function_AsmLElement, gen_AsmL_VarOrMethod_LocatedElement, gen_AsmL_Method_Function, gen_AsmL_Method_VarOrMethod, gen_AsmL_Parameter_LocatedElement, gen_AsmL_Main_Function, gen_AsmL_Initially_LocatedElement, gen_AsmL_Rule_LocatedElement, gen_AsmL_SkipRule_Rule, gen_AsmL_Step_Rule, gen_AsmL_StepUntilFixPoint_Step, gen_AsmL_StepExpression_Step, gen_AsmL_StepWhile_StepExpression, gen_AsmL_StepUntil_StepExpression, gen_AsmL_StepForEach_Step, gen_AsmL_MethodInvocation_Rule, gen_AsmL_UpdateRule_Rule, gen_AsmL_UpdateVarRule_UpdateRule, gen_AsmL_UpdateFieldRule_UpdateRule, gen_AsmL_ChooseRule_Rule, gen_AsmL_ForallRule_Rule, gen_AsmL_UpdateMapRule_UpdateRule, gen_AsmL_ConditionalRule_Rule, gen_AsmL_ElseIf_ConditionalRule, gen_AsmL_ReturnRule_Rule, gen_AsmL_AddRule_Rule, gen_AsmL_RemoveRule_Rule, gen_AsmL_Type_AsmLElement, gen_AsmL_NamedType_Type, gen_AsmL_MapType_Type, gen_AsmL_SetType_Type, gen_AsmL_SequenceType_Type, gen_AsmL_Term_LocatedElement, gen_AsmL_VarTerm_Term, gen_AsmL_TupletType_Type, gen_AsmL_MapTerm_Term, gen_AsmL_Operator_Term, gen_AsmL_TulpletTerm_Term, gen_AsmL_MethodCallTerm_Term, gen_AsmL_ForAllTerm_PredicateTerm, gen_AsmL_ExistsTerm_PredicateTerm, gen_AsmL_AnyIn_PredicateTerm, gen_AsmL_SetTerm_Term, gen_AsmL_EnumerateSet_SetTerm, gen_AsmL_NewInstance_MethodCallTerm, gen_AsmL_PredicateTerm_Term, gen_AsmL_AlgorithmSet_SetTerm, gen_AsmL_SequenceTerm_Term, gen_AsmL_EnumerateSequence_SequenceTerm, gen_AsmL_RangeSet_SetTerm, gen_AsmL_RangeSequence_SequenceTerm, gen_AsmL_Constant_Term, gen_AsmL_BooleanConstant_Constant, gen_AsmL_StringConstant_Constant, gen_AsmL_NullConstant_Constant, gen_AsmL_IntegerConstant_Constant},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)