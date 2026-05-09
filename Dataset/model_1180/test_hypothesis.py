import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    HelperParameter,
    gbind::dsl::BaseHelper,
    gbind::dsl::ConceptFeatureRef,
    ConceptFeatureRef,
    Metaclass,
    gbind::dsl::ConcreteMetaclass,
    gbind::dsl::ConceptMetaclass,
    dsl::gbind::EClass,
    VirtualFeature,
    gbind::dsl::VirtualAttribute,
    gbind::dsl::VirtualReference,
    gbind::dsl::VirtualFeature,
    VirtualAttribute,
    VirtualReference,
    gbind::dsl::VirtualMetaclass,
    BaseFeatureBinding,
    gbind::dsl::OclFeatureBinding,
    gbind::dsl::RenamingFeatureBinding,
    ConcreteReferencDeclaringVar,
    BindingModel,
    gbind::dsl::ConceptBinding,
    OclModelElement,
    gbind::dsl::Metaclass,
    gbind::dsl::BindingOptions,
    BindingOptions,
    MetamodelDeclaration,
    VirtualMetaclass,
    ConcreteMetaclass,
    ConceptMetaclass,
    BaseHelper,
    gbind::dsl::LocalHelper,
    gbind::dsl::ConceptHelper,
    ConceptBinding,
    gbind::dsl::VirtualClassBinding,
    gbind::dsl::BaseFeatureBinding,
    gbind::dsl::ClassBinding,
    gbind::dsl::IntermediateClassBinding,
    gbind::dsl::BindingModel,
    OclInstanceModel,
    OclFeature,
    Parameter,
    gbind::simpleocl::Operation,
    gbind::simpleocl::Attribute,
    OclFeatureDefinition,
    OclModel,
    gbind::simpleocl::OclInstanceModel,
    gbind::simpleocl::OclMetamodel,
    TupleType,
    NumericType,
    gbind::simpleocl::RealType,
    gbind::simpleocl::IntegerType,
    Primitive,
    gbind::simpleocl::NumericType,
    gbind::simpleocl::BooleanType,
    gbind::simpleocl::StringType,
    LambdaType,
    TupleTypeAttribute,
    CollectionType,
    gbind::simpleocl::BagType,
    gbind::simpleocl::SequenceType,
    gbind::simpleocl::OrderedSetType,
    gbind::simpleocl::SetType,
    MapType,
    OclContextDefinition,
    IterateExp,
    VariableExp,
    gbind::simpleocl::LambdaCallExp,
    Iterator,
    StaticPropertyCallExp,
    StaticPropertyCall,
    gbind::simpleocl::StaticOperationCall,
    gbind::simpleocl::StaticNavigationOrAttributeCall,
    PropertyCall,
    gbind::simpleocl::NavigationOrAttributeCall,
    gbind::simpleocl::OperationCall,
    gbind::simpleocl::LoopExp,
    NumericExp,
    gbind::simpleocl::RealExp,
    PrimitiveExp,
    gbind::simpleocl::BooleanExp,
    gbind::simpleocl::NumericExp,
    gbind::simpleocl::StringExp,
    MapExp,
    MapElement,
    TupleExp,
    TuplePart,
    gbind::simpleocl::IntegerExp,
    ModuleElement,
    gbind::simpleocl::OclFeatureDefinition,
    Import,
    OclMetamodel,
    gbind::dsl::MetamodelDeclaration,
    NamedElement,
    gbind::simpleocl::OclFeature,
    gbind::simpleocl::OclModel,
    gbind::simpleocl::Module,
    VariableDeclaration,
    gbind::simpleocl::Iterator,
    gbind::dsl::ConcreteReferencDeclaringVar,
    gbind::dsl::HelperParameter,
    gbind::simpleocl::Parameter,
    gbind::simpleocl::LocalVariable,
    OclExpression,
    gbind::simpleocl::BraceExp,
    gbind::simpleocl::CollectionExp,
    gbind::simpleocl::MapExp,
    gbind::simpleocl::SuperExp,
    gbind::simpleocl::StaticPropertyCallExp,
    gbind::simpleocl::LetExp,
    gbind::simpleocl::EnvExp,
    gbind::simpleocl::IfExp,
    gbind::simpleocl::OperatorCallExp,
    gbind::simpleocl::SelfExp,
    gbind::simpleocl::PrimitiveExp,
    gbind::simpleocl::OclUndefinedExp,
    gbind::simpleocl::OclModelElementExp,
    gbind::simpleocl::PropertyCallExp,
    gbind::simpleocl::TupleExp,
    gbind::simpleocl::EnumLiteralExp,
    gbind::simpleocl::VariableExp,
    OperatorCallExp,
    gbind::simpleocl::IntOpCallExp,
    gbind::simpleocl::EqOpCallExp,
    gbind::simpleocl::RelOpCallExp,
    gbind::simpleocl::NotOpCallExp,
    gbind::simpleocl::MulOpCallExp,
    gbind::simpleocl::AddOpCallExp,
    Attribute,
    Operation,
    LocalVariable,
    gbind::simpleocl::TuplePart,
    OperationCall,
    gbind::simpleocl::CollectionOperationCall,
    LoopExp,
    gbind::simpleocl::IterateExp,
    gbind::simpleocl::IteratorExp,
    LetExp,
    CollectionExp,
    gbind::simpleocl::BagExp,
    gbind::simpleocl::SetExp,
    gbind::simpleocl::OrderedSetExp,
    gbind::simpleocl::SequenceExp,
    PropertyCallExp,
    IfExp,
    OclType,
    gbind::simpleocl::TupleType,
    gbind::simpleocl::CollectionType,
    gbind::simpleocl::Primitive,
    gbind::simpleocl::OclModelElement,
    gbind::simpleocl::OclAnyType,
    gbind::simpleocl::LambdaType,
    gbind::simpleocl::MapType,
    gbind::simpleocl::EnvType,
    gbind::simpleocl::Import,
    Module,
    LocatedElement,
    gbind::simpleocl::PropertyCall,
    gbind::simpleocl::OclContextDefinition,
    gbind::simpleocl::TupleTypeAttribute,
    gbind::simpleocl::OclType,
    gbind::simpleocl::ModuleElement,
    gbind::simpleocl::MapElement,
    gbind::simpleocl::VariableDeclaration,
    gbind::simpleocl::StaticPropertyCall,
    gbind::simpleocl::OclExpression,
    gbind::simpleocl::NamedElement,
    gbind::simpleocl::LocatedElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_helperparameter_is_not_abstract():
    assert not inspect.isabstract(HelperParameter)


def test_helperparameter_constructor_exists():
    assert callable(HelperParameter.__init__)


def test_helperparameter_constructor_args():
    sig = inspect.signature(HelperParameter.__init__)
    params = list(sig.parameters.keys())



def test_gbind::dsl::basehelper_is_not_abstract():
    assert not inspect.isabstract(gbind::dsl::BaseHelper)


def test_gbind::dsl::basehelper_constructor_exists():
    assert callable(gbind::dsl::BaseHelper.__init__)


def test_gbind::dsl::basehelper_constructor_args():
    sig = inspect.signature(gbind::dsl::BaseHelper.__init__)
    params = list(sig.parameters.keys())
    assert "feature" in params, "Missing parameter 'feature'"

def test_gbind::dsl::basehelper_has_feature():
    assert hasattr(gbind::dsl::BaseHelper, "feature")
    descriptor = None
    for klass in gbind::dsl::BaseHelper.__mro__:
        if "feature" in klass.__dict__:
            descriptor = klass.__dict__["feature"]
            break
    assert isinstance(descriptor, property)



def test_gbind::dsl::conceptfeatureref_is_not_abstract():
    assert not inspect.isabstract(gbind::dsl::ConceptFeatureRef)


def test_gbind::dsl::conceptfeatureref_constructor_exists():
    assert callable(gbind::dsl::ConceptFeatureRef.__init__)


def test_gbind::dsl::conceptfeatureref_constructor_args():
    sig = inspect.signature(gbind::dsl::ConceptFeatureRef.__init__)
    params = list(sig.parameters.keys())
    assert "featureName" in params, "Missing parameter 'featureName'"

def test_gbind::dsl::conceptfeatureref_has_featureName():
    assert hasattr(gbind::dsl::ConceptFeatureRef, "featureName")
    descriptor = None
    for klass in gbind::dsl::ConceptFeatureRef.__mro__:
        if "featureName" in klass.__dict__:
            descriptor = klass.__dict__["featureName"]
            break
    assert isinstance(descriptor, property)



def test_conceptfeatureref_is_not_abstract():
    assert not inspect.isabstract(ConceptFeatureRef)


def test_conceptfeatureref_constructor_exists():
    assert callable(ConceptFeatureRef.__init__)


def test_conceptfeatureref_constructor_args():
    sig = inspect.signature(ConceptFeatureRef.__init__)
    params = list(sig.parameters.keys())



def test_metaclass_is_not_abstract():
    assert not inspect.isabstract(Metaclass)


def test_metaclass_constructor_exists():
    assert callable(Metaclass.__init__)


def test_metaclass_constructor_args():
    sig = inspect.signature(Metaclass.__init__)
    params = list(sig.parameters.keys())



def test_gbind::dsl::concretemetaclass_is_not_abstract():
    assert not inspect.isabstract(gbind::dsl::ConcreteMetaclass)


def test_gbind::dsl::concretemetaclass_constructor_exists():
    assert callable(gbind::dsl::ConcreteMetaclass.__init__)


def test_gbind::dsl::concretemetaclass_constructor_args():
    sig = inspect.signature(gbind::dsl::ConcreteMetaclass.__init__)
    params = list(sig.parameters.keys())



def test_gbind::dsl::conceptmetaclass_is_not_abstract():
    assert not inspect.isabstract(gbind::dsl::ConceptMetaclass)


def test_gbind::dsl::conceptmetaclass_constructor_exists():
    assert callable(gbind::dsl::ConceptMetaclass.__init__)


def test_gbind::dsl::conceptmetaclass_constructor_args():
    sig = inspect.signature(gbind::dsl::ConceptMetaclass.__init__)
    params = list(sig.parameters.keys())



def test_dsl::gbind::eclass_is_not_abstract():
    assert not inspect.isabstract(dsl::gbind::EClass)


def test_dsl::gbind::eclass_constructor_exists():
    assert callable(dsl::gbind::EClass.__init__)


def test_dsl::gbind::eclass_constructor_args():
    sig = inspect.signature(dsl::gbind::EClass.__init__)
    params = list(sig.parameters.keys())



def test_virtualfeature_is_not_abstract():
    assert not inspect.isabstract(VirtualFeature)


def test_virtualfeature_constructor_exists():
    assert callable(VirtualFeature.__init__)


def test_virtualfeature_constructor_args():
    sig = inspect.signature(VirtualFeature.__init__)
    params = list(sig.parameters.keys())



def test_gbind::dsl::virtualattribute_is_not_abstract():
    assert not inspect.isabstract(gbind::dsl::VirtualAttribute)


def test_gbind::dsl::virtualattribute_constructor_exists():
    assert callable(gbind::dsl::VirtualAttribute.__init__)


def test_gbind::dsl::virtualattribute_constructor_args():
    sig = inspect.signature(gbind::dsl::VirtualAttribute.__init__)
    params = list(sig.parameters.keys())



def test_gbind::dsl::virtualreference_is_not_abstract():
    assert not inspect.isabstract(gbind::dsl::VirtualReference)


def test_gbind::dsl::virtualreference_constructor_exists():
    assert callable(gbind::dsl::VirtualReference.__init__)


def test_gbind::dsl::virtualreference_constructor_args():
    sig = inspect.signature(gbind::dsl::VirtualReference.__init__)
    params = list(sig.parameters.keys())



def test_gbind::dsl::virtualfeature_is_not_abstract():
    assert not inspect.isabstract(gbind::dsl::VirtualFeature)


def test_gbind::dsl::virtualfeature_constructor_exists():
    assert callable(gbind::dsl::VirtualFeature.__init__)


def test_gbind::dsl::virtualfeature_constructor_args():
    sig = inspect.signature(gbind::dsl::VirtualFeature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gbind::dsl::virtualfeature_has_name():
    assert hasattr(gbind::dsl::VirtualFeature, "name")
    descriptor = None
    for klass in gbind::dsl::VirtualFeature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_virtualattribute_is_not_abstract():
    assert not inspect.isabstract(VirtualAttribute)


def test_virtualattribute_constructor_exists():
    assert callable(VirtualAttribute.__init__)


def test_virtualattribute_constructor_args():
    sig = inspect.signature(VirtualAttribute.__init__)
    params = list(sig.parameters.keys())



def test_virtualreference_is_not_abstract():
    assert not inspect.isabstract(VirtualReference)


def test_virtualreference_constructor_exists():
    assert callable(VirtualReference.__init__)


def test_virtualreference_constructor_args():
    sig = inspect.signature(VirtualReference.__init__)
    params = list(sig.parameters.keys())



def test_gbind::dsl::virtualmetaclass_is_not_abstract():
    assert not inspect.isabstract(gbind::dsl::VirtualMetaclass)


def test_gbind::dsl::virtualmetaclass_constructor_exists():
    assert callable(gbind::dsl::VirtualMetaclass.__init__)


def test_gbind::dsl::virtualmetaclass_constructor_args():
    sig = inspect.signature(gbind::dsl::VirtualMetaclass.__init__)
    params = list(sig.parameters.keys())



def test_basefeaturebinding_is_not_abstract():
    assert not inspect.isabstract(BaseFeatureBinding)


def test_basefeaturebinding_constructor_exists():
    assert callable(BaseFeatureBinding.__init__)


def test_basefeaturebinding_constructor_args():
    sig = inspect.signature(BaseFeatureBinding.__init__)
    params = list(sig.parameters.keys())



def test_gbind::dsl::oclfeaturebinding_is_not_abstract():
    assert not inspect.isabstract(gbind::dsl::OclFeatureBinding)


def test_gbind::dsl::oclfeaturebinding_constructor_exists():
    assert callable(gbind::dsl::OclFeatureBinding.__init__)


def test_gbind::dsl::oclfeaturebinding_constructor_args():
    sig = inspect.signature(gbind::dsl::OclFeatureBinding.__init__)
    params = list(sig.parameters.keys())



def test_gbind::dsl::renamingfeaturebinding_is_not_abstract():
    assert not inspect.isabstract(gbind::dsl::RenamingFeatureBinding)


def test_gbind::dsl::renamingfeaturebinding_constructor_exists():
    assert callable(gbind::dsl::RenamingFeatureBinding.__init__)


def test_gbind::dsl::renamingfeaturebinding_constructor_args():
    sig = inspect.signature(gbind::dsl::RenamingFeatureBinding.__init__)
    params = list(sig.parameters.keys())
    assert "concreteFeature" in params, "Missing parameter 'concreteFeature'"

def test_gbind::dsl::renamingfeaturebinding_has_concreteFeature():
    assert hasattr(gbind::dsl::RenamingFeatureBinding, "concreteFeature")
    descriptor = None
    for klass in gbind::dsl::RenamingFeatureBinding.__mro__:
        if "concreteFeature" in klass.__dict__:
            descriptor = klass.__dict__["concreteFeature"]
            break
    assert isinstance(descriptor, property)



def test_concretereferencdeclaringvar_is_not_abstract():
    assert not inspect.isabstract(ConcreteReferencDeclaringVar)


def test_concretereferencdeclaringvar_constructor_exists():
    assert callable(ConcreteReferencDeclaringVar.__init__)


def test_concretereferencdeclaringvar_constructor_args():
    sig = inspect.signature(ConcreteReferencDeclaringVar.__init__)
    params = list(sig.parameters.keys())



def test_bindingmodel_is_not_abstract():
    assert not inspect.isabstract(BindingModel)


def test_bindingmodel_constructor_exists():
    assert callable(BindingModel.__init__)


def test_bindingmodel_constructor_args():
    sig = inspect.signature(BindingModel.__init__)
    params = list(sig.parameters.keys())



def test_gbind::dsl::conceptbinding_is_not_abstract():
    assert not inspect.isabstract(gbind::dsl::ConceptBinding)


def test_gbind::dsl::conceptbinding_constructor_exists():
    assert callable(gbind::dsl::ConceptBinding.__init__)


def test_gbind::dsl::conceptbinding_constructor_args():
    sig = inspect.signature(gbind::dsl::ConceptBinding.__init__)
    params = list(sig.parameters.keys())
    assert "debugName" in params, "Missing parameter 'debugName'"

def test_gbind::dsl::conceptbinding_has_debugName():
    assert hasattr(gbind::dsl::ConceptBinding, "debugName")
    descriptor = None
    for klass in gbind::dsl::ConceptBinding.__mro__:
        if "debugName" in klass.__dict__:
            descriptor = klass.__dict__["debugName"]
            break
    assert isinstance(descriptor, property)



def test_oclmodelelement_is_not_abstract():
    assert not inspect.isabstract(OclModelElement)


def test_oclmodelelement_constructor_exists():
    assert callable(OclModelElement.__init__)


def test_oclmodelelement_constructor_args():
    sig = inspect.signature(OclModelElement.__init__)
    params = list(sig.parameters.keys())



def test_gbind::dsl::metaclass_is_not_abstract():
    assert not inspect.isabstract(gbind::dsl::Metaclass)


def test_gbind::dsl::metaclass_constructor_exists():
    assert callable(gbind::dsl::Metaclass.__init__)


def test_gbind::dsl::metaclass_constructor_args():
    sig = inspect.signature(gbind::dsl::Metaclass.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gbind::dsl::metaclass_has_name():
    assert hasattr(gbind::dsl::Metaclass, "name")
    descriptor = None
    for klass in gbind::dsl::Metaclass.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gbind::dsl::bindingoptions_is_not_abstract():
    assert not inspect.isabstract(gbind::dsl::BindingOptions)


def test_gbind::dsl::bindingoptions_constructor_exists():
    assert callable(gbind::dsl::BindingOptions.__init__)


def test_gbind::dsl::bindingoptions_constructor_args():
    sig = inspect.signature(gbind::dsl::BindingOptions.__init__)
    params = list(sig.parameters.keys())
    assert "enableClassMerge" in params, "Missing parameter 'enableClassMerge'"

def test_gbind::dsl::bindingoptions_has_enableClassMerge():
    assert hasattr(gbind::dsl::BindingOptions, "enableClassMerge")
    descriptor = None
    for klass in gbind::dsl::BindingOptions.__mro__:
        if "enableClassMerge" in klass.__dict__:
            descriptor = klass.__dict__["enableClassMerge"]
            break
    assert isinstance(descriptor, property)



def test_bindingoptions_is_not_abstract():
    assert not inspect.isabstract(BindingOptions)


def test_bindingoptions_constructor_exists():
    assert callable(BindingOptions.__init__)


def test_bindingoptions_constructor_args():
    sig = inspect.signature(BindingOptions.__init__)
    params = list(sig.parameters.keys())



def test_metamodeldeclaration_is_not_abstract():
    assert not inspect.isabstract(MetamodelDeclaration)


def test_metamodeldeclaration_constructor_exists():
    assert callable(MetamodelDeclaration.__init__)


def test_metamodeldeclaration_constructor_args():
    sig = inspect.signature(MetamodelDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_virtualmetaclass_is_not_abstract():
    assert not inspect.isabstract(VirtualMetaclass)


def test_virtualmetaclass_constructor_exists():
    assert callable(VirtualMetaclass.__init__)


def test_virtualmetaclass_constructor_args():
    sig = inspect.signature(VirtualMetaclass.__init__)
    params = list(sig.parameters.keys())



def test_concretemetaclass_is_not_abstract():
    assert not inspect.isabstract(ConcreteMetaclass)


def test_concretemetaclass_constructor_exists():
    assert callable(ConcreteMetaclass.__init__)


def test_concretemetaclass_constructor_args():
    sig = inspect.signature(ConcreteMetaclass.__init__)
    params = list(sig.parameters.keys())



def test_conceptmetaclass_is_not_abstract():
    assert not inspect.isabstract(ConceptMetaclass)


def test_conceptmetaclass_constructor_exists():
    assert callable(ConceptMetaclass.__init__)


def test_conceptmetaclass_constructor_args():
    sig = inspect.signature(ConceptMetaclass.__init__)
    params = list(sig.parameters.keys())



def test_basehelper_is_not_abstract():
    assert not inspect.isabstract(BaseHelper)


def test_basehelper_constructor_exists():
    assert callable(BaseHelper.__init__)


def test_basehelper_constructor_args():
    sig = inspect.signature(BaseHelper.__init__)
    params = list(sig.parameters.keys())



def test_gbind::dsl::localhelper_is_not_abstract():
    assert not inspect.isabstract(gbind::dsl::LocalHelper)


def test_gbind::dsl::localhelper_constructor_exists():
    assert callable(gbind::dsl::LocalHelper.__init__)


def test_gbind::dsl::localhelper_constructor_args():
    sig = inspect.signature(gbind::dsl::LocalHelper.__init__)
    params = list(sig.parameters.keys())



def test_gbind::dsl::concepthelper_is_not_abstract():
    assert not inspect.isabstract(gbind::dsl::ConceptHelper)


def test_gbind::dsl::concepthelper_constructor_exists():
    assert callable(gbind::dsl::ConceptHelper.__init__)


def test_gbind::dsl::concepthelper_constructor_args():
    sig = inspect.signature(gbind::dsl::ConceptHelper.__init__)
    params = list(sig.parameters.keys())



def test_conceptbinding_is_not_abstract():
    assert not inspect.isabstract(ConceptBinding)


def test_conceptbinding_constructor_exists():
    assert callable(ConceptBinding.__init__)


def test_conceptbinding_constructor_args():
    sig = inspect.signature(ConceptBinding.__init__)
    params = list(sig.parameters.keys())



def test_gbind::dsl::virtualclassbinding_is_not_abstract():
    assert not inspect.isabstract(gbind::dsl::VirtualClassBinding)


def test_gbind::dsl::virtualclassbinding_constructor_exists():
    assert callable(gbind::dsl::VirtualClassBinding.__init__)


def test_gbind::dsl::virtualclassbinding_constructor_args():
    sig = inspect.signature(gbind::dsl::VirtualClassBinding.__init__)
    params = list(sig.parameters.keys())



def test_gbind::dsl::basefeaturebinding_is_not_abstract():
    assert not inspect.isabstract(gbind::dsl::BaseFeatureBinding)


def test_gbind::dsl::basefeaturebinding_constructor_exists():
    assert callable(gbind::dsl::BaseFeatureBinding.__init__)


def test_gbind::dsl::basefeaturebinding_constructor_args():
    sig = inspect.signature(gbind::dsl::BaseFeatureBinding.__init__)
    params = list(sig.parameters.keys())
    assert "conceptFeature" in params, "Missing parameter 'conceptFeature'"

def test_gbind::dsl::basefeaturebinding_has_conceptFeature():
    assert hasattr(gbind::dsl::BaseFeatureBinding, "conceptFeature")
    descriptor = None
    for klass in gbind::dsl::BaseFeatureBinding.__mro__:
        if "conceptFeature" in klass.__dict__:
            descriptor = klass.__dict__["conceptFeature"]
            break
    assert isinstance(descriptor, property)



def test_gbind::dsl::classbinding_is_not_abstract():
    assert not inspect.isabstract(gbind::dsl::ClassBinding)


def test_gbind::dsl::classbinding_constructor_exists():
    assert callable(gbind::dsl::ClassBinding.__init__)


def test_gbind::dsl::classbinding_constructor_args():
    sig = inspect.signature(gbind::dsl::ClassBinding.__init__)
    params = list(sig.parameters.keys())



def test_gbind::dsl::intermediateclassbinding_is_not_abstract():
    assert not inspect.isabstract(gbind::dsl::IntermediateClassBinding)


def test_gbind::dsl::intermediateclassbinding_constructor_exists():
    assert callable(gbind::dsl::IntermediateClassBinding.__init__)


def test_gbind::dsl::intermediateclassbinding_constructor_args():
    sig = inspect.signature(gbind::dsl::IntermediateClassBinding.__init__)
    params = list(sig.parameters.keys())
    assert "conceptReferenceName" in params, "Missing parameter 'conceptReferenceName'"

def test_gbind::dsl::intermediateclassbinding_has_conceptReferenceName():
    assert hasattr(gbind::dsl::IntermediateClassBinding, "conceptReferenceName")
    descriptor = None
    for klass in gbind::dsl::IntermediateClassBinding.__mro__:
        if "conceptReferenceName" in klass.__dict__:
            descriptor = klass.__dict__["conceptReferenceName"]
            break
    assert isinstance(descriptor, property)



def test_gbind::dsl::bindingmodel_is_not_abstract():
    assert not inspect.isabstract(gbind::dsl::BindingModel)


def test_gbind::dsl::bindingmodel_constructor_exists():
    assert callable(gbind::dsl::BindingModel.__init__)


def test_gbind::dsl::bindingmodel_constructor_args():
    sig = inspect.signature(gbind::dsl::BindingModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gbind::dsl::bindingmodel_has_name():
    assert hasattr(gbind::dsl::BindingModel, "name")
    descriptor = None
    for klass in gbind::dsl::BindingModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_oclinstancemodel_is_not_abstract():
    assert not inspect.isabstract(OclInstanceModel)


def test_oclinstancemodel_constructor_exists():
    assert callable(OclInstanceModel.__init__)


def test_oclinstancemodel_constructor_args():
    sig = inspect.signature(OclInstanceModel.__init__)
    params = list(sig.parameters.keys())



def test_oclfeature_is_not_abstract():
    assert not inspect.isabstract(OclFeature)


def test_oclfeature_constructor_exists():
    assert callable(OclFeature.__init__)


def test_oclfeature_constructor_args():
    sig = inspect.signature(OclFeature.__init__)
    params = list(sig.parameters.keys())



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::operation_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::Operation)


def test_gbind::simpleocl::operation_constructor_exists():
    assert callable(gbind::simpleocl::Operation.__init__)


def test_gbind::simpleocl::operation_constructor_args():
    sig = inspect.signature(gbind::simpleocl::Operation.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::attribute_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::Attribute)


def test_gbind::simpleocl::attribute_constructor_exists():
    assert callable(gbind::simpleocl::Attribute.__init__)


def test_gbind::simpleocl::attribute_constructor_args():
    sig = inspect.signature(gbind::simpleocl::Attribute.__init__)
    params = list(sig.parameters.keys())



def test_oclfeaturedefinition_is_not_abstract():
    assert not inspect.isabstract(OclFeatureDefinition)


def test_oclfeaturedefinition_constructor_exists():
    assert callable(OclFeatureDefinition.__init__)


def test_oclfeaturedefinition_constructor_args():
    sig = inspect.signature(OclFeatureDefinition.__init__)
    params = list(sig.parameters.keys())



def test_oclmodel_is_not_abstract():
    assert not inspect.isabstract(OclModel)


def test_oclmodel_constructor_exists():
    assert callable(OclModel.__init__)


def test_oclmodel_constructor_args():
    sig = inspect.signature(OclModel.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::oclinstancemodel_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::OclInstanceModel)


def test_gbind::simpleocl::oclinstancemodel_constructor_exists():
    assert callable(gbind::simpleocl::OclInstanceModel.__init__)


def test_gbind::simpleocl::oclinstancemodel_constructor_args():
    sig = inspect.signature(gbind::simpleocl::OclInstanceModel.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::oclmetamodel_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::OclMetamodel)


def test_gbind::simpleocl::oclmetamodel_constructor_exists():
    assert callable(gbind::simpleocl::OclMetamodel.__init__)


def test_gbind::simpleocl::oclmetamodel_constructor_args():
    sig = inspect.signature(gbind::simpleocl::OclMetamodel.__init__)
    params = list(sig.parameters.keys())
    assert "uri" in params, "Missing parameter 'uri'"

def test_gbind::simpleocl::oclmetamodel_has_uri():
    assert hasattr(gbind::simpleocl::OclMetamodel, "uri")
    descriptor = None
    for klass in gbind::simpleocl::OclMetamodel.__mro__:
        if "uri" in klass.__dict__:
            descriptor = klass.__dict__["uri"]
            break
    assert isinstance(descriptor, property)



def test_tupletype_is_not_abstract():
    assert not inspect.isabstract(TupleType)


def test_tupletype_constructor_exists():
    assert callable(TupleType.__init__)


def test_tupletype_constructor_args():
    sig = inspect.signature(TupleType.__init__)
    params = list(sig.parameters.keys())



def test_numerictype_is_not_abstract():
    assert not inspect.isabstract(NumericType)


def test_numerictype_constructor_exists():
    assert callable(NumericType.__init__)


def test_numerictype_constructor_args():
    sig = inspect.signature(NumericType.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::realtype_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::RealType)


def test_gbind::simpleocl::realtype_constructor_exists():
    assert callable(gbind::simpleocl::RealType.__init__)


def test_gbind::simpleocl::realtype_constructor_args():
    sig = inspect.signature(gbind::simpleocl::RealType.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::integertype_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::IntegerType)


def test_gbind::simpleocl::integertype_constructor_exists():
    assert callable(gbind::simpleocl::IntegerType.__init__)


def test_gbind::simpleocl::integertype_constructor_args():
    sig = inspect.signature(gbind::simpleocl::IntegerType.__init__)
    params = list(sig.parameters.keys())



def test_primitive_is_not_abstract():
    assert not inspect.isabstract(Primitive)


def test_primitive_constructor_exists():
    assert callable(Primitive.__init__)


def test_primitive_constructor_args():
    sig = inspect.signature(Primitive.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::numerictype_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::NumericType)


def test_gbind::simpleocl::numerictype_constructor_exists():
    assert callable(gbind::simpleocl::NumericType.__init__)


def test_gbind::simpleocl::numerictype_constructor_args():
    sig = inspect.signature(gbind::simpleocl::NumericType.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::booleantype_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::BooleanType)


def test_gbind::simpleocl::booleantype_constructor_exists():
    assert callable(gbind::simpleocl::BooleanType.__init__)


def test_gbind::simpleocl::booleantype_constructor_args():
    sig = inspect.signature(gbind::simpleocl::BooleanType.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::stringtype_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::StringType)


def test_gbind::simpleocl::stringtype_constructor_exists():
    assert callable(gbind::simpleocl::StringType.__init__)


def test_gbind::simpleocl::stringtype_constructor_args():
    sig = inspect.signature(gbind::simpleocl::StringType.__init__)
    params = list(sig.parameters.keys())



def test_lambdatype_is_not_abstract():
    assert not inspect.isabstract(LambdaType)


def test_lambdatype_constructor_exists():
    assert callable(LambdaType.__init__)


def test_lambdatype_constructor_args():
    sig = inspect.signature(LambdaType.__init__)
    params = list(sig.parameters.keys())



def test_tupletypeattribute_is_not_abstract():
    assert not inspect.isabstract(TupleTypeAttribute)


def test_tupletypeattribute_constructor_exists():
    assert callable(TupleTypeAttribute.__init__)


def test_tupletypeattribute_constructor_args():
    sig = inspect.signature(TupleTypeAttribute.__init__)
    params = list(sig.parameters.keys())



def test_collectiontype_is_not_abstract():
    assert not inspect.isabstract(CollectionType)


def test_collectiontype_constructor_exists():
    assert callable(CollectionType.__init__)


def test_collectiontype_constructor_args():
    sig = inspect.signature(CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::bagtype_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::BagType)


def test_gbind::simpleocl::bagtype_constructor_exists():
    assert callable(gbind::simpleocl::BagType.__init__)


def test_gbind::simpleocl::bagtype_constructor_args():
    sig = inspect.signature(gbind::simpleocl::BagType.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::sequencetype_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::SequenceType)


def test_gbind::simpleocl::sequencetype_constructor_exists():
    assert callable(gbind::simpleocl::SequenceType.__init__)


def test_gbind::simpleocl::sequencetype_constructor_args():
    sig = inspect.signature(gbind::simpleocl::SequenceType.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::orderedsettype_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::OrderedSetType)


def test_gbind::simpleocl::orderedsettype_constructor_exists():
    assert callable(gbind::simpleocl::OrderedSetType.__init__)


def test_gbind::simpleocl::orderedsettype_constructor_args():
    sig = inspect.signature(gbind::simpleocl::OrderedSetType.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::settype_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::SetType)


def test_gbind::simpleocl::settype_constructor_exists():
    assert callable(gbind::simpleocl::SetType.__init__)


def test_gbind::simpleocl::settype_constructor_args():
    sig = inspect.signature(gbind::simpleocl::SetType.__init__)
    params = list(sig.parameters.keys())



def test_maptype_is_not_abstract():
    assert not inspect.isabstract(MapType)


def test_maptype_constructor_exists():
    assert callable(MapType.__init__)


def test_maptype_constructor_args():
    sig = inspect.signature(MapType.__init__)
    params = list(sig.parameters.keys())



def test_oclcontextdefinition_is_not_abstract():
    assert not inspect.isabstract(OclContextDefinition)


def test_oclcontextdefinition_constructor_exists():
    assert callable(OclContextDefinition.__init__)


def test_oclcontextdefinition_constructor_args():
    sig = inspect.signature(OclContextDefinition.__init__)
    params = list(sig.parameters.keys())



def test_iterateexp_is_not_abstract():
    assert not inspect.isabstract(IterateExp)


def test_iterateexp_constructor_exists():
    assert callable(IterateExp.__init__)


def test_iterateexp_constructor_args():
    sig = inspect.signature(IterateExp.__init__)
    params = list(sig.parameters.keys())



def test_variableexp_is_not_abstract():
    assert not inspect.isabstract(VariableExp)


def test_variableexp_constructor_exists():
    assert callable(VariableExp.__init__)


def test_variableexp_constructor_args():
    sig = inspect.signature(VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::lambdacallexp_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::LambdaCallExp)


def test_gbind::simpleocl::lambdacallexp_constructor_exists():
    assert callable(gbind::simpleocl::LambdaCallExp.__init__)


def test_gbind::simpleocl::lambdacallexp_constructor_args():
    sig = inspect.signature(gbind::simpleocl::LambdaCallExp.__init__)
    params = list(sig.parameters.keys())



def test_iterator_is_not_abstract():
    assert not inspect.isabstract(Iterator)


def test_iterator_constructor_exists():
    assert callable(Iterator.__init__)


def test_iterator_constructor_args():
    sig = inspect.signature(Iterator.__init__)
    params = list(sig.parameters.keys())



def test_staticpropertycallexp_is_not_abstract():
    assert not inspect.isabstract(StaticPropertyCallExp)


def test_staticpropertycallexp_constructor_exists():
    assert callable(StaticPropertyCallExp.__init__)


def test_staticpropertycallexp_constructor_args():
    sig = inspect.signature(StaticPropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_staticpropertycall_is_not_abstract():
    assert not inspect.isabstract(StaticPropertyCall)


def test_staticpropertycall_constructor_exists():
    assert callable(StaticPropertyCall.__init__)


def test_staticpropertycall_constructor_args():
    sig = inspect.signature(StaticPropertyCall.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::staticoperationcall_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::StaticOperationCall)


def test_gbind::simpleocl::staticoperationcall_constructor_exists():
    assert callable(gbind::simpleocl::StaticOperationCall.__init__)


def test_gbind::simpleocl::staticoperationcall_constructor_args():
    sig = inspect.signature(gbind::simpleocl::StaticOperationCall.__init__)
    params = list(sig.parameters.keys())
    assert "operationName" in params, "Missing parameter 'operationName'"

def test_gbind::simpleocl::staticoperationcall_has_operationName():
    assert hasattr(gbind::simpleocl::StaticOperationCall, "operationName")
    descriptor = None
    for klass in gbind::simpleocl::StaticOperationCall.__mro__:
        if "operationName" in klass.__dict__:
            descriptor = klass.__dict__["operationName"]
            break
    assert isinstance(descriptor, property)



def test_gbind::simpleocl::staticnavigationorattributecall_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::StaticNavigationOrAttributeCall)


def test_gbind::simpleocl::staticnavigationorattributecall_constructor_exists():
    assert callable(gbind::simpleocl::StaticNavigationOrAttributeCall.__init__)


def test_gbind::simpleocl::staticnavigationorattributecall_constructor_args():
    sig = inspect.signature(gbind::simpleocl::StaticNavigationOrAttributeCall.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gbind::simpleocl::staticnavigationorattributecall_has_name():
    assert hasattr(gbind::simpleocl::StaticNavigationOrAttributeCall, "name")
    descriptor = None
    for klass in gbind::simpleocl::StaticNavigationOrAttributeCall.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_propertycall_is_not_abstract():
    assert not inspect.isabstract(PropertyCall)


def test_propertycall_constructor_exists():
    assert callable(PropertyCall.__init__)


def test_propertycall_constructor_args():
    sig = inspect.signature(PropertyCall.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::navigationorattributecall_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::NavigationOrAttributeCall)


def test_gbind::simpleocl::navigationorattributecall_constructor_exists():
    assert callable(gbind::simpleocl::NavigationOrAttributeCall.__init__)


def test_gbind::simpleocl::navigationorattributecall_constructor_args():
    sig = inspect.signature(gbind::simpleocl::NavigationOrAttributeCall.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gbind::simpleocl::navigationorattributecall_has_name():
    assert hasattr(gbind::simpleocl::NavigationOrAttributeCall, "name")
    descriptor = None
    for klass in gbind::simpleocl::NavigationOrAttributeCall.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gbind::simpleocl::operationcall_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::OperationCall)


def test_gbind::simpleocl::operationcall_constructor_exists():
    assert callable(gbind::simpleocl::OperationCall.__init__)


def test_gbind::simpleocl::operationcall_constructor_args():
    sig = inspect.signature(gbind::simpleocl::OperationCall.__init__)
    params = list(sig.parameters.keys())
    assert "operationName" in params, "Missing parameter 'operationName'"

def test_gbind::simpleocl::operationcall_has_operationName():
    assert hasattr(gbind::simpleocl::OperationCall, "operationName")
    descriptor = None
    for klass in gbind::simpleocl::OperationCall.__mro__:
        if "operationName" in klass.__dict__:
            descriptor = klass.__dict__["operationName"]
            break
    assert isinstance(descriptor, property)



def test_gbind::simpleocl::loopexp_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::LoopExp)


def test_gbind::simpleocl::loopexp_constructor_exists():
    assert callable(gbind::simpleocl::LoopExp.__init__)


def test_gbind::simpleocl::loopexp_constructor_args():
    sig = inspect.signature(gbind::simpleocl::LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_numericexp_is_not_abstract():
    assert not inspect.isabstract(NumericExp)


def test_numericexp_constructor_exists():
    assert callable(NumericExp.__init__)


def test_numericexp_constructor_args():
    sig = inspect.signature(NumericExp.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::realexp_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::RealExp)


def test_gbind::simpleocl::realexp_constructor_exists():
    assert callable(gbind::simpleocl::RealExp.__init__)


def test_gbind::simpleocl::realexp_constructor_args():
    sig = inspect.signature(gbind::simpleocl::RealExp.__init__)
    params = list(sig.parameters.keys())
    assert "realSymbol" in params, "Missing parameter 'realSymbol'"

def test_gbind::simpleocl::realexp_has_realSymbol():
    assert hasattr(gbind::simpleocl::RealExp, "realSymbol")
    descriptor = None
    for klass in gbind::simpleocl::RealExp.__mro__:
        if "realSymbol" in klass.__dict__:
            descriptor = klass.__dict__["realSymbol"]
            break
    assert isinstance(descriptor, property)



def test_primitiveexp_is_not_abstract():
    assert not inspect.isabstract(PrimitiveExp)


def test_primitiveexp_constructor_exists():
    assert callable(PrimitiveExp.__init__)


def test_primitiveexp_constructor_args():
    sig = inspect.signature(PrimitiveExp.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::booleanexp_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::BooleanExp)


def test_gbind::simpleocl::booleanexp_constructor_exists():
    assert callable(gbind::simpleocl::BooleanExp.__init__)


def test_gbind::simpleocl::booleanexp_constructor_args():
    sig = inspect.signature(gbind::simpleocl::BooleanExp.__init__)
    params = list(sig.parameters.keys())
    assert "booleanSymbol" in params, "Missing parameter 'booleanSymbol'"

def test_gbind::simpleocl::booleanexp_has_booleanSymbol():
    assert hasattr(gbind::simpleocl::BooleanExp, "booleanSymbol")
    descriptor = None
    for klass in gbind::simpleocl::BooleanExp.__mro__:
        if "booleanSymbol" in klass.__dict__:
            descriptor = klass.__dict__["booleanSymbol"]
            break
    assert isinstance(descriptor, property)



def test_gbind::simpleocl::numericexp_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::NumericExp)


def test_gbind::simpleocl::numericexp_constructor_exists():
    assert callable(gbind::simpleocl::NumericExp.__init__)


def test_gbind::simpleocl::numericexp_constructor_args():
    sig = inspect.signature(gbind::simpleocl::NumericExp.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::stringexp_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::StringExp)


def test_gbind::simpleocl::stringexp_constructor_exists():
    assert callable(gbind::simpleocl::StringExp.__init__)


def test_gbind::simpleocl::stringexp_constructor_args():
    sig = inspect.signature(gbind::simpleocl::StringExp.__init__)
    params = list(sig.parameters.keys())
    assert "stringSymbol" in params, "Missing parameter 'stringSymbol'"

def test_gbind::simpleocl::stringexp_has_stringSymbol():
    assert hasattr(gbind::simpleocl::StringExp, "stringSymbol")
    descriptor = None
    for klass in gbind::simpleocl::StringExp.__mro__:
        if "stringSymbol" in klass.__dict__:
            descriptor = klass.__dict__["stringSymbol"]
            break
    assert isinstance(descriptor, property)



def test_mapexp_is_not_abstract():
    assert not inspect.isabstract(MapExp)


def test_mapexp_constructor_exists():
    assert callable(MapExp.__init__)


def test_mapexp_constructor_args():
    sig = inspect.signature(MapExp.__init__)
    params = list(sig.parameters.keys())



def test_mapelement_is_not_abstract():
    assert not inspect.isabstract(MapElement)


def test_mapelement_constructor_exists():
    assert callable(MapElement.__init__)


def test_mapelement_constructor_args():
    sig = inspect.signature(MapElement.__init__)
    params = list(sig.parameters.keys())



def test_tupleexp_is_not_abstract():
    assert not inspect.isabstract(TupleExp)


def test_tupleexp_constructor_exists():
    assert callable(TupleExp.__init__)


def test_tupleexp_constructor_args():
    sig = inspect.signature(TupleExp.__init__)
    params = list(sig.parameters.keys())



def test_tuplepart_is_not_abstract():
    assert not inspect.isabstract(TuplePart)


def test_tuplepart_constructor_exists():
    assert callable(TuplePart.__init__)


def test_tuplepart_constructor_args():
    sig = inspect.signature(TuplePart.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::integerexp_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::IntegerExp)


def test_gbind::simpleocl::integerexp_constructor_exists():
    assert callable(gbind::simpleocl::IntegerExp.__init__)


def test_gbind::simpleocl::integerexp_constructor_args():
    sig = inspect.signature(gbind::simpleocl::IntegerExp.__init__)
    params = list(sig.parameters.keys())
    assert "integerSymbol" in params, "Missing parameter 'integerSymbol'"

def test_gbind::simpleocl::integerexp_has_integerSymbol():
    assert hasattr(gbind::simpleocl::IntegerExp, "integerSymbol")
    descriptor = None
    for klass in gbind::simpleocl::IntegerExp.__mro__:
        if "integerSymbol" in klass.__dict__:
            descriptor = klass.__dict__["integerSymbol"]
            break
    assert isinstance(descriptor, property)



def test_moduleelement_is_not_abstract():
    assert not inspect.isabstract(ModuleElement)


def test_moduleelement_constructor_exists():
    assert callable(ModuleElement.__init__)


def test_moduleelement_constructor_args():
    sig = inspect.signature(ModuleElement.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::oclfeaturedefinition_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::OclFeatureDefinition)


def test_gbind::simpleocl::oclfeaturedefinition_constructor_exists():
    assert callable(gbind::simpleocl::OclFeatureDefinition.__init__)


def test_gbind::simpleocl::oclfeaturedefinition_constructor_args():
    sig = inspect.signature(gbind::simpleocl::OclFeatureDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"

def test_gbind::simpleocl::oclfeaturedefinition_has_static():
    assert hasattr(gbind::simpleocl::OclFeatureDefinition, "static")
    descriptor = None
    for klass in gbind::simpleocl::OclFeatureDefinition.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)



def test_import_is_not_abstract():
    assert not inspect.isabstract(Import)


def test_import_constructor_exists():
    assert callable(Import.__init__)


def test_import_constructor_args():
    sig = inspect.signature(Import.__init__)
    params = list(sig.parameters.keys())



def test_oclmetamodel_is_not_abstract():
    assert not inspect.isabstract(OclMetamodel)


def test_oclmetamodel_constructor_exists():
    assert callable(OclMetamodel.__init__)


def test_oclmetamodel_constructor_args():
    sig = inspect.signature(OclMetamodel.__init__)
    params = list(sig.parameters.keys())



def test_gbind::dsl::metamodeldeclaration_is_not_abstract():
    assert not inspect.isabstract(gbind::dsl::MetamodelDeclaration)


def test_gbind::dsl::metamodeldeclaration_constructor_exists():
    assert callable(gbind::dsl::MetamodelDeclaration.__init__)


def test_gbind::dsl::metamodeldeclaration_constructor_args():
    sig = inspect.signature(gbind::dsl::MetamodelDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "metamodelURI" in params, "Missing parameter 'metamodelURI'"

def test_gbind::dsl::metamodeldeclaration_has_metamodelURI():
    assert hasattr(gbind::dsl::MetamodelDeclaration, "metamodelURI")
    descriptor = None
    for klass in gbind::dsl::MetamodelDeclaration.__mro__:
        if "metamodelURI" in klass.__dict__:
            descriptor = klass.__dict__["metamodelURI"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::oclfeature_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::OclFeature)


def test_gbind::simpleocl::oclfeature_constructor_exists():
    assert callable(gbind::simpleocl::OclFeature.__init__)


def test_gbind::simpleocl::oclfeature_constructor_args():
    sig = inspect.signature(gbind::simpleocl::OclFeature.__init__)
    params = list(sig.parameters.keys())
    assert "eq" in params, "Missing parameter 'eq'"

def test_gbind::simpleocl::oclfeature_has_eq():
    assert hasattr(gbind::simpleocl::OclFeature, "eq")
    descriptor = None
    for klass in gbind::simpleocl::OclFeature.__mro__:
        if "eq" in klass.__dict__:
            descriptor = klass.__dict__["eq"]
            break
    assert isinstance(descriptor, property)



def test_gbind::simpleocl::oclmodel_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::OclModel)


def test_gbind::simpleocl::oclmodel_constructor_exists():
    assert callable(gbind::simpleocl::OclModel.__init__)


def test_gbind::simpleocl::oclmodel_constructor_args():
    sig = inspect.signature(gbind::simpleocl::OclModel.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::module_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::Module)


def test_gbind::simpleocl::module_constructor_exists():
    assert callable(gbind::simpleocl::Module.__init__)


def test_gbind::simpleocl::module_constructor_args():
    sig = inspect.signature(gbind::simpleocl::Module.__init__)
    params = list(sig.parameters.keys())



def test_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(VariableDeclaration)


def test_variabledeclaration_constructor_exists():
    assert callable(VariableDeclaration.__init__)


def test_variabledeclaration_constructor_args():
    sig = inspect.signature(VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::iterator_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::Iterator)


def test_gbind::simpleocl::iterator_constructor_exists():
    assert callable(gbind::simpleocl::Iterator.__init__)


def test_gbind::simpleocl::iterator_constructor_args():
    sig = inspect.signature(gbind::simpleocl::Iterator.__init__)
    params = list(sig.parameters.keys())



def test_gbind::dsl::concretereferencdeclaringvar_is_not_abstract():
    assert not inspect.isabstract(gbind::dsl::ConcreteReferencDeclaringVar)


def test_gbind::dsl::concretereferencdeclaringvar_constructor_exists():
    assert callable(gbind::dsl::ConcreteReferencDeclaringVar.__init__)


def test_gbind::dsl::concretereferencdeclaringvar_constructor_args():
    sig = inspect.signature(gbind::dsl::ConcreteReferencDeclaringVar.__init__)
    params = list(sig.parameters.keys())



def test_gbind::dsl::helperparameter_is_not_abstract():
    assert not inspect.isabstract(gbind::dsl::HelperParameter)


def test_gbind::dsl::helperparameter_constructor_exists():
    assert callable(gbind::dsl::HelperParameter.__init__)


def test_gbind::dsl::helperparameter_constructor_args():
    sig = inspect.signature(gbind::dsl::HelperParameter.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::parameter_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::Parameter)


def test_gbind::simpleocl::parameter_constructor_exists():
    assert callable(gbind::simpleocl::Parameter.__init__)


def test_gbind::simpleocl::parameter_constructor_args():
    sig = inspect.signature(gbind::simpleocl::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::localvariable_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::LocalVariable)


def test_gbind::simpleocl::localvariable_constructor_exists():
    assert callable(gbind::simpleocl::LocalVariable.__init__)


def test_gbind::simpleocl::localvariable_constructor_args():
    sig = inspect.signature(gbind::simpleocl::LocalVariable.__init__)
    params = list(sig.parameters.keys())
    assert "eq" in params, "Missing parameter 'eq'"

def test_gbind::simpleocl::localvariable_has_eq():
    assert hasattr(gbind::simpleocl::LocalVariable, "eq")
    descriptor = None
    for klass in gbind::simpleocl::LocalVariable.__mro__:
        if "eq" in klass.__dict__:
            descriptor = klass.__dict__["eq"]
            break
    assert isinstance(descriptor, property)



def test_oclexpression_is_not_abstract():
    assert not inspect.isabstract(OclExpression)


def test_oclexpression_constructor_exists():
    assert callable(OclExpression.__init__)


def test_oclexpression_constructor_args():
    sig = inspect.signature(OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::braceexp_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::BraceExp)


def test_gbind::simpleocl::braceexp_constructor_exists():
    assert callable(gbind::simpleocl::BraceExp.__init__)


def test_gbind::simpleocl::braceexp_constructor_args():
    sig = inspect.signature(gbind::simpleocl::BraceExp.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::collectionexp_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::CollectionExp)


def test_gbind::simpleocl::collectionexp_constructor_exists():
    assert callable(gbind::simpleocl::CollectionExp.__init__)


def test_gbind::simpleocl::collectionexp_constructor_args():
    sig = inspect.signature(gbind::simpleocl::CollectionExp.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::mapexp_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::MapExp)


def test_gbind::simpleocl::mapexp_constructor_exists():
    assert callable(gbind::simpleocl::MapExp.__init__)


def test_gbind::simpleocl::mapexp_constructor_args():
    sig = inspect.signature(gbind::simpleocl::MapExp.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::superexp_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::SuperExp)


def test_gbind::simpleocl::superexp_constructor_exists():
    assert callable(gbind::simpleocl::SuperExp.__init__)


def test_gbind::simpleocl::superexp_constructor_args():
    sig = inspect.signature(gbind::simpleocl::SuperExp.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::staticpropertycallexp_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::StaticPropertyCallExp)


def test_gbind::simpleocl::staticpropertycallexp_constructor_exists():
    assert callable(gbind::simpleocl::StaticPropertyCallExp.__init__)


def test_gbind::simpleocl::staticpropertycallexp_constructor_args():
    sig = inspect.signature(gbind::simpleocl::StaticPropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::letexp_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::LetExp)


def test_gbind::simpleocl::letexp_constructor_exists():
    assert callable(gbind::simpleocl::LetExp.__init__)


def test_gbind::simpleocl::letexp_constructor_args():
    sig = inspect.signature(gbind::simpleocl::LetExp.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::envexp_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::EnvExp)


def test_gbind::simpleocl::envexp_constructor_exists():
    assert callable(gbind::simpleocl::EnvExp.__init__)


def test_gbind::simpleocl::envexp_constructor_args():
    sig = inspect.signature(gbind::simpleocl::EnvExp.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::ifexp_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::IfExp)


def test_gbind::simpleocl::ifexp_constructor_exists():
    assert callable(gbind::simpleocl::IfExp.__init__)


def test_gbind::simpleocl::ifexp_constructor_args():
    sig = inspect.signature(gbind::simpleocl::IfExp.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::operatorcallexp_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::OperatorCallExp)


def test_gbind::simpleocl::operatorcallexp_constructor_exists():
    assert callable(gbind::simpleocl::OperatorCallExp.__init__)


def test_gbind::simpleocl::operatorcallexp_constructor_args():
    sig = inspect.signature(gbind::simpleocl::OperatorCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "operationName" in params, "Missing parameter 'operationName'"

def test_gbind::simpleocl::operatorcallexp_has_operationName():
    assert hasattr(gbind::simpleocl::OperatorCallExp, "operationName")
    descriptor = None
    for klass in gbind::simpleocl::OperatorCallExp.__mro__:
        if "operationName" in klass.__dict__:
            descriptor = klass.__dict__["operationName"]
            break
    assert isinstance(descriptor, property)



def test_gbind::simpleocl::selfexp_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::SelfExp)


def test_gbind::simpleocl::selfexp_constructor_exists():
    assert callable(gbind::simpleocl::SelfExp.__init__)


def test_gbind::simpleocl::selfexp_constructor_args():
    sig = inspect.signature(gbind::simpleocl::SelfExp.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::primitiveexp_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::PrimitiveExp)


def test_gbind::simpleocl::primitiveexp_constructor_exists():
    assert callable(gbind::simpleocl::PrimitiveExp.__init__)


def test_gbind::simpleocl::primitiveexp_constructor_args():
    sig = inspect.signature(gbind::simpleocl::PrimitiveExp.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::oclundefinedexp_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::OclUndefinedExp)


def test_gbind::simpleocl::oclundefinedexp_constructor_exists():
    assert callable(gbind::simpleocl::OclUndefinedExp.__init__)


def test_gbind::simpleocl::oclundefinedexp_constructor_args():
    sig = inspect.signature(gbind::simpleocl::OclUndefinedExp.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::oclmodelelementexp_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::OclModelElementExp)


def test_gbind::simpleocl::oclmodelelementexp_constructor_exists():
    assert callable(gbind::simpleocl::OclModelElementExp.__init__)


def test_gbind::simpleocl::oclmodelelementexp_constructor_args():
    sig = inspect.signature(gbind::simpleocl::OclModelElementExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gbind::simpleocl::oclmodelelementexp_has_name():
    assert hasattr(gbind::simpleocl::OclModelElementExp, "name")
    descriptor = None
    for klass in gbind::simpleocl::OclModelElementExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gbind::simpleocl::propertycallexp_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::PropertyCallExp)


def test_gbind::simpleocl::propertycallexp_constructor_exists():
    assert callable(gbind::simpleocl::PropertyCallExp.__init__)


def test_gbind::simpleocl::propertycallexp_constructor_args():
    sig = inspect.signature(gbind::simpleocl::PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::tupleexp_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::TupleExp)


def test_gbind::simpleocl::tupleexp_constructor_exists():
    assert callable(gbind::simpleocl::TupleExp.__init__)


def test_gbind::simpleocl::tupleexp_constructor_args():
    sig = inspect.signature(gbind::simpleocl::TupleExp.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::enumliteralexp_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::EnumLiteralExp)


def test_gbind::simpleocl::enumliteralexp_constructor_exists():
    assert callable(gbind::simpleocl::EnumLiteralExp.__init__)


def test_gbind::simpleocl::enumliteralexp_constructor_args():
    sig = inspect.signature(gbind::simpleocl::EnumLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gbind::simpleocl::enumliteralexp_has_name():
    assert hasattr(gbind::simpleocl::EnumLiteralExp, "name")
    descriptor = None
    for klass in gbind::simpleocl::EnumLiteralExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gbind::simpleocl::variableexp_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::VariableExp)


def test_gbind::simpleocl::variableexp_constructor_exists():
    assert callable(gbind::simpleocl::VariableExp.__init__)


def test_gbind::simpleocl::variableexp_constructor_args():
    sig = inspect.signature(gbind::simpleocl::VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_operatorcallexp_is_not_abstract():
    assert not inspect.isabstract(OperatorCallExp)


def test_operatorcallexp_constructor_exists():
    assert callable(OperatorCallExp.__init__)


def test_operatorcallexp_constructor_args():
    sig = inspect.signature(OperatorCallExp.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::intopcallexp_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::IntOpCallExp)


def test_gbind::simpleocl::intopcallexp_constructor_exists():
    assert callable(gbind::simpleocl::IntOpCallExp.__init__)


def test_gbind::simpleocl::intopcallexp_constructor_args():
    sig = inspect.signature(gbind::simpleocl::IntOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::eqopcallexp_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::EqOpCallExp)


def test_gbind::simpleocl::eqopcallexp_constructor_exists():
    assert callable(gbind::simpleocl::EqOpCallExp.__init__)


def test_gbind::simpleocl::eqopcallexp_constructor_args():
    sig = inspect.signature(gbind::simpleocl::EqOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::relopcallexp_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::RelOpCallExp)


def test_gbind::simpleocl::relopcallexp_constructor_exists():
    assert callable(gbind::simpleocl::RelOpCallExp.__init__)


def test_gbind::simpleocl::relopcallexp_constructor_args():
    sig = inspect.signature(gbind::simpleocl::RelOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::notopcallexp_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::NotOpCallExp)


def test_gbind::simpleocl::notopcallexp_constructor_exists():
    assert callable(gbind::simpleocl::NotOpCallExp.__init__)


def test_gbind::simpleocl::notopcallexp_constructor_args():
    sig = inspect.signature(gbind::simpleocl::NotOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::mulopcallexp_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::MulOpCallExp)


def test_gbind::simpleocl::mulopcallexp_constructor_exists():
    assert callable(gbind::simpleocl::MulOpCallExp.__init__)


def test_gbind::simpleocl::mulopcallexp_constructor_args():
    sig = inspect.signature(gbind::simpleocl::MulOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::addopcallexp_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::AddOpCallExp)


def test_gbind::simpleocl::addopcallexp_constructor_exists():
    assert callable(gbind::simpleocl::AddOpCallExp.__init__)


def test_gbind::simpleocl::addopcallexp_constructor_args():
    sig = inspect.signature(gbind::simpleocl::AddOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_attribute_is_not_abstract():
    assert not inspect.isabstract(Attribute)


def test_attribute_constructor_exists():
    assert callable(Attribute.__init__)


def test_attribute_constructor_args():
    sig = inspect.signature(Attribute.__init__)
    params = list(sig.parameters.keys())



def test_operation_is_not_abstract():
    assert not inspect.isabstract(Operation)


def test_operation_constructor_exists():
    assert callable(Operation.__init__)


def test_operation_constructor_args():
    sig = inspect.signature(Operation.__init__)
    params = list(sig.parameters.keys())



def test_localvariable_is_not_abstract():
    assert not inspect.isabstract(LocalVariable)


def test_localvariable_constructor_exists():
    assert callable(LocalVariable.__init__)


def test_localvariable_constructor_args():
    sig = inspect.signature(LocalVariable.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::tuplepart_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::TuplePart)


def test_gbind::simpleocl::tuplepart_constructor_exists():
    assert callable(gbind::simpleocl::TuplePart.__init__)


def test_gbind::simpleocl::tuplepart_constructor_args():
    sig = inspect.signature(gbind::simpleocl::TuplePart.__init__)
    params = list(sig.parameters.keys())



def test_operationcall_is_not_abstract():
    assert not inspect.isabstract(OperationCall)


def test_operationcall_constructor_exists():
    assert callable(OperationCall.__init__)


def test_operationcall_constructor_args():
    sig = inspect.signature(OperationCall.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::collectionoperationcall_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::CollectionOperationCall)


def test_gbind::simpleocl::collectionoperationcall_constructor_exists():
    assert callable(gbind::simpleocl::CollectionOperationCall.__init__)


def test_gbind::simpleocl::collectionoperationcall_constructor_args():
    sig = inspect.signature(gbind::simpleocl::CollectionOperationCall.__init__)
    params = list(sig.parameters.keys())



def test_loopexp_is_not_abstract():
    assert not inspect.isabstract(LoopExp)


def test_loopexp_constructor_exists():
    assert callable(LoopExp.__init__)


def test_loopexp_constructor_args():
    sig = inspect.signature(LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::iterateexp_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::IterateExp)


def test_gbind::simpleocl::iterateexp_constructor_exists():
    assert callable(gbind::simpleocl::IterateExp.__init__)


def test_gbind::simpleocl::iterateexp_constructor_args():
    sig = inspect.signature(gbind::simpleocl::IterateExp.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::iteratorexp_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::IteratorExp)


def test_gbind::simpleocl::iteratorexp_constructor_exists():
    assert callable(gbind::simpleocl::IteratorExp.__init__)


def test_gbind::simpleocl::iteratorexp_constructor_args():
    sig = inspect.signature(gbind::simpleocl::IteratorExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gbind::simpleocl::iteratorexp_has_name():
    assert hasattr(gbind::simpleocl::IteratorExp, "name")
    descriptor = None
    for klass in gbind::simpleocl::IteratorExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_letexp_is_not_abstract():
    assert not inspect.isabstract(LetExp)


def test_letexp_constructor_exists():
    assert callable(LetExp.__init__)


def test_letexp_constructor_args():
    sig = inspect.signature(LetExp.__init__)
    params = list(sig.parameters.keys())



def test_collectionexp_is_not_abstract():
    assert not inspect.isabstract(CollectionExp)


def test_collectionexp_constructor_exists():
    assert callable(CollectionExp.__init__)


def test_collectionexp_constructor_args():
    sig = inspect.signature(CollectionExp.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::bagexp_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::BagExp)


def test_gbind::simpleocl::bagexp_constructor_exists():
    assert callable(gbind::simpleocl::BagExp.__init__)


def test_gbind::simpleocl::bagexp_constructor_args():
    sig = inspect.signature(gbind::simpleocl::BagExp.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::setexp_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::SetExp)


def test_gbind::simpleocl::setexp_constructor_exists():
    assert callable(gbind::simpleocl::SetExp.__init__)


def test_gbind::simpleocl::setexp_constructor_args():
    sig = inspect.signature(gbind::simpleocl::SetExp.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::orderedsetexp_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::OrderedSetExp)


def test_gbind::simpleocl::orderedsetexp_constructor_exists():
    assert callable(gbind::simpleocl::OrderedSetExp.__init__)


def test_gbind::simpleocl::orderedsetexp_constructor_args():
    sig = inspect.signature(gbind::simpleocl::OrderedSetExp.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::sequenceexp_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::SequenceExp)


def test_gbind::simpleocl::sequenceexp_constructor_exists():
    assert callable(gbind::simpleocl::SequenceExp.__init__)


def test_gbind::simpleocl::sequenceexp_constructor_args():
    sig = inspect.signature(gbind::simpleocl::SequenceExp.__init__)
    params = list(sig.parameters.keys())



def test_propertycallexp_is_not_abstract():
    assert not inspect.isabstract(PropertyCallExp)


def test_propertycallexp_constructor_exists():
    assert callable(PropertyCallExp.__init__)


def test_propertycallexp_constructor_args():
    sig = inspect.signature(PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ifexp_is_not_abstract():
    assert not inspect.isabstract(IfExp)


def test_ifexp_constructor_exists():
    assert callable(IfExp.__init__)


def test_ifexp_constructor_args():
    sig = inspect.signature(IfExp.__init__)
    params = list(sig.parameters.keys())



def test_ocltype_is_not_abstract():
    assert not inspect.isabstract(OclType)


def test_ocltype_constructor_exists():
    assert callable(OclType.__init__)


def test_ocltype_constructor_args():
    sig = inspect.signature(OclType.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::tupletype_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::TupleType)


def test_gbind::simpleocl::tupletype_constructor_exists():
    assert callable(gbind::simpleocl::TupleType.__init__)


def test_gbind::simpleocl::tupletype_constructor_args():
    sig = inspect.signature(gbind::simpleocl::TupleType.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::collectiontype_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::CollectionType)


def test_gbind::simpleocl::collectiontype_constructor_exists():
    assert callable(gbind::simpleocl::CollectionType.__init__)


def test_gbind::simpleocl::collectiontype_constructor_args():
    sig = inspect.signature(gbind::simpleocl::CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::primitive_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::Primitive)


def test_gbind::simpleocl::primitive_constructor_exists():
    assert callable(gbind::simpleocl::Primitive.__init__)


def test_gbind::simpleocl::primitive_constructor_args():
    sig = inspect.signature(gbind::simpleocl::Primitive.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::oclmodelelement_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::OclModelElement)


def test_gbind::simpleocl::oclmodelelement_constructor_exists():
    assert callable(gbind::simpleocl::OclModelElement.__init__)


def test_gbind::simpleocl::oclmodelelement_constructor_args():
    sig = inspect.signature(gbind::simpleocl::OclModelElement.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::oclanytype_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::OclAnyType)


def test_gbind::simpleocl::oclanytype_constructor_exists():
    assert callable(gbind::simpleocl::OclAnyType.__init__)


def test_gbind::simpleocl::oclanytype_constructor_args():
    sig = inspect.signature(gbind::simpleocl::OclAnyType.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::lambdatype_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::LambdaType)


def test_gbind::simpleocl::lambdatype_constructor_exists():
    assert callable(gbind::simpleocl::LambdaType.__init__)


def test_gbind::simpleocl::lambdatype_constructor_args():
    sig = inspect.signature(gbind::simpleocl::LambdaType.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::maptype_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::MapType)


def test_gbind::simpleocl::maptype_constructor_exists():
    assert callable(gbind::simpleocl::MapType.__init__)


def test_gbind::simpleocl::maptype_constructor_args():
    sig = inspect.signature(gbind::simpleocl::MapType.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::envtype_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::EnvType)


def test_gbind::simpleocl::envtype_constructor_exists():
    assert callable(gbind::simpleocl::EnvType.__init__)


def test_gbind::simpleocl::envtype_constructor_args():
    sig = inspect.signature(gbind::simpleocl::EnvType.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::import_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::Import)


def test_gbind::simpleocl::import_constructor_exists():
    assert callable(gbind::simpleocl::Import.__init__)


def test_gbind::simpleocl::import_constructor_args():
    sig = inspect.signature(gbind::simpleocl::Import.__init__)
    params = list(sig.parameters.keys())



def test_module_is_not_abstract():
    assert not inspect.isabstract(Module)


def test_module_constructor_exists():
    assert callable(Module.__init__)


def test_module_constructor_args():
    sig = inspect.signature(Module.__init__)
    params = list(sig.parameters.keys())



def test_locatedelement_is_not_abstract():
    assert not inspect.isabstract(LocatedElement)


def test_locatedelement_constructor_exists():
    assert callable(LocatedElement.__init__)


def test_locatedelement_constructor_args():
    sig = inspect.signature(LocatedElement.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::propertycall_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::PropertyCall)


def test_gbind::simpleocl::propertycall_constructor_exists():
    assert callable(gbind::simpleocl::PropertyCall.__init__)


def test_gbind::simpleocl::propertycall_constructor_args():
    sig = inspect.signature(gbind::simpleocl::PropertyCall.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::oclcontextdefinition_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::OclContextDefinition)


def test_gbind::simpleocl::oclcontextdefinition_constructor_exists():
    assert callable(gbind::simpleocl::OclContextDefinition.__init__)


def test_gbind::simpleocl::oclcontextdefinition_constructor_args():
    sig = inspect.signature(gbind::simpleocl::OclContextDefinition.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::tupletypeattribute_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::TupleTypeAttribute)


def test_gbind::simpleocl::tupletypeattribute_constructor_exists():
    assert callable(gbind::simpleocl::TupleTypeAttribute.__init__)


def test_gbind::simpleocl::tupletypeattribute_constructor_args():
    sig = inspect.signature(gbind::simpleocl::TupleTypeAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gbind::simpleocl::tupletypeattribute_has_name():
    assert hasattr(gbind::simpleocl::TupleTypeAttribute, "name")
    descriptor = None
    for klass in gbind::simpleocl::TupleTypeAttribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gbind::simpleocl::ocltype_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::OclType)


def test_gbind::simpleocl::ocltype_constructor_exists():
    assert callable(gbind::simpleocl::OclType.__init__)


def test_gbind::simpleocl::ocltype_constructor_args():
    sig = inspect.signature(gbind::simpleocl::OclType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gbind::simpleocl::ocltype_has_name():
    assert hasattr(gbind::simpleocl::OclType, "name")
    descriptor = None
    for klass in gbind::simpleocl::OclType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gbind::simpleocl::moduleelement_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::ModuleElement)


def test_gbind::simpleocl::moduleelement_constructor_exists():
    assert callable(gbind::simpleocl::ModuleElement.__init__)


def test_gbind::simpleocl::moduleelement_constructor_args():
    sig = inspect.signature(gbind::simpleocl::ModuleElement.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::mapelement_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::MapElement)


def test_gbind::simpleocl::mapelement_constructor_exists():
    assert callable(gbind::simpleocl::MapElement.__init__)


def test_gbind::simpleocl::mapelement_constructor_args():
    sig = inspect.signature(gbind::simpleocl::MapElement.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::VariableDeclaration)


def test_gbind::simpleocl::variabledeclaration_constructor_exists():
    assert callable(gbind::simpleocl::VariableDeclaration.__init__)


def test_gbind::simpleocl::variabledeclaration_constructor_args():
    sig = inspect.signature(gbind::simpleocl::VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"

def test_gbind::simpleocl::variabledeclaration_has_varName():
    assert hasattr(gbind::simpleocl::VariableDeclaration, "varName")
    descriptor = None
    for klass in gbind::simpleocl::VariableDeclaration.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_gbind::simpleocl::staticpropertycall_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::StaticPropertyCall)


def test_gbind::simpleocl::staticpropertycall_constructor_exists():
    assert callable(gbind::simpleocl::StaticPropertyCall.__init__)


def test_gbind::simpleocl::staticpropertycall_constructor_args():
    sig = inspect.signature(gbind::simpleocl::StaticPropertyCall.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::oclexpression_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::OclExpression)


def test_gbind::simpleocl::oclexpression_constructor_exists():
    assert callable(gbind::simpleocl::OclExpression.__init__)


def test_gbind::simpleocl::oclexpression_constructor_args():
    sig = inspect.signature(gbind::simpleocl::OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_gbind::simpleocl::namedelement_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::NamedElement)


def test_gbind::simpleocl::namedelement_constructor_exists():
    assert callable(gbind::simpleocl::NamedElement.__init__)


def test_gbind::simpleocl::namedelement_constructor_args():
    sig = inspect.signature(gbind::simpleocl::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gbind::simpleocl::namedelement_has_name():
    assert hasattr(gbind::simpleocl::NamedElement, "name")
    descriptor = None
    for klass in gbind::simpleocl::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gbind::simpleocl::locatedelement_is_not_abstract():
    assert not inspect.isabstract(gbind::simpleocl::LocatedElement)


def test_gbind::simpleocl::locatedelement_constructor_exists():
    assert callable(gbind::simpleocl::LocatedElement.__init__)


def test_gbind::simpleocl::locatedelement_constructor_args():
    sig = inspect.signature(gbind::simpleocl::LocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "line" in params, "Missing parameter 'line'"
    assert "charStart" in params, "Missing parameter 'charStart'"
    assert "charEnd" in params, "Missing parameter 'charEnd'"
    assert "column" in params, "Missing parameter 'column'"

def test_gbind::simpleocl::locatedelement_has_line():
    assert hasattr(gbind::simpleocl::LocatedElement, "line")
    descriptor = None
    for klass in gbind::simpleocl::LocatedElement.__mro__:
        if "line" in klass.__dict__:
            descriptor = klass.__dict__["line"]
            break
    assert isinstance(descriptor, property)

def test_gbind::simpleocl::locatedelement_has_charStart():
    assert hasattr(gbind::simpleocl::LocatedElement, "charStart")
    descriptor = None
    for klass in gbind::simpleocl::LocatedElement.__mro__:
        if "charStart" in klass.__dict__:
            descriptor = klass.__dict__["charStart"]
            break
    assert isinstance(descriptor, property)

def test_gbind::simpleocl::locatedelement_has_charEnd():
    assert hasattr(gbind::simpleocl::LocatedElement, "charEnd")
    descriptor = None
    for klass in gbind::simpleocl::LocatedElement.__mro__:
        if "charEnd" in klass.__dict__:
            descriptor = klass.__dict__["charEnd"]
            break
    assert isinstance(descriptor, property)

def test_gbind::simpleocl::locatedelement_has_column():
    assert hasattr(gbind::simpleocl::LocatedElement, "column")
    descriptor = None
    for klass in gbind::simpleocl::LocatedElement.__mro__:
        if "column" in klass.__dict__:
            descriptor = klass.__dict__["column"]
            break
    assert isinstance(descriptor, property)


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
HelperParameter_strategy = st.builds(
    HelperParameter,
)
gbind::dsl::BaseHelper_strategy = st.builds(
    gbind::dsl::BaseHelper,
    feature=
        safe_text
)
gbind::dsl::ConceptFeatureRef_strategy = st.builds(
    gbind::dsl::ConceptFeatureRef,
    featureName=
        safe_text
)
ConceptFeatureRef_strategy = st.builds(
    ConceptFeatureRef,
)
Metaclass_strategy = st.builds(
    Metaclass,
)
gbind::dsl::ConcreteMetaclass_strategy = st.builds(
    gbind::dsl::ConcreteMetaclass,
)
gbind::dsl::ConceptMetaclass_strategy = st.builds(
    gbind::dsl::ConceptMetaclass,
)
dsl::gbind::EClass_strategy = st.builds(
    dsl::gbind::EClass,
)
VirtualFeature_strategy = st.builds(
    VirtualFeature,
)
gbind::dsl::VirtualAttribute_strategy = st.builds(
    gbind::dsl::VirtualAttribute,
)
gbind::dsl::VirtualReference_strategy = st.builds(
    gbind::dsl::VirtualReference,
)
gbind::dsl::VirtualFeature_strategy = st.builds(
    gbind::dsl::VirtualFeature,
    name=
        safe_text
)
VirtualAttribute_strategy = st.builds(
    VirtualAttribute,
)
VirtualReference_strategy = st.builds(
    VirtualReference,
)
gbind::dsl::VirtualMetaclass_strategy = st.builds(
    gbind::dsl::VirtualMetaclass,
)
BaseFeatureBinding_strategy = st.builds(
    BaseFeatureBinding,
)
gbind::dsl::OclFeatureBinding_strategy = st.builds(
    gbind::dsl::OclFeatureBinding,
)
gbind::dsl::RenamingFeatureBinding_strategy = st.builds(
    gbind::dsl::RenamingFeatureBinding,
    concreteFeature=
        safe_text
)
ConcreteReferencDeclaringVar_strategy = st.builds(
    ConcreteReferencDeclaringVar,
)
BindingModel_strategy = st.builds(
    BindingModel,
)
gbind::dsl::ConceptBinding_strategy = st.builds(
    gbind::dsl::ConceptBinding,
    debugName=
        safe_text
)
OclModelElement_strategy = st.builds(
    OclModelElement,
)
gbind::dsl::Metaclass_strategy = st.builds(
    gbind::dsl::Metaclass,
    name=
        safe_text
)
gbind::dsl::BindingOptions_strategy = st.builds(
    gbind::dsl::BindingOptions,
    enableClassMerge=
        st.booleans()
)
BindingOptions_strategy = st.builds(
    BindingOptions,
)
MetamodelDeclaration_strategy = st.builds(
    MetamodelDeclaration,
)
VirtualMetaclass_strategy = st.builds(
    VirtualMetaclass,
)
ConcreteMetaclass_strategy = st.builds(
    ConcreteMetaclass,
)
ConceptMetaclass_strategy = st.builds(
    ConceptMetaclass,
)
BaseHelper_strategy = st.builds(
    BaseHelper,
)
gbind::dsl::LocalHelper_strategy = st.builds(
    gbind::dsl::LocalHelper,
)
gbind::dsl::ConceptHelper_strategy = st.builds(
    gbind::dsl::ConceptHelper,
)
ConceptBinding_strategy = st.builds(
    ConceptBinding,
)
gbind::dsl::VirtualClassBinding_strategy = st.builds(
    gbind::dsl::VirtualClassBinding,
)
gbind::dsl::BaseFeatureBinding_strategy = st.builds(
    gbind::dsl::BaseFeatureBinding,
    conceptFeature=
        safe_text
)
gbind::dsl::ClassBinding_strategy = st.builds(
    gbind::dsl::ClassBinding,
)
gbind::dsl::IntermediateClassBinding_strategy = st.builds(
    gbind::dsl::IntermediateClassBinding,
    conceptReferenceName=
        safe_text
)
gbind::dsl::BindingModel_strategy = st.builds(
    gbind::dsl::BindingModel,
    name=
        safe_text
)
OclInstanceModel_strategy = st.builds(
    OclInstanceModel,
)
OclFeature_strategy = st.builds(
    OclFeature,
)
Parameter_strategy = st.builds(
    Parameter,
)
gbind::simpleocl::Operation_strategy = st.builds(
    gbind::simpleocl::Operation,
)
gbind::simpleocl::Attribute_strategy = st.builds(
    gbind::simpleocl::Attribute,
)
OclFeatureDefinition_strategy = st.builds(
    OclFeatureDefinition,
)
OclModel_strategy = st.builds(
    OclModel,
)
gbind::simpleocl::OclInstanceModel_strategy = st.builds(
    gbind::simpleocl::OclInstanceModel,
)
gbind::simpleocl::OclMetamodel_strategy = st.builds(
    gbind::simpleocl::OclMetamodel,
    uri=
        safe_text
)
TupleType_strategy = st.builds(
    TupleType,
)
NumericType_strategy = st.builds(
    NumericType,
)
gbind::simpleocl::RealType_strategy = st.builds(
    gbind::simpleocl::RealType,
)
gbind::simpleocl::IntegerType_strategy = st.builds(
    gbind::simpleocl::IntegerType,
)
Primitive_strategy = st.builds(
    Primitive,
)
gbind::simpleocl::NumericType_strategy = st.builds(
    gbind::simpleocl::NumericType,
)
gbind::simpleocl::BooleanType_strategy = st.builds(
    gbind::simpleocl::BooleanType,
)
gbind::simpleocl::StringType_strategy = st.builds(
    gbind::simpleocl::StringType,
)
LambdaType_strategy = st.builds(
    LambdaType,
)
TupleTypeAttribute_strategy = st.builds(
    TupleTypeAttribute,
)
CollectionType_strategy = st.builds(
    CollectionType,
)
gbind::simpleocl::BagType_strategy = st.builds(
    gbind::simpleocl::BagType,
)
gbind::simpleocl::SequenceType_strategy = st.builds(
    gbind::simpleocl::SequenceType,
)
gbind::simpleocl::OrderedSetType_strategy = st.builds(
    gbind::simpleocl::OrderedSetType,
)
gbind::simpleocl::SetType_strategy = st.builds(
    gbind::simpleocl::SetType,
)
MapType_strategy = st.builds(
    MapType,
)
OclContextDefinition_strategy = st.builds(
    OclContextDefinition,
)
IterateExp_strategy = st.builds(
    IterateExp,
)
VariableExp_strategy = st.builds(
    VariableExp,
)
gbind::simpleocl::LambdaCallExp_strategy = st.builds(
    gbind::simpleocl::LambdaCallExp,
)
Iterator_strategy = st.builds(
    Iterator,
)
StaticPropertyCallExp_strategy = st.builds(
    StaticPropertyCallExp,
)
StaticPropertyCall_strategy = st.builds(
    StaticPropertyCall,
)
gbind::simpleocl::StaticOperationCall_strategy = st.builds(
    gbind::simpleocl::StaticOperationCall,
    operationName=
        safe_text
)
gbind::simpleocl::StaticNavigationOrAttributeCall_strategy = st.builds(
    gbind::simpleocl::StaticNavigationOrAttributeCall,
    name=
        safe_text
)
PropertyCall_strategy = st.builds(
    PropertyCall,
)
gbind::simpleocl::NavigationOrAttributeCall_strategy = st.builds(
    gbind::simpleocl::NavigationOrAttributeCall,
    name=
        safe_text
)
gbind::simpleocl::OperationCall_strategy = st.builds(
    gbind::simpleocl::OperationCall,
    operationName=
        safe_text
)
gbind::simpleocl::LoopExp_strategy = st.builds(
    gbind::simpleocl::LoopExp,
)
NumericExp_strategy = st.builds(
    NumericExp,
)
gbind::simpleocl::RealExp_strategy = st.builds(
    gbind::simpleocl::RealExp,
    realSymbol=
        safe_text
)
PrimitiveExp_strategy = st.builds(
    PrimitiveExp,
)
gbind::simpleocl::BooleanExp_strategy = st.builds(
    gbind::simpleocl::BooleanExp,
    booleanSymbol=
        safe_text
)
gbind::simpleocl::NumericExp_strategy = st.builds(
    gbind::simpleocl::NumericExp,
)
gbind::simpleocl::StringExp_strategy = st.builds(
    gbind::simpleocl::StringExp,
    stringSymbol=
        safe_text
)
MapExp_strategy = st.builds(
    MapExp,
)
MapElement_strategy = st.builds(
    MapElement,
)
TupleExp_strategy = st.builds(
    TupleExp,
)
TuplePart_strategy = st.builds(
    TuplePart,
)
gbind::simpleocl::IntegerExp_strategy = st.builds(
    gbind::simpleocl::IntegerExp,
    integerSymbol=
        safe_text
)
ModuleElement_strategy = st.builds(
    ModuleElement,
)
gbind::simpleocl::OclFeatureDefinition_strategy = st.builds(
    gbind::simpleocl::OclFeatureDefinition,
    static=
        safe_text
)
Import_strategy = st.builds(
    Import,
)
OclMetamodel_strategy = st.builds(
    OclMetamodel,
)
gbind::dsl::MetamodelDeclaration_strategy = st.builds(
    gbind::dsl::MetamodelDeclaration,
    metamodelURI=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
gbind::simpleocl::OclFeature_strategy = st.builds(
    gbind::simpleocl::OclFeature,
    eq=
        safe_text
)
gbind::simpleocl::OclModel_strategy = st.builds(
    gbind::simpleocl::OclModel,
)
gbind::simpleocl::Module_strategy = st.builds(
    gbind::simpleocl::Module,
)
VariableDeclaration_strategy = st.builds(
    VariableDeclaration,
)
gbind::simpleocl::Iterator_strategy = st.builds(
    gbind::simpleocl::Iterator,
)
gbind::dsl::ConcreteReferencDeclaringVar_strategy = st.builds(
    gbind::dsl::ConcreteReferencDeclaringVar,
)
gbind::dsl::HelperParameter_strategy = st.builds(
    gbind::dsl::HelperParameter,
)
gbind::simpleocl::Parameter_strategy = st.builds(
    gbind::simpleocl::Parameter,
)
gbind::simpleocl::LocalVariable_strategy = st.builds(
    gbind::simpleocl::LocalVariable,
    eq=
        safe_text
)
OclExpression_strategy = st.builds(
    OclExpression,
)
gbind::simpleocl::BraceExp_strategy = st.builds(
    gbind::simpleocl::BraceExp,
)
gbind::simpleocl::CollectionExp_strategy = st.builds(
    gbind::simpleocl::CollectionExp,
)
gbind::simpleocl::MapExp_strategy = st.builds(
    gbind::simpleocl::MapExp,
)
gbind::simpleocl::SuperExp_strategy = st.builds(
    gbind::simpleocl::SuperExp,
)
gbind::simpleocl::StaticPropertyCallExp_strategy = st.builds(
    gbind::simpleocl::StaticPropertyCallExp,
)
gbind::simpleocl::LetExp_strategy = st.builds(
    gbind::simpleocl::LetExp,
)
gbind::simpleocl::EnvExp_strategy = st.builds(
    gbind::simpleocl::EnvExp,
)
gbind::simpleocl::IfExp_strategy = st.builds(
    gbind::simpleocl::IfExp,
)
gbind::simpleocl::OperatorCallExp_strategy = st.builds(
    gbind::simpleocl::OperatorCallExp,
    operationName=
        safe_text
)
gbind::simpleocl::SelfExp_strategy = st.builds(
    gbind::simpleocl::SelfExp,
)
gbind::simpleocl::PrimitiveExp_strategy = st.builds(
    gbind::simpleocl::PrimitiveExp,
)
gbind::simpleocl::OclUndefinedExp_strategy = st.builds(
    gbind::simpleocl::OclUndefinedExp,
)
gbind::simpleocl::OclModelElementExp_strategy = st.builds(
    gbind::simpleocl::OclModelElementExp,
    name=
        safe_text
)
gbind::simpleocl::PropertyCallExp_strategy = st.builds(
    gbind::simpleocl::PropertyCallExp,
)
gbind::simpleocl::TupleExp_strategy = st.builds(
    gbind::simpleocl::TupleExp,
)
gbind::simpleocl::EnumLiteralExp_strategy = st.builds(
    gbind::simpleocl::EnumLiteralExp,
    name=
        safe_text
)
gbind::simpleocl::VariableExp_strategy = st.builds(
    gbind::simpleocl::VariableExp,
)
OperatorCallExp_strategy = st.builds(
    OperatorCallExp,
)
gbind::simpleocl::IntOpCallExp_strategy = st.builds(
    gbind::simpleocl::IntOpCallExp,
)
gbind::simpleocl::EqOpCallExp_strategy = st.builds(
    gbind::simpleocl::EqOpCallExp,
)
gbind::simpleocl::RelOpCallExp_strategy = st.builds(
    gbind::simpleocl::RelOpCallExp,
)
gbind::simpleocl::NotOpCallExp_strategy = st.builds(
    gbind::simpleocl::NotOpCallExp,
)
gbind::simpleocl::MulOpCallExp_strategy = st.builds(
    gbind::simpleocl::MulOpCallExp,
)
gbind::simpleocl::AddOpCallExp_strategy = st.builds(
    gbind::simpleocl::AddOpCallExp,
)
Attribute_strategy = st.builds(
    Attribute,
)
Operation_strategy = st.builds(
    Operation,
)
LocalVariable_strategy = st.builds(
    LocalVariable,
)
gbind::simpleocl::TuplePart_strategy = st.builds(
    gbind::simpleocl::TuplePart,
)
OperationCall_strategy = st.builds(
    OperationCall,
)
gbind::simpleocl::CollectionOperationCall_strategy = st.builds(
    gbind::simpleocl::CollectionOperationCall,
)
LoopExp_strategy = st.builds(
    LoopExp,
)
gbind::simpleocl::IterateExp_strategy = st.builds(
    gbind::simpleocl::IterateExp,
)
gbind::simpleocl::IteratorExp_strategy = st.builds(
    gbind::simpleocl::IteratorExp,
    name=
        safe_text
)
LetExp_strategy = st.builds(
    LetExp,
)
CollectionExp_strategy = st.builds(
    CollectionExp,
)
gbind::simpleocl::BagExp_strategy = st.builds(
    gbind::simpleocl::BagExp,
)
gbind::simpleocl::SetExp_strategy = st.builds(
    gbind::simpleocl::SetExp,
)
gbind::simpleocl::OrderedSetExp_strategy = st.builds(
    gbind::simpleocl::OrderedSetExp,
)
gbind::simpleocl::SequenceExp_strategy = st.builds(
    gbind::simpleocl::SequenceExp,
)
PropertyCallExp_strategy = st.builds(
    PropertyCallExp,
)
IfExp_strategy = st.builds(
    IfExp,
)
OclType_strategy = st.builds(
    OclType,
)
gbind::simpleocl::TupleType_strategy = st.builds(
    gbind::simpleocl::TupleType,
)
gbind::simpleocl::CollectionType_strategy = st.builds(
    gbind::simpleocl::CollectionType,
)
gbind::simpleocl::Primitive_strategy = st.builds(
    gbind::simpleocl::Primitive,
)
gbind::simpleocl::OclModelElement_strategy = st.builds(
    gbind::simpleocl::OclModelElement,
)
gbind::simpleocl::OclAnyType_strategy = st.builds(
    gbind::simpleocl::OclAnyType,
)
gbind::simpleocl::LambdaType_strategy = st.builds(
    gbind::simpleocl::LambdaType,
)
gbind::simpleocl::MapType_strategy = st.builds(
    gbind::simpleocl::MapType,
)
gbind::simpleocl::EnvType_strategy = st.builds(
    gbind::simpleocl::EnvType,
)
gbind::simpleocl::Import_strategy = st.builds(
    gbind::simpleocl::Import,
)
Module_strategy = st.builds(
    Module,
)
LocatedElement_strategy = st.builds(
    LocatedElement,
)
gbind::simpleocl::PropertyCall_strategy = st.builds(
    gbind::simpleocl::PropertyCall,
)
gbind::simpleocl::OclContextDefinition_strategy = st.builds(
    gbind::simpleocl::OclContextDefinition,
)
gbind::simpleocl::TupleTypeAttribute_strategy = st.builds(
    gbind::simpleocl::TupleTypeAttribute,
    name=
        safe_text
)
gbind::simpleocl::OclType_strategy = st.builds(
    gbind::simpleocl::OclType,
    name=
        safe_text
)
gbind::simpleocl::ModuleElement_strategy = st.builds(
    gbind::simpleocl::ModuleElement,
)
gbind::simpleocl::MapElement_strategy = st.builds(
    gbind::simpleocl::MapElement,
)
gbind::simpleocl::VariableDeclaration_strategy = st.builds(
    gbind::simpleocl::VariableDeclaration,
    varName=
        safe_text
)
gbind::simpleocl::StaticPropertyCall_strategy = st.builds(
    gbind::simpleocl::StaticPropertyCall,
)
gbind::simpleocl::OclExpression_strategy = st.builds(
    gbind::simpleocl::OclExpression,
)
gbind::simpleocl::NamedElement_strategy = st.builds(
    gbind::simpleocl::NamedElement,
    name=
        safe_text
)
gbind::simpleocl::LocatedElement_strategy = st.builds(
    gbind::simpleocl::LocatedElement,
    line=
        safe_text,
    charStart=
        safe_text,
    charEnd=
        safe_text,
    column=
        safe_text
)

@given(instance=HelperParameter_strategy)
@settings(max_examples=50)
def test_helperparameter_instantiation(instance):
    assert isinstance(instance, HelperParameter)

@given(instance=gbind::dsl::BaseHelper_strategy)
@settings(max_examples=50)
def test_gbind::dsl::basehelper_instantiation(instance):
    assert isinstance(instance, gbind::dsl::BaseHelper)

@given(instance=gbind::dsl::BaseHelper_strategy)
def test_gbind::dsl::basehelper_feature_type(instance):
    assert isinstance(instance.feature, str)


@given(instance=gbind::dsl::BaseHelper_strategy)
def test_gbind::dsl::basehelper_feature_setter(instance):
    original = instance.feature
    instance.feature = original
    assert instance.feature == original

@given(instance=gbind::dsl::ConceptFeatureRef_strategy)
@settings(max_examples=50)
def test_gbind::dsl::conceptfeatureref_instantiation(instance):
    assert isinstance(instance, gbind::dsl::ConceptFeatureRef)

@given(instance=gbind::dsl::ConceptFeatureRef_strategy)
def test_gbind::dsl::conceptfeatureref_featureName_type(instance):
    assert isinstance(instance.featureName, str)


@given(instance=gbind::dsl::ConceptFeatureRef_strategy)
def test_gbind::dsl::conceptfeatureref_featureName_setter(instance):
    original = instance.featureName
    instance.featureName = original
    assert instance.featureName == original

@given(instance=ConceptFeatureRef_strategy)
@settings(max_examples=50)
def test_conceptfeatureref_instantiation(instance):
    assert isinstance(instance, ConceptFeatureRef)

@given(instance=Metaclass_strategy)
@settings(max_examples=50)
def test_metaclass_instantiation(instance):
    assert isinstance(instance, Metaclass)

@given(instance=gbind::dsl::ConcreteMetaclass_strategy)
@settings(max_examples=50)
def test_gbind::dsl::concretemetaclass_instantiation(instance):
    assert isinstance(instance, gbind::dsl::ConcreteMetaclass)

@given(instance=gbind::dsl::ConceptMetaclass_strategy)
@settings(max_examples=50)
def test_gbind::dsl::conceptmetaclass_instantiation(instance):
    assert isinstance(instance, gbind::dsl::ConceptMetaclass)

@given(instance=dsl::gbind::EClass_strategy)
@settings(max_examples=50)
def test_dsl::gbind::eclass_instantiation(instance):
    assert isinstance(instance, dsl::gbind::EClass)

@given(instance=VirtualFeature_strategy)
@settings(max_examples=50)
def test_virtualfeature_instantiation(instance):
    assert isinstance(instance, VirtualFeature)

@given(instance=gbind::dsl::VirtualAttribute_strategy)
@settings(max_examples=50)
def test_gbind::dsl::virtualattribute_instantiation(instance):
    assert isinstance(instance, gbind::dsl::VirtualAttribute)

@given(instance=gbind::dsl::VirtualReference_strategy)
@settings(max_examples=50)
def test_gbind::dsl::virtualreference_instantiation(instance):
    assert isinstance(instance, gbind::dsl::VirtualReference)

@given(instance=gbind::dsl::VirtualFeature_strategy)
@settings(max_examples=50)
def test_gbind::dsl::virtualfeature_instantiation(instance):
    assert isinstance(instance, gbind::dsl::VirtualFeature)

@given(instance=gbind::dsl::VirtualFeature_strategy)
def test_gbind::dsl::virtualfeature_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=gbind::dsl::VirtualFeature_strategy)
def test_gbind::dsl::virtualfeature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=VirtualAttribute_strategy)
@settings(max_examples=50)
def test_virtualattribute_instantiation(instance):
    assert isinstance(instance, VirtualAttribute)

@given(instance=VirtualReference_strategy)
@settings(max_examples=50)
def test_virtualreference_instantiation(instance):
    assert isinstance(instance, VirtualReference)

@given(instance=gbind::dsl::VirtualMetaclass_strategy)
@settings(max_examples=50)
def test_gbind::dsl::virtualmetaclass_instantiation(instance):
    assert isinstance(instance, gbind::dsl::VirtualMetaclass)

@given(instance=BaseFeatureBinding_strategy)
@settings(max_examples=50)
def test_basefeaturebinding_instantiation(instance):
    assert isinstance(instance, BaseFeatureBinding)

@given(instance=gbind::dsl::OclFeatureBinding_strategy)
@settings(max_examples=50)
def test_gbind::dsl::oclfeaturebinding_instantiation(instance):
    assert isinstance(instance, gbind::dsl::OclFeatureBinding)

@given(instance=gbind::dsl::RenamingFeatureBinding_strategy)
@settings(max_examples=50)
def test_gbind::dsl::renamingfeaturebinding_instantiation(instance):
    assert isinstance(instance, gbind::dsl::RenamingFeatureBinding)

@given(instance=gbind::dsl::RenamingFeatureBinding_strategy)
def test_gbind::dsl::renamingfeaturebinding_concreteFeature_type(instance):
    assert isinstance(instance.concreteFeature, str)


@given(instance=gbind::dsl::RenamingFeatureBinding_strategy)
def test_gbind::dsl::renamingfeaturebinding_concreteFeature_setter(instance):
    original = instance.concreteFeature
    instance.concreteFeature = original
    assert instance.concreteFeature == original

@given(instance=ConcreteReferencDeclaringVar_strategy)
@settings(max_examples=50)
def test_concretereferencdeclaringvar_instantiation(instance):
    assert isinstance(instance, ConcreteReferencDeclaringVar)

@given(instance=BindingModel_strategy)
@settings(max_examples=50)
def test_bindingmodel_instantiation(instance):
    assert isinstance(instance, BindingModel)

@given(instance=gbind::dsl::ConceptBinding_strategy)
@settings(max_examples=50)
def test_gbind::dsl::conceptbinding_instantiation(instance):
    assert isinstance(instance, gbind::dsl::ConceptBinding)

@given(instance=gbind::dsl::ConceptBinding_strategy)
def test_gbind::dsl::conceptbinding_debugName_type(instance):
    assert isinstance(instance.debugName, str)


@given(instance=gbind::dsl::ConceptBinding_strategy)
def test_gbind::dsl::conceptbinding_debugName_setter(instance):
    original = instance.debugName
    instance.debugName = original
    assert instance.debugName == original

@given(instance=OclModelElement_strategy)
@settings(max_examples=50)
def test_oclmodelelement_instantiation(instance):
    assert isinstance(instance, OclModelElement)

@given(instance=gbind::dsl::Metaclass_strategy)
@settings(max_examples=50)
def test_gbind::dsl::metaclass_instantiation(instance):
    assert isinstance(instance, gbind::dsl::Metaclass)

@given(instance=gbind::dsl::Metaclass_strategy)
def test_gbind::dsl::metaclass_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=gbind::dsl::Metaclass_strategy)
def test_gbind::dsl::metaclass_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gbind::dsl::BindingOptions_strategy)
@settings(max_examples=50)
def test_gbind::dsl::bindingoptions_instantiation(instance):
    assert isinstance(instance, gbind::dsl::BindingOptions)

@given(instance=gbind::dsl::BindingOptions_strategy)
def test_gbind::dsl::bindingoptions_enableClassMerge_type(instance):
    assert isinstance(instance.enableClassMerge, bool)


@given(instance=gbind::dsl::BindingOptions_strategy)
def test_gbind::dsl::bindingoptions_enableClassMerge_setter(instance):
    original = instance.enableClassMerge
    instance.enableClassMerge = original
    assert instance.enableClassMerge == original

@given(instance=BindingOptions_strategy)
@settings(max_examples=50)
def test_bindingoptions_instantiation(instance):
    assert isinstance(instance, BindingOptions)

@given(instance=MetamodelDeclaration_strategy)
@settings(max_examples=50)
def test_metamodeldeclaration_instantiation(instance):
    assert isinstance(instance, MetamodelDeclaration)

@given(instance=VirtualMetaclass_strategy)
@settings(max_examples=50)
def test_virtualmetaclass_instantiation(instance):
    assert isinstance(instance, VirtualMetaclass)

@given(instance=ConcreteMetaclass_strategy)
@settings(max_examples=50)
def test_concretemetaclass_instantiation(instance):
    assert isinstance(instance, ConcreteMetaclass)

@given(instance=ConceptMetaclass_strategy)
@settings(max_examples=50)
def test_conceptmetaclass_instantiation(instance):
    assert isinstance(instance, ConceptMetaclass)

@given(instance=BaseHelper_strategy)
@settings(max_examples=50)
def test_basehelper_instantiation(instance):
    assert isinstance(instance, BaseHelper)

@given(instance=gbind::dsl::LocalHelper_strategy)
@settings(max_examples=50)
def test_gbind::dsl::localhelper_instantiation(instance):
    assert isinstance(instance, gbind::dsl::LocalHelper)

@given(instance=gbind::dsl::ConceptHelper_strategy)
@settings(max_examples=50)
def test_gbind::dsl::concepthelper_instantiation(instance):
    assert isinstance(instance, gbind::dsl::ConceptHelper)

@given(instance=ConceptBinding_strategy)
@settings(max_examples=50)
def test_conceptbinding_instantiation(instance):
    assert isinstance(instance, ConceptBinding)

@given(instance=gbind::dsl::VirtualClassBinding_strategy)
@settings(max_examples=50)
def test_gbind::dsl::virtualclassbinding_instantiation(instance):
    assert isinstance(instance, gbind::dsl::VirtualClassBinding)

@given(instance=gbind::dsl::BaseFeatureBinding_strategy)
@settings(max_examples=50)
def test_gbind::dsl::basefeaturebinding_instantiation(instance):
    assert isinstance(instance, gbind::dsl::BaseFeatureBinding)

@given(instance=gbind::dsl::BaseFeatureBinding_strategy)
def test_gbind::dsl::basefeaturebinding_conceptFeature_type(instance):
    assert isinstance(instance.conceptFeature, str)


@given(instance=gbind::dsl::BaseFeatureBinding_strategy)
def test_gbind::dsl::basefeaturebinding_conceptFeature_setter(instance):
    original = instance.conceptFeature
    instance.conceptFeature = original
    assert instance.conceptFeature == original

@given(instance=gbind::dsl::ClassBinding_strategy)
@settings(max_examples=50)
def test_gbind::dsl::classbinding_instantiation(instance):
    assert isinstance(instance, gbind::dsl::ClassBinding)

@given(instance=gbind::dsl::IntermediateClassBinding_strategy)
@settings(max_examples=50)
def test_gbind::dsl::intermediateclassbinding_instantiation(instance):
    assert isinstance(instance, gbind::dsl::IntermediateClassBinding)

@given(instance=gbind::dsl::IntermediateClassBinding_strategy)
def test_gbind::dsl::intermediateclassbinding_conceptReferenceName_type(instance):
    assert isinstance(instance.conceptReferenceName, str)


@given(instance=gbind::dsl::IntermediateClassBinding_strategy)
def test_gbind::dsl::intermediateclassbinding_conceptReferenceName_setter(instance):
    original = instance.conceptReferenceName
    instance.conceptReferenceName = original
    assert instance.conceptReferenceName == original

@given(instance=gbind::dsl::BindingModel_strategy)
@settings(max_examples=50)
def test_gbind::dsl::bindingmodel_instantiation(instance):
    assert isinstance(instance, gbind::dsl::BindingModel)

@given(instance=gbind::dsl::BindingModel_strategy)
def test_gbind::dsl::bindingmodel_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=gbind::dsl::BindingModel_strategy)
def test_gbind::dsl::bindingmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=OclInstanceModel_strategy)
@settings(max_examples=50)
def test_oclinstancemodel_instantiation(instance):
    assert isinstance(instance, OclInstanceModel)

@given(instance=OclFeature_strategy)
@settings(max_examples=50)
def test_oclfeature_instantiation(instance):
    assert isinstance(instance, OclFeature)

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=gbind::simpleocl::Operation_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::operation_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::Operation)

@given(instance=gbind::simpleocl::Attribute_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::attribute_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::Attribute)

@given(instance=OclFeatureDefinition_strategy)
@settings(max_examples=50)
def test_oclfeaturedefinition_instantiation(instance):
    assert isinstance(instance, OclFeatureDefinition)

@given(instance=OclModel_strategy)
@settings(max_examples=50)
def test_oclmodel_instantiation(instance):
    assert isinstance(instance, OclModel)

@given(instance=gbind::simpleocl::OclInstanceModel_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::oclinstancemodel_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::OclInstanceModel)

@given(instance=gbind::simpleocl::OclMetamodel_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::oclmetamodel_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::OclMetamodel)

@given(instance=gbind::simpleocl::OclMetamodel_strategy)
def test_gbind::simpleocl::oclmetamodel_uri_type(instance):
    assert isinstance(instance.uri, str)


@given(instance=gbind::simpleocl::OclMetamodel_strategy)
def test_gbind::simpleocl::oclmetamodel_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original

@given(instance=TupleType_strategy)
@settings(max_examples=50)
def test_tupletype_instantiation(instance):
    assert isinstance(instance, TupleType)

@given(instance=NumericType_strategy)
@settings(max_examples=50)
def test_numerictype_instantiation(instance):
    assert isinstance(instance, NumericType)

@given(instance=gbind::simpleocl::RealType_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::realtype_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::RealType)

@given(instance=gbind::simpleocl::IntegerType_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::integertype_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::IntegerType)

@given(instance=Primitive_strategy)
@settings(max_examples=50)
def test_primitive_instantiation(instance):
    assert isinstance(instance, Primitive)

@given(instance=gbind::simpleocl::NumericType_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::numerictype_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::NumericType)

@given(instance=gbind::simpleocl::BooleanType_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::booleantype_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::BooleanType)

@given(instance=gbind::simpleocl::StringType_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::stringtype_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::StringType)

@given(instance=LambdaType_strategy)
@settings(max_examples=50)
def test_lambdatype_instantiation(instance):
    assert isinstance(instance, LambdaType)

@given(instance=TupleTypeAttribute_strategy)
@settings(max_examples=50)
def test_tupletypeattribute_instantiation(instance):
    assert isinstance(instance, TupleTypeAttribute)

@given(instance=CollectionType_strategy)
@settings(max_examples=50)
def test_collectiontype_instantiation(instance):
    assert isinstance(instance, CollectionType)

@given(instance=gbind::simpleocl::BagType_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::bagtype_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::BagType)

@given(instance=gbind::simpleocl::SequenceType_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::sequencetype_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::SequenceType)

@given(instance=gbind::simpleocl::OrderedSetType_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::orderedsettype_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::OrderedSetType)

@given(instance=gbind::simpleocl::SetType_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::settype_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::SetType)

@given(instance=MapType_strategy)
@settings(max_examples=50)
def test_maptype_instantiation(instance):
    assert isinstance(instance, MapType)

@given(instance=OclContextDefinition_strategy)
@settings(max_examples=50)
def test_oclcontextdefinition_instantiation(instance):
    assert isinstance(instance, OclContextDefinition)

@given(instance=IterateExp_strategy)
@settings(max_examples=50)
def test_iterateexp_instantiation(instance):
    assert isinstance(instance, IterateExp)

@given(instance=VariableExp_strategy)
@settings(max_examples=50)
def test_variableexp_instantiation(instance):
    assert isinstance(instance, VariableExp)

@given(instance=gbind::simpleocl::LambdaCallExp_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::lambdacallexp_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::LambdaCallExp)

@given(instance=Iterator_strategy)
@settings(max_examples=50)
def test_iterator_instantiation(instance):
    assert isinstance(instance, Iterator)

@given(instance=StaticPropertyCallExp_strategy)
@settings(max_examples=50)
def test_staticpropertycallexp_instantiation(instance):
    assert isinstance(instance, StaticPropertyCallExp)

@given(instance=StaticPropertyCall_strategy)
@settings(max_examples=50)
def test_staticpropertycall_instantiation(instance):
    assert isinstance(instance, StaticPropertyCall)

@given(instance=gbind::simpleocl::StaticOperationCall_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::staticoperationcall_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::StaticOperationCall)

@given(instance=gbind::simpleocl::StaticOperationCall_strategy)
def test_gbind::simpleocl::staticoperationcall_operationName_type(instance):
    assert isinstance(instance.operationName, str)


@given(instance=gbind::simpleocl::StaticOperationCall_strategy)
def test_gbind::simpleocl::staticoperationcall_operationName_setter(instance):
    original = instance.operationName
    instance.operationName = original
    assert instance.operationName == original

@given(instance=gbind::simpleocl::StaticNavigationOrAttributeCall_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::staticnavigationorattributecall_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::StaticNavigationOrAttributeCall)

@given(instance=gbind::simpleocl::StaticNavigationOrAttributeCall_strategy)
def test_gbind::simpleocl::staticnavigationorattributecall_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=gbind::simpleocl::StaticNavigationOrAttributeCall_strategy)
def test_gbind::simpleocl::staticnavigationorattributecall_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PropertyCall_strategy)
@settings(max_examples=50)
def test_propertycall_instantiation(instance):
    assert isinstance(instance, PropertyCall)

@given(instance=gbind::simpleocl::NavigationOrAttributeCall_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::navigationorattributecall_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::NavigationOrAttributeCall)

@given(instance=gbind::simpleocl::NavigationOrAttributeCall_strategy)
def test_gbind::simpleocl::navigationorattributecall_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=gbind::simpleocl::NavigationOrAttributeCall_strategy)
def test_gbind::simpleocl::navigationorattributecall_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gbind::simpleocl::OperationCall_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::operationcall_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::OperationCall)

@given(instance=gbind::simpleocl::OperationCall_strategy)
def test_gbind::simpleocl::operationcall_operationName_type(instance):
    assert isinstance(instance.operationName, str)


@given(instance=gbind::simpleocl::OperationCall_strategy)
def test_gbind::simpleocl::operationcall_operationName_setter(instance):
    original = instance.operationName
    instance.operationName = original
    assert instance.operationName == original

@given(instance=gbind::simpleocl::LoopExp_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::loopexp_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::LoopExp)

@given(instance=NumericExp_strategy)
@settings(max_examples=50)
def test_numericexp_instantiation(instance):
    assert isinstance(instance, NumericExp)

@given(instance=gbind::simpleocl::RealExp_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::realexp_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::RealExp)

@given(instance=gbind::simpleocl::RealExp_strategy)
def test_gbind::simpleocl::realexp_realSymbol_type(instance):
    assert isinstance(instance.realSymbol, str)


@given(instance=gbind::simpleocl::RealExp_strategy)
def test_gbind::simpleocl::realexp_realSymbol_setter(instance):
    original = instance.realSymbol
    instance.realSymbol = original
    assert instance.realSymbol == original

@given(instance=PrimitiveExp_strategy)
@settings(max_examples=50)
def test_primitiveexp_instantiation(instance):
    assert isinstance(instance, PrimitiveExp)

@given(instance=gbind::simpleocl::BooleanExp_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::booleanexp_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::BooleanExp)

@given(instance=gbind::simpleocl::BooleanExp_strategy)
def test_gbind::simpleocl::booleanexp_booleanSymbol_type(instance):
    assert isinstance(instance.booleanSymbol, str)


@given(instance=gbind::simpleocl::BooleanExp_strategy)
def test_gbind::simpleocl::booleanexp_booleanSymbol_setter(instance):
    original = instance.booleanSymbol
    instance.booleanSymbol = original
    assert instance.booleanSymbol == original

@given(instance=gbind::simpleocl::NumericExp_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::numericexp_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::NumericExp)

@given(instance=gbind::simpleocl::StringExp_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::stringexp_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::StringExp)

@given(instance=gbind::simpleocl::StringExp_strategy)
def test_gbind::simpleocl::stringexp_stringSymbol_type(instance):
    assert isinstance(instance.stringSymbol, str)


@given(instance=gbind::simpleocl::StringExp_strategy)
def test_gbind::simpleocl::stringexp_stringSymbol_setter(instance):
    original = instance.stringSymbol
    instance.stringSymbol = original
    assert instance.stringSymbol == original

@given(instance=MapExp_strategy)
@settings(max_examples=50)
def test_mapexp_instantiation(instance):
    assert isinstance(instance, MapExp)

@given(instance=MapElement_strategy)
@settings(max_examples=50)
def test_mapelement_instantiation(instance):
    assert isinstance(instance, MapElement)

@given(instance=TupleExp_strategy)
@settings(max_examples=50)
def test_tupleexp_instantiation(instance):
    assert isinstance(instance, TupleExp)

@given(instance=TuplePart_strategy)
@settings(max_examples=50)
def test_tuplepart_instantiation(instance):
    assert isinstance(instance, TuplePart)

@given(instance=gbind::simpleocl::IntegerExp_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::integerexp_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::IntegerExp)

@given(instance=gbind::simpleocl::IntegerExp_strategy)
def test_gbind::simpleocl::integerexp_integerSymbol_type(instance):
    assert isinstance(instance.integerSymbol, str)


@given(instance=gbind::simpleocl::IntegerExp_strategy)
def test_gbind::simpleocl::integerexp_integerSymbol_setter(instance):
    original = instance.integerSymbol
    instance.integerSymbol = original
    assert instance.integerSymbol == original

@given(instance=ModuleElement_strategy)
@settings(max_examples=50)
def test_moduleelement_instantiation(instance):
    assert isinstance(instance, ModuleElement)

@given(instance=gbind::simpleocl::OclFeatureDefinition_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::oclfeaturedefinition_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::OclFeatureDefinition)

@given(instance=gbind::simpleocl::OclFeatureDefinition_strategy)
def test_gbind::simpleocl::oclfeaturedefinition_static_type(instance):
    assert isinstance(instance.static, str)


@given(instance=gbind::simpleocl::OclFeatureDefinition_strategy)
def test_gbind::simpleocl::oclfeaturedefinition_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=Import_strategy)
@settings(max_examples=50)
def test_import_instantiation(instance):
    assert isinstance(instance, Import)

@given(instance=OclMetamodel_strategy)
@settings(max_examples=50)
def test_oclmetamodel_instantiation(instance):
    assert isinstance(instance, OclMetamodel)

@given(instance=gbind::dsl::MetamodelDeclaration_strategy)
@settings(max_examples=50)
def test_gbind::dsl::metamodeldeclaration_instantiation(instance):
    assert isinstance(instance, gbind::dsl::MetamodelDeclaration)

@given(instance=gbind::dsl::MetamodelDeclaration_strategy)
def test_gbind::dsl::metamodeldeclaration_metamodelURI_type(instance):
    assert isinstance(instance.metamodelURI, str)


@given(instance=gbind::dsl::MetamodelDeclaration_strategy)
def test_gbind::dsl::metamodeldeclaration_metamodelURI_setter(instance):
    original = instance.metamodelURI
    instance.metamodelURI = original
    assert instance.metamodelURI == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=gbind::simpleocl::OclFeature_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::oclfeature_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::OclFeature)

@given(instance=gbind::simpleocl::OclFeature_strategy)
def test_gbind::simpleocl::oclfeature_eq_type(instance):
    assert isinstance(instance.eq, str)


@given(instance=gbind::simpleocl::OclFeature_strategy)
def test_gbind::simpleocl::oclfeature_eq_setter(instance):
    original = instance.eq
    instance.eq = original
    assert instance.eq == original

@given(instance=gbind::simpleocl::OclModel_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::oclmodel_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::OclModel)

@given(instance=gbind::simpleocl::Module_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::module_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::Module)

@given(instance=VariableDeclaration_strategy)
@settings(max_examples=50)
def test_variabledeclaration_instantiation(instance):
    assert isinstance(instance, VariableDeclaration)

@given(instance=gbind::simpleocl::Iterator_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::iterator_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::Iterator)

@given(instance=gbind::dsl::ConcreteReferencDeclaringVar_strategy)
@settings(max_examples=50)
def test_gbind::dsl::concretereferencdeclaringvar_instantiation(instance):
    assert isinstance(instance, gbind::dsl::ConcreteReferencDeclaringVar)

@given(instance=gbind::dsl::HelperParameter_strategy)
@settings(max_examples=50)
def test_gbind::dsl::helperparameter_instantiation(instance):
    assert isinstance(instance, gbind::dsl::HelperParameter)

@given(instance=gbind::simpleocl::Parameter_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::parameter_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::Parameter)

@given(instance=gbind::simpleocl::LocalVariable_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::localvariable_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::LocalVariable)

@given(instance=gbind::simpleocl::LocalVariable_strategy)
def test_gbind::simpleocl::localvariable_eq_type(instance):
    assert isinstance(instance.eq, str)


@given(instance=gbind::simpleocl::LocalVariable_strategy)
def test_gbind::simpleocl::localvariable_eq_setter(instance):
    original = instance.eq
    instance.eq = original
    assert instance.eq == original

@given(instance=OclExpression_strategy)
@settings(max_examples=50)
def test_oclexpression_instantiation(instance):
    assert isinstance(instance, OclExpression)

@given(instance=gbind::simpleocl::BraceExp_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::braceexp_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::BraceExp)

@given(instance=gbind::simpleocl::CollectionExp_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::collectionexp_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::CollectionExp)

@given(instance=gbind::simpleocl::MapExp_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::mapexp_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::MapExp)

@given(instance=gbind::simpleocl::SuperExp_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::superexp_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::SuperExp)

@given(instance=gbind::simpleocl::StaticPropertyCallExp_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::staticpropertycallexp_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::StaticPropertyCallExp)

@given(instance=gbind::simpleocl::LetExp_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::letexp_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::LetExp)

@given(instance=gbind::simpleocl::EnvExp_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::envexp_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::EnvExp)

@given(instance=gbind::simpleocl::IfExp_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::ifexp_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::IfExp)

@given(instance=gbind::simpleocl::OperatorCallExp_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::operatorcallexp_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::OperatorCallExp)

@given(instance=gbind::simpleocl::OperatorCallExp_strategy)
def test_gbind::simpleocl::operatorcallexp_operationName_type(instance):
    assert isinstance(instance.operationName, str)


@given(instance=gbind::simpleocl::OperatorCallExp_strategy)
def test_gbind::simpleocl::operatorcallexp_operationName_setter(instance):
    original = instance.operationName
    instance.operationName = original
    assert instance.operationName == original

@given(instance=gbind::simpleocl::SelfExp_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::selfexp_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::SelfExp)

@given(instance=gbind::simpleocl::PrimitiveExp_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::primitiveexp_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::PrimitiveExp)

@given(instance=gbind::simpleocl::OclUndefinedExp_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::oclundefinedexp_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::OclUndefinedExp)

@given(instance=gbind::simpleocl::OclModelElementExp_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::oclmodelelementexp_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::OclModelElementExp)

@given(instance=gbind::simpleocl::OclModelElementExp_strategy)
def test_gbind::simpleocl::oclmodelelementexp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=gbind::simpleocl::OclModelElementExp_strategy)
def test_gbind::simpleocl::oclmodelelementexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gbind::simpleocl::PropertyCallExp_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::propertycallexp_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::PropertyCallExp)

@given(instance=gbind::simpleocl::TupleExp_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::tupleexp_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::TupleExp)

@given(instance=gbind::simpleocl::EnumLiteralExp_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::enumliteralexp_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::EnumLiteralExp)

@given(instance=gbind::simpleocl::EnumLiteralExp_strategy)
def test_gbind::simpleocl::enumliteralexp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=gbind::simpleocl::EnumLiteralExp_strategy)
def test_gbind::simpleocl::enumliteralexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gbind::simpleocl::VariableExp_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::variableexp_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::VariableExp)

@given(instance=OperatorCallExp_strategy)
@settings(max_examples=50)
def test_operatorcallexp_instantiation(instance):
    assert isinstance(instance, OperatorCallExp)

@given(instance=gbind::simpleocl::IntOpCallExp_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::intopcallexp_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::IntOpCallExp)

@given(instance=gbind::simpleocl::EqOpCallExp_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::eqopcallexp_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::EqOpCallExp)

@given(instance=gbind::simpleocl::RelOpCallExp_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::relopcallexp_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::RelOpCallExp)

@given(instance=gbind::simpleocl::NotOpCallExp_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::notopcallexp_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::NotOpCallExp)

@given(instance=gbind::simpleocl::MulOpCallExp_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::mulopcallexp_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::MulOpCallExp)

@given(instance=gbind::simpleocl::AddOpCallExp_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::addopcallexp_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::AddOpCallExp)

@given(instance=Attribute_strategy)
@settings(max_examples=50)
def test_attribute_instantiation(instance):
    assert isinstance(instance, Attribute)

@given(instance=Operation_strategy)
@settings(max_examples=50)
def test_operation_instantiation(instance):
    assert isinstance(instance, Operation)

@given(instance=LocalVariable_strategy)
@settings(max_examples=50)
def test_localvariable_instantiation(instance):
    assert isinstance(instance, LocalVariable)

@given(instance=gbind::simpleocl::TuplePart_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::tuplepart_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::TuplePart)

@given(instance=OperationCall_strategy)
@settings(max_examples=50)
def test_operationcall_instantiation(instance):
    assert isinstance(instance, OperationCall)

@given(instance=gbind::simpleocl::CollectionOperationCall_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::collectionoperationcall_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::CollectionOperationCall)

@given(instance=LoopExp_strategy)
@settings(max_examples=50)
def test_loopexp_instantiation(instance):
    assert isinstance(instance, LoopExp)

@given(instance=gbind::simpleocl::IterateExp_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::iterateexp_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::IterateExp)

@given(instance=gbind::simpleocl::IteratorExp_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::iteratorexp_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::IteratorExp)

@given(instance=gbind::simpleocl::IteratorExp_strategy)
def test_gbind::simpleocl::iteratorexp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=gbind::simpleocl::IteratorExp_strategy)
def test_gbind::simpleocl::iteratorexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=LetExp_strategy)
@settings(max_examples=50)
def test_letexp_instantiation(instance):
    assert isinstance(instance, LetExp)

@given(instance=CollectionExp_strategy)
@settings(max_examples=50)
def test_collectionexp_instantiation(instance):
    assert isinstance(instance, CollectionExp)

@given(instance=gbind::simpleocl::BagExp_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::bagexp_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::BagExp)

@given(instance=gbind::simpleocl::SetExp_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::setexp_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::SetExp)

@given(instance=gbind::simpleocl::OrderedSetExp_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::orderedsetexp_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::OrderedSetExp)

@given(instance=gbind::simpleocl::SequenceExp_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::sequenceexp_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::SequenceExp)

@given(instance=PropertyCallExp_strategy)
@settings(max_examples=50)
def test_propertycallexp_instantiation(instance):
    assert isinstance(instance, PropertyCallExp)

@given(instance=IfExp_strategy)
@settings(max_examples=50)
def test_ifexp_instantiation(instance):
    assert isinstance(instance, IfExp)

@given(instance=OclType_strategy)
@settings(max_examples=50)
def test_ocltype_instantiation(instance):
    assert isinstance(instance, OclType)

@given(instance=gbind::simpleocl::TupleType_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::tupletype_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::TupleType)

@given(instance=gbind::simpleocl::CollectionType_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::collectiontype_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::CollectionType)

@given(instance=gbind::simpleocl::Primitive_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::primitive_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::Primitive)

@given(instance=gbind::simpleocl::OclModelElement_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::oclmodelelement_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::OclModelElement)

@given(instance=gbind::simpleocl::OclAnyType_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::oclanytype_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::OclAnyType)

@given(instance=gbind::simpleocl::LambdaType_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::lambdatype_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::LambdaType)

@given(instance=gbind::simpleocl::MapType_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::maptype_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::MapType)

@given(instance=gbind::simpleocl::EnvType_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::envtype_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::EnvType)

@given(instance=gbind::simpleocl::Import_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::import_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::Import)

@given(instance=Module_strategy)
@settings(max_examples=50)
def test_module_instantiation(instance):
    assert isinstance(instance, Module)

@given(instance=LocatedElement_strategy)
@settings(max_examples=50)
def test_locatedelement_instantiation(instance):
    assert isinstance(instance, LocatedElement)

@given(instance=gbind::simpleocl::PropertyCall_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::propertycall_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::PropertyCall)

@given(instance=gbind::simpleocl::OclContextDefinition_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::oclcontextdefinition_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::OclContextDefinition)

@given(instance=gbind::simpleocl::TupleTypeAttribute_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::tupletypeattribute_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::TupleTypeAttribute)

@given(instance=gbind::simpleocl::TupleTypeAttribute_strategy)
def test_gbind::simpleocl::tupletypeattribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=gbind::simpleocl::TupleTypeAttribute_strategy)
def test_gbind::simpleocl::tupletypeattribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gbind::simpleocl::OclType_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::ocltype_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::OclType)

@given(instance=gbind::simpleocl::OclType_strategy)
def test_gbind::simpleocl::ocltype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=gbind::simpleocl::OclType_strategy)
def test_gbind::simpleocl::ocltype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gbind::simpleocl::ModuleElement_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::moduleelement_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::ModuleElement)

@given(instance=gbind::simpleocl::MapElement_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::mapelement_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::MapElement)

@given(instance=gbind::simpleocl::VariableDeclaration_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::variabledeclaration_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::VariableDeclaration)

@given(instance=gbind::simpleocl::VariableDeclaration_strategy)
def test_gbind::simpleocl::variabledeclaration_varName_type(instance):
    assert isinstance(instance.varName, str)


@given(instance=gbind::simpleocl::VariableDeclaration_strategy)
def test_gbind::simpleocl::variabledeclaration_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=gbind::simpleocl::StaticPropertyCall_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::staticpropertycall_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::StaticPropertyCall)

@given(instance=gbind::simpleocl::OclExpression_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::oclexpression_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::OclExpression)

@given(instance=gbind::simpleocl::NamedElement_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::namedelement_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::NamedElement)

@given(instance=gbind::simpleocl::NamedElement_strategy)
def test_gbind::simpleocl::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=gbind::simpleocl::NamedElement_strategy)
def test_gbind::simpleocl::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gbind::simpleocl::LocatedElement_strategy)
@settings(max_examples=50)
def test_gbind::simpleocl::locatedelement_instantiation(instance):
    assert isinstance(instance, gbind::simpleocl::LocatedElement)

@given(instance=gbind::simpleocl::LocatedElement_strategy)
def test_gbind::simpleocl::locatedelement_line_type(instance):
    assert isinstance(instance.line, str)


@given(instance=gbind::simpleocl::LocatedElement_strategy)
def test_gbind::simpleocl::locatedelement_line_setter(instance):
    original = instance.line
    instance.line = original
    assert instance.line == original

@given(instance=gbind::simpleocl::LocatedElement_strategy)
def test_gbind::simpleocl::locatedelement_charStart_type(instance):
    assert isinstance(instance.charStart, str)


@given(instance=gbind::simpleocl::LocatedElement_strategy)
def test_gbind::simpleocl::locatedelement_charStart_setter(instance):
    original = instance.charStart
    instance.charStart = original
    assert instance.charStart == original

@given(instance=gbind::simpleocl::LocatedElement_strategy)
def test_gbind::simpleocl::locatedelement_charEnd_type(instance):
    assert isinstance(instance.charEnd, str)


@given(instance=gbind::simpleocl::LocatedElement_strategy)
def test_gbind::simpleocl::locatedelement_charEnd_setter(instance):
    original = instance.charEnd
    instance.charEnd = original
    assert instance.charEnd == original

@given(instance=gbind::simpleocl::LocatedElement_strategy)
def test_gbind::simpleocl::locatedelement_column_type(instance):
    assert isinstance(instance.column, str)


@given(instance=gbind::simpleocl::LocatedElement_strategy)
def test_gbind::simpleocl::locatedelement_column_setter(instance):
    original = instance.column
    instance.column = original
    assert instance.column == original
