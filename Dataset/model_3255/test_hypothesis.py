import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    LiteralString,
    frameweb_VocabularyLiteral,
    VocabularyClassExpression,
    Individual,
    frameweb_AnonymousIndividual,
    DataType,
    VocabularyAssociation,
    VocabularyEntity,
    frameweb_DataProperty,
    frameweb_VocabularyClass,
    frameweb_NamedIndividual,
    frameweb_AnnotationProperty,
    frameweb_VocabularyDataType,
    frameweb_ObjectProperty,
    frameweb_NewInterface115,
    frameweb_Type,
    Relationship,
    Classifier,
    frameweb_VocabularyEntity,
    frameweb_Association,
    frameweb_ValueSpecification,
    frameweb_Class,
    frameweb_Interface,
    frameweb_DataType,
    DeploymentTarget,
    ConnectableElement,
    StructuralFeature,
    frameweb_Property,
    FrameworkExtension,
    frameweb_DomainExtension,
    frameweb_NavigationExtension,
    NavigationProperty,
    frameweb_NavigationCompositionWhole,
    frameweb_NavigationCompositionPart,
    ExtensionEnd,
    frameweb_AttributeMappingExtensionEnd,
    frameweb_TagExtensionEnd,
    frameweb_ClassMappingExtensionEnd,
    frameweb_ResultExtensionEnd,
    frameweb_ControllerExtensionEnd,
    DomainExtension,
    frameweb_AttributeMappingExtension,
    frameweb_ClassMappingExtension,
    ProfileApplication,
    frameweb_FrameworkApplication,
    NavigationExtension,
    frameweb_ControllerExtension,
    frameweb_ResultExtension,
    frameweb_TagExtension,
    Extension,
    frameweb_FrameworkExtension,
    GeneralizationSet,
    frameweb_NavigationGeneralizationSet,
    frameweb_ServiceGeneralizationSet,
    frameweb_DAOGeneralizationSet,
    frameweb_DomainGeneralizationSet,
    NavigationConstraint,
    Constraint,
    frameweb_VocabularyConstraints,
    frameweb_DomainConstraints,
    frameweb_NavigationConstraint,
    Stereotype,
    frameweb_Tag,
    frameweb_Controller,
    frameweb_ClassMapping,
    frameweb_AttributeMapping,
    frameweb_ResultType,
    NavigationPackage,
    frameweb_ControllerPackage,
    frameweb_ViewPackage,
    Package,
    frameweb_ControllerSet,
    frameweb_ResultSet,
    frameweb_PersistencePackage,
    frameweb_NavigationPackage,
    frameweb_Vocabulary,
    frameweb_ApplicationPackage,
    frameweb_SemanticPackage,
    frameweb_MappingLib,
    frameweb_DomainPackage,
    Dependency,
    frameweb_NavigationDependency,
    frameweb_ChainingConstraint,
    frameweb_PageConstraint,
    frameweb_MethodCosntraint,
    frameweb_TagLib,
    ServiceAssociation,
    frameweb_DAOServiceAssociation,
    frameweb_ServiceControllerAssociation,
    Generalization_,
    frameweb_DAOGeneralization,
    frameweb_NavigationGeneralization,
    frameweb_DomainGeneralization,
    frameweb_ServiceGeneralization,
    Operation,
    frameweb_ServiceMethod,
    frameweb_DomainMethod,
    frameweb_DAOMethod,
    frameweb_ResultConstraint,
    frameweb_FrontControllerMethod,
    NavigationDependency,
    frameweb_FrontControllerDependency,
    frameweb_ChainingDependency,
    frameweb_PageDependency,
    frameweb_ResultDependency,
    NavigationAttribute,
    frameweb_UIComponentField,
    frameweb_IOParameter,
    InterfaceRealization,
    frameweb_SeviceRealization,
    frameweb_DAORealization,
    Class,
    frameweb_Annotation,
    frameweb_DomainClass,
    frameweb_NavigationClass,
    frameweb_Axiom,
    frameweb_ServiceClass,
    frameweb_FrontControllerClass,
    frameweb_VocabularyClassExpression,
    frameweb_Result,
    frameweb_DAOClass,
    Interface,
    frameweb_ServiceInterface,
    frameweb_DAOInterface,
    NavigationClass,
    frameweb_UIComponent,
    frameweb_Template,
    frameweb_Page,
    DomainAttribute,
    frameweb_LOBAttribute,
    frameweb_EmbeddedAttribute,
    frameweb_IdAttribute,
    frameweb_DecimalAttribute,
    frameweb_DateTimeAttribute,
    frameweb_VersionAttribute,
    Property,
    frameweb_DAOAttribute,
    frameweb_ResultProperty,
    frameweb_AttributeMappingProperty,
    frameweb_DomainProperty,
    frameweb_NavigationProperty,
    frameweb_ServiceAttribute,
    frameweb_IRI,
    frameweb_VocabularyProperty,
    frameweb_NavigationAttribute,
    frameweb_ClassMappingPropery,
    frameweb_ControllerProperty,
    frameweb_Individual,
    frameweb_TagProperty,
    frameweb_DomainAttribute,
    Association,
    frameweb_VocabularyAssociation,
    frameweb_ServiceAssociation,
    frameweb_NavigationAssociation,
    frameweb_DomainAssociation,
    FramewebModel,
    frameweb_PersistenceModel,
    frameweb_ApplicationModel,
    frameweb_VocabularyModel,
    frameweb_NavigationModel,
    frameweb_EntityModel,
    Profile,
    Model,
    frameweb_FrameworkProfile,
    frameweb_FramewebModel,
    frameweb_FramewebProject,
    Fetch,
    Order,
    Generation,
    Cascade,
    FrameworkCategoryList,
    DateTimePrecision,
    Collection,
    InheritanceMapping,
    FrameworkKindList,
    ConstantNameList,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_literalstring_is_not_abstract():
    assert not inspect.isabstract(LiteralString)


def test_literalstring_constructor_exists():
    assert callable(LiteralString.__init__)


def test_literalstring_constructor_args():
    sig = inspect.signature(LiteralString.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_vocabularyliteral_is_not_abstract():
    assert not inspect.isabstract(frameweb_VocabularyLiteral)


def test_frameweb_vocabularyliteral_constructor_exists():
    assert callable(frameweb_VocabularyLiteral.__init__)


def test_frameweb_vocabularyliteral_constructor_args():
    sig = inspect.signature(frameweb_VocabularyLiteral.__init__)
    params = list(sig.parameters.keys())



def test_vocabularyclassexpression_is_not_abstract():
    assert not inspect.isabstract(VocabularyClassExpression)


def test_vocabularyclassexpression_constructor_exists():
    assert callable(VocabularyClassExpression.__init__)


def test_vocabularyclassexpression_constructor_args():
    sig = inspect.signature(VocabularyClassExpression.__init__)
    params = list(sig.parameters.keys())



def test_individual_is_not_abstract():
    assert not inspect.isabstract(Individual)


def test_individual_constructor_exists():
    assert callable(Individual.__init__)


def test_individual_constructor_args():
    sig = inspect.signature(Individual.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_anonymousindividual_is_not_abstract():
    assert not inspect.isabstract(frameweb_AnonymousIndividual)


def test_frameweb_anonymousindividual_constructor_exists():
    assert callable(frameweb_AnonymousIndividual.__init__)


def test_frameweb_anonymousindividual_constructor_args():
    sig = inspect.signature(frameweb_AnonymousIndividual.__init__)
    params = list(sig.parameters.keys())



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_vocabularyassociation_is_not_abstract():
    assert not inspect.isabstract(VocabularyAssociation)


def test_vocabularyassociation_constructor_exists():
    assert callable(VocabularyAssociation.__init__)


def test_vocabularyassociation_constructor_args():
    sig = inspect.signature(VocabularyAssociation.__init__)
    params = list(sig.parameters.keys())



def test_vocabularyentity_is_not_abstract():
    assert not inspect.isabstract(VocabularyEntity)


def test_vocabularyentity_constructor_exists():
    assert callable(VocabularyEntity.__init__)


def test_vocabularyentity_constructor_args():
    sig = inspect.signature(VocabularyEntity.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_dataproperty_is_not_abstract():
    assert not inspect.isabstract(frameweb_DataProperty)


def test_frameweb_dataproperty_constructor_exists():
    assert callable(frameweb_DataProperty.__init__)


def test_frameweb_dataproperty_constructor_args():
    sig = inspect.signature(frameweb_DataProperty.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_vocabularyclass_is_not_abstract():
    assert not inspect.isabstract(frameweb_VocabularyClass)


def test_frameweb_vocabularyclass_constructor_exists():
    assert callable(frameweb_VocabularyClass.__init__)


def test_frameweb_vocabularyclass_constructor_args():
    sig = inspect.signature(frameweb_VocabularyClass.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_namedindividual_is_not_abstract():
    assert not inspect.isabstract(frameweb_NamedIndividual)


def test_frameweb_namedindividual_constructor_exists():
    assert callable(frameweb_NamedIndividual.__init__)


def test_frameweb_namedindividual_constructor_args():
    sig = inspect.signature(frameweb_NamedIndividual.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_annotationproperty_is_not_abstract():
    assert not inspect.isabstract(frameweb_AnnotationProperty)


def test_frameweb_annotationproperty_constructor_exists():
    assert callable(frameweb_AnnotationProperty.__init__)


def test_frameweb_annotationproperty_constructor_args():
    sig = inspect.signature(frameweb_AnnotationProperty.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_vocabularydatatype_is_not_abstract():
    assert not inspect.isabstract(frameweb_VocabularyDataType)


def test_frameweb_vocabularydatatype_constructor_exists():
    assert callable(frameweb_VocabularyDataType.__init__)


def test_frameweb_vocabularydatatype_constructor_args():
    sig = inspect.signature(frameweb_VocabularyDataType.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_objectproperty_is_not_abstract():
    assert not inspect.isabstract(frameweb_ObjectProperty)


def test_frameweb_objectproperty_constructor_exists():
    assert callable(frameweb_ObjectProperty.__init__)


def test_frameweb_objectproperty_constructor_args():
    sig = inspect.signature(frameweb_ObjectProperty.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_newinterface115_is_not_abstract():
    assert not inspect.isabstract(frameweb_NewInterface115)


def test_frameweb_newinterface115_constructor_exists():
    assert callable(frameweb_NewInterface115.__init__)


def test_frameweb_newinterface115_constructor_args():
    sig = inspect.signature(frameweb_NewInterface115.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_type_is_not_abstract():
    assert not inspect.isabstract(frameweb_Type)


def test_frameweb_type_constructor_exists():
    assert callable(frameweb_Type.__init__)


def test_frameweb_type_constructor_args():
    sig = inspect.signature(frameweb_Type.__init__)
    params = list(sig.parameters.keys())



def test_relationship_is_not_abstract():
    assert not inspect.isabstract(Relationship)


def test_relationship_constructor_exists():
    assert callable(Relationship.__init__)


def test_relationship_constructor_args():
    sig = inspect.signature(Relationship.__init__)
    params = list(sig.parameters.keys())



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_vocabularyentity_is_not_abstract():
    assert not inspect.isabstract(frameweb_VocabularyEntity)


def test_frameweb_vocabularyentity_constructor_exists():
    assert callable(frameweb_VocabularyEntity.__init__)


def test_frameweb_vocabularyentity_constructor_args():
    sig = inspect.signature(frameweb_VocabularyEntity.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_association_is_not_abstract():
    assert not inspect.isabstract(frameweb_Association)


def test_frameweb_association_constructor_exists():
    assert callable(frameweb_Association.__init__)


def test_frameweb_association_constructor_args():
    sig = inspect.signature(frameweb_Association.__init__)
    params = list(sig.parameters.keys())
    assert "isDerived" in params, "Missing parameter 'isDerived'"

def test_frameweb_association_has_isDerived():
    assert hasattr(frameweb_Association, "isDerived")
    descriptor = None
    for klass in frameweb_Association.__mro__:
        if "isDerived" in klass.__dict__:
            descriptor = klass.__dict__["isDerived"]
            break
    assert isinstance(descriptor, property)



def test_frameweb_valuespecification_is_not_abstract():
    assert not inspect.isabstract(frameweb_ValueSpecification)


def test_frameweb_valuespecification_constructor_exists():
    assert callable(frameweb_ValueSpecification.__init__)


def test_frameweb_valuespecification_constructor_args():
    sig = inspect.signature(frameweb_ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_class_is_not_abstract():
    assert not inspect.isabstract(frameweb_Class)


def test_frameweb_class_constructor_exists():
    assert callable(frameweb_Class.__init__)


def test_frameweb_class_constructor_args():
    sig = inspect.signature(frameweb_Class.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_interface_is_not_abstract():
    assert not inspect.isabstract(frameweb_Interface)


def test_frameweb_interface_constructor_exists():
    assert callable(frameweb_Interface.__init__)


def test_frameweb_interface_constructor_args():
    sig = inspect.signature(frameweb_Interface.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_datatype_is_not_abstract():
    assert not inspect.isabstract(frameweb_DataType)


def test_frameweb_datatype_constructor_exists():
    assert callable(frameweb_DataType.__init__)


def test_frameweb_datatype_constructor_args():
    sig = inspect.signature(frameweb_DataType.__init__)
    params = list(sig.parameters.keys())



def test_deploymenttarget_is_not_abstract():
    assert not inspect.isabstract(DeploymentTarget)


def test_deploymenttarget_constructor_exists():
    assert callable(DeploymentTarget.__init__)


def test_deploymenttarget_constructor_args():
    sig = inspect.signature(DeploymentTarget.__init__)
    params = list(sig.parameters.keys())



def test_connectableelement_is_not_abstract():
    assert not inspect.isabstract(ConnectableElement)


def test_connectableelement_constructor_exists():
    assert callable(ConnectableElement.__init__)


def test_connectableelement_constructor_args():
    sig = inspect.signature(ConnectableElement.__init__)
    params = list(sig.parameters.keys())



def test_structuralfeature_is_not_abstract():
    assert not inspect.isabstract(StructuralFeature)


def test_structuralfeature_constructor_exists():
    assert callable(StructuralFeature.__init__)


def test_structuralfeature_constructor_args():
    sig = inspect.signature(StructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_property_is_not_abstract():
    assert not inspect.isabstract(frameweb_Property)


def test_frameweb_property_constructor_exists():
    assert callable(frameweb_Property.__init__)


def test_frameweb_property_constructor_args():
    sig = inspect.signature(frameweb_Property.__init__)
    params = list(sig.parameters.keys())
    assert "isDerivedUnion" in params, "Missing parameter 'isDerivedUnion'"
    assert "default" in params, "Missing parameter 'default'"
    assert "isID" in params, "Missing parameter 'isID'"
    assert "isDerived" in params, "Missing parameter 'isDerived'"
    assert "aggregation" in params, "Missing parameter 'aggregation'"
    assert "isComposite" in params, "Missing parameter 'isComposite'"

def test_frameweb_property_has_isDerivedUnion():
    assert hasattr(frameweb_Property, "isDerivedUnion")
    descriptor = None
    for klass in frameweb_Property.__mro__:
        if "isDerivedUnion" in klass.__dict__:
            descriptor = klass.__dict__["isDerivedUnion"]
            break
    assert isinstance(descriptor, property)

def test_frameweb_property_has_default():
    assert hasattr(frameweb_Property, "default")
    descriptor = None
    for klass in frameweb_Property.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)

def test_frameweb_property_has_isID():
    assert hasattr(frameweb_Property, "isID")
    descriptor = None
    for klass in frameweb_Property.__mro__:
        if "isID" in klass.__dict__:
            descriptor = klass.__dict__["isID"]
            break
    assert isinstance(descriptor, property)

def test_frameweb_property_has_isDerived():
    assert hasattr(frameweb_Property, "isDerived")
    descriptor = None
    for klass in frameweb_Property.__mro__:
        if "isDerived" in klass.__dict__:
            descriptor = klass.__dict__["isDerived"]
            break
    assert isinstance(descriptor, property)

def test_frameweb_property_has_aggregation():
    assert hasattr(frameweb_Property, "aggregation")
    descriptor = None
    for klass in frameweb_Property.__mro__:
        if "aggregation" in klass.__dict__:
            descriptor = klass.__dict__["aggregation"]
            break
    assert isinstance(descriptor, property)

def test_frameweb_property_has_isComposite():
    assert hasattr(frameweb_Property, "isComposite")
    descriptor = None
    for klass in frameweb_Property.__mro__:
        if "isComposite" in klass.__dict__:
            descriptor = klass.__dict__["isComposite"]
            break
    assert isinstance(descriptor, property)



def test_frameworkextension_is_not_abstract():
    assert not inspect.isabstract(FrameworkExtension)


def test_frameworkextension_constructor_exists():
    assert callable(FrameworkExtension.__init__)


def test_frameworkextension_constructor_args():
    sig = inspect.signature(FrameworkExtension.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_domainextension_is_not_abstract():
    assert not inspect.isabstract(frameweb_DomainExtension)


def test_frameweb_domainextension_constructor_exists():
    assert callable(frameweb_DomainExtension.__init__)


def test_frameweb_domainextension_constructor_args():
    sig = inspect.signature(frameweb_DomainExtension.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_navigationextension_is_not_abstract():
    assert not inspect.isabstract(frameweb_NavigationExtension)


def test_frameweb_navigationextension_constructor_exists():
    assert callable(frameweb_NavigationExtension.__init__)


def test_frameweb_navigationextension_constructor_args():
    sig = inspect.signature(frameweb_NavigationExtension.__init__)
    params = list(sig.parameters.keys())



def test_navigationproperty_is_not_abstract():
    assert not inspect.isabstract(NavigationProperty)


def test_navigationproperty_constructor_exists():
    assert callable(NavigationProperty.__init__)


def test_navigationproperty_constructor_args():
    sig = inspect.signature(NavigationProperty.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_navigationcompositionwhole_is_not_abstract():
    assert not inspect.isabstract(frameweb_NavigationCompositionWhole)


def test_frameweb_navigationcompositionwhole_constructor_exists():
    assert callable(frameweb_NavigationCompositionWhole.__init__)


def test_frameweb_navigationcompositionwhole_constructor_args():
    sig = inspect.signature(frameweb_NavigationCompositionWhole.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_navigationcompositionpart_is_not_abstract():
    assert not inspect.isabstract(frameweb_NavigationCompositionPart)


def test_frameweb_navigationcompositionpart_constructor_exists():
    assert callable(frameweb_NavigationCompositionPart.__init__)


def test_frameweb_navigationcompositionpart_constructor_args():
    sig = inspect.signature(frameweb_NavigationCompositionPart.__init__)
    params = list(sig.parameters.keys())



def test_extensionend_is_not_abstract():
    assert not inspect.isabstract(ExtensionEnd)


def test_extensionend_constructor_exists():
    assert callable(ExtensionEnd.__init__)


def test_extensionend_constructor_args():
    sig = inspect.signature(ExtensionEnd.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_attributemappingextensionend_is_not_abstract():
    assert not inspect.isabstract(frameweb_AttributeMappingExtensionEnd)


def test_frameweb_attributemappingextensionend_constructor_exists():
    assert callable(frameweb_AttributeMappingExtensionEnd.__init__)


def test_frameweb_attributemappingextensionend_constructor_args():
    sig = inspect.signature(frameweb_AttributeMappingExtensionEnd.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_tagextensionend_is_not_abstract():
    assert not inspect.isabstract(frameweb_TagExtensionEnd)


def test_frameweb_tagextensionend_constructor_exists():
    assert callable(frameweb_TagExtensionEnd.__init__)


def test_frameweb_tagextensionend_constructor_args():
    sig = inspect.signature(frameweb_TagExtensionEnd.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_classmappingextensionend_is_not_abstract():
    assert not inspect.isabstract(frameweb_ClassMappingExtensionEnd)


def test_frameweb_classmappingextensionend_constructor_exists():
    assert callable(frameweb_ClassMappingExtensionEnd.__init__)


def test_frameweb_classmappingextensionend_constructor_args():
    sig = inspect.signature(frameweb_ClassMappingExtensionEnd.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_resultextensionend_is_not_abstract():
    assert not inspect.isabstract(frameweb_ResultExtensionEnd)


def test_frameweb_resultextensionend_constructor_exists():
    assert callable(frameweb_ResultExtensionEnd.__init__)


def test_frameweb_resultextensionend_constructor_args():
    sig = inspect.signature(frameweb_ResultExtensionEnd.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_controllerextensionend_is_not_abstract():
    assert not inspect.isabstract(frameweb_ControllerExtensionEnd)


def test_frameweb_controllerextensionend_constructor_exists():
    assert callable(frameweb_ControllerExtensionEnd.__init__)


def test_frameweb_controllerextensionend_constructor_args():
    sig = inspect.signature(frameweb_ControllerExtensionEnd.__init__)
    params = list(sig.parameters.keys())



def test_domainextension_is_not_abstract():
    assert not inspect.isabstract(DomainExtension)


def test_domainextension_constructor_exists():
    assert callable(DomainExtension.__init__)


def test_domainextension_constructor_args():
    sig = inspect.signature(DomainExtension.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_attributemappingextension_is_not_abstract():
    assert not inspect.isabstract(frameweb_AttributeMappingExtension)


def test_frameweb_attributemappingextension_constructor_exists():
    assert callable(frameweb_AttributeMappingExtension.__init__)


def test_frameweb_attributemappingextension_constructor_args():
    sig = inspect.signature(frameweb_AttributeMappingExtension.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_classmappingextension_is_not_abstract():
    assert not inspect.isabstract(frameweb_ClassMappingExtension)


def test_frameweb_classmappingextension_constructor_exists():
    assert callable(frameweb_ClassMappingExtension.__init__)


def test_frameweb_classmappingextension_constructor_args():
    sig = inspect.signature(frameweb_ClassMappingExtension.__init__)
    params = list(sig.parameters.keys())



def test_profileapplication_is_not_abstract():
    assert not inspect.isabstract(ProfileApplication)


def test_profileapplication_constructor_exists():
    assert callable(ProfileApplication.__init__)


def test_profileapplication_constructor_args():
    sig = inspect.signature(ProfileApplication.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_frameworkapplication_is_not_abstract():
    assert not inspect.isabstract(frameweb_FrameworkApplication)


def test_frameweb_frameworkapplication_constructor_exists():
    assert callable(frameweb_FrameworkApplication.__init__)


def test_frameweb_frameworkapplication_constructor_args():
    sig = inspect.signature(frameweb_FrameworkApplication.__init__)
    params = list(sig.parameters.keys())



def test_navigationextension_is_not_abstract():
    assert not inspect.isabstract(NavigationExtension)


def test_navigationextension_constructor_exists():
    assert callable(NavigationExtension.__init__)


def test_navigationextension_constructor_args():
    sig = inspect.signature(NavigationExtension.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_controllerextension_is_not_abstract():
    assert not inspect.isabstract(frameweb_ControllerExtension)


def test_frameweb_controllerextension_constructor_exists():
    assert callable(frameweb_ControllerExtension.__init__)


def test_frameweb_controllerextension_constructor_args():
    sig = inspect.signature(frameweb_ControllerExtension.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_resultextension_is_not_abstract():
    assert not inspect.isabstract(frameweb_ResultExtension)


def test_frameweb_resultextension_constructor_exists():
    assert callable(frameweb_ResultExtension.__init__)


def test_frameweb_resultextension_constructor_args():
    sig = inspect.signature(frameweb_ResultExtension.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_tagextension_is_not_abstract():
    assert not inspect.isabstract(frameweb_TagExtension)


def test_frameweb_tagextension_constructor_exists():
    assert callable(frameweb_TagExtension.__init__)


def test_frameweb_tagextension_constructor_args():
    sig = inspect.signature(frameweb_TagExtension.__init__)
    params = list(sig.parameters.keys())



def test_extension_is_not_abstract():
    assert not inspect.isabstract(Extension)


def test_extension_constructor_exists():
    assert callable(Extension.__init__)


def test_extension_constructor_args():
    sig = inspect.signature(Extension.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_frameworkextension_is_not_abstract():
    assert not inspect.isabstract(frameweb_FrameworkExtension)


def test_frameweb_frameworkextension_constructor_exists():
    assert callable(frameweb_FrameworkExtension.__init__)


def test_frameweb_frameworkextension_constructor_args():
    sig = inspect.signature(frameweb_FrameworkExtension.__init__)
    params = list(sig.parameters.keys())



def test_generalizationset_is_not_abstract():
    assert not inspect.isabstract(GeneralizationSet)


def test_generalizationset_constructor_exists():
    assert callable(GeneralizationSet.__init__)


def test_generalizationset_constructor_args():
    sig = inspect.signature(GeneralizationSet.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_navigationgeneralizationset_is_not_abstract():
    assert not inspect.isabstract(frameweb_NavigationGeneralizationSet)


def test_frameweb_navigationgeneralizationset_constructor_exists():
    assert callable(frameweb_NavigationGeneralizationSet.__init__)


def test_frameweb_navigationgeneralizationset_constructor_args():
    sig = inspect.signature(frameweb_NavigationGeneralizationSet.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_servicegeneralizationset_is_not_abstract():
    assert not inspect.isabstract(frameweb_ServiceGeneralizationSet)


def test_frameweb_servicegeneralizationset_constructor_exists():
    assert callable(frameweb_ServiceGeneralizationSet.__init__)


def test_frameweb_servicegeneralizationset_constructor_args():
    sig = inspect.signature(frameweb_ServiceGeneralizationSet.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_daogeneralizationset_is_not_abstract():
    assert not inspect.isabstract(frameweb_DAOGeneralizationSet)


def test_frameweb_daogeneralizationset_constructor_exists():
    assert callable(frameweb_DAOGeneralizationSet.__init__)


def test_frameweb_daogeneralizationset_constructor_args():
    sig = inspect.signature(frameweb_DAOGeneralizationSet.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_domaingeneralizationset_is_not_abstract():
    assert not inspect.isabstract(frameweb_DomainGeneralizationSet)


def test_frameweb_domaingeneralizationset_constructor_exists():
    assert callable(frameweb_DomainGeneralizationSet.__init__)


def test_frameweb_domaingeneralizationset_constructor_args():
    sig = inspect.signature(frameweb_DomainGeneralizationSet.__init__)
    params = list(sig.parameters.keys())
    assert "mapping" in params, "Missing parameter 'mapping'"

def test_frameweb_domaingeneralizationset_has_mapping():
    assert hasattr(frameweb_DomainGeneralizationSet, "mapping")
    descriptor = None
    for klass in frameweb_DomainGeneralizationSet.__mro__:
        if "mapping" in klass.__dict__:
            descriptor = klass.__dict__["mapping"]
            break
    assert isinstance(descriptor, property)



def test_navigationconstraint_is_not_abstract():
    assert not inspect.isabstract(NavigationConstraint)


def test_navigationconstraint_constructor_exists():
    assert callable(NavigationConstraint.__init__)


def test_navigationconstraint_constructor_args():
    sig = inspect.signature(NavigationConstraint.__init__)
    params = list(sig.parameters.keys())



def test_constraint_is_not_abstract():
    assert not inspect.isabstract(Constraint)


def test_constraint_constructor_exists():
    assert callable(Constraint.__init__)


def test_constraint_constructor_args():
    sig = inspect.signature(Constraint.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_vocabularyconstraints_is_not_abstract():
    assert not inspect.isabstract(frameweb_VocabularyConstraints)


def test_frameweb_vocabularyconstraints_constructor_exists():
    assert callable(frameweb_VocabularyConstraints.__init__)


def test_frameweb_vocabularyconstraints_constructor_args():
    sig = inspect.signature(frameweb_VocabularyConstraints.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_domainconstraints_is_not_abstract():
    assert not inspect.isabstract(frameweb_DomainConstraints)


def test_frameweb_domainconstraints_constructor_exists():
    assert callable(frameweb_DomainConstraints.__init__)


def test_frameweb_domainconstraints_constructor_args():
    sig = inspect.signature(frameweb_DomainConstraints.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_navigationconstraint_is_not_abstract():
    assert not inspect.isabstract(frameweb_NavigationConstraint)


def test_frameweb_navigationconstraint_constructor_exists():
    assert callable(frameweb_NavigationConstraint.__init__)


def test_frameweb_navigationconstraint_constructor_args():
    sig = inspect.signature(frameweb_NavigationConstraint.__init__)
    params = list(sig.parameters.keys())



def test_stereotype_is_not_abstract():
    assert not inspect.isabstract(Stereotype)


def test_stereotype_constructor_exists():
    assert callable(Stereotype.__init__)


def test_stereotype_constructor_args():
    sig = inspect.signature(Stereotype.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_tag_is_not_abstract():
    assert not inspect.isabstract(frameweb_Tag)


def test_frameweb_tag_constructor_exists():
    assert callable(frameweb_Tag.__init__)


def test_frameweb_tag_constructor_args():
    sig = inspect.signature(frameweb_Tag.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_controller_is_not_abstract():
    assert not inspect.isabstract(frameweb_Controller)


def test_frameweb_controller_constructor_exists():
    assert callable(frameweb_Controller.__init__)


def test_frameweb_controller_constructor_args():
    sig = inspect.signature(frameweb_Controller.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_classmapping_is_not_abstract():
    assert not inspect.isabstract(frameweb_ClassMapping)


def test_frameweb_classmapping_constructor_exists():
    assert callable(frameweb_ClassMapping.__init__)


def test_frameweb_classmapping_constructor_args():
    sig = inspect.signature(frameweb_ClassMapping.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_attributemapping_is_not_abstract():
    assert not inspect.isabstract(frameweb_AttributeMapping)


def test_frameweb_attributemapping_constructor_exists():
    assert callable(frameweb_AttributeMapping.__init__)


def test_frameweb_attributemapping_constructor_args():
    sig = inspect.signature(frameweb_AttributeMapping.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_resulttype_is_not_abstract():
    assert not inspect.isabstract(frameweb_ResultType)


def test_frameweb_resulttype_constructor_exists():
    assert callable(frameweb_ResultType.__init__)


def test_frameweb_resulttype_constructor_args():
    sig = inspect.signature(frameweb_ResultType.__init__)
    params = list(sig.parameters.keys())



def test_navigationpackage_is_not_abstract():
    assert not inspect.isabstract(NavigationPackage)


def test_navigationpackage_constructor_exists():
    assert callable(NavigationPackage.__init__)


def test_navigationpackage_constructor_args():
    sig = inspect.signature(NavigationPackage.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_controllerpackage_is_not_abstract():
    assert not inspect.isabstract(frameweb_ControllerPackage)


def test_frameweb_controllerpackage_constructor_exists():
    assert callable(frameweb_ControllerPackage.__init__)


def test_frameweb_controllerpackage_constructor_args():
    sig = inspect.signature(frameweb_ControllerPackage.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_viewpackage_is_not_abstract():
    assert not inspect.isabstract(frameweb_ViewPackage)


def test_frameweb_viewpackage_constructor_exists():
    assert callable(frameweb_ViewPackage.__init__)


def test_frameweb_viewpackage_constructor_args():
    sig = inspect.signature(frameweb_ViewPackage.__init__)
    params = list(sig.parameters.keys())



def test_package_is_not_abstract():
    assert not inspect.isabstract(Package)


def test_package_constructor_exists():
    assert callable(Package.__init__)


def test_package_constructor_args():
    sig = inspect.signature(Package.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_controllerset_is_not_abstract():
    assert not inspect.isabstract(frameweb_ControllerSet)


def test_frameweb_controllerset_constructor_exists():
    assert callable(frameweb_ControllerSet.__init__)


def test_frameweb_controllerset_constructor_args():
    sig = inspect.signature(frameweb_ControllerSet.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_resultset_is_not_abstract():
    assert not inspect.isabstract(frameweb_ResultSet)


def test_frameweb_resultset_constructor_exists():
    assert callable(frameweb_ResultSet.__init__)


def test_frameweb_resultset_constructor_args():
    sig = inspect.signature(frameweb_ResultSet.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_persistencepackage_is_not_abstract():
    assert not inspect.isabstract(frameweb_PersistencePackage)


def test_frameweb_persistencepackage_constructor_exists():
    assert callable(frameweb_PersistencePackage.__init__)


def test_frameweb_persistencepackage_constructor_args():
    sig = inspect.signature(frameweb_PersistencePackage.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_navigationpackage_is_not_abstract():
    assert not inspect.isabstract(frameweb_NavigationPackage)


def test_frameweb_navigationpackage_constructor_exists():
    assert callable(frameweb_NavigationPackage.__init__)


def test_frameweb_navigationpackage_constructor_args():
    sig = inspect.signature(frameweb_NavigationPackage.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_vocabulary_is_not_abstract():
    assert not inspect.isabstract(frameweb_Vocabulary)


def test_frameweb_vocabulary_constructor_exists():
    assert callable(frameweb_Vocabulary.__init__)


def test_frameweb_vocabulary_constructor_args():
    sig = inspect.signature(frameweb_Vocabulary.__init__)
    params = list(sig.parameters.keys())
    assert "vocabularyDocument" in params, "Missing parameter 'vocabularyDocument'"

def test_frameweb_vocabulary_has_vocabularyDocument():
    assert hasattr(frameweb_Vocabulary, "vocabularyDocument")
    descriptor = None
    for klass in frameweb_Vocabulary.__mro__:
        if "vocabularyDocument" in klass.__dict__:
            descriptor = klass.__dict__["vocabularyDocument"]
            break
    assert isinstance(descriptor, property)



def test_frameweb_applicationpackage_is_not_abstract():
    assert not inspect.isabstract(frameweb_ApplicationPackage)


def test_frameweb_applicationpackage_constructor_exists():
    assert callable(frameweb_ApplicationPackage.__init__)


def test_frameweb_applicationpackage_constructor_args():
    sig = inspect.signature(frameweb_ApplicationPackage.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_semanticpackage_is_not_abstract():
    assert not inspect.isabstract(frameweb_SemanticPackage)


def test_frameweb_semanticpackage_constructor_exists():
    assert callable(frameweb_SemanticPackage.__init__)


def test_frameweb_semanticpackage_constructor_args():
    sig = inspect.signature(frameweb_SemanticPackage.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_mappinglib_is_not_abstract():
    assert not inspect.isabstract(frameweb_MappingLib)


def test_frameweb_mappinglib_constructor_exists():
    assert callable(frameweb_MappingLib.__init__)


def test_frameweb_mappinglib_constructor_args():
    sig = inspect.signature(frameweb_MappingLib.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_domainpackage_is_not_abstract():
    assert not inspect.isabstract(frameweb_DomainPackage)


def test_frameweb_domainpackage_constructor_exists():
    assert callable(frameweb_DomainPackage.__init__)


def test_frameweb_domainpackage_constructor_args():
    sig = inspect.signature(frameweb_DomainPackage.__init__)
    params = list(sig.parameters.keys())



def test_dependency_is_not_abstract():
    assert not inspect.isabstract(Dependency)


def test_dependency_constructor_exists():
    assert callable(Dependency.__init__)


def test_dependency_constructor_args():
    sig = inspect.signature(Dependency.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_navigationdependency_is_not_abstract():
    assert not inspect.isabstract(frameweb_NavigationDependency)


def test_frameweb_navigationdependency_constructor_exists():
    assert callable(frameweb_NavigationDependency.__init__)


def test_frameweb_navigationdependency_constructor_args():
    sig = inspect.signature(frameweb_NavigationDependency.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_chainingconstraint_is_not_abstract():
    assert not inspect.isabstract(frameweb_ChainingConstraint)


def test_frameweb_chainingconstraint_constructor_exists():
    assert callable(frameweb_ChainingConstraint.__init__)


def test_frameweb_chainingconstraint_constructor_args():
    sig = inspect.signature(frameweb_ChainingConstraint.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_pageconstraint_is_not_abstract():
    assert not inspect.isabstract(frameweb_PageConstraint)


def test_frameweb_pageconstraint_constructor_exists():
    assert callable(frameweb_PageConstraint.__init__)


def test_frameweb_pageconstraint_constructor_args():
    sig = inspect.signature(frameweb_PageConstraint.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_methodcosntraint_is_not_abstract():
    assert not inspect.isabstract(frameweb_MethodCosntraint)


def test_frameweb_methodcosntraint_constructor_exists():
    assert callable(frameweb_MethodCosntraint.__init__)


def test_frameweb_methodcosntraint_constructor_args():
    sig = inspect.signature(frameweb_MethodCosntraint.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_taglib_is_not_abstract():
    assert not inspect.isabstract(frameweb_TagLib)


def test_frameweb_taglib_constructor_exists():
    assert callable(frameweb_TagLib.__init__)


def test_frameweb_taglib_constructor_args():
    sig = inspect.signature(frameweb_TagLib.__init__)
    params = list(sig.parameters.keys())
    assert "prefix" in params, "Missing parameter 'prefix'"

def test_frameweb_taglib_has_prefix():
    assert hasattr(frameweb_TagLib, "prefix")
    descriptor = None
    for klass in frameweb_TagLib.__mro__:
        if "prefix" in klass.__dict__:
            descriptor = klass.__dict__["prefix"]
            break
    assert isinstance(descriptor, property)



def test_serviceassociation_is_not_abstract():
    assert not inspect.isabstract(ServiceAssociation)


def test_serviceassociation_constructor_exists():
    assert callable(ServiceAssociation.__init__)


def test_serviceassociation_constructor_args():
    sig = inspect.signature(ServiceAssociation.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_daoserviceassociation_is_not_abstract():
    assert not inspect.isabstract(frameweb_DAOServiceAssociation)


def test_frameweb_daoserviceassociation_constructor_exists():
    assert callable(frameweb_DAOServiceAssociation.__init__)


def test_frameweb_daoserviceassociation_constructor_args():
    sig = inspect.signature(frameweb_DAOServiceAssociation.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_servicecontrollerassociation_is_not_abstract():
    assert not inspect.isabstract(frameweb_ServiceControllerAssociation)


def test_frameweb_servicecontrollerassociation_constructor_exists():
    assert callable(frameweb_ServiceControllerAssociation.__init__)


def test_frameweb_servicecontrollerassociation_constructor_args():
    sig = inspect.signature(frameweb_ServiceControllerAssociation.__init__)
    params = list(sig.parameters.keys())



def test_generalization__is_not_abstract():
    assert not inspect.isabstract(Generalization_)


def test_generalization__constructor_exists():
    assert callable(Generalization_.__init__)


def test_generalization__constructor_args():
    sig = inspect.signature(Generalization_.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_daogeneralization_is_not_abstract():
    assert not inspect.isabstract(frameweb_DAOGeneralization)


def test_frameweb_daogeneralization_constructor_exists():
    assert callable(frameweb_DAOGeneralization.__init__)


def test_frameweb_daogeneralization_constructor_args():
    sig = inspect.signature(frameweb_DAOGeneralization.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_navigationgeneralization_is_not_abstract():
    assert not inspect.isabstract(frameweb_NavigationGeneralization)


def test_frameweb_navigationgeneralization_constructor_exists():
    assert callable(frameweb_NavigationGeneralization.__init__)


def test_frameweb_navigationgeneralization_constructor_args():
    sig = inspect.signature(frameweb_NavigationGeneralization.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_domaingeneralization_is_not_abstract():
    assert not inspect.isabstract(frameweb_DomainGeneralization)


def test_frameweb_domaingeneralization_constructor_exists():
    assert callable(frameweb_DomainGeneralization.__init__)


def test_frameweb_domaingeneralization_constructor_args():
    sig = inspect.signature(frameweb_DomainGeneralization.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_servicegeneralization_is_not_abstract():
    assert not inspect.isabstract(frameweb_ServiceGeneralization)


def test_frameweb_servicegeneralization_constructor_exists():
    assert callable(frameweb_ServiceGeneralization.__init__)


def test_frameweb_servicegeneralization_constructor_args():
    sig = inspect.signature(frameweb_ServiceGeneralization.__init__)
    params = list(sig.parameters.keys())



def test_operation_is_not_abstract():
    assert not inspect.isabstract(Operation)


def test_operation_constructor_exists():
    assert callable(Operation.__init__)


def test_operation_constructor_args():
    sig = inspect.signature(Operation.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_servicemethod_is_not_abstract():
    assert not inspect.isabstract(frameweb_ServiceMethod)


def test_frameweb_servicemethod_constructor_exists():
    assert callable(frameweb_ServiceMethod.__init__)


def test_frameweb_servicemethod_constructor_args():
    sig = inspect.signature(frameweb_ServiceMethod.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_domainmethod_is_not_abstract():
    assert not inspect.isabstract(frameweb_DomainMethod)


def test_frameweb_domainmethod_constructor_exists():
    assert callable(frameweb_DomainMethod.__init__)


def test_frameweb_domainmethod_constructor_args():
    sig = inspect.signature(frameweb_DomainMethod.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_daomethod_is_not_abstract():
    assert not inspect.isabstract(frameweb_DAOMethod)


def test_frameweb_daomethod_constructor_exists():
    assert callable(frameweb_DAOMethod.__init__)


def test_frameweb_daomethod_constructor_args():
    sig = inspect.signature(frameweb_DAOMethod.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_resultconstraint_is_not_abstract():
    assert not inspect.isabstract(frameweb_ResultConstraint)


def test_frameweb_resultconstraint_constructor_exists():
    assert callable(frameweb_ResultConstraint.__init__)


def test_frameweb_resultconstraint_constructor_args():
    sig = inspect.signature(frameweb_ResultConstraint.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_frontcontrollermethod_is_not_abstract():
    assert not inspect.isabstract(frameweb_FrontControllerMethod)


def test_frameweb_frontcontrollermethod_constructor_exists():
    assert callable(frameweb_FrontControllerMethod.__init__)


def test_frameweb_frontcontrollermethod_constructor_args():
    sig = inspect.signature(frameweb_FrontControllerMethod.__init__)
    params = list(sig.parameters.keys())
    assert "isDefault" in params, "Missing parameter 'isDefault'"

def test_frameweb_frontcontrollermethod_has_isDefault():
    assert hasattr(frameweb_FrontControllerMethod, "isDefault")
    descriptor = None
    for klass in frameweb_FrontControllerMethod.__mro__:
        if "isDefault" in klass.__dict__:
            descriptor = klass.__dict__["isDefault"]
            break
    assert isinstance(descriptor, property)



def test_navigationdependency_is_not_abstract():
    assert not inspect.isabstract(NavigationDependency)


def test_navigationdependency_constructor_exists():
    assert callable(NavigationDependency.__init__)


def test_navigationdependency_constructor_args():
    sig = inspect.signature(NavigationDependency.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_frontcontrollerdependency_is_not_abstract():
    assert not inspect.isabstract(frameweb_FrontControllerDependency)


def test_frameweb_frontcontrollerdependency_constructor_exists():
    assert callable(frameweb_FrontControllerDependency.__init__)


def test_frameweb_frontcontrollerdependency_constructor_args():
    sig = inspect.signature(frameweb_FrontControllerDependency.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_chainingdependency_is_not_abstract():
    assert not inspect.isabstract(frameweb_ChainingDependency)


def test_frameweb_chainingdependency_constructor_exists():
    assert callable(frameweb_ChainingDependency.__init__)


def test_frameweb_chainingdependency_constructor_args():
    sig = inspect.signature(frameweb_ChainingDependency.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_pagedependency_is_not_abstract():
    assert not inspect.isabstract(frameweb_PageDependency)


def test_frameweb_pagedependency_constructor_exists():
    assert callable(frameweb_PageDependency.__init__)


def test_frameweb_pagedependency_constructor_args():
    sig = inspect.signature(frameweb_PageDependency.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_resultdependency_is_not_abstract():
    assert not inspect.isabstract(frameweb_ResultDependency)


def test_frameweb_resultdependency_constructor_exists():
    assert callable(frameweb_ResultDependency.__init__)


def test_frameweb_resultdependency_constructor_args():
    sig = inspect.signature(frameweb_ResultDependency.__init__)
    params = list(sig.parameters.keys())
    assert "execute" in params, "Missing parameter 'execute'"
    assert "ajax" in params, "Missing parameter 'ajax'"
    assert "render" in params, "Missing parameter 'render'"

def test_frameweb_resultdependency_has_execute():
    assert hasattr(frameweb_ResultDependency, "execute")
    descriptor = None
    for klass in frameweb_ResultDependency.__mro__:
        if "execute" in klass.__dict__:
            descriptor = klass.__dict__["execute"]
            break
    assert isinstance(descriptor, property)

def test_frameweb_resultdependency_has_ajax():
    assert hasattr(frameweb_ResultDependency, "ajax")
    descriptor = None
    for klass in frameweb_ResultDependency.__mro__:
        if "ajax" in klass.__dict__:
            descriptor = klass.__dict__["ajax"]
            break
    assert isinstance(descriptor, property)

def test_frameweb_resultdependency_has_render():
    assert hasattr(frameweb_ResultDependency, "render")
    descriptor = None
    for klass in frameweb_ResultDependency.__mro__:
        if "render" in klass.__dict__:
            descriptor = klass.__dict__["render"]
            break
    assert isinstance(descriptor, property)



def test_navigationattribute_is_not_abstract():
    assert not inspect.isabstract(NavigationAttribute)


def test_navigationattribute_constructor_exists():
    assert callable(NavigationAttribute.__init__)


def test_navigationattribute_constructor_args():
    sig = inspect.signature(NavigationAttribute.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_uicomponentfield_is_not_abstract():
    assert not inspect.isabstract(frameweb_UIComponentField)


def test_frameweb_uicomponentfield_constructor_exists():
    assert callable(frameweb_UIComponentField.__init__)


def test_frameweb_uicomponentfield_constructor_args():
    sig = inspect.signature(frameweb_UIComponentField.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_ioparameter_is_not_abstract():
    assert not inspect.isabstract(frameweb_IOParameter)


def test_frameweb_ioparameter_constructor_exists():
    assert callable(frameweb_IOParameter.__init__)


def test_frameweb_ioparameter_constructor_args():
    sig = inspect.signature(frameweb_IOParameter.__init__)
    params = list(sig.parameters.keys())



def test_interfacerealization_is_not_abstract():
    assert not inspect.isabstract(InterfaceRealization)


def test_interfacerealization_constructor_exists():
    assert callable(InterfaceRealization.__init__)


def test_interfacerealization_constructor_args():
    sig = inspect.signature(InterfaceRealization.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_sevicerealization_is_not_abstract():
    assert not inspect.isabstract(frameweb_SeviceRealization)


def test_frameweb_sevicerealization_constructor_exists():
    assert callable(frameweb_SeviceRealization.__init__)


def test_frameweb_sevicerealization_constructor_args():
    sig = inspect.signature(frameweb_SeviceRealization.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_daorealization_is_not_abstract():
    assert not inspect.isabstract(frameweb_DAORealization)


def test_frameweb_daorealization_constructor_exists():
    assert callable(frameweb_DAORealization.__init__)


def test_frameweb_daorealization_constructor_args():
    sig = inspect.signature(frameweb_DAORealization.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_annotation_is_not_abstract():
    assert not inspect.isabstract(frameweb_Annotation)


def test_frameweb_annotation_constructor_exists():
    assert callable(frameweb_Annotation.__init__)


def test_frameweb_annotation_constructor_args():
    sig = inspect.signature(frameweb_Annotation.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_domainclass_is_not_abstract():
    assert not inspect.isabstract(frameweb_DomainClass)


def test_frameweb_domainclass_constructor_exists():
    assert callable(frameweb_DomainClass.__init__)


def test_frameweb_domainclass_constructor_args():
    sig = inspect.signature(frameweb_DomainClass.__init__)
    params = list(sig.parameters.keys())
    assert "table" in params, "Missing parameter 'table'"

def test_frameweb_domainclass_has_table():
    assert hasattr(frameweb_DomainClass, "table")
    descriptor = None
    for klass in frameweb_DomainClass.__mro__:
        if "table" in klass.__dict__:
            descriptor = klass.__dict__["table"]
            break
    assert isinstance(descriptor, property)



def test_frameweb_navigationclass_is_not_abstract():
    assert not inspect.isabstract(frameweb_NavigationClass)


def test_frameweb_navigationclass_constructor_exists():
    assert callable(frameweb_NavigationClass.__init__)


def test_frameweb_navigationclass_constructor_args():
    sig = inspect.signature(frameweb_NavigationClass.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_axiom_is_not_abstract():
    assert not inspect.isabstract(frameweb_Axiom)


def test_frameweb_axiom_constructor_exists():
    assert callable(frameweb_Axiom.__init__)


def test_frameweb_axiom_constructor_args():
    sig = inspect.signature(frameweb_Axiom.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_serviceclass_is_not_abstract():
    assert not inspect.isabstract(frameweb_ServiceClass)


def test_frameweb_serviceclass_constructor_exists():
    assert callable(frameweb_ServiceClass.__init__)


def test_frameweb_serviceclass_constructor_args():
    sig = inspect.signature(frameweb_ServiceClass.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_frontcontrollerclass_is_not_abstract():
    assert not inspect.isabstract(frameweb_FrontControllerClass)


def test_frameweb_frontcontrollerclass_constructor_exists():
    assert callable(frameweb_FrontControllerClass.__init__)


def test_frameweb_frontcontrollerclass_constructor_args():
    sig = inspect.signature(frameweb_FrontControllerClass.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_vocabularyclassexpression_is_not_abstract():
    assert not inspect.isabstract(frameweb_VocabularyClassExpression)


def test_frameweb_vocabularyclassexpression_constructor_exists():
    assert callable(frameweb_VocabularyClassExpression.__init__)


def test_frameweb_vocabularyclassexpression_constructor_args():
    sig = inspect.signature(frameweb_VocabularyClassExpression.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_result_is_not_abstract():
    assert not inspect.isabstract(frameweb_Result)


def test_frameweb_result_constructor_exists():
    assert callable(frameweb_Result.__init__)


def test_frameweb_result_constructor_args():
    sig = inspect.signature(frameweb_Result.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_daoclass_is_not_abstract():
    assert not inspect.isabstract(frameweb_DAOClass)


def test_frameweb_daoclass_constructor_exists():
    assert callable(frameweb_DAOClass.__init__)


def test_frameweb_daoclass_constructor_args():
    sig = inspect.signature(frameweb_DAOClass.__init__)
    params = list(sig.parameters.keys())
    assert "sufix" in params, "Missing parameter 'sufix'"
    assert "infix" in params, "Missing parameter 'infix'"
    assert "prefix" in params, "Missing parameter 'prefix'"

def test_frameweb_daoclass_has_sufix():
    assert hasattr(frameweb_DAOClass, "sufix")
    descriptor = None
    for klass in frameweb_DAOClass.__mro__:
        if "sufix" in klass.__dict__:
            descriptor = klass.__dict__["sufix"]
            break
    assert isinstance(descriptor, property)

def test_frameweb_daoclass_has_infix():
    assert hasattr(frameweb_DAOClass, "infix")
    descriptor = None
    for klass in frameweb_DAOClass.__mro__:
        if "infix" in klass.__dict__:
            descriptor = klass.__dict__["infix"]
            break
    assert isinstance(descriptor, property)

def test_frameweb_daoclass_has_prefix():
    assert hasattr(frameweb_DAOClass, "prefix")
    descriptor = None
    for klass in frameweb_DAOClass.__mro__:
        if "prefix" in klass.__dict__:
            descriptor = klass.__dict__["prefix"]
            break
    assert isinstance(descriptor, property)



def test_interface_is_not_abstract():
    assert not inspect.isabstract(Interface)


def test_interface_constructor_exists():
    assert callable(Interface.__init__)


def test_interface_constructor_args():
    sig = inspect.signature(Interface.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_serviceinterface_is_not_abstract():
    assert not inspect.isabstract(frameweb_ServiceInterface)


def test_frameweb_serviceinterface_constructor_exists():
    assert callable(frameweb_ServiceInterface.__init__)


def test_frameweb_serviceinterface_constructor_args():
    sig = inspect.signature(frameweb_ServiceInterface.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_daointerface_is_not_abstract():
    assert not inspect.isabstract(frameweb_DAOInterface)


def test_frameweb_daointerface_constructor_exists():
    assert callable(frameweb_DAOInterface.__init__)


def test_frameweb_daointerface_constructor_args():
    sig = inspect.signature(frameweb_DAOInterface.__init__)
    params = list(sig.parameters.keys())
    assert "sufix" in params, "Missing parameter 'sufix'"
    assert "infix" in params, "Missing parameter 'infix'"

def test_frameweb_daointerface_has_sufix():
    assert hasattr(frameweb_DAOInterface, "sufix")
    descriptor = None
    for klass in frameweb_DAOInterface.__mro__:
        if "sufix" in klass.__dict__:
            descriptor = klass.__dict__["sufix"]
            break
    assert isinstance(descriptor, property)

def test_frameweb_daointerface_has_infix():
    assert hasattr(frameweb_DAOInterface, "infix")
    descriptor = None
    for klass in frameweb_DAOInterface.__mro__:
        if "infix" in klass.__dict__:
            descriptor = klass.__dict__["infix"]
            break
    assert isinstance(descriptor, property)



def test_navigationclass_is_not_abstract():
    assert not inspect.isabstract(NavigationClass)


def test_navigationclass_constructor_exists():
    assert callable(NavigationClass.__init__)


def test_navigationclass_constructor_args():
    sig = inspect.signature(NavigationClass.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_uicomponent_is_not_abstract():
    assert not inspect.isabstract(frameweb_UIComponent)


def test_frameweb_uicomponent_constructor_exists():
    assert callable(frameweb_UIComponent.__init__)


def test_frameweb_uicomponent_constructor_args():
    sig = inspect.signature(frameweb_UIComponent.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_template_is_not_abstract():
    assert not inspect.isabstract(frameweb_Template)


def test_frameweb_template_constructor_exists():
    assert callable(frameweb_Template.__init__)


def test_frameweb_template_constructor_args():
    sig = inspect.signature(frameweb_Template.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_page_is_not_abstract():
    assert not inspect.isabstract(frameweb_Page)


def test_frameweb_page_constructor_exists():
    assert callable(frameweb_Page.__init__)


def test_frameweb_page_constructor_args():
    sig = inspect.signature(frameweb_Page.__init__)
    params = list(sig.parameters.keys())



def test_domainattribute_is_not_abstract():
    assert not inspect.isabstract(DomainAttribute)


def test_domainattribute_constructor_exists():
    assert callable(DomainAttribute.__init__)


def test_domainattribute_constructor_args():
    sig = inspect.signature(DomainAttribute.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_lobattribute_is_not_abstract():
    assert not inspect.isabstract(frameweb_LOBAttribute)


def test_frameweb_lobattribute_constructor_exists():
    assert callable(frameweb_LOBAttribute.__init__)


def test_frameweb_lobattribute_constructor_args():
    sig = inspect.signature(frameweb_LOBAttribute.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_embeddedattribute_is_not_abstract():
    assert not inspect.isabstract(frameweb_EmbeddedAttribute)


def test_frameweb_embeddedattribute_constructor_exists():
    assert callable(frameweb_EmbeddedAttribute.__init__)


def test_frameweb_embeddedattribute_constructor_args():
    sig = inspect.signature(frameweb_EmbeddedAttribute.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_idattribute_is_not_abstract():
    assert not inspect.isabstract(frameweb_IdAttribute)


def test_frameweb_idattribute_constructor_exists():
    assert callable(frameweb_IdAttribute.__init__)


def test_frameweb_idattribute_constructor_args():
    sig = inspect.signature(frameweb_IdAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "generation" in params, "Missing parameter 'generation'"

def test_frameweb_idattribute_has_generation():
    assert hasattr(frameweb_IdAttribute, "generation")
    descriptor = None
    for klass in frameweb_IdAttribute.__mro__:
        if "generation" in klass.__dict__:
            descriptor = klass.__dict__["generation"]
            break
    assert isinstance(descriptor, property)



def test_frameweb_decimalattribute_is_not_abstract():
    assert not inspect.isabstract(frameweb_DecimalAttribute)


def test_frameweb_decimalattribute_constructor_exists():
    assert callable(frameweb_DecimalAttribute.__init__)


def test_frameweb_decimalattribute_constructor_args():
    sig = inspect.signature(frameweb_DecimalAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "decimalPrecision" in params, "Missing parameter 'decimalPrecision'"
    assert "decimalScale" in params, "Missing parameter 'decimalScale'"

def test_frameweb_decimalattribute_has_decimalPrecision():
    assert hasattr(frameweb_DecimalAttribute, "decimalPrecision")
    descriptor = None
    for klass in frameweb_DecimalAttribute.__mro__:
        if "decimalPrecision" in klass.__dict__:
            descriptor = klass.__dict__["decimalPrecision"]
            break
    assert isinstance(descriptor, property)

def test_frameweb_decimalattribute_has_decimalScale():
    assert hasattr(frameweb_DecimalAttribute, "decimalScale")
    descriptor = None
    for klass in frameweb_DecimalAttribute.__mro__:
        if "decimalScale" in klass.__dict__:
            descriptor = klass.__dict__["decimalScale"]
            break
    assert isinstance(descriptor, property)



def test_frameweb_datetimeattribute_is_not_abstract():
    assert not inspect.isabstract(frameweb_DateTimeAttribute)


def test_frameweb_datetimeattribute_constructor_exists():
    assert callable(frameweb_DateTimeAttribute.__init__)


def test_frameweb_datetimeattribute_constructor_args():
    sig = inspect.signature(frameweb_DateTimeAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "dateTimePrecision" in params, "Missing parameter 'dateTimePrecision'"

def test_frameweb_datetimeattribute_has_dateTimePrecision():
    assert hasattr(frameweb_DateTimeAttribute, "dateTimePrecision")
    descriptor = None
    for klass in frameweb_DateTimeAttribute.__mro__:
        if "dateTimePrecision" in klass.__dict__:
            descriptor = klass.__dict__["dateTimePrecision"]
            break
    assert isinstance(descriptor, property)



def test_frameweb_versionattribute_is_not_abstract():
    assert not inspect.isabstract(frameweb_VersionAttribute)


def test_frameweb_versionattribute_constructor_exists():
    assert callable(frameweb_VersionAttribute.__init__)


def test_frameweb_versionattribute_constructor_args():
    sig = inspect.signature(frameweb_VersionAttribute.__init__)
    params = list(sig.parameters.keys())



def test_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_property_constructor_exists():
    assert callable(Property.__init__)


def test_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_daoattribute_is_not_abstract():
    assert not inspect.isabstract(frameweb_DAOAttribute)


def test_frameweb_daoattribute_constructor_exists():
    assert callable(frameweb_DAOAttribute.__init__)


def test_frameweb_daoattribute_constructor_args():
    sig = inspect.signature(frameweb_DAOAttribute.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_resultproperty_is_not_abstract():
    assert not inspect.isabstract(frameweb_ResultProperty)


def test_frameweb_resultproperty_constructor_exists():
    assert callable(frameweb_ResultProperty.__init__)


def test_frameweb_resultproperty_constructor_args():
    sig = inspect.signature(frameweb_ResultProperty.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_attributemappingproperty_is_not_abstract():
    assert not inspect.isabstract(frameweb_AttributeMappingProperty)


def test_frameweb_attributemappingproperty_constructor_exists():
    assert callable(frameweb_AttributeMappingProperty.__init__)


def test_frameweb_attributemappingproperty_constructor_args():
    sig = inspect.signature(frameweb_AttributeMappingProperty.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_domainproperty_is_not_abstract():
    assert not inspect.isabstract(frameweb_DomainProperty)


def test_frameweb_domainproperty_constructor_exists():
    assert callable(frameweb_DomainProperty.__init__)


def test_frameweb_domainproperty_constructor_args():
    sig = inspect.signature(frameweb_DomainProperty.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_navigationproperty_is_not_abstract():
    assert not inspect.isabstract(frameweb_NavigationProperty)


def test_frameweb_navigationproperty_constructor_exists():
    assert callable(frameweb_NavigationProperty.__init__)


def test_frameweb_navigationproperty_constructor_args():
    sig = inspect.signature(frameweb_NavigationProperty.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_serviceattribute_is_not_abstract():
    assert not inspect.isabstract(frameweb_ServiceAttribute)


def test_frameweb_serviceattribute_constructor_exists():
    assert callable(frameweb_ServiceAttribute.__init__)


def test_frameweb_serviceattribute_constructor_args():
    sig = inspect.signature(frameweb_ServiceAttribute.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_iri_is_not_abstract():
    assert not inspect.isabstract(frameweb_IRI)


def test_frameweb_iri_constructor_exists():
    assert callable(frameweb_IRI.__init__)


def test_frameweb_iri_constructor_args():
    sig = inspect.signature(frameweb_IRI.__init__)
    params = list(sig.parameters.keys())
    assert "iriVersion" in params, "Missing parameter 'iriVersion'"
    assert "iri" in params, "Missing parameter 'iri'"

def test_frameweb_iri_has_iriVersion():
    assert hasattr(frameweb_IRI, "iriVersion")
    descriptor = None
    for klass in frameweb_IRI.__mro__:
        if "iriVersion" in klass.__dict__:
            descriptor = klass.__dict__["iriVersion"]
            break
    assert isinstance(descriptor, property)

def test_frameweb_iri_has_iri():
    assert hasattr(frameweb_IRI, "iri")
    descriptor = None
    for klass in frameweb_IRI.__mro__:
        if "iri" in klass.__dict__:
            descriptor = klass.__dict__["iri"]
            break
    assert isinstance(descriptor, property)



def test_frameweb_vocabularyproperty_is_not_abstract():
    assert not inspect.isabstract(frameweb_VocabularyProperty)


def test_frameweb_vocabularyproperty_constructor_exists():
    assert callable(frameweb_VocabularyProperty.__init__)


def test_frameweb_vocabularyproperty_constructor_args():
    sig = inspect.signature(frameweb_VocabularyProperty.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_navigationattribute_is_not_abstract():
    assert not inspect.isabstract(frameweb_NavigationAttribute)


def test_frameweb_navigationattribute_constructor_exists():
    assert callable(frameweb_NavigationAttribute.__init__)


def test_frameweb_navigationattribute_constructor_args():
    sig = inspect.signature(frameweb_NavigationAttribute.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_classmappingpropery_is_not_abstract():
    assert not inspect.isabstract(frameweb_ClassMappingPropery)


def test_frameweb_classmappingpropery_constructor_exists():
    assert callable(frameweb_ClassMappingPropery.__init__)


def test_frameweb_classmappingpropery_constructor_args():
    sig = inspect.signature(frameweb_ClassMappingPropery.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_controllerproperty_is_not_abstract():
    assert not inspect.isabstract(frameweb_ControllerProperty)


def test_frameweb_controllerproperty_constructor_exists():
    assert callable(frameweb_ControllerProperty.__init__)


def test_frameweb_controllerproperty_constructor_args():
    sig = inspect.signature(frameweb_ControllerProperty.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_individual_is_not_abstract():
    assert not inspect.isabstract(frameweb_Individual)


def test_frameweb_individual_constructor_exists():
    assert callable(frameweb_Individual.__init__)


def test_frameweb_individual_constructor_args():
    sig = inspect.signature(frameweb_Individual.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_tagproperty_is_not_abstract():
    assert not inspect.isabstract(frameweb_TagProperty)


def test_frameweb_tagproperty_constructor_exists():
    assert callable(frameweb_TagProperty.__init__)


def test_frameweb_tagproperty_constructor_args():
    sig = inspect.signature(frameweb_TagProperty.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_domainattribute_is_not_abstract():
    assert not inspect.isabstract(frameweb_DomainAttribute)


def test_frameweb_domainattribute_constructor_exists():
    assert callable(frameweb_DomainAttribute.__init__)


def test_frameweb_domainattribute_constructor_args():
    sig = inspect.signature(frameweb_DomainAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "isNull" in params, "Missing parameter 'isNull'"
    assert "isPersistent" in params, "Missing parameter 'isPersistent'"
    assert "size" in params, "Missing parameter 'size'"

def test_frameweb_domainattribute_has_isNull():
    assert hasattr(frameweb_DomainAttribute, "isNull")
    descriptor = None
    for klass in frameweb_DomainAttribute.__mro__:
        if "isNull" in klass.__dict__:
            descriptor = klass.__dict__["isNull"]
            break
    assert isinstance(descriptor, property)

def test_frameweb_domainattribute_has_isPersistent():
    assert hasattr(frameweb_DomainAttribute, "isPersistent")
    descriptor = None
    for klass in frameweb_DomainAttribute.__mro__:
        if "isPersistent" in klass.__dict__:
            descriptor = klass.__dict__["isPersistent"]
            break
    assert isinstance(descriptor, property)

def test_frameweb_domainattribute_has_size():
    assert hasattr(frameweb_DomainAttribute, "size")
    descriptor = None
    for klass in frameweb_DomainAttribute.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_association_is_not_abstract():
    assert not inspect.isabstract(Association)


def test_association_constructor_exists():
    assert callable(Association.__init__)


def test_association_constructor_args():
    sig = inspect.signature(Association.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_vocabularyassociation_is_not_abstract():
    assert not inspect.isabstract(frameweb_VocabularyAssociation)


def test_frameweb_vocabularyassociation_constructor_exists():
    assert callable(frameweb_VocabularyAssociation.__init__)


def test_frameweb_vocabularyassociation_constructor_args():
    sig = inspect.signature(frameweb_VocabularyAssociation.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_serviceassociation_is_not_abstract():
    assert not inspect.isabstract(frameweb_ServiceAssociation)


def test_frameweb_serviceassociation_constructor_exists():
    assert callable(frameweb_ServiceAssociation.__init__)


def test_frameweb_serviceassociation_constructor_args():
    sig = inspect.signature(frameweb_ServiceAssociation.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_navigationassociation_is_not_abstract():
    assert not inspect.isabstract(frameweb_NavigationAssociation)


def test_frameweb_navigationassociation_constructor_exists():
    assert callable(frameweb_NavigationAssociation.__init__)


def test_frameweb_navigationassociation_constructor_args():
    sig = inspect.signature(frameweb_NavigationAssociation.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_domainassociation_is_not_abstract():
    assert not inspect.isabstract(frameweb_DomainAssociation)


def test_frameweb_domainassociation_constructor_exists():
    assert callable(frameweb_DomainAssociation.__init__)


def test_frameweb_domainassociation_constructor_args():
    sig = inspect.signature(frameweb_DomainAssociation.__init__)
    params = list(sig.parameters.keys())
    assert "order" in params, "Missing parameter 'order'"
    assert "fetch" in params, "Missing parameter 'fetch'"
    assert "collection" in params, "Missing parameter 'collection'"
    assert "cascade" in params, "Missing parameter 'cascade'"

def test_frameweb_domainassociation_has_order():
    assert hasattr(frameweb_DomainAssociation, "order")
    descriptor = None
    for klass in frameweb_DomainAssociation.__mro__:
        if "order" in klass.__dict__:
            descriptor = klass.__dict__["order"]
            break
    assert isinstance(descriptor, property)

def test_frameweb_domainassociation_has_fetch():
    assert hasattr(frameweb_DomainAssociation, "fetch")
    descriptor = None
    for klass in frameweb_DomainAssociation.__mro__:
        if "fetch" in klass.__dict__:
            descriptor = klass.__dict__["fetch"]
            break
    assert isinstance(descriptor, property)

def test_frameweb_domainassociation_has_collection():
    assert hasattr(frameweb_DomainAssociation, "collection")
    descriptor = None
    for klass in frameweb_DomainAssociation.__mro__:
        if "collection" in klass.__dict__:
            descriptor = klass.__dict__["collection"]
            break
    assert isinstance(descriptor, property)

def test_frameweb_domainassociation_has_cascade():
    assert hasattr(frameweb_DomainAssociation, "cascade")
    descriptor = None
    for klass in frameweb_DomainAssociation.__mro__:
        if "cascade" in klass.__dict__:
            descriptor = klass.__dict__["cascade"]
            break
    assert isinstance(descriptor, property)



def test_framewebmodel_is_not_abstract():
    assert not inspect.isabstract(FramewebModel)


def test_framewebmodel_constructor_exists():
    assert callable(FramewebModel.__init__)


def test_framewebmodel_constructor_args():
    sig = inspect.signature(FramewebModel.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_persistencemodel_is_not_abstract():
    assert not inspect.isabstract(frameweb_PersistenceModel)


def test_frameweb_persistencemodel_constructor_exists():
    assert callable(frameweb_PersistenceModel.__init__)


def test_frameweb_persistencemodel_constructor_args():
    sig = inspect.signature(frameweb_PersistenceModel.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_applicationmodel_is_not_abstract():
    assert not inspect.isabstract(frameweb_ApplicationModel)


def test_frameweb_applicationmodel_constructor_exists():
    assert callable(frameweb_ApplicationModel.__init__)


def test_frameweb_applicationmodel_constructor_args():
    sig = inspect.signature(frameweb_ApplicationModel.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_vocabularymodel_is_not_abstract():
    assert not inspect.isabstract(frameweb_VocabularyModel)


def test_frameweb_vocabularymodel_constructor_exists():
    assert callable(frameweb_VocabularyModel.__init__)


def test_frameweb_vocabularymodel_constructor_args():
    sig = inspect.signature(frameweb_VocabularyModel.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_navigationmodel_is_not_abstract():
    assert not inspect.isabstract(frameweb_NavigationModel)


def test_frameweb_navigationmodel_constructor_exists():
    assert callable(frameweb_NavigationModel.__init__)


def test_frameweb_navigationmodel_constructor_args():
    sig = inspect.signature(frameweb_NavigationModel.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_entitymodel_is_not_abstract():
    assert not inspect.isabstract(frameweb_EntityModel)


def test_frameweb_entitymodel_constructor_exists():
    assert callable(frameweb_EntityModel.__init__)


def test_frameweb_entitymodel_constructor_args():
    sig = inspect.signature(frameweb_EntityModel.__init__)
    params = list(sig.parameters.keys())



def test_profile_is_not_abstract():
    assert not inspect.isabstract(Profile)


def test_profile_constructor_exists():
    assert callable(Profile.__init__)


def test_profile_constructor_args():
    sig = inspect.signature(Profile.__init__)
    params = list(sig.parameters.keys())



def test_model_is_not_abstract():
    assert not inspect.isabstract(Model)


def test_model_constructor_exists():
    assert callable(Model.__init__)


def test_model_constructor_args():
    sig = inspect.signature(Model.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_frameworkprofile_is_not_abstract():
    assert not inspect.isabstract(frameweb_FrameworkProfile)


def test_frameweb_frameworkprofile_constructor_exists():
    assert callable(frameweb_FrameworkProfile.__init__)


def test_frameweb_frameworkprofile_constructor_args():
    sig = inspect.signature(frameweb_FrameworkProfile.__init__)
    params = list(sig.parameters.keys())
    assert "category" in params, "Missing parameter 'category'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_frameweb_frameworkprofile_has_category():
    assert hasattr(frameweb_FrameworkProfile, "category")
    descriptor = None
    for klass in frameweb_FrameworkProfile.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)

def test_frameweb_frameworkprofile_has_kind():
    assert hasattr(frameweb_FrameworkProfile, "kind")
    descriptor = None
    for klass in frameweb_FrameworkProfile.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_frameweb_framewebmodel_is_not_abstract():
    assert not inspect.isabstract(frameweb_FramewebModel)


def test_frameweb_framewebmodel_constructor_exists():
    assert callable(frameweb_FramewebModel.__init__)


def test_frameweb_framewebmodel_constructor_args():
    sig = inspect.signature(frameweb_FramewebModel.__init__)
    params = list(sig.parameters.keys())



def test_frameweb_framewebproject_is_not_abstract():
    assert not inspect.isabstract(frameweb_FramewebProject)


def test_frameweb_framewebproject_constructor_exists():
    assert callable(frameweb_FramewebProject.__init__)


def test_frameweb_framewebproject_constructor_args():
    sig = inspect.signature(frameweb_FramewebProject.__init__)
    params = list(sig.parameters.keys())

def test_fetch_exists():
    # Check that the Enumeration exists
    assert Fetch is not None

def test_fetch_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Fetch]
    expected_literals = [
        "lazy",
        "eager",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Fetch"

def test_order_exists():
    # Check that the Enumeration exists
    assert Order is not None

def test_order_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Order]
    expected_literals = [
        "columnNameAsc",
        "columnNameDesc",
        "natural",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Order"

def test_generation_exists():
    # Check that the Enumeration exists
    assert Generation is not None

def test_generation_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Generation]
    expected_literals = [
        "none",
        "sequence",
        "table",
        "auto",
        "identity",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Generation"

def test_cascade_exists():
    # Check that the Enumeration exists
    assert Cascade is not None

def test_cascade_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Cascade]
    expected_literals = [
        "remove",
        "none",
        "merge",
        "persist",
        "refresh",
        "all",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Cascade"

def test_frameworkcategorylist_exists():
    # Check that the Enumeration exists
    assert FrameworkCategoryList is not None

def test_frameworkcategorylist_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FrameworkCategoryList]
    expected_literals = [
        "FrontController",
        "DependencyInjection",
        "ObjetoRelacional",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FrameworkCategoryList"

def test_datetimeprecision_exists():
    # Check that the Enumeration exists
    assert DateTimePrecision is not None

def test_datetimeprecision_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DateTimePrecision]
    expected_literals = [
        "timestamp",
        "time",
        "date",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DateTimePrecision"

def test_collection_exists():
    # Check that the Enumeration exists
    assert Collection is not None

def test_collection_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Collection]
    expected_literals = [
        "list",
        "set",
        "map",
        "bag",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Collection"

def test_inheritancemapping_exists():
    # Check that the Enumeration exists
    assert InheritanceMapping is not None

def test_inheritancemapping_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InheritanceMapping]
    expected_literals = [
        "join",
        "union",
        "singletable",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InheritanceMapping"

def test_frameworkkindlist_exists():
    # Check that the Enumeration exists
    assert FrameworkKindList is not None

def test_frameworkkindlist_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FrameworkKindList]
    expected_literals = [
        "Custom",
        "FrameworkImplementation",
        "StandardSpecification",
        "FrameworkSpecification",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FrameworkKindList"

def test_constantnamelist_exists():
    # Check that the Enumeration exists
    assert ConstantNameList is not None

def test_constantnamelist_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConstantNameList]
    expected_literals = [
        "Persistence",
        "Domain",
        "View",
        "DAO",
        "base",
        "Controller",
        "impl",
        "interface",
        "class_",
        "Application",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConstantNameList"


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
LiteralString_strategy = st.builds(
    LiteralString,
)
frameweb_VocabularyLiteral_strategy = st.builds(
    frameweb_VocabularyLiteral,
)
VocabularyClassExpression_strategy = st.builds(
    VocabularyClassExpression,
)
Individual_strategy = st.builds(
    Individual,
)
frameweb_AnonymousIndividual_strategy = st.builds(
    frameweb_AnonymousIndividual,
)
DataType_strategy = st.builds(
    DataType,
)
VocabularyAssociation_strategy = st.builds(
    VocabularyAssociation,
)
VocabularyEntity_strategy = st.builds(
    VocabularyEntity,
)
frameweb_DataProperty_strategy = st.builds(
    frameweb_DataProperty,
)
frameweb_VocabularyClass_strategy = st.builds(
    frameweb_VocabularyClass,
)
frameweb_NamedIndividual_strategy = st.builds(
    frameweb_NamedIndividual,
)
frameweb_AnnotationProperty_strategy = st.builds(
    frameweb_AnnotationProperty,
)
frameweb_VocabularyDataType_strategy = st.builds(
    frameweb_VocabularyDataType,
)
frameweb_ObjectProperty_strategy = st.builds(
    frameweb_ObjectProperty,
)
frameweb_NewInterface115_strategy = st.builds(
    frameweb_NewInterface115,
)
frameweb_Type_strategy = st.builds(
    frameweb_Type,
)
Relationship_strategy = st.builds(
    Relationship,
)
Classifier_strategy = st.builds(
    Classifier,
)
frameweb_VocabularyEntity_strategy = st.builds(
    frameweb_VocabularyEntity,
)
frameweb_Association_strategy = st.builds(
    frameweb_Association,
    isDerived=
        safe_text
)
frameweb_ValueSpecification_strategy = st.builds(
    frameweb_ValueSpecification,
)
frameweb_Class_strategy = st.builds(
    frameweb_Class,
)
frameweb_Interface_strategy = st.builds(
    frameweb_Interface,
)
frameweb_DataType_strategy = st.builds(
    frameweb_DataType,
)
DeploymentTarget_strategy = st.builds(
    DeploymentTarget,
)
ConnectableElement_strategy = st.builds(
    ConnectableElement,
)
StructuralFeature_strategy = st.builds(
    StructuralFeature,
)
frameweb_Property_strategy = st.builds(
    frameweb_Property,
    isDerivedUnion=
        safe_text,
    default=
        safe_text,
    isID=
        safe_text,
    isDerived=
        safe_text,
    aggregation=
        safe_text,
    isComposite=
        safe_text
)
FrameworkExtension_strategy = st.builds(
    FrameworkExtension,
)
frameweb_DomainExtension_strategy = st.builds(
    frameweb_DomainExtension,
)
frameweb_NavigationExtension_strategy = st.builds(
    frameweb_NavigationExtension,
)
NavigationProperty_strategy = st.builds(
    NavigationProperty,
)
frameweb_NavigationCompositionWhole_strategy = st.builds(
    frameweb_NavigationCompositionWhole,
)
frameweb_NavigationCompositionPart_strategy = st.builds(
    frameweb_NavigationCompositionPart,
)
ExtensionEnd_strategy = st.builds(
    ExtensionEnd,
)
frameweb_AttributeMappingExtensionEnd_strategy = st.builds(
    frameweb_AttributeMappingExtensionEnd,
)
frameweb_TagExtensionEnd_strategy = st.builds(
    frameweb_TagExtensionEnd,
)
frameweb_ClassMappingExtensionEnd_strategy = st.builds(
    frameweb_ClassMappingExtensionEnd,
)
frameweb_ResultExtensionEnd_strategy = st.builds(
    frameweb_ResultExtensionEnd,
)
frameweb_ControllerExtensionEnd_strategy = st.builds(
    frameweb_ControllerExtensionEnd,
)
DomainExtension_strategy = st.builds(
    DomainExtension,
)
frameweb_AttributeMappingExtension_strategy = st.builds(
    frameweb_AttributeMappingExtension,
)
frameweb_ClassMappingExtension_strategy = st.builds(
    frameweb_ClassMappingExtension,
)
ProfileApplication_strategy = st.builds(
    ProfileApplication,
)
frameweb_FrameworkApplication_strategy = st.builds(
    frameweb_FrameworkApplication,
)
NavigationExtension_strategy = st.builds(
    NavigationExtension,
)
frameweb_ControllerExtension_strategy = st.builds(
    frameweb_ControllerExtension,
)
frameweb_ResultExtension_strategy = st.builds(
    frameweb_ResultExtension,
)
frameweb_TagExtension_strategy = st.builds(
    frameweb_TagExtension,
)
Extension_strategy = st.builds(
    Extension,
)
frameweb_FrameworkExtension_strategy = st.builds(
    frameweb_FrameworkExtension,
)
GeneralizationSet_strategy = st.builds(
    GeneralizationSet,
)
frameweb_NavigationGeneralizationSet_strategy = st.builds(
    frameweb_NavigationGeneralizationSet,
)
frameweb_ServiceGeneralizationSet_strategy = st.builds(
    frameweb_ServiceGeneralizationSet,
)
frameweb_DAOGeneralizationSet_strategy = st.builds(
    frameweb_DAOGeneralizationSet,
)
frameweb_DomainGeneralizationSet_strategy = st.builds(
    frameweb_DomainGeneralizationSet,
    mapping=
        safe_text
)
NavigationConstraint_strategy = st.builds(
    NavigationConstraint,
)
Constraint_strategy = st.builds(
    Constraint,
)
frameweb_VocabularyConstraints_strategy = st.builds(
    frameweb_VocabularyConstraints,
)
frameweb_DomainConstraints_strategy = st.builds(
    frameweb_DomainConstraints,
)
frameweb_NavigationConstraint_strategy = st.builds(
    frameweb_NavigationConstraint,
)
Stereotype_strategy = st.builds(
    Stereotype,
)
frameweb_Tag_strategy = st.builds(
    frameweb_Tag,
)
frameweb_Controller_strategy = st.builds(
    frameweb_Controller,
)
frameweb_ClassMapping_strategy = st.builds(
    frameweb_ClassMapping,
)
frameweb_AttributeMapping_strategy = st.builds(
    frameweb_AttributeMapping,
)
frameweb_ResultType_strategy = st.builds(
    frameweb_ResultType,
)
NavigationPackage_strategy = st.builds(
    NavigationPackage,
)
frameweb_ControllerPackage_strategy = st.builds(
    frameweb_ControllerPackage,
)
frameweb_ViewPackage_strategy = st.builds(
    frameweb_ViewPackage,
)
Package_strategy = st.builds(
    Package,
)
frameweb_ControllerSet_strategy = st.builds(
    frameweb_ControllerSet,
)
frameweb_ResultSet_strategy = st.builds(
    frameweb_ResultSet,
)
frameweb_PersistencePackage_strategy = st.builds(
    frameweb_PersistencePackage,
)
frameweb_NavigationPackage_strategy = st.builds(
    frameweb_NavigationPackage,
)
frameweb_Vocabulary_strategy = st.builds(
    frameweb_Vocabulary,
    vocabularyDocument=
        safe_text
)
frameweb_ApplicationPackage_strategy = st.builds(
    frameweb_ApplicationPackage,
)
frameweb_SemanticPackage_strategy = st.builds(
    frameweb_SemanticPackage,
)
frameweb_MappingLib_strategy = st.builds(
    frameweb_MappingLib,
)
frameweb_DomainPackage_strategy = st.builds(
    frameweb_DomainPackage,
)
Dependency_strategy = st.builds(
    Dependency,
)
frameweb_NavigationDependency_strategy = st.builds(
    frameweb_NavigationDependency,
)
frameweb_ChainingConstraint_strategy = st.builds(
    frameweb_ChainingConstraint,
)
frameweb_PageConstraint_strategy = st.builds(
    frameweb_PageConstraint,
)
frameweb_MethodCosntraint_strategy = st.builds(
    frameweb_MethodCosntraint,
)
frameweb_TagLib_strategy = st.builds(
    frameweb_TagLib,
    prefix=
        safe_text
)
ServiceAssociation_strategy = st.builds(
    ServiceAssociation,
)
frameweb_DAOServiceAssociation_strategy = st.builds(
    frameweb_DAOServiceAssociation,
)
frameweb_ServiceControllerAssociation_strategy = st.builds(
    frameweb_ServiceControllerAssociation,
)
Generalization__strategy = st.builds(
    Generalization_,
)
frameweb_DAOGeneralization_strategy = st.builds(
    frameweb_DAOGeneralization,
)
frameweb_NavigationGeneralization_strategy = st.builds(
    frameweb_NavigationGeneralization,
)
frameweb_DomainGeneralization_strategy = st.builds(
    frameweb_DomainGeneralization,
)
frameweb_ServiceGeneralization_strategy = st.builds(
    frameweb_ServiceGeneralization,
)
Operation_strategy = st.builds(
    Operation,
)
frameweb_ServiceMethod_strategy = st.builds(
    frameweb_ServiceMethod,
)
frameweb_DomainMethod_strategy = st.builds(
    frameweb_DomainMethod,
)
frameweb_DAOMethod_strategy = st.builds(
    frameweb_DAOMethod,
)
frameweb_ResultConstraint_strategy = st.builds(
    frameweb_ResultConstraint,
)
frameweb_FrontControllerMethod_strategy = st.builds(
    frameweb_FrontControllerMethod,
    isDefault=
        st.booleans()
)
NavigationDependency_strategy = st.builds(
    NavigationDependency,
)
frameweb_FrontControllerDependency_strategy = st.builds(
    frameweb_FrontControllerDependency,
)
frameweb_ChainingDependency_strategy = st.builds(
    frameweb_ChainingDependency,
)
frameweb_PageDependency_strategy = st.builds(
    frameweb_PageDependency,
)
frameweb_ResultDependency_strategy = st.builds(
    frameweb_ResultDependency,
    execute=
        safe_text,
    ajax=
        st.booleans(),
    render=
        safe_text
)
NavigationAttribute_strategy = st.builds(
    NavigationAttribute,
)
frameweb_UIComponentField_strategy = st.builds(
    frameweb_UIComponentField,
)
frameweb_IOParameter_strategy = st.builds(
    frameweb_IOParameter,
)
InterfaceRealization_strategy = st.builds(
    InterfaceRealization,
)
frameweb_SeviceRealization_strategy = st.builds(
    frameweb_SeviceRealization,
)
frameweb_DAORealization_strategy = st.builds(
    frameweb_DAORealization,
)
Class_strategy = st.builds(
    Class,
)
frameweb_Annotation_strategy = st.builds(
    frameweb_Annotation,
)
frameweb_DomainClass_strategy = st.builds(
    frameweb_DomainClass,
    table=
        safe_text
)
frameweb_NavigationClass_strategy = st.builds(
    frameweb_NavigationClass,
)
frameweb_Axiom_strategy = st.builds(
    frameweb_Axiom,
)
frameweb_ServiceClass_strategy = st.builds(
    frameweb_ServiceClass,
)
frameweb_FrontControllerClass_strategy = st.builds(
    frameweb_FrontControllerClass,
)
frameweb_VocabularyClassExpression_strategy = st.builds(
    frameweb_VocabularyClassExpression,
)
frameweb_Result_strategy = st.builds(
    frameweb_Result,
)
frameweb_DAOClass_strategy = st.builds(
    frameweb_DAOClass,
    sufix=
        safe_text,
    infix=
        safe_text,
    prefix=
        safe_text
)
Interface_strategy = st.builds(
    Interface,
)
frameweb_ServiceInterface_strategy = st.builds(
    frameweb_ServiceInterface,
)
frameweb_DAOInterface_strategy = st.builds(
    frameweb_DAOInterface,
    sufix=
        safe_text,
    infix=
        safe_text
)
NavigationClass_strategy = st.builds(
    NavigationClass,
)
frameweb_UIComponent_strategy = st.builds(
    frameweb_UIComponent,
)
frameweb_Template_strategy = st.builds(
    frameweb_Template,
)
frameweb_Page_strategy = st.builds(
    frameweb_Page,
)
DomainAttribute_strategy = st.builds(
    DomainAttribute,
)
frameweb_LOBAttribute_strategy = st.builds(
    frameweb_LOBAttribute,
)
frameweb_EmbeddedAttribute_strategy = st.builds(
    frameweb_EmbeddedAttribute,
)
frameweb_IdAttribute_strategy = st.builds(
    frameweb_IdAttribute,
    generation=
        safe_text
)
frameweb_DecimalAttribute_strategy = st.builds(
    frameweb_DecimalAttribute,
    decimalPrecision=
        safe_text,
    decimalScale=
        safe_text
)
frameweb_DateTimeAttribute_strategy = st.builds(
    frameweb_DateTimeAttribute,
    dateTimePrecision=
        safe_text
)
frameweb_VersionAttribute_strategy = st.builds(
    frameweb_VersionAttribute,
)
Property_strategy = st.builds(
    Property,
)
frameweb_DAOAttribute_strategy = st.builds(
    frameweb_DAOAttribute,
)
frameweb_ResultProperty_strategy = st.builds(
    frameweb_ResultProperty,
)
frameweb_AttributeMappingProperty_strategy = st.builds(
    frameweb_AttributeMappingProperty,
)
frameweb_DomainProperty_strategy = st.builds(
    frameweb_DomainProperty,
)
frameweb_NavigationProperty_strategy = st.builds(
    frameweb_NavigationProperty,
)
frameweb_ServiceAttribute_strategy = st.builds(
    frameweb_ServiceAttribute,
)
frameweb_IRI_strategy = st.builds(
    frameweb_IRI,
    iriVersion=
        safe_text,
    iri=
        safe_text
)
frameweb_VocabularyProperty_strategy = st.builds(
    frameweb_VocabularyProperty,
)
frameweb_NavigationAttribute_strategy = st.builds(
    frameweb_NavigationAttribute,
)
frameweb_ClassMappingPropery_strategy = st.builds(
    frameweb_ClassMappingPropery,
)
frameweb_ControllerProperty_strategy = st.builds(
    frameweb_ControllerProperty,
)
frameweb_Individual_strategy = st.builds(
    frameweb_Individual,
)
frameweb_TagProperty_strategy = st.builds(
    frameweb_TagProperty,
)
frameweb_DomainAttribute_strategy = st.builds(
    frameweb_DomainAttribute,
    isNull=
        st.booleans(),
    isPersistent=
        st.booleans(),
    size=
        safe_text
)
Association_strategy = st.builds(
    Association,
)
frameweb_VocabularyAssociation_strategy = st.builds(
    frameweb_VocabularyAssociation,
)
frameweb_ServiceAssociation_strategy = st.builds(
    frameweb_ServiceAssociation,
)
frameweb_NavigationAssociation_strategy = st.builds(
    frameweb_NavigationAssociation,
)
frameweb_DomainAssociation_strategy = st.builds(
    frameweb_DomainAssociation,
    order=
        safe_text,
    fetch=
        safe_text,
    collection=
        safe_text,
    cascade=
        safe_text
)
FramewebModel_strategy = st.builds(
    FramewebModel,
)
frameweb_PersistenceModel_strategy = st.builds(
    frameweb_PersistenceModel,
)
frameweb_ApplicationModel_strategy = st.builds(
    frameweb_ApplicationModel,
)
frameweb_VocabularyModel_strategy = st.builds(
    frameweb_VocabularyModel,
)
frameweb_NavigationModel_strategy = st.builds(
    frameweb_NavigationModel,
)
frameweb_EntityModel_strategy = st.builds(
    frameweb_EntityModel,
)
Profile_strategy = st.builds(
    Profile,
)
Model_strategy = st.builds(
    Model,
)
frameweb_FrameworkProfile_strategy = st.builds(
    frameweb_FrameworkProfile,
    category=
        safe_text,
    kind=
        safe_text
)
frameweb_FramewebModel_strategy = st.builds(
    frameweb_FramewebModel,
)
frameweb_FramewebProject_strategy = st.builds(
    frameweb_FramewebProject,
)

@given(instance=LiteralString_strategy)
@settings(max_examples=50)
def test_literalstring_instantiation(instance):
    assert isinstance(instance, LiteralString)

@given(instance=frameweb_VocabularyLiteral_strategy)
@settings(max_examples=50)
def test_frameweb_vocabularyliteral_instantiation(instance):
    assert isinstance(instance, frameweb_VocabularyLiteral)

@given(instance=VocabularyClassExpression_strategy)
@settings(max_examples=50)
def test_vocabularyclassexpression_instantiation(instance):
    assert isinstance(instance, VocabularyClassExpression)

@given(instance=Individual_strategy)
@settings(max_examples=50)
def test_individual_instantiation(instance):
    assert isinstance(instance, Individual)

@given(instance=frameweb_AnonymousIndividual_strategy)
@settings(max_examples=50)
def test_frameweb_anonymousindividual_instantiation(instance):
    assert isinstance(instance, frameweb_AnonymousIndividual)

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=VocabularyAssociation_strategy)
@settings(max_examples=50)
def test_vocabularyassociation_instantiation(instance):
    assert isinstance(instance, VocabularyAssociation)

@given(instance=VocabularyEntity_strategy)
@settings(max_examples=50)
def test_vocabularyentity_instantiation(instance):
    assert isinstance(instance, VocabularyEntity)

@given(instance=frameweb_DataProperty_strategy)
@settings(max_examples=50)
def test_frameweb_dataproperty_instantiation(instance):
    assert isinstance(instance, frameweb_DataProperty)

@given(instance=frameweb_VocabularyClass_strategy)
@settings(max_examples=50)
def test_frameweb_vocabularyclass_instantiation(instance):
    assert isinstance(instance, frameweb_VocabularyClass)

@given(instance=frameweb_NamedIndividual_strategy)
@settings(max_examples=50)
def test_frameweb_namedindividual_instantiation(instance):
    assert isinstance(instance, frameweb_NamedIndividual)

@given(instance=frameweb_AnnotationProperty_strategy)
@settings(max_examples=50)
def test_frameweb_annotationproperty_instantiation(instance):
    assert isinstance(instance, frameweb_AnnotationProperty)

@given(instance=frameweb_VocabularyDataType_strategy)
@settings(max_examples=50)
def test_frameweb_vocabularydatatype_instantiation(instance):
    assert isinstance(instance, frameweb_VocabularyDataType)

@given(instance=frameweb_ObjectProperty_strategy)
@settings(max_examples=50)
def test_frameweb_objectproperty_instantiation(instance):
    assert isinstance(instance, frameweb_ObjectProperty)

@given(instance=frameweb_NewInterface115_strategy)
@settings(max_examples=50)
def test_frameweb_newinterface115_instantiation(instance):
    assert isinstance(instance, frameweb_NewInterface115)

@given(instance=frameweb_Type_strategy)
@settings(max_examples=50)
def test_frameweb_type_instantiation(instance):
    assert isinstance(instance, frameweb_Type)

@given(instance=Relationship_strategy)
@settings(max_examples=50)
def test_relationship_instantiation(instance):
    assert isinstance(instance, Relationship)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=frameweb_VocabularyEntity_strategy)
@settings(max_examples=50)
def test_frameweb_vocabularyentity_instantiation(instance):
    assert isinstance(instance, frameweb_VocabularyEntity)

@given(instance=frameweb_Association_strategy)
@settings(max_examples=50)
def test_frameweb_association_instantiation(instance):
    assert isinstance(instance, frameweb_Association)



@given(instance=frameweb_Association_strategy)
def test_frameweb_association_isDerived_setter(instance):
    original = instance.isDerived
    instance.isDerived = original
    assert instance.isDerived == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=frameweb_Association_strategy)
@settings(max_examples=30)
def test_frameweb_association_ends_must_be_typed_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.ends_must_be_typed(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.ends_must_be_typed).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'ends_must_be_typed' in frameweb_Association is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'ends_must_be_typed' in frameweb_Association did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'ends_must_be_typed' in frameweb_Association is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=frameweb_Association_strategy)
@settings(max_examples=30)
def test_frameweb_association_specialized_end_types_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.specialized_end_types(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.specialized_end_types).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'specialized_end_types' in frameweb_Association is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'specialized_end_types' in frameweb_Association did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'specialized_end_types' in frameweb_Association is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=frameweb_Association_strategy)
@settings(max_examples=30)
def test_frameweb_association_binary_associations_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.binary_associations(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.binary_associations).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'binary_associations' in frameweb_Association is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'binary_associations' in frameweb_Association did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'binary_associations' in frameweb_Association is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=frameweb_Association_strategy)
@settings(max_examples=30)
def test_frameweb_association_isbinary_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isBinary()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isBinary).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isBinary' in frameweb_Association is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isBinary' in frameweb_Association did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isBinary' in frameweb_Association is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=frameweb_Association_strategy)
@settings(max_examples=30)
def test_frameweb_association_specialized_end_number_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.specialized_end_number(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.specialized_end_number).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'specialized_end_number' in frameweb_Association is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'specialized_end_number' in frameweb_Association did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'specialized_end_number' in frameweb_Association is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=frameweb_Association_strategy)
@settings(max_examples=30)
def test_frameweb_association_association_ends_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.association_ends(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.association_ends).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'association_ends' in frameweb_Association is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'association_ends' in frameweb_Association did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'association_ends' in frameweb_Association is not implemented or raised an error")

@given(instance=frameweb_ValueSpecification_strategy)
@settings(max_examples=50)
def test_frameweb_valuespecification_instantiation(instance):
    assert isinstance(instance, frameweb_ValueSpecification)

@given(instance=frameweb_Class_strategy)
@settings(max_examples=50)
def test_frameweb_class_instantiation(instance):
    assert isinstance(instance, frameweb_Class)

@given(instance=frameweb_Interface_strategy)
@settings(max_examples=50)
def test_frameweb_interface_instantiation(instance):
    assert isinstance(instance, frameweb_Interface)

@given(instance=frameweb_DataType_strategy)
@settings(max_examples=50)
def test_frameweb_datatype_instantiation(instance):
    assert isinstance(instance, frameweb_DataType)

@given(instance=DeploymentTarget_strategy)
@settings(max_examples=50)
def test_deploymenttarget_instantiation(instance):
    assert isinstance(instance, DeploymentTarget)

@given(instance=ConnectableElement_strategy)
@settings(max_examples=50)
def test_connectableelement_instantiation(instance):
    assert isinstance(instance, ConnectableElement)

@given(instance=StructuralFeature_strategy)
@settings(max_examples=50)
def test_structuralfeature_instantiation(instance):
    assert isinstance(instance, StructuralFeature)

@given(instance=frameweb_Property_strategy)
@settings(max_examples=50)
def test_frameweb_property_instantiation(instance):
    assert isinstance(instance, frameweb_Property)



@given(instance=frameweb_Property_strategy)
def test_frameweb_property_isDerivedUnion_setter(instance):
    original = instance.isDerivedUnion
    instance.isDerivedUnion = original
    assert instance.isDerivedUnion == original



@given(instance=frameweb_Property_strategy)
def test_frameweb_property_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original



@given(instance=frameweb_Property_strategy)
def test_frameweb_property_isID_setter(instance):
    original = instance.isID
    instance.isID = original
    assert instance.isID == original



@given(instance=frameweb_Property_strategy)
def test_frameweb_property_isDerived_setter(instance):
    original = instance.isDerived
    instance.isDerived = original
    assert instance.isDerived == original



@given(instance=frameweb_Property_strategy)
def test_frameweb_property_aggregation_setter(instance):
    original = instance.aggregation
    instance.aggregation = original
    assert instance.aggregation == original



@given(instance=frameweb_Property_strategy)
def test_frameweb_property_isComposite_setter(instance):
    original = instance.isComposite
    instance.isComposite = original
    assert instance.isComposite == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=frameweb_Property_strategy)
@settings(max_examples=30)
def test_frameweb_property_qualified_is_association_end_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.qualified_is_association_end(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.qualified_is_association_end).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'qualified_is_association_end' in frameweb_Property is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'qualified_is_association_end' in frameweb_Property did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'qualified_is_association_end' in frameweb_Property is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=frameweb_Property_strategy)
@settings(max_examples=30)
def test_frameweb_property_setintegerdefaultvalue_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setIntegerDefaultValue(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setIntegerDefaultValue).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setIntegerDefaultValue' in frameweb_Property is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setIntegerDefaultValue' in frameweb_Property did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setIntegerDefaultValue' in frameweb_Property is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=frameweb_Property_strategy)
@settings(max_examples=30)
def test_frameweb_property_setstringdefaultvalue_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setStringDefaultValue(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setStringDefaultValue).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setStringDefaultValue' in frameweb_Property is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setStringDefaultValue' in frameweb_Property did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setStringDefaultValue' in frameweb_Property is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=frameweb_Property_strategy)
@settings(max_examples=30)
def test_frameweb_property_iscomposite_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isComposite()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isComposite).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isComposite' in frameweb_Property is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isComposite' in frameweb_Property did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isComposite' in frameweb_Property is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=frameweb_Property_strategy)
@settings(max_examples=30)
def test_frameweb_property_redefined_property_inherited_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.redefined_property_inherited(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.redefined_property_inherited).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'redefined_property_inherited' in frameweb_Property is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'redefined_property_inherited' in frameweb_Property did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'redefined_property_inherited' in frameweb_Property is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=frameweb_Property_strategy)
@settings(max_examples=30)
def test_frameweb_property_isnavigable_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isNavigable()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isNavigable).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isNavigable' in frameweb_Property is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isNavigable' in frameweb_Property did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isNavigable' in frameweb_Property is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=frameweb_Property_strategy)
@settings(max_examples=30)
def test_frameweb_property_setiscomposite_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setIsComposite(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setIsComposite).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setIsComposite' in frameweb_Property is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setIsComposite' in frameweb_Property did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setIsComposite' in frameweb_Property is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=frameweb_Property_strategy)
@settings(max_examples=30)
def test_frameweb_property_setopposite_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setOpposite(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setOpposite).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setOpposite' in frameweb_Property is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setOpposite' in frameweb_Property did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setOpposite' in frameweb_Property is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=frameweb_Property_strategy)
@settings(max_examples=30)
def test_frameweb_property_unsetdefault_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.unsetDefault()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.unsetDefault).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'unsetDefault' in frameweb_Property is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'unsetDefault' in frameweb_Property did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'unsetDefault' in frameweb_Property is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=frameweb_Property_strategy)
@settings(max_examples=30)
def test_frameweb_property_type_of_opposite_end_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.type_of_opposite_end(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.type_of_opposite_end).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'type_of_opposite_end' in frameweb_Property is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'type_of_opposite_end' in frameweb_Property did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'type_of_opposite_end' in frameweb_Property is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=frameweb_Property_strategy)
@settings(max_examples=30)
def test_frameweb_property_setisnavigable_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setIsNavigable(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setIsNavigable).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setIsNavigable' in frameweb_Property is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setIsNavigable' in frameweb_Property did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setIsNavigable' in frameweb_Property is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=frameweb_Property_strategy)
@settings(max_examples=30)
def test_frameweb_property_setrealdefaultvalue_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setRealDefaultValue(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setRealDefaultValue).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setRealDefaultValue' in frameweb_Property is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setRealDefaultValue' in frameweb_Property did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setRealDefaultValue' in frameweb_Property is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=frameweb_Property_strategy)
@settings(max_examples=30)
def test_frameweb_property_binding_to_attribute_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.binding_to_attribute(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.binding_to_attribute).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'binding_to_attribute' in frameweb_Property is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'binding_to_attribute' in frameweb_Property did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'binding_to_attribute' in frameweb_Property is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=frameweb_Property_strategy)
@settings(max_examples=30)
def test_frameweb_property_derived_union_is_derived_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.derived_union_is_derived(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.derived_union_is_derived).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'derived_union_is_derived' in frameweb_Property is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'derived_union_is_derived' in frameweb_Property did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'derived_union_is_derived' in frameweb_Property is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=frameweb_Property_strategy)
@settings(max_examples=30)
def test_frameweb_property_subsettingcontext_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.subsettingContext()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.subsettingContext).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'subsettingContext' in frameweb_Property is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'subsettingContext' in frameweb_Property did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'subsettingContext' in frameweb_Property is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=frameweb_Property_strategy)
@settings(max_examples=30)
def test_frameweb_property_setdefault_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setDefault(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setDefault).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setDefault' in frameweb_Property is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setDefault' in frameweb_Property did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setDefault' in frameweb_Property is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=frameweb_Property_strategy)
@settings(max_examples=30)
def test_frameweb_property_setnulldefaultvalue_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setNullDefaultValue()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setNullDefaultValue).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setNullDefaultValue' in frameweb_Property is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setNullDefaultValue' in frameweb_Property did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setNullDefaultValue' in frameweb_Property is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=frameweb_Property_strategy)
@settings(max_examples=30)
def test_frameweb_property_setunlimitednaturaldefaultvalue_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setUnlimitedNaturalDefaultValue(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setUnlimitedNaturalDefaultValue).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setUnlimitedNaturalDefaultValue' in frameweb_Property is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setUnlimitedNaturalDefaultValue' in frameweb_Property did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setUnlimitedNaturalDefaultValue' in frameweb_Property is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=frameweb_Property_strategy)
@settings(max_examples=30)
def test_frameweb_property_derived_union_is_read_only_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.derived_union_is_read_only(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.derived_union_is_read_only).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'derived_union_is_read_only' in frameweb_Property is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'derived_union_is_read_only' in frameweb_Property did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'derived_union_is_read_only' in frameweb_Property is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=frameweb_Property_strategy)
@settings(max_examples=30)
def test_frameweb_property_subsetting_context_conforms_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.subsetting_context_conforms(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.subsetting_context_conforms).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'subsetting_context_conforms' in frameweb_Property is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'subsetting_context_conforms' in frameweb_Property did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'subsetting_context_conforms' in frameweb_Property is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=frameweb_Property_strategy)
@settings(max_examples=30)
def test_frameweb_property_multiplicity_of_composite_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.multiplicity_of_composite(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.multiplicity_of_composite).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'multiplicity_of_composite' in frameweb_Property is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'multiplicity_of_composite' in frameweb_Property did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'multiplicity_of_composite' in frameweb_Property is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=frameweb_Property_strategy)
@settings(max_examples=30)
def test_frameweb_property_setbooleandefaultvalue_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setBooleanDefaultValue(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setBooleanDefaultValue).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setBooleanDefaultValue' in frameweb_Property is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setBooleanDefaultValue' in frameweb_Property did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setBooleanDefaultValue' in frameweb_Property is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=frameweb_Property_strategy)
@settings(max_examples=30)
def test_frameweb_property_isattribute_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isAttribute()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isAttribute).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isAttribute' in frameweb_Property is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isAttribute' in frameweb_Property did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isAttribute' in frameweb_Property is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=frameweb_Property_strategy)
@settings(max_examples=30)
def test_frameweb_property_subsetting_rules_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.subsetting_rules(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.subsetting_rules).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'subsetting_rules' in frameweb_Property is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'subsetting_rules' in frameweb_Property did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'subsetting_rules' in frameweb_Property is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=frameweb_Property_strategy)
@settings(max_examples=30)
def test_frameweb_property_issetdefault_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isSetDefault()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isSetDefault).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isSetDefault' in frameweb_Property is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isSetDefault' in frameweb_Property did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isSetDefault' in frameweb_Property is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=frameweb_Property_strategy)
@settings(max_examples=30)
def test_frameweb_property_subsetted_property_names_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.subsetted_property_names(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.subsetted_property_names).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'subsetted_property_names' in frameweb_Property is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'subsetted_property_names' in frameweb_Property did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'subsetted_property_names' in frameweb_Property is not implemented or raised an error")

@given(instance=FrameworkExtension_strategy)
@settings(max_examples=50)
def test_frameworkextension_instantiation(instance):
    assert isinstance(instance, FrameworkExtension)

@given(instance=frameweb_DomainExtension_strategy)
@settings(max_examples=50)
def test_frameweb_domainextension_instantiation(instance):
    assert isinstance(instance, frameweb_DomainExtension)

@given(instance=frameweb_NavigationExtension_strategy)
@settings(max_examples=50)
def test_frameweb_navigationextension_instantiation(instance):
    assert isinstance(instance, frameweb_NavigationExtension)

@given(instance=NavigationProperty_strategy)
@settings(max_examples=50)
def test_navigationproperty_instantiation(instance):
    assert isinstance(instance, NavigationProperty)

@given(instance=frameweb_NavigationCompositionWhole_strategy)
@settings(max_examples=50)
def test_frameweb_navigationcompositionwhole_instantiation(instance):
    assert isinstance(instance, frameweb_NavigationCompositionWhole)

@given(instance=frameweb_NavigationCompositionPart_strategy)
@settings(max_examples=50)
def test_frameweb_navigationcompositionpart_instantiation(instance):
    assert isinstance(instance, frameweb_NavigationCompositionPart)

@given(instance=ExtensionEnd_strategy)
@settings(max_examples=50)
def test_extensionend_instantiation(instance):
    assert isinstance(instance, ExtensionEnd)

@given(instance=frameweb_AttributeMappingExtensionEnd_strategy)
@settings(max_examples=50)
def test_frameweb_attributemappingextensionend_instantiation(instance):
    assert isinstance(instance, frameweb_AttributeMappingExtensionEnd)

@given(instance=frameweb_TagExtensionEnd_strategy)
@settings(max_examples=50)
def test_frameweb_tagextensionend_instantiation(instance):
    assert isinstance(instance, frameweb_TagExtensionEnd)

@given(instance=frameweb_ClassMappingExtensionEnd_strategy)
@settings(max_examples=50)
def test_frameweb_classmappingextensionend_instantiation(instance):
    assert isinstance(instance, frameweb_ClassMappingExtensionEnd)

@given(instance=frameweb_ResultExtensionEnd_strategy)
@settings(max_examples=50)
def test_frameweb_resultextensionend_instantiation(instance):
    assert isinstance(instance, frameweb_ResultExtensionEnd)

@given(instance=frameweb_ControllerExtensionEnd_strategy)
@settings(max_examples=50)
def test_frameweb_controllerextensionend_instantiation(instance):
    assert isinstance(instance, frameweb_ControllerExtensionEnd)

@given(instance=DomainExtension_strategy)
@settings(max_examples=50)
def test_domainextension_instantiation(instance):
    assert isinstance(instance, DomainExtension)

@given(instance=frameweb_AttributeMappingExtension_strategy)
@settings(max_examples=50)
def test_frameweb_attributemappingextension_instantiation(instance):
    assert isinstance(instance, frameweb_AttributeMappingExtension)

@given(instance=frameweb_ClassMappingExtension_strategy)
@settings(max_examples=50)
def test_frameweb_classmappingextension_instantiation(instance):
    assert isinstance(instance, frameweb_ClassMappingExtension)

@given(instance=ProfileApplication_strategy)
@settings(max_examples=50)
def test_profileapplication_instantiation(instance):
    assert isinstance(instance, ProfileApplication)

@given(instance=frameweb_FrameworkApplication_strategy)
@settings(max_examples=50)
def test_frameweb_frameworkapplication_instantiation(instance):
    assert isinstance(instance, frameweb_FrameworkApplication)

@given(instance=NavigationExtension_strategy)
@settings(max_examples=50)
def test_navigationextension_instantiation(instance):
    assert isinstance(instance, NavigationExtension)

@given(instance=frameweb_ControllerExtension_strategy)
@settings(max_examples=50)
def test_frameweb_controllerextension_instantiation(instance):
    assert isinstance(instance, frameweb_ControllerExtension)

@given(instance=frameweb_ResultExtension_strategy)
@settings(max_examples=50)
def test_frameweb_resultextension_instantiation(instance):
    assert isinstance(instance, frameweb_ResultExtension)

@given(instance=frameweb_TagExtension_strategy)
@settings(max_examples=50)
def test_frameweb_tagextension_instantiation(instance):
    assert isinstance(instance, frameweb_TagExtension)

@given(instance=Extension_strategy)
@settings(max_examples=50)
def test_extension_instantiation(instance):
    assert isinstance(instance, Extension)

@given(instance=frameweb_FrameworkExtension_strategy)
@settings(max_examples=50)
def test_frameweb_frameworkextension_instantiation(instance):
    assert isinstance(instance, frameweb_FrameworkExtension)

@given(instance=GeneralizationSet_strategy)
@settings(max_examples=50)
def test_generalizationset_instantiation(instance):
    assert isinstance(instance, GeneralizationSet)

@given(instance=frameweb_NavigationGeneralizationSet_strategy)
@settings(max_examples=50)
def test_frameweb_navigationgeneralizationset_instantiation(instance):
    assert isinstance(instance, frameweb_NavigationGeneralizationSet)

@given(instance=frameweb_ServiceGeneralizationSet_strategy)
@settings(max_examples=50)
def test_frameweb_servicegeneralizationset_instantiation(instance):
    assert isinstance(instance, frameweb_ServiceGeneralizationSet)

@given(instance=frameweb_DAOGeneralizationSet_strategy)
@settings(max_examples=50)
def test_frameweb_daogeneralizationset_instantiation(instance):
    assert isinstance(instance, frameweb_DAOGeneralizationSet)

@given(instance=frameweb_DomainGeneralizationSet_strategy)
@settings(max_examples=50)
def test_frameweb_domaingeneralizationset_instantiation(instance):
    assert isinstance(instance, frameweb_DomainGeneralizationSet)



@given(instance=frameweb_DomainGeneralizationSet_strategy)
def test_frameweb_domaingeneralizationset_mapping_setter(instance):
    original = instance.mapping
    instance.mapping = original
    assert instance.mapping == original

@given(instance=NavigationConstraint_strategy)
@settings(max_examples=50)
def test_navigationconstraint_instantiation(instance):
    assert isinstance(instance, NavigationConstraint)

@given(instance=Constraint_strategy)
@settings(max_examples=50)
def test_constraint_instantiation(instance):
    assert isinstance(instance, Constraint)

@given(instance=frameweb_VocabularyConstraints_strategy)
@settings(max_examples=50)
def test_frameweb_vocabularyconstraints_instantiation(instance):
    assert isinstance(instance, frameweb_VocabularyConstraints)

@given(instance=frameweb_DomainConstraints_strategy)
@settings(max_examples=50)
def test_frameweb_domainconstraints_instantiation(instance):
    assert isinstance(instance, frameweb_DomainConstraints)

@given(instance=frameweb_NavigationConstraint_strategy)
@settings(max_examples=50)
def test_frameweb_navigationconstraint_instantiation(instance):
    assert isinstance(instance, frameweb_NavigationConstraint)

@given(instance=Stereotype_strategy)
@settings(max_examples=50)
def test_stereotype_instantiation(instance):
    assert isinstance(instance, Stereotype)

@given(instance=frameweb_Tag_strategy)
@settings(max_examples=50)
def test_frameweb_tag_instantiation(instance):
    assert isinstance(instance, frameweb_Tag)

@given(instance=frameweb_Controller_strategy)
@settings(max_examples=50)
def test_frameweb_controller_instantiation(instance):
    assert isinstance(instance, frameweb_Controller)

@given(instance=frameweb_ClassMapping_strategy)
@settings(max_examples=50)
def test_frameweb_classmapping_instantiation(instance):
    assert isinstance(instance, frameweb_ClassMapping)

@given(instance=frameweb_AttributeMapping_strategy)
@settings(max_examples=50)
def test_frameweb_attributemapping_instantiation(instance):
    assert isinstance(instance, frameweb_AttributeMapping)

@given(instance=frameweb_ResultType_strategy)
@settings(max_examples=50)
def test_frameweb_resulttype_instantiation(instance):
    assert isinstance(instance, frameweb_ResultType)

@given(instance=NavigationPackage_strategy)
@settings(max_examples=50)
def test_navigationpackage_instantiation(instance):
    assert isinstance(instance, NavigationPackage)

@given(instance=frameweb_ControllerPackage_strategy)
@settings(max_examples=50)
def test_frameweb_controllerpackage_instantiation(instance):
    assert isinstance(instance, frameweb_ControllerPackage)

@given(instance=frameweb_ViewPackage_strategy)
@settings(max_examples=50)
def test_frameweb_viewpackage_instantiation(instance):
    assert isinstance(instance, frameweb_ViewPackage)

@given(instance=Package_strategy)
@settings(max_examples=50)
def test_package_instantiation(instance):
    assert isinstance(instance, Package)

@given(instance=frameweb_ControllerSet_strategy)
@settings(max_examples=50)
def test_frameweb_controllerset_instantiation(instance):
    assert isinstance(instance, frameweb_ControllerSet)

@given(instance=frameweb_ResultSet_strategy)
@settings(max_examples=50)
def test_frameweb_resultset_instantiation(instance):
    assert isinstance(instance, frameweb_ResultSet)

@given(instance=frameweb_PersistencePackage_strategy)
@settings(max_examples=50)
def test_frameweb_persistencepackage_instantiation(instance):
    assert isinstance(instance, frameweb_PersistencePackage)

@given(instance=frameweb_NavigationPackage_strategy)
@settings(max_examples=50)
def test_frameweb_navigationpackage_instantiation(instance):
    assert isinstance(instance, frameweb_NavigationPackage)

@given(instance=frameweb_Vocabulary_strategy)
@settings(max_examples=50)
def test_frameweb_vocabulary_instantiation(instance):
    assert isinstance(instance, frameweb_Vocabulary)



@given(instance=frameweb_Vocabulary_strategy)
def test_frameweb_vocabulary_vocabularyDocument_setter(instance):
    original = instance.vocabularyDocument
    instance.vocabularyDocument = original
    assert instance.vocabularyDocument == original

@given(instance=frameweb_ApplicationPackage_strategy)
@settings(max_examples=50)
def test_frameweb_applicationpackage_instantiation(instance):
    assert isinstance(instance, frameweb_ApplicationPackage)

@given(instance=frameweb_SemanticPackage_strategy)
@settings(max_examples=50)
def test_frameweb_semanticpackage_instantiation(instance):
    assert isinstance(instance, frameweb_SemanticPackage)

@given(instance=frameweb_MappingLib_strategy)
@settings(max_examples=50)
def test_frameweb_mappinglib_instantiation(instance):
    assert isinstance(instance, frameweb_MappingLib)

@given(instance=frameweb_DomainPackage_strategy)
@settings(max_examples=50)
def test_frameweb_domainpackage_instantiation(instance):
    assert isinstance(instance, frameweb_DomainPackage)

@given(instance=Dependency_strategy)
@settings(max_examples=50)
def test_dependency_instantiation(instance):
    assert isinstance(instance, Dependency)

@given(instance=frameweb_NavigationDependency_strategy)
@settings(max_examples=50)
def test_frameweb_navigationdependency_instantiation(instance):
    assert isinstance(instance, frameweb_NavigationDependency)

@given(instance=frameweb_ChainingConstraint_strategy)
@settings(max_examples=50)
def test_frameweb_chainingconstraint_instantiation(instance):
    assert isinstance(instance, frameweb_ChainingConstraint)

@given(instance=frameweb_PageConstraint_strategy)
@settings(max_examples=50)
def test_frameweb_pageconstraint_instantiation(instance):
    assert isinstance(instance, frameweb_PageConstraint)

@given(instance=frameweb_MethodCosntraint_strategy)
@settings(max_examples=50)
def test_frameweb_methodcosntraint_instantiation(instance):
    assert isinstance(instance, frameweb_MethodCosntraint)

@given(instance=frameweb_TagLib_strategy)
@settings(max_examples=50)
def test_frameweb_taglib_instantiation(instance):
    assert isinstance(instance, frameweb_TagLib)



@given(instance=frameweb_TagLib_strategy)
def test_frameweb_taglib_prefix_setter(instance):
    original = instance.prefix
    instance.prefix = original
    assert instance.prefix == original

@given(instance=ServiceAssociation_strategy)
@settings(max_examples=50)
def test_serviceassociation_instantiation(instance):
    assert isinstance(instance, ServiceAssociation)

@given(instance=frameweb_DAOServiceAssociation_strategy)
@settings(max_examples=50)
def test_frameweb_daoserviceassociation_instantiation(instance):
    assert isinstance(instance, frameweb_DAOServiceAssociation)

@given(instance=frameweb_ServiceControllerAssociation_strategy)
@settings(max_examples=50)
def test_frameweb_servicecontrollerassociation_instantiation(instance):
    assert isinstance(instance, frameweb_ServiceControllerAssociation)

@given(instance=Generalization__strategy)
@settings(max_examples=50)
def test_generalization__instantiation(instance):
    assert isinstance(instance, Generalization_)

@given(instance=frameweb_DAOGeneralization_strategy)
@settings(max_examples=50)
def test_frameweb_daogeneralization_instantiation(instance):
    assert isinstance(instance, frameweb_DAOGeneralization)

@given(instance=frameweb_NavigationGeneralization_strategy)
@settings(max_examples=50)
def test_frameweb_navigationgeneralization_instantiation(instance):
    assert isinstance(instance, frameweb_NavigationGeneralization)

@given(instance=frameweb_DomainGeneralization_strategy)
@settings(max_examples=50)
def test_frameweb_domaingeneralization_instantiation(instance):
    assert isinstance(instance, frameweb_DomainGeneralization)

@given(instance=frameweb_ServiceGeneralization_strategy)
@settings(max_examples=50)
def test_frameweb_servicegeneralization_instantiation(instance):
    assert isinstance(instance, frameweb_ServiceGeneralization)

@given(instance=Operation_strategy)
@settings(max_examples=50)
def test_operation_instantiation(instance):
    assert isinstance(instance, Operation)

@given(instance=frameweb_ServiceMethod_strategy)
@settings(max_examples=50)
def test_frameweb_servicemethod_instantiation(instance):
    assert isinstance(instance, frameweb_ServiceMethod)

@given(instance=frameweb_DomainMethod_strategy)
@settings(max_examples=50)
def test_frameweb_domainmethod_instantiation(instance):
    assert isinstance(instance, frameweb_DomainMethod)

@given(instance=frameweb_DAOMethod_strategy)
@settings(max_examples=50)
def test_frameweb_daomethod_instantiation(instance):
    assert isinstance(instance, frameweb_DAOMethod)

@given(instance=frameweb_ResultConstraint_strategy)
@settings(max_examples=50)
def test_frameweb_resultconstraint_instantiation(instance):
    assert isinstance(instance, frameweb_ResultConstraint)

@given(instance=frameweb_FrontControllerMethod_strategy)
@settings(max_examples=50)
def test_frameweb_frontcontrollermethod_instantiation(instance):
    assert isinstance(instance, frameweb_FrontControllerMethod)



@given(instance=frameweb_FrontControllerMethod_strategy)
def test_frameweb_frontcontrollermethod_isDefault_setter(instance):
    original = instance.isDefault
    instance.isDefault = original
    assert instance.isDefault == original

@given(instance=NavigationDependency_strategy)
@settings(max_examples=50)
def test_navigationdependency_instantiation(instance):
    assert isinstance(instance, NavigationDependency)

@given(instance=frameweb_FrontControllerDependency_strategy)
@settings(max_examples=50)
def test_frameweb_frontcontrollerdependency_instantiation(instance):
    assert isinstance(instance, frameweb_FrontControllerDependency)

@given(instance=frameweb_ChainingDependency_strategy)
@settings(max_examples=50)
def test_frameweb_chainingdependency_instantiation(instance):
    assert isinstance(instance, frameweb_ChainingDependency)

@given(instance=frameweb_PageDependency_strategy)
@settings(max_examples=50)
def test_frameweb_pagedependency_instantiation(instance):
    assert isinstance(instance, frameweb_PageDependency)

@given(instance=frameweb_ResultDependency_strategy)
@settings(max_examples=50)
def test_frameweb_resultdependency_instantiation(instance):
    assert isinstance(instance, frameweb_ResultDependency)



@given(instance=frameweb_ResultDependency_strategy)
def test_frameweb_resultdependency_execute_setter(instance):
    original = instance.execute
    instance.execute = original
    assert instance.execute == original



@given(instance=frameweb_ResultDependency_strategy)
def test_frameweb_resultdependency_ajax_setter(instance):
    original = instance.ajax
    instance.ajax = original
    assert instance.ajax == original



@given(instance=frameweb_ResultDependency_strategy)
def test_frameweb_resultdependency_render_setter(instance):
    original = instance.render
    instance.render = original
    assert instance.render == original

@given(instance=NavigationAttribute_strategy)
@settings(max_examples=50)
def test_navigationattribute_instantiation(instance):
    assert isinstance(instance, NavigationAttribute)

@given(instance=frameweb_UIComponentField_strategy)
@settings(max_examples=50)
def test_frameweb_uicomponentfield_instantiation(instance):
    assert isinstance(instance, frameweb_UIComponentField)

@given(instance=frameweb_IOParameter_strategy)
@settings(max_examples=50)
def test_frameweb_ioparameter_instantiation(instance):
    assert isinstance(instance, frameweb_IOParameter)

@given(instance=InterfaceRealization_strategy)
@settings(max_examples=50)
def test_interfacerealization_instantiation(instance):
    assert isinstance(instance, InterfaceRealization)

@given(instance=frameweb_SeviceRealization_strategy)
@settings(max_examples=50)
def test_frameweb_sevicerealization_instantiation(instance):
    assert isinstance(instance, frameweb_SeviceRealization)

@given(instance=frameweb_DAORealization_strategy)
@settings(max_examples=50)
def test_frameweb_daorealization_instantiation(instance):
    assert isinstance(instance, frameweb_DAORealization)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=frameweb_Annotation_strategy)
@settings(max_examples=50)
def test_frameweb_annotation_instantiation(instance):
    assert isinstance(instance, frameweb_Annotation)

@given(instance=frameweb_DomainClass_strategy)
@settings(max_examples=50)
def test_frameweb_domainclass_instantiation(instance):
    assert isinstance(instance, frameweb_DomainClass)



@given(instance=frameweb_DomainClass_strategy)
def test_frameweb_domainclass_table_setter(instance):
    original = instance.table
    instance.table = original
    assert instance.table == original

@given(instance=frameweb_NavigationClass_strategy)
@settings(max_examples=50)
def test_frameweb_navigationclass_instantiation(instance):
    assert isinstance(instance, frameweb_NavigationClass)

@given(instance=frameweb_Axiom_strategy)
@settings(max_examples=50)
def test_frameweb_axiom_instantiation(instance):
    assert isinstance(instance, frameweb_Axiom)

@given(instance=frameweb_ServiceClass_strategy)
@settings(max_examples=50)
def test_frameweb_serviceclass_instantiation(instance):
    assert isinstance(instance, frameweb_ServiceClass)

@given(instance=frameweb_FrontControllerClass_strategy)
@settings(max_examples=50)
def test_frameweb_frontcontrollerclass_instantiation(instance):
    assert isinstance(instance, frameweb_FrontControllerClass)

@given(instance=frameweb_VocabularyClassExpression_strategy)
@settings(max_examples=50)
def test_frameweb_vocabularyclassexpression_instantiation(instance):
    assert isinstance(instance, frameweb_VocabularyClassExpression)

@given(instance=frameweb_Result_strategy)
@settings(max_examples=50)
def test_frameweb_result_instantiation(instance):
    assert isinstance(instance, frameweb_Result)

@given(instance=frameweb_DAOClass_strategy)
@settings(max_examples=50)
def test_frameweb_daoclass_instantiation(instance):
    assert isinstance(instance, frameweb_DAOClass)



@given(instance=frameweb_DAOClass_strategy)
def test_frameweb_daoclass_sufix_setter(instance):
    original = instance.sufix
    instance.sufix = original
    assert instance.sufix == original



@given(instance=frameweb_DAOClass_strategy)
def test_frameweb_daoclass_infix_setter(instance):
    original = instance.infix
    instance.infix = original
    assert instance.infix == original



@given(instance=frameweb_DAOClass_strategy)
def test_frameweb_daoclass_prefix_setter(instance):
    original = instance.prefix
    instance.prefix = original
    assert instance.prefix == original

@given(instance=Interface_strategy)
@settings(max_examples=50)
def test_interface_instantiation(instance):
    assert isinstance(instance, Interface)

@given(instance=frameweb_ServiceInterface_strategy)
@settings(max_examples=50)
def test_frameweb_serviceinterface_instantiation(instance):
    assert isinstance(instance, frameweb_ServiceInterface)

@given(instance=frameweb_DAOInterface_strategy)
@settings(max_examples=50)
def test_frameweb_daointerface_instantiation(instance):
    assert isinstance(instance, frameweb_DAOInterface)



@given(instance=frameweb_DAOInterface_strategy)
def test_frameweb_daointerface_sufix_setter(instance):
    original = instance.sufix
    instance.sufix = original
    assert instance.sufix == original



@given(instance=frameweb_DAOInterface_strategy)
def test_frameweb_daointerface_infix_setter(instance):
    original = instance.infix
    instance.infix = original
    assert instance.infix == original

@given(instance=NavigationClass_strategy)
@settings(max_examples=50)
def test_navigationclass_instantiation(instance):
    assert isinstance(instance, NavigationClass)

@given(instance=frameweb_UIComponent_strategy)
@settings(max_examples=50)
def test_frameweb_uicomponent_instantiation(instance):
    assert isinstance(instance, frameweb_UIComponent)

@given(instance=frameweb_Template_strategy)
@settings(max_examples=50)
def test_frameweb_template_instantiation(instance):
    assert isinstance(instance, frameweb_Template)

@given(instance=frameweb_Page_strategy)
@settings(max_examples=50)
def test_frameweb_page_instantiation(instance):
    assert isinstance(instance, frameweb_Page)

@given(instance=DomainAttribute_strategy)
@settings(max_examples=50)
def test_domainattribute_instantiation(instance):
    assert isinstance(instance, DomainAttribute)

@given(instance=frameweb_LOBAttribute_strategy)
@settings(max_examples=50)
def test_frameweb_lobattribute_instantiation(instance):
    assert isinstance(instance, frameweb_LOBAttribute)

@given(instance=frameweb_EmbeddedAttribute_strategy)
@settings(max_examples=50)
def test_frameweb_embeddedattribute_instantiation(instance):
    assert isinstance(instance, frameweb_EmbeddedAttribute)

@given(instance=frameweb_IdAttribute_strategy)
@settings(max_examples=50)
def test_frameweb_idattribute_instantiation(instance):
    assert isinstance(instance, frameweb_IdAttribute)



@given(instance=frameweb_IdAttribute_strategy)
def test_frameweb_idattribute_generation_setter(instance):
    original = instance.generation
    instance.generation = original
    assert instance.generation == original

@given(instance=frameweb_DecimalAttribute_strategy)
@settings(max_examples=50)
def test_frameweb_decimalattribute_instantiation(instance):
    assert isinstance(instance, frameweb_DecimalAttribute)



@given(instance=frameweb_DecimalAttribute_strategy)
def test_frameweb_decimalattribute_decimalPrecision_setter(instance):
    original = instance.decimalPrecision
    instance.decimalPrecision = original
    assert instance.decimalPrecision == original



@given(instance=frameweb_DecimalAttribute_strategy)
def test_frameweb_decimalattribute_decimalScale_setter(instance):
    original = instance.decimalScale
    instance.decimalScale = original
    assert instance.decimalScale == original

@given(instance=frameweb_DateTimeAttribute_strategy)
@settings(max_examples=50)
def test_frameweb_datetimeattribute_instantiation(instance):
    assert isinstance(instance, frameweb_DateTimeAttribute)



@given(instance=frameweb_DateTimeAttribute_strategy)
def test_frameweb_datetimeattribute_dateTimePrecision_setter(instance):
    original = instance.dateTimePrecision
    instance.dateTimePrecision = original
    assert instance.dateTimePrecision == original

@given(instance=frameweb_VersionAttribute_strategy)
@settings(max_examples=50)
def test_frameweb_versionattribute_instantiation(instance):
    assert isinstance(instance, frameweb_VersionAttribute)

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=frameweb_DAOAttribute_strategy)
@settings(max_examples=50)
def test_frameweb_daoattribute_instantiation(instance):
    assert isinstance(instance, frameweb_DAOAttribute)

@given(instance=frameweb_ResultProperty_strategy)
@settings(max_examples=50)
def test_frameweb_resultproperty_instantiation(instance):
    assert isinstance(instance, frameweb_ResultProperty)

@given(instance=frameweb_AttributeMappingProperty_strategy)
@settings(max_examples=50)
def test_frameweb_attributemappingproperty_instantiation(instance):
    assert isinstance(instance, frameweb_AttributeMappingProperty)

@given(instance=frameweb_DomainProperty_strategy)
@settings(max_examples=50)
def test_frameweb_domainproperty_instantiation(instance):
    assert isinstance(instance, frameweb_DomainProperty)

@given(instance=frameweb_NavigationProperty_strategy)
@settings(max_examples=50)
def test_frameweb_navigationproperty_instantiation(instance):
    assert isinstance(instance, frameweb_NavigationProperty)

@given(instance=frameweb_ServiceAttribute_strategy)
@settings(max_examples=50)
def test_frameweb_serviceattribute_instantiation(instance):
    assert isinstance(instance, frameweb_ServiceAttribute)

@given(instance=frameweb_IRI_strategy)
@settings(max_examples=50)
def test_frameweb_iri_instantiation(instance):
    assert isinstance(instance, frameweb_IRI)



@given(instance=frameweb_IRI_strategy)
def test_frameweb_iri_iriVersion_setter(instance):
    original = instance.iriVersion
    instance.iriVersion = original
    assert instance.iriVersion == original



@given(instance=frameweb_IRI_strategy)
def test_frameweb_iri_iri_setter(instance):
    original = instance.iri
    instance.iri = original
    assert instance.iri == original

@given(instance=frameweb_VocabularyProperty_strategy)
@settings(max_examples=50)
def test_frameweb_vocabularyproperty_instantiation(instance):
    assert isinstance(instance, frameweb_VocabularyProperty)

@given(instance=frameweb_NavigationAttribute_strategy)
@settings(max_examples=50)
def test_frameweb_navigationattribute_instantiation(instance):
    assert isinstance(instance, frameweb_NavigationAttribute)

@given(instance=frameweb_ClassMappingPropery_strategy)
@settings(max_examples=50)
def test_frameweb_classmappingpropery_instantiation(instance):
    assert isinstance(instance, frameweb_ClassMappingPropery)

@given(instance=frameweb_ControllerProperty_strategy)
@settings(max_examples=50)
def test_frameweb_controllerproperty_instantiation(instance):
    assert isinstance(instance, frameweb_ControllerProperty)

@given(instance=frameweb_Individual_strategy)
@settings(max_examples=50)
def test_frameweb_individual_instantiation(instance):
    assert isinstance(instance, frameweb_Individual)

@given(instance=frameweb_TagProperty_strategy)
@settings(max_examples=50)
def test_frameweb_tagproperty_instantiation(instance):
    assert isinstance(instance, frameweb_TagProperty)

@given(instance=frameweb_DomainAttribute_strategy)
@settings(max_examples=50)
def test_frameweb_domainattribute_instantiation(instance):
    assert isinstance(instance, frameweb_DomainAttribute)



@given(instance=frameweb_DomainAttribute_strategy)
def test_frameweb_domainattribute_isNull_setter(instance):
    original = instance.isNull
    instance.isNull = original
    assert instance.isNull == original



@given(instance=frameweb_DomainAttribute_strategy)
def test_frameweb_domainattribute_isPersistent_setter(instance):
    original = instance.isPersistent
    instance.isPersistent = original
    assert instance.isPersistent == original



@given(instance=frameweb_DomainAttribute_strategy)
def test_frameweb_domainattribute_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=Association_strategy)
@settings(max_examples=50)
def test_association_instantiation(instance):
    assert isinstance(instance, Association)

@given(instance=frameweb_VocabularyAssociation_strategy)
@settings(max_examples=50)
def test_frameweb_vocabularyassociation_instantiation(instance):
    assert isinstance(instance, frameweb_VocabularyAssociation)

@given(instance=frameweb_ServiceAssociation_strategy)
@settings(max_examples=50)
def test_frameweb_serviceassociation_instantiation(instance):
    assert isinstance(instance, frameweb_ServiceAssociation)

@given(instance=frameweb_NavigationAssociation_strategy)
@settings(max_examples=50)
def test_frameweb_navigationassociation_instantiation(instance):
    assert isinstance(instance, frameweb_NavigationAssociation)

@given(instance=frameweb_DomainAssociation_strategy)
@settings(max_examples=50)
def test_frameweb_domainassociation_instantiation(instance):
    assert isinstance(instance, frameweb_DomainAssociation)



@given(instance=frameweb_DomainAssociation_strategy)
def test_frameweb_domainassociation_order_setter(instance):
    original = instance.order
    instance.order = original
    assert instance.order == original



@given(instance=frameweb_DomainAssociation_strategy)
def test_frameweb_domainassociation_fetch_setter(instance):
    original = instance.fetch
    instance.fetch = original
    assert instance.fetch == original



@given(instance=frameweb_DomainAssociation_strategy)
def test_frameweb_domainassociation_collection_setter(instance):
    original = instance.collection
    instance.collection = original
    assert instance.collection == original



@given(instance=frameweb_DomainAssociation_strategy)
def test_frameweb_domainassociation_cascade_setter(instance):
    original = instance.cascade
    instance.cascade = original
    assert instance.cascade == original

@given(instance=FramewebModel_strategy)
@settings(max_examples=50)
def test_framewebmodel_instantiation(instance):
    assert isinstance(instance, FramewebModel)

@given(instance=frameweb_PersistenceModel_strategy)
@settings(max_examples=50)
def test_frameweb_persistencemodel_instantiation(instance):
    assert isinstance(instance, frameweb_PersistenceModel)

@given(instance=frameweb_ApplicationModel_strategy)
@settings(max_examples=50)
def test_frameweb_applicationmodel_instantiation(instance):
    assert isinstance(instance, frameweb_ApplicationModel)

@given(instance=frameweb_VocabularyModel_strategy)
@settings(max_examples=50)
def test_frameweb_vocabularymodel_instantiation(instance):
    assert isinstance(instance, frameweb_VocabularyModel)

@given(instance=frameweb_NavigationModel_strategy)
@settings(max_examples=50)
def test_frameweb_navigationmodel_instantiation(instance):
    assert isinstance(instance, frameweb_NavigationModel)

@given(instance=frameweb_EntityModel_strategy)
@settings(max_examples=50)
def test_frameweb_entitymodel_instantiation(instance):
    assert isinstance(instance, frameweb_EntityModel)

@given(instance=Profile_strategy)
@settings(max_examples=50)
def test_profile_instantiation(instance):
    assert isinstance(instance, Profile)

@given(instance=Model_strategy)
@settings(max_examples=50)
def test_model_instantiation(instance):
    assert isinstance(instance, Model)

@given(instance=frameweb_FrameworkProfile_strategy)
@settings(max_examples=50)
def test_frameweb_frameworkprofile_instantiation(instance):
    assert isinstance(instance, frameweb_FrameworkProfile)



@given(instance=frameweb_FrameworkProfile_strategy)
def test_frameweb_frameworkprofile_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original



@given(instance=frameweb_FrameworkProfile_strategy)
def test_frameweb_frameworkprofile_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=frameweb_FramewebModel_strategy)
@settings(max_examples=50)
def test_frameweb_framewebmodel_instantiation(instance):
    assert isinstance(instance, frameweb_FramewebModel)

@given(instance=frameweb_FramewebProject_strategy)
@settings(max_examples=50)
def test_frameweb_framewebproject_instantiation(instance):
    assert isinstance(instance, frameweb_FramewebProject)
