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
QuantityKind = Class(name="QuantityKind")
Unit = Class(name="Unit")
Dimension = Class(name="Dimension")
Prefix = Class(name="Prefix")
QuantityKindFactor = Class(name="QuantityKindFactor")
SystemOfQuantities = Class(name="SystemOfQuantities")
SystemOfUnits = Class(name="SystemOfUnits")
SysML_ValueTypes_QUDV_ROOT_RESOURCE_SHAPE_CONTAINER = Class(name="SysML::ValueTypes::QUDV::ROOT::RESOURCE::SHAPE::CONTAINER")
Number = Class(name="Number")
UnitFactor = Class(name="UnitFactor")
SysML_ValueTypes_QUDV_PrimitiveValueTypes_Number = Class(name="SysML::ValueTypes::QUDV::PrimitiveValueTypes::Number", is_abstract=True)
SysML_ValueTypes_QUDV_PrimitiveValueTypes_Complex = Class(name="SysML::ValueTypes::QUDV::PrimitiveValueTypes::Complex")
SysML_ValueTypes_QUDV_PrimitiveValueTypes_Real = Class(name="SysML::ValueTypes::QUDV::PrimitiveValueTypes::Real")
Real = Class(name="Real")
SysML_ValueTypes_QUDV_PrimitiveValueTypes_Integer = Class(name="SysML::ValueTypes::QUDV::PrimitiveValueTypes::Integer")
SysML_ValueTypes_QUDV_UnitAndQuantityKind_QuantityKind = Class(name="SysML::ValueTypes::QUDV::UnitAndQuantityKind::QuantityKind")
SysML_ValueTypes_QUDV_PrimitiveValueTypes_Rational = Class(name="SysML::ValueTypes::QUDV::PrimitiveValueTypes::Rational")
Integer = Class(name="Integer")
SysML_ValueTypes_QUDV_QUDV_AffineConversionUnit = Class(name="SysML::ValueTypes::QUDV::QUDV::AffineConversionUnit")
ConversionBasedUnit = Class(name="ConversionBasedUnit")
SysML_ValueTypes_QUDV_UnitAndQuantityKind_Unit = Class(name="SysML::ValueTypes::QUDV::UnitAndQuantityKind::Unit")
SysML_ValueTypes_QUDV_QUDV_ConversionBasedUnit = Class(name="SysML::ValueTypes::QUDV::QUDV::ConversionBasedUnit", is_abstract=True)
SysML_ValueTypes_QUDV_QUDV_DerivedQuantityKind = Class(name="SysML::ValueTypes::QUDV::QUDV::DerivedQuantityKind")
SysML_ValueTypes_QUDV_QUDV_DerivedUnit = Class(name="SysML::ValueTypes::QUDV::QUDV::DerivedUnit")
SysML_ValueTypes_QUDV_QUDV_GeneralConversionUnit = Class(name="SysML::ValueTypes::QUDV::QUDV::GeneralConversionUnit")
SysML_ValueTypes_QUDV_QUDV_LinearConversionUnit = Class(name="SysML::ValueTypes::QUDV::QUDV::LinearConversionUnit")
SysML_ValueTypes_QUDV_QUDV_Dimension = Class(name="SysML::ValueTypes::QUDV::QUDV::Dimension")
SysML_ValueTypes_QUDV_QUDV_PrefixedUnit = Class(name="SysML::ValueTypes::QUDV::QUDV::PrefixedUnit")
SysML_ValueTypes_QUDV_QUDV_QuantityKind = Class(name="SysML::ValueTypes::QUDV::QUDV::QuantityKind", is_abstract=True)
SysML_ValueTypes_QUDV_QUDV_Prefix = Class(name="SysML::ValueTypes::QUDV::QUDV::Prefix")
Rational = Class(name="Rational")
SysML_ValueTypes_QUDV_QUDV_QuantityKindFactor = Class(name="SysML::ValueTypes::QUDV::QUDV::QuantityKindFactor")
SysML_ValueTypes_QUDV_QUDV_SimpleQuantityKind = Class(name="SysML::ValueTypes::QUDV::QUDV::SimpleQuantityKind")
SysML_ValueTypes_QUDV_QUDV_SimpleUnit = Class(name="SysML::ValueTypes::QUDV::QUDV::SimpleUnit")
SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities = Class(name="SysML::ValueTypes::QUDV::QUDV::SystemOfQuantities")
SysML_ValueTypes_QUDV_QUDV_SystemOfUnits = Class(name="SysML::ValueTypes::QUDV::QUDV::SystemOfUnits")
SysML_ValueTypes_QUDV_QUDV_Unit = Class(name="SysML::ValueTypes::QUDV::QUDV::Unit", is_abstract=True)
SysML_ValueTypes_QUDV_QUDV_UnitFactor = Class(name="SysML::ValueTypes::QUDV::QUDV::UnitFactor")

# QuantityKind class attributes and methods

# Unit class attributes and methods

# Dimension class attributes and methods

# Prefix class attributes and methods

# QuantityKindFactor class attributes and methods

# SystemOfQuantities class attributes and methods

# SystemOfUnits class attributes and methods

# SysML_ValueTypes_QUDV_ROOT_RESOURCE_SHAPE_CONTAINER class attributes and methods

# Number class attributes and methods

# UnitFactor class attributes and methods

# SysML_ValueTypes_QUDV_PrimitiveValueTypes_Number class attributes and methods
SysML_ValueTypes_QUDV_PrimitiveValueTypes_Number_name: Property = Property(name="name", type=BooleanType)
SysML_ValueTypes_QUDV_PrimitiveValueTypes_Number_m_equals: Method = Method(name="equals", parameters={Parameter(name='x')})
SysML_ValueTypes_QUDV_PrimitiveValueTypes_Number.attributes={SysML_ValueTypes_QUDV_PrimitiveValueTypes_Number_name}
SysML_ValueTypes_QUDV_PrimitiveValueTypes_Number.methods={SysML_ValueTypes_QUDV_PrimitiveValueTypes_Number_m_equals}

# SysML_ValueTypes_QUDV_PrimitiveValueTypes_Complex class attributes and methods
SysML_ValueTypes_QUDV_PrimitiveValueTypes_Complex_m_equals: Method = Method(name="equals", parameters={Parameter(name='x')})
SysML_ValueTypes_QUDV_PrimitiveValueTypes_Complex_m_lessOrEqual: Method = Method(name="lessOrEqual", parameters={Parameter(name='x')})
SysML_ValueTypes_QUDV_PrimitiveValueTypes_Complex_m_lessThan: Method = Method(name="lessThan", parameters={Parameter(name='x')})
SysML_ValueTypes_QUDV_PrimitiveValueTypes_Complex_m_plus: Method = Method(name="plus", parameters={Parameter(name='x')}, type=StringType)
SysML_ValueTypes_QUDV_PrimitiveValueTypes_Complex_m_times: Method = Method(name="times", parameters={Parameter(name='x')}, type=StringType)
SysML_ValueTypes_QUDV_PrimitiveValueTypes_Complex.methods={SysML_ValueTypes_QUDV_PrimitiveValueTypes_Complex_m_lessThan, SysML_ValueTypes_QUDV_PrimitiveValueTypes_Complex_m_lessOrEqual, SysML_ValueTypes_QUDV_PrimitiveValueTypes_Complex_m_times, SysML_ValueTypes_QUDV_PrimitiveValueTypes_Complex_m_plus, SysML_ValueTypes_QUDV_PrimitiveValueTypes_Complex_m_equals}

# SysML_ValueTypes_QUDV_PrimitiveValueTypes_Real class attributes and methods
SysML_ValueTypes_QUDV_PrimitiveValueTypes_Real_m_equals: Method = Method(name="equals", parameters={Parameter(name='x')})
SysML_ValueTypes_QUDV_PrimitiveValueTypes_Real_m_lessOrEqual: Method = Method(name="lessOrEqual", parameters={Parameter(name='x')})
SysML_ValueTypes_QUDV_PrimitiveValueTypes_Real_m_lessThan: Method = Method(name="lessThan", parameters={Parameter(name='x')})
SysML_ValueTypes_QUDV_PrimitiveValueTypes_Real_m_plus: Method = Method(name="plus", parameters={Parameter(name='x')}, type=StringType)
SysML_ValueTypes_QUDV_PrimitiveValueTypes_Real_m_times: Method = Method(name="times", parameters={Parameter(name='x')}, type=StringType)
SysML_ValueTypes_QUDV_PrimitiveValueTypes_Real.methods={SysML_ValueTypes_QUDV_PrimitiveValueTypes_Real_m_plus, SysML_ValueTypes_QUDV_PrimitiveValueTypes_Real_m_lessThan, SysML_ValueTypes_QUDV_PrimitiveValueTypes_Real_m_times, SysML_ValueTypes_QUDV_PrimitiveValueTypes_Real_m_equals, SysML_ValueTypes_QUDV_PrimitiveValueTypes_Real_m_lessOrEqual}

# Real class attributes and methods

# SysML_ValueTypes_QUDV_PrimitiveValueTypes_Integer class attributes and methods
SysML_ValueTypes_QUDV_PrimitiveValueTypes_Integer_m_lessOrEqual: Method = Method(name="lessOrEqual", parameters={Parameter(name='x')})
SysML_ValueTypes_QUDV_PrimitiveValueTypes_Integer_m_lessThan: Method = Method(name="lessThan", parameters={Parameter(name='x')})
SysML_ValueTypes_QUDV_PrimitiveValueTypes_Integer_m_plus: Method = Method(name="plus", parameters={Parameter(name='x')}, type=StringType)
SysML_ValueTypes_QUDV_PrimitiveValueTypes_Integer_m_times: Method = Method(name="times", parameters={Parameter(name='x')}, type=StringType)
SysML_ValueTypes_QUDV_PrimitiveValueTypes_Integer_m_equals: Method = Method(name="equals", parameters={Parameter(name='x')})
SysML_ValueTypes_QUDV_PrimitiveValueTypes_Integer.methods={SysML_ValueTypes_QUDV_PrimitiveValueTypes_Integer_m_times, SysML_ValueTypes_QUDV_PrimitiveValueTypes_Integer_m_lessOrEqual, SysML_ValueTypes_QUDV_PrimitiveValueTypes_Integer_m_plus, SysML_ValueTypes_QUDV_PrimitiveValueTypes_Integer_m_lessThan, SysML_ValueTypes_QUDV_PrimitiveValueTypes_Integer_m_equals}

# SysML_ValueTypes_QUDV_UnitAndQuantityKind_QuantityKind class attributes and methods
SysML_ValueTypes_QUDV_UnitAndQuantityKind_QuantityKind_definitionURI: Property = Property(name="definitionURI", type=StringType)
SysML_ValueTypes_QUDV_UnitAndQuantityKind_QuantityKind_description: Property = Property(name="description", type=StringType)
SysML_ValueTypes_QUDV_UnitAndQuantityKind_QuantityKind_symbol: Property = Property(name="symbol", type=StringType)
SysML_ValueTypes_QUDV_UnitAndQuantityKind_QuantityKind_name: Property = Property(name="name", type=StringType)
SysML_ValueTypes_QUDV_UnitAndQuantityKind_QuantityKind.attributes={SysML_ValueTypes_QUDV_UnitAndQuantityKind_QuantityKind_description, SysML_ValueTypes_QUDV_UnitAndQuantityKind_QuantityKind_name, SysML_ValueTypes_QUDV_UnitAndQuantityKind_QuantityKind_symbol, SysML_ValueTypes_QUDV_UnitAndQuantityKind_QuantityKind_definitionURI}

# SysML_ValueTypes_QUDV_PrimitiveValueTypes_Rational class attributes and methods
SysML_ValueTypes_QUDV_PrimitiveValueTypes_Rational_m_equivalent: Method = Method(name="equivalent", parameters={Parameter(name='r')})
SysML_ValueTypes_QUDV_PrimitiveValueTypes_Rational_m_plus: Method = Method(name="plus", parameters={Parameter(name='r')}, type=StringType)
SysML_ValueTypes_QUDV_PrimitiveValueTypes_Rational_m_times: Method = Method(name="times", parameters={Parameter(name='r')}, type=StringType)
SysML_ValueTypes_QUDV_PrimitiveValueTypes_Rational.methods={SysML_ValueTypes_QUDV_PrimitiveValueTypes_Rational_m_equivalent, SysML_ValueTypes_QUDV_PrimitiveValueTypes_Rational_m_times, SysML_ValueTypes_QUDV_PrimitiveValueTypes_Rational_m_plus}

# Integer class attributes and methods

# SysML_ValueTypes_QUDV_QUDV_AffineConversionUnit class attributes and methods

# ConversionBasedUnit class attributes and methods

# SysML_ValueTypes_QUDV_UnitAndQuantityKind_Unit class attributes and methods
SysML_ValueTypes_QUDV_UnitAndQuantityKind_Unit_name: Property = Property(name="name", type=StringType)
SysML_ValueTypes_QUDV_UnitAndQuantityKind_Unit_definitionURI: Property = Property(name="definitionURI", type=StringType)
SysML_ValueTypes_QUDV_UnitAndQuantityKind_Unit_description: Property = Property(name="description", type=StringType)
SysML_ValueTypes_QUDV_UnitAndQuantityKind_Unit_symbol: Property = Property(name="symbol", type=StringType)
SysML_ValueTypes_QUDV_UnitAndQuantityKind_Unit.attributes={SysML_ValueTypes_QUDV_UnitAndQuantityKind_Unit_symbol, SysML_ValueTypes_QUDV_UnitAndQuantityKind_Unit_definitionURI, SysML_ValueTypes_QUDV_UnitAndQuantityKind_Unit_description, SysML_ValueTypes_QUDV_UnitAndQuantityKind_Unit_name}

# SysML_ValueTypes_QUDV_QUDV_ConversionBasedUnit class attributes and methods
SysML_ValueTypes_QUDV_QUDV_ConversionBasedUnit_isInvertible: Property = Property(name="isInvertible", type=BooleanType)
SysML_ValueTypes_QUDV_QUDV_ConversionBasedUnit_m_dependsOnUnits: Method = Method(name="dependsOnUnits", parameters={}, type=StringType)
SysML_ValueTypes_QUDV_QUDV_ConversionBasedUnit.attributes={SysML_ValueTypes_QUDV_QUDV_ConversionBasedUnit_isInvertible}
SysML_ValueTypes_QUDV_QUDV_ConversionBasedUnit.methods={SysML_ValueTypes_QUDV_QUDV_ConversionBasedUnit_m_dependsOnUnits}

# SysML_ValueTypes_QUDV_QUDV_DerivedQuantityKind class attributes and methods
SysML_ValueTypes_QUDV_QUDV_DerivedQuantityKind_m_dependsOnQuantityKinds: Method = Method(name="dependsOnQuantityKinds", parameters={}, type=StringType)
SysML_ValueTypes_QUDV_QUDV_DerivedQuantityKind.methods={SysML_ValueTypes_QUDV_QUDV_DerivedQuantityKind_m_dependsOnQuantityKinds}

# SysML_ValueTypes_QUDV_QUDV_DerivedUnit class attributes and methods
SysML_ValueTypes_QUDV_QUDV_DerivedUnit_m_dependsOnUnits: Method = Method(name="dependsOnUnits", parameters={}, type=StringType)
SysML_ValueTypes_QUDV_QUDV_DerivedUnit.methods={SysML_ValueTypes_QUDV_QUDV_DerivedUnit_m_dependsOnUnits}

# SysML_ValueTypes_QUDV_QUDV_GeneralConversionUnit class attributes and methods
SysML_ValueTypes_QUDV_QUDV_GeneralConversionUnit_expression: Property = Property(name="expression", type=StringType)
SysML_ValueTypes_QUDV_QUDV_GeneralConversionUnit_expressionLanguageURI: Property = Property(name="expressionLanguageURI", type=StringType)
SysML_ValueTypes_QUDV_QUDV_GeneralConversionUnit.attributes={SysML_ValueTypes_QUDV_QUDV_GeneralConversionUnit_expressionLanguageURI, SysML_ValueTypes_QUDV_QUDV_GeneralConversionUnit_expression}

# SysML_ValueTypes_QUDV_QUDV_LinearConversionUnit class attributes and methods

# SysML_ValueTypes_QUDV_QUDV_Dimension class attributes and methods
SysML_ValueTypes_QUDV_QUDV_Dimension_name: Property = Property(name="name", type=StringType)
SysML_ValueTypes_QUDV_QUDV_Dimension.attributes={SysML_ValueTypes_QUDV_QUDV_Dimension_name}

# SysML_ValueTypes_QUDV_QUDV_PrefixedUnit class attributes and methods

# SysML_ValueTypes_QUDV_QUDV_QuantityKind class attributes and methods
SysML_ValueTypes_QUDV_QUDV_QuantityKind_isNumberOfEntities: Property = Property(name="isNumberOfEntities", type=BooleanType)
SysML_ValueTypes_QUDV_QUDV_QuantityKind_isQuantityOfDimensionOne: Property = Property(name="isQuantityOfDimensionOne", type=BooleanType)
SysML_ValueTypes_QUDV_QUDV_QuantityKind_m_dependsOnQuantityKinds: Method = Method(name="dependsOnQuantityKinds", parameters={}, type=StringType)
SysML_ValueTypes_QUDV_QUDV_QuantityKind.attributes={SysML_ValueTypes_QUDV_QUDV_QuantityKind_isQuantityOfDimensionOne, SysML_ValueTypes_QUDV_QUDV_QuantityKind_isNumberOfEntities}
SysML_ValueTypes_QUDV_QUDV_QuantityKind.methods={SysML_ValueTypes_QUDV_QUDV_QuantityKind_m_dependsOnQuantityKinds}

# SysML_ValueTypes_QUDV_QUDV_Prefix class attributes and methods
SysML_ValueTypes_QUDV_QUDV_Prefix_symbol: Property = Property(name="symbol", type=StringType)
SysML_ValueTypes_QUDV_QUDV_Prefix_name: Property = Property(name="name", type=StringType)
SysML_ValueTypes_QUDV_QUDV_Prefix.attributes={SysML_ValueTypes_QUDV_QUDV_Prefix_symbol, SysML_ValueTypes_QUDV_QUDV_Prefix_name}

# Rational class attributes and methods

# SysML_ValueTypes_QUDV_QUDV_QuantityKindFactor class attributes and methods
SysML_ValueTypes_QUDV_QUDV_QuantityKindFactor_name: Property = Property(name="name", type=StringType)
SysML_ValueTypes_QUDV_QUDV_QuantityKindFactor.attributes={SysML_ValueTypes_QUDV_QUDV_QuantityKindFactor_name}

# SysML_ValueTypes_QUDV_QUDV_SimpleQuantityKind class attributes and methods
SysML_ValueTypes_QUDV_QUDV_SimpleQuantityKind_m_dependsOnQuantityKinds: Method = Method(name="dependsOnQuantityKinds", parameters={}, type=StringType)
SysML_ValueTypes_QUDV_QUDV_SimpleQuantityKind.methods={SysML_ValueTypes_QUDV_QUDV_SimpleQuantityKind_m_dependsOnQuantityKinds}

# SysML_ValueTypes_QUDV_QUDV_SimpleUnit class attributes and methods
SysML_ValueTypes_QUDV_QUDV_SimpleUnit_m_dependsOnUnits: Method = Method(name="dependsOnUnits", parameters={}, type=StringType)
SysML_ValueTypes_QUDV_QUDV_SimpleUnit.methods={SysML_ValueTypes_QUDV_QUDV_SimpleUnit_m_dependsOnUnits}

# SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities class attributes and methods
SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities_symbol: Property = Property(name="symbol", type=StringType)
SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities_name: Property = Property(name="name", type=BooleanType)
SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities_definitionURI: Property = Property(name="definitionURI", type=StringType)
SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities_description: Property = Property(name="description", type=StringType)
SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities_m_allAccessibleQuantityKinds: Method = Method(name="allAccessibleQuantityKinds", parameters={}, type=StringType)
SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities_m_allAccessibleSystemOfQuantities: Method = Method(name="allAccessibleSystemOfQuantities", parameters={}, type=StringType)
SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities_m_allBaseQuantityKinds: Method = Method(name="allBaseQuantityKinds", parameters={}, type=StringType)
SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities_m_allIncludedSystemOfQuantities: Method = Method(name="allIncludedSystemOfQuantities", parameters={}, type=StringType)
SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities_m_allQuantityKinds: Method = Method(name="allQuantityKinds", parameters={}, type=StringType)
SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities_m_getDimension: Method = Method(name="getDimension", parameters={Parameter(name='qk')}, type=StringType)
SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities.attributes={SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities_definitionURI, SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities_description, SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities_name, SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities_symbol}
SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities.methods={SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities_m_allAccessibleQuantityKinds, SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities_m_allAccessibleSystemOfQuantities, SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities_m_allQuantityKinds, SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities_m_allBaseQuantityKinds, SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities_m_getDimension, SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities_m_allIncludedSystemOfQuantities}

# SysML_ValueTypes_QUDV_QUDV_SystemOfUnits class attributes and methods
SysML_ValueTypes_QUDV_QUDV_SystemOfUnits_definitionURI: Property = Property(name="definitionURI", type=StringType)
SysML_ValueTypes_QUDV_QUDV_SystemOfUnits_description: Property = Property(name="description", type=StringType)
SysML_ValueTypes_QUDV_QUDV_SystemOfUnits_name: Property = Property(name="name", type=StringType)
SysML_ValueTypes_QUDV_QUDV_SystemOfUnits_symbol: Property = Property(name="symbol", type=StringType)
SysML_ValueTypes_QUDV_QUDV_SystemOfUnits_m_getUnit: Method = Method(name="getUnit", parameters={Parameter(name='name')}, type=StringType)
SysML_ValueTypes_QUDV_QUDV_SystemOfUnits_m_allBaseQuantityKinds: Method = Method(name="allBaseQuantityKinds", parameters={}, type=StringType)
SysML_ValueTypes_QUDV_QUDV_SystemOfUnits_m_allAccessibleUnits: Method = Method(name="allAccessibleUnits", parameters={}, type=StringType)
SysML_ValueTypes_QUDV_QUDV_SystemOfUnits_m_allBaseUnits: Method = Method(name="allBaseUnits", parameters={}, type=StringType)
SysML_ValueTypes_QUDV_QUDV_SystemOfUnits_m_allIncludedSystemOfUnits: Method = Method(name="allIncludedSystemOfUnits", parameters={}, type=StringType)
SysML_ValueTypes_QUDV_QUDV_SystemOfUnits_m_allMeasurementUnitsDefinedForSomeQuantityKind: Method = Method(name="allMeasurementUnitsDefinedForSomeQuantityKind", parameters={})
SysML_ValueTypes_QUDV_QUDV_SystemOfUnits_m_allPrefixes: Method = Method(name="allPrefixes", parameters={}, type=StringType)
SysML_ValueTypes_QUDV_QUDV_SystemOfUnits_m_allUnits: Method = Method(name="allUnits", parameters={}, type=StringType)
SysML_ValueTypes_QUDV_QUDV_SystemOfUnits_m_getAdoptedBaseUnitForMeasurementUnit: Method = Method(name="getAdoptedBaseUnitForMeasurementUnit", parameters={Parameter(name='u')}, type=StringType)
SysML_ValueTypes_QUDV_QUDV_SystemOfUnits_m_allAccessibleSystemOfUnits: Method = Method(name="allAccessibleSystemOfUnits", parameters={}, type=StringType)
SysML_ValueTypes_QUDV_QUDV_SystemOfUnits_m_getEffectiveSystemOfQuantities: Method = Method(name="getEffectiveSystemOfQuantities", parameters={}, type=StringType)
SysML_ValueTypes_QUDV_QUDV_SystemOfUnits_m_getKindOfQuantitiesForMeasurementUnit: Method = Method(name="getKindOfQuantitiesForMeasurementUnit", parameters={Parameter(name='u')}, type=StringType)
SysML_ValueTypes_QUDV_QUDV_SystemOfUnits_m_isCoherent: Method = Method(name="isCoherent", parameters={Parameter(name='du')})
SysML_ValueTypes_QUDV_QUDV_SystemOfUnits_m_isCoherent: Method = Method(name="isCoherent", parameters={})
SysML_ValueTypes_QUDV_QUDV_SystemOfUnits_m_getAdoptedQuantityKindForAdoptedBaseUnitOfMeasurementUnit: Method = Method(name="getAdoptedQuantityKindForAdoptedBaseUnitOfMeasurementUnit", parameters={Parameter(name='u')}, type=StringType)
SysML_ValueTypes_QUDV_QUDV_SystemOfUnits.attributes={SysML_ValueTypes_QUDV_QUDV_SystemOfUnits_symbol, SysML_ValueTypes_QUDV_QUDV_SystemOfUnits_definitionURI, SysML_ValueTypes_QUDV_QUDV_SystemOfUnits_name, SysML_ValueTypes_QUDV_QUDV_SystemOfUnits_description}
SysML_ValueTypes_QUDV_QUDV_SystemOfUnits.methods={SysML_ValueTypes_QUDV_QUDV_SystemOfUnits_m_isCoherent, SysML_ValueTypes_QUDV_QUDV_SystemOfUnits_m_allBaseQuantityKinds, SysML_ValueTypes_QUDV_QUDV_SystemOfUnits_m_allIncludedSystemOfUnits, SysML_ValueTypes_QUDV_QUDV_SystemOfUnits_m_allAccessibleSystemOfUnits, SysML_ValueTypes_QUDV_QUDV_SystemOfUnits_m_getAdoptedQuantityKindForAdoptedBaseUnitOfMeasurementUnit, SysML_ValueTypes_QUDV_QUDV_SystemOfUnits_m_getEffectiveSystemOfQuantities, SysML_ValueTypes_QUDV_QUDV_SystemOfUnits_m_getKindOfQuantitiesForMeasurementUnit, SysML_ValueTypes_QUDV_QUDV_SystemOfUnits_m_isCoherent, SysML_ValueTypes_QUDV_QUDV_SystemOfUnits_m_allPrefixes, SysML_ValueTypes_QUDV_QUDV_SystemOfUnits_m_allAccessibleUnits, SysML_ValueTypes_QUDV_QUDV_SystemOfUnits_m_allBaseUnits, SysML_ValueTypes_QUDV_QUDV_SystemOfUnits_m_allMeasurementUnitsDefinedForSomeQuantityKind, SysML_ValueTypes_QUDV_QUDV_SystemOfUnits_m_allUnits, SysML_ValueTypes_QUDV_QUDV_SystemOfUnits_m_getAdoptedBaseUnitForMeasurementUnit, SysML_ValueTypes_QUDV_QUDV_SystemOfUnits_m_getUnit}

# SysML_ValueTypes_QUDV_QUDV_Unit class attributes and methods
SysML_ValueTypes_QUDV_QUDV_Unit_isUnitCountOfEntities: Property = Property(name="isUnitCountOfEntities", type=BooleanType)
SysML_ValueTypes_QUDV_QUDV_Unit_isUnitForQuantityOfDimensionOne: Property = Property(name="isUnitForQuantityOfDimensionOne", type=BooleanType)
SysML_ValueTypes_QUDV_QUDV_Unit_m_dependsOnUnits: Method = Method(name="dependsOnUnits", parameters={}, type=StringType)
SysML_ValueTypes_QUDV_QUDV_Unit.attributes={SysML_ValueTypes_QUDV_QUDV_Unit_isUnitCountOfEntities, SysML_ValueTypes_QUDV_QUDV_Unit_isUnitForQuantityOfDimensionOne}
SysML_ValueTypes_QUDV_QUDV_Unit.methods={SysML_ValueTypes_QUDV_QUDV_Unit_m_dependsOnUnits}

# SysML_ValueTypes_QUDV_QUDV_UnitFactor class attributes and methods
SysML_ValueTypes_QUDV_QUDV_UnitFactor_name: Property = Property(name="name", type=StringType)
SysML_ValueTypes_QUDV_QUDV_UnitFactor.attributes={SysML_ValueTypes_QUDV_QUDV_UnitFactor_name}

# Relationships
quantityKind1: BinaryAssociation = BinaryAssociation(
    name="quantityKind1",
    ends={
        Property(name="QuantityKind", type=SysML_ValueTypes_QUDV_ROOT_RESOURCE_SHAPE_CONTAINER, multiplicity=Multiplicity(1, 1)),
        Property(name="SysML_ValueTypes_QUDV_ROOT_RESOURCE_SHAPE_CONTAINER2", type=QuantityKind, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
unit3: BinaryAssociation = BinaryAssociation(
    name="unit3",
    ends={
        Property(name="Unit", type=SysML_ValueTypes_QUDV_ROOT_RESOURCE_SHAPE_CONTAINER, multiplicity=Multiplicity(1, 1)),
        Property(name="SysML_ValueTypes_QUDV_ROOT_RESOURCE_SHAPE_CONTAINER4", type=Unit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dimension5: BinaryAssociation = BinaryAssociation(
    name="dimension5",
    ends={
        Property(name="Dimension", type=SysML_ValueTypes_QUDV_ROOT_RESOURCE_SHAPE_CONTAINER, multiplicity=Multiplicity(1, 1)),
        Property(name="SysML_ValueTypes_QUDV_ROOT_RESOURCE_SHAPE_CONTAINER6", type=Dimension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
prefix7: BinaryAssociation = BinaryAssociation(
    name="prefix7",
    ends={
        Property(name="Prefix", type=SysML_ValueTypes_QUDV_ROOT_RESOURCE_SHAPE_CONTAINER, multiplicity=Multiplicity(1, 1)),
        Property(name="SysML_ValueTypes_QUDV_ROOT_RESOURCE_SHAPE_CONTAINER8", type=Prefix, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
quantityKindFactor9: BinaryAssociation = BinaryAssociation(
    name="quantityKindFactor9",
    ends={
        Property(name="QuantityKindFactor", type=SysML_ValueTypes_QUDV_ROOT_RESOURCE_SHAPE_CONTAINER, multiplicity=Multiplicity(1, 1)),
        Property(name="SysML_ValueTypes_QUDV_ROOT_RESOURCE_SHAPE_CONTAINER10", type=QuantityKindFactor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
systemOfQuantities11: BinaryAssociation = BinaryAssociation(
    name="systemOfQuantities11",
    ends={
        Property(name="SystemOfQuantities", type=SysML_ValueTypes_QUDV_ROOT_RESOURCE_SHAPE_CONTAINER, multiplicity=Multiplicity(1, 1)),
        Property(name="SysML_ValueTypes_QUDV_ROOT_RESOURCE_SHAPE_CONTAINER12", type=SystemOfQuantities, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
number0: BinaryAssociation = BinaryAssociation(
    name="number0",
    ends={
        Property(name="Number", type=SysML_ValueTypes_QUDV_ROOT_RESOURCE_SHAPE_CONTAINER, multiplicity=Multiplicity(1, 1)),
        Property(name="SysML_ValueTypes_QUDV_ROOT_RESOURCE_SHAPE_CONTAINER", type=Number, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
unitFactor15: BinaryAssociation = BinaryAssociation(
    name="unitFactor15",
    ends={
        Property(name="UnitFactor", type=SysML_ValueTypes_QUDV_ROOT_RESOURCE_SHAPE_CONTAINER, multiplicity=Multiplicity(1, 1)),
        Property(name="SysML_ValueTypes_QUDV_ROOT_RESOURCE_SHAPE_CONTAINER16", type=UnitFactor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
systemOfUnits13: BinaryAssociation = BinaryAssociation(
    name="systemOfUnits13",
    ends={
        Property(name="SystemOfUnits", type=SysML_ValueTypes_QUDV_ROOT_RESOURCE_SHAPE_CONTAINER, multiplicity=Multiplicity(1, 1)),
        Property(name="SysML_ValueTypes_QUDV_ROOT_RESOURCE_SHAPE_CONTAINER14", type=SystemOfUnits, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
realPart17: BinaryAssociation = BinaryAssociation(
    name="realPart17",
    ends={
        Property(name="Real", type=SysML_ValueTypes_QUDV_PrimitiveValueTypes_Complex, multiplicity=Multiplicity(1, 1)),
        Property(name="SysML_ValueTypes_QUDV_PrimitiveValueTypes_Complex", type=Real, multiplicity=Multiplicity(1, 1))
    }
)
imaginaryPart18: BinaryAssociation = BinaryAssociation(
    name="imaginaryPart18",
    ends={
        Property(name="Real20", type=SysML_ValueTypes_QUDV_PrimitiveValueTypes_Complex, multiplicity=Multiplicity(1, 1)),
        Property(name="SysML_ValueTypes_QUDV_PrimitiveValueTypes_Complex19", type=Real, multiplicity=Multiplicity(1, 1))
    }
)
denominator22: BinaryAssociation = BinaryAssociation(
    name="denominator22",
    ends={
        Property(name="Integer24", type=SysML_ValueTypes_QUDV_PrimitiveValueTypes_Rational, multiplicity=Multiplicity(1, 1)),
        Property(name="SysML_ValueTypes_QUDV_PrimitiveValueTypes_Rational23", type=Integer, multiplicity=Multiplicity(1, 1))
    }
)
numerator21: BinaryAssociation = BinaryAssociation(
    name="numerator21",
    ends={
        Property(name="Integer", type=SysML_ValueTypes_QUDV_PrimitiveValueTypes_Rational, multiplicity=Multiplicity(1, 1)),
        Property(name="SysML_ValueTypes_QUDV_PrimitiveValueTypes_Rational", type=Integer, multiplicity=Multiplicity(1, 1))
    }
)
factor27: BinaryAssociation = BinaryAssociation(
    name="factor27",
    ends={
        Property(name="Number28", type=SysML_ValueTypes_QUDV_QUDV_AffineConversionUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="SysML_ValueTypes_QUDV_QUDV_AffineConversionUnit", type=Number, multiplicity=Multiplicity(1, 1))
    }
)
offset29: BinaryAssociation = BinaryAssociation(
    name="offset29",
    ends={
        Property(name="Number31", type=SysML_ValueTypes_QUDV_QUDV_AffineConversionUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="SysML_ValueTypes_QUDV_QUDV_AffineConversionUnit30", type=Number, multiplicity=Multiplicity(1, 1))
    }
)
quantityKind25: BinaryAssociation = BinaryAssociation(
    name="quantityKind25",
    ends={
        Property(name="QuantityKind26", type=SysML_ValueTypes_QUDV_UnitAndQuantityKind_Unit, multiplicity=Multiplicity(1, 1)),
        Property(name="SysML_ValueTypes_QUDV_UnitAndQuantityKind_Unit", type=QuantityKind, multiplicity=Multiplicity(0, 9999))
    }
)
referenceUnit32: BinaryAssociation = BinaryAssociation(
    name="referenceUnit32",
    ends={
        Property(name="Unit33", type=SysML_ValueTypes_QUDV_QUDV_ConversionBasedUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="SysML_ValueTypes_QUDV_QUDV_ConversionBasedUnit", type=Unit, multiplicity=Multiplicity(1, 1))
    }
)
factor34: BinaryAssociation = BinaryAssociation(
    name="factor34",
    ends={
        Property(name="QuantityKindFactor35", type=SysML_ValueTypes_QUDV_QUDV_DerivedQuantityKind, multiplicity=Multiplicity(1, 1)),
        Property(name="SysML_ValueTypes_QUDV_QUDV_DerivedQuantityKind", type=QuantityKindFactor, multiplicity=Multiplicity(1, 9999))
    }
)
factor38: BinaryAssociation = BinaryAssociation(
    name="factor38",
    ends={
        Property(name="QuantityKindFactor39", type=SysML_ValueTypes_QUDV_QUDV_Dimension, multiplicity=Multiplicity(1, 1)),
        Property(name="SysML_ValueTypes_QUDV_QUDV_Dimension", type=QuantityKindFactor, multiplicity=Multiplicity(0, 9999))
    }
)
factor40: BinaryAssociation = BinaryAssociation(
    name="factor40",
    ends={
        Property(name="Number41", type=SysML_ValueTypes_QUDV_QUDV_LinearConversionUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="SysML_ValueTypes_QUDV_QUDV_LinearConversionUnit", type=Number, multiplicity=Multiplicity(1, 1))
    }
)
factor36: BinaryAssociation = BinaryAssociation(
    name="factor36",
    ends={
        Property(name="UnitFactor37", type=SysML_ValueTypes_QUDV_QUDV_DerivedUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="SysML_ValueTypes_QUDV_QUDV_DerivedUnit", type=UnitFactor, multiplicity=Multiplicity(1, 9999))
    }
)
prefix43: BinaryAssociation = BinaryAssociation(
    name="prefix43",
    ends={
        Property(name="Prefix44", type=SysML_ValueTypes_QUDV_QUDV_PrefixedUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="SysML_ValueTypes_QUDV_QUDV_PrefixedUnit", type=Prefix, multiplicity=Multiplicity(1, 1))
    }
)
dependsOnQuantityKinds45: BinaryAssociation = BinaryAssociation(
    name="dependsOnQuantityKinds45",
    ends={
        Property(name="QuantityKind46", type=SysML_ValueTypes_QUDV_QUDV_QuantityKind, multiplicity=Multiplicity(1, 1)),
        Property(name="SysML_ValueTypes_QUDV_QUDV_QuantityKind", type=QuantityKind, multiplicity=Multiplicity(0, 9999))
    }
)
factor42: BinaryAssociation = BinaryAssociation(
    name="factor42",
    ends={
        Property(name="Rational", type=SysML_ValueTypes_QUDV_QUDV_Prefix, multiplicity=Multiplicity(1, 1)),
        Property(name="SysML_ValueTypes_QUDV_QUDV_Prefix", type=Rational, multiplicity=Multiplicity(1, 1))
    }
)
exponent50: BinaryAssociation = BinaryAssociation(
    name="exponent50",
    ends={
        Property(name="Rational51", type=SysML_ValueTypes_QUDV_QUDV_QuantityKindFactor, multiplicity=Multiplicity(1, 1)),
        Property(name="SysML_ValueTypes_QUDV_QUDV_QuantityKindFactor", type=Rational, multiplicity=Multiplicity(1, 1))
    }
)
quantityKind52: BinaryAssociation = BinaryAssociation(
    name="quantityKind52",
    ends={
        Property(name="QuantityKind54", type=SysML_ValueTypes_QUDV_QUDV_QuantityKindFactor, multiplicity=Multiplicity(1, 1)),
        Property(name="SysML_ValueTypes_QUDV_QUDV_QuantityKindFactor53", type=QuantityKind, multiplicity=Multiplicity(1, 1))
    }
)
general47: BinaryAssociation = BinaryAssociation(
    name="general47",
    ends={
        Property(name="QuantityKind49", type=SysML_ValueTypes_QUDV_QUDV_QuantityKind, multiplicity=Multiplicity(1, 1)),
        Property(name="SysML_ValueTypes_QUDV_QUDV_QuantityKind48", type=QuantityKind, multiplicity=Multiplicity(0, 9999))
    }
)
baseQuantityKind55: BinaryAssociation = BinaryAssociation(
    name="baseQuantityKind55",
    ends={
        Property(name="QuantityKind56", type=SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities, multiplicity=Multiplicity(1, 1)),
        Property(name="SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities", type=QuantityKind, multiplicity=Multiplicity(0, 9999))
    }
)
includedSystemOfQuantities57: BinaryAssociation = BinaryAssociation(
    name="includedSystemOfQuantities57",
    ends={
        Property(name="SystemOfQuantities59", type=SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities, multiplicity=Multiplicity(1, 1)),
        Property(name="SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities58", type=SystemOfQuantities, multiplicity=Multiplicity(0, 9999))
    }
)
quantityKind60: BinaryAssociation = BinaryAssociation(
    name="quantityKind60",
    ends={
        Property(name="QuantityKind62", type=SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities, multiplicity=Multiplicity(1, 1)),
        Property(name="SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities61", type=QuantityKind, multiplicity=Multiplicity(0, 9999))
    }
)
usedSystemOfQuantities63: BinaryAssociation = BinaryAssociation(
    name="usedSystemOfQuantities63",
    ends={
        Property(name="SystemOfQuantities65", type=SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities, multiplicity=Multiplicity(1, 1)),
        Property(name="SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities64", type=SystemOfQuantities, multiplicity=Multiplicity(0, 9999))
    }
)
baseUnit66: BinaryAssociation = BinaryAssociation(
    name="baseUnit66",
    ends={
        Property(name="Unit67", type=SysML_ValueTypes_QUDV_QUDV_SystemOfUnits, multiplicity=Multiplicity(1, 1)),
        Property(name="SysML_ValueTypes_QUDV_QUDV_SystemOfUnits", type=Unit, multiplicity=Multiplicity(0, 9999))
    }
)
includedSystemOfUnits68: BinaryAssociation = BinaryAssociation(
    name="includedSystemOfUnits68",
    ends={
        Property(name="SystemOfUnits70", type=SysML_ValueTypes_QUDV_QUDV_SystemOfUnits, multiplicity=Multiplicity(1, 1)),
        Property(name="SysML_ValueTypes_QUDV_QUDV_SystemOfUnits69", type=SystemOfUnits, multiplicity=Multiplicity(0, 9999))
    }
)
systemOfQuantities74: BinaryAssociation = BinaryAssociation(
    name="systemOfQuantities74",
    ends={
        Property(name="SystemOfQuantities76", type=SysML_ValueTypes_QUDV_QUDV_SystemOfUnits, multiplicity=Multiplicity(1, 1)),
        Property(name="SysML_ValueTypes_QUDV_QUDV_SystemOfUnits75", type=SystemOfQuantities, multiplicity=Multiplicity(0, 1))
    }
)
unit77: BinaryAssociation = BinaryAssociation(
    name="unit77",
    ends={
        Property(name="Unit79", type=SysML_ValueTypes_QUDV_QUDV_SystemOfUnits, multiplicity=Multiplicity(1, 1)),
        Property(name="SysML_ValueTypes_QUDV_QUDV_SystemOfUnits78", type=Unit, multiplicity=Multiplicity(0, 9999))
    }
)
usedSystemOfUnits80: BinaryAssociation = BinaryAssociation(
    name="usedSystemOfUnits80",
    ends={
        Property(name="SystemOfUnits82", type=SysML_ValueTypes_QUDV_QUDV_SystemOfUnits, multiplicity=Multiplicity(1, 1)),
        Property(name="SysML_ValueTypes_QUDV_QUDV_SystemOfUnits81", type=SystemOfUnits, multiplicity=Multiplicity(0, 9999))
    }
)
dependsOnUnits83: BinaryAssociation = BinaryAssociation(
    name="dependsOnUnits83",
    ends={
        Property(name="Unit84", type=SysML_ValueTypes_QUDV_QUDV_Unit, multiplicity=Multiplicity(1, 1)),
        Property(name="SysML_ValueTypes_QUDV_QUDV_Unit", type=Unit, multiplicity=Multiplicity(0, 9999))
    }
)
prefix71: BinaryAssociation = BinaryAssociation(
    name="prefix71",
    ends={
        Property(name="Prefix73", type=SysML_ValueTypes_QUDV_QUDV_SystemOfUnits, multiplicity=Multiplicity(1, 1)),
        Property(name="SysML_ValueTypes_QUDV_QUDV_SystemOfUnits72", type=Prefix, multiplicity=Multiplicity(0, 9999))
    }
)
exponent88: BinaryAssociation = BinaryAssociation(
    name="exponent88",
    ends={
        Property(name="Rational89", type=SysML_ValueTypes_QUDV_QUDV_UnitFactor, multiplicity=Multiplicity(1, 1)),
        Property(name="SysML_ValueTypes_QUDV_QUDV_UnitFactor", type=Rational, multiplicity=Multiplicity(1, 1))
    }
)
unit90: BinaryAssociation = BinaryAssociation(
    name="unit90",
    ends={
        Property(name="Unit92", type=SysML_ValueTypes_QUDV_QUDV_UnitFactor, multiplicity=Multiplicity(1, 1)),
        Property(name="SysML_ValueTypes_QUDV_QUDV_UnitFactor91", type=Unit, multiplicity=Multiplicity(1, 1))
    }
)
general85: BinaryAssociation = BinaryAssociation(
    name="general85",
    ends={
        Property(name="Unit87", type=SysML_ValueTypes_QUDV_QUDV_Unit, multiplicity=Multiplicity(1, 1)),
        Property(name="SysML_ValueTypes_QUDV_QUDV_Unit86", type=Unit, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_SysML_ValueTypes_QUDV_PrimitiveValueTypes_Complex_Number = Generalization(general=Number, specific=SysML_ValueTypes_QUDV_PrimitiveValueTypes_Complex)
gen_SysML_ValueTypes_QUDV_PrimitiveValueTypes_Real_Number = Generalization(general=Number, specific=SysML_ValueTypes_QUDV_PrimitiveValueTypes_Real)
gen_SysML_ValueTypes_QUDV_PrimitiveValueTypes_Integer_Number = Generalization(general=Number, specific=SysML_ValueTypes_QUDV_PrimitiveValueTypes_Integer)
gen_SysML_ValueTypes_QUDV_PrimitiveValueTypes_Rational_Number = Generalization(general=Number, specific=SysML_ValueTypes_QUDV_PrimitiveValueTypes_Rational)
gen_SysML_ValueTypes_QUDV_QUDV_AffineConversionUnit_ConversionBasedUnit = Generalization(general=ConversionBasedUnit, specific=SysML_ValueTypes_QUDV_QUDV_AffineConversionUnit)
gen_SysML_ValueTypes_QUDV_QUDV_ConversionBasedUnit_Unit = Generalization(general=Unit, specific=SysML_ValueTypes_QUDV_QUDV_ConversionBasedUnit)
gen_SysML_ValueTypes_QUDV_QUDV_DerivedQuantityKind_QuantityKind = Generalization(general=QuantityKind, specific=SysML_ValueTypes_QUDV_QUDV_DerivedQuantityKind)
gen_SysML_ValueTypes_QUDV_QUDV_DerivedUnit_Unit = Generalization(general=Unit, specific=SysML_ValueTypes_QUDV_QUDV_DerivedUnit)
gen_SysML_ValueTypes_QUDV_QUDV_GeneralConversionUnit_ConversionBasedUnit = Generalization(general=ConversionBasedUnit, specific=SysML_ValueTypes_QUDV_QUDV_GeneralConversionUnit)
gen_SysML_ValueTypes_QUDV_QUDV_LinearConversionUnit_ConversionBasedUnit = Generalization(general=ConversionBasedUnit, specific=SysML_ValueTypes_QUDV_QUDV_LinearConversionUnit)
gen_SysML_ValueTypes_QUDV_QUDV_PrefixedUnit_ConversionBasedUnit = Generalization(general=ConversionBasedUnit, specific=SysML_ValueTypes_QUDV_QUDV_PrefixedUnit)
gen_SysML_ValueTypes_QUDV_QUDV_QuantityKind_QuantityKind = Generalization(general=QuantityKind, specific=SysML_ValueTypes_QUDV_QUDV_QuantityKind)
gen_SysML_ValueTypes_QUDV_QUDV_SimpleQuantityKind_QuantityKind = Generalization(general=QuantityKind, specific=SysML_ValueTypes_QUDV_QUDV_SimpleQuantityKind)
gen_SysML_ValueTypes_QUDV_QUDV_SimpleUnit_Unit = Generalization(general=Unit, specific=SysML_ValueTypes_QUDV_QUDV_SimpleUnit)
gen_SysML_ValueTypes_QUDV_QUDV_Unit_Unit = Generalization(general=Unit, specific=SysML_ValueTypes_QUDV_QUDV_Unit)

# Domain Model
domain_model = DomainModel(
    name="SysML_ValueTypes_QUDV",
    types={QuantityKind, Unit, Dimension, Prefix, QuantityKindFactor, SystemOfQuantities, SystemOfUnits, SysML_ValueTypes_QUDV_ROOT_RESOURCE_SHAPE_CONTAINER, Number, UnitFactor, SysML_ValueTypes_QUDV_PrimitiveValueTypes_Number, SysML_ValueTypes_QUDV_PrimitiveValueTypes_Complex, SysML_ValueTypes_QUDV_PrimitiveValueTypes_Real, Real, SysML_ValueTypes_QUDV_PrimitiveValueTypes_Integer, SysML_ValueTypes_QUDV_UnitAndQuantityKind_QuantityKind, SysML_ValueTypes_QUDV_PrimitiveValueTypes_Rational, Integer, SysML_ValueTypes_QUDV_QUDV_AffineConversionUnit, ConversionBasedUnit, SysML_ValueTypes_QUDV_UnitAndQuantityKind_Unit, SysML_ValueTypes_QUDV_QUDV_ConversionBasedUnit, SysML_ValueTypes_QUDV_QUDV_DerivedQuantityKind, SysML_ValueTypes_QUDV_QUDV_DerivedUnit, SysML_ValueTypes_QUDV_QUDV_GeneralConversionUnit, SysML_ValueTypes_QUDV_QUDV_LinearConversionUnit, SysML_ValueTypes_QUDV_QUDV_Dimension, SysML_ValueTypes_QUDV_QUDV_PrefixedUnit, SysML_ValueTypes_QUDV_QUDV_QuantityKind, SysML_ValueTypes_QUDV_QUDV_Prefix, Rational, SysML_ValueTypes_QUDV_QUDV_QuantityKindFactor, SysML_ValueTypes_QUDV_QUDV_SimpleQuantityKind, SysML_ValueTypes_QUDV_QUDV_SimpleUnit, SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities, SysML_ValueTypes_QUDV_QUDV_SystemOfUnits, SysML_ValueTypes_QUDV_QUDV_Unit, SysML_ValueTypes_QUDV_QUDV_UnitFactor},
    associations={quantityKind1, unit3, dimension5, prefix7, quantityKindFactor9, systemOfQuantities11, number0, unitFactor15, systemOfUnits13, realPart17, imaginaryPart18, denominator22, numerator21, factor27, offset29, quantityKind25, referenceUnit32, factor34, factor38, factor40, factor36, prefix43, dependsOnQuantityKinds45, factor42, exponent50, quantityKind52, general47, baseQuantityKind55, includedSystemOfQuantities57, quantityKind60, usedSystemOfQuantities63, baseUnit66, includedSystemOfUnits68, systemOfQuantities74, unit77, usedSystemOfUnits80, dependsOnUnits83, prefix71, exponent88, unit90, general85},
    generalizations={gen_SysML_ValueTypes_QUDV_PrimitiveValueTypes_Complex_Number, gen_SysML_ValueTypes_QUDV_PrimitiveValueTypes_Real_Number, gen_SysML_ValueTypes_QUDV_PrimitiveValueTypes_Integer_Number, gen_SysML_ValueTypes_QUDV_PrimitiveValueTypes_Rational_Number, gen_SysML_ValueTypes_QUDV_QUDV_AffineConversionUnit_ConversionBasedUnit, gen_SysML_ValueTypes_QUDV_QUDV_ConversionBasedUnit_Unit, gen_SysML_ValueTypes_QUDV_QUDV_DerivedQuantityKind_QuantityKind, gen_SysML_ValueTypes_QUDV_QUDV_DerivedUnit_Unit, gen_SysML_ValueTypes_QUDV_QUDV_GeneralConversionUnit_ConversionBasedUnit, gen_SysML_ValueTypes_QUDV_QUDV_LinearConversionUnit_ConversionBasedUnit, gen_SysML_ValueTypes_QUDV_QUDV_PrefixedUnit_ConversionBasedUnit, gen_SysML_ValueTypes_QUDV_QUDV_QuantityKind_QuantityKind, gen_SysML_ValueTypes_QUDV_QUDV_SimpleQuantityKind_QuantityKind, gen_SysML_ValueTypes_QUDV_QUDV_SimpleUnit_Unit, gen_SysML_ValueTypes_QUDV_QUDV_Unit_Unit},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)