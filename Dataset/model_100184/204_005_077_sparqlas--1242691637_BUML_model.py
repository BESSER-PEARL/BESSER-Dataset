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
sparqlas_PrefixDefinition = Class(name="sparqlas_PrefixDefinition")
sparqlas_Query = Class(name="sparqlas_Query", is_abstract=True)
sparqlas_OntologyDocument = Class(name="sparqlas_OntologyDocument")
sparqlas_IRI = Class(name="sparqlas_IRI", is_abstract=True)
sparqlas_Import = Class(name="sparqlas_Import")
sparqlas_AskQuery = Class(name="sparqlas_AskQuery")
sparqlas_DescribeQuery = Class(name="sparqlas_DescribeQuery")
sparqlas_FullIRI = Class(name="sparqlas_FullIRI")
sparqlas_SelectQuery = Class(name="sparqlas_SelectQuery")
Query = Class(name="Query")
TemplateableElement = Class(name="TemplateableElement")
sparqlas_Atom = Class(name="sparqlas_Atom", is_abstract=True)
sparqlas_Variable = Class(name="sparqlas_Variable")
sparqlas_ConstructQuery = Class(name="sparqlas_ConstructQuery")
sparqlas_IndividualVariable = Class(name="sparqlas_IndividualVariable")
Individual = Class(name="Individual")
sparqlas_Constant = Class(name="sparqlas_Constant", is_abstract=True)
sparqlas_Class = Class(name="sparqlas_Class")
IRI = Class(name="IRI")
sparqlas_AbbreviatedIRI = Class(name="sparqlas_AbbreviatedIRI")
sparqlas_Term = Class(name="sparqlas_Term", is_abstract=True)
Term = Class(name="Term")
sparqlas_ClassVariable = Class(name="sparqlas_ClassVariable")
Variable = Class(name="Variable")
ClassExpression = Class(name="ClassExpression")
sparqlas_ObjectPropertyVariable = Class(name="sparqlas_ObjectPropertyVariable")
ObjectPropertyExpression = Class(name="ObjectPropertyExpression")
sparqlas_DataPropertyVariable = Class(name="sparqlas_DataPropertyVariable")
DataPropertyExpression = Class(name="DataPropertyExpression")
sparqlas_ObjectPropertyAssertion = Class(name="sparqlas_ObjectPropertyAssertion")
sparqlas_ObjectPropertyExpression = Class(name="sparqlas_ObjectPropertyExpression", is_abstract=True)
Constant = Class(name="Constant")
sparqlas_Datatype = Class(name="sparqlas_Datatype")
DataRange = Class(name="DataRange")
sparqlas_ObjectProperty = Class(name="sparqlas_ObjectProperty")
sparqlas_DataProperty = Class(name="sparqlas_DataProperty")
sparqlas_Individual = Class(name="sparqlas_Individual", is_abstract=True)
sparqlas_NamedIndividual = Class(name="sparqlas_NamedIndividual")
sparqlas_AnonymousIndividual = Class(name="sparqlas_AnonymousIndividual")
sparqlas_AbstractLiteral = Class(name="sparqlas_AbstractLiteral", is_abstract=True)
sparqlas_LiteralVariable = Class(name="sparqlas_LiteralVariable")
AbstractLiteral = Class(name="AbstractLiteral")
sparqlas_Literal = Class(name="sparqlas_Literal")
sparqlas_Expression = Class(name="sparqlas_Expression", is_abstract=True)
ParameterableElement = Class(name="ParameterableElement")
sparqlas_Assertion = Class(name="sparqlas_Assertion", is_abstract=True)
Atom = Class(name="Atom")
sparqlas_ClassAssertion = Class(name="sparqlas_ClassAssertion")
Assertion = Class(name="Assertion")
sparqlas_ClassExpression = Class(name="sparqlas_ClassExpression", is_abstract=True)
sparqlas_SameIndividual = Class(name="sparqlas_SameIndividual")
sparqlas_DifferentIndividuals = Class(name="sparqlas_DifferentIndividuals")
sparqlas_DataPropertyAssertion = Class(name="sparqlas_DataPropertyAssertion")
sparqlas_DataPropertyExpression = Class(name="sparqlas_DataPropertyExpression", is_abstract=True)
sparqlas_NegativeObjectPropertyAssertion = Class(name="sparqlas_NegativeObjectPropertyAssertion")
sparqlas_NegativeDataPropertyAssertion = Class(name="sparqlas_NegativeDataPropertyAssertion")
sparqlas_DisjointClasses = Class(name="sparqlas_DisjointClasses")
sparqlas_ClassAtom = Class(name="sparqlas_ClassAtom", is_abstract=True)
sparqlas_SubClassOf = Class(name="sparqlas_SubClassOf")
ClassAtom = Class(name="ClassAtom")
sparqlas_EquivalentClasses = Class(name="sparqlas_EquivalentClasses")
sparqlas_ObjectComplementOf = Class(name="sparqlas_ObjectComplementOf")
sparqlas_DisjointUnion = Class(name="sparqlas_DisjointUnion")
Expression = Class(name="Expression")
sparqlas_ObjectUnionOf = Class(name="sparqlas_ObjectUnionOf")
sparqlas_ObjectSomeValuesFrom = Class(name="sparqlas_ObjectSomeValuesFrom")
sparqlas_ObjectOneOf = Class(name="sparqlas_ObjectOneOf")
sparqlas_ObjectIntersectionOf = Class(name="sparqlas_ObjectIntersectionOf")
sparqlas_ObjectAllValuesFrom = Class(name="sparqlas_ObjectAllValuesFrom")
sparqlas_ObjectMaxCardinality = Class(name="sparqlas_ObjectMaxCardinality")
sparqlas_ObjectHasValue = Class(name="sparqlas_ObjectHasValue")
sparqlas_ObjectMinCardinality = Class(name="sparqlas_ObjectMinCardinality")
sparqlas_DataRange = Class(name="sparqlas_DataRange", is_abstract=True)
sparqlas_ObjectExactCardinality = Class(name="sparqlas_ObjectExactCardinality")
sparqlas_DataAllValuesFrom = Class(name="sparqlas_DataAllValuesFrom")
sparqlas_DataMaxCardinality = Class(name="sparqlas_DataMaxCardinality")
sparqlas_DataSomeValuesFrom = Class(name="sparqlas_DataSomeValuesFrom")
sparqlas_DataHasValue = Class(name="sparqlas_DataHasValue")
sparqlas_DataMinCardinality = Class(name="sparqlas_DataMinCardinality")
sparqlas_DataComplementOf = Class(name="sparqlas_DataComplementOf")
sparqlas_DataOneOf = Class(name="sparqlas_DataOneOf")
sparqlas_DataExactCardinality = Class(name="sparqlas_DataExactCardinality")
sparqlas_DataUnionOf = Class(name="sparqlas_DataUnionOf")
sparqlas_ObjectPropertyAtom = Class(name="sparqlas_ObjectPropertyAtom", is_abstract=True)
sparqlas_SubObjectPropertyOf = Class(name="sparqlas_SubObjectPropertyOf")
sparqlas_DataIntersectionOf = Class(name="sparqlas_DataIntersectionOf")
sparqlas_DatatypeRestriction = Class(name="sparqlas_DatatypeRestriction")
sparqlas_FacetRestriction = Class(name="sparqlas_FacetRestriction")
sparqlas_DisjointObjectProperties = Class(name="sparqlas_DisjointObjectProperties")
sparqlas_ObjectPropertyDomain = Class(name="sparqlas_ObjectPropertyDomain")
ObjectPropertyAtom = Class(name="ObjectPropertyAtom")
sparqlas_ObjectPropertyChain = Class(name="sparqlas_ObjectPropertyChain")
sparqlas_EquivalentObjectProperties = Class(name="sparqlas_EquivalentObjectProperties")
sparqlas_FunctionalObjectProperty = Class(name="sparqlas_FunctionalObjectProperty")
sparqlas_ObjectPropertyRange = Class(name="sparqlas_ObjectPropertyRange")
sparqlas_InverseObjectPropertyAtom = Class(name="sparqlas_InverseObjectPropertyAtom")
sparqlas_SymmetricObjectProperty = Class(name="sparqlas_SymmetricObjectProperty")
sparqlas_InverseFunctionalObjectProperty = Class(name="sparqlas_InverseFunctionalObjectProperty")
sparqlas_ReflexiveObjectProperty = Class(name="sparqlas_ReflexiveObjectProperty")
sparqlas_IrreflexiveObjectProperty = Class(name="sparqlas_IrreflexiveObjectProperty")
sparqlas_DataPropertyAtom = Class(name="sparqlas_DataPropertyAtom", is_abstract=True)
sparqlas_SubDataPropertyOf = Class(name="sparqlas_SubDataPropertyOf")
DataPropertyAtom = Class(name="DataPropertyAtom")
sparqlas_AsymmetricObjectProperty = Class(name="sparqlas_AsymmetricObjectProperty")
sparqlas_TransitiveObjectProperty = Class(name="sparqlas_TransitiveObjectProperty")
sparqlas_InverseObjectProperty = Class(name="sparqlas_InverseObjectProperty")
sparqlas_DataPropertyRange = Class(name="sparqlas_DataPropertyRange")
sparqlas_EquivalentDataProperties = Class(name="sparqlas_EquivalentDataProperties")
sparqlas_DisjointDataProperties = Class(name="sparqlas_DisjointDataProperties")
sparqlas_DataPropertyDomain = Class(name="sparqlas_DataPropertyDomain")
sparqlas_Declaration = Class(name="sparqlas_Declaration", is_abstract=True)
sparqlas_FunctionalDataProperty = Class(name="sparqlas_FunctionalDataProperty")
sparqlas_HasKey = Class(name="sparqlas_HasKey")
sparqlas_IndividualDeclaration = Class(name="sparqlas_IndividualDeclaration")
sparqlas_ClassDeclaration = Class(name="sparqlas_ClassDeclaration")
Declaration = Class(name="Declaration")
sparqlas_ObjectPropertyDeclaration = Class(name="sparqlas_ObjectPropertyDeclaration")
sparqlas_DatatypePropertyDeclaration = Class(name="sparqlas_DatatypePropertyDeclaration")
sparqlas_ParameterableElement = Class(name="sparqlas_ParameterableElement", is_abstract=True)
sparqlas_TemplateParameter = Class(name="sparqlas_TemplateParameter")
sparqlas_TemplateSignature = Class(name="sparqlas_TemplateSignature")
sparqlas_TemplateParameterSubstitution = Class(name="sparqlas_TemplateParameterSubstitution")
sparqlas_TemplateableElement = Class(name="sparqlas_TemplateableElement", is_abstract=True)
sparqlas_TemplateBinding = Class(name="sparqlas_TemplateBinding")
sparqlas_DirectClassAssertion = Class(name="sparqlas_DirectClassAssertion")
sparqlas_DirectSubClassOf = Class(name="sparqlas_DirectSubClassOf")
sparqlas_StrictSubClassOf = Class(name="sparqlas_StrictSubClassOf")

# sparqlas_PrefixDefinition class attributes and methods
sparqlas_PrefixDefinition_pref: Property = Property(name="pref", type=StringType)
sparqlas_PrefixDefinition.attributes={sparqlas_PrefixDefinition_pref}

# sparqlas_Query class attributes and methods

# sparqlas_OntologyDocument class attributes and methods

# sparqlas_IRI class attributes and methods
sparqlas_IRI_id: Property = Property(name="id", type=StringType)
sparqlas_IRI.attributes={sparqlas_IRI_id}

# sparqlas_Import class attributes and methods

# sparqlas_AskQuery class attributes and methods

# sparqlas_DescribeQuery class attributes and methods

# sparqlas_FullIRI class attributes and methods

# sparqlas_SelectQuery class attributes and methods

# Query class attributes and methods

# TemplateableElement class attributes and methods

# sparqlas_Atom class attributes and methods

# sparqlas_Variable class attributes and methods
sparqlas_Variable_symbol: Property = Property(name="symbol", type=StringType)
sparqlas_Variable.attributes={sparqlas_Variable_symbol}

# sparqlas_ConstructQuery class attributes and methods

# sparqlas_IndividualVariable class attributes and methods

# Individual class attributes and methods

# sparqlas_Constant class attributes and methods

# sparqlas_Class class attributes and methods

# IRI class attributes and methods

# sparqlas_AbbreviatedIRI class attributes and methods

# sparqlas_Term class attributes and methods

# Term class attributes and methods

# sparqlas_ClassVariable class attributes and methods

# Variable class attributes and methods

# ClassExpression class attributes and methods

# sparqlas_ObjectPropertyVariable class attributes and methods

# ObjectPropertyExpression class attributes and methods

# sparqlas_DataPropertyVariable class attributes and methods

# DataPropertyExpression class attributes and methods

# sparqlas_ObjectPropertyAssertion class attributes and methods

# sparqlas_ObjectPropertyExpression class attributes and methods

# Constant class attributes and methods

# sparqlas_Datatype class attributes and methods

# DataRange class attributes and methods

# sparqlas_ObjectProperty class attributes and methods

# sparqlas_DataProperty class attributes and methods

# sparqlas_Individual class attributes and methods

# sparqlas_NamedIndividual class attributes and methods

# sparqlas_AnonymousIndividual class attributes and methods
sparqlas_AnonymousIndividual_nodeID: Property = Property(name="nodeID", type=StringType)
sparqlas_AnonymousIndividual.attributes={sparqlas_AnonymousIndividual_nodeID}

# sparqlas_AbstractLiteral class attributes and methods

# sparqlas_LiteralVariable class attributes and methods

# AbstractLiteral class attributes and methods

# sparqlas_Literal class attributes and methods
sparqlas_Literal_lexicalForm: Property = Property(name="lexicalForm", type=StringType)
sparqlas_Literal.attributes={sparqlas_Literal_lexicalForm}

# sparqlas_Expression class attributes and methods

# ParameterableElement class attributes and methods

# sparqlas_Assertion class attributes and methods

# Atom class attributes and methods

# sparqlas_ClassAssertion class attributes and methods

# Assertion class attributes and methods

# sparqlas_ClassExpression class attributes and methods

# sparqlas_SameIndividual class attributes and methods

# sparqlas_DifferentIndividuals class attributes and methods

# sparqlas_DataPropertyAssertion class attributes and methods

# sparqlas_DataPropertyExpression class attributes and methods

# sparqlas_NegativeObjectPropertyAssertion class attributes and methods

# sparqlas_NegativeDataPropertyAssertion class attributes and methods

# sparqlas_DisjointClasses class attributes and methods

# sparqlas_ClassAtom class attributes and methods

# sparqlas_SubClassOf class attributes and methods

# ClassAtom class attributes and methods

# sparqlas_EquivalentClasses class attributes and methods

# sparqlas_ObjectComplementOf class attributes and methods

# sparqlas_DisjointUnion class attributes and methods

# Expression class attributes and methods

# sparqlas_ObjectUnionOf class attributes and methods

# sparqlas_ObjectSomeValuesFrom class attributes and methods

# sparqlas_ObjectOneOf class attributes and methods

# sparqlas_ObjectIntersectionOf class attributes and methods

# sparqlas_ObjectAllValuesFrom class attributes and methods

# sparqlas_ObjectMaxCardinality class attributes and methods
sparqlas_ObjectMaxCardinality_cardinality: Property = Property(name="cardinality", type=IntegerType)
sparqlas_ObjectMaxCardinality.attributes={sparqlas_ObjectMaxCardinality_cardinality}

# sparqlas_ObjectHasValue class attributes and methods

# sparqlas_ObjectMinCardinality class attributes and methods
sparqlas_ObjectMinCardinality_cardinality: Property = Property(name="cardinality", type=IntegerType)
sparqlas_ObjectMinCardinality.attributes={sparqlas_ObjectMinCardinality_cardinality}

# sparqlas_DataRange class attributes and methods

# sparqlas_ObjectExactCardinality class attributes and methods
sparqlas_ObjectExactCardinality_cardinality: Property = Property(name="cardinality", type=IntegerType)
sparqlas_ObjectExactCardinality.attributes={sparqlas_ObjectExactCardinality_cardinality}

# sparqlas_DataAllValuesFrom class attributes and methods

# sparqlas_DataMaxCardinality class attributes and methods
sparqlas_DataMaxCardinality_cardinality: Property = Property(name="cardinality", type=IntegerType)
sparqlas_DataMaxCardinality.attributes={sparqlas_DataMaxCardinality_cardinality}

# sparqlas_DataSomeValuesFrom class attributes and methods

# sparqlas_DataHasValue class attributes and methods

# sparqlas_DataMinCardinality class attributes and methods
sparqlas_DataMinCardinality_cardinality: Property = Property(name="cardinality", type=IntegerType)
sparqlas_DataMinCardinality.attributes={sparqlas_DataMinCardinality_cardinality}

# sparqlas_DataComplementOf class attributes and methods

# sparqlas_DataOneOf class attributes and methods

# sparqlas_DataExactCardinality class attributes and methods
sparqlas_DataExactCardinality_cardinality: Property = Property(name="cardinality", type=IntegerType)
sparqlas_DataExactCardinality.attributes={sparqlas_DataExactCardinality_cardinality}

# sparqlas_DataUnionOf class attributes and methods

# sparqlas_ObjectPropertyAtom class attributes and methods

# sparqlas_SubObjectPropertyOf class attributes and methods

# sparqlas_DataIntersectionOf class attributes and methods

# sparqlas_DatatypeRestriction class attributes and methods

# sparqlas_FacetRestriction class attributes and methods

# sparqlas_DisjointObjectProperties class attributes and methods

# sparqlas_ObjectPropertyDomain class attributes and methods

# ObjectPropertyAtom class attributes and methods

# sparqlas_ObjectPropertyChain class attributes and methods

# sparqlas_EquivalentObjectProperties class attributes and methods

# sparqlas_FunctionalObjectProperty class attributes and methods

# sparqlas_ObjectPropertyRange class attributes and methods

# sparqlas_InverseObjectPropertyAtom class attributes and methods

# sparqlas_SymmetricObjectProperty class attributes and methods

# sparqlas_InverseFunctionalObjectProperty class attributes and methods

# sparqlas_ReflexiveObjectProperty class attributes and methods

# sparqlas_IrreflexiveObjectProperty class attributes and methods

# sparqlas_DataPropertyAtom class attributes and methods

# sparqlas_SubDataPropertyOf class attributes and methods

# DataPropertyAtom class attributes and methods

# sparqlas_AsymmetricObjectProperty class attributes and methods

# sparqlas_TransitiveObjectProperty class attributes and methods

# sparqlas_InverseObjectProperty class attributes and methods

# sparqlas_DataPropertyRange class attributes and methods

# sparqlas_EquivalentDataProperties class attributes and methods

# sparqlas_DisjointDataProperties class attributes and methods

# sparqlas_DataPropertyDomain class attributes and methods

# sparqlas_Declaration class attributes and methods

# sparqlas_FunctionalDataProperty class attributes and methods

# sparqlas_HasKey class attributes and methods

# sparqlas_IndividualDeclaration class attributes and methods

# sparqlas_ClassDeclaration class attributes and methods

# Declaration class attributes and methods

# sparqlas_ObjectPropertyDeclaration class attributes and methods

# sparqlas_DatatypePropertyDeclaration class attributes and methods

# sparqlas_ParameterableElement class attributes and methods

# sparqlas_TemplateParameter class attributes and methods

# sparqlas_TemplateSignature class attributes and methods

# sparqlas_TemplateParameterSubstitution class attributes and methods

# sparqlas_TemplateableElement class attributes and methods

# sparqlas_TemplateBinding class attributes and methods

# sparqlas_DirectClassAssertion class attributes and methods

# sparqlas_DirectSubClassOf class attributes and methods

# sparqlas_StrictSubClassOf class attributes and methods

# Relationships
prefixDefinition3: BinaryAssociation = BinaryAssociation(
    name="prefixDefinition3",
    ends={
        Property(name="sparqlas_PrefixDefinition", type=sparqlas_OntologyDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_OntologyDocument4", type=sparqlas_PrefixDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
query5: BinaryAssociation = BinaryAssociation(
    name="query5",
    ends={
        Property(name="sparqlas_Query", type=sparqlas_OntologyDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_OntologyDocument6", type=sparqlas_Query, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
queryIRI0: BinaryAssociation = BinaryAssociation(
    name="queryIRI0",
    ends={
        Property(name="sparqlas_IRI", type=sparqlas_OntologyDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_OntologyDocument", type=sparqlas_IRI, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
import_1: BinaryAssociation = BinaryAssociation(
    name="import_1",
    ends={
        Property(name="sparqlas_Import", type=sparqlas_OntologyDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_OntologyDocument2", type=sparqlas_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
atoms20: BinaryAssociation = BinaryAssociation(
    name="atoms20",
    ends={
        Property(name="sparqlas_Atom21", type=sparqlas_AskQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_AskQuery", type=sparqlas_Atom, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
describeIRI22: BinaryAssociation = BinaryAssociation(
    name="describeIRI22",
    ends={
        Property(name="sparqlas_IRI23", type=sparqlas_DescribeQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_DescribeQuery", type=sparqlas_IRI, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
importIRI7: BinaryAssociation = BinaryAssociation(
    name="importIRI7",
    ends={
        Property(name="sparqlas_IRI9", type=sparqlas_Import, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_Import8", type=sparqlas_IRI, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
namespace10: BinaryAssociation = BinaryAssociation(
    name="namespace10",
    ends={
        Property(name="sparqlas_FullIRI", type=sparqlas_PrefixDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_PrefixDefinition11", type=sparqlas_FullIRI, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
atoms12: BinaryAssociation = BinaryAssociation(
    name="atoms12",
    ends={
        Property(name="sparqlas_Atom", type=sparqlas_SelectQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_SelectQuery", type=sparqlas_Atom, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variables13: BinaryAssociation = BinaryAssociation(
    name="variables13",
    ends={
        Property(name="sparqlas_Variable", type=sparqlas_SelectQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_SelectQuery14", type=sparqlas_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constructAtoms15: BinaryAssociation = BinaryAssociation(
    name="constructAtoms15",
    ends={
        Property(name="sparqlas_Atom16", type=sparqlas_ConstructQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_ConstructQuery", type=sparqlas_Atom, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
whereAtoms17: BinaryAssociation = BinaryAssociation(
    name="whereAtoms17",
    ends={
        Property(name="sparqlas_Atom19", type=sparqlas_ConstructQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_ConstructQuery18", type=sparqlas_Atom, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constantIRI27: BinaryAssociation = BinaryAssociation(
    name="constantIRI27",
    ends={
        Property(name="sparqlas_IRI28", type=sparqlas_Constant, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_Constant", type=sparqlas_IRI, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
atoms24: BinaryAssociation = BinaryAssociation(
    name="atoms24",
    ends={
        Property(name="sparqlas_Atom26", type=sparqlas_DescribeQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_DescribeQuery25", type=sparqlas_Atom, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classExpression31: BinaryAssociation = BinaryAssociation(
    name="classExpression31",
    ends={
        Property(name="sparqlas_ClassAssertion32", type=sparqlas_ClassExpression, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="sparqlas_ClassExpression", type=sparqlas_ClassAssertion, multiplicity=Multiplicity(1, 1))
    }
)
sourceIndividual33: BinaryAssociation = BinaryAssociation(
    name="sourceIndividual33",
    ends={
        Property(name="sparqlas_Individual34", type=sparqlas_ObjectPropertyAssertion, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_ObjectPropertyAssertion", type=sparqlas_Individual, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
targetIndividual35: BinaryAssociation = BinaryAssociation(
    name="targetIndividual35",
    ends={
        Property(name="sparqlas_Individual37", type=sparqlas_ObjectPropertyAssertion, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_ObjectPropertyAssertion36", type=sparqlas_Individual, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
objectPropertyExpression38: BinaryAssociation = BinaryAssociation(
    name="objectPropertyExpression38",
    ends={
        Property(name="sparqlas_ObjectPropertyExpression", type=sparqlas_ObjectPropertyAssertion, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_ObjectPropertyAssertion39", type=sparqlas_ObjectPropertyExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
datatype29: BinaryAssociation = BinaryAssociation(
    name="datatype29",
    ends={
        Property(name="sparqlas_Datatype", type=sparqlas_Literal, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_Literal", type=sparqlas_Datatype, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
individual30: BinaryAssociation = BinaryAssociation(
    name="individual30",
    ends={
        Property(name="sparqlas_Individual", type=sparqlas_ClassAssertion, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_ClassAssertion", type=sparqlas_Individual, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
individuals62: BinaryAssociation = BinaryAssociation(
    name="individuals62",
    ends={
        Property(name="sparqlas_Individual63", type=sparqlas_SameIndividual, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_SameIndividual", type=sparqlas_Individual, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
sourceIndividual40: BinaryAssociation = BinaryAssociation(
    name="sourceIndividual40",
    ends={
        Property(name="sparqlas_Individual41", type=sparqlas_DataPropertyAssertion, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_DataPropertyAssertion", type=sparqlas_Individual, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
targetValue42: BinaryAssociation = BinaryAssociation(
    name="targetValue42",
    ends={
        Property(name="sparqlas_AbstractLiteral", type=sparqlas_DataPropertyAssertion, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_DataPropertyAssertion43", type=sparqlas_AbstractLiteral, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
dataPropertyExpression44: BinaryAssociation = BinaryAssociation(
    name="dataPropertyExpression44",
    ends={
        Property(name="sparqlas_DataPropertyExpression", type=sparqlas_DataPropertyAssertion, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_DataPropertyAssertion45", type=sparqlas_DataPropertyExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sourceIndividual46: BinaryAssociation = BinaryAssociation(
    name="sourceIndividual46",
    ends={
        Property(name="sparqlas_Individual47", type=sparqlas_NegativeObjectPropertyAssertion, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_NegativeObjectPropertyAssertion", type=sparqlas_Individual, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
targetIndividual48: BinaryAssociation = BinaryAssociation(
    name="targetIndividual48",
    ends={
        Property(name="sparqlas_Individual50", type=sparqlas_NegativeObjectPropertyAssertion, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_NegativeObjectPropertyAssertion49", type=sparqlas_Individual, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
objectPropertyExpression51: BinaryAssociation = BinaryAssociation(
    name="objectPropertyExpression51",
    ends={
        Property(name="sparqlas_ObjectPropertyExpression53", type=sparqlas_NegativeObjectPropertyAssertion, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_NegativeObjectPropertyAssertion52", type=sparqlas_ObjectPropertyExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sourceIndividual54: BinaryAssociation = BinaryAssociation(
    name="sourceIndividual54",
    ends={
        Property(name="sparqlas_Individual55", type=sparqlas_NegativeDataPropertyAssertion, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_NegativeDataPropertyAssertion", type=sparqlas_Individual, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
targetValue56: BinaryAssociation = BinaryAssociation(
    name="targetValue56",
    ends={
        Property(name="sparqlas_AbstractLiteral58", type=sparqlas_NegativeDataPropertyAssertion, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_NegativeDataPropertyAssertion57", type=sparqlas_AbstractLiteral, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
dataPropertyExpression59: BinaryAssociation = BinaryAssociation(
    name="dataPropertyExpression59",
    ends={
        Property(name="sparqlas_DataPropertyExpression61", type=sparqlas_NegativeDataPropertyAssertion, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_NegativeDataPropertyAssertion60", type=sparqlas_DataPropertyExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
classExpressions71: BinaryAssociation = BinaryAssociation(
    name="classExpressions71",
    ends={
        Property(name="sparqlas_EquivalentClasses", type=sparqlas_ClassExpression, multiplicity=Multiplicity(2, 9999), is_composite=True),
        Property(name="sparqlas_ClassExpression72", type=sparqlas_EquivalentClasses, multiplicity=Multiplicity(1, 1))
    }
)
individuals64: BinaryAssociation = BinaryAssociation(
    name="individuals64",
    ends={
        Property(name="sparqlas_Individual65", type=sparqlas_DifferentIndividuals, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_DifferentIndividuals", type=sparqlas_Individual, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
subClassExpression66: BinaryAssociation = BinaryAssociation(
    name="subClassExpression66",
    ends={
        Property(name="sparqlas_ClassExpression67", type=sparqlas_SubClassOf, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_SubClassOf", type=sparqlas_ClassExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
superClassExpression68: BinaryAssociation = BinaryAssociation(
    name="superClassExpression68",
    ends={
        Property(name="sparqlas_ClassExpression70", type=sparqlas_SubClassOf, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_SubClassOf69", type=sparqlas_ClassExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
classExpressions81: BinaryAssociation = BinaryAssociation(
    name="classExpressions81",
    ends={
        Property(name="sparqlas_ObjectUnionOf", type=sparqlas_ClassExpression, multiplicity=Multiplicity(2, 9999), is_composite=True),
        Property(name="sparqlas_ClassExpression82", type=sparqlas_ObjectUnionOf, multiplicity=Multiplicity(1, 1))
    }
)
classExpression83: BinaryAssociation = BinaryAssociation(
    name="classExpression83",
    ends={
        Property(name="sparqlas_ClassExpression84", type=sparqlas_ObjectComplementOf, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_ObjectComplementOf", type=sparqlas_ClassExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
classExpressions73: BinaryAssociation = BinaryAssociation(
    name="classExpressions73",
    ends={
        Property(name="sparqlas_ClassExpression74", type=sparqlas_DisjointClasses, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_DisjointClasses", type=sparqlas_ClassExpression, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
class_75: BinaryAssociation = BinaryAssociation(
    name="class_75",
    ends={
        Property(name="sparqlas_Class", type=sparqlas_DisjointUnion, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_DisjointUnion", type=sparqlas_Class, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classVariable76: BinaryAssociation = BinaryAssociation(
    name="classVariable76",
    ends={
        Property(name="sparqlas_ClassVariable", type=sparqlas_DisjointUnion, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_DisjointUnion77", type=sparqlas_ClassVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
disjointClassExpressions78: BinaryAssociation = BinaryAssociation(
    name="disjointClassExpressions78",
    ends={
        Property(name="sparqlas_ClassExpression80", type=sparqlas_DisjointUnion, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_DisjointUnion79", type=sparqlas_ClassExpression, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
classExpression94: BinaryAssociation = BinaryAssociation(
    name="classExpression94",
    ends={
        Property(name="sparqlas_ClassExpression95", type=sparqlas_ObjectSomeValuesFrom, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_ObjectSomeValuesFrom", type=sparqlas_ClassExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
objectPropertyExpression96: BinaryAssociation = BinaryAssociation(
    name="objectPropertyExpression96",
    ends={
        Property(name="sparqlas_ObjectPropertyExpression98", type=sparqlas_ObjectSomeValuesFrom, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_ObjectSomeValuesFrom97", type=sparqlas_ObjectPropertyExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
individuals85: BinaryAssociation = BinaryAssociation(
    name="individuals85",
    ends={
        Property(name="sparqlas_Individual86", type=sparqlas_ObjectOneOf, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_ObjectOneOf", type=sparqlas_Individual, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
classExpressions87: BinaryAssociation = BinaryAssociation(
    name="classExpressions87",
    ends={
        Property(name="sparqlas_ClassExpression88", type=sparqlas_ObjectIntersectionOf, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_ObjectIntersectionOf", type=sparqlas_ClassExpression, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
classExpression89: BinaryAssociation = BinaryAssociation(
    name="classExpression89",
    ends={
        Property(name="sparqlas_ClassExpression90", type=sparqlas_ObjectAllValuesFrom, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_ObjectAllValuesFrom", type=sparqlas_ClassExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
objectPropertyExpression91: BinaryAssociation = BinaryAssociation(
    name="objectPropertyExpression91",
    ends={
        Property(name="sparqlas_ObjectPropertyExpression93", type=sparqlas_ObjectAllValuesFrom, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_ObjectAllValuesFrom92", type=sparqlas_ObjectPropertyExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
objectPropertyExpression106: BinaryAssociation = BinaryAssociation(
    name="objectPropertyExpression106",
    ends={
        Property(name="sparqlas_ObjectMinCardinality107", type=sparqlas_ObjectPropertyExpression, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="sparqlas_ObjectPropertyExpression108", type=sparqlas_ObjectMinCardinality, multiplicity=Multiplicity(1, 1))
    }
)
individual99: BinaryAssociation = BinaryAssociation(
    name="individual99",
    ends={
        Property(name="sparqlas_Individual100", type=sparqlas_ObjectHasValue, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_ObjectHasValue", type=sparqlas_Individual, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
objectPropertyExpression101: BinaryAssociation = BinaryAssociation(
    name="objectPropertyExpression101",
    ends={
        Property(name="sparqlas_ObjectPropertyExpression103", type=sparqlas_ObjectHasValue, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_ObjectHasValue102", type=sparqlas_ObjectPropertyExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
classExpression104: BinaryAssociation = BinaryAssociation(
    name="classExpression104",
    ends={
        Property(name="sparqlas_ClassExpression105", type=sparqlas_ObjectMinCardinality, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_ObjectMinCardinality", type=sparqlas_ClassExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dataRange119: BinaryAssociation = BinaryAssociation(
    name="dataRange119",
    ends={
        Property(name="sparqlas_DataRange", type=sparqlas_DataAllValuesFrom, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_DataAllValuesFrom", type=sparqlas_DataRange, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
dataPropertyExpressions120: BinaryAssociation = BinaryAssociation(
    name="dataPropertyExpressions120",
    ends={
        Property(name="sparqlas_DataPropertyExpression122", type=sparqlas_DataAllValuesFrom, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_DataAllValuesFrom121", type=sparqlas_DataPropertyExpression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
classExpression109: BinaryAssociation = BinaryAssociation(
    name="classExpression109",
    ends={
        Property(name="sparqlas_ClassExpression110", type=sparqlas_ObjectMaxCardinality, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_ObjectMaxCardinality", type=sparqlas_ClassExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
objectPropertyExpression111: BinaryAssociation = BinaryAssociation(
    name="objectPropertyExpression111",
    ends={
        Property(name="sparqlas_ObjectPropertyExpression113", type=sparqlas_ObjectMaxCardinality, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_ObjectMaxCardinality112", type=sparqlas_ObjectPropertyExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
classExpression114: BinaryAssociation = BinaryAssociation(
    name="classExpression114",
    ends={
        Property(name="sparqlas_ClassExpression115", type=sparqlas_ObjectExactCardinality, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_ObjectExactCardinality", type=sparqlas_ClassExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
objectPropertyExpression116: BinaryAssociation = BinaryAssociation(
    name="objectPropertyExpression116",
    ends={
        Property(name="sparqlas_ObjectPropertyExpression118", type=sparqlas_ObjectExactCardinality, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_ObjectExactCardinality117", type=sparqlas_ObjectPropertyExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
dataPropertyExpression135: BinaryAssociation = BinaryAssociation(
    name="dataPropertyExpression135",
    ends={
        Property(name="sparqlas_DataPropertyExpression137", type=sparqlas_DataMinCardinality, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_DataMinCardinality136", type=sparqlas_DataPropertyExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
dataRange123: BinaryAssociation = BinaryAssociation(
    name="dataRange123",
    ends={
        Property(name="sparqlas_DataRange124", type=sparqlas_DataSomeValuesFrom, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_DataSomeValuesFrom", type=sparqlas_DataRange, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
dataPropertyExpressions125: BinaryAssociation = BinaryAssociation(
    name="dataPropertyExpressions125",
    ends={
        Property(name="sparqlas_DataPropertyExpression127", type=sparqlas_DataSomeValuesFrom, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_DataSomeValuesFrom126", type=sparqlas_DataPropertyExpression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
literal128: BinaryAssociation = BinaryAssociation(
    name="literal128",
    ends={
        Property(name="sparqlas_AbstractLiteral129", type=sparqlas_DataHasValue, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_DataHasValue", type=sparqlas_AbstractLiteral, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
dataPropertyExpression130: BinaryAssociation = BinaryAssociation(
    name="dataPropertyExpression130",
    ends={
        Property(name="sparqlas_DataPropertyExpression132", type=sparqlas_DataHasValue, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_DataHasValue131", type=sparqlas_DataPropertyExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
dataRange133: BinaryAssociation = BinaryAssociation(
    name="dataRange133",
    ends={
        Property(name="sparqlas_DataRange134", type=sparqlas_DataMinCardinality, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_DataMinCardinality", type=sparqlas_DataRange, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dataRange150: BinaryAssociation = BinaryAssociation(
    name="dataRange150",
    ends={
        Property(name="sparqlas_DataRange151", type=sparqlas_DataComplementOf, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_DataComplementOf", type=sparqlas_DataRange, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
dataRange138: BinaryAssociation = BinaryAssociation(
    name="dataRange138",
    ends={
        Property(name="sparqlas_DataRange139", type=sparqlas_DataMaxCardinality, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_DataMaxCardinality", type=sparqlas_DataRange, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dataPropertyExpression140: BinaryAssociation = BinaryAssociation(
    name="dataPropertyExpression140",
    ends={
        Property(name="sparqlas_DataPropertyExpression142", type=sparqlas_DataMaxCardinality, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_DataMaxCardinality141", type=sparqlas_DataPropertyExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
dataRange143: BinaryAssociation = BinaryAssociation(
    name="dataRange143",
    ends={
        Property(name="sparqlas_DataRange144", type=sparqlas_DataExactCardinality, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_DataExactCardinality", type=sparqlas_DataRange, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dataPropertyExpression145: BinaryAssociation = BinaryAssociation(
    name="dataPropertyExpression145",
    ends={
        Property(name="sparqlas_DataPropertyExpression147", type=sparqlas_DataExactCardinality, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_DataExactCardinality146", type=sparqlas_DataPropertyExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
dataRanges148: BinaryAssociation = BinaryAssociation(
    name="dataRanges148",
    ends={
        Property(name="sparqlas_DataRange149", type=sparqlas_DataUnionOf, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_DataUnionOf", type=sparqlas_DataRange, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
restrictionValue163: BinaryAssociation = BinaryAssociation(
    name="restrictionValue163",
    ends={
        Property(name="sparqlas_AbstractLiteral165", type=sparqlas_FacetRestriction, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_FacetRestriction164", type=sparqlas_AbstractLiteral, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
literals152: BinaryAssociation = BinaryAssociation(
    name="literals152",
    ends={
        Property(name="sparqlas_AbstractLiteral153", type=sparqlas_DataOneOf, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_DataOneOf", type=sparqlas_AbstractLiteral, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
dataRanges154: BinaryAssociation = BinaryAssociation(
    name="dataRanges154",
    ends={
        Property(name="sparqlas_DataRange155", type=sparqlas_DataIntersectionOf, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_DataIntersectionOf", type=sparqlas_DataRange, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
datatype156: BinaryAssociation = BinaryAssociation(
    name="datatype156",
    ends={
        Property(name="sparqlas_Datatype157", type=sparqlas_DatatypeRestriction, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_DatatypeRestriction", type=sparqlas_Datatype, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
restrictions158: BinaryAssociation = BinaryAssociation(
    name="restrictions158",
    ends={
        Property(name="sparqlas_FacetRestriction", type=sparqlas_DatatypeRestriction, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_DatatypeRestriction159", type=sparqlas_FacetRestriction, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
constrainingFacet160: BinaryAssociation = BinaryAssociation(
    name="constrainingFacet160",
    ends={
        Property(name="sparqlas_IRI162", type=sparqlas_FacetRestriction, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_FacetRestriction161", type=sparqlas_IRI, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
objectPropertyExpression178: BinaryAssociation = BinaryAssociation(
    name="objectPropertyExpression178",
    ends={
        Property(name="sparqlas_ObjectPropertyExpression179", type=sparqlas_DisjointObjectProperties, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_DisjointObjectProperties", type=sparqlas_ObjectPropertyExpression, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
subObjectPropertyExpression166: BinaryAssociation = BinaryAssociation(
    name="subObjectPropertyExpression166",
    ends={
        Property(name="sparqlas_ObjectPropertyExpression167", type=sparqlas_SubObjectPropertyOf, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_SubObjectPropertyOf", type=sparqlas_ObjectPropertyExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subObjectPropertyChain168: BinaryAssociation = BinaryAssociation(
    name="subObjectPropertyChain168",
    ends={
        Property(name="sparqlas_ObjectPropertyChain", type=sparqlas_SubObjectPropertyOf, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_SubObjectPropertyOf169", type=sparqlas_ObjectPropertyChain, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
superObjectPropertyExpression170: BinaryAssociation = BinaryAssociation(
    name="superObjectPropertyExpression170",
    ends={
        Property(name="sparqlas_ObjectPropertyExpression172", type=sparqlas_SubObjectPropertyOf, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_SubObjectPropertyOf171", type=sparqlas_ObjectPropertyExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
objectPropertyExpression173: BinaryAssociation = BinaryAssociation(
    name="objectPropertyExpression173",
    ends={
        Property(name="sparqlas_ObjectPropertyExpression175", type=sparqlas_ObjectPropertyChain, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_ObjectPropertyChain174", type=sparqlas_ObjectPropertyExpression, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
objectPropertyExpression176: BinaryAssociation = BinaryAssociation(
    name="objectPropertyExpression176",
    ends={
        Property(name="sparqlas_ObjectPropertyExpression177", type=sparqlas_EquivalentObjectProperties, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_EquivalentObjectProperties", type=sparqlas_ObjectPropertyExpression, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
objectPropertyExpression2192: BinaryAssociation = BinaryAssociation(
    name="objectPropertyExpression2192",
    ends={
        Property(name="sparqlas_ObjectPropertyExpression194", type=sparqlas_InverseObjectPropertyAtom, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_InverseObjectPropertyAtom193", type=sparqlas_ObjectPropertyExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
objectPropertyExpression180: BinaryAssociation = BinaryAssociation(
    name="objectPropertyExpression180",
    ends={
        Property(name="sparqlas_ObjectPropertyExpression181", type=sparqlas_ObjectPropertyDomain, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_ObjectPropertyDomain", type=sparqlas_ObjectPropertyExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
domain182: BinaryAssociation = BinaryAssociation(
    name="domain182",
    ends={
        Property(name="sparqlas_ClassExpression184", type=sparqlas_ObjectPropertyDomain, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_ObjectPropertyDomain183", type=sparqlas_ClassExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
objectPropertyExpression185: BinaryAssociation = BinaryAssociation(
    name="objectPropertyExpression185",
    ends={
        Property(name="sparqlas_ObjectPropertyExpression186", type=sparqlas_ObjectPropertyRange, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_ObjectPropertyRange", type=sparqlas_ObjectPropertyExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
range187: BinaryAssociation = BinaryAssociation(
    name="range187",
    ends={
        Property(name="sparqlas_ClassExpression189", type=sparqlas_ObjectPropertyRange, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_ObjectPropertyRange188", type=sparqlas_ClassExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
objectPropertyExpression1190: BinaryAssociation = BinaryAssociation(
    name="objectPropertyExpression1190",
    ends={
        Property(name="sparqlas_ObjectPropertyExpression191", type=sparqlas_InverseObjectPropertyAtom, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_InverseObjectPropertyAtom", type=sparqlas_ObjectPropertyExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
objectPropertyExpression201: BinaryAssociation = BinaryAssociation(
    name="objectPropertyExpression201",
    ends={
        Property(name="sparqlas_ObjectPropertyExpression202", type=sparqlas_IrreflexiveObjectProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_IrreflexiveObjectProperty", type=sparqlas_ObjectPropertyExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
objectPropertyExpression195: BinaryAssociation = BinaryAssociation(
    name="objectPropertyExpression195",
    ends={
        Property(name="sparqlas_ObjectPropertyExpression196", type=sparqlas_FunctionalObjectProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_FunctionalObjectProperty", type=sparqlas_ObjectPropertyExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
objectPropertyExpression197: BinaryAssociation = BinaryAssociation(
    name="objectPropertyExpression197",
    ends={
        Property(name="sparqlas_ObjectPropertyExpression198", type=sparqlas_InverseFunctionalObjectProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_InverseFunctionalObjectProperty", type=sparqlas_ObjectPropertyExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
objectPropertyExpression199: BinaryAssociation = BinaryAssociation(
    name="objectPropertyExpression199",
    ends={
        Property(name="sparqlas_ObjectPropertyExpression200", type=sparqlas_ReflexiveObjectProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_ReflexiveObjectProperty", type=sparqlas_ObjectPropertyExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
objectProperty209: BinaryAssociation = BinaryAssociation(
    name="objectProperty209",
    ends={
        Property(name="sparqlas_ObjectPropertyExpression210", type=sparqlas_InverseObjectProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_InverseObjectProperty", type=sparqlas_ObjectPropertyExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
objectPropertyExpression203: BinaryAssociation = BinaryAssociation(
    name="objectPropertyExpression203",
    ends={
        Property(name="sparqlas_ObjectPropertyExpression204", type=sparqlas_SymmetricObjectProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_SymmetricObjectProperty", type=sparqlas_ObjectPropertyExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
objectPropertyExpression205: BinaryAssociation = BinaryAssociation(
    name="objectPropertyExpression205",
    ends={
        Property(name="sparqlas_ObjectPropertyExpression206", type=sparqlas_AsymmetricObjectProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_AsymmetricObjectProperty", type=sparqlas_ObjectPropertyExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
objectPropertyExpression207: BinaryAssociation = BinaryAssociation(
    name="objectPropertyExpression207",
    ends={
        Property(name="sparqlas_ObjectPropertyExpression208", type=sparqlas_TransitiveObjectProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_TransitiveObjectProperty", type=sparqlas_ObjectPropertyExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
domain222: BinaryAssociation = BinaryAssociation(
    name="domain222",
    ends={
        Property(name="sparqlas_ClassExpression224", type=sparqlas_DataPropertyDomain, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_DataPropertyDomain223", type=sparqlas_ClassExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
subDataPropertyExpression211: BinaryAssociation = BinaryAssociation(
    name="subDataPropertyExpression211",
    ends={
        Property(name="sparqlas_DataPropertyExpression212", type=sparqlas_SubDataPropertyOf, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_SubDataPropertyOf", type=sparqlas_DataPropertyExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
superDataPropertyExpression213: BinaryAssociation = BinaryAssociation(
    name="superDataPropertyExpression213",
    ends={
        Property(name="sparqlas_DataPropertyExpression215", type=sparqlas_SubDataPropertyOf, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_SubDataPropertyOf214", type=sparqlas_DataPropertyExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
dataPropertyExpression216: BinaryAssociation = BinaryAssociation(
    name="dataPropertyExpression216",
    ends={
        Property(name="sparqlas_DataPropertyExpression217", type=sparqlas_EquivalentDataProperties, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_EquivalentDataProperties", type=sparqlas_DataPropertyExpression, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
dataPropertyExpression218: BinaryAssociation = BinaryAssociation(
    name="dataPropertyExpression218",
    ends={
        Property(name="sparqlas_DataPropertyExpression219", type=sparqlas_DisjointDataProperties, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_DisjointDataProperties", type=sparqlas_DataPropertyExpression, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
dataPropertyExpression220: BinaryAssociation = BinaryAssociation(
    name="dataPropertyExpression220",
    ends={
        Property(name="sparqlas_DataPropertyExpression221", type=sparqlas_DataPropertyDomain, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_DataPropertyDomain", type=sparqlas_DataPropertyExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
objectPropertyExpression234: BinaryAssociation = BinaryAssociation(
    name="objectPropertyExpression234",
    ends={
        Property(name="sparqlas_ObjectPropertyExpression236", type=sparqlas_HasKey, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_HasKey235", type=sparqlas_ObjectPropertyExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataPropertyExpression237: BinaryAssociation = BinaryAssociation(
    name="dataPropertyExpression237",
    ends={
        Property(name="sparqlas_DataPropertyExpression239", type=sparqlas_HasKey, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_HasKey238", type=sparqlas_DataPropertyExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataPropertyExpression225: BinaryAssociation = BinaryAssociation(
    name="dataPropertyExpression225",
    ends={
        Property(name="sparqlas_DataPropertyExpression226", type=sparqlas_DataPropertyRange, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_DataPropertyRange", type=sparqlas_DataPropertyExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
range227: BinaryAssociation = BinaryAssociation(
    name="range227",
    ends={
        Property(name="sparqlas_DataRange229", type=sparqlas_DataPropertyRange, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_DataPropertyRange228", type=sparqlas_DataRange, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
dataPropertyExpression230: BinaryAssociation = BinaryAssociation(
    name="dataPropertyExpression230",
    ends={
        Property(name="sparqlas_DataPropertyExpression231", type=sparqlas_FunctionalDataProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_FunctionalDataProperty", type=sparqlas_DataPropertyExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
classExpression232: BinaryAssociation = BinaryAssociation(
    name="classExpression232",
    ends={
        Property(name="sparqlas_ClassExpression233", type=sparqlas_HasKey, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_HasKey", type=sparqlas_ClassExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
datatypeProperty248: BinaryAssociation = BinaryAssociation(
    name="datatypeProperty248",
    ends={
        Property(name="sparqlas_DataProperty", type=sparqlas_DatatypePropertyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_DatatypePropertyDeclaration", type=sparqlas_DataProperty, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
datatypePropertyVariable249: BinaryAssociation = BinaryAssociation(
    name="datatypePropertyVariable249",
    ends={
        Property(name="sparqlas_DataPropertyVariable", type=sparqlas_DatatypePropertyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_DatatypePropertyDeclaration250", type=sparqlas_DataPropertyVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
class_240: BinaryAssociation = BinaryAssociation(
    name="class_240",
    ends={
        Property(name="sparqlas_Class241", type=sparqlas_ClassDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_ClassDeclaration", type=sparqlas_Class, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classVariable242: BinaryAssociation = BinaryAssociation(
    name="classVariable242",
    ends={
        Property(name="sparqlas_ClassVariable244", type=sparqlas_ClassDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_ClassDeclaration243", type=sparqlas_ClassVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
objectProperty245: BinaryAssociation = BinaryAssociation(
    name="objectProperty245",
    ends={
        Property(name="sparqlas_ObjectProperty", type=sparqlas_ObjectPropertyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_ObjectPropertyDeclaration", type=sparqlas_ObjectProperty, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
objectPropertyVariable246: BinaryAssociation = BinaryAssociation(
    name="objectPropertyVariable246",
    ends={
        Property(name="sparqlas_ObjectPropertyVariable", type=sparqlas_ObjectPropertyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_ObjectPropertyDeclaration247", type=sparqlas_ObjectPropertyVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
individual251: BinaryAssociation = BinaryAssociation(
    name="individual251",
    ends={
        Property(name="sparqlas_NamedIndividual", type=sparqlas_IndividualDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_IndividualDeclaration", type=sparqlas_NamedIndividual, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
individualVariable252: BinaryAssociation = BinaryAssociation(
    name="individualVariable252",
    ends={
        Property(name="sparqlas_IndividualVariable", type=sparqlas_IndividualDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_IndividualDeclaration253", type=sparqlas_IndividualVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
signature254: BinaryAssociation = BinaryAssociation(
    name="signature254",
    ends={
        Property(name="TemplateSignature", type=sparqlas_TemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedParameter", type=sparqlas_TemplateSignature, multiplicity=Multiplicity(1, 1))
    }
)
templateParameter257: BinaryAssociation = BinaryAssociation(
    name="templateParameter257",
    ends={
        Property(name="TemplateParameter", type=sparqlas_ParameterableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="parameteredElement", type=sparqlas_TemplateParameter, multiplicity=Multiplicity(0, 1))
    }
)
parameteredElement255: BinaryAssociation = BinaryAssociation(
    name="parameteredElement255",
    ends={
        Property(name="ParameterableElement", type=sparqlas_TemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="templateParameter", type=sparqlas_ParameterableElement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameterSubstitution256: BinaryAssociation = BinaryAssociation(
    name="parameterSubstitution256",
    ends={
        Property(name="sparqlas_TemplateParameterSubstitution", type=sparqlas_TemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_TemplateParameter", type=sparqlas_TemplateParameterSubstitution, multiplicity=Multiplicity(1, 1))
    }
)
template260: BinaryAssociation = BinaryAssociation(
    name="template260",
    ends={
        Property(name="ownedTemplateSignature", type=sparqlas_TemplateableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="TemplateableElement", type=sparqlas_TemplateSignature, multiplicity=Multiplicity(1, 1))
    }
)
ownedParameter258: BinaryAssociation = BinaryAssociation(
    name="ownedParameter258",
    ends={
        Property(name="TemplateParameter259", type=sparqlas_TemplateSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="signature", type=sparqlas_TemplateParameter, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
actual264: BinaryAssociation = BinaryAssociation(
    name="actual264",
    ends={
        Property(name="sparqlas_ParameterableElement", type=sparqlas_TemplateParameterSubstitution, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_TemplateParameterSubstitution265", type=sparqlas_ParameterableElement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ownedTemplateSignature261: BinaryAssociation = BinaryAssociation(
    name="ownedTemplateSignature261",
    ends={
        Property(name="TemplateSignature262", type=sparqlas_TemplateableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="template", type=sparqlas_TemplateSignature, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
templateBinding263: BinaryAssociation = BinaryAssociation(
    name="templateBinding263",
    ends={
        Property(name="TemplateBinding", type=sparqlas_TemplateableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="boundElement", type=sparqlas_TemplateBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
individual276: BinaryAssociation = BinaryAssociation(
    name="individual276",
    ends={
        Property(name="sparqlas_Individual277", type=sparqlas_DirectClassAssertion, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_DirectClassAssertion", type=sparqlas_Individual, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
templateBinding266: BinaryAssociation = BinaryAssociation(
    name="templateBinding266",
    ends={
        Property(name="TemplateBinding267", type=sparqlas_TemplateParameterSubstitution, multiplicity=Multiplicity(1, 1)),
        Property(name="parameterSubstitution", type=sparqlas_TemplateBinding, multiplicity=Multiplicity(1, 1))
    }
)
formal268: BinaryAssociation = BinaryAssociation(
    name="formal268",
    ends={
        Property(name="sparqlas_ParameterableElement270", type=sparqlas_TemplateParameterSubstitution, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_TemplateParameterSubstitution269", type=sparqlas_ParameterableElement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameterSubstitution271: BinaryAssociation = BinaryAssociation(
    name="parameterSubstitution271",
    ends={
        Property(name="TemplateParameterSubstitution", type=sparqlas_TemplateBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="templateBinding", type=sparqlas_TemplateParameterSubstitution, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
boundElement272: BinaryAssociation = BinaryAssociation(
    name="boundElement272",
    ends={
        Property(name="TemplateableElement274", type=sparqlas_TemplateBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="templateBinding273", type=sparqlas_TemplateableElement, multiplicity=Multiplicity(1, 1))
    }
)
signature275: BinaryAssociation = BinaryAssociation(
    name="signature275",
    ends={
        Property(name="sparqlas_TemplateSignature", type=sparqlas_TemplateBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_TemplateBinding", type=sparqlas_TemplateSignature, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
superClassExpression288: BinaryAssociation = BinaryAssociation(
    name="superClassExpression288",
    ends={
        Property(name="sparqlas_StrictSubClassOf289", type=sparqlas_ClassExpression, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="sparqlas_ClassExpression290", type=sparqlas_StrictSubClassOf, multiplicity=Multiplicity(1, 1))
    }
)
classExpression278: BinaryAssociation = BinaryAssociation(
    name="classExpression278",
    ends={
        Property(name="sparqlas_ClassExpression280", type=sparqlas_DirectClassAssertion, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_DirectClassAssertion279", type=sparqlas_ClassExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
subClassExpression281: BinaryAssociation = BinaryAssociation(
    name="subClassExpression281",
    ends={
        Property(name="sparqlas_ClassExpression282", type=sparqlas_DirectSubClassOf, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_DirectSubClassOf", type=sparqlas_ClassExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
superClassExpression283: BinaryAssociation = BinaryAssociation(
    name="superClassExpression283",
    ends={
        Property(name="sparqlas_ClassExpression285", type=sparqlas_DirectSubClassOf, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_DirectSubClassOf284", type=sparqlas_ClassExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
subClassExpression286: BinaryAssociation = BinaryAssociation(
    name="subClassExpression286",
    ends={
        Property(name="sparqlas_ClassExpression287", type=sparqlas_StrictSubClassOf, multiplicity=Multiplicity(1, 1)),
        Property(name="sparqlas_StrictSubClassOf", type=sparqlas_ClassExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_sparqlas_AskQuery_Query = Generalization(general=Query, specific=sparqlas_AskQuery)
gen_sparqlas_AskQuery_TemplateableElement = Generalization(general=TemplateableElement, specific=sparqlas_AskQuery)
gen_sparqlas_DescribeQuery_Query = Generalization(general=Query, specific=sparqlas_DescribeQuery)
gen_sparqlas_DescribeQuery_TemplateableElement = Generalization(general=TemplateableElement, specific=sparqlas_DescribeQuery)
gen_sparqlas_SelectQuery_Query = Generalization(general=Query, specific=sparqlas_SelectQuery)
gen_sparqlas_SelectQuery_TemplateableElement = Generalization(general=TemplateableElement, specific=sparqlas_SelectQuery)
gen_sparqlas_ConstructQuery_Query = Generalization(general=Query, specific=sparqlas_ConstructQuery)
gen_sparqlas_ConstructQuery_TemplateableElement = Generalization(general=TemplateableElement, specific=sparqlas_ConstructQuery)
gen_sparqlas_IndividualVariable_Variable = Generalization(general=Variable, specific=sparqlas_IndividualVariable)
gen_sparqlas_IndividualVariable_Individual = Generalization(general=Individual, specific=sparqlas_IndividualVariable)
gen_sparqlas_Constant_Term = Generalization(general=Term, specific=sparqlas_Constant)
gen_sparqlas_FullIRI_IRI = Generalization(general=IRI, specific=sparqlas_FullIRI)
gen_sparqlas_AbbreviatedIRI_IRI = Generalization(general=IRI, specific=sparqlas_AbbreviatedIRI)
gen_sparqlas_Variable_Term = Generalization(general=Term, specific=sparqlas_Variable)
gen_sparqlas_ClassVariable_Variable = Generalization(general=Variable, specific=sparqlas_ClassVariable)
gen_sparqlas_ClassVariable_ClassExpression = Generalization(general=ClassExpression, specific=sparqlas_ClassVariable)
gen_sparqlas_ObjectPropertyVariable_Variable = Generalization(general=Variable, specific=sparqlas_ObjectPropertyVariable)
gen_sparqlas_ObjectPropertyVariable_ObjectPropertyExpression = Generalization(general=ObjectPropertyExpression, specific=sparqlas_ObjectPropertyVariable)
gen_sparqlas_DataPropertyVariable_Variable = Generalization(general=Variable, specific=sparqlas_DataPropertyVariable)
gen_sparqlas_DataPropertyVariable_DataPropertyExpression = Generalization(general=DataPropertyExpression, specific=sparqlas_DataPropertyVariable)
gen_sparqlas_ObjectPropertyAssertion_Assertion = Generalization(general=Assertion, specific=sparqlas_ObjectPropertyAssertion)
gen_sparqlas_Class_ClassExpression = Generalization(general=ClassExpression, specific=sparqlas_Class)
gen_sparqlas_Class_Constant = Generalization(general=Constant, specific=sparqlas_Class)
gen_sparqlas_Datatype_Constant = Generalization(general=Constant, specific=sparqlas_Datatype)
gen_sparqlas_Datatype_DataRange = Generalization(general=DataRange, specific=sparqlas_Datatype)
gen_sparqlas_ObjectProperty_ObjectPropertyExpression = Generalization(general=ObjectPropertyExpression, specific=sparqlas_ObjectProperty)
gen_sparqlas_ObjectProperty_Constant = Generalization(general=Constant, specific=sparqlas_ObjectProperty)
gen_sparqlas_DataProperty_DataPropertyExpression = Generalization(general=DataPropertyExpression, specific=sparqlas_DataProperty)
gen_sparqlas_DataProperty_Constant = Generalization(general=Constant, specific=sparqlas_DataProperty)
gen_sparqlas_NamedIndividual_Individual = Generalization(general=Individual, specific=sparqlas_NamedIndividual)
gen_sparqlas_NamedIndividual_Constant = Generalization(general=Constant, specific=sparqlas_NamedIndividual)
gen_sparqlas_AnonymousIndividual_Individual = Generalization(general=Individual, specific=sparqlas_AnonymousIndividual)
gen_sparqlas_LiteralVariable_Variable = Generalization(general=Variable, specific=sparqlas_LiteralVariable)
gen_sparqlas_LiteralVariable_AbstractLiteral = Generalization(general=AbstractLiteral, specific=sparqlas_LiteralVariable)
gen_sparqlas_Literal_AbstractLiteral = Generalization(general=AbstractLiteral, specific=sparqlas_Literal)
gen_sparqlas_Expression_ParameterableElement = Generalization(general=ParameterableElement, specific=sparqlas_Expression)
gen_sparqlas_Assertion_Atom = Generalization(general=Atom, specific=sparqlas_Assertion)
gen_sparqlas_ClassAssertion_Assertion = Generalization(general=Assertion, specific=sparqlas_ClassAssertion)
gen_sparqlas_SameIndividual_Assertion = Generalization(general=Assertion, specific=sparqlas_SameIndividual)
gen_sparqlas_DifferentIndividuals_Assertion = Generalization(general=Assertion, specific=sparqlas_DifferentIndividuals)
gen_sparqlas_DataPropertyAssertion_Assertion = Generalization(general=Assertion, specific=sparqlas_DataPropertyAssertion)
gen_sparqlas_NegativeObjectPropertyAssertion_Assertion = Generalization(general=Assertion, specific=sparqlas_NegativeObjectPropertyAssertion)
gen_sparqlas_NegativeDataPropertyAssertion_Assertion = Generalization(general=Assertion, specific=sparqlas_NegativeDataPropertyAssertion)
gen_sparqlas_DisjointClasses_ClassAtom = Generalization(general=ClassAtom, specific=sparqlas_DisjointClasses)
gen_sparqlas_ClassAtom_Atom = Generalization(general=Atom, specific=sparqlas_ClassAtom)
gen_sparqlas_SubClassOf_ClassAtom = Generalization(general=ClassAtom, specific=sparqlas_SubClassOf)
gen_sparqlas_EquivalentClasses_ClassAtom = Generalization(general=ClassAtom, specific=sparqlas_EquivalentClasses)
gen_sparqlas_ObjectComplementOf_ClassExpression = Generalization(general=ClassExpression, specific=sparqlas_ObjectComplementOf)
gen_sparqlas_DisjointUnion_ClassAtom = Generalization(general=ClassAtom, specific=sparqlas_DisjointUnion)
gen_sparqlas_ClassExpression_Expression = Generalization(general=Expression, specific=sparqlas_ClassExpression)
gen_sparqlas_ObjectUnionOf_ClassExpression = Generalization(general=ClassExpression, specific=sparqlas_ObjectUnionOf)
gen_sparqlas_ObjectSomeValuesFrom_ClassExpression = Generalization(general=ClassExpression, specific=sparqlas_ObjectSomeValuesFrom)
gen_sparqlas_ObjectOneOf_ClassExpression = Generalization(general=ClassExpression, specific=sparqlas_ObjectOneOf)
gen_sparqlas_ObjectIntersectionOf_ClassExpression = Generalization(general=ClassExpression, specific=sparqlas_ObjectIntersectionOf)
gen_sparqlas_ObjectAllValuesFrom_ClassExpression = Generalization(general=ClassExpression, specific=sparqlas_ObjectAllValuesFrom)
gen_sparqlas_ObjectMaxCardinality_ClassExpression = Generalization(general=ClassExpression, specific=sparqlas_ObjectMaxCardinality)
gen_sparqlas_ObjectHasValue_ClassExpression = Generalization(general=ClassExpression, specific=sparqlas_ObjectHasValue)
gen_sparqlas_ObjectMinCardinality_ClassExpression = Generalization(general=ClassExpression, specific=sparqlas_ObjectMinCardinality)
gen_sparqlas_ObjectExactCardinality_ClassExpression = Generalization(general=ClassExpression, specific=sparqlas_ObjectExactCardinality)
gen_sparqlas_DataAllValuesFrom_ClassExpression = Generalization(general=ClassExpression, specific=sparqlas_DataAllValuesFrom)
gen_sparqlas_DataMaxCardinality_ClassExpression = Generalization(general=ClassExpression, specific=sparqlas_DataMaxCardinality)
gen_sparqlas_DataSomeValuesFrom_ClassExpression = Generalization(general=ClassExpression, specific=sparqlas_DataSomeValuesFrom)
gen_sparqlas_DataHasValue_ClassExpression = Generalization(general=ClassExpression, specific=sparqlas_DataHasValue)
gen_sparqlas_DataMinCardinality_ClassExpression = Generalization(general=ClassExpression, specific=sparqlas_DataMinCardinality)
gen_sparqlas_DataComplementOf_DataRange = Generalization(general=DataRange, specific=sparqlas_DataComplementOf)
gen_sparqlas_DataExactCardinality_ClassExpression = Generalization(general=ClassExpression, specific=sparqlas_DataExactCardinality)
gen_sparqlas_DataUnionOf_DataRange = Generalization(general=DataRange, specific=sparqlas_DataUnionOf)
gen_sparqlas_ObjectPropertyAtom_Atom = Generalization(general=Atom, specific=sparqlas_ObjectPropertyAtom)
gen_sparqlas_DataOneOf_DataRange = Generalization(general=DataRange, specific=sparqlas_DataOneOf)
gen_sparqlas_DataIntersectionOf_DataRange = Generalization(general=DataRange, specific=sparqlas_DataIntersectionOf)
gen_sparqlas_DatatypeRestriction_DataRange = Generalization(general=DataRange, specific=sparqlas_DatatypeRestriction)
gen_sparqlas_DisjointObjectProperties_ObjectPropertyAtom = Generalization(general=ObjectPropertyAtom, specific=sparqlas_DisjointObjectProperties)
gen_sparqlas_ObjectPropertyDomain_ObjectPropertyAtom = Generalization(general=ObjectPropertyAtom, specific=sparqlas_ObjectPropertyDomain)
gen_sparqlas_SubObjectPropertyOf_ObjectPropertyAtom = Generalization(general=ObjectPropertyAtom, specific=sparqlas_SubObjectPropertyOf)
gen_sparqlas_EquivalentObjectProperties_ObjectPropertyAtom = Generalization(general=ObjectPropertyAtom, specific=sparqlas_EquivalentObjectProperties)
gen_sparqlas_FunctionalObjectProperty_ObjectPropertyAtom = Generalization(general=ObjectPropertyAtom, specific=sparqlas_FunctionalObjectProperty)
gen_sparqlas_ObjectPropertyRange_ObjectPropertyAtom = Generalization(general=ObjectPropertyAtom, specific=sparqlas_ObjectPropertyRange)
gen_sparqlas_InverseObjectPropertyAtom_ObjectPropertyAtom = Generalization(general=ObjectPropertyAtom, specific=sparqlas_InverseObjectPropertyAtom)
gen_sparqlas_SymmetricObjectProperty_ObjectPropertyAtom = Generalization(general=ObjectPropertyAtom, specific=sparqlas_SymmetricObjectProperty)
gen_sparqlas_InverseFunctionalObjectProperty_ObjectPropertyAtom = Generalization(general=ObjectPropertyAtom, specific=sparqlas_InverseFunctionalObjectProperty)
gen_sparqlas_ReflexiveObjectProperty_ObjectPropertyAtom = Generalization(general=ObjectPropertyAtom, specific=sparqlas_ReflexiveObjectProperty)
gen_sparqlas_IrreflexiveObjectProperty_ObjectPropertyAtom = Generalization(general=ObjectPropertyAtom, specific=sparqlas_IrreflexiveObjectProperty)
gen_sparqlas_DataPropertyAtom_Atom = Generalization(general=Atom, specific=sparqlas_DataPropertyAtom)
gen_sparqlas_SubDataPropertyOf_DataPropertyAtom = Generalization(general=DataPropertyAtom, specific=sparqlas_SubDataPropertyOf)
gen_sparqlas_AsymmetricObjectProperty_ObjectPropertyAtom = Generalization(general=ObjectPropertyAtom, specific=sparqlas_AsymmetricObjectProperty)
gen_sparqlas_TransitiveObjectProperty_ObjectPropertyAtom = Generalization(general=ObjectPropertyAtom, specific=sparqlas_TransitiveObjectProperty)
gen_sparqlas_ObjectPropertyExpression_Expression = Generalization(general=Expression, specific=sparqlas_ObjectPropertyExpression)
gen_sparqlas_InverseObjectProperty_ObjectPropertyExpression = Generalization(general=ObjectPropertyExpression, specific=sparqlas_InverseObjectProperty)
gen_sparqlas_DataPropertyRange_DataPropertyAtom = Generalization(general=DataPropertyAtom, specific=sparqlas_DataPropertyRange)
gen_sparqlas_EquivalentDataProperties_DataPropertyAtom = Generalization(general=DataPropertyAtom, specific=sparqlas_EquivalentDataProperties)
gen_sparqlas_DisjointDataProperties_DataPropertyAtom = Generalization(general=DataPropertyAtom, specific=sparqlas_DisjointDataProperties)
gen_sparqlas_DataPropertyDomain_DataPropertyAtom = Generalization(general=DataPropertyAtom, specific=sparqlas_DataPropertyDomain)
gen_sparqlas_Declaration_Atom = Generalization(general=Atom, specific=sparqlas_Declaration)
gen_sparqlas_FunctionalDataProperty_DataPropertyAtom = Generalization(general=DataPropertyAtom, specific=sparqlas_FunctionalDataProperty)
gen_sparqlas_DataPropertyExpression_Expression = Generalization(general=Expression, specific=sparqlas_DataPropertyExpression)
gen_sparqlas_HasKey_Atom = Generalization(general=Atom, specific=sparqlas_HasKey)
gen_sparqlas_IndividualDeclaration_Declaration = Generalization(general=Declaration, specific=sparqlas_IndividualDeclaration)
gen_sparqlas_ClassDeclaration_Declaration = Generalization(general=Declaration, specific=sparqlas_ClassDeclaration)
gen_sparqlas_ObjectPropertyDeclaration_Declaration = Generalization(general=Declaration, specific=sparqlas_ObjectPropertyDeclaration)
gen_sparqlas_DatatypePropertyDeclaration_Declaration = Generalization(general=Declaration, specific=sparqlas_DatatypePropertyDeclaration)
gen_sparqlas_DirectClassAssertion_Assertion = Generalization(general=Assertion, specific=sparqlas_DirectClassAssertion)
gen_sparqlas_DirectSubClassOf_ClassAtom = Generalization(general=ClassAtom, specific=sparqlas_DirectSubClassOf)
gen_sparqlas_StrictSubClassOf_ClassAtom = Generalization(general=ClassAtom, specific=sparqlas_StrictSubClassOf)

# Domain Model
domain_model = DomainModel(
    name="sparqlas",
    types={sparqlas_PrefixDefinition, sparqlas_Query, sparqlas_OntologyDocument, sparqlas_IRI, sparqlas_Import, sparqlas_AskQuery, sparqlas_DescribeQuery, sparqlas_FullIRI, sparqlas_SelectQuery, Query, TemplateableElement, sparqlas_Atom, sparqlas_Variable, sparqlas_ConstructQuery, sparqlas_IndividualVariable, Individual, sparqlas_Constant, sparqlas_Class, IRI, sparqlas_AbbreviatedIRI, sparqlas_Term, Term, sparqlas_ClassVariable, Variable, ClassExpression, sparqlas_ObjectPropertyVariable, ObjectPropertyExpression, sparqlas_DataPropertyVariable, DataPropertyExpression, sparqlas_ObjectPropertyAssertion, sparqlas_ObjectPropertyExpression, Constant, sparqlas_Datatype, DataRange, sparqlas_ObjectProperty, sparqlas_DataProperty, sparqlas_Individual, sparqlas_NamedIndividual, sparqlas_AnonymousIndividual, sparqlas_AbstractLiteral, sparqlas_LiteralVariable, AbstractLiteral, sparqlas_Literal, sparqlas_Expression, ParameterableElement, sparqlas_Assertion, Atom, sparqlas_ClassAssertion, Assertion, sparqlas_ClassExpression, sparqlas_SameIndividual, sparqlas_DifferentIndividuals, sparqlas_DataPropertyAssertion, sparqlas_DataPropertyExpression, sparqlas_NegativeObjectPropertyAssertion, sparqlas_NegativeDataPropertyAssertion, sparqlas_DisjointClasses, sparqlas_ClassAtom, sparqlas_SubClassOf, ClassAtom, sparqlas_EquivalentClasses, sparqlas_ObjectComplementOf, sparqlas_DisjointUnion, Expression, sparqlas_ObjectUnionOf, sparqlas_ObjectSomeValuesFrom, sparqlas_ObjectOneOf, sparqlas_ObjectIntersectionOf, sparqlas_ObjectAllValuesFrom, sparqlas_ObjectMaxCardinality, sparqlas_ObjectHasValue, sparqlas_ObjectMinCardinality, sparqlas_DataRange, sparqlas_ObjectExactCardinality, sparqlas_DataAllValuesFrom, sparqlas_DataMaxCardinality, sparqlas_DataSomeValuesFrom, sparqlas_DataHasValue, sparqlas_DataMinCardinality, sparqlas_DataComplementOf, sparqlas_DataOneOf, sparqlas_DataExactCardinality, sparqlas_DataUnionOf, sparqlas_ObjectPropertyAtom, sparqlas_SubObjectPropertyOf, sparqlas_DataIntersectionOf, sparqlas_DatatypeRestriction, sparqlas_FacetRestriction, sparqlas_DisjointObjectProperties, sparqlas_ObjectPropertyDomain, ObjectPropertyAtom, sparqlas_ObjectPropertyChain, sparqlas_EquivalentObjectProperties, sparqlas_FunctionalObjectProperty, sparqlas_ObjectPropertyRange, sparqlas_InverseObjectPropertyAtom, sparqlas_SymmetricObjectProperty, sparqlas_InverseFunctionalObjectProperty, sparqlas_ReflexiveObjectProperty, sparqlas_IrreflexiveObjectProperty, sparqlas_DataPropertyAtom, sparqlas_SubDataPropertyOf, DataPropertyAtom, sparqlas_AsymmetricObjectProperty, sparqlas_TransitiveObjectProperty, sparqlas_InverseObjectProperty, sparqlas_DataPropertyRange, sparqlas_EquivalentDataProperties, sparqlas_DisjointDataProperties, sparqlas_DataPropertyDomain, sparqlas_Declaration, sparqlas_FunctionalDataProperty, sparqlas_HasKey, sparqlas_IndividualDeclaration, sparqlas_ClassDeclaration, Declaration, sparqlas_ObjectPropertyDeclaration, sparqlas_DatatypePropertyDeclaration, sparqlas_ParameterableElement, sparqlas_TemplateParameter, sparqlas_TemplateSignature, sparqlas_TemplateParameterSubstitution, sparqlas_TemplateableElement, sparqlas_TemplateBinding, sparqlas_DirectClassAssertion, sparqlas_DirectSubClassOf, sparqlas_StrictSubClassOf},
    associations={prefixDefinition3, query5, queryIRI0, import_1, atoms20, describeIRI22, importIRI7, namespace10, atoms12, variables13, constructAtoms15, whereAtoms17, constantIRI27, atoms24, classExpression31, sourceIndividual33, targetIndividual35, objectPropertyExpression38, datatype29, individual30, individuals62, sourceIndividual40, targetValue42, dataPropertyExpression44, sourceIndividual46, targetIndividual48, objectPropertyExpression51, sourceIndividual54, targetValue56, dataPropertyExpression59, classExpressions71, individuals64, subClassExpression66, superClassExpression68, classExpressions81, classExpression83, classExpressions73, class_75, classVariable76, disjointClassExpressions78, classExpression94, objectPropertyExpression96, individuals85, classExpressions87, classExpression89, objectPropertyExpression91, objectPropertyExpression106, individual99, objectPropertyExpression101, classExpression104, dataRange119, dataPropertyExpressions120, classExpression109, objectPropertyExpression111, classExpression114, objectPropertyExpression116, dataPropertyExpression135, dataRange123, dataPropertyExpressions125, literal128, dataPropertyExpression130, dataRange133, dataRange150, dataRange138, dataPropertyExpression140, dataRange143, dataPropertyExpression145, dataRanges148, restrictionValue163, literals152, dataRanges154, datatype156, restrictions158, constrainingFacet160, objectPropertyExpression178, subObjectPropertyExpression166, subObjectPropertyChain168, superObjectPropertyExpression170, objectPropertyExpression173, objectPropertyExpression176, objectPropertyExpression2192, objectPropertyExpression180, domain182, objectPropertyExpression185, range187, objectPropertyExpression1190, objectPropertyExpression201, objectPropertyExpression195, objectPropertyExpression197, objectPropertyExpression199, objectProperty209, objectPropertyExpression203, objectPropertyExpression205, objectPropertyExpression207, domain222, subDataPropertyExpression211, superDataPropertyExpression213, dataPropertyExpression216, dataPropertyExpression218, dataPropertyExpression220, objectPropertyExpression234, dataPropertyExpression237, dataPropertyExpression225, range227, dataPropertyExpression230, classExpression232, datatypeProperty248, datatypePropertyVariable249, class_240, classVariable242, objectProperty245, objectPropertyVariable246, individual251, individualVariable252, signature254, templateParameter257, parameteredElement255, parameterSubstitution256, template260, ownedParameter258, actual264, ownedTemplateSignature261, templateBinding263, individual276, templateBinding266, formal268, parameterSubstitution271, boundElement272, signature275, superClassExpression288, classExpression278, subClassExpression281, superClassExpression283, subClassExpression286},
    generalizations={gen_sparqlas_AskQuery_Query, gen_sparqlas_AskQuery_TemplateableElement, gen_sparqlas_DescribeQuery_Query, gen_sparqlas_DescribeQuery_TemplateableElement, gen_sparqlas_SelectQuery_Query, gen_sparqlas_SelectQuery_TemplateableElement, gen_sparqlas_ConstructQuery_Query, gen_sparqlas_ConstructQuery_TemplateableElement, gen_sparqlas_IndividualVariable_Variable, gen_sparqlas_IndividualVariable_Individual, gen_sparqlas_Constant_Term, gen_sparqlas_FullIRI_IRI, gen_sparqlas_AbbreviatedIRI_IRI, gen_sparqlas_Variable_Term, gen_sparqlas_ClassVariable_Variable, gen_sparqlas_ClassVariable_ClassExpression, gen_sparqlas_ObjectPropertyVariable_Variable, gen_sparqlas_ObjectPropertyVariable_ObjectPropertyExpression, gen_sparqlas_DataPropertyVariable_Variable, gen_sparqlas_DataPropertyVariable_DataPropertyExpression, gen_sparqlas_ObjectPropertyAssertion_Assertion, gen_sparqlas_Class_ClassExpression, gen_sparqlas_Class_Constant, gen_sparqlas_Datatype_Constant, gen_sparqlas_Datatype_DataRange, gen_sparqlas_ObjectProperty_ObjectPropertyExpression, gen_sparqlas_ObjectProperty_Constant, gen_sparqlas_DataProperty_DataPropertyExpression, gen_sparqlas_DataProperty_Constant, gen_sparqlas_NamedIndividual_Individual, gen_sparqlas_NamedIndividual_Constant, gen_sparqlas_AnonymousIndividual_Individual, gen_sparqlas_LiteralVariable_Variable, gen_sparqlas_LiteralVariable_AbstractLiteral, gen_sparqlas_Literal_AbstractLiteral, gen_sparqlas_Expression_ParameterableElement, gen_sparqlas_Assertion_Atom, gen_sparqlas_ClassAssertion_Assertion, gen_sparqlas_SameIndividual_Assertion, gen_sparqlas_DifferentIndividuals_Assertion, gen_sparqlas_DataPropertyAssertion_Assertion, gen_sparqlas_NegativeObjectPropertyAssertion_Assertion, gen_sparqlas_NegativeDataPropertyAssertion_Assertion, gen_sparqlas_DisjointClasses_ClassAtom, gen_sparqlas_ClassAtom_Atom, gen_sparqlas_SubClassOf_ClassAtom, gen_sparqlas_EquivalentClasses_ClassAtom, gen_sparqlas_ObjectComplementOf_ClassExpression, gen_sparqlas_DisjointUnion_ClassAtom, gen_sparqlas_ClassExpression_Expression, gen_sparqlas_ObjectUnionOf_ClassExpression, gen_sparqlas_ObjectSomeValuesFrom_ClassExpression, gen_sparqlas_ObjectOneOf_ClassExpression, gen_sparqlas_ObjectIntersectionOf_ClassExpression, gen_sparqlas_ObjectAllValuesFrom_ClassExpression, gen_sparqlas_ObjectMaxCardinality_ClassExpression, gen_sparqlas_ObjectHasValue_ClassExpression, gen_sparqlas_ObjectMinCardinality_ClassExpression, gen_sparqlas_ObjectExactCardinality_ClassExpression, gen_sparqlas_DataAllValuesFrom_ClassExpression, gen_sparqlas_DataMaxCardinality_ClassExpression, gen_sparqlas_DataSomeValuesFrom_ClassExpression, gen_sparqlas_DataHasValue_ClassExpression, gen_sparqlas_DataMinCardinality_ClassExpression, gen_sparqlas_DataComplementOf_DataRange, gen_sparqlas_DataExactCardinality_ClassExpression, gen_sparqlas_DataUnionOf_DataRange, gen_sparqlas_ObjectPropertyAtom_Atom, gen_sparqlas_DataOneOf_DataRange, gen_sparqlas_DataIntersectionOf_DataRange, gen_sparqlas_DatatypeRestriction_DataRange, gen_sparqlas_DisjointObjectProperties_ObjectPropertyAtom, gen_sparqlas_ObjectPropertyDomain_ObjectPropertyAtom, gen_sparqlas_SubObjectPropertyOf_ObjectPropertyAtom, gen_sparqlas_EquivalentObjectProperties_ObjectPropertyAtom, gen_sparqlas_FunctionalObjectProperty_ObjectPropertyAtom, gen_sparqlas_ObjectPropertyRange_ObjectPropertyAtom, gen_sparqlas_InverseObjectPropertyAtom_ObjectPropertyAtom, gen_sparqlas_SymmetricObjectProperty_ObjectPropertyAtom, gen_sparqlas_InverseFunctionalObjectProperty_ObjectPropertyAtom, gen_sparqlas_ReflexiveObjectProperty_ObjectPropertyAtom, gen_sparqlas_IrreflexiveObjectProperty_ObjectPropertyAtom, gen_sparqlas_DataPropertyAtom_Atom, gen_sparqlas_SubDataPropertyOf_DataPropertyAtom, gen_sparqlas_AsymmetricObjectProperty_ObjectPropertyAtom, gen_sparqlas_TransitiveObjectProperty_ObjectPropertyAtom, gen_sparqlas_ObjectPropertyExpression_Expression, gen_sparqlas_InverseObjectProperty_ObjectPropertyExpression, gen_sparqlas_DataPropertyRange_DataPropertyAtom, gen_sparqlas_EquivalentDataProperties_DataPropertyAtom, gen_sparqlas_DisjointDataProperties_DataPropertyAtom, gen_sparqlas_DataPropertyDomain_DataPropertyAtom, gen_sparqlas_Declaration_Atom, gen_sparqlas_FunctionalDataProperty_DataPropertyAtom, gen_sparqlas_DataPropertyExpression_Expression, gen_sparqlas_HasKey_Atom, gen_sparqlas_IndividualDeclaration_Declaration, gen_sparqlas_ClassDeclaration_Declaration, gen_sparqlas_ObjectPropertyDeclaration_Declaration, gen_sparqlas_DatatypePropertyDeclaration_Declaration, gen_sparqlas_DirectClassAssertion_Assertion, gen_sparqlas_DirectSubClassOf_ClassAtom, gen_sparqlas_StrictSubClassOf_ClassAtom},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)