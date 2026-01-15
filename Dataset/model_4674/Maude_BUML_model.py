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
ImportationMode: Enumeration = Enumeration(
    name="ImportationMode",
    literals={
            EnumerationLiteral(name="protecting"),
			EnumerationLiteral(name="including"),
			EnumerationLiteral(name="extending")
    }
)

# Classes
Maude_TheoryIdModExp = Class(name="Maude::TheoryIdModExp")
Maude_Theory = Class(name="Maude::Theory", is_abstract=True)
Maude_MaudeSpec = Class(name="Maude::MaudeSpec")
Maude_MaudeTopEl = Class(name="Maude::MaudeTopEl", is_abstract=True)
Maude_ModExpression = Class(name="Maude::ModExpression", is_abstract=True)
Maude_InstModExp = Class(name="Maude::InstModExp")
ModExpression = Class(name="ModExpression")
Maude_View = Class(name="Maude::View")
Maude_RenModExp = Class(name="Maude::RenModExp")
Maude_RenMapping = Class(name="Maude::RenMapping", is_abstract=True)
Maude_CompModExp = Class(name="Maude::CompModExp")
Maude_ModuleIdModExp = Class(name="Maude::ModuleIdModExp")
Maude_Module = Class(name="Maude::Module", is_abstract=True)
Maude_Parameter = Class(name="Maude::Parameter")
MaudeTopEl = Class(name="MaudeTopEl")
Maude_ModElement = Class(name="Maude::ModElement", is_abstract=True)
Maude_FTheory = Class(name="Maude::FTheory")
Theory = Class(name="Theory")
Maude_STheory = Class(name="Maude::STheory")
Maude_FModule = Class(name="Maude::FModule")
Module = Class(name="Module")
Maude_SModule = Class(name="Maude::SModule")
Maude_ModImportation = Class(name="Maude::ModImportation")
ModElement = Class(name="ModElement")
Maude_Type = Class(name="Maude::Type", is_abstract=True)
Maude_Sort = Class(name="Maude::Sort")
Type = Class(name="Type")
Maude_SubsortRel = Class(name="Maude::SubsortRel")
Maude_Kind = Class(name="Maude::Kind")
Maude_MembershipCond = Class(name="Maude::MembershipCond")
EquationalCond = Class(name="EquationalCond")
Maude_BooleanCond = Class(name="Maude::BooleanCond")
Maude_MatchingCond = Class(name="Maude::MatchingCond")
Maude_Operation = Class(name="Maude::Operation")
Maude_Statement = Class(name="Maude::Statement", is_abstract=True)
Maude_Condition = Class(name="Maude::Condition", is_abstract=True)
Maude_Membership = Class(name="Maude::Membership")
Statement = Class(name="Statement")
Maude_Term = Class(name="Maude::Term", is_abstract=True)
Maude_Equation = Class(name="Maude::Equation")
Maude_Rule = Class(name="Maude::Rule")
Maude_EquationalCond = Class(name="Maude::EquationalCond", is_abstract=True)
Condition = Class(name="Condition")
Maude_RewriteCond = Class(name="Maude::RewriteCond")
Maude_OpTypedMapping = Class(name="Maude::OpTypedMapping")
Maude_EqualCond = Class(name="Maude::EqualCond")
Maude_Constant = Class(name="Maude::Constant")
Term = Class(name="Term")
Maude_RecTerm = Class(name="Maude::RecTerm")
Maude_Variable = Class(name="Maude::Variable")
Maude_ViewMapping = Class(name="Maude::ViewMapping", is_abstract=True)
ViewMapping = Class(name="ViewMapping")
Maude_TermMapping = Class(name="Maude::TermMapping")
Maude_SortMapping = Class(name="Maude::SortMapping")
RenMapping = Class(name="RenMapping")
Maude_OpMapping = Class(name="Maude::OpMapping")
Maude_LabelMapping = Class(name="Maude::LabelMapping")

# Maude_TheoryIdModExp class attributes and methods

# Maude_Theory class attributes and methods

# Maude_MaudeSpec class attributes and methods

# Maude_MaudeTopEl class attributes and methods
Maude_MaudeTopEl_name: Property = Property(name="name", type=StringType)
Maude_MaudeTopEl.attributes={Maude_MaudeTopEl_name}

# Maude_ModExpression class attributes and methods

# Maude_InstModExp class attributes and methods

# ModExpression class attributes and methods

# Maude_View class attributes and methods

# Maude_RenModExp class attributes and methods

# Maude_RenMapping class attributes and methods

# Maude_CompModExp class attributes and methods

# Maude_ModuleIdModExp class attributes and methods

# Maude_Module class attributes and methods

# Maude_Parameter class attributes and methods
Maude_Parameter_label: Property = Property(name="label", type=StringType)
Maude_Parameter.attributes={Maude_Parameter_label}

# MaudeTopEl class attributes and methods

# Maude_ModElement class attributes and methods

# Maude_FTheory class attributes and methods

# Theory class attributes and methods

# Maude_STheory class attributes and methods

# Maude_FModule class attributes and methods

# Module class attributes and methods

# Maude_SModule class attributes and methods

# Maude_ModImportation class attributes and methods
Maude_ModImportation_mode: Property = Property(name="mode", type=StringType)
Maude_ModImportation.attributes={Maude_ModImportation_mode}

# ModElement class attributes and methods

# Maude_Type class attributes and methods
Maude_Type_name: Property = Property(name="name", type=StringType)
Maude_Type.attributes={Maude_Type_name}

# Maude_Sort class attributes and methods

# Type class attributes and methods

# Maude_SubsortRel class attributes and methods

# Maude_Kind class attributes and methods

# Maude_MembershipCond class attributes and methods

# EquationalCond class attributes and methods

# Maude_BooleanCond class attributes and methods

# Maude_MatchingCond class attributes and methods

# Maude_Operation class attributes and methods
Maude_Operation_name: Property = Property(name="name", type=StringType)
Maude_Operation_atts: Property = Property(name="atts", type=StringType)
Maude_Operation.attributes={Maude_Operation_name, Maude_Operation_atts}

# Maude_Statement class attributes and methods
Maude_Statement_label: Property = Property(name="label", type=StringType)
Maude_Statement_atts: Property = Property(name="atts", type=StringType)
Maude_Statement.attributes={Maude_Statement_atts, Maude_Statement_label}

# Maude_Condition class attributes and methods

# Maude_Membership class attributes and methods

# Statement class attributes and methods

# Maude_Term class attributes and methods

# Maude_Equation class attributes and methods

# Maude_Rule class attributes and methods

# Maude_EquationalCond class attributes and methods

# Condition class attributes and methods

# Maude_RewriteCond class attributes and methods

# Maude_OpTypedMapping class attributes and methods
Maude_OpTypedMapping_to: Property = Property(name="to", type=StringType)
Maude_OpTypedMapping_atts: Property = Property(name="atts", type=StringType)
Maude_OpTypedMapping.attributes={Maude_OpTypedMapping_atts, Maude_OpTypedMapping_to}

# Maude_EqualCond class attributes and methods

# Maude_Constant class attributes and methods
Maude_Constant_op: Property = Property(name="op", type=StringType)
Maude_Constant.attributes={Maude_Constant_op}

# Term class attributes and methods

# Maude_RecTerm class attributes and methods
Maude_RecTerm_op: Property = Property(name="op", type=StringType)
Maude_RecTerm.attributes={Maude_RecTerm_op}

# Maude_Variable class attributes and methods
Maude_Variable_name: Property = Property(name="name", type=StringType)
Maude_Variable.attributes={Maude_Variable_name}

# Maude_ViewMapping class attributes and methods

# ViewMapping class attributes and methods

# Maude_TermMapping class attributes and methods

# Maude_SortMapping class attributes and methods
Maude_SortMapping_to: Property = Property(name="to", type=StringType)
Maude_SortMapping.attributes={Maude_SortMapping_to}

# RenMapping class attributes and methods

# Maude_OpMapping class attributes and methods
Maude_OpMapping_to: Property = Property(name="to", type=StringType)
Maude_OpMapping.attributes={Maude_OpMapping_to}

# Maude_LabelMapping class attributes and methods
Maude_LabelMapping_from: Property = Property(name="from", type=StringType)
Maude_LabelMapping_to: Property = Property(name="to", type=StringType)
Maude_LabelMapping.attributes={Maude_LabelMapping_from, Maude_LabelMapping_to}

# Relationships
theory14: BinaryAssociation = BinaryAssociation(
    name="theory14",
    ends={
        Property(name="Maude_Theory", type=Maude_TheoryIdModExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Maude_TheoryIdModExp", type=Maude_Theory, multiplicity=Multiplicity(1, 1))
    }
)
els0: BinaryAssociation = BinaryAssociation(
    name="els0",
    ends={
        Property(name="Maude_MaudeTopEl", type=Maude_MaudeSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="Maude_MaudeSpec", type=Maude_MaudeTopEl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
printableEls1: BinaryAssociation = BinaryAssociation(
    name="printableEls1",
    ends={
        Property(name="Maude_MaudeTopEl3", type=Maude_MaudeSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="Maude_MaudeSpec2", type=Maude_MaudeTopEl, multiplicity=Multiplicity(0, 9999))
    }
)
modExp4: BinaryAssociation = BinaryAssociation(
    name="modExp4",
    ends={
        Property(name="Maude_ModExpression", type=Maude_InstModExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Maude_InstModExp", type=Maude_ModExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
views5: BinaryAssociation = BinaryAssociation(
    name="views5",
    ends={
        Property(name="Maude_View", type=Maude_InstModExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Maude_InstModExp6", type=Maude_View, multiplicity=Multiplicity(1, 9999))
    }
)
modExp7: BinaryAssociation = BinaryAssociation(
    name="modExp7",
    ends={
        Property(name="Maude_ModExpression8", type=Maude_RenModExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Maude_RenModExp", type=Maude_ModExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
renamings9: BinaryAssociation = BinaryAssociation(
    name="renamings9",
    ends={
        Property(name="Maude_RenMapping", type=Maude_RenModExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Maude_RenModExp10", type=Maude_RenMapping, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
modExps11: BinaryAssociation = BinaryAssociation(
    name="modExps11",
    ends={
        Property(name="Maude_ModExpression12", type=Maude_CompModExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Maude_CompModExp", type=Maude_ModExpression, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
module13: BinaryAssociation = BinaryAssociation(
    name="module13",
    ends={
        Property(name="Maude_Module", type=Maude_ModuleIdModExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Maude_ModuleIdModExp", type=Maude_Module, multiplicity=Multiplicity(1, 1))
    }
)
sorts32: BinaryAssociation = BinaryAssociation(
    name="sorts32",
    ends={
        Property(name="Sort", type=Maude_Kind, multiplicity=Multiplicity(1, 1)),
        Property(name="kind", type=Maude_Sort, multiplicity=Multiplicity(1, 9999))
    }
)
subsorts33: BinaryAssociation = BinaryAssociation(
    name="subsorts33",
    ends={
        Property(name="Sort34", type=Maude_SubsortRel, multiplicity=Multiplicity(1, 1)),
        Property(name="supersortRels", type=Maude_Sort, multiplicity=Multiplicity(1, 9999))
    }
)
modExp15: BinaryAssociation = BinaryAssociation(
    name="modExp15",
    ends={
        Property(name="Maude_ModExpression16", type=Maude_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="Maude_Parameter", type=Maude_ModExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
els17: BinaryAssociation = BinaryAssociation(
    name="els17",
    ends={
        Property(name="ModElement", type=Maude_Theory, multiplicity=Multiplicity(1, 1)),
        Property(name="theory", type=Maude_ModElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
els18: BinaryAssociation = BinaryAssociation(
    name="els18",
    ends={
        Property(name="ModElement19", type=Maude_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="module", type=Maude_ModElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
params20: BinaryAssociation = BinaryAssociation(
    name="params20",
    ends={
        Property(name="Maude_Parameter22", type=Maude_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="Maude_Module21", type=Maude_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
module23: BinaryAssociation = BinaryAssociation(
    name="module23",
    ends={
        Property(name="Module", type=Maude_ModElement, multiplicity=Multiplicity(1, 1)),
        Property(name="els", type=Maude_Module, multiplicity=Multiplicity(0, 1))
    }
)
theory24: BinaryAssociation = BinaryAssociation(
    name="theory24",
    ends={
        Property(name="Theory", type=Maude_ModElement, multiplicity=Multiplicity(1, 1)),
        Property(name="els25", type=Maude_Theory, multiplicity=Multiplicity(0, 1))
    }
)
imports26: BinaryAssociation = BinaryAssociation(
    name="imports26",
    ends={
        Property(name="Maude_ModExpression27", type=Maude_ModImportation, multiplicity=Multiplicity(1, 1)),
        Property(name="Maude_ModImportation", type=Maude_ModExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
subsortRels28: BinaryAssociation = BinaryAssociation(
    name="subsortRels28",
    ends={
        Property(name="SubsortRel", type=Maude_Sort, multiplicity=Multiplicity(1, 1)),
        Property(name="supersorts", type=Maude_SubsortRel, multiplicity=Multiplicity(0, 9999))
    }
)
supersortRels29: BinaryAssociation = BinaryAssociation(
    name="supersortRels29",
    ends={
        Property(name="SubsortRel30", type=Maude_Sort, multiplicity=Multiplicity(1, 1)),
        Property(name="subsorts", type=Maude_SubsortRel, multiplicity=Multiplicity(0, 9999))
    }
)
kind31: BinaryAssociation = BinaryAssociation(
    name="kind31",
    ends={
        Property(name="Kind", type=Maude_Sort, multiplicity=Multiplicity(1, 1)),
        Property(name="sorts", type=Maude_Kind, multiplicity=Multiplicity(1, 1))
    }
)
rhs60: BinaryAssociation = BinaryAssociation(
    name="rhs60",
    ends={
        Property(name="Maude_Sort61", type=Maude_MembershipCond, multiplicity=Multiplicity(1, 1)),
        Property(name="Maude_MembershipCond", type=Maude_Sort, multiplicity=Multiplicity(1, 1))
    }
)
rhs62: BinaryAssociation = BinaryAssociation(
    name="rhs62",
    ends={
        Property(name="Maude_Term63", type=Maude_MatchingCond, multiplicity=Multiplicity(1, 1)),
        Property(name="Maude_MatchingCond", type=Maude_Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
supersorts35: BinaryAssociation = BinaryAssociation(
    name="supersorts35",
    ends={
        Property(name="Sort36", type=Maude_SubsortRel, multiplicity=Multiplicity(1, 1)),
        Property(name="subsortRels", type=Maude_Sort, multiplicity=Multiplicity(1, 9999))
    }
)
coarity37: BinaryAssociation = BinaryAssociation(
    name="coarity37",
    ends={
        Property(name="Maude_Type", type=Maude_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="Maude_Operation", type=Maude_Type, multiplicity=Multiplicity(1, 1))
    }
)
arity38: BinaryAssociation = BinaryAssociation(
    name="arity38",
    ends={
        Property(name="Maude_Type40", type=Maude_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="Maude_Operation39", type=Maude_Type, multiplicity=Multiplicity(0, 9999))
    }
)
conds41: BinaryAssociation = BinaryAssociation(
    name="conds41",
    ends={
        Property(name="Maude_Condition", type=Maude_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="Maude_Statement", type=Maude_Condition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
term42: BinaryAssociation = BinaryAssociation(
    name="term42",
    ends={
        Property(name="Maude_Term", type=Maude_Membership, multiplicity=Multiplicity(1, 1)),
        Property(name="Maude_Membership", type=Maude_Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sort43: BinaryAssociation = BinaryAssociation(
    name="sort43",
    ends={
        Property(name="Maude_Sort", type=Maude_Membership, multiplicity=Multiplicity(1, 1)),
        Property(name="Maude_Membership44", type=Maude_Sort, multiplicity=Multiplicity(1, 1))
    }
)
lhs45: BinaryAssociation = BinaryAssociation(
    name="lhs45",
    ends={
        Property(name="Maude_Term46", type=Maude_Equation, multiplicity=Multiplicity(1, 1)),
        Property(name="Maude_Equation", type=Maude_Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs47: BinaryAssociation = BinaryAssociation(
    name="rhs47",
    ends={
        Property(name="Maude_Term49", type=Maude_Equation, multiplicity=Multiplicity(1, 1)),
        Property(name="Maude_Equation48", type=Maude_Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lhs50: BinaryAssociation = BinaryAssociation(
    name="lhs50",
    ends={
        Property(name="Maude_Term51", type=Maude_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="Maude_Rule", type=Maude_Term, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs52: BinaryAssociation = BinaryAssociation(
    name="rhs52",
    ends={
        Property(name="Maude_Term54", type=Maude_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="Maude_Rule53", type=Maude_Term, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs55: BinaryAssociation = BinaryAssociation(
    name="lhs55",
    ends={
        Property(name="Maude_Term57", type=Maude_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="Maude_Condition56", type=Maude_Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs58: BinaryAssociation = BinaryAssociation(
    name="rhs58",
    ends={
        Property(name="Maude_Term59", type=Maude_RewriteCond, multiplicity=Multiplicity(1, 1)),
        Property(name="Maude_RewriteCond", type=Maude_Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
from84: BinaryAssociation = BinaryAssociation(
    name="from84",
    ends={
        Property(name="Maude_Sort85", type=Maude_SortMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="Maude_SortMapping", type=Maude_Sort, multiplicity=Multiplicity(1, 1))
    }
)
rhs64: BinaryAssociation = BinaryAssociation(
    name="rhs64",
    ends={
        Property(name="Maude_Term65", type=Maude_EqualCond, multiplicity=Multiplicity(1, 1)),
        Property(name="Maude_EqualCond", type=Maude_Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type66: BinaryAssociation = BinaryAssociation(
    name="type66",
    ends={
        Property(name="Maude_Type68", type=Maude_Term, multiplicity=Multiplicity(1, 1)),
        Property(name="Maude_Term67", type=Maude_Type, multiplicity=Multiplicity(1, 1))
    }
)
args69: BinaryAssociation = BinaryAssociation(
    name="args69",
    ends={
        Property(name="Maude_Term70", type=Maude_RecTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="Maude_RecTerm", type=Maude_Term, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
from71: BinaryAssociation = BinaryAssociation(
    name="from71",
    ends={
        Property(name="Maude_ModExpression73", type=Maude_View, multiplicity=Multiplicity(1, 1)),
        Property(name="Maude_View72", type=Maude_ModExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
to74: BinaryAssociation = BinaryAssociation(
    name="to74",
    ends={
        Property(name="Maude_ModExpression76", type=Maude_View, multiplicity=Multiplicity(1, 1)),
        Property(name="Maude_View75", type=Maude_ModExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
els77: BinaryAssociation = BinaryAssociation(
    name="els77",
    ends={
        Property(name="Maude_ViewMapping", type=Maude_View, multiplicity=Multiplicity(1, 1)),
        Property(name="Maude_View78", type=Maude_ViewMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
from79: BinaryAssociation = BinaryAssociation(
    name="from79",
    ends={
        Property(name="Maude_Term80", type=Maude_TermMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="Maude_TermMapping", type=Maude_Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
to81: BinaryAssociation = BinaryAssociation(
    name="to81",
    ends={
        Property(name="Maude_Term83", type=Maude_TermMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="Maude_TermMapping82", type=Maude_Term, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
from86: BinaryAssociation = BinaryAssociation(
    name="from86",
    ends={
        Property(name="Maude_Operation87", type=Maude_OpTypedMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="Maude_OpTypedMapping", type=Maude_Operation, multiplicity=Multiplicity(1, 1))
    }
)
from88: BinaryAssociation = BinaryAssociation(
    name="from88",
    ends={
        Property(name="Maude_Operation89", type=Maude_OpMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="Maude_OpMapping", type=Maude_Operation, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_Maude_TheoryIdModExp_ModExpression = Generalization(general=ModExpression, specific=Maude_TheoryIdModExp)
gen_Maude_InstModExp_ModExpression = Generalization(general=ModExpression, specific=Maude_InstModExp)
gen_Maude_RenModExp_ModExpression = Generalization(general=ModExpression, specific=Maude_RenModExp)
gen_Maude_CompModExp_ModExpression = Generalization(general=ModExpression, specific=Maude_CompModExp)
gen_Maude_ModuleIdModExp_ModExpression = Generalization(general=ModExpression, specific=Maude_ModuleIdModExp)
gen_Maude_Kind_Type = Generalization(general=Type, specific=Maude_Kind)
gen_Maude_SubsortRel_ModElement = Generalization(general=ModElement, specific=Maude_SubsortRel)
gen_Maude_Parameter_ModExpression = Generalization(general=ModExpression, specific=Maude_Parameter)
gen_Maude_Theory_MaudeTopEl = Generalization(general=MaudeTopEl, specific=Maude_Theory)
gen_Maude_FTheory_Theory = Generalization(general=Theory, specific=Maude_FTheory)
gen_Maude_STheory_Theory = Generalization(general=Theory, specific=Maude_STheory)
gen_Maude_Module_MaudeTopEl = Generalization(general=MaudeTopEl, specific=Maude_Module)
gen_Maude_FModule_Module = Generalization(general=Module, specific=Maude_FModule)
gen_Maude_SModule_Module = Generalization(general=Module, specific=Maude_SModule)
gen_Maude_ModImportation_ModElement = Generalization(general=ModElement, specific=Maude_ModImportation)
gen_Maude_Sort_Type = Generalization(general=Type, specific=Maude_Sort)
gen_Maude_Sort_ModElement = Generalization(general=ModElement, specific=Maude_Sort)
gen_Maude_MembershipCond_EquationalCond = Generalization(general=EquationalCond, specific=Maude_MembershipCond)
gen_Maude_BooleanCond_EquationalCond = Generalization(general=EquationalCond, specific=Maude_BooleanCond)
gen_Maude_MatchingCond_EquationalCond = Generalization(general=EquationalCond, specific=Maude_MatchingCond)
gen_Maude_Operation_ModElement = Generalization(general=ModElement, specific=Maude_Operation)
gen_Maude_Statement_ModElement = Generalization(general=ModElement, specific=Maude_Statement)
gen_Maude_Membership_Statement = Generalization(general=Statement, specific=Maude_Membership)
gen_Maude_Equation_Statement = Generalization(general=Statement, specific=Maude_Equation)
gen_Maude_Rule_Statement = Generalization(general=Statement, specific=Maude_Rule)
gen_Maude_EquationalCond_Condition = Generalization(general=Condition, specific=Maude_EquationalCond)
gen_Maude_RewriteCond_Condition = Generalization(general=Condition, specific=Maude_RewriteCond)
gen_Maude_OpTypedMapping_RenMapping = Generalization(general=RenMapping, specific=Maude_OpTypedMapping)
gen_Maude_EqualCond_EquationalCond = Generalization(general=EquationalCond, specific=Maude_EqualCond)
gen_Maude_Constant_Term = Generalization(general=Term, specific=Maude_Constant)
gen_Maude_RecTerm_Term = Generalization(general=Term, specific=Maude_RecTerm)
gen_Maude_Variable_Term = Generalization(general=Term, specific=Maude_Variable)
gen_Maude_View_MaudeTopEl = Generalization(general=MaudeTopEl, specific=Maude_View)
gen_Maude_RenMapping_ViewMapping = Generalization(general=ViewMapping, specific=Maude_RenMapping)
gen_Maude_TermMapping_ViewMapping = Generalization(general=ViewMapping, specific=Maude_TermMapping)
gen_Maude_SortMapping_RenMapping = Generalization(general=RenMapping, specific=Maude_SortMapping)
gen_Maude_OpMapping_RenMapping = Generalization(general=RenMapping, specific=Maude_OpMapping)
gen_Maude_LabelMapping_RenMapping = Generalization(general=RenMapping, specific=Maude_LabelMapping)

# Domain Model
domain_model = DomainModel(
    name="Maude",
    types={Maude_TheoryIdModExp, Maude_Theory, Maude_MaudeSpec, Maude_MaudeTopEl, Maude_ModExpression, Maude_InstModExp, ModExpression, Maude_View, Maude_RenModExp, Maude_RenMapping, Maude_CompModExp, Maude_ModuleIdModExp, Maude_Module, Maude_Parameter, MaudeTopEl, Maude_ModElement, Maude_FTheory, Theory, Maude_STheory, Maude_FModule, Module, Maude_SModule, Maude_ModImportation, ModElement, Maude_Type, Maude_Sort, Type, Maude_SubsortRel, Maude_Kind, Maude_MembershipCond, EquationalCond, Maude_BooleanCond, Maude_MatchingCond, Maude_Operation, Maude_Statement, Maude_Condition, Maude_Membership, Statement, Maude_Term, Maude_Equation, Maude_Rule, Maude_EquationalCond, Condition, Maude_RewriteCond, Maude_OpTypedMapping, Maude_EqualCond, Maude_Constant, Term, Maude_RecTerm, Maude_Variable, Maude_ViewMapping, ViewMapping, Maude_TermMapping, Maude_SortMapping, RenMapping, Maude_OpMapping, Maude_LabelMapping, ImportationMode},
    associations={theory14, els0, printableEls1, modExp4, views5, modExp7, renamings9, modExps11, module13, sorts32, subsorts33, modExp15, els17, els18, params20, module23, theory24, imports26, subsortRels28, supersortRels29, kind31, rhs60, rhs62, supersorts35, coarity37, arity38, conds41, term42, sort43, lhs45, rhs47, lhs50, rhs52, lhs55, rhs58, from84, rhs64, type66, args69, from71, to74, els77, from79, to81, from86, from88},
    generalizations={gen_Maude_TheoryIdModExp_ModExpression, gen_Maude_InstModExp_ModExpression, gen_Maude_RenModExp_ModExpression, gen_Maude_CompModExp_ModExpression, gen_Maude_ModuleIdModExp_ModExpression, gen_Maude_Kind_Type, gen_Maude_SubsortRel_ModElement, gen_Maude_Parameter_ModExpression, gen_Maude_Theory_MaudeTopEl, gen_Maude_FTheory_Theory, gen_Maude_STheory_Theory, gen_Maude_Module_MaudeTopEl, gen_Maude_FModule_Module, gen_Maude_SModule_Module, gen_Maude_ModImportation_ModElement, gen_Maude_Sort_Type, gen_Maude_Sort_ModElement, gen_Maude_MembershipCond_EquationalCond, gen_Maude_BooleanCond_EquationalCond, gen_Maude_MatchingCond_EquationalCond, gen_Maude_Operation_ModElement, gen_Maude_Statement_ModElement, gen_Maude_Membership_Statement, gen_Maude_Equation_Statement, gen_Maude_Rule_Statement, gen_Maude_EquationalCond_Condition, gen_Maude_RewriteCond_Condition, gen_Maude_OpTypedMapping_RenMapping, gen_Maude_EqualCond_EquationalCond, gen_Maude_Constant_Term, gen_Maude_RecTerm_Term, gen_Maude_Variable_Term, gen_Maude_View_MaudeTopEl, gen_Maude_RenMapping_ViewMapping, gen_Maude_TermMapping_ViewMapping, gen_Maude_SortMapping_RenMapping, gen_Maude_OpMapping_RenMapping, gen_Maude_LabelMapping_RenMapping},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)