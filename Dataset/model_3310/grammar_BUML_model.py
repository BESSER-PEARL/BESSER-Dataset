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
grammar_Grammar = Class(name="grammar::Grammar")
Named = Class(name="Named")
grammar_Rule = Class(name="grammar::Rule")
grammar_LHS = Class(name="grammar::LHS")
grammar_Embedding = Class(name="grammar::Embedding")
grammar_Node = Class(name="grammar::Node")
grammar_Graph = Class(name="grammar::Graph")
grammar_ConnexionInstruction = Class(name="grammar::ConnexionInstruction")
grammar_RHS = Class(name="grammar::RHS")

# grammar_Grammar class attributes and methods

# Named class attributes and methods

# grammar_Rule class attributes and methods
grammar_Rule_name: Property = Property(name="name", type=StringType)
grammar_Rule_priority: Property = Property(name="priority", type=IntegerType)
grammar_Rule.attributes={grammar_Rule_priority, grammar_Rule_name}

# grammar_LHS class attributes and methods

# grammar_Embedding class attributes and methods

# grammar_Node class attributes and methods

# grammar_Graph class attributes and methods

# grammar_ConnexionInstruction class attributes and methods
grammar_ConnexionInstruction_m: Property = Property(name="m", type=StringType)
grammar_ConnexionInstruction.attributes={grammar_ConnexionInstruction_m}

# grammar_RHS class attributes and methods

# Relationships
rules0: BinaryAssociation = BinaryAssociation(
    name="rules0",
    ends={
        Property(name="Rule", type=grammar_Grammar, multiplicity=Multiplicity(1, 1)),
        Property(name="parentGrammar", type=grammar_Rule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentGrammar1: BinaryAssociation = BinaryAssociation(
    name="parentGrammar1",
    ends={
        Property(name="Grammar", type=grammar_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="rules", type=grammar_Grammar, multiplicity=Multiplicity(1, 1))
    }
)
lhs2: BinaryAssociation = BinaryAssociation(
    name="lhs2",
    ends={
        Property(name="LHS", type=grammar_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="parentRule", type=grammar_LHS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs3: BinaryAssociation = BinaryAssociation(
    name="rhs3",
    ends={
        Property(name="RHS", type=grammar_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="parentRule4", type=grammar_RHS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
EmbeddingMechanism5: BinaryAssociation = BinaryAssociation(
    name="EmbeddingMechanism5",
    ends={
        Property(name="Embedding", type=grammar_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="ParentRule", type=grammar_Embedding, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parentRule6: BinaryAssociation = BinaryAssociation(
    name="parentRule6",
    ends={
        Property(name="Rule7", type=grammar_LHS, multiplicity=Multiplicity(1, 1)),
        Property(name="lhs", type=grammar_Rule, multiplicity=Multiplicity(1, 1))
    }
)
node8: BinaryAssociation = BinaryAssociation(
    name="node8",
    ends={
        Property(name="grammar_Node", type=grammar_LHS, multiplicity=Multiplicity(1, 1)),
        Property(name="grammar_LHS", type=grammar_Node, multiplicity=Multiplicity(1, 1))
    }
)
parentRule9: BinaryAssociation = BinaryAssociation(
    name="parentRule9",
    ends={
        Property(name="Rule10", type=grammar_RHS, multiplicity=Multiplicity(1, 1)),
        Property(name="rhs", type=grammar_Rule, multiplicity=Multiplicity(1, 1))
    }
)
subGraph11: BinaryAssociation = BinaryAssociation(
    name="subGraph11",
    ends={
        Property(name="grammar_Graph", type=grammar_RHS, multiplicity=Multiplicity(1, 1)),
        Property(name="grammar_RHS", type=grammar_Graph, multiplicity=Multiplicity(1, 1))
    }
)
ParentRule12: BinaryAssociation = BinaryAssociation(
    name="ParentRule12",
    ends={
        Property(name="Rule13", type=grammar_Embedding, multiplicity=Multiplicity(1, 1)),
        Property(name="EmbeddingMechanism", type=grammar_Rule, multiplicity=Multiplicity(1, 1))
    }
)
instructions14: BinaryAssociation = BinaryAssociation(
    name="instructions14",
    ends={
        Property(name="ConnexionInstruction", type=grammar_Embedding, multiplicity=Multiplicity(1, 1)),
        Property(name="parentEmbedding", type=grammar_ConnexionInstruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentEmbedding15: BinaryAssociation = BinaryAssociation(
    name="parentEmbedding15",
    ends={
        Property(name="Embedding16", type=grammar_ConnexionInstruction, multiplicity=Multiplicity(1, 1)),
        Property(name="instructions", type=grammar_Embedding, multiplicity=Multiplicity(1, 1))
    }
)
d17: BinaryAssociation = BinaryAssociation(
    name="d17",
    ends={
        Property(name="grammar_Node18", type=grammar_ConnexionInstruction, multiplicity=Multiplicity(1, 1)),
        Property(name="grammar_ConnexionInstruction", type=grammar_Node, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_grammar_Grammar_Named = Generalization(general=Named, specific=grammar_Grammar)

# Domain Model
domain_model = DomainModel(
    name="grammar",
    types={grammar_Grammar, Named, grammar_Rule, grammar_LHS, grammar_Embedding, grammar_Node, grammar_Graph, grammar_ConnexionInstruction, grammar_RHS},
    associations={rules0, parentGrammar1, lhs2, rhs3, EmbeddingMechanism5, parentRule6, node8, parentRule9, subGraph11, ParentRule12, instructions14, parentEmbedding15, d17},
    generalizations={gen_grammar_Grammar_Named},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)