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
Usu_rio_Actor = Class(name="Usu_rio_Actor")
Aplicativo_Actor = Class(name="Aplicativo_Actor")
Servi_o_Web_Actor = Class(name="Servi_o_Web_Actor")
Autenticar_se_UseCase = Class(name="Autenticar_se_UseCase")
Selecionar_treino_UseCase = Class(name="Selecionar_treino_UseCase")
Iniciar_parar_monitoramento_card_aco_UseCase = Class(name="Iniciar_parar_monitoramento_card_aco_UseCase")
Receber_responder_requisi__es_UseCase = Class(name="Receber_responder_requisi__es_UseCase")
Analisar_dados_UseCase = Class(name="Analisar_dados_UseCase")
Sincronizar_dados_do_usu_rio_UseCase = Class(name="Sincronizar_dados_do_usu_rio_UseCase")
Estabelecer_comunica__o_com_wearable_UseCase = Class(name="Estabelecer_comunica__o_com_wearable_UseCase")
Usuario = Class(name="Usuario")
MedicaoBatimento = Class(name="MedicaoBatimento")
Treino = Class(name="Treino")
ServicoWeb = Class(name="ServicoWeb")
TreinoMonitoramento = Class(name="TreinoMonitoramento")
DispositivoBluetooth = Class(name="DispositivoBluetooth")
Aluno_Actor = Class(name="Aluno_Actor")
M_dulo_Pedag_gico_Actor = Class(name="M_dulo_Pedag_gico_Actor")
Sequenciar_atividades_UseCase = Class(name="Sequenciar_atividades_UseCase")
Avaliar_plano_de_ensino_UseCase = Class(name="Avaliar_plano_de_ensino_UseCase")
Adequar_sequ_ncia_UseCase = Class(name="Adequar_sequ_ncia_UseCase")
Fornecer_feedback_UseCase = Class(name="Fornecer_feedback_UseCase")
Identificar_erros_comuns_UseCase = Class(name="Identificar_erros_comuns_UseCase")
Solicitar_dica_UseCase = Class(name="Solicitar_dica_UseCase")
Fornecer_dica_UseCase = Class(name="Fornecer_dica_UseCase")
Fornecer_lista_de_atividades_superadas_UseCase = Class(name="Fornecer_lista_de_atividades_superadas_UseCase")
Propor_desafio_UseCase = Class(name="Propor_desafio_UseCase")
Acessar_atividade_UseCase = Class(name="Acessar_atividade_UseCase")
Subject = Class(name="Subject")
StudentSubject = Class(name="StudentSubject")
Activity = Class(name="Activity")
Exercise = Class(name="Exercise")
Instruction = Class(name="Instruction")
Curriculum = Class(name="Curriculum")
StudentHistory = Class(name="StudentHistory")
Step = Class(name="Step")
TutorStep = Class(name="TutorStep")
UserStep = Class(name="UserStep")
AlternativeCategory = Class(name="AlternativeCategory")
Alternative = Class(name="Alternative")
Feedback = Class(name="Feedback")
StudentStepHistory = Class(name="StudentStepHistory")
Student_Interface = Class(name="Student_Interface")
is_exercise_activity_id__UseCase = Class(name="is_exercise_activity_id__UseCase")
is_user_step_step_id__UseCase = Class(name="is_user_step_step_id__UseCase")
sequence_student__UseCase = Class(name="sequence_student__UseCase")
select_activity_request__UseCase = Class(name="select_activity_request__UseCase")
student_module_views_get_student_domains_student__UseCase = Class(name="student_module_views_get_student_domains_student__UseCase")
select_exercise_student__subject__UseCase = Class(name="select_exercise_student__subject__UseCase")
update_history_request__UseCase = Class(name="update_history_request__UseCase")
student_module_views_update_evidence_student__evidence_dict__UseCase = Class(name="student_module_views_update_evidence_student__evidence_dict__UseCase")
update_student_subject_student__student_knowledge__UseCase = Class(name="update_student_subject_student__student_knowledge__UseCase")
handle_user_answer_request__UseCase = Class(name="handle_user_answer_request__UseCase")
correct_alternative_alternative_id__alternative_answer__student__user_exercise__UseCase = Class(name="correct_alternative_alternative_id__alternative_answer__student__user_exercise__UseCase")

# Usu_rio_Actor class attributes and methods

# Aplicativo_Actor class attributes and methods

# Servi_o_Web_Actor class attributes and methods

# Autenticar_se_UseCase class attributes and methods

# Selecionar_treino_UseCase class attributes and methods

# Iniciar_parar_monitoramento_card_aco_UseCase class attributes and methods

# Receber_responder_requisi__es_UseCase class attributes and methods

# Analisar_dados_UseCase class attributes and methods

# Sincronizar_dados_do_usu_rio_UseCase class attributes and methods

# Estabelecer_comunica__o_com_wearable_UseCase class attributes and methods

# Usuario class attributes and methods
Usuario_nome: Property = Property(name="nome", type=StringType)
Usuario_dataNascimento: Property = Property(name="dataNascimento", type=StringType)
Usuario_peso: Property = Property(name="peso", type=StringType)
Usuario_cpf: Property = Property(name="cpf", type=StringType)
Usuario_senha: Property = Property(name="senha", type=StringType)
Usuario.attributes={Usuario_nome, Usuario_peso, Usuario_senha, Usuario_dataNascimento, Usuario_cpf}

# MedicaoBatimento class attributes and methods
MedicaoBatimento_usuario: Property = Property(name="usuario", type=Usu_rio_Actor)
MedicaoBatimento_valor: Property = Property(name="valor", type=IntegerType)
MedicaoBatimento_enviado: Property = Property(name="enviado", type=BooleanType)
MedicaoBatimento_instante: Property = Property(name="instante", type=StringType)
MedicaoBatimento_treino: Property = Property(name="treino", type=Treino)
MedicaoBatimento.attributes={MedicaoBatimento_valor, MedicaoBatimento_enviado, MedicaoBatimento_usuario, MedicaoBatimento_instante, MedicaoBatimento_treino}

# Treino class attributes and methods
Treino_nome: Property = Property(name="nome", type=StringType)
Treino.attributes={Treino_nome}

# ServicoWeb class attributes and methods

# TreinoMonitoramento class attributes and methods
TreinoMonitoramento_fim: Property = Property(name="fim", type=StringType)
TreinoMonitoramento_inicio: Property = Property(name="inicio", type=StringType)
TreinoMonitoramento.attributes={TreinoMonitoramento_inicio, TreinoMonitoramento_fim}

# DispositivoBluetooth class attributes and methods
DispositivoBluetooth_macAddress: Property = Property(name="macAddress", type=StringType)
DispositivoBluetooth_nome: Property = Property(name="nome", type=StringType)
DispositivoBluetooth.attributes={DispositivoBluetooth_macAddress, DispositivoBluetooth_nome}

# Aluno_Actor class attributes and methods

# M_dulo_Pedag_gico_Actor class attributes and methods

# Sequenciar_atividades_UseCase class attributes and methods

# Avaliar_plano_de_ensino_UseCase class attributes and methods

# Adequar_sequ_ncia_UseCase class attributes and methods

# Fornecer_feedback_UseCase class attributes and methods

# Identificar_erros_comuns_UseCase class attributes and methods

# Solicitar_dica_UseCase class attributes and methods

# Fornecer_dica_UseCase class attributes and methods

# Fornecer_lista_de_atividades_superadas_UseCase class attributes and methods

# Propor_desafio_UseCase class attributes and methods

# Acessar_atividade_UseCase class attributes and methods

# Subject class attributes and methods
Subject_name: Property = Property(name="name", type=StringType)
Subject.attributes={Subject_name}

# StudentSubject class attributes and methods
StudentSubject_student: Property = Property(name="student", type=Student_Interface)
StudentSubject_subject: Property = Property(name="subject", type=Subject)
StudentSubject_level: Property = Property(name="level", type=IntegerType)
StudentSubject.attributes={StudentSubject_subject, StudentSubject_student, StudentSubject_level}

# Activity class attributes and methods
Activity_content: Property = Property(name="content", type=StringType)
Activity_subject: Property = Property(name="subject", type=Subject)
Activity.attributes={Activity_content, Activity_subject}

# Exercise class attributes and methods
Exercise_difficulty: Property = Property(name="difficulty", type=IntegerType)
Exercise_user_exercise: Property = Property(name="user_exercise", type=BooleanType)
Exercise.attributes={Exercise_user_exercise, Exercise_difficulty}

# Instruction class attributes and methods
Instruction_title: Property = Property(name="title", type=StringType)
Instruction_level: Property = Property(name="level", type=IntegerType)
Instruction.attributes={Instruction_level, Instruction_title}

# Curriculum class attributes and methods
Curriculum_sequence: Property = Property(name="sequence", type=IntegerType)
Curriculum_activity: Property = Property(name="activity", type=Activity)
Curriculum.attributes={Curriculum_sequence, Curriculum_activity}

# StudentHistory class attributes and methods
StudentHistory_student: Property = Property(name="student", type=Student_Interface)
StudentHistory_activity: Property = Property(name="activity", type=Activity)
StudentHistory_sequence: Property = Property(name="sequence", type=IntegerType)
StudentHistory.attributes={StudentHistory_student, StudentHistory_sequence, StudentHistory_activity}

# Step class attributes and methods
Step_exercise: Property = Property(name="exercise", type=Exercise)
Step_content: Property = Property(name="content", type=StringType)
Step.attributes={Step_exercise, Step_content}

# TutorStep class attributes and methods
TutorStep_evidence: Property = Property(name="evidence", type=StringType)
TutorStep_difficulty: Property = Property(name="difficulty", type=IntegerType)
TutorStep.attributes={TutorStep_difficulty, TutorStep_evidence}

# UserStep class attributes and methods

# AlternativeCategory class attributes and methods
AlternativeCategory_name: Property = Property(name="name", type=StringType)
AlternativeCategory.attributes={AlternativeCategory_name}

# Alternative class attributes and methods
Alternative_step: Property = Property(name="step", type=Step)
Alternative_content: Property = Property(name="content", type=StringType)
Alternative_answer: Property = Property(name="answer", type=StringType)
Alternative_answer_text: Property = Property(name="answer_text", type=StringType)
Alternative_category: Property = Property(name="category", type=AlternativeCategory)
Alternative.attributes={Alternative_step, Alternative_content, Alternative_answer_text, Alternative_answer, Alternative_category}

# Feedback class attributes and methods
Feedback_alternative: Property = Property(name="alternative", type=Alternative)
Feedback_feedback: Property = Property(name="feedback", type=StringType)
Feedback_state: Property = Property(name="state", type=BooleanType)
Feedback_level: Property = Property(name="level", type=IntegerType)
Feedback.attributes={Feedback_alternative, Feedback_level, Feedback_feedback, Feedback_state}

# StudentStepHistory class attributes and methods
StudentStepHistory_student: Property = Property(name="student", type=Student_Interface)
StudentStepHistory_step: Property = Property(name="step", type=Step)
StudentStepHistory_status: Property = Property(name="status", type=BooleanType)
StudentStepHistory_tries: Property = Property(name="tries", type=IntegerType)
StudentStepHistory.attributes={StudentStepHistory_step, StudentStepHistory_status, StudentStepHistory_tries, StudentStepHistory_student}

# Student_Interface class attributes and methods

# is_exercise_activity_id__UseCase class attributes and methods

# is_user_step_step_id__UseCase class attributes and methods

# sequence_student__UseCase class attributes and methods

# select_activity_request__UseCase class attributes and methods

# student_module_views_get_student_domains_student__UseCase class attributes and methods

# select_exercise_student__subject__UseCase class attributes and methods

# update_history_request__UseCase class attributes and methods

# student_module_views_update_evidence_student__evidence_dict__UseCase class attributes and methods

# update_student_subject_student__student_knowledge__UseCase class attributes and methods

# handle_user_answer_request__UseCase class attributes and methods

# correct_alternative_alternative_id__alternative_answer__student__user_exercise__UseCase class attributes and methods

# Relationships
Autenticar_se_Usu_rio: BinaryAssociation = BinaryAssociation(
    name="Autenticar_se_Usu_rio",
    ends={
        Property(name="usu_rio0", type=Usu_rio_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="autenticar_se1", type=Autenticar_se_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Selecionar_treino_Usu_rio: BinaryAssociation = BinaryAssociation(
    name="Selecionar_treino_Usu_rio",
    ends={
        Property(name="usu_rio2", type=Usu_rio_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="selecionar_treino3", type=Selecionar_treino_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Iniciar_parar_monitoramento_card_aco_Usu_rio: BinaryAssociation = BinaryAssociation(
    name="Iniciar_parar_monitoramento_card_aco_Usu_rio",
    ends={
        Property(name="usu_rio4", type=Usu_rio_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="iniciar_parar_monitoramento_card_aco5", type=Iniciar_parar_monitoramento_card_aco_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Servi_o_Web_Receber_responder_requisi__es: BinaryAssociation = BinaryAssociation(
    name="Servi_o_Web_Receber_responder_requisi__es",
    ends={
        Property(name="receber_responder_requisi__es6", type=Receber_responder_requisi__es_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="servi_o_Web7", type=Servi_o_Web_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Analisar_dados_Servi_o_Web: BinaryAssociation = BinaryAssociation(
    name="Analisar_dados_Servi_o_Web",
    ends={
        Property(name="servi_o_Web8", type=Servi_o_Web_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="analisar_dados9", type=Analisar_dados_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Sincronizar_dados_Aplicativo: BinaryAssociation = BinaryAssociation(
    name="Sincronizar_dados_Aplicativo",
    ends={
        Property(name="aplicativo10", type=Aplicativo_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="sincronizar_dados11", type=Sincronizar_dados_do_usu_rio_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Aplicativo_Estabelecer_comunica__o_com_wearable: BinaryAssociation = BinaryAssociation(
    name="Aplicativo_Estabelecer_comunica__o_com_wearable",
    ends={
        Property(name="estabelecer_comunica__o_com_wearable12", type=Estabelecer_comunica__o_com_wearable_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="aplicativo13", type=Aplicativo_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Sequenciar_atividades_M_dulo_Pedag_gico: BinaryAssociation = BinaryAssociation(
    name="Sequenciar_atividades_M_dulo_Pedag_gico",
    ends={
        Property(name="m_dulo_Pedag_gico14", type=M_dulo_Pedag_gico_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="sequenciar_atividades15", type=Sequenciar_atividades_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Fornecer_feedback_M_dulo_Pedag_gico: BinaryAssociation = BinaryAssociation(
    name="Fornecer_feedback_M_dulo_Pedag_gico",
    ends={
        Property(name="m_dulo_Pedag_gico16", type=M_dulo_Pedag_gico_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="fornecer_feedback17", type=Fornecer_feedback_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Aluno_Solicitar_dica: BinaryAssociation = BinaryAssociation(
    name="Aluno_Solicitar_dica",
    ends={
        Property(name="solicitar_dica18", type=Solicitar_dica_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="aluno19", type=Aluno_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Activity_StudentHistory: BinaryAssociation = BinaryAssociation(
    name="Activity_StudentHistory",
    ends={
        Property(name="activity235", type=Activity, multiplicity=Multiplicity(0, 1)),
        Property(name="studentHistory34", type=StudentHistory, multiplicity=Multiplicity(0, 1))
    }
)
Exercise_Step: BinaryAssociation = BinaryAssociation(
    name="Exercise_Step",
    ends={
        Property(name="step36", type=Step, multiplicity=Multiplicity(0, 1)),
        Property(name="exercise237", type=Exercise, multiplicity=Multiplicity(0, 1))
    }
)
Alternative_AlternativeCategory: BinaryAssociation = BinaryAssociation(
    name="Alternative_AlternativeCategory",
    ends={
        Property(name="alternativeCategory38", type=AlternativeCategory, multiplicity=Multiplicity(0, 1)),
        Property(name="alternative39", type=Alternative, multiplicity=Multiplicity(0, 1))
    }
)
Alternative_Step: BinaryAssociation = BinaryAssociation(
    name="Alternative_Step",
    ends={
        Property(name="step240", type=Step, multiplicity=Multiplicity(0, 1)),
        Property(name="alternative41", type=Alternative, multiplicity=Multiplicity(0, 1))
    }
)
Alternative_Feedback: BinaryAssociation = BinaryAssociation(
    name="Alternative_Feedback",
    ends={
        Property(name="feedback42", type=Feedback, multiplicity=Multiplicity(0, 1)),
        Property(name="alternative243", type=Alternative, multiplicity=Multiplicity(0, 1))
    }
)
Step_StudentStepHistory: BinaryAssociation = BinaryAssociation(
    name="Step_StudentStepHistory",
    ends={
        Property(name="studentStepHistory44", type=StudentStepHistory, multiplicity=Multiplicity(0, 1)),
        Property(name="step245", type=Step, multiplicity=Multiplicity(0, 1))
    }
)
M_dulo_Pedag_gico_Fornecer_dica: BinaryAssociation = BinaryAssociation(
    name="M_dulo_Pedag_gico_Fornecer_dica",
    ends={
        Property(name="fornecer_dica20", type=Fornecer_dica_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="m_dulo_Pedag_gico21", type=M_dulo_Pedag_gico_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Fornecer_lista_de_atividades_superadas_M_dulo_Pedag_gico: BinaryAssociation = BinaryAssociation(
    name="Fornecer_lista_de_atividades_superadas_M_dulo_Pedag_gico",
    ends={
        Property(name="m_dulo_Pedag_gico22", type=M_dulo_Pedag_gico_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="fornecer_lista_de_atividades_superadas23", type=Fornecer_lista_de_atividades_superadas_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Propor_desafio_M_dulo_Pedag_gico: BinaryAssociation = BinaryAssociation(
    name="Propor_desafio_M_dulo_Pedag_gico",
    ends={
        Property(name="m_dulo_Pedag_gico24", type=M_dulo_Pedag_gico_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="propor_desafio25", type=Propor_desafio_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Acessar_atividade_Aluno: BinaryAssociation = BinaryAssociation(
    name="Acessar_atividade_Aluno",
    ends={
        Property(name="aluno26", type=Aluno_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="acessar_atividade27", type=Acessar_atividade_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Subject_StudentSubject: BinaryAssociation = BinaryAssociation(
    name="Subject_StudentSubject",
    ends={
        Property(name="studentSubject28", type=StudentSubject, multiplicity=Multiplicity(0, 1)),
        Property(name="subject229", type=Subject, multiplicity=Multiplicity(0, 1))
    }
)
Subject_Activity: BinaryAssociation = BinaryAssociation(
    name="Subject_Activity",
    ends={
        Property(name="activity30", type=Activity, multiplicity=Multiplicity(0, 1)),
        Property(name="subject231", type=Subject, multiplicity=Multiplicity(0, 1))
    }
)
Activity_Curriculum: BinaryAssociation = BinaryAssociation(
    name="Activity_Curriculum",
    ends={
        Property(name="curriculum32", type=Curriculum, multiplicity=Multiplicity(0, 1)),
        Property(name="activity233", type=Activity, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_oLXE0D9QEeeTJ_4Vl2J2rQ",
    types={Usu_rio_Actor, Aplicativo_Actor, Servi_o_Web_Actor, Autenticar_se_UseCase, Selecionar_treino_UseCase, Iniciar_parar_monitoramento_card_aco_UseCase, Receber_responder_requisi__es_UseCase, Analisar_dados_UseCase, Sincronizar_dados_do_usu_rio_UseCase, Estabelecer_comunica__o_com_wearable_UseCase, Usuario, MedicaoBatimento, Treino, ServicoWeb, TreinoMonitoramento, DispositivoBluetooth, Aluno_Actor, M_dulo_Pedag_gico_Actor, Sequenciar_atividades_UseCase, Avaliar_plano_de_ensino_UseCase, Adequar_sequ_ncia_UseCase, Fornecer_feedback_UseCase, Identificar_erros_comuns_UseCase, Solicitar_dica_UseCase, Fornecer_dica_UseCase, Fornecer_lista_de_atividades_superadas_UseCase, Propor_desafio_UseCase, Acessar_atividade_UseCase, Subject, StudentSubject, Activity, Exercise, Instruction, Curriculum, StudentHistory, Step, TutorStep, UserStep, AlternativeCategory, Alternative, Feedback, StudentStepHistory, Student_Interface, is_exercise_activity_id__UseCase, is_user_step_step_id__UseCase, sequence_student__UseCase, select_activity_request__UseCase, student_module_views_get_student_domains_student__UseCase, select_exercise_student__subject__UseCase, update_history_request__UseCase, student_module_views_update_evidence_student__evidence_dict__UseCase, update_student_subject_student__student_knowledge__UseCase, handle_user_answer_request__UseCase, correct_alternative_alternative_id__alternative_answer__student__user_exercise__UseCase},
    associations={Autenticar_se_Usu_rio, Selecionar_treino_Usu_rio, Iniciar_parar_monitoramento_card_aco_Usu_rio, Servi_o_Web_Receber_responder_requisi__es, Analisar_dados_Servi_o_Web, Sincronizar_dados_Aplicativo, Aplicativo_Estabelecer_comunica__o_com_wearable, Sequenciar_atividades_M_dulo_Pedag_gico, Fornecer_feedback_M_dulo_Pedag_gico, Aluno_Solicitar_dica, Activity_StudentHistory, Exercise_Step, Alternative_AlternativeCategory, Alternative_Step, Alternative_Feedback, Step_StudentStepHistory, M_dulo_Pedag_gico_Fornecer_dica, Fornecer_lista_de_atividades_superadas_M_dulo_Pedag_gico, Propor_desafio_M_dulo_Pedag_gico, Acessar_atividade_Aluno, Subject_StudentSubject, Subject_Activity, Activity_Curriculum},
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