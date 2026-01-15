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

# Enumerations
EnumModular: Enumeration = Enumeration(
    name="EnumModular",
    literals={
            EnumerationLiteral(name="Default"),
			EnumerationLiteral(name="Project"),
			EnumerationLiteral(name="Package"),
			EnumerationLiteral(name="Unit"),
			EnumerationLiteral(name="InsideUnit"),
			EnumerationLiteral(name="InsidePackage"),
			EnumerationLiteral(name="InsideProject"),
			EnumerationLiteral(name="AbstractPackageUnit"),
			EnumerationLiteral(name="AbstractPackage"),
			EnumerationLiteral(name="AbstractUnit"),
			EnumerationLiteral(name="RecursionPackage"),
			EnumerationLiteral(name="RecursionAbstractPackage"),
			EnumerationLiteral(name="RecursionUnit"),
			EnumerationLiteral(name="RecursionAbstractUnit")
    }
)

# Classes
MetaModelGraph_Graph = Class(name="MetaModelGraph::Graph")
MetaModelGraph_SubGraph = Class(name="MetaModelGraph::SubGraph")
MetaModelGraph_EClass = Class(name="MetaModelGraph::EClass")
MetaModelGraph_Node = Class(name="MetaModelGraph::Node")
MetaModelGraph_Relation = Class(name="MetaModelGraph::Relation", is_abstract=True)
MetaModelGraph_Reference = Class(name="MetaModelGraph::Reference")
MetaModelGraph_SubClass = Class(name="MetaModelGraph::SubClass")
MetaModelGraph_Composition = Class(name="MetaModelGraph::Composition")
MetaModelGraph_EAttribute = Class(name="MetaModelGraph::EAttribute")
Relation = Class(name="Relation")
MetaModelGraph_EReference = Class(name="MetaModelGraph::EReference")

# MetaModelGraph_Graph class attributes and methods
MetaModelGraph_Graph_amountEClasses: Property = Property(name="amountEClasses", type=IntegerType)
MetaModelGraph_Graph_amountAbstractEClasses: Property = Property(name="amountAbstractEClasses", type=IntegerType)
MetaModelGraph_Graph_amountConcreteEClass: Property = Property(name="amountConcreteEClass", type=IntegerType)
MetaModelGraph_Graph.attributes={MetaModelGraph_Graph_amountEClasses, MetaModelGraph_Graph_amountConcreteEClass, MetaModelGraph_Graph_amountAbstractEClasses}

# MetaModelGraph_SubGraph class attributes and methods
MetaModelGraph_SubGraph_height: Property = Property(name="height", type=IntegerType)
MetaModelGraph_SubGraph_amountOfConcreteEClass: Property = Property(name="amountOfConcreteEClass", type=IntegerType)
MetaModelGraph_SubGraph_amountEClassesOut: Property = Property(name="amountEClassesOut", type=IntegerType)
MetaModelGraph_SubGraph_amountOfAbstractEClass: Property = Property(name="amountOfAbstractEClass", type=IntegerType)
MetaModelGraph_SubGraph_amountOfParentEClass: Property = Property(name="amountOfParentEClass", type=IntegerType)
MetaModelGraph_SubGraph_amountOfParentAbstractEClass: Property = Property(name="amountOfParentAbstractEClass", type=IntegerType)
MetaModelGraph_SubGraph_amountPackages: Property = Property(name="amountPackages", type=IntegerType)
MetaModelGraph_SubGraph_amountUnits: Property = Property(name="amountUnits", type=IntegerType)
MetaModelGraph_SubGraph_amountRecursionUnits: Property = Property(name="amountRecursionUnits", type=IntegerType)
MetaModelGraph_SubGraph_amountOfRecursionPackages: Property = Property(name="amountOfRecursionPackages", type=IntegerType)
MetaModelGraph_SubGraph.attributes={MetaModelGraph_SubGraph_amountOfParentAbstractEClass, MetaModelGraph_SubGraph_amountOfRecursionPackages, MetaModelGraph_SubGraph_amountOfAbstractEClass, MetaModelGraph_SubGraph_amountOfParentEClass, MetaModelGraph_SubGraph_height, MetaModelGraph_SubGraph_amountEClassesOut, MetaModelGraph_SubGraph_amountOfConcreteEClass, MetaModelGraph_SubGraph_amountUnits, MetaModelGraph_SubGraph_amountRecursionUnits, MetaModelGraph_SubGraph_amountPackages}

# MetaModelGraph_EClass class attributes and methods

# MetaModelGraph_Node class attributes and methods
MetaModelGraph_Node_enumModularNotation: Property = Property(name="enumModularNotation", type=StringType)
MetaModelGraph_Node_icon: Property = Property(name="icon", type=StringType)
MetaModelGraph_Node_extension: Property = Property(name="extension", type=StringType)
MetaModelGraph_Node_insideRecursion: Property = Property(name="insideRecursion", type=BooleanType)
MetaModelGraph_Node.attributes={MetaModelGraph_Node_icon, MetaModelGraph_Node_enumModularNotation, MetaModelGraph_Node_insideRecursion, MetaModelGraph_Node_extension}

# MetaModelGraph_Relation class attributes and methods

# MetaModelGraph_Reference class attributes and methods

# MetaModelGraph_SubClass class attributes and methods

# MetaModelGraph_Composition class attributes and methods

# MetaModelGraph_EAttribute class attributes and methods

# Relation class attributes and methods

# MetaModelGraph_EReference class attributes and methods

# Relationships
subgraph0: BinaryAssociation = BinaryAssociation(
    name="subgraph0",
    ends={
        Property(name="MetaModelGraph_SubGraph", type=MetaModelGraph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="MetaModelGraph_Graph", type=MetaModelGraph_SubGraph, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eClassList1: BinaryAssociation = BinaryAssociation(
    name="eClassList1",
    ends={
        Property(name="MetaModelGraph_EClass", type=MetaModelGraph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="MetaModelGraph_Graph2", type=MetaModelGraph_EClass, multiplicity=Multiplicity(0, 9999))
    }
)
eClassAbstract3: BinaryAssociation = BinaryAssociation(
    name="eClassAbstract3",
    ends={
        Property(name="MetaModelGraph_EClass5", type=MetaModelGraph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="MetaModelGraph_Graph4", type=MetaModelGraph_EClass, multiplicity=Multiplicity(0, 9999))
    }
)
relations8: BinaryAssociation = BinaryAssociation(
    name="relations8",
    ends={
        Property(name="MetaModelGraph_Relation", type=MetaModelGraph_SubGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="MetaModelGraph_SubGraph9", type=MetaModelGraph_Relation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eClassesListOut10: BinaryAssociation = BinaryAssociation(
    name="eClassesListOut10",
    ends={
        Property(name="MetaModelGraph_EClass12", type=MetaModelGraph_SubGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="MetaModelGraph_SubGraph11", type=MetaModelGraph_EClass, multiplicity=Multiplicity(0, 9999))
    }
)
root13: BinaryAssociation = BinaryAssociation(
    name="root13",
    ends={
        Property(name="MetaModelGraph_Node15", type=MetaModelGraph_SubGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="MetaModelGraph_SubGraph14", type=MetaModelGraph_Node, multiplicity=Multiplicity(0, 1))
    }
)
nodes6: BinaryAssociation = BinaryAssociation(
    name="nodes6",
    ends={
        Property(name="MetaModelGraph_Node", type=MetaModelGraph_SubGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="MetaModelGraph_SubGraph7", type=MetaModelGraph_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
references17: BinaryAssociation = BinaryAssociation(
    name="references17",
    ends={
        Property(name="MetaModelGraph_Reference", type=MetaModelGraph_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="MetaModelGraph_Node18", type=MetaModelGraph_Reference, multiplicity=Multiplicity(0, 9999))
    }
)
subClasses19: BinaryAssociation = BinaryAssociation(
    name="subClasses19",
    ends={
        Property(name="MetaModelGraph_SubClass", type=MetaModelGraph_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="MetaModelGraph_Node20", type=MetaModelGraph_SubClass, multiplicity=Multiplicity(0, 9999))
    }
)
eClass21: BinaryAssociation = BinaryAssociation(
    name="eClass21",
    ends={
        Property(name="MetaModelGraph_EClass23", type=MetaModelGraph_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="MetaModelGraph_Node22", type=MetaModelGraph_EClass, multiplicity=Multiplicity(0, 1))
    }
)
relations24: BinaryAssociation = BinaryAssociation(
    name="relations24",
    ends={
        Property(name="Relation", type=MetaModelGraph_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=MetaModelGraph_Relation, multiplicity=Multiplicity(0, 9999))
    }
)
listNodes26: BinaryAssociation = BinaryAssociation(
    name="listNodes26",
    ends={
        Property(name="MetaModelGraph_Node27", type=MetaModelGraph_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="MetaModelGraph_Node25", type=MetaModelGraph_Node, multiplicity=Multiplicity(0, 9999))
    }
)
directSubclasses28: BinaryAssociation = BinaryAssociation(
    name="directSubclasses28",
    ends={
        Property(name="MetaModelGraph_SubClass30", type=MetaModelGraph_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="MetaModelGraph_Node29", type=MetaModelGraph_SubClass, multiplicity=Multiplicity(0, 9999))
    }
)
compositions16: BinaryAssociation = BinaryAssociation(
    name="compositions16",
    ends={
        Property(name="Composition", type=MetaModelGraph_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="parentNode", type=MetaModelGraph_Composition, multiplicity=Multiplicity(0, 9999))
    }
)
name33: BinaryAssociation = BinaryAssociation(
    name="name33",
    ends={
        Property(name="MetaModelGraph_EAttribute", type=MetaModelGraph_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="MetaModelGraph_Node34", type=MetaModelGraph_EAttribute, multiplicity=Multiplicity(0, 1))
    }
)
target35: BinaryAssociation = BinaryAssociation(
    name="target35",
    ends={
        Property(name="Node", type=MetaModelGraph_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="relations", type=MetaModelGraph_Node, multiplicity=Multiplicity(0, 1))
    }
)
eReference36: BinaryAssociation = BinaryAssociation(
    name="eReference36",
    ends={
        Property(name="MetaModelGraph_EReference", type=MetaModelGraph_Composition, multiplicity=Multiplicity(1, 1)),
        Property(name="MetaModelGraph_Composition37", type=MetaModelGraph_EReference, multiplicity=Multiplicity(0, 1))
    }
)
parentNode38: BinaryAssociation = BinaryAssociation(
    name="parentNode38",
    ends={
        Property(name="Node39", type=MetaModelGraph_Composition, multiplicity=Multiplicity(1, 1)),
        Property(name="compositions", type=MetaModelGraph_Node, multiplicity=Multiplicity(0, 1))
    }
)
directComposition31: BinaryAssociation = BinaryAssociation(
    name="directComposition31",
    ends={
        Property(name="MetaModelGraph_Composition", type=MetaModelGraph_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="MetaModelGraph_Node32", type=MetaModelGraph_Composition, multiplicity=Multiplicity(0, 9999))
    }
)
eReference40: BinaryAssociation = BinaryAssociation(
    name="eReference40",
    ends={
        Property(name="MetaModelGraph_EReference42", type=MetaModelGraph_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="MetaModelGraph_Reference41", type=MetaModelGraph_EReference, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_MetaModelGraph_Composition_Relation = Generalization(general=Relation, specific=MetaModelGraph_Composition)
gen_MetaModelGraph_Reference_Relation = Generalization(general=Relation, specific=MetaModelGraph_Reference)
gen_MetaModelGraph_SubClass_Relation = Generalization(general=Relation, specific=MetaModelGraph_SubClass)

# Domain Model
domain_model = DomainModel(
    name="MetaModelGraph",
    types={MetaModelGraph_Graph, MetaModelGraph_SubGraph, MetaModelGraph_EClass, MetaModelGraph_Node, MetaModelGraph_Relation, MetaModelGraph_Reference, MetaModelGraph_SubClass, MetaModelGraph_Composition, MetaModelGraph_EAttribute, Relation, MetaModelGraph_EReference, EnumModular},
    associations={subgraph0, eClassList1, eClassAbstract3, relations8, eClassesListOut10, root13, nodes6, references17, subClasses19, eClass21, relations24, listNodes26, directSubclasses28, compositions16, name33, target35, eReference36, parentNode38, directComposition31, eReference40},
    generalizations={gen_MetaModelGraph_Composition_Relation, gen_MetaModelGraph_Reference_Relation, gen_MetaModelGraph_SubClass_Relation},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)