import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    gbind_dsl_BaseHelper,
    HelperParameter,
    VirtualAttribute,
    VirtualReference,
    BaseFeatureBinding,
    gbind_dsl_OclFeatureBinding,
    ConcreteReferencDeclaringVar,
    gbind_dsl_RenamingFeatureBinding,
    gbind_dsl_ConceptFeatureRef,
    ConceptFeatureRef,
    VirtualFeature,
    gbind_dsl_VirtualAttribute,
    gbind_dsl_VirtualReference,
    gbind_dsl_VirtualFeature,
    ConcreteMetaclass,
    ConceptMetaclass,
    BaseHelper,
    gbind_dsl_ConceptHelper,
    gbind_dsl_LocalHelper,
    ConceptBinding,
    gbind_dsl_BaseFeatureBinding,
    gbind_dsl_VirtualClassBinding,
    gbind_dsl_IntermediateClassBinding,
    gbind_dsl_BindingModel,
    gbind_dsl_ClassBinding,
    BindingModel,
    gbind_dsl_ConceptBinding,
    Metaclass,
    gbind_dsl_ConcreteMetaclass,
    gbind_dsl_VirtualMetaclass,
    gbind_dsl_ConceptMetaclass,
    dsl_gbind_EClass,
    gbind_dsl_Metaclass,
    gbind_dsl_BindingOptions,
    BindingOptions,
    MetamodelDeclaration,
    VirtualMetaclass,
    OclFeatureDefinition,
    OclFeature,
    OclInstanceModel,
    OclModelElement,
    Parameter,
    gbind_simpleocl_Operation,
    gbind_simpleocl_Attribute,
    NumericType,
    gbind_simpleocl_IntegerType,
    Primitive,
    gbind_simpleocl_NumericType,
    gbind_simpleocl_BooleanType,
    gbind_simpleocl_StringType,
    OclModel,
    gbind_simpleocl_OclInstanceModel,
    gbind_simpleocl_OclMetamodel,
    LambdaType,
    TupleType,
    gbind_simpleocl_RealType,
    IterateExp,
    TupleTypeAttribute,
    CollectionType,
    gbind_simpleocl_SetType,
    gbind_simpleocl_BagType,
    gbind_simpleocl_OrderedSetType,
    gbind_simpleocl_SequenceType,
    MapType,
    OclContextDefinition,
    VariableExp,
    gbind_simpleocl_LambdaCallExp,
    Iterator,
    StaticPropertyCallExp,
    StaticPropertyCall,
    gbind_simpleocl_StaticOperationCall,
    gbind_simpleocl_StaticNavigationOrAttributeCall,
    PropertyCall,
    gbind_simpleocl_NavigationOrAttributeCall,
    gbind_simpleocl_OperationCall,
    gbind_simpleocl_LoopExp,
    NumericExp,
    gbind_simpleocl_RealExp,
    PrimitiveExp,
    gbind_simpleocl_BooleanExp,
    gbind_simpleocl_NumericExp,
    gbind_simpleocl_StringExp,
    VariableDeclaration,
    gbind_simpleocl_Parameter,
    gbind_dsl_HelperParameter,
    gbind_simpleocl_LocalVariable,
    gbind_dsl_ConcreteReferencDeclaringVar,
    gbind_simpleocl_Iterator,
    OclExpression,
    gbind_simpleocl_BraceExp,
    gbind_simpleocl_IfExp,
    gbind_simpleocl_StaticPropertyCallExp,
    gbind_simpleocl_SuperExp,
    gbind_simpleocl_PropertyCallExp,
    gbind_simpleocl_EnvExp,
    gbind_simpleocl_LetExp,
    gbind_simpleocl_OperatorCallExp,
    gbind_simpleocl_PrimitiveExp,
    gbind_simpleocl_OclUndefinedExp,
    gbind_simpleocl_OclModelElementExp,
    gbind_simpleocl_SelfExp,
    gbind_simpleocl_VariableExp,
    gbind_simpleocl_EnumLiteralExp,
    MapExp,
    MapElement,
    gbind_simpleocl_MapExp,
    TupleExp,
    TuplePart,
    gbind_simpleocl_TupleExp,
    gbind_simpleocl_CollectionExp,
    gbind_simpleocl_IntegerExp,
    Module,
    ModuleElement,
    gbind_simpleocl_OclFeatureDefinition,
    Import,
    OclMetamodel,
    gbind_dsl_MetamodelDeclaration,
    NamedElement,
    gbind_simpleocl_OclFeature,
    gbind_simpleocl_OclModel,
    gbind_simpleocl_Module,
    LocatedElement,
    gbind_simpleocl_OclContextDefinition,
    gbind_simpleocl_ModuleElement,
    gbind_simpleocl_MapElement,
    gbind_simpleocl_VariableDeclaration,
    gbind_simpleocl_PropertyCall,
    gbind_simpleocl_StaticPropertyCall,
    gbind_simpleocl_OclType,
    gbind_simpleocl_TupleTypeAttribute,
    gbind_simpleocl_NamedElement,
    OperatorCallExp,
    gbind_simpleocl_EqOpCallExp,
    gbind_simpleocl_MulOpCallExp,
    gbind_simpleocl_NotOpCallExp,
    gbind_simpleocl_IntOpCallExp,
    gbind_simpleocl_RelOpCallExp,
    gbind_simpleocl_AddOpCallExp,
    Attribute,
    Operation,
    LocalVariable,
    gbind_simpleocl_TuplePart,
    OperationCall,
    gbind_simpleocl_CollectionOperationCall,
    LoopExp,
    gbind_simpleocl_IterateExp,
    gbind_simpleocl_IteratorExp,
    LetExp,
    CollectionExp,
    gbind_simpleocl_SetExp,
    gbind_simpleocl_OrderedSetExp,
    gbind_simpleocl_BagExp,
    gbind_simpleocl_SequenceExp,
    PropertyCallExp,
    IfExp,
    OclType,
    gbind_simpleocl_EnvType,
    gbind_simpleocl_CollectionType,
    gbind_simpleocl_LambdaType,
    gbind_simpleocl_OclModelElement,
    gbind_simpleocl_MapType,
    gbind_simpleocl_TupleType,
    gbind_simpleocl_OclAnyType,
    gbind_simpleocl_Primitive,
    gbind_simpleocl_OclExpression,
    gbind_simpleocl_Import,
    gbind_simpleocl_LocatedElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_gbind_dsl_basehelper_is_not_abstract():
    assert not inspect.isabstract(gbind_dsl_BaseHelper)


def test_gbind_dsl_basehelper_constructor_exists():
    assert callable(gbind_dsl_BaseHelper.__init__)


def test_gbind_dsl_basehelper_constructor_args():
    sig = inspect.signature(gbind_dsl_BaseHelper.__init__)
    params = list(sig.parameters.keys())
    assert "feature" in params, "Missing parameter 'feature'"

def test_gbind_dsl_basehelper_has_feature():
    assert hasattr(gbind_dsl_BaseHelper, "feature")
    descriptor = None
    for klass in gbind_dsl_BaseHelper.__mro__:
        if "feature" in klass.__dict__:
            descriptor = klass.__dict__["feature"]
            break
    assert isinstance(descriptor, property)



def test_helperparameter_is_not_abstract():
    assert not inspect.isabstract(HelperParameter)


def test_helperparameter_constructor_exists():
    assert callable(HelperParameter.__init__)


def test_helperparameter_constructor_args():
    sig = inspect.signature(HelperParameter.__init__)
    params = list(sig.parameters.keys())



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



def test_basefeaturebinding_is_not_abstract():
    assert not inspect.isabstract(BaseFeatureBinding)


def test_basefeaturebinding_constructor_exists():
    assert callable(BaseFeatureBinding.__init__)


def test_basefeaturebinding_constructor_args():
    sig = inspect.signature(BaseFeatureBinding.__init__)
    params = list(sig.parameters.keys())



def test_gbind_dsl_oclfeaturebinding_is_not_abstract():
    assert not inspect.isabstract(gbind_dsl_OclFeatureBinding)


def test_gbind_dsl_oclfeaturebinding_constructor_exists():
    assert callable(gbind_dsl_OclFeatureBinding.__init__)


def test_gbind_dsl_oclfeaturebinding_constructor_args():
    sig = inspect.signature(gbind_dsl_OclFeatureBinding.__init__)
    params = list(sig.parameters.keys())



def test_concretereferencdeclaringvar_is_not_abstract():
    assert not inspect.isabstract(ConcreteReferencDeclaringVar)


def test_concretereferencdeclaringvar_constructor_exists():
    assert callable(ConcreteReferencDeclaringVar.__init__)


def test_concretereferencdeclaringvar_constructor_args():
    sig = inspect.signature(ConcreteReferencDeclaringVar.__init__)
    params = list(sig.parameters.keys())



def test_gbind_dsl_renamingfeaturebinding_is_not_abstract():
    assert not inspect.isabstract(gbind_dsl_RenamingFeatureBinding)


def test_gbind_dsl_renamingfeaturebinding_constructor_exists():
    assert callable(gbind_dsl_RenamingFeatureBinding.__init__)


def test_gbind_dsl_renamingfeaturebinding_constructor_args():
    sig = inspect.signature(gbind_dsl_RenamingFeatureBinding.__init__)
    params = list(sig.parameters.keys())
    assert "concreteFeature" in params, "Missing parameter 'concreteFeature'"

def test_gbind_dsl_renamingfeaturebinding_has_concreteFeature():
    assert hasattr(gbind_dsl_RenamingFeatureBinding, "concreteFeature")
    descriptor = None
    for klass in gbind_dsl_RenamingFeatureBinding.__mro__:
        if "concreteFeature" in klass.__dict__:
            descriptor = klass.__dict__["concreteFeature"]
            break
    assert isinstance(descriptor, property)



def test_gbind_dsl_conceptfeatureref_is_not_abstract():
    assert not inspect.isabstract(gbind_dsl_ConceptFeatureRef)


def test_gbind_dsl_conceptfeatureref_constructor_exists():
    assert callable(gbind_dsl_ConceptFeatureRef.__init__)


def test_gbind_dsl_conceptfeatureref_constructor_args():
    sig = inspect.signature(gbind_dsl_ConceptFeatureRef.__init__)
    params = list(sig.parameters.keys())
    assert "featureName" in params, "Missing parameter 'featureName'"

def test_gbind_dsl_conceptfeatureref_has_featureName():
    assert hasattr(gbind_dsl_ConceptFeatureRef, "featureName")
    descriptor = None
    for klass in gbind_dsl_ConceptFeatureRef.__mro__:
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



def test_virtualfeature_is_not_abstract():
    assert not inspect.isabstract(VirtualFeature)


def test_virtualfeature_constructor_exists():
    assert callable(VirtualFeature.__init__)


def test_virtualfeature_constructor_args():
    sig = inspect.signature(VirtualFeature.__init__)
    params = list(sig.parameters.keys())



def test_gbind_dsl_virtualattribute_is_not_abstract():
    assert not inspect.isabstract(gbind_dsl_VirtualAttribute)


def test_gbind_dsl_virtualattribute_constructor_exists():
    assert callable(gbind_dsl_VirtualAttribute.__init__)


def test_gbind_dsl_virtualattribute_constructor_args():
    sig = inspect.signature(gbind_dsl_VirtualAttribute.__init__)
    params = list(sig.parameters.keys())



def test_gbind_dsl_virtualreference_is_not_abstract():
    assert not inspect.isabstract(gbind_dsl_VirtualReference)


def test_gbind_dsl_virtualreference_constructor_exists():
    assert callable(gbind_dsl_VirtualReference.__init__)


def test_gbind_dsl_virtualreference_constructor_args():
    sig = inspect.signature(gbind_dsl_VirtualReference.__init__)
    params = list(sig.parameters.keys())



def test_gbind_dsl_virtualfeature_is_not_abstract():
    assert not inspect.isabstract(gbind_dsl_VirtualFeature)


def test_gbind_dsl_virtualfeature_constructor_exists():
    assert callable(gbind_dsl_VirtualFeature.__init__)


def test_gbind_dsl_virtualfeature_constructor_args():
    sig = inspect.signature(gbind_dsl_VirtualFeature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gbind_dsl_virtualfeature_has_name():
    assert hasattr(gbind_dsl_VirtualFeature, "name")
    descriptor = None
    for klass in gbind_dsl_VirtualFeature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



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



def test_gbind_dsl_concepthelper_is_not_abstract():
    assert not inspect.isabstract(gbind_dsl_ConceptHelper)


def test_gbind_dsl_concepthelper_constructor_exists():
    assert callable(gbind_dsl_ConceptHelper.__init__)


def test_gbind_dsl_concepthelper_constructor_args():
    sig = inspect.signature(gbind_dsl_ConceptHelper.__init__)
    params = list(sig.parameters.keys())



def test_gbind_dsl_localhelper_is_not_abstract():
    assert not inspect.isabstract(gbind_dsl_LocalHelper)


def test_gbind_dsl_localhelper_constructor_exists():
    assert callable(gbind_dsl_LocalHelper.__init__)


def test_gbind_dsl_localhelper_constructor_args():
    sig = inspect.signature(gbind_dsl_LocalHelper.__init__)
    params = list(sig.parameters.keys())



def test_conceptbinding_is_not_abstract():
    assert not inspect.isabstract(ConceptBinding)


def test_conceptbinding_constructor_exists():
    assert callable(ConceptBinding.__init__)


def test_conceptbinding_constructor_args():
    sig = inspect.signature(ConceptBinding.__init__)
    params = list(sig.parameters.keys())



def test_gbind_dsl_basefeaturebinding_is_not_abstract():
    assert not inspect.isabstract(gbind_dsl_BaseFeatureBinding)


def test_gbind_dsl_basefeaturebinding_constructor_exists():
    assert callable(gbind_dsl_BaseFeatureBinding.__init__)


def test_gbind_dsl_basefeaturebinding_constructor_args():
    sig = inspect.signature(gbind_dsl_BaseFeatureBinding.__init__)
    params = list(sig.parameters.keys())
    assert "conceptFeature" in params, "Missing parameter 'conceptFeature'"

def test_gbind_dsl_basefeaturebinding_has_conceptFeature():
    assert hasattr(gbind_dsl_BaseFeatureBinding, "conceptFeature")
    descriptor = None
    for klass in gbind_dsl_BaseFeatureBinding.__mro__:
        if "conceptFeature" in klass.__dict__:
            descriptor = klass.__dict__["conceptFeature"]
            break
    assert isinstance(descriptor, property)



def test_gbind_dsl_virtualclassbinding_is_not_abstract():
    assert not inspect.isabstract(gbind_dsl_VirtualClassBinding)


def test_gbind_dsl_virtualclassbinding_constructor_exists():
    assert callable(gbind_dsl_VirtualClassBinding.__init__)


def test_gbind_dsl_virtualclassbinding_constructor_args():
    sig = inspect.signature(gbind_dsl_VirtualClassBinding.__init__)
    params = list(sig.parameters.keys())



def test_gbind_dsl_intermediateclassbinding_is_not_abstract():
    assert not inspect.isabstract(gbind_dsl_IntermediateClassBinding)


def test_gbind_dsl_intermediateclassbinding_constructor_exists():
    assert callable(gbind_dsl_IntermediateClassBinding.__init__)


def test_gbind_dsl_intermediateclassbinding_constructor_args():
    sig = inspect.signature(gbind_dsl_IntermediateClassBinding.__init__)
    params = list(sig.parameters.keys())
    assert "conceptReferenceName" in params, "Missing parameter 'conceptReferenceName'"

def test_gbind_dsl_intermediateclassbinding_has_conceptReferenceName():
    assert hasattr(gbind_dsl_IntermediateClassBinding, "conceptReferenceName")
    descriptor = None
    for klass in gbind_dsl_IntermediateClassBinding.__mro__:
        if "conceptReferenceName" in klass.__dict__:
            descriptor = klass.__dict__["conceptReferenceName"]
            break
    assert isinstance(descriptor, property)



def test_gbind_dsl_bindingmodel_is_not_abstract():
    assert not inspect.isabstract(gbind_dsl_BindingModel)


def test_gbind_dsl_bindingmodel_constructor_exists():
    assert callable(gbind_dsl_BindingModel.__init__)


def test_gbind_dsl_bindingmodel_constructor_args():
    sig = inspect.signature(gbind_dsl_BindingModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gbind_dsl_bindingmodel_has_name():
    assert hasattr(gbind_dsl_BindingModel, "name")
    descriptor = None
    for klass in gbind_dsl_BindingModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gbind_dsl_classbinding_is_not_abstract():
    assert not inspect.isabstract(gbind_dsl_ClassBinding)


def test_gbind_dsl_classbinding_constructor_exists():
    assert callable(gbind_dsl_ClassBinding.__init__)


def test_gbind_dsl_classbinding_constructor_args():
    sig = inspect.signature(gbind_dsl_ClassBinding.__init__)
    params = list(sig.parameters.keys())



def test_bindingmodel_is_not_abstract():
    assert not inspect.isabstract(BindingModel)


def test_bindingmodel_constructor_exists():
    assert callable(BindingModel.__init__)


def test_bindingmodel_constructor_args():
    sig = inspect.signature(BindingModel.__init__)
    params = list(sig.parameters.keys())



def test_gbind_dsl_conceptbinding_is_not_abstract():
    assert not inspect.isabstract(gbind_dsl_ConceptBinding)


def test_gbind_dsl_conceptbinding_constructor_exists():
    assert callable(gbind_dsl_ConceptBinding.__init__)


def test_gbind_dsl_conceptbinding_constructor_args():
    sig = inspect.signature(gbind_dsl_ConceptBinding.__init__)
    params = list(sig.parameters.keys())
    assert "debugName" in params, "Missing parameter 'debugName'"

def test_gbind_dsl_conceptbinding_has_debugName():
    assert hasattr(gbind_dsl_ConceptBinding, "debugName")
    descriptor = None
    for klass in gbind_dsl_ConceptBinding.__mro__:
        if "debugName" in klass.__dict__:
            descriptor = klass.__dict__["debugName"]
            break
    assert isinstance(descriptor, property)



def test_metaclass_is_not_abstract():
    assert not inspect.isabstract(Metaclass)


def test_metaclass_constructor_exists():
    assert callable(Metaclass.__init__)


def test_metaclass_constructor_args():
    sig = inspect.signature(Metaclass.__init__)
    params = list(sig.parameters.keys())



def test_gbind_dsl_concretemetaclass_is_not_abstract():
    assert not inspect.isabstract(gbind_dsl_ConcreteMetaclass)


def test_gbind_dsl_concretemetaclass_constructor_exists():
    assert callable(gbind_dsl_ConcreteMetaclass.__init__)


def test_gbind_dsl_concretemetaclass_constructor_args():
    sig = inspect.signature(gbind_dsl_ConcreteMetaclass.__init__)
    params = list(sig.parameters.keys())



def test_gbind_dsl_virtualmetaclass_is_not_abstract():
    assert not inspect.isabstract(gbind_dsl_VirtualMetaclass)


def test_gbind_dsl_virtualmetaclass_constructor_exists():
    assert callable(gbind_dsl_VirtualMetaclass.__init__)


def test_gbind_dsl_virtualmetaclass_constructor_args():
    sig = inspect.signature(gbind_dsl_VirtualMetaclass.__init__)
    params = list(sig.parameters.keys())



def test_gbind_dsl_conceptmetaclass_is_not_abstract():
    assert not inspect.isabstract(gbind_dsl_ConceptMetaclass)


def test_gbind_dsl_conceptmetaclass_constructor_exists():
    assert callable(gbind_dsl_ConceptMetaclass.__init__)


def test_gbind_dsl_conceptmetaclass_constructor_args():
    sig = inspect.signature(gbind_dsl_ConceptMetaclass.__init__)
    params = list(sig.parameters.keys())



def test_dsl_gbind_eclass_is_not_abstract():
    assert not inspect.isabstract(dsl_gbind_EClass)


def test_dsl_gbind_eclass_constructor_exists():
    assert callable(dsl_gbind_EClass.__init__)


def test_dsl_gbind_eclass_constructor_args():
    sig = inspect.signature(dsl_gbind_EClass.__init__)
    params = list(sig.parameters.keys())



def test_gbind_dsl_metaclass_is_not_abstract():
    assert not inspect.isabstract(gbind_dsl_Metaclass)


def test_gbind_dsl_metaclass_constructor_exists():
    assert callable(gbind_dsl_Metaclass.__init__)


def test_gbind_dsl_metaclass_constructor_args():
    sig = inspect.signature(gbind_dsl_Metaclass.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gbind_dsl_metaclass_has_name():
    assert hasattr(gbind_dsl_Metaclass, "name")
    descriptor = None
    for klass in gbind_dsl_Metaclass.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gbind_dsl_bindingoptions_is_not_abstract():
    assert not inspect.isabstract(gbind_dsl_BindingOptions)


def test_gbind_dsl_bindingoptions_constructor_exists():
    assert callable(gbind_dsl_BindingOptions.__init__)


def test_gbind_dsl_bindingoptions_constructor_args():
    sig = inspect.signature(gbind_dsl_BindingOptions.__init__)
    params = list(sig.parameters.keys())
    assert "enableClassMerge" in params, "Missing parameter 'enableClassMerge'"

def test_gbind_dsl_bindingoptions_has_enableClassMerge():
    assert hasattr(gbind_dsl_BindingOptions, "enableClassMerge")
    descriptor = None
    for klass in gbind_dsl_BindingOptions.__mro__:
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



def test_oclfeaturedefinition_is_not_abstract():
    assert not inspect.isabstract(OclFeatureDefinition)


def test_oclfeaturedefinition_constructor_exists():
    assert callable(OclFeatureDefinition.__init__)


def test_oclfeaturedefinition_constructor_args():
    sig = inspect.signature(OclFeatureDefinition.__init__)
    params = list(sig.parameters.keys())



def test_oclfeature_is_not_abstract():
    assert not inspect.isabstract(OclFeature)


def test_oclfeature_constructor_exists():
    assert callable(OclFeature.__init__)


def test_oclfeature_constructor_args():
    sig = inspect.signature(OclFeature.__init__)
    params = list(sig.parameters.keys())



def test_oclinstancemodel_is_not_abstract():
    assert not inspect.isabstract(OclInstanceModel)


def test_oclinstancemodel_constructor_exists():
    assert callable(OclInstanceModel.__init__)


def test_oclinstancemodel_constructor_args():
    sig = inspect.signature(OclInstanceModel.__init__)
    params = list(sig.parameters.keys())



def test_oclmodelelement_is_not_abstract():
    assert not inspect.isabstract(OclModelElement)


def test_oclmodelelement_constructor_exists():
    assert callable(OclModelElement.__init__)


def test_oclmodelelement_constructor_args():
    sig = inspect.signature(OclModelElement.__init__)
    params = list(sig.parameters.keys())



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_gbind_simpleocl_operation_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_Operation)


def test_gbind_simpleocl_operation_constructor_exists():
    assert callable(gbind_simpleocl_Operation.__init__)


def test_gbind_simpleocl_operation_constructor_args():
    sig = inspect.signature(gbind_simpleocl_Operation.__init__)
    params = list(sig.parameters.keys())



def test_gbind_simpleocl_attribute_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_Attribute)


def test_gbind_simpleocl_attribute_constructor_exists():
    assert callable(gbind_simpleocl_Attribute.__init__)


def test_gbind_simpleocl_attribute_constructor_args():
    sig = inspect.signature(gbind_simpleocl_Attribute.__init__)
    params = list(sig.parameters.keys())



def test_numerictype_is_not_abstract():
    assert not inspect.isabstract(NumericType)


def test_numerictype_constructor_exists():
    assert callable(NumericType.__init__)


def test_numerictype_constructor_args():
    sig = inspect.signature(NumericType.__init__)
    params = list(sig.parameters.keys())



def test_gbind_simpleocl_integertype_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_IntegerType)


def test_gbind_simpleocl_integertype_constructor_exists():
    assert callable(gbind_simpleocl_IntegerType.__init__)


def test_gbind_simpleocl_integertype_constructor_args():
    sig = inspect.signature(gbind_simpleocl_IntegerType.__init__)
    params = list(sig.parameters.keys())



def test_primitive_is_not_abstract():
    assert not inspect.isabstract(Primitive)


def test_primitive_constructor_exists():
    assert callable(Primitive.__init__)


def test_primitive_constructor_args():
    sig = inspect.signature(Primitive.__init__)
    params = list(sig.parameters.keys())



def test_gbind_simpleocl_numerictype_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_NumericType)


def test_gbind_simpleocl_numerictype_constructor_exists():
    assert callable(gbind_simpleocl_NumericType.__init__)


def test_gbind_simpleocl_numerictype_constructor_args():
    sig = inspect.signature(gbind_simpleocl_NumericType.__init__)
    params = list(sig.parameters.keys())



def test_gbind_simpleocl_booleantype_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_BooleanType)


def test_gbind_simpleocl_booleantype_constructor_exists():
    assert callable(gbind_simpleocl_BooleanType.__init__)


def test_gbind_simpleocl_booleantype_constructor_args():
    sig = inspect.signature(gbind_simpleocl_BooleanType.__init__)
    params = list(sig.parameters.keys())



def test_gbind_simpleocl_stringtype_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_StringType)


def test_gbind_simpleocl_stringtype_constructor_exists():
    assert callable(gbind_simpleocl_StringType.__init__)


def test_gbind_simpleocl_stringtype_constructor_args():
    sig = inspect.signature(gbind_simpleocl_StringType.__init__)
    params = list(sig.parameters.keys())



def test_oclmodel_is_not_abstract():
    assert not inspect.isabstract(OclModel)


def test_oclmodel_constructor_exists():
    assert callable(OclModel.__init__)


def test_oclmodel_constructor_args():
    sig = inspect.signature(OclModel.__init__)
    params = list(sig.parameters.keys())



def test_gbind_simpleocl_oclinstancemodel_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_OclInstanceModel)


def test_gbind_simpleocl_oclinstancemodel_constructor_exists():
    assert callable(gbind_simpleocl_OclInstanceModel.__init__)


def test_gbind_simpleocl_oclinstancemodel_constructor_args():
    sig = inspect.signature(gbind_simpleocl_OclInstanceModel.__init__)
    params = list(sig.parameters.keys())



def test_gbind_simpleocl_oclmetamodel_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_OclMetamodel)


def test_gbind_simpleocl_oclmetamodel_constructor_exists():
    assert callable(gbind_simpleocl_OclMetamodel.__init__)


def test_gbind_simpleocl_oclmetamodel_constructor_args():
    sig = inspect.signature(gbind_simpleocl_OclMetamodel.__init__)
    params = list(sig.parameters.keys())
    assert "uri" in params, "Missing parameter 'uri'"

def test_gbind_simpleocl_oclmetamodel_has_uri():
    assert hasattr(gbind_simpleocl_OclMetamodel, "uri")
    descriptor = None
    for klass in gbind_simpleocl_OclMetamodel.__mro__:
        if "uri" in klass.__dict__:
            descriptor = klass.__dict__["uri"]
            break
    assert isinstance(descriptor, property)



def test_lambdatype_is_not_abstract():
    assert not inspect.isabstract(LambdaType)


def test_lambdatype_constructor_exists():
    assert callable(LambdaType.__init__)


def test_lambdatype_constructor_args():
    sig = inspect.signature(LambdaType.__init__)
    params = list(sig.parameters.keys())



def test_tupletype_is_not_abstract():
    assert not inspect.isabstract(TupleType)


def test_tupletype_constructor_exists():
    assert callable(TupleType.__init__)


def test_tupletype_constructor_args():
    sig = inspect.signature(TupleType.__init__)
    params = list(sig.parameters.keys())



def test_gbind_simpleocl_realtype_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_RealType)


def test_gbind_simpleocl_realtype_constructor_exists():
    assert callable(gbind_simpleocl_RealType.__init__)


def test_gbind_simpleocl_realtype_constructor_args():
    sig = inspect.signature(gbind_simpleocl_RealType.__init__)
    params = list(sig.parameters.keys())



def test_iterateexp_is_not_abstract():
    assert not inspect.isabstract(IterateExp)


def test_iterateexp_constructor_exists():
    assert callable(IterateExp.__init__)


def test_iterateexp_constructor_args():
    sig = inspect.signature(IterateExp.__init__)
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



def test_gbind_simpleocl_settype_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_SetType)


def test_gbind_simpleocl_settype_constructor_exists():
    assert callable(gbind_simpleocl_SetType.__init__)


def test_gbind_simpleocl_settype_constructor_args():
    sig = inspect.signature(gbind_simpleocl_SetType.__init__)
    params = list(sig.parameters.keys())



def test_gbind_simpleocl_bagtype_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_BagType)


def test_gbind_simpleocl_bagtype_constructor_exists():
    assert callable(gbind_simpleocl_BagType.__init__)


def test_gbind_simpleocl_bagtype_constructor_args():
    sig = inspect.signature(gbind_simpleocl_BagType.__init__)
    params = list(sig.parameters.keys())



def test_gbind_simpleocl_orderedsettype_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_OrderedSetType)


def test_gbind_simpleocl_orderedsettype_constructor_exists():
    assert callable(gbind_simpleocl_OrderedSetType.__init__)


def test_gbind_simpleocl_orderedsettype_constructor_args():
    sig = inspect.signature(gbind_simpleocl_OrderedSetType.__init__)
    params = list(sig.parameters.keys())



def test_gbind_simpleocl_sequencetype_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_SequenceType)


def test_gbind_simpleocl_sequencetype_constructor_exists():
    assert callable(gbind_simpleocl_SequenceType.__init__)


def test_gbind_simpleocl_sequencetype_constructor_args():
    sig = inspect.signature(gbind_simpleocl_SequenceType.__init__)
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



def test_variableexp_is_not_abstract():
    assert not inspect.isabstract(VariableExp)


def test_variableexp_constructor_exists():
    assert callable(VariableExp.__init__)


def test_variableexp_constructor_args():
    sig = inspect.signature(VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_gbind_simpleocl_lambdacallexp_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_LambdaCallExp)


def test_gbind_simpleocl_lambdacallexp_constructor_exists():
    assert callable(gbind_simpleocl_LambdaCallExp.__init__)


def test_gbind_simpleocl_lambdacallexp_constructor_args():
    sig = inspect.signature(gbind_simpleocl_LambdaCallExp.__init__)
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



def test_gbind_simpleocl_staticoperationcall_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_StaticOperationCall)


def test_gbind_simpleocl_staticoperationcall_constructor_exists():
    assert callable(gbind_simpleocl_StaticOperationCall.__init__)


def test_gbind_simpleocl_staticoperationcall_constructor_args():
    sig = inspect.signature(gbind_simpleocl_StaticOperationCall.__init__)
    params = list(sig.parameters.keys())
    assert "operationName" in params, "Missing parameter 'operationName'"

def test_gbind_simpleocl_staticoperationcall_has_operationName():
    assert hasattr(gbind_simpleocl_StaticOperationCall, "operationName")
    descriptor = None
    for klass in gbind_simpleocl_StaticOperationCall.__mro__:
        if "operationName" in klass.__dict__:
            descriptor = klass.__dict__["operationName"]
            break
    assert isinstance(descriptor, property)



def test_gbind_simpleocl_staticnavigationorattributecall_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_StaticNavigationOrAttributeCall)


def test_gbind_simpleocl_staticnavigationorattributecall_constructor_exists():
    assert callable(gbind_simpleocl_StaticNavigationOrAttributeCall.__init__)


def test_gbind_simpleocl_staticnavigationorattributecall_constructor_args():
    sig = inspect.signature(gbind_simpleocl_StaticNavigationOrAttributeCall.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gbind_simpleocl_staticnavigationorattributecall_has_name():
    assert hasattr(gbind_simpleocl_StaticNavigationOrAttributeCall, "name")
    descriptor = None
    for klass in gbind_simpleocl_StaticNavigationOrAttributeCall.__mro__:
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



def test_gbind_simpleocl_navigationorattributecall_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_NavigationOrAttributeCall)


def test_gbind_simpleocl_navigationorattributecall_constructor_exists():
    assert callable(gbind_simpleocl_NavigationOrAttributeCall.__init__)


def test_gbind_simpleocl_navigationorattributecall_constructor_args():
    sig = inspect.signature(gbind_simpleocl_NavigationOrAttributeCall.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gbind_simpleocl_navigationorattributecall_has_name():
    assert hasattr(gbind_simpleocl_NavigationOrAttributeCall, "name")
    descriptor = None
    for klass in gbind_simpleocl_NavigationOrAttributeCall.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gbind_simpleocl_operationcall_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_OperationCall)


def test_gbind_simpleocl_operationcall_constructor_exists():
    assert callable(gbind_simpleocl_OperationCall.__init__)


def test_gbind_simpleocl_operationcall_constructor_args():
    sig = inspect.signature(gbind_simpleocl_OperationCall.__init__)
    params = list(sig.parameters.keys())
    assert "operationName" in params, "Missing parameter 'operationName'"

def test_gbind_simpleocl_operationcall_has_operationName():
    assert hasattr(gbind_simpleocl_OperationCall, "operationName")
    descriptor = None
    for klass in gbind_simpleocl_OperationCall.__mro__:
        if "operationName" in klass.__dict__:
            descriptor = klass.__dict__["operationName"]
            break
    assert isinstance(descriptor, property)



def test_gbind_simpleocl_loopexp_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_LoopExp)


def test_gbind_simpleocl_loopexp_constructor_exists():
    assert callable(gbind_simpleocl_LoopExp.__init__)


def test_gbind_simpleocl_loopexp_constructor_args():
    sig = inspect.signature(gbind_simpleocl_LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_numericexp_is_not_abstract():
    assert not inspect.isabstract(NumericExp)


def test_numericexp_constructor_exists():
    assert callable(NumericExp.__init__)


def test_numericexp_constructor_args():
    sig = inspect.signature(NumericExp.__init__)
    params = list(sig.parameters.keys())



def test_gbind_simpleocl_realexp_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_RealExp)


def test_gbind_simpleocl_realexp_constructor_exists():
    assert callable(gbind_simpleocl_RealExp.__init__)


def test_gbind_simpleocl_realexp_constructor_args():
    sig = inspect.signature(gbind_simpleocl_RealExp.__init__)
    params = list(sig.parameters.keys())
    assert "realSymbol" in params, "Missing parameter 'realSymbol'"

def test_gbind_simpleocl_realexp_has_realSymbol():
    assert hasattr(gbind_simpleocl_RealExp, "realSymbol")
    descriptor = None
    for klass in gbind_simpleocl_RealExp.__mro__:
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



def test_gbind_simpleocl_booleanexp_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_BooleanExp)


def test_gbind_simpleocl_booleanexp_constructor_exists():
    assert callable(gbind_simpleocl_BooleanExp.__init__)


def test_gbind_simpleocl_booleanexp_constructor_args():
    sig = inspect.signature(gbind_simpleocl_BooleanExp.__init__)
    params = list(sig.parameters.keys())
    assert "booleanSymbol" in params, "Missing parameter 'booleanSymbol'"

def test_gbind_simpleocl_booleanexp_has_booleanSymbol():
    assert hasattr(gbind_simpleocl_BooleanExp, "booleanSymbol")
    descriptor = None
    for klass in gbind_simpleocl_BooleanExp.__mro__:
        if "booleanSymbol" in klass.__dict__:
            descriptor = klass.__dict__["booleanSymbol"]
            break
    assert isinstance(descriptor, property)



def test_gbind_simpleocl_numericexp_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_NumericExp)


def test_gbind_simpleocl_numericexp_constructor_exists():
    assert callable(gbind_simpleocl_NumericExp.__init__)


def test_gbind_simpleocl_numericexp_constructor_args():
    sig = inspect.signature(gbind_simpleocl_NumericExp.__init__)
    params = list(sig.parameters.keys())



def test_gbind_simpleocl_stringexp_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_StringExp)


def test_gbind_simpleocl_stringexp_constructor_exists():
    assert callable(gbind_simpleocl_StringExp.__init__)


def test_gbind_simpleocl_stringexp_constructor_args():
    sig = inspect.signature(gbind_simpleocl_StringExp.__init__)
    params = list(sig.parameters.keys())
    assert "stringSymbol" in params, "Missing parameter 'stringSymbol'"

def test_gbind_simpleocl_stringexp_has_stringSymbol():
    assert hasattr(gbind_simpleocl_StringExp, "stringSymbol")
    descriptor = None
    for klass in gbind_simpleocl_StringExp.__mro__:
        if "stringSymbol" in klass.__dict__:
            descriptor = klass.__dict__["stringSymbol"]
            break
    assert isinstance(descriptor, property)



def test_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(VariableDeclaration)


def test_variabledeclaration_constructor_exists():
    assert callable(VariableDeclaration.__init__)


def test_variabledeclaration_constructor_args():
    sig = inspect.signature(VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_gbind_simpleocl_parameter_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_Parameter)


def test_gbind_simpleocl_parameter_constructor_exists():
    assert callable(gbind_simpleocl_Parameter.__init__)


def test_gbind_simpleocl_parameter_constructor_args():
    sig = inspect.signature(gbind_simpleocl_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_gbind_dsl_helperparameter_is_not_abstract():
    assert not inspect.isabstract(gbind_dsl_HelperParameter)


def test_gbind_dsl_helperparameter_constructor_exists():
    assert callable(gbind_dsl_HelperParameter.__init__)


def test_gbind_dsl_helperparameter_constructor_args():
    sig = inspect.signature(gbind_dsl_HelperParameter.__init__)
    params = list(sig.parameters.keys())



def test_gbind_simpleocl_localvariable_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_LocalVariable)


def test_gbind_simpleocl_localvariable_constructor_exists():
    assert callable(gbind_simpleocl_LocalVariable.__init__)


def test_gbind_simpleocl_localvariable_constructor_args():
    sig = inspect.signature(gbind_simpleocl_LocalVariable.__init__)
    params = list(sig.parameters.keys())
    assert "eq" in params, "Missing parameter 'eq'"

def test_gbind_simpleocl_localvariable_has_eq():
    assert hasattr(gbind_simpleocl_LocalVariable, "eq")
    descriptor = None
    for klass in gbind_simpleocl_LocalVariable.__mro__:
        if "eq" in klass.__dict__:
            descriptor = klass.__dict__["eq"]
            break
    assert isinstance(descriptor, property)



def test_gbind_dsl_concretereferencdeclaringvar_is_not_abstract():
    assert not inspect.isabstract(gbind_dsl_ConcreteReferencDeclaringVar)


def test_gbind_dsl_concretereferencdeclaringvar_constructor_exists():
    assert callable(gbind_dsl_ConcreteReferencDeclaringVar.__init__)


def test_gbind_dsl_concretereferencdeclaringvar_constructor_args():
    sig = inspect.signature(gbind_dsl_ConcreteReferencDeclaringVar.__init__)
    params = list(sig.parameters.keys())



def test_gbind_simpleocl_iterator_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_Iterator)


def test_gbind_simpleocl_iterator_constructor_exists():
    assert callable(gbind_simpleocl_Iterator.__init__)


def test_gbind_simpleocl_iterator_constructor_args():
    sig = inspect.signature(gbind_simpleocl_Iterator.__init__)
    params = list(sig.parameters.keys())



def test_oclexpression_is_not_abstract():
    assert not inspect.isabstract(OclExpression)


def test_oclexpression_constructor_exists():
    assert callable(OclExpression.__init__)


def test_oclexpression_constructor_args():
    sig = inspect.signature(OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_gbind_simpleocl_braceexp_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_BraceExp)


def test_gbind_simpleocl_braceexp_constructor_exists():
    assert callable(gbind_simpleocl_BraceExp.__init__)


def test_gbind_simpleocl_braceexp_constructor_args():
    sig = inspect.signature(gbind_simpleocl_BraceExp.__init__)
    params = list(sig.parameters.keys())



def test_gbind_simpleocl_ifexp_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_IfExp)


def test_gbind_simpleocl_ifexp_constructor_exists():
    assert callable(gbind_simpleocl_IfExp.__init__)


def test_gbind_simpleocl_ifexp_constructor_args():
    sig = inspect.signature(gbind_simpleocl_IfExp.__init__)
    params = list(sig.parameters.keys())



def test_gbind_simpleocl_staticpropertycallexp_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_StaticPropertyCallExp)


def test_gbind_simpleocl_staticpropertycallexp_constructor_exists():
    assert callable(gbind_simpleocl_StaticPropertyCallExp.__init__)


def test_gbind_simpleocl_staticpropertycallexp_constructor_args():
    sig = inspect.signature(gbind_simpleocl_StaticPropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_gbind_simpleocl_superexp_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_SuperExp)


def test_gbind_simpleocl_superexp_constructor_exists():
    assert callable(gbind_simpleocl_SuperExp.__init__)


def test_gbind_simpleocl_superexp_constructor_args():
    sig = inspect.signature(gbind_simpleocl_SuperExp.__init__)
    params = list(sig.parameters.keys())



def test_gbind_simpleocl_propertycallexp_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_PropertyCallExp)


def test_gbind_simpleocl_propertycallexp_constructor_exists():
    assert callable(gbind_simpleocl_PropertyCallExp.__init__)


def test_gbind_simpleocl_propertycallexp_constructor_args():
    sig = inspect.signature(gbind_simpleocl_PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_gbind_simpleocl_envexp_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_EnvExp)


def test_gbind_simpleocl_envexp_constructor_exists():
    assert callable(gbind_simpleocl_EnvExp.__init__)


def test_gbind_simpleocl_envexp_constructor_args():
    sig = inspect.signature(gbind_simpleocl_EnvExp.__init__)
    params = list(sig.parameters.keys())



def test_gbind_simpleocl_letexp_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_LetExp)


def test_gbind_simpleocl_letexp_constructor_exists():
    assert callable(gbind_simpleocl_LetExp.__init__)


def test_gbind_simpleocl_letexp_constructor_args():
    sig = inspect.signature(gbind_simpleocl_LetExp.__init__)
    params = list(sig.parameters.keys())



def test_gbind_simpleocl_operatorcallexp_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_OperatorCallExp)


def test_gbind_simpleocl_operatorcallexp_constructor_exists():
    assert callable(gbind_simpleocl_OperatorCallExp.__init__)


def test_gbind_simpleocl_operatorcallexp_constructor_args():
    sig = inspect.signature(gbind_simpleocl_OperatorCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "operationName" in params, "Missing parameter 'operationName'"

def test_gbind_simpleocl_operatorcallexp_has_operationName():
    assert hasattr(gbind_simpleocl_OperatorCallExp, "operationName")
    descriptor = None
    for klass in gbind_simpleocl_OperatorCallExp.__mro__:
        if "operationName" in klass.__dict__:
            descriptor = klass.__dict__["operationName"]
            break
    assert isinstance(descriptor, property)



def test_gbind_simpleocl_primitiveexp_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_PrimitiveExp)


def test_gbind_simpleocl_primitiveexp_constructor_exists():
    assert callable(gbind_simpleocl_PrimitiveExp.__init__)


def test_gbind_simpleocl_primitiveexp_constructor_args():
    sig = inspect.signature(gbind_simpleocl_PrimitiveExp.__init__)
    params = list(sig.parameters.keys())



def test_gbind_simpleocl_oclundefinedexp_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_OclUndefinedExp)


def test_gbind_simpleocl_oclundefinedexp_constructor_exists():
    assert callable(gbind_simpleocl_OclUndefinedExp.__init__)


def test_gbind_simpleocl_oclundefinedexp_constructor_args():
    sig = inspect.signature(gbind_simpleocl_OclUndefinedExp.__init__)
    params = list(sig.parameters.keys())



def test_gbind_simpleocl_oclmodelelementexp_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_OclModelElementExp)


def test_gbind_simpleocl_oclmodelelementexp_constructor_exists():
    assert callable(gbind_simpleocl_OclModelElementExp.__init__)


def test_gbind_simpleocl_oclmodelelementexp_constructor_args():
    sig = inspect.signature(gbind_simpleocl_OclModelElementExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gbind_simpleocl_oclmodelelementexp_has_name():
    assert hasattr(gbind_simpleocl_OclModelElementExp, "name")
    descriptor = None
    for klass in gbind_simpleocl_OclModelElementExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gbind_simpleocl_selfexp_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_SelfExp)


def test_gbind_simpleocl_selfexp_constructor_exists():
    assert callable(gbind_simpleocl_SelfExp.__init__)


def test_gbind_simpleocl_selfexp_constructor_args():
    sig = inspect.signature(gbind_simpleocl_SelfExp.__init__)
    params = list(sig.parameters.keys())



def test_gbind_simpleocl_variableexp_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_VariableExp)


def test_gbind_simpleocl_variableexp_constructor_exists():
    assert callable(gbind_simpleocl_VariableExp.__init__)


def test_gbind_simpleocl_variableexp_constructor_args():
    sig = inspect.signature(gbind_simpleocl_VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_gbind_simpleocl_enumliteralexp_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_EnumLiteralExp)


def test_gbind_simpleocl_enumliteralexp_constructor_exists():
    assert callable(gbind_simpleocl_EnumLiteralExp.__init__)


def test_gbind_simpleocl_enumliteralexp_constructor_args():
    sig = inspect.signature(gbind_simpleocl_EnumLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gbind_simpleocl_enumliteralexp_has_name():
    assert hasattr(gbind_simpleocl_EnumLiteralExp, "name")
    descriptor = None
    for klass in gbind_simpleocl_EnumLiteralExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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



def test_gbind_simpleocl_mapexp_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_MapExp)


def test_gbind_simpleocl_mapexp_constructor_exists():
    assert callable(gbind_simpleocl_MapExp.__init__)


def test_gbind_simpleocl_mapexp_constructor_args():
    sig = inspect.signature(gbind_simpleocl_MapExp.__init__)
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



def test_gbind_simpleocl_tupleexp_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_TupleExp)


def test_gbind_simpleocl_tupleexp_constructor_exists():
    assert callable(gbind_simpleocl_TupleExp.__init__)


def test_gbind_simpleocl_tupleexp_constructor_args():
    sig = inspect.signature(gbind_simpleocl_TupleExp.__init__)
    params = list(sig.parameters.keys())



def test_gbind_simpleocl_collectionexp_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_CollectionExp)


def test_gbind_simpleocl_collectionexp_constructor_exists():
    assert callable(gbind_simpleocl_CollectionExp.__init__)


def test_gbind_simpleocl_collectionexp_constructor_args():
    sig = inspect.signature(gbind_simpleocl_CollectionExp.__init__)
    params = list(sig.parameters.keys())



def test_gbind_simpleocl_integerexp_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_IntegerExp)


def test_gbind_simpleocl_integerexp_constructor_exists():
    assert callable(gbind_simpleocl_IntegerExp.__init__)


def test_gbind_simpleocl_integerexp_constructor_args():
    sig = inspect.signature(gbind_simpleocl_IntegerExp.__init__)
    params = list(sig.parameters.keys())
    assert "integerSymbol" in params, "Missing parameter 'integerSymbol'"

def test_gbind_simpleocl_integerexp_has_integerSymbol():
    assert hasattr(gbind_simpleocl_IntegerExp, "integerSymbol")
    descriptor = None
    for klass in gbind_simpleocl_IntegerExp.__mro__:
        if "integerSymbol" in klass.__dict__:
            descriptor = klass.__dict__["integerSymbol"]
            break
    assert isinstance(descriptor, property)



def test_module_is_not_abstract():
    assert not inspect.isabstract(Module)


def test_module_constructor_exists():
    assert callable(Module.__init__)


def test_module_constructor_args():
    sig = inspect.signature(Module.__init__)
    params = list(sig.parameters.keys())



def test_moduleelement_is_not_abstract():
    assert not inspect.isabstract(ModuleElement)


def test_moduleelement_constructor_exists():
    assert callable(ModuleElement.__init__)


def test_moduleelement_constructor_args():
    sig = inspect.signature(ModuleElement.__init__)
    params = list(sig.parameters.keys())



def test_gbind_simpleocl_oclfeaturedefinition_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_OclFeatureDefinition)


def test_gbind_simpleocl_oclfeaturedefinition_constructor_exists():
    assert callable(gbind_simpleocl_OclFeatureDefinition.__init__)


def test_gbind_simpleocl_oclfeaturedefinition_constructor_args():
    sig = inspect.signature(gbind_simpleocl_OclFeatureDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"

def test_gbind_simpleocl_oclfeaturedefinition_has_static():
    assert hasattr(gbind_simpleocl_OclFeatureDefinition, "static")
    descriptor = None
    for klass in gbind_simpleocl_OclFeatureDefinition.__mro__:
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



def test_gbind_dsl_metamodeldeclaration_is_not_abstract():
    assert not inspect.isabstract(gbind_dsl_MetamodelDeclaration)


def test_gbind_dsl_metamodeldeclaration_constructor_exists():
    assert callable(gbind_dsl_MetamodelDeclaration.__init__)


def test_gbind_dsl_metamodeldeclaration_constructor_args():
    sig = inspect.signature(gbind_dsl_MetamodelDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "metamodelURI" in params, "Missing parameter 'metamodelURI'"

def test_gbind_dsl_metamodeldeclaration_has_metamodelURI():
    assert hasattr(gbind_dsl_MetamodelDeclaration, "metamodelURI")
    descriptor = None
    for klass in gbind_dsl_MetamodelDeclaration.__mro__:
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



def test_gbind_simpleocl_oclfeature_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_OclFeature)


def test_gbind_simpleocl_oclfeature_constructor_exists():
    assert callable(gbind_simpleocl_OclFeature.__init__)


def test_gbind_simpleocl_oclfeature_constructor_args():
    sig = inspect.signature(gbind_simpleocl_OclFeature.__init__)
    params = list(sig.parameters.keys())
    assert "eq" in params, "Missing parameter 'eq'"

def test_gbind_simpleocl_oclfeature_has_eq():
    assert hasattr(gbind_simpleocl_OclFeature, "eq")
    descriptor = None
    for klass in gbind_simpleocl_OclFeature.__mro__:
        if "eq" in klass.__dict__:
            descriptor = klass.__dict__["eq"]
            break
    assert isinstance(descriptor, property)



def test_gbind_simpleocl_oclmodel_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_OclModel)


def test_gbind_simpleocl_oclmodel_constructor_exists():
    assert callable(gbind_simpleocl_OclModel.__init__)


def test_gbind_simpleocl_oclmodel_constructor_args():
    sig = inspect.signature(gbind_simpleocl_OclModel.__init__)
    params = list(sig.parameters.keys())



def test_gbind_simpleocl_module_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_Module)


def test_gbind_simpleocl_module_constructor_exists():
    assert callable(gbind_simpleocl_Module.__init__)


def test_gbind_simpleocl_module_constructor_args():
    sig = inspect.signature(gbind_simpleocl_Module.__init__)
    params = list(sig.parameters.keys())



def test_locatedelement_is_not_abstract():
    assert not inspect.isabstract(LocatedElement)


def test_locatedelement_constructor_exists():
    assert callable(LocatedElement.__init__)


def test_locatedelement_constructor_args():
    sig = inspect.signature(LocatedElement.__init__)
    params = list(sig.parameters.keys())



def test_gbind_simpleocl_oclcontextdefinition_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_OclContextDefinition)


def test_gbind_simpleocl_oclcontextdefinition_constructor_exists():
    assert callable(gbind_simpleocl_OclContextDefinition.__init__)


def test_gbind_simpleocl_oclcontextdefinition_constructor_args():
    sig = inspect.signature(gbind_simpleocl_OclContextDefinition.__init__)
    params = list(sig.parameters.keys())



def test_gbind_simpleocl_moduleelement_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_ModuleElement)


def test_gbind_simpleocl_moduleelement_constructor_exists():
    assert callable(gbind_simpleocl_ModuleElement.__init__)


def test_gbind_simpleocl_moduleelement_constructor_args():
    sig = inspect.signature(gbind_simpleocl_ModuleElement.__init__)
    params = list(sig.parameters.keys())



def test_gbind_simpleocl_mapelement_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_MapElement)


def test_gbind_simpleocl_mapelement_constructor_exists():
    assert callable(gbind_simpleocl_MapElement.__init__)


def test_gbind_simpleocl_mapelement_constructor_args():
    sig = inspect.signature(gbind_simpleocl_MapElement.__init__)
    params = list(sig.parameters.keys())



def test_gbind_simpleocl_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_VariableDeclaration)


def test_gbind_simpleocl_variabledeclaration_constructor_exists():
    assert callable(gbind_simpleocl_VariableDeclaration.__init__)


def test_gbind_simpleocl_variabledeclaration_constructor_args():
    sig = inspect.signature(gbind_simpleocl_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"

def test_gbind_simpleocl_variabledeclaration_has_varName():
    assert hasattr(gbind_simpleocl_VariableDeclaration, "varName")
    descriptor = None
    for klass in gbind_simpleocl_VariableDeclaration.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_gbind_simpleocl_propertycall_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_PropertyCall)


def test_gbind_simpleocl_propertycall_constructor_exists():
    assert callable(gbind_simpleocl_PropertyCall.__init__)


def test_gbind_simpleocl_propertycall_constructor_args():
    sig = inspect.signature(gbind_simpleocl_PropertyCall.__init__)
    params = list(sig.parameters.keys())



def test_gbind_simpleocl_staticpropertycall_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_StaticPropertyCall)


def test_gbind_simpleocl_staticpropertycall_constructor_exists():
    assert callable(gbind_simpleocl_StaticPropertyCall.__init__)


def test_gbind_simpleocl_staticpropertycall_constructor_args():
    sig = inspect.signature(gbind_simpleocl_StaticPropertyCall.__init__)
    params = list(sig.parameters.keys())



def test_gbind_simpleocl_ocltype_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_OclType)


def test_gbind_simpleocl_ocltype_constructor_exists():
    assert callable(gbind_simpleocl_OclType.__init__)


def test_gbind_simpleocl_ocltype_constructor_args():
    sig = inspect.signature(gbind_simpleocl_OclType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gbind_simpleocl_ocltype_has_name():
    assert hasattr(gbind_simpleocl_OclType, "name")
    descriptor = None
    for klass in gbind_simpleocl_OclType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gbind_simpleocl_tupletypeattribute_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_TupleTypeAttribute)


def test_gbind_simpleocl_tupletypeattribute_constructor_exists():
    assert callable(gbind_simpleocl_TupleTypeAttribute.__init__)


def test_gbind_simpleocl_tupletypeattribute_constructor_args():
    sig = inspect.signature(gbind_simpleocl_TupleTypeAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gbind_simpleocl_tupletypeattribute_has_name():
    assert hasattr(gbind_simpleocl_TupleTypeAttribute, "name")
    descriptor = None
    for klass in gbind_simpleocl_TupleTypeAttribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gbind_simpleocl_namedelement_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_NamedElement)


def test_gbind_simpleocl_namedelement_constructor_exists():
    assert callable(gbind_simpleocl_NamedElement.__init__)


def test_gbind_simpleocl_namedelement_constructor_args():
    sig = inspect.signature(gbind_simpleocl_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gbind_simpleocl_namedelement_has_name():
    assert hasattr(gbind_simpleocl_NamedElement, "name")
    descriptor = None
    for klass in gbind_simpleocl_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_operatorcallexp_is_not_abstract():
    assert not inspect.isabstract(OperatorCallExp)


def test_operatorcallexp_constructor_exists():
    assert callable(OperatorCallExp.__init__)


def test_operatorcallexp_constructor_args():
    sig = inspect.signature(OperatorCallExp.__init__)
    params = list(sig.parameters.keys())



def test_gbind_simpleocl_eqopcallexp_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_EqOpCallExp)


def test_gbind_simpleocl_eqopcallexp_constructor_exists():
    assert callable(gbind_simpleocl_EqOpCallExp.__init__)


def test_gbind_simpleocl_eqopcallexp_constructor_args():
    sig = inspect.signature(gbind_simpleocl_EqOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_gbind_simpleocl_mulopcallexp_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_MulOpCallExp)


def test_gbind_simpleocl_mulopcallexp_constructor_exists():
    assert callable(gbind_simpleocl_MulOpCallExp.__init__)


def test_gbind_simpleocl_mulopcallexp_constructor_args():
    sig = inspect.signature(gbind_simpleocl_MulOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_gbind_simpleocl_notopcallexp_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_NotOpCallExp)


def test_gbind_simpleocl_notopcallexp_constructor_exists():
    assert callable(gbind_simpleocl_NotOpCallExp.__init__)


def test_gbind_simpleocl_notopcallexp_constructor_args():
    sig = inspect.signature(gbind_simpleocl_NotOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_gbind_simpleocl_intopcallexp_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_IntOpCallExp)


def test_gbind_simpleocl_intopcallexp_constructor_exists():
    assert callable(gbind_simpleocl_IntOpCallExp.__init__)


def test_gbind_simpleocl_intopcallexp_constructor_args():
    sig = inspect.signature(gbind_simpleocl_IntOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_gbind_simpleocl_relopcallexp_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_RelOpCallExp)


def test_gbind_simpleocl_relopcallexp_constructor_exists():
    assert callable(gbind_simpleocl_RelOpCallExp.__init__)


def test_gbind_simpleocl_relopcallexp_constructor_args():
    sig = inspect.signature(gbind_simpleocl_RelOpCallExp.__init__)
    params = list(sig.parameters.keys())



def test_gbind_simpleocl_addopcallexp_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_AddOpCallExp)


def test_gbind_simpleocl_addopcallexp_constructor_exists():
    assert callable(gbind_simpleocl_AddOpCallExp.__init__)


def test_gbind_simpleocl_addopcallexp_constructor_args():
    sig = inspect.signature(gbind_simpleocl_AddOpCallExp.__init__)
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



def test_gbind_simpleocl_tuplepart_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_TuplePart)


def test_gbind_simpleocl_tuplepart_constructor_exists():
    assert callable(gbind_simpleocl_TuplePart.__init__)


def test_gbind_simpleocl_tuplepart_constructor_args():
    sig = inspect.signature(gbind_simpleocl_TuplePart.__init__)
    params = list(sig.parameters.keys())



def test_operationcall_is_not_abstract():
    assert not inspect.isabstract(OperationCall)


def test_operationcall_constructor_exists():
    assert callable(OperationCall.__init__)


def test_operationcall_constructor_args():
    sig = inspect.signature(OperationCall.__init__)
    params = list(sig.parameters.keys())



def test_gbind_simpleocl_collectionoperationcall_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_CollectionOperationCall)


def test_gbind_simpleocl_collectionoperationcall_constructor_exists():
    assert callable(gbind_simpleocl_CollectionOperationCall.__init__)


def test_gbind_simpleocl_collectionoperationcall_constructor_args():
    sig = inspect.signature(gbind_simpleocl_CollectionOperationCall.__init__)
    params = list(sig.parameters.keys())



def test_loopexp_is_not_abstract():
    assert not inspect.isabstract(LoopExp)


def test_loopexp_constructor_exists():
    assert callable(LoopExp.__init__)


def test_loopexp_constructor_args():
    sig = inspect.signature(LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_gbind_simpleocl_iterateexp_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_IterateExp)


def test_gbind_simpleocl_iterateexp_constructor_exists():
    assert callable(gbind_simpleocl_IterateExp.__init__)


def test_gbind_simpleocl_iterateexp_constructor_args():
    sig = inspect.signature(gbind_simpleocl_IterateExp.__init__)
    params = list(sig.parameters.keys())



def test_gbind_simpleocl_iteratorexp_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_IteratorExp)


def test_gbind_simpleocl_iteratorexp_constructor_exists():
    assert callable(gbind_simpleocl_IteratorExp.__init__)


def test_gbind_simpleocl_iteratorexp_constructor_args():
    sig = inspect.signature(gbind_simpleocl_IteratorExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gbind_simpleocl_iteratorexp_has_name():
    assert hasattr(gbind_simpleocl_IteratorExp, "name")
    descriptor = None
    for klass in gbind_simpleocl_IteratorExp.__mro__:
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



def test_gbind_simpleocl_setexp_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_SetExp)


def test_gbind_simpleocl_setexp_constructor_exists():
    assert callable(gbind_simpleocl_SetExp.__init__)


def test_gbind_simpleocl_setexp_constructor_args():
    sig = inspect.signature(gbind_simpleocl_SetExp.__init__)
    params = list(sig.parameters.keys())



def test_gbind_simpleocl_orderedsetexp_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_OrderedSetExp)


def test_gbind_simpleocl_orderedsetexp_constructor_exists():
    assert callable(gbind_simpleocl_OrderedSetExp.__init__)


def test_gbind_simpleocl_orderedsetexp_constructor_args():
    sig = inspect.signature(gbind_simpleocl_OrderedSetExp.__init__)
    params = list(sig.parameters.keys())



def test_gbind_simpleocl_bagexp_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_BagExp)


def test_gbind_simpleocl_bagexp_constructor_exists():
    assert callable(gbind_simpleocl_BagExp.__init__)


def test_gbind_simpleocl_bagexp_constructor_args():
    sig = inspect.signature(gbind_simpleocl_BagExp.__init__)
    params = list(sig.parameters.keys())



def test_gbind_simpleocl_sequenceexp_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_SequenceExp)


def test_gbind_simpleocl_sequenceexp_constructor_exists():
    assert callable(gbind_simpleocl_SequenceExp.__init__)


def test_gbind_simpleocl_sequenceexp_constructor_args():
    sig = inspect.signature(gbind_simpleocl_SequenceExp.__init__)
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



def test_gbind_simpleocl_envtype_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_EnvType)


def test_gbind_simpleocl_envtype_constructor_exists():
    assert callable(gbind_simpleocl_EnvType.__init__)


def test_gbind_simpleocl_envtype_constructor_args():
    sig = inspect.signature(gbind_simpleocl_EnvType.__init__)
    params = list(sig.parameters.keys())



def test_gbind_simpleocl_collectiontype_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_CollectionType)


def test_gbind_simpleocl_collectiontype_constructor_exists():
    assert callable(gbind_simpleocl_CollectionType.__init__)


def test_gbind_simpleocl_collectiontype_constructor_args():
    sig = inspect.signature(gbind_simpleocl_CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_gbind_simpleocl_lambdatype_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_LambdaType)


def test_gbind_simpleocl_lambdatype_constructor_exists():
    assert callable(gbind_simpleocl_LambdaType.__init__)


def test_gbind_simpleocl_lambdatype_constructor_args():
    sig = inspect.signature(gbind_simpleocl_LambdaType.__init__)
    params = list(sig.parameters.keys())



def test_gbind_simpleocl_oclmodelelement_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_OclModelElement)


def test_gbind_simpleocl_oclmodelelement_constructor_exists():
    assert callable(gbind_simpleocl_OclModelElement.__init__)


def test_gbind_simpleocl_oclmodelelement_constructor_args():
    sig = inspect.signature(gbind_simpleocl_OclModelElement.__init__)
    params = list(sig.parameters.keys())



def test_gbind_simpleocl_maptype_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_MapType)


def test_gbind_simpleocl_maptype_constructor_exists():
    assert callable(gbind_simpleocl_MapType.__init__)


def test_gbind_simpleocl_maptype_constructor_args():
    sig = inspect.signature(gbind_simpleocl_MapType.__init__)
    params = list(sig.parameters.keys())



def test_gbind_simpleocl_tupletype_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_TupleType)


def test_gbind_simpleocl_tupletype_constructor_exists():
    assert callable(gbind_simpleocl_TupleType.__init__)


def test_gbind_simpleocl_tupletype_constructor_args():
    sig = inspect.signature(gbind_simpleocl_TupleType.__init__)
    params = list(sig.parameters.keys())



def test_gbind_simpleocl_oclanytype_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_OclAnyType)


def test_gbind_simpleocl_oclanytype_constructor_exists():
    assert callable(gbind_simpleocl_OclAnyType.__init__)


def test_gbind_simpleocl_oclanytype_constructor_args():
    sig = inspect.signature(gbind_simpleocl_OclAnyType.__init__)
    params = list(sig.parameters.keys())



def test_gbind_simpleocl_primitive_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_Primitive)


def test_gbind_simpleocl_primitive_constructor_exists():
    assert callable(gbind_simpleocl_Primitive.__init__)


def test_gbind_simpleocl_primitive_constructor_args():
    sig = inspect.signature(gbind_simpleocl_Primitive.__init__)
    params = list(sig.parameters.keys())



def test_gbind_simpleocl_oclexpression_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_OclExpression)


def test_gbind_simpleocl_oclexpression_constructor_exists():
    assert callable(gbind_simpleocl_OclExpression.__init__)


def test_gbind_simpleocl_oclexpression_constructor_args():
    sig = inspect.signature(gbind_simpleocl_OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_gbind_simpleocl_import_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_Import)


def test_gbind_simpleocl_import_constructor_exists():
    assert callable(gbind_simpleocl_Import.__init__)


def test_gbind_simpleocl_import_constructor_args():
    sig = inspect.signature(gbind_simpleocl_Import.__init__)
    params = list(sig.parameters.keys())



def test_gbind_simpleocl_locatedelement_is_not_abstract():
    assert not inspect.isabstract(gbind_simpleocl_LocatedElement)


def test_gbind_simpleocl_locatedelement_constructor_exists():
    assert callable(gbind_simpleocl_LocatedElement.__init__)


def test_gbind_simpleocl_locatedelement_constructor_args():
    sig = inspect.signature(gbind_simpleocl_LocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "charStart" in params, "Missing parameter 'charStart'"
    assert "column" in params, "Missing parameter 'column'"
    assert "line" in params, "Missing parameter 'line'"
    assert "charEnd" in params, "Missing parameter 'charEnd'"

def test_gbind_simpleocl_locatedelement_has_charStart():
    assert hasattr(gbind_simpleocl_LocatedElement, "charStart")
    descriptor = None
    for klass in gbind_simpleocl_LocatedElement.__mro__:
        if "charStart" in klass.__dict__:
            descriptor = klass.__dict__["charStart"]
            break
    assert isinstance(descriptor, property)

def test_gbind_simpleocl_locatedelement_has_column():
    assert hasattr(gbind_simpleocl_LocatedElement, "column")
    descriptor = None
    for klass in gbind_simpleocl_LocatedElement.__mro__:
        if "column" in klass.__dict__:
            descriptor = klass.__dict__["column"]
            break
    assert isinstance(descriptor, property)

def test_gbind_simpleocl_locatedelement_has_line():
    assert hasattr(gbind_simpleocl_LocatedElement, "line")
    descriptor = None
    for klass in gbind_simpleocl_LocatedElement.__mro__:
        if "line" in klass.__dict__:
            descriptor = klass.__dict__["line"]
            break
    assert isinstance(descriptor, property)

def test_gbind_simpleocl_locatedelement_has_charEnd():
    assert hasattr(gbind_simpleocl_LocatedElement, "charEnd")
    descriptor = None
    for klass in gbind_simpleocl_LocatedElement.__mro__:
        if "charEnd" in klass.__dict__:
            descriptor = klass.__dict__["charEnd"]
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
gbind_dsl_BaseHelper_strategy = st.builds(
    gbind_dsl_BaseHelper,
    feature=
        safe_text
)
HelperParameter_strategy = st.builds(
    HelperParameter,
)
VirtualAttribute_strategy = st.builds(
    VirtualAttribute,
)
VirtualReference_strategy = st.builds(
    VirtualReference,
)
BaseFeatureBinding_strategy = st.builds(
    BaseFeatureBinding,
)
gbind_dsl_OclFeatureBinding_strategy = st.builds(
    gbind_dsl_OclFeatureBinding,
)
ConcreteReferencDeclaringVar_strategy = st.builds(
    ConcreteReferencDeclaringVar,
)
gbind_dsl_RenamingFeatureBinding_strategy = st.builds(
    gbind_dsl_RenamingFeatureBinding,
    concreteFeature=
        safe_text
)
gbind_dsl_ConceptFeatureRef_strategy = st.builds(
    gbind_dsl_ConceptFeatureRef,
    featureName=
        safe_text
)
ConceptFeatureRef_strategy = st.builds(
    ConceptFeatureRef,
)
VirtualFeature_strategy = st.builds(
    VirtualFeature,
)
gbind_dsl_VirtualAttribute_strategy = st.builds(
    gbind_dsl_VirtualAttribute,
)
gbind_dsl_VirtualReference_strategy = st.builds(
    gbind_dsl_VirtualReference,
)
gbind_dsl_VirtualFeature_strategy = st.builds(
    gbind_dsl_VirtualFeature,
    name=
        safe_text
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
gbind_dsl_ConceptHelper_strategy = st.builds(
    gbind_dsl_ConceptHelper,
)
gbind_dsl_LocalHelper_strategy = st.builds(
    gbind_dsl_LocalHelper,
)
ConceptBinding_strategy = st.builds(
    ConceptBinding,
)
gbind_dsl_BaseFeatureBinding_strategy = st.builds(
    gbind_dsl_BaseFeatureBinding,
    conceptFeature=
        safe_text
)
gbind_dsl_VirtualClassBinding_strategy = st.builds(
    gbind_dsl_VirtualClassBinding,
)
gbind_dsl_IntermediateClassBinding_strategy = st.builds(
    gbind_dsl_IntermediateClassBinding,
    conceptReferenceName=
        safe_text
)
gbind_dsl_BindingModel_strategy = st.builds(
    gbind_dsl_BindingModel,
    name=
        safe_text
)
gbind_dsl_ClassBinding_strategy = st.builds(
    gbind_dsl_ClassBinding,
)
BindingModel_strategy = st.builds(
    BindingModel,
)
gbind_dsl_ConceptBinding_strategy = st.builds(
    gbind_dsl_ConceptBinding,
    debugName=
        safe_text
)
Metaclass_strategy = st.builds(
    Metaclass,
)
gbind_dsl_ConcreteMetaclass_strategy = st.builds(
    gbind_dsl_ConcreteMetaclass,
)
gbind_dsl_VirtualMetaclass_strategy = st.builds(
    gbind_dsl_VirtualMetaclass,
)
gbind_dsl_ConceptMetaclass_strategy = st.builds(
    gbind_dsl_ConceptMetaclass,
)
dsl_gbind_EClass_strategy = st.builds(
    dsl_gbind_EClass,
)
gbind_dsl_Metaclass_strategy = st.builds(
    gbind_dsl_Metaclass,
    name=
        safe_text
)
gbind_dsl_BindingOptions_strategy = st.builds(
    gbind_dsl_BindingOptions,
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
OclFeatureDefinition_strategy = st.builds(
    OclFeatureDefinition,
)
OclFeature_strategy = st.builds(
    OclFeature,
)
OclInstanceModel_strategy = st.builds(
    OclInstanceModel,
)
OclModelElement_strategy = st.builds(
    OclModelElement,
)
Parameter_strategy = st.builds(
    Parameter,
)
gbind_simpleocl_Operation_strategy = st.builds(
    gbind_simpleocl_Operation,
)
gbind_simpleocl_Attribute_strategy = st.builds(
    gbind_simpleocl_Attribute,
)
NumericType_strategy = st.builds(
    NumericType,
)
gbind_simpleocl_IntegerType_strategy = st.builds(
    gbind_simpleocl_IntegerType,
)
Primitive_strategy = st.builds(
    Primitive,
)
gbind_simpleocl_NumericType_strategy = st.builds(
    gbind_simpleocl_NumericType,
)
gbind_simpleocl_BooleanType_strategy = st.builds(
    gbind_simpleocl_BooleanType,
)
gbind_simpleocl_StringType_strategy = st.builds(
    gbind_simpleocl_StringType,
)
OclModel_strategy = st.builds(
    OclModel,
)
gbind_simpleocl_OclInstanceModel_strategy = st.builds(
    gbind_simpleocl_OclInstanceModel,
)
gbind_simpleocl_OclMetamodel_strategy = st.builds(
    gbind_simpleocl_OclMetamodel,
    uri=
        safe_text
)
LambdaType_strategy = st.builds(
    LambdaType,
)
TupleType_strategy = st.builds(
    TupleType,
)
gbind_simpleocl_RealType_strategy = st.builds(
    gbind_simpleocl_RealType,
)
IterateExp_strategy = st.builds(
    IterateExp,
)
TupleTypeAttribute_strategy = st.builds(
    TupleTypeAttribute,
)
CollectionType_strategy = st.builds(
    CollectionType,
)
gbind_simpleocl_SetType_strategy = st.builds(
    gbind_simpleocl_SetType,
)
gbind_simpleocl_BagType_strategy = st.builds(
    gbind_simpleocl_BagType,
)
gbind_simpleocl_OrderedSetType_strategy = st.builds(
    gbind_simpleocl_OrderedSetType,
)
gbind_simpleocl_SequenceType_strategy = st.builds(
    gbind_simpleocl_SequenceType,
)
MapType_strategy = st.builds(
    MapType,
)
OclContextDefinition_strategy = st.builds(
    OclContextDefinition,
)
VariableExp_strategy = st.builds(
    VariableExp,
)
gbind_simpleocl_LambdaCallExp_strategy = st.builds(
    gbind_simpleocl_LambdaCallExp,
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
gbind_simpleocl_StaticOperationCall_strategy = st.builds(
    gbind_simpleocl_StaticOperationCall,
    operationName=
        safe_text
)
gbind_simpleocl_StaticNavigationOrAttributeCall_strategy = st.builds(
    gbind_simpleocl_StaticNavigationOrAttributeCall,
    name=
        safe_text
)
PropertyCall_strategy = st.builds(
    PropertyCall,
)
gbind_simpleocl_NavigationOrAttributeCall_strategy = st.builds(
    gbind_simpleocl_NavigationOrAttributeCall,
    name=
        safe_text
)
gbind_simpleocl_OperationCall_strategy = st.builds(
    gbind_simpleocl_OperationCall,
    operationName=
        safe_text
)
gbind_simpleocl_LoopExp_strategy = st.builds(
    gbind_simpleocl_LoopExp,
)
NumericExp_strategy = st.builds(
    NumericExp,
)
gbind_simpleocl_RealExp_strategy = st.builds(
    gbind_simpleocl_RealExp,
    realSymbol=
        safe_text
)
PrimitiveExp_strategy = st.builds(
    PrimitiveExp,
)
gbind_simpleocl_BooleanExp_strategy = st.builds(
    gbind_simpleocl_BooleanExp,
    booleanSymbol=
        safe_text
)
gbind_simpleocl_NumericExp_strategy = st.builds(
    gbind_simpleocl_NumericExp,
)
gbind_simpleocl_StringExp_strategy = st.builds(
    gbind_simpleocl_StringExp,
    stringSymbol=
        safe_text
)
VariableDeclaration_strategy = st.builds(
    VariableDeclaration,
)
gbind_simpleocl_Parameter_strategy = st.builds(
    gbind_simpleocl_Parameter,
)
gbind_dsl_HelperParameter_strategy = st.builds(
    gbind_dsl_HelperParameter,
)
gbind_simpleocl_LocalVariable_strategy = st.builds(
    gbind_simpleocl_LocalVariable,
    eq=
        safe_text
)
gbind_dsl_ConcreteReferencDeclaringVar_strategy = st.builds(
    gbind_dsl_ConcreteReferencDeclaringVar,
)
gbind_simpleocl_Iterator_strategy = st.builds(
    gbind_simpleocl_Iterator,
)
OclExpression_strategy = st.builds(
    OclExpression,
)
gbind_simpleocl_BraceExp_strategy = st.builds(
    gbind_simpleocl_BraceExp,
)
gbind_simpleocl_IfExp_strategy = st.builds(
    gbind_simpleocl_IfExp,
)
gbind_simpleocl_StaticPropertyCallExp_strategy = st.builds(
    gbind_simpleocl_StaticPropertyCallExp,
)
gbind_simpleocl_SuperExp_strategy = st.builds(
    gbind_simpleocl_SuperExp,
)
gbind_simpleocl_PropertyCallExp_strategy = st.builds(
    gbind_simpleocl_PropertyCallExp,
)
gbind_simpleocl_EnvExp_strategy = st.builds(
    gbind_simpleocl_EnvExp,
)
gbind_simpleocl_LetExp_strategy = st.builds(
    gbind_simpleocl_LetExp,
)
gbind_simpleocl_OperatorCallExp_strategy = st.builds(
    gbind_simpleocl_OperatorCallExp,
    operationName=
        safe_text
)
gbind_simpleocl_PrimitiveExp_strategy = st.builds(
    gbind_simpleocl_PrimitiveExp,
)
gbind_simpleocl_OclUndefinedExp_strategy = st.builds(
    gbind_simpleocl_OclUndefinedExp,
)
gbind_simpleocl_OclModelElementExp_strategy = st.builds(
    gbind_simpleocl_OclModelElementExp,
    name=
        safe_text
)
gbind_simpleocl_SelfExp_strategy = st.builds(
    gbind_simpleocl_SelfExp,
)
gbind_simpleocl_VariableExp_strategy = st.builds(
    gbind_simpleocl_VariableExp,
)
gbind_simpleocl_EnumLiteralExp_strategy = st.builds(
    gbind_simpleocl_EnumLiteralExp,
    name=
        safe_text
)
MapExp_strategy = st.builds(
    MapExp,
)
MapElement_strategy = st.builds(
    MapElement,
)
gbind_simpleocl_MapExp_strategy = st.builds(
    gbind_simpleocl_MapExp,
)
TupleExp_strategy = st.builds(
    TupleExp,
)
TuplePart_strategy = st.builds(
    TuplePart,
)
gbind_simpleocl_TupleExp_strategy = st.builds(
    gbind_simpleocl_TupleExp,
)
gbind_simpleocl_CollectionExp_strategy = st.builds(
    gbind_simpleocl_CollectionExp,
)
gbind_simpleocl_IntegerExp_strategy = st.builds(
    gbind_simpleocl_IntegerExp,
    integerSymbol=
        safe_text
)
Module_strategy = st.builds(
    Module,
)
ModuleElement_strategy = st.builds(
    ModuleElement,
)
gbind_simpleocl_OclFeatureDefinition_strategy = st.builds(
    gbind_simpleocl_OclFeatureDefinition,
    static=
        safe_text
)
Import_strategy = st.builds(
    Import,
)
OclMetamodel_strategy = st.builds(
    OclMetamodel,
)
gbind_dsl_MetamodelDeclaration_strategy = st.builds(
    gbind_dsl_MetamodelDeclaration,
    metamodelURI=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
gbind_simpleocl_OclFeature_strategy = st.builds(
    gbind_simpleocl_OclFeature,
    eq=
        safe_text
)
gbind_simpleocl_OclModel_strategy = st.builds(
    gbind_simpleocl_OclModel,
)
gbind_simpleocl_Module_strategy = st.builds(
    gbind_simpleocl_Module,
)
LocatedElement_strategy = st.builds(
    LocatedElement,
)
gbind_simpleocl_OclContextDefinition_strategy = st.builds(
    gbind_simpleocl_OclContextDefinition,
)
gbind_simpleocl_ModuleElement_strategy = st.builds(
    gbind_simpleocl_ModuleElement,
)
gbind_simpleocl_MapElement_strategy = st.builds(
    gbind_simpleocl_MapElement,
)
gbind_simpleocl_VariableDeclaration_strategy = st.builds(
    gbind_simpleocl_VariableDeclaration,
    varName=
        safe_text
)
gbind_simpleocl_PropertyCall_strategy = st.builds(
    gbind_simpleocl_PropertyCall,
)
gbind_simpleocl_StaticPropertyCall_strategy = st.builds(
    gbind_simpleocl_StaticPropertyCall,
)
gbind_simpleocl_OclType_strategy = st.builds(
    gbind_simpleocl_OclType,
    name=
        safe_text
)
gbind_simpleocl_TupleTypeAttribute_strategy = st.builds(
    gbind_simpleocl_TupleTypeAttribute,
    name=
        safe_text
)
gbind_simpleocl_NamedElement_strategy = st.builds(
    gbind_simpleocl_NamedElement,
    name=
        safe_text
)
OperatorCallExp_strategy = st.builds(
    OperatorCallExp,
)
gbind_simpleocl_EqOpCallExp_strategy = st.builds(
    gbind_simpleocl_EqOpCallExp,
)
gbind_simpleocl_MulOpCallExp_strategy = st.builds(
    gbind_simpleocl_MulOpCallExp,
)
gbind_simpleocl_NotOpCallExp_strategy = st.builds(
    gbind_simpleocl_NotOpCallExp,
)
gbind_simpleocl_IntOpCallExp_strategy = st.builds(
    gbind_simpleocl_IntOpCallExp,
)
gbind_simpleocl_RelOpCallExp_strategy = st.builds(
    gbind_simpleocl_RelOpCallExp,
)
gbind_simpleocl_AddOpCallExp_strategy = st.builds(
    gbind_simpleocl_AddOpCallExp,
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
gbind_simpleocl_TuplePart_strategy = st.builds(
    gbind_simpleocl_TuplePart,
)
OperationCall_strategy = st.builds(
    OperationCall,
)
gbind_simpleocl_CollectionOperationCall_strategy = st.builds(
    gbind_simpleocl_CollectionOperationCall,
)
LoopExp_strategy = st.builds(
    LoopExp,
)
gbind_simpleocl_IterateExp_strategy = st.builds(
    gbind_simpleocl_IterateExp,
)
gbind_simpleocl_IteratorExp_strategy = st.builds(
    gbind_simpleocl_IteratorExp,
    name=
        safe_text
)
LetExp_strategy = st.builds(
    LetExp,
)
CollectionExp_strategy = st.builds(
    CollectionExp,
)
gbind_simpleocl_SetExp_strategy = st.builds(
    gbind_simpleocl_SetExp,
)
gbind_simpleocl_OrderedSetExp_strategy = st.builds(
    gbind_simpleocl_OrderedSetExp,
)
gbind_simpleocl_BagExp_strategy = st.builds(
    gbind_simpleocl_BagExp,
)
gbind_simpleocl_SequenceExp_strategy = st.builds(
    gbind_simpleocl_SequenceExp,
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
gbind_simpleocl_EnvType_strategy = st.builds(
    gbind_simpleocl_EnvType,
)
gbind_simpleocl_CollectionType_strategy = st.builds(
    gbind_simpleocl_CollectionType,
)
gbind_simpleocl_LambdaType_strategy = st.builds(
    gbind_simpleocl_LambdaType,
)
gbind_simpleocl_OclModelElement_strategy = st.builds(
    gbind_simpleocl_OclModelElement,
)
gbind_simpleocl_MapType_strategy = st.builds(
    gbind_simpleocl_MapType,
)
gbind_simpleocl_TupleType_strategy = st.builds(
    gbind_simpleocl_TupleType,
)
gbind_simpleocl_OclAnyType_strategy = st.builds(
    gbind_simpleocl_OclAnyType,
)
gbind_simpleocl_Primitive_strategy = st.builds(
    gbind_simpleocl_Primitive,
)
gbind_simpleocl_OclExpression_strategy = st.builds(
    gbind_simpleocl_OclExpression,
)
gbind_simpleocl_Import_strategy = st.builds(
    gbind_simpleocl_Import,
)
gbind_simpleocl_LocatedElement_strategy = st.builds(
    gbind_simpleocl_LocatedElement,
    charStart=
        safe_text,
    column=
        safe_text,
    line=
        safe_text,
    charEnd=
        safe_text
)

@given(instance=gbind_dsl_BaseHelper_strategy)
@settings(max_examples=50)
def test_gbind_dsl_basehelper_instantiation(instance):
    assert isinstance(instance, gbind_dsl_BaseHelper)



@given(instance=gbind_dsl_BaseHelper_strategy)
def test_gbind_dsl_basehelper_feature_setter(instance):
    original = instance.feature
    instance.feature = original
    assert instance.feature == original

@given(instance=HelperParameter_strategy)
@settings(max_examples=50)
def test_helperparameter_instantiation(instance):
    assert isinstance(instance, HelperParameter)

@given(instance=VirtualAttribute_strategy)
@settings(max_examples=50)
def test_virtualattribute_instantiation(instance):
    assert isinstance(instance, VirtualAttribute)

@given(instance=VirtualReference_strategy)
@settings(max_examples=50)
def test_virtualreference_instantiation(instance):
    assert isinstance(instance, VirtualReference)

@given(instance=BaseFeatureBinding_strategy)
@settings(max_examples=50)
def test_basefeaturebinding_instantiation(instance):
    assert isinstance(instance, BaseFeatureBinding)

@given(instance=gbind_dsl_OclFeatureBinding_strategy)
@settings(max_examples=50)
def test_gbind_dsl_oclfeaturebinding_instantiation(instance):
    assert isinstance(instance, gbind_dsl_OclFeatureBinding)

@given(instance=ConcreteReferencDeclaringVar_strategy)
@settings(max_examples=50)
def test_concretereferencdeclaringvar_instantiation(instance):
    assert isinstance(instance, ConcreteReferencDeclaringVar)

@given(instance=gbind_dsl_RenamingFeatureBinding_strategy)
@settings(max_examples=50)
def test_gbind_dsl_renamingfeaturebinding_instantiation(instance):
    assert isinstance(instance, gbind_dsl_RenamingFeatureBinding)



@given(instance=gbind_dsl_RenamingFeatureBinding_strategy)
def test_gbind_dsl_renamingfeaturebinding_concreteFeature_setter(instance):
    original = instance.concreteFeature
    instance.concreteFeature = original
    assert instance.concreteFeature == original

@given(instance=gbind_dsl_ConceptFeatureRef_strategy)
@settings(max_examples=50)
def test_gbind_dsl_conceptfeatureref_instantiation(instance):
    assert isinstance(instance, gbind_dsl_ConceptFeatureRef)



@given(instance=gbind_dsl_ConceptFeatureRef_strategy)
def test_gbind_dsl_conceptfeatureref_featureName_setter(instance):
    original = instance.featureName
    instance.featureName = original
    assert instance.featureName == original

@given(instance=ConceptFeatureRef_strategy)
@settings(max_examples=50)
def test_conceptfeatureref_instantiation(instance):
    assert isinstance(instance, ConceptFeatureRef)

@given(instance=VirtualFeature_strategy)
@settings(max_examples=50)
def test_virtualfeature_instantiation(instance):
    assert isinstance(instance, VirtualFeature)

@given(instance=gbind_dsl_VirtualAttribute_strategy)
@settings(max_examples=50)
def test_gbind_dsl_virtualattribute_instantiation(instance):
    assert isinstance(instance, gbind_dsl_VirtualAttribute)

@given(instance=gbind_dsl_VirtualReference_strategy)
@settings(max_examples=50)
def test_gbind_dsl_virtualreference_instantiation(instance):
    assert isinstance(instance, gbind_dsl_VirtualReference)

@given(instance=gbind_dsl_VirtualFeature_strategy)
@settings(max_examples=50)
def test_gbind_dsl_virtualfeature_instantiation(instance):
    assert isinstance(instance, gbind_dsl_VirtualFeature)



@given(instance=gbind_dsl_VirtualFeature_strategy)
def test_gbind_dsl_virtualfeature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

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

@given(instance=gbind_dsl_ConceptHelper_strategy)
@settings(max_examples=50)
def test_gbind_dsl_concepthelper_instantiation(instance):
    assert isinstance(instance, gbind_dsl_ConceptHelper)

@given(instance=gbind_dsl_LocalHelper_strategy)
@settings(max_examples=50)
def test_gbind_dsl_localhelper_instantiation(instance):
    assert isinstance(instance, gbind_dsl_LocalHelper)

@given(instance=ConceptBinding_strategy)
@settings(max_examples=50)
def test_conceptbinding_instantiation(instance):
    assert isinstance(instance, ConceptBinding)

@given(instance=gbind_dsl_BaseFeatureBinding_strategy)
@settings(max_examples=50)
def test_gbind_dsl_basefeaturebinding_instantiation(instance):
    assert isinstance(instance, gbind_dsl_BaseFeatureBinding)



@given(instance=gbind_dsl_BaseFeatureBinding_strategy)
def test_gbind_dsl_basefeaturebinding_conceptFeature_setter(instance):
    original = instance.conceptFeature
    instance.conceptFeature = original
    assert instance.conceptFeature == original

@given(instance=gbind_dsl_VirtualClassBinding_strategy)
@settings(max_examples=50)
def test_gbind_dsl_virtualclassbinding_instantiation(instance):
    assert isinstance(instance, gbind_dsl_VirtualClassBinding)

@given(instance=gbind_dsl_IntermediateClassBinding_strategy)
@settings(max_examples=50)
def test_gbind_dsl_intermediateclassbinding_instantiation(instance):
    assert isinstance(instance, gbind_dsl_IntermediateClassBinding)



@given(instance=gbind_dsl_IntermediateClassBinding_strategy)
def test_gbind_dsl_intermediateclassbinding_conceptReferenceName_setter(instance):
    original = instance.conceptReferenceName
    instance.conceptReferenceName = original
    assert instance.conceptReferenceName == original

@given(instance=gbind_dsl_BindingModel_strategy)
@settings(max_examples=50)
def test_gbind_dsl_bindingmodel_instantiation(instance):
    assert isinstance(instance, gbind_dsl_BindingModel)



@given(instance=gbind_dsl_BindingModel_strategy)
def test_gbind_dsl_bindingmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gbind_dsl_ClassBinding_strategy)
@settings(max_examples=50)
def test_gbind_dsl_classbinding_instantiation(instance):
    assert isinstance(instance, gbind_dsl_ClassBinding)

@given(instance=BindingModel_strategy)
@settings(max_examples=50)
def test_bindingmodel_instantiation(instance):
    assert isinstance(instance, BindingModel)

@given(instance=gbind_dsl_ConceptBinding_strategy)
@settings(max_examples=50)
def test_gbind_dsl_conceptbinding_instantiation(instance):
    assert isinstance(instance, gbind_dsl_ConceptBinding)



@given(instance=gbind_dsl_ConceptBinding_strategy)
def test_gbind_dsl_conceptbinding_debugName_setter(instance):
    original = instance.debugName
    instance.debugName = original
    assert instance.debugName == original

@given(instance=Metaclass_strategy)
@settings(max_examples=50)
def test_metaclass_instantiation(instance):
    assert isinstance(instance, Metaclass)

@given(instance=gbind_dsl_ConcreteMetaclass_strategy)
@settings(max_examples=50)
def test_gbind_dsl_concretemetaclass_instantiation(instance):
    assert isinstance(instance, gbind_dsl_ConcreteMetaclass)

@given(instance=gbind_dsl_VirtualMetaclass_strategy)
@settings(max_examples=50)
def test_gbind_dsl_virtualmetaclass_instantiation(instance):
    assert isinstance(instance, gbind_dsl_VirtualMetaclass)

@given(instance=gbind_dsl_ConceptMetaclass_strategy)
@settings(max_examples=50)
def test_gbind_dsl_conceptmetaclass_instantiation(instance):
    assert isinstance(instance, gbind_dsl_ConceptMetaclass)

@given(instance=dsl_gbind_EClass_strategy)
@settings(max_examples=50)
def test_dsl_gbind_eclass_instantiation(instance):
    assert isinstance(instance, dsl_gbind_EClass)

@given(instance=gbind_dsl_Metaclass_strategy)
@settings(max_examples=50)
def test_gbind_dsl_metaclass_instantiation(instance):
    assert isinstance(instance, gbind_dsl_Metaclass)



@given(instance=gbind_dsl_Metaclass_strategy)
def test_gbind_dsl_metaclass_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gbind_dsl_BindingOptions_strategy)
@settings(max_examples=50)
def test_gbind_dsl_bindingoptions_instantiation(instance):
    assert isinstance(instance, gbind_dsl_BindingOptions)



@given(instance=gbind_dsl_BindingOptions_strategy)
def test_gbind_dsl_bindingoptions_enableClassMerge_setter(instance):
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

@given(instance=OclFeatureDefinition_strategy)
@settings(max_examples=50)
def test_oclfeaturedefinition_instantiation(instance):
    assert isinstance(instance, OclFeatureDefinition)

@given(instance=OclFeature_strategy)
@settings(max_examples=50)
def test_oclfeature_instantiation(instance):
    assert isinstance(instance, OclFeature)

@given(instance=OclInstanceModel_strategy)
@settings(max_examples=50)
def test_oclinstancemodel_instantiation(instance):
    assert isinstance(instance, OclInstanceModel)

@given(instance=OclModelElement_strategy)
@settings(max_examples=50)
def test_oclmodelelement_instantiation(instance):
    assert isinstance(instance, OclModelElement)

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=gbind_simpleocl_Operation_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_operation_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_Operation)

@given(instance=gbind_simpleocl_Attribute_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_attribute_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_Attribute)

@given(instance=NumericType_strategy)
@settings(max_examples=50)
def test_numerictype_instantiation(instance):
    assert isinstance(instance, NumericType)

@given(instance=gbind_simpleocl_IntegerType_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_integertype_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_IntegerType)

@given(instance=Primitive_strategy)
@settings(max_examples=50)
def test_primitive_instantiation(instance):
    assert isinstance(instance, Primitive)

@given(instance=gbind_simpleocl_NumericType_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_numerictype_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_NumericType)

@given(instance=gbind_simpleocl_BooleanType_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_booleantype_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_BooleanType)

@given(instance=gbind_simpleocl_StringType_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_stringtype_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_StringType)

@given(instance=OclModel_strategy)
@settings(max_examples=50)
def test_oclmodel_instantiation(instance):
    assert isinstance(instance, OclModel)

@given(instance=gbind_simpleocl_OclInstanceModel_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_oclinstancemodel_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_OclInstanceModel)

@given(instance=gbind_simpleocl_OclMetamodel_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_oclmetamodel_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_OclMetamodel)



@given(instance=gbind_simpleocl_OclMetamodel_strategy)
def test_gbind_simpleocl_oclmetamodel_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original

@given(instance=LambdaType_strategy)
@settings(max_examples=50)
def test_lambdatype_instantiation(instance):
    assert isinstance(instance, LambdaType)

@given(instance=TupleType_strategy)
@settings(max_examples=50)
def test_tupletype_instantiation(instance):
    assert isinstance(instance, TupleType)

@given(instance=gbind_simpleocl_RealType_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_realtype_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_RealType)

@given(instance=IterateExp_strategy)
@settings(max_examples=50)
def test_iterateexp_instantiation(instance):
    assert isinstance(instance, IterateExp)

@given(instance=TupleTypeAttribute_strategy)
@settings(max_examples=50)
def test_tupletypeattribute_instantiation(instance):
    assert isinstance(instance, TupleTypeAttribute)

@given(instance=CollectionType_strategy)
@settings(max_examples=50)
def test_collectiontype_instantiation(instance):
    assert isinstance(instance, CollectionType)

@given(instance=gbind_simpleocl_SetType_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_settype_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_SetType)

@given(instance=gbind_simpleocl_BagType_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_bagtype_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_BagType)

@given(instance=gbind_simpleocl_OrderedSetType_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_orderedsettype_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_OrderedSetType)

@given(instance=gbind_simpleocl_SequenceType_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_sequencetype_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_SequenceType)

@given(instance=MapType_strategy)
@settings(max_examples=50)
def test_maptype_instantiation(instance):
    assert isinstance(instance, MapType)

@given(instance=OclContextDefinition_strategy)
@settings(max_examples=50)
def test_oclcontextdefinition_instantiation(instance):
    assert isinstance(instance, OclContextDefinition)

@given(instance=VariableExp_strategy)
@settings(max_examples=50)
def test_variableexp_instantiation(instance):
    assert isinstance(instance, VariableExp)

@given(instance=gbind_simpleocl_LambdaCallExp_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_lambdacallexp_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_LambdaCallExp)

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

@given(instance=gbind_simpleocl_StaticOperationCall_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_staticoperationcall_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_StaticOperationCall)



@given(instance=gbind_simpleocl_StaticOperationCall_strategy)
def test_gbind_simpleocl_staticoperationcall_operationName_setter(instance):
    original = instance.operationName
    instance.operationName = original
    assert instance.operationName == original

@given(instance=gbind_simpleocl_StaticNavigationOrAttributeCall_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_staticnavigationorattributecall_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_StaticNavigationOrAttributeCall)



@given(instance=gbind_simpleocl_StaticNavigationOrAttributeCall_strategy)
def test_gbind_simpleocl_staticnavigationorattributecall_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PropertyCall_strategy)
@settings(max_examples=50)
def test_propertycall_instantiation(instance):
    assert isinstance(instance, PropertyCall)

@given(instance=gbind_simpleocl_NavigationOrAttributeCall_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_navigationorattributecall_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_NavigationOrAttributeCall)



@given(instance=gbind_simpleocl_NavigationOrAttributeCall_strategy)
def test_gbind_simpleocl_navigationorattributecall_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gbind_simpleocl_OperationCall_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_operationcall_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_OperationCall)



@given(instance=gbind_simpleocl_OperationCall_strategy)
def test_gbind_simpleocl_operationcall_operationName_setter(instance):
    original = instance.operationName
    instance.operationName = original
    assert instance.operationName == original

@given(instance=gbind_simpleocl_LoopExp_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_loopexp_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_LoopExp)

@given(instance=NumericExp_strategy)
@settings(max_examples=50)
def test_numericexp_instantiation(instance):
    assert isinstance(instance, NumericExp)

@given(instance=gbind_simpleocl_RealExp_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_realexp_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_RealExp)



@given(instance=gbind_simpleocl_RealExp_strategy)
def test_gbind_simpleocl_realexp_realSymbol_setter(instance):
    original = instance.realSymbol
    instance.realSymbol = original
    assert instance.realSymbol == original

@given(instance=PrimitiveExp_strategy)
@settings(max_examples=50)
def test_primitiveexp_instantiation(instance):
    assert isinstance(instance, PrimitiveExp)

@given(instance=gbind_simpleocl_BooleanExp_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_booleanexp_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_BooleanExp)



@given(instance=gbind_simpleocl_BooleanExp_strategy)
def test_gbind_simpleocl_booleanexp_booleanSymbol_setter(instance):
    original = instance.booleanSymbol
    instance.booleanSymbol = original
    assert instance.booleanSymbol == original

@given(instance=gbind_simpleocl_NumericExp_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_numericexp_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_NumericExp)

@given(instance=gbind_simpleocl_StringExp_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_stringexp_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_StringExp)



@given(instance=gbind_simpleocl_StringExp_strategy)
def test_gbind_simpleocl_stringexp_stringSymbol_setter(instance):
    original = instance.stringSymbol
    instance.stringSymbol = original
    assert instance.stringSymbol == original

@given(instance=VariableDeclaration_strategy)
@settings(max_examples=50)
def test_variabledeclaration_instantiation(instance):
    assert isinstance(instance, VariableDeclaration)

@given(instance=gbind_simpleocl_Parameter_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_parameter_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_Parameter)

@given(instance=gbind_dsl_HelperParameter_strategy)
@settings(max_examples=50)
def test_gbind_dsl_helperparameter_instantiation(instance):
    assert isinstance(instance, gbind_dsl_HelperParameter)

@given(instance=gbind_simpleocl_LocalVariable_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_localvariable_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_LocalVariable)



@given(instance=gbind_simpleocl_LocalVariable_strategy)
def test_gbind_simpleocl_localvariable_eq_setter(instance):
    original = instance.eq
    instance.eq = original
    assert instance.eq == original

@given(instance=gbind_dsl_ConcreteReferencDeclaringVar_strategy)
@settings(max_examples=50)
def test_gbind_dsl_concretereferencdeclaringvar_instantiation(instance):
    assert isinstance(instance, gbind_dsl_ConcreteReferencDeclaringVar)

@given(instance=gbind_simpleocl_Iterator_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_iterator_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_Iterator)

@given(instance=OclExpression_strategy)
@settings(max_examples=50)
def test_oclexpression_instantiation(instance):
    assert isinstance(instance, OclExpression)

@given(instance=gbind_simpleocl_BraceExp_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_braceexp_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_BraceExp)

@given(instance=gbind_simpleocl_IfExp_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_ifexp_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_IfExp)

@given(instance=gbind_simpleocl_StaticPropertyCallExp_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_staticpropertycallexp_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_StaticPropertyCallExp)

@given(instance=gbind_simpleocl_SuperExp_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_superexp_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_SuperExp)

@given(instance=gbind_simpleocl_PropertyCallExp_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_propertycallexp_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_PropertyCallExp)

@given(instance=gbind_simpleocl_EnvExp_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_envexp_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_EnvExp)

@given(instance=gbind_simpleocl_LetExp_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_letexp_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_LetExp)

@given(instance=gbind_simpleocl_OperatorCallExp_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_operatorcallexp_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_OperatorCallExp)



@given(instance=gbind_simpleocl_OperatorCallExp_strategy)
def test_gbind_simpleocl_operatorcallexp_operationName_setter(instance):
    original = instance.operationName
    instance.operationName = original
    assert instance.operationName == original

@given(instance=gbind_simpleocl_PrimitiveExp_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_primitiveexp_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_PrimitiveExp)

@given(instance=gbind_simpleocl_OclUndefinedExp_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_oclundefinedexp_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_OclUndefinedExp)

@given(instance=gbind_simpleocl_OclModelElementExp_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_oclmodelelementexp_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_OclModelElementExp)



@given(instance=gbind_simpleocl_OclModelElementExp_strategy)
def test_gbind_simpleocl_oclmodelelementexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gbind_simpleocl_SelfExp_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_selfexp_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_SelfExp)

@given(instance=gbind_simpleocl_VariableExp_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_variableexp_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_VariableExp)

@given(instance=gbind_simpleocl_EnumLiteralExp_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_enumliteralexp_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_EnumLiteralExp)



@given(instance=gbind_simpleocl_EnumLiteralExp_strategy)
def test_gbind_simpleocl_enumliteralexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MapExp_strategy)
@settings(max_examples=50)
def test_mapexp_instantiation(instance):
    assert isinstance(instance, MapExp)

@given(instance=MapElement_strategy)
@settings(max_examples=50)
def test_mapelement_instantiation(instance):
    assert isinstance(instance, MapElement)

@given(instance=gbind_simpleocl_MapExp_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_mapexp_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_MapExp)

@given(instance=TupleExp_strategy)
@settings(max_examples=50)
def test_tupleexp_instantiation(instance):
    assert isinstance(instance, TupleExp)

@given(instance=TuplePart_strategy)
@settings(max_examples=50)
def test_tuplepart_instantiation(instance):
    assert isinstance(instance, TuplePart)

@given(instance=gbind_simpleocl_TupleExp_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_tupleexp_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_TupleExp)

@given(instance=gbind_simpleocl_CollectionExp_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_collectionexp_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_CollectionExp)

@given(instance=gbind_simpleocl_IntegerExp_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_integerexp_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_IntegerExp)



@given(instance=gbind_simpleocl_IntegerExp_strategy)
def test_gbind_simpleocl_integerexp_integerSymbol_setter(instance):
    original = instance.integerSymbol
    instance.integerSymbol = original
    assert instance.integerSymbol == original

@given(instance=Module_strategy)
@settings(max_examples=50)
def test_module_instantiation(instance):
    assert isinstance(instance, Module)

@given(instance=ModuleElement_strategy)
@settings(max_examples=50)
def test_moduleelement_instantiation(instance):
    assert isinstance(instance, ModuleElement)

@given(instance=gbind_simpleocl_OclFeatureDefinition_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_oclfeaturedefinition_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_OclFeatureDefinition)



@given(instance=gbind_simpleocl_OclFeatureDefinition_strategy)
def test_gbind_simpleocl_oclfeaturedefinition_static_setter(instance):
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

@given(instance=gbind_dsl_MetamodelDeclaration_strategy)
@settings(max_examples=50)
def test_gbind_dsl_metamodeldeclaration_instantiation(instance):
    assert isinstance(instance, gbind_dsl_MetamodelDeclaration)



@given(instance=gbind_dsl_MetamodelDeclaration_strategy)
def test_gbind_dsl_metamodeldeclaration_metamodelURI_setter(instance):
    original = instance.metamodelURI
    instance.metamodelURI = original
    assert instance.metamodelURI == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=gbind_simpleocl_OclFeature_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_oclfeature_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_OclFeature)



@given(instance=gbind_simpleocl_OclFeature_strategy)
def test_gbind_simpleocl_oclfeature_eq_setter(instance):
    original = instance.eq
    instance.eq = original
    assert instance.eq == original

@given(instance=gbind_simpleocl_OclModel_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_oclmodel_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_OclModel)

@given(instance=gbind_simpleocl_Module_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_module_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_Module)

@given(instance=LocatedElement_strategy)
@settings(max_examples=50)
def test_locatedelement_instantiation(instance):
    assert isinstance(instance, LocatedElement)

@given(instance=gbind_simpleocl_OclContextDefinition_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_oclcontextdefinition_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_OclContextDefinition)

@given(instance=gbind_simpleocl_ModuleElement_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_moduleelement_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_ModuleElement)

@given(instance=gbind_simpleocl_MapElement_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_mapelement_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_MapElement)

@given(instance=gbind_simpleocl_VariableDeclaration_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_variabledeclaration_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_VariableDeclaration)



@given(instance=gbind_simpleocl_VariableDeclaration_strategy)
def test_gbind_simpleocl_variabledeclaration_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=gbind_simpleocl_PropertyCall_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_propertycall_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_PropertyCall)

@given(instance=gbind_simpleocl_StaticPropertyCall_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_staticpropertycall_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_StaticPropertyCall)

@given(instance=gbind_simpleocl_OclType_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_ocltype_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_OclType)



@given(instance=gbind_simpleocl_OclType_strategy)
def test_gbind_simpleocl_ocltype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gbind_simpleocl_TupleTypeAttribute_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_tupletypeattribute_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_TupleTypeAttribute)



@given(instance=gbind_simpleocl_TupleTypeAttribute_strategy)
def test_gbind_simpleocl_tupletypeattribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gbind_simpleocl_NamedElement_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_namedelement_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_NamedElement)



@given(instance=gbind_simpleocl_NamedElement_strategy)
def test_gbind_simpleocl_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=OperatorCallExp_strategy)
@settings(max_examples=50)
def test_operatorcallexp_instantiation(instance):
    assert isinstance(instance, OperatorCallExp)

@given(instance=gbind_simpleocl_EqOpCallExp_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_eqopcallexp_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_EqOpCallExp)

@given(instance=gbind_simpleocl_MulOpCallExp_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_mulopcallexp_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_MulOpCallExp)

@given(instance=gbind_simpleocl_NotOpCallExp_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_notopcallexp_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_NotOpCallExp)

@given(instance=gbind_simpleocl_IntOpCallExp_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_intopcallexp_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_IntOpCallExp)

@given(instance=gbind_simpleocl_RelOpCallExp_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_relopcallexp_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_RelOpCallExp)

@given(instance=gbind_simpleocl_AddOpCallExp_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_addopcallexp_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_AddOpCallExp)

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

@given(instance=gbind_simpleocl_TuplePart_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_tuplepart_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_TuplePart)

@given(instance=OperationCall_strategy)
@settings(max_examples=50)
def test_operationcall_instantiation(instance):
    assert isinstance(instance, OperationCall)

@given(instance=gbind_simpleocl_CollectionOperationCall_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_collectionoperationcall_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_CollectionOperationCall)

@given(instance=LoopExp_strategy)
@settings(max_examples=50)
def test_loopexp_instantiation(instance):
    assert isinstance(instance, LoopExp)

@given(instance=gbind_simpleocl_IterateExp_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_iterateexp_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_IterateExp)

@given(instance=gbind_simpleocl_IteratorExp_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_iteratorexp_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_IteratorExp)



@given(instance=gbind_simpleocl_IteratorExp_strategy)
def test_gbind_simpleocl_iteratorexp_name_setter(instance):
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

@given(instance=gbind_simpleocl_SetExp_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_setexp_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_SetExp)

@given(instance=gbind_simpleocl_OrderedSetExp_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_orderedsetexp_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_OrderedSetExp)

@given(instance=gbind_simpleocl_BagExp_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_bagexp_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_BagExp)

@given(instance=gbind_simpleocl_SequenceExp_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_sequenceexp_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_SequenceExp)

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

@given(instance=gbind_simpleocl_EnvType_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_envtype_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_EnvType)

@given(instance=gbind_simpleocl_CollectionType_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_collectiontype_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_CollectionType)

@given(instance=gbind_simpleocl_LambdaType_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_lambdatype_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_LambdaType)

@given(instance=gbind_simpleocl_OclModelElement_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_oclmodelelement_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_OclModelElement)

@given(instance=gbind_simpleocl_MapType_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_maptype_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_MapType)

@given(instance=gbind_simpleocl_TupleType_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_tupletype_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_TupleType)

@given(instance=gbind_simpleocl_OclAnyType_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_oclanytype_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_OclAnyType)

@given(instance=gbind_simpleocl_Primitive_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_primitive_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_Primitive)

@given(instance=gbind_simpleocl_OclExpression_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_oclexpression_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_OclExpression)

@given(instance=gbind_simpleocl_Import_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_import_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_Import)

@given(instance=gbind_simpleocl_LocatedElement_strategy)
@settings(max_examples=50)
def test_gbind_simpleocl_locatedelement_instantiation(instance):
    assert isinstance(instance, gbind_simpleocl_LocatedElement)



@given(instance=gbind_simpleocl_LocatedElement_strategy)
def test_gbind_simpleocl_locatedelement_charStart_setter(instance):
    original = instance.charStart
    instance.charStart = original
    assert instance.charStart == original



@given(instance=gbind_simpleocl_LocatedElement_strategy)
def test_gbind_simpleocl_locatedelement_column_setter(instance):
    original = instance.column
    instance.column = original
    assert instance.column == original



@given(instance=gbind_simpleocl_LocatedElement_strategy)
def test_gbind_simpleocl_locatedelement_line_setter(instance):
    original = instance.line
    instance.line = original
    assert instance.line == original



@given(instance=gbind_simpleocl_LocatedElement_strategy)
def test_gbind_simpleocl_locatedelement_charEnd_setter(instance):
    original = instance.charEnd
    instance.charEnd = original
    assert instance.charEnd == original
