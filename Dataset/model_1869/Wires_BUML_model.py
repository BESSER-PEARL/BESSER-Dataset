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
Wires_Transformation = Class(name="Wires::Transformation", is_abstract=True)
TypedElement = Class(name="TypedElement")
Wires_InputActualParameter = Class(name="Wires::InputActualParameter")
Wires_OutputActualParameter = Class(name="Wires::OutputActualParameter")
Wires_DecisionNode = Class(name="Wires::DecisionNode")
Wires_Query = Class(name="Wires::Query")
Transformation = Class(name="Transformation")
Wires_AtomicModelTransformation = Class(name="Wires::AtomicModelTransformation")
Wires_TypedElement = Class(name="Wires::TypedElement", is_abstract=True)
ConnectableElement = Class(name="ConnectableElement")
Wires_Type = Class(name="Wires::Type", is_abstract=True)
Wires_ConnectableElement = Class(name="Wires::ConnectableElement", is_abstract=True)
Wires_ModelType = Class(name="Wires::ModelType")
DataType = Class(name="DataType")
Wires_DataType = Class(name="Wires::DataType", is_abstract=True)
Type = Class(name="Type")
Wires_ActualParameter = Class(name="Wires::ActualParameter", is_abstract=True)
WiresElement = Class(name="WiresElement")
Wires_DataFlow = Class(name="Wires::DataFlow")
Wires_TransformationType = Class(name="Wires::TransformationType", is_abstract=True)
Wires_OutputFormalParameter = Class(name="Wires::OutputFormalParameter")
Wires_LibraryRef = Class(name="Wires::LibraryRef")
Wires_InputFormalParameter = Class(name="Wires::InputFormalParameter")
Wires_FormalParameter = Class(name="Wires::FormalParameter", is_abstract=True)
Wires_QueryType = Class(name="Wires::QueryType")
TransformationType = Class(name="TransformationType")
Wires_Model = Class(name="Wires::Model")
Wires_BasicData = Class(name="Wires::BasicData")
Wires_CompositeTransformationType = Class(name="Wires::CompositeTransformationType")
WiresSpecification = Class(name="WiresSpecification")
Wires_CompositeTransformation = Class(name="Wires::CompositeTransformation")
Wires_BasicDataType = Class(name="Wires::BasicDataType")
Wires_WiresSpecification = Class(name="Wires::WiresSpecification")
Wires_WiresElement = Class(name="Wires::WiresElement", is_abstract=True)
AtomicModelTransformation = Class(name="AtomicModelTransformation")
Wires_Library = Class(name="Wires::Library")
FormalParameter = Class(name="FormalParameter")
ActualParameter = Class(name="ActualParameter")
Wires_AtomicModelTransfomationType = Class(name="Wires::AtomicModelTransfomationType")
Wires_IdentityTransformation = Class(name="Wires::IdentityTransformation")
Wires_GenericTransformation = Class(name="Wires::GenericTransformation")
Wires_TypeParameter = Class(name="Wires::TypeParameter")
Wires_GenericQuery = Class(name="Wires::GenericQuery")
Query = Class(name="Query")

# Wires_Transformation class attributes and methods

# TypedElement class attributes and methods

# Wires_InputActualParameter class attributes and methods

# Wires_OutputActualParameter class attributes and methods

# Wires_DecisionNode class attributes and methods
Wires_DecisionNode_expression: Property = Property(name="expression", type=StringType)
Wires_DecisionNode.attributes={Wires_DecisionNode_expression}

# Wires_Query class attributes and methods

# Transformation class attributes and methods

# Wires_AtomicModelTransformation class attributes and methods

# Wires_TypedElement class attributes and methods

# ConnectableElement class attributes and methods

# Wires_Type class attributes and methods
Wires_Type_path: Property = Property(name="path", type=StringType)
Wires_Type.attributes={Wires_Type_path}

# Wires_ConnectableElement class attributes and methods
Wires_ConnectableElement_name: Property = Property(name="name", type=StringType)
Wires_ConnectableElement.attributes={Wires_ConnectableElement_name}

# Wires_ModelType class attributes and methods
Wires_ModelType_uri: Property = Property(name="uri", type=StringType)
Wires_ModelType.attributes={Wires_ModelType_uri}

# DataType class attributes and methods

# Wires_DataType class attributes and methods

# Type class attributes and methods

# Wires_ActualParameter class attributes and methods

# WiresElement class attributes and methods

# Wires_DataFlow class attributes and methods

# Wires_TransformationType class attributes and methods

# Wires_OutputFormalParameter class attributes and methods

# Wires_LibraryRef class attributes and methods
Wires_LibraryRef_name: Property = Property(name="name", type=StringType)
Wires_LibraryRef.attributes={Wires_LibraryRef_name}

# Wires_InputFormalParameter class attributes and methods

# Wires_FormalParameter class attributes and methods
Wires_FormalParameter_typeName: Property = Property(name="typeName", type=StringType)
Wires_FormalParameter.attributes={Wires_FormalParameter_typeName}

# Wires_QueryType class attributes and methods

# TransformationType class attributes and methods

# Wires_Model class attributes and methods
Wires_Model_path: Property = Property(name="path", type=StringType)
Wires_Model.attributes={Wires_Model_path}

# Wires_BasicData class attributes and methods
Wires_BasicData_path: Property = Property(name="path", type=StringType)
Wires_BasicData.attributes={Wires_BasicData_path}

# Wires_CompositeTransformationType class attributes and methods

# WiresSpecification class attributes and methods

# Wires_CompositeTransformation class attributes and methods

# Wires_BasicDataType class attributes and methods

# Wires_WiresSpecification class attributes and methods

# Wires_WiresElement class attributes and methods

# AtomicModelTransformation class attributes and methods

# Wires_Library class attributes and methods
Wires_Library_name: Property = Property(name="name", type=StringType)
Wires_Library_path: Property = Property(name="path", type=StringType)
Wires_Library.attributes={Wires_Library_name, Wires_Library_path}

# FormalParameter class attributes and methods

# ActualParameter class attributes and methods

# Wires_AtomicModelTransfomationType class attributes and methods

# Wires_IdentityTransformation class attributes and methods

# Wires_GenericTransformation class attributes and methods

# Wires_TypeParameter class attributes and methods

# Wires_GenericQuery class attributes and methods

# Query class attributes and methods

# Relationships
inParams0: BinaryAssociation = BinaryAssociation(
    name="inParams0",
    ends={
        Property(name="Wires_InputActualParameter", type=Wires_Transformation, multiplicity=Multiplicity(1, 1)),
        Property(name="Wires_Transformation", type=Wires_InputActualParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outParams1: BinaryAssociation = BinaryAssociation(
    name="outParams1",
    ends={
        Property(name="Wires_OutputActualParameter", type=Wires_Transformation, multiplicity=Multiplicity(1, 1)),
        Property(name="Wires_Transformation2", type=Wires_OutputActualParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
controlNode3: BinaryAssociation = BinaryAssociation(
    name="controlNode3",
    ends={
        Property(name="Wires_DecisionNode", type=Wires_Transformation, multiplicity=Multiplicity(1, 1)),
        Property(name="Wires_Transformation4", type=Wires_DecisionNode, multiplicity=Multiplicity(0, 1))
    }
)
type5: BinaryAssociation = BinaryAssociation(
    name="type5",
    ends={
        Property(name="Wires_Type", type=Wires_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="Wires_TypedElement", type=Wires_Type, multiplicity=Multiplicity(0, 1))
    }
)
target15: BinaryAssociation = BinaryAssociation(
    name="target15",
    ends={
        Property(name="ConnectableElement", type=Wires_DataFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=Wires_ConnectableElement, multiplicity=Multiplicity(1, 1))
    }
)
trueBranch6: BinaryAssociation = BinaryAssociation(
    name="trueBranch6",
    ends={
        Property(name="Wires_Transformation8", type=Wires_DecisionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Wires_DecisionNode7", type=Wires_Transformation, multiplicity=Multiplicity(0, 9999))
    }
)
falseBranch9: BinaryAssociation = BinaryAssociation(
    name="falseBranch9",
    ends={
        Property(name="Wires_Transformation11", type=Wires_DecisionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Wires_DecisionNode10", type=Wires_Transformation, multiplicity=Multiplicity(0, 9999))
    }
)
inParams12: BinaryAssociation = BinaryAssociation(
    name="inParams12",
    ends={
        Property(name="Wires_InputActualParameter14", type=Wires_DecisionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Wires_DecisionNode13", type=Wires_InputActualParameter, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
src16: BinaryAssociation = BinaryAssociation(
    name="src16",
    ends={
        Property(name="ConnectableElement17", type=Wires_DataFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=Wires_ConnectableElement, multiplicity=Multiplicity(1, 1))
    }
)
outParams18: BinaryAssociation = BinaryAssociation(
    name="outParams18",
    ends={
        Property(name="Wires_OutputFormalParameter", type=Wires_TransformationType, multiplicity=Multiplicity(1, 1)),
        Property(name="Wires_TransformationType", type=Wires_OutputFormalParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
libraries19: BinaryAssociation = BinaryAssociation(
    name="libraries19",
    ends={
        Property(name="Wires_LibraryRef", type=Wires_TransformationType, multiplicity=Multiplicity(1, 1)),
        Property(name="Wires_TransformationType20", type=Wires_LibraryRef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inParams21: BinaryAssociation = BinaryAssociation(
    name="inParams21",
    ends={
        Property(name="Wires_InputFormalParameter", type=Wires_TransformationType, multiplicity=Multiplicity(1, 1)),
        Property(name="Wires_TransformationType22", type=Wires_InputFormalParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeEl23: BinaryAssociation = BinaryAssociation(
    name="typeEl23",
    ends={
        Property(name="Wires_DataType", type=Wires_FormalParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="Wires_FormalParameter", type=Wires_DataType, multiplicity=Multiplicity(1, 1))
    }
)
incoming24: BinaryAssociation = BinaryAssociation(
    name="incoming24",
    ends={
        Property(name="DataFlow", type=Wires_ConnectableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=Wires_DataFlow, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing25: BinaryAssociation = BinaryAssociation(
    name="outgoing25",
    ends={
        Property(name="DataFlow26", type=Wires_ConnectableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="src", type=Wires_DataFlow, multiplicity=Multiplicity(0, 9999))
    }
)
els27: BinaryAssociation = BinaryAssociation(
    name="els27",
    ends={
        Property(name="Wires_WiresElement", type=Wires_WiresSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="Wires_WiresSpecification", type=Wires_WiresElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
library28: BinaryAssociation = BinaryAssociation(
    name="library28",
    ends={
        Property(name="Wires_Library", type=Wires_LibraryRef, multiplicity=Multiplicity(1, 1)),
        Property(name="Wires_LibraryRef29", type=Wires_Library, multiplicity=Multiplicity(1, 1))
    }
)
libraries30: BinaryAssociation = BinaryAssociation(
    name="libraries30",
    ends={
        Property(name="Wires_LibraryRef32", type=Wires_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="Wires_Library31", type=Wires_LibraryRef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeParam33: BinaryAssociation = BinaryAssociation(
    name="typeParam33",
    ends={
        Property(name="Wires_TypeParameter", type=Wires_GenericTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="Wires_GenericTransformation", type=Wires_TypeParameter, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeParam34: BinaryAssociation = BinaryAssociation(
    name="typeParam34",
    ends={
        Property(name="Wires_TypeParameter35", type=Wires_GenericQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="Wires_GenericQuery", type=Wires_TypeParameter, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_Wires_Transformation_TypedElement = Generalization(general=TypedElement, specific=Wires_Transformation)
gen_Wires_Query_Transformation = Generalization(general=Transformation, specific=Wires_Query)
gen_Wires_AtomicModelTransformation_Transformation = Generalization(general=Transformation, specific=Wires_AtomicModelTransformation)
gen_Wires_TypedElement_ConnectableElement = Generalization(general=ConnectableElement, specific=Wires_TypedElement)
gen_Wires_Type_ConnectableElement = Generalization(general=ConnectableElement, specific=Wires_Type)
gen_Wires_ModelType_DataType = Generalization(general=DataType, specific=Wires_ModelType)
gen_Wires_DataType_Type = Generalization(general=Type, specific=Wires_DataType)
gen_Wires_ActualParameter_TypedElement = Generalization(general=TypedElement, specific=Wires_ActualParameter)
gen_Wires_DecisionNode_WiresElement = Generalization(general=WiresElement, specific=Wires_DecisionNode)
gen_Wires_DataFlow_WiresElement = Generalization(general=WiresElement, specific=Wires_DataFlow)
gen_Wires_QueryType_TransformationType = Generalization(general=TransformationType, specific=Wires_QueryType)
gen_Wires_ConnectableElement_WiresElement = Generalization(general=WiresElement, specific=Wires_ConnectableElement)
gen_Wires_TransformationType_Type = Generalization(general=Type, specific=Wires_TransformationType)
gen_Wires_FormalParameter_Type = Generalization(general=Type, specific=Wires_FormalParameter)
gen_Wires_Model_TypedElement = Generalization(general=TypedElement, specific=Wires_Model)
gen_Wires_BasicData_TypedElement = Generalization(general=TypedElement, specific=Wires_BasicData)
gen_Wires_CompositeTransformationType_TransformationType = Generalization(general=TransformationType, specific=Wires_CompositeTransformationType)
gen_Wires_CompositeTransformationType_WiresSpecification = Generalization(general=WiresSpecification, specific=Wires_CompositeTransformationType)
gen_Wires_CompositeTransformation_Transformation = Generalization(general=Transformation, specific=Wires_CompositeTransformation)
gen_Wires_BasicDataType_DataType = Generalization(general=DataType, specific=Wires_BasicDataType)
gen_Wires_IdentityTransformation_AtomicModelTransformation = Generalization(general=AtomicModelTransformation, specific=Wires_IdentityTransformation)
gen_Wires_Library_WiresElement = Generalization(general=WiresElement, specific=Wires_Library)
gen_Wires_InputFormalParameter_FormalParameter = Generalization(general=FormalParameter, specific=Wires_InputFormalParameter)
gen_Wires_OutputFormalParameter_FormalParameter = Generalization(general=FormalParameter, specific=Wires_OutputFormalParameter)
gen_Wires_InputActualParameter_ActualParameter = Generalization(general=ActualParameter, specific=Wires_InputActualParameter)
gen_Wires_OutputActualParameter_ActualParameter = Generalization(general=ActualParameter, specific=Wires_OutputActualParameter)
gen_Wires_AtomicModelTransfomationType_TransformationType = Generalization(general=TransformationType, specific=Wires_AtomicModelTransfomationType)
gen_Wires_GenericTransformation_AtomicModelTransformation = Generalization(general=AtomicModelTransformation, specific=Wires_GenericTransformation)
gen_Wires_TypeParameter_ActualParameter = Generalization(general=ActualParameter, specific=Wires_TypeParameter)
gen_Wires_GenericQuery_Query = Generalization(general=Query, specific=Wires_GenericQuery)

# Domain Model
domain_model = DomainModel(
    name="Wires",
    types={Wires_Transformation, TypedElement, Wires_InputActualParameter, Wires_OutputActualParameter, Wires_DecisionNode, Wires_Query, Transformation, Wires_AtomicModelTransformation, Wires_TypedElement, ConnectableElement, Wires_Type, Wires_ConnectableElement, Wires_ModelType, DataType, Wires_DataType, Type, Wires_ActualParameter, WiresElement, Wires_DataFlow, Wires_TransformationType, Wires_OutputFormalParameter, Wires_LibraryRef, Wires_InputFormalParameter, Wires_FormalParameter, Wires_QueryType, TransformationType, Wires_Model, Wires_BasicData, Wires_CompositeTransformationType, WiresSpecification, Wires_CompositeTransformation, Wires_BasicDataType, Wires_WiresSpecification, Wires_WiresElement, AtomicModelTransformation, Wires_Library, FormalParameter, ActualParameter, Wires_AtomicModelTransfomationType, Wires_IdentityTransformation, Wires_GenericTransformation, Wires_TypeParameter, Wires_GenericQuery, Query},
    associations={inParams0, outParams1, controlNode3, type5, target15, trueBranch6, falseBranch9, inParams12, src16, outParams18, libraries19, inParams21, typeEl23, incoming24, outgoing25, els27, library28, libraries30, typeParam33, typeParam34},
    generalizations={gen_Wires_Transformation_TypedElement, gen_Wires_Query_Transformation, gen_Wires_AtomicModelTransformation_Transformation, gen_Wires_TypedElement_ConnectableElement, gen_Wires_Type_ConnectableElement, gen_Wires_ModelType_DataType, gen_Wires_DataType_Type, gen_Wires_ActualParameter_TypedElement, gen_Wires_DecisionNode_WiresElement, gen_Wires_DataFlow_WiresElement, gen_Wires_QueryType_TransformationType, gen_Wires_ConnectableElement_WiresElement, gen_Wires_TransformationType_Type, gen_Wires_FormalParameter_Type, gen_Wires_Model_TypedElement, gen_Wires_BasicData_TypedElement, gen_Wires_CompositeTransformationType_TransformationType, gen_Wires_CompositeTransformationType_WiresSpecification, gen_Wires_CompositeTransformation_Transformation, gen_Wires_BasicDataType_DataType, gen_Wires_IdentityTransformation_AtomicModelTransformation, gen_Wires_Library_WiresElement, gen_Wires_InputFormalParameter_FormalParameter, gen_Wires_OutputFormalParameter_FormalParameter, gen_Wires_InputActualParameter_ActualParameter, gen_Wires_OutputActualParameter_ActualParameter, gen_Wires_AtomicModelTransfomationType_TransformationType, gen_Wires_GenericTransformation_AtomicModelTransformation, gen_Wires_TypeParameter_ActualParameter, gen_Wires_GenericQuery_Query},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)