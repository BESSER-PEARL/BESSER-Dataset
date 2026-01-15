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
TokenType: Enumeration = Enumeration(
    name="TokenType",
    literals={
            EnumerationLiteral(name="Basic"),
			EnumerationLiteral(name="External"),
			EnumerationLiteral(name="Undeveloped"),
			EnumerationLiteral(name="Intermediate"),
			EnumerationLiteral(name="Component"),
			EnumerationLiteral(name="System"),
			EnumerationLiteral(name="Unhandled"),
			EnumerationLiteral(name="Sink")
    }
)

TokenTraceType: Enumeration = Enumeration(
    name="TokenTraceType",
    literals={
            EnumerationLiteral(name="TokenGraph"),
			EnumerationLiteral(name="TokenTrace"),
			EnumerationLiteral(name="CompositeParts"),
			EnumerationLiteral(name="MinimalCutSet")
    }
)

# Classes
TokenTrace_TokenTrace = Class(name="TokenTrace::TokenTrace")
TokenTrace_Token = Class(name="TokenTrace::Token")
TokenTrace_EObject = Class(name="TokenTrace::EObject")
TokenTrace_Literal = Class(name="TokenTrace::Literal")
MultiLiteralConstraint = Class(name="MultiLiteralConstraint")

# TokenTrace_TokenTrace class attributes and methods
TokenTrace_TokenTrace_name: Property = Property(name="name", type=StringType)
TokenTrace_TokenTrace_message: Property = Property(name="message", type=StringType)
TokenTrace_TokenTrace_tokenTraceType: Property = Property(name="tokenTraceType", type=StringType)
TokenTrace_TokenTrace.attributes={TokenTrace_TokenTrace_name, TokenTrace_TokenTrace_message, TokenTrace_TokenTrace_tokenTraceType}

# TokenTrace_Token class attributes and methods
TokenTrace_Token_name: Property = Property(name="name", type=StringType)
TokenTrace_Token_message: Property = Property(name="message", type=StringType)
TokenTrace_Token_tokenType: Property = Property(name="tokenType", type=StringType)
TokenTrace_Token_referenceCount: Property = Property(name="referenceCount", type=IntegerType)
TokenTrace_Token_assignedProbability: Property = Property(name="assignedProbability", type=StringType)
TokenTrace_Token_computedProbability: Property = Property(name="computedProbability", type=StringType)
TokenTrace_Token_scale: Property = Property(name="scale", type=StringType)
TokenTrace_Token_m_getProbability: Method = Method(name="getProbability", parameters={}, type=StringType)
TokenTrace_Token.attributes={TokenTrace_Token_tokenType, TokenTrace_Token_message, TokenTrace_Token_scale, TokenTrace_Token_referenceCount, TokenTrace_Token_assignedProbability, TokenTrace_Token_name, TokenTrace_Token_computedProbability}
TokenTrace_Token.methods={TokenTrace_Token_m_getProbability}

# TokenTrace_EObject class attributes and methods

# TokenTrace_Literal class attributes and methods

# MultiLiteralConstraint class attributes and methods

# Relationships
root0: BinaryAssociation = BinaryAssociation(
    name="root0",
    ends={
        Property(name="TokenTrace_Token", type=TokenTrace_TokenTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="TokenTrace_TokenTrace", type=TokenTrace_Token, multiplicity=Multiplicity(0, 1))
    }
)
instanceRoot1: BinaryAssociation = BinaryAssociation(
    name="instanceRoot1",
    ends={
        Property(name="TokenTrace_EObject", type=TokenTrace_TokenTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="TokenTrace_TokenTrace2", type=TokenTrace_EObject, multiplicity=Multiplicity(0, 1))
    }
)
tokens3: BinaryAssociation = BinaryAssociation(
    name="tokens3",
    ends={
        Property(name="TokenTrace_Token5", type=TokenTrace_TokenTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="TokenTrace_TokenTrace4", type=TokenTrace_Token, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inferredRootLiteral6: BinaryAssociation = BinaryAssociation(
    name="inferredRootLiteral6",
    ends={
        Property(name="TokenTrace_Literal", type=TokenTrace_TokenTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="TokenTrace_TokenTrace7", type=TokenTrace_Literal, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tokens9: BinaryAssociation = BinaryAssociation(
    name="tokens9",
    ends={
        Property(name="TokenTrace_Token10", type=TokenTrace_Token, multiplicity=Multiplicity(1, 1)),
        Property(name="TokenTrace_Token8", type=TokenTrace_Token, multiplicity=Multiplicity(0, 9999))
    }
)
relatedEObject11: BinaryAssociation = BinaryAssociation(
    name="relatedEObject11",
    ends={
        Property(name="TokenTrace_EObject13", type=TokenTrace_Token, multiplicity=Multiplicity(1, 1)),
        Property(name="TokenTrace_Token12", type=TokenTrace_EObject, multiplicity=Multiplicity(0, 1))
    }
)
tokenLiteral14: BinaryAssociation = BinaryAssociation(
    name="tokenLiteral14",
    ends={
        Property(name="TokenTrace_Literal16", type=TokenTrace_Token, multiplicity=Multiplicity(1, 1)),
        Property(name="TokenTrace_Token15", type=TokenTrace_Literal, multiplicity=Multiplicity(0, 1))
    }
)
literalSink17: BinaryAssociation = BinaryAssociation(
    name="literalSink17",
    ends={
        Property(name="TokenTrace_Literal19", type=TokenTrace_Token, multiplicity=Multiplicity(1, 1)),
        Property(name="TokenTrace_Token18", type=TokenTrace_Literal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_TokenTrace_Token_MultiLiteralConstraint = Generalization(general=MultiLiteralConstraint, specific=TokenTrace_Token)

# Domain Model
domain_model = DomainModel(
    name="TokenTrace",
    types={TokenTrace_TokenTrace, TokenTrace_Token, TokenTrace_EObject, TokenTrace_Literal, MultiLiteralConstraint, TokenType, TokenTraceType},
    associations={root0, instanceRoot1, tokens3, inferredRootLiteral6, tokens9, relatedEObject11, tokenLiteral14, literalSink17},
    generalizations={gen_TokenTrace_Token_MultiLiteralConstraint},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)