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
units_pc_av_UnitRepository = Class(name="units::pc::av::UnitRepository")
units_pc_av_UnitMultiplication = Class(name="units::pc::av::UnitMultiplication")
Unit = Class(name="Unit")
units_pc_av_UnitPower = Class(name="units::pc::av::UnitPower")
units_pc_av_UnitLiteral = Class(name="units::pc::av::UnitLiteral")
units_pc_av_Pointcut = Class(name="units::pc::av::Pointcut")
units_pc_av_EObject = Class(name="units::pc::av::EObject")
units_pc_av_UnitCarryingElement = Class(name="units::pc::av::UnitCarryingElement")
units_pc_av_Unit = Class(name="units::pc::av::Unit")
units_pc_av_BaseUnit = Class(name="units::pc::av::BaseUnit")
units_pc_av_Advice = Class(name="units::pc::av::Advice")
units_pc_av_GlobalScope = Class(name="units::pc::av::GlobalScope")
units_pc_av_PerJoinPointScope = Class(name="units::pc::av::PerJoinPointScope")

# units_pc_av_UnitRepository class attributes and methods

# units_pc_av_UnitMultiplication class attributes and methods

# Unit class attributes and methods

# units_pc_av_UnitPower class attributes and methods
units_pc_av_UnitPower_exponent: Property = Property(name="exponent", type=IntegerType)
units_pc_av_UnitPower.attributes={units_pc_av_UnitPower_exponent}

# units_pc_av_UnitLiteral class attributes and methods

# units_pc_av_Pointcut class attributes and methods

# units_pc_av_EObject class attributes and methods

# units_pc_av_UnitCarryingElement class attributes and methods
units_pc_av_UnitCarryingElement_unitSpecification: Property = Property(name="unitSpecification", type=StringType)
units_pc_av_UnitCarryingElement.attributes={units_pc_av_UnitCarryingElement_unitSpecification}

# units_pc_av_Unit class attributes and methods

# units_pc_av_BaseUnit class attributes and methods
units_pc_av_BaseUnit_name: Property = Property(name="name", type=StringType)
units_pc_av_BaseUnit.attributes={units_pc_av_BaseUnit_name}

# units_pc_av_Advice class attributes and methods

# units_pc_av_GlobalScope class attributes and methods

# units_pc_av_PerJoinPointScope class attributes and methods

# Relationships
units1: BinaryAssociation = BinaryAssociation(
    name="units1",
    ends={
        Property(name="units_pc_av_BaseUnit", type=units_pc_av_UnitRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="units_pc_av_UnitRepository", type=units_pc_av_BaseUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
units2: BinaryAssociation = BinaryAssociation(
    name="units2",
    ends={
        Property(name="units_pc_av_Unit3", type=units_pc_av_UnitMultiplication, multiplicity=Multiplicity(1, 1)),
        Property(name="units_pc_av_UnitMultiplication", type=units_pc_av_Unit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
unit4: BinaryAssociation = BinaryAssociation(
    name="unit4",
    ends={
        Property(name="units_pc_av_Unit5", type=units_pc_av_UnitPower, multiplicity=Multiplicity(1, 1)),
        Property(name="units_pc_av_UnitPower", type=units_pc_av_Unit, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
baseUnit6: BinaryAssociation = BinaryAssociation(
    name="baseUnit6",
    ends={
        Property(name="units_pc_av_BaseUnit7", type=units_pc_av_UnitLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="units_pc_av_UnitLiteral", type=units_pc_av_BaseUnit, multiplicity=Multiplicity(0, 1))
    }
)
unit0: BinaryAssociation = BinaryAssociation(
    name="unit0",
    ends={
        Property(name="units_pc_av_Unit", type=units_pc_av_UnitCarryingElement, multiplicity=Multiplicity(1, 1)),
        Property(name="units_pc_av_UnitCarryingElement", type=units_pc_av_Unit, multiplicity=Multiplicity(0, 1))
    }
)
children8: BinaryAssociation = BinaryAssociation(
    name="children8",
    ends={
        Property(name="units_pc_av_EObject", type=units_pc_av_Pointcut, multiplicity=Multiplicity(1, 1)),
        Property(name="units_pc_av_Pointcut", type=units_pc_av_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
children9: BinaryAssociation = BinaryAssociation(
    name="children9",
    ends={
        Property(name="units_pc_av_EObject10", type=units_pc_av_Advice, multiplicity=Multiplicity(1, 1)),
        Property(name="units_pc_av_Advice", type=units_pc_av_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
scopedObject11: BinaryAssociation = BinaryAssociation(
    name="scopedObject11",
    ends={
        Property(name="units_pc_av_EObject12", type=units_pc_av_GlobalScope, multiplicity=Multiplicity(1, 1)),
        Property(name="units_pc_av_GlobalScope", type=units_pc_av_EObject, multiplicity=Multiplicity(1, 1))
    }
)
scopedObject13: BinaryAssociation = BinaryAssociation(
    name="scopedObject13",
    ends={
        Property(name="units_pc_av_EObject14", type=units_pc_av_PerJoinPointScope, multiplicity=Multiplicity(1, 1)),
        Property(name="units_pc_av_PerJoinPointScope", type=units_pc_av_EObject, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_units_pc_av_UnitMultiplication_Unit = Generalization(general=Unit, specific=units_pc_av_UnitMultiplication)
gen_units_pc_av_UnitPower_Unit = Generalization(general=Unit, specific=units_pc_av_UnitPower)
gen_units_pc_av_UnitLiteral_Unit = Generalization(general=Unit, specific=units_pc_av_UnitLiteral)

# Domain Model
domain_model = DomainModel(
    name="units_pc_av",
    types={units_pc_av_UnitRepository, units_pc_av_UnitMultiplication, Unit, units_pc_av_UnitPower, units_pc_av_UnitLiteral, units_pc_av_Pointcut, units_pc_av_EObject, units_pc_av_UnitCarryingElement, units_pc_av_Unit, units_pc_av_BaseUnit, units_pc_av_Advice, units_pc_av_GlobalScope, units_pc_av_PerJoinPointScope},
    associations={units1, units2, unit4, baseUnit6, unit0, children8, children9, scopedObject11, scopedObject13},
    generalizations={gen_units_pc_av_UnitMultiplication_Unit, gen_units_pc_av_UnitPower_Unit, gen_units_pc_av_UnitLiteral_Unit},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)