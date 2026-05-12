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
Color: Enumeration = Enumeration(
    name="Color",
    literals={
            EnumerationLiteral(name="black"),
			EnumerationLiteral(name="red"),
			EnumerationLiteral(name="green"),
			EnumerationLiteral(name="yellow"),
			EnumerationLiteral(name="orange"),
			EnumerationLiteral(name="brown"),
			EnumerationLiteral(name="pink")
    }
)

# Classes
fruit_Apple = Class(name="fruit_Apple")
Fruit = Class(name="Fruit")
fruit_Fruit = Class(name="fruit_Fruit", is_abstract=True)
fruit_FruitUtil = Class(name="fruit_FruitUtil")
fruit_Stem = Class(name="fruit_Stem")
fruit_Tree = Class(name="fruit_Tree")
fruit_apple_EatingApple = Class(name="fruit_apple_EatingApple")
Apple = Class(name="Apple")
fruit_apple_CookingApple = Class(name="fruit_apple_CookingApple")

# fruit_Apple class attributes and methods
fruit_Apple_label: Property = Property(name="label", type=StringType)
fruit_Apple_m_label: Method = Method(name="label", parameters={Parameter(name='fruit_text', type=StringType)})
fruit_Apple_m_newApple: Method = Method(name="newApple", parameters={}, type=StringType)
fruit_Apple_m_preferredLabel: Method = Method(name="preferredLabel", parameters={Parameter(name='fruit_text', type=StringType)}, type=StringType)
fruit_Apple.attributes={fruit_Apple_label}
fruit_Apple.methods={fruit_Apple_m_label, fruit_Apple_m_newApple, fruit_Apple_m_preferredLabel}

# Fruit class attributes and methods

# fruit_Fruit class attributes and methods
fruit_Fruit_color: Property = Property(name="color", type=StringType)
fruit_Fruit_name: Property = Property(name="name", type=StringType)
fruit_Fruit_m_preferredColor: Method = Method(name="preferredColor", parameters={}, type=StringType)
fruit_Fruit_m_newFruit: Method = Method(name="newFruit", parameters={}, type=StringType)
fruit_Fruit_m_setColor: Method = Method(name="setColor", parameters={Parameter(name='fruit_newColor', type=StringType), Parameter(name='fruit_fruit', type=StringType)})
fruit_Fruit_m_ripen: Method = Method(name="ripen", parameters={Parameter(name='fruit_color', type=StringType)}, type=BooleanType)
fruit_Fruit.attributes={fruit_Fruit_color, fruit_Fruit_name}
fruit_Fruit.methods={fruit_Fruit_m_newFruit, fruit_Fruit_m_setColor, fruit_Fruit_m_ripen, fruit_Fruit_m_preferredColor}

# fruit_FruitUtil class attributes and methods
fruit_FruitUtil_m_processOrderedSet: Method = Method(name="processOrderedSet", parameters={Parameter(name='fruit_fruits', type=StringType)}, type=Fruit)
fruit_FruitUtil_m_processSet: Method = Method(name="processSet", parameters={Parameter(name='fruit_fruits', type=StringType)}, type=Fruit)
fruit_FruitUtil_m_processBag: Method = Method(name="processBag", parameters={Parameter(name='fruit_fruits', type=StringType)}, type=Fruit)
fruit_FruitUtil_m_processSequence: Method = Method(name="processSequence", parameters={Parameter(name='fruit_fruits', type=StringType)}, type=Fruit)
fruit_FruitUtil.methods={fruit_FruitUtil_m_processBag, fruit_FruitUtil_m_processSet, fruit_FruitUtil_m_processSequence, fruit_FruitUtil_m_processOrderedSet}

# fruit_Stem class attributes and methods

# fruit_Tree class attributes and methods
fruit_Tree_name: Property = Property(name="name", type=StringType)
fruit_Tree.attributes={fruit_Tree_name}

# fruit_apple_EatingApple class attributes and methods

# Apple class attributes and methods

# fruit_apple_CookingApple class attributes and methods

# Relationships
relatedFruits1: BinaryAssociation = BinaryAssociation(
    name="relatedFruits1",
    ends={
        Property(name="fruit_Fruit", type=fruit_Fruit, multiplicity=Multiplicity(1, 1)),
        Property(name="fruit_Fruit0", type=fruit_Fruit, multiplicity=Multiplicity(0, 9999))
    }
)
stem2: BinaryAssociation = BinaryAssociation(
    name="stem2",
    ends={
        Property(name="fruit_Stem", type=fruit_Apple, multiplicity=Multiplicity(1, 1)),
        Property(name="fruit_Apple", type=fruit_Stem, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sequence11: BinaryAssociation = BinaryAssociation(
    name="sequence11",
    ends={
        Property(name="fruit_Fruit13", type=fruit_FruitUtil, multiplicity=Multiplicity(1, 1)),
        Property(name="fruit_FruitUtil12", type=fruit_Fruit, multiplicity=Multiplicity(0, 9999))
    }
)
fruits14: BinaryAssociation = BinaryAssociation(
    name="fruits14",
    ends={
        Property(name="fruit_Fruit15", type=fruit_Tree, multiplicity=Multiplicity(1, 1)),
        Property(name="fruit_Tree", type=fruit_Fruit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
orderedSet3: BinaryAssociation = BinaryAssociation(
    name="orderedSet3",
    ends={
        Property(name="fruit_Fruit4", type=fruit_FruitUtil, multiplicity=Multiplicity(1, 1)),
        Property(name="fruit_FruitUtil", type=fruit_Fruit, multiplicity=Multiplicity(0, 9999))
    }
)
set5: BinaryAssociation = BinaryAssociation(
    name="set5",
    ends={
        Property(name="fruit_Fruit7", type=fruit_FruitUtil, multiplicity=Multiplicity(1, 1)),
        Property(name="fruit_FruitUtil6", type=fruit_Fruit, multiplicity=Multiplicity(0, 9999))
    }
)
bag8: BinaryAssociation = BinaryAssociation(
    name="bag8",
    ends={
        Property(name="fruit_Fruit10", type=fruit_FruitUtil, multiplicity=Multiplicity(1, 1)),
        Property(name="fruit_FruitUtil9", type=fruit_Fruit, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_fruit_Apple_Fruit = Generalization(general=Fruit, specific=fruit_Apple)
gen_fruit_apple_EatingApple_Apple = Generalization(general=Apple, specific=fruit_apple_EatingApple)
gen_fruit_apple_CookingApple_Apple = Generalization(general=Apple, specific=fruit_apple_CookingApple)

# Domain Model
domain_model = DomainModel(
    name="fruit",
    types={fruit_Apple, Fruit, fruit_Fruit, fruit_FruitUtil, fruit_Stem, fruit_Tree, fruit_apple_EatingApple, Apple, fruit_apple_CookingApple, Color},
    associations={relatedFruits1, stem2, sequence11, fruits14, orderedSet3, set5, bag8},
    generalizations={gen_fruit_Apple_Fruit, gen_fruit_apple_EatingApple_Apple, gen_fruit_apple_CookingApple_Apple},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)