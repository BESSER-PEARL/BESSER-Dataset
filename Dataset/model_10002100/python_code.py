from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class correct_alternative_alternative_id__alternative_answer__student__user_exercise__UseCase:

    pass


class handle_user_answer_request__UseCase:

    pass


class update_student_subject_student__student_knowledge__UseCase:

    pass


class student_module_views_update_evidence_student__evidence_dict__UseCase:

    pass


class update_history_request__UseCase:

    pass


class select_exercise_student__subject__UseCase:

    pass


class student_module_views_get_student_domains_student__UseCase:

    pass


class select_activity_request__UseCase:

    pass


class sequence_student__UseCase:

    pass


class is_user_step_step_id__UseCase:

    pass


class is_exercise_activity_id__UseCase:

    pass


class Acessar_atividade_UseCase:

    pass


class Propor_desafio_UseCase:

    pass


class Fornecer_lista_de_atividades_superadas_UseCase:

    pass


class Fornecer_dica_UseCase:

    pass


class Solicitar_dica_UseCase:

    pass


class Identificar_erros_comuns_UseCase:

    pass


class Fornecer_feedback_UseCase:

    pass


class Adequar_sequ_ncia_UseCase:

    pass


class Avaliar_plano_de_ensino_UseCase:

    pass


class Sequenciar_atividades_UseCase:

    pass


class M_dulo_Pedag_gico_Actor:

    pass


class Aluno_Actor:

    pass


class Estabelecer_comunica__o_com_wearable_UseCase:

    pass


class Sincronizar_dados_do_usu_rio_UseCase:

    pass


class Analisar_dados_UseCase:

    pass


class Receber_responder_requisi__es_UseCase:

    pass


class Iniciar_parar_monitoramento_card_aco_UseCase:

    pass


class Selecionar_treino_UseCase:

    pass


class Autenticar_se_UseCase:

    pass


class Servi_o_Web_Actor:

    pass


class Aplicativo_Actor:

    pass


class Usu_rio_Actor:

    pass





class Student_Interface:

    pass


class StudentStepHistory:

    def __init__(self, student: Student_Interface, step: Step, status: bool, tries: int, step245: "Step" = None):
        self.student = student
        self.step = step
        self.status = status
        self.tries = tries
        self.step245 = step245
        
        pass
    @property
    def student(self):
        return self.__student
    @student.setter
    def student(self, student: Student_Interface):
        self.__student = student

    @property
    def tries(self):
        return self.__tries
    @tries.setter
    def tries(self, tries: int):
        self.__tries = tries

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: bool):
        self.__status = status

    @property
    def step(self):
        return self.__step
    @step.setter
    def step(self, step: Step):
        self.__step = step

    @property
    def step245(self):
        return self.__step245
    @step245.setter
    def step245(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StudentStepHistory__step245", None)
        self.__step245 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studentStepHistory44"):
                opp_val = getattr(old_value, "studentStepHistory44", None)
                if opp_val == self:
                    setattr(old_value, "studentStepHistory44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studentStepHistory44"):
                opp_val = getattr(value, "studentStepHistory44", None)
                setattr(value, "studentStepHistory44", self)



class Feedback:

    def __init__(self, alternative: Alternative, feedback: str, state: bool, level: int, alternative243: "Alternative" = None):
        self.alternative = alternative
        self.feedback = feedback
        self.state = state
        self.level = level
        self.alternative243 = alternative243
        
        pass
    @property
    def feedback(self):
        return self.__feedback
    @feedback.setter
    def feedback(self, feedback: str):
        self.__feedback = feedback

    @property
    def state(self):
        return self.__state
    @state.setter
    def state(self, state: bool):
        self.__state = state

    @property
    def level(self):
        return self.__level
    @level.setter
    def level(self, level: int):
        self.__level = level

    @property
    def alternative(self):
        return self.__alternative
    @alternative.setter
    def alternative(self, alternative: Alternative):
        self.__alternative = alternative

    @property
    def alternative243(self):
        return self.__alternative243
    @alternative243.setter
    def alternative243(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Feedback__alternative243", None)
        self.__alternative243 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "feedback42"):
                opp_val = getattr(old_value, "feedback42", None)
                if opp_val == self:
                    setattr(old_value, "feedback42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "feedback42"):
                opp_val = getattr(value, "feedback42", None)
                setattr(value, "feedback42", self)



class Alternative:

    def __init__(self, step: Step, content: str, answer: str, answer_text: str, category: AlternativeCategory, alternativeCategory38: "AlternativeCategory" = None, step240: "Step" = None, feedback42: "Feedback" = None):
        self.step = step
        self.content = content
        self.answer = answer
        self.answer_text = answer_text
        self.category = category
        self.alternativeCategory38 = alternativeCategory38
        self.step240 = step240
        self.feedback42 = feedback42
        
        pass
    @property
    def answer_text(self):
        return self.__answer_text
    @answer_text.setter
    def answer_text(self, answer_text: str):
        self.__answer_text = answer_text

    @property
    def content(self):
        return self.__content
    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def category(self):
        return self.__category
    @category.setter
    def category(self, category: AlternativeCategory):
        self.__category = category

    @property
    def answer(self):
        return self.__answer
    @answer.setter
    def answer(self, answer: str):
        self.__answer = answer

    @property
    def step(self):
        return self.__step
    @step.setter
    def step(self, step: Step):
        self.__step = step

    @property
    def step240(self):
        return self.__step240
    @step240.setter
    def step240(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Alternative__step240", None)
        self.__step240 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alternative41"):
                opp_val = getattr(old_value, "alternative41", None)
                if opp_val == self:
                    setattr(old_value, "alternative41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alternative41"):
                opp_val = getattr(value, "alternative41", None)
                setattr(value, "alternative41", self)

    @property
    def alternativeCategory38(self):
        return self.__alternativeCategory38
    @alternativeCategory38.setter
    def alternativeCategory38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Alternative__alternativeCategory38", None)
        self.__alternativeCategory38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alternative39"):
                opp_val = getattr(old_value, "alternative39", None)
                if opp_val == self:
                    setattr(old_value, "alternative39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alternative39"):
                opp_val = getattr(value, "alternative39", None)
                setattr(value, "alternative39", self)

    @property
    def feedback42(self):
        return self.__feedback42
    @feedback42.setter
    def feedback42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Alternative__feedback42", None)
        self.__feedback42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alternative243"):
                opp_val = getattr(old_value, "alternative243", None)
                if opp_val == self:
                    setattr(old_value, "alternative243", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alternative243"):
                opp_val = getattr(value, "alternative243", None)
                setattr(value, "alternative243", self)



class AlternativeCategory:

    def __init__(self, name: str, alternative39: "Alternative" = None):
        self.name = name
        self.alternative39 = alternative39
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def alternative39(self):
        return self.__alternative39
    @alternative39.setter
    def alternative39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AlternativeCategory__alternative39", None)
        self.__alternative39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alternativeCategory38"):
                opp_val = getattr(old_value, "alternativeCategory38", None)
                if opp_val == self:
                    setattr(old_value, "alternativeCategory38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alternativeCategory38"):
                opp_val = getattr(value, "alternativeCategory38", None)
                setattr(value, "alternativeCategory38", self)



class UserStep:

    pass


class TutorStep:

    def __init__(self, evidence: str, difficulty: int):
        self.evidence = evidence
        self.difficulty = difficulty
        
        pass
    @property
    def evidence(self):
        return self.__evidence
    @evidence.setter
    def evidence(self, evidence: str):
        self.__evidence = evidence

    @property
    def difficulty(self):
        return self.__difficulty
    @difficulty.setter
    def difficulty(self, difficulty: int):
        self.__difficulty = difficulty



class Step:

    def __init__(self, exercise: Exercise, content: str, exercise237: "Exercise" = None, alternative41: "Alternative" = None, studentStepHistory44: "StudentStepHistory" = None):
        self.exercise = exercise
        self.content = content
        self.exercise237 = exercise237
        self.alternative41 = alternative41
        self.studentStepHistory44 = studentStepHistory44
        
        pass
    @property
    def exercise(self):
        return self.__exercise
    @exercise.setter
    def exercise(self, exercise: Exercise):
        self.__exercise = exercise

    @property
    def content(self):
        return self.__content
    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def alternative41(self):
        return self.__alternative41
    @alternative41.setter
    def alternative41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Step__alternative41", None)
        self.__alternative41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "step240"):
                opp_val = getattr(old_value, "step240", None)
                if opp_val == self:
                    setattr(old_value, "step240", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "step240"):
                opp_val = getattr(value, "step240", None)
                setattr(value, "step240", self)

    @property
    def studentStepHistory44(self):
        return self.__studentStepHistory44
    @studentStepHistory44.setter
    def studentStepHistory44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Step__studentStepHistory44", None)
        self.__studentStepHistory44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "step245"):
                opp_val = getattr(old_value, "step245", None)
                if opp_val == self:
                    setattr(old_value, "step245", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "step245"):
                opp_val = getattr(value, "step245", None)
                setattr(value, "step245", self)

    @property
    def exercise237(self):
        return self.__exercise237
    @exercise237.setter
    def exercise237(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Step__exercise237", None)
        self.__exercise237 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "step36"):
                opp_val = getattr(old_value, "step36", None)
                if opp_val == self:
                    setattr(old_value, "step36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "step36"):
                opp_val = getattr(value, "step36", None)
                setattr(value, "step36", self)



class StudentHistory:

    def __init__(self, student: Student_Interface, activity: Activity, sequence: int, activity235: "Activity" = None):
        self.student = student
        self.activity = activity
        self.sequence = sequence
        self.activity235 = activity235
        
        pass
    @property
    def activity(self):
        return self.__activity
    @activity.setter
    def activity(self, activity: Activity):
        self.__activity = activity

    @property
    def sequence(self):
        return self.__sequence
    @sequence.setter
    def sequence(self, sequence: int):
        self.__sequence = sequence

    @property
    def student(self):
        return self.__student
    @student.setter
    def student(self, student: Student_Interface):
        self.__student = student

    @property
    def activity235(self):
        return self.__activity235
    @activity235.setter
    def activity235(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StudentHistory__activity235", None)
        self.__activity235 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studentHistory34"):
                opp_val = getattr(old_value, "studentHistory34", None)
                if opp_val == self:
                    setattr(old_value, "studentHistory34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studentHistory34"):
                opp_val = getattr(value, "studentHistory34", None)
                setattr(value, "studentHistory34", self)



class Curriculum:

    def __init__(self, sequence: int, activity: Activity, activity233: "Activity" = None):
        self.sequence = sequence
        self.activity = activity
        self.activity233 = activity233
        
        pass
    @property
    def activity(self):
        return self.__activity
    @activity.setter
    def activity(self, activity: Activity):
        self.__activity = activity

    @property
    def sequence(self):
        return self.__sequence
    @sequence.setter
    def sequence(self, sequence: int):
        self.__sequence = sequence

    @property
    def activity233(self):
        return self.__activity233
    @activity233.setter
    def activity233(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Curriculum__activity233", None)
        self.__activity233 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "curriculum32"):
                opp_val = getattr(old_value, "curriculum32", None)
                if opp_val == self:
                    setattr(old_value, "curriculum32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "curriculum32"):
                opp_val = getattr(value, "curriculum32", None)
                setattr(value, "curriculum32", self)



class Instruction:

    def __init__(self, title: str, level: int):
        self.title = title
        self.level = level
        
        pass
    @property
    def title(self):
        return self.__title
    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def level(self):
        return self.__level
    @level.setter
    def level(self, level: int):
        self.__level = level



class Exercise:

    def __init__(self, difficulty: int, user_exercise: bool, step36: "Step" = None):
        self.difficulty = difficulty
        self.user_exercise = user_exercise
        self.step36 = step36
        
        pass
    @property
    def user_exercise(self):
        return self.__user_exercise
    @user_exercise.setter
    def user_exercise(self, user_exercise: bool):
        self.__user_exercise = user_exercise

    @property
    def difficulty(self):
        return self.__difficulty
    @difficulty.setter
    def difficulty(self, difficulty: int):
        self.__difficulty = difficulty

    @property
    def step36(self):
        return self.__step36
    @step36.setter
    def step36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Exercise__step36", None)
        self.__step36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "exercise237"):
                opp_val = getattr(old_value, "exercise237", None)
                if opp_val == self:
                    setattr(old_value, "exercise237", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "exercise237"):
                opp_val = getattr(value, "exercise237", None)
                setattr(value, "exercise237", self)



class Activity:

    def __init__(self, content: str, subject: Subject, subject231: "Subject" = None, curriculum32: "Curriculum" = None, studentHistory34: "StudentHistory" = None):
        self.content = content
        self.subject = subject
        self.subject231 = subject231
        self.curriculum32 = curriculum32
        self.studentHistory34 = studentHistory34
        
        pass
    @property
    def content(self):
        return self.__content
    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def subject(self):
        return self.__subject
    @subject.setter
    def subject(self, subject: Subject):
        self.__subject = subject

    @property
    def curriculum32(self):
        return self.__curriculum32
    @curriculum32.setter
    def curriculum32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activity__curriculum32", None)
        self.__curriculum32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activity233"):
                opp_val = getattr(old_value, "activity233", None)
                if opp_val == self:
                    setattr(old_value, "activity233", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activity233"):
                opp_val = getattr(value, "activity233", None)
                setattr(value, "activity233", self)

    @property
    def subject231(self):
        return self.__subject231
    @subject231.setter
    def subject231(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activity__subject231", None)
        self.__subject231 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activity30"):
                opp_val = getattr(old_value, "activity30", None)
                if opp_val == self:
                    setattr(old_value, "activity30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activity30"):
                opp_val = getattr(value, "activity30", None)
                setattr(value, "activity30", self)

    @property
    def studentHistory34(self):
        return self.__studentHistory34
    @studentHistory34.setter
    def studentHistory34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Activity__studentHistory34", None)
        self.__studentHistory34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activity235"):
                opp_val = getattr(old_value, "activity235", None)
                if opp_val == self:
                    setattr(old_value, "activity235", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activity235"):
                opp_val = getattr(value, "activity235", None)
                setattr(value, "activity235", self)



class StudentSubject:

    def __init__(self, student: Student_Interface, subject: Subject, level: int, subject229: "Subject" = None):
        self.student = student
        self.subject = subject
        self.level = level
        self.subject229 = subject229
        
        pass
    @property
    def subject(self):
        return self.__subject
    @subject.setter
    def subject(self, subject: Subject):
        self.__subject = subject

    @property
    def student(self):
        return self.__student
    @student.setter
    def student(self, student: Student_Interface):
        self.__student = student

    @property
    def level(self):
        return self.__level
    @level.setter
    def level(self, level: int):
        self.__level = level

    @property
    def subject229(self):
        return self.__subject229
    @subject229.setter
    def subject229(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StudentSubject__subject229", None)
        self.__subject229 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studentSubject28"):
                opp_val = getattr(old_value, "studentSubject28", None)
                if opp_val == self:
                    setattr(old_value, "studentSubject28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studentSubject28"):
                opp_val = getattr(value, "studentSubject28", None)
                setattr(value, "studentSubject28", self)



class Subject:

    def __init__(self, name: str, studentSubject28: "StudentSubject" = None, activity30: "Activity" = None):
        self.name = name
        self.studentSubject28 = studentSubject28
        self.activity30 = activity30
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def studentSubject28(self):
        return self.__studentSubject28
    @studentSubject28.setter
    def studentSubject28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Subject__studentSubject28", None)
        self.__studentSubject28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "subject229"):
                opp_val = getattr(old_value, "subject229", None)
                if opp_val == self:
                    setattr(old_value, "subject229", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "subject229"):
                opp_val = getattr(value, "subject229", None)
                setattr(value, "subject229", self)

    @property
    def activity30(self):
        return self.__activity30
    @activity30.setter
    def activity30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Subject__activity30", None)
        self.__activity30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "subject231"):
                opp_val = getattr(old_value, "subject231", None)
                if opp_val == self:
                    setattr(old_value, "subject231", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "subject231"):
                opp_val = getattr(value, "subject231", None)
                setattr(value, "subject231", self)



class DispositivoBluetooth:

    def __init__(self, macAddress: str, nome: str):
        self.macAddress = macAddress
        self.nome = nome
        
        pass
    @property
    def macAddress(self):
        return self.__macAddress
    @macAddress.setter
    def macAddress(self, macAddress: str):
        self.__macAddress = macAddress

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome



class TreinoMonitoramento:

    def __init__(self, fim: str, inicio: str):
        self.fim = fim
        self.inicio = inicio
        
        pass
    @property
    def fim(self):
        return self.__fim
    @fim.setter
    def fim(self, fim: str):
        self.__fim = fim

    @property
    def inicio(self):
        return self.__inicio
    @inicio.setter
    def inicio(self, inicio: str):
        self.__inicio = inicio



class ServicoWeb:

    pass


class Treino:

    def __init__(self, nome: str):
        self.nome = nome
        
        pass
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome



class MedicaoBatimento:

    def __init__(self, usuario: Usu_rio_Actor, valor: int, enviado: bool, instante: str, treino: Treino):
        self.usuario = usuario
        self.valor = valor
        self.enviado = enviado
        self.instante = instante
        self.treino = treino
        
        pass
    @property
    def treino(self):
        return self.__treino
    @treino.setter
    def treino(self, treino: Treino):
        self.__treino = treino

    @property
    def valor(self):
        return self.__valor
    @valor.setter
    def valor(self, valor: int):
        self.__valor = valor

    @property
    def instante(self):
        return self.__instante
    @instante.setter
    def instante(self, instante: str):
        self.__instante = instante

    @property
    def enviado(self):
        return self.__enviado
    @enviado.setter
    def enviado(self, enviado: bool):
        self.__enviado = enviado

    @property
    def usuario(self):
        return self.__usuario
    @usuario.setter
    def usuario(self, usuario: Usu_rio_Actor):
        self.__usuario = usuario



class Usuario:

    def __init__(self, nome: str, dataNascimento: str, peso: str, cpf: str, senha: str):
        self.nome = nome
        self.dataNascimento = dataNascimento
        self.peso = peso
        self.cpf = cpf
        self.senha = senha
        
        pass
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self, cpf: str):
        self.__cpf = cpf

    @property
    def senha(self):
        return self.__senha
    @senha.setter
    def senha(self, senha: str):
        self.__senha = senha

    @property
    def dataNascimento(self):
        return self.__dataNascimento
    @dataNascimento.setter
    def dataNascimento(self, dataNascimento: str):
        self.__dataNascimento = dataNascimento

    @property
    def peso(self):
        return self.__peso
    @peso.setter
    def peso(self, peso: str):
        self.__peso = peso

