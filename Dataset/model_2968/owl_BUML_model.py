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
owl_RDFSLiteral = Class(name="owl::RDFSLiteral")
owl_OWLOntology = Class(name="owl::OWLOntology")
Ontology = Class(name="Ontology")
owl_OWLOntologyProperty = Class(name="owl::OWLOntologyProperty")
RDFProperty = Class(name="RDFProperty")
owl_OWLClass = Class(name="owl::OWLClass")
RDFSClass = Class(name="RDFSClass")
owl_UnionClass = Class(name="owl::UnionClass")
owl_ComplementClass = Class(name="owl::ComplementClass")
owl_OWLRestriction = Class(name="owl::OWLRestriction", is_abstract=True)
OWLClass = Class(name="OWLClass")
owl_RDFProperty = Class(name="owl::RDFProperty")
owl_OWLObjectProperty = Class(name="owl::OWLObjectProperty")
Property_ = Class(name="Property")
owl_IntersectionClass = Class(name="owl::IntersectionClass")
owl_Property = Class(name="owl::Property")
owl_Individual = Class(name="owl::Individual")
RDFSResource = Class(name="RDFSResource")
owl_OWLAllDifferent = Class(name="owl::OWLAllDifferent")
owl_DatatypeSlot = Class(name="owl::DatatypeSlot")
owl_ObjectSlot = Class(name="owl::ObjectSlot")
owl_OWLDataRange = Class(name="owl::OWLDataRange")
owl_OWLAnnotationProperty = Class(name="owl::OWLAnnotationProperty")
owl_OWLDatatypeProperty = Class(name="owl::OWLDatatypeProperty")
owl_EnumeratedClass = Class(name="owl::EnumeratedClass")
owl_HasValueRestriction = Class(name="owl::HasValueRestriction")
OWLRestriction = Class(name="OWLRestriction")
owl_RDFSResource = Class(name="owl::RDFSResource")
owl_AllValuesFromRestriction = Class(name="owl::AllValuesFromRestriction")
owl_RDFSClass = Class(name="owl::RDFSClass")
owl_SomeValuesFromRestriction = Class(name="owl::SomeValuesFromRestriction")
owl_CardinalityRestriction = Class(name="owl::CardinalityRestriction")
owl_MaxCardinalityRestriction = Class(name="owl::MaxCardinalityRestriction")
owl_MinCardinalityRestriction = Class(name="owl::MinCardinalityRestriction")

# owl_RDFSLiteral class attributes and methods

# owl_OWLOntology class attributes and methods

# Ontology class attributes and methods

# owl_OWLOntologyProperty class attributes and methods

# RDFProperty class attributes and methods

# owl_OWLClass class attributes and methods
owl_OWLClass_deprecated: Property = Property(name="deprecated", type=StringType)
owl_OWLClass.attributes={owl_OWLClass_deprecated}

# RDFSClass class attributes and methods

# owl_UnionClass class attributes and methods

# owl_ComplementClass class attributes and methods

# owl_OWLRestriction class attributes and methods

# OWLClass class attributes and methods

# owl_RDFProperty class attributes and methods

# owl_OWLObjectProperty class attributes and methods
owl_OWLObjectProperty_transitive: Property = Property(name="transitive", type=StringType)
owl_OWLObjectProperty_inverseFunctional: Property = Property(name="inverseFunctional", type=StringType)
owl_OWLObjectProperty_symmetric: Property = Property(name="symmetric", type=StringType)
owl_OWLObjectProperty.attributes={owl_OWLObjectProperty_inverseFunctional, owl_OWLObjectProperty_symmetric, owl_OWLObjectProperty_transitive}

# Property class attributes and methods

# owl_IntersectionClass class attributes and methods

# owl_Property class attributes and methods
owl_Property_deprecated: Property = Property(name="deprecated", type=StringType)
owl_Property_functional: Property = Property(name="functional", type=StringType)
owl_Property.attributes={owl_Property_deprecated, owl_Property_functional}

# owl_Individual class attributes and methods

# RDFSResource class attributes and methods

# owl_OWLAllDifferent class attributes and methods

# owl_DatatypeSlot class attributes and methods

# owl_ObjectSlot class attributes and methods

# owl_OWLDataRange class attributes and methods

# owl_OWLAnnotationProperty class attributes and methods

# owl_OWLDatatypeProperty class attributes and methods

# owl_EnumeratedClass class attributes and methods

# owl_HasValueRestriction class attributes and methods

# OWLRestriction class attributes and methods

# owl_RDFSResource class attributes and methods

# owl_AllValuesFromRestriction class attributes and methods

# owl_RDFSClass class attributes and methods

# owl_SomeValuesFromRestriction class attributes and methods

# owl_CardinalityRestriction class attributes and methods

# owl_MaxCardinalityRestriction class attributes and methods

# owl_MinCardinalityRestriction class attributes and methods

# Relationships
OWLBackwardCompatibleWith1: BinaryAssociation = BinaryAssociation(
    name="OWLBackwardCompatibleWith1",
    ends={
        Property(name="owl_OWLOntology", type=owl_OWLOntology, multiplicity=Multiplicity(1, 1)),
        Property(name="owl_OWLOntology0", type=owl_OWLOntology, multiplicity=Multiplicity(0, 9999))
    }
)
OWLImports3: BinaryAssociation = BinaryAssociation(
    name="OWLImports3",
    ends={
        Property(name="owl_OWLOntology4", type=owl_OWLOntology, multiplicity=Multiplicity(1, 1)),
        Property(name="owl_OWLOntology2", type=owl_OWLOntology, multiplicity=Multiplicity(0, 9999))
    }
)
OWLIncompatibleWith6: BinaryAssociation = BinaryAssociation(
    name="OWLIncompatibleWith6",
    ends={
        Property(name="owl_OWLOntology7", type=owl_OWLOntology, multiplicity=Multiplicity(1, 1)),
        Property(name="owl_OWLOntology5", type=owl_OWLOntology, multiplicity=Multiplicity(0, 9999))
    }
)
OWLPriorVersion9: BinaryAssociation = BinaryAssociation(
    name="OWLPriorVersion9",
    ends={
        Property(name="owl_OWLOntology10", type=owl_OWLOntology, multiplicity=Multiplicity(1, 1)),
        Property(name="owl_OWLOntology8", type=owl_OWLOntology, multiplicity=Multiplicity(0, 9999))
    }
)
OWLVersionInfo11: BinaryAssociation = BinaryAssociation(
    name="OWLVersionInfo11",
    ends={
        Property(name="owl_RDFSLiteral", type=owl_OWLOntology, multiplicity=Multiplicity(1, 1)),
        Property(name="owl_OWLOntology12", type=owl_RDFSLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
invOWLEquivalentClass14: BinaryAssociation = BinaryAssociation(
    name="invOWLEquivalentClass14",
    ends={
        Property(name="OWLClass", type=owl_OWLClass, multiplicity=Multiplicity(1, 1)),
        Property(name="OWLEquivalentClass", type=owl_OWLClass, multiplicity=Multiplicity(0, 9999))
    }
)
OWLEquivalentClass16: BinaryAssociation = BinaryAssociation(
    name="OWLEquivalentClass16",
    ends={
        Property(name="OWLClass17", type=owl_OWLClass, multiplicity=Multiplicity(1, 1)),
        Property(name="invOWLEquivalentClass", type=owl_OWLClass, multiplicity=Multiplicity(0, 9999))
    }
)
OWLDisjointWith19: BinaryAssociation = BinaryAssociation(
    name="OWLDisjointWith19",
    ends={
        Property(name="OWLClass20", type=owl_OWLClass, multiplicity=Multiplicity(1, 1)),
        Property(name="invOWLDisjointWith", type=owl_OWLClass, multiplicity=Multiplicity(0, 9999))
    }
)
invOWLDisjointWith22: BinaryAssociation = BinaryAssociation(
    name="invOWLDisjointWith22",
    ends={
        Property(name="OWLClass23", type=owl_OWLClass, multiplicity=Multiplicity(1, 1)),
        Property(name="OWLDisjointWith", type=owl_OWLClass, multiplicity=Multiplicity(0, 9999))
    }
)
refByUnionClass25: BinaryAssociation = BinaryAssociation(
    name="refByUnionClass25",
    ends={
        Property(name="UnionClass", type=owl_OWLClass, multiplicity=Multiplicity(1, 1)),
        Property(name="OWLUnionOf", type=owl_UnionClass, multiplicity=Multiplicity(0, 9999))
    }
)
invOWLComplementOf26: BinaryAssociation = BinaryAssociation(
    name="invOWLComplementOf26",
    ends={
        Property(name="ComplementClass", type=owl_OWLClass, multiplicity=Multiplicity(1, 1)),
        Property(name="OWLComplementOf", type=owl_ComplementClass, multiplicity=Multiplicity(0, 9999))
    }
)
OWLOnProperty27: BinaryAssociation = BinaryAssociation(
    name="OWLOnProperty27",
    ends={
        Property(name="rdfs.ecoreRDFProperty", type=owl_OWLRestriction, multiplicity=Multiplicity(1, 1)),
        Property(name="refByRestriction", type=owl_RDFProperty, multiplicity=Multiplicity(1, 1))
    }
)
refByIntersectionClass24: BinaryAssociation = BinaryAssociation(
    name="refByIntersectionClass24",
    ends={
        Property(name="IntersectionClass", type=owl_OWLClass, multiplicity=Multiplicity(1, 1)),
        Property(name="OWLIntersectionOf", type=owl_IntersectionClass, multiplicity=Multiplicity(0, 9999))
    }
)
OWLInverseOf29: BinaryAssociation = BinaryAssociation(
    name="OWLInverseOf29",
    ends={
        Property(name="OWLObjectProperty", type=owl_OWLObjectProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="invOWLInverseOf", type=owl_OWLObjectProperty, multiplicity=Multiplicity(0, 1))
    }
)
invOWLInverseOf31: BinaryAssociation = BinaryAssociation(
    name="invOWLInverseOf31",
    ends={
        Property(name="OWLObjectProperty32", type=owl_OWLObjectProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="OWLInverseOf", type=owl_OWLObjectProperty, multiplicity=Multiplicity(0, 9999))
    }
)
OWLEquivalentProperty34: BinaryAssociation = BinaryAssociation(
    name="OWLEquivalentProperty34",
    ends={
        Property(name="Property", type=owl_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="invOWLEquivalentProperty", type=owl_Property, multiplicity=Multiplicity(0, 9999))
    }
)
invOWLEquivalentProperty36: BinaryAssociation = BinaryAssociation(
    name="invOWLEquivalentProperty36",
    ends={
        Property(name="Property37", type=owl_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="OWLEquivalentProperty", type=owl_Property, multiplicity=Multiplicity(0, 9999))
    }
)
OWLDifferentFrom39: BinaryAssociation = BinaryAssociation(
    name="OWLDifferentFrom39",
    ends={
        Property(name="Individual", type=owl_Individual, multiplicity=Multiplicity(1, 1)),
        Property(name="invOWLDifferentFrom", type=owl_Individual, multiplicity=Multiplicity(0, 9999))
    }
)
invOWLDifferentFrom41: BinaryAssociation = BinaryAssociation(
    name="invOWLDifferentFrom41",
    ends={
        Property(name="Individual42", type=owl_Individual, multiplicity=Multiplicity(1, 1)),
        Property(name="OWLDifferentFrom", type=owl_Individual, multiplicity=Multiplicity(0, 9999))
    }
)
refByOWLDistinctMembers43: BinaryAssociation = BinaryAssociation(
    name="refByOWLDistinctMembers43",
    ends={
        Property(name="OWLAllDifferent", type=owl_Individual, multiplicity=Multiplicity(1, 1)),
        Property(name="OWLDistinctMembers", type=owl_OWLAllDifferent, multiplicity=Multiplicity(0, 9999))
    }
)
invOWLSameAs48: BinaryAssociation = BinaryAssociation(
    name="invOWLSameAs48",
    ends={
        Property(name="Individual49", type=owl_Individual, multiplicity=Multiplicity(1, 1)),
        Property(name="OWLSameAs", type=owl_Individual, multiplicity=Multiplicity(0, 9999))
    }
)
datatypeSlot50: BinaryAssociation = BinaryAssociation(
    name="datatypeSlot50",
    ends={
        Property(name="DatatypeSlot", type=owl_Individual, multiplicity=Multiplicity(1, 1)),
        Property(name="Individual51", type=owl_DatatypeSlot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
objectSlot52: BinaryAssociation = BinaryAssociation(
    name="objectSlot52",
    ends={
        Property(name="ObjectSlot", type=owl_Individual, multiplicity=Multiplicity(1, 1)),
        Property(name="Individual53", type=owl_ObjectSlot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
OWLDistinctMembers54: BinaryAssociation = BinaryAssociation(
    name="OWLDistinctMembers54",
    ends={
        Property(name="Individual55", type=owl_OWLAllDifferent, multiplicity=Multiplicity(1, 1)),
        Property(name="refByOWLDistinctMembers", type=owl_Individual, multiplicity=Multiplicity(2, 9999))
    }
)
OWLSameAs45: BinaryAssociation = BinaryAssociation(
    name="OWLSameAs45",
    ends={
        Property(name="Individual46", type=owl_Individual, multiplicity=Multiplicity(1, 1)),
        Property(name="invOWLSameAs", type=owl_Individual, multiplicity=Multiplicity(0, 9999))
    }
)
Individual58: BinaryAssociation = BinaryAssociation(
    name="Individual58",
    ends={
        Property(name="Individual59", type=owl_DatatypeSlot, multiplicity=Multiplicity(1, 1)),
        Property(name="datatypeSlot", type=owl_Individual, multiplicity=Multiplicity(0, 1))
    }
)
content60: BinaryAssociation = BinaryAssociation(
    name="content60",
    ends={
        Property(name="rdfs.ecoreRDFSLiteral", type=owl_DatatypeSlot, multiplicity=Multiplicity(1, 1)),
        Property(name="DatatypeSlot61", type=owl_RDFSLiteral, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
OWLOneOf56: BinaryAssociation = BinaryAssociation(
    name="OWLOneOf56",
    ends={
        Property(name="owl_RDFSLiteral57", type=owl_OWLDataRange, multiplicity=Multiplicity(1, 1)),
        Property(name="owl_OWLDataRange", type=owl_RDFSLiteral, multiplicity=Multiplicity(1, 9999))
    }
)
content65: BinaryAssociation = BinaryAssociation(
    name="content65",
    ends={
        Property(name="owl_Individual", type=owl_ObjectSlot, multiplicity=Multiplicity(1, 1)),
        Property(name="owl_ObjectSlot", type=owl_Individual, multiplicity=Multiplicity(1, 9999))
    }
)
property66: BinaryAssociation = BinaryAssociation(
    name="property66",
    ends={
        Property(name="owl_OWLObjectProperty", type=owl_ObjectSlot, multiplicity=Multiplicity(1, 1)),
        Property(name="owl_ObjectSlot67", type=owl_OWLObjectProperty, multiplicity=Multiplicity(1, 1))
    }
)
OWLOneOf68: BinaryAssociation = BinaryAssociation(
    name="OWLOneOf68",
    ends={
        Property(name="owl_Individual69", type=owl_EnumeratedClass, multiplicity=Multiplicity(1, 1)),
        Property(name="owl_EnumeratedClass", type=owl_Individual, multiplicity=Multiplicity(0, 9999))
    }
)
property62: BinaryAssociation = BinaryAssociation(
    name="property62",
    ends={
        Property(name="owl_OWLDatatypeProperty", type=owl_DatatypeSlot, multiplicity=Multiplicity(1, 1)),
        Property(name="owl_DatatypeSlot", type=owl_OWLDatatypeProperty, multiplicity=Multiplicity(1, 1))
    }
)
Individual63: BinaryAssociation = BinaryAssociation(
    name="Individual63",
    ends={
        Property(name="Individual64", type=owl_ObjectSlot, multiplicity=Multiplicity(1, 1)),
        Property(name="objectSlot", type=owl_Individual, multiplicity=Multiplicity(0, 1))
    }
)
OWLHasValue74: BinaryAssociation = BinaryAssociation(
    name="OWLHasValue74",
    ends={
        Property(name="owl_RDFSResource", type=owl_HasValueRestriction, multiplicity=Multiplicity(1, 1)),
        Property(name="owl_HasValueRestriction", type=owl_RDFSResource, multiplicity=Multiplicity(1, 1))
    }
)
OWLAllValuesFrom75: BinaryAssociation = BinaryAssociation(
    name="OWLAllValuesFrom75",
    ends={
        Property(name="rdfs.ecoreRDFSClass", type=owl_AllValuesFromRestriction, multiplicity=Multiplicity(1, 1)),
        Property(name="refByAVFRestriction", type=owl_RDFSClass, multiplicity=Multiplicity(1, 1))
    }
)
OWLSomeValuesFrom76: BinaryAssociation = BinaryAssociation(
    name="OWLSomeValuesFrom76",
    ends={
        Property(name="rdfs.ecoreRDFSClass77", type=owl_SomeValuesFromRestriction, multiplicity=Multiplicity(1, 1)),
        Property(name="refBySVFRestriction", type=owl_RDFSClass, multiplicity=Multiplicity(1, 1))
    }
)
OWLCardinality78: BinaryAssociation = BinaryAssociation(
    name="OWLCardinality78",
    ends={
        Property(name="owl_RDFSLiteral79", type=owl_CardinalityRestriction, multiplicity=Multiplicity(1, 1)),
        Property(name="owl_CardinalityRestriction", type=owl_RDFSLiteral, multiplicity=Multiplicity(1, 1))
    }
)
OWLIntersectionOf70: BinaryAssociation = BinaryAssociation(
    name="OWLIntersectionOf70",
    ends={
        Property(name="OWLClass71", type=owl_IntersectionClass, multiplicity=Multiplicity(1, 1)),
        Property(name="refByIntersectionClass", type=owl_OWLClass, multiplicity=Multiplicity(0, 9999))
    }
)
OWLUnionOf72: BinaryAssociation = BinaryAssociation(
    name="OWLUnionOf72",
    ends={
        Property(name="OWLClass73", type=owl_UnionClass, multiplicity=Multiplicity(1, 1)),
        Property(name="refByUnionClass", type=owl_OWLClass, multiplicity=Multiplicity(0, 9999))
    }
)
OWLMaxCardinality80: BinaryAssociation = BinaryAssociation(
    name="OWLMaxCardinality80",
    ends={
        Property(name="owl_RDFSLiteral81", type=owl_MaxCardinalityRestriction, multiplicity=Multiplicity(1, 1)),
        Property(name="owl_MaxCardinalityRestriction", type=owl_RDFSLiteral, multiplicity=Multiplicity(1, 1))
    }
)
OWLMinCardinality82: BinaryAssociation = BinaryAssociation(
    name="OWLMinCardinality82",
    ends={
        Property(name="owl_RDFSLiteral83", type=owl_MinCardinalityRestriction, multiplicity=Multiplicity(1, 1)),
        Property(name="owl_MinCardinalityRestriction", type=owl_RDFSLiteral, multiplicity=Multiplicity(1, 1))
    }
)
OWLComplementOf84: BinaryAssociation = BinaryAssociation(
    name="OWLComplementOf84",
    ends={
        Property(name="OWLClass85", type=owl_ComplementClass, multiplicity=Multiplicity(1, 1)),
        Property(name="invOWLComplementOf", type=owl_OWLClass, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_owl_OWLOntology_Ontology = Generalization(general=Ontology, specific=owl_OWLOntology)
gen_owl_OWLOntologyProperty_RDFProperty = Generalization(general=RDFProperty, specific=owl_OWLOntologyProperty)
gen_owl_OWLClass_RDFSClass = Generalization(general=RDFSClass, specific=owl_OWLClass)
gen_owl_OWLRestriction_OWLClass = Generalization(general=OWLClass, specific=owl_OWLRestriction)
gen_owl_Property_RDFProperty = Generalization(general=RDFProperty, specific=owl_Property)
gen_owl_OWLObjectProperty_Property = Generalization(general=Property_, specific=owl_OWLObjectProperty)
gen_owl_Individual_RDFSResource = Generalization(general=RDFSResource, specific=owl_Individual)
gen_owl_OWLAllDifferent_RDFSResource = Generalization(general=RDFSResource, specific=owl_OWLAllDifferent)
gen_owl_OWLDataRange_RDFSClass = Generalization(general=RDFSClass, specific=owl_OWLDataRange)
gen_owl_OWLAnnotationProperty_RDFProperty = Generalization(general=RDFProperty, specific=owl_OWLAnnotationProperty)
gen_owl_EnumeratedClass_OWLClass = Generalization(general=OWLClass, specific=owl_EnumeratedClass)
gen_owl_IntersectionClass_OWLClass = Generalization(general=OWLClass, specific=owl_IntersectionClass)
gen_owl_HasValueRestriction_OWLRestriction = Generalization(general=OWLRestriction, specific=owl_HasValueRestriction)
gen_owl_AllValuesFromRestriction_OWLRestriction = Generalization(general=OWLRestriction, specific=owl_AllValuesFromRestriction)
gen_owl_SomeValuesFromRestriction_OWLRestriction = Generalization(general=OWLRestriction, specific=owl_SomeValuesFromRestriction)
gen_owl_CardinalityRestriction_OWLRestriction = Generalization(general=OWLRestriction, specific=owl_CardinalityRestriction)
gen_owl_MaxCardinalityRestriction_OWLRestriction = Generalization(general=OWLRestriction, specific=owl_MaxCardinalityRestriction)
gen_owl_UnionClass_OWLClass = Generalization(general=OWLClass, specific=owl_UnionClass)
gen_owl_OWLDatatypeProperty_Property = Generalization(general=Property_, specific=owl_OWLDatatypeProperty)
gen_owl_MinCardinalityRestriction_OWLRestriction = Generalization(general=OWLRestriction, specific=owl_MinCardinalityRestriction)
gen_owl_ComplementClass_OWLClass = Generalization(general=OWLClass, specific=owl_ComplementClass)

# Domain Model
domain_model = DomainModel(
    name="owl",
    types={owl_RDFSLiteral, owl_OWLOntology, Ontology, owl_OWLOntologyProperty, RDFProperty, owl_OWLClass, RDFSClass, owl_UnionClass, owl_ComplementClass, owl_OWLRestriction, OWLClass, owl_RDFProperty, owl_OWLObjectProperty, Property_, owl_IntersectionClass, owl_Property, owl_Individual, RDFSResource, owl_OWLAllDifferent, owl_DatatypeSlot, owl_ObjectSlot, owl_OWLDataRange, owl_OWLAnnotationProperty, owl_OWLDatatypeProperty, owl_EnumeratedClass, owl_HasValueRestriction, OWLRestriction, owl_RDFSResource, owl_AllValuesFromRestriction, owl_RDFSClass, owl_SomeValuesFromRestriction, owl_CardinalityRestriction, owl_MaxCardinalityRestriction, owl_MinCardinalityRestriction},
    associations={OWLBackwardCompatibleWith1, OWLImports3, OWLIncompatibleWith6, OWLPriorVersion9, OWLVersionInfo11, invOWLEquivalentClass14, OWLEquivalentClass16, OWLDisjointWith19, invOWLDisjointWith22, refByUnionClass25, invOWLComplementOf26, OWLOnProperty27, refByIntersectionClass24, OWLInverseOf29, invOWLInverseOf31, OWLEquivalentProperty34, invOWLEquivalentProperty36, OWLDifferentFrom39, invOWLDifferentFrom41, refByOWLDistinctMembers43, invOWLSameAs48, datatypeSlot50, objectSlot52, OWLDistinctMembers54, OWLSameAs45, Individual58, content60, OWLOneOf56, content65, property66, OWLOneOf68, property62, Individual63, OWLHasValue74, OWLAllValuesFrom75, OWLSomeValuesFrom76, OWLCardinality78, OWLIntersectionOf70, OWLUnionOf72, OWLMaxCardinality80, OWLMinCardinality82, OWLComplementOf84},
    generalizations={gen_owl_OWLOntology_Ontology, gen_owl_OWLOntologyProperty_RDFProperty, gen_owl_OWLClass_RDFSClass, gen_owl_OWLRestriction_OWLClass, gen_owl_Property_RDFProperty, gen_owl_OWLObjectProperty_Property, gen_owl_Individual_RDFSResource, gen_owl_OWLAllDifferent_RDFSResource, gen_owl_OWLDataRange_RDFSClass, gen_owl_OWLAnnotationProperty_RDFProperty, gen_owl_EnumeratedClass_OWLClass, gen_owl_IntersectionClass_OWLClass, gen_owl_HasValueRestriction_OWLRestriction, gen_owl_AllValuesFromRestriction_OWLRestriction, gen_owl_SomeValuesFromRestriction_OWLRestriction, gen_owl_CardinalityRestriction_OWLRestriction, gen_owl_MaxCardinalityRestriction_OWLRestriction, gen_owl_UnionClass_OWLClass, gen_owl_OWLDatatypeProperty_Property, gen_owl_MinCardinalityRestriction_OWLRestriction, gen_owl_ComplementClass_OWLClass},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)