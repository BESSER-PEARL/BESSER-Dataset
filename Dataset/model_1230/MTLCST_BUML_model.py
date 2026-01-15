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
cst_CSTNode = Class(name="cst::CSTNode", is_abstract=True)
cst_Module = Class(name="cst::Module")
EPackage = Class(name="EPackage")
CSTNode = Class(name="CSTNode")
cst_EPackage = Class(name="cst::EPackage")
cst_Comment = Class(name="cst::Comment")
ModuleElement = Class(name="ModuleElement")
TemplateExpression = Class(name="TemplateExpression")
cst_Template = Class(name="cst::Template")
Block = Class(name="Block")
cst_TemplateOverridesValue = Class(name="cst::TemplateOverridesValue")
cst_Variable = Class(name="cst::Variable")
cst_TypedModel = Class(name="cst::TypedModel")
cst_ModelExpression = Class(name="cst::ModelExpression")
cst_ModuleElement = Class(name="cst::ModuleElement", is_abstract=True)
cst_ModuleExtendsValue = Class(name="cst::ModuleExtendsValue")
cst_ModuleImportsValue = Class(name="cst::ModuleImportsValue")
cst_Documentation = Class(name="cst::Documentation")
cst_TemplateExpression = Class(name="cst::TemplateExpression")
cst_TextExpression = Class(name="cst::TextExpression")
cst_Block = Class(name="cst::Block")
cst_InitSection = Class(name="cst::InitSection")
cst_ProtectedAreaBlock = Class(name="cst::ProtectedAreaBlock")
cst_ForBlock = Class(name="cst::ForBlock")
cst_IfBlock = Class(name="cst::IfBlock")
cst_LetBlock = Class(name="cst::LetBlock")
cst_FileBlock = Class(name="cst::FileBlock")
Comment = Class(name="Comment")
cst_TraceBlock = Class(name="cst::TraceBlock")
cst_Macro = Class(name="cst::Macro")
cst_Query = Class(name="cst::Query")

# cst_CSTNode class attributes and methods
cst_CSTNode_startPosition: Property = Property(name="startPosition", type=IntegerType)
cst_CSTNode_endPosition: Property = Property(name="endPosition", type=IntegerType)
cst_CSTNode.attributes={cst_CSTNode_endPosition, cst_CSTNode_startPosition}

# cst_Module class attributes and methods

# EPackage class attributes and methods

# CSTNode class attributes and methods

# cst_EPackage class attributes and methods

# cst_Comment class attributes and methods
cst_Comment_body: Property = Property(name="body", type=StringType)
cst_Comment.attributes={cst_Comment_body}

# ModuleElement class attributes and methods

# TemplateExpression class attributes and methods

# cst_Template class attributes and methods

# Block class attributes and methods

# cst_TemplateOverridesValue class attributes and methods
cst_TemplateOverridesValue_name: Property = Property(name="name", type=StringType)
cst_TemplateOverridesValue.attributes={cst_TemplateOverridesValue_name}

# cst_Variable class attributes and methods
cst_Variable_name: Property = Property(name="name", type=StringType)
cst_Variable_type: Property = Property(name="type", type=StringType)
cst_Variable.attributes={cst_Variable_type, cst_Variable_name}

# cst_TypedModel class attributes and methods

# cst_ModelExpression class attributes and methods
cst_ModelExpression_body: Property = Property(name="body", type=StringType)
cst_ModelExpression.attributes={cst_ModelExpression_body}

# cst_ModuleElement class attributes and methods
cst_ModuleElement_name: Property = Property(name="name", type=StringType)
cst_ModuleElement_visibility: Property = Property(name="visibility", type=StringType)
cst_ModuleElement.attributes={cst_ModuleElement_name, cst_ModuleElement_visibility}

# cst_ModuleExtendsValue class attributes and methods
cst_ModuleExtendsValue_name: Property = Property(name="name", type=StringType)
cst_ModuleExtendsValue.attributes={cst_ModuleExtendsValue_name}

# cst_ModuleImportsValue class attributes and methods
cst_ModuleImportsValue_name: Property = Property(name="name", type=StringType)
cst_ModuleImportsValue.attributes={cst_ModuleImportsValue_name}

# cst_Documentation class attributes and methods

# cst_TemplateExpression class attributes and methods

# cst_TextExpression class attributes and methods
cst_TextExpression_value: Property = Property(name="value", type=StringType)
cst_TextExpression.attributes={cst_TextExpression_value}

# cst_Block class attributes and methods

# cst_InitSection class attributes and methods

# cst_ProtectedAreaBlock class attributes and methods

# cst_ForBlock class attributes and methods

# cst_IfBlock class attributes and methods

# cst_LetBlock class attributes and methods

# cst_FileBlock class attributes and methods
cst_FileBlock_openMode: Property = Property(name="openMode", type=StringType)
cst_FileBlock.attributes={cst_FileBlock_openMode}

# Comment class attributes and methods

# cst_TraceBlock class attributes and methods

# cst_Macro class attributes and methods
cst_Macro_type: Property = Property(name="type", type=StringType)
cst_Macro.attributes={cst_Macro_type}

# cst_Query class attributes and methods
cst_Query_type: Property = Property(name="type", type=StringType)
cst_Query.attributes={cst_Query_type}

# Relationships
takesTypesFrom9: BinaryAssociation = BinaryAssociation(
    name="takesTypesFrom9",
    ends={
        Property(name="cst_EPackage", type=cst_TypedModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cst_TypedModel10", type=cst_EPackage, multiplicity=Multiplicity(1, 9999))
    }
)
overrides11: BinaryAssociation = BinaryAssociation(
    name="overrides11",
    ends={
        Property(name="cst_TemplateOverridesValue", type=cst_Template, multiplicity=Multiplicity(1, 1)),
        Property(name="cst_Template", type=cst_TemplateOverridesValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter12: BinaryAssociation = BinaryAssociation(
    name="parameter12",
    ends={
        Property(name="cst_Variable", type=cst_Template, multiplicity=Multiplicity(1, 1)),
        Property(name="cst_Template13", type=cst_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
input0: BinaryAssociation = BinaryAssociation(
    name="input0",
    ends={
        Property(name="cst_TypedModel", type=cst_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="cst_Module", type=cst_TypedModel, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
guard14: BinaryAssociation = BinaryAssociation(
    name="guard14",
    ends={
        Property(name="cst_ModelExpression", type=cst_Template, multiplicity=Multiplicity(1, 1)),
        Property(name="cst_Template15", type=cst_ModelExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedModuleElement1: BinaryAssociation = BinaryAssociation(
    name="ownedModuleElement1",
    ends={
        Property(name="cst_ModuleElement", type=cst_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="cst_Module2", type=cst_ModuleElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
extends3: BinaryAssociation = BinaryAssociation(
    name="extends3",
    ends={
        Property(name="cst_ModuleExtendsValue", type=cst_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="cst_Module4", type=cst_ModuleExtendsValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
imports5: BinaryAssociation = BinaryAssociation(
    name="imports5",
    ends={
        Property(name="cst_ModuleImportsValue", type=cst_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="cst_Module6", type=cst_ModuleImportsValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
documentation7: BinaryAssociation = BinaryAssociation(
    name="documentation7",
    ends={
        Property(name="cst_Documentation", type=cst_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="cst_Module8", type=cst_Documentation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
before23: BinaryAssociation = BinaryAssociation(
    name="before23",
    ends={
        Property(name="cst_ModelExpression24", type=cst_ModelExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cst_ModelExpression22", type=cst_ModelExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
each26: BinaryAssociation = BinaryAssociation(
    name="each26",
    ends={
        Property(name="cst_ModelExpression27", type=cst_ModelExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cst_ModelExpression25", type=cst_ModelExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
after29: BinaryAssociation = BinaryAssociation(
    name="after29",
    ends={
        Property(name="cst_ModelExpression30", type=cst_ModelExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cst_ModelExpression28", type=cst_ModelExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
init31: BinaryAssociation = BinaryAssociation(
    name="init31",
    ends={
        Property(name="cst_InitSection", type=cst_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="cst_Block", type=cst_InitSection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body32: BinaryAssociation = BinaryAssociation(
    name="body32",
    ends={
        Property(name="cst_TemplateExpression", type=cst_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="cst_Block33", type=cst_TemplateExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable34: BinaryAssociation = BinaryAssociation(
    name="variable34",
    ends={
        Property(name="cst_Variable36", type=cst_InitSection, multiplicity=Multiplicity(1, 1)),
        Property(name="cst_InitSection35", type=cst_Variable, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
marker37: BinaryAssociation = BinaryAssociation(
    name="marker37",
    ends={
        Property(name="cst_ModelExpression38", type=cst_ProtectedAreaBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="cst_ProtectedAreaBlock", type=cst_ModelExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
loopVariable39: BinaryAssociation = BinaryAssociation(
    name="loopVariable39",
    ends={
        Property(name="cst_Variable40", type=cst_ForBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="cst_ForBlock", type=cst_Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
post16: BinaryAssociation = BinaryAssociation(
    name="post16",
    ends={
        Property(name="cst_ModelExpression18", type=cst_Template, multiplicity=Multiplicity(1, 1)),
        Property(name="cst_Template17", type=cst_ModelExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initExpression19: BinaryAssociation = BinaryAssociation(
    name="initExpression19",
    ends={
        Property(name="cst_ModelExpression21", type=cst_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="cst_Variable20", type=cst_ModelExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifExpr56: BinaryAssociation = BinaryAssociation(
    name="ifExpr56",
    ends={
        Property(name="cst_ModelExpression57", type=cst_IfBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="cst_IfBlock", type=cst_ModelExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
else58: BinaryAssociation = BinaryAssociation(
    name="else58",
    ends={
        Property(name="cst_Block60", type=cst_IfBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="cst_IfBlock59", type=cst_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseIf62: BinaryAssociation = BinaryAssociation(
    name="elseIf62",
    ends={
        Property(name="cst_IfBlock63", type=cst_IfBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="cst_IfBlock61", type=cst_IfBlock, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseLet65: BinaryAssociation = BinaryAssociation(
    name="elseLet65",
    ends={
        Property(name="cst_LetBlock", type=cst_LetBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="cst_LetBlock64", type=cst_LetBlock, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
else66: BinaryAssociation = BinaryAssociation(
    name="else66",
    ends={
        Property(name="cst_Block68", type=cst_LetBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="cst_LetBlock67", type=cst_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
letVariable69: BinaryAssociation = BinaryAssociation(
    name="letVariable69",
    ends={
        Property(name="cst_Variable71", type=cst_LetBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="cst_LetBlock70", type=cst_Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fileUrl72: BinaryAssociation = BinaryAssociation(
    name="fileUrl72",
    ends={
        Property(name="cst_ModelExpression73", type=cst_FileBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="cst_FileBlock", type=cst_ModelExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
uniqId74: BinaryAssociation = BinaryAssociation(
    name="uniqId74",
    ends={
        Property(name="cst_ModelExpression76", type=cst_FileBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="cst_FileBlock75", type=cst_ModelExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
charset77: BinaryAssociation = BinaryAssociation(
    name="charset77",
    ends={
        Property(name="cst_ModelExpression79", type=cst_FileBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="cst_FileBlock78", type=cst_ModelExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
iterSet41: BinaryAssociation = BinaryAssociation(
    name="iterSet41",
    ends={
        Property(name="cst_ModelExpression43", type=cst_ForBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="cst_ForBlock42", type=cst_ModelExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
before44: BinaryAssociation = BinaryAssociation(
    name="before44",
    ends={
        Property(name="cst_ModelExpression46", type=cst_ForBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="cst_ForBlock45", type=cst_ModelExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
each47: BinaryAssociation = BinaryAssociation(
    name="each47",
    ends={
        Property(name="cst_ModelExpression49", type=cst_ForBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="cst_ForBlock48", type=cst_ModelExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
after50: BinaryAssociation = BinaryAssociation(
    name="after50",
    ends={
        Property(name="cst_ModelExpression52", type=cst_ForBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="cst_ForBlock51", type=cst_ModelExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
guard53: BinaryAssociation = BinaryAssociation(
    name="guard53",
    ends={
        Property(name="cst_ModelExpression55", type=cst_ForBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="cst_ForBlock54", type=cst_ModelExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameter84: BinaryAssociation = BinaryAssociation(
    name="parameter84",
    ends={
        Property(name="cst_Variable85", type=cst_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="cst_Query", type=cst_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression86: BinaryAssociation = BinaryAssociation(
    name="expression86",
    ends={
        Property(name="cst_ModelExpression88", type=cst_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="cst_Query87", type=cst_ModelExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modelElement80: BinaryAssociation = BinaryAssociation(
    name="modelElement80",
    ends={
        Property(name="cst_ModelExpression81", type=cst_TraceBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="cst_TraceBlock", type=cst_ModelExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameter82: BinaryAssociation = BinaryAssociation(
    name="parameter82",
    ends={
        Property(name="cst_Variable83", type=cst_Macro, multiplicity=Multiplicity(1, 1)),
        Property(name="cst_Macro", type=cst_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_cst_Module_EPackage = Generalization(general=EPackage, specific=cst_Module)
gen_cst_Module_CSTNode = Generalization(general=CSTNode, specific=cst_Module)
gen_cst_ModuleExtendsValue_CSTNode = Generalization(general=CSTNode, specific=cst_ModuleExtendsValue)
gen_cst_ModuleImportsValue_CSTNode = Generalization(general=CSTNode, specific=cst_ModuleImportsValue)
gen_cst_TypedModel_CSTNode = Generalization(general=CSTNode, specific=cst_TypedModel)
gen_cst_ModuleElement_CSTNode = Generalization(general=CSTNode, specific=cst_ModuleElement)
gen_cst_Comment_ModuleElement = Generalization(general=ModuleElement, specific=cst_Comment)
gen_cst_Comment_TemplateExpression = Generalization(general=TemplateExpression, specific=cst_Comment)
gen_cst_Template_Block = Generalization(general=Block, specific=cst_Template)
gen_cst_Template_ModuleElement = Generalization(general=ModuleElement, specific=cst_Template)
gen_cst_TemplateExpression_CSTNode = Generalization(general=CSTNode, specific=cst_TemplateExpression)
gen_cst_ModelExpression_TemplateExpression = Generalization(general=TemplateExpression, specific=cst_ModelExpression)
gen_cst_TextExpression_TemplateExpression = Generalization(general=TemplateExpression, specific=cst_TextExpression)
gen_cst_Block_TemplateExpression = Generalization(general=TemplateExpression, specific=cst_Block)
gen_cst_InitSection_CSTNode = Generalization(general=CSTNode, specific=cst_InitSection)
gen_cst_ProtectedAreaBlock_Block = Generalization(general=Block, specific=cst_ProtectedAreaBlock)
gen_cst_ForBlock_Block = Generalization(general=Block, specific=cst_ForBlock)
gen_cst_TemplateOverridesValue_CSTNode = Generalization(general=CSTNode, specific=cst_TemplateOverridesValue)
gen_cst_Variable_CSTNode = Generalization(general=CSTNode, specific=cst_Variable)
gen_cst_IfBlock_Block = Generalization(general=Block, specific=cst_IfBlock)
gen_cst_LetBlock_Block = Generalization(general=Block, specific=cst_LetBlock)
gen_cst_FileBlock_Block = Generalization(general=Block, specific=cst_FileBlock)
gen_cst_Documentation_Comment = Generalization(general=Comment, specific=cst_Documentation)
gen_cst_TraceBlock_Block = Generalization(general=Block, specific=cst_TraceBlock)
gen_cst_Macro_Block = Generalization(general=Block, specific=cst_Macro)
gen_cst_Macro_ModuleElement = Generalization(general=ModuleElement, specific=cst_Macro)
gen_cst_Query_ModuleElement = Generalization(general=ModuleElement, specific=cst_Query)

# Domain Model
domain_model = DomainModel(
    name="cst",
    types={cst_CSTNode, cst_Module, EPackage, CSTNode, cst_EPackage, cst_Comment, ModuleElement, TemplateExpression, cst_Template, Block, cst_TemplateOverridesValue, cst_Variable, cst_TypedModel, cst_ModelExpression, cst_ModuleElement, cst_ModuleExtendsValue, cst_ModuleImportsValue, cst_Documentation, cst_TemplateExpression, cst_TextExpression, cst_Block, cst_InitSection, cst_ProtectedAreaBlock, cst_ForBlock, cst_IfBlock, cst_LetBlock, cst_FileBlock, Comment, cst_TraceBlock, cst_Macro, cst_Query, VisibilityKind, OpenModeKind},
    associations={takesTypesFrom9, overrides11, parameter12, input0, guard14, ownedModuleElement1, extends3, imports5, documentation7, before23, each26, after29, init31, body32, variable34, marker37, loopVariable39, post16, initExpression19, ifExpr56, else58, elseIf62, elseLet65, else66, letVariable69, fileUrl72, uniqId74, charset77, iterSet41, before44, each47, after50, guard53, parameter84, expression86, modelElement80, parameter82},
    generalizations={gen_cst_Module_EPackage, gen_cst_Module_CSTNode, gen_cst_ModuleExtendsValue_CSTNode, gen_cst_ModuleImportsValue_CSTNode, gen_cst_TypedModel_CSTNode, gen_cst_ModuleElement_CSTNode, gen_cst_Comment_ModuleElement, gen_cst_Comment_TemplateExpression, gen_cst_Template_Block, gen_cst_Template_ModuleElement, gen_cst_TemplateExpression_CSTNode, gen_cst_ModelExpression_TemplateExpression, gen_cst_TextExpression_TemplateExpression, gen_cst_Block_TemplateExpression, gen_cst_InitSection_CSTNode, gen_cst_ProtectedAreaBlock_Block, gen_cst_ForBlock_Block, gen_cst_TemplateOverridesValue_CSTNode, gen_cst_Variable_CSTNode, gen_cst_IfBlock_Block, gen_cst_LetBlock_Block, gen_cst_FileBlock_Block, gen_cst_Documentation_Comment, gen_cst_TraceBlock_Block, gen_cst_Macro_Block, gen_cst_Macro_ModuleElement, gen_cst_Query_ModuleElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)