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
int = Class(name="int")
classes_Card = Class(name="classes_Card")
combinations_Combination = Class(name="combinations_Combination", is_abstract=True)
combinations_PlusHauteCarte = Class(name="combinations_PlusHauteCarte")
combinations_Paire = Class(name="combinations_Paire")
combinations_DoublePaire = Class(name="combinations_DoublePaire")
combinations_Brelan = Class(name="combinations_Brelan")
combinations_Suite = Class(name="combinations_Suite")
combinations_Couleur = Class(name="combinations_Couleur")
combinations_Full = Class(name="combinations_Full")
combinations_Carre = Class(name="combinations_Carre")
combinations_QuinteFlush = Class(name="combinations_QuinteFlush")
classes_Hand = Class(name="classes_Hand")
utils_Parser = Class(name="utils_Parser")

# int class attributes and methods

# classes_Card class attributes and methods
classes_Card_name: Property = Property(name="name", type=StringType)
classes_Card_value: Property = Property(name="value", type=IntegerType)
classes_Card.attributes={classes_Card_value, classes_Card_name}

# combinations_Combination class attributes and methods
combinations_Combination_name: Property = Property(name="name", type=StringType)
combinations_Combination_value: Property = Property(name="value", type=IntegerType)
combinations_Combination.attributes={combinations_Combination_name, combinations_Combination_value}

# combinations_PlusHauteCarte class attributes and methods

# combinations_Paire class attributes and methods
combinations_Paire_paire: Property = Property(name="paire", type=classes_Card)
combinations_Paire.attributes={combinations_Paire_paire}

# combinations_DoublePaire class attributes and methods
combinations_DoublePaire_strongPaire: Property = Property(name="strongPaire", type=classes_Card)
combinations_DoublePaire_weakPaire: Property = Property(name="weakPaire", type=classes_Card)
combinations_DoublePaire.attributes={combinations_DoublePaire_strongPaire, combinations_DoublePaire_weakPaire}

# combinations_Brelan class attributes and methods
combinations_Brelan_triplet: Property = Property(name="triplet", type=classes_Card)
combinations_Brelan.attributes={combinations_Brelan_triplet}

# combinations_Suite class attributes and methods
combinations_Suite_start: Property = Property(name="start", type=classes_Card)
combinations_Suite.attributes={combinations_Suite_start}

# combinations_Couleur class attributes and methods

# combinations_Full class attributes and methods
combinations_Full_paire: Property = Property(name="paire", type=classes_Card)
combinations_Full_triplet: Property = Property(name="triplet", type=classes_Card)
combinations_Full.attributes={combinations_Full_paire, combinations_Full_triplet}

# combinations_Carre class attributes and methods
combinations_Carre_quartet: Property = Property(name="quartet", type=classes_Card)
combinations_Carre.attributes={combinations_Carre_quartet}

# combinations_QuinteFlush class attributes and methods
combinations_QuinteFlush_start: Property = Property(name="start", type=classes_Card)
combinations_QuinteFlush.attributes={combinations_QuinteFlush_start}

# classes_Hand class attributes and methods

# utils_Parser class attributes and methods

# Relationships
Hand_Card: BinaryAssociation = BinaryAssociation(
    name="Hand_Card",
    ends={
        Property(name="cards0", type=classes_Card, multiplicity=Multiplicity(0, 9999)),
        Property(name="hand1", type=combinations_Combination, multiplicity=Multiplicity(0, 1))
    }
)
Hand_Card2: BinaryAssociation = BinaryAssociation(
    name="Hand_Card2",
    ends={
        Property(name="hand2", type=classes_Card, multiplicity=Multiplicity(1, 9999)),
        Property(name="hand3", type=classes_Hand, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_164781c0_1d74_4156_96cc_fd9c6c41e483",
    types={int, classes_Card, combinations_Combination, combinations_PlusHauteCarte, combinations_Paire, combinations_DoublePaire, combinations_Brelan, combinations_Suite, combinations_Couleur, combinations_Full, combinations_Carre, combinations_QuinteFlush, classes_Hand, utils_Parser},
    associations={Hand_Card, Hand_Card2},
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