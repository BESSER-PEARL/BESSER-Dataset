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
Question_T__Interface = Class(name="Question_T__Interface")
TF = Class(name="TF")
MC = Class(name="MC")
ShortAnswer = Class(name="ShortAnswer")
Essay = Class(name="Essay")
Ranking = Class(name="Ranking")
MachingQuestion_Interface = Class(name="MachingQuestion_Interface")
Matching = Class(name="Matching")

# Question_T__Interface class attributes and methods

# TF class attributes and methods
TF_question: Property = Property(name="question", type=StringType)
TF_c1__c2__c3__c4: Property = Property(name="c1__c2__c3__c4", type=StringType)
TF_answer: Property = Property(name="answer", type=StringType)
TF_multians: Property = Property(name="multians", type=BooleanType)
TF.attributes={TF_answer, TF_c1__c2__c3__c4, TF_question, TF_multians}

# MC class attributes and methods
MC_c1__c2__c3__c4: Property = Property(name="c1__c2__c3__c4", type=StringType)
MC_answer: Property = Property(name="answer", type=StringType)
MC_multians: Property = Property(name="multians", type=BooleanType)
MC_question: Property = Property(name="question", type=StringType)
MC.attributes={MC_c1__c2__c3__c4, MC_question, MC_multians, MC_answer}

# ShortAnswer class attributes and methods
ShortAnswer_question: Property = Property(name="question", type=StringType)
ShortAnswer_c1__c2__c3__c4: Property = Property(name="c1__c2__c3__c4", type=StringType)
ShortAnswer_answer: Property = Property(name="answer", type=StringType)
ShortAnswer_multians: Property = Property(name="multians", type=BooleanType)
ShortAnswer.attributes={ShortAnswer_multians, ShortAnswer_c1__c2__c3__c4, ShortAnswer_answer, ShortAnswer_question}

# Essay class attributes and methods
Essay_question: Property = Property(name="question", type=StringType)
Essay_c1__c2__c3__c4: Property = Property(name="c1__c2__c3__c4", type=StringType)
Essay_answer: Property = Property(name="answer", type=StringType)
Essay_multians: Property = Property(name="multians", type=BooleanType)
Essay.attributes={Essay_c1__c2__c3__c4, Essay_answer, Essay_question, Essay_multians}

# Ranking class attributes and methods
Ranking_question: Property = Property(name="question", type=StringType)
Ranking_c1__c2__c3__c4: Property = Property(name="c1__c2__c3__c4", type=StringType)
Ranking_answer: Property = Property(name="answer", type=StringType)
Ranking_multians: Property = Property(name="multians", type=BooleanType)
Ranking.attributes={Ranking_answer, Ranking_c1__c2__c3__c4, Ranking_question, Ranking_multians}

# MachingQuestion_Interface class attributes and methods

# Matching class attributes and methods
Matching_question: Property = Property(name="question", type=StringType)
Matching_c1__c2__c3__c4: Property = Property(name="c1__c2__c3__c4", type=StringType)
Matching_col1__col2: Property = Property(name="col1__col2", type=StringType)
Matching_answer: Property = Property(name="answer", type=StringType)
Matching_multians: Property = Property(name="multians", type=BooleanType)
Matching.attributes={Matching_answer, Matching_c1__c2__c3__c4, Matching_col1__col2, Matching_multians, Matching_question}

# Domain Model
domain_model = DomainModel(
    name="_JgcMELajEee7sYPkE4_GPA",
    types={Question_T__Interface, TF, MC, ShortAnswer, Essay, Ranking, MachingQuestion_Interface, Matching},
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