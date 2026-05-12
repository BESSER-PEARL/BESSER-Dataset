import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Mexp,
    abs_MexpAnd_expr,
    abs_MexpMulDivOrMod_expr,
    abs_MexpImplies_expr,
    abs_MexpPrimary_expr,
    abs_MexpPlusOrMinus_expr,
    abs_MexpOr_exp,
    Product_expr,
    abs_ProductMinus_exp,
    abs_ProductAnd_exp,
    abs_ProductOr_expr,
    Application_condition,
    abs_AppAnd_exp,
    abs_AppOr_exp,
    abs_MexpComparison_expr,
    abs_MexpEquality_expr,
    Guard,
    abs_AndGuard,
    abs_Mexp,
    abs_Fnode,
    abs_Feature_decl_constraint,
    abs_Feature_decl_attribute,
    abs_Feature_decl_group,
    Fnode,
    abs_Product_expr,
    abs_Product_reconfiguration,
    abs_Application_condition,
    abs_Deltaspec,
    abs_When_condition,
    abs_From_condition,
    abs_After_condition,
    abs_Class_modifier_fragment,
    abs_Delta_clause,
    abs_Feature,
    abs_Object_update_assign_stmt,
    abs_Update_preamble_declaration,
    abs_Object_update,
    abs_Interface_modifier_fragment,
    Module_modifier,
    abs_OO_modifier,
    abs_Namespace_modifier,
    abs_Functional_modifier,
    abs_Module_modifier,
    abs_Delta_access,
    abs_Delta_param,
    abs_Trait_oper,
    abs_Guard,
    Interface_modifier_fragment,
    Class_modifier_fragment,
    abs_Trait_expr,
    abs_Interface_name,
    abs_Methodsig,
    abs_Exp,
    abs_Method,
    abs_Trait_usage,
    abs_Casestmtbranch,
    abs_Stmt,
    Case_branch,
    abs_Pattern,
    abs_Field_decl,
    Pure_exp,
    abs_Or_expr,
    abs_And_expr,
    abs_Equality_expr,
    abs_MulDivOrMod_expr,
    abs_PlusOrMinus_expr,
    abs_Comparison_expr,
    abs_Var_or_field_ref,
    Update_preamble_declaration,
    abs_Type_exp,
    Delta_param,
    abs_Has_condition,
    abs_Param_decl,
    Function_param,
    abs_Anon_function_decl,
    abs_Function_name_param_decl,
    abs_Pure_exp_list,
    abs_Function_param,
    abs_Function_list,
    Eff_expr,
    abs_Delta_id,
    Exp,
    abs_Eff_expr,
    Annotation,
    Data_constructor_arg,
    abs_Case_branch,
    abs_Main_block,
    abs_Decl,
    abs_Fextension,
    abs_Feature_decl,
    abs_Annotation,
    abs_Annotations,
    abs_Data_constructor_arg,
    abs_Data_constructor,
    Functional_modifier,
    abs_Function_name_decl,
    abs_Pure_exp,
    abs_Param_list,
    abs_Function_name_list,
    abs_Type_use,
    Decl,
    abs_Function_decl,
    abs_Interface_decl,
    abs_Exception_decl,
    abs_DataType_decl,
    abs_Trait_decl,
    abs_Typesyn_decl,
    abs_Class_decl,
    abs_Par_function_decl,
    Namespace_modifier,
    abs_Module_import,
    abs_Module_export,
    abs_Product_decl,
    abs_Productline_decl,
    abs_Update_decl,
    abs_Delta_decl,
    abs_Module_decl,
    DomainModel_,
    abs_Compilation_Unit,
    abs_DomainModel_,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mexp_is_not_abstract():
    assert not inspect.isabstract(Mexp)


def test_mexp_constructor_exists():
    assert callable(Mexp.__init__)


def test_mexp_constructor_args():
    sig = inspect.signature(Mexp.__init__)
    params = list(sig.parameters.keys())



def test_abs_mexpand_expr_is_not_abstract():
    assert not inspect.isabstract(abs_MexpAnd_expr)


def test_abs_mexpand_expr_constructor_exists():
    assert callable(abs_MexpAnd_expr.__init__)


def test_abs_mexpand_expr_constructor_args():
    sig = inspect.signature(abs_MexpAnd_expr.__init__)
    params = list(sig.parameters.keys())



def test_abs_mexpmuldivormod_expr_is_not_abstract():
    assert not inspect.isabstract(abs_MexpMulDivOrMod_expr)


def test_abs_mexpmuldivormod_expr_constructor_exists():
    assert callable(abs_MexpMulDivOrMod_expr.__init__)


def test_abs_mexpmuldivormod_expr_constructor_args():
    sig = inspect.signature(abs_MexpMulDivOrMod_expr.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_abs_mexpmuldivormod_expr_has_op():
    assert hasattr(abs_MexpMulDivOrMod_expr, "op")
    descriptor = None
    for klass in abs_MexpMulDivOrMod_expr.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_abs_mexpimplies_expr_is_not_abstract():
    assert not inspect.isabstract(abs_MexpImplies_expr)


def test_abs_mexpimplies_expr_constructor_exists():
    assert callable(abs_MexpImplies_expr.__init__)


def test_abs_mexpimplies_expr_constructor_args():
    sig = inspect.signature(abs_MexpImplies_expr.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_abs_mexpimplies_expr_has_op():
    assert hasattr(abs_MexpImplies_expr, "op")
    descriptor = None
    for klass in abs_MexpImplies_expr.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_abs_mexpprimary_expr_is_not_abstract():
    assert not inspect.isabstract(abs_MexpPrimary_expr)


def test_abs_mexpprimary_expr_constructor_exists():
    assert callable(abs_MexpPrimary_expr.__init__)


def test_abs_mexpprimary_expr_constructor_args():
    sig = inspect.signature(abs_MexpPrimary_expr.__init__)
    params = list(sig.parameters.keys())



def test_abs_mexpplusorminus_expr_is_not_abstract():
    assert not inspect.isabstract(abs_MexpPlusOrMinus_expr)


def test_abs_mexpplusorminus_expr_constructor_exists():
    assert callable(abs_MexpPlusOrMinus_expr.__init__)


def test_abs_mexpplusorminus_expr_constructor_args():
    sig = inspect.signature(abs_MexpPlusOrMinus_expr.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_abs_mexpplusorminus_expr_has_op():
    assert hasattr(abs_MexpPlusOrMinus_expr, "op")
    descriptor = None
    for klass in abs_MexpPlusOrMinus_expr.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_abs_mexpor_exp_is_not_abstract():
    assert not inspect.isabstract(abs_MexpOr_exp)


def test_abs_mexpor_exp_constructor_exists():
    assert callable(abs_MexpOr_exp.__init__)


def test_abs_mexpor_exp_constructor_args():
    sig = inspect.signature(abs_MexpOr_exp.__init__)
    params = list(sig.parameters.keys())



def test_product_expr_is_not_abstract():
    assert not inspect.isabstract(Product_expr)


def test_product_expr_constructor_exists():
    assert callable(Product_expr.__init__)


def test_product_expr_constructor_args():
    sig = inspect.signature(Product_expr.__init__)
    params = list(sig.parameters.keys())



def test_abs_productminus_exp_is_not_abstract():
    assert not inspect.isabstract(abs_ProductMinus_exp)


def test_abs_productminus_exp_constructor_exists():
    assert callable(abs_ProductMinus_exp.__init__)


def test_abs_productminus_exp_constructor_args():
    sig = inspect.signature(abs_ProductMinus_exp.__init__)
    params = list(sig.parameters.keys())



def test_abs_productand_exp_is_not_abstract():
    assert not inspect.isabstract(abs_ProductAnd_exp)


def test_abs_productand_exp_constructor_exists():
    assert callable(abs_ProductAnd_exp.__init__)


def test_abs_productand_exp_constructor_args():
    sig = inspect.signature(abs_ProductAnd_exp.__init__)
    params = list(sig.parameters.keys())



def test_abs_productor_expr_is_not_abstract():
    assert not inspect.isabstract(abs_ProductOr_expr)


def test_abs_productor_expr_constructor_exists():
    assert callable(abs_ProductOr_expr.__init__)


def test_abs_productor_expr_constructor_args():
    sig = inspect.signature(abs_ProductOr_expr.__init__)
    params = list(sig.parameters.keys())



def test_application_condition_is_not_abstract():
    assert not inspect.isabstract(Application_condition)


def test_application_condition_constructor_exists():
    assert callable(Application_condition.__init__)


def test_application_condition_constructor_args():
    sig = inspect.signature(Application_condition.__init__)
    params = list(sig.parameters.keys())



def test_abs_appand_exp_is_not_abstract():
    assert not inspect.isabstract(abs_AppAnd_exp)


def test_abs_appand_exp_constructor_exists():
    assert callable(abs_AppAnd_exp.__init__)


def test_abs_appand_exp_constructor_args():
    sig = inspect.signature(abs_AppAnd_exp.__init__)
    params = list(sig.parameters.keys())



def test_abs_appor_exp_is_not_abstract():
    assert not inspect.isabstract(abs_AppOr_exp)


def test_abs_appor_exp_constructor_exists():
    assert callable(abs_AppOr_exp.__init__)


def test_abs_appor_exp_constructor_args():
    sig = inspect.signature(abs_AppOr_exp.__init__)
    params = list(sig.parameters.keys())



def test_abs_mexpcomparison_expr_is_not_abstract():
    assert not inspect.isabstract(abs_MexpComparison_expr)


def test_abs_mexpcomparison_expr_constructor_exists():
    assert callable(abs_MexpComparison_expr.__init__)


def test_abs_mexpcomparison_expr_constructor_args():
    sig = inspect.signature(abs_MexpComparison_expr.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_abs_mexpcomparison_expr_has_op():
    assert hasattr(abs_MexpComparison_expr, "op")
    descriptor = None
    for klass in abs_MexpComparison_expr.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_abs_mexpequality_expr_is_not_abstract():
    assert not inspect.isabstract(abs_MexpEquality_expr)


def test_abs_mexpequality_expr_constructor_exists():
    assert callable(abs_MexpEquality_expr.__init__)


def test_abs_mexpequality_expr_constructor_args():
    sig = inspect.signature(abs_MexpEquality_expr.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_abs_mexpequality_expr_has_op():
    assert hasattr(abs_MexpEquality_expr, "op")
    descriptor = None
    for klass in abs_MexpEquality_expr.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_guard_is_not_abstract():
    assert not inspect.isabstract(Guard)


def test_guard_constructor_exists():
    assert callable(Guard.__init__)


def test_guard_constructor_args():
    sig = inspect.signature(Guard.__init__)
    params = list(sig.parameters.keys())



def test_abs_andguard_is_not_abstract():
    assert not inspect.isabstract(abs_AndGuard)


def test_abs_andguard_constructor_exists():
    assert callable(abs_AndGuard.__init__)


def test_abs_andguard_constructor_args():
    sig = inspect.signature(abs_AndGuard.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_abs_andguard_has_op():
    assert hasattr(abs_AndGuard, "op")
    descriptor = None
    for klass in abs_AndGuard.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_abs_mexp_is_not_abstract():
    assert not inspect.isabstract(abs_Mexp)


def test_abs_mexp_constructor_exists():
    assert callable(abs_Mexp.__init__)


def test_abs_mexp_constructor_args():
    sig = inspect.signature(abs_Mexp.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_abs_mexp_has_value():
    assert hasattr(abs_Mexp, "value")
    descriptor = None
    for klass in abs_Mexp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_abs_fnode_is_not_abstract():
    assert not inspect.isabstract(abs_Fnode)


def test_abs_fnode_constructor_exists():
    assert callable(abs_Fnode.__init__)


def test_abs_fnode_constructor_args():
    sig = inspect.signature(abs_Fnode.__init__)
    params = list(sig.parameters.keys())



def test_abs_feature_decl_constraint_is_not_abstract():
    assert not inspect.isabstract(abs_Feature_decl_constraint)


def test_abs_feature_decl_constraint_constructor_exists():
    assert callable(abs_Feature_decl_constraint.__init__)


def test_abs_feature_decl_constraint_constructor_args():
    sig = inspect.signature(abs_Feature_decl_constraint.__init__)
    params = list(sig.parameters.keys())



def test_abs_feature_decl_attribute_is_not_abstract():
    assert not inspect.isabstract(abs_Feature_decl_attribute)


def test_abs_feature_decl_attribute_constructor_exists():
    assert callable(abs_Feature_decl_attribute.__init__)


def test_abs_feature_decl_attribute_constructor_args():
    sig = inspect.signature(abs_Feature_decl_attribute.__init__)
    params = list(sig.parameters.keys())
    assert "boundary_val" in params, "Missing parameter 'boundary_val'"
    assert "uBoundary_int" in params, "Missing parameter 'uBoundary_int'"
    assert "lBoundary_int" in params, "Missing parameter 'lBoundary_int'"

def test_abs_feature_decl_attribute_has_boundary_val():
    assert hasattr(abs_Feature_decl_attribute, "boundary_val")
    descriptor = None
    for klass in abs_Feature_decl_attribute.__mro__:
        if "boundary_val" in klass.__dict__:
            descriptor = klass.__dict__["boundary_val"]
            break
    assert isinstance(descriptor, property)

def test_abs_feature_decl_attribute_has_uBoundary_int():
    assert hasattr(abs_Feature_decl_attribute, "uBoundary_int")
    descriptor = None
    for klass in abs_Feature_decl_attribute.__mro__:
        if "uBoundary_int" in klass.__dict__:
            descriptor = klass.__dict__["uBoundary_int"]
            break
    assert isinstance(descriptor, property)

def test_abs_feature_decl_attribute_has_lBoundary_int():
    assert hasattr(abs_Feature_decl_attribute, "lBoundary_int")
    descriptor = None
    for klass in abs_Feature_decl_attribute.__mro__:
        if "lBoundary_int" in klass.__dict__:
            descriptor = klass.__dict__["lBoundary_int"]
            break
    assert isinstance(descriptor, property)



def test_abs_feature_decl_group_is_not_abstract():
    assert not inspect.isabstract(abs_Feature_decl_group)


def test_abs_feature_decl_group_constructor_exists():
    assert callable(abs_Feature_decl_group.__init__)


def test_abs_feature_decl_group_constructor_args():
    sig = inspect.signature(abs_Feature_decl_group.__init__)
    params = list(sig.parameters.keys())



def test_fnode_is_not_abstract():
    assert not inspect.isabstract(Fnode)


def test_fnode_constructor_exists():
    assert callable(Fnode.__init__)


def test_fnode_constructor_args():
    sig = inspect.signature(Fnode.__init__)
    params = list(sig.parameters.keys())



def test_abs_product_expr_is_not_abstract():
    assert not inspect.isabstract(abs_Product_expr)


def test_abs_product_expr_constructor_exists():
    assert callable(abs_Product_expr.__init__)


def test_abs_product_expr_constructor_args():
    sig = inspect.signature(abs_Product_expr.__init__)
    params = list(sig.parameters.keys())



def test_abs_product_reconfiguration_is_not_abstract():
    assert not inspect.isabstract(abs_Product_reconfiguration)


def test_abs_product_reconfiguration_constructor_exists():
    assert callable(abs_Product_reconfiguration.__init__)


def test_abs_product_reconfiguration_constructor_args():
    sig = inspect.signature(abs_Product_reconfiguration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "update" in params, "Missing parameter 'update'"

def test_abs_product_reconfiguration_has_name():
    assert hasattr(abs_Product_reconfiguration, "name")
    descriptor = None
    for klass in abs_Product_reconfiguration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_abs_product_reconfiguration_has_update():
    assert hasattr(abs_Product_reconfiguration, "update")
    descriptor = None
    for klass in abs_Product_reconfiguration.__mro__:
        if "update" in klass.__dict__:
            descriptor = klass.__dict__["update"]
            break
    assert isinstance(descriptor, property)



def test_abs_application_condition_is_not_abstract():
    assert not inspect.isabstract(abs_Application_condition)


def test_abs_application_condition_constructor_exists():
    assert callable(abs_Application_condition.__init__)


def test_abs_application_condition_constructor_args():
    sig = inspect.signature(abs_Application_condition.__init__)
    params = list(sig.parameters.keys())



def test_abs_deltaspec_is_not_abstract():
    assert not inspect.isabstract(abs_Deltaspec)


def test_abs_deltaspec_constructor_exists():
    assert callable(abs_Deltaspec.__init__)


def test_abs_deltaspec_constructor_args():
    sig = inspect.signature(abs_Deltaspec.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "deltaspec_param" in params, "Missing parameter 'deltaspec_param'"

def test_abs_deltaspec_has_name():
    assert hasattr(abs_Deltaspec, "name")
    descriptor = None
    for klass in abs_Deltaspec.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_abs_deltaspec_has_deltaspec_param():
    assert hasattr(abs_Deltaspec, "deltaspec_param")
    descriptor = None
    for klass in abs_Deltaspec.__mro__:
        if "deltaspec_param" in klass.__dict__:
            descriptor = klass.__dict__["deltaspec_param"]
            break
    assert isinstance(descriptor, property)



def test_abs_when_condition_is_not_abstract():
    assert not inspect.isabstract(abs_When_condition)


def test_abs_when_condition_constructor_exists():
    assert callable(abs_When_condition.__init__)


def test_abs_when_condition_constructor_args():
    sig = inspect.signature(abs_When_condition.__init__)
    params = list(sig.parameters.keys())



def test_abs_from_condition_is_not_abstract():
    assert not inspect.isabstract(abs_From_condition)


def test_abs_from_condition_constructor_exists():
    assert callable(abs_From_condition.__init__)


def test_abs_from_condition_constructor_args():
    sig = inspect.signature(abs_From_condition.__init__)
    params = list(sig.parameters.keys())



def test_abs_after_condition_is_not_abstract():
    assert not inspect.isabstract(abs_After_condition)


def test_abs_after_condition_constructor_exists():
    assert callable(abs_After_condition.__init__)


def test_abs_after_condition_constructor_args():
    sig = inspect.signature(abs_After_condition.__init__)
    params = list(sig.parameters.keys())



def test_abs_class_modifier_fragment_is_not_abstract():
    assert not inspect.isabstract(abs_Class_modifier_fragment)


def test_abs_class_modifier_fragment_constructor_exists():
    assert callable(abs_Class_modifier_fragment.__init__)


def test_abs_class_modifier_fragment_constructor_args():
    sig = inspect.signature(abs_Class_modifier_fragment.__init__)
    params = list(sig.parameters.keys())



def test_abs_delta_clause_is_not_abstract():
    assert not inspect.isabstract(abs_Delta_clause)


def test_abs_delta_clause_constructor_exists():
    assert callable(abs_Delta_clause.__init__)


def test_abs_delta_clause_constructor_args():
    sig = inspect.signature(abs_Delta_clause.__init__)
    params = list(sig.parameters.keys())



def test_abs_feature_is_not_abstract():
    assert not inspect.isabstract(abs_Feature)


def test_abs_feature_constructor_exists():
    assert callable(abs_Feature.__init__)


def test_abs_feature_constructor_args():
    sig = inspect.signature(abs_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "p" in params, "Missing parameter 'p'"
    assert "attr_assignment" in params, "Missing parameter 'attr_assignment'"

def test_abs_feature_has_p():
    assert hasattr(abs_Feature, "p")
    descriptor = None
    for klass in abs_Feature.__mro__:
        if "p" in klass.__dict__:
            descriptor = klass.__dict__["p"]
            break
    assert isinstance(descriptor, property)

def test_abs_feature_has_attr_assignment():
    assert hasattr(abs_Feature, "attr_assignment")
    descriptor = None
    for klass in abs_Feature.__mro__:
        if "attr_assignment" in klass.__dict__:
            descriptor = klass.__dict__["attr_assignment"]
            break
    assert isinstance(descriptor, property)



def test_abs_object_update_assign_stmt_is_not_abstract():
    assert not inspect.isabstract(abs_Object_update_assign_stmt)


def test_abs_object_update_assign_stmt_constructor_exists():
    assert callable(abs_Object_update_assign_stmt.__init__)


def test_abs_object_update_assign_stmt_constructor_args():
    sig = inspect.signature(abs_Object_update_assign_stmt.__init__)
    params = list(sig.parameters.keys())



def test_abs_update_preamble_declaration_is_not_abstract():
    assert not inspect.isabstract(abs_Update_preamble_declaration)


def test_abs_update_preamble_declaration_constructor_exists():
    assert callable(abs_Update_preamble_declaration.__init__)


def test_abs_update_preamble_declaration_constructor_args():
    sig = inspect.signature(abs_Update_preamble_declaration.__init__)
    params = list(sig.parameters.keys())



def test_abs_object_update_is_not_abstract():
    assert not inspect.isabstract(abs_Object_update)


def test_abs_object_update_constructor_exists():
    assert callable(abs_Object_update.__init__)


def test_abs_object_update_constructor_args():
    sig = inspect.signature(abs_Object_update.__init__)
    params = list(sig.parameters.keys())



def test_abs_interface_modifier_fragment_is_not_abstract():
    assert not inspect.isabstract(abs_Interface_modifier_fragment)


def test_abs_interface_modifier_fragment_constructor_exists():
    assert callable(abs_Interface_modifier_fragment.__init__)


def test_abs_interface_modifier_fragment_constructor_args():
    sig = inspect.signature(abs_Interface_modifier_fragment.__init__)
    params = list(sig.parameters.keys())



def test_module_modifier_is_not_abstract():
    assert not inspect.isabstract(Module_modifier)


def test_module_modifier_constructor_exists():
    assert callable(Module_modifier.__init__)


def test_module_modifier_constructor_args():
    sig = inspect.signature(Module_modifier.__init__)
    params = list(sig.parameters.keys())



def test_abs_oo_modifier_is_not_abstract():
    assert not inspect.isabstract(abs_OO_modifier)


def test_abs_oo_modifier_constructor_exists():
    assert callable(abs_OO_modifier.__init__)


def test_abs_oo_modifier_constructor_args():
    sig = inspect.signature(abs_OO_modifier.__init__)
    params = list(sig.parameters.keys())



def test_abs_namespace_modifier_is_not_abstract():
    assert not inspect.isabstract(abs_Namespace_modifier)


def test_abs_namespace_modifier_constructor_exists():
    assert callable(abs_Namespace_modifier.__init__)


def test_abs_namespace_modifier_constructor_args():
    sig = inspect.signature(abs_Namespace_modifier.__init__)
    params = list(sig.parameters.keys())
    assert "star" in params, "Missing parameter 'star'"

def test_abs_namespace_modifier_has_star():
    assert hasattr(abs_Namespace_modifier, "star")
    descriptor = None
    for klass in abs_Namespace_modifier.__mro__:
        if "star" in klass.__dict__:
            descriptor = klass.__dict__["star"]
            break
    assert isinstance(descriptor, property)



def test_abs_functional_modifier_is_not_abstract():
    assert not inspect.isabstract(abs_Functional_modifier)


def test_abs_functional_modifier_constructor_exists():
    assert callable(abs_Functional_modifier.__init__)


def test_abs_functional_modifier_constructor_args():
    sig = inspect.signature(abs_Functional_modifier.__init__)
    params = list(sig.parameters.keys())



def test_abs_module_modifier_is_not_abstract():
    assert not inspect.isabstract(abs_Module_modifier)


def test_abs_module_modifier_constructor_exists():
    assert callable(abs_Module_modifier.__init__)


def test_abs_module_modifier_constructor_args():
    sig = inspect.signature(abs_Module_modifier.__init__)
    params = list(sig.parameters.keys())



def test_abs_delta_access_is_not_abstract():
    assert not inspect.isabstract(abs_Delta_access)


def test_abs_delta_access_constructor_exists():
    assert callable(abs_Delta_access.__init__)


def test_abs_delta_access_constructor_args():
    sig = inspect.signature(abs_Delta_access.__init__)
    params = list(sig.parameters.keys())



def test_abs_delta_param_is_not_abstract():
    assert not inspect.isabstract(abs_Delta_param)


def test_abs_delta_param_constructor_exists():
    assert callable(abs_Delta_param.__init__)


def test_abs_delta_param_constructor_args():
    sig = inspect.signature(abs_Delta_param.__init__)
    params = list(sig.parameters.keys())



def test_abs_trait_oper_is_not_abstract():
    assert not inspect.isabstract(abs_Trait_oper)


def test_abs_trait_oper_constructor_exists():
    assert callable(abs_Trait_oper.__init__)


def test_abs_trait_oper_constructor_args():
    sig = inspect.signature(abs_Trait_oper.__init__)
    params = list(sig.parameters.keys())



def test_abs_guard_is_not_abstract():
    assert not inspect.isabstract(abs_Guard)


def test_abs_guard_constructor_exists():
    assert callable(abs_Guard.__init__)


def test_abs_guard_constructor_args():
    sig = inspect.signature(abs_Guard.__init__)
    params = list(sig.parameters.keys())



def test_interface_modifier_fragment_is_not_abstract():
    assert not inspect.isabstract(Interface_modifier_fragment)


def test_interface_modifier_fragment_constructor_exists():
    assert callable(Interface_modifier_fragment.__init__)


def test_interface_modifier_fragment_constructor_args():
    sig = inspect.signature(Interface_modifier_fragment.__init__)
    params = list(sig.parameters.keys())



def test_class_modifier_fragment_is_not_abstract():
    assert not inspect.isabstract(Class_modifier_fragment)


def test_class_modifier_fragment_constructor_exists():
    assert callable(Class_modifier_fragment.__init__)


def test_class_modifier_fragment_constructor_args():
    sig = inspect.signature(Class_modifier_fragment.__init__)
    params = list(sig.parameters.keys())



def test_abs_trait_expr_is_not_abstract():
    assert not inspect.isabstract(abs_Trait_expr)


def test_abs_trait_expr_constructor_exists():
    assert callable(abs_Trait_expr.__init__)


def test_abs_trait_expr_constructor_args():
    sig = inspect.signature(abs_Trait_expr.__init__)
    params = list(sig.parameters.keys())



def test_abs_interface_name_is_not_abstract():
    assert not inspect.isabstract(abs_Interface_name)


def test_abs_interface_name_constructor_exists():
    assert callable(abs_Interface_name.__init__)


def test_abs_interface_name_constructor_args():
    sig = inspect.signature(abs_Interface_name.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_abs_interface_name_has_name():
    assert hasattr(abs_Interface_name, "name")
    descriptor = None
    for klass in abs_Interface_name.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_abs_methodsig_is_not_abstract():
    assert not inspect.isabstract(abs_Methodsig)


def test_abs_methodsig_constructor_exists():
    assert callable(abs_Methodsig.__init__)


def test_abs_methodsig_constructor_args():
    sig = inspect.signature(abs_Methodsig.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_abs_methodsig_has_name():
    assert hasattr(abs_Methodsig, "name")
    descriptor = None
    for klass in abs_Methodsig.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_abs_exp_is_not_abstract():
    assert not inspect.isabstract(abs_Exp)


def test_abs_exp_constructor_exists():
    assert callable(abs_Exp.__init__)


def test_abs_exp_constructor_args():
    sig = inspect.signature(abs_Exp.__init__)
    params = list(sig.parameters.keys())



def test_abs_method_is_not_abstract():
    assert not inspect.isabstract(abs_Method)


def test_abs_method_constructor_exists():
    assert callable(abs_Method.__init__)


def test_abs_method_constructor_args():
    sig = inspect.signature(abs_Method.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_abs_method_has_name():
    assert hasattr(abs_Method, "name")
    descriptor = None
    for klass in abs_Method.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_abs_trait_usage_is_not_abstract():
    assert not inspect.isabstract(abs_Trait_usage)


def test_abs_trait_usage_constructor_exists():
    assert callable(abs_Trait_usage.__init__)


def test_abs_trait_usage_constructor_args():
    sig = inspect.signature(abs_Trait_usage.__init__)
    params = list(sig.parameters.keys())



def test_abs_casestmtbranch_is_not_abstract():
    assert not inspect.isabstract(abs_Casestmtbranch)


def test_abs_casestmtbranch_constructor_exists():
    assert callable(abs_Casestmtbranch.__init__)


def test_abs_casestmtbranch_constructor_args():
    sig = inspect.signature(abs_Casestmtbranch.__init__)
    params = list(sig.parameters.keys())



def test_abs_stmt_is_not_abstract():
    assert not inspect.isabstract(abs_Stmt)


def test_abs_stmt_constructor_exists():
    assert callable(abs_Stmt.__init__)


def test_abs_stmt_constructor_args():
    sig = inspect.signature(abs_Stmt.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_abs_stmt_has_name():
    assert hasattr(abs_Stmt, "name")
    descriptor = None
    for klass in abs_Stmt.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_case_branch_is_not_abstract():
    assert not inspect.isabstract(Case_branch)


def test_case_branch_constructor_exists():
    assert callable(Case_branch.__init__)


def test_case_branch_constructor_args():
    sig = inspect.signature(Case_branch.__init__)
    params = list(sig.parameters.keys())



def test_abs_pattern_is_not_abstract():
    assert not inspect.isabstract(abs_Pattern)


def test_abs_pattern_constructor_exists():
    assert callable(abs_Pattern.__init__)


def test_abs_pattern_constructor_args():
    sig = inspect.signature(abs_Pattern.__init__)
    params = list(sig.parameters.keys())



def test_abs_field_decl_is_not_abstract():
    assert not inspect.isabstract(abs_Field_decl)


def test_abs_field_decl_constructor_exists():
    assert callable(abs_Field_decl.__init__)


def test_abs_field_decl_constructor_args():
    sig = inspect.signature(abs_Field_decl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_abs_field_decl_has_name():
    assert hasattr(abs_Field_decl, "name")
    descriptor = None
    for klass in abs_Field_decl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_pure_exp_is_not_abstract():
    assert not inspect.isabstract(Pure_exp)


def test_pure_exp_constructor_exists():
    assert callable(Pure_exp.__init__)


def test_pure_exp_constructor_args():
    sig = inspect.signature(Pure_exp.__init__)
    params = list(sig.parameters.keys())



def test_abs_or_expr_is_not_abstract():
    assert not inspect.isabstract(abs_Or_expr)


def test_abs_or_expr_constructor_exists():
    assert callable(abs_Or_expr.__init__)


def test_abs_or_expr_constructor_args():
    sig = inspect.signature(abs_Or_expr.__init__)
    params = list(sig.parameters.keys())



def test_abs_and_expr_is_not_abstract():
    assert not inspect.isabstract(abs_And_expr)


def test_abs_and_expr_constructor_exists():
    assert callable(abs_And_expr.__init__)


def test_abs_and_expr_constructor_args():
    sig = inspect.signature(abs_And_expr.__init__)
    params = list(sig.parameters.keys())



def test_abs_equality_expr_is_not_abstract():
    assert not inspect.isabstract(abs_Equality_expr)


def test_abs_equality_expr_constructor_exists():
    assert callable(abs_Equality_expr.__init__)


def test_abs_equality_expr_constructor_args():
    sig = inspect.signature(abs_Equality_expr.__init__)
    params = list(sig.parameters.keys())



def test_abs_muldivormod_expr_is_not_abstract():
    assert not inspect.isabstract(abs_MulDivOrMod_expr)


def test_abs_muldivormod_expr_constructor_exists():
    assert callable(abs_MulDivOrMod_expr.__init__)


def test_abs_muldivormod_expr_constructor_args():
    sig = inspect.signature(abs_MulDivOrMod_expr.__init__)
    params = list(sig.parameters.keys())



def test_abs_plusorminus_expr_is_not_abstract():
    assert not inspect.isabstract(abs_PlusOrMinus_expr)


def test_abs_plusorminus_expr_constructor_exists():
    assert callable(abs_PlusOrMinus_expr.__init__)


def test_abs_plusorminus_expr_constructor_args():
    sig = inspect.signature(abs_PlusOrMinus_expr.__init__)
    params = list(sig.parameters.keys())



def test_abs_comparison_expr_is_not_abstract():
    assert not inspect.isabstract(abs_Comparison_expr)


def test_abs_comparison_expr_constructor_exists():
    assert callable(abs_Comparison_expr.__init__)


def test_abs_comparison_expr_constructor_args():
    sig = inspect.signature(abs_Comparison_expr.__init__)
    params = list(sig.parameters.keys())



def test_abs_var_or_field_ref_is_not_abstract():
    assert not inspect.isabstract(abs_Var_or_field_ref)


def test_abs_var_or_field_ref_constructor_exists():
    assert callable(abs_Var_or_field_ref.__init__)


def test_abs_var_or_field_ref_constructor_args():
    sig = inspect.signature(abs_Var_or_field_ref.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_abs_var_or_field_ref_has_name():
    assert hasattr(abs_Var_or_field_ref, "name")
    descriptor = None
    for klass in abs_Var_or_field_ref.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_update_preamble_declaration_is_not_abstract():
    assert not inspect.isabstract(Update_preamble_declaration)


def test_update_preamble_declaration_constructor_exists():
    assert callable(Update_preamble_declaration.__init__)


def test_update_preamble_declaration_constructor_args():
    sig = inspect.signature(Update_preamble_declaration.__init__)
    params = list(sig.parameters.keys())



def test_abs_type_exp_is_not_abstract():
    assert not inspect.isabstract(abs_Type_exp)


def test_abs_type_exp_constructor_exists():
    assert callable(abs_Type_exp.__init__)


def test_abs_type_exp_constructor_args():
    sig = inspect.signature(abs_Type_exp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_abs_type_exp_has_name():
    assert hasattr(abs_Type_exp, "name")
    descriptor = None
    for klass in abs_Type_exp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_delta_param_is_not_abstract():
    assert not inspect.isabstract(Delta_param)


def test_delta_param_constructor_exists():
    assert callable(Delta_param.__init__)


def test_delta_param_constructor_args():
    sig = inspect.signature(Delta_param.__init__)
    params = list(sig.parameters.keys())



def test_abs_has_condition_is_not_abstract():
    assert not inspect.isabstract(abs_Has_condition)


def test_abs_has_condition_constructor_exists():
    assert callable(abs_Has_condition.__init__)


def test_abs_has_condition_constructor_args():
    sig = inspect.signature(abs_Has_condition.__init__)
    params = list(sig.parameters.keys())



def test_abs_param_decl_is_not_abstract():
    assert not inspect.isabstract(abs_Param_decl)


def test_abs_param_decl_constructor_exists():
    assert callable(abs_Param_decl.__init__)


def test_abs_param_decl_constructor_args():
    sig = inspect.signature(abs_Param_decl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_abs_param_decl_has_name():
    assert hasattr(abs_Param_decl, "name")
    descriptor = None
    for klass in abs_Param_decl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_function_param_is_not_abstract():
    assert not inspect.isabstract(Function_param)


def test_function_param_constructor_exists():
    assert callable(Function_param.__init__)


def test_function_param_constructor_args():
    sig = inspect.signature(Function_param.__init__)
    params = list(sig.parameters.keys())



def test_abs_anon_function_decl_is_not_abstract():
    assert not inspect.isabstract(abs_Anon_function_decl)


def test_abs_anon_function_decl_constructor_exists():
    assert callable(abs_Anon_function_decl.__init__)


def test_abs_anon_function_decl_constructor_args():
    sig = inspect.signature(abs_Anon_function_decl.__init__)
    params = list(sig.parameters.keys())



def test_abs_function_name_param_decl_is_not_abstract():
    assert not inspect.isabstract(abs_Function_name_param_decl)


def test_abs_function_name_param_decl_constructor_exists():
    assert callable(abs_Function_name_param_decl.__init__)


def test_abs_function_name_param_decl_constructor_args():
    sig = inspect.signature(abs_Function_name_param_decl.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_abs_function_name_param_decl_has_value():
    assert hasattr(abs_Function_name_param_decl, "value")
    descriptor = None
    for klass in abs_Function_name_param_decl.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_abs_pure_exp_list_is_not_abstract():
    assert not inspect.isabstract(abs_Pure_exp_list)


def test_abs_pure_exp_list_constructor_exists():
    assert callable(abs_Pure_exp_list.__init__)


def test_abs_pure_exp_list_constructor_args():
    sig = inspect.signature(abs_Pure_exp_list.__init__)
    params = list(sig.parameters.keys())



def test_abs_function_param_is_not_abstract():
    assert not inspect.isabstract(abs_Function_param)


def test_abs_function_param_constructor_exists():
    assert callable(abs_Function_param.__init__)


def test_abs_function_param_constructor_args():
    sig = inspect.signature(abs_Function_param.__init__)
    params = list(sig.parameters.keys())



def test_abs_function_list_is_not_abstract():
    assert not inspect.isabstract(abs_Function_list)


def test_abs_function_list_constructor_exists():
    assert callable(abs_Function_list.__init__)


def test_abs_function_list_constructor_args():
    sig = inspect.signature(abs_Function_list.__init__)
    params = list(sig.parameters.keys())



def test_eff_expr_is_not_abstract():
    assert not inspect.isabstract(Eff_expr)


def test_eff_expr_constructor_exists():
    assert callable(Eff_expr.__init__)


def test_eff_expr_constructor_args():
    sig = inspect.signature(Eff_expr.__init__)
    params = list(sig.parameters.keys())



def test_abs_delta_id_is_not_abstract():
    assert not inspect.isabstract(abs_Delta_id)


def test_abs_delta_id_constructor_exists():
    assert callable(abs_Delta_id.__init__)


def test_abs_delta_id_constructor_args():
    sig = inspect.signature(abs_Delta_id.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_abs_delta_id_has_name():
    assert hasattr(abs_Delta_id, "name")
    descriptor = None
    for klass in abs_Delta_id.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_exp_is_not_abstract():
    assert not inspect.isabstract(Exp)


def test_exp_constructor_exists():
    assert callable(Exp.__init__)


def test_exp_constructor_args():
    sig = inspect.signature(Exp.__init__)
    params = list(sig.parameters.keys())



def test_abs_eff_expr_is_not_abstract():
    assert not inspect.isabstract(abs_Eff_expr)


def test_abs_eff_expr_constructor_exists():
    assert callable(abs_Eff_expr.__init__)


def test_abs_eff_expr_constructor_args():
    sig = inspect.signature(abs_Eff_expr.__init__)
    params = list(sig.parameters.keys())
    assert "l" in params, "Missing parameter 'l'"

def test_abs_eff_expr_has_l():
    assert hasattr(abs_Eff_expr, "l")
    descriptor = None
    for klass in abs_Eff_expr.__mro__:
        if "l" in klass.__dict__:
            descriptor = klass.__dict__["l"]
            break
    assert isinstance(descriptor, property)



def test_annotation_is_not_abstract():
    assert not inspect.isabstract(Annotation)


def test_annotation_constructor_exists():
    assert callable(Annotation.__init__)


def test_annotation_constructor_args():
    sig = inspect.signature(Annotation.__init__)
    params = list(sig.parameters.keys())



def test_data_constructor_arg_is_not_abstract():
    assert not inspect.isabstract(Data_constructor_arg)


def test_data_constructor_arg_constructor_exists():
    assert callable(Data_constructor_arg.__init__)


def test_data_constructor_arg_constructor_args():
    sig = inspect.signature(Data_constructor_arg.__init__)
    params = list(sig.parameters.keys())



def test_abs_case_branch_is_not_abstract():
    assert not inspect.isabstract(abs_Case_branch)


def test_abs_case_branch_constructor_exists():
    assert callable(abs_Case_branch.__init__)


def test_abs_case_branch_constructor_args():
    sig = inspect.signature(abs_Case_branch.__init__)
    params = list(sig.parameters.keys())



def test_abs_main_block_is_not_abstract():
    assert not inspect.isabstract(abs_Main_block)


def test_abs_main_block_constructor_exists():
    assert callable(abs_Main_block.__init__)


def test_abs_main_block_constructor_args():
    sig = inspect.signature(abs_Main_block.__init__)
    params = list(sig.parameters.keys())



def test_abs_decl_is_not_abstract():
    assert not inspect.isabstract(abs_Decl)


def test_abs_decl_constructor_exists():
    assert callable(abs_Decl.__init__)


def test_abs_decl_constructor_args():
    sig = inspect.signature(abs_Decl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_abs_decl_has_name():
    assert hasattr(abs_Decl, "name")
    descriptor = None
    for klass in abs_Decl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_abs_fextension_is_not_abstract():
    assert not inspect.isabstract(abs_Fextension)


def test_abs_fextension_constructor_exists():
    assert callable(abs_Fextension.__init__)


def test_abs_fextension_constructor_args():
    sig = inspect.signature(abs_Fextension.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_abs_fextension_has_name():
    assert hasattr(abs_Fextension, "name")
    descriptor = None
    for klass in abs_Fextension.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_abs_feature_decl_is_not_abstract():
    assert not inspect.isabstract(abs_Feature_decl)


def test_abs_feature_decl_constructor_exists():
    assert callable(abs_Feature_decl.__init__)


def test_abs_feature_decl_constructor_args():
    sig = inspect.signature(abs_Feature_decl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_abs_feature_decl_has_name():
    assert hasattr(abs_Feature_decl, "name")
    descriptor = None
    for klass in abs_Feature_decl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_abs_annotation_is_not_abstract():
    assert not inspect.isabstract(abs_Annotation)


def test_abs_annotation_constructor_exists():
    assert callable(abs_Annotation.__init__)


def test_abs_annotation_constructor_args():
    sig = inspect.signature(abs_Annotation.__init__)
    params = list(sig.parameters.keys())



def test_abs_annotations_is_not_abstract():
    assert not inspect.isabstract(abs_Annotations)


def test_abs_annotations_constructor_exists():
    assert callable(abs_Annotations.__init__)


def test_abs_annotations_constructor_args():
    sig = inspect.signature(abs_Annotations.__init__)
    params = list(sig.parameters.keys())



def test_abs_data_constructor_arg_is_not_abstract():
    assert not inspect.isabstract(abs_Data_constructor_arg)


def test_abs_data_constructor_arg_constructor_exists():
    assert callable(abs_Data_constructor_arg.__init__)


def test_abs_data_constructor_arg_constructor_args():
    sig = inspect.signature(abs_Data_constructor_arg.__init__)
    params = list(sig.parameters.keys())



def test_abs_data_constructor_is_not_abstract():
    assert not inspect.isabstract(abs_Data_constructor)


def test_abs_data_constructor_constructor_exists():
    assert callable(abs_Data_constructor.__init__)


def test_abs_data_constructor_constructor_args():
    sig = inspect.signature(abs_Data_constructor.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_abs_data_constructor_has_name():
    assert hasattr(abs_Data_constructor, "name")
    descriptor = None
    for klass in abs_Data_constructor.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_functional_modifier_is_not_abstract():
    assert not inspect.isabstract(Functional_modifier)


def test_functional_modifier_constructor_exists():
    assert callable(Functional_modifier.__init__)


def test_functional_modifier_constructor_args():
    sig = inspect.signature(Functional_modifier.__init__)
    params = list(sig.parameters.keys())



def test_abs_function_name_decl_is_not_abstract():
    assert not inspect.isabstract(abs_Function_name_decl)


def test_abs_function_name_decl_constructor_exists():
    assert callable(abs_Function_name_decl.__init__)


def test_abs_function_name_decl_constructor_args():
    sig = inspect.signature(abs_Function_name_decl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_abs_function_name_decl_has_name():
    assert hasattr(abs_Function_name_decl, "name")
    descriptor = None
    for klass in abs_Function_name_decl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_abs_pure_exp_is_not_abstract():
    assert not inspect.isabstract(abs_Pure_exp)


def test_abs_pure_exp_constructor_exists():
    assert callable(abs_Pure_exp.__init__)


def test_abs_pure_exp_constructor_args():
    sig = inspect.signature(abs_Pure_exp.__init__)
    params = list(sig.parameters.keys())
    assert "await_" in params, "Missing parameter 'await_'"
    assert "value" in params, "Missing parameter 'value'"
    assert "val" in params, "Missing parameter 'val'"
    assert "op" in params, "Missing parameter 'op'"

def test_abs_pure_exp_has_await_():
    assert hasattr(abs_Pure_exp, "await_")
    descriptor = None
    for klass in abs_Pure_exp.__mro__:
        if "await_" in klass.__dict__:
            descriptor = klass.__dict__["await_"]
            break
    assert isinstance(descriptor, property)

def test_abs_pure_exp_has_value():
    assert hasattr(abs_Pure_exp, "value")
    descriptor = None
    for klass in abs_Pure_exp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_abs_pure_exp_has_val():
    assert hasattr(abs_Pure_exp, "val")
    descriptor = None
    for klass in abs_Pure_exp.__mro__:
        if "val" in klass.__dict__:
            descriptor = klass.__dict__["val"]
            break
    assert isinstance(descriptor, property)

def test_abs_pure_exp_has_op():
    assert hasattr(abs_Pure_exp, "op")
    descriptor = None
    for klass in abs_Pure_exp.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_abs_param_list_is_not_abstract():
    assert not inspect.isabstract(abs_Param_list)


def test_abs_param_list_constructor_exists():
    assert callable(abs_Param_list.__init__)


def test_abs_param_list_constructor_args():
    sig = inspect.signature(abs_Param_list.__init__)
    params = list(sig.parameters.keys())



def test_abs_function_name_list_is_not_abstract():
    assert not inspect.isabstract(abs_Function_name_list)


def test_abs_function_name_list_constructor_exists():
    assert callable(abs_Function_name_list.__init__)


def test_abs_function_name_list_constructor_args():
    sig = inspect.signature(abs_Function_name_list.__init__)
    params = list(sig.parameters.keys())



def test_abs_type_use_is_not_abstract():
    assert not inspect.isabstract(abs_Type_use)


def test_abs_type_use_constructor_exists():
    assert callable(abs_Type_use.__init__)


def test_abs_type_use_constructor_args():
    sig = inspect.signature(abs_Type_use.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_abs_type_use_has_name():
    assert hasattr(abs_Type_use, "name")
    descriptor = None
    for klass in abs_Type_use.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_decl_is_not_abstract():
    assert not inspect.isabstract(Decl)


def test_decl_constructor_exists():
    assert callable(Decl.__init__)


def test_decl_constructor_args():
    sig = inspect.signature(Decl.__init__)
    params = list(sig.parameters.keys())



def test_abs_function_decl_is_not_abstract():
    assert not inspect.isabstract(abs_Function_decl)


def test_abs_function_decl_constructor_exists():
    assert callable(abs_Function_decl.__init__)


def test_abs_function_decl_constructor_args():
    sig = inspect.signature(abs_Function_decl.__init__)
    params = list(sig.parameters.keys())
    assert "p" in params, "Missing parameter 'p'"

def test_abs_function_decl_has_p():
    assert hasattr(abs_Function_decl, "p")
    descriptor = None
    for klass in abs_Function_decl.__mro__:
        if "p" in klass.__dict__:
            descriptor = klass.__dict__["p"]
            break
    assert isinstance(descriptor, property)



def test_abs_interface_decl_is_not_abstract():
    assert not inspect.isabstract(abs_Interface_decl)


def test_abs_interface_decl_constructor_exists():
    assert callable(abs_Interface_decl.__init__)


def test_abs_interface_decl_constructor_args():
    sig = inspect.signature(abs_Interface_decl.__init__)
    params = list(sig.parameters.keys())



def test_abs_exception_decl_is_not_abstract():
    assert not inspect.isabstract(abs_Exception_decl)


def test_abs_exception_decl_constructor_exists():
    assert callable(abs_Exception_decl.__init__)


def test_abs_exception_decl_constructor_args():
    sig = inspect.signature(abs_Exception_decl.__init__)
    params = list(sig.parameters.keys())



def test_abs_datatype_decl_is_not_abstract():
    assert not inspect.isabstract(abs_DataType_decl)


def test_abs_datatype_decl_constructor_exists():
    assert callable(abs_DataType_decl.__init__)


def test_abs_datatype_decl_constructor_args():
    sig = inspect.signature(abs_DataType_decl.__init__)
    params = list(sig.parameters.keys())
    assert "p" in params, "Missing parameter 'p'"

def test_abs_datatype_decl_has_p():
    assert hasattr(abs_DataType_decl, "p")
    descriptor = None
    for klass in abs_DataType_decl.__mro__:
        if "p" in klass.__dict__:
            descriptor = klass.__dict__["p"]
            break
    assert isinstance(descriptor, property)



def test_abs_trait_decl_is_not_abstract():
    assert not inspect.isabstract(abs_Trait_decl)


def test_abs_trait_decl_constructor_exists():
    assert callable(abs_Trait_decl.__init__)


def test_abs_trait_decl_constructor_args():
    sig = inspect.signature(abs_Trait_decl.__init__)
    params = list(sig.parameters.keys())



def test_abs_typesyn_decl_is_not_abstract():
    assert not inspect.isabstract(abs_Typesyn_decl)


def test_abs_typesyn_decl_constructor_exists():
    assert callable(abs_Typesyn_decl.__init__)


def test_abs_typesyn_decl_constructor_args():
    sig = inspect.signature(abs_Typesyn_decl.__init__)
    params = list(sig.parameters.keys())



def test_abs_class_decl_is_not_abstract():
    assert not inspect.isabstract(abs_Class_decl)


def test_abs_class_decl_constructor_exists():
    assert callable(abs_Class_decl.__init__)


def test_abs_class_decl_constructor_args():
    sig = inspect.signature(abs_Class_decl.__init__)
    params = list(sig.parameters.keys())



def test_abs_par_function_decl_is_not_abstract():
    assert not inspect.isabstract(abs_Par_function_decl)


def test_abs_par_function_decl_constructor_exists():
    assert callable(abs_Par_function_decl.__init__)


def test_abs_par_function_decl_constructor_args():
    sig = inspect.signature(abs_Par_function_decl.__init__)
    params = list(sig.parameters.keys())
    assert "p" in params, "Missing parameter 'p'"

def test_abs_par_function_decl_has_p():
    assert hasattr(abs_Par_function_decl, "p")
    descriptor = None
    for klass in abs_Par_function_decl.__mro__:
        if "p" in klass.__dict__:
            descriptor = klass.__dict__["p"]
            break
    assert isinstance(descriptor, property)



def test_namespace_modifier_is_not_abstract():
    assert not inspect.isabstract(Namespace_modifier)


def test_namespace_modifier_constructor_exists():
    assert callable(Namespace_modifier.__init__)


def test_namespace_modifier_constructor_args():
    sig = inspect.signature(Namespace_modifier.__init__)
    params = list(sig.parameters.keys())



def test_abs_module_import_is_not_abstract():
    assert not inspect.isabstract(abs_Module_import)


def test_abs_module_import_constructor_exists():
    assert callable(abs_Module_import.__init__)


def test_abs_module_import_constructor_args():
    sig = inspect.signature(abs_Module_import.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"
    assert "name" in params, "Missing parameter 'name'"

def test_abs_module_import_has_importedNamespace():
    assert hasattr(abs_Module_import, "importedNamespace")
    descriptor = None
    for klass in abs_Module_import.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)

def test_abs_module_import_has_name():
    assert hasattr(abs_Module_import, "name")
    descriptor = None
    for klass in abs_Module_import.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_abs_module_export_is_not_abstract():
    assert not inspect.isabstract(abs_Module_export)


def test_abs_module_export_constructor_exists():
    assert callable(abs_Module_export.__init__)


def test_abs_module_export_constructor_args():
    sig = inspect.signature(abs_Module_export.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"
    assert "anyPackage" in params, "Missing parameter 'anyPackage'"

def test_abs_module_export_has_importedNamespace():
    assert hasattr(abs_Module_export, "importedNamespace")
    descriptor = None
    for klass in abs_Module_export.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)

def test_abs_module_export_has_anyPackage():
    assert hasattr(abs_Module_export, "anyPackage")
    descriptor = None
    for klass in abs_Module_export.__mro__:
        if "anyPackage" in klass.__dict__:
            descriptor = klass.__dict__["anyPackage"]
            break
    assert isinstance(descriptor, property)



def test_abs_product_decl_is_not_abstract():
    assert not inspect.isabstract(abs_Product_decl)


def test_abs_product_decl_constructor_exists():
    assert callable(abs_Product_decl.__init__)


def test_abs_product_decl_constructor_args():
    sig = inspect.signature(abs_Product_decl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_abs_product_decl_has_name():
    assert hasattr(abs_Product_decl, "name")
    descriptor = None
    for klass in abs_Product_decl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_abs_productline_decl_is_not_abstract():
    assert not inspect.isabstract(abs_Productline_decl)


def test_abs_productline_decl_constructor_exists():
    assert callable(abs_Productline_decl.__init__)


def test_abs_productline_decl_constructor_args():
    sig = inspect.signature(abs_Productline_decl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_abs_productline_decl_has_name():
    assert hasattr(abs_Productline_decl, "name")
    descriptor = None
    for klass in abs_Productline_decl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_abs_update_decl_is_not_abstract():
    assert not inspect.isabstract(abs_Update_decl)


def test_abs_update_decl_constructor_exists():
    assert callable(abs_Update_decl.__init__)


def test_abs_update_decl_constructor_args():
    sig = inspect.signature(abs_Update_decl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_abs_update_decl_has_name():
    assert hasattr(abs_Update_decl, "name")
    descriptor = None
    for klass in abs_Update_decl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_abs_delta_decl_is_not_abstract():
    assert not inspect.isabstract(abs_Delta_decl)


def test_abs_delta_decl_constructor_exists():
    assert callable(abs_Delta_decl.__init__)


def test_abs_delta_decl_constructor_args():
    sig = inspect.signature(abs_Delta_decl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_abs_delta_decl_has_name():
    assert hasattr(abs_Delta_decl, "name")
    descriptor = None
    for klass in abs_Delta_decl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_abs_module_decl_is_not_abstract():
    assert not inspect.isabstract(abs_Module_decl)


def test_abs_module_decl_constructor_exists():
    assert callable(abs_Module_decl.__init__)


def test_abs_module_decl_constructor_args():
    sig = inspect.signature(abs_Module_decl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_abs_module_decl_has_name():
    assert hasattr(abs_Module_decl, "name")
    descriptor = None
    for klass in abs_Module_decl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domainmodel__is_not_abstract():
    assert not inspect.isabstract(DomainModel_)


def test_domainmodel__constructor_exists():
    assert callable(DomainModel_.__init__)


def test_domainmodel__constructor_args():
    sig = inspect.signature(DomainModel_.__init__)
    params = list(sig.parameters.keys())



def test_abs_compilation_unit_is_not_abstract():
    assert not inspect.isabstract(abs_Compilation_Unit)


def test_abs_compilation_unit_constructor_exists():
    assert callable(abs_Compilation_Unit.__init__)


def test_abs_compilation_unit_constructor_args():
    sig = inspect.signature(abs_Compilation_Unit.__init__)
    params = list(sig.parameters.keys())



def test_abs_domainmodel__is_not_abstract():
    assert not inspect.isabstract(abs_DomainModel_)


def test_abs_domainmodel__constructor_exists():
    assert callable(abs_DomainModel_.__init__)


def test_abs_domainmodel__constructor_args():
    sig = inspect.signature(abs_DomainModel_.__init__)
    params = list(sig.parameters.keys())


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
Mexp_strategy = st.builds(
    Mexp,
)
abs_MexpAnd_expr_strategy = st.builds(
    abs_MexpAnd_expr,
)
abs_MexpMulDivOrMod_expr_strategy = st.builds(
    abs_MexpMulDivOrMod_expr,
    op=
        safe_text
)
abs_MexpImplies_expr_strategy = st.builds(
    abs_MexpImplies_expr,
    op=
        safe_text
)
abs_MexpPrimary_expr_strategy = st.builds(
    abs_MexpPrimary_expr,
)
abs_MexpPlusOrMinus_expr_strategy = st.builds(
    abs_MexpPlusOrMinus_expr,
    op=
        safe_text
)
abs_MexpOr_exp_strategy = st.builds(
    abs_MexpOr_exp,
)
Product_expr_strategy = st.builds(
    Product_expr,
)
abs_ProductMinus_exp_strategy = st.builds(
    abs_ProductMinus_exp,
)
abs_ProductAnd_exp_strategy = st.builds(
    abs_ProductAnd_exp,
)
abs_ProductOr_expr_strategy = st.builds(
    abs_ProductOr_expr,
)
Application_condition_strategy = st.builds(
    Application_condition,
)
abs_AppAnd_exp_strategy = st.builds(
    abs_AppAnd_exp,
)
abs_AppOr_exp_strategy = st.builds(
    abs_AppOr_exp,
)
abs_MexpComparison_expr_strategy = st.builds(
    abs_MexpComparison_expr,
    op=
        safe_text
)
abs_MexpEquality_expr_strategy = st.builds(
    abs_MexpEquality_expr,
    op=
        safe_text
)
Guard_strategy = st.builds(
    Guard,
)
abs_AndGuard_strategy = st.builds(
    abs_AndGuard,
    op=
        safe_text
)
abs_Mexp_strategy = st.builds(
    abs_Mexp,
    value=
        st.integers()
)
abs_Fnode_strategy = st.builds(
    abs_Fnode,
)
abs_Feature_decl_constraint_strategy = st.builds(
    abs_Feature_decl_constraint,
)
abs_Feature_decl_attribute_strategy = st.builds(
    abs_Feature_decl_attribute,
    boundary_val=
        safe_text,
    uBoundary_int=
        safe_text,
    lBoundary_int=
        safe_text
)
abs_Feature_decl_group_strategy = st.builds(
    abs_Feature_decl_group,
)
Fnode_strategy = st.builds(
    Fnode,
)
abs_Product_expr_strategy = st.builds(
    abs_Product_expr,
)
abs_Product_reconfiguration_strategy = st.builds(
    abs_Product_reconfiguration,
    name=
        safe_text,
    update=
        safe_text
)
abs_Application_condition_strategy = st.builds(
    abs_Application_condition,
)
abs_Deltaspec_strategy = st.builds(
    abs_Deltaspec,
    name=
        safe_text,
    deltaspec_param=
        safe_text
)
abs_When_condition_strategy = st.builds(
    abs_When_condition,
)
abs_From_condition_strategy = st.builds(
    abs_From_condition,
)
abs_After_condition_strategy = st.builds(
    abs_After_condition,
)
abs_Class_modifier_fragment_strategy = st.builds(
    abs_Class_modifier_fragment,
)
abs_Delta_clause_strategy = st.builds(
    abs_Delta_clause,
)
abs_Feature_strategy = st.builds(
    abs_Feature,
    p=
        safe_text,
    attr_assignment=
        safe_text
)
abs_Object_update_assign_stmt_strategy = st.builds(
    abs_Object_update_assign_stmt,
)
abs_Update_preamble_declaration_strategy = st.builds(
    abs_Update_preamble_declaration,
)
abs_Object_update_strategy = st.builds(
    abs_Object_update,
)
abs_Interface_modifier_fragment_strategy = st.builds(
    abs_Interface_modifier_fragment,
)
Module_modifier_strategy = st.builds(
    Module_modifier,
)
abs_OO_modifier_strategy = st.builds(
    abs_OO_modifier,
)
abs_Namespace_modifier_strategy = st.builds(
    abs_Namespace_modifier,
    star=
        safe_text
)
abs_Functional_modifier_strategy = st.builds(
    abs_Functional_modifier,
)
abs_Module_modifier_strategy = st.builds(
    abs_Module_modifier,
)
abs_Delta_access_strategy = st.builds(
    abs_Delta_access,
)
abs_Delta_param_strategy = st.builds(
    abs_Delta_param,
)
abs_Trait_oper_strategy = st.builds(
    abs_Trait_oper,
)
abs_Guard_strategy = st.builds(
    abs_Guard,
)
Interface_modifier_fragment_strategy = st.builds(
    Interface_modifier_fragment,
)
Class_modifier_fragment_strategy = st.builds(
    Class_modifier_fragment,
)
abs_Trait_expr_strategy = st.builds(
    abs_Trait_expr,
)
abs_Interface_name_strategy = st.builds(
    abs_Interface_name,
    name=
        safe_text
)
abs_Methodsig_strategy = st.builds(
    abs_Methodsig,
    name=
        safe_text
)
abs_Exp_strategy = st.builds(
    abs_Exp,
)
abs_Method_strategy = st.builds(
    abs_Method,
    name=
        safe_text
)
abs_Trait_usage_strategy = st.builds(
    abs_Trait_usage,
)
abs_Casestmtbranch_strategy = st.builds(
    abs_Casestmtbranch,
)
abs_Stmt_strategy = st.builds(
    abs_Stmt,
    name=
        safe_text
)
Case_branch_strategy = st.builds(
    Case_branch,
)
abs_Pattern_strategy = st.builds(
    abs_Pattern,
)
abs_Field_decl_strategy = st.builds(
    abs_Field_decl,
    name=
        safe_text
)
Pure_exp_strategy = st.builds(
    Pure_exp,
)
abs_Or_expr_strategy = st.builds(
    abs_Or_expr,
)
abs_And_expr_strategy = st.builds(
    abs_And_expr,
)
abs_Equality_expr_strategy = st.builds(
    abs_Equality_expr,
)
abs_MulDivOrMod_expr_strategy = st.builds(
    abs_MulDivOrMod_expr,
)
abs_PlusOrMinus_expr_strategy = st.builds(
    abs_PlusOrMinus_expr,
)
abs_Comparison_expr_strategy = st.builds(
    abs_Comparison_expr,
)
abs_Var_or_field_ref_strategy = st.builds(
    abs_Var_or_field_ref,
    name=
        safe_text
)
Update_preamble_declaration_strategy = st.builds(
    Update_preamble_declaration,
)
abs_Type_exp_strategy = st.builds(
    abs_Type_exp,
    name=
        safe_text
)
Delta_param_strategy = st.builds(
    Delta_param,
)
abs_Has_condition_strategy = st.builds(
    abs_Has_condition,
)
abs_Param_decl_strategy = st.builds(
    abs_Param_decl,
    name=
        safe_text
)
Function_param_strategy = st.builds(
    Function_param,
)
abs_Anon_function_decl_strategy = st.builds(
    abs_Anon_function_decl,
)
abs_Function_name_param_decl_strategy = st.builds(
    abs_Function_name_param_decl,
    value=
        safe_text
)
abs_Pure_exp_list_strategy = st.builds(
    abs_Pure_exp_list,
)
abs_Function_param_strategy = st.builds(
    abs_Function_param,
)
abs_Function_list_strategy = st.builds(
    abs_Function_list,
)
Eff_expr_strategy = st.builds(
    Eff_expr,
)
abs_Delta_id_strategy = st.builds(
    abs_Delta_id,
    name=
        safe_text
)
Exp_strategy = st.builds(
    Exp,
)
abs_Eff_expr_strategy = st.builds(
    abs_Eff_expr,
    l=
        safe_text
)
Annotation_strategy = st.builds(
    Annotation,
)
Data_constructor_arg_strategy = st.builds(
    Data_constructor_arg,
)
abs_Case_branch_strategy = st.builds(
    abs_Case_branch,
)
abs_Main_block_strategy = st.builds(
    abs_Main_block,
)
abs_Decl_strategy = st.builds(
    abs_Decl,
    name=
        safe_text
)
abs_Fextension_strategy = st.builds(
    abs_Fextension,
    name=
        safe_text
)
abs_Feature_decl_strategy = st.builds(
    abs_Feature_decl,
    name=
        safe_text
)
abs_Annotation_strategy = st.builds(
    abs_Annotation,
)
abs_Annotations_strategy = st.builds(
    abs_Annotations,
)
abs_Data_constructor_arg_strategy = st.builds(
    abs_Data_constructor_arg,
)
abs_Data_constructor_strategy = st.builds(
    abs_Data_constructor,
    name=
        safe_text
)
Functional_modifier_strategy = st.builds(
    Functional_modifier,
)
abs_Function_name_decl_strategy = st.builds(
    abs_Function_name_decl,
    name=
        safe_text
)
abs_Pure_exp_strategy = st.builds(
    abs_Pure_exp,
    await_=
        safe_text,
    value=
        safe_text,
    val=
        safe_text,
    op=
        safe_text
)
abs_Param_list_strategy = st.builds(
    abs_Param_list,
)
abs_Function_name_list_strategy = st.builds(
    abs_Function_name_list,
)
abs_Type_use_strategy = st.builds(
    abs_Type_use,
    name=
        safe_text
)
Decl_strategy = st.builds(
    Decl,
)
abs_Function_decl_strategy = st.builds(
    abs_Function_decl,
    p=
        safe_text
)
abs_Interface_decl_strategy = st.builds(
    abs_Interface_decl,
)
abs_Exception_decl_strategy = st.builds(
    abs_Exception_decl,
)
abs_DataType_decl_strategy = st.builds(
    abs_DataType_decl,
    p=
        safe_text
)
abs_Trait_decl_strategy = st.builds(
    abs_Trait_decl,
)
abs_Typesyn_decl_strategy = st.builds(
    abs_Typesyn_decl,
)
abs_Class_decl_strategy = st.builds(
    abs_Class_decl,
)
abs_Par_function_decl_strategy = st.builds(
    abs_Par_function_decl,
    p=
        safe_text
)
Namespace_modifier_strategy = st.builds(
    Namespace_modifier,
)
abs_Module_import_strategy = st.builds(
    abs_Module_import,
    importedNamespace=
        safe_text,
    name=
        safe_text
)
abs_Module_export_strategy = st.builds(
    abs_Module_export,
    importedNamespace=
        safe_text,
    anyPackage=
        safe_text
)
abs_Product_decl_strategy = st.builds(
    abs_Product_decl,
    name=
        safe_text
)
abs_Productline_decl_strategy = st.builds(
    abs_Productline_decl,
    name=
        safe_text
)
abs_Update_decl_strategy = st.builds(
    abs_Update_decl,
    name=
        safe_text
)
abs_Delta_decl_strategy = st.builds(
    abs_Delta_decl,
    name=
        safe_text
)
abs_Module_decl_strategy = st.builds(
    abs_Module_decl,
    name=
        safe_text
)
DomainModel__strategy = st.builds(
    DomainModel_,
)
abs_Compilation_Unit_strategy = st.builds(
    abs_Compilation_Unit,
)
abs_DomainModel__strategy = st.builds(
    abs_DomainModel_,
)

@given(instance=Mexp_strategy)
@settings(max_examples=50)
def test_mexp_instantiation(instance):
    assert isinstance(instance, Mexp)

@given(instance=abs_MexpAnd_expr_strategy)
@settings(max_examples=50)
def test_abs_mexpand_expr_instantiation(instance):
    assert isinstance(instance, abs_MexpAnd_expr)

@given(instance=abs_MexpMulDivOrMod_expr_strategy)
@settings(max_examples=50)
def test_abs_mexpmuldivormod_expr_instantiation(instance):
    assert isinstance(instance, abs_MexpMulDivOrMod_expr)



@given(instance=abs_MexpMulDivOrMod_expr_strategy)
def test_abs_mexpmuldivormod_expr_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=abs_MexpImplies_expr_strategy)
@settings(max_examples=50)
def test_abs_mexpimplies_expr_instantiation(instance):
    assert isinstance(instance, abs_MexpImplies_expr)



@given(instance=abs_MexpImplies_expr_strategy)
def test_abs_mexpimplies_expr_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=abs_MexpPrimary_expr_strategy)
@settings(max_examples=50)
def test_abs_mexpprimary_expr_instantiation(instance):
    assert isinstance(instance, abs_MexpPrimary_expr)

@given(instance=abs_MexpPlusOrMinus_expr_strategy)
@settings(max_examples=50)
def test_abs_mexpplusorminus_expr_instantiation(instance):
    assert isinstance(instance, abs_MexpPlusOrMinus_expr)



@given(instance=abs_MexpPlusOrMinus_expr_strategy)
def test_abs_mexpplusorminus_expr_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=abs_MexpOr_exp_strategy)
@settings(max_examples=50)
def test_abs_mexpor_exp_instantiation(instance):
    assert isinstance(instance, abs_MexpOr_exp)

@given(instance=Product_expr_strategy)
@settings(max_examples=50)
def test_product_expr_instantiation(instance):
    assert isinstance(instance, Product_expr)

@given(instance=abs_ProductMinus_exp_strategy)
@settings(max_examples=50)
def test_abs_productminus_exp_instantiation(instance):
    assert isinstance(instance, abs_ProductMinus_exp)

@given(instance=abs_ProductAnd_exp_strategy)
@settings(max_examples=50)
def test_abs_productand_exp_instantiation(instance):
    assert isinstance(instance, abs_ProductAnd_exp)

@given(instance=abs_ProductOr_expr_strategy)
@settings(max_examples=50)
def test_abs_productor_expr_instantiation(instance):
    assert isinstance(instance, abs_ProductOr_expr)

@given(instance=Application_condition_strategy)
@settings(max_examples=50)
def test_application_condition_instantiation(instance):
    assert isinstance(instance, Application_condition)

@given(instance=abs_AppAnd_exp_strategy)
@settings(max_examples=50)
def test_abs_appand_exp_instantiation(instance):
    assert isinstance(instance, abs_AppAnd_exp)

@given(instance=abs_AppOr_exp_strategy)
@settings(max_examples=50)
def test_abs_appor_exp_instantiation(instance):
    assert isinstance(instance, abs_AppOr_exp)

@given(instance=abs_MexpComparison_expr_strategy)
@settings(max_examples=50)
def test_abs_mexpcomparison_expr_instantiation(instance):
    assert isinstance(instance, abs_MexpComparison_expr)



@given(instance=abs_MexpComparison_expr_strategy)
def test_abs_mexpcomparison_expr_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=abs_MexpEquality_expr_strategy)
@settings(max_examples=50)
def test_abs_mexpequality_expr_instantiation(instance):
    assert isinstance(instance, abs_MexpEquality_expr)



@given(instance=abs_MexpEquality_expr_strategy)
def test_abs_mexpequality_expr_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=Guard_strategy)
@settings(max_examples=50)
def test_guard_instantiation(instance):
    assert isinstance(instance, Guard)

@given(instance=abs_AndGuard_strategy)
@settings(max_examples=50)
def test_abs_andguard_instantiation(instance):
    assert isinstance(instance, abs_AndGuard)



@given(instance=abs_AndGuard_strategy)
def test_abs_andguard_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=abs_Mexp_strategy)
@settings(max_examples=50)
def test_abs_mexp_instantiation(instance):
    assert isinstance(instance, abs_Mexp)



@given(instance=abs_Mexp_strategy)
def test_abs_mexp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=abs_Fnode_strategy)
@settings(max_examples=50)
def test_abs_fnode_instantiation(instance):
    assert isinstance(instance, abs_Fnode)

@given(instance=abs_Feature_decl_constraint_strategy)
@settings(max_examples=50)
def test_abs_feature_decl_constraint_instantiation(instance):
    assert isinstance(instance, abs_Feature_decl_constraint)

@given(instance=abs_Feature_decl_attribute_strategy)
@settings(max_examples=50)
def test_abs_feature_decl_attribute_instantiation(instance):
    assert isinstance(instance, abs_Feature_decl_attribute)



@given(instance=abs_Feature_decl_attribute_strategy)
def test_abs_feature_decl_attribute_boundary_val_setter(instance):
    original = instance.boundary_val
    instance.boundary_val = original
    assert instance.boundary_val == original



@given(instance=abs_Feature_decl_attribute_strategy)
def test_abs_feature_decl_attribute_uBoundary_int_setter(instance):
    original = instance.uBoundary_int
    instance.uBoundary_int = original
    assert instance.uBoundary_int == original



@given(instance=abs_Feature_decl_attribute_strategy)
def test_abs_feature_decl_attribute_lBoundary_int_setter(instance):
    original = instance.lBoundary_int
    instance.lBoundary_int = original
    assert instance.lBoundary_int == original

@given(instance=abs_Feature_decl_group_strategy)
@settings(max_examples=50)
def test_abs_feature_decl_group_instantiation(instance):
    assert isinstance(instance, abs_Feature_decl_group)

@given(instance=Fnode_strategy)
@settings(max_examples=50)
def test_fnode_instantiation(instance):
    assert isinstance(instance, Fnode)

@given(instance=abs_Product_expr_strategy)
@settings(max_examples=50)
def test_abs_product_expr_instantiation(instance):
    assert isinstance(instance, abs_Product_expr)

@given(instance=abs_Product_reconfiguration_strategy)
@settings(max_examples=50)
def test_abs_product_reconfiguration_instantiation(instance):
    assert isinstance(instance, abs_Product_reconfiguration)



@given(instance=abs_Product_reconfiguration_strategy)
def test_abs_product_reconfiguration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=abs_Product_reconfiguration_strategy)
def test_abs_product_reconfiguration_update_setter(instance):
    original = instance.update
    instance.update = original
    assert instance.update == original

@given(instance=abs_Application_condition_strategy)
@settings(max_examples=50)
def test_abs_application_condition_instantiation(instance):
    assert isinstance(instance, abs_Application_condition)

@given(instance=abs_Deltaspec_strategy)
@settings(max_examples=50)
def test_abs_deltaspec_instantiation(instance):
    assert isinstance(instance, abs_Deltaspec)



@given(instance=abs_Deltaspec_strategy)
def test_abs_deltaspec_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=abs_Deltaspec_strategy)
def test_abs_deltaspec_deltaspec_param_setter(instance):
    original = instance.deltaspec_param
    instance.deltaspec_param = original
    assert instance.deltaspec_param == original

@given(instance=abs_When_condition_strategy)
@settings(max_examples=50)
def test_abs_when_condition_instantiation(instance):
    assert isinstance(instance, abs_When_condition)

@given(instance=abs_From_condition_strategy)
@settings(max_examples=50)
def test_abs_from_condition_instantiation(instance):
    assert isinstance(instance, abs_From_condition)

@given(instance=abs_After_condition_strategy)
@settings(max_examples=50)
def test_abs_after_condition_instantiation(instance):
    assert isinstance(instance, abs_After_condition)

@given(instance=abs_Class_modifier_fragment_strategy)
@settings(max_examples=50)
def test_abs_class_modifier_fragment_instantiation(instance):
    assert isinstance(instance, abs_Class_modifier_fragment)

@given(instance=abs_Delta_clause_strategy)
@settings(max_examples=50)
def test_abs_delta_clause_instantiation(instance):
    assert isinstance(instance, abs_Delta_clause)

@given(instance=abs_Feature_strategy)
@settings(max_examples=50)
def test_abs_feature_instantiation(instance):
    assert isinstance(instance, abs_Feature)



@given(instance=abs_Feature_strategy)
def test_abs_feature_p_setter(instance):
    original = instance.p
    instance.p = original
    assert instance.p == original



@given(instance=abs_Feature_strategy)
def test_abs_feature_attr_assignment_setter(instance):
    original = instance.attr_assignment
    instance.attr_assignment = original
    assert instance.attr_assignment == original

@given(instance=abs_Object_update_assign_stmt_strategy)
@settings(max_examples=50)
def test_abs_object_update_assign_stmt_instantiation(instance):
    assert isinstance(instance, abs_Object_update_assign_stmt)

@given(instance=abs_Update_preamble_declaration_strategy)
@settings(max_examples=50)
def test_abs_update_preamble_declaration_instantiation(instance):
    assert isinstance(instance, abs_Update_preamble_declaration)

@given(instance=abs_Object_update_strategy)
@settings(max_examples=50)
def test_abs_object_update_instantiation(instance):
    assert isinstance(instance, abs_Object_update)

@given(instance=abs_Interface_modifier_fragment_strategy)
@settings(max_examples=50)
def test_abs_interface_modifier_fragment_instantiation(instance):
    assert isinstance(instance, abs_Interface_modifier_fragment)

@given(instance=Module_modifier_strategy)
@settings(max_examples=50)
def test_module_modifier_instantiation(instance):
    assert isinstance(instance, Module_modifier)

@given(instance=abs_OO_modifier_strategy)
@settings(max_examples=50)
def test_abs_oo_modifier_instantiation(instance):
    assert isinstance(instance, abs_OO_modifier)

@given(instance=abs_Namespace_modifier_strategy)
@settings(max_examples=50)
def test_abs_namespace_modifier_instantiation(instance):
    assert isinstance(instance, abs_Namespace_modifier)



@given(instance=abs_Namespace_modifier_strategy)
def test_abs_namespace_modifier_star_setter(instance):
    original = instance.star
    instance.star = original
    assert instance.star == original

@given(instance=abs_Functional_modifier_strategy)
@settings(max_examples=50)
def test_abs_functional_modifier_instantiation(instance):
    assert isinstance(instance, abs_Functional_modifier)

@given(instance=abs_Module_modifier_strategy)
@settings(max_examples=50)
def test_abs_module_modifier_instantiation(instance):
    assert isinstance(instance, abs_Module_modifier)

@given(instance=abs_Delta_access_strategy)
@settings(max_examples=50)
def test_abs_delta_access_instantiation(instance):
    assert isinstance(instance, abs_Delta_access)

@given(instance=abs_Delta_param_strategy)
@settings(max_examples=50)
def test_abs_delta_param_instantiation(instance):
    assert isinstance(instance, abs_Delta_param)

@given(instance=abs_Trait_oper_strategy)
@settings(max_examples=50)
def test_abs_trait_oper_instantiation(instance):
    assert isinstance(instance, abs_Trait_oper)

@given(instance=abs_Guard_strategy)
@settings(max_examples=50)
def test_abs_guard_instantiation(instance):
    assert isinstance(instance, abs_Guard)

@given(instance=Interface_modifier_fragment_strategy)
@settings(max_examples=50)
def test_interface_modifier_fragment_instantiation(instance):
    assert isinstance(instance, Interface_modifier_fragment)

@given(instance=Class_modifier_fragment_strategy)
@settings(max_examples=50)
def test_class_modifier_fragment_instantiation(instance):
    assert isinstance(instance, Class_modifier_fragment)

@given(instance=abs_Trait_expr_strategy)
@settings(max_examples=50)
def test_abs_trait_expr_instantiation(instance):
    assert isinstance(instance, abs_Trait_expr)

@given(instance=abs_Interface_name_strategy)
@settings(max_examples=50)
def test_abs_interface_name_instantiation(instance):
    assert isinstance(instance, abs_Interface_name)



@given(instance=abs_Interface_name_strategy)
def test_abs_interface_name_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=abs_Methodsig_strategy)
@settings(max_examples=50)
def test_abs_methodsig_instantiation(instance):
    assert isinstance(instance, abs_Methodsig)



@given(instance=abs_Methodsig_strategy)
def test_abs_methodsig_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=abs_Exp_strategy)
@settings(max_examples=50)
def test_abs_exp_instantiation(instance):
    assert isinstance(instance, abs_Exp)

@given(instance=abs_Method_strategy)
@settings(max_examples=50)
def test_abs_method_instantiation(instance):
    assert isinstance(instance, abs_Method)



@given(instance=abs_Method_strategy)
def test_abs_method_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=abs_Trait_usage_strategy)
@settings(max_examples=50)
def test_abs_trait_usage_instantiation(instance):
    assert isinstance(instance, abs_Trait_usage)

@given(instance=abs_Casestmtbranch_strategy)
@settings(max_examples=50)
def test_abs_casestmtbranch_instantiation(instance):
    assert isinstance(instance, abs_Casestmtbranch)

@given(instance=abs_Stmt_strategy)
@settings(max_examples=50)
def test_abs_stmt_instantiation(instance):
    assert isinstance(instance, abs_Stmt)



@given(instance=abs_Stmt_strategy)
def test_abs_stmt_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Case_branch_strategy)
@settings(max_examples=50)
def test_case_branch_instantiation(instance):
    assert isinstance(instance, Case_branch)

@given(instance=abs_Pattern_strategy)
@settings(max_examples=50)
def test_abs_pattern_instantiation(instance):
    assert isinstance(instance, abs_Pattern)

@given(instance=abs_Field_decl_strategy)
@settings(max_examples=50)
def test_abs_field_decl_instantiation(instance):
    assert isinstance(instance, abs_Field_decl)



@given(instance=abs_Field_decl_strategy)
def test_abs_field_decl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Pure_exp_strategy)
@settings(max_examples=50)
def test_pure_exp_instantiation(instance):
    assert isinstance(instance, Pure_exp)

@given(instance=abs_Or_expr_strategy)
@settings(max_examples=50)
def test_abs_or_expr_instantiation(instance):
    assert isinstance(instance, abs_Or_expr)

@given(instance=abs_And_expr_strategy)
@settings(max_examples=50)
def test_abs_and_expr_instantiation(instance):
    assert isinstance(instance, abs_And_expr)

@given(instance=abs_Equality_expr_strategy)
@settings(max_examples=50)
def test_abs_equality_expr_instantiation(instance):
    assert isinstance(instance, abs_Equality_expr)

@given(instance=abs_MulDivOrMod_expr_strategy)
@settings(max_examples=50)
def test_abs_muldivormod_expr_instantiation(instance):
    assert isinstance(instance, abs_MulDivOrMod_expr)

@given(instance=abs_PlusOrMinus_expr_strategy)
@settings(max_examples=50)
def test_abs_plusorminus_expr_instantiation(instance):
    assert isinstance(instance, abs_PlusOrMinus_expr)

@given(instance=abs_Comparison_expr_strategy)
@settings(max_examples=50)
def test_abs_comparison_expr_instantiation(instance):
    assert isinstance(instance, abs_Comparison_expr)

@given(instance=abs_Var_or_field_ref_strategy)
@settings(max_examples=50)
def test_abs_var_or_field_ref_instantiation(instance):
    assert isinstance(instance, abs_Var_or_field_ref)



@given(instance=abs_Var_or_field_ref_strategy)
def test_abs_var_or_field_ref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Update_preamble_declaration_strategy)
@settings(max_examples=50)
def test_update_preamble_declaration_instantiation(instance):
    assert isinstance(instance, Update_preamble_declaration)

@given(instance=abs_Type_exp_strategy)
@settings(max_examples=50)
def test_abs_type_exp_instantiation(instance):
    assert isinstance(instance, abs_Type_exp)



@given(instance=abs_Type_exp_strategy)
def test_abs_type_exp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Delta_param_strategy)
@settings(max_examples=50)
def test_delta_param_instantiation(instance):
    assert isinstance(instance, Delta_param)

@given(instance=abs_Has_condition_strategy)
@settings(max_examples=50)
def test_abs_has_condition_instantiation(instance):
    assert isinstance(instance, abs_Has_condition)

@given(instance=abs_Param_decl_strategy)
@settings(max_examples=50)
def test_abs_param_decl_instantiation(instance):
    assert isinstance(instance, abs_Param_decl)



@given(instance=abs_Param_decl_strategy)
def test_abs_param_decl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Function_param_strategy)
@settings(max_examples=50)
def test_function_param_instantiation(instance):
    assert isinstance(instance, Function_param)

@given(instance=abs_Anon_function_decl_strategy)
@settings(max_examples=50)
def test_abs_anon_function_decl_instantiation(instance):
    assert isinstance(instance, abs_Anon_function_decl)

@given(instance=abs_Function_name_param_decl_strategy)
@settings(max_examples=50)
def test_abs_function_name_param_decl_instantiation(instance):
    assert isinstance(instance, abs_Function_name_param_decl)



@given(instance=abs_Function_name_param_decl_strategy)
def test_abs_function_name_param_decl_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=abs_Pure_exp_list_strategy)
@settings(max_examples=50)
def test_abs_pure_exp_list_instantiation(instance):
    assert isinstance(instance, abs_Pure_exp_list)

@given(instance=abs_Function_param_strategy)
@settings(max_examples=50)
def test_abs_function_param_instantiation(instance):
    assert isinstance(instance, abs_Function_param)

@given(instance=abs_Function_list_strategy)
@settings(max_examples=50)
def test_abs_function_list_instantiation(instance):
    assert isinstance(instance, abs_Function_list)

@given(instance=Eff_expr_strategy)
@settings(max_examples=50)
def test_eff_expr_instantiation(instance):
    assert isinstance(instance, Eff_expr)

@given(instance=abs_Delta_id_strategy)
@settings(max_examples=50)
def test_abs_delta_id_instantiation(instance):
    assert isinstance(instance, abs_Delta_id)



@given(instance=abs_Delta_id_strategy)
def test_abs_delta_id_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Exp_strategy)
@settings(max_examples=50)
def test_exp_instantiation(instance):
    assert isinstance(instance, Exp)

@given(instance=abs_Eff_expr_strategy)
@settings(max_examples=50)
def test_abs_eff_expr_instantiation(instance):
    assert isinstance(instance, abs_Eff_expr)



@given(instance=abs_Eff_expr_strategy)
def test_abs_eff_expr_l_setter(instance):
    original = instance.l
    instance.l = original
    assert instance.l == original

@given(instance=Annotation_strategy)
@settings(max_examples=50)
def test_annotation_instantiation(instance):
    assert isinstance(instance, Annotation)

@given(instance=Data_constructor_arg_strategy)
@settings(max_examples=50)
def test_data_constructor_arg_instantiation(instance):
    assert isinstance(instance, Data_constructor_arg)

@given(instance=abs_Case_branch_strategy)
@settings(max_examples=50)
def test_abs_case_branch_instantiation(instance):
    assert isinstance(instance, abs_Case_branch)

@given(instance=abs_Main_block_strategy)
@settings(max_examples=50)
def test_abs_main_block_instantiation(instance):
    assert isinstance(instance, abs_Main_block)

@given(instance=abs_Decl_strategy)
@settings(max_examples=50)
def test_abs_decl_instantiation(instance):
    assert isinstance(instance, abs_Decl)



@given(instance=abs_Decl_strategy)
def test_abs_decl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=abs_Fextension_strategy)
@settings(max_examples=50)
def test_abs_fextension_instantiation(instance):
    assert isinstance(instance, abs_Fextension)



@given(instance=abs_Fextension_strategy)
def test_abs_fextension_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=abs_Feature_decl_strategy)
@settings(max_examples=50)
def test_abs_feature_decl_instantiation(instance):
    assert isinstance(instance, abs_Feature_decl)



@given(instance=abs_Feature_decl_strategy)
def test_abs_feature_decl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=abs_Annotation_strategy)
@settings(max_examples=50)
def test_abs_annotation_instantiation(instance):
    assert isinstance(instance, abs_Annotation)

@given(instance=abs_Annotations_strategy)
@settings(max_examples=50)
def test_abs_annotations_instantiation(instance):
    assert isinstance(instance, abs_Annotations)

@given(instance=abs_Data_constructor_arg_strategy)
@settings(max_examples=50)
def test_abs_data_constructor_arg_instantiation(instance):
    assert isinstance(instance, abs_Data_constructor_arg)

@given(instance=abs_Data_constructor_strategy)
@settings(max_examples=50)
def test_abs_data_constructor_instantiation(instance):
    assert isinstance(instance, abs_Data_constructor)



@given(instance=abs_Data_constructor_strategy)
def test_abs_data_constructor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Functional_modifier_strategy)
@settings(max_examples=50)
def test_functional_modifier_instantiation(instance):
    assert isinstance(instance, Functional_modifier)

@given(instance=abs_Function_name_decl_strategy)
@settings(max_examples=50)
def test_abs_function_name_decl_instantiation(instance):
    assert isinstance(instance, abs_Function_name_decl)



@given(instance=abs_Function_name_decl_strategy)
def test_abs_function_name_decl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=abs_Pure_exp_strategy)
@settings(max_examples=50)
def test_abs_pure_exp_instantiation(instance):
    assert isinstance(instance, abs_Pure_exp)



@given(instance=abs_Pure_exp_strategy)
def test_abs_pure_exp_await__setter(instance):
    original = instance.await_
    instance.await_ = original
    assert instance.await_ == original



@given(instance=abs_Pure_exp_strategy)
def test_abs_pure_exp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=abs_Pure_exp_strategy)
def test_abs_pure_exp_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original



@given(instance=abs_Pure_exp_strategy)
def test_abs_pure_exp_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=abs_Param_list_strategy)
@settings(max_examples=50)
def test_abs_param_list_instantiation(instance):
    assert isinstance(instance, abs_Param_list)

@given(instance=abs_Function_name_list_strategy)
@settings(max_examples=50)
def test_abs_function_name_list_instantiation(instance):
    assert isinstance(instance, abs_Function_name_list)

@given(instance=abs_Type_use_strategy)
@settings(max_examples=50)
def test_abs_type_use_instantiation(instance):
    assert isinstance(instance, abs_Type_use)



@given(instance=abs_Type_use_strategy)
def test_abs_type_use_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Decl_strategy)
@settings(max_examples=50)
def test_decl_instantiation(instance):
    assert isinstance(instance, Decl)

@given(instance=abs_Function_decl_strategy)
@settings(max_examples=50)
def test_abs_function_decl_instantiation(instance):
    assert isinstance(instance, abs_Function_decl)



@given(instance=abs_Function_decl_strategy)
def test_abs_function_decl_p_setter(instance):
    original = instance.p
    instance.p = original
    assert instance.p == original

@given(instance=abs_Interface_decl_strategy)
@settings(max_examples=50)
def test_abs_interface_decl_instantiation(instance):
    assert isinstance(instance, abs_Interface_decl)

@given(instance=abs_Exception_decl_strategy)
@settings(max_examples=50)
def test_abs_exception_decl_instantiation(instance):
    assert isinstance(instance, abs_Exception_decl)

@given(instance=abs_DataType_decl_strategy)
@settings(max_examples=50)
def test_abs_datatype_decl_instantiation(instance):
    assert isinstance(instance, abs_DataType_decl)



@given(instance=abs_DataType_decl_strategy)
def test_abs_datatype_decl_p_setter(instance):
    original = instance.p
    instance.p = original
    assert instance.p == original

@given(instance=abs_Trait_decl_strategy)
@settings(max_examples=50)
def test_abs_trait_decl_instantiation(instance):
    assert isinstance(instance, abs_Trait_decl)

@given(instance=abs_Typesyn_decl_strategy)
@settings(max_examples=50)
def test_abs_typesyn_decl_instantiation(instance):
    assert isinstance(instance, abs_Typesyn_decl)

@given(instance=abs_Class_decl_strategy)
@settings(max_examples=50)
def test_abs_class_decl_instantiation(instance):
    assert isinstance(instance, abs_Class_decl)

@given(instance=abs_Par_function_decl_strategy)
@settings(max_examples=50)
def test_abs_par_function_decl_instantiation(instance):
    assert isinstance(instance, abs_Par_function_decl)



@given(instance=abs_Par_function_decl_strategy)
def test_abs_par_function_decl_p_setter(instance):
    original = instance.p
    instance.p = original
    assert instance.p == original

@given(instance=Namespace_modifier_strategy)
@settings(max_examples=50)
def test_namespace_modifier_instantiation(instance):
    assert isinstance(instance, Namespace_modifier)

@given(instance=abs_Module_import_strategy)
@settings(max_examples=50)
def test_abs_module_import_instantiation(instance):
    assert isinstance(instance, abs_Module_import)



@given(instance=abs_Module_import_strategy)
def test_abs_module_import_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original



@given(instance=abs_Module_import_strategy)
def test_abs_module_import_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=abs_Module_export_strategy)
@settings(max_examples=50)
def test_abs_module_export_instantiation(instance):
    assert isinstance(instance, abs_Module_export)



@given(instance=abs_Module_export_strategy)
def test_abs_module_export_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original



@given(instance=abs_Module_export_strategy)
def test_abs_module_export_anyPackage_setter(instance):
    original = instance.anyPackage
    instance.anyPackage = original
    assert instance.anyPackage == original

@given(instance=abs_Product_decl_strategy)
@settings(max_examples=50)
def test_abs_product_decl_instantiation(instance):
    assert isinstance(instance, abs_Product_decl)



@given(instance=abs_Product_decl_strategy)
def test_abs_product_decl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=abs_Productline_decl_strategy)
@settings(max_examples=50)
def test_abs_productline_decl_instantiation(instance):
    assert isinstance(instance, abs_Productline_decl)



@given(instance=abs_Productline_decl_strategy)
def test_abs_productline_decl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=abs_Update_decl_strategy)
@settings(max_examples=50)
def test_abs_update_decl_instantiation(instance):
    assert isinstance(instance, abs_Update_decl)



@given(instance=abs_Update_decl_strategy)
def test_abs_update_decl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=abs_Delta_decl_strategy)
@settings(max_examples=50)
def test_abs_delta_decl_instantiation(instance):
    assert isinstance(instance, abs_Delta_decl)



@given(instance=abs_Delta_decl_strategy)
def test_abs_delta_decl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=abs_Module_decl_strategy)
@settings(max_examples=50)
def test_abs_module_decl_instantiation(instance):
    assert isinstance(instance, abs_Module_decl)



@given(instance=abs_Module_decl_strategy)
def test_abs_module_decl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=DomainModel__strategy)
@settings(max_examples=50)
def test_domainmodel__instantiation(instance):
    assert isinstance(instance, DomainModel_)

@given(instance=abs_Compilation_Unit_strategy)
@settings(max_examples=50)
def test_abs_compilation_unit_instantiation(instance):
    assert isinstance(instance, abs_Compilation_Unit)

@given(instance=abs_DomainModel__strategy)
@settings(max_examples=50)
def test_abs_domainmodel__instantiation(instance):
    assert isinstance(instance, abs_DomainModel_)
