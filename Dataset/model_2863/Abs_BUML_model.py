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
abs_Delta_decl = Class(name="abs::Delta::decl")
abs_Update_decl = Class(name="abs::Update::decl")
abs_Productline_decl = Class(name="abs::Productline::decl")
abs_Product_decl = Class(name="abs::Product::decl")
abs_DomainModel = Class(name="abs::DomainModel")
abs_Compilation_Unit = Class(name="abs::Compilation::Unit")
DomainModel = Class(name="DomainModel")
abs_Module_decl = Class(name="abs::Module::decl")
Namespace_modifier = Class(name="Namespace::modifier")
abs_Feature_decl = Class(name="abs::Feature::decl")
abs_Fextension = Class(name="abs::Fextension")
abs_Module_export = Class(name="abs::Module::export")
abs_Module_import = Class(name="abs::Module::import")
abs_Decl = Class(name="abs::Decl")
abs_Main_block = Class(name="abs::Main::block")
abs_Function_name_decl = Class(name="abs::Function::name::decl")
abs_DataType_decl = Class(name="abs::DataType::decl")
Functional_modifier = Class(name="Functional::modifier")
abs_Data_constructor = Class(name="abs::Data::constructor")
abs_Par_function_decl = Class(name="abs::Par::function::decl")
Decl = Class(name="Decl")
abs_Type_use = Class(name="abs::Type::use")
abs_Function_name_list = Class(name="abs::Function::name::list")
abs_Param_list = Class(name="abs::Param::list")
abs_Pure_exp = Class(name="abs::Pure::exp")
Annotation = Class(name="Annotation")
Exp = Class(name="Exp")
Eff_expr = Class(name="Eff::expr")
abs_Function_list = Class(name="abs::Function::list")
abs_Pure_exp_list = Class(name="abs::Pure::exp::list")
abs_Data_constructor_arg = Class(name="abs::Data::constructor::arg")
abs_Annotations = Class(name="abs::Annotations")
abs_Annotation = Class(name="abs::Annotation")
Data_constructor_arg = Class(name="Data::constructor::arg")
abs_Case_branch = Class(name="abs::Case::branch")
abs_Function_param = Class(name="abs::Function::param")
abs_Function_name_param_decl = Class(name="abs::Function::name::param::decl")
Function_param = Class(name="Function::param")
abs_Anon_function_decl = Class(name="abs::Anon::function::decl")
abs_Var_or_field_ref = Class(name="abs::Var::or::field::ref")
Pure_exp = Class(name="Pure::exp")
abs_Field_decl = Class(name="abs::Field::decl")
abs_Pattern = Class(name="abs::Pattern")
Case_branch = Class(name="Case::branch")
abs_Typesyn_decl = Class(name="abs::Typesyn::decl")
abs_Exception_decl = Class(name="abs::Exception::decl")
abs_Interface_decl = Class(name="abs::Interface::decl")
abs_Methodsig = Class(name="abs::Methodsig")
abs_Interface_name = Class(name="abs::Interface::name")
Class_modifier_fragment = Class(name="Class::modifier::fragment")
Interface_modifier_fragment = Class(name="Interface::modifier::fragment")
abs_Param_decl = Class(name="abs::Param::decl")
Delta_param = Class(name="Delta::param")
abs_Type_exp = Class(name="abs::Type::exp")
Update_preamble_declaration = Class(name="Update::preamble::declaration")
abs_Function_decl = Class(name="abs::Function::decl")
abs_Exp = Class(name="abs::Exp")
abs_Class_decl = Class(name="abs::Class::decl")
abs_Stmt = Class(name="abs::Stmt")
abs_Casestmtbranch = Class(name="abs::Casestmtbranch")
abs_Trait_usage = Class(name="abs::Trait::usage")
abs_Method = Class(name="abs::Method")
abs_Guard = Class(name="abs::Guard")
abs_Eff_expr = Class(name="abs::Eff::expr")
abs_Delta_id = Class(name="abs::Delta::id")
abs_Trait_oper = Class(name="abs::Trait::oper")
abs_Trait_decl = Class(name="abs::Trait::decl")
abs_Trait_expr = Class(name="abs::Trait::expr")
abs_Delta_param = Class(name="abs::Delta::param")
abs_Delta_access = Class(name="abs::Delta::access")
abs_Module_modifier = Class(name="abs::Module::modifier")
abs_Has_condition = Class(name="abs::Has::condition")
abs_Class_modifier_fragment = Class(name="abs::Class::modifier::fragment")
abs_Interface_modifier_fragment = Class(name="abs::Interface::modifier::fragment")
abs_Functional_modifier = Class(name="abs::Functional::modifier")
Module_modifier = Class(name="Module::modifier")
abs_OO_modifier = Class(name="abs::OO::modifier")
abs_Update_preamble_declaration = Class(name="abs::Update::preamble::declaration")
abs_Object_update_assign_stmt = Class(name="abs::Object::update::assign::stmt")
abs_Namespace_modifier = Class(name="abs::Namespace::modifier")
abs_Object_update = Class(name="abs::Object::update")
abs_After_condition = Class(name="abs::After::condition")
abs_From_condition = Class(name="abs::From::condition")
abs_When_condition = Class(name="abs::When::condition")
abs_Deltaspec = Class(name="abs::Deltaspec")
abs_Feature = Class(name="abs::Feature")
abs_Delta_clause = Class(name="abs::Delta::clause")
abs_Product_reconfiguration = Class(name="abs::Product::reconfiguration")
abs_Product_expr = Class(name="abs::Product::expr")
abs_Application_condition = Class(name="abs::Application::condition")
Fnode = Class(name="Fnode")
abs_Feature_decl_group = Class(name="abs::Feature::decl::group")
abs_Feature_decl_attribute = Class(name="abs::Feature::decl::attribute")
abs_Feature_decl_constraint = Class(name="abs::Feature::decl::constraint")
abs_Fnode = Class(name="abs::Fnode")
abs_Or_expr = Class(name="abs::Or::expr")
abs_And_expr = Class(name="abs::And::expr")
abs_Mexp = Class(name="abs::Mexp")
abs_Equality_expr = Class(name="abs::Equality::expr")
abs_Comparison_expr = Class(name="abs::Comparison::expr")
abs_AndGuard = Class(name="abs::AndGuard")
Guard = Class(name="Guard")
abs_AppOr_exp = Class(name="abs::AppOr::exp")
Application_condition = Class(name="Application::condition")
abs_AppAnd_exp = Class(name="abs::AppAnd::exp")
abs_ProductOr_expr = Class(name="abs::ProductOr::expr")
Product_expr = Class(name="Product::expr")
abs_ProductAnd_exp = Class(name="abs::ProductAnd::exp")
abs_ProductMinus_exp = Class(name="abs::ProductMinus::exp")
abs_MexpOr_exp = Class(name="abs::MexpOr::exp")
Mexp = Class(name="Mexp")
abs_PlusOrMinus_expr = Class(name="abs::PlusOrMinus::expr")
abs_MulDivOrMod_expr = Class(name="abs::MulDivOrMod::expr")
abs_MexpEquality_expr = Class(name="abs::MexpEquality::expr")
abs_MexpAnd_expr = Class(name="abs::MexpAnd::expr")
abs_MexpImplies_expr = Class(name="abs::MexpImplies::expr")
abs_MexpMulDivOrMod_expr = Class(name="abs::MexpMulDivOrMod::expr")
abs_MexpComparison_expr = Class(name="abs::MexpComparison::expr")
abs_MexpPlusOrMinus_expr = Class(name="abs::MexpPlusOrMinus::expr")
abs_MexpPrimary_expr = Class(name="abs::MexpPrimary::expr")

# abs_Delta_decl class attributes and methods
abs_Delta_decl_name: Property = Property(name="name", type=StringType)
abs_Delta_decl.attributes={abs_Delta_decl_name}

# abs_Update_decl class attributes and methods
abs_Update_decl_name: Property = Property(name="name", type=StringType)
abs_Update_decl.attributes={abs_Update_decl_name}

# abs_Productline_decl class attributes and methods
abs_Productline_decl_name: Property = Property(name="name", type=StringType)
abs_Productline_decl.attributes={abs_Productline_decl_name}

# abs_Product_decl class attributes and methods
abs_Product_decl_name: Property = Property(name="name", type=StringType)
abs_Product_decl.attributes={abs_Product_decl_name}

# abs_DomainModel class attributes and methods

# abs_Compilation_Unit class attributes and methods

# DomainModel class attributes and methods

# abs_Module_decl class attributes and methods
abs_Module_decl_name: Property = Property(name="name", type=StringType)
abs_Module_decl.attributes={abs_Module_decl_name}

# Namespace_modifier class attributes and methods

# abs_Feature_decl class attributes and methods
abs_Feature_decl_name: Property = Property(name="name", type=StringType)
abs_Feature_decl.attributes={abs_Feature_decl_name}

# abs_Fextension class attributes and methods
abs_Fextension_name: Property = Property(name="name", type=StringType)
abs_Fextension.attributes={abs_Fextension_name}

# abs_Module_export class attributes and methods
abs_Module_export_anyPackage: Property = Property(name="anyPackage", type=StringType)
abs_Module_export_importedNamespace: Property = Property(name="importedNamespace", type=StringType)
abs_Module_export.attributes={abs_Module_export_importedNamespace, abs_Module_export_anyPackage}

# abs_Module_import class attributes and methods
abs_Module_import_importedNamespace: Property = Property(name="importedNamespace", type=StringType)
abs_Module_import_name: Property = Property(name="name", type=StringType)
abs_Module_import.attributes={abs_Module_import_name, abs_Module_import_importedNamespace}

# abs_Decl class attributes and methods
abs_Decl_name: Property = Property(name="name", type=StringType)
abs_Decl.attributes={abs_Decl_name}

# abs_Main_block class attributes and methods

# abs_Function_name_decl class attributes and methods
abs_Function_name_decl_name: Property = Property(name="name", type=StringType)
abs_Function_name_decl.attributes={abs_Function_name_decl_name}

# abs_DataType_decl class attributes and methods
abs_DataType_decl_p: Property = Property(name="p", type=StringType)
abs_DataType_decl.attributes={abs_DataType_decl_p}

# Functional_modifier class attributes and methods

# abs_Data_constructor class attributes and methods
abs_Data_constructor_name: Property = Property(name="name", type=StringType)
abs_Data_constructor.attributes={abs_Data_constructor_name}

# abs_Par_function_decl class attributes and methods
abs_Par_function_decl_p: Property = Property(name="p", type=StringType)
abs_Par_function_decl.attributes={abs_Par_function_decl_p}

# Decl class attributes and methods

# abs_Type_use class attributes and methods
abs_Type_use_name: Property = Property(name="name", type=StringType)
abs_Type_use.attributes={abs_Type_use_name}

# abs_Function_name_list class attributes and methods

# abs_Param_list class attributes and methods

# abs_Pure_exp class attributes and methods
abs_Pure_exp_value: Property = Property(name="value", type=StringType)
abs_Pure_exp_op: Property = Property(name="op", type=StringType)
abs_Pure_exp_await: Property = Property(name="await", type=StringType)
abs_Pure_exp_val: Property = Property(name="val", type=StringType)
abs_Pure_exp.attributes={abs_Pure_exp_await, abs_Pure_exp_value, abs_Pure_exp_op, abs_Pure_exp_val}

# Annotation class attributes and methods

# Exp class attributes and methods

# Eff_expr class attributes and methods

# abs_Function_list class attributes and methods

# abs_Pure_exp_list class attributes and methods

# abs_Data_constructor_arg class attributes and methods

# abs_Annotations class attributes and methods

# abs_Annotation class attributes and methods

# Data_constructor_arg class attributes and methods

# abs_Case_branch class attributes and methods

# abs_Function_param class attributes and methods

# abs_Function_name_param_decl class attributes and methods
abs_Function_name_param_decl_value: Property = Property(name="value", type=StringType)
abs_Function_name_param_decl.attributes={abs_Function_name_param_decl_value}

# Function_param class attributes and methods

# abs_Anon_function_decl class attributes and methods

# abs_Var_or_field_ref class attributes and methods
abs_Var_or_field_ref_name: Property = Property(name="name", type=StringType)
abs_Var_or_field_ref.attributes={abs_Var_or_field_ref_name}

# Pure_exp class attributes and methods

# abs_Field_decl class attributes and methods
abs_Field_decl_name: Property = Property(name="name", type=StringType)
abs_Field_decl.attributes={abs_Field_decl_name}

# abs_Pattern class attributes and methods

# Case_branch class attributes and methods

# abs_Typesyn_decl class attributes and methods

# abs_Exception_decl class attributes and methods

# abs_Interface_decl class attributes and methods

# abs_Methodsig class attributes and methods
abs_Methodsig_name: Property = Property(name="name", type=StringType)
abs_Methodsig.attributes={abs_Methodsig_name}

# abs_Interface_name class attributes and methods
abs_Interface_name_name: Property = Property(name="name", type=StringType)
abs_Interface_name.attributes={abs_Interface_name_name}

# Class_modifier_fragment class attributes and methods

# Interface_modifier_fragment class attributes and methods

# abs_Param_decl class attributes and methods
abs_Param_decl_name: Property = Property(name="name", type=StringType)
abs_Param_decl.attributes={abs_Param_decl_name}

# Delta_param class attributes and methods

# abs_Type_exp class attributes and methods
abs_Type_exp_name: Property = Property(name="name", type=StringType)
abs_Type_exp.attributes={abs_Type_exp_name}

# Update_preamble_declaration class attributes and methods

# abs_Function_decl class attributes and methods
abs_Function_decl_p: Property = Property(name="p", type=StringType)
abs_Function_decl.attributes={abs_Function_decl_p}

# abs_Exp class attributes and methods

# abs_Class_decl class attributes and methods

# abs_Stmt class attributes and methods
abs_Stmt_name: Property = Property(name="name", type=StringType)
abs_Stmt.attributes={abs_Stmt_name}

# abs_Casestmtbranch class attributes and methods

# abs_Trait_usage class attributes and methods

# abs_Method class attributes and methods
abs_Method_name: Property = Property(name="name", type=StringType)
abs_Method.attributes={abs_Method_name}

# abs_Guard class attributes and methods

# abs_Eff_expr class attributes and methods
abs_Eff_expr_l: Property = Property(name="l", type=StringType)
abs_Eff_expr.attributes={abs_Eff_expr_l}

# abs_Delta_id class attributes and methods
abs_Delta_id_name: Property = Property(name="name", type=StringType)
abs_Delta_id.attributes={abs_Delta_id_name}

# abs_Trait_oper class attributes and methods

# abs_Trait_decl class attributes and methods

# abs_Trait_expr class attributes and methods

# abs_Delta_param class attributes and methods

# abs_Delta_access class attributes and methods

# abs_Module_modifier class attributes and methods

# abs_Has_condition class attributes and methods

# abs_Class_modifier_fragment class attributes and methods

# abs_Interface_modifier_fragment class attributes and methods

# abs_Functional_modifier class attributes and methods

# Module_modifier class attributes and methods

# abs_OO_modifier class attributes and methods

# abs_Update_preamble_declaration class attributes and methods

# abs_Object_update_assign_stmt class attributes and methods

# abs_Namespace_modifier class attributes and methods
abs_Namespace_modifier_star: Property = Property(name="star", type=StringType)
abs_Namespace_modifier.attributes={abs_Namespace_modifier_star}

# abs_Object_update class attributes and methods

# abs_After_condition class attributes and methods

# abs_From_condition class attributes and methods

# abs_When_condition class attributes and methods

# abs_Deltaspec class attributes and methods
abs_Deltaspec_name: Property = Property(name="name", type=StringType)
abs_Deltaspec_deltaspec_param: Property = Property(name="deltaspec_param", type=StringType)
abs_Deltaspec.attributes={abs_Deltaspec_deltaspec_param, abs_Deltaspec_name}

# abs_Feature class attributes and methods
abs_Feature_p: Property = Property(name="p", type=StringType)
abs_Feature_attr_assignment: Property = Property(name="attr_assignment", type=StringType)
abs_Feature.attributes={abs_Feature_attr_assignment, abs_Feature_p}

# abs_Delta_clause class attributes and methods

# abs_Product_reconfiguration class attributes and methods
abs_Product_reconfiguration_name: Property = Property(name="name", type=StringType)
abs_Product_reconfiguration_update: Property = Property(name="update", type=StringType)
abs_Product_reconfiguration.attributes={abs_Product_reconfiguration_update, abs_Product_reconfiguration_name}

# abs_Product_expr class attributes and methods

# abs_Application_condition class attributes and methods

# Fnode class attributes and methods

# abs_Feature_decl_group class attributes and methods

# abs_Feature_decl_attribute class attributes and methods
abs_Feature_decl_attribute_boundary_val: Property = Property(name="boundary_val", type=StringType)
abs_Feature_decl_attribute_lBoundary_int: Property = Property(name="lBoundary_int", type=StringType)
abs_Feature_decl_attribute_uBoundary_int: Property = Property(name="uBoundary_int", type=StringType)
abs_Feature_decl_attribute.attributes={abs_Feature_decl_attribute_boundary_val, abs_Feature_decl_attribute_uBoundary_int, abs_Feature_decl_attribute_lBoundary_int}

# abs_Feature_decl_constraint class attributes and methods

# abs_Fnode class attributes and methods

# abs_Or_expr class attributes and methods

# abs_And_expr class attributes and methods

# abs_Mexp class attributes and methods
abs_Mexp_value: Property = Property(name="value", type=IntegerType)
abs_Mexp.attributes={abs_Mexp_value}

# abs_Equality_expr class attributes and methods

# abs_Comparison_expr class attributes and methods

# abs_AndGuard class attributes and methods
abs_AndGuard_op: Property = Property(name="op", type=StringType)
abs_AndGuard.attributes={abs_AndGuard_op}

# Guard class attributes and methods

# abs_AppOr_exp class attributes and methods

# Application_condition class attributes and methods

# abs_AppAnd_exp class attributes and methods

# abs_ProductOr_expr class attributes and methods

# Product_expr class attributes and methods

# abs_ProductAnd_exp class attributes and methods

# abs_ProductMinus_exp class attributes and methods

# abs_MexpOr_exp class attributes and methods

# Mexp class attributes and methods

# abs_PlusOrMinus_expr class attributes and methods

# abs_MulDivOrMod_expr class attributes and methods

# abs_MexpEquality_expr class attributes and methods
abs_MexpEquality_expr_op: Property = Property(name="op", type=StringType)
abs_MexpEquality_expr.attributes={abs_MexpEquality_expr_op}

# abs_MexpAnd_expr class attributes and methods

# abs_MexpImplies_expr class attributes and methods
abs_MexpImplies_expr_op: Property = Property(name="op", type=StringType)
abs_MexpImplies_expr.attributes={abs_MexpImplies_expr_op}

# abs_MexpMulDivOrMod_expr class attributes and methods
abs_MexpMulDivOrMod_expr_op: Property = Property(name="op", type=StringType)
abs_MexpMulDivOrMod_expr.attributes={abs_MexpMulDivOrMod_expr_op}

# abs_MexpComparison_expr class attributes and methods
abs_MexpComparison_expr_op: Property = Property(name="op", type=StringType)
abs_MexpComparison_expr.attributes={abs_MexpComparison_expr_op}

# abs_MexpPlusOrMinus_expr class attributes and methods
abs_MexpPlusOrMinus_expr_op: Property = Property(name="op", type=StringType)
abs_MexpPlusOrMinus_expr.attributes={abs_MexpPlusOrMinus_expr_op}

# abs_MexpPrimary_expr class attributes and methods

# Relationships
deltaDecl1: BinaryAssociation = BinaryAssociation(
    name="deltaDecl1",
    ends={
        Property(name="abs_Delta_decl", type=abs_Compilation_Unit, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Compilation_Unit2", type=abs_Delta_decl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
update_decl3: BinaryAssociation = BinaryAssociation(
    name="update_decl3",
    ends={
        Property(name="abs_Update_decl", type=abs_Compilation_Unit, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Compilation_Unit4", type=abs_Update_decl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
productline_decl5: BinaryAssociation = BinaryAssociation(
    name="productline_decl5",
    ends={
        Property(name="abs_Productline_decl", type=abs_Compilation_Unit, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Compilation_Unit6", type=abs_Productline_decl, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
product_decl7: BinaryAssociation = BinaryAssociation(
    name="product_decl7",
    ends={
        Property(name="abs_Product_decl", type=abs_Compilation_Unit, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Compilation_Unit8", type=abs_Product_decl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
module0: BinaryAssociation = BinaryAssociation(
    name="module0",
    ends={
        Property(name="abs_Module_decl", type=abs_Compilation_Unit, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Compilation_Unit", type=abs_Module_decl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
main_block19: BinaryAssociation = BinaryAssociation(
    name="main_block19",
    ends={
        Property(name="abs_Main_block", type=abs_Module_decl, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Module_decl20", type=abs_Main_block, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
feature_decl9: BinaryAssociation = BinaryAssociation(
    name="feature_decl9",
    ends={
        Property(name="abs_Feature_decl", type=abs_Compilation_Unit, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Compilation_Unit10", type=abs_Feature_decl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fextension11: BinaryAssociation = BinaryAssociation(
    name="fextension11",
    ends={
        Property(name="abs_Fextension", type=abs_Compilation_Unit, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Compilation_Unit12", type=abs_Fextension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
module_export13: BinaryAssociation = BinaryAssociation(
    name="module_export13",
    ends={
        Property(name="abs_Module_export", type=abs_Module_decl, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Module_decl14", type=abs_Module_export, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
module_import15: BinaryAssociation = BinaryAssociation(
    name="module_import15",
    ends={
        Property(name="abs_Module_import", type=abs_Module_decl, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Module_decl16", type=abs_Module_import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
decl17: BinaryAssociation = BinaryAssociation(
    name="decl17",
    ends={
        Property(name="abs_Decl", type=abs_Module_decl, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Module_decl18", type=abs_Decl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
function_name_decl28: BinaryAssociation = BinaryAssociation(
    name="function_name_decl28",
    ends={
        Property(name="abs_Function_name_decl", type=abs_Function_name_list, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Function_name_list29", type=abs_Function_name_decl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
data_constructor30: BinaryAssociation = BinaryAssociation(
    name="data_constructor30",
    ends={
        Property(name="abs_Data_constructor", type=abs_DataType_decl, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_DataType_decl", type=abs_Data_constructor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type_use21: BinaryAssociation = BinaryAssociation(
    name="type_use21",
    ends={
        Property(name="abs_Type_use", type=abs_Par_function_decl, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Par_function_decl", type=abs_Type_use, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
functions22: BinaryAssociation = BinaryAssociation(
    name="functions22",
    ends={
        Property(name="abs_Function_name_list", type=abs_Par_function_decl, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Par_function_decl23", type=abs_Function_name_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
params24: BinaryAssociation = BinaryAssociation(
    name="params24",
    ends={
        Property(name="abs_Param_list", type=abs_Par_function_decl, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Par_function_decl25", type=abs_Param_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
e26: BinaryAssociation = BinaryAssociation(
    name="e26",
    ends={
        Property(name="abs_Pure_exp", type=abs_Par_function_decl, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Par_function_decl27", type=abs_Pure_exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type_use38: BinaryAssociation = BinaryAssociation(
    name="type_use38",
    ends={
        Property(name="abs_Type_use39", type=abs_Type_use, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Type_use37", type=abs_Type_use, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
function_list40: BinaryAssociation = BinaryAssociation(
    name="function_list40",
    ends={
        Property(name="abs_Function_list", type=abs_Pure_exp, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Pure_exp41", type=abs_Function_list, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
partial_function_pure_exp_list42: BinaryAssociation = BinaryAssociation(
    name="partial_function_pure_exp_list42",
    ends={
        Property(name="abs_Pure_exp_list", type=abs_Pure_exp, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Pure_exp43", type=abs_Pure_exp_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
data_constructor_arg31: BinaryAssociation = BinaryAssociation(
    name="data_constructor_arg31",
    ends={
        Property(name="abs_Data_constructor_arg", type=abs_Data_constructor, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Data_constructor32", type=abs_Data_constructor_arg, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotation33: BinaryAssociation = BinaryAssociation(
    name="annotation33",
    ends={
        Property(name="abs_Annotation", type=abs_Annotations, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Annotations", type=abs_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pure_exp34: BinaryAssociation = BinaryAssociation(
    name="pure_exp34",
    ends={
        Property(name="abs_Pure_exp36", type=abs_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Annotation35", type=abs_Pure_exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type_use61: BinaryAssociation = BinaryAssociation(
    name="type_use61",
    ends={
        Property(name="abs_Type_use63", type=abs_Pure_exp, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Pure_exp62", type=abs_Type_use, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
i65: BinaryAssociation = BinaryAssociation(
    name="i65",
    ends={
        Property(name="abs_Pure_exp66", type=abs_Pure_exp, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Pure_exp64", type=abs_Pure_exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
b68: BinaryAssociation = BinaryAssociation(
    name="b68",
    ends={
        Property(name="abs_Pure_exp69", type=abs_Pure_exp, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Pure_exp67", type=abs_Pure_exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pure_exp71: BinaryAssociation = BinaryAssociation(
    name="pure_exp71",
    ends={
        Property(name="abs_Pure_exp72", type=abs_Pure_exp, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Pure_exp70", type=abs_Pure_exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variadic_exp_list44: BinaryAssociation = BinaryAssociation(
    name="variadic_exp_list44",
    ends={
        Property(name="abs_Pure_exp_list46", type=abs_Pure_exp, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Pure_exp45", type=abs_Pure_exp_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
if48: BinaryAssociation = BinaryAssociation(
    name="if48",
    ends={
        Property(name="abs_Pure_exp49", type=abs_Pure_exp, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Pure_exp47", type=abs_Pure_exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
then51: BinaryAssociation = BinaryAssociation(
    name="then51",
    ends={
        Property(name="abs_Pure_exp52", type=abs_Pure_exp, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Pure_exp50", type=abs_Pure_exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
else54: BinaryAssociation = BinaryAssociation(
    name="else54",
    ends={
        Property(name="abs_Pure_exp55", type=abs_Pure_exp, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Pure_exp53", type=abs_Pure_exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
case57: BinaryAssociation = BinaryAssociation(
    name="case57",
    ends={
        Property(name="abs_Pure_exp58", type=abs_Pure_exp, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Pure_exp56", type=abs_Pure_exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
casebranch59: BinaryAssociation = BinaryAssociation(
    name="casebranch59",
    ends={
        Property(name="abs_Case_branch", type=abs_Pure_exp, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Pure_exp60", type=abs_Case_branch, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pure_exp79: BinaryAssociation = BinaryAssociation(
    name="pure_exp79",
    ends={
        Property(name="abs_Pure_exp81", type=abs_Pure_exp_list, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Pure_exp_list80", type=abs_Pure_exp, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
function_param82: BinaryAssociation = BinaryAssociation(
    name="function_param82",
    ends={
        Property(name="abs_Function_param", type=abs_Function_list, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Function_list83", type=abs_Function_param, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
params84: BinaryAssociation = BinaryAssociation(
    name="params84",
    ends={
        Property(name="abs_Param_list85", type=abs_Anon_function_decl, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Anon_function_decl", type=abs_Param_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pure_exp86: BinaryAssociation = BinaryAssociation(
    name="pure_exp86",
    ends={
        Property(name="abs_Pure_exp88", type=abs_Anon_function_decl, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Anon_function_decl87", type=abs_Pure_exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ref73: BinaryAssociation = BinaryAssociation(
    name="ref73",
    ends={
        Property(name="abs_Field_decl", type=abs_Var_or_field_ref, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Var_or_field_ref", type=abs_Field_decl, multiplicity=Multiplicity(0, 1))
    }
)
pure_exp74: BinaryAssociation = BinaryAssociation(
    name="pure_exp74",
    ends={
        Property(name="abs_Pure_exp75", type=abs_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Pattern", type=abs_Pure_exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pattern77: BinaryAssociation = BinaryAssociation(
    name="pattern77",
    ends={
        Property(name="abs_Pattern78", type=abs_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Pattern76", type=abs_Pattern, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type_use104: BinaryAssociation = BinaryAssociation(
    name="type_use104",
    ends={
        Property(name="abs_Type_use105", type=abs_Typesyn_decl, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Typesyn_decl", type=abs_Type_use, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type106: BinaryAssociation = BinaryAssociation(
    name="type106",
    ends={
        Property(name="abs_Data_constructor_arg107", type=abs_Exception_decl, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Exception_decl", type=abs_Data_constructor_arg, multiplicity=Multiplicity(0, 9999))
    }
)
interface_name109: BinaryAssociation = BinaryAssociation(
    name="interface_name109",
    ends={
        Property(name="abs_Interface_decl", type=abs_Interface_decl, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Interface_decl108", type=abs_Interface_decl, multiplicity=Multiplicity(0, 9999))
    }
)
methodsig110: BinaryAssociation = BinaryAssociation(
    name="methodsig110",
    ends={
        Property(name="abs_Methodsig", type=abs_Interface_decl, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Interface_decl111", type=abs_Methodsig, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type_use112: BinaryAssociation = BinaryAssociation(
    name="type_use112",
    ends={
        Property(name="abs_Type_use114", type=abs_Methodsig, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Methodsig113", type=abs_Type_use, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
param_decl89: BinaryAssociation = BinaryAssociation(
    name="param_decl89",
    ends={
        Property(name="abs_Param_decl", type=abs_Param_list, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Param_list90", type=abs_Param_decl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type_exp91: BinaryAssociation = BinaryAssociation(
    name="type_exp91",
    ends={
        Property(name="abs_Type_exp", type=abs_Param_decl, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Param_decl92", type=abs_Type_exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
p93: BinaryAssociation = BinaryAssociation(
    name="p93",
    ends={
        Property(name="abs_Type_use95", type=abs_Type_exp, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Type_exp94", type=abs_Type_use, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type_use96: BinaryAssociation = BinaryAssociation(
    name="type_use96",
    ends={
        Property(name="abs_Type_use97", type=abs_Function_decl, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Function_decl", type=abs_Type_use, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
paramlist98: BinaryAssociation = BinaryAssociation(
    name="paramlist98",
    ends={
        Property(name="abs_Param_list100", type=abs_Function_decl, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Function_decl99", type=abs_Param_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type_use134: BinaryAssociation = BinaryAssociation(
    name="type_use134",
    ends={
        Property(name="abs_Type_use136", type=abs_Field_decl, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Field_decl135", type=abs_Type_use, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pure_exp101: BinaryAssociation = BinaryAssociation(
    name="pure_exp101",
    ends={
        Property(name="abs_Pure_exp103", type=abs_Function_decl, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Function_decl102", type=abs_Pure_exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pure_exp137: BinaryAssociation = BinaryAssociation(
    name="pure_exp137",
    ends={
        Property(name="abs_Pure_exp139", type=abs_Field_decl, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Field_decl138", type=abs_Pure_exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type_exp140: BinaryAssociation = BinaryAssociation(
    name="type_exp140",
    ends={
        Property(name="abs_Type_exp142", type=abs_Stmt, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Stmt141", type=abs_Type_exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp143: BinaryAssociation = BinaryAssociation(
    name="exp143",
    ends={
        Property(name="abs_Exp", type=abs_Stmt, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Stmt144", type=abs_Exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
var_or_field_ref145: BinaryAssociation = BinaryAssociation(
    name="var_or_field_ref145",
    ends={
        Property(name="abs_Var_or_field_ref147", type=abs_Stmt, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Stmt146", type=abs_Var_or_field_ref, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stmt149: BinaryAssociation = BinaryAssociation(
    name="stmt149",
    ends={
        Property(name="abs_Stmt150", type=abs_Stmt, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Stmt148", type=abs_Stmt, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pure_exp151: BinaryAssociation = BinaryAssociation(
    name="pure_exp151",
    ends={
        Property(name="abs_Pure_exp153", type=abs_Stmt, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Stmt152", type=abs_Pure_exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifstmt155: BinaryAssociation = BinaryAssociation(
    name="ifstmt155",
    ends={
        Property(name="abs_Stmt156", type=abs_Stmt, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Stmt154", type=abs_Stmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
paramlist115: BinaryAssociation = BinaryAssociation(
    name="paramlist115",
    ends={
        Property(name="abs_Param_list117", type=abs_Methodsig, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Methodsig116", type=abs_Param_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
paramlist118: BinaryAssociation = BinaryAssociation(
    name="paramlist118",
    ends={
        Property(name="abs_Param_list119", type=abs_Class_decl, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Class_decl", type=abs_Param_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
interface_name120: BinaryAssociation = BinaryAssociation(
    name="interface_name120",
    ends={
        Property(name="abs_Interface_decl122", type=abs_Class_decl, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Class_decl121", type=abs_Interface_decl, multiplicity=Multiplicity(0, 9999))
    }
)
field_decl123: BinaryAssociation = BinaryAssociation(
    name="field_decl123",
    ends={
        Property(name="abs_Field_decl125", type=abs_Class_decl, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Class_decl124", type=abs_Field_decl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stmt126: BinaryAssociation = BinaryAssociation(
    name="stmt126",
    ends={
        Property(name="abs_Stmt", type=abs_Class_decl, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Class_decl127", type=abs_Stmt, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
casestmtbranch128: BinaryAssociation = BinaryAssociation(
    name="casestmtbranch128",
    ends={
        Property(name="abs_Casestmtbranch", type=abs_Class_decl, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Class_decl129", type=abs_Casestmtbranch, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
trait_usage130: BinaryAssociation = BinaryAssociation(
    name="trait_usage130",
    ends={
        Property(name="abs_Trait_usage", type=abs_Class_decl, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Class_decl131", type=abs_Trait_usage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
method132: BinaryAssociation = BinaryAssociation(
    name="method132",
    ends={
        Property(name="abs_Method", type=abs_Class_decl, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Class_decl133", type=abs_Method, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
f180: BinaryAssociation = BinaryAssociation(
    name="f180",
    ends={
        Property(name="abs_Pure_exp182", type=abs_Stmt, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Stmt181", type=abs_Pure_exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
t183: BinaryAssociation = BinaryAssociation(
    name="t183",
    ends={
        Property(name="abs_Pure_exp185", type=abs_Stmt, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Stmt184", type=abs_Pure_exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
throwPureExp186: BinaryAssociation = BinaryAssociation(
    name="throwPureExp186",
    ends={
        Property(name="abs_Pure_exp188", type=abs_Stmt, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Stmt187", type=abs_Pure_exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
diePureExp189: BinaryAssociation = BinaryAssociation(
    name="diePureExp189",
    ends={
        Property(name="abs_Pure_exp191", type=abs_Stmt, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Stmt190", type=abs_Pure_exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
moveCogTo192: BinaryAssociation = BinaryAssociation(
    name="moveCogTo192",
    ends={
        Property(name="abs_Pure_exp194", type=abs_Stmt, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Stmt193", type=abs_Pure_exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
c195: BinaryAssociation = BinaryAssociation(
    name="c195",
    ends={
        Property(name="abs_Pure_exp197", type=abs_Stmt, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Stmt196", type=abs_Pure_exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elsestmt158: BinaryAssociation = BinaryAssociation(
    name="elsestmt158",
    ends={
        Property(name="abs_Stmt159", type=abs_Stmt, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Stmt157", type=abs_Stmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition160: BinaryAssociation = BinaryAssociation(
    name="condition160",
    ends={
        Property(name="abs_Pure_exp162", type=abs_Stmt, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Stmt161", type=abs_Pure_exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
whilestmt164: BinaryAssociation = BinaryAssociation(
    name="whilestmt164",
    ends={
        Property(name="abs_Stmt165", type=abs_Stmt, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Stmt163", type=abs_Stmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
l166: BinaryAssociation = BinaryAssociation(
    name="l166",
    ends={
        Property(name="abs_Pure_exp168", type=abs_Stmt, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Stmt167", type=abs_Pure_exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
foreachstmt170: BinaryAssociation = BinaryAssociation(
    name="foreachstmt170",
    ends={
        Property(name="abs_Stmt171", type=abs_Stmt, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Stmt169", type=abs_Stmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
trystmt173: BinaryAssociation = BinaryAssociation(
    name="trystmt173",
    ends={
        Property(name="abs_Stmt174", type=abs_Stmt, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Stmt172", type=abs_Stmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
casestmtbranch175: BinaryAssociation = BinaryAssociation(
    name="casestmtbranch175",
    ends={
        Property(name="abs_Casestmtbranch177", type=abs_Stmt, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Stmt176", type=abs_Casestmtbranch, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ref178: BinaryAssociation = BinaryAssociation(
    name="ref178",
    ends={
        Property(name="abs_Guard", type=abs_Stmt, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Stmt179", type=abs_Guard, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ref203: BinaryAssociation = BinaryAssociation(
    name="ref203",
    ends={
        Property(name="abs_Var_or_field_ref205", type=abs_Guard, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Guard204", type=abs_Var_or_field_ref, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
min206: BinaryAssociation = BinaryAssociation(
    name="min206",
    ends={
        Property(name="abs_Pure_exp208", type=abs_Guard, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Guard207", type=abs_Pure_exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
max209: BinaryAssociation = BinaryAssociation(
    name="max209",
    ends={
        Property(name="abs_Pure_exp211", type=abs_Guard, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Guard210", type=abs_Pure_exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
guard212: BinaryAssociation = BinaryAssociation(
    name="guard212",
    ends={
        Property(name="abs_Pure_exp214", type=abs_Guard, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Guard213", type=abs_Pure_exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pattern215: BinaryAssociation = BinaryAssociation(
    name="pattern215",
    ends={
        Property(name="abs_Pattern217", type=abs_Casestmtbranch, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Casestmtbranch216", type=abs_Pattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pure_exp_list198: BinaryAssociation = BinaryAssociation(
    name="pure_exp_list198",
    ends={
        Property(name="abs_Pure_exp_list199", type=abs_Eff_expr, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Eff_expr", type=abs_Pure_exp_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
list200: BinaryAssociation = BinaryAssociation(
    name="list200",
    ends={
        Property(name="abs_Pure_exp_list202", type=abs_Eff_expr, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Eff_expr201", type=abs_Pure_exp_list, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
op231: BinaryAssociation = BinaryAssociation(
    name="op231",
    ends={
        Property(name="abs_Trait_oper", type=abs_Trait_expr, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Trait_expr232", type=abs_Trait_oper, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
trait_expr234: BinaryAssociation = BinaryAssociation(
    name="trait_expr234",
    ends={
        Property(name="abs_Trait_expr235", type=abs_Trait_expr, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Trait_expr233", type=abs_Trait_expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
method236: BinaryAssociation = BinaryAssociation(
    name="method236",
    ends={
        Property(name="abs_Methodsig238", type=abs_Trait_oper, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Trait_oper237", type=abs_Methodsig, multiplicity=Multiplicity(0, 1))
    }
)
methodsig239: BinaryAssociation = BinaryAssociation(
    name="methodsig239",
    ends={
        Property(name="abs_Methodsig241", type=abs_Trait_oper, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Trait_oper240", type=abs_Methodsig, multiplicity=Multiplicity(0, 9999))
    }
)
trait_expr242: BinaryAssociation = BinaryAssociation(
    name="trait_expr242",
    ends={
        Property(name="abs_Trait_expr244", type=abs_Trait_oper, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Trait_oper243", type=abs_Trait_expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
trait_exp245: BinaryAssociation = BinaryAssociation(
    name="trait_exp245",
    ends={
        Property(name="abs_Trait_expr247", type=abs_Trait_oper, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Trait_oper246", type=abs_Trait_expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stmt218: BinaryAssociation = BinaryAssociation(
    name="stmt218",
    ends={
        Property(name="abs_Stmt220", type=abs_Casestmtbranch, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Casestmtbranch219", type=abs_Stmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
traitUsage221: BinaryAssociation = BinaryAssociation(
    name="traitUsage221",
    ends={
        Property(name="abs_Trait_decl", type=abs_Trait_usage, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Trait_usage222", type=abs_Trait_decl, multiplicity=Multiplicity(0, 9999))
    }
)
method223: BinaryAssociation = BinaryAssociation(
    name="method223",
    ends={
        Property(name="abs_Method224", type=abs_Trait_expr, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Trait_expr", type=abs_Method, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
traitMethod225: BinaryAssociation = BinaryAssociation(
    name="traitMethod225",
    ends={
        Property(name="abs_Method227", type=abs_Trait_expr, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Trait_expr226", type=abs_Method, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
traitName228: BinaryAssociation = BinaryAssociation(
    name="traitName228",
    ends={
        Property(name="abs_Trait_decl230", type=abs_Trait_expr, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Trait_expr229", type=abs_Trait_decl, multiplicity=Multiplicity(0, 1))
    }
)
p263: BinaryAssociation = BinaryAssociation(
    name="p263",
    ends={
        Property(name="abs_Delta_param", type=abs_Delta_decl, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Delta_decl264", type=abs_Delta_param, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
delta_access265: BinaryAssociation = BinaryAssociation(
    name="delta_access265",
    ends={
        Property(name="abs_Delta_access", type=abs_Delta_decl, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Delta_decl266", type=abs_Delta_access, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
module_modifier267: BinaryAssociation = BinaryAssociation(
    name="module_modifier267",
    ends={
        Property(name="abs_Module_modifier", type=abs_Delta_decl, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Delta_decl268", type=abs_Module_modifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
field269: BinaryAssociation = BinaryAssociation(
    name="field269",
    ends={
        Property(name="abs_Field_decl270", type=abs_Has_condition, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Has_condition", type=abs_Field_decl, multiplicity=Multiplicity(0, 1))
    }
)
method271: BinaryAssociation = BinaryAssociation(
    name="method271",
    ends={
        Property(name="abs_Methodsig273", type=abs_Has_condition, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Has_condition272", type=abs_Methodsig, multiplicity=Multiplicity(0, 1))
    }
)
type_use248: BinaryAssociation = BinaryAssociation(
    name="type_use248",
    ends={
        Property(name="abs_Type_use250", type=abs_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Method249", type=abs_Type_use, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
interface274: BinaryAssociation = BinaryAssociation(
    name="interface274",
    ends={
        Property(name="abs_Interface_decl276", type=abs_Has_condition, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Has_condition275", type=abs_Interface_decl, multiplicity=Multiplicity(0, 1))
    }
)
paramlist251: BinaryAssociation = BinaryAssociation(
    name="paramlist251",
    ends={
        Property(name="abs_Param_list253", type=abs_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Method252", type=abs_Param_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stmt254: BinaryAssociation = BinaryAssociation(
    name="stmt254",
    ends={
        Property(name="abs_Stmt256", type=abs_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Method255", type=abs_Stmt, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
traitExpr257: BinaryAssociation = BinaryAssociation(
    name="traitExpr257",
    ends={
        Property(name="abs_Trait_expr259", type=abs_Trait_decl, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Trait_decl258", type=abs_Trait_expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stmt260: BinaryAssociation = BinaryAssociation(
    name="stmt260",
    ends={
        Property(name="abs_Stmt262", type=abs_Main_block, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Main_block261", type=abs_Stmt, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inteface288: BinaryAssociation = BinaryAssociation(
    name="inteface288",
    ends={
        Property(name="abs_Interface_decl290", type=abs_OO_modifier, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_OO_modifier289", type=abs_Interface_decl, multiplicity=Multiplicity(0, 1))
    }
)
interfaceName291: BinaryAssociation = BinaryAssociation(
    name="interfaceName291",
    ends={
        Property(name="abs_Interface_decl293", type=abs_OO_modifier, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_OO_modifier292", type=abs_Interface_decl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
removedInterface294: BinaryAssociation = BinaryAssociation(
    name="removedInterface294",
    ends={
        Property(name="abs_Interface_decl296", type=abs_OO_modifier, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_OO_modifier295", type=abs_Interface_decl, multiplicity=Multiplicity(0, 9999))
    }
)
class_modifier_fragment297: BinaryAssociation = BinaryAssociation(
    name="class_modifier_fragment297",
    ends={
        Property(name="abs_Class_modifier_fragment", type=abs_OO_modifier, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_OO_modifier298", type=abs_Class_modifier_fragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interface299: BinaryAssociation = BinaryAssociation(
    name="interface299",
    ends={
        Property(name="abs_Interface_decl301", type=abs_OO_modifier, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_OO_modifier300", type=abs_Interface_decl, multiplicity=Multiplicity(0, 1))
    }
)
interface_modifier_fragment302: BinaryAssociation = BinaryAssociation(
    name="interface_modifier_fragment302",
    ends={
        Property(name="abs_Interface_modifier_fragment", type=abs_OO_modifier, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_OO_modifier303", type=abs_Interface_modifier_fragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
module_ref277: BinaryAssociation = BinaryAssociation(
    name="module_ref277",
    ends={
        Property(name="abs_Module_decl279", type=abs_Delta_access, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Delta_access278", type=abs_Module_decl, multiplicity=Multiplicity(0, 1))
    }
)
class_decl280: BinaryAssociation = BinaryAssociation(
    name="class_decl280",
    ends={
        Property(name="abs_Class_decl281", type=abs_OO_modifier, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_OO_modifier", type=abs_Class_decl, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
interface_decl282: BinaryAssociation = BinaryAssociation(
    name="interface_decl282",
    ends={
        Property(name="abs_Interface_decl284", type=abs_OO_modifier, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_OO_modifier283", type=abs_Interface_decl, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
class285: BinaryAssociation = BinaryAssociation(
    name="class285",
    ends={
        Property(name="abs_Class_decl287", type=abs_OO_modifier, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_OO_modifier286", type=abs_Class_decl, multiplicity=Multiplicity(0, 1))
    }
)
update_preamble_declaration312: BinaryAssociation = BinaryAssociation(
    name="update_preamble_declaration312",
    ends={
        Property(name="abs_Update_preamble_declaration", type=abs_Object_update, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Object_update313", type=abs_Update_preamble_declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pre314: BinaryAssociation = BinaryAssociation(
    name="pre314",
    ends={
        Property(name="abs_Object_update_assign_stmt", type=abs_Object_update, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Object_update315", type=abs_Object_update_assign_stmt, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
post316: BinaryAssociation = BinaryAssociation(
    name="post316",
    ends={
        Property(name="abs_Object_update_assign_stmt318", type=abs_Object_update, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Object_update317", type=abs_Object_update_assign_stmt, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
var_or_field_ref319: BinaryAssociation = BinaryAssociation(
    name="var_or_field_ref319",
    ends={
        Property(name="abs_Var_or_field_ref321", type=abs_Object_update_assign_stmt, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Object_update_assign_stmt320", type=abs_Var_or_field_ref, multiplicity=Multiplicity(0, 1))
    }
)
exp322: BinaryAssociation = BinaryAssociation(
    name="exp322",
    ends={
        Property(name="abs_Exp324", type=abs_Object_update_assign_stmt, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Object_update_assign_stmt323", type=abs_Exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
methodsig304: BinaryAssociation = BinaryAssociation(
    name="methodsig304",
    ends={
        Property(name="abs_Methodsig306", type=abs_Class_modifier_fragment, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Class_modifier_fragment305", type=abs_Methodsig, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
object_update307: BinaryAssociation = BinaryAssociation(
    name="object_update307",
    ends={
        Property(name="abs_Object_update", type=abs_Update_decl, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Update_decl308", type=abs_Object_update, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
guard309: BinaryAssociation = BinaryAssociation(
    name="guard309",
    ends={
        Property(name="abs_Guard311", type=abs_Object_update, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Object_update310", type=abs_Guard, multiplicity=Multiplicity(0, 1))
    }
)
after_condition335: BinaryAssociation = BinaryAssociation(
    name="after_condition335",
    ends={
        Property(name="abs_After_condition", type=abs_Delta_clause, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Delta_clause336", type=abs_After_condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
from_condition337: BinaryAssociation = BinaryAssociation(
    name="from_condition337",
    ends={
        Property(name="abs_From_condition", type=abs_Delta_clause, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Delta_clause338", type=abs_From_condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
when_condition339: BinaryAssociation = BinaryAssociation(
    name="when_condition339",
    ends={
        Property(name="abs_When_condition", type=abs_Delta_clause, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Delta_clause340", type=abs_When_condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
delta_id341: BinaryAssociation = BinaryAssociation(
    name="delta_id341",
    ends={
        Property(name="abs_Delta_decl343", type=abs_After_condition, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_After_condition342", type=abs_Delta_decl, multiplicity=Multiplicity(0, 9999))
    }
)
feature325: BinaryAssociation = BinaryAssociation(
    name="feature325",
    ends={
        Property(name="abs_Feature", type=abs_Productline_decl, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Productline_decl326", type=abs_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
delta_clause327: BinaryAssociation = BinaryAssociation(
    name="delta_clause327",
    ends={
        Property(name="abs_Delta_clause", type=abs_Productline_decl, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Productline_decl328", type=abs_Delta_clause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
feature_decl329: BinaryAssociation = BinaryAssociation(
    name="feature_decl329",
    ends={
        Property(name="abs_Feature_decl331", type=abs_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Feature330", type=abs_Feature_decl, multiplicity=Multiplicity(0, 1))
    }
)
deltaspec332: BinaryAssociation = BinaryAssociation(
    name="deltaspec332",
    ends={
        Property(name="abs_Delta_decl334", type=abs_Delta_clause, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Delta_clause333", type=abs_Delta_decl, multiplicity=Multiplicity(0, 1))
    }
)
right359: BinaryAssociation = BinaryAssociation(
    name="right359",
    ends={
        Property(name="abs_Application_condition360", type=abs_Application_condition, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Application_condition358", type=abs_Application_condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
feature361: BinaryAssociation = BinaryAssociation(
    name="feature361",
    ends={
        Property(name="abs_Feature363", type=abs_Product_decl, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Product_decl362", type=abs_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
product_reconfiguration364: BinaryAssociation = BinaryAssociation(
    name="product_reconfiguration364",
    ends={
        Property(name="abs_Product_reconfiguration", type=abs_Product_decl, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Product_decl365", type=abs_Product_reconfiguration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
product_expr366: BinaryAssociation = BinaryAssociation(
    name="product_expr366",
    ends={
        Property(name="abs_Product_expr", type=abs_Product_decl, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Product_decl367", type=abs_Product_expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
feature368: BinaryAssociation = BinaryAssociation(
    name="feature368",
    ends={
        Property(name="abs_Feature_decl370", type=abs_Product_expr, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Product_expr369", type=abs_Feature_decl, multiplicity=Multiplicity(0, 9999))
    }
)
application_condition344: BinaryAssociation = BinaryAssociation(
    name="application_condition344",
    ends={
        Property(name="abs_Application_condition", type=abs_From_condition, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_From_condition345", type=abs_Application_condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
application_condition346: BinaryAssociation = BinaryAssociation(
    name="application_condition346",
    ends={
        Property(name="abs_Application_condition348", type=abs_When_condition, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_When_condition347", type=abs_Application_condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand350: BinaryAssociation = BinaryAssociation(
    name="operand350",
    ends={
        Property(name="abs_Application_condition351", type=abs_Application_condition, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Application_condition349", type=abs_Application_condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
feature352: BinaryAssociation = BinaryAssociation(
    name="feature352",
    ends={
        Property(name="abs_Feature354", type=abs_Application_condition, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Application_condition353", type=abs_Feature, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left356: BinaryAssociation = BinaryAssociation(
    name="left356",
    ends={
        Property(name="abs_Application_condition357", type=abs_Application_condition, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Application_condition355", type=abs_Application_condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
feature_decl_group382: BinaryAssociation = BinaryAssociation(
    name="feature_decl_group382",
    ends={
        Property(name="abs_Feature_decl_group", type=abs_Feature_decl, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Feature_decl383", type=abs_Feature_decl_group, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
feature_decl_attribute384: BinaryAssociation = BinaryAssociation(
    name="feature_decl_attribute384",
    ends={
        Property(name="abs_Feature_decl_attribute", type=abs_Feature_decl, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Feature_decl385", type=abs_Feature_decl_attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
feature_decl_constraint386: BinaryAssociation = BinaryAssociation(
    name="feature_decl_constraint386",
    ends={
        Property(name="abs_Feature_decl_constraint", type=abs_Feature_decl, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Feature_decl387", type=abs_Feature_decl_constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fnode388: BinaryAssociation = BinaryAssociation(
    name="fnode388",
    ends={
        Property(name="abs_Fnode", type=abs_Feature_decl_group, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Feature_decl_group389", type=abs_Fnode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
productDecl371: BinaryAssociation = BinaryAssociation(
    name="productDecl371",
    ends={
        Property(name="abs_Product_decl373", type=abs_Product_expr, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Product_expr372", type=abs_Product_decl, multiplicity=Multiplicity(0, 1))
    }
)
left375: BinaryAssociation = BinaryAssociation(
    name="left375",
    ends={
        Property(name="abs_Product_expr376", type=abs_Product_expr, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Product_expr374", type=abs_Product_expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right378: BinaryAssociation = BinaryAssociation(
    name="right378",
    ends={
        Property(name="abs_Product_expr379", type=abs_Product_expr, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Product_expr377", type=abs_Product_expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
delta_id380: BinaryAssociation = BinaryAssociation(
    name="delta_id380",
    ends={
        Property(name="abs_Delta_id", type=abs_Product_reconfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Product_reconfiguration381", type=abs_Delta_id, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
feature_decl_attribute395: BinaryAssociation = BinaryAssociation(
    name="feature_decl_attribute395",
    ends={
        Property(name="abs_Fextension396", type=abs_Feature_decl_attribute, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="abs_Feature_decl_attribute397", type=abs_Fextension, multiplicity=Multiplicity(1, 1))
    }
)
feature_decl_constraint398: BinaryAssociation = BinaryAssociation(
    name="feature_decl_constraint398",
    ends={
        Property(name="abs_Feature_decl_constraint400", type=abs_Fextension, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Fextension399", type=abs_Feature_decl_constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
left401: BinaryAssociation = BinaryAssociation(
    name="left401",
    ends={
        Property(name="abs_Pure_exp402", type=abs_Or_expr, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Or_expr", type=abs_Pure_exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right403: BinaryAssociation = BinaryAssociation(
    name="right403",
    ends={
        Property(name="abs_Pure_exp405", type=abs_Or_expr, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Or_expr404", type=abs_Pure_exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mexp390: BinaryAssociation = BinaryAssociation(
    name="mexp390",
    ends={
        Property(name="abs_Mexp", type=abs_Feature_decl_constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Feature_decl_constraint391", type=abs_Mexp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
feature_decl_group392: BinaryAssociation = BinaryAssociation(
    name="feature_decl_group392",
    ends={
        Property(name="abs_Feature_decl_group394", type=abs_Fextension, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Fextension393", type=abs_Feature_decl_group, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left411: BinaryAssociation = BinaryAssociation(
    name="left411",
    ends={
        Property(name="abs_Pure_exp412", type=abs_Equality_expr, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Equality_expr", type=abs_Pure_exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right413: BinaryAssociation = BinaryAssociation(
    name="right413",
    ends={
        Property(name="abs_Pure_exp415", type=abs_Equality_expr, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Equality_expr414", type=abs_Pure_exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left406: BinaryAssociation = BinaryAssociation(
    name="left406",
    ends={
        Property(name="abs_Pure_exp407", type=abs_And_expr, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_And_expr", type=abs_Pure_exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right408: BinaryAssociation = BinaryAssociation(
    name="right408",
    ends={
        Property(name="abs_Pure_exp410", type=abs_And_expr, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_And_expr409", type=abs_Pure_exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right428: BinaryAssociation = BinaryAssociation(
    name="right428",
    ends={
        Property(name="abs_Pure_exp430", type=abs_MulDivOrMod_expr, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_MulDivOrMod_expr429", type=abs_Pure_exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left431: BinaryAssociation = BinaryAssociation(
    name="left431",
    ends={
        Property(name="abs_Guard432", type=abs_AndGuard, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_AndGuard", type=abs_Guard, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right433: BinaryAssociation = BinaryAssociation(
    name="right433",
    ends={
        Property(name="abs_Guard435", type=abs_AndGuard, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_AndGuard434", type=abs_Guard, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left416: BinaryAssociation = BinaryAssociation(
    name="left416",
    ends={
        Property(name="abs_Pure_exp417", type=abs_Comparison_expr, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Comparison_expr", type=abs_Pure_exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right418: BinaryAssociation = BinaryAssociation(
    name="right418",
    ends={
        Property(name="abs_Pure_exp420", type=abs_Comparison_expr, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_Comparison_expr419", type=abs_Pure_exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left421: BinaryAssociation = BinaryAssociation(
    name="left421",
    ends={
        Property(name="abs_Pure_exp422", type=abs_PlusOrMinus_expr, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_PlusOrMinus_expr", type=abs_Pure_exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right423: BinaryAssociation = BinaryAssociation(
    name="right423",
    ends={
        Property(name="abs_Pure_exp425", type=abs_PlusOrMinus_expr, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_PlusOrMinus_expr424", type=abs_Pure_exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left426: BinaryAssociation = BinaryAssociation(
    name="left426",
    ends={
        Property(name="abs_Pure_exp427", type=abs_MulDivOrMod_expr, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_MulDivOrMod_expr", type=abs_Pure_exp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right448: BinaryAssociation = BinaryAssociation(
    name="right448",
    ends={
        Property(name="abs_Mexp450", type=abs_MexpImplies_expr, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_MexpImplies_expr449", type=abs_Mexp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left451: BinaryAssociation = BinaryAssociation(
    name="left451",
    ends={
        Property(name="abs_Mexp452", type=abs_MexpEquality_expr, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_MexpEquality_expr", type=abs_Mexp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right453: BinaryAssociation = BinaryAssociation(
    name="right453",
    ends={
        Property(name="abs_Mexp455", type=abs_MexpEquality_expr, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_MexpEquality_expr454", type=abs_Mexp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left436: BinaryAssociation = BinaryAssociation(
    name="left436",
    ends={
        Property(name="abs_Mexp437", type=abs_MexpOr_exp, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_MexpOr_exp", type=abs_Mexp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right438: BinaryAssociation = BinaryAssociation(
    name="right438",
    ends={
        Property(name="abs_Mexp440", type=abs_MexpOr_exp, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_MexpOr_exp439", type=abs_Mexp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left441: BinaryAssociation = BinaryAssociation(
    name="left441",
    ends={
        Property(name="abs_Mexp442", type=abs_MexpAnd_expr, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_MexpAnd_expr", type=abs_Mexp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right443: BinaryAssociation = BinaryAssociation(
    name="right443",
    ends={
        Property(name="abs_Mexp445", type=abs_MexpAnd_expr, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_MexpAnd_expr444", type=abs_Mexp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left446: BinaryAssociation = BinaryAssociation(
    name="left446",
    ends={
        Property(name="abs_Mexp447", type=abs_MexpImplies_expr, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_MexpImplies_expr", type=abs_Mexp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left461: BinaryAssociation = BinaryAssociation(
    name="left461",
    ends={
        Property(name="abs_Mexp462", type=abs_MexpPlusOrMinus_expr, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_MexpPlusOrMinus_expr", type=abs_Mexp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right463: BinaryAssociation = BinaryAssociation(
    name="right463",
    ends={
        Property(name="abs_Mexp465", type=abs_MexpPlusOrMinus_expr, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_MexpPlusOrMinus_expr464", type=abs_Mexp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left466: BinaryAssociation = BinaryAssociation(
    name="left466",
    ends={
        Property(name="abs_Mexp467", type=abs_MexpMulDivOrMod_expr, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_MexpMulDivOrMod_expr", type=abs_Mexp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right468: BinaryAssociation = BinaryAssociation(
    name="right468",
    ends={
        Property(name="abs_Mexp470", type=abs_MexpMulDivOrMod_expr, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_MexpMulDivOrMod_expr469", type=abs_Mexp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left456: BinaryAssociation = BinaryAssociation(
    name="left456",
    ends={
        Property(name="abs_Mexp457", type=abs_MexpComparison_expr, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_MexpComparison_expr", type=abs_Mexp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right458: BinaryAssociation = BinaryAssociation(
    name="right458",
    ends={
        Property(name="abs_Mexp460", type=abs_MexpComparison_expr, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_MexpComparison_expr459", type=abs_Mexp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
a471: BinaryAssociation = BinaryAssociation(
    name="a471",
    ends={
        Property(name="abs_Mexp472", type=abs_MexpPrimary_expr, multiplicity=Multiplicity(1, 1)),
        Property(name="abs_MexpPrimary_expr", type=abs_Mexp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_abs_Compilation_Unit_DomainModel = Generalization(general=DomainModel, specific=abs_Compilation_Unit)
gen_abs_Module_export_Namespace_modifier = Generalization(general=Namespace_modifier, specific=abs_Module_export)
gen_abs_Module_import_Namespace_modifier = Generalization(general=Namespace_modifier, specific=abs_Module_import)
gen_abs_DataType_decl_Decl = Generalization(general=Decl, specific=abs_DataType_decl)
gen_abs_DataType_decl_Functional_modifier = Generalization(general=Functional_modifier, specific=abs_DataType_decl)
gen_abs_Par_function_decl_Decl = Generalization(general=Decl, specific=abs_Par_function_decl)
gen_abs_Type_use_Annotation = Generalization(general=Annotation, specific=abs_Type_use)
gen_abs_Pure_exp_Exp = Generalization(general=Exp, specific=abs_Pure_exp)
gen_abs_Pure_exp_Eff_expr = Generalization(general=Eff_expr, specific=abs_Pure_exp)
gen_abs_Type_use_Data_constructor_arg = Generalization(general=Data_constructor_arg, specific=abs_Type_use)
gen_abs_Function_name_param_decl_Function_param = Generalization(general=Function_param, specific=abs_Function_name_param_decl)
gen_abs_Anon_function_decl_Function_param = Generalization(general=Function_param, specific=abs_Anon_function_decl)
gen_abs_Var_or_field_ref_Pure_exp = Generalization(general=Pure_exp, specific=abs_Var_or_field_ref)
gen_abs_Pattern_Case_branch = Generalization(general=Case_branch, specific=abs_Pattern)
gen_abs_Typesyn_decl_Decl = Generalization(general=Decl, specific=abs_Typesyn_decl)
gen_abs_Typesyn_decl_Functional_modifier = Generalization(general=Functional_modifier, specific=abs_Typesyn_decl)
gen_abs_Exception_decl_Decl = Generalization(general=Decl, specific=abs_Exception_decl)
gen_abs_Interface_decl_Decl = Generalization(general=Decl, specific=abs_Interface_decl)
gen_abs_Methodsig_Class_modifier_fragment = Generalization(general=Class_modifier_fragment, specific=abs_Methodsig)
gen_abs_Methodsig_Interface_modifier_fragment = Generalization(general=Interface_modifier_fragment, specific=abs_Methodsig)
gen_abs_Param_decl_Delta_param = Generalization(general=Delta_param, specific=abs_Param_decl)
gen_abs_Type_exp_Update_preamble_declaration = Generalization(general=Update_preamble_declaration, specific=abs_Type_exp)
gen_abs_Function_decl_Decl = Generalization(general=Decl, specific=abs_Function_decl)
gen_abs_Function_decl_Functional_modifier = Generalization(general=Functional_modifier, specific=abs_Function_decl)
gen_abs_Class_decl_Decl = Generalization(general=Decl, specific=abs_Class_decl)
gen_abs_Field_decl_Class_modifier_fragment = Generalization(general=Class_modifier_fragment, specific=abs_Field_decl)
gen_abs_Eff_expr_Exp = Generalization(general=Exp, specific=abs_Eff_expr)
gen_abs_Delta_id_Eff_expr = Generalization(general=Eff_expr, specific=abs_Delta_id)
gen_abs_Trait_expr_Class_modifier_fragment = Generalization(general=Class_modifier_fragment, specific=abs_Trait_expr)
gen_abs_Has_condition_Delta_param = Generalization(general=Delta_param, specific=abs_Has_condition)
gen_abs_Trait_decl_Decl = Generalization(general=Decl, specific=abs_Trait_decl)
gen_abs_Functional_modifier_Module_modifier = Generalization(general=Module_modifier, specific=abs_Functional_modifier)
gen_abs_OO_modifier_Module_modifier = Generalization(general=Module_modifier, specific=abs_OO_modifier)
gen_abs_Namespace_modifier_Module_modifier = Generalization(general=Module_modifier, specific=abs_Namespace_modifier)
gen_abs_Feature_decl_Fnode = Generalization(general=Fnode, specific=abs_Feature_decl)
gen_abs_Or_expr_Pure_exp = Generalization(general=Pure_exp, specific=abs_Or_expr)
gen_abs_And_expr_Pure_exp = Generalization(general=Pure_exp, specific=abs_And_expr)
gen_abs_Equality_expr_Pure_exp = Generalization(general=Pure_exp, specific=abs_Equality_expr)
gen_abs_Comparison_expr_Pure_exp = Generalization(general=Pure_exp, specific=abs_Comparison_expr)
gen_abs_AndGuard_Guard = Generalization(general=Guard, specific=abs_AndGuard)
gen_abs_AppOr_exp_Application_condition = Generalization(general=Application_condition, specific=abs_AppOr_exp)
gen_abs_AppAnd_exp_Application_condition = Generalization(general=Application_condition, specific=abs_AppAnd_exp)
gen_abs_ProductOr_expr_Product_expr = Generalization(general=Product_expr, specific=abs_ProductOr_expr)
gen_abs_ProductAnd_exp_Product_expr = Generalization(general=Product_expr, specific=abs_ProductAnd_exp)
gen_abs_ProductMinus_exp_Product_expr = Generalization(general=Product_expr, specific=abs_ProductMinus_exp)
gen_abs_MexpOr_exp_Mexp = Generalization(general=Mexp, specific=abs_MexpOr_exp)
gen_abs_PlusOrMinus_expr_Pure_exp = Generalization(general=Pure_exp, specific=abs_PlusOrMinus_expr)
gen_abs_MulDivOrMod_expr_Pure_exp = Generalization(general=Pure_exp, specific=abs_MulDivOrMod_expr)
gen_abs_MexpEquality_expr_Mexp = Generalization(general=Mexp, specific=abs_MexpEquality_expr)
gen_abs_MexpAnd_expr_Mexp = Generalization(general=Mexp, specific=abs_MexpAnd_expr)
gen_abs_MexpImplies_expr_Mexp = Generalization(general=Mexp, specific=abs_MexpImplies_expr)
gen_abs_MexpMulDivOrMod_expr_Mexp = Generalization(general=Mexp, specific=abs_MexpMulDivOrMod_expr)
gen_abs_MexpComparison_expr_Mexp = Generalization(general=Mexp, specific=abs_MexpComparison_expr)
gen_abs_MexpPlusOrMinus_expr_Mexp = Generalization(general=Mexp, specific=abs_MexpPlusOrMinus_expr)
gen_abs_MexpPrimary_expr_Mexp = Generalization(general=Mexp, specific=abs_MexpPrimary_expr)

# Domain Model
domain_model = DomainModel(
    name="abs",
    types={abs_Delta_decl, abs_Update_decl, abs_Productline_decl, abs_Product_decl, abs_DomainModel, abs_Compilation_Unit, DomainModel, abs_Module_decl, Namespace_modifier, abs_Feature_decl, abs_Fextension, abs_Module_export, abs_Module_import, abs_Decl, abs_Main_block, abs_Function_name_decl, abs_DataType_decl, Functional_modifier, abs_Data_constructor, abs_Par_function_decl, Decl, abs_Type_use, abs_Function_name_list, abs_Param_list, abs_Pure_exp, Annotation, Exp, Eff_expr, abs_Function_list, abs_Pure_exp_list, abs_Data_constructor_arg, abs_Annotations, abs_Annotation, Data_constructor_arg, abs_Case_branch, abs_Function_param, abs_Function_name_param_decl, Function_param, abs_Anon_function_decl, abs_Var_or_field_ref, Pure_exp, abs_Field_decl, abs_Pattern, Case_branch, abs_Typesyn_decl, abs_Exception_decl, abs_Interface_decl, abs_Methodsig, abs_Interface_name, Class_modifier_fragment, Interface_modifier_fragment, abs_Param_decl, Delta_param, abs_Type_exp, Update_preamble_declaration, abs_Function_decl, abs_Exp, abs_Class_decl, abs_Stmt, abs_Casestmtbranch, abs_Trait_usage, abs_Method, abs_Guard, abs_Eff_expr, abs_Delta_id, abs_Trait_oper, abs_Trait_decl, abs_Trait_expr, abs_Delta_param, abs_Delta_access, abs_Module_modifier, abs_Has_condition, abs_Class_modifier_fragment, abs_Interface_modifier_fragment, abs_Functional_modifier, Module_modifier, abs_OO_modifier, abs_Update_preamble_declaration, abs_Object_update_assign_stmt, abs_Namespace_modifier, abs_Object_update, abs_After_condition, abs_From_condition, abs_When_condition, abs_Deltaspec, abs_Feature, abs_Delta_clause, abs_Product_reconfiguration, abs_Product_expr, abs_Application_condition, Fnode, abs_Feature_decl_group, abs_Feature_decl_attribute, abs_Feature_decl_constraint, abs_Fnode, abs_Or_expr, abs_And_expr, abs_Mexp, abs_Equality_expr, abs_Comparison_expr, abs_AndGuard, Guard, abs_AppOr_exp, Application_condition, abs_AppAnd_exp, abs_ProductOr_expr, Product_expr, abs_ProductAnd_exp, abs_ProductMinus_exp, abs_MexpOr_exp, Mexp, abs_PlusOrMinus_expr, abs_MulDivOrMod_expr, abs_MexpEquality_expr, abs_MexpAnd_expr, abs_MexpImplies_expr, abs_MexpMulDivOrMod_expr, abs_MexpComparison_expr, abs_MexpPlusOrMinus_expr, abs_MexpPrimary_expr},
    associations={deltaDecl1, update_decl3, productline_decl5, product_decl7, module0, main_block19, feature_decl9, fextension11, module_export13, module_import15, decl17, function_name_decl28, data_constructor30, type_use21, functions22, params24, e26, type_use38, function_list40, partial_function_pure_exp_list42, data_constructor_arg31, annotation33, pure_exp34, type_use61, i65, b68, pure_exp71, variadic_exp_list44, if48, then51, else54, case57, casebranch59, pure_exp79, function_param82, params84, pure_exp86, ref73, pure_exp74, pattern77, type_use104, type106, interface_name109, methodsig110, type_use112, param_decl89, type_exp91, p93, type_use96, paramlist98, type_use134, pure_exp101, pure_exp137, type_exp140, exp143, var_or_field_ref145, stmt149, pure_exp151, ifstmt155, paramlist115, paramlist118, interface_name120, field_decl123, stmt126, casestmtbranch128, trait_usage130, method132, f180, t183, throwPureExp186, diePureExp189, moveCogTo192, c195, elsestmt158, condition160, whilestmt164, l166, foreachstmt170, trystmt173, casestmtbranch175, ref178, ref203, min206, max209, guard212, pattern215, pure_exp_list198, list200, op231, trait_expr234, method236, methodsig239, trait_expr242, trait_exp245, stmt218, traitUsage221, method223, traitMethod225, traitName228, p263, delta_access265, module_modifier267, field269, method271, type_use248, interface274, paramlist251, stmt254, traitExpr257, stmt260, inteface288, interfaceName291, removedInterface294, class_modifier_fragment297, interface299, interface_modifier_fragment302, module_ref277, class_decl280, interface_decl282, class285, update_preamble_declaration312, pre314, post316, var_or_field_ref319, exp322, methodsig304, object_update307, guard309, after_condition335, from_condition337, when_condition339, delta_id341, feature325, delta_clause327, feature_decl329, deltaspec332, right359, feature361, product_reconfiguration364, product_expr366, feature368, application_condition344, application_condition346, operand350, feature352, left356, feature_decl_group382, feature_decl_attribute384, feature_decl_constraint386, fnode388, productDecl371, left375, right378, delta_id380, feature_decl_attribute395, feature_decl_constraint398, left401, right403, mexp390, feature_decl_group392, left411, right413, left406, right408, right428, left431, right433, left416, right418, left421, right423, left426, right448, left451, right453, left436, right438, left441, right443, left446, left461, right463, left466, right468, left456, right458, a471},
    generalizations={gen_abs_Compilation_Unit_DomainModel, gen_abs_Module_export_Namespace_modifier, gen_abs_Module_import_Namespace_modifier, gen_abs_DataType_decl_Decl, gen_abs_DataType_decl_Functional_modifier, gen_abs_Par_function_decl_Decl, gen_abs_Type_use_Annotation, gen_abs_Pure_exp_Exp, gen_abs_Pure_exp_Eff_expr, gen_abs_Type_use_Data_constructor_arg, gen_abs_Function_name_param_decl_Function_param, gen_abs_Anon_function_decl_Function_param, gen_abs_Var_or_field_ref_Pure_exp, gen_abs_Pattern_Case_branch, gen_abs_Typesyn_decl_Decl, gen_abs_Typesyn_decl_Functional_modifier, gen_abs_Exception_decl_Decl, gen_abs_Interface_decl_Decl, gen_abs_Methodsig_Class_modifier_fragment, gen_abs_Methodsig_Interface_modifier_fragment, gen_abs_Param_decl_Delta_param, gen_abs_Type_exp_Update_preamble_declaration, gen_abs_Function_decl_Decl, gen_abs_Function_decl_Functional_modifier, gen_abs_Class_decl_Decl, gen_abs_Field_decl_Class_modifier_fragment, gen_abs_Eff_expr_Exp, gen_abs_Delta_id_Eff_expr, gen_abs_Trait_expr_Class_modifier_fragment, gen_abs_Has_condition_Delta_param, gen_abs_Trait_decl_Decl, gen_abs_Functional_modifier_Module_modifier, gen_abs_OO_modifier_Module_modifier, gen_abs_Namespace_modifier_Module_modifier, gen_abs_Feature_decl_Fnode, gen_abs_Or_expr_Pure_exp, gen_abs_And_expr_Pure_exp, gen_abs_Equality_expr_Pure_exp, gen_abs_Comparison_expr_Pure_exp, gen_abs_AndGuard_Guard, gen_abs_AppOr_exp_Application_condition, gen_abs_AppAnd_exp_Application_condition, gen_abs_ProductOr_expr_Product_expr, gen_abs_ProductAnd_exp_Product_expr, gen_abs_ProductMinus_exp_Product_expr, gen_abs_MexpOr_exp_Mexp, gen_abs_PlusOrMinus_expr_Pure_exp, gen_abs_MulDivOrMod_expr_Pure_exp, gen_abs_MexpEquality_expr_Mexp, gen_abs_MexpAnd_expr_Mexp, gen_abs_MexpImplies_expr_Mexp, gen_abs_MexpMulDivOrMod_expr_Mexp, gen_abs_MexpComparison_expr_Mexp, gen_abs_MexpPlusOrMinus_expr_Mexp, gen_abs_MexpPrimary_expr_Mexp},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)