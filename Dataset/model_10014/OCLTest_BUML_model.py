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
OclTest_FruitUtil = Class(name="OclTest_FruitUtil")
OclTest_Fruit = Class(name="OclTest_Fruit", is_abstract=True)
OclTest_Apple = Class(name="OclTest_Apple")
Fruit = Class(name="Fruit")
OclTest_Stem = Class(name="OclTest_Stem")
OclTest_Tree = Class(name="OclTest_Tree")

# OclTest_FruitUtil class attributes and methods
OclTest_FruitUtil_m_processOrderedSet: Method = Method(name="processOrderedSet", parameters={Parameter(name='OclTest_fruits', type=StringType)}, type=Fruit)
OclTest_FruitUtil_m_processSet: Method = Method(name="processSet", parameters={Parameter(name='OclTest_fruits', type=StringType)}, type=Fruit)
OclTest_FruitUtil_m_processBag: Method = Method(name="processBag", parameters={Parameter(name='OclTest_fruits', type=StringType)}, type=Fruit)
OclTest_FruitUtil_m_processSequence: Method = Method(name="processSequence", parameters={Parameter(name='OclTest_fruits', type=StringType)}, type=Fruit)
OclTest_FruitUtil.methods={OclTest_FruitUtil_m_processSequence, OclTest_FruitUtil_m_processSet, OclTest_FruitUtil_m_processOrderedSet, OclTest_FruitUtil_m_processBag}

# OclTest_Fruit class attributes and methods
OclTest_Fruit_color: Property = Property(name="color", type=StringType)
OclTest_Fruit_name: Property = Property(name="name", type=StringType)
OclTest_Fruit_m_ripen: Method = Method(name="ripen", parameters={Parameter(name='OclTest_color', type=StringType)}, type=BooleanType)
OclTest_Fruit_m_preferredColor: Method = Method(name="preferredColor", parameters={}, type=StringType)
OclTest_Fruit_m_newFruit: Method = Method(name="newFruit", parameters={}, type=StringType)
OclTest_Fruit_m_setColor: Method = Method(name="setColor", parameters={Parameter(name='OclTest_fruit', type=StringType), Parameter(name='OclTest_newColor', type=StringType)})
OclTest_Fruit.attributes={OclTest_Fruit_color, OclTest_Fruit_name}
OclTest_Fruit.methods={OclTest_Fruit_m_newFruit, OclTest_Fruit_m_preferredColor, OclTest_Fruit_m_setColor, OclTest_Fruit_m_ripen}

# OclTest_Apple class attributes and methods
OclTest_Apple_label: Property = Property(name="label", type=StringType)
OclTest_Apple_m_label: Method = Method(name="label", parameters={Parameter(name='OclTest_text', type=StringType)})
OclTest_Apple_m_newApple: Method = Method(name="newApple", parameters={}, type=StringType)
OclTest_Apple_m_preferredLabel: Method = Method(name="preferredLabel", parameters={Parameter(name='OclTest_text', type=StringType)}, type=StringType)
OclTest_Apple.attributes={OclTest_Apple_label}
OclTest_Apple.methods={OclTest_Apple_m_label, OclTest_Apple_m_preferredLabel, OclTest_Apple_m_newApple}

# Fruit class attributes and methods

# OclTest_Stem class attributes and methods

# OclTest_Tree class attributes and methods
OclTest_Tree_name: Property = Property(name="name", type=StringType)
OclTest_Tree.attributes={OclTest_Tree_name}

# Relationships
relatedFruits1: BinaryAssociation = BinaryAssociation(
    name="relatedFruits1",
    ends={
        Property(name="OclTest_Fruit", type=OclTest_Fruit, multiplicity=Multiplicity(1, 1)),
        Property(name="OclTest_Fruit0", type=OclTest_Fruit, multiplicity=Multiplicity(0, 9999))
    }
)
stem2: BinaryAssociation = BinaryAssociation(
    name="stem2",
    ends={
        Property(name="OclTest_Stem", type=OclTest_Apple, multiplicity=Multiplicity(1, 1)),
        Property(name="OclTest_Apple", type=OclTest_Stem, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
orderedSet3: BinaryAssociation = BinaryAssociation(
    name="orderedSet3",
    ends={
        Property(name="OclTest_Fruit4", type=OclTest_FruitUtil, multiplicity=Multiplicity(1, 1)),
        Property(name="OclTest_FruitUtil", type=OclTest_Fruit, multiplicity=Multiplicity(0, 9999))
    }
)
set5: BinaryAssociation = BinaryAssociation(
    name="set5",
    ends={
        Property(name="OclTest_Fruit7", type=OclTest_FruitUtil, multiplicity=Multiplicity(1, 1)),
        Property(name="OclTest_FruitUtil6", type=OclTest_Fruit, multiplicity=Multiplicity(0, 9999))
    }
)
bag8: BinaryAssociation = BinaryAssociation(
    name="bag8",
    ends={
        Property(name="OclTest_Fruit10", type=OclTest_FruitUtil, multiplicity=Multiplicity(1, 1)),
        Property(name="OclTest_FruitUtil9", type=OclTest_Fruit, multiplicity=Multiplicity(0, 9999))
    }
)
sequence11: BinaryAssociation = BinaryAssociation(
    name="sequence11",
    ends={
        Property(name="OclTest_Fruit13", type=OclTest_FruitUtil, multiplicity=Multiplicity(1, 1)),
        Property(name="OclTest_FruitUtil12", type=OclTest_Fruit, multiplicity=Multiplicity(0, 9999))
    }
)
fruits14: BinaryAssociation = BinaryAssociation(
    name="fruits14",
    ends={
        Property(name="OclTest_Fruit15", type=OclTest_Tree, multiplicity=Multiplicity(1, 1)),
        Property(name="OclTest_Tree", type=OclTest_Fruit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fruitsDroppedUnder16: BinaryAssociation = BinaryAssociation(
    name="fruitsDroppedUnder16",
    ends={
        Property(name="OclTest_Fruit18", type=OclTest_Tree, multiplicity=Multiplicity(1, 1)),
        Property(name="OclTest_Tree17", type=OclTest_Fruit, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_OclTest_Apple_Fruit = Generalization(general=Fruit, specific=OclTest_Apple)


# OCL Constraints
not_black: Constraint = Constraint(
    name="not_black",
    context=OclTest_Fruit,
    expression="context Fruit inv: self.color <> Color_black",
    language="OCL"
)
not_foo: Constraint = Constraint(
    name="not_foo",
    context=OclTest_Fruit,
    expression="context Fruit inv: self.name <> 'Foo'",
    language="OCL"
)
not_pink: Constraint = Constraint(
    name="not_pink",
    context=OclTest_Fruit,
    expression="context Fruit inv: color <> Color_pink",
    language="OCL"
)
second_classifier_context: Constraint = Constraint(
    name="second_classifier_context",
    context=OclTest_Apple,
    expression="context Apple inv: label.oclIsUndefined() implies true",
    language="OCL"
)
not_black1: Constraint = Constraint(
    name="not_black1",
    context=OclTest_Fruit,
    expression="context Fruit inv: self.color <> Color_black",
    language="OCL"
)
not_foo1: Constraint = Constraint(
    name="not_foo1",
    context=OclTest_Fruit,
    expression="context Fruit inv: self.name <> 'Foo'",
    language="OCL"
)
not_pink1: Constraint = Constraint(
    name="not_pink1",
    context=OclTest_Fruit,
    expression="context Fruit inv: color <> Color_pink",
    language="OCL"
)

# Domain Model
domain_model = DomainModel(
    name="OclTest",
    types={OclTest_FruitUtil, OclTest_Fruit, OclTest_Apple, Fruit, OclTest_Stem, OclTest_Tree, Color},
    associations={relatedFruits1, stem2, orderedSet3, set5, bag8, sequence11, fruits14, fruitsDroppedUnder16},
    constraints={not_black, not_foo, not_pink, second_classifier_context, not_black1, not_foo1, not_pink1},
    generalizations={gen_OclTest_Apple_Fruit},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)