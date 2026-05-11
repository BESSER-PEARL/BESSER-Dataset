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
dependencies_EPackage = Class(name="dependencies_EPackage")
dependencies_Required = Class(name="dependencies_Required")
dependencies_Graph = Class(name="dependencies_Graph")
NamedElement = Class(name="NamedElement")
dependencies_Domain = Class(name="dependencies_Domain")
dependencies_Equivalence = Class(name="dependencies_Equivalence")
dependencies_Operation = Class(name="dependencies_Operation")
dependencies_SemiRequired = Class(name="dependencies_SemiRequired")
dependencies_Create = Class(name="dependencies_Create")
dependencies_RCPackage = Class(name="dependencies_RCPackage")
dependencies_Block = Class(name="dependencies_Block", is_abstract=True)
dependencies_CoreClass = Class(name="dependencies_CoreClass")
Block = Class(name="Block")
Vertex = Class(name="Vertex")
dependencies_EClass = Class(name="dependencies_EClass")
dependencies_Vertex = Class(name="dependencies_Vertex", is_abstract=True)
dependencies_Edge = Class(name="dependencies_Edge")
dependencies_SimpleTerm = Class(name="dependencies_SimpleTerm")
dependencies_RightTerm = Class(name="dependencies_RightTerm")
dependencies_Term = Class(name="dependencies_Term", is_abstract=True)
Term = Class(name="Term")
dependencies_NamedElement = Class(name="dependencies_NamedElement", is_abstract=True)

# dependencies_EPackage class attributes and methods

# dependencies_Required class attributes and methods

# dependencies_Graph class attributes and methods
dependencies_Graph_priority: Property = Property(name="priority", type=StringType)
dependencies_Graph.attributes={dependencies_Graph_priority}

# NamedElement class attributes and methods

# dependencies_Domain class attributes and methods

# dependencies_Equivalence class attributes and methods

# dependencies_Operation class attributes and methods
dependencies_Operation_operationType: Property = Property(name="operationType", type=StringType)
dependencies_Operation.attributes={dependencies_Operation_operationType}

# dependencies_SemiRequired class attributes and methods

# dependencies_Create class attributes and methods

# dependencies_RCPackage class attributes and methods

# dependencies_Block class attributes and methods

# dependencies_CoreClass class attributes and methods

# Block class attributes and methods

# Vertex class attributes and methods

# dependencies_EClass class attributes and methods

# dependencies_Vertex class attributes and methods

# dependencies_Edge class attributes and methods
dependencies_Edge_referredTo: Property = Property(name="referredTo", type=BooleanType)
dependencies_Edge_equal: Property = Property(name="equal", type=BooleanType)
dependencies_Edge.attributes={dependencies_Edge_equal, dependencies_Edge_referredTo}

# dependencies_SimpleTerm class attributes and methods

# dependencies_RightTerm class attributes and methods
dependencies_RightTerm_value: Property = Property(name="value", type=StringType)
dependencies_RightTerm.attributes={dependencies_RightTerm_value}

# dependencies_Term class attributes and methods

# Term class attributes and methods

# dependencies_NamedElement class attributes and methods
dependencies_NamedElement_name: Property = Property(name="name", type=StringType)
dependencies_NamedElement.attributes={dependencies_NamedElement_name}

# Relationships
modelPackage3: BinaryAssociation = BinaryAssociation(
    name="modelPackage3",
    ends={
        Property(name="dependencies_EPackage", type=dependencies_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="dependencies_Domain4", type=dependencies_EPackage, multiplicity=Multiplicity(1, 1))
    }
)
required5: BinaryAssociation = BinaryAssociation(
    name="required5",
    ends={
        Property(name="dependencies_Required", type=dependencies_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="dependencies_Domain6", type=dependencies_Required, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modelDomains0: BinaryAssociation = BinaryAssociation(
    name="modelDomains0",
    ends={
        Property(name="dependencies_Domain", type=dependencies_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="dependencies_Graph", type=dependencies_Domain, multiplicity=Multiplicity(1, 2), is_composite=True)
    }
)
modelEquivalence1: BinaryAssociation = BinaryAssociation(
    name="modelEquivalence1",
    ends={
        Property(name="dependencies_Equivalence", type=dependencies_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="dependencies_Graph2", type=dependencies_Equivalence, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
role24: BinaryAssociation = BinaryAssociation(
    name="role24",
    ends={
        Property(name="dependencies_EClass26", type=dependencies_SimpleTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="dependencies_SimpleTerm25", type=dependencies_EClass, multiplicity=Multiplicity(0, 1))
    }
)
operation27: BinaryAssociation = BinaryAssociation(
    name="operation27",
    ends={
        Property(name="dependencies_Operation", type=dependencies_RightTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="dependencies_RightTerm28", type=dependencies_Operation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
semiRequired7: BinaryAssociation = BinaryAssociation(
    name="semiRequired7",
    ends={
        Property(name="dependencies_SemiRequired", type=dependencies_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="dependencies_Domain8", type=dependencies_SemiRequired, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
create9: BinaryAssociation = BinaryAssociation(
    name="create9",
    ends={
        Property(name="dependencies_Create", type=dependencies_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="dependencies_Domain10", type=dependencies_Create, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rcPackage11: BinaryAssociation = BinaryAssociation(
    name="rcPackage11",
    ends={
        Property(name="dependencies_RCPackage", type=dependencies_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="dependencies_Domain12", type=dependencies_RCPackage, multiplicity=Multiplicity(1, 1))
    }
)
coreClasses13: BinaryAssociation = BinaryAssociation(
    name="coreClasses13",
    ends={
        Property(name="dependencies_CoreClass", type=dependencies_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="dependencies_Block", type=dependencies_CoreClass, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
type14: BinaryAssociation = BinaryAssociation(
    name="type14",
    ends={
        Property(name="dependencies_EClass", type=dependencies_CoreClass, multiplicity=Multiplicity(1, 1)),
        Property(name="dependencies_CoreClass15", type=dependencies_EClass, multiplicity=Multiplicity(1, 1))
    }
)
edges16: BinaryAssociation = BinaryAssociation(
    name="edges16",
    ends={
        Property(name="dependencies_Edge", type=dependencies_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="dependencies_Vertex", type=dependencies_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
simpleTerm17: BinaryAssociation = BinaryAssociation(
    name="simpleTerm17",
    ends={
        Property(name="dependencies_SimpleTerm", type=dependencies_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="dependencies_Edge18", type=dependencies_SimpleTerm, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightTerm19: BinaryAssociation = BinaryAssociation(
    name="rightTerm19",
    ends={
        Property(name="dependencies_RightTerm", type=dependencies_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="dependencies_Edge20", type=dependencies_RightTerm, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
coreClass21: BinaryAssociation = BinaryAssociation(
    name="coreClass21",
    ends={
        Property(name="dependencies_CoreClass23", type=dependencies_SimpleTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="dependencies_SimpleTerm22", type=dependencies_CoreClass, multiplicity=Multiplicity(0, 1))
    }
)
simpleTerms29: BinaryAssociation = BinaryAssociation(
    name="simpleTerms29",
    ends={
        Property(name="dependencies_SimpleTerm31", type=dependencies_RightTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="dependencies_RightTerm30", type=dependencies_SimpleTerm, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rightTerms32: BinaryAssociation = BinaryAssociation(
    name="rightTerms32",
    ends={
        Property(name="dependencies_RightTerm34", type=dependencies_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="dependencies_Operation33", type=dependencies_RightTerm, multiplicity=Multiplicity(1, 2), is_composite=True)
    }
)

# Generalizations
gen_dependencies_Graph_NamedElement = Generalization(general=NamedElement, specific=dependencies_Graph)
gen_dependencies_Domain_NamedElement = Generalization(general=NamedElement, specific=dependencies_Domain)
gen_dependencies_RightTerm_Term = Generalization(general=Term, specific=dependencies_RightTerm)
gen_dependencies_Required_Block = Generalization(general=Block, specific=dependencies_Required)
gen_dependencies_SemiRequired_Block = Generalization(general=Block, specific=dependencies_SemiRequired)
gen_dependencies_Create_Block = Generalization(general=Block, specific=dependencies_Create)
gen_dependencies_Equivalence_Vertex = Generalization(general=Vertex, specific=dependencies_Equivalence)
gen_dependencies_CoreClass_Vertex = Generalization(general=Vertex, specific=dependencies_CoreClass)
gen_dependencies_CoreClass_NamedElement = Generalization(general=NamedElement, specific=dependencies_CoreClass)
gen_dependencies_SimpleTerm_Term = Generalization(general=Term, specific=dependencies_SimpleTerm)

# Domain Model
domain_model = DomainModel(
    name="dependencies",
    types={dependencies_EPackage, dependencies_Required, dependencies_Graph, NamedElement, dependencies_Domain, dependencies_Equivalence, dependencies_Operation, dependencies_SemiRequired, dependencies_Create, dependencies_RCPackage, dependencies_Block, dependencies_CoreClass, Block, Vertex, dependencies_EClass, dependencies_Vertex, dependencies_Edge, dependencies_SimpleTerm, dependencies_RightTerm, dependencies_Term, Term, dependencies_NamedElement},
    associations={modelPackage3, required5, modelDomains0, modelEquivalence1, role24, operation27, semiRequired7, create9, rcPackage11, coreClasses13, type14, edges16, simpleTerm17, rightTerm19, coreClass21, simpleTerms29, rightTerms32},
    generalizations={gen_dependencies_Graph_NamedElement, gen_dependencies_Domain_NamedElement, gen_dependencies_RightTerm_Term, gen_dependencies_Required_Block, gen_dependencies_SemiRequired_Block, gen_dependencies_Create_Block, gen_dependencies_Equivalence_Vertex, gen_dependencies_CoreClass_Vertex, gen_dependencies_CoreClass_NamedElement, gen_dependencies_SimpleTerm_Term},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)