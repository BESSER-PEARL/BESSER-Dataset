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
UnitNames: Enumeration = Enumeration(
    name="UnitNames",
    literals={
            EnumerationLiteral(name="UNITLESS"),
			EnumerationLiteral(name="BYTE"),
			EnumerationLiteral(name="SECOND"),
			EnumerationLiteral(name="METER")
    }
)

# Classes
units_UnitDivision = Class(name="units::UnitDivision")
units_UnitCarryingElement = Class(name="units::UnitCarryingElement", is_abstract=True)
units_Unit = Class(name="units::Unit", is_abstract=True)
units_BaseUnit = Class(name="units::BaseUnit")
Unit = Class(name="Unit")
units_UnitRepository = Class(name="units::UnitRepository")
units_UnitMultiplication = Class(name="units::UnitMultiplication")
units_UnitPower = Class(name="units::UnitPower")

# units_UnitDivision class attributes and methods

# units_UnitCarryingElement class attributes and methods

# units_Unit class attributes and methods

# units_BaseUnit class attributes and methods
units_BaseUnit_name: Property = Property(name="name", type=StringType)
units_BaseUnit.attributes={units_BaseUnit_name}

# Unit class attributes and methods

# units_UnitRepository class attributes and methods

# units_UnitMultiplication class attributes and methods

# units_UnitPower class attributes and methods
units_UnitPower_exponent: Property = Property(name="exponent", type=IntegerType)
units_UnitPower.attributes={units_UnitPower_exponent}

# Relationships
dividend6: BinaryAssociation = BinaryAssociation(
    name="dividend6",
    ends={
        Property(name="units_Unit7", type=units_UnitDivision, multiplicity=Multiplicity(1, 1)),
        Property(name="units_UnitDivision", type=units_Unit, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
divisor8: BinaryAssociation = BinaryAssociation(
    name="divisor8",
    ends={
        Property(name="units_Unit10", type=units_UnitDivision, multiplicity=Multiplicity(1, 1)),
        Property(name="units_UnitDivision9", type=units_Unit, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
unit0: BinaryAssociation = BinaryAssociation(
    name="unit0",
    ends={
        Property(name="units_Unit", type=units_UnitCarryingElement, multiplicity=Multiplicity(1, 1)),
        Property(name="units_UnitCarryingElement", type=units_Unit, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
units1: BinaryAssociation = BinaryAssociation(
    name="units1",
    ends={
        Property(name="units_BaseUnit", type=units_UnitRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="units_UnitRepository", type=units_BaseUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
units2: BinaryAssociation = BinaryAssociation(
    name="units2",
    ends={
        Property(name="units_Unit3", type=units_UnitMultiplication, multiplicity=Multiplicity(1, 1)),
        Property(name="units_UnitMultiplication", type=units_Unit, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
unit4: BinaryAssociation = BinaryAssociation(
    name="unit4",
    ends={
        Property(name="units_Unit5", type=units_UnitPower, multiplicity=Multiplicity(1, 1)),
        Property(name="units_UnitPower", type=units_Unit, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_units_UnitDivision_Unit = Generalization(general=Unit, specific=units_UnitDivision)
gen_units_BaseUnit_Unit = Generalization(general=Unit, specific=units_BaseUnit)
gen_units_UnitMultiplication_Unit = Generalization(general=Unit, specific=units_UnitMultiplication)
gen_units_UnitPower_Unit = Generalization(general=Unit, specific=units_UnitPower)

# Domain Model
domain_model = DomainModel(
    name="units",
    types={units_UnitDivision, units_UnitCarryingElement, units_Unit, units_BaseUnit, Unit, units_UnitRepository, units_UnitMultiplication, units_UnitPower, UnitNames},
    associations={dividend6, divisor8, unit0, units1, units2, unit4},
    generalizations={gen_units_UnitDivision_Unit, gen_units_BaseUnit_Unit, gen_units_UnitMultiplication_Unit, gen_units_UnitPower_Unit},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)