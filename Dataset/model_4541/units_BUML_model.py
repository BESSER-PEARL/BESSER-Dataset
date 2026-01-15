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
units_Centimeter = Class(name="units::Centimeter")
MetricSystemUnit = Class(name="MetricSystemUnit")
LengthUnit = Class(name="LengthUnit")
units_Millimeter = Class(name="units::Millimeter")
units_Meter = Class(name="units::Meter")
units_Foot = Class(name="units::Foot")
ImperialSystemUnit = Class(name="ImperialSystemUnit")
units_Inch = Class(name="units::Inch")
units_Unit = Class(name="units::Unit", is_abstract=True)
units_LengthUnit = Class(name="units::LengthUnit", is_abstract=True)
Unit = Class(name="Unit")
units_LengthSubtract = Class(name="units::LengthSubtract")
units_LengthScalarMultiply = Class(name="units::LengthScalarMultiply")
QuantityScalarOperation = Class(name="QuantityScalarOperation")
units_LengthScalarDivide = Class(name="units::LengthScalarDivide")
units_LengthEquals = Class(name="units::LengthEquals")
units_LengthDistinct = Class(name="units::LengthDistinct")
units_LengthSmaller = Class(name="units::LengthSmaller")
units_Yard = Class(name="units::Yard")
units_MetricSystemUnit = Class(name="units::MetricSystemUnit", is_abstract=True)
units_ImperialSystemUnit = Class(name="units::ImperialSystemUnit", is_abstract=True)
units_AngleUnit = Class(name="units::AngleUnit", is_abstract=True)
units_Radian = Class(name="units::Radian")
AngleUnit = Class(name="AngleUnit")
units_Degree = Class(name="units::Degree")
units_Turn = Class(name="units::Turn")
units_Gradian = Class(name="units::Gradian")
units_Quantity = Class(name="units::Quantity", is_abstract=True)
units_Length = Class(name="units::Length")
Quantity = Class(name="Quantity")
units_Angle = Class(name="units::Angle")
units_QuantityOperation = Class(name="units::QuantityOperation", is_abstract=True)
units_LengthOperation = Class(name="units::LengthOperation", is_abstract=True)
QuantityOperation = Class(name="QuantityOperation")
units_LengthAdd = Class(name="units::LengthAdd")
LengthOperation = Class(name="LengthOperation")
QuantityHomogenousOperation = Class(name="QuantityHomogenousOperation")
units_LengthGreater = Class(name="units::LengthGreater")
units_AngleOperation = Class(name="units::AngleOperation", is_abstract=True)
units_AngleAdd = Class(name="units::AngleAdd")
AngleOperation = Class(name="AngleOperation")
units_AngleSubtract = Class(name="units::AngleSubtract")
units_AngleScalarMultiply = Class(name="units::AngleScalarMultiply")
units_AngleScalarDivide = Class(name="units::AngleScalarDivide")
units_AngleEquals = Class(name="units::AngleEquals")
units_AngleDistinct = Class(name="units::AngleDistinct")
units_AngleSmaller = Class(name="units::AngleSmaller")
units_AngleGreater = Class(name="units::AngleGreater")
units_QuantityArithmeticOperation = Class(name="units::QuantityArithmeticOperation", is_abstract=True)
units_QuantityComparisonOperation = Class(name="units::QuantityComparisonOperation", is_abstract=True)
units_QuantityHomogenousOperation = Class(name="units::QuantityHomogenousOperation", is_abstract=True)
units_QuantityScalarOperation = Class(name="units::QuantityScalarOperation", is_abstract=True)

# units_Centimeter class attributes and methods

# MetricSystemUnit class attributes and methods

# LengthUnit class attributes and methods

# units_Millimeter class attributes and methods

# units_Meter class attributes and methods

# units_Foot class attributes and methods

# ImperialSystemUnit class attributes and methods

# units_Inch class attributes and methods

# units_Unit class attributes and methods

# units_LengthUnit class attributes and methods

# Unit class attributes and methods

# units_LengthSubtract class attributes and methods

# units_LengthScalarMultiply class attributes and methods

# QuantityScalarOperation class attributes and methods

# units_LengthScalarDivide class attributes and methods

# units_LengthEquals class attributes and methods

# units_LengthDistinct class attributes and methods

# units_LengthSmaller class attributes and methods

# units_Yard class attributes and methods

# units_MetricSystemUnit class attributes and methods

# units_ImperialSystemUnit class attributes and methods

# units_AngleUnit class attributes and methods

# units_Radian class attributes and methods

# AngleUnit class attributes and methods

# units_Degree class attributes and methods

# units_Turn class attributes and methods

# units_Gradian class attributes and methods

# units_Quantity class attributes and methods
units_Quantity_value: Property = Property(name="value", type=FloatType)
units_Quantity.attributes={units_Quantity_value}

# units_Length class attributes and methods

# Quantity class attributes and methods

# units_Angle class attributes and methods

# units_QuantityOperation class attributes and methods

# units_LengthOperation class attributes and methods

# QuantityOperation class attributes and methods

# units_LengthAdd class attributes and methods

# LengthOperation class attributes and methods

# QuantityHomogenousOperation class attributes and methods

# units_LengthGreater class attributes and methods

# units_AngleOperation class attributes and methods

# units_AngleAdd class attributes and methods

# AngleOperation class attributes and methods

# units_AngleSubtract class attributes and methods

# units_AngleScalarMultiply class attributes and methods

# units_AngleScalarDivide class attributes and methods

# units_AngleEquals class attributes and methods

# units_AngleDistinct class attributes and methods

# units_AngleSmaller class attributes and methods

# units_AngleGreater class attributes and methods

# units_QuantityArithmeticOperation class attributes and methods

# units_QuantityComparisonOperation class attributes and methods

# units_QuantityHomogenousOperation class attributes and methods

# units_QuantityScalarOperation class attributes and methods
units_QuantityScalarOperation_rhs: Property = Property(name="rhs", type=FloatType)
units_QuantityScalarOperation.attributes={units_QuantityScalarOperation_rhs}

# Relationships
unit0: BinaryAssociation = BinaryAssociation(
    name="unit0",
    ends={
        Property(name="units_Unit", type=units_Quantity, multiplicity=Multiplicity(1, 1)),
        Property(name="units_Quantity", type=units_Unit, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lhs1: BinaryAssociation = BinaryAssociation(
    name="lhs1",
    ends={
        Property(name="units_Quantity2", type=units_QuantityHomogenousOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="units_QuantityHomogenousOperation", type=units_Quantity, multiplicity=Multiplicity(1, 1))
    }
)
rhs3: BinaryAssociation = BinaryAssociation(
    name="rhs3",
    ends={
        Property(name="units_Quantity5", type=units_QuantityHomogenousOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="units_QuantityHomogenousOperation4", type=units_Quantity, multiplicity=Multiplicity(1, 1))
    }
)
lhs6: BinaryAssociation = BinaryAssociation(
    name="lhs6",
    ends={
        Property(name="units_Quantity7", type=units_QuantityScalarOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="units_QuantityScalarOperation", type=units_Quantity, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_units_Centimeter_MetricSystemUnit = Generalization(general=MetricSystemUnit, specific=units_Centimeter)
gen_units_Centimeter_LengthUnit = Generalization(general=LengthUnit, specific=units_Centimeter)
gen_units_Millimeter_MetricSystemUnit = Generalization(general=MetricSystemUnit, specific=units_Millimeter)
gen_units_Millimeter_LengthUnit = Generalization(general=LengthUnit, specific=units_Millimeter)
gen_units_Meter_MetricSystemUnit = Generalization(general=MetricSystemUnit, specific=units_Meter)
gen_units_Meter_LengthUnit = Generalization(general=LengthUnit, specific=units_Meter)
gen_units_Foot_ImperialSystemUnit = Generalization(general=ImperialSystemUnit, specific=units_Foot)
gen_units_Foot_LengthUnit = Generalization(general=LengthUnit, specific=units_Foot)
gen_units_Inch_ImperialSystemUnit = Generalization(general=ImperialSystemUnit, specific=units_Inch)
gen_units_Inch_LengthUnit = Generalization(general=LengthUnit, specific=units_Inch)
gen_units_LengthUnit_Unit = Generalization(general=Unit, specific=units_LengthUnit)
gen_units_LengthSubtract_LengthOperation = Generalization(general=LengthOperation, specific=units_LengthSubtract)
gen_units_LengthSubtract_QuantityHomogenousOperation = Generalization(general=QuantityHomogenousOperation, specific=units_LengthSubtract)
gen_units_LengthScalarMultiply_LengthOperation = Generalization(general=LengthOperation, specific=units_LengthScalarMultiply)
gen_units_LengthScalarMultiply_QuantityScalarOperation = Generalization(general=QuantityScalarOperation, specific=units_LengthScalarMultiply)
gen_units_LengthScalarDivide_LengthOperation = Generalization(general=LengthOperation, specific=units_LengthScalarDivide)
gen_units_LengthScalarDivide_QuantityScalarOperation = Generalization(general=QuantityScalarOperation, specific=units_LengthScalarDivide)
gen_units_LengthEquals_LengthOperation = Generalization(general=LengthOperation, specific=units_LengthEquals)
gen_units_LengthEquals_QuantityHomogenousOperation = Generalization(general=QuantityHomogenousOperation, specific=units_LengthEquals)
gen_units_LengthDistinct_LengthOperation = Generalization(general=LengthOperation, specific=units_LengthDistinct)
gen_units_LengthDistinct_QuantityHomogenousOperation = Generalization(general=QuantityHomogenousOperation, specific=units_LengthDistinct)
gen_units_LengthSmaller_LengthOperation = Generalization(general=LengthOperation, specific=units_LengthSmaller)
gen_units_LengthSmaller_QuantityHomogenousOperation = Generalization(general=QuantityHomogenousOperation, specific=units_LengthSmaller)
gen_units_Yard_ImperialSystemUnit = Generalization(general=ImperialSystemUnit, specific=units_Yard)
gen_units_Yard_LengthUnit = Generalization(general=LengthUnit, specific=units_Yard)
gen_units_MetricSystemUnit_Unit = Generalization(general=Unit, specific=units_MetricSystemUnit)
gen_units_ImperialSystemUnit_Unit = Generalization(general=Unit, specific=units_ImperialSystemUnit)
gen_units_AngleUnit_Unit = Generalization(general=Unit, specific=units_AngleUnit)
gen_units_Radian_AngleUnit = Generalization(general=AngleUnit, specific=units_Radian)
gen_units_Degree_AngleUnit = Generalization(general=AngleUnit, specific=units_Degree)
gen_units_Turn_AngleUnit = Generalization(general=AngleUnit, specific=units_Turn)
gen_units_Gradian_AngleUnit = Generalization(general=AngleUnit, specific=units_Gradian)
gen_units_Length_Quantity = Generalization(general=Quantity, specific=units_Length)
gen_units_Angle_Quantity = Generalization(general=Quantity, specific=units_Angle)
gen_units_LengthOperation_QuantityOperation = Generalization(general=QuantityOperation, specific=units_LengthOperation)
gen_units_LengthAdd_LengthOperation = Generalization(general=LengthOperation, specific=units_LengthAdd)
gen_units_LengthAdd_QuantityHomogenousOperation = Generalization(general=QuantityHomogenousOperation, specific=units_LengthAdd)
gen_units_LengthGreater_LengthOperation = Generalization(general=LengthOperation, specific=units_LengthGreater)
gen_units_LengthGreater_QuantityHomogenousOperation = Generalization(general=QuantityHomogenousOperation, specific=units_LengthGreater)
gen_units_AngleOperation_QuantityOperation = Generalization(general=QuantityOperation, specific=units_AngleOperation)
gen_units_AngleAdd_AngleOperation = Generalization(general=AngleOperation, specific=units_AngleAdd)
gen_units_AngleAdd_QuantityHomogenousOperation = Generalization(general=QuantityHomogenousOperation, specific=units_AngleAdd)
gen_units_AngleSubtract_AngleOperation = Generalization(general=AngleOperation, specific=units_AngleSubtract)
gen_units_AngleSubtract_QuantityHomogenousOperation = Generalization(general=QuantityHomogenousOperation, specific=units_AngleSubtract)
gen_units_AngleScalarMultiply_AngleOperation = Generalization(general=AngleOperation, specific=units_AngleScalarMultiply)
gen_units_AngleScalarMultiply_QuantityScalarOperation = Generalization(general=QuantityScalarOperation, specific=units_AngleScalarMultiply)
gen_units_AngleScalarDivide_AngleOperation = Generalization(general=AngleOperation, specific=units_AngleScalarDivide)
gen_units_AngleScalarDivide_QuantityScalarOperation = Generalization(general=QuantityScalarOperation, specific=units_AngleScalarDivide)
gen_units_AngleEquals_AngleOperation = Generalization(general=AngleOperation, specific=units_AngleEquals)
gen_units_AngleEquals_QuantityHomogenousOperation = Generalization(general=QuantityHomogenousOperation, specific=units_AngleEquals)
gen_units_AngleDistinct_AngleOperation = Generalization(general=AngleOperation, specific=units_AngleDistinct)
gen_units_AngleDistinct_QuantityHomogenousOperation = Generalization(general=QuantityHomogenousOperation, specific=units_AngleDistinct)
gen_units_AngleSmaller_AngleOperation = Generalization(general=AngleOperation, specific=units_AngleSmaller)
gen_units_AngleSmaller_QuantityHomogenousOperation = Generalization(general=QuantityHomogenousOperation, specific=units_AngleSmaller)
gen_units_AngleGreater_AngleOperation = Generalization(general=AngleOperation, specific=units_AngleGreater)
gen_units_AngleGreater_QuantityHomogenousOperation = Generalization(general=QuantityHomogenousOperation, specific=units_AngleGreater)
gen_units_QuantityArithmeticOperation_QuantityOperation = Generalization(general=QuantityOperation, specific=units_QuantityArithmeticOperation)
gen_units_QuantityComparisonOperation_QuantityOperation = Generalization(general=QuantityOperation, specific=units_QuantityComparisonOperation)
gen_units_QuantityHomogenousOperation_QuantityOperation = Generalization(general=QuantityOperation, specific=units_QuantityHomogenousOperation)
gen_units_QuantityScalarOperation_QuantityOperation = Generalization(general=QuantityOperation, specific=units_QuantityScalarOperation)

# Domain Model
domain_model = DomainModel(
    name="units",
    types={units_Centimeter, MetricSystemUnit, LengthUnit, units_Millimeter, units_Meter, units_Foot, ImperialSystemUnit, units_Inch, units_Unit, units_LengthUnit, Unit, units_LengthSubtract, units_LengthScalarMultiply, QuantityScalarOperation, units_LengthScalarDivide, units_LengthEquals, units_LengthDistinct, units_LengthSmaller, units_Yard, units_MetricSystemUnit, units_ImperialSystemUnit, units_AngleUnit, units_Radian, AngleUnit, units_Degree, units_Turn, units_Gradian, units_Quantity, units_Length, Quantity, units_Angle, units_QuantityOperation, units_LengthOperation, QuantityOperation, units_LengthAdd, LengthOperation, QuantityHomogenousOperation, units_LengthGreater, units_AngleOperation, units_AngleAdd, AngleOperation, units_AngleSubtract, units_AngleScalarMultiply, units_AngleScalarDivide, units_AngleEquals, units_AngleDistinct, units_AngleSmaller, units_AngleGreater, units_QuantityArithmeticOperation, units_QuantityComparisonOperation, units_QuantityHomogenousOperation, units_QuantityScalarOperation},
    associations={unit0, lhs1, rhs3, lhs6},
    generalizations={gen_units_Centimeter_MetricSystemUnit, gen_units_Centimeter_LengthUnit, gen_units_Millimeter_MetricSystemUnit, gen_units_Millimeter_LengthUnit, gen_units_Meter_MetricSystemUnit, gen_units_Meter_LengthUnit, gen_units_Foot_ImperialSystemUnit, gen_units_Foot_LengthUnit, gen_units_Inch_ImperialSystemUnit, gen_units_Inch_LengthUnit, gen_units_LengthUnit_Unit, gen_units_LengthSubtract_LengthOperation, gen_units_LengthSubtract_QuantityHomogenousOperation, gen_units_LengthScalarMultiply_LengthOperation, gen_units_LengthScalarMultiply_QuantityScalarOperation, gen_units_LengthScalarDivide_LengthOperation, gen_units_LengthScalarDivide_QuantityScalarOperation, gen_units_LengthEquals_LengthOperation, gen_units_LengthEquals_QuantityHomogenousOperation, gen_units_LengthDistinct_LengthOperation, gen_units_LengthDistinct_QuantityHomogenousOperation, gen_units_LengthSmaller_LengthOperation, gen_units_LengthSmaller_QuantityHomogenousOperation, gen_units_Yard_ImperialSystemUnit, gen_units_Yard_LengthUnit, gen_units_MetricSystemUnit_Unit, gen_units_ImperialSystemUnit_Unit, gen_units_AngleUnit_Unit, gen_units_Radian_AngleUnit, gen_units_Degree_AngleUnit, gen_units_Turn_AngleUnit, gen_units_Gradian_AngleUnit, gen_units_Length_Quantity, gen_units_Angle_Quantity, gen_units_LengthOperation_QuantityOperation, gen_units_LengthAdd_LengthOperation, gen_units_LengthAdd_QuantityHomogenousOperation, gen_units_LengthGreater_LengthOperation, gen_units_LengthGreater_QuantityHomogenousOperation, gen_units_AngleOperation_QuantityOperation, gen_units_AngleAdd_AngleOperation, gen_units_AngleAdd_QuantityHomogenousOperation, gen_units_AngleSubtract_AngleOperation, gen_units_AngleSubtract_QuantityHomogenousOperation, gen_units_AngleScalarMultiply_AngleOperation, gen_units_AngleScalarMultiply_QuantityScalarOperation, gen_units_AngleScalarDivide_AngleOperation, gen_units_AngleScalarDivide_QuantityScalarOperation, gen_units_AngleEquals_AngleOperation, gen_units_AngleEquals_QuantityHomogenousOperation, gen_units_AngleDistinct_AngleOperation, gen_units_AngleDistinct_QuantityHomogenousOperation, gen_units_AngleSmaller_AngleOperation, gen_units_AngleSmaller_QuantityHomogenousOperation, gen_units_AngleGreater_AngleOperation, gen_units_AngleGreater_QuantityHomogenousOperation, gen_units_QuantityArithmeticOperation_QuantityOperation, gen_units_QuantityComparisonOperation_QuantityOperation, gen_units_QuantityHomogenousOperation_QuantityOperation, gen_units_QuantityScalarOperation_QuantityOperation},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)