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
AccessUpdateType: Enumeration = Enumeration(
    name="AccessUpdateType",
    literals={
            EnumerationLiteral(name="access"),
			EnumerationLiteral(name="update")
    }
)

AsmType: Enumeration = Enumeration(
    name="AsmType",
    literals={
            EnumerationLiteral(name="function"),
			EnumerationLiteral(name="subasm")
    }
)

# Classes
ASM_LocatedElement = Class(name="ASM_LocatedElement", is_abstract=True)
ASM_XAsmFile = Class(name="ASM_XAsmFile", is_abstract=True)
LocatedElement = Class(name="LocatedElement")
ASM_XAsmSpec = Class(name="ASM_XAsmSpec")
XAsmFile = Class(name="XAsmFile")
Asm = Class(name="Asm")
ASM_Asm = Class(name="ASM_Asm")
Signature = Class(name="Signature")
MetaInformation = Class(name="MetaInformation")
Body = Class(name="Body")
ASM_Signature = Class(name="ASM_Signature")
Argument = Class(name="Argument")
ASM_Body = Class(name="ASM_Body")
Declaration = Class(name="Declaration")
Initialization = Class(name="Initialization")
Rule = Class(name="Rule")
ASM_MetaInformation = Class(name="ASM_MetaInformation")
AccessUpdateFunction = Class(name="AccessUpdateFunction")
ASM_AccessUpdateFunction = Class(name="ASM_AccessUpdateFunction")
ASM_Argument = Class(name="ASM_Argument")
VariableDecl = Class(name="VariableDecl")
Function = Class(name="Function")
ASM_Declaration = Class(name="ASM_Declaration", is_abstract=True)
ASM_Function = Class(name="ASM_Function")
ElementDecl = Class(name="ElementDecl")
Parameter_ = Class(name="Parameter")
Term = Class(name="Term")
ASM_Parameter = Class(name="ASM_Parameter")
ASM_Universe = Class(name="ASM_Universe")
Universe = Class(name="Universe")
ASM_Initialization = Class(name="ASM_Initialization")
ASM_Term = Class(name="ASM_Term", is_abstract=True)
ASM_Constant = Class(name="ASM_Constant", is_abstract=True)
ASM_FunctionOrVariableTerm = Class(name="ASM_FunctionOrVariableTerm")
ASM_OperatorTerm = Class(name="ASM_OperatorTerm")
ASM_BooleanConstant = Class(name="ASM_BooleanConstant")
Constant = Class(name="Constant")
ASM_IntegerConstant = Class(name="ASM_IntegerConstant")
ASM_StringConstant = Class(name="ASM_StringConstant")
ASM_UndefConstant = Class(name="ASM_UndefConstant")
ASM_Rule = Class(name="ASM_Rule", is_abstract=True)
ASM_SkipRule = Class(name="ASM_SkipRule")
ASM_AsmInvocation = Class(name="ASM_AsmInvocation")
ASM_UpdateRule = Class(name="ASM_UpdateRule")
FunctionOrVariableTerm = Class(name="FunctionOrVariableTerm")
ASM_ChooseRule = Class(name="ASM_ChooseRule")
ASM_DoForallRule = Class(name="ASM_DoForallRule")
ASM_ConditionalRule = Class(name="ASM_ConditionalRule")
ElseIf = Class(name="ElseIf")
ASM_ElseIf = Class(name="ASM_ElseIf")
ASM_ExtendRule = Class(name="ASM_ExtendRule")
ASM_ElementDecl = Class(name="ASM_ElementDecl", is_abstract=True)
ASM_VariableDecl = Class(name="ASM_VariableDecl")
ASM_Extension = Class(name="ASM_Extension")
ASM_ReturnRule = Class(name="ASM_ReturnRule")
Extension = Class(name="Extension")

# ASM_LocatedElement class attributes and methods
ASM_LocatedElement_location: Property = Property(name="location", type=StringType)
ASM_LocatedElement.attributes={ASM_LocatedElement_location}

# ASM_XAsmFile class attributes and methods

# LocatedElement class attributes and methods

# ASM_XAsmSpec class attributes and methods

# XAsmFile class attributes and methods

# Asm class attributes and methods

# ASM_Asm class attributes and methods
ASM_Asm_returnType: Property = Property(name="returnType", type=StringType)
ASM_Asm.attributes={ASM_Asm_returnType}

# Signature class attributes and methods

# MetaInformation class attributes and methods

# Body class attributes and methods

# ASM_Signature class attributes and methods
ASM_Signature_isMain: Property = Property(name="isMain", type=StringType)
ASM_Signature_name: Property = Property(name="name", type=StringType)
ASM_Signature.attributes={ASM_Signature_name, ASM_Signature_isMain}

# Argument class attributes and methods

# ASM_Body class attributes and methods

# Declaration class attributes and methods

# Initialization class attributes and methods

# Rule class attributes and methods

# ASM_MetaInformation class attributes and methods
ASM_MetaInformation_usedAs: Property = Property(name="usedAs", type=StringType)
ASM_MetaInformation.attributes={ASM_MetaInformation_usedAs}

# AccessUpdateFunction class attributes and methods

# ASM_AccessUpdateFunction class attributes and methods
ASM_AccessUpdateFunction_type: Property = Property(name="type", type=StringType)
ASM_AccessUpdateFunction.attributes={ASM_AccessUpdateFunction_type}

# ASM_Argument class attributes and methods
ASM_Argument_type: Property = Property(name="type", type=StringType)
ASM_Argument.attributes={ASM_Argument_type}

# VariableDecl class attributes and methods

# Function class attributes and methods

# ASM_Declaration class attributes and methods

# ASM_Function class attributes and methods
ASM_Function_returnType: Property = Property(name="returnType", type=StringType)
ASM_Function_isExternal: Property = Property(name="isExternal", type=StringType)
ASM_Function.attributes={ASM_Function_isExternal, ASM_Function_returnType}

# ElementDecl class attributes and methods

# Parameter class attributes and methods

# Term class attributes and methods

# ASM_Parameter class attributes and methods
ASM_Parameter_name: Property = Property(name="name", type=StringType)
ASM_Parameter_type: Property = Property(name="type", type=StringType)
ASM_Parameter.attributes={ASM_Parameter_name, ASM_Parameter_type}

# ASM_Universe class attributes and methods
ASM_Universe_name: Property = Property(name="name", type=StringType)
ASM_Universe_contents: Property = Property(name="contents", type=StringType)
ASM_Universe.attributes={ASM_Universe_name, ASM_Universe_contents}

# Universe class attributes and methods

# ASM_Initialization class attributes and methods

# ASM_Term class attributes and methods

# ASM_Constant class attributes and methods

# ASM_FunctionOrVariableTerm class attributes and methods

# ASM_OperatorTerm class attributes and methods
ASM_OperatorTerm_opName: Property = Property(name="opName", type=StringType)
ASM_OperatorTerm.attributes={ASM_OperatorTerm_opName}

# ASM_BooleanConstant class attributes and methods
ASM_BooleanConstant_value: Property = Property(name="value", type=StringType)
ASM_BooleanConstant.attributes={ASM_BooleanConstant_value}

# Constant class attributes and methods

# ASM_IntegerConstant class attributes and methods
ASM_IntegerConstant_value: Property = Property(name="value", type=StringType)
ASM_IntegerConstant.attributes={ASM_IntegerConstant_value}

# ASM_StringConstant class attributes and methods
ASM_StringConstant_value: Property = Property(name="value", type=StringType)
ASM_StringConstant.attributes={ASM_StringConstant_value}

# ASM_UndefConstant class attributes and methods

# ASM_Rule class attributes and methods
ASM_Rule_inSequence: Property = Property(name="inSequence", type=StringType)
ASM_Rule.attributes={ASM_Rule_inSequence}

# ASM_SkipRule class attributes and methods

# ASM_AsmInvocation class attributes and methods
ASM_AsmInvocation_asmName: Property = Property(name="asmName", type=StringType)
ASM_AsmInvocation.attributes={ASM_AsmInvocation_asmName}

# ASM_UpdateRule class attributes and methods

# FunctionOrVariableTerm class attributes and methods

# ASM_ChooseRule class attributes and methods

# ASM_DoForallRule class attributes and methods

# ASM_ConditionalRule class attributes and methods

# ElseIf class attributes and methods

# ASM_ElseIf class attributes and methods

# ASM_ExtendRule class attributes and methods

# ASM_ElementDecl class attributes and methods
ASM_ElementDecl_name: Property = Property(name="name", type=StringType)
ASM_ElementDecl.attributes={ASM_ElementDecl_name}

# ASM_VariableDecl class attributes and methods

# ASM_Extension class attributes and methods

# ASM_ReturnRule class attributes and methods

# Extension class attributes and methods

# Relationships
Asm0: BinaryAssociation = BinaryAssociation(
    name="Asm0",
    ends={
        Property(name="Asm", type=ASM_XAsmSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="ASM_XAsmSpec", type=Asm, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
signature1: BinaryAssociation = BinaryAssociation(
    name="signature1",
    ends={
        Property(name="Signature", type=ASM_Asm, multiplicity=Multiplicity(1, 1)),
        Property(name="ASM_Asm", type=Signature, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
metaInformation2: BinaryAssociation = BinaryAssociation(
    name="metaInformation2",
    ends={
        Property(name="MetaInformation", type=ASM_Asm, multiplicity=Multiplicity(1, 1)),
        Property(name="ASM_Asm3", type=MetaInformation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body4: BinaryAssociation = BinaryAssociation(
    name="body4",
    ends={
        Property(name="Body", type=ASM_Asm, multiplicity=Multiplicity(1, 1)),
        Property(name="ASM_Asm5", type=Body, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments6: BinaryAssociation = BinaryAssociation(
    name="arguments6",
    ends={
        Property(name="Argument", type=ASM_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="ASM_Signature", type=Argument, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declarations7: BinaryAssociation = BinaryAssociation(
    name="declarations7",
    ends={
        Property(name="Declaration", type=ASM_Body, multiplicity=Multiplicity(1, 1)),
        Property(name="ASM_Body", type=Declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialization8: BinaryAssociation = BinaryAssociation(
    name="initialization8",
    ends={
        Property(name="Initialization", type=ASM_Body, multiplicity=Multiplicity(1, 1)),
        Property(name="ASM_Body9", type=Initialization, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rules10: BinaryAssociation = BinaryAssociation(
    name="rules10",
    ends={
        Property(name="Rule", type=ASM_Body, multiplicity=Multiplicity(1, 1)),
        Property(name="ASM_Body11", type=Rule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usedAsIn12: BinaryAssociation = BinaryAssociation(
    name="usedAsIn12",
    ends={
        Property(name="Signature13", type=ASM_MetaInformation, multiplicity=Multiplicity(1, 1)),
        Property(name="ASM_MetaInformation", type=Signature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
accessUpdateFunctions14: BinaryAssociation = BinaryAssociation(
    name="accessUpdateFunctions14",
    ends={
        Property(name="AccessUpdateFunction", type=ASM_MetaInformation, multiplicity=Multiplicity(1, 1)),
        Property(name="ASM_MetaInformation15", type=AccessUpdateFunction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functions16: BinaryAssociation = BinaryAssociation(
    name="functions16",
    ends={
        Property(name="Function", type=ASM_AccessUpdateFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="ASM_AccessUpdateFunction", type=Function, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
parameters17: BinaryAssociation = BinaryAssociation(
    name="parameters17",
    ends={
        Property(name="Parameter", type=ASM_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="ASM_Function", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initTerm18: BinaryAssociation = BinaryAssociation(
    name="initTerm18",
    ends={
        Property(name="Term", type=ASM_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="ASM_Function19", type=Term, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
superUniverses20: BinaryAssociation = BinaryAssociation(
    name="superUniverses20",
    ends={
        Property(name="Universe", type=ASM_Universe, multiplicity=Multiplicity(1, 1)),
        Property(name="ASM_Universe", type=Universe, multiplicity=Multiplicity(0, 9999))
    }
)
rules21: BinaryAssociation = BinaryAssociation(
    name="rules21",
    ends={
        Property(name="Rule22", type=ASM_Initialization, multiplicity=Multiplicity(1, 1)),
        Property(name="ASM_Initialization", type=Rule, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
declaration23: BinaryAssociation = BinaryAssociation(
    name="declaration23",
    ends={
        Property(name="ElementDecl", type=ASM_FunctionOrVariableTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="ASM_FunctionOrVariableTerm", type=ElementDecl, multiplicity=Multiplicity(1, 1))
    }
)
leftExp27: BinaryAssociation = BinaryAssociation(
    name="leftExp27",
    ends={
        Property(name="Term28", type=ASM_OperatorTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="ASM_OperatorTerm", type=Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightExp29: BinaryAssociation = BinaryAssociation(
    name="rightExp29",
    ends={
        Property(name="Term31", type=ASM_OperatorTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="ASM_OperatorTerm30", type=Term, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
terms24: BinaryAssociation = BinaryAssociation(
    name="terms24",
    ends={
        Property(name="Term26", type=ASM_FunctionOrVariableTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="ASM_FunctionOrVariableTerm25", type=Term, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arguments32: BinaryAssociation = BinaryAssociation(
    name="arguments32",
    ends={
        Property(name="Term33", type=ASM_AsmInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="ASM_AsmInvocation", type=Term, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
function34: BinaryAssociation = BinaryAssociation(
    name="function34",
    ends={
        Property(name="FunctionOrVariableTerm", type=ASM_UpdateRule, multiplicity=Multiplicity(1, 1)),
        Property(name="ASM_UpdateRule", type=FunctionOrVariableTerm, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
updateTerm35: BinaryAssociation = BinaryAssociation(
    name="updateTerm35",
    ends={
        Property(name="Term37", type=ASM_UpdateRule, multiplicity=Multiplicity(1, 1)),
        Property(name="ASM_UpdateRule36", type=Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
chooseId38: BinaryAssociation = BinaryAssociation(
    name="chooseId38",
    ends={
        Property(name="VariableDecl", type=ASM_ChooseRule, multiplicity=Multiplicity(1, 1)),
        Property(name="ASM_ChooseRule", type=VariableDecl, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
inSet39: BinaryAssociation = BinaryAssociation(
    name="inSet39",
    ends={
        Property(name="Universe41", type=ASM_ChooseRule, multiplicity=Multiplicity(1, 1)),
        Property(name="ASM_ChooseRule40", type=Universe, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
guard42: BinaryAssociation = BinaryAssociation(
    name="guard42",
    ends={
        Property(name="Term44", type=ASM_ChooseRule, multiplicity=Multiplicity(1, 1)),
        Property(name="ASM_ChooseRule43", type=Term, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifChoosenRules45: BinaryAssociation = BinaryAssociation(
    name="ifChoosenRules45",
    ends={
        Property(name="Rule47", type=ASM_ChooseRule, multiplicity=Multiplicity(1, 1)),
        Property(name="ASM_ChooseRule46", type=Rule, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
ifNotChoosenRule48: BinaryAssociation = BinaryAssociation(
    name="ifNotChoosenRule48",
    ends={
        Property(name="Rule50", type=ASM_ChooseRule, multiplicity=Multiplicity(1, 1)),
        Property(name="ASM_ChooseRule49", type=Rule, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inSet53: BinaryAssociation = BinaryAssociation(
    name="inSet53",
    ends={
        Property(name="Universe55", type=ASM_DoForallRule, multiplicity=Multiplicity(1, 1)),
        Property(name="ASM_DoForallRule54", type=Universe, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition56: BinaryAssociation = BinaryAssociation(
    name="condition56",
    ends={
        Property(name="Term58", type=ASM_DoForallRule, multiplicity=Multiplicity(1, 1)),
        Property(name="ASM_DoForallRule57", type=Term, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
doRule59: BinaryAssociation = BinaryAssociation(
    name="doRule59",
    ends={
        Property(name="Rule61", type=ASM_DoForallRule, multiplicity=Multiplicity(1, 1)),
        Property(name="ASM_DoForallRule60", type=Rule, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
condition62: BinaryAssociation = BinaryAssociation(
    name="condition62",
    ends={
        Property(name="Term63", type=ASM_ConditionalRule, multiplicity=Multiplicity(1, 1)),
        Property(name="ASM_ConditionalRule", type=Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenRule64: BinaryAssociation = BinaryAssociation(
    name="thenRule64",
    ends={
        Property(name="Rule66", type=ASM_ConditionalRule, multiplicity=Multiplicity(1, 1)),
        Property(name="ASM_ConditionalRule65", type=Rule, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
elseRule67: BinaryAssociation = BinaryAssociation(
    name="elseRule67",
    ends={
        Property(name="Rule69", type=ASM_ConditionalRule, multiplicity=Multiplicity(1, 1)),
        Property(name="ASM_ConditionalRule68", type=Rule, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
id51: BinaryAssociation = BinaryAssociation(
    name="id51",
    ends={
        Property(name="VariableDecl52", type=ASM_DoForallRule, multiplicity=Multiplicity(1, 1)),
        Property(name="ASM_DoForallRule", type=VariableDecl, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseIfRule70: BinaryAssociation = BinaryAssociation(
    name="elseIfRule70",
    ends={
        Property(name="ElseIf", type=ASM_ConditionalRule, multiplicity=Multiplicity(1, 1)),
        Property(name="ASM_ConditionalRule71", type=ElseIf, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition72: BinaryAssociation = BinaryAssociation(
    name="condition72",
    ends={
        Property(name="Term73", type=ASM_ElseIf, multiplicity=Multiplicity(1, 1)),
        Property(name="ASM_ElseIf", type=Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenRule74: BinaryAssociation = BinaryAssociation(
    name="thenRule74",
    ends={
        Property(name="Rule76", type=ASM_ElseIf, multiplicity=Multiplicity(1, 1)),
        Property(name="ASM_ElseIf75", type=Rule, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
elseRule77: BinaryAssociation = BinaryAssociation(
    name="elseRule77",
    ends={
        Property(name="Rule79", type=ASM_ElseIf, multiplicity=Multiplicity(1, 1)),
        Property(name="ASM_ElseIf78", type=Rule, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseIfRule80: BinaryAssociation = BinaryAssociation(
    name="elseIfRule80",
    ends={
        Property(name="ElseIf82", type=ASM_ElseIf, multiplicity=Multiplicity(1, 1)),
        Property(name="ASM_ElseIf81", type=ElseIf, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extensions83: BinaryAssociation = BinaryAssociation(
    name="extensions83",
    ends={
        Property(name="Extension", type=ASM_ExtendRule, multiplicity=Multiplicity(1, 1)),
        Property(name="ASM_ExtendRule", type=Extension, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
rules84: BinaryAssociation = BinaryAssociation(
    name="rules84",
    ends={
        Property(name="Rule86", type=ASM_ExtendRule, multiplicity=Multiplicity(1, 1)),
        Property(name="ASM_ExtendRule85", type=Rule, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
elements87: BinaryAssociation = BinaryAssociation(
    name="elements87",
    ends={
        Property(name="VariableDecl88", type=ASM_Extension, multiplicity=Multiplicity(1, 1)),
        Property(name="ASM_Extension", type=VariableDecl, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
universe89: BinaryAssociation = BinaryAssociation(
    name="universe89",
    ends={
        Property(name="Universe91", type=ASM_Extension, multiplicity=Multiplicity(1, 1)),
        Property(name="ASM_Extension90", type=Universe, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
term92: BinaryAssociation = BinaryAssociation(
    name="term92",
    ends={
        Property(name="Term93", type=ASM_ReturnRule, multiplicity=Multiplicity(1, 1)),
        Property(name="ASM_ReturnRule", type=Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_ASM_XAsmFile_LocatedElement = Generalization(general=LocatedElement, specific=ASM_XAsmFile)
gen_ASM_XAsmSpec_XAsmFile = Generalization(general=XAsmFile, specific=ASM_XAsmSpec)
gen_ASM_Asm_LocatedElement = Generalization(general=LocatedElement, specific=ASM_Asm)
gen_ASM_Signature_LocatedElement = Generalization(general=LocatedElement, specific=ASM_Signature)
gen_ASM_Argument_VariableDecl = Generalization(general=VariableDecl, specific=ASM_Argument)
gen_ASM_Body_XAsmFile = Generalization(general=XAsmFile, specific=ASM_Body)
gen_ASM_MetaInformation_LocatedElement = Generalization(general=LocatedElement, specific=ASM_MetaInformation)
gen_ASM_AccessUpdateFunction_LocatedElement = Generalization(general=LocatedElement, specific=ASM_AccessUpdateFunction)
gen_ASM_Declaration_LocatedElement = Generalization(general=LocatedElement, specific=ASM_Declaration)
gen_ASM_Function_Declaration = Generalization(general=Declaration, specific=ASM_Function)
gen_ASM_Function_ElementDecl = Generalization(general=ElementDecl, specific=ASM_Function)
gen_ASM_Parameter_LocatedElement = Generalization(general=LocatedElement, specific=ASM_Parameter)
gen_ASM_Universe_Declaration = Generalization(general=Declaration, specific=ASM_Universe)
gen_ASM_Initialization_LocatedElement = Generalization(general=LocatedElement, specific=ASM_Initialization)
gen_ASM_Term_LocatedElement = Generalization(general=LocatedElement, specific=ASM_Term)
gen_ASM_Constant_Term = Generalization(general=Term, specific=ASM_Constant)
gen_ASM_FunctionOrVariableTerm_Term = Generalization(general=Term, specific=ASM_FunctionOrVariableTerm)
gen_ASM_OperatorTerm_Term = Generalization(general=Term, specific=ASM_OperatorTerm)
gen_ASM_BooleanConstant_Constant = Generalization(general=Constant, specific=ASM_BooleanConstant)
gen_ASM_IntegerConstant_Constant = Generalization(general=Constant, specific=ASM_IntegerConstant)
gen_ASM_StringConstant_Constant = Generalization(general=Constant, specific=ASM_StringConstant)
gen_ASM_UndefConstant_Constant = Generalization(general=Constant, specific=ASM_UndefConstant)
gen_ASM_Rule_LocatedElement = Generalization(general=LocatedElement, specific=ASM_Rule)
gen_ASM_SkipRule_Rule = Generalization(general=Rule, specific=ASM_SkipRule)
gen_ASM_AsmInvocation_Rule = Generalization(general=Rule, specific=ASM_AsmInvocation)
gen_ASM_UpdateRule_Rule = Generalization(general=Rule, specific=ASM_UpdateRule)
gen_ASM_ChooseRule_Rule = Generalization(general=Rule, specific=ASM_ChooseRule)
gen_ASM_DoForallRule_Rule = Generalization(general=Rule, specific=ASM_DoForallRule)
gen_ASM_ConditionalRule_Rule = Generalization(general=Rule, specific=ASM_ConditionalRule)
gen_ASM_ElseIf_LocatedElement = Generalization(general=LocatedElement, specific=ASM_ElseIf)
gen_ASM_ExtendRule_Rule = Generalization(general=Rule, specific=ASM_ExtendRule)
gen_ASM_ElementDecl_LocatedElement = Generalization(general=LocatedElement, specific=ASM_ElementDecl)
gen_ASM_VariableDecl_ElementDecl = Generalization(general=ElementDecl, specific=ASM_VariableDecl)
gen_ASM_Extension_LocatedElement = Generalization(general=LocatedElement, specific=ASM_Extension)
gen_ASM_ReturnRule_Rule = Generalization(general=Rule, specific=ASM_ReturnRule)

# Domain Model
domain_model = DomainModel(
    name="Enum",
    types={ASM_LocatedElement, ASM_XAsmFile, LocatedElement, ASM_XAsmSpec, XAsmFile, Asm, ASM_Asm, Signature, MetaInformation, Body, ASM_Signature, Argument, ASM_Body, Declaration, Initialization, Rule, ASM_MetaInformation, AccessUpdateFunction, ASM_AccessUpdateFunction, ASM_Argument, VariableDecl, Function, ASM_Declaration, ASM_Function, ElementDecl, Parameter_, Term, ASM_Parameter, ASM_Universe, Universe, ASM_Initialization, ASM_Term, ASM_Constant, ASM_FunctionOrVariableTerm, ASM_OperatorTerm, ASM_BooleanConstant, Constant, ASM_IntegerConstant, ASM_StringConstant, ASM_UndefConstant, ASM_Rule, ASM_SkipRule, ASM_AsmInvocation, ASM_UpdateRule, FunctionOrVariableTerm, ASM_ChooseRule, ASM_DoForallRule, ASM_ConditionalRule, ElseIf, ASM_ElseIf, ASM_ExtendRule, ASM_ElementDecl, ASM_VariableDecl, ASM_Extension, ASM_ReturnRule, Extension, AccessUpdateType, AsmType},
    associations={Asm0, signature1, metaInformation2, body4, arguments6, declarations7, initialization8, rules10, usedAsIn12, accessUpdateFunctions14, functions16, parameters17, initTerm18, superUniverses20, rules21, declaration23, leftExp27, rightExp29, terms24, arguments32, function34, updateTerm35, chooseId38, inSet39, guard42, ifChoosenRules45, ifNotChoosenRule48, inSet53, condition56, doRule59, condition62, thenRule64, elseRule67, id51, elseIfRule70, condition72, thenRule74, elseRule77, elseIfRule80, extensions83, rules84, elements87, universe89, term92},
    generalizations={gen_ASM_XAsmFile_LocatedElement, gen_ASM_XAsmSpec_XAsmFile, gen_ASM_Asm_LocatedElement, gen_ASM_Signature_LocatedElement, gen_ASM_Argument_VariableDecl, gen_ASM_Body_XAsmFile, gen_ASM_MetaInformation_LocatedElement, gen_ASM_AccessUpdateFunction_LocatedElement, gen_ASM_Declaration_LocatedElement, gen_ASM_Function_Declaration, gen_ASM_Function_ElementDecl, gen_ASM_Parameter_LocatedElement, gen_ASM_Universe_Declaration, gen_ASM_Initialization_LocatedElement, gen_ASM_Term_LocatedElement, gen_ASM_Constant_Term, gen_ASM_FunctionOrVariableTerm_Term, gen_ASM_OperatorTerm_Term, gen_ASM_BooleanConstant_Constant, gen_ASM_IntegerConstant_Constant, gen_ASM_StringConstant_Constant, gen_ASM_UndefConstant_Constant, gen_ASM_Rule_LocatedElement, gen_ASM_SkipRule_Rule, gen_ASM_AsmInvocation_Rule, gen_ASM_UpdateRule_Rule, gen_ASM_ChooseRule_Rule, gen_ASM_DoForallRule_Rule, gen_ASM_ConditionalRule_Rule, gen_ASM_ElseIf_LocatedElement, gen_ASM_ExtendRule_Rule, gen_ASM_ElementDecl_LocatedElement, gen_ASM_VariableDecl_ElementDecl, gen_ASM_Extension_LocatedElement, gen_ASM_ReturnRule_Rule},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)