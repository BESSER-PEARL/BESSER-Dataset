import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    sparqlas_TemplateBinding,
    sparqlas_TemplateableElement,
    sparqlas_TemplateParameterSubstitution,
    sparqlas_TemplateSignature,
    sparqlas_TemplateParameter,
    sparqlas_ParameterableElement,
    Declaration,
    sparqlas_ObjectPropertyDeclaration,
    sparqlas_DatatypePropertyDeclaration,
    sparqlas_ClassDeclaration,
    sparqlas_IndividualDeclaration,
    DataPropertyAtom,
    sparqlas_DisjointDataProperties,
    sparqlas_DataPropertyDomain,
    sparqlas_EquivalentDataProperties,
    sparqlas_DataPropertyRange,
    sparqlas_FunctionalDataProperty,
    sparqlas_SubDataPropertyOf,
    sparqlas_ObjectPropertyChain,
    ObjectPropertyAtom,
    sparqlas_FunctionalObjectProperty,
    sparqlas_AsymmetricObjectProperty,
    sparqlas_IrreflexiveObjectProperty,
    sparqlas_EquivalentObjectProperties,
    sparqlas_TransitiveObjectProperty,
    sparqlas_ObjectPropertyRange,
    sparqlas_SymmetricObjectProperty,
    sparqlas_ReflexiveObjectProperty,
    sparqlas_InverseFunctionalObjectProperty,
    sparqlas_InverseObjectPropertyAtom,
    sparqlas_ObjectPropertyDomain,
    sparqlas_DisjointObjectProperties,
    sparqlas_FacetRestriction,
    sparqlas_SubObjectPropertyOf,
    sparqlas_DataRange,
    Expression,
    ClassAtom,
    sparqlas_EquivalentClasses,
    sparqlas_DirectSubClassOf,
    sparqlas_StrictSubClassOf,
    sparqlas_DisjointUnion,
    sparqlas_SubClassOf,
    sparqlas_DisjointClasses,
    sparqlas_DataPropertyExpression,
    sparqlas_ClassExpression,
    Assertion,
    sparqlas_DirectClassAssertion,
    sparqlas_NegativeObjectPropertyAssertion,
    sparqlas_NegativeDataPropertyAssertion,
    sparqlas_DataPropertyAssertion,
    sparqlas_DifferentIndividuals,
    sparqlas_SameIndividual,
    sparqlas_ClassAssertion,
    Atom,
    sparqlas_ClassAtom,
    sparqlas_Declaration,
    sparqlas_HasKey,
    sparqlas_ObjectPropertyAtom,
    sparqlas_DataPropertyAtom,
    sparqlas_Assertion,
    ParameterableElement,
    sparqlas_Expression,
    AbstractLiteral,
    sparqlas_Literal,
    sparqlas_AbstractLiteral,
    sparqlas_Individual,
    DataRange,
    sparqlas_DataIntersectionOf,
    sparqlas_DataComplementOf,
    sparqlas_DatatypeRestriction,
    sparqlas_DataOneOf,
    sparqlas_DataUnionOf,
    Constant,
    sparqlas_Datatype,
    sparqlas_ObjectPropertyExpression,
    sparqlas_ObjectPropertyAssertion,
    DataPropertyExpression,
    sparqlas_DataProperty,
    ObjectPropertyExpression,
    sparqlas_ObjectProperty,
    sparqlas_InverseObjectProperty,
    ClassExpression,
    sparqlas_ObjectComplementOf,
    sparqlas_DataAllValuesFrom,
    sparqlas_ObjectHasValue,
    sparqlas_DataHasValue,
    sparqlas_ObjectIntersectionOf,
    sparqlas_DataSomeValuesFrom,
    sparqlas_ObjectExactCardinality,
    sparqlas_ObjectSomeValuesFrom,
    sparqlas_DataExactCardinality,
    sparqlas_DataMinCardinality,
    sparqlas_ObjectMaxCardinality,
    sparqlas_ObjectMinCardinality,
    sparqlas_ObjectOneOf,
    sparqlas_ObjectUnionOf,
    sparqlas_ObjectAllValuesFrom,
    sparqlas_DataMaxCardinality,
    Variable,
    sparqlas_LiteralVariable,
    sparqlas_ObjectPropertyVariable,
    sparqlas_DataPropertyVariable,
    sparqlas_ClassVariable,
    Term,
    sparqlas_Term,
    IRI,
    sparqlas_AbbreviatedIRI,
    sparqlas_Class,
    sparqlas_Constant,
    Individual,
    sparqlas_AnonymousIndividual,
    sparqlas_NamedIndividual,
    sparqlas_IndividualVariable,
    sparqlas_Variable,
    sparqlas_Atom,
    TemplateableElement,
    Query,
    sparqlas_ConstructQuery,
    sparqlas_SelectQuery,
    sparqlas_FullIRI,
    sparqlas_DescribeQuery,
    sparqlas_AskQuery,
    sparqlas_Import,
    sparqlas_IRI,
    sparqlas_OntologyDocument,
    sparqlas_Query,
    sparqlas_PrefixDefinition,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sparqlas_templatebinding_is_not_abstract():
    assert not inspect.isabstract(sparqlas_TemplateBinding)


def test_sparqlas_templatebinding_constructor_exists():
    assert callable(sparqlas_TemplateBinding.__init__)


def test_sparqlas_templatebinding_constructor_args():
    sig = inspect.signature(sparqlas_TemplateBinding.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_templateableelement_is_not_abstract():
    assert not inspect.isabstract(sparqlas_TemplateableElement)


def test_sparqlas_templateableelement_constructor_exists():
    assert callable(sparqlas_TemplateableElement.__init__)


def test_sparqlas_templateableelement_constructor_args():
    sig = inspect.signature(sparqlas_TemplateableElement.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_templateparametersubstitution_is_not_abstract():
    assert not inspect.isabstract(sparqlas_TemplateParameterSubstitution)


def test_sparqlas_templateparametersubstitution_constructor_exists():
    assert callable(sparqlas_TemplateParameterSubstitution.__init__)


def test_sparqlas_templateparametersubstitution_constructor_args():
    sig = inspect.signature(sparqlas_TemplateParameterSubstitution.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_templatesignature_is_not_abstract():
    assert not inspect.isabstract(sparqlas_TemplateSignature)


def test_sparqlas_templatesignature_constructor_exists():
    assert callable(sparqlas_TemplateSignature.__init__)


def test_sparqlas_templatesignature_constructor_args():
    sig = inspect.signature(sparqlas_TemplateSignature.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_templateparameter_is_not_abstract():
    assert not inspect.isabstract(sparqlas_TemplateParameter)


def test_sparqlas_templateparameter_constructor_exists():
    assert callable(sparqlas_TemplateParameter.__init__)


def test_sparqlas_templateparameter_constructor_args():
    sig = inspect.signature(sparqlas_TemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_parameterableelement_is_not_abstract():
    assert not inspect.isabstract(sparqlas_ParameterableElement)


def test_sparqlas_parameterableelement_constructor_exists():
    assert callable(sparqlas_ParameterableElement.__init__)


def test_sparqlas_parameterableelement_constructor_args():
    sig = inspect.signature(sparqlas_ParameterableElement.__init__)
    params = list(sig.parameters.keys())



def test_declaration_is_not_abstract():
    assert not inspect.isabstract(Declaration)


def test_declaration_constructor_exists():
    assert callable(Declaration.__init__)


def test_declaration_constructor_args():
    sig = inspect.signature(Declaration.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_objectpropertydeclaration_is_not_abstract():
    assert not inspect.isabstract(sparqlas_ObjectPropertyDeclaration)


def test_sparqlas_objectpropertydeclaration_constructor_exists():
    assert callable(sparqlas_ObjectPropertyDeclaration.__init__)


def test_sparqlas_objectpropertydeclaration_constructor_args():
    sig = inspect.signature(sparqlas_ObjectPropertyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_datatypepropertydeclaration_is_not_abstract():
    assert not inspect.isabstract(sparqlas_DatatypePropertyDeclaration)


def test_sparqlas_datatypepropertydeclaration_constructor_exists():
    assert callable(sparqlas_DatatypePropertyDeclaration.__init__)


def test_sparqlas_datatypepropertydeclaration_constructor_args():
    sig = inspect.signature(sparqlas_DatatypePropertyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_classdeclaration_is_not_abstract():
    assert not inspect.isabstract(sparqlas_ClassDeclaration)


def test_sparqlas_classdeclaration_constructor_exists():
    assert callable(sparqlas_ClassDeclaration.__init__)


def test_sparqlas_classdeclaration_constructor_args():
    sig = inspect.signature(sparqlas_ClassDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_individualdeclaration_is_not_abstract():
    assert not inspect.isabstract(sparqlas_IndividualDeclaration)


def test_sparqlas_individualdeclaration_constructor_exists():
    assert callable(sparqlas_IndividualDeclaration.__init__)


def test_sparqlas_individualdeclaration_constructor_args():
    sig = inspect.signature(sparqlas_IndividualDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_datapropertyatom_is_not_abstract():
    assert not inspect.isabstract(DataPropertyAtom)


def test_datapropertyatom_constructor_exists():
    assert callable(DataPropertyAtom.__init__)


def test_datapropertyatom_constructor_args():
    sig = inspect.signature(DataPropertyAtom.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_disjointdataproperties_is_not_abstract():
    assert not inspect.isabstract(sparqlas_DisjointDataProperties)


def test_sparqlas_disjointdataproperties_constructor_exists():
    assert callable(sparqlas_DisjointDataProperties.__init__)


def test_sparqlas_disjointdataproperties_constructor_args():
    sig = inspect.signature(sparqlas_DisjointDataProperties.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_datapropertydomain_is_not_abstract():
    assert not inspect.isabstract(sparqlas_DataPropertyDomain)


def test_sparqlas_datapropertydomain_constructor_exists():
    assert callable(sparqlas_DataPropertyDomain.__init__)


def test_sparqlas_datapropertydomain_constructor_args():
    sig = inspect.signature(sparqlas_DataPropertyDomain.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_equivalentdataproperties_is_not_abstract():
    assert not inspect.isabstract(sparqlas_EquivalentDataProperties)


def test_sparqlas_equivalentdataproperties_constructor_exists():
    assert callable(sparqlas_EquivalentDataProperties.__init__)


def test_sparqlas_equivalentdataproperties_constructor_args():
    sig = inspect.signature(sparqlas_EquivalentDataProperties.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_datapropertyrange_is_not_abstract():
    assert not inspect.isabstract(sparqlas_DataPropertyRange)


def test_sparqlas_datapropertyrange_constructor_exists():
    assert callable(sparqlas_DataPropertyRange.__init__)


def test_sparqlas_datapropertyrange_constructor_args():
    sig = inspect.signature(sparqlas_DataPropertyRange.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_functionaldataproperty_is_not_abstract():
    assert not inspect.isabstract(sparqlas_FunctionalDataProperty)


def test_sparqlas_functionaldataproperty_constructor_exists():
    assert callable(sparqlas_FunctionalDataProperty.__init__)


def test_sparqlas_functionaldataproperty_constructor_args():
    sig = inspect.signature(sparqlas_FunctionalDataProperty.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_subdatapropertyof_is_not_abstract():
    assert not inspect.isabstract(sparqlas_SubDataPropertyOf)


def test_sparqlas_subdatapropertyof_constructor_exists():
    assert callable(sparqlas_SubDataPropertyOf.__init__)


def test_sparqlas_subdatapropertyof_constructor_args():
    sig = inspect.signature(sparqlas_SubDataPropertyOf.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_objectpropertychain_is_not_abstract():
    assert not inspect.isabstract(sparqlas_ObjectPropertyChain)


def test_sparqlas_objectpropertychain_constructor_exists():
    assert callable(sparqlas_ObjectPropertyChain.__init__)


def test_sparqlas_objectpropertychain_constructor_args():
    sig = inspect.signature(sparqlas_ObjectPropertyChain.__init__)
    params = list(sig.parameters.keys())



def test_objectpropertyatom_is_not_abstract():
    assert not inspect.isabstract(ObjectPropertyAtom)


def test_objectpropertyatom_constructor_exists():
    assert callable(ObjectPropertyAtom.__init__)


def test_objectpropertyatom_constructor_args():
    sig = inspect.signature(ObjectPropertyAtom.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_functionalobjectproperty_is_not_abstract():
    assert not inspect.isabstract(sparqlas_FunctionalObjectProperty)


def test_sparqlas_functionalobjectproperty_constructor_exists():
    assert callable(sparqlas_FunctionalObjectProperty.__init__)


def test_sparqlas_functionalobjectproperty_constructor_args():
    sig = inspect.signature(sparqlas_FunctionalObjectProperty.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_asymmetricobjectproperty_is_not_abstract():
    assert not inspect.isabstract(sparqlas_AsymmetricObjectProperty)


def test_sparqlas_asymmetricobjectproperty_constructor_exists():
    assert callable(sparqlas_AsymmetricObjectProperty.__init__)


def test_sparqlas_asymmetricobjectproperty_constructor_args():
    sig = inspect.signature(sparqlas_AsymmetricObjectProperty.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_irreflexiveobjectproperty_is_not_abstract():
    assert not inspect.isabstract(sparqlas_IrreflexiveObjectProperty)


def test_sparqlas_irreflexiveobjectproperty_constructor_exists():
    assert callable(sparqlas_IrreflexiveObjectProperty.__init__)


def test_sparqlas_irreflexiveobjectproperty_constructor_args():
    sig = inspect.signature(sparqlas_IrreflexiveObjectProperty.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_equivalentobjectproperties_is_not_abstract():
    assert not inspect.isabstract(sparqlas_EquivalentObjectProperties)


def test_sparqlas_equivalentobjectproperties_constructor_exists():
    assert callable(sparqlas_EquivalentObjectProperties.__init__)


def test_sparqlas_equivalentobjectproperties_constructor_args():
    sig = inspect.signature(sparqlas_EquivalentObjectProperties.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_transitiveobjectproperty_is_not_abstract():
    assert not inspect.isabstract(sparqlas_TransitiveObjectProperty)


def test_sparqlas_transitiveobjectproperty_constructor_exists():
    assert callable(sparqlas_TransitiveObjectProperty.__init__)


def test_sparqlas_transitiveobjectproperty_constructor_args():
    sig = inspect.signature(sparqlas_TransitiveObjectProperty.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_objectpropertyrange_is_not_abstract():
    assert not inspect.isabstract(sparqlas_ObjectPropertyRange)


def test_sparqlas_objectpropertyrange_constructor_exists():
    assert callable(sparqlas_ObjectPropertyRange.__init__)


def test_sparqlas_objectpropertyrange_constructor_args():
    sig = inspect.signature(sparqlas_ObjectPropertyRange.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_symmetricobjectproperty_is_not_abstract():
    assert not inspect.isabstract(sparqlas_SymmetricObjectProperty)


def test_sparqlas_symmetricobjectproperty_constructor_exists():
    assert callable(sparqlas_SymmetricObjectProperty.__init__)


def test_sparqlas_symmetricobjectproperty_constructor_args():
    sig = inspect.signature(sparqlas_SymmetricObjectProperty.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_reflexiveobjectproperty_is_not_abstract():
    assert not inspect.isabstract(sparqlas_ReflexiveObjectProperty)


def test_sparqlas_reflexiveobjectproperty_constructor_exists():
    assert callable(sparqlas_ReflexiveObjectProperty.__init__)


def test_sparqlas_reflexiveobjectproperty_constructor_args():
    sig = inspect.signature(sparqlas_ReflexiveObjectProperty.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_inversefunctionalobjectproperty_is_not_abstract():
    assert not inspect.isabstract(sparqlas_InverseFunctionalObjectProperty)


def test_sparqlas_inversefunctionalobjectproperty_constructor_exists():
    assert callable(sparqlas_InverseFunctionalObjectProperty.__init__)


def test_sparqlas_inversefunctionalobjectproperty_constructor_args():
    sig = inspect.signature(sparqlas_InverseFunctionalObjectProperty.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_inverseobjectpropertyatom_is_not_abstract():
    assert not inspect.isabstract(sparqlas_InverseObjectPropertyAtom)


def test_sparqlas_inverseobjectpropertyatom_constructor_exists():
    assert callable(sparqlas_InverseObjectPropertyAtom.__init__)


def test_sparqlas_inverseobjectpropertyatom_constructor_args():
    sig = inspect.signature(sparqlas_InverseObjectPropertyAtom.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_objectpropertydomain_is_not_abstract():
    assert not inspect.isabstract(sparqlas_ObjectPropertyDomain)


def test_sparqlas_objectpropertydomain_constructor_exists():
    assert callable(sparqlas_ObjectPropertyDomain.__init__)


def test_sparqlas_objectpropertydomain_constructor_args():
    sig = inspect.signature(sparqlas_ObjectPropertyDomain.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_disjointobjectproperties_is_not_abstract():
    assert not inspect.isabstract(sparqlas_DisjointObjectProperties)


def test_sparqlas_disjointobjectproperties_constructor_exists():
    assert callable(sparqlas_DisjointObjectProperties.__init__)


def test_sparqlas_disjointobjectproperties_constructor_args():
    sig = inspect.signature(sparqlas_DisjointObjectProperties.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_facetrestriction_is_not_abstract():
    assert not inspect.isabstract(sparqlas_FacetRestriction)


def test_sparqlas_facetrestriction_constructor_exists():
    assert callable(sparqlas_FacetRestriction.__init__)


def test_sparqlas_facetrestriction_constructor_args():
    sig = inspect.signature(sparqlas_FacetRestriction.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_subobjectpropertyof_is_not_abstract():
    assert not inspect.isabstract(sparqlas_SubObjectPropertyOf)


def test_sparqlas_subobjectpropertyof_constructor_exists():
    assert callable(sparqlas_SubObjectPropertyOf.__init__)


def test_sparqlas_subobjectpropertyof_constructor_args():
    sig = inspect.signature(sparqlas_SubObjectPropertyOf.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_datarange_is_not_abstract():
    assert not inspect.isabstract(sparqlas_DataRange)


def test_sparqlas_datarange_constructor_exists():
    assert callable(sparqlas_DataRange.__init__)


def test_sparqlas_datarange_constructor_args():
    sig = inspect.signature(sparqlas_DataRange.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_classatom_is_not_abstract():
    assert not inspect.isabstract(ClassAtom)


def test_classatom_constructor_exists():
    assert callable(ClassAtom.__init__)


def test_classatom_constructor_args():
    sig = inspect.signature(ClassAtom.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_equivalentclasses_is_not_abstract():
    assert not inspect.isabstract(sparqlas_EquivalentClasses)


def test_sparqlas_equivalentclasses_constructor_exists():
    assert callable(sparqlas_EquivalentClasses.__init__)


def test_sparqlas_equivalentclasses_constructor_args():
    sig = inspect.signature(sparqlas_EquivalentClasses.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_directsubclassof_is_not_abstract():
    assert not inspect.isabstract(sparqlas_DirectSubClassOf)


def test_sparqlas_directsubclassof_constructor_exists():
    assert callable(sparqlas_DirectSubClassOf.__init__)


def test_sparqlas_directsubclassof_constructor_args():
    sig = inspect.signature(sparqlas_DirectSubClassOf.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_strictsubclassof_is_not_abstract():
    assert not inspect.isabstract(sparqlas_StrictSubClassOf)


def test_sparqlas_strictsubclassof_constructor_exists():
    assert callable(sparqlas_StrictSubClassOf.__init__)


def test_sparqlas_strictsubclassof_constructor_args():
    sig = inspect.signature(sparqlas_StrictSubClassOf.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_disjointunion_is_not_abstract():
    assert not inspect.isabstract(sparqlas_DisjointUnion)


def test_sparqlas_disjointunion_constructor_exists():
    assert callable(sparqlas_DisjointUnion.__init__)


def test_sparqlas_disjointunion_constructor_args():
    sig = inspect.signature(sparqlas_DisjointUnion.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_subclassof_is_not_abstract():
    assert not inspect.isabstract(sparqlas_SubClassOf)


def test_sparqlas_subclassof_constructor_exists():
    assert callable(sparqlas_SubClassOf.__init__)


def test_sparqlas_subclassof_constructor_args():
    sig = inspect.signature(sparqlas_SubClassOf.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_disjointclasses_is_not_abstract():
    assert not inspect.isabstract(sparqlas_DisjointClasses)


def test_sparqlas_disjointclasses_constructor_exists():
    assert callable(sparqlas_DisjointClasses.__init__)


def test_sparqlas_disjointclasses_constructor_args():
    sig = inspect.signature(sparqlas_DisjointClasses.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_datapropertyexpression_is_not_abstract():
    assert not inspect.isabstract(sparqlas_DataPropertyExpression)


def test_sparqlas_datapropertyexpression_constructor_exists():
    assert callable(sparqlas_DataPropertyExpression.__init__)


def test_sparqlas_datapropertyexpression_constructor_args():
    sig = inspect.signature(sparqlas_DataPropertyExpression.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_classexpression_is_not_abstract():
    assert not inspect.isabstract(sparqlas_ClassExpression)


def test_sparqlas_classexpression_constructor_exists():
    assert callable(sparqlas_ClassExpression.__init__)


def test_sparqlas_classexpression_constructor_args():
    sig = inspect.signature(sparqlas_ClassExpression.__init__)
    params = list(sig.parameters.keys())



def test_assertion_is_not_abstract():
    assert not inspect.isabstract(Assertion)


def test_assertion_constructor_exists():
    assert callable(Assertion.__init__)


def test_assertion_constructor_args():
    sig = inspect.signature(Assertion.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_directclassassertion_is_not_abstract():
    assert not inspect.isabstract(sparqlas_DirectClassAssertion)


def test_sparqlas_directclassassertion_constructor_exists():
    assert callable(sparqlas_DirectClassAssertion.__init__)


def test_sparqlas_directclassassertion_constructor_args():
    sig = inspect.signature(sparqlas_DirectClassAssertion.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_negativeobjectpropertyassertion_is_not_abstract():
    assert not inspect.isabstract(sparqlas_NegativeObjectPropertyAssertion)


def test_sparqlas_negativeobjectpropertyassertion_constructor_exists():
    assert callable(sparqlas_NegativeObjectPropertyAssertion.__init__)


def test_sparqlas_negativeobjectpropertyassertion_constructor_args():
    sig = inspect.signature(sparqlas_NegativeObjectPropertyAssertion.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_negativedatapropertyassertion_is_not_abstract():
    assert not inspect.isabstract(sparqlas_NegativeDataPropertyAssertion)


def test_sparqlas_negativedatapropertyassertion_constructor_exists():
    assert callable(sparqlas_NegativeDataPropertyAssertion.__init__)


def test_sparqlas_negativedatapropertyassertion_constructor_args():
    sig = inspect.signature(sparqlas_NegativeDataPropertyAssertion.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_datapropertyassertion_is_not_abstract():
    assert not inspect.isabstract(sparqlas_DataPropertyAssertion)


def test_sparqlas_datapropertyassertion_constructor_exists():
    assert callable(sparqlas_DataPropertyAssertion.__init__)


def test_sparqlas_datapropertyassertion_constructor_args():
    sig = inspect.signature(sparqlas_DataPropertyAssertion.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_differentindividuals_is_not_abstract():
    assert not inspect.isabstract(sparqlas_DifferentIndividuals)


def test_sparqlas_differentindividuals_constructor_exists():
    assert callable(sparqlas_DifferentIndividuals.__init__)


def test_sparqlas_differentindividuals_constructor_args():
    sig = inspect.signature(sparqlas_DifferentIndividuals.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_sameindividual_is_not_abstract():
    assert not inspect.isabstract(sparqlas_SameIndividual)


def test_sparqlas_sameindividual_constructor_exists():
    assert callable(sparqlas_SameIndividual.__init__)


def test_sparqlas_sameindividual_constructor_args():
    sig = inspect.signature(sparqlas_SameIndividual.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_classassertion_is_not_abstract():
    assert not inspect.isabstract(sparqlas_ClassAssertion)


def test_sparqlas_classassertion_constructor_exists():
    assert callable(sparqlas_ClassAssertion.__init__)


def test_sparqlas_classassertion_constructor_args():
    sig = inspect.signature(sparqlas_ClassAssertion.__init__)
    params = list(sig.parameters.keys())



def test_atom_is_not_abstract():
    assert not inspect.isabstract(Atom)


def test_atom_constructor_exists():
    assert callable(Atom.__init__)


def test_atom_constructor_args():
    sig = inspect.signature(Atom.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_classatom_is_not_abstract():
    assert not inspect.isabstract(sparqlas_ClassAtom)


def test_sparqlas_classatom_constructor_exists():
    assert callable(sparqlas_ClassAtom.__init__)


def test_sparqlas_classatom_constructor_args():
    sig = inspect.signature(sparqlas_ClassAtom.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_declaration_is_not_abstract():
    assert not inspect.isabstract(sparqlas_Declaration)


def test_sparqlas_declaration_constructor_exists():
    assert callable(sparqlas_Declaration.__init__)


def test_sparqlas_declaration_constructor_args():
    sig = inspect.signature(sparqlas_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_haskey_is_not_abstract():
    assert not inspect.isabstract(sparqlas_HasKey)


def test_sparqlas_haskey_constructor_exists():
    assert callable(sparqlas_HasKey.__init__)


def test_sparqlas_haskey_constructor_args():
    sig = inspect.signature(sparqlas_HasKey.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_objectpropertyatom_is_not_abstract():
    assert not inspect.isabstract(sparqlas_ObjectPropertyAtom)


def test_sparqlas_objectpropertyatom_constructor_exists():
    assert callable(sparqlas_ObjectPropertyAtom.__init__)


def test_sparqlas_objectpropertyatom_constructor_args():
    sig = inspect.signature(sparqlas_ObjectPropertyAtom.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_datapropertyatom_is_not_abstract():
    assert not inspect.isabstract(sparqlas_DataPropertyAtom)


def test_sparqlas_datapropertyatom_constructor_exists():
    assert callable(sparqlas_DataPropertyAtom.__init__)


def test_sparqlas_datapropertyatom_constructor_args():
    sig = inspect.signature(sparqlas_DataPropertyAtom.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_assertion_is_not_abstract():
    assert not inspect.isabstract(sparqlas_Assertion)


def test_sparqlas_assertion_constructor_exists():
    assert callable(sparqlas_Assertion.__init__)


def test_sparqlas_assertion_constructor_args():
    sig = inspect.signature(sparqlas_Assertion.__init__)
    params = list(sig.parameters.keys())



def test_parameterableelement_is_not_abstract():
    assert not inspect.isabstract(ParameterableElement)


def test_parameterableelement_constructor_exists():
    assert callable(ParameterableElement.__init__)


def test_parameterableelement_constructor_args():
    sig = inspect.signature(ParameterableElement.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_expression_is_not_abstract():
    assert not inspect.isabstract(sparqlas_Expression)


def test_sparqlas_expression_constructor_exists():
    assert callable(sparqlas_Expression.__init__)


def test_sparqlas_expression_constructor_args():
    sig = inspect.signature(sparqlas_Expression.__init__)
    params = list(sig.parameters.keys())



def test_abstractliteral_is_not_abstract():
    assert not inspect.isabstract(AbstractLiteral)


def test_abstractliteral_constructor_exists():
    assert callable(AbstractLiteral.__init__)


def test_abstractliteral_constructor_args():
    sig = inspect.signature(AbstractLiteral.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_literal_is_not_abstract():
    assert not inspect.isabstract(sparqlas_Literal)


def test_sparqlas_literal_constructor_exists():
    assert callable(sparqlas_Literal.__init__)


def test_sparqlas_literal_constructor_args():
    sig = inspect.signature(sparqlas_Literal.__init__)
    params = list(sig.parameters.keys())
    assert "lexicalForm" in params, "Missing parameter 'lexicalForm'"

def test_sparqlas_literal_has_lexicalForm():
    assert hasattr(sparqlas_Literal, "lexicalForm")
    descriptor = None
    for klass in sparqlas_Literal.__mro__:
        if "lexicalForm" in klass.__dict__:
            descriptor = klass.__dict__["lexicalForm"]
            break
    assert isinstance(descriptor, property)



def test_sparqlas_abstractliteral_is_not_abstract():
    assert not inspect.isabstract(sparqlas_AbstractLiteral)


def test_sparqlas_abstractliteral_constructor_exists():
    assert callable(sparqlas_AbstractLiteral.__init__)


def test_sparqlas_abstractliteral_constructor_args():
    sig = inspect.signature(sparqlas_AbstractLiteral.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_individual_is_not_abstract():
    assert not inspect.isabstract(sparqlas_Individual)


def test_sparqlas_individual_constructor_exists():
    assert callable(sparqlas_Individual.__init__)


def test_sparqlas_individual_constructor_args():
    sig = inspect.signature(sparqlas_Individual.__init__)
    params = list(sig.parameters.keys())



def test_datarange_is_not_abstract():
    assert not inspect.isabstract(DataRange)


def test_datarange_constructor_exists():
    assert callable(DataRange.__init__)


def test_datarange_constructor_args():
    sig = inspect.signature(DataRange.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_dataintersectionof_is_not_abstract():
    assert not inspect.isabstract(sparqlas_DataIntersectionOf)


def test_sparqlas_dataintersectionof_constructor_exists():
    assert callable(sparqlas_DataIntersectionOf.__init__)


def test_sparqlas_dataintersectionof_constructor_args():
    sig = inspect.signature(sparqlas_DataIntersectionOf.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_datacomplementof_is_not_abstract():
    assert not inspect.isabstract(sparqlas_DataComplementOf)


def test_sparqlas_datacomplementof_constructor_exists():
    assert callable(sparqlas_DataComplementOf.__init__)


def test_sparqlas_datacomplementof_constructor_args():
    sig = inspect.signature(sparqlas_DataComplementOf.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_datatyperestriction_is_not_abstract():
    assert not inspect.isabstract(sparqlas_DatatypeRestriction)


def test_sparqlas_datatyperestriction_constructor_exists():
    assert callable(sparqlas_DatatypeRestriction.__init__)


def test_sparqlas_datatyperestriction_constructor_args():
    sig = inspect.signature(sparqlas_DatatypeRestriction.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_dataoneof_is_not_abstract():
    assert not inspect.isabstract(sparqlas_DataOneOf)


def test_sparqlas_dataoneof_constructor_exists():
    assert callable(sparqlas_DataOneOf.__init__)


def test_sparqlas_dataoneof_constructor_args():
    sig = inspect.signature(sparqlas_DataOneOf.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_dataunionof_is_not_abstract():
    assert not inspect.isabstract(sparqlas_DataUnionOf)


def test_sparqlas_dataunionof_constructor_exists():
    assert callable(sparqlas_DataUnionOf.__init__)


def test_sparqlas_dataunionof_constructor_args():
    sig = inspect.signature(sparqlas_DataUnionOf.__init__)
    params = list(sig.parameters.keys())



def test_constant_is_not_abstract():
    assert not inspect.isabstract(Constant)


def test_constant_constructor_exists():
    assert callable(Constant.__init__)


def test_constant_constructor_args():
    sig = inspect.signature(Constant.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_datatype_is_not_abstract():
    assert not inspect.isabstract(sparqlas_Datatype)


def test_sparqlas_datatype_constructor_exists():
    assert callable(sparqlas_Datatype.__init__)


def test_sparqlas_datatype_constructor_args():
    sig = inspect.signature(sparqlas_Datatype.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_objectpropertyexpression_is_not_abstract():
    assert not inspect.isabstract(sparqlas_ObjectPropertyExpression)


def test_sparqlas_objectpropertyexpression_constructor_exists():
    assert callable(sparqlas_ObjectPropertyExpression.__init__)


def test_sparqlas_objectpropertyexpression_constructor_args():
    sig = inspect.signature(sparqlas_ObjectPropertyExpression.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_objectpropertyassertion_is_not_abstract():
    assert not inspect.isabstract(sparqlas_ObjectPropertyAssertion)


def test_sparqlas_objectpropertyassertion_constructor_exists():
    assert callable(sparqlas_ObjectPropertyAssertion.__init__)


def test_sparqlas_objectpropertyassertion_constructor_args():
    sig = inspect.signature(sparqlas_ObjectPropertyAssertion.__init__)
    params = list(sig.parameters.keys())



def test_datapropertyexpression_is_not_abstract():
    assert not inspect.isabstract(DataPropertyExpression)


def test_datapropertyexpression_constructor_exists():
    assert callable(DataPropertyExpression.__init__)


def test_datapropertyexpression_constructor_args():
    sig = inspect.signature(DataPropertyExpression.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_dataproperty_is_not_abstract():
    assert not inspect.isabstract(sparqlas_DataProperty)


def test_sparqlas_dataproperty_constructor_exists():
    assert callable(sparqlas_DataProperty.__init__)


def test_sparqlas_dataproperty_constructor_args():
    sig = inspect.signature(sparqlas_DataProperty.__init__)
    params = list(sig.parameters.keys())



def test_objectpropertyexpression_is_not_abstract():
    assert not inspect.isabstract(ObjectPropertyExpression)


def test_objectpropertyexpression_constructor_exists():
    assert callable(ObjectPropertyExpression.__init__)


def test_objectpropertyexpression_constructor_args():
    sig = inspect.signature(ObjectPropertyExpression.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_objectproperty_is_not_abstract():
    assert not inspect.isabstract(sparqlas_ObjectProperty)


def test_sparqlas_objectproperty_constructor_exists():
    assert callable(sparqlas_ObjectProperty.__init__)


def test_sparqlas_objectproperty_constructor_args():
    sig = inspect.signature(sparqlas_ObjectProperty.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_inverseobjectproperty_is_not_abstract():
    assert not inspect.isabstract(sparqlas_InverseObjectProperty)


def test_sparqlas_inverseobjectproperty_constructor_exists():
    assert callable(sparqlas_InverseObjectProperty.__init__)


def test_sparqlas_inverseobjectproperty_constructor_args():
    sig = inspect.signature(sparqlas_InverseObjectProperty.__init__)
    params = list(sig.parameters.keys())



def test_classexpression_is_not_abstract():
    assert not inspect.isabstract(ClassExpression)


def test_classexpression_constructor_exists():
    assert callable(ClassExpression.__init__)


def test_classexpression_constructor_args():
    sig = inspect.signature(ClassExpression.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_objectcomplementof_is_not_abstract():
    assert not inspect.isabstract(sparqlas_ObjectComplementOf)


def test_sparqlas_objectcomplementof_constructor_exists():
    assert callable(sparqlas_ObjectComplementOf.__init__)


def test_sparqlas_objectcomplementof_constructor_args():
    sig = inspect.signature(sparqlas_ObjectComplementOf.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_dataallvaluesfrom_is_not_abstract():
    assert not inspect.isabstract(sparqlas_DataAllValuesFrom)


def test_sparqlas_dataallvaluesfrom_constructor_exists():
    assert callable(sparqlas_DataAllValuesFrom.__init__)


def test_sparqlas_dataallvaluesfrom_constructor_args():
    sig = inspect.signature(sparqlas_DataAllValuesFrom.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_objecthasvalue_is_not_abstract():
    assert not inspect.isabstract(sparqlas_ObjectHasValue)


def test_sparqlas_objecthasvalue_constructor_exists():
    assert callable(sparqlas_ObjectHasValue.__init__)


def test_sparqlas_objecthasvalue_constructor_args():
    sig = inspect.signature(sparqlas_ObjectHasValue.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_datahasvalue_is_not_abstract():
    assert not inspect.isabstract(sparqlas_DataHasValue)


def test_sparqlas_datahasvalue_constructor_exists():
    assert callable(sparqlas_DataHasValue.__init__)


def test_sparqlas_datahasvalue_constructor_args():
    sig = inspect.signature(sparqlas_DataHasValue.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_objectintersectionof_is_not_abstract():
    assert not inspect.isabstract(sparqlas_ObjectIntersectionOf)


def test_sparqlas_objectintersectionof_constructor_exists():
    assert callable(sparqlas_ObjectIntersectionOf.__init__)


def test_sparqlas_objectintersectionof_constructor_args():
    sig = inspect.signature(sparqlas_ObjectIntersectionOf.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_datasomevaluesfrom_is_not_abstract():
    assert not inspect.isabstract(sparqlas_DataSomeValuesFrom)


def test_sparqlas_datasomevaluesfrom_constructor_exists():
    assert callable(sparqlas_DataSomeValuesFrom.__init__)


def test_sparqlas_datasomevaluesfrom_constructor_args():
    sig = inspect.signature(sparqlas_DataSomeValuesFrom.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_objectexactcardinality_is_not_abstract():
    assert not inspect.isabstract(sparqlas_ObjectExactCardinality)


def test_sparqlas_objectexactcardinality_constructor_exists():
    assert callable(sparqlas_ObjectExactCardinality.__init__)


def test_sparqlas_objectexactcardinality_constructor_args():
    sig = inspect.signature(sparqlas_ObjectExactCardinality.__init__)
    params = list(sig.parameters.keys())
    assert "cardinality" in params, "Missing parameter 'cardinality'"

def test_sparqlas_objectexactcardinality_has_cardinality():
    assert hasattr(sparqlas_ObjectExactCardinality, "cardinality")
    descriptor = None
    for klass in sparqlas_ObjectExactCardinality.__mro__:
        if "cardinality" in klass.__dict__:
            descriptor = klass.__dict__["cardinality"]
            break
    assert isinstance(descriptor, property)



def test_sparqlas_objectsomevaluesfrom_is_not_abstract():
    assert not inspect.isabstract(sparqlas_ObjectSomeValuesFrom)


def test_sparqlas_objectsomevaluesfrom_constructor_exists():
    assert callable(sparqlas_ObjectSomeValuesFrom.__init__)


def test_sparqlas_objectsomevaluesfrom_constructor_args():
    sig = inspect.signature(sparqlas_ObjectSomeValuesFrom.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_dataexactcardinality_is_not_abstract():
    assert not inspect.isabstract(sparqlas_DataExactCardinality)


def test_sparqlas_dataexactcardinality_constructor_exists():
    assert callable(sparqlas_DataExactCardinality.__init__)


def test_sparqlas_dataexactcardinality_constructor_args():
    sig = inspect.signature(sparqlas_DataExactCardinality.__init__)
    params = list(sig.parameters.keys())
    assert "cardinality" in params, "Missing parameter 'cardinality'"

def test_sparqlas_dataexactcardinality_has_cardinality():
    assert hasattr(sparqlas_DataExactCardinality, "cardinality")
    descriptor = None
    for klass in sparqlas_DataExactCardinality.__mro__:
        if "cardinality" in klass.__dict__:
            descriptor = klass.__dict__["cardinality"]
            break
    assert isinstance(descriptor, property)



def test_sparqlas_datamincardinality_is_not_abstract():
    assert not inspect.isabstract(sparqlas_DataMinCardinality)


def test_sparqlas_datamincardinality_constructor_exists():
    assert callable(sparqlas_DataMinCardinality.__init__)


def test_sparqlas_datamincardinality_constructor_args():
    sig = inspect.signature(sparqlas_DataMinCardinality.__init__)
    params = list(sig.parameters.keys())
    assert "cardinality" in params, "Missing parameter 'cardinality'"

def test_sparqlas_datamincardinality_has_cardinality():
    assert hasattr(sparqlas_DataMinCardinality, "cardinality")
    descriptor = None
    for klass in sparqlas_DataMinCardinality.__mro__:
        if "cardinality" in klass.__dict__:
            descriptor = klass.__dict__["cardinality"]
            break
    assert isinstance(descriptor, property)



def test_sparqlas_objectmaxcardinality_is_not_abstract():
    assert not inspect.isabstract(sparqlas_ObjectMaxCardinality)


def test_sparqlas_objectmaxcardinality_constructor_exists():
    assert callable(sparqlas_ObjectMaxCardinality.__init__)


def test_sparqlas_objectmaxcardinality_constructor_args():
    sig = inspect.signature(sparqlas_ObjectMaxCardinality.__init__)
    params = list(sig.parameters.keys())
    assert "cardinality" in params, "Missing parameter 'cardinality'"

def test_sparqlas_objectmaxcardinality_has_cardinality():
    assert hasattr(sparqlas_ObjectMaxCardinality, "cardinality")
    descriptor = None
    for klass in sparqlas_ObjectMaxCardinality.__mro__:
        if "cardinality" in klass.__dict__:
            descriptor = klass.__dict__["cardinality"]
            break
    assert isinstance(descriptor, property)



def test_sparqlas_objectmincardinality_is_not_abstract():
    assert not inspect.isabstract(sparqlas_ObjectMinCardinality)


def test_sparqlas_objectmincardinality_constructor_exists():
    assert callable(sparqlas_ObjectMinCardinality.__init__)


def test_sparqlas_objectmincardinality_constructor_args():
    sig = inspect.signature(sparqlas_ObjectMinCardinality.__init__)
    params = list(sig.parameters.keys())
    assert "cardinality" in params, "Missing parameter 'cardinality'"

def test_sparqlas_objectmincardinality_has_cardinality():
    assert hasattr(sparqlas_ObjectMinCardinality, "cardinality")
    descriptor = None
    for klass in sparqlas_ObjectMinCardinality.__mro__:
        if "cardinality" in klass.__dict__:
            descriptor = klass.__dict__["cardinality"]
            break
    assert isinstance(descriptor, property)



def test_sparqlas_objectoneof_is_not_abstract():
    assert not inspect.isabstract(sparqlas_ObjectOneOf)


def test_sparqlas_objectoneof_constructor_exists():
    assert callable(sparqlas_ObjectOneOf.__init__)


def test_sparqlas_objectoneof_constructor_args():
    sig = inspect.signature(sparqlas_ObjectOneOf.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_objectunionof_is_not_abstract():
    assert not inspect.isabstract(sparqlas_ObjectUnionOf)


def test_sparqlas_objectunionof_constructor_exists():
    assert callable(sparqlas_ObjectUnionOf.__init__)


def test_sparqlas_objectunionof_constructor_args():
    sig = inspect.signature(sparqlas_ObjectUnionOf.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_objectallvaluesfrom_is_not_abstract():
    assert not inspect.isabstract(sparqlas_ObjectAllValuesFrom)


def test_sparqlas_objectallvaluesfrom_constructor_exists():
    assert callable(sparqlas_ObjectAllValuesFrom.__init__)


def test_sparqlas_objectallvaluesfrom_constructor_args():
    sig = inspect.signature(sparqlas_ObjectAllValuesFrom.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_datamaxcardinality_is_not_abstract():
    assert not inspect.isabstract(sparqlas_DataMaxCardinality)


def test_sparqlas_datamaxcardinality_constructor_exists():
    assert callable(sparqlas_DataMaxCardinality.__init__)


def test_sparqlas_datamaxcardinality_constructor_args():
    sig = inspect.signature(sparqlas_DataMaxCardinality.__init__)
    params = list(sig.parameters.keys())
    assert "cardinality" in params, "Missing parameter 'cardinality'"

def test_sparqlas_datamaxcardinality_has_cardinality():
    assert hasattr(sparqlas_DataMaxCardinality, "cardinality")
    descriptor = None
    for klass in sparqlas_DataMaxCardinality.__mro__:
        if "cardinality" in klass.__dict__:
            descriptor = klass.__dict__["cardinality"]
            break
    assert isinstance(descriptor, property)



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_literalvariable_is_not_abstract():
    assert not inspect.isabstract(sparqlas_LiteralVariable)


def test_sparqlas_literalvariable_constructor_exists():
    assert callable(sparqlas_LiteralVariable.__init__)


def test_sparqlas_literalvariable_constructor_args():
    sig = inspect.signature(sparqlas_LiteralVariable.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_objectpropertyvariable_is_not_abstract():
    assert not inspect.isabstract(sparqlas_ObjectPropertyVariable)


def test_sparqlas_objectpropertyvariable_constructor_exists():
    assert callable(sparqlas_ObjectPropertyVariable.__init__)


def test_sparqlas_objectpropertyvariable_constructor_args():
    sig = inspect.signature(sparqlas_ObjectPropertyVariable.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_datapropertyvariable_is_not_abstract():
    assert not inspect.isabstract(sparqlas_DataPropertyVariable)


def test_sparqlas_datapropertyvariable_constructor_exists():
    assert callable(sparqlas_DataPropertyVariable.__init__)


def test_sparqlas_datapropertyvariable_constructor_args():
    sig = inspect.signature(sparqlas_DataPropertyVariable.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_classvariable_is_not_abstract():
    assert not inspect.isabstract(sparqlas_ClassVariable)


def test_sparqlas_classvariable_constructor_exists():
    assert callable(sparqlas_ClassVariable.__init__)


def test_sparqlas_classvariable_constructor_args():
    sig = inspect.signature(sparqlas_ClassVariable.__init__)
    params = list(sig.parameters.keys())



def test_term_is_not_abstract():
    assert not inspect.isabstract(Term)


def test_term_constructor_exists():
    assert callable(Term.__init__)


def test_term_constructor_args():
    sig = inspect.signature(Term.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_term_is_not_abstract():
    assert not inspect.isabstract(sparqlas_Term)


def test_sparqlas_term_constructor_exists():
    assert callable(sparqlas_Term.__init__)


def test_sparqlas_term_constructor_args():
    sig = inspect.signature(sparqlas_Term.__init__)
    params = list(sig.parameters.keys())



def test_iri_is_not_abstract():
    assert not inspect.isabstract(IRI)


def test_iri_constructor_exists():
    assert callable(IRI.__init__)


def test_iri_constructor_args():
    sig = inspect.signature(IRI.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_abbreviatediri_is_not_abstract():
    assert not inspect.isabstract(sparqlas_AbbreviatedIRI)


def test_sparqlas_abbreviatediri_constructor_exists():
    assert callable(sparqlas_AbbreviatedIRI.__init__)


def test_sparqlas_abbreviatediri_constructor_args():
    sig = inspect.signature(sparqlas_AbbreviatedIRI.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_class_is_not_abstract():
    assert not inspect.isabstract(sparqlas_Class)


def test_sparqlas_class_constructor_exists():
    assert callable(sparqlas_Class.__init__)


def test_sparqlas_class_constructor_args():
    sig = inspect.signature(sparqlas_Class.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_constant_is_not_abstract():
    assert not inspect.isabstract(sparqlas_Constant)


def test_sparqlas_constant_constructor_exists():
    assert callable(sparqlas_Constant.__init__)


def test_sparqlas_constant_constructor_args():
    sig = inspect.signature(sparqlas_Constant.__init__)
    params = list(sig.parameters.keys())



def test_individual_is_not_abstract():
    assert not inspect.isabstract(Individual)


def test_individual_constructor_exists():
    assert callable(Individual.__init__)


def test_individual_constructor_args():
    sig = inspect.signature(Individual.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_anonymousindividual_is_not_abstract():
    assert not inspect.isabstract(sparqlas_AnonymousIndividual)


def test_sparqlas_anonymousindividual_constructor_exists():
    assert callable(sparqlas_AnonymousIndividual.__init__)


def test_sparqlas_anonymousindividual_constructor_args():
    sig = inspect.signature(sparqlas_AnonymousIndividual.__init__)
    params = list(sig.parameters.keys())
    assert "nodeID" in params, "Missing parameter 'nodeID'"

def test_sparqlas_anonymousindividual_has_nodeID():
    assert hasattr(sparqlas_AnonymousIndividual, "nodeID")
    descriptor = None
    for klass in sparqlas_AnonymousIndividual.__mro__:
        if "nodeID" in klass.__dict__:
            descriptor = klass.__dict__["nodeID"]
            break
    assert isinstance(descriptor, property)



def test_sparqlas_namedindividual_is_not_abstract():
    assert not inspect.isabstract(sparqlas_NamedIndividual)


def test_sparqlas_namedindividual_constructor_exists():
    assert callable(sparqlas_NamedIndividual.__init__)


def test_sparqlas_namedindividual_constructor_args():
    sig = inspect.signature(sparqlas_NamedIndividual.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_individualvariable_is_not_abstract():
    assert not inspect.isabstract(sparqlas_IndividualVariable)


def test_sparqlas_individualvariable_constructor_exists():
    assert callable(sparqlas_IndividualVariable.__init__)


def test_sparqlas_individualvariable_constructor_args():
    sig = inspect.signature(sparqlas_IndividualVariable.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_variable_is_not_abstract():
    assert not inspect.isabstract(sparqlas_Variable)


def test_sparqlas_variable_constructor_exists():
    assert callable(sparqlas_Variable.__init__)


def test_sparqlas_variable_constructor_args():
    sig = inspect.signature(sparqlas_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_sparqlas_variable_has_symbol():
    assert hasattr(sparqlas_Variable, "symbol")
    descriptor = None
    for klass in sparqlas_Variable.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)



def test_sparqlas_atom_is_not_abstract():
    assert not inspect.isabstract(sparqlas_Atom)


def test_sparqlas_atom_constructor_exists():
    assert callable(sparqlas_Atom.__init__)


def test_sparqlas_atom_constructor_args():
    sig = inspect.signature(sparqlas_Atom.__init__)
    params = list(sig.parameters.keys())



def test_templateableelement_is_not_abstract():
    assert not inspect.isabstract(TemplateableElement)


def test_templateableelement_constructor_exists():
    assert callable(TemplateableElement.__init__)


def test_templateableelement_constructor_args():
    sig = inspect.signature(TemplateableElement.__init__)
    params = list(sig.parameters.keys())



def test_query_is_not_abstract():
    assert not inspect.isabstract(Query)


def test_query_constructor_exists():
    assert callable(Query.__init__)


def test_query_constructor_args():
    sig = inspect.signature(Query.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_constructquery_is_not_abstract():
    assert not inspect.isabstract(sparqlas_ConstructQuery)


def test_sparqlas_constructquery_constructor_exists():
    assert callable(sparqlas_ConstructQuery.__init__)


def test_sparqlas_constructquery_constructor_args():
    sig = inspect.signature(sparqlas_ConstructQuery.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_selectquery_is_not_abstract():
    assert not inspect.isabstract(sparqlas_SelectQuery)


def test_sparqlas_selectquery_constructor_exists():
    assert callable(sparqlas_SelectQuery.__init__)


def test_sparqlas_selectquery_constructor_args():
    sig = inspect.signature(sparqlas_SelectQuery.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_fulliri_is_not_abstract():
    assert not inspect.isabstract(sparqlas_FullIRI)


def test_sparqlas_fulliri_constructor_exists():
    assert callable(sparqlas_FullIRI.__init__)


def test_sparqlas_fulliri_constructor_args():
    sig = inspect.signature(sparqlas_FullIRI.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_describequery_is_not_abstract():
    assert not inspect.isabstract(sparqlas_DescribeQuery)


def test_sparqlas_describequery_constructor_exists():
    assert callable(sparqlas_DescribeQuery.__init__)


def test_sparqlas_describequery_constructor_args():
    sig = inspect.signature(sparqlas_DescribeQuery.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_askquery_is_not_abstract():
    assert not inspect.isabstract(sparqlas_AskQuery)


def test_sparqlas_askquery_constructor_exists():
    assert callable(sparqlas_AskQuery.__init__)


def test_sparqlas_askquery_constructor_args():
    sig = inspect.signature(sparqlas_AskQuery.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_import_is_not_abstract():
    assert not inspect.isabstract(sparqlas_Import)


def test_sparqlas_import_constructor_exists():
    assert callable(sparqlas_Import.__init__)


def test_sparqlas_import_constructor_args():
    sig = inspect.signature(sparqlas_Import.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_iri_is_not_abstract():
    assert not inspect.isabstract(sparqlas_IRI)


def test_sparqlas_iri_constructor_exists():
    assert callable(sparqlas_IRI.__init__)


def test_sparqlas_iri_constructor_args():
    sig = inspect.signature(sparqlas_IRI.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_sparqlas_iri_has_id():
    assert hasattr(sparqlas_IRI, "id")
    descriptor = None
    for klass in sparqlas_IRI.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_sparqlas_ontologydocument_is_not_abstract():
    assert not inspect.isabstract(sparqlas_OntologyDocument)


def test_sparqlas_ontologydocument_constructor_exists():
    assert callable(sparqlas_OntologyDocument.__init__)


def test_sparqlas_ontologydocument_constructor_args():
    sig = inspect.signature(sparqlas_OntologyDocument.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_query_is_not_abstract():
    assert not inspect.isabstract(sparqlas_Query)


def test_sparqlas_query_constructor_exists():
    assert callable(sparqlas_Query.__init__)


def test_sparqlas_query_constructor_args():
    sig = inspect.signature(sparqlas_Query.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas_prefixdefinition_is_not_abstract():
    assert not inspect.isabstract(sparqlas_PrefixDefinition)


def test_sparqlas_prefixdefinition_constructor_exists():
    assert callable(sparqlas_PrefixDefinition.__init__)


def test_sparqlas_prefixdefinition_constructor_args():
    sig = inspect.signature(sparqlas_PrefixDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "pref" in params, "Missing parameter 'pref'"

def test_sparqlas_prefixdefinition_has_pref():
    assert hasattr(sparqlas_PrefixDefinition, "pref")
    descriptor = None
    for klass in sparqlas_PrefixDefinition.__mro__:
        if "pref" in klass.__dict__:
            descriptor = klass.__dict__["pref"]
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
sparqlas_TemplateBinding_strategy = st.builds(
    sparqlas_TemplateBinding,
)
sparqlas_TemplateableElement_strategy = st.builds(
    sparqlas_TemplateableElement,
)
sparqlas_TemplateParameterSubstitution_strategy = st.builds(
    sparqlas_TemplateParameterSubstitution,
)
sparqlas_TemplateSignature_strategy = st.builds(
    sparqlas_TemplateSignature,
)
sparqlas_TemplateParameter_strategy = st.builds(
    sparqlas_TemplateParameter,
)
sparqlas_ParameterableElement_strategy = st.builds(
    sparqlas_ParameterableElement,
)
Declaration_strategy = st.builds(
    Declaration,
)
sparqlas_ObjectPropertyDeclaration_strategy = st.builds(
    sparqlas_ObjectPropertyDeclaration,
)
sparqlas_DatatypePropertyDeclaration_strategy = st.builds(
    sparqlas_DatatypePropertyDeclaration,
)
sparqlas_ClassDeclaration_strategy = st.builds(
    sparqlas_ClassDeclaration,
)
sparqlas_IndividualDeclaration_strategy = st.builds(
    sparqlas_IndividualDeclaration,
)
DataPropertyAtom_strategy = st.builds(
    DataPropertyAtom,
)
sparqlas_DisjointDataProperties_strategy = st.builds(
    sparqlas_DisjointDataProperties,
)
sparqlas_DataPropertyDomain_strategy = st.builds(
    sparqlas_DataPropertyDomain,
)
sparqlas_EquivalentDataProperties_strategy = st.builds(
    sparqlas_EquivalentDataProperties,
)
sparqlas_DataPropertyRange_strategy = st.builds(
    sparqlas_DataPropertyRange,
)
sparqlas_FunctionalDataProperty_strategy = st.builds(
    sparqlas_FunctionalDataProperty,
)
sparqlas_SubDataPropertyOf_strategy = st.builds(
    sparqlas_SubDataPropertyOf,
)
sparqlas_ObjectPropertyChain_strategy = st.builds(
    sparqlas_ObjectPropertyChain,
)
ObjectPropertyAtom_strategy = st.builds(
    ObjectPropertyAtom,
)
sparqlas_FunctionalObjectProperty_strategy = st.builds(
    sparqlas_FunctionalObjectProperty,
)
sparqlas_AsymmetricObjectProperty_strategy = st.builds(
    sparqlas_AsymmetricObjectProperty,
)
sparqlas_IrreflexiveObjectProperty_strategy = st.builds(
    sparqlas_IrreflexiveObjectProperty,
)
sparqlas_EquivalentObjectProperties_strategy = st.builds(
    sparqlas_EquivalentObjectProperties,
)
sparqlas_TransitiveObjectProperty_strategy = st.builds(
    sparqlas_TransitiveObjectProperty,
)
sparqlas_ObjectPropertyRange_strategy = st.builds(
    sparqlas_ObjectPropertyRange,
)
sparqlas_SymmetricObjectProperty_strategy = st.builds(
    sparqlas_SymmetricObjectProperty,
)
sparqlas_ReflexiveObjectProperty_strategy = st.builds(
    sparqlas_ReflexiveObjectProperty,
)
sparqlas_InverseFunctionalObjectProperty_strategy = st.builds(
    sparqlas_InverseFunctionalObjectProperty,
)
sparqlas_InverseObjectPropertyAtom_strategy = st.builds(
    sparqlas_InverseObjectPropertyAtom,
)
sparqlas_ObjectPropertyDomain_strategy = st.builds(
    sparqlas_ObjectPropertyDomain,
)
sparqlas_DisjointObjectProperties_strategy = st.builds(
    sparqlas_DisjointObjectProperties,
)
sparqlas_FacetRestriction_strategy = st.builds(
    sparqlas_FacetRestriction,
)
sparqlas_SubObjectPropertyOf_strategy = st.builds(
    sparqlas_SubObjectPropertyOf,
)
sparqlas_DataRange_strategy = st.builds(
    sparqlas_DataRange,
)
Expression_strategy = st.builds(
    Expression,
)
ClassAtom_strategy = st.builds(
    ClassAtom,
)
sparqlas_EquivalentClasses_strategy = st.builds(
    sparqlas_EquivalentClasses,
)
sparqlas_DirectSubClassOf_strategy = st.builds(
    sparqlas_DirectSubClassOf,
)
sparqlas_StrictSubClassOf_strategy = st.builds(
    sparqlas_StrictSubClassOf,
)
sparqlas_DisjointUnion_strategy = st.builds(
    sparqlas_DisjointUnion,
)
sparqlas_SubClassOf_strategy = st.builds(
    sparqlas_SubClassOf,
)
sparqlas_DisjointClasses_strategy = st.builds(
    sparqlas_DisjointClasses,
)
sparqlas_DataPropertyExpression_strategy = st.builds(
    sparqlas_DataPropertyExpression,
)
sparqlas_ClassExpression_strategy = st.builds(
    sparqlas_ClassExpression,
)
Assertion_strategy = st.builds(
    Assertion,
)
sparqlas_DirectClassAssertion_strategy = st.builds(
    sparqlas_DirectClassAssertion,
)
sparqlas_NegativeObjectPropertyAssertion_strategy = st.builds(
    sparqlas_NegativeObjectPropertyAssertion,
)
sparqlas_NegativeDataPropertyAssertion_strategy = st.builds(
    sparqlas_NegativeDataPropertyAssertion,
)
sparqlas_DataPropertyAssertion_strategy = st.builds(
    sparqlas_DataPropertyAssertion,
)
sparqlas_DifferentIndividuals_strategy = st.builds(
    sparqlas_DifferentIndividuals,
)
sparqlas_SameIndividual_strategy = st.builds(
    sparqlas_SameIndividual,
)
sparqlas_ClassAssertion_strategy = st.builds(
    sparqlas_ClassAssertion,
)
Atom_strategy = st.builds(
    Atom,
)
sparqlas_ClassAtom_strategy = st.builds(
    sparqlas_ClassAtom,
)
sparqlas_Declaration_strategy = st.builds(
    sparqlas_Declaration,
)
sparqlas_HasKey_strategy = st.builds(
    sparqlas_HasKey,
)
sparqlas_ObjectPropertyAtom_strategy = st.builds(
    sparqlas_ObjectPropertyAtom,
)
sparqlas_DataPropertyAtom_strategy = st.builds(
    sparqlas_DataPropertyAtom,
)
sparqlas_Assertion_strategy = st.builds(
    sparqlas_Assertion,
)
ParameterableElement_strategy = st.builds(
    ParameterableElement,
)
sparqlas_Expression_strategy = st.builds(
    sparqlas_Expression,
)
AbstractLiteral_strategy = st.builds(
    AbstractLiteral,
)
sparqlas_Literal_strategy = st.builds(
    sparqlas_Literal,
    lexicalForm=
        safe_text
)
sparqlas_AbstractLiteral_strategy = st.builds(
    sparqlas_AbstractLiteral,
)
sparqlas_Individual_strategy = st.builds(
    sparqlas_Individual,
)
DataRange_strategy = st.builds(
    DataRange,
)
sparqlas_DataIntersectionOf_strategy = st.builds(
    sparqlas_DataIntersectionOf,
)
sparqlas_DataComplementOf_strategy = st.builds(
    sparqlas_DataComplementOf,
)
sparqlas_DatatypeRestriction_strategy = st.builds(
    sparqlas_DatatypeRestriction,
)
sparqlas_DataOneOf_strategy = st.builds(
    sparqlas_DataOneOf,
)
sparqlas_DataUnionOf_strategy = st.builds(
    sparqlas_DataUnionOf,
)
Constant_strategy = st.builds(
    Constant,
)
sparqlas_Datatype_strategy = st.builds(
    sparqlas_Datatype,
)
sparqlas_ObjectPropertyExpression_strategy = st.builds(
    sparqlas_ObjectPropertyExpression,
)
sparqlas_ObjectPropertyAssertion_strategy = st.builds(
    sparqlas_ObjectPropertyAssertion,
)
DataPropertyExpression_strategy = st.builds(
    DataPropertyExpression,
)
sparqlas_DataProperty_strategy = st.builds(
    sparqlas_DataProperty,
)
ObjectPropertyExpression_strategy = st.builds(
    ObjectPropertyExpression,
)
sparqlas_ObjectProperty_strategy = st.builds(
    sparqlas_ObjectProperty,
)
sparqlas_InverseObjectProperty_strategy = st.builds(
    sparqlas_InverseObjectProperty,
)
ClassExpression_strategy = st.builds(
    ClassExpression,
)
sparqlas_ObjectComplementOf_strategy = st.builds(
    sparqlas_ObjectComplementOf,
)
sparqlas_DataAllValuesFrom_strategy = st.builds(
    sparqlas_DataAllValuesFrom,
)
sparqlas_ObjectHasValue_strategy = st.builds(
    sparqlas_ObjectHasValue,
)
sparqlas_DataHasValue_strategy = st.builds(
    sparqlas_DataHasValue,
)
sparqlas_ObjectIntersectionOf_strategy = st.builds(
    sparqlas_ObjectIntersectionOf,
)
sparqlas_DataSomeValuesFrom_strategy = st.builds(
    sparqlas_DataSomeValuesFrom,
)
sparqlas_ObjectExactCardinality_strategy = st.builds(
    sparqlas_ObjectExactCardinality,
    cardinality=
        st.integers()
)
sparqlas_ObjectSomeValuesFrom_strategy = st.builds(
    sparqlas_ObjectSomeValuesFrom,
)
sparqlas_DataExactCardinality_strategy = st.builds(
    sparqlas_DataExactCardinality,
    cardinality=
        st.integers()
)
sparqlas_DataMinCardinality_strategy = st.builds(
    sparqlas_DataMinCardinality,
    cardinality=
        st.integers()
)
sparqlas_ObjectMaxCardinality_strategy = st.builds(
    sparqlas_ObjectMaxCardinality,
    cardinality=
        st.integers()
)
sparqlas_ObjectMinCardinality_strategy = st.builds(
    sparqlas_ObjectMinCardinality,
    cardinality=
        st.integers()
)
sparqlas_ObjectOneOf_strategy = st.builds(
    sparqlas_ObjectOneOf,
)
sparqlas_ObjectUnionOf_strategy = st.builds(
    sparqlas_ObjectUnionOf,
)
sparqlas_ObjectAllValuesFrom_strategy = st.builds(
    sparqlas_ObjectAllValuesFrom,
)
sparqlas_DataMaxCardinality_strategy = st.builds(
    sparqlas_DataMaxCardinality,
    cardinality=
        st.integers()
)
Variable_strategy = st.builds(
    Variable,
)
sparqlas_LiteralVariable_strategy = st.builds(
    sparqlas_LiteralVariable,
)
sparqlas_ObjectPropertyVariable_strategy = st.builds(
    sparqlas_ObjectPropertyVariable,
)
sparqlas_DataPropertyVariable_strategy = st.builds(
    sparqlas_DataPropertyVariable,
)
sparqlas_ClassVariable_strategy = st.builds(
    sparqlas_ClassVariable,
)
Term_strategy = st.builds(
    Term,
)
sparqlas_Term_strategy = st.builds(
    sparqlas_Term,
)
IRI_strategy = st.builds(
    IRI,
)
sparqlas_AbbreviatedIRI_strategy = st.builds(
    sparqlas_AbbreviatedIRI,
)
sparqlas_Class_strategy = st.builds(
    sparqlas_Class,
)
sparqlas_Constant_strategy = st.builds(
    sparqlas_Constant,
)
Individual_strategy = st.builds(
    Individual,
)
sparqlas_AnonymousIndividual_strategy = st.builds(
    sparqlas_AnonymousIndividual,
    nodeID=
        safe_text
)
sparqlas_NamedIndividual_strategy = st.builds(
    sparqlas_NamedIndividual,
)
sparqlas_IndividualVariable_strategy = st.builds(
    sparqlas_IndividualVariable,
)
sparqlas_Variable_strategy = st.builds(
    sparqlas_Variable,
    symbol=
        safe_text
)
sparqlas_Atom_strategy = st.builds(
    sparqlas_Atom,
)
TemplateableElement_strategy = st.builds(
    TemplateableElement,
)
Query_strategy = st.builds(
    Query,
)
sparqlas_ConstructQuery_strategy = st.builds(
    sparqlas_ConstructQuery,
)
sparqlas_SelectQuery_strategy = st.builds(
    sparqlas_SelectQuery,
)
sparqlas_FullIRI_strategy = st.builds(
    sparqlas_FullIRI,
)
sparqlas_DescribeQuery_strategy = st.builds(
    sparqlas_DescribeQuery,
)
sparqlas_AskQuery_strategy = st.builds(
    sparqlas_AskQuery,
)
sparqlas_Import_strategy = st.builds(
    sparqlas_Import,
)
sparqlas_IRI_strategy = st.builds(
    sparqlas_IRI,
    id=
        safe_text
)
sparqlas_OntologyDocument_strategy = st.builds(
    sparqlas_OntologyDocument,
)
sparqlas_Query_strategy = st.builds(
    sparqlas_Query,
)
sparqlas_PrefixDefinition_strategy = st.builds(
    sparqlas_PrefixDefinition,
    pref=
        safe_text
)

@given(instance=sparqlas_TemplateBinding_strategy)
@settings(max_examples=50)
def test_sparqlas_templatebinding_instantiation(instance):
    assert isinstance(instance, sparqlas_TemplateBinding)

@given(instance=sparqlas_TemplateableElement_strategy)
@settings(max_examples=50)
def test_sparqlas_templateableelement_instantiation(instance):
    assert isinstance(instance, sparqlas_TemplateableElement)

@given(instance=sparqlas_TemplateParameterSubstitution_strategy)
@settings(max_examples=50)
def test_sparqlas_templateparametersubstitution_instantiation(instance):
    assert isinstance(instance, sparqlas_TemplateParameterSubstitution)

@given(instance=sparqlas_TemplateSignature_strategy)
@settings(max_examples=50)
def test_sparqlas_templatesignature_instantiation(instance):
    assert isinstance(instance, sparqlas_TemplateSignature)

@given(instance=sparqlas_TemplateParameter_strategy)
@settings(max_examples=50)
def test_sparqlas_templateparameter_instantiation(instance):
    assert isinstance(instance, sparqlas_TemplateParameter)

@given(instance=sparqlas_ParameterableElement_strategy)
@settings(max_examples=50)
def test_sparqlas_parameterableelement_instantiation(instance):
    assert isinstance(instance, sparqlas_ParameterableElement)

@given(instance=Declaration_strategy)
@settings(max_examples=50)
def test_declaration_instantiation(instance):
    assert isinstance(instance, Declaration)

@given(instance=sparqlas_ObjectPropertyDeclaration_strategy)
@settings(max_examples=50)
def test_sparqlas_objectpropertydeclaration_instantiation(instance):
    assert isinstance(instance, sparqlas_ObjectPropertyDeclaration)

@given(instance=sparqlas_DatatypePropertyDeclaration_strategy)
@settings(max_examples=50)
def test_sparqlas_datatypepropertydeclaration_instantiation(instance):
    assert isinstance(instance, sparqlas_DatatypePropertyDeclaration)

@given(instance=sparqlas_ClassDeclaration_strategy)
@settings(max_examples=50)
def test_sparqlas_classdeclaration_instantiation(instance):
    assert isinstance(instance, sparqlas_ClassDeclaration)

@given(instance=sparqlas_IndividualDeclaration_strategy)
@settings(max_examples=50)
def test_sparqlas_individualdeclaration_instantiation(instance):
    assert isinstance(instance, sparqlas_IndividualDeclaration)

@given(instance=DataPropertyAtom_strategy)
@settings(max_examples=50)
def test_datapropertyatom_instantiation(instance):
    assert isinstance(instance, DataPropertyAtom)

@given(instance=sparqlas_DisjointDataProperties_strategy)
@settings(max_examples=50)
def test_sparqlas_disjointdataproperties_instantiation(instance):
    assert isinstance(instance, sparqlas_DisjointDataProperties)

@given(instance=sparqlas_DataPropertyDomain_strategy)
@settings(max_examples=50)
def test_sparqlas_datapropertydomain_instantiation(instance):
    assert isinstance(instance, sparqlas_DataPropertyDomain)

@given(instance=sparqlas_EquivalentDataProperties_strategy)
@settings(max_examples=50)
def test_sparqlas_equivalentdataproperties_instantiation(instance):
    assert isinstance(instance, sparqlas_EquivalentDataProperties)

@given(instance=sparqlas_DataPropertyRange_strategy)
@settings(max_examples=50)
def test_sparqlas_datapropertyrange_instantiation(instance):
    assert isinstance(instance, sparqlas_DataPropertyRange)

@given(instance=sparqlas_FunctionalDataProperty_strategy)
@settings(max_examples=50)
def test_sparqlas_functionaldataproperty_instantiation(instance):
    assert isinstance(instance, sparqlas_FunctionalDataProperty)

@given(instance=sparqlas_SubDataPropertyOf_strategy)
@settings(max_examples=50)
def test_sparqlas_subdatapropertyof_instantiation(instance):
    assert isinstance(instance, sparqlas_SubDataPropertyOf)

@given(instance=sparqlas_ObjectPropertyChain_strategy)
@settings(max_examples=50)
def test_sparqlas_objectpropertychain_instantiation(instance):
    assert isinstance(instance, sparqlas_ObjectPropertyChain)

@given(instance=ObjectPropertyAtom_strategy)
@settings(max_examples=50)
def test_objectpropertyatom_instantiation(instance):
    assert isinstance(instance, ObjectPropertyAtom)

@given(instance=sparqlas_FunctionalObjectProperty_strategy)
@settings(max_examples=50)
def test_sparqlas_functionalobjectproperty_instantiation(instance):
    assert isinstance(instance, sparqlas_FunctionalObjectProperty)

@given(instance=sparqlas_AsymmetricObjectProperty_strategy)
@settings(max_examples=50)
def test_sparqlas_asymmetricobjectproperty_instantiation(instance):
    assert isinstance(instance, sparqlas_AsymmetricObjectProperty)

@given(instance=sparqlas_IrreflexiveObjectProperty_strategy)
@settings(max_examples=50)
def test_sparqlas_irreflexiveobjectproperty_instantiation(instance):
    assert isinstance(instance, sparqlas_IrreflexiveObjectProperty)

@given(instance=sparqlas_EquivalentObjectProperties_strategy)
@settings(max_examples=50)
def test_sparqlas_equivalentobjectproperties_instantiation(instance):
    assert isinstance(instance, sparqlas_EquivalentObjectProperties)

@given(instance=sparqlas_TransitiveObjectProperty_strategy)
@settings(max_examples=50)
def test_sparqlas_transitiveobjectproperty_instantiation(instance):
    assert isinstance(instance, sparqlas_TransitiveObjectProperty)

@given(instance=sparqlas_ObjectPropertyRange_strategy)
@settings(max_examples=50)
def test_sparqlas_objectpropertyrange_instantiation(instance):
    assert isinstance(instance, sparqlas_ObjectPropertyRange)

@given(instance=sparqlas_SymmetricObjectProperty_strategy)
@settings(max_examples=50)
def test_sparqlas_symmetricobjectproperty_instantiation(instance):
    assert isinstance(instance, sparqlas_SymmetricObjectProperty)

@given(instance=sparqlas_ReflexiveObjectProperty_strategy)
@settings(max_examples=50)
def test_sparqlas_reflexiveobjectproperty_instantiation(instance):
    assert isinstance(instance, sparqlas_ReflexiveObjectProperty)

@given(instance=sparqlas_InverseFunctionalObjectProperty_strategy)
@settings(max_examples=50)
def test_sparqlas_inversefunctionalobjectproperty_instantiation(instance):
    assert isinstance(instance, sparqlas_InverseFunctionalObjectProperty)

@given(instance=sparqlas_InverseObjectPropertyAtom_strategy)
@settings(max_examples=50)
def test_sparqlas_inverseobjectpropertyatom_instantiation(instance):
    assert isinstance(instance, sparqlas_InverseObjectPropertyAtom)

@given(instance=sparqlas_ObjectPropertyDomain_strategy)
@settings(max_examples=50)
def test_sparqlas_objectpropertydomain_instantiation(instance):
    assert isinstance(instance, sparqlas_ObjectPropertyDomain)

@given(instance=sparqlas_DisjointObjectProperties_strategy)
@settings(max_examples=50)
def test_sparqlas_disjointobjectproperties_instantiation(instance):
    assert isinstance(instance, sparqlas_DisjointObjectProperties)

@given(instance=sparqlas_FacetRestriction_strategy)
@settings(max_examples=50)
def test_sparqlas_facetrestriction_instantiation(instance):
    assert isinstance(instance, sparqlas_FacetRestriction)

@given(instance=sparqlas_SubObjectPropertyOf_strategy)
@settings(max_examples=50)
def test_sparqlas_subobjectpropertyof_instantiation(instance):
    assert isinstance(instance, sparqlas_SubObjectPropertyOf)

@given(instance=sparqlas_DataRange_strategy)
@settings(max_examples=50)
def test_sparqlas_datarange_instantiation(instance):
    assert isinstance(instance, sparqlas_DataRange)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=ClassAtom_strategy)
@settings(max_examples=50)
def test_classatom_instantiation(instance):
    assert isinstance(instance, ClassAtom)

@given(instance=sparqlas_EquivalentClasses_strategy)
@settings(max_examples=50)
def test_sparqlas_equivalentclasses_instantiation(instance):
    assert isinstance(instance, sparqlas_EquivalentClasses)

@given(instance=sparqlas_DirectSubClassOf_strategy)
@settings(max_examples=50)
def test_sparqlas_directsubclassof_instantiation(instance):
    assert isinstance(instance, sparqlas_DirectSubClassOf)

@given(instance=sparqlas_StrictSubClassOf_strategy)
@settings(max_examples=50)
def test_sparqlas_strictsubclassof_instantiation(instance):
    assert isinstance(instance, sparqlas_StrictSubClassOf)

@given(instance=sparqlas_DisjointUnion_strategy)
@settings(max_examples=50)
def test_sparqlas_disjointunion_instantiation(instance):
    assert isinstance(instance, sparqlas_DisjointUnion)

@given(instance=sparqlas_SubClassOf_strategy)
@settings(max_examples=50)
def test_sparqlas_subclassof_instantiation(instance):
    assert isinstance(instance, sparqlas_SubClassOf)

@given(instance=sparqlas_DisjointClasses_strategy)
@settings(max_examples=50)
def test_sparqlas_disjointclasses_instantiation(instance):
    assert isinstance(instance, sparqlas_DisjointClasses)

@given(instance=sparqlas_DataPropertyExpression_strategy)
@settings(max_examples=50)
def test_sparqlas_datapropertyexpression_instantiation(instance):
    assert isinstance(instance, sparqlas_DataPropertyExpression)

@given(instance=sparqlas_ClassExpression_strategy)
@settings(max_examples=50)
def test_sparqlas_classexpression_instantiation(instance):
    assert isinstance(instance, sparqlas_ClassExpression)

@given(instance=Assertion_strategy)
@settings(max_examples=50)
def test_assertion_instantiation(instance):
    assert isinstance(instance, Assertion)

@given(instance=sparqlas_DirectClassAssertion_strategy)
@settings(max_examples=50)
def test_sparqlas_directclassassertion_instantiation(instance):
    assert isinstance(instance, sparqlas_DirectClassAssertion)

@given(instance=sparqlas_NegativeObjectPropertyAssertion_strategy)
@settings(max_examples=50)
def test_sparqlas_negativeobjectpropertyassertion_instantiation(instance):
    assert isinstance(instance, sparqlas_NegativeObjectPropertyAssertion)

@given(instance=sparqlas_NegativeDataPropertyAssertion_strategy)
@settings(max_examples=50)
def test_sparqlas_negativedatapropertyassertion_instantiation(instance):
    assert isinstance(instance, sparqlas_NegativeDataPropertyAssertion)

@given(instance=sparqlas_DataPropertyAssertion_strategy)
@settings(max_examples=50)
def test_sparqlas_datapropertyassertion_instantiation(instance):
    assert isinstance(instance, sparqlas_DataPropertyAssertion)

@given(instance=sparqlas_DifferentIndividuals_strategy)
@settings(max_examples=50)
def test_sparqlas_differentindividuals_instantiation(instance):
    assert isinstance(instance, sparqlas_DifferentIndividuals)

@given(instance=sparqlas_SameIndividual_strategy)
@settings(max_examples=50)
def test_sparqlas_sameindividual_instantiation(instance):
    assert isinstance(instance, sparqlas_SameIndividual)

@given(instance=sparqlas_ClassAssertion_strategy)
@settings(max_examples=50)
def test_sparqlas_classassertion_instantiation(instance):
    assert isinstance(instance, sparqlas_ClassAssertion)

@given(instance=Atom_strategy)
@settings(max_examples=50)
def test_atom_instantiation(instance):
    assert isinstance(instance, Atom)

@given(instance=sparqlas_ClassAtom_strategy)
@settings(max_examples=50)
def test_sparqlas_classatom_instantiation(instance):
    assert isinstance(instance, sparqlas_ClassAtom)

@given(instance=sparqlas_Declaration_strategy)
@settings(max_examples=50)
def test_sparqlas_declaration_instantiation(instance):
    assert isinstance(instance, sparqlas_Declaration)

@given(instance=sparqlas_HasKey_strategy)
@settings(max_examples=50)
def test_sparqlas_haskey_instantiation(instance):
    assert isinstance(instance, sparqlas_HasKey)

@given(instance=sparqlas_ObjectPropertyAtom_strategy)
@settings(max_examples=50)
def test_sparqlas_objectpropertyatom_instantiation(instance):
    assert isinstance(instance, sparqlas_ObjectPropertyAtom)

@given(instance=sparqlas_DataPropertyAtom_strategy)
@settings(max_examples=50)
def test_sparqlas_datapropertyatom_instantiation(instance):
    assert isinstance(instance, sparqlas_DataPropertyAtom)

@given(instance=sparqlas_Assertion_strategy)
@settings(max_examples=50)
def test_sparqlas_assertion_instantiation(instance):
    assert isinstance(instance, sparqlas_Assertion)

@given(instance=ParameterableElement_strategy)
@settings(max_examples=50)
def test_parameterableelement_instantiation(instance):
    assert isinstance(instance, ParameterableElement)

@given(instance=sparqlas_Expression_strategy)
@settings(max_examples=50)
def test_sparqlas_expression_instantiation(instance):
    assert isinstance(instance, sparqlas_Expression)

@given(instance=AbstractLiteral_strategy)
@settings(max_examples=50)
def test_abstractliteral_instantiation(instance):
    assert isinstance(instance, AbstractLiteral)

@given(instance=sparqlas_Literal_strategy)
@settings(max_examples=50)
def test_sparqlas_literal_instantiation(instance):
    assert isinstance(instance, sparqlas_Literal)



@given(instance=sparqlas_Literal_strategy)
def test_sparqlas_literal_lexicalForm_setter(instance):
    original = instance.lexicalForm
    instance.lexicalForm = original
    assert instance.lexicalForm == original

@given(instance=sparqlas_AbstractLiteral_strategy)
@settings(max_examples=50)
def test_sparqlas_abstractliteral_instantiation(instance):
    assert isinstance(instance, sparqlas_AbstractLiteral)

@given(instance=sparqlas_Individual_strategy)
@settings(max_examples=50)
def test_sparqlas_individual_instantiation(instance):
    assert isinstance(instance, sparqlas_Individual)

@given(instance=DataRange_strategy)
@settings(max_examples=50)
def test_datarange_instantiation(instance):
    assert isinstance(instance, DataRange)

@given(instance=sparqlas_DataIntersectionOf_strategy)
@settings(max_examples=50)
def test_sparqlas_dataintersectionof_instantiation(instance):
    assert isinstance(instance, sparqlas_DataIntersectionOf)

@given(instance=sparqlas_DataComplementOf_strategy)
@settings(max_examples=50)
def test_sparqlas_datacomplementof_instantiation(instance):
    assert isinstance(instance, sparqlas_DataComplementOf)

@given(instance=sparqlas_DatatypeRestriction_strategy)
@settings(max_examples=50)
def test_sparqlas_datatyperestriction_instantiation(instance):
    assert isinstance(instance, sparqlas_DatatypeRestriction)

@given(instance=sparqlas_DataOneOf_strategy)
@settings(max_examples=50)
def test_sparqlas_dataoneof_instantiation(instance):
    assert isinstance(instance, sparqlas_DataOneOf)

@given(instance=sparqlas_DataUnionOf_strategy)
@settings(max_examples=50)
def test_sparqlas_dataunionof_instantiation(instance):
    assert isinstance(instance, sparqlas_DataUnionOf)

@given(instance=Constant_strategy)
@settings(max_examples=50)
def test_constant_instantiation(instance):
    assert isinstance(instance, Constant)

@given(instance=sparqlas_Datatype_strategy)
@settings(max_examples=50)
def test_sparqlas_datatype_instantiation(instance):
    assert isinstance(instance, sparqlas_Datatype)

@given(instance=sparqlas_ObjectPropertyExpression_strategy)
@settings(max_examples=50)
def test_sparqlas_objectpropertyexpression_instantiation(instance):
    assert isinstance(instance, sparqlas_ObjectPropertyExpression)

@given(instance=sparqlas_ObjectPropertyAssertion_strategy)
@settings(max_examples=50)
def test_sparqlas_objectpropertyassertion_instantiation(instance):
    assert isinstance(instance, sparqlas_ObjectPropertyAssertion)

@given(instance=DataPropertyExpression_strategy)
@settings(max_examples=50)
def test_datapropertyexpression_instantiation(instance):
    assert isinstance(instance, DataPropertyExpression)

@given(instance=sparqlas_DataProperty_strategy)
@settings(max_examples=50)
def test_sparqlas_dataproperty_instantiation(instance):
    assert isinstance(instance, sparqlas_DataProperty)

@given(instance=ObjectPropertyExpression_strategy)
@settings(max_examples=50)
def test_objectpropertyexpression_instantiation(instance):
    assert isinstance(instance, ObjectPropertyExpression)

@given(instance=sparqlas_ObjectProperty_strategy)
@settings(max_examples=50)
def test_sparqlas_objectproperty_instantiation(instance):
    assert isinstance(instance, sparqlas_ObjectProperty)

@given(instance=sparqlas_InverseObjectProperty_strategy)
@settings(max_examples=50)
def test_sparqlas_inverseobjectproperty_instantiation(instance):
    assert isinstance(instance, sparqlas_InverseObjectProperty)

@given(instance=ClassExpression_strategy)
@settings(max_examples=50)
def test_classexpression_instantiation(instance):
    assert isinstance(instance, ClassExpression)

@given(instance=sparqlas_ObjectComplementOf_strategy)
@settings(max_examples=50)
def test_sparqlas_objectcomplementof_instantiation(instance):
    assert isinstance(instance, sparqlas_ObjectComplementOf)

@given(instance=sparqlas_DataAllValuesFrom_strategy)
@settings(max_examples=50)
def test_sparqlas_dataallvaluesfrom_instantiation(instance):
    assert isinstance(instance, sparqlas_DataAllValuesFrom)

@given(instance=sparqlas_ObjectHasValue_strategy)
@settings(max_examples=50)
def test_sparqlas_objecthasvalue_instantiation(instance):
    assert isinstance(instance, sparqlas_ObjectHasValue)

@given(instance=sparqlas_DataHasValue_strategy)
@settings(max_examples=50)
def test_sparqlas_datahasvalue_instantiation(instance):
    assert isinstance(instance, sparqlas_DataHasValue)

@given(instance=sparqlas_ObjectIntersectionOf_strategy)
@settings(max_examples=50)
def test_sparqlas_objectintersectionof_instantiation(instance):
    assert isinstance(instance, sparqlas_ObjectIntersectionOf)

@given(instance=sparqlas_DataSomeValuesFrom_strategy)
@settings(max_examples=50)
def test_sparqlas_datasomevaluesfrom_instantiation(instance):
    assert isinstance(instance, sparqlas_DataSomeValuesFrom)

@given(instance=sparqlas_ObjectExactCardinality_strategy)
@settings(max_examples=50)
def test_sparqlas_objectexactcardinality_instantiation(instance):
    assert isinstance(instance, sparqlas_ObjectExactCardinality)



@given(instance=sparqlas_ObjectExactCardinality_strategy)
def test_sparqlas_objectexactcardinality_cardinality_setter(instance):
    original = instance.cardinality
    instance.cardinality = original
    assert instance.cardinality == original

@given(instance=sparqlas_ObjectSomeValuesFrom_strategy)
@settings(max_examples=50)
def test_sparqlas_objectsomevaluesfrom_instantiation(instance):
    assert isinstance(instance, sparqlas_ObjectSomeValuesFrom)

@given(instance=sparqlas_DataExactCardinality_strategy)
@settings(max_examples=50)
def test_sparqlas_dataexactcardinality_instantiation(instance):
    assert isinstance(instance, sparqlas_DataExactCardinality)



@given(instance=sparqlas_DataExactCardinality_strategy)
def test_sparqlas_dataexactcardinality_cardinality_setter(instance):
    original = instance.cardinality
    instance.cardinality = original
    assert instance.cardinality == original

@given(instance=sparqlas_DataMinCardinality_strategy)
@settings(max_examples=50)
def test_sparqlas_datamincardinality_instantiation(instance):
    assert isinstance(instance, sparqlas_DataMinCardinality)



@given(instance=sparqlas_DataMinCardinality_strategy)
def test_sparqlas_datamincardinality_cardinality_setter(instance):
    original = instance.cardinality
    instance.cardinality = original
    assert instance.cardinality == original

@given(instance=sparqlas_ObjectMaxCardinality_strategy)
@settings(max_examples=50)
def test_sparqlas_objectmaxcardinality_instantiation(instance):
    assert isinstance(instance, sparqlas_ObjectMaxCardinality)



@given(instance=sparqlas_ObjectMaxCardinality_strategy)
def test_sparqlas_objectmaxcardinality_cardinality_setter(instance):
    original = instance.cardinality
    instance.cardinality = original
    assert instance.cardinality == original

@given(instance=sparqlas_ObjectMinCardinality_strategy)
@settings(max_examples=50)
def test_sparqlas_objectmincardinality_instantiation(instance):
    assert isinstance(instance, sparqlas_ObjectMinCardinality)



@given(instance=sparqlas_ObjectMinCardinality_strategy)
def test_sparqlas_objectmincardinality_cardinality_setter(instance):
    original = instance.cardinality
    instance.cardinality = original
    assert instance.cardinality == original

@given(instance=sparqlas_ObjectOneOf_strategy)
@settings(max_examples=50)
def test_sparqlas_objectoneof_instantiation(instance):
    assert isinstance(instance, sparqlas_ObjectOneOf)

@given(instance=sparqlas_ObjectUnionOf_strategy)
@settings(max_examples=50)
def test_sparqlas_objectunionof_instantiation(instance):
    assert isinstance(instance, sparqlas_ObjectUnionOf)

@given(instance=sparqlas_ObjectAllValuesFrom_strategy)
@settings(max_examples=50)
def test_sparqlas_objectallvaluesfrom_instantiation(instance):
    assert isinstance(instance, sparqlas_ObjectAllValuesFrom)

@given(instance=sparqlas_DataMaxCardinality_strategy)
@settings(max_examples=50)
def test_sparqlas_datamaxcardinality_instantiation(instance):
    assert isinstance(instance, sparqlas_DataMaxCardinality)



@given(instance=sparqlas_DataMaxCardinality_strategy)
def test_sparqlas_datamaxcardinality_cardinality_setter(instance):
    original = instance.cardinality
    instance.cardinality = original
    assert instance.cardinality == original

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=sparqlas_LiteralVariable_strategy)
@settings(max_examples=50)
def test_sparqlas_literalvariable_instantiation(instance):
    assert isinstance(instance, sparqlas_LiteralVariable)

@given(instance=sparqlas_ObjectPropertyVariable_strategy)
@settings(max_examples=50)
def test_sparqlas_objectpropertyvariable_instantiation(instance):
    assert isinstance(instance, sparqlas_ObjectPropertyVariable)

@given(instance=sparqlas_DataPropertyVariable_strategy)
@settings(max_examples=50)
def test_sparqlas_datapropertyvariable_instantiation(instance):
    assert isinstance(instance, sparqlas_DataPropertyVariable)

@given(instance=sparqlas_ClassVariable_strategy)
@settings(max_examples=50)
def test_sparqlas_classvariable_instantiation(instance):
    assert isinstance(instance, sparqlas_ClassVariable)

@given(instance=Term_strategy)
@settings(max_examples=50)
def test_term_instantiation(instance):
    assert isinstance(instance, Term)

@given(instance=sparqlas_Term_strategy)
@settings(max_examples=50)
def test_sparqlas_term_instantiation(instance):
    assert isinstance(instance, sparqlas_Term)

@given(instance=IRI_strategy)
@settings(max_examples=50)
def test_iri_instantiation(instance):
    assert isinstance(instance, IRI)

@given(instance=sparqlas_AbbreviatedIRI_strategy)
@settings(max_examples=50)
def test_sparqlas_abbreviatediri_instantiation(instance):
    assert isinstance(instance, sparqlas_AbbreviatedIRI)

@given(instance=sparqlas_Class_strategy)
@settings(max_examples=50)
def test_sparqlas_class_instantiation(instance):
    assert isinstance(instance, sparqlas_Class)

@given(instance=sparqlas_Constant_strategy)
@settings(max_examples=50)
def test_sparqlas_constant_instantiation(instance):
    assert isinstance(instance, sparqlas_Constant)

@given(instance=Individual_strategy)
@settings(max_examples=50)
def test_individual_instantiation(instance):
    assert isinstance(instance, Individual)

@given(instance=sparqlas_AnonymousIndividual_strategy)
@settings(max_examples=50)
def test_sparqlas_anonymousindividual_instantiation(instance):
    assert isinstance(instance, sparqlas_AnonymousIndividual)



@given(instance=sparqlas_AnonymousIndividual_strategy)
def test_sparqlas_anonymousindividual_nodeID_setter(instance):
    original = instance.nodeID
    instance.nodeID = original
    assert instance.nodeID == original

@given(instance=sparqlas_NamedIndividual_strategy)
@settings(max_examples=50)
def test_sparqlas_namedindividual_instantiation(instance):
    assert isinstance(instance, sparqlas_NamedIndividual)

@given(instance=sparqlas_IndividualVariable_strategy)
@settings(max_examples=50)
def test_sparqlas_individualvariable_instantiation(instance):
    assert isinstance(instance, sparqlas_IndividualVariable)

@given(instance=sparqlas_Variable_strategy)
@settings(max_examples=50)
def test_sparqlas_variable_instantiation(instance):
    assert isinstance(instance, sparqlas_Variable)



@given(instance=sparqlas_Variable_strategy)
def test_sparqlas_variable_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=sparqlas_Atom_strategy)
@settings(max_examples=50)
def test_sparqlas_atom_instantiation(instance):
    assert isinstance(instance, sparqlas_Atom)

@given(instance=TemplateableElement_strategy)
@settings(max_examples=50)
def test_templateableelement_instantiation(instance):
    assert isinstance(instance, TemplateableElement)

@given(instance=Query_strategy)
@settings(max_examples=50)
def test_query_instantiation(instance):
    assert isinstance(instance, Query)

@given(instance=sparqlas_ConstructQuery_strategy)
@settings(max_examples=50)
def test_sparqlas_constructquery_instantiation(instance):
    assert isinstance(instance, sparqlas_ConstructQuery)

@given(instance=sparqlas_SelectQuery_strategy)
@settings(max_examples=50)
def test_sparqlas_selectquery_instantiation(instance):
    assert isinstance(instance, sparqlas_SelectQuery)

@given(instance=sparqlas_FullIRI_strategy)
@settings(max_examples=50)
def test_sparqlas_fulliri_instantiation(instance):
    assert isinstance(instance, sparqlas_FullIRI)

@given(instance=sparqlas_DescribeQuery_strategy)
@settings(max_examples=50)
def test_sparqlas_describequery_instantiation(instance):
    assert isinstance(instance, sparqlas_DescribeQuery)

@given(instance=sparqlas_AskQuery_strategy)
@settings(max_examples=50)
def test_sparqlas_askquery_instantiation(instance):
    assert isinstance(instance, sparqlas_AskQuery)

@given(instance=sparqlas_Import_strategy)
@settings(max_examples=50)
def test_sparqlas_import_instantiation(instance):
    assert isinstance(instance, sparqlas_Import)

@given(instance=sparqlas_IRI_strategy)
@settings(max_examples=50)
def test_sparqlas_iri_instantiation(instance):
    assert isinstance(instance, sparqlas_IRI)



@given(instance=sparqlas_IRI_strategy)
def test_sparqlas_iri_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=sparqlas_OntologyDocument_strategy)
@settings(max_examples=50)
def test_sparqlas_ontologydocument_instantiation(instance):
    assert isinstance(instance, sparqlas_OntologyDocument)

@given(instance=sparqlas_Query_strategy)
@settings(max_examples=50)
def test_sparqlas_query_instantiation(instance):
    assert isinstance(instance, sparqlas_Query)

@given(instance=sparqlas_PrefixDefinition_strategy)
@settings(max_examples=50)
def test_sparqlas_prefixdefinition_instantiation(instance):
    assert isinstance(instance, sparqlas_PrefixDefinition)



@given(instance=sparqlas_PrefixDefinition_strategy)
def test_sparqlas_prefixdefinition_pref_setter(instance):
    original = instance.pref
    instance.pref = original
    assert instance.pref == original
