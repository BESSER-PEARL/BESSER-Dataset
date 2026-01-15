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
units_UnitCarryingElement = Class(name="units::UnitCarryingElement", is_abstract=True)
units_Unit = Class(name="units::Unit", is_abstract=True)
units_UnitLiteral = Class(name="units::UnitLiteral")
units_BaseUnit = Class(name="units::BaseUnit")
units_UnitRepository = Class(name="units::UnitRepository")
units_UnitMultiplication = Class(name="units::UnitMultiplication")
Unit = Class(name="Unit")
units_UnitPower = Class(name="units::UnitPower")

# units_UnitCarryingElement class attributes and methods
units_UnitCarryingElement_unitSpecification: Property = Property(name="unitSpecification", type=StringType)
units_UnitCarryingElement.attributes={units_UnitCarryingElement_unitSpecification}

# units_Unit class attributes and methods

# units_UnitLiteral class attributes and methods

# units_BaseUnit class attributes and methods
units_BaseUnit_name: Property = Property(name="name", type=StringType)
units_BaseUnit.attributes={units_BaseUnit_name}

# units_UnitRepository class attributes and methods

# units_UnitMultiplication class attributes and methods

# Unit class attributes and methods

# units_UnitPower class attributes and methods
units_UnitPower_exponent: Property = Property(name="exponent", type=IntegerType)
units_UnitPower.attributes={units_UnitPower_exponent}

# Relationships
unit0: BinaryAssociation = BinaryAssociation(
    name="unit0",
    ends={
        Property(name="units_Unit", type=units_UnitCarryingElement, multiplicity=Multiplicity(1, 1)),
        Property(name="units_UnitCarryingElement", type=units_Unit, multiplicity=Multiplicity(0, 1))
    }
)
baseUnit6: BinaryAssociation = BinaryAssociation(
    name="baseUnit6",
    ends={
        Property(name="units_BaseUnit7", type=units_UnitLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="units_UnitLiteral", type=units_BaseUnit, multiplicity=Multiplicity(1, 1))
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
gen_units_UnitLiteral_Unit = Generalization(general=Unit, specific=units_UnitLiteral)
gen_units_UnitMultiplication_Unit = Generalization(general=Unit, specific=units_UnitMultiplication)
gen_units_UnitPower_Unit = Generalization(general=Unit, specific=units_UnitPower)

# Domain Model
domain_model = DomainModel(
    name="units",
    types={units_UnitCarryingElement, units_Unit, units_UnitLiteral, units_BaseUnit, units_UnitRepository, units_UnitMultiplication, Unit, units_UnitPower},
    associations={unit0, baseUnit6, units1, units2, unit4},
    generalizations={gen_units_UnitLiteral_Unit, gen_units_UnitMultiplication_Unit, gen_units_UnitPower_Unit},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)