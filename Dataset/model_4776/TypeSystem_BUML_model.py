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
OperatorKind: Enumeration = Enumeration(
    name="OperatorKind",
    literals={
            EnumerationLiteral(name="Add"),
			EnumerationLiteral(name="Subtract"),
			EnumerationLiteral(name="Multiply"),
			EnumerationLiteral(name="Divide"),
			EnumerationLiteral(name="ElementWiseMultiply"),
			EnumerationLiteral(name="ElementWiseDivide"),
			EnumerationLiteral(name="ElementWisePower"),
			EnumerationLiteral(name="Negate"),
			EnumerationLiteral(name="Power"),
			EnumerationLiteral(name="Root"),
			EnumerationLiteral(name="Transpose"),
			EnumerationLiteral(name="LogicalAnd"),
			EnumerationLiteral(name="LogicalOr"),
			EnumerationLiteral(name="LogicalNot"),
			EnumerationLiteral(name="Implies"),
			EnumerationLiteral(name="LessThan"),
			EnumerationLiteral(name="LessThanOrEqualTo"),
			EnumerationLiteral(name="GreaterThan"),
			EnumerationLiteral(name="GreaterThanOrEqualTo"),
			EnumerationLiteral(name="EqualTo"),
			EnumerationLiteral(name="NotEqualTo")
    }
)

# Classes
typesystem_RealType = Class(name="typesystem::RealType")
NumericType = Class(name="NumericType")
typesystem_IntegerType = Class(name="typesystem::IntegerType")
typesystem_ComplexType = Class(name="typesystem::ComplexType")
typesystem_DataType = Class(name="typesystem::DataType", is_abstract=True)
typesystem_GaussianType = Class(name="typesystem::GaussianType")
typesystem_BooleanType = Class(name="typesystem::BooleanType")
typesystem_StringType = Class(name="typesystem::StringType")
typesystem_ArrayType = Class(name="typesystem::ArrayType")
typesystem_ArrayDimension = Class(name="typesystem::ArrayDimension")
typesystem_InvalidDataType = Class(name="typesystem::InvalidDataType")
DataType = Class(name="DataType")
typesystem_AnyDataType = Class(name="typesystem::AnyDataType")
typesystem_UnitType = Class(name="typesystem::UnitType")
typesystem_PrimitiveType = Class(name="typesystem::PrimitiveType")
typesystem_NumericType = Class(name="typesystem::NumericType")
PrimitiveType = Class(name="PrimitiveType")
typesystem_Unit = Class(name="typesystem::Unit")
typesystem_UnitProduct = Class(name="typesystem::UnitProduct", is_abstract=True)
typesystem_UnitFactor = Class(name="typesystem::UnitFactor")
UnitProduct = Class(name="UnitProduct")
typesystem_Literal = Class(name="typesystem::Literal")
Expression = Class(name="Expression")
typesystem_NumericLiteral = Class(name="typesystem::NumericLiteral")
Literal = Class(name="Literal")
typesystem_RealLiteral = Class(name="typesystem::RealLiteral")
typesystem_TensorType = Class(name="typesystem::TensorType")
NumericLiteral = Class(name="NumericLiteral")
ArrayType = Class(name="ArrayType")
typesystem_IntegerLiteral = Class(name="typesystem::IntegerLiteral")
typesystem_Expression = Class(name="typesystem::Expression")
typesystem_UnitNumerator = Class(name="typesystem::UnitNumerator")
typesystem_UnitDenominator = Class(name="typesystem::UnitDenominator")
typesystem_BooleanLiteral = Class(name="typesystem::BooleanLiteral")
typesystem_StringLiteral = Class(name="typesystem::StringLiteral")

# typesystem_RealType class attributes and methods

# NumericType class attributes and methods

# typesystem_IntegerType class attributes and methods

# typesystem_ComplexType class attributes and methods

# typesystem_DataType class attributes and methods
typesystem_DataType_m_evaluate: Method = Method(name="evaluate", parameters={Parameter(name='other'), Parameter(name='operator')}, type=StringType)
typesystem_DataType_m_evaluate: Method = Method(name="evaluate", parameters={Parameter(name='n'), Parameter(name='operator')}, type=StringType)
typesystem_DataType_m_isAssignableFrom: Method = Method(name="isAssignableFrom", parameters={Parameter(name='other')}, type=BooleanType)
typesystem_DataType_m_isEquivalentTo: Method = Method(name="isEquivalentTo", parameters={Parameter(name='other')}, type=BooleanType)
typesystem_DataType.methods={typesystem_DataType_m_evaluate, typesystem_DataType_m_evaluate, typesystem_DataType_m_isAssignableFrom, typesystem_DataType_m_isEquivalentTo}

# typesystem_GaussianType class attributes and methods

# typesystem_BooleanType class attributes and methods

# typesystem_StringType class attributes and methods

# typesystem_ArrayType class attributes and methods
typesystem_ArrayType_dimensionality: Property = Property(name="dimensionality", type=IntegerType)
typesystem_ArrayType_dimensional: Property = Property(name="dimensional", type=BooleanType)
typesystem_ArrayType_multidimensional: Property = Property(name="multidimensional", type=BooleanType)
typesystem_ArrayType.attributes={typesystem_ArrayType_multidimensional, typesystem_ArrayType_dimensionality, typesystem_ArrayType_dimensional}

# typesystem_ArrayDimension class attributes and methods

# typesystem_InvalidDataType class attributes and methods

# DataType class attributes and methods

# typesystem_AnyDataType class attributes and methods

# typesystem_UnitType class attributes and methods

# typesystem_PrimitiveType class attributes and methods

# typesystem_NumericType class attributes and methods

# PrimitiveType class attributes and methods

# typesystem_Unit class attributes and methods
typesystem_Unit_scale: Property = Property(name="scale", type=IntegerType)
typesystem_Unit_wildcard: Property = Property(name="wildcard", type=BooleanType)
typesystem_Unit_m_getNormalized: Method = Method(name="getNormalized", parameters={}, type=StringType)
typesystem_Unit_m_evaluate: Method = Method(name="evaluate", parameters={Parameter(name='other'), Parameter(name='operator')}, type=StringType)
typesystem_Unit_m_evaluate: Method = Method(name="evaluate", parameters={Parameter(name='n'), Parameter(name='operator')}, type=StringType)
typesystem_Unit_m_isEquivalentTo: Method = Method(name="isEquivalentTo", parameters={Parameter(name='other'), Parameter(name='ignoreScale')}, type=BooleanType)
typesystem_Unit.attributes={typesystem_Unit_scale, typesystem_Unit_wildcard}
typesystem_Unit.methods={typesystem_Unit_m_isEquivalentTo, typesystem_Unit_m_evaluate, typesystem_Unit_m_getNormalized, typesystem_Unit_m_evaluate}

# typesystem_UnitProduct class attributes and methods
typesystem_UnitProduct_m_getFactor: Method = Method(name="getFactor", parameters={Parameter(name='symbol')}, type=StringType)
typesystem_UnitProduct.methods={typesystem_UnitProduct_m_getFactor}

# typesystem_UnitFactor class attributes and methods
typesystem_UnitFactor_symbol: Property = Property(name="symbol", type=StringType)
typesystem_UnitFactor_exponent: Property = Property(name="exponent", type=IntegerType)
typesystem_UnitFactor.attributes={typesystem_UnitFactor_exponent, typesystem_UnitFactor_symbol}

# UnitProduct class attributes and methods

# typesystem_Literal class attributes and methods

# Expression class attributes and methods

# typesystem_NumericLiteral class attributes and methods
typesystem_NumericLiteral_m_isComplex: Method = Method(name="isComplex", parameters={}, type=BooleanType)
typesystem_NumericLiteral.methods={typesystem_NumericLiteral_m_isComplex}

# Literal class attributes and methods

# typesystem_RealLiteral class attributes and methods
typesystem_RealLiteral_data: Property = Property(name="data", type=StringType)
typesystem_RealLiteral_value: Property = Property(name="value", type=FloatType)
typesystem_RealLiteral.attributes={typesystem_RealLiteral_value, typesystem_RealLiteral_data}

# typesystem_TensorType class attributes and methods
typesystem_TensorType_vector: Property = Property(name="vector", type=BooleanType)
typesystem_TensorType_matrix: Property = Property(name="matrix", type=BooleanType)
typesystem_TensorType.attributes={typesystem_TensorType_vector, typesystem_TensorType_matrix}

# NumericLiteral class attributes and methods

# ArrayType class attributes and methods

# typesystem_IntegerLiteral class attributes and methods
typesystem_IntegerLiteral_data: Property = Property(name="data", type=StringType)
typesystem_IntegerLiteral_value: Property = Property(name="value", type=StringType)
typesystem_IntegerLiteral.attributes={typesystem_IntegerLiteral_value, typesystem_IntegerLiteral_data}

# typesystem_Expression class attributes and methods

# typesystem_UnitNumerator class attributes and methods

# typesystem_UnitDenominator class attributes and methods

# typesystem_BooleanLiteral class attributes and methods
typesystem_BooleanLiteral_true: Property = Property(name="true", type=BooleanType)
typesystem_BooleanLiteral.attributes={typesystem_BooleanLiteral_true}

# typesystem_StringLiteral class attributes and methods
typesystem_StringLiteral_value: Property = Property(name="value", type=StringType)
typesystem_StringLiteral.attributes={typesystem_StringLiteral_value}

# Relationships
unit0: BinaryAssociation = BinaryAssociation(
    name="unit0",
    ends={
        Property(name="typesystem_Unit", type=typesystem_NumericType, multiplicity=Multiplicity(1, 1)),
        Property(name="typesystem_NumericType", type=typesystem_Unit, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elementType1: BinaryAssociation = BinaryAssociation(
    name="elementType1",
    ends={
        Property(name="typesystem_DataType", type=typesystem_ArrayType, multiplicity=Multiplicity(1, 1)),
        Property(name="typesystem_ArrayType", type=typesystem_DataType, multiplicity=Multiplicity(0, 1))
    }
)
definedElementType2: BinaryAssociation = BinaryAssociation(
    name="definedElementType2",
    ends={
        Property(name="typesystem_DataType4", type=typesystem_ArrayType, multiplicity=Multiplicity(1, 1)),
        Property(name="typesystem_ArrayType3", type=typesystem_DataType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dimensions5: BinaryAssociation = BinaryAssociation(
    name="dimensions5",
    ends={
        Property(name="typesystem_ArrayDimension", type=typesystem_ArrayType, multiplicity=Multiplicity(1, 1)),
        Property(name="typesystem_ArrayType6", type=typesystem_ArrayDimension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
factors13: BinaryAssociation = BinaryAssociation(
    name="factors13",
    ends={
        Property(name="typesystem_UnitFactor", type=typesystem_UnitProduct, multiplicity=Multiplicity(1, 1)),
        Property(name="typesystem_UnitProduct", type=typesystem_UnitFactor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
unit14: BinaryAssociation = BinaryAssociation(
    name="unit14",
    ends={
        Property(name="typesystem_Unit15", type=typesystem_NumericLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="typesystem_NumericLiteral", type=typesystem_Unit, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
size7: BinaryAssociation = BinaryAssociation(
    name="size7",
    ends={
        Property(name="typesystem_Expression", type=typesystem_ArrayDimension, multiplicity=Multiplicity(1, 1)),
        Property(name="typesystem_ArrayDimension8", type=typesystem_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
numerator9: BinaryAssociation = BinaryAssociation(
    name="numerator9",
    ends={
        Property(name="typesystem_UnitNumerator", type=typesystem_Unit, multiplicity=Multiplicity(1, 1)),
        Property(name="typesystem_Unit10", type=typesystem_UnitNumerator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
denominator11: BinaryAssociation = BinaryAssociation(
    name="denominator11",
    ends={
        Property(name="typesystem_UnitDenominator", type=typesystem_Unit, multiplicity=Multiplicity(1, 1)),
        Property(name="typesystem_Unit12", type=typesystem_UnitDenominator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_typesystem_RealType_NumericType = Generalization(general=NumericType, specific=typesystem_RealType)
gen_typesystem_IntegerType_NumericType = Generalization(general=NumericType, specific=typesystem_IntegerType)
gen_typesystem_ComplexType_NumericType = Generalization(general=NumericType, specific=typesystem_ComplexType)
gen_typesystem_GaussianType_NumericType = Generalization(general=NumericType, specific=typesystem_GaussianType)
gen_typesystem_BooleanType_PrimitiveType = Generalization(general=PrimitiveType, specific=typesystem_BooleanType)
gen_typesystem_StringType_PrimitiveType = Generalization(general=PrimitiveType, specific=typesystem_StringType)
gen_typesystem_ArrayType_DataType = Generalization(general=DataType, specific=typesystem_ArrayType)
gen_typesystem_InvalidDataType_DataType = Generalization(general=DataType, specific=typesystem_InvalidDataType)
gen_typesystem_AnyDataType_DataType = Generalization(general=DataType, specific=typesystem_AnyDataType)
gen_typesystem_UnitType_DataType = Generalization(general=DataType, specific=typesystem_UnitType)
gen_typesystem_PrimitiveType_DataType = Generalization(general=DataType, specific=typesystem_PrimitiveType)
gen_typesystem_NumericType_PrimitiveType = Generalization(general=PrimitiveType, specific=typesystem_NumericType)
gen_typesystem_UnitNumerator_UnitProduct = Generalization(general=UnitProduct, specific=typesystem_UnitNumerator)
gen_typesystem_UnitDenominator_UnitProduct = Generalization(general=UnitProduct, specific=typesystem_UnitDenominator)
gen_typesystem_Literal_Expression = Generalization(general=Expression, specific=typesystem_Literal)
gen_typesystem_NumericLiteral_Literal = Generalization(general=Literal, specific=typesystem_NumericLiteral)
gen_typesystem_RealLiteral_NumericLiteral = Generalization(general=NumericLiteral, specific=typesystem_RealLiteral)
gen_typesystem_TensorType_ArrayType = Generalization(general=ArrayType, specific=typesystem_TensorType)
gen_typesystem_IntegerLiteral_NumericLiteral = Generalization(general=NumericLiteral, specific=typesystem_IntegerLiteral)
gen_typesystem_BooleanLiteral_Literal = Generalization(general=Literal, specific=typesystem_BooleanLiteral)
gen_typesystem_StringLiteral_Literal = Generalization(general=Literal, specific=typesystem_StringLiteral)

# Domain Model
domain_model = DomainModel(
    name="typesystem",
    types={typesystem_RealType, NumericType, typesystem_IntegerType, typesystem_ComplexType, typesystem_DataType, typesystem_GaussianType, typesystem_BooleanType, typesystem_StringType, typesystem_ArrayType, typesystem_ArrayDimension, typesystem_InvalidDataType, DataType, typesystem_AnyDataType, typesystem_UnitType, typesystem_PrimitiveType, typesystem_NumericType, PrimitiveType, typesystem_Unit, typesystem_UnitProduct, typesystem_UnitFactor, UnitProduct, typesystem_Literal, Expression, typesystem_NumericLiteral, Literal, typesystem_RealLiteral, typesystem_TensorType, NumericLiteral, ArrayType, typesystem_IntegerLiteral, typesystem_Expression, typesystem_UnitNumerator, typesystem_UnitDenominator, typesystem_BooleanLiteral, typesystem_StringLiteral, OperatorKind},
    associations={unit0, elementType1, definedElementType2, dimensions5, factors13, unit14, size7, numerator9, denominator11},
    generalizations={gen_typesystem_RealType_NumericType, gen_typesystem_IntegerType_NumericType, gen_typesystem_ComplexType_NumericType, gen_typesystem_GaussianType_NumericType, gen_typesystem_BooleanType_PrimitiveType, gen_typesystem_StringType_PrimitiveType, gen_typesystem_ArrayType_DataType, gen_typesystem_InvalidDataType_DataType, gen_typesystem_AnyDataType_DataType, gen_typesystem_UnitType_DataType, gen_typesystem_PrimitiveType_DataType, gen_typesystem_NumericType_PrimitiveType, gen_typesystem_UnitNumerator_UnitProduct, gen_typesystem_UnitDenominator_UnitProduct, gen_typesystem_Literal_Expression, gen_typesystem_NumericLiteral_Literal, gen_typesystem_RealLiteral_NumericLiteral, gen_typesystem_TensorType_ArrayType, gen_typesystem_IntegerLiteral_NumericLiteral, gen_typesystem_BooleanLiteral_Literal, gen_typesystem_StringLiteral_Literal},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)