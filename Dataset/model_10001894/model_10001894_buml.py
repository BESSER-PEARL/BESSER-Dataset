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
WeaponAttack = Class(name="WeaponAttack")
CastSpell = Class(name="CastSpell")
Action = Class(name="Action")
Weapon = Class(name="Weapon")
Spell = Class(name="Spell")
Dash = Class(name="Dash")
Dash2 = Class(name="Dash2")

# WeaponAttack class attributes and methods
WeaponAttack_execute__: Property = Property(name="execute__", type=StringType)
WeaponAttack_weapon: Property = Property(name="weapon", type=Weapon)
WeaponAttack.attributes={WeaponAttack_execute__, WeaponAttack_weapon}

# CastSpell class attributes and methods
CastSpell_execute__: Property = Property(name="execute__", type=StringType)
CastSpell_spell: Property = Property(name="spell", type=Spell)
CastSpell.attributes={CastSpell_execute__, CastSpell_spell}

# Action class attributes and methods
Action_execute__: Property = Property(name="execute__", type=StringType)
Action.attributes={Action_execute__}

# Weapon class attributes and methods

# Spell class attributes and methods

# Dash class attributes and methods
Dash_execute__: Property = Property(name="execute__", type=StringType)
Dash.attributes={Dash_execute__}

# Dash2 class attributes and methods
Dash2_execute__: Property = Property(name="execute__", type=StringType)
Dash2.attributes={Dash2_execute__}

# Domain Model
domain_model = DomainModel(
    name="_bybUkBneEeig8qiayYYCew",
    types={WeaponAttack, CastSpell, Action, Weapon, Spell, Dash, Dash2},
    associations={},
    generalizations={},
    metadata=None
)

###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)