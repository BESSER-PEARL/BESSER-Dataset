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
model3_Class1 = Class(name="model3::Class1")
Class2 = Class(name="Class2")
model3_MetaRef = Class(name="model3::MetaRef")
model3_EPackage = Class(name="model3::EPackage")
model3_EClass = Class(name="model3::EClass")
model3_EReference = Class(name="model3::EReference")
model3_Polygon = Class(name="model3::Polygon")
model3_PolygonWithDuplicates = Class(name="model3::PolygonWithDuplicates")
model3_NodeA = Class(name="model3::NodeA")
model3_NodeB = Class(name="model3::NodeB")
model3_NodeC = Class(name="model3::NodeC")
model3_NodeD = Class(name="model3::NodeD")
model3_NodeE = Class(name="model3::NodeE")
model3_Image = Class(name="model3::Image")
model3_File = Class(name="model3::File")
model3_ClassWithIDAttribute = Class(name="model3::ClassWithIDAttribute")
model3_ClassWithJavaClassAttribute = Class(name="model3::ClassWithJavaClassAttribute")
model3_ClassWithJavaObjectAttribute = Class(name="model3::ClassWithJavaObjectAttribute")
model3_ClassWithTransientContainment = Class(name="model3::ClassWithTransientContainment")
model3_EdgeTarget = Class(name="model3::EdgeTarget")
model3_Edge = Class(name="model3::Edge")
model3_NodeF = Class(name="model3::NodeF")
EdgeTarget = Class(name="EdgeTarget")
model3_Diagram = Class(name="model3::Diagram")
model3_subpackage_Class2 = Class(name="model3::subpackage::Class2")
subpackage_model3_Class1 = Class(name="subpackage::model3::Class1")

# model3_Class1 class attributes and methods
model3_Class1_additionalValue: Property = Property(name="additionalValue", type=StringType)
model3_Class1.attributes={model3_Class1_additionalValue}

# Class2 class attributes and methods

# model3_MetaRef class attributes and methods

# model3_EPackage class attributes and methods

# model3_EClass class attributes and methods

# model3_EReference class attributes and methods

# model3_Polygon class attributes and methods
model3_Polygon_points: Property = Property(name="points", type=StringType)
model3_Polygon.attributes={model3_Polygon_points}

# model3_PolygonWithDuplicates class attributes and methods
model3_PolygonWithDuplicates_points: Property = Property(name="points", type=StringType)
model3_PolygonWithDuplicates.attributes={model3_PolygonWithDuplicates_points}

# model3_NodeA class attributes and methods
model3_NodeA_name: Property = Property(name="name", type=StringType)
model3_NodeA.attributes={model3_NodeA_name}

# model3_NodeB class attributes and methods
model3_NodeB_name: Property = Property(name="name", type=StringType)
model3_NodeB.attributes={model3_NodeB_name}

# model3_NodeC class attributes and methods
model3_NodeC_name: Property = Property(name="name", type=StringType)
model3_NodeC.attributes={model3_NodeC_name}

# model3_NodeD class attributes and methods
model3_NodeD_name: Property = Property(name="name", type=StringType)
model3_NodeD.attributes={model3_NodeD_name}

# model3_NodeE class attributes and methods
model3_NodeE_name: Property = Property(name="name", type=StringType)
model3_NodeE.attributes={model3_NodeE_name}

# model3_Image class attributes and methods
model3_Image_width: Property = Property(name="width", type=IntegerType)
model3_Image_height: Property = Property(name="height", type=IntegerType)
model3_Image_data: Property = Property(name="data", type=StringType)
model3_Image.attributes={model3_Image_data, model3_Image_height, model3_Image_width}

# model3_File class attributes and methods
model3_File_name: Property = Property(name="name", type=StringType)
model3_File_data: Property = Property(name="data", type=StringType)
model3_File.attributes={model3_File_name, model3_File_data}

# model3_ClassWithIDAttribute class attributes and methods
model3_ClassWithIDAttribute_id: Property = Property(name="id", type=StringType)
model3_ClassWithIDAttribute.attributes={model3_ClassWithIDAttribute_id}

# model3_ClassWithJavaClassAttribute class attributes and methods
model3_ClassWithJavaClassAttribute_javaClass: Property = Property(name="javaClass", type=StringType)
model3_ClassWithJavaClassAttribute.attributes={model3_ClassWithJavaClassAttribute_javaClass}

# model3_ClassWithJavaObjectAttribute class attributes and methods
model3_ClassWithJavaObjectAttribute_javaObject: Property = Property(name="javaObject", type=StringType)
model3_ClassWithJavaObjectAttribute.attributes={model3_ClassWithJavaObjectAttribute_javaObject}

# model3_ClassWithTransientContainment class attributes and methods
model3_ClassWithTransientContainment_name: Property = Property(name="name", type=StringType)
model3_ClassWithTransientContainment.attributes={model3_ClassWithTransientContainment_name}

# model3_EdgeTarget class attributes and methods

# model3_Edge class attributes and methods

# model3_NodeF class attributes and methods

# EdgeTarget class attributes and methods

# model3_Diagram class attributes and methods

# model3_subpackage_Class2 class attributes and methods

# subpackage_model3_Class1 class attributes and methods

# Relationships
class20: BinaryAssociation = BinaryAssociation(
    name="class20",
    ends={
        Property(name="subpackage", type=model3_Class1, multiplicity=Multiplicity(1, 1)),
        Property(name="Class2", type=Class2, multiplicity=Multiplicity(0, 9999))
    }
)
eClassRef2: BinaryAssociation = BinaryAssociation(
    name="eClassRef2",
    ends={
        Property(name="model3_EClass", type=model3_MetaRef, multiplicity=Multiplicity(1, 1)),
        Property(name="model3_MetaRef3", type=model3_EClass, multiplicity=Multiplicity(0, 1))
    }
)
eReferenceRef4: BinaryAssociation = BinaryAssociation(
    name="eReferenceRef4",
    ends={
        Property(name="model3_EReference", type=model3_MetaRef, multiplicity=Multiplicity(1, 1)),
        Property(name="model3_MetaRef5", type=model3_EReference, multiplicity=Multiplicity(0, 1))
    }
)
children7: BinaryAssociation = BinaryAssociation(
    name="children7",
    ends={
        Property(name="model3_NodeA", type=model3_NodeA, multiplicity=Multiplicity(1, 1)),
        Property(name="model3_NodeA6", type=model3_NodeA, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
otherNodes9: BinaryAssociation = BinaryAssociation(
    name="otherNodes9",
    ends={
        Property(name="model3_NodeA10", type=model3_NodeA, multiplicity=Multiplicity(1, 1)),
        Property(name="model3_NodeA8", type=model3_NodeA, multiplicity=Multiplicity(0, 9999))
    }
)
children12: BinaryAssociation = BinaryAssociation(
    name="children12",
    ends={
        Property(name="NodeB", type=model3_NodeB, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=model3_NodeB, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent14: BinaryAssociation = BinaryAssociation(
    name="parent14",
    ends={
        Property(name="NodeB15", type=model3_NodeB, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=model3_NodeB, multiplicity=Multiplicity(0, 1))
    }
)
children17: BinaryAssociation = BinaryAssociation(
    name="children17",
    ends={
        Property(name="NodeC", type=model3_NodeC, multiplicity=Multiplicity(1, 1)),
        Property(name="parent18", type=model3_NodeC, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent20: BinaryAssociation = BinaryAssociation(
    name="parent20",
    ends={
        Property(name="NodeC22", type=model3_NodeC, multiplicity=Multiplicity(1, 1)),
        Property(name="children21", type=model3_NodeC, multiplicity=Multiplicity(0, 1))
    }
)
otherNodes24: BinaryAssociation = BinaryAssociation(
    name="otherNodes24",
    ends={
        Property(name="NodeC25", type=model3_NodeC, multiplicity=Multiplicity(1, 1)),
        Property(name="oppositeNodes", type=model3_NodeC, multiplicity=Multiplicity(0, 9999))
    }
)
oppositeNodes27: BinaryAssociation = BinaryAssociation(
    name="oppositeNodes27",
    ends={
        Property(name="NodeC28", type=model3_NodeC, multiplicity=Multiplicity(1, 1)),
        Property(name="otherNodes", type=model3_NodeC, multiplicity=Multiplicity(0, 9999))
    }
)
children30: BinaryAssociation = BinaryAssociation(
    name="children30",
    ends={
        Property(name="NodeD", type=model3_NodeD, multiplicity=Multiplicity(1, 1)),
        Property(name="parent31", type=model3_NodeD, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent33: BinaryAssociation = BinaryAssociation(
    name="parent33",
    ends={
        Property(name="NodeD35", type=model3_NodeD, multiplicity=Multiplicity(1, 1)),
        Property(name="children34", type=model3_NodeD, multiplicity=Multiplicity(0, 1))
    }
)
otherNodes37: BinaryAssociation = BinaryAssociation(
    name="otherNodes37",
    ends={
        Property(name="NodeD38", type=model3_NodeD, multiplicity=Multiplicity(1, 1)),
        Property(name="oppositeNode", type=model3_NodeD, multiplicity=Multiplicity(0, 9999))
    }
)
ePackageRef1: BinaryAssociation = BinaryAssociation(
    name="ePackageRef1",
    ends={
        Property(name="model3_EPackage", type=model3_MetaRef, multiplicity=Multiplicity(1, 1)),
        Property(name="model3_MetaRef", type=model3_EPackage, multiplicity=Multiplicity(0, 1))
    }
)
mainNode43: BinaryAssociation = BinaryAssociation(
    name="mainNode43",
    ends={
        Property(name="model3_NodeA44", type=model3_NodeE, multiplicity=Multiplicity(1, 1)),
        Property(name="model3_NodeE", type=model3_NodeA, multiplicity=Multiplicity(0, 1))
    }
)
otherNodes45: BinaryAssociation = BinaryAssociation(
    name="otherNodes45",
    ends={
        Property(name="model3_NodeA47", type=model3_NodeE, multiplicity=Multiplicity(1, 1)),
        Property(name="model3_NodeE46", type=model3_NodeA, multiplicity=Multiplicity(0, 9999))
    }
)
transientChild49: BinaryAssociation = BinaryAssociation(
    name="transientChild49",
    ends={
        Property(name="model3_ClassWithTransientContainment", type=model3_ClassWithTransientContainment, multiplicity=Multiplicity(1, 1)),
        Property(name="model3_ClassWithTransientContainment48", type=model3_ClassWithTransientContainment, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
transientChildren51: BinaryAssociation = BinaryAssociation(
    name="transientChildren51",
    ends={
        Property(name="model3_ClassWithTransientContainment52", type=model3_ClassWithTransientContainment, multiplicity=Multiplicity(1, 1)),
        Property(name="model3_ClassWithTransientContainment50", type=model3_ClassWithTransientContainment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
persistentChild54: BinaryAssociation = BinaryAssociation(
    name="persistentChild54",
    ends={
        Property(name="model3_ClassWithTransientContainment55", type=model3_ClassWithTransientContainment, multiplicity=Multiplicity(1, 1)),
        Property(name="model3_ClassWithTransientContainment53", type=model3_ClassWithTransientContainment, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
persistentChildren57: BinaryAssociation = BinaryAssociation(
    name="persistentChildren57",
    ends={
        Property(name="model3_ClassWithTransientContainment58", type=model3_ClassWithTransientContainment, multiplicity=Multiplicity(1, 1)),
        Property(name="model3_ClassWithTransientContainment56", type=model3_ClassWithTransientContainment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoingEdges59: BinaryAssociation = BinaryAssociation(
    name="outgoingEdges59",
    ends={
        Property(name="Edge", type=model3_EdgeTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="sourceNode", type=model3_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
incomingEdges60: BinaryAssociation = BinaryAssociation(
    name="incomingEdges60",
    ends={
        Property(name="Edge61", type=model3_EdgeTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="targetNode", type=model3_Edge, multiplicity=Multiplicity(0, 9999))
    }
)
sourceNode62: BinaryAssociation = BinaryAssociation(
    name="sourceNode62",
    ends={
        Property(name="EdgeTarget", type=model3_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingEdges", type=model3_EdgeTarget, multiplicity=Multiplicity(1, 1))
    }
)
targetNode63: BinaryAssociation = BinaryAssociation(
    name="targetNode63",
    ends={
        Property(name="EdgeTarget64", type=model3_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingEdges", type=model3_EdgeTarget, multiplicity=Multiplicity(1, 1))
    }
)
edges65: BinaryAssociation = BinaryAssociation(
    name="edges65",
    ends={
        Property(name="model3_Edge", type=model3_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="model3_Diagram", type=model3_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edgeTargets66: BinaryAssociation = BinaryAssociation(
    name="edgeTargets66",
    ends={
        Property(name="model3_EdgeTarget", type=model3_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="model3_Diagram67", type=model3_EdgeTarget, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
oppositeNode40: BinaryAssociation = BinaryAssociation(
    name="oppositeNode40",
    ends={
        Property(name="NodeD42", type=model3_NodeD, multiplicity=Multiplicity(1, 1)),
        Property(name="otherNodes41", type=model3_NodeD, multiplicity=Multiplicity(0, 1))
    }
)
class168: BinaryAssociation = BinaryAssociation(
    name="class168",
    ends={
        Property(name="Class1", type=model3_subpackage_Class2, multiplicity=Multiplicity(1, 1)),
        Property(name="class2", type=subpackage_model3_Class1, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_model3_NodeF_EdgeTarget = Generalization(general=EdgeTarget, specific=model3_NodeF)

# Domain Model
domain_model = DomainModel(
    name="model3",
    types={model3_Class1, Class2, model3_MetaRef, model3_EPackage, model3_EClass, model3_EReference, model3_Polygon, model3_PolygonWithDuplicates, model3_NodeA, model3_NodeB, model3_NodeC, model3_NodeD, model3_NodeE, model3_Image, model3_File, model3_ClassWithIDAttribute, model3_ClassWithJavaClassAttribute, model3_ClassWithJavaObjectAttribute, model3_ClassWithTransientContainment, model3_EdgeTarget, model3_Edge, model3_NodeF, EdgeTarget, model3_Diagram, model3_subpackage_Class2, subpackage_model3_Class1},
    associations={class20, eClassRef2, eReferenceRef4, children7, otherNodes9, children12, parent14, children17, parent20, otherNodes24, oppositeNodes27, children30, parent33, otherNodes37, ePackageRef1, mainNode43, otherNodes45, transientChild49, transientChildren51, persistentChild54, persistentChildren57, outgoingEdges59, incomingEdges60, sourceNode62, targetNode63, edges65, edgeTargets66, oppositeNode40, class168},
    generalizations={gen_model3_NodeF_EdgeTarget},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)