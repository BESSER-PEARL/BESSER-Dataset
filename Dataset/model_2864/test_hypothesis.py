import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Mexp,
    abs::MexpPrimary::expr,
    abs::MexpImplies::expr,
    abs::MexpMulDivOrMod::expr,
    abs::MexpAnd::expr,
    abs::MexpPlusOrMinus::expr,
    abs::MexpOr::exp,
    Product::expr,
    abs::ProductAnd::exp,
    abs::ProductMinus::exp,
    abs::ProductOr::expr,
    Application::condition,
    abs::AppAnd::exp,
    abs::AppOr::exp,
    abs::MexpComparison::expr,
    abs::MexpEquality::expr,
    Guard,
    abs::AndGuard,
    abs::Mexp,
    abs::Fnode,
    abs::Feature::decl::constraint,
    abs::Feature::decl::attribute,
    abs::Feature::decl::group,
    Fnode,
    abs::Product::expr,
    abs::Product::reconfiguration,
    abs::Application::condition,
    abs::Deltaspec,
    abs::When::condition,
    abs::From::condition,
    abs::After::condition,
    abs::Class::modifier::fragment,
    abs::Delta::clause,
    abs::Feature,
    abs::Object::update::assign::stmt,
    abs::Update::preamble::declaration,
    abs::Object::update,
    abs::Interface::modifier::fragment,
    Module::modifier,
    abs::OO::modifier,
    abs::Namespace::modifier,
    abs::Functional::modifier,
    abs::Module::modifier,
    abs::Delta::access,
    abs::Delta::param,
    abs::Trait::oper,
    abs::Guard,
    Interface::modifier::fragment,
    Class::modifier::fragment,
    abs::Trait::expr,
    abs::Interface::name,
    abs::Methodsig,
    abs::Exp,
    abs::Method,
    abs::Trait::usage,
    abs::Casestmtbranch,
    abs::Stmt,
    Case::branch,
    abs::Pattern,
    abs::Field::decl,
    Pure::exp,
    abs::Equality::expr,
    abs::Comparison::expr,
    abs::Or::expr,
    abs::PlusOrMinus::expr,
    abs::MulDivOrMod::expr,
    abs::And::expr,
    abs::Var::or::field::ref,
    Update::preamble::declaration,
    abs::Type::exp,
    Delta::param,
    abs::Has::condition,
    abs::Param::decl,
    Function::param,
    abs::Anon::function::decl,
    abs::Function::name::param::decl,
    abs::Pure::exp::list,
    abs::Function::param,
    abs::Function::list,
    Eff::expr,
    abs::Delta::id,
    Exp,
    abs::Eff::expr,
    Annotation,
    Data::constructor::arg,
    abs::Case::branch,
    abs::Main::block,
    abs::Decl,
    abs::Fextension,
    abs::Feature::decl,
    abs::Annotation,
    abs::Annotations,
    abs::Data::constructor::arg,
    abs::Data::constructor,
    Functional::modifier,
    abs::Function::name::decl,
    abs::Pure::exp,
    abs::Param::list,
    abs::Function::name::list,
    abs::Type::use,
    Decl,
    abs::Trait::decl,
    abs::Function::decl,
    abs::Class::decl,
    abs::Interface::decl,
    abs::DataType::decl,
    abs::Exception::decl,
    abs::Typesyn::decl,
    abs::Par::function::decl,
    Namespace::modifier,
    abs::Module::import,
    abs::Module::export,
    abs::Product::decl,
    abs::Productline::decl,
    abs::Update::decl,
    abs::Delta::decl,
    abs::Module::decl,
    DomainModel_,
    abs::Compilation::Unit,
    abs::DomainModel_,
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



def test_abs::mexpprimary::expr_is_not_abstract():
    assert not inspect.isabstract(abs::MexpPrimary::expr)


def test_abs::mexpprimary::expr_constructor_exists():
    assert callable(abs::MexpPrimary::expr.__init__)


def test_abs::mexpprimary::expr_constructor_args():
    sig = inspect.signature(abs::MexpPrimary::expr.__init__)
    params = list(sig.parameters.keys())



def test_abs::mexpimplies::expr_is_not_abstract():
    assert not inspect.isabstract(abs::MexpImplies::expr)


def test_abs::mexpimplies::expr_constructor_exists():
    assert callable(abs::MexpImplies::expr.__init__)


def test_abs::mexpimplies::expr_constructor_args():
    sig = inspect.signature(abs::MexpImplies::expr.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_abs::mexpimplies::expr_has_op():
    assert hasattr(abs::MexpImplies::expr, "op")
    descriptor = None
    for klass in abs::MexpImplies::expr.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_abs::mexpmuldivormod::expr_is_not_abstract():
    assert not inspect.isabstract(abs::MexpMulDivOrMod::expr)


def test_abs::mexpmuldivormod::expr_constructor_exists():
    assert callable(abs::MexpMulDivOrMod::expr.__init__)


def test_abs::mexpmuldivormod::expr_constructor_args():
    sig = inspect.signature(abs::MexpMulDivOrMod::expr.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_abs::mexpmuldivormod::expr_has_op():
    assert hasattr(abs::MexpMulDivOrMod::expr, "op")
    descriptor = None
    for klass in abs::MexpMulDivOrMod::expr.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_abs::mexpand::expr_is_not_abstract():
    assert not inspect.isabstract(abs::MexpAnd::expr)


def test_abs::mexpand::expr_constructor_exists():
    assert callable(abs::MexpAnd::expr.__init__)


def test_abs::mexpand::expr_constructor_args():
    sig = inspect.signature(abs::MexpAnd::expr.__init__)
    params = list(sig.parameters.keys())



def test_abs::mexpplusorminus::expr_is_not_abstract():
    assert not inspect.isabstract(abs::MexpPlusOrMinus::expr)


def test_abs::mexpplusorminus::expr_constructor_exists():
    assert callable(abs::MexpPlusOrMinus::expr.__init__)


def test_abs::mexpplusorminus::expr_constructor_args():
    sig = inspect.signature(abs::MexpPlusOrMinus::expr.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_abs::mexpplusorminus::expr_has_op():
    assert hasattr(abs::MexpPlusOrMinus::expr, "op")
    descriptor = None
    for klass in abs::MexpPlusOrMinus::expr.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_abs::mexpor::exp_is_not_abstract():
    assert not inspect.isabstract(abs::MexpOr::exp)


def test_abs::mexpor::exp_constructor_exists():
    assert callable(abs::MexpOr::exp.__init__)


def test_abs::mexpor::exp_constructor_args():
    sig = inspect.signature(abs::MexpOr::exp.__init__)
    params = list(sig.parameters.keys())



def test_product::expr_is_not_abstract():
    assert not inspect.isabstract(Product::expr)


def test_product::expr_constructor_exists():
    assert callable(Product::expr.__init__)


def test_product::expr_constructor_args():
    sig = inspect.signature(Product::expr.__init__)
    params = list(sig.parameters.keys())



def test_abs::productand::exp_is_not_abstract():
    assert not inspect.isabstract(abs::ProductAnd::exp)


def test_abs::productand::exp_constructor_exists():
    assert callable(abs::ProductAnd::exp.__init__)


def test_abs::productand::exp_constructor_args():
    sig = inspect.signature(abs::ProductAnd::exp.__init__)
    params = list(sig.parameters.keys())



def test_abs::productminus::exp_is_not_abstract():
    assert not inspect.isabstract(abs::ProductMinus::exp)


def test_abs::productminus::exp_constructor_exists():
    assert callable(abs::ProductMinus::exp.__init__)


def test_abs::productminus::exp_constructor_args():
    sig = inspect.signature(abs::ProductMinus::exp.__init__)
    params = list(sig.parameters.keys())



def test_abs::productor::expr_is_not_abstract():
    assert not inspect.isabstract(abs::ProductOr::expr)


def test_abs::productor::expr_constructor_exists():
    assert callable(abs::ProductOr::expr.__init__)


def test_abs::productor::expr_constructor_args():
    sig = inspect.signature(abs::ProductOr::expr.__init__)
    params = list(sig.parameters.keys())



def test_application::condition_is_not_abstract():
    assert not inspect.isabstract(Application::condition)


def test_application::condition_constructor_exists():
    assert callable(Application::condition.__init__)


def test_application::condition_constructor_args():
    sig = inspect.signature(Application::condition.__init__)
    params = list(sig.parameters.keys())



def test_abs::appand::exp_is_not_abstract():
    assert not inspect.isabstract(abs::AppAnd::exp)


def test_abs::appand::exp_constructor_exists():
    assert callable(abs::AppAnd::exp.__init__)


def test_abs::appand::exp_constructor_args():
    sig = inspect.signature(abs::AppAnd::exp.__init__)
    params = list(sig.parameters.keys())



def test_abs::appor::exp_is_not_abstract():
    assert not inspect.isabstract(abs::AppOr::exp)


def test_abs::appor::exp_constructor_exists():
    assert callable(abs::AppOr::exp.__init__)


def test_abs::appor::exp_constructor_args():
    sig = inspect.signature(abs::AppOr::exp.__init__)
    params = list(sig.parameters.keys())



def test_abs::mexpcomparison::expr_is_not_abstract():
    assert not inspect.isabstract(abs::MexpComparison::expr)


def test_abs::mexpcomparison::expr_constructor_exists():
    assert callable(abs::MexpComparison::expr.__init__)


def test_abs::mexpcomparison::expr_constructor_args():
    sig = inspect.signature(abs::MexpComparison::expr.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_abs::mexpcomparison::expr_has_op():
    assert hasattr(abs::MexpComparison::expr, "op")
    descriptor = None
    for klass in abs::MexpComparison::expr.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_abs::mexpequality::expr_is_not_abstract():
    assert not inspect.isabstract(abs::MexpEquality::expr)


def test_abs::mexpequality::expr_constructor_exists():
    assert callable(abs::MexpEquality::expr.__init__)


def test_abs::mexpequality::expr_constructor_args():
    sig = inspect.signature(abs::MexpEquality::expr.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_abs::mexpequality::expr_has_op():
    assert hasattr(abs::MexpEquality::expr, "op")
    descriptor = None
    for klass in abs::MexpEquality::expr.__mro__:
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



def test_abs::andguard_is_not_abstract():
    assert not inspect.isabstract(abs::AndGuard)


def test_abs::andguard_constructor_exists():
    assert callable(abs::AndGuard.__init__)


def test_abs::andguard_constructor_args():
    sig = inspect.signature(abs::AndGuard.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_abs::andguard_has_op():
    assert hasattr(abs::AndGuard, "op")
    descriptor = None
    for klass in abs::AndGuard.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_abs::mexp_is_not_abstract():
    assert not inspect.isabstract(abs::Mexp)


def test_abs::mexp_constructor_exists():
    assert callable(abs::Mexp.__init__)


def test_abs::mexp_constructor_args():
    sig = inspect.signature(abs::Mexp.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_abs::mexp_has_value():
    assert hasattr(abs::Mexp, "value")
    descriptor = None
    for klass in abs::Mexp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_abs::fnode_is_not_abstract():
    assert not inspect.isabstract(abs::Fnode)


def test_abs::fnode_constructor_exists():
    assert callable(abs::Fnode.__init__)


def test_abs::fnode_constructor_args():
    sig = inspect.signature(abs::Fnode.__init__)
    params = list(sig.parameters.keys())



def test_abs::feature::decl::constraint_is_not_abstract():
    assert not inspect.isabstract(abs::Feature::decl::constraint)


def test_abs::feature::decl::constraint_constructor_exists():
    assert callable(abs::Feature::decl::constraint.__init__)


def test_abs::feature::decl::constraint_constructor_args():
    sig = inspect.signature(abs::Feature::decl::constraint.__init__)
    params = list(sig.parameters.keys())



def test_abs::feature::decl::attribute_is_not_abstract():
    assert not inspect.isabstract(abs::Feature::decl::attribute)


def test_abs::feature::decl::attribute_constructor_exists():
    assert callable(abs::Feature::decl::attribute.__init__)


def test_abs::feature::decl::attribute_constructor_args():
    sig = inspect.signature(abs::Feature::decl::attribute.__init__)
    params = list(sig.parameters.keys())
    assert "lBoundary_int" in params, "Missing parameter 'lBoundary_int'"
    assert "uBoundary_int" in params, "Missing parameter 'uBoundary_int'"
    assert "boundary_val" in params, "Missing parameter 'boundary_val'"

def test_abs::feature::decl::attribute_has_lBoundary_int():
    assert hasattr(abs::Feature::decl::attribute, "lBoundary_int")
    descriptor = None
    for klass in abs::Feature::decl::attribute.__mro__:
        if "lBoundary_int" in klass.__dict__:
            descriptor = klass.__dict__["lBoundary_int"]
            break
    assert isinstance(descriptor, property)

def test_abs::feature::decl::attribute_has_uBoundary_int():
    assert hasattr(abs::Feature::decl::attribute, "uBoundary_int")
    descriptor = None
    for klass in abs::Feature::decl::attribute.__mro__:
        if "uBoundary_int" in klass.__dict__:
            descriptor = klass.__dict__["uBoundary_int"]
            break
    assert isinstance(descriptor, property)

def test_abs::feature::decl::attribute_has_boundary_val():
    assert hasattr(abs::Feature::decl::attribute, "boundary_val")
    descriptor = None
    for klass in abs::Feature::decl::attribute.__mro__:
        if "boundary_val" in klass.__dict__:
            descriptor = klass.__dict__["boundary_val"]
            break
    assert isinstance(descriptor, property)



def test_abs::feature::decl::group_is_not_abstract():
    assert not inspect.isabstract(abs::Feature::decl::group)


def test_abs::feature::decl::group_constructor_exists():
    assert callable(abs::Feature::decl::group.__init__)


def test_abs::feature::decl::group_constructor_args():
    sig = inspect.signature(abs::Feature::decl::group.__init__)
    params = list(sig.parameters.keys())



def test_fnode_is_not_abstract():
    assert not inspect.isabstract(Fnode)


def test_fnode_constructor_exists():
    assert callable(Fnode.__init__)


def test_fnode_constructor_args():
    sig = inspect.signature(Fnode.__init__)
    params = list(sig.parameters.keys())



def test_abs::product::expr_is_not_abstract():
    assert not inspect.isabstract(abs::Product::expr)


def test_abs::product::expr_constructor_exists():
    assert callable(abs::Product::expr.__init__)


def test_abs::product::expr_constructor_args():
    sig = inspect.signature(abs::Product::expr.__init__)
    params = list(sig.parameters.keys())



def test_abs::product::reconfiguration_is_not_abstract():
    assert not inspect.isabstract(abs::Product::reconfiguration)


def test_abs::product::reconfiguration_constructor_exists():
    assert callable(abs::Product::reconfiguration.__init__)


def test_abs::product::reconfiguration_constructor_args():
    sig = inspect.signature(abs::Product::reconfiguration.__init__)
    params = list(sig.parameters.keys())
    assert "update" in params, "Missing parameter 'update'"
    assert "name" in params, "Missing parameter 'name'"

def test_abs::product::reconfiguration_has_update():
    assert hasattr(abs::Product::reconfiguration, "update")
    descriptor = None
    for klass in abs::Product::reconfiguration.__mro__:
        if "update" in klass.__dict__:
            descriptor = klass.__dict__["update"]
            break
    assert isinstance(descriptor, property)

def test_abs::product::reconfiguration_has_name():
    assert hasattr(abs::Product::reconfiguration, "name")
    descriptor = None
    for klass in abs::Product::reconfiguration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_abs::application::condition_is_not_abstract():
    assert not inspect.isabstract(abs::Application::condition)


def test_abs::application::condition_constructor_exists():
    assert callable(abs::Application::condition.__init__)


def test_abs::application::condition_constructor_args():
    sig = inspect.signature(abs::Application::condition.__init__)
    params = list(sig.parameters.keys())



def test_abs::deltaspec_is_not_abstract():
    assert not inspect.isabstract(abs::Deltaspec)


def test_abs::deltaspec_constructor_exists():
    assert callable(abs::Deltaspec.__init__)


def test_abs::deltaspec_constructor_args():
    sig = inspect.signature(abs::Deltaspec.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "deltaspec_param" in params, "Missing parameter 'deltaspec_param'"

def test_abs::deltaspec_has_name():
    assert hasattr(abs::Deltaspec, "name")
    descriptor = None
    for klass in abs::Deltaspec.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_abs::deltaspec_has_deltaspec_param():
    assert hasattr(abs::Deltaspec, "deltaspec_param")
    descriptor = None
    for klass in abs::Deltaspec.__mro__:
        if "deltaspec_param" in klass.__dict__:
            descriptor = klass.__dict__["deltaspec_param"]
            break
    assert isinstance(descriptor, property)



def test_abs::when::condition_is_not_abstract():
    assert not inspect.isabstract(abs::When::condition)


def test_abs::when::condition_constructor_exists():
    assert callable(abs::When::condition.__init__)


def test_abs::when::condition_constructor_args():
    sig = inspect.signature(abs::When::condition.__init__)
    params = list(sig.parameters.keys())



def test_abs::from::condition_is_not_abstract():
    assert not inspect.isabstract(abs::From::condition)


def test_abs::from::condition_constructor_exists():
    assert callable(abs::From::condition.__init__)


def test_abs::from::condition_constructor_args():
    sig = inspect.signature(abs::From::condition.__init__)
    params = list(sig.parameters.keys())



def test_abs::after::condition_is_not_abstract():
    assert not inspect.isabstract(abs::After::condition)


def test_abs::after::condition_constructor_exists():
    assert callable(abs::After::condition.__init__)


def test_abs::after::condition_constructor_args():
    sig = inspect.signature(abs::After::condition.__init__)
    params = list(sig.parameters.keys())



def test_abs::class::modifier::fragment_is_not_abstract():
    assert not inspect.isabstract(abs::Class::modifier::fragment)


def test_abs::class::modifier::fragment_constructor_exists():
    assert callable(abs::Class::modifier::fragment.__init__)


def test_abs::class::modifier::fragment_constructor_args():
    sig = inspect.signature(abs::Class::modifier::fragment.__init__)
    params = list(sig.parameters.keys())



def test_abs::delta::clause_is_not_abstract():
    assert not inspect.isabstract(abs::Delta::clause)


def test_abs::delta::clause_constructor_exists():
    assert callable(abs::Delta::clause.__init__)


def test_abs::delta::clause_constructor_args():
    sig = inspect.signature(abs::Delta::clause.__init__)
    params = list(sig.parameters.keys())



def test_abs::feature_is_not_abstract():
    assert not inspect.isabstract(abs::Feature)


def test_abs::feature_constructor_exists():
    assert callable(abs::Feature.__init__)


def test_abs::feature_constructor_args():
    sig = inspect.signature(abs::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "p" in params, "Missing parameter 'p'"
    assert "attr_assignment" in params, "Missing parameter 'attr_assignment'"

def test_abs::feature_has_p():
    assert hasattr(abs::Feature, "p")
    descriptor = None
    for klass in abs::Feature.__mro__:
        if "p" in klass.__dict__:
            descriptor = klass.__dict__["p"]
            break
    assert isinstance(descriptor, property)

def test_abs::feature_has_attr_assignment():
    assert hasattr(abs::Feature, "attr_assignment")
    descriptor = None
    for klass in abs::Feature.__mro__:
        if "attr_assignment" in klass.__dict__:
            descriptor = klass.__dict__["attr_assignment"]
            break
    assert isinstance(descriptor, property)



def test_abs::object::update::assign::stmt_is_not_abstract():
    assert not inspect.isabstract(abs::Object::update::assign::stmt)


def test_abs::object::update::assign::stmt_constructor_exists():
    assert callable(abs::Object::update::assign::stmt.__init__)


def test_abs::object::update::assign::stmt_constructor_args():
    sig = inspect.signature(abs::Object::update::assign::stmt.__init__)
    params = list(sig.parameters.keys())



def test_abs::update::preamble::declaration_is_not_abstract():
    assert not inspect.isabstract(abs::Update::preamble::declaration)


def test_abs::update::preamble::declaration_constructor_exists():
    assert callable(abs::Update::preamble::declaration.__init__)


def test_abs::update::preamble::declaration_constructor_args():
    sig = inspect.signature(abs::Update::preamble::declaration.__init__)
    params = list(sig.parameters.keys())



def test_abs::object::update_is_not_abstract():
    assert not inspect.isabstract(abs::Object::update)


def test_abs::object::update_constructor_exists():
    assert callable(abs::Object::update.__init__)


def test_abs::object::update_constructor_args():
    sig = inspect.signature(abs::Object::update.__init__)
    params = list(sig.parameters.keys())



def test_abs::interface::modifier::fragment_is_not_abstract():
    assert not inspect.isabstract(abs::Interface::modifier::fragment)


def test_abs::interface::modifier::fragment_constructor_exists():
    assert callable(abs::Interface::modifier::fragment.__init__)


def test_abs::interface::modifier::fragment_constructor_args():
    sig = inspect.signature(abs::Interface::modifier::fragment.__init__)
    params = list(sig.parameters.keys())



def test_module::modifier_is_not_abstract():
    assert not inspect.isabstract(Module::modifier)


def test_module::modifier_constructor_exists():
    assert callable(Module::modifier.__init__)


def test_module::modifier_constructor_args():
    sig = inspect.signature(Module::modifier.__init__)
    params = list(sig.parameters.keys())



def test_abs::oo::modifier_is_not_abstract():
    assert not inspect.isabstract(abs::OO::modifier)


def test_abs::oo::modifier_constructor_exists():
    assert callable(abs::OO::modifier.__init__)


def test_abs::oo::modifier_constructor_args():
    sig = inspect.signature(abs::OO::modifier.__init__)
    params = list(sig.parameters.keys())



def test_abs::namespace::modifier_is_not_abstract():
    assert not inspect.isabstract(abs::Namespace::modifier)


def test_abs::namespace::modifier_constructor_exists():
    assert callable(abs::Namespace::modifier.__init__)


def test_abs::namespace::modifier_constructor_args():
    sig = inspect.signature(abs::Namespace::modifier.__init__)
    params = list(sig.parameters.keys())
    assert "star" in params, "Missing parameter 'star'"

def test_abs::namespace::modifier_has_star():
    assert hasattr(abs::Namespace::modifier, "star")
    descriptor = None
    for klass in abs::Namespace::modifier.__mro__:
        if "star" in klass.__dict__:
            descriptor = klass.__dict__["star"]
            break
    assert isinstance(descriptor, property)



def test_abs::functional::modifier_is_not_abstract():
    assert not inspect.isabstract(abs::Functional::modifier)


def test_abs::functional::modifier_constructor_exists():
    assert callable(abs::Functional::modifier.__init__)


def test_abs::functional::modifier_constructor_args():
    sig = inspect.signature(abs::Functional::modifier.__init__)
    params = list(sig.parameters.keys())



def test_abs::module::modifier_is_not_abstract():
    assert not inspect.isabstract(abs::Module::modifier)


def test_abs::module::modifier_constructor_exists():
    assert callable(abs::Module::modifier.__init__)


def test_abs::module::modifier_constructor_args():
    sig = inspect.signature(abs::Module::modifier.__init__)
    params = list(sig.parameters.keys())



def test_abs::delta::access_is_not_abstract():
    assert not inspect.isabstract(abs::Delta::access)


def test_abs::delta::access_constructor_exists():
    assert callable(abs::Delta::access.__init__)


def test_abs::delta::access_constructor_args():
    sig = inspect.signature(abs::Delta::access.__init__)
    params = list(sig.parameters.keys())



def test_abs::delta::param_is_not_abstract():
    assert not inspect.isabstract(abs::Delta::param)


def test_abs::delta::param_constructor_exists():
    assert callable(abs::Delta::param.__init__)


def test_abs::delta::param_constructor_args():
    sig = inspect.signature(abs::Delta::param.__init__)
    params = list(sig.parameters.keys())



def test_abs::trait::oper_is_not_abstract():
    assert not inspect.isabstract(abs::Trait::oper)


def test_abs::trait::oper_constructor_exists():
    assert callable(abs::Trait::oper.__init__)


def test_abs::trait::oper_constructor_args():
    sig = inspect.signature(abs::Trait::oper.__init__)
    params = list(sig.parameters.keys())



def test_abs::guard_is_not_abstract():
    assert not inspect.isabstract(abs::Guard)


def test_abs::guard_constructor_exists():
    assert callable(abs::Guard.__init__)


def test_abs::guard_constructor_args():
    sig = inspect.signature(abs::Guard.__init__)
    params = list(sig.parameters.keys())



def test_interface::modifier::fragment_is_not_abstract():
    assert not inspect.isabstract(Interface::modifier::fragment)


def test_interface::modifier::fragment_constructor_exists():
    assert callable(Interface::modifier::fragment.__init__)


def test_interface::modifier::fragment_constructor_args():
    sig = inspect.signature(Interface::modifier::fragment.__init__)
    params = list(sig.parameters.keys())



def test_class::modifier::fragment_is_not_abstract():
    assert not inspect.isabstract(Class::modifier::fragment)


def test_class::modifier::fragment_constructor_exists():
    assert callable(Class::modifier::fragment.__init__)


def test_class::modifier::fragment_constructor_args():
    sig = inspect.signature(Class::modifier::fragment.__init__)
    params = list(sig.parameters.keys())



def test_abs::trait::expr_is_not_abstract():
    assert not inspect.isabstract(abs::Trait::expr)


def test_abs::trait::expr_constructor_exists():
    assert callable(abs::Trait::expr.__init__)


def test_abs::trait::expr_constructor_args():
    sig = inspect.signature(abs::Trait::expr.__init__)
    params = list(sig.parameters.keys())



def test_abs::interface::name_is_not_abstract():
    assert not inspect.isabstract(abs::Interface::name)


def test_abs::interface::name_constructor_exists():
    assert callable(abs::Interface::name.__init__)


def test_abs::interface::name_constructor_args():
    sig = inspect.signature(abs::Interface::name.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_abs::interface::name_has_name():
    assert hasattr(abs::Interface::name, "name")
    descriptor = None
    for klass in abs::Interface::name.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_abs::methodsig_is_not_abstract():
    assert not inspect.isabstract(abs::Methodsig)


def test_abs::methodsig_constructor_exists():
    assert callable(abs::Methodsig.__init__)


def test_abs::methodsig_constructor_args():
    sig = inspect.signature(abs::Methodsig.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_abs::methodsig_has_name():
    assert hasattr(abs::Methodsig, "name")
    descriptor = None
    for klass in abs::Methodsig.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_abs::exp_is_not_abstract():
    assert not inspect.isabstract(abs::Exp)


def test_abs::exp_constructor_exists():
    assert callable(abs::Exp.__init__)


def test_abs::exp_constructor_args():
    sig = inspect.signature(abs::Exp.__init__)
    params = list(sig.parameters.keys())



def test_abs::method_is_not_abstract():
    assert not inspect.isabstract(abs::Method)


def test_abs::method_constructor_exists():
    assert callable(abs::Method.__init__)


def test_abs::method_constructor_args():
    sig = inspect.signature(abs::Method.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_abs::method_has_name():
    assert hasattr(abs::Method, "name")
    descriptor = None
    for klass in abs::Method.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_abs::trait::usage_is_not_abstract():
    assert not inspect.isabstract(abs::Trait::usage)


def test_abs::trait::usage_constructor_exists():
    assert callable(abs::Trait::usage.__init__)


def test_abs::trait::usage_constructor_args():
    sig = inspect.signature(abs::Trait::usage.__init__)
    params = list(sig.parameters.keys())



def test_abs::casestmtbranch_is_not_abstract():
    assert not inspect.isabstract(abs::Casestmtbranch)


def test_abs::casestmtbranch_constructor_exists():
    assert callable(abs::Casestmtbranch.__init__)


def test_abs::casestmtbranch_constructor_args():
    sig = inspect.signature(abs::Casestmtbranch.__init__)
    params = list(sig.parameters.keys())



def test_abs::stmt_is_not_abstract():
    assert not inspect.isabstract(abs::Stmt)


def test_abs::stmt_constructor_exists():
    assert callable(abs::Stmt.__init__)


def test_abs::stmt_constructor_args():
    sig = inspect.signature(abs::Stmt.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_abs::stmt_has_name():
    assert hasattr(abs::Stmt, "name")
    descriptor = None
    for klass in abs::Stmt.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_case::branch_is_not_abstract():
    assert not inspect.isabstract(Case::branch)


def test_case::branch_constructor_exists():
    assert callable(Case::branch.__init__)


def test_case::branch_constructor_args():
    sig = inspect.signature(Case::branch.__init__)
    params = list(sig.parameters.keys())



def test_abs::pattern_is_not_abstract():
    assert not inspect.isabstract(abs::Pattern)


def test_abs::pattern_constructor_exists():
    assert callable(abs::Pattern.__init__)


def test_abs::pattern_constructor_args():
    sig = inspect.signature(abs::Pattern.__init__)
    params = list(sig.parameters.keys())



def test_abs::field::decl_is_not_abstract():
    assert not inspect.isabstract(abs::Field::decl)


def test_abs::field::decl_constructor_exists():
    assert callable(abs::Field::decl.__init__)


def test_abs::field::decl_constructor_args():
    sig = inspect.signature(abs::Field::decl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_abs::field::decl_has_name():
    assert hasattr(abs::Field::decl, "name")
    descriptor = None
    for klass in abs::Field::decl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_pure::exp_is_not_abstract():
    assert not inspect.isabstract(Pure::exp)


def test_pure::exp_constructor_exists():
    assert callable(Pure::exp.__init__)


def test_pure::exp_constructor_args():
    sig = inspect.signature(Pure::exp.__init__)
    params = list(sig.parameters.keys())



def test_abs::equality::expr_is_not_abstract():
    assert not inspect.isabstract(abs::Equality::expr)


def test_abs::equality::expr_constructor_exists():
    assert callable(abs::Equality::expr.__init__)


def test_abs::equality::expr_constructor_args():
    sig = inspect.signature(abs::Equality::expr.__init__)
    params = list(sig.parameters.keys())



def test_abs::comparison::expr_is_not_abstract():
    assert not inspect.isabstract(abs::Comparison::expr)


def test_abs::comparison::expr_constructor_exists():
    assert callable(abs::Comparison::expr.__init__)


def test_abs::comparison::expr_constructor_args():
    sig = inspect.signature(abs::Comparison::expr.__init__)
    params = list(sig.parameters.keys())



def test_abs::or::expr_is_not_abstract():
    assert not inspect.isabstract(abs::Or::expr)


def test_abs::or::expr_constructor_exists():
    assert callable(abs::Or::expr.__init__)


def test_abs::or::expr_constructor_args():
    sig = inspect.signature(abs::Or::expr.__init__)
    params = list(sig.parameters.keys())



def test_abs::plusorminus::expr_is_not_abstract():
    assert not inspect.isabstract(abs::PlusOrMinus::expr)


def test_abs::plusorminus::expr_constructor_exists():
    assert callable(abs::PlusOrMinus::expr.__init__)


def test_abs::plusorminus::expr_constructor_args():
    sig = inspect.signature(abs::PlusOrMinus::expr.__init__)
    params = list(sig.parameters.keys())



def test_abs::muldivormod::expr_is_not_abstract():
    assert not inspect.isabstract(abs::MulDivOrMod::expr)


def test_abs::muldivormod::expr_constructor_exists():
    assert callable(abs::MulDivOrMod::expr.__init__)


def test_abs::muldivormod::expr_constructor_args():
    sig = inspect.signature(abs::MulDivOrMod::expr.__init__)
    params = list(sig.parameters.keys())



def test_abs::and::expr_is_not_abstract():
    assert not inspect.isabstract(abs::And::expr)


def test_abs::and::expr_constructor_exists():
    assert callable(abs::And::expr.__init__)


def test_abs::and::expr_constructor_args():
    sig = inspect.signature(abs::And::expr.__init__)
    params = list(sig.parameters.keys())



def test_abs::var::or::field::ref_is_not_abstract():
    assert not inspect.isabstract(abs::Var::or::field::ref)


def test_abs::var::or::field::ref_constructor_exists():
    assert callable(abs::Var::or::field::ref.__init__)


def test_abs::var::or::field::ref_constructor_args():
    sig = inspect.signature(abs::Var::or::field::ref.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_abs::var::or::field::ref_has_name():
    assert hasattr(abs::Var::or::field::ref, "name")
    descriptor = None
    for klass in abs::Var::or::field::ref.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_update::preamble::declaration_is_not_abstract():
    assert not inspect.isabstract(Update::preamble::declaration)


def test_update::preamble::declaration_constructor_exists():
    assert callable(Update::preamble::declaration.__init__)


def test_update::preamble::declaration_constructor_args():
    sig = inspect.signature(Update::preamble::declaration.__init__)
    params = list(sig.parameters.keys())



def test_abs::type::exp_is_not_abstract():
    assert not inspect.isabstract(abs::Type::exp)


def test_abs::type::exp_constructor_exists():
    assert callable(abs::Type::exp.__init__)


def test_abs::type::exp_constructor_args():
    sig = inspect.signature(abs::Type::exp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_abs::type::exp_has_name():
    assert hasattr(abs::Type::exp, "name")
    descriptor = None
    for klass in abs::Type::exp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_delta::param_is_not_abstract():
    assert not inspect.isabstract(Delta::param)


def test_delta::param_constructor_exists():
    assert callable(Delta::param.__init__)


def test_delta::param_constructor_args():
    sig = inspect.signature(Delta::param.__init__)
    params = list(sig.parameters.keys())



def test_abs::has::condition_is_not_abstract():
    assert not inspect.isabstract(abs::Has::condition)


def test_abs::has::condition_constructor_exists():
    assert callable(abs::Has::condition.__init__)


def test_abs::has::condition_constructor_args():
    sig = inspect.signature(abs::Has::condition.__init__)
    params = list(sig.parameters.keys())



def test_abs::param::decl_is_not_abstract():
    assert not inspect.isabstract(abs::Param::decl)


def test_abs::param::decl_constructor_exists():
    assert callable(abs::Param::decl.__init__)


def test_abs::param::decl_constructor_args():
    sig = inspect.signature(abs::Param::decl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_abs::param::decl_has_name():
    assert hasattr(abs::Param::decl, "name")
    descriptor = None
    for klass in abs::Param::decl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_function::param_is_not_abstract():
    assert not inspect.isabstract(Function::param)


def test_function::param_constructor_exists():
    assert callable(Function::param.__init__)


def test_function::param_constructor_args():
    sig = inspect.signature(Function::param.__init__)
    params = list(sig.parameters.keys())



def test_abs::anon::function::decl_is_not_abstract():
    assert not inspect.isabstract(abs::Anon::function::decl)


def test_abs::anon::function::decl_constructor_exists():
    assert callable(abs::Anon::function::decl.__init__)


def test_abs::anon::function::decl_constructor_args():
    sig = inspect.signature(abs::Anon::function::decl.__init__)
    params = list(sig.parameters.keys())



def test_abs::function::name::param::decl_is_not_abstract():
    assert not inspect.isabstract(abs::Function::name::param::decl)


def test_abs::function::name::param::decl_constructor_exists():
    assert callable(abs::Function::name::param::decl.__init__)


def test_abs::function::name::param::decl_constructor_args():
    sig = inspect.signature(abs::Function::name::param::decl.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_abs::function::name::param::decl_has_value():
    assert hasattr(abs::Function::name::param::decl, "value")
    descriptor = None
    for klass in abs::Function::name::param::decl.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_abs::pure::exp::list_is_not_abstract():
    assert not inspect.isabstract(abs::Pure::exp::list)


def test_abs::pure::exp::list_constructor_exists():
    assert callable(abs::Pure::exp::list.__init__)


def test_abs::pure::exp::list_constructor_args():
    sig = inspect.signature(abs::Pure::exp::list.__init__)
    params = list(sig.parameters.keys())



def test_abs::function::param_is_not_abstract():
    assert not inspect.isabstract(abs::Function::param)


def test_abs::function::param_constructor_exists():
    assert callable(abs::Function::param.__init__)


def test_abs::function::param_constructor_args():
    sig = inspect.signature(abs::Function::param.__init__)
    params = list(sig.parameters.keys())



def test_abs::function::list_is_not_abstract():
    assert not inspect.isabstract(abs::Function::list)


def test_abs::function::list_constructor_exists():
    assert callable(abs::Function::list.__init__)


def test_abs::function::list_constructor_args():
    sig = inspect.signature(abs::Function::list.__init__)
    params = list(sig.parameters.keys())



def test_eff::expr_is_not_abstract():
    assert not inspect.isabstract(Eff::expr)


def test_eff::expr_constructor_exists():
    assert callable(Eff::expr.__init__)


def test_eff::expr_constructor_args():
    sig = inspect.signature(Eff::expr.__init__)
    params = list(sig.parameters.keys())



def test_abs::delta::id_is_not_abstract():
    assert not inspect.isabstract(abs::Delta::id)


def test_abs::delta::id_constructor_exists():
    assert callable(abs::Delta::id.__init__)


def test_abs::delta::id_constructor_args():
    sig = inspect.signature(abs::Delta::id.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_abs::delta::id_has_name():
    assert hasattr(abs::Delta::id, "name")
    descriptor = None
    for klass in abs::Delta::id.__mro__:
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



def test_abs::eff::expr_is_not_abstract():
    assert not inspect.isabstract(abs::Eff::expr)


def test_abs::eff::expr_constructor_exists():
    assert callable(abs::Eff::expr.__init__)


def test_abs::eff::expr_constructor_args():
    sig = inspect.signature(abs::Eff::expr.__init__)
    params = list(sig.parameters.keys())
    assert "l" in params, "Missing parameter 'l'"

def test_abs::eff::expr_has_l():
    assert hasattr(abs::Eff::expr, "l")
    descriptor = None
    for klass in abs::Eff::expr.__mro__:
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



def test_data::constructor::arg_is_not_abstract():
    assert not inspect.isabstract(Data::constructor::arg)


def test_data::constructor::arg_constructor_exists():
    assert callable(Data::constructor::arg.__init__)


def test_data::constructor::arg_constructor_args():
    sig = inspect.signature(Data::constructor::arg.__init__)
    params = list(sig.parameters.keys())



def test_abs::case::branch_is_not_abstract():
    assert not inspect.isabstract(abs::Case::branch)


def test_abs::case::branch_constructor_exists():
    assert callable(abs::Case::branch.__init__)


def test_abs::case::branch_constructor_args():
    sig = inspect.signature(abs::Case::branch.__init__)
    params = list(sig.parameters.keys())



def test_abs::main::block_is_not_abstract():
    assert not inspect.isabstract(abs::Main::block)


def test_abs::main::block_constructor_exists():
    assert callable(abs::Main::block.__init__)


def test_abs::main::block_constructor_args():
    sig = inspect.signature(abs::Main::block.__init__)
    params = list(sig.parameters.keys())



def test_abs::decl_is_not_abstract():
    assert not inspect.isabstract(abs::Decl)


def test_abs::decl_constructor_exists():
    assert callable(abs::Decl.__init__)


def test_abs::decl_constructor_args():
    sig = inspect.signature(abs::Decl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_abs::decl_has_name():
    assert hasattr(abs::Decl, "name")
    descriptor = None
    for klass in abs::Decl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_abs::fextension_is_not_abstract():
    assert not inspect.isabstract(abs::Fextension)


def test_abs::fextension_constructor_exists():
    assert callable(abs::Fextension.__init__)


def test_abs::fextension_constructor_args():
    sig = inspect.signature(abs::Fextension.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_abs::fextension_has_name():
    assert hasattr(abs::Fextension, "name")
    descriptor = None
    for klass in abs::Fextension.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_abs::feature::decl_is_not_abstract():
    assert not inspect.isabstract(abs::Feature::decl)


def test_abs::feature::decl_constructor_exists():
    assert callable(abs::Feature::decl.__init__)


def test_abs::feature::decl_constructor_args():
    sig = inspect.signature(abs::Feature::decl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_abs::feature::decl_has_name():
    assert hasattr(abs::Feature::decl, "name")
    descriptor = None
    for klass in abs::Feature::decl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_abs::annotation_is_not_abstract():
    assert not inspect.isabstract(abs::Annotation)


def test_abs::annotation_constructor_exists():
    assert callable(abs::Annotation.__init__)


def test_abs::annotation_constructor_args():
    sig = inspect.signature(abs::Annotation.__init__)
    params = list(sig.parameters.keys())



def test_abs::annotations_is_not_abstract():
    assert not inspect.isabstract(abs::Annotations)


def test_abs::annotations_constructor_exists():
    assert callable(abs::Annotations.__init__)


def test_abs::annotations_constructor_args():
    sig = inspect.signature(abs::Annotations.__init__)
    params = list(sig.parameters.keys())



def test_abs::data::constructor::arg_is_not_abstract():
    assert not inspect.isabstract(abs::Data::constructor::arg)


def test_abs::data::constructor::arg_constructor_exists():
    assert callable(abs::Data::constructor::arg.__init__)


def test_abs::data::constructor::arg_constructor_args():
    sig = inspect.signature(abs::Data::constructor::arg.__init__)
    params = list(sig.parameters.keys())



def test_abs::data::constructor_is_not_abstract():
    assert not inspect.isabstract(abs::Data::constructor)


def test_abs::data::constructor_constructor_exists():
    assert callable(abs::Data::constructor.__init__)


def test_abs::data::constructor_constructor_args():
    sig = inspect.signature(abs::Data::constructor.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_abs::data::constructor_has_name():
    assert hasattr(abs::Data::constructor, "name")
    descriptor = None
    for klass in abs::Data::constructor.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_functional::modifier_is_not_abstract():
    assert not inspect.isabstract(Functional::modifier)


def test_functional::modifier_constructor_exists():
    assert callable(Functional::modifier.__init__)


def test_functional::modifier_constructor_args():
    sig = inspect.signature(Functional::modifier.__init__)
    params = list(sig.parameters.keys())



def test_abs::function::name::decl_is_not_abstract():
    assert not inspect.isabstract(abs::Function::name::decl)


def test_abs::function::name::decl_constructor_exists():
    assert callable(abs::Function::name::decl.__init__)


def test_abs::function::name::decl_constructor_args():
    sig = inspect.signature(abs::Function::name::decl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_abs::function::name::decl_has_name():
    assert hasattr(abs::Function::name::decl, "name")
    descriptor = None
    for klass in abs::Function::name::decl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_abs::pure::exp_is_not_abstract():
    assert not inspect.isabstract(abs::Pure::exp)


def test_abs::pure::exp_constructor_exists():
    assert callable(abs::Pure::exp.__init__)


def test_abs::pure::exp_constructor_args():
    sig = inspect.signature(abs::Pure::exp.__init__)
    params = list(sig.parameters.keys())
    assert "await_" in params, "Missing parameter 'await_'"
    assert "op" in params, "Missing parameter 'op'"
    assert "value" in params, "Missing parameter 'value'"
    assert "val" in params, "Missing parameter 'val'"

def test_abs::pure::exp_has_await_():
    assert hasattr(abs::Pure::exp, "await_")
    descriptor = None
    for klass in abs::Pure::exp.__mro__:
        if "await_" in klass.__dict__:
            descriptor = klass.__dict__["await_"]
            break
    assert isinstance(descriptor, property)

def test_abs::pure::exp_has_op():
    assert hasattr(abs::Pure::exp, "op")
    descriptor = None
    for klass in abs::Pure::exp.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)

def test_abs::pure::exp_has_value():
    assert hasattr(abs::Pure::exp, "value")
    descriptor = None
    for klass in abs::Pure::exp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_abs::pure::exp_has_val():
    assert hasattr(abs::Pure::exp, "val")
    descriptor = None
    for klass in abs::Pure::exp.__mro__:
        if "val" in klass.__dict__:
            descriptor = klass.__dict__["val"]
            break
    assert isinstance(descriptor, property)



def test_abs::param::list_is_not_abstract():
    assert not inspect.isabstract(abs::Param::list)


def test_abs::param::list_constructor_exists():
    assert callable(abs::Param::list.__init__)


def test_abs::param::list_constructor_args():
    sig = inspect.signature(abs::Param::list.__init__)
    params = list(sig.parameters.keys())



def test_abs::function::name::list_is_not_abstract():
    assert not inspect.isabstract(abs::Function::name::list)


def test_abs::function::name::list_constructor_exists():
    assert callable(abs::Function::name::list.__init__)


def test_abs::function::name::list_constructor_args():
    sig = inspect.signature(abs::Function::name::list.__init__)
    params = list(sig.parameters.keys())



def test_abs::type::use_is_not_abstract():
    assert not inspect.isabstract(abs::Type::use)


def test_abs::type::use_constructor_exists():
    assert callable(abs::Type::use.__init__)


def test_abs::type::use_constructor_args():
    sig = inspect.signature(abs::Type::use.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_abs::type::use_has_name():
    assert hasattr(abs::Type::use, "name")
    descriptor = None
    for klass in abs::Type::use.__mro__:
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



def test_abs::trait::decl_is_not_abstract():
    assert not inspect.isabstract(abs::Trait::decl)


def test_abs::trait::decl_constructor_exists():
    assert callable(abs::Trait::decl.__init__)


def test_abs::trait::decl_constructor_args():
    sig = inspect.signature(abs::Trait::decl.__init__)
    params = list(sig.parameters.keys())



def test_abs::function::decl_is_not_abstract():
    assert not inspect.isabstract(abs::Function::decl)


def test_abs::function::decl_constructor_exists():
    assert callable(abs::Function::decl.__init__)


def test_abs::function::decl_constructor_args():
    sig = inspect.signature(abs::Function::decl.__init__)
    params = list(sig.parameters.keys())
    assert "p" in params, "Missing parameter 'p'"

def test_abs::function::decl_has_p():
    assert hasattr(abs::Function::decl, "p")
    descriptor = None
    for klass in abs::Function::decl.__mro__:
        if "p" in klass.__dict__:
            descriptor = klass.__dict__["p"]
            break
    assert isinstance(descriptor, property)



def test_abs::class::decl_is_not_abstract():
    assert not inspect.isabstract(abs::Class::decl)


def test_abs::class::decl_constructor_exists():
    assert callable(abs::Class::decl.__init__)


def test_abs::class::decl_constructor_args():
    sig = inspect.signature(abs::Class::decl.__init__)
    params = list(sig.parameters.keys())



def test_abs::interface::decl_is_not_abstract():
    assert not inspect.isabstract(abs::Interface::decl)


def test_abs::interface::decl_constructor_exists():
    assert callable(abs::Interface::decl.__init__)


def test_abs::interface::decl_constructor_args():
    sig = inspect.signature(abs::Interface::decl.__init__)
    params = list(sig.parameters.keys())



def test_abs::datatype::decl_is_not_abstract():
    assert not inspect.isabstract(abs::DataType::decl)


def test_abs::datatype::decl_constructor_exists():
    assert callable(abs::DataType::decl.__init__)


def test_abs::datatype::decl_constructor_args():
    sig = inspect.signature(abs::DataType::decl.__init__)
    params = list(sig.parameters.keys())
    assert "p" in params, "Missing parameter 'p'"

def test_abs::datatype::decl_has_p():
    assert hasattr(abs::DataType::decl, "p")
    descriptor = None
    for klass in abs::DataType::decl.__mro__:
        if "p" in klass.__dict__:
            descriptor = klass.__dict__["p"]
            break
    assert isinstance(descriptor, property)



def test_abs::exception::decl_is_not_abstract():
    assert not inspect.isabstract(abs::Exception::decl)


def test_abs::exception::decl_constructor_exists():
    assert callable(abs::Exception::decl.__init__)


def test_abs::exception::decl_constructor_args():
    sig = inspect.signature(abs::Exception::decl.__init__)
    params = list(sig.parameters.keys())



def test_abs::typesyn::decl_is_not_abstract():
    assert not inspect.isabstract(abs::Typesyn::decl)


def test_abs::typesyn::decl_constructor_exists():
    assert callable(abs::Typesyn::decl.__init__)


def test_abs::typesyn::decl_constructor_args():
    sig = inspect.signature(abs::Typesyn::decl.__init__)
    params = list(sig.parameters.keys())



def test_abs::par::function::decl_is_not_abstract():
    assert not inspect.isabstract(abs::Par::function::decl)


def test_abs::par::function::decl_constructor_exists():
    assert callable(abs::Par::function::decl.__init__)


def test_abs::par::function::decl_constructor_args():
    sig = inspect.signature(abs::Par::function::decl.__init__)
    params = list(sig.parameters.keys())
    assert "p" in params, "Missing parameter 'p'"

def test_abs::par::function::decl_has_p():
    assert hasattr(abs::Par::function::decl, "p")
    descriptor = None
    for klass in abs::Par::function::decl.__mro__:
        if "p" in klass.__dict__:
            descriptor = klass.__dict__["p"]
            break
    assert isinstance(descriptor, property)



def test_namespace::modifier_is_not_abstract():
    assert not inspect.isabstract(Namespace::modifier)


def test_namespace::modifier_constructor_exists():
    assert callable(Namespace::modifier.__init__)


def test_namespace::modifier_constructor_args():
    sig = inspect.signature(Namespace::modifier.__init__)
    params = list(sig.parameters.keys())



def test_abs::module::import_is_not_abstract():
    assert not inspect.isabstract(abs::Module::import)


def test_abs::module::import_constructor_exists():
    assert callable(abs::Module::import.__init__)


def test_abs::module::import_constructor_args():
    sig = inspect.signature(abs::Module::import.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"

def test_abs::module::import_has_name():
    assert hasattr(abs::Module::import, "name")
    descriptor = None
    for klass in abs::Module::import.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_abs::module::import_has_importedNamespace():
    assert hasattr(abs::Module::import, "importedNamespace")
    descriptor = None
    for klass in abs::Module::import.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)



def test_abs::module::export_is_not_abstract():
    assert not inspect.isabstract(abs::Module::export)


def test_abs::module::export_constructor_exists():
    assert callable(abs::Module::export.__init__)


def test_abs::module::export_constructor_args():
    sig = inspect.signature(abs::Module::export.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"
    assert "anyPackage" in params, "Missing parameter 'anyPackage'"

def test_abs::module::export_has_importedNamespace():
    assert hasattr(abs::Module::export, "importedNamespace")
    descriptor = None
    for klass in abs::Module::export.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)

def test_abs::module::export_has_anyPackage():
    assert hasattr(abs::Module::export, "anyPackage")
    descriptor = None
    for klass in abs::Module::export.__mro__:
        if "anyPackage" in klass.__dict__:
            descriptor = klass.__dict__["anyPackage"]
            break
    assert isinstance(descriptor, property)



def test_abs::product::decl_is_not_abstract():
    assert not inspect.isabstract(abs::Product::decl)


def test_abs::product::decl_constructor_exists():
    assert callable(abs::Product::decl.__init__)


def test_abs::product::decl_constructor_args():
    sig = inspect.signature(abs::Product::decl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_abs::product::decl_has_name():
    assert hasattr(abs::Product::decl, "name")
    descriptor = None
    for klass in abs::Product::decl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_abs::productline::decl_is_not_abstract():
    assert not inspect.isabstract(abs::Productline::decl)


def test_abs::productline::decl_constructor_exists():
    assert callable(abs::Productline::decl.__init__)


def test_abs::productline::decl_constructor_args():
    sig = inspect.signature(abs::Productline::decl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_abs::productline::decl_has_name():
    assert hasattr(abs::Productline::decl, "name")
    descriptor = None
    for klass in abs::Productline::decl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_abs::update::decl_is_not_abstract():
    assert not inspect.isabstract(abs::Update::decl)


def test_abs::update::decl_constructor_exists():
    assert callable(abs::Update::decl.__init__)


def test_abs::update::decl_constructor_args():
    sig = inspect.signature(abs::Update::decl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_abs::update::decl_has_name():
    assert hasattr(abs::Update::decl, "name")
    descriptor = None
    for klass in abs::Update::decl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_abs::delta::decl_is_not_abstract():
    assert not inspect.isabstract(abs::Delta::decl)


def test_abs::delta::decl_constructor_exists():
    assert callable(abs::Delta::decl.__init__)


def test_abs::delta::decl_constructor_args():
    sig = inspect.signature(abs::Delta::decl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_abs::delta::decl_has_name():
    assert hasattr(abs::Delta::decl, "name")
    descriptor = None
    for klass in abs::Delta::decl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_abs::module::decl_is_not_abstract():
    assert not inspect.isabstract(abs::Module::decl)


def test_abs::module::decl_constructor_exists():
    assert callable(abs::Module::decl.__init__)


def test_abs::module::decl_constructor_args():
    sig = inspect.signature(abs::Module::decl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_abs::module::decl_has_name():
    assert hasattr(abs::Module::decl, "name")
    descriptor = None
    for klass in abs::Module::decl.__mro__:
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



def test_abs::compilation::unit_is_not_abstract():
    assert not inspect.isabstract(abs::Compilation::Unit)


def test_abs::compilation::unit_constructor_exists():
    assert callable(abs::Compilation::Unit.__init__)


def test_abs::compilation::unit_constructor_args():
    sig = inspect.signature(abs::Compilation::Unit.__init__)
    params = list(sig.parameters.keys())



def test_abs::domainmodel__is_not_abstract():
    assert not inspect.isabstract(abs::DomainModel_)


def test_abs::domainmodel__constructor_exists():
    assert callable(abs::DomainModel_.__init__)


def test_abs::domainmodel__constructor_args():
    sig = inspect.signature(abs::DomainModel_.__init__)
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
abs::MexpPrimary::expr_strategy = st.builds(
    abs::MexpPrimary::expr,
)
abs::MexpImplies::expr_strategy = st.builds(
    abs::MexpImplies::expr,
    op=
        safe_text
)
abs::MexpMulDivOrMod::expr_strategy = st.builds(
    abs::MexpMulDivOrMod::expr,
    op=
        safe_text
)
abs::MexpAnd::expr_strategy = st.builds(
    abs::MexpAnd::expr,
)
abs::MexpPlusOrMinus::expr_strategy = st.builds(
    abs::MexpPlusOrMinus::expr,
    op=
        safe_text
)
abs::MexpOr::exp_strategy = st.builds(
    abs::MexpOr::exp,
)
Product::expr_strategy = st.builds(
    Product::expr,
)
abs::ProductAnd::exp_strategy = st.builds(
    abs::ProductAnd::exp,
)
abs::ProductMinus::exp_strategy = st.builds(
    abs::ProductMinus::exp,
)
abs::ProductOr::expr_strategy = st.builds(
    abs::ProductOr::expr,
)
Application::condition_strategy = st.builds(
    Application::condition,
)
abs::AppAnd::exp_strategy = st.builds(
    abs::AppAnd::exp,
)
abs::AppOr::exp_strategy = st.builds(
    abs::AppOr::exp,
)
abs::MexpComparison::expr_strategy = st.builds(
    abs::MexpComparison::expr,
    op=
        safe_text
)
abs::MexpEquality::expr_strategy = st.builds(
    abs::MexpEquality::expr,
    op=
        safe_text
)
Guard_strategy = st.builds(
    Guard,
)
abs::AndGuard_strategy = st.builds(
    abs::AndGuard,
    op=
        safe_text
)
abs::Mexp_strategy = st.builds(
    abs::Mexp,
    value=
        st.integers()
)
abs::Fnode_strategy = st.builds(
    abs::Fnode,
)
abs::Feature::decl::constraint_strategy = st.builds(
    abs::Feature::decl::constraint,
)
abs::Feature::decl::attribute_strategy = st.builds(
    abs::Feature::decl::attribute,
    lBoundary_int=
        safe_text,
    uBoundary_int=
        safe_text,
    boundary_val=
        safe_text
)
abs::Feature::decl::group_strategy = st.builds(
    abs::Feature::decl::group,
)
Fnode_strategy = st.builds(
    Fnode,
)
abs::Product::expr_strategy = st.builds(
    abs::Product::expr,
)
abs::Product::reconfiguration_strategy = st.builds(
    abs::Product::reconfiguration,
    update=
        safe_text,
    name=
        safe_text
)
abs::Application::condition_strategy = st.builds(
    abs::Application::condition,
)
abs::Deltaspec_strategy = st.builds(
    abs::Deltaspec,
    name=
        safe_text,
    deltaspec_param=
        safe_text
)
abs::When::condition_strategy = st.builds(
    abs::When::condition,
)
abs::From::condition_strategy = st.builds(
    abs::From::condition,
)
abs::After::condition_strategy = st.builds(
    abs::After::condition,
)
abs::Class::modifier::fragment_strategy = st.builds(
    abs::Class::modifier::fragment,
)
abs::Delta::clause_strategy = st.builds(
    abs::Delta::clause,
)
abs::Feature_strategy = st.builds(
    abs::Feature,
    p=
        safe_text,
    attr_assignment=
        safe_text
)
abs::Object::update::assign::stmt_strategy = st.builds(
    abs::Object::update::assign::stmt,
)
abs::Update::preamble::declaration_strategy = st.builds(
    abs::Update::preamble::declaration,
)
abs::Object::update_strategy = st.builds(
    abs::Object::update,
)
abs::Interface::modifier::fragment_strategy = st.builds(
    abs::Interface::modifier::fragment,
)
Module::modifier_strategy = st.builds(
    Module::modifier,
)
abs::OO::modifier_strategy = st.builds(
    abs::OO::modifier,
)
abs::Namespace::modifier_strategy = st.builds(
    abs::Namespace::modifier,
    star=
        safe_text
)
abs::Functional::modifier_strategy = st.builds(
    abs::Functional::modifier,
)
abs::Module::modifier_strategy = st.builds(
    abs::Module::modifier,
)
abs::Delta::access_strategy = st.builds(
    abs::Delta::access,
)
abs::Delta::param_strategy = st.builds(
    abs::Delta::param,
)
abs::Trait::oper_strategy = st.builds(
    abs::Trait::oper,
)
abs::Guard_strategy = st.builds(
    abs::Guard,
)
Interface::modifier::fragment_strategy = st.builds(
    Interface::modifier::fragment,
)
Class::modifier::fragment_strategy = st.builds(
    Class::modifier::fragment,
)
abs::Trait::expr_strategy = st.builds(
    abs::Trait::expr,
)
abs::Interface::name_strategy = st.builds(
    abs::Interface::name,
    name=
        safe_text
)
abs::Methodsig_strategy = st.builds(
    abs::Methodsig,
    name=
        safe_text
)
abs::Exp_strategy = st.builds(
    abs::Exp,
)
abs::Method_strategy = st.builds(
    abs::Method,
    name=
        safe_text
)
abs::Trait::usage_strategy = st.builds(
    abs::Trait::usage,
)
abs::Casestmtbranch_strategy = st.builds(
    abs::Casestmtbranch,
)
abs::Stmt_strategy = st.builds(
    abs::Stmt,
    name=
        safe_text
)
Case::branch_strategy = st.builds(
    Case::branch,
)
abs::Pattern_strategy = st.builds(
    abs::Pattern,
)
abs::Field::decl_strategy = st.builds(
    abs::Field::decl,
    name=
        safe_text
)
Pure::exp_strategy = st.builds(
    Pure::exp,
)
abs::Equality::expr_strategy = st.builds(
    abs::Equality::expr,
)
abs::Comparison::expr_strategy = st.builds(
    abs::Comparison::expr,
)
abs::Or::expr_strategy = st.builds(
    abs::Or::expr,
)
abs::PlusOrMinus::expr_strategy = st.builds(
    abs::PlusOrMinus::expr,
)
abs::MulDivOrMod::expr_strategy = st.builds(
    abs::MulDivOrMod::expr,
)
abs::And::expr_strategy = st.builds(
    abs::And::expr,
)
abs::Var::or::field::ref_strategy = st.builds(
    abs::Var::or::field::ref,
    name=
        safe_text
)
Update::preamble::declaration_strategy = st.builds(
    Update::preamble::declaration,
)
abs::Type::exp_strategy = st.builds(
    abs::Type::exp,
    name=
        safe_text
)
Delta::param_strategy = st.builds(
    Delta::param,
)
abs::Has::condition_strategy = st.builds(
    abs::Has::condition,
)
abs::Param::decl_strategy = st.builds(
    abs::Param::decl,
    name=
        safe_text
)
Function::param_strategy = st.builds(
    Function::param,
)
abs::Anon::function::decl_strategy = st.builds(
    abs::Anon::function::decl,
)
abs::Function::name::param::decl_strategy = st.builds(
    abs::Function::name::param::decl,
    value=
        safe_text
)
abs::Pure::exp::list_strategy = st.builds(
    abs::Pure::exp::list,
)
abs::Function::param_strategy = st.builds(
    abs::Function::param,
)
abs::Function::list_strategy = st.builds(
    abs::Function::list,
)
Eff::expr_strategy = st.builds(
    Eff::expr,
)
abs::Delta::id_strategy = st.builds(
    abs::Delta::id,
    name=
        safe_text
)
Exp_strategy = st.builds(
    Exp,
)
abs::Eff::expr_strategy = st.builds(
    abs::Eff::expr,
    l=
        safe_text
)
Annotation_strategy = st.builds(
    Annotation,
)
Data::constructor::arg_strategy = st.builds(
    Data::constructor::arg,
)
abs::Case::branch_strategy = st.builds(
    abs::Case::branch,
)
abs::Main::block_strategy = st.builds(
    abs::Main::block,
)
abs::Decl_strategy = st.builds(
    abs::Decl,
    name=
        safe_text
)
abs::Fextension_strategy = st.builds(
    abs::Fextension,
    name=
        safe_text
)
abs::Feature::decl_strategy = st.builds(
    abs::Feature::decl,
    name=
        safe_text
)
abs::Annotation_strategy = st.builds(
    abs::Annotation,
)
abs::Annotations_strategy = st.builds(
    abs::Annotations,
)
abs::Data::constructor::arg_strategy = st.builds(
    abs::Data::constructor::arg,
)
abs::Data::constructor_strategy = st.builds(
    abs::Data::constructor,
    name=
        safe_text
)
Functional::modifier_strategy = st.builds(
    Functional::modifier,
)
abs::Function::name::decl_strategy = st.builds(
    abs::Function::name::decl,
    name=
        safe_text
)
abs::Pure::exp_strategy = st.builds(
    abs::Pure::exp,
    await_=
        safe_text,
    op=
        safe_text,
    value=
        safe_text,
    val=
        safe_text
)
abs::Param::list_strategy = st.builds(
    abs::Param::list,
)
abs::Function::name::list_strategy = st.builds(
    abs::Function::name::list,
)
abs::Type::use_strategy = st.builds(
    abs::Type::use,
    name=
        safe_text
)
Decl_strategy = st.builds(
    Decl,
)
abs::Trait::decl_strategy = st.builds(
    abs::Trait::decl,
)
abs::Function::decl_strategy = st.builds(
    abs::Function::decl,
    p=
        safe_text
)
abs::Class::decl_strategy = st.builds(
    abs::Class::decl,
)
abs::Interface::decl_strategy = st.builds(
    abs::Interface::decl,
)
abs::DataType::decl_strategy = st.builds(
    abs::DataType::decl,
    p=
        safe_text
)
abs::Exception::decl_strategy = st.builds(
    abs::Exception::decl,
)
abs::Typesyn::decl_strategy = st.builds(
    abs::Typesyn::decl,
)
abs::Par::function::decl_strategy = st.builds(
    abs::Par::function::decl,
    p=
        safe_text
)
Namespace::modifier_strategy = st.builds(
    Namespace::modifier,
)
abs::Module::import_strategy = st.builds(
    abs::Module::import,
    name=
        safe_text,
    importedNamespace=
        safe_text
)
abs::Module::export_strategy = st.builds(
    abs::Module::export,
    importedNamespace=
        safe_text,
    anyPackage=
        safe_text
)
abs::Product::decl_strategy = st.builds(
    abs::Product::decl,
    name=
        safe_text
)
abs::Productline::decl_strategy = st.builds(
    abs::Productline::decl,
    name=
        safe_text
)
abs::Update::decl_strategy = st.builds(
    abs::Update::decl,
    name=
        safe_text
)
abs::Delta::decl_strategy = st.builds(
    abs::Delta::decl,
    name=
        safe_text
)
abs::Module::decl_strategy = st.builds(
    abs::Module::decl,
    name=
        safe_text
)
DomainModel__strategy = st.builds(
    DomainModel_,
)
abs::Compilation::Unit_strategy = st.builds(
    abs::Compilation::Unit,
)
abs::DomainModel__strategy = st.builds(
    abs::DomainModel_,
)

@given(instance=Mexp_strategy)
@settings(max_examples=50)
def test_mexp_instantiation(instance):
    assert isinstance(instance, Mexp)

@given(instance=abs::MexpPrimary::expr_strategy)
@settings(max_examples=50)
def test_abs::mexpprimary::expr_instantiation(instance):
    assert isinstance(instance, abs::MexpPrimary::expr)

@given(instance=abs::MexpImplies::expr_strategy)
@settings(max_examples=50)
def test_abs::mexpimplies::expr_instantiation(instance):
    assert isinstance(instance, abs::MexpImplies::expr)

@given(instance=abs::MexpImplies::expr_strategy)
def test_abs::mexpimplies::expr_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=abs::MexpImplies::expr_strategy)
def test_abs::mexpimplies::expr_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=abs::MexpMulDivOrMod::expr_strategy)
@settings(max_examples=50)
def test_abs::mexpmuldivormod::expr_instantiation(instance):
    assert isinstance(instance, abs::MexpMulDivOrMod::expr)

@given(instance=abs::MexpMulDivOrMod::expr_strategy)
def test_abs::mexpmuldivormod::expr_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=abs::MexpMulDivOrMod::expr_strategy)
def test_abs::mexpmuldivormod::expr_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=abs::MexpAnd::expr_strategy)
@settings(max_examples=50)
def test_abs::mexpand::expr_instantiation(instance):
    assert isinstance(instance, abs::MexpAnd::expr)

@given(instance=abs::MexpPlusOrMinus::expr_strategy)
@settings(max_examples=50)
def test_abs::mexpplusorminus::expr_instantiation(instance):
    assert isinstance(instance, abs::MexpPlusOrMinus::expr)

@given(instance=abs::MexpPlusOrMinus::expr_strategy)
def test_abs::mexpplusorminus::expr_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=abs::MexpPlusOrMinus::expr_strategy)
def test_abs::mexpplusorminus::expr_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=abs::MexpOr::exp_strategy)
@settings(max_examples=50)
def test_abs::mexpor::exp_instantiation(instance):
    assert isinstance(instance, abs::MexpOr::exp)

@given(instance=Product::expr_strategy)
@settings(max_examples=50)
def test_product::expr_instantiation(instance):
    assert isinstance(instance, Product::expr)

@given(instance=abs::ProductAnd::exp_strategy)
@settings(max_examples=50)
def test_abs::productand::exp_instantiation(instance):
    assert isinstance(instance, abs::ProductAnd::exp)

@given(instance=abs::ProductMinus::exp_strategy)
@settings(max_examples=50)
def test_abs::productminus::exp_instantiation(instance):
    assert isinstance(instance, abs::ProductMinus::exp)

@given(instance=abs::ProductOr::expr_strategy)
@settings(max_examples=50)
def test_abs::productor::expr_instantiation(instance):
    assert isinstance(instance, abs::ProductOr::expr)

@given(instance=Application::condition_strategy)
@settings(max_examples=50)
def test_application::condition_instantiation(instance):
    assert isinstance(instance, Application::condition)

@given(instance=abs::AppAnd::exp_strategy)
@settings(max_examples=50)
def test_abs::appand::exp_instantiation(instance):
    assert isinstance(instance, abs::AppAnd::exp)

@given(instance=abs::AppOr::exp_strategy)
@settings(max_examples=50)
def test_abs::appor::exp_instantiation(instance):
    assert isinstance(instance, abs::AppOr::exp)

@given(instance=abs::MexpComparison::expr_strategy)
@settings(max_examples=50)
def test_abs::mexpcomparison::expr_instantiation(instance):
    assert isinstance(instance, abs::MexpComparison::expr)

@given(instance=abs::MexpComparison::expr_strategy)
def test_abs::mexpcomparison::expr_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=abs::MexpComparison::expr_strategy)
def test_abs::mexpcomparison::expr_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=abs::MexpEquality::expr_strategy)
@settings(max_examples=50)
def test_abs::mexpequality::expr_instantiation(instance):
    assert isinstance(instance, abs::MexpEquality::expr)

@given(instance=abs::MexpEquality::expr_strategy)
def test_abs::mexpequality::expr_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=abs::MexpEquality::expr_strategy)
def test_abs::mexpequality::expr_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=Guard_strategy)
@settings(max_examples=50)
def test_guard_instantiation(instance):
    assert isinstance(instance, Guard)

@given(instance=abs::AndGuard_strategy)
@settings(max_examples=50)
def test_abs::andguard_instantiation(instance):
    assert isinstance(instance, abs::AndGuard)

@given(instance=abs::AndGuard_strategy)
def test_abs::andguard_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=abs::AndGuard_strategy)
def test_abs::andguard_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=abs::Mexp_strategy)
@settings(max_examples=50)
def test_abs::mexp_instantiation(instance):
    assert isinstance(instance, abs::Mexp)

@given(instance=abs::Mexp_strategy)
def test_abs::mexp_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=abs::Mexp_strategy)
def test_abs::mexp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=abs::Fnode_strategy)
@settings(max_examples=50)
def test_abs::fnode_instantiation(instance):
    assert isinstance(instance, abs::Fnode)

@given(instance=abs::Feature::decl::constraint_strategy)
@settings(max_examples=50)
def test_abs::feature::decl::constraint_instantiation(instance):
    assert isinstance(instance, abs::Feature::decl::constraint)

@given(instance=abs::Feature::decl::attribute_strategy)
@settings(max_examples=50)
def test_abs::feature::decl::attribute_instantiation(instance):
    assert isinstance(instance, abs::Feature::decl::attribute)

@given(instance=abs::Feature::decl::attribute_strategy)
def test_abs::feature::decl::attribute_lBoundary_int_type(instance):
    assert isinstance(instance.lBoundary_int, str)


@given(instance=abs::Feature::decl::attribute_strategy)
def test_abs::feature::decl::attribute_lBoundary_int_setter(instance):
    original = instance.lBoundary_int
    instance.lBoundary_int = original
    assert instance.lBoundary_int == original

@given(instance=abs::Feature::decl::attribute_strategy)
def test_abs::feature::decl::attribute_uBoundary_int_type(instance):
    assert isinstance(instance.uBoundary_int, str)


@given(instance=abs::Feature::decl::attribute_strategy)
def test_abs::feature::decl::attribute_uBoundary_int_setter(instance):
    original = instance.uBoundary_int
    instance.uBoundary_int = original
    assert instance.uBoundary_int == original

@given(instance=abs::Feature::decl::attribute_strategy)
def test_abs::feature::decl::attribute_boundary_val_type(instance):
    assert isinstance(instance.boundary_val, str)


@given(instance=abs::Feature::decl::attribute_strategy)
def test_abs::feature::decl::attribute_boundary_val_setter(instance):
    original = instance.boundary_val
    instance.boundary_val = original
    assert instance.boundary_val == original

@given(instance=abs::Feature::decl::group_strategy)
@settings(max_examples=50)
def test_abs::feature::decl::group_instantiation(instance):
    assert isinstance(instance, abs::Feature::decl::group)

@given(instance=Fnode_strategy)
@settings(max_examples=50)
def test_fnode_instantiation(instance):
    assert isinstance(instance, Fnode)

@given(instance=abs::Product::expr_strategy)
@settings(max_examples=50)
def test_abs::product::expr_instantiation(instance):
    assert isinstance(instance, abs::Product::expr)

@given(instance=abs::Product::reconfiguration_strategy)
@settings(max_examples=50)
def test_abs::product::reconfiguration_instantiation(instance):
    assert isinstance(instance, abs::Product::reconfiguration)

@given(instance=abs::Product::reconfiguration_strategy)
def test_abs::product::reconfiguration_update_type(instance):
    assert isinstance(instance.update, str)


@given(instance=abs::Product::reconfiguration_strategy)
def test_abs::product::reconfiguration_update_setter(instance):
    original = instance.update
    instance.update = original
    assert instance.update == original

@given(instance=abs::Product::reconfiguration_strategy)
def test_abs::product::reconfiguration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=abs::Product::reconfiguration_strategy)
def test_abs::product::reconfiguration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=abs::Application::condition_strategy)
@settings(max_examples=50)
def test_abs::application::condition_instantiation(instance):
    assert isinstance(instance, abs::Application::condition)

@given(instance=abs::Deltaspec_strategy)
@settings(max_examples=50)
def test_abs::deltaspec_instantiation(instance):
    assert isinstance(instance, abs::Deltaspec)

@given(instance=abs::Deltaspec_strategy)
def test_abs::deltaspec_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=abs::Deltaspec_strategy)
def test_abs::deltaspec_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=abs::Deltaspec_strategy)
def test_abs::deltaspec_deltaspec_param_type(instance):
    assert isinstance(instance.deltaspec_param, str)


@given(instance=abs::Deltaspec_strategy)
def test_abs::deltaspec_deltaspec_param_setter(instance):
    original = instance.deltaspec_param
    instance.deltaspec_param = original
    assert instance.deltaspec_param == original

@given(instance=abs::When::condition_strategy)
@settings(max_examples=50)
def test_abs::when::condition_instantiation(instance):
    assert isinstance(instance, abs::When::condition)

@given(instance=abs::From::condition_strategy)
@settings(max_examples=50)
def test_abs::from::condition_instantiation(instance):
    assert isinstance(instance, abs::From::condition)

@given(instance=abs::After::condition_strategy)
@settings(max_examples=50)
def test_abs::after::condition_instantiation(instance):
    assert isinstance(instance, abs::After::condition)

@given(instance=abs::Class::modifier::fragment_strategy)
@settings(max_examples=50)
def test_abs::class::modifier::fragment_instantiation(instance):
    assert isinstance(instance, abs::Class::modifier::fragment)

@given(instance=abs::Delta::clause_strategy)
@settings(max_examples=50)
def test_abs::delta::clause_instantiation(instance):
    assert isinstance(instance, abs::Delta::clause)

@given(instance=abs::Feature_strategy)
@settings(max_examples=50)
def test_abs::feature_instantiation(instance):
    assert isinstance(instance, abs::Feature)

@given(instance=abs::Feature_strategy)
def test_abs::feature_p_type(instance):
    assert isinstance(instance.p, str)


@given(instance=abs::Feature_strategy)
def test_abs::feature_p_setter(instance):
    original = instance.p
    instance.p = original
    assert instance.p == original

@given(instance=abs::Feature_strategy)
def test_abs::feature_attr_assignment_type(instance):
    assert isinstance(instance.attr_assignment, str)


@given(instance=abs::Feature_strategy)
def test_abs::feature_attr_assignment_setter(instance):
    original = instance.attr_assignment
    instance.attr_assignment = original
    assert instance.attr_assignment == original

@given(instance=abs::Object::update::assign::stmt_strategy)
@settings(max_examples=50)
def test_abs::object::update::assign::stmt_instantiation(instance):
    assert isinstance(instance, abs::Object::update::assign::stmt)

@given(instance=abs::Update::preamble::declaration_strategy)
@settings(max_examples=50)
def test_abs::update::preamble::declaration_instantiation(instance):
    assert isinstance(instance, abs::Update::preamble::declaration)

@given(instance=abs::Object::update_strategy)
@settings(max_examples=50)
def test_abs::object::update_instantiation(instance):
    assert isinstance(instance, abs::Object::update)

@given(instance=abs::Interface::modifier::fragment_strategy)
@settings(max_examples=50)
def test_abs::interface::modifier::fragment_instantiation(instance):
    assert isinstance(instance, abs::Interface::modifier::fragment)

@given(instance=Module::modifier_strategy)
@settings(max_examples=50)
def test_module::modifier_instantiation(instance):
    assert isinstance(instance, Module::modifier)

@given(instance=abs::OO::modifier_strategy)
@settings(max_examples=50)
def test_abs::oo::modifier_instantiation(instance):
    assert isinstance(instance, abs::OO::modifier)

@given(instance=abs::Namespace::modifier_strategy)
@settings(max_examples=50)
def test_abs::namespace::modifier_instantiation(instance):
    assert isinstance(instance, abs::Namespace::modifier)

@given(instance=abs::Namespace::modifier_strategy)
def test_abs::namespace::modifier_star_type(instance):
    assert isinstance(instance.star, str)


@given(instance=abs::Namespace::modifier_strategy)
def test_abs::namespace::modifier_star_setter(instance):
    original = instance.star
    instance.star = original
    assert instance.star == original

@given(instance=abs::Functional::modifier_strategy)
@settings(max_examples=50)
def test_abs::functional::modifier_instantiation(instance):
    assert isinstance(instance, abs::Functional::modifier)

@given(instance=abs::Module::modifier_strategy)
@settings(max_examples=50)
def test_abs::module::modifier_instantiation(instance):
    assert isinstance(instance, abs::Module::modifier)

@given(instance=abs::Delta::access_strategy)
@settings(max_examples=50)
def test_abs::delta::access_instantiation(instance):
    assert isinstance(instance, abs::Delta::access)

@given(instance=abs::Delta::param_strategy)
@settings(max_examples=50)
def test_abs::delta::param_instantiation(instance):
    assert isinstance(instance, abs::Delta::param)

@given(instance=abs::Trait::oper_strategy)
@settings(max_examples=50)
def test_abs::trait::oper_instantiation(instance):
    assert isinstance(instance, abs::Trait::oper)

@given(instance=abs::Guard_strategy)
@settings(max_examples=50)
def test_abs::guard_instantiation(instance):
    assert isinstance(instance, abs::Guard)

@given(instance=Interface::modifier::fragment_strategy)
@settings(max_examples=50)
def test_interface::modifier::fragment_instantiation(instance):
    assert isinstance(instance, Interface::modifier::fragment)

@given(instance=Class::modifier::fragment_strategy)
@settings(max_examples=50)
def test_class::modifier::fragment_instantiation(instance):
    assert isinstance(instance, Class::modifier::fragment)

@given(instance=abs::Trait::expr_strategy)
@settings(max_examples=50)
def test_abs::trait::expr_instantiation(instance):
    assert isinstance(instance, abs::Trait::expr)

@given(instance=abs::Interface::name_strategy)
@settings(max_examples=50)
def test_abs::interface::name_instantiation(instance):
    assert isinstance(instance, abs::Interface::name)

@given(instance=abs::Interface::name_strategy)
def test_abs::interface::name_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=abs::Interface::name_strategy)
def test_abs::interface::name_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=abs::Methodsig_strategy)
@settings(max_examples=50)
def test_abs::methodsig_instantiation(instance):
    assert isinstance(instance, abs::Methodsig)

@given(instance=abs::Methodsig_strategy)
def test_abs::methodsig_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=abs::Methodsig_strategy)
def test_abs::methodsig_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=abs::Exp_strategy)
@settings(max_examples=50)
def test_abs::exp_instantiation(instance):
    assert isinstance(instance, abs::Exp)

@given(instance=abs::Method_strategy)
@settings(max_examples=50)
def test_abs::method_instantiation(instance):
    assert isinstance(instance, abs::Method)

@given(instance=abs::Method_strategy)
def test_abs::method_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=abs::Method_strategy)
def test_abs::method_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=abs::Trait::usage_strategy)
@settings(max_examples=50)
def test_abs::trait::usage_instantiation(instance):
    assert isinstance(instance, abs::Trait::usage)

@given(instance=abs::Casestmtbranch_strategy)
@settings(max_examples=50)
def test_abs::casestmtbranch_instantiation(instance):
    assert isinstance(instance, abs::Casestmtbranch)

@given(instance=abs::Stmt_strategy)
@settings(max_examples=50)
def test_abs::stmt_instantiation(instance):
    assert isinstance(instance, abs::Stmt)

@given(instance=abs::Stmt_strategy)
def test_abs::stmt_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=abs::Stmt_strategy)
def test_abs::stmt_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Case::branch_strategy)
@settings(max_examples=50)
def test_case::branch_instantiation(instance):
    assert isinstance(instance, Case::branch)

@given(instance=abs::Pattern_strategy)
@settings(max_examples=50)
def test_abs::pattern_instantiation(instance):
    assert isinstance(instance, abs::Pattern)

@given(instance=abs::Field::decl_strategy)
@settings(max_examples=50)
def test_abs::field::decl_instantiation(instance):
    assert isinstance(instance, abs::Field::decl)

@given(instance=abs::Field::decl_strategy)
def test_abs::field::decl_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=abs::Field::decl_strategy)
def test_abs::field::decl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Pure::exp_strategy)
@settings(max_examples=50)
def test_pure::exp_instantiation(instance):
    assert isinstance(instance, Pure::exp)

@given(instance=abs::Equality::expr_strategy)
@settings(max_examples=50)
def test_abs::equality::expr_instantiation(instance):
    assert isinstance(instance, abs::Equality::expr)

@given(instance=abs::Comparison::expr_strategy)
@settings(max_examples=50)
def test_abs::comparison::expr_instantiation(instance):
    assert isinstance(instance, abs::Comparison::expr)

@given(instance=abs::Or::expr_strategy)
@settings(max_examples=50)
def test_abs::or::expr_instantiation(instance):
    assert isinstance(instance, abs::Or::expr)

@given(instance=abs::PlusOrMinus::expr_strategy)
@settings(max_examples=50)
def test_abs::plusorminus::expr_instantiation(instance):
    assert isinstance(instance, abs::PlusOrMinus::expr)

@given(instance=abs::MulDivOrMod::expr_strategy)
@settings(max_examples=50)
def test_abs::muldivormod::expr_instantiation(instance):
    assert isinstance(instance, abs::MulDivOrMod::expr)

@given(instance=abs::And::expr_strategy)
@settings(max_examples=50)
def test_abs::and::expr_instantiation(instance):
    assert isinstance(instance, abs::And::expr)

@given(instance=abs::Var::or::field::ref_strategy)
@settings(max_examples=50)
def test_abs::var::or::field::ref_instantiation(instance):
    assert isinstance(instance, abs::Var::or::field::ref)

@given(instance=abs::Var::or::field::ref_strategy)
def test_abs::var::or::field::ref_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=abs::Var::or::field::ref_strategy)
def test_abs::var::or::field::ref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Update::preamble::declaration_strategy)
@settings(max_examples=50)
def test_update::preamble::declaration_instantiation(instance):
    assert isinstance(instance, Update::preamble::declaration)

@given(instance=abs::Type::exp_strategy)
@settings(max_examples=50)
def test_abs::type::exp_instantiation(instance):
    assert isinstance(instance, abs::Type::exp)

@given(instance=abs::Type::exp_strategy)
def test_abs::type::exp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=abs::Type::exp_strategy)
def test_abs::type::exp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Delta::param_strategy)
@settings(max_examples=50)
def test_delta::param_instantiation(instance):
    assert isinstance(instance, Delta::param)

@given(instance=abs::Has::condition_strategy)
@settings(max_examples=50)
def test_abs::has::condition_instantiation(instance):
    assert isinstance(instance, abs::Has::condition)

@given(instance=abs::Param::decl_strategy)
@settings(max_examples=50)
def test_abs::param::decl_instantiation(instance):
    assert isinstance(instance, abs::Param::decl)

@given(instance=abs::Param::decl_strategy)
def test_abs::param::decl_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=abs::Param::decl_strategy)
def test_abs::param::decl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Function::param_strategy)
@settings(max_examples=50)
def test_function::param_instantiation(instance):
    assert isinstance(instance, Function::param)

@given(instance=abs::Anon::function::decl_strategy)
@settings(max_examples=50)
def test_abs::anon::function::decl_instantiation(instance):
    assert isinstance(instance, abs::Anon::function::decl)

@given(instance=abs::Function::name::param::decl_strategy)
@settings(max_examples=50)
def test_abs::function::name::param::decl_instantiation(instance):
    assert isinstance(instance, abs::Function::name::param::decl)

@given(instance=abs::Function::name::param::decl_strategy)
def test_abs::function::name::param::decl_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=abs::Function::name::param::decl_strategy)
def test_abs::function::name::param::decl_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=abs::Pure::exp::list_strategy)
@settings(max_examples=50)
def test_abs::pure::exp::list_instantiation(instance):
    assert isinstance(instance, abs::Pure::exp::list)

@given(instance=abs::Function::param_strategy)
@settings(max_examples=50)
def test_abs::function::param_instantiation(instance):
    assert isinstance(instance, abs::Function::param)

@given(instance=abs::Function::list_strategy)
@settings(max_examples=50)
def test_abs::function::list_instantiation(instance):
    assert isinstance(instance, abs::Function::list)

@given(instance=Eff::expr_strategy)
@settings(max_examples=50)
def test_eff::expr_instantiation(instance):
    assert isinstance(instance, Eff::expr)

@given(instance=abs::Delta::id_strategy)
@settings(max_examples=50)
def test_abs::delta::id_instantiation(instance):
    assert isinstance(instance, abs::Delta::id)

@given(instance=abs::Delta::id_strategy)
def test_abs::delta::id_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=abs::Delta::id_strategy)
def test_abs::delta::id_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Exp_strategy)
@settings(max_examples=50)
def test_exp_instantiation(instance):
    assert isinstance(instance, Exp)

@given(instance=abs::Eff::expr_strategy)
@settings(max_examples=50)
def test_abs::eff::expr_instantiation(instance):
    assert isinstance(instance, abs::Eff::expr)

@given(instance=abs::Eff::expr_strategy)
def test_abs::eff::expr_l_type(instance):
    assert isinstance(instance.l, str)


@given(instance=abs::Eff::expr_strategy)
def test_abs::eff::expr_l_setter(instance):
    original = instance.l
    instance.l = original
    assert instance.l == original

@given(instance=Annotation_strategy)
@settings(max_examples=50)
def test_annotation_instantiation(instance):
    assert isinstance(instance, Annotation)

@given(instance=Data::constructor::arg_strategy)
@settings(max_examples=50)
def test_data::constructor::arg_instantiation(instance):
    assert isinstance(instance, Data::constructor::arg)

@given(instance=abs::Case::branch_strategy)
@settings(max_examples=50)
def test_abs::case::branch_instantiation(instance):
    assert isinstance(instance, abs::Case::branch)

@given(instance=abs::Main::block_strategy)
@settings(max_examples=50)
def test_abs::main::block_instantiation(instance):
    assert isinstance(instance, abs::Main::block)

@given(instance=abs::Decl_strategy)
@settings(max_examples=50)
def test_abs::decl_instantiation(instance):
    assert isinstance(instance, abs::Decl)

@given(instance=abs::Decl_strategy)
def test_abs::decl_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=abs::Decl_strategy)
def test_abs::decl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=abs::Fextension_strategy)
@settings(max_examples=50)
def test_abs::fextension_instantiation(instance):
    assert isinstance(instance, abs::Fextension)

@given(instance=abs::Fextension_strategy)
def test_abs::fextension_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=abs::Fextension_strategy)
def test_abs::fextension_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=abs::Feature::decl_strategy)
@settings(max_examples=50)
def test_abs::feature::decl_instantiation(instance):
    assert isinstance(instance, abs::Feature::decl)

@given(instance=abs::Feature::decl_strategy)
def test_abs::feature::decl_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=abs::Feature::decl_strategy)
def test_abs::feature::decl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=abs::Annotation_strategy)
@settings(max_examples=50)
def test_abs::annotation_instantiation(instance):
    assert isinstance(instance, abs::Annotation)

@given(instance=abs::Annotations_strategy)
@settings(max_examples=50)
def test_abs::annotations_instantiation(instance):
    assert isinstance(instance, abs::Annotations)

@given(instance=abs::Data::constructor::arg_strategy)
@settings(max_examples=50)
def test_abs::data::constructor::arg_instantiation(instance):
    assert isinstance(instance, abs::Data::constructor::arg)

@given(instance=abs::Data::constructor_strategy)
@settings(max_examples=50)
def test_abs::data::constructor_instantiation(instance):
    assert isinstance(instance, abs::Data::constructor)

@given(instance=abs::Data::constructor_strategy)
def test_abs::data::constructor_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=abs::Data::constructor_strategy)
def test_abs::data::constructor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Functional::modifier_strategy)
@settings(max_examples=50)
def test_functional::modifier_instantiation(instance):
    assert isinstance(instance, Functional::modifier)

@given(instance=abs::Function::name::decl_strategy)
@settings(max_examples=50)
def test_abs::function::name::decl_instantiation(instance):
    assert isinstance(instance, abs::Function::name::decl)

@given(instance=abs::Function::name::decl_strategy)
def test_abs::function::name::decl_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=abs::Function::name::decl_strategy)
def test_abs::function::name::decl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=abs::Pure::exp_strategy)
@settings(max_examples=50)
def test_abs::pure::exp_instantiation(instance):
    assert isinstance(instance, abs::Pure::exp)

@given(instance=abs::Pure::exp_strategy)
def test_abs::pure::exp_await__type(instance):
    assert isinstance(instance.await_, str)


@given(instance=abs::Pure::exp_strategy)
def test_abs::pure::exp_await__setter(instance):
    original = instance.await_
    instance.await_ = original
    assert instance.await_ == original

@given(instance=abs::Pure::exp_strategy)
def test_abs::pure::exp_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=abs::Pure::exp_strategy)
def test_abs::pure::exp_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=abs::Pure::exp_strategy)
def test_abs::pure::exp_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=abs::Pure::exp_strategy)
def test_abs::pure::exp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=abs::Pure::exp_strategy)
def test_abs::pure::exp_val_type(instance):
    assert isinstance(instance.val, str)


@given(instance=abs::Pure::exp_strategy)
def test_abs::pure::exp_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original

@given(instance=abs::Param::list_strategy)
@settings(max_examples=50)
def test_abs::param::list_instantiation(instance):
    assert isinstance(instance, abs::Param::list)

@given(instance=abs::Function::name::list_strategy)
@settings(max_examples=50)
def test_abs::function::name::list_instantiation(instance):
    assert isinstance(instance, abs::Function::name::list)

@given(instance=abs::Type::use_strategy)
@settings(max_examples=50)
def test_abs::type::use_instantiation(instance):
    assert isinstance(instance, abs::Type::use)

@given(instance=abs::Type::use_strategy)
def test_abs::type::use_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=abs::Type::use_strategy)
def test_abs::type::use_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Decl_strategy)
@settings(max_examples=50)
def test_decl_instantiation(instance):
    assert isinstance(instance, Decl)

@given(instance=abs::Trait::decl_strategy)
@settings(max_examples=50)
def test_abs::trait::decl_instantiation(instance):
    assert isinstance(instance, abs::Trait::decl)

@given(instance=abs::Function::decl_strategy)
@settings(max_examples=50)
def test_abs::function::decl_instantiation(instance):
    assert isinstance(instance, abs::Function::decl)

@given(instance=abs::Function::decl_strategy)
def test_abs::function::decl_p_type(instance):
    assert isinstance(instance.p, str)


@given(instance=abs::Function::decl_strategy)
def test_abs::function::decl_p_setter(instance):
    original = instance.p
    instance.p = original
    assert instance.p == original

@given(instance=abs::Class::decl_strategy)
@settings(max_examples=50)
def test_abs::class::decl_instantiation(instance):
    assert isinstance(instance, abs::Class::decl)

@given(instance=abs::Interface::decl_strategy)
@settings(max_examples=50)
def test_abs::interface::decl_instantiation(instance):
    assert isinstance(instance, abs::Interface::decl)

@given(instance=abs::DataType::decl_strategy)
@settings(max_examples=50)
def test_abs::datatype::decl_instantiation(instance):
    assert isinstance(instance, abs::DataType::decl)

@given(instance=abs::DataType::decl_strategy)
def test_abs::datatype::decl_p_type(instance):
    assert isinstance(instance.p, str)


@given(instance=abs::DataType::decl_strategy)
def test_abs::datatype::decl_p_setter(instance):
    original = instance.p
    instance.p = original
    assert instance.p == original

@given(instance=abs::Exception::decl_strategy)
@settings(max_examples=50)
def test_abs::exception::decl_instantiation(instance):
    assert isinstance(instance, abs::Exception::decl)

@given(instance=abs::Typesyn::decl_strategy)
@settings(max_examples=50)
def test_abs::typesyn::decl_instantiation(instance):
    assert isinstance(instance, abs::Typesyn::decl)

@given(instance=abs::Par::function::decl_strategy)
@settings(max_examples=50)
def test_abs::par::function::decl_instantiation(instance):
    assert isinstance(instance, abs::Par::function::decl)

@given(instance=abs::Par::function::decl_strategy)
def test_abs::par::function::decl_p_type(instance):
    assert isinstance(instance.p, str)


@given(instance=abs::Par::function::decl_strategy)
def test_abs::par::function::decl_p_setter(instance):
    original = instance.p
    instance.p = original
    assert instance.p == original

@given(instance=Namespace::modifier_strategy)
@settings(max_examples=50)
def test_namespace::modifier_instantiation(instance):
    assert isinstance(instance, Namespace::modifier)

@given(instance=abs::Module::import_strategy)
@settings(max_examples=50)
def test_abs::module::import_instantiation(instance):
    assert isinstance(instance, abs::Module::import)

@given(instance=abs::Module::import_strategy)
def test_abs::module::import_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=abs::Module::import_strategy)
def test_abs::module::import_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=abs::Module::import_strategy)
def test_abs::module::import_importedNamespace_type(instance):
    assert isinstance(instance.importedNamespace, str)


@given(instance=abs::Module::import_strategy)
def test_abs::module::import_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original

@given(instance=abs::Module::export_strategy)
@settings(max_examples=50)
def test_abs::module::export_instantiation(instance):
    assert isinstance(instance, abs::Module::export)

@given(instance=abs::Module::export_strategy)
def test_abs::module::export_importedNamespace_type(instance):
    assert isinstance(instance.importedNamespace, str)


@given(instance=abs::Module::export_strategy)
def test_abs::module::export_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original

@given(instance=abs::Module::export_strategy)
def test_abs::module::export_anyPackage_type(instance):
    assert isinstance(instance.anyPackage, str)


@given(instance=abs::Module::export_strategy)
def test_abs::module::export_anyPackage_setter(instance):
    original = instance.anyPackage
    instance.anyPackage = original
    assert instance.anyPackage == original

@given(instance=abs::Product::decl_strategy)
@settings(max_examples=50)
def test_abs::product::decl_instantiation(instance):
    assert isinstance(instance, abs::Product::decl)

@given(instance=abs::Product::decl_strategy)
def test_abs::product::decl_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=abs::Product::decl_strategy)
def test_abs::product::decl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=abs::Productline::decl_strategy)
@settings(max_examples=50)
def test_abs::productline::decl_instantiation(instance):
    assert isinstance(instance, abs::Productline::decl)

@given(instance=abs::Productline::decl_strategy)
def test_abs::productline::decl_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=abs::Productline::decl_strategy)
def test_abs::productline::decl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=abs::Update::decl_strategy)
@settings(max_examples=50)
def test_abs::update::decl_instantiation(instance):
    assert isinstance(instance, abs::Update::decl)

@given(instance=abs::Update::decl_strategy)
def test_abs::update::decl_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=abs::Update::decl_strategy)
def test_abs::update::decl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=abs::Delta::decl_strategy)
@settings(max_examples=50)
def test_abs::delta::decl_instantiation(instance):
    assert isinstance(instance, abs::Delta::decl)

@given(instance=abs::Delta::decl_strategy)
def test_abs::delta::decl_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=abs::Delta::decl_strategy)
def test_abs::delta::decl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=abs::Module::decl_strategy)
@settings(max_examples=50)
def test_abs::module::decl_instantiation(instance):
    assert isinstance(instance, abs::Module::decl)

@given(instance=abs::Module::decl_strategy)
def test_abs::module::decl_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=abs::Module::decl_strategy)
def test_abs::module::decl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=DomainModel__strategy)
@settings(max_examples=50)
def test_domainmodel__instantiation(instance):
    assert isinstance(instance, DomainModel_)

@given(instance=abs::Compilation::Unit_strategy)
@settings(max_examples=50)
def test_abs::compilation::unit_instantiation(instance):
    assert isinstance(instance, abs::Compilation::Unit)

@given(instance=abs::DomainModel__strategy)
@settings(max_examples=50)
def test_abs::domainmodel__instantiation(instance):
    assert isinstance(instance, abs::DomainModel_)
