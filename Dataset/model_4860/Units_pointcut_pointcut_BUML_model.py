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
units_pc_pc_BaseUnit = Class(name="units::pc::pc::BaseUnit")
units_pc_pc_UnitRepository = Class(name="units::pc::pc::UnitRepository")
units_pc_pc_UnitMultiplication = Class(name="units::pc::pc::UnitMultiplication")
Unit = Class(name="Unit")
units_pc_pc_UnitCarryingElement = Class(name="units::pc::pc::UnitCarryingElement")
units_pc_pc_Unit = Class(name="units::pc::pc::Unit")
units_pc_pc_UnitPower = Class(name="units::pc::pc::UnitPower")
units_pc_pc_UnitLiteral = Class(name="units::pc::pc::UnitLiteral")
units_pc_pc_PointcutPointcut = Class(name="units::pc::pc::PointcutPointcut")
units_pc_pc_EObject = Class(name="units::pc::pc::EObject")
units_pc_pc_Pointcut = Class(name="units::pc::pc::Pointcut")

# units_pc_pc_BaseUnit class attributes and methods
units_pc_pc_BaseUnit_name: Property = Property(name="name", type=StringType)
units_pc_pc_BaseUnit.attributes={units_pc_pc_BaseUnit_name}

# units_pc_pc_UnitRepository class attributes and methods

# units_pc_pc_UnitMultiplication class attributes and methods

# Unit class attributes and methods

# units_pc_pc_UnitCarryingElement class attributes and methods
units_pc_pc_UnitCarryingElement_unitSpecification: Property = Property(name="unitSpecification", type=StringType)
units_pc_pc_UnitCarryingElement.attributes={units_pc_pc_UnitCarryingElement_unitSpecification}

# units_pc_pc_Unit class attributes and methods

# units_pc_pc_UnitPower class attributes and methods
units_pc_pc_UnitPower_exponent: Property = Property(name="exponent", type=IntegerType)
units_pc_pc_UnitPower.attributes={units_pc_pc_UnitPower_exponent}

# units_pc_pc_UnitLiteral class attributes and methods

# units_pc_pc_PointcutPointcut class attributes and methods

# units_pc_pc_EObject class attributes and methods

# units_pc_pc_Pointcut class attributes and methods

# Relationships
unit0: BinaryAssociation = BinaryAssociation(
    name="unit0",
    ends={
        Property(name="units_pc_pc_UnitCarryingElement", type=units_pc_pc_Unit, multiplicity=Multiplicity(0, 1)),
        Property(name="units_pc_pc_Unit", type=units_pc_pc_UnitCarryingElement, multiplicity=Multiplicity(1, 1))
    }
)
units1: BinaryAssociation = BinaryAssociation(
    name="units1",
    ends={
        Property(name="units_pc_pc_BaseUnit", type=units_pc_pc_UnitRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="units_pc_pc_UnitRepository", type=units_pc_pc_BaseUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
units2: BinaryAssociation = BinaryAssociation(
    name="units2",
    ends={
        Property(name="units_pc_pc_Unit3", type=units_pc_pc_UnitMultiplication, multiplicity=Multiplicity(1, 1)),
        Property(name="units_pc_pc_UnitMultiplication", type=units_pc_pc_Unit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
unit4: BinaryAssociation = BinaryAssociation(
    name="unit4",
    ends={
        Property(name="units_pc_pc_Unit5", type=units_pc_pc_UnitPower, multiplicity=Multiplicity(1, 1)),
        Property(name="units_pc_pc_UnitPower", type=units_pc_pc_Unit, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
baseUnit6: BinaryAssociation = BinaryAssociation(
    name="baseUnit6",
    ends={
        Property(name="units_pc_pc_BaseUnit7", type=units_pc_pc_UnitLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="units_pc_pc_UnitLiteral", type=units_pc_pc_BaseUnit, multiplicity=Multiplicity(0, 1))
    }
)
children8: BinaryAssociation = BinaryAssociation(
    name="children8",
    ends={
        Property(name="units_pc_pc_EObject", type=units_pc_pc_PointcutPointcut, multiplicity=Multiplicity(1, 1)),
        Property(name="units_pc_pc_PointcutPointcut", type=units_pc_pc_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
children9: BinaryAssociation = BinaryAssociation(
    name="children9",
    ends={
        Property(name="units_pc_pc_EObject10", type=units_pc_pc_Pointcut, multiplicity=Multiplicity(1, 1)),
        Property(name="units_pc_pc_Pointcut", type=units_pc_pc_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_units_pc_pc_UnitMultiplication_Unit = Generalization(general=Unit, specific=units_pc_pc_UnitMultiplication)
gen_units_pc_pc_UnitPower_Unit = Generalization(general=Unit, specific=units_pc_pc_UnitPower)
gen_units_pc_pc_UnitLiteral_Unit = Generalization(general=Unit, specific=units_pc_pc_UnitLiteral)

# Domain Model
domain_model = DomainModel(
    name="units_pc_pc",
    types={units_pc_pc_BaseUnit, units_pc_pc_UnitRepository, units_pc_pc_UnitMultiplication, Unit, units_pc_pc_UnitCarryingElement, units_pc_pc_Unit, units_pc_pc_UnitPower, units_pc_pc_UnitLiteral, units_pc_pc_PointcutPointcut, units_pc_pc_EObject, units_pc_pc_Pointcut},
    associations={unit0, units1, units2, unit4, baseUnit6, children8, children9},
    generalizations={gen_units_pc_pc_UnitMultiplication_Unit, gen_units_pc_pc_UnitPower_Unit, gen_units_pc_pc_UnitLiteral_Unit},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)