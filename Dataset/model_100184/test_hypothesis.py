import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    sparqlas::TemplateBinding,
    sparqlas::TemplateableElement,
    sparqlas::TemplateParameterSubstitution,
    sparqlas::TemplateSignature,
    sparqlas::TemplateParameter,
    sparqlas::ParameterableElement,
    Declaration,
    sparqlas::DatatypePropertyDeclaration,
    sparqlas::ObjectPropertyDeclaration,
    sparqlas::ClassDeclaration,
    sparqlas::IndividualDeclaration,
    DataPropertyAtom,
    sparqlas::DisjointDataProperties,
    sparqlas::FunctionalDataProperty,
    sparqlas::DataPropertyDomain,
    sparqlas::DataPropertyRange,
    sparqlas::EquivalentDataProperties,
    sparqlas::SubDataPropertyOf,
    sparqlas::ObjectPropertyChain,
    ObjectPropertyAtom,
    sparqlas::SymmetricObjectProperty,
    sparqlas::EquivalentObjectProperties,
    sparqlas::IrreflexiveObjectProperty,
    sparqlas::ObjectPropertyRange,
    sparqlas::TransitiveObjectProperty,
    sparqlas::InverseObjectPropertyAtom,
    sparqlas::AsymmetricObjectProperty,
    sparqlas::ReflexiveObjectProperty,
    sparqlas::InverseFunctionalObjectProperty,
    sparqlas::FunctionalObjectProperty,
    sparqlas::ObjectPropertyDomain,
    sparqlas::DisjointObjectProperties,
    sparqlas::FacetRestriction,
    sparqlas::SubObjectPropertyOf,
    sparqlas::DataRange,
    Expression,
    ClassAtom,
    sparqlas::StrictSubClassOf,
    sparqlas::DirectSubClassOf,
    sparqlas::DisjointUnion,
    sparqlas::EquivalentClasses,
    sparqlas::SubClassOf,
    sparqlas::DisjointClasses,
    sparqlas::DataPropertyExpression,
    sparqlas::ClassExpression,
    Assertion,
    sparqlas::DataPropertyAssertion,
    sparqlas::NegativeDataPropertyAssertion,
    sparqlas::SameIndividual,
    sparqlas::DirectClassAssertion,
    sparqlas::NegativeObjectPropertyAssertion,
    sparqlas::DifferentIndividuals,
    sparqlas::ClassAssertion,
    Atom,
    sparqlas::HasKey,
    sparqlas::ClassAtom,
    sparqlas::Declaration,
    sparqlas::ObjectPropertyAtom,
    sparqlas::DataPropertyAtom,
    sparqlas::Assertion,
    ParameterableElement,
    sparqlas::Expression,
    AbstractLiteral,
    sparqlas::Literal,
    sparqlas::AbstractLiteral,
    sparqlas::Individual,
    DataRange,
    sparqlas::DatatypeRestriction,
    sparqlas::DataOneOf,
    sparqlas::DataComplementOf,
    sparqlas::DataIntersectionOf,
    sparqlas::DataUnionOf,
    Constant,
    sparqlas::Datatype,
    sparqlas::ObjectPropertyExpression,
    sparqlas::ObjectPropertyAssertion,
    DataPropertyExpression,
    sparqlas::DataProperty,
    ObjectPropertyExpression,
    sparqlas::ObjectProperty,
    sparqlas::InverseObjectProperty,
    ClassExpression,
    sparqlas::ObjectAllValuesFrom,
    sparqlas::ObjectUnionOf,
    sparqlas::ObjectExactCardinality,
    sparqlas::ObjectHasValue,
    sparqlas::ObjectMinCardinality,
    sparqlas::ObjectOneOf,
    sparqlas::DataHasValue,
    sparqlas::DataAllValuesFrom,
    sparqlas::ObjectIntersectionOf,
    sparqlas::DataExactCardinality,
    sparqlas::DataSomeValuesFrom,
    sparqlas::DataMaxCardinality,
    sparqlas::ObjectComplementOf,
    sparqlas::ObjectMaxCardinality,
    sparqlas::DataMinCardinality,
    sparqlas::ObjectSomeValuesFrom,
    Variable,
    sparqlas::ObjectPropertyVariable,
    sparqlas::LiteralVariable,
    sparqlas::DataPropertyVariable,
    sparqlas::ClassVariable,
    Term,
    sparqlas::Term,
    IRI,
    sparqlas::AbbreviatedIRI,
    sparqlas::Class,
    sparqlas::Constant,
    Individual,
    sparqlas::NamedIndividual,
    sparqlas::AnonymousIndividual,
    sparqlas::IndividualVariable,
    sparqlas::Variable,
    sparqlas::Atom,
    TemplateableElement,
    Query,
    sparqlas::ConstructQuery,
    sparqlas::SelectQuery,
    sparqlas::FullIRI,
    sparqlas::DescribeQuery,
    sparqlas::AskQuery,
    sparqlas::Import,
    sparqlas::IRI,
    sparqlas::OntologyDocument,
    sparqlas::Query,
    sparqlas::PrefixDefinition,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sparqlas::templatebinding_is_not_abstract():
    assert not inspect.isabstract(sparqlas::TemplateBinding)


def test_sparqlas::templatebinding_constructor_exists():
    assert callable(sparqlas::TemplateBinding.__init__)


def test_sparqlas::templatebinding_constructor_args():
    sig = inspect.signature(sparqlas::TemplateBinding.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::templateableelement_is_not_abstract():
    assert not inspect.isabstract(sparqlas::TemplateableElement)


def test_sparqlas::templateableelement_constructor_exists():
    assert callable(sparqlas::TemplateableElement.__init__)


def test_sparqlas::templateableelement_constructor_args():
    sig = inspect.signature(sparqlas::TemplateableElement.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::templateparametersubstitution_is_not_abstract():
    assert not inspect.isabstract(sparqlas::TemplateParameterSubstitution)


def test_sparqlas::templateparametersubstitution_constructor_exists():
    assert callable(sparqlas::TemplateParameterSubstitution.__init__)


def test_sparqlas::templateparametersubstitution_constructor_args():
    sig = inspect.signature(sparqlas::TemplateParameterSubstitution.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::templatesignature_is_not_abstract():
    assert not inspect.isabstract(sparqlas::TemplateSignature)


def test_sparqlas::templatesignature_constructor_exists():
    assert callable(sparqlas::TemplateSignature.__init__)


def test_sparqlas::templatesignature_constructor_args():
    sig = inspect.signature(sparqlas::TemplateSignature.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::templateparameter_is_not_abstract():
    assert not inspect.isabstract(sparqlas::TemplateParameter)


def test_sparqlas::templateparameter_constructor_exists():
    assert callable(sparqlas::TemplateParameter.__init__)


def test_sparqlas::templateparameter_constructor_args():
    sig = inspect.signature(sparqlas::TemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::parameterableelement_is_not_abstract():
    assert not inspect.isabstract(sparqlas::ParameterableElement)


def test_sparqlas::parameterableelement_constructor_exists():
    assert callable(sparqlas::ParameterableElement.__init__)


def test_sparqlas::parameterableelement_constructor_args():
    sig = inspect.signature(sparqlas::ParameterableElement.__init__)
    params = list(sig.parameters.keys())



def test_declaration_is_not_abstract():
    assert not inspect.isabstract(Declaration)


def test_declaration_constructor_exists():
    assert callable(Declaration.__init__)


def test_declaration_constructor_args():
    sig = inspect.signature(Declaration.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::datatypepropertydeclaration_is_not_abstract():
    assert not inspect.isabstract(sparqlas::DatatypePropertyDeclaration)


def test_sparqlas::datatypepropertydeclaration_constructor_exists():
    assert callable(sparqlas::DatatypePropertyDeclaration.__init__)


def test_sparqlas::datatypepropertydeclaration_constructor_args():
    sig = inspect.signature(sparqlas::DatatypePropertyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::objectpropertydeclaration_is_not_abstract():
    assert not inspect.isabstract(sparqlas::ObjectPropertyDeclaration)


def test_sparqlas::objectpropertydeclaration_constructor_exists():
    assert callable(sparqlas::ObjectPropertyDeclaration.__init__)


def test_sparqlas::objectpropertydeclaration_constructor_args():
    sig = inspect.signature(sparqlas::ObjectPropertyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::classdeclaration_is_not_abstract():
    assert not inspect.isabstract(sparqlas::ClassDeclaration)


def test_sparqlas::classdeclaration_constructor_exists():
    assert callable(sparqlas::ClassDeclaration.__init__)


def test_sparqlas::classdeclaration_constructor_args():
    sig = inspect.signature(sparqlas::ClassDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::individualdeclaration_is_not_abstract():
    assert not inspect.isabstract(sparqlas::IndividualDeclaration)


def test_sparqlas::individualdeclaration_constructor_exists():
    assert callable(sparqlas::IndividualDeclaration.__init__)


def test_sparqlas::individualdeclaration_constructor_args():
    sig = inspect.signature(sparqlas::IndividualDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_datapropertyatom_is_not_abstract():
    assert not inspect.isabstract(DataPropertyAtom)


def test_datapropertyatom_constructor_exists():
    assert callable(DataPropertyAtom.__init__)


def test_datapropertyatom_constructor_args():
    sig = inspect.signature(DataPropertyAtom.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::disjointdataproperties_is_not_abstract():
    assert not inspect.isabstract(sparqlas::DisjointDataProperties)


def test_sparqlas::disjointdataproperties_constructor_exists():
    assert callable(sparqlas::DisjointDataProperties.__init__)


def test_sparqlas::disjointdataproperties_constructor_args():
    sig = inspect.signature(sparqlas::DisjointDataProperties.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::functionaldataproperty_is_not_abstract():
    assert not inspect.isabstract(sparqlas::FunctionalDataProperty)


def test_sparqlas::functionaldataproperty_constructor_exists():
    assert callable(sparqlas::FunctionalDataProperty.__init__)


def test_sparqlas::functionaldataproperty_constructor_args():
    sig = inspect.signature(sparqlas::FunctionalDataProperty.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::datapropertydomain_is_not_abstract():
    assert not inspect.isabstract(sparqlas::DataPropertyDomain)


def test_sparqlas::datapropertydomain_constructor_exists():
    assert callable(sparqlas::DataPropertyDomain.__init__)


def test_sparqlas::datapropertydomain_constructor_args():
    sig = inspect.signature(sparqlas::DataPropertyDomain.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::datapropertyrange_is_not_abstract():
    assert not inspect.isabstract(sparqlas::DataPropertyRange)


def test_sparqlas::datapropertyrange_constructor_exists():
    assert callable(sparqlas::DataPropertyRange.__init__)


def test_sparqlas::datapropertyrange_constructor_args():
    sig = inspect.signature(sparqlas::DataPropertyRange.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::equivalentdataproperties_is_not_abstract():
    assert not inspect.isabstract(sparqlas::EquivalentDataProperties)


def test_sparqlas::equivalentdataproperties_constructor_exists():
    assert callable(sparqlas::EquivalentDataProperties.__init__)


def test_sparqlas::equivalentdataproperties_constructor_args():
    sig = inspect.signature(sparqlas::EquivalentDataProperties.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::subdatapropertyof_is_not_abstract():
    assert not inspect.isabstract(sparqlas::SubDataPropertyOf)


def test_sparqlas::subdatapropertyof_constructor_exists():
    assert callable(sparqlas::SubDataPropertyOf.__init__)


def test_sparqlas::subdatapropertyof_constructor_args():
    sig = inspect.signature(sparqlas::SubDataPropertyOf.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::objectpropertychain_is_not_abstract():
    assert not inspect.isabstract(sparqlas::ObjectPropertyChain)


def test_sparqlas::objectpropertychain_constructor_exists():
    assert callable(sparqlas::ObjectPropertyChain.__init__)


def test_sparqlas::objectpropertychain_constructor_args():
    sig = inspect.signature(sparqlas::ObjectPropertyChain.__init__)
    params = list(sig.parameters.keys())



def test_objectpropertyatom_is_not_abstract():
    assert not inspect.isabstract(ObjectPropertyAtom)


def test_objectpropertyatom_constructor_exists():
    assert callable(ObjectPropertyAtom.__init__)


def test_objectpropertyatom_constructor_args():
    sig = inspect.signature(ObjectPropertyAtom.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::symmetricobjectproperty_is_not_abstract():
    assert not inspect.isabstract(sparqlas::SymmetricObjectProperty)


def test_sparqlas::symmetricobjectproperty_constructor_exists():
    assert callable(sparqlas::SymmetricObjectProperty.__init__)


def test_sparqlas::symmetricobjectproperty_constructor_args():
    sig = inspect.signature(sparqlas::SymmetricObjectProperty.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::equivalentobjectproperties_is_not_abstract():
    assert not inspect.isabstract(sparqlas::EquivalentObjectProperties)


def test_sparqlas::equivalentobjectproperties_constructor_exists():
    assert callable(sparqlas::EquivalentObjectProperties.__init__)


def test_sparqlas::equivalentobjectproperties_constructor_args():
    sig = inspect.signature(sparqlas::EquivalentObjectProperties.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::irreflexiveobjectproperty_is_not_abstract():
    assert not inspect.isabstract(sparqlas::IrreflexiveObjectProperty)


def test_sparqlas::irreflexiveobjectproperty_constructor_exists():
    assert callable(sparqlas::IrreflexiveObjectProperty.__init__)


def test_sparqlas::irreflexiveobjectproperty_constructor_args():
    sig = inspect.signature(sparqlas::IrreflexiveObjectProperty.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::objectpropertyrange_is_not_abstract():
    assert not inspect.isabstract(sparqlas::ObjectPropertyRange)


def test_sparqlas::objectpropertyrange_constructor_exists():
    assert callable(sparqlas::ObjectPropertyRange.__init__)


def test_sparqlas::objectpropertyrange_constructor_args():
    sig = inspect.signature(sparqlas::ObjectPropertyRange.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::transitiveobjectproperty_is_not_abstract():
    assert not inspect.isabstract(sparqlas::TransitiveObjectProperty)


def test_sparqlas::transitiveobjectproperty_constructor_exists():
    assert callable(sparqlas::TransitiveObjectProperty.__init__)


def test_sparqlas::transitiveobjectproperty_constructor_args():
    sig = inspect.signature(sparqlas::TransitiveObjectProperty.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::inverseobjectpropertyatom_is_not_abstract():
    assert not inspect.isabstract(sparqlas::InverseObjectPropertyAtom)


def test_sparqlas::inverseobjectpropertyatom_constructor_exists():
    assert callable(sparqlas::InverseObjectPropertyAtom.__init__)


def test_sparqlas::inverseobjectpropertyatom_constructor_args():
    sig = inspect.signature(sparqlas::InverseObjectPropertyAtom.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::asymmetricobjectproperty_is_not_abstract():
    assert not inspect.isabstract(sparqlas::AsymmetricObjectProperty)


def test_sparqlas::asymmetricobjectproperty_constructor_exists():
    assert callable(sparqlas::AsymmetricObjectProperty.__init__)


def test_sparqlas::asymmetricobjectproperty_constructor_args():
    sig = inspect.signature(sparqlas::AsymmetricObjectProperty.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::reflexiveobjectproperty_is_not_abstract():
    assert not inspect.isabstract(sparqlas::ReflexiveObjectProperty)


def test_sparqlas::reflexiveobjectproperty_constructor_exists():
    assert callable(sparqlas::ReflexiveObjectProperty.__init__)


def test_sparqlas::reflexiveobjectproperty_constructor_args():
    sig = inspect.signature(sparqlas::ReflexiveObjectProperty.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::inversefunctionalobjectproperty_is_not_abstract():
    assert not inspect.isabstract(sparqlas::InverseFunctionalObjectProperty)


def test_sparqlas::inversefunctionalobjectproperty_constructor_exists():
    assert callable(sparqlas::InverseFunctionalObjectProperty.__init__)


def test_sparqlas::inversefunctionalobjectproperty_constructor_args():
    sig = inspect.signature(sparqlas::InverseFunctionalObjectProperty.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::functionalobjectproperty_is_not_abstract():
    assert not inspect.isabstract(sparqlas::FunctionalObjectProperty)


def test_sparqlas::functionalobjectproperty_constructor_exists():
    assert callable(sparqlas::FunctionalObjectProperty.__init__)


def test_sparqlas::functionalobjectproperty_constructor_args():
    sig = inspect.signature(sparqlas::FunctionalObjectProperty.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::objectpropertydomain_is_not_abstract():
    assert not inspect.isabstract(sparqlas::ObjectPropertyDomain)


def test_sparqlas::objectpropertydomain_constructor_exists():
    assert callable(sparqlas::ObjectPropertyDomain.__init__)


def test_sparqlas::objectpropertydomain_constructor_args():
    sig = inspect.signature(sparqlas::ObjectPropertyDomain.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::disjointobjectproperties_is_not_abstract():
    assert not inspect.isabstract(sparqlas::DisjointObjectProperties)


def test_sparqlas::disjointobjectproperties_constructor_exists():
    assert callable(sparqlas::DisjointObjectProperties.__init__)


def test_sparqlas::disjointobjectproperties_constructor_args():
    sig = inspect.signature(sparqlas::DisjointObjectProperties.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::facetrestriction_is_not_abstract():
    assert not inspect.isabstract(sparqlas::FacetRestriction)


def test_sparqlas::facetrestriction_constructor_exists():
    assert callable(sparqlas::FacetRestriction.__init__)


def test_sparqlas::facetrestriction_constructor_args():
    sig = inspect.signature(sparqlas::FacetRestriction.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::subobjectpropertyof_is_not_abstract():
    assert not inspect.isabstract(sparqlas::SubObjectPropertyOf)


def test_sparqlas::subobjectpropertyof_constructor_exists():
    assert callable(sparqlas::SubObjectPropertyOf.__init__)


def test_sparqlas::subobjectpropertyof_constructor_args():
    sig = inspect.signature(sparqlas::SubObjectPropertyOf.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::datarange_is_not_abstract():
    assert not inspect.isabstract(sparqlas::DataRange)


def test_sparqlas::datarange_constructor_exists():
    assert callable(sparqlas::DataRange.__init__)


def test_sparqlas::datarange_constructor_args():
    sig = inspect.signature(sparqlas::DataRange.__init__)
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



def test_sparqlas::strictsubclassof_is_not_abstract():
    assert not inspect.isabstract(sparqlas::StrictSubClassOf)


def test_sparqlas::strictsubclassof_constructor_exists():
    assert callable(sparqlas::StrictSubClassOf.__init__)


def test_sparqlas::strictsubclassof_constructor_args():
    sig = inspect.signature(sparqlas::StrictSubClassOf.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::directsubclassof_is_not_abstract():
    assert not inspect.isabstract(sparqlas::DirectSubClassOf)


def test_sparqlas::directsubclassof_constructor_exists():
    assert callable(sparqlas::DirectSubClassOf.__init__)


def test_sparqlas::directsubclassof_constructor_args():
    sig = inspect.signature(sparqlas::DirectSubClassOf.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::disjointunion_is_not_abstract():
    assert not inspect.isabstract(sparqlas::DisjointUnion)


def test_sparqlas::disjointunion_constructor_exists():
    assert callable(sparqlas::DisjointUnion.__init__)


def test_sparqlas::disjointunion_constructor_args():
    sig = inspect.signature(sparqlas::DisjointUnion.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::equivalentclasses_is_not_abstract():
    assert not inspect.isabstract(sparqlas::EquivalentClasses)


def test_sparqlas::equivalentclasses_constructor_exists():
    assert callable(sparqlas::EquivalentClasses.__init__)


def test_sparqlas::equivalentclasses_constructor_args():
    sig = inspect.signature(sparqlas::EquivalentClasses.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::subclassof_is_not_abstract():
    assert not inspect.isabstract(sparqlas::SubClassOf)


def test_sparqlas::subclassof_constructor_exists():
    assert callable(sparqlas::SubClassOf.__init__)


def test_sparqlas::subclassof_constructor_args():
    sig = inspect.signature(sparqlas::SubClassOf.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::disjointclasses_is_not_abstract():
    assert not inspect.isabstract(sparqlas::DisjointClasses)


def test_sparqlas::disjointclasses_constructor_exists():
    assert callable(sparqlas::DisjointClasses.__init__)


def test_sparqlas::disjointclasses_constructor_args():
    sig = inspect.signature(sparqlas::DisjointClasses.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::datapropertyexpression_is_not_abstract():
    assert not inspect.isabstract(sparqlas::DataPropertyExpression)


def test_sparqlas::datapropertyexpression_constructor_exists():
    assert callable(sparqlas::DataPropertyExpression.__init__)


def test_sparqlas::datapropertyexpression_constructor_args():
    sig = inspect.signature(sparqlas::DataPropertyExpression.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::classexpression_is_not_abstract():
    assert not inspect.isabstract(sparqlas::ClassExpression)


def test_sparqlas::classexpression_constructor_exists():
    assert callable(sparqlas::ClassExpression.__init__)


def test_sparqlas::classexpression_constructor_args():
    sig = inspect.signature(sparqlas::ClassExpression.__init__)
    params = list(sig.parameters.keys())



def test_assertion_is_not_abstract():
    assert not inspect.isabstract(Assertion)


def test_assertion_constructor_exists():
    assert callable(Assertion.__init__)


def test_assertion_constructor_args():
    sig = inspect.signature(Assertion.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::datapropertyassertion_is_not_abstract():
    assert not inspect.isabstract(sparqlas::DataPropertyAssertion)


def test_sparqlas::datapropertyassertion_constructor_exists():
    assert callable(sparqlas::DataPropertyAssertion.__init__)


def test_sparqlas::datapropertyassertion_constructor_args():
    sig = inspect.signature(sparqlas::DataPropertyAssertion.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::negativedatapropertyassertion_is_not_abstract():
    assert not inspect.isabstract(sparqlas::NegativeDataPropertyAssertion)


def test_sparqlas::negativedatapropertyassertion_constructor_exists():
    assert callable(sparqlas::NegativeDataPropertyAssertion.__init__)


def test_sparqlas::negativedatapropertyassertion_constructor_args():
    sig = inspect.signature(sparqlas::NegativeDataPropertyAssertion.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::sameindividual_is_not_abstract():
    assert not inspect.isabstract(sparqlas::SameIndividual)


def test_sparqlas::sameindividual_constructor_exists():
    assert callable(sparqlas::SameIndividual.__init__)


def test_sparqlas::sameindividual_constructor_args():
    sig = inspect.signature(sparqlas::SameIndividual.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::directclassassertion_is_not_abstract():
    assert not inspect.isabstract(sparqlas::DirectClassAssertion)


def test_sparqlas::directclassassertion_constructor_exists():
    assert callable(sparqlas::DirectClassAssertion.__init__)


def test_sparqlas::directclassassertion_constructor_args():
    sig = inspect.signature(sparqlas::DirectClassAssertion.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::negativeobjectpropertyassertion_is_not_abstract():
    assert not inspect.isabstract(sparqlas::NegativeObjectPropertyAssertion)


def test_sparqlas::negativeobjectpropertyassertion_constructor_exists():
    assert callable(sparqlas::NegativeObjectPropertyAssertion.__init__)


def test_sparqlas::negativeobjectpropertyassertion_constructor_args():
    sig = inspect.signature(sparqlas::NegativeObjectPropertyAssertion.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::differentindividuals_is_not_abstract():
    assert not inspect.isabstract(sparqlas::DifferentIndividuals)


def test_sparqlas::differentindividuals_constructor_exists():
    assert callable(sparqlas::DifferentIndividuals.__init__)


def test_sparqlas::differentindividuals_constructor_args():
    sig = inspect.signature(sparqlas::DifferentIndividuals.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::classassertion_is_not_abstract():
    assert not inspect.isabstract(sparqlas::ClassAssertion)


def test_sparqlas::classassertion_constructor_exists():
    assert callable(sparqlas::ClassAssertion.__init__)


def test_sparqlas::classassertion_constructor_args():
    sig = inspect.signature(sparqlas::ClassAssertion.__init__)
    params = list(sig.parameters.keys())



def test_atom_is_not_abstract():
    assert not inspect.isabstract(Atom)


def test_atom_constructor_exists():
    assert callable(Atom.__init__)


def test_atom_constructor_args():
    sig = inspect.signature(Atom.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::haskey_is_not_abstract():
    assert not inspect.isabstract(sparqlas::HasKey)


def test_sparqlas::haskey_constructor_exists():
    assert callable(sparqlas::HasKey.__init__)


def test_sparqlas::haskey_constructor_args():
    sig = inspect.signature(sparqlas::HasKey.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::classatom_is_not_abstract():
    assert not inspect.isabstract(sparqlas::ClassAtom)


def test_sparqlas::classatom_constructor_exists():
    assert callable(sparqlas::ClassAtom.__init__)


def test_sparqlas::classatom_constructor_args():
    sig = inspect.signature(sparqlas::ClassAtom.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::declaration_is_not_abstract():
    assert not inspect.isabstract(sparqlas::Declaration)


def test_sparqlas::declaration_constructor_exists():
    assert callable(sparqlas::Declaration.__init__)


def test_sparqlas::declaration_constructor_args():
    sig = inspect.signature(sparqlas::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::objectpropertyatom_is_not_abstract():
    assert not inspect.isabstract(sparqlas::ObjectPropertyAtom)


def test_sparqlas::objectpropertyatom_constructor_exists():
    assert callable(sparqlas::ObjectPropertyAtom.__init__)


def test_sparqlas::objectpropertyatom_constructor_args():
    sig = inspect.signature(sparqlas::ObjectPropertyAtom.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::datapropertyatom_is_not_abstract():
    assert not inspect.isabstract(sparqlas::DataPropertyAtom)


def test_sparqlas::datapropertyatom_constructor_exists():
    assert callable(sparqlas::DataPropertyAtom.__init__)


def test_sparqlas::datapropertyatom_constructor_args():
    sig = inspect.signature(sparqlas::DataPropertyAtom.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::assertion_is_not_abstract():
    assert not inspect.isabstract(sparqlas::Assertion)


def test_sparqlas::assertion_constructor_exists():
    assert callable(sparqlas::Assertion.__init__)


def test_sparqlas::assertion_constructor_args():
    sig = inspect.signature(sparqlas::Assertion.__init__)
    params = list(sig.parameters.keys())



def test_parameterableelement_is_not_abstract():
    assert not inspect.isabstract(ParameterableElement)


def test_parameterableelement_constructor_exists():
    assert callable(ParameterableElement.__init__)


def test_parameterableelement_constructor_args():
    sig = inspect.signature(ParameterableElement.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::expression_is_not_abstract():
    assert not inspect.isabstract(sparqlas::Expression)


def test_sparqlas::expression_constructor_exists():
    assert callable(sparqlas::Expression.__init__)


def test_sparqlas::expression_constructor_args():
    sig = inspect.signature(sparqlas::Expression.__init__)
    params = list(sig.parameters.keys())



def test_abstractliteral_is_not_abstract():
    assert not inspect.isabstract(AbstractLiteral)


def test_abstractliteral_constructor_exists():
    assert callable(AbstractLiteral.__init__)


def test_abstractliteral_constructor_args():
    sig = inspect.signature(AbstractLiteral.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::literal_is_not_abstract():
    assert not inspect.isabstract(sparqlas::Literal)


def test_sparqlas::literal_constructor_exists():
    assert callable(sparqlas::Literal.__init__)


def test_sparqlas::literal_constructor_args():
    sig = inspect.signature(sparqlas::Literal.__init__)
    params = list(sig.parameters.keys())
    assert "lexicalForm" in params, "Missing parameter 'lexicalForm'"

def test_sparqlas::literal_has_lexicalForm():
    assert hasattr(sparqlas::Literal, "lexicalForm")
    descriptor = None
    for klass in sparqlas::Literal.__mro__:
        if "lexicalForm" in klass.__dict__:
            descriptor = klass.__dict__["lexicalForm"]
            break
    assert isinstance(descriptor, property)



def test_sparqlas::abstractliteral_is_not_abstract():
    assert not inspect.isabstract(sparqlas::AbstractLiteral)


def test_sparqlas::abstractliteral_constructor_exists():
    assert callable(sparqlas::AbstractLiteral.__init__)


def test_sparqlas::abstractliteral_constructor_args():
    sig = inspect.signature(sparqlas::AbstractLiteral.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::individual_is_not_abstract():
    assert not inspect.isabstract(sparqlas::Individual)


def test_sparqlas::individual_constructor_exists():
    assert callable(sparqlas::Individual.__init__)


def test_sparqlas::individual_constructor_args():
    sig = inspect.signature(sparqlas::Individual.__init__)
    params = list(sig.parameters.keys())



def test_datarange_is_not_abstract():
    assert not inspect.isabstract(DataRange)


def test_datarange_constructor_exists():
    assert callable(DataRange.__init__)


def test_datarange_constructor_args():
    sig = inspect.signature(DataRange.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::datatyperestriction_is_not_abstract():
    assert not inspect.isabstract(sparqlas::DatatypeRestriction)


def test_sparqlas::datatyperestriction_constructor_exists():
    assert callable(sparqlas::DatatypeRestriction.__init__)


def test_sparqlas::datatyperestriction_constructor_args():
    sig = inspect.signature(sparqlas::DatatypeRestriction.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::dataoneof_is_not_abstract():
    assert not inspect.isabstract(sparqlas::DataOneOf)


def test_sparqlas::dataoneof_constructor_exists():
    assert callable(sparqlas::DataOneOf.__init__)


def test_sparqlas::dataoneof_constructor_args():
    sig = inspect.signature(sparqlas::DataOneOf.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::datacomplementof_is_not_abstract():
    assert not inspect.isabstract(sparqlas::DataComplementOf)


def test_sparqlas::datacomplementof_constructor_exists():
    assert callable(sparqlas::DataComplementOf.__init__)


def test_sparqlas::datacomplementof_constructor_args():
    sig = inspect.signature(sparqlas::DataComplementOf.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::dataintersectionof_is_not_abstract():
    assert not inspect.isabstract(sparqlas::DataIntersectionOf)


def test_sparqlas::dataintersectionof_constructor_exists():
    assert callable(sparqlas::DataIntersectionOf.__init__)


def test_sparqlas::dataintersectionof_constructor_args():
    sig = inspect.signature(sparqlas::DataIntersectionOf.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::dataunionof_is_not_abstract():
    assert not inspect.isabstract(sparqlas::DataUnionOf)


def test_sparqlas::dataunionof_constructor_exists():
    assert callable(sparqlas::DataUnionOf.__init__)


def test_sparqlas::dataunionof_constructor_args():
    sig = inspect.signature(sparqlas::DataUnionOf.__init__)
    params = list(sig.parameters.keys())



def test_constant_is_not_abstract():
    assert not inspect.isabstract(Constant)


def test_constant_constructor_exists():
    assert callable(Constant.__init__)


def test_constant_constructor_args():
    sig = inspect.signature(Constant.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::datatype_is_not_abstract():
    assert not inspect.isabstract(sparqlas::Datatype)


def test_sparqlas::datatype_constructor_exists():
    assert callable(sparqlas::Datatype.__init__)


def test_sparqlas::datatype_constructor_args():
    sig = inspect.signature(sparqlas::Datatype.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::objectpropertyexpression_is_not_abstract():
    assert not inspect.isabstract(sparqlas::ObjectPropertyExpression)


def test_sparqlas::objectpropertyexpression_constructor_exists():
    assert callable(sparqlas::ObjectPropertyExpression.__init__)


def test_sparqlas::objectpropertyexpression_constructor_args():
    sig = inspect.signature(sparqlas::ObjectPropertyExpression.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::objectpropertyassertion_is_not_abstract():
    assert not inspect.isabstract(sparqlas::ObjectPropertyAssertion)


def test_sparqlas::objectpropertyassertion_constructor_exists():
    assert callable(sparqlas::ObjectPropertyAssertion.__init__)


def test_sparqlas::objectpropertyassertion_constructor_args():
    sig = inspect.signature(sparqlas::ObjectPropertyAssertion.__init__)
    params = list(sig.parameters.keys())



def test_datapropertyexpression_is_not_abstract():
    assert not inspect.isabstract(DataPropertyExpression)


def test_datapropertyexpression_constructor_exists():
    assert callable(DataPropertyExpression.__init__)


def test_datapropertyexpression_constructor_args():
    sig = inspect.signature(DataPropertyExpression.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::dataproperty_is_not_abstract():
    assert not inspect.isabstract(sparqlas::DataProperty)


def test_sparqlas::dataproperty_constructor_exists():
    assert callable(sparqlas::DataProperty.__init__)


def test_sparqlas::dataproperty_constructor_args():
    sig = inspect.signature(sparqlas::DataProperty.__init__)
    params = list(sig.parameters.keys())



def test_objectpropertyexpression_is_not_abstract():
    assert not inspect.isabstract(ObjectPropertyExpression)


def test_objectpropertyexpression_constructor_exists():
    assert callable(ObjectPropertyExpression.__init__)


def test_objectpropertyexpression_constructor_args():
    sig = inspect.signature(ObjectPropertyExpression.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::objectproperty_is_not_abstract():
    assert not inspect.isabstract(sparqlas::ObjectProperty)


def test_sparqlas::objectproperty_constructor_exists():
    assert callable(sparqlas::ObjectProperty.__init__)


def test_sparqlas::objectproperty_constructor_args():
    sig = inspect.signature(sparqlas::ObjectProperty.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::inverseobjectproperty_is_not_abstract():
    assert not inspect.isabstract(sparqlas::InverseObjectProperty)


def test_sparqlas::inverseobjectproperty_constructor_exists():
    assert callable(sparqlas::InverseObjectProperty.__init__)


def test_sparqlas::inverseobjectproperty_constructor_args():
    sig = inspect.signature(sparqlas::InverseObjectProperty.__init__)
    params = list(sig.parameters.keys())



def test_classexpression_is_not_abstract():
    assert not inspect.isabstract(ClassExpression)


def test_classexpression_constructor_exists():
    assert callable(ClassExpression.__init__)


def test_classexpression_constructor_args():
    sig = inspect.signature(ClassExpression.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::objectallvaluesfrom_is_not_abstract():
    assert not inspect.isabstract(sparqlas::ObjectAllValuesFrom)


def test_sparqlas::objectallvaluesfrom_constructor_exists():
    assert callable(sparqlas::ObjectAllValuesFrom.__init__)


def test_sparqlas::objectallvaluesfrom_constructor_args():
    sig = inspect.signature(sparqlas::ObjectAllValuesFrom.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::objectunionof_is_not_abstract():
    assert not inspect.isabstract(sparqlas::ObjectUnionOf)


def test_sparqlas::objectunionof_constructor_exists():
    assert callable(sparqlas::ObjectUnionOf.__init__)


def test_sparqlas::objectunionof_constructor_args():
    sig = inspect.signature(sparqlas::ObjectUnionOf.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::objectexactcardinality_is_not_abstract():
    assert not inspect.isabstract(sparqlas::ObjectExactCardinality)


def test_sparqlas::objectexactcardinality_constructor_exists():
    assert callable(sparqlas::ObjectExactCardinality.__init__)


def test_sparqlas::objectexactcardinality_constructor_args():
    sig = inspect.signature(sparqlas::ObjectExactCardinality.__init__)
    params = list(sig.parameters.keys())
    assert "cardinality" in params, "Missing parameter 'cardinality'"

def test_sparqlas::objectexactcardinality_has_cardinality():
    assert hasattr(sparqlas::ObjectExactCardinality, "cardinality")
    descriptor = None
    for klass in sparqlas::ObjectExactCardinality.__mro__:
        if "cardinality" in klass.__dict__:
            descriptor = klass.__dict__["cardinality"]
            break
    assert isinstance(descriptor, property)



def test_sparqlas::objecthasvalue_is_not_abstract():
    assert not inspect.isabstract(sparqlas::ObjectHasValue)


def test_sparqlas::objecthasvalue_constructor_exists():
    assert callable(sparqlas::ObjectHasValue.__init__)


def test_sparqlas::objecthasvalue_constructor_args():
    sig = inspect.signature(sparqlas::ObjectHasValue.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::objectmincardinality_is_not_abstract():
    assert not inspect.isabstract(sparqlas::ObjectMinCardinality)


def test_sparqlas::objectmincardinality_constructor_exists():
    assert callable(sparqlas::ObjectMinCardinality.__init__)


def test_sparqlas::objectmincardinality_constructor_args():
    sig = inspect.signature(sparqlas::ObjectMinCardinality.__init__)
    params = list(sig.parameters.keys())
    assert "cardinality" in params, "Missing parameter 'cardinality'"

def test_sparqlas::objectmincardinality_has_cardinality():
    assert hasattr(sparqlas::ObjectMinCardinality, "cardinality")
    descriptor = None
    for klass in sparqlas::ObjectMinCardinality.__mro__:
        if "cardinality" in klass.__dict__:
            descriptor = klass.__dict__["cardinality"]
            break
    assert isinstance(descriptor, property)



def test_sparqlas::objectoneof_is_not_abstract():
    assert not inspect.isabstract(sparqlas::ObjectOneOf)


def test_sparqlas::objectoneof_constructor_exists():
    assert callable(sparqlas::ObjectOneOf.__init__)


def test_sparqlas::objectoneof_constructor_args():
    sig = inspect.signature(sparqlas::ObjectOneOf.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::datahasvalue_is_not_abstract():
    assert not inspect.isabstract(sparqlas::DataHasValue)


def test_sparqlas::datahasvalue_constructor_exists():
    assert callable(sparqlas::DataHasValue.__init__)


def test_sparqlas::datahasvalue_constructor_args():
    sig = inspect.signature(sparqlas::DataHasValue.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::dataallvaluesfrom_is_not_abstract():
    assert not inspect.isabstract(sparqlas::DataAllValuesFrom)


def test_sparqlas::dataallvaluesfrom_constructor_exists():
    assert callable(sparqlas::DataAllValuesFrom.__init__)


def test_sparqlas::dataallvaluesfrom_constructor_args():
    sig = inspect.signature(sparqlas::DataAllValuesFrom.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::objectintersectionof_is_not_abstract():
    assert not inspect.isabstract(sparqlas::ObjectIntersectionOf)


def test_sparqlas::objectintersectionof_constructor_exists():
    assert callable(sparqlas::ObjectIntersectionOf.__init__)


def test_sparqlas::objectintersectionof_constructor_args():
    sig = inspect.signature(sparqlas::ObjectIntersectionOf.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::dataexactcardinality_is_not_abstract():
    assert not inspect.isabstract(sparqlas::DataExactCardinality)


def test_sparqlas::dataexactcardinality_constructor_exists():
    assert callable(sparqlas::DataExactCardinality.__init__)


def test_sparqlas::dataexactcardinality_constructor_args():
    sig = inspect.signature(sparqlas::DataExactCardinality.__init__)
    params = list(sig.parameters.keys())
    assert "cardinality" in params, "Missing parameter 'cardinality'"

def test_sparqlas::dataexactcardinality_has_cardinality():
    assert hasattr(sparqlas::DataExactCardinality, "cardinality")
    descriptor = None
    for klass in sparqlas::DataExactCardinality.__mro__:
        if "cardinality" in klass.__dict__:
            descriptor = klass.__dict__["cardinality"]
            break
    assert isinstance(descriptor, property)



def test_sparqlas::datasomevaluesfrom_is_not_abstract():
    assert not inspect.isabstract(sparqlas::DataSomeValuesFrom)


def test_sparqlas::datasomevaluesfrom_constructor_exists():
    assert callable(sparqlas::DataSomeValuesFrom.__init__)


def test_sparqlas::datasomevaluesfrom_constructor_args():
    sig = inspect.signature(sparqlas::DataSomeValuesFrom.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::datamaxcardinality_is_not_abstract():
    assert not inspect.isabstract(sparqlas::DataMaxCardinality)


def test_sparqlas::datamaxcardinality_constructor_exists():
    assert callable(sparqlas::DataMaxCardinality.__init__)


def test_sparqlas::datamaxcardinality_constructor_args():
    sig = inspect.signature(sparqlas::DataMaxCardinality.__init__)
    params = list(sig.parameters.keys())
    assert "cardinality" in params, "Missing parameter 'cardinality'"

def test_sparqlas::datamaxcardinality_has_cardinality():
    assert hasattr(sparqlas::DataMaxCardinality, "cardinality")
    descriptor = None
    for klass in sparqlas::DataMaxCardinality.__mro__:
        if "cardinality" in klass.__dict__:
            descriptor = klass.__dict__["cardinality"]
            break
    assert isinstance(descriptor, property)



def test_sparqlas::objectcomplementof_is_not_abstract():
    assert not inspect.isabstract(sparqlas::ObjectComplementOf)


def test_sparqlas::objectcomplementof_constructor_exists():
    assert callable(sparqlas::ObjectComplementOf.__init__)


def test_sparqlas::objectcomplementof_constructor_args():
    sig = inspect.signature(sparqlas::ObjectComplementOf.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::objectmaxcardinality_is_not_abstract():
    assert not inspect.isabstract(sparqlas::ObjectMaxCardinality)


def test_sparqlas::objectmaxcardinality_constructor_exists():
    assert callable(sparqlas::ObjectMaxCardinality.__init__)


def test_sparqlas::objectmaxcardinality_constructor_args():
    sig = inspect.signature(sparqlas::ObjectMaxCardinality.__init__)
    params = list(sig.parameters.keys())
    assert "cardinality" in params, "Missing parameter 'cardinality'"

def test_sparqlas::objectmaxcardinality_has_cardinality():
    assert hasattr(sparqlas::ObjectMaxCardinality, "cardinality")
    descriptor = None
    for klass in sparqlas::ObjectMaxCardinality.__mro__:
        if "cardinality" in klass.__dict__:
            descriptor = klass.__dict__["cardinality"]
            break
    assert isinstance(descriptor, property)



def test_sparqlas::datamincardinality_is_not_abstract():
    assert not inspect.isabstract(sparqlas::DataMinCardinality)


def test_sparqlas::datamincardinality_constructor_exists():
    assert callable(sparqlas::DataMinCardinality.__init__)


def test_sparqlas::datamincardinality_constructor_args():
    sig = inspect.signature(sparqlas::DataMinCardinality.__init__)
    params = list(sig.parameters.keys())
    assert "cardinality" in params, "Missing parameter 'cardinality'"

def test_sparqlas::datamincardinality_has_cardinality():
    assert hasattr(sparqlas::DataMinCardinality, "cardinality")
    descriptor = None
    for klass in sparqlas::DataMinCardinality.__mro__:
        if "cardinality" in klass.__dict__:
            descriptor = klass.__dict__["cardinality"]
            break
    assert isinstance(descriptor, property)



def test_sparqlas::objectsomevaluesfrom_is_not_abstract():
    assert not inspect.isabstract(sparqlas::ObjectSomeValuesFrom)


def test_sparqlas::objectsomevaluesfrom_constructor_exists():
    assert callable(sparqlas::ObjectSomeValuesFrom.__init__)


def test_sparqlas::objectsomevaluesfrom_constructor_args():
    sig = inspect.signature(sparqlas::ObjectSomeValuesFrom.__init__)
    params = list(sig.parameters.keys())



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::objectpropertyvariable_is_not_abstract():
    assert not inspect.isabstract(sparqlas::ObjectPropertyVariable)


def test_sparqlas::objectpropertyvariable_constructor_exists():
    assert callable(sparqlas::ObjectPropertyVariable.__init__)


def test_sparqlas::objectpropertyvariable_constructor_args():
    sig = inspect.signature(sparqlas::ObjectPropertyVariable.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::literalvariable_is_not_abstract():
    assert not inspect.isabstract(sparqlas::LiteralVariable)


def test_sparqlas::literalvariable_constructor_exists():
    assert callable(sparqlas::LiteralVariable.__init__)


def test_sparqlas::literalvariable_constructor_args():
    sig = inspect.signature(sparqlas::LiteralVariable.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::datapropertyvariable_is_not_abstract():
    assert not inspect.isabstract(sparqlas::DataPropertyVariable)


def test_sparqlas::datapropertyvariable_constructor_exists():
    assert callable(sparqlas::DataPropertyVariable.__init__)


def test_sparqlas::datapropertyvariable_constructor_args():
    sig = inspect.signature(sparqlas::DataPropertyVariable.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::classvariable_is_not_abstract():
    assert not inspect.isabstract(sparqlas::ClassVariable)


def test_sparqlas::classvariable_constructor_exists():
    assert callable(sparqlas::ClassVariable.__init__)


def test_sparqlas::classvariable_constructor_args():
    sig = inspect.signature(sparqlas::ClassVariable.__init__)
    params = list(sig.parameters.keys())



def test_term_is_not_abstract():
    assert not inspect.isabstract(Term)


def test_term_constructor_exists():
    assert callable(Term.__init__)


def test_term_constructor_args():
    sig = inspect.signature(Term.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::term_is_not_abstract():
    assert not inspect.isabstract(sparqlas::Term)


def test_sparqlas::term_constructor_exists():
    assert callable(sparqlas::Term.__init__)


def test_sparqlas::term_constructor_args():
    sig = inspect.signature(sparqlas::Term.__init__)
    params = list(sig.parameters.keys())



def test_iri_is_not_abstract():
    assert not inspect.isabstract(IRI)


def test_iri_constructor_exists():
    assert callable(IRI.__init__)


def test_iri_constructor_args():
    sig = inspect.signature(IRI.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::abbreviatediri_is_not_abstract():
    assert not inspect.isabstract(sparqlas::AbbreviatedIRI)


def test_sparqlas::abbreviatediri_constructor_exists():
    assert callable(sparqlas::AbbreviatedIRI.__init__)


def test_sparqlas::abbreviatediri_constructor_args():
    sig = inspect.signature(sparqlas::AbbreviatedIRI.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::class_is_not_abstract():
    assert not inspect.isabstract(sparqlas::Class)


def test_sparqlas::class_constructor_exists():
    assert callable(sparqlas::Class.__init__)


def test_sparqlas::class_constructor_args():
    sig = inspect.signature(sparqlas::Class.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::constant_is_not_abstract():
    assert not inspect.isabstract(sparqlas::Constant)


def test_sparqlas::constant_constructor_exists():
    assert callable(sparqlas::Constant.__init__)


def test_sparqlas::constant_constructor_args():
    sig = inspect.signature(sparqlas::Constant.__init__)
    params = list(sig.parameters.keys())



def test_individual_is_not_abstract():
    assert not inspect.isabstract(Individual)


def test_individual_constructor_exists():
    assert callable(Individual.__init__)


def test_individual_constructor_args():
    sig = inspect.signature(Individual.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::namedindividual_is_not_abstract():
    assert not inspect.isabstract(sparqlas::NamedIndividual)


def test_sparqlas::namedindividual_constructor_exists():
    assert callable(sparqlas::NamedIndividual.__init__)


def test_sparqlas::namedindividual_constructor_args():
    sig = inspect.signature(sparqlas::NamedIndividual.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::anonymousindividual_is_not_abstract():
    assert not inspect.isabstract(sparqlas::AnonymousIndividual)


def test_sparqlas::anonymousindividual_constructor_exists():
    assert callable(sparqlas::AnonymousIndividual.__init__)


def test_sparqlas::anonymousindividual_constructor_args():
    sig = inspect.signature(sparqlas::AnonymousIndividual.__init__)
    params = list(sig.parameters.keys())
    assert "nodeID" in params, "Missing parameter 'nodeID'"

def test_sparqlas::anonymousindividual_has_nodeID():
    assert hasattr(sparqlas::AnonymousIndividual, "nodeID")
    descriptor = None
    for klass in sparqlas::AnonymousIndividual.__mro__:
        if "nodeID" in klass.__dict__:
            descriptor = klass.__dict__["nodeID"]
            break
    assert isinstance(descriptor, property)



def test_sparqlas::individualvariable_is_not_abstract():
    assert not inspect.isabstract(sparqlas::IndividualVariable)


def test_sparqlas::individualvariable_constructor_exists():
    assert callable(sparqlas::IndividualVariable.__init__)


def test_sparqlas::individualvariable_constructor_args():
    sig = inspect.signature(sparqlas::IndividualVariable.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::variable_is_not_abstract():
    assert not inspect.isabstract(sparqlas::Variable)


def test_sparqlas::variable_constructor_exists():
    assert callable(sparqlas::Variable.__init__)


def test_sparqlas::variable_constructor_args():
    sig = inspect.signature(sparqlas::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_sparqlas::variable_has_symbol():
    assert hasattr(sparqlas::Variable, "symbol")
    descriptor = None
    for klass in sparqlas::Variable.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)



def test_sparqlas::atom_is_not_abstract():
    assert not inspect.isabstract(sparqlas::Atom)


def test_sparqlas::atom_constructor_exists():
    assert callable(sparqlas::Atom.__init__)


def test_sparqlas::atom_constructor_args():
    sig = inspect.signature(sparqlas::Atom.__init__)
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



def test_sparqlas::constructquery_is_not_abstract():
    assert not inspect.isabstract(sparqlas::ConstructQuery)


def test_sparqlas::constructquery_constructor_exists():
    assert callable(sparqlas::ConstructQuery.__init__)


def test_sparqlas::constructquery_constructor_args():
    sig = inspect.signature(sparqlas::ConstructQuery.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::selectquery_is_not_abstract():
    assert not inspect.isabstract(sparqlas::SelectQuery)


def test_sparqlas::selectquery_constructor_exists():
    assert callable(sparqlas::SelectQuery.__init__)


def test_sparqlas::selectquery_constructor_args():
    sig = inspect.signature(sparqlas::SelectQuery.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::fulliri_is_not_abstract():
    assert not inspect.isabstract(sparqlas::FullIRI)


def test_sparqlas::fulliri_constructor_exists():
    assert callable(sparqlas::FullIRI.__init__)


def test_sparqlas::fulliri_constructor_args():
    sig = inspect.signature(sparqlas::FullIRI.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::describequery_is_not_abstract():
    assert not inspect.isabstract(sparqlas::DescribeQuery)


def test_sparqlas::describequery_constructor_exists():
    assert callable(sparqlas::DescribeQuery.__init__)


def test_sparqlas::describequery_constructor_args():
    sig = inspect.signature(sparqlas::DescribeQuery.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::askquery_is_not_abstract():
    assert not inspect.isabstract(sparqlas::AskQuery)


def test_sparqlas::askquery_constructor_exists():
    assert callable(sparqlas::AskQuery.__init__)


def test_sparqlas::askquery_constructor_args():
    sig = inspect.signature(sparqlas::AskQuery.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::import_is_not_abstract():
    assert not inspect.isabstract(sparqlas::Import)


def test_sparqlas::import_constructor_exists():
    assert callable(sparqlas::Import.__init__)


def test_sparqlas::import_constructor_args():
    sig = inspect.signature(sparqlas::Import.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::iri_is_not_abstract():
    assert not inspect.isabstract(sparqlas::IRI)


def test_sparqlas::iri_constructor_exists():
    assert callable(sparqlas::IRI.__init__)


def test_sparqlas::iri_constructor_args():
    sig = inspect.signature(sparqlas::IRI.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_sparqlas::iri_has_id():
    assert hasattr(sparqlas::IRI, "id")
    descriptor = None
    for klass in sparqlas::IRI.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_sparqlas::ontologydocument_is_not_abstract():
    assert not inspect.isabstract(sparqlas::OntologyDocument)


def test_sparqlas::ontologydocument_constructor_exists():
    assert callable(sparqlas::OntologyDocument.__init__)


def test_sparqlas::ontologydocument_constructor_args():
    sig = inspect.signature(sparqlas::OntologyDocument.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::query_is_not_abstract():
    assert not inspect.isabstract(sparqlas::Query)


def test_sparqlas::query_constructor_exists():
    assert callable(sparqlas::Query.__init__)


def test_sparqlas::query_constructor_args():
    sig = inspect.signature(sparqlas::Query.__init__)
    params = list(sig.parameters.keys())



def test_sparqlas::prefixdefinition_is_not_abstract():
    assert not inspect.isabstract(sparqlas::PrefixDefinition)


def test_sparqlas::prefixdefinition_constructor_exists():
    assert callable(sparqlas::PrefixDefinition.__init__)


def test_sparqlas::prefixdefinition_constructor_args():
    sig = inspect.signature(sparqlas::PrefixDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "pref" in params, "Missing parameter 'pref'"

def test_sparqlas::prefixdefinition_has_pref():
    assert hasattr(sparqlas::PrefixDefinition, "pref")
    descriptor = None
    for klass in sparqlas::PrefixDefinition.__mro__:
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
sparqlas::TemplateBinding_strategy = st.builds(
    sparqlas::TemplateBinding,
)
sparqlas::TemplateableElement_strategy = st.builds(
    sparqlas::TemplateableElement,
)
sparqlas::TemplateParameterSubstitution_strategy = st.builds(
    sparqlas::TemplateParameterSubstitution,
)
sparqlas::TemplateSignature_strategy = st.builds(
    sparqlas::TemplateSignature,
)
sparqlas::TemplateParameter_strategy = st.builds(
    sparqlas::TemplateParameter,
)
sparqlas::ParameterableElement_strategy = st.builds(
    sparqlas::ParameterableElement,
)
Declaration_strategy = st.builds(
    Declaration,
)
sparqlas::DatatypePropertyDeclaration_strategy = st.builds(
    sparqlas::DatatypePropertyDeclaration,
)
sparqlas::ObjectPropertyDeclaration_strategy = st.builds(
    sparqlas::ObjectPropertyDeclaration,
)
sparqlas::ClassDeclaration_strategy = st.builds(
    sparqlas::ClassDeclaration,
)
sparqlas::IndividualDeclaration_strategy = st.builds(
    sparqlas::IndividualDeclaration,
)
DataPropertyAtom_strategy = st.builds(
    DataPropertyAtom,
)
sparqlas::DisjointDataProperties_strategy = st.builds(
    sparqlas::DisjointDataProperties,
)
sparqlas::FunctionalDataProperty_strategy = st.builds(
    sparqlas::FunctionalDataProperty,
)
sparqlas::DataPropertyDomain_strategy = st.builds(
    sparqlas::DataPropertyDomain,
)
sparqlas::DataPropertyRange_strategy = st.builds(
    sparqlas::DataPropertyRange,
)
sparqlas::EquivalentDataProperties_strategy = st.builds(
    sparqlas::EquivalentDataProperties,
)
sparqlas::SubDataPropertyOf_strategy = st.builds(
    sparqlas::SubDataPropertyOf,
)
sparqlas::ObjectPropertyChain_strategy = st.builds(
    sparqlas::ObjectPropertyChain,
)
ObjectPropertyAtom_strategy = st.builds(
    ObjectPropertyAtom,
)
sparqlas::SymmetricObjectProperty_strategy = st.builds(
    sparqlas::SymmetricObjectProperty,
)
sparqlas::EquivalentObjectProperties_strategy = st.builds(
    sparqlas::EquivalentObjectProperties,
)
sparqlas::IrreflexiveObjectProperty_strategy = st.builds(
    sparqlas::IrreflexiveObjectProperty,
)
sparqlas::ObjectPropertyRange_strategy = st.builds(
    sparqlas::ObjectPropertyRange,
)
sparqlas::TransitiveObjectProperty_strategy = st.builds(
    sparqlas::TransitiveObjectProperty,
)
sparqlas::InverseObjectPropertyAtom_strategy = st.builds(
    sparqlas::InverseObjectPropertyAtom,
)
sparqlas::AsymmetricObjectProperty_strategy = st.builds(
    sparqlas::AsymmetricObjectProperty,
)
sparqlas::ReflexiveObjectProperty_strategy = st.builds(
    sparqlas::ReflexiveObjectProperty,
)
sparqlas::InverseFunctionalObjectProperty_strategy = st.builds(
    sparqlas::InverseFunctionalObjectProperty,
)
sparqlas::FunctionalObjectProperty_strategy = st.builds(
    sparqlas::FunctionalObjectProperty,
)
sparqlas::ObjectPropertyDomain_strategy = st.builds(
    sparqlas::ObjectPropertyDomain,
)
sparqlas::DisjointObjectProperties_strategy = st.builds(
    sparqlas::DisjointObjectProperties,
)
sparqlas::FacetRestriction_strategy = st.builds(
    sparqlas::FacetRestriction,
)
sparqlas::SubObjectPropertyOf_strategy = st.builds(
    sparqlas::SubObjectPropertyOf,
)
sparqlas::DataRange_strategy = st.builds(
    sparqlas::DataRange,
)
Expression_strategy = st.builds(
    Expression,
)
ClassAtom_strategy = st.builds(
    ClassAtom,
)
sparqlas::StrictSubClassOf_strategy = st.builds(
    sparqlas::StrictSubClassOf,
)
sparqlas::DirectSubClassOf_strategy = st.builds(
    sparqlas::DirectSubClassOf,
)
sparqlas::DisjointUnion_strategy = st.builds(
    sparqlas::DisjointUnion,
)
sparqlas::EquivalentClasses_strategy = st.builds(
    sparqlas::EquivalentClasses,
)
sparqlas::SubClassOf_strategy = st.builds(
    sparqlas::SubClassOf,
)
sparqlas::DisjointClasses_strategy = st.builds(
    sparqlas::DisjointClasses,
)
sparqlas::DataPropertyExpression_strategy = st.builds(
    sparqlas::DataPropertyExpression,
)
sparqlas::ClassExpression_strategy = st.builds(
    sparqlas::ClassExpression,
)
Assertion_strategy = st.builds(
    Assertion,
)
sparqlas::DataPropertyAssertion_strategy = st.builds(
    sparqlas::DataPropertyAssertion,
)
sparqlas::NegativeDataPropertyAssertion_strategy = st.builds(
    sparqlas::NegativeDataPropertyAssertion,
)
sparqlas::SameIndividual_strategy = st.builds(
    sparqlas::SameIndividual,
)
sparqlas::DirectClassAssertion_strategy = st.builds(
    sparqlas::DirectClassAssertion,
)
sparqlas::NegativeObjectPropertyAssertion_strategy = st.builds(
    sparqlas::NegativeObjectPropertyAssertion,
)
sparqlas::DifferentIndividuals_strategy = st.builds(
    sparqlas::DifferentIndividuals,
)
sparqlas::ClassAssertion_strategy = st.builds(
    sparqlas::ClassAssertion,
)
Atom_strategy = st.builds(
    Atom,
)
sparqlas::HasKey_strategy = st.builds(
    sparqlas::HasKey,
)
sparqlas::ClassAtom_strategy = st.builds(
    sparqlas::ClassAtom,
)
sparqlas::Declaration_strategy = st.builds(
    sparqlas::Declaration,
)
sparqlas::ObjectPropertyAtom_strategy = st.builds(
    sparqlas::ObjectPropertyAtom,
)
sparqlas::DataPropertyAtom_strategy = st.builds(
    sparqlas::DataPropertyAtom,
)
sparqlas::Assertion_strategy = st.builds(
    sparqlas::Assertion,
)
ParameterableElement_strategy = st.builds(
    ParameterableElement,
)
sparqlas::Expression_strategy = st.builds(
    sparqlas::Expression,
)
AbstractLiteral_strategy = st.builds(
    AbstractLiteral,
)
sparqlas::Literal_strategy = st.builds(
    sparqlas::Literal,
    lexicalForm=
        safe_text
)
sparqlas::AbstractLiteral_strategy = st.builds(
    sparqlas::AbstractLiteral,
)
sparqlas::Individual_strategy = st.builds(
    sparqlas::Individual,
)
DataRange_strategy = st.builds(
    DataRange,
)
sparqlas::DatatypeRestriction_strategy = st.builds(
    sparqlas::DatatypeRestriction,
)
sparqlas::DataOneOf_strategy = st.builds(
    sparqlas::DataOneOf,
)
sparqlas::DataComplementOf_strategy = st.builds(
    sparqlas::DataComplementOf,
)
sparqlas::DataIntersectionOf_strategy = st.builds(
    sparqlas::DataIntersectionOf,
)
sparqlas::DataUnionOf_strategy = st.builds(
    sparqlas::DataUnionOf,
)
Constant_strategy = st.builds(
    Constant,
)
sparqlas::Datatype_strategy = st.builds(
    sparqlas::Datatype,
)
sparqlas::ObjectPropertyExpression_strategy = st.builds(
    sparqlas::ObjectPropertyExpression,
)
sparqlas::ObjectPropertyAssertion_strategy = st.builds(
    sparqlas::ObjectPropertyAssertion,
)
DataPropertyExpression_strategy = st.builds(
    DataPropertyExpression,
)
sparqlas::DataProperty_strategy = st.builds(
    sparqlas::DataProperty,
)
ObjectPropertyExpression_strategy = st.builds(
    ObjectPropertyExpression,
)
sparqlas::ObjectProperty_strategy = st.builds(
    sparqlas::ObjectProperty,
)
sparqlas::InverseObjectProperty_strategy = st.builds(
    sparqlas::InverseObjectProperty,
)
ClassExpression_strategy = st.builds(
    ClassExpression,
)
sparqlas::ObjectAllValuesFrom_strategy = st.builds(
    sparqlas::ObjectAllValuesFrom,
)
sparqlas::ObjectUnionOf_strategy = st.builds(
    sparqlas::ObjectUnionOf,
)
sparqlas::ObjectExactCardinality_strategy = st.builds(
    sparqlas::ObjectExactCardinality,
    cardinality=
        st.integers()
)
sparqlas::ObjectHasValue_strategy = st.builds(
    sparqlas::ObjectHasValue,
)
sparqlas::ObjectMinCardinality_strategy = st.builds(
    sparqlas::ObjectMinCardinality,
    cardinality=
        st.integers()
)
sparqlas::ObjectOneOf_strategy = st.builds(
    sparqlas::ObjectOneOf,
)
sparqlas::DataHasValue_strategy = st.builds(
    sparqlas::DataHasValue,
)
sparqlas::DataAllValuesFrom_strategy = st.builds(
    sparqlas::DataAllValuesFrom,
)
sparqlas::ObjectIntersectionOf_strategy = st.builds(
    sparqlas::ObjectIntersectionOf,
)
sparqlas::DataExactCardinality_strategy = st.builds(
    sparqlas::DataExactCardinality,
    cardinality=
        st.integers()
)
sparqlas::DataSomeValuesFrom_strategy = st.builds(
    sparqlas::DataSomeValuesFrom,
)
sparqlas::DataMaxCardinality_strategy = st.builds(
    sparqlas::DataMaxCardinality,
    cardinality=
        st.integers()
)
sparqlas::ObjectComplementOf_strategy = st.builds(
    sparqlas::ObjectComplementOf,
)
sparqlas::ObjectMaxCardinality_strategy = st.builds(
    sparqlas::ObjectMaxCardinality,
    cardinality=
        st.integers()
)
sparqlas::DataMinCardinality_strategy = st.builds(
    sparqlas::DataMinCardinality,
    cardinality=
        st.integers()
)
sparqlas::ObjectSomeValuesFrom_strategy = st.builds(
    sparqlas::ObjectSomeValuesFrom,
)
Variable_strategy = st.builds(
    Variable,
)
sparqlas::ObjectPropertyVariable_strategy = st.builds(
    sparqlas::ObjectPropertyVariable,
)
sparqlas::LiteralVariable_strategy = st.builds(
    sparqlas::LiteralVariable,
)
sparqlas::DataPropertyVariable_strategy = st.builds(
    sparqlas::DataPropertyVariable,
)
sparqlas::ClassVariable_strategy = st.builds(
    sparqlas::ClassVariable,
)
Term_strategy = st.builds(
    Term,
)
sparqlas::Term_strategy = st.builds(
    sparqlas::Term,
)
IRI_strategy = st.builds(
    IRI,
)
sparqlas::AbbreviatedIRI_strategy = st.builds(
    sparqlas::AbbreviatedIRI,
)
sparqlas::Class_strategy = st.builds(
    sparqlas::Class,
)
sparqlas::Constant_strategy = st.builds(
    sparqlas::Constant,
)
Individual_strategy = st.builds(
    Individual,
)
sparqlas::NamedIndividual_strategy = st.builds(
    sparqlas::NamedIndividual,
)
sparqlas::AnonymousIndividual_strategy = st.builds(
    sparqlas::AnonymousIndividual,
    nodeID=
        safe_text
)
sparqlas::IndividualVariable_strategy = st.builds(
    sparqlas::IndividualVariable,
)
sparqlas::Variable_strategy = st.builds(
    sparqlas::Variable,
    symbol=
        safe_text
)
sparqlas::Atom_strategy = st.builds(
    sparqlas::Atom,
)
TemplateableElement_strategy = st.builds(
    TemplateableElement,
)
Query_strategy = st.builds(
    Query,
)
sparqlas::ConstructQuery_strategy = st.builds(
    sparqlas::ConstructQuery,
)
sparqlas::SelectQuery_strategy = st.builds(
    sparqlas::SelectQuery,
)
sparqlas::FullIRI_strategy = st.builds(
    sparqlas::FullIRI,
)
sparqlas::DescribeQuery_strategy = st.builds(
    sparqlas::DescribeQuery,
)
sparqlas::AskQuery_strategy = st.builds(
    sparqlas::AskQuery,
)
sparqlas::Import_strategy = st.builds(
    sparqlas::Import,
)
sparqlas::IRI_strategy = st.builds(
    sparqlas::IRI,
    id=
        safe_text
)
sparqlas::OntologyDocument_strategy = st.builds(
    sparqlas::OntologyDocument,
)
sparqlas::Query_strategy = st.builds(
    sparqlas::Query,
)
sparqlas::PrefixDefinition_strategy = st.builds(
    sparqlas::PrefixDefinition,
    pref=
        safe_text
)

@given(instance=sparqlas::TemplateBinding_strategy)
@settings(max_examples=50)
def test_sparqlas::templatebinding_instantiation(instance):
    assert isinstance(instance, sparqlas::TemplateBinding)

@given(instance=sparqlas::TemplateableElement_strategy)
@settings(max_examples=50)
def test_sparqlas::templateableelement_instantiation(instance):
    assert isinstance(instance, sparqlas::TemplateableElement)

@given(instance=sparqlas::TemplateParameterSubstitution_strategy)
@settings(max_examples=50)
def test_sparqlas::templateparametersubstitution_instantiation(instance):
    assert isinstance(instance, sparqlas::TemplateParameterSubstitution)

@given(instance=sparqlas::TemplateSignature_strategy)
@settings(max_examples=50)
def test_sparqlas::templatesignature_instantiation(instance):
    assert isinstance(instance, sparqlas::TemplateSignature)

@given(instance=sparqlas::TemplateParameter_strategy)
@settings(max_examples=50)
def test_sparqlas::templateparameter_instantiation(instance):
    assert isinstance(instance, sparqlas::TemplateParameter)

@given(instance=sparqlas::ParameterableElement_strategy)
@settings(max_examples=50)
def test_sparqlas::parameterableelement_instantiation(instance):
    assert isinstance(instance, sparqlas::ParameterableElement)

@given(instance=Declaration_strategy)
@settings(max_examples=50)
def test_declaration_instantiation(instance):
    assert isinstance(instance, Declaration)

@given(instance=sparqlas::DatatypePropertyDeclaration_strategy)
@settings(max_examples=50)
def test_sparqlas::datatypepropertydeclaration_instantiation(instance):
    assert isinstance(instance, sparqlas::DatatypePropertyDeclaration)

@given(instance=sparqlas::ObjectPropertyDeclaration_strategy)
@settings(max_examples=50)
def test_sparqlas::objectpropertydeclaration_instantiation(instance):
    assert isinstance(instance, sparqlas::ObjectPropertyDeclaration)

@given(instance=sparqlas::ClassDeclaration_strategy)
@settings(max_examples=50)
def test_sparqlas::classdeclaration_instantiation(instance):
    assert isinstance(instance, sparqlas::ClassDeclaration)

@given(instance=sparqlas::IndividualDeclaration_strategy)
@settings(max_examples=50)
def test_sparqlas::individualdeclaration_instantiation(instance):
    assert isinstance(instance, sparqlas::IndividualDeclaration)

@given(instance=DataPropertyAtom_strategy)
@settings(max_examples=50)
def test_datapropertyatom_instantiation(instance):
    assert isinstance(instance, DataPropertyAtom)

@given(instance=sparqlas::DisjointDataProperties_strategy)
@settings(max_examples=50)
def test_sparqlas::disjointdataproperties_instantiation(instance):
    assert isinstance(instance, sparqlas::DisjointDataProperties)

@given(instance=sparqlas::FunctionalDataProperty_strategy)
@settings(max_examples=50)
def test_sparqlas::functionaldataproperty_instantiation(instance):
    assert isinstance(instance, sparqlas::FunctionalDataProperty)

@given(instance=sparqlas::DataPropertyDomain_strategy)
@settings(max_examples=50)
def test_sparqlas::datapropertydomain_instantiation(instance):
    assert isinstance(instance, sparqlas::DataPropertyDomain)

@given(instance=sparqlas::DataPropertyRange_strategy)
@settings(max_examples=50)
def test_sparqlas::datapropertyrange_instantiation(instance):
    assert isinstance(instance, sparqlas::DataPropertyRange)

@given(instance=sparqlas::EquivalentDataProperties_strategy)
@settings(max_examples=50)
def test_sparqlas::equivalentdataproperties_instantiation(instance):
    assert isinstance(instance, sparqlas::EquivalentDataProperties)

@given(instance=sparqlas::SubDataPropertyOf_strategy)
@settings(max_examples=50)
def test_sparqlas::subdatapropertyof_instantiation(instance):
    assert isinstance(instance, sparqlas::SubDataPropertyOf)

@given(instance=sparqlas::ObjectPropertyChain_strategy)
@settings(max_examples=50)
def test_sparqlas::objectpropertychain_instantiation(instance):
    assert isinstance(instance, sparqlas::ObjectPropertyChain)

@given(instance=ObjectPropertyAtom_strategy)
@settings(max_examples=50)
def test_objectpropertyatom_instantiation(instance):
    assert isinstance(instance, ObjectPropertyAtom)

@given(instance=sparqlas::SymmetricObjectProperty_strategy)
@settings(max_examples=50)
def test_sparqlas::symmetricobjectproperty_instantiation(instance):
    assert isinstance(instance, sparqlas::SymmetricObjectProperty)

@given(instance=sparqlas::EquivalentObjectProperties_strategy)
@settings(max_examples=50)
def test_sparqlas::equivalentobjectproperties_instantiation(instance):
    assert isinstance(instance, sparqlas::EquivalentObjectProperties)

@given(instance=sparqlas::IrreflexiveObjectProperty_strategy)
@settings(max_examples=50)
def test_sparqlas::irreflexiveobjectproperty_instantiation(instance):
    assert isinstance(instance, sparqlas::IrreflexiveObjectProperty)

@given(instance=sparqlas::ObjectPropertyRange_strategy)
@settings(max_examples=50)
def test_sparqlas::objectpropertyrange_instantiation(instance):
    assert isinstance(instance, sparqlas::ObjectPropertyRange)

@given(instance=sparqlas::TransitiveObjectProperty_strategy)
@settings(max_examples=50)
def test_sparqlas::transitiveobjectproperty_instantiation(instance):
    assert isinstance(instance, sparqlas::TransitiveObjectProperty)

@given(instance=sparqlas::InverseObjectPropertyAtom_strategy)
@settings(max_examples=50)
def test_sparqlas::inverseobjectpropertyatom_instantiation(instance):
    assert isinstance(instance, sparqlas::InverseObjectPropertyAtom)

@given(instance=sparqlas::AsymmetricObjectProperty_strategy)
@settings(max_examples=50)
def test_sparqlas::asymmetricobjectproperty_instantiation(instance):
    assert isinstance(instance, sparqlas::AsymmetricObjectProperty)

@given(instance=sparqlas::ReflexiveObjectProperty_strategy)
@settings(max_examples=50)
def test_sparqlas::reflexiveobjectproperty_instantiation(instance):
    assert isinstance(instance, sparqlas::ReflexiveObjectProperty)

@given(instance=sparqlas::InverseFunctionalObjectProperty_strategy)
@settings(max_examples=50)
def test_sparqlas::inversefunctionalobjectproperty_instantiation(instance):
    assert isinstance(instance, sparqlas::InverseFunctionalObjectProperty)

@given(instance=sparqlas::FunctionalObjectProperty_strategy)
@settings(max_examples=50)
def test_sparqlas::functionalobjectproperty_instantiation(instance):
    assert isinstance(instance, sparqlas::FunctionalObjectProperty)

@given(instance=sparqlas::ObjectPropertyDomain_strategy)
@settings(max_examples=50)
def test_sparqlas::objectpropertydomain_instantiation(instance):
    assert isinstance(instance, sparqlas::ObjectPropertyDomain)

@given(instance=sparqlas::DisjointObjectProperties_strategy)
@settings(max_examples=50)
def test_sparqlas::disjointobjectproperties_instantiation(instance):
    assert isinstance(instance, sparqlas::DisjointObjectProperties)

@given(instance=sparqlas::FacetRestriction_strategy)
@settings(max_examples=50)
def test_sparqlas::facetrestriction_instantiation(instance):
    assert isinstance(instance, sparqlas::FacetRestriction)

@given(instance=sparqlas::SubObjectPropertyOf_strategy)
@settings(max_examples=50)
def test_sparqlas::subobjectpropertyof_instantiation(instance):
    assert isinstance(instance, sparqlas::SubObjectPropertyOf)

@given(instance=sparqlas::DataRange_strategy)
@settings(max_examples=50)
def test_sparqlas::datarange_instantiation(instance):
    assert isinstance(instance, sparqlas::DataRange)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=ClassAtom_strategy)
@settings(max_examples=50)
def test_classatom_instantiation(instance):
    assert isinstance(instance, ClassAtom)

@given(instance=sparqlas::StrictSubClassOf_strategy)
@settings(max_examples=50)
def test_sparqlas::strictsubclassof_instantiation(instance):
    assert isinstance(instance, sparqlas::StrictSubClassOf)

@given(instance=sparqlas::DirectSubClassOf_strategy)
@settings(max_examples=50)
def test_sparqlas::directsubclassof_instantiation(instance):
    assert isinstance(instance, sparqlas::DirectSubClassOf)

@given(instance=sparqlas::DisjointUnion_strategy)
@settings(max_examples=50)
def test_sparqlas::disjointunion_instantiation(instance):
    assert isinstance(instance, sparqlas::DisjointUnion)

@given(instance=sparqlas::EquivalentClasses_strategy)
@settings(max_examples=50)
def test_sparqlas::equivalentclasses_instantiation(instance):
    assert isinstance(instance, sparqlas::EquivalentClasses)

@given(instance=sparqlas::SubClassOf_strategy)
@settings(max_examples=50)
def test_sparqlas::subclassof_instantiation(instance):
    assert isinstance(instance, sparqlas::SubClassOf)

@given(instance=sparqlas::DisjointClasses_strategy)
@settings(max_examples=50)
def test_sparqlas::disjointclasses_instantiation(instance):
    assert isinstance(instance, sparqlas::DisjointClasses)

@given(instance=sparqlas::DataPropertyExpression_strategy)
@settings(max_examples=50)
def test_sparqlas::datapropertyexpression_instantiation(instance):
    assert isinstance(instance, sparqlas::DataPropertyExpression)

@given(instance=sparqlas::ClassExpression_strategy)
@settings(max_examples=50)
def test_sparqlas::classexpression_instantiation(instance):
    assert isinstance(instance, sparqlas::ClassExpression)

@given(instance=Assertion_strategy)
@settings(max_examples=50)
def test_assertion_instantiation(instance):
    assert isinstance(instance, Assertion)

@given(instance=sparqlas::DataPropertyAssertion_strategy)
@settings(max_examples=50)
def test_sparqlas::datapropertyassertion_instantiation(instance):
    assert isinstance(instance, sparqlas::DataPropertyAssertion)

@given(instance=sparqlas::NegativeDataPropertyAssertion_strategy)
@settings(max_examples=50)
def test_sparqlas::negativedatapropertyassertion_instantiation(instance):
    assert isinstance(instance, sparqlas::NegativeDataPropertyAssertion)

@given(instance=sparqlas::SameIndividual_strategy)
@settings(max_examples=50)
def test_sparqlas::sameindividual_instantiation(instance):
    assert isinstance(instance, sparqlas::SameIndividual)

@given(instance=sparqlas::DirectClassAssertion_strategy)
@settings(max_examples=50)
def test_sparqlas::directclassassertion_instantiation(instance):
    assert isinstance(instance, sparqlas::DirectClassAssertion)

@given(instance=sparqlas::NegativeObjectPropertyAssertion_strategy)
@settings(max_examples=50)
def test_sparqlas::negativeobjectpropertyassertion_instantiation(instance):
    assert isinstance(instance, sparqlas::NegativeObjectPropertyAssertion)

@given(instance=sparqlas::DifferentIndividuals_strategy)
@settings(max_examples=50)
def test_sparqlas::differentindividuals_instantiation(instance):
    assert isinstance(instance, sparqlas::DifferentIndividuals)

@given(instance=sparqlas::ClassAssertion_strategy)
@settings(max_examples=50)
def test_sparqlas::classassertion_instantiation(instance):
    assert isinstance(instance, sparqlas::ClassAssertion)

@given(instance=Atom_strategy)
@settings(max_examples=50)
def test_atom_instantiation(instance):
    assert isinstance(instance, Atom)

@given(instance=sparqlas::HasKey_strategy)
@settings(max_examples=50)
def test_sparqlas::haskey_instantiation(instance):
    assert isinstance(instance, sparqlas::HasKey)

@given(instance=sparqlas::ClassAtom_strategy)
@settings(max_examples=50)
def test_sparqlas::classatom_instantiation(instance):
    assert isinstance(instance, sparqlas::ClassAtom)

@given(instance=sparqlas::Declaration_strategy)
@settings(max_examples=50)
def test_sparqlas::declaration_instantiation(instance):
    assert isinstance(instance, sparqlas::Declaration)

@given(instance=sparqlas::ObjectPropertyAtom_strategy)
@settings(max_examples=50)
def test_sparqlas::objectpropertyatom_instantiation(instance):
    assert isinstance(instance, sparqlas::ObjectPropertyAtom)

@given(instance=sparqlas::DataPropertyAtom_strategy)
@settings(max_examples=50)
def test_sparqlas::datapropertyatom_instantiation(instance):
    assert isinstance(instance, sparqlas::DataPropertyAtom)

@given(instance=sparqlas::Assertion_strategy)
@settings(max_examples=50)
def test_sparqlas::assertion_instantiation(instance):
    assert isinstance(instance, sparqlas::Assertion)

@given(instance=ParameterableElement_strategy)
@settings(max_examples=50)
def test_parameterableelement_instantiation(instance):
    assert isinstance(instance, ParameterableElement)

@given(instance=sparqlas::Expression_strategy)
@settings(max_examples=50)
def test_sparqlas::expression_instantiation(instance):
    assert isinstance(instance, sparqlas::Expression)

@given(instance=AbstractLiteral_strategy)
@settings(max_examples=50)
def test_abstractliteral_instantiation(instance):
    assert isinstance(instance, AbstractLiteral)

@given(instance=sparqlas::Literal_strategy)
@settings(max_examples=50)
def test_sparqlas::literal_instantiation(instance):
    assert isinstance(instance, sparqlas::Literal)

@given(instance=sparqlas::Literal_strategy)
def test_sparqlas::literal_lexicalForm_type(instance):
    assert isinstance(instance.lexicalForm, str)


@given(instance=sparqlas::Literal_strategy)
def test_sparqlas::literal_lexicalForm_setter(instance):
    original = instance.lexicalForm
    instance.lexicalForm = original
    assert instance.lexicalForm == original

@given(instance=sparqlas::AbstractLiteral_strategy)
@settings(max_examples=50)
def test_sparqlas::abstractliteral_instantiation(instance):
    assert isinstance(instance, sparqlas::AbstractLiteral)

@given(instance=sparqlas::Individual_strategy)
@settings(max_examples=50)
def test_sparqlas::individual_instantiation(instance):
    assert isinstance(instance, sparqlas::Individual)

@given(instance=DataRange_strategy)
@settings(max_examples=50)
def test_datarange_instantiation(instance):
    assert isinstance(instance, DataRange)

@given(instance=sparqlas::DatatypeRestriction_strategy)
@settings(max_examples=50)
def test_sparqlas::datatyperestriction_instantiation(instance):
    assert isinstance(instance, sparqlas::DatatypeRestriction)

@given(instance=sparqlas::DataOneOf_strategy)
@settings(max_examples=50)
def test_sparqlas::dataoneof_instantiation(instance):
    assert isinstance(instance, sparqlas::DataOneOf)

@given(instance=sparqlas::DataComplementOf_strategy)
@settings(max_examples=50)
def test_sparqlas::datacomplementof_instantiation(instance):
    assert isinstance(instance, sparqlas::DataComplementOf)

@given(instance=sparqlas::DataIntersectionOf_strategy)
@settings(max_examples=50)
def test_sparqlas::dataintersectionof_instantiation(instance):
    assert isinstance(instance, sparqlas::DataIntersectionOf)

@given(instance=sparqlas::DataUnionOf_strategy)
@settings(max_examples=50)
def test_sparqlas::dataunionof_instantiation(instance):
    assert isinstance(instance, sparqlas::DataUnionOf)

@given(instance=Constant_strategy)
@settings(max_examples=50)
def test_constant_instantiation(instance):
    assert isinstance(instance, Constant)

@given(instance=sparqlas::Datatype_strategy)
@settings(max_examples=50)
def test_sparqlas::datatype_instantiation(instance):
    assert isinstance(instance, sparqlas::Datatype)

@given(instance=sparqlas::ObjectPropertyExpression_strategy)
@settings(max_examples=50)
def test_sparqlas::objectpropertyexpression_instantiation(instance):
    assert isinstance(instance, sparqlas::ObjectPropertyExpression)

@given(instance=sparqlas::ObjectPropertyAssertion_strategy)
@settings(max_examples=50)
def test_sparqlas::objectpropertyassertion_instantiation(instance):
    assert isinstance(instance, sparqlas::ObjectPropertyAssertion)

@given(instance=DataPropertyExpression_strategy)
@settings(max_examples=50)
def test_datapropertyexpression_instantiation(instance):
    assert isinstance(instance, DataPropertyExpression)

@given(instance=sparqlas::DataProperty_strategy)
@settings(max_examples=50)
def test_sparqlas::dataproperty_instantiation(instance):
    assert isinstance(instance, sparqlas::DataProperty)

@given(instance=ObjectPropertyExpression_strategy)
@settings(max_examples=50)
def test_objectpropertyexpression_instantiation(instance):
    assert isinstance(instance, ObjectPropertyExpression)

@given(instance=sparqlas::ObjectProperty_strategy)
@settings(max_examples=50)
def test_sparqlas::objectproperty_instantiation(instance):
    assert isinstance(instance, sparqlas::ObjectProperty)

@given(instance=sparqlas::InverseObjectProperty_strategy)
@settings(max_examples=50)
def test_sparqlas::inverseobjectproperty_instantiation(instance):
    assert isinstance(instance, sparqlas::InverseObjectProperty)

@given(instance=ClassExpression_strategy)
@settings(max_examples=50)
def test_classexpression_instantiation(instance):
    assert isinstance(instance, ClassExpression)

@given(instance=sparqlas::ObjectAllValuesFrom_strategy)
@settings(max_examples=50)
def test_sparqlas::objectallvaluesfrom_instantiation(instance):
    assert isinstance(instance, sparqlas::ObjectAllValuesFrom)

@given(instance=sparqlas::ObjectUnionOf_strategy)
@settings(max_examples=50)
def test_sparqlas::objectunionof_instantiation(instance):
    assert isinstance(instance, sparqlas::ObjectUnionOf)

@given(instance=sparqlas::ObjectExactCardinality_strategy)
@settings(max_examples=50)
def test_sparqlas::objectexactcardinality_instantiation(instance):
    assert isinstance(instance, sparqlas::ObjectExactCardinality)

@given(instance=sparqlas::ObjectExactCardinality_strategy)
def test_sparqlas::objectexactcardinality_cardinality_type(instance):
    assert isinstance(instance.cardinality, int)


@given(instance=sparqlas::ObjectExactCardinality_strategy)
def test_sparqlas::objectexactcardinality_cardinality_setter(instance):
    original = instance.cardinality
    instance.cardinality = original
    assert instance.cardinality == original

@given(instance=sparqlas::ObjectHasValue_strategy)
@settings(max_examples=50)
def test_sparqlas::objecthasvalue_instantiation(instance):
    assert isinstance(instance, sparqlas::ObjectHasValue)

@given(instance=sparqlas::ObjectMinCardinality_strategy)
@settings(max_examples=50)
def test_sparqlas::objectmincardinality_instantiation(instance):
    assert isinstance(instance, sparqlas::ObjectMinCardinality)

@given(instance=sparqlas::ObjectMinCardinality_strategy)
def test_sparqlas::objectmincardinality_cardinality_type(instance):
    assert isinstance(instance.cardinality, int)


@given(instance=sparqlas::ObjectMinCardinality_strategy)
def test_sparqlas::objectmincardinality_cardinality_setter(instance):
    original = instance.cardinality
    instance.cardinality = original
    assert instance.cardinality == original

@given(instance=sparqlas::ObjectOneOf_strategy)
@settings(max_examples=50)
def test_sparqlas::objectoneof_instantiation(instance):
    assert isinstance(instance, sparqlas::ObjectOneOf)

@given(instance=sparqlas::DataHasValue_strategy)
@settings(max_examples=50)
def test_sparqlas::datahasvalue_instantiation(instance):
    assert isinstance(instance, sparqlas::DataHasValue)

@given(instance=sparqlas::DataAllValuesFrom_strategy)
@settings(max_examples=50)
def test_sparqlas::dataallvaluesfrom_instantiation(instance):
    assert isinstance(instance, sparqlas::DataAllValuesFrom)

@given(instance=sparqlas::ObjectIntersectionOf_strategy)
@settings(max_examples=50)
def test_sparqlas::objectintersectionof_instantiation(instance):
    assert isinstance(instance, sparqlas::ObjectIntersectionOf)

@given(instance=sparqlas::DataExactCardinality_strategy)
@settings(max_examples=50)
def test_sparqlas::dataexactcardinality_instantiation(instance):
    assert isinstance(instance, sparqlas::DataExactCardinality)

@given(instance=sparqlas::DataExactCardinality_strategy)
def test_sparqlas::dataexactcardinality_cardinality_type(instance):
    assert isinstance(instance.cardinality, int)


@given(instance=sparqlas::DataExactCardinality_strategy)
def test_sparqlas::dataexactcardinality_cardinality_setter(instance):
    original = instance.cardinality
    instance.cardinality = original
    assert instance.cardinality == original

@given(instance=sparqlas::DataSomeValuesFrom_strategy)
@settings(max_examples=50)
def test_sparqlas::datasomevaluesfrom_instantiation(instance):
    assert isinstance(instance, sparqlas::DataSomeValuesFrom)

@given(instance=sparqlas::DataMaxCardinality_strategy)
@settings(max_examples=50)
def test_sparqlas::datamaxcardinality_instantiation(instance):
    assert isinstance(instance, sparqlas::DataMaxCardinality)

@given(instance=sparqlas::DataMaxCardinality_strategy)
def test_sparqlas::datamaxcardinality_cardinality_type(instance):
    assert isinstance(instance.cardinality, int)


@given(instance=sparqlas::DataMaxCardinality_strategy)
def test_sparqlas::datamaxcardinality_cardinality_setter(instance):
    original = instance.cardinality
    instance.cardinality = original
    assert instance.cardinality == original

@given(instance=sparqlas::ObjectComplementOf_strategy)
@settings(max_examples=50)
def test_sparqlas::objectcomplementof_instantiation(instance):
    assert isinstance(instance, sparqlas::ObjectComplementOf)

@given(instance=sparqlas::ObjectMaxCardinality_strategy)
@settings(max_examples=50)
def test_sparqlas::objectmaxcardinality_instantiation(instance):
    assert isinstance(instance, sparqlas::ObjectMaxCardinality)

@given(instance=sparqlas::ObjectMaxCardinality_strategy)
def test_sparqlas::objectmaxcardinality_cardinality_type(instance):
    assert isinstance(instance.cardinality, int)


@given(instance=sparqlas::ObjectMaxCardinality_strategy)
def test_sparqlas::objectmaxcardinality_cardinality_setter(instance):
    original = instance.cardinality
    instance.cardinality = original
    assert instance.cardinality == original

@given(instance=sparqlas::DataMinCardinality_strategy)
@settings(max_examples=50)
def test_sparqlas::datamincardinality_instantiation(instance):
    assert isinstance(instance, sparqlas::DataMinCardinality)

@given(instance=sparqlas::DataMinCardinality_strategy)
def test_sparqlas::datamincardinality_cardinality_type(instance):
    assert isinstance(instance.cardinality, int)


@given(instance=sparqlas::DataMinCardinality_strategy)
def test_sparqlas::datamincardinality_cardinality_setter(instance):
    original = instance.cardinality
    instance.cardinality = original
    assert instance.cardinality == original

@given(instance=sparqlas::ObjectSomeValuesFrom_strategy)
@settings(max_examples=50)
def test_sparqlas::objectsomevaluesfrom_instantiation(instance):
    assert isinstance(instance, sparqlas::ObjectSomeValuesFrom)

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=sparqlas::ObjectPropertyVariable_strategy)
@settings(max_examples=50)
def test_sparqlas::objectpropertyvariable_instantiation(instance):
    assert isinstance(instance, sparqlas::ObjectPropertyVariable)

@given(instance=sparqlas::LiteralVariable_strategy)
@settings(max_examples=50)
def test_sparqlas::literalvariable_instantiation(instance):
    assert isinstance(instance, sparqlas::LiteralVariable)

@given(instance=sparqlas::DataPropertyVariable_strategy)
@settings(max_examples=50)
def test_sparqlas::datapropertyvariable_instantiation(instance):
    assert isinstance(instance, sparqlas::DataPropertyVariable)

@given(instance=sparqlas::ClassVariable_strategy)
@settings(max_examples=50)
def test_sparqlas::classvariable_instantiation(instance):
    assert isinstance(instance, sparqlas::ClassVariable)

@given(instance=Term_strategy)
@settings(max_examples=50)
def test_term_instantiation(instance):
    assert isinstance(instance, Term)

@given(instance=sparqlas::Term_strategy)
@settings(max_examples=50)
def test_sparqlas::term_instantiation(instance):
    assert isinstance(instance, sparqlas::Term)

@given(instance=IRI_strategy)
@settings(max_examples=50)
def test_iri_instantiation(instance):
    assert isinstance(instance, IRI)

@given(instance=sparqlas::AbbreviatedIRI_strategy)
@settings(max_examples=50)
def test_sparqlas::abbreviatediri_instantiation(instance):
    assert isinstance(instance, sparqlas::AbbreviatedIRI)

@given(instance=sparqlas::Class_strategy)
@settings(max_examples=50)
def test_sparqlas::class_instantiation(instance):
    assert isinstance(instance, sparqlas::Class)

@given(instance=sparqlas::Constant_strategy)
@settings(max_examples=50)
def test_sparqlas::constant_instantiation(instance):
    assert isinstance(instance, sparqlas::Constant)

@given(instance=Individual_strategy)
@settings(max_examples=50)
def test_individual_instantiation(instance):
    assert isinstance(instance, Individual)

@given(instance=sparqlas::NamedIndividual_strategy)
@settings(max_examples=50)
def test_sparqlas::namedindividual_instantiation(instance):
    assert isinstance(instance, sparqlas::NamedIndividual)

@given(instance=sparqlas::AnonymousIndividual_strategy)
@settings(max_examples=50)
def test_sparqlas::anonymousindividual_instantiation(instance):
    assert isinstance(instance, sparqlas::AnonymousIndividual)

@given(instance=sparqlas::AnonymousIndividual_strategy)
def test_sparqlas::anonymousindividual_nodeID_type(instance):
    assert isinstance(instance.nodeID, str)


@given(instance=sparqlas::AnonymousIndividual_strategy)
def test_sparqlas::anonymousindividual_nodeID_setter(instance):
    original = instance.nodeID
    instance.nodeID = original
    assert instance.nodeID == original

@given(instance=sparqlas::IndividualVariable_strategy)
@settings(max_examples=50)
def test_sparqlas::individualvariable_instantiation(instance):
    assert isinstance(instance, sparqlas::IndividualVariable)

@given(instance=sparqlas::Variable_strategy)
@settings(max_examples=50)
def test_sparqlas::variable_instantiation(instance):
    assert isinstance(instance, sparqlas::Variable)

@given(instance=sparqlas::Variable_strategy)
def test_sparqlas::variable_symbol_type(instance):
    assert isinstance(instance.symbol, str)


@given(instance=sparqlas::Variable_strategy)
def test_sparqlas::variable_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=sparqlas::Atom_strategy)
@settings(max_examples=50)
def test_sparqlas::atom_instantiation(instance):
    assert isinstance(instance, sparqlas::Atom)

@given(instance=TemplateableElement_strategy)
@settings(max_examples=50)
def test_templateableelement_instantiation(instance):
    assert isinstance(instance, TemplateableElement)

@given(instance=Query_strategy)
@settings(max_examples=50)
def test_query_instantiation(instance):
    assert isinstance(instance, Query)

@given(instance=sparqlas::ConstructQuery_strategy)
@settings(max_examples=50)
def test_sparqlas::constructquery_instantiation(instance):
    assert isinstance(instance, sparqlas::ConstructQuery)

@given(instance=sparqlas::SelectQuery_strategy)
@settings(max_examples=50)
def test_sparqlas::selectquery_instantiation(instance):
    assert isinstance(instance, sparqlas::SelectQuery)

@given(instance=sparqlas::FullIRI_strategy)
@settings(max_examples=50)
def test_sparqlas::fulliri_instantiation(instance):
    assert isinstance(instance, sparqlas::FullIRI)

@given(instance=sparqlas::DescribeQuery_strategy)
@settings(max_examples=50)
def test_sparqlas::describequery_instantiation(instance):
    assert isinstance(instance, sparqlas::DescribeQuery)

@given(instance=sparqlas::AskQuery_strategy)
@settings(max_examples=50)
def test_sparqlas::askquery_instantiation(instance):
    assert isinstance(instance, sparqlas::AskQuery)

@given(instance=sparqlas::Import_strategy)
@settings(max_examples=50)
def test_sparqlas::import_instantiation(instance):
    assert isinstance(instance, sparqlas::Import)

@given(instance=sparqlas::IRI_strategy)
@settings(max_examples=50)
def test_sparqlas::iri_instantiation(instance):
    assert isinstance(instance, sparqlas::IRI)

@given(instance=sparqlas::IRI_strategy)
def test_sparqlas::iri_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=sparqlas::IRI_strategy)
def test_sparqlas::iri_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=sparqlas::OntologyDocument_strategy)
@settings(max_examples=50)
def test_sparqlas::ontologydocument_instantiation(instance):
    assert isinstance(instance, sparqlas::OntologyDocument)

@given(instance=sparqlas::Query_strategy)
@settings(max_examples=50)
def test_sparqlas::query_instantiation(instance):
    assert isinstance(instance, sparqlas::Query)

@given(instance=sparqlas::PrefixDefinition_strategy)
@settings(max_examples=50)
def test_sparqlas::prefixdefinition_instantiation(instance):
    assert isinstance(instance, sparqlas::PrefixDefinition)

@given(instance=sparqlas::PrefixDefinition_strategy)
def test_sparqlas::prefixdefinition_pref_type(instance):
    assert isinstance(instance.pref, str)


@given(instance=sparqlas::PrefixDefinition_strategy)
def test_sparqlas::prefixdefinition_pref_setter(instance):
    original = instance.pref
    instance.pref = original
    assert instance.pref == original
