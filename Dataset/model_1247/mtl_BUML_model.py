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
VisibilityKind: Enumeration = Enumeration(
    name="VisibilityKind",
    literals={
            EnumerationLiteral(name="Private"),
			EnumerationLiteral(name="Protected"),
			EnumerationLiteral(name="Public")
    }
)

OpenModeKind: Enumeration = Enumeration(
    name="OpenModeKind",
    literals={
            EnumerationLiteral(name="Append"),
			EnumerationLiteral(name="OverWrite")
    }
)

# Classes
mtl_Module = Class(name="mtl::Module")
EPackage = Class(name="EPackage")
DocumentedElement = Class(name="DocumentedElement")
mtl_TypedModel = Class(name="mtl::TypedModel")
mtl_Block = Class(name="mtl::Block")
TemplateExpression = Class(name="TemplateExpression")
mtl_InitSection = Class(name="mtl::InitSection")
ASTNode = Class(name="ASTNode")
Variable = Class(name="Variable")
mtl_Template = Class(name="mtl::Template")
Block = Class(name="Block")
ModuleElement = Class(name="ModuleElement")
mtl_ModuleElement = Class(name="mtl::ModuleElement", is_abstract=True)
ENamedElement = Class(name="ENamedElement")
utilities_ASTNode = Class(name="utilities::ASTNode")
mtl_TemplateExpression = Class(name="mtl::TemplateExpression")
OCLExpression = Class(name="OCLExpression")
mtl_EClassifier = Class(name="mtl::EClassifier")
mtl_QueryInvocation = Class(name="mtl::QueryInvocation")
mtl_ProtectedAreaBlock = Class(name="mtl::ProtectedAreaBlock")
mtl_ForBlock = Class(name="mtl::ForBlock")
mtl_TemplateInvocation = Class(name="mtl::TemplateInvocation")
mtl_Query = Class(name="mtl::Query")
mtl_LetBlock = Class(name="mtl::LetBlock")
mtl_FileBlock = Class(name="mtl::FileBlock")
mtl_IfBlock = Class(name="mtl::IfBlock")
mtl_MacroInvocation = Class(name="mtl::MacroInvocation")
mtl_EPackage = Class(name="mtl::EPackage")
mtl_Comment = Class(name="mtl::Comment")
mtl_CommentBody = Class(name="mtl::CommentBody")
mtl_Documentation = Class(name="mtl::Documentation")
Comment = Class(name="Comment")
mtl_DocumentedElement = Class(name="mtl::DocumentedElement", is_abstract=True)
mtl_TraceBlock = Class(name="mtl::TraceBlock")
mtl_ModuleDocumentation = Class(name="mtl::ModuleDocumentation")
Documentation = Class(name="Documentation")
mtl_Macro = Class(name="mtl::Macro")
mtl_ModuleElementDocumentation = Class(name="mtl::ModuleElementDocumentation")
mtl_ParameterDocumentation = Class(name="mtl::ParameterDocumentation")

# mtl_Module class attributes and methods
mtl_Module_startHeaderPosition: Property = Property(name="startHeaderPosition", type=IntegerType)
mtl_Module_endHeaderPosition: Property = Property(name="endHeaderPosition", type=IntegerType)
mtl_Module.attributes={mtl_Module_endHeaderPosition, mtl_Module_startHeaderPosition}

# EPackage class attributes and methods

# DocumentedElement class attributes and methods

# mtl_TypedModel class attributes and methods

# mtl_Block class attributes and methods

# TemplateExpression class attributes and methods

# mtl_InitSection class attributes and methods

# ASTNode class attributes and methods

# Variable class attributes and methods

# mtl_Template class attributes and methods
mtl_Template_main: Property = Property(name="main", type=BooleanType)
mtl_Template.attributes={mtl_Template_main}

# Block class attributes and methods

# ModuleElement class attributes and methods

# mtl_ModuleElement class attributes and methods
mtl_ModuleElement_visibility: Property = Property(name="visibility", type=StringType)
mtl_ModuleElement.attributes={mtl_ModuleElement_visibility}

# ENamedElement class attributes and methods

# utilities_ASTNode class attributes and methods

# mtl_TemplateExpression class attributes and methods

# OCLExpression class attributes and methods

# mtl_EClassifier class attributes and methods

# mtl_QueryInvocation class attributes and methods

# mtl_ProtectedAreaBlock class attributes and methods

# mtl_ForBlock class attributes and methods

# mtl_TemplateInvocation class attributes and methods
mtl_TemplateInvocation_super: Property = Property(name="super", type=BooleanType)
mtl_TemplateInvocation.attributes={mtl_TemplateInvocation_super}

# mtl_Query class attributes and methods

# mtl_LetBlock class attributes and methods

# mtl_FileBlock class attributes and methods
mtl_FileBlock_openMode: Property = Property(name="openMode", type=StringType)
mtl_FileBlock.attributes={mtl_FileBlock_openMode}

# mtl_IfBlock class attributes and methods

# mtl_MacroInvocation class attributes and methods

# mtl_EPackage class attributes and methods

# mtl_Comment class attributes and methods

# mtl_CommentBody class attributes and methods
mtl_CommentBody_startPosition: Property = Property(name="startPosition", type=IntegerType)
mtl_CommentBody_endPosition: Property = Property(name="endPosition", type=IntegerType)
mtl_CommentBody_value: Property = Property(name="value", type=StringType)
mtl_CommentBody.attributes={mtl_CommentBody_value, mtl_CommentBody_endPosition, mtl_CommentBody_startPosition}

# mtl_Documentation class attributes and methods

# Comment class attributes and methods

# mtl_DocumentedElement class attributes and methods
mtl_DocumentedElement_deprecated: Property = Property(name="deprecated", type=BooleanType)
mtl_DocumentedElement.attributes={mtl_DocumentedElement_deprecated}

# mtl_TraceBlock class attributes and methods

# mtl_ModuleDocumentation class attributes and methods
mtl_ModuleDocumentation_author: Property = Property(name="author", type=StringType)
mtl_ModuleDocumentation_version: Property = Property(name="version", type=StringType)
mtl_ModuleDocumentation_since: Property = Property(name="since", type=StringType)
mtl_ModuleDocumentation.attributes={mtl_ModuleDocumentation_author, mtl_ModuleDocumentation_version, mtl_ModuleDocumentation_since}

# Documentation class attributes and methods

# mtl_Macro class attributes and methods

# mtl_ModuleElementDocumentation class attributes and methods

# mtl_ParameterDocumentation class attributes and methods

# Relationships
input0: BinaryAssociation = BinaryAssociation(
    name="input0",
    ends={
        Property(name="mtl_TypedModel", type=mtl_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="mtl_Module", type=mtl_TypedModel, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
extends2: BinaryAssociation = BinaryAssociation(
    name="extends2",
    ends={
        Property(name="mtl_Module3", type=mtl_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="mtl_Module1", type=mtl_Module, multiplicity=Multiplicity(0, 9999))
    }
)
init9: BinaryAssociation = BinaryAssociation(
    name="init9",
    ends={
        Property(name="mtl_InitSection", type=mtl_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="mtl_Block", type=mtl_InitSection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body10: BinaryAssociation = BinaryAssociation(
    name="body10",
    ends={
        Property(name="OCLExpression", type=mtl_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="mtl_Block11", type=OCLExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable12: BinaryAssociation = BinaryAssociation(
    name="variable12",
    ends={
        Property(name="Variable", type=mtl_InitSection, multiplicity=Multiplicity(1, 1)),
        Property(name="mtl_InitSection13", type=Variable, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
overrides15: BinaryAssociation = BinaryAssociation(
    name="overrides15",
    ends={
        Property(name="mtl_Template", type=mtl_Template, multiplicity=Multiplicity(1, 1)),
        Property(name="mtl_Template14", type=mtl_Template, multiplicity=Multiplicity(0, 9999))
    }
)
parameter16: BinaryAssociation = BinaryAssociation(
    name="parameter16",
    ends={
        Property(name="Variable18", type=mtl_Template, multiplicity=Multiplicity(1, 1)),
        Property(name="mtl_Template17", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
imports5: BinaryAssociation = BinaryAssociation(
    name="imports5",
    ends={
        Property(name="mtl_Module6", type=mtl_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="mtl_Module4", type=mtl_Module, multiplicity=Multiplicity(0, 9999))
    }
)
ownedModuleElement7: BinaryAssociation = BinaryAssociation(
    name="ownedModuleElement7",
    ends={
        Property(name="mtl_ModuleElement", type=mtl_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="mtl_Module8", type=mtl_ModuleElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
parameter39: BinaryAssociation = BinaryAssociation(
    name="parameter39",
    ends={
        Property(name="Variable40", type=mtl_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="mtl_Query", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression41: BinaryAssociation = BinaryAssociation(
    name="expression41",
    ends={
        Property(name="OCLExpression43", type=mtl_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="mtl_Query42", type=OCLExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type44: BinaryAssociation = BinaryAssociation(
    name="type44",
    ends={
        Property(name="mtl_EClassifier", type=mtl_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="mtl_Query45", type=mtl_EClassifier, multiplicity=Multiplicity(1, 1))
    }
)
definition46: BinaryAssociation = BinaryAssociation(
    name="definition46",
    ends={
        Property(name="mtl_Query47", type=mtl_QueryInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="mtl_QueryInvocation", type=mtl_Query, multiplicity=Multiplicity(1, 1))
    }
)
argument48: BinaryAssociation = BinaryAssociation(
    name="argument48",
    ends={
        Property(name="OCLExpression50", type=mtl_QueryInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="mtl_QueryInvocation49", type=OCLExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
marker51: BinaryAssociation = BinaryAssociation(
    name="marker51",
    ends={
        Property(name="OCLExpression52", type=mtl_ProtectedAreaBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="mtl_ProtectedAreaBlock", type=OCLExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
guard19: BinaryAssociation = BinaryAssociation(
    name="guard19",
    ends={
        Property(name="OCLExpression21", type=mtl_Template, multiplicity=Multiplicity(1, 1)),
        Property(name="mtl_Template20", type=OCLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
loopVariable53: BinaryAssociation = BinaryAssociation(
    name="loopVariable53",
    ends={
        Property(name="Variable54", type=mtl_ForBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="mtl_ForBlock", type=Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
post22: BinaryAssociation = BinaryAssociation(
    name="post22",
    ends={
        Property(name="OCLExpression24", type=mtl_Template, multiplicity=Multiplicity(1, 1)),
        Property(name="mtl_Template23", type=OCLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definition25: BinaryAssociation = BinaryAssociation(
    name="definition25",
    ends={
        Property(name="mtl_Template26", type=mtl_TemplateInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="mtl_TemplateInvocation", type=mtl_Template, multiplicity=Multiplicity(1, 1))
    }
)
argument27: BinaryAssociation = BinaryAssociation(
    name="argument27",
    ends={
        Property(name="OCLExpression29", type=mtl_TemplateInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="mtl_TemplateInvocation28", type=OCLExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
before30: BinaryAssociation = BinaryAssociation(
    name="before30",
    ends={
        Property(name="OCLExpression32", type=mtl_TemplateInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="mtl_TemplateInvocation31", type=OCLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
after33: BinaryAssociation = BinaryAssociation(
    name="after33",
    ends={
        Property(name="OCLExpression35", type=mtl_TemplateInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="mtl_TemplateInvocation34", type=OCLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
each36: BinaryAssociation = BinaryAssociation(
    name="each36",
    ends={
        Property(name="OCLExpression38", type=mtl_TemplateInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="mtl_TemplateInvocation37", type=OCLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifExpr70: BinaryAssociation = BinaryAssociation(
    name="ifExpr70",
    ends={
        Property(name="OCLExpression71", type=mtl_IfBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="mtl_IfBlock", type=OCLExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
else72: BinaryAssociation = BinaryAssociation(
    name="else72",
    ends={
        Property(name="mtl_Block74", type=mtl_IfBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="mtl_IfBlock73", type=mtl_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseIf76: BinaryAssociation = BinaryAssociation(
    name="elseIf76",
    ends={
        Property(name="mtl_IfBlock77", type=mtl_IfBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="mtl_IfBlock75", type=mtl_IfBlock, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseLet79: BinaryAssociation = BinaryAssociation(
    name="elseLet79",
    ends={
        Property(name="mtl_LetBlock", type=mtl_LetBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="mtl_LetBlock78", type=mtl_LetBlock, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
else80: BinaryAssociation = BinaryAssociation(
    name="else80",
    ends={
        Property(name="mtl_Block82", type=mtl_LetBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="mtl_LetBlock81", type=mtl_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
letVariable83: BinaryAssociation = BinaryAssociation(
    name="letVariable83",
    ends={
        Property(name="Variable85", type=mtl_LetBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="mtl_LetBlock84", type=Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fileUrl86: BinaryAssociation = BinaryAssociation(
    name="fileUrl86",
    ends={
        Property(name="OCLExpression87", type=mtl_FileBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="mtl_FileBlock", type=OCLExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
uniqId88: BinaryAssociation = BinaryAssociation(
    name="uniqId88",
    ends={
        Property(name="OCLExpression90", type=mtl_FileBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="mtl_FileBlock89", type=OCLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
iterSet55: BinaryAssociation = BinaryAssociation(
    name="iterSet55",
    ends={
        Property(name="OCLExpression57", type=mtl_ForBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="mtl_ForBlock56", type=OCLExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
before58: BinaryAssociation = BinaryAssociation(
    name="before58",
    ends={
        Property(name="OCLExpression60", type=mtl_ForBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="mtl_ForBlock59", type=OCLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
each61: BinaryAssociation = BinaryAssociation(
    name="each61",
    ends={
        Property(name="OCLExpression63", type=mtl_ForBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="mtl_ForBlock62", type=OCLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
after64: BinaryAssociation = BinaryAssociation(
    name="after64",
    ends={
        Property(name="OCLExpression66", type=mtl_ForBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="mtl_ForBlock65", type=OCLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
guard67: BinaryAssociation = BinaryAssociation(
    name="guard67",
    ends={
        Property(name="OCLExpression69", type=mtl_ForBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="mtl_ForBlock68", type=OCLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definition101: BinaryAssociation = BinaryAssociation(
    name="definition101",
    ends={
        Property(name="mtl_Macro102", type=mtl_MacroInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="mtl_MacroInvocation", type=mtl_Macro, multiplicity=Multiplicity(1, 1))
    }
)
argument103: BinaryAssociation = BinaryAssociation(
    name="argument103",
    ends={
        Property(name="OCLExpression105", type=mtl_MacroInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="mtl_MacroInvocation104", type=OCLExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
takesTypesFrom106: BinaryAssociation = BinaryAssociation(
    name="takesTypesFrom106",
    ends={
        Property(name="mtl_EPackage", type=mtl_TypedModel, multiplicity=Multiplicity(1, 1)),
        Property(name="mtl_TypedModel107", type=mtl_EPackage, multiplicity=Multiplicity(1, 9999))
    }
)
body108: BinaryAssociation = BinaryAssociation(
    name="body108",
    ends={
        Property(name="mtl_CommentBody", type=mtl_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="mtl_Comment", type=mtl_CommentBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
documentedElement109: BinaryAssociation = BinaryAssociation(
    name="documentedElement109",
    ends={
        Property(name="DocumentedElement", type=mtl_Documentation, multiplicity=Multiplicity(1, 1)),
        Property(name="documentation", type=mtl_DocumentedElement, multiplicity=Multiplicity(0, 1))
    }
)
documentation110: BinaryAssociation = BinaryAssociation(
    name="documentation110",
    ends={
        Property(name="Documentation", type=mtl_DocumentedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="documentedElement", type=mtl_Documentation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
charset91: BinaryAssociation = BinaryAssociation(
    name="charset91",
    ends={
        Property(name="OCLExpression93", type=mtl_FileBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="mtl_FileBlock92", type=OCLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modelElement94: BinaryAssociation = BinaryAssociation(
    name="modelElement94",
    ends={
        Property(name="OCLExpression95", type=mtl_TraceBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="mtl_TraceBlock", type=OCLExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameter96: BinaryAssociation = BinaryAssociation(
    name="parameter96",
    ends={
        Property(name="Variable97", type=mtl_Macro, multiplicity=Multiplicity(1, 1)),
        Property(name="mtl_Macro", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parametersDocumentation111: BinaryAssociation = BinaryAssociation(
    name="parametersDocumentation111",
    ends={
        Property(name="mtl_ParameterDocumentation", type=mtl_ModuleElementDocumentation, multiplicity=Multiplicity(1, 1)),
        Property(name="mtl_ModuleElementDocumentation", type=mtl_ParameterDocumentation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type98: BinaryAssociation = BinaryAssociation(
    name="type98",
    ends={
        Property(name="mtl_EClassifier100", type=mtl_Macro, multiplicity=Multiplicity(1, 1)),
        Property(name="mtl_Macro99", type=mtl_EClassifier, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_mtl_Module_EPackage = Generalization(general=EPackage, specific=mtl_Module)
gen_mtl_Module_DocumentedElement = Generalization(general=DocumentedElement, specific=mtl_Module)
gen_mtl_Block_TemplateExpression = Generalization(general=TemplateExpression, specific=mtl_Block)
gen_mtl_InitSection_ASTNode = Generalization(general=ASTNode, specific=mtl_InitSection)
gen_mtl_Template_Block = Generalization(general=Block, specific=mtl_Template)
gen_mtl_Template_ModuleElement = Generalization(general=ModuleElement, specific=mtl_Template)
gen_mtl_Template_DocumentedElement = Generalization(general=DocumentedElement, specific=mtl_Template)
gen_mtl_ModuleElement_ENamedElement = Generalization(general=ENamedElement, specific=mtl_ModuleElement)
gen_mtl_ModuleElement_utilities_ASTNode = Generalization(general=utilities_ASTNode, specific=mtl_ModuleElement)
gen_mtl_Query_DocumentedElement = Generalization(general=DocumentedElement, specific=mtl_Query)
gen_mtl_TemplateExpression_OCLExpression = Generalization(general=OCLExpression, specific=mtl_TemplateExpression)
gen_mtl_QueryInvocation_TemplateExpression = Generalization(general=TemplateExpression, specific=mtl_QueryInvocation)
gen_mtl_ProtectedAreaBlock_Block = Generalization(general=Block, specific=mtl_ProtectedAreaBlock)
gen_mtl_ForBlock_Block = Generalization(general=Block, specific=mtl_ForBlock)
gen_mtl_TemplateInvocation_TemplateExpression = Generalization(general=TemplateExpression, specific=mtl_TemplateInvocation)
gen_mtl_Query_ModuleElement = Generalization(general=ModuleElement, specific=mtl_Query)
gen_mtl_LetBlock_Block = Generalization(general=Block, specific=mtl_LetBlock)
gen_mtl_FileBlock_Block = Generalization(general=Block, specific=mtl_FileBlock)
gen_mtl_IfBlock_Block = Generalization(general=Block, specific=mtl_IfBlock)
gen_mtl_MacroInvocation_TemplateExpression = Generalization(general=TemplateExpression, specific=mtl_MacroInvocation)
gen_mtl_Comment_ModuleElement = Generalization(general=ModuleElement, specific=mtl_Comment)
gen_mtl_Documentation_Comment = Generalization(general=Comment, specific=mtl_Documentation)
gen_mtl_TraceBlock_Block = Generalization(general=Block, specific=mtl_TraceBlock)
gen_mtl_ModuleDocumentation_Documentation = Generalization(general=Documentation, specific=mtl_ModuleDocumentation)
gen_mtl_Macro_Block = Generalization(general=Block, specific=mtl_Macro)
gen_mtl_Macro_ModuleElement = Generalization(general=ModuleElement, specific=mtl_Macro)
gen_mtl_Macro_DocumentedElement = Generalization(general=DocumentedElement, specific=mtl_Macro)
gen_mtl_ModuleElementDocumentation_Documentation = Generalization(general=Documentation, specific=mtl_ModuleElementDocumentation)
gen_mtl_ParameterDocumentation_Comment = Generalization(general=Comment, specific=mtl_ParameterDocumentation)

# Domain Model
domain_model = DomainModel(
    name="mtl",
    types={mtl_Module, EPackage, DocumentedElement, mtl_TypedModel, mtl_Block, TemplateExpression, mtl_InitSection, ASTNode, Variable, mtl_Template, Block, ModuleElement, mtl_ModuleElement, ENamedElement, utilities_ASTNode, mtl_TemplateExpression, OCLExpression, mtl_EClassifier, mtl_QueryInvocation, mtl_ProtectedAreaBlock, mtl_ForBlock, mtl_TemplateInvocation, mtl_Query, mtl_LetBlock, mtl_FileBlock, mtl_IfBlock, mtl_MacroInvocation, mtl_EPackage, mtl_Comment, mtl_CommentBody, mtl_Documentation, Comment, mtl_DocumentedElement, mtl_TraceBlock, mtl_ModuleDocumentation, Documentation, mtl_Macro, mtl_ModuleElementDocumentation, mtl_ParameterDocumentation, VisibilityKind, OpenModeKind},
    associations={input0, extends2, init9, body10, variable12, overrides15, parameter16, imports5, ownedModuleElement7, parameter39, expression41, type44, definition46, argument48, marker51, guard19, loopVariable53, post22, definition25, argument27, before30, after33, each36, ifExpr70, else72, elseIf76, elseLet79, else80, letVariable83, fileUrl86, uniqId88, iterSet55, before58, each61, after64, guard67, definition101, argument103, takesTypesFrom106, body108, documentedElement109, documentation110, charset91, modelElement94, parameter96, parametersDocumentation111, type98},
    generalizations={gen_mtl_Module_EPackage, gen_mtl_Module_DocumentedElement, gen_mtl_Block_TemplateExpression, gen_mtl_InitSection_ASTNode, gen_mtl_Template_Block, gen_mtl_Template_ModuleElement, gen_mtl_Template_DocumentedElement, gen_mtl_ModuleElement_ENamedElement, gen_mtl_ModuleElement_utilities_ASTNode, gen_mtl_Query_DocumentedElement, gen_mtl_TemplateExpression_OCLExpression, gen_mtl_QueryInvocation_TemplateExpression, gen_mtl_ProtectedAreaBlock_Block, gen_mtl_ForBlock_Block, gen_mtl_TemplateInvocation_TemplateExpression, gen_mtl_Query_ModuleElement, gen_mtl_LetBlock_Block, gen_mtl_FileBlock_Block, gen_mtl_IfBlock_Block, gen_mtl_MacroInvocation_TemplateExpression, gen_mtl_Comment_ModuleElement, gen_mtl_Documentation_Comment, gen_mtl_TraceBlock_Block, gen_mtl_ModuleDocumentation_Documentation, gen_mtl_Macro_Block, gen_mtl_Macro_ModuleElement, gen_mtl_Macro_DocumentedElement, gen_mtl_ModuleElementDocumentation_Documentation, gen_mtl_ParameterDocumentation_Comment},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)