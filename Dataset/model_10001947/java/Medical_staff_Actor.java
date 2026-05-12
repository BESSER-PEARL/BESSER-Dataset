





import java.util.List;
import java.util.ArrayList;

public class Medical_staff_Actor  {






    private Decision_support_system_Check_treatment_recommendation_for_diagnosed_disease_UseCase decision_support_system_check_treatment_recommendation_for_diagnosed_disease_usecase;




    private Decision_support_system_Input_heart_disease_symptoms_UseCase decision_support_system_input_heart_disease_symptoms_usecase;




    private Decision_support_system_Generate_heart_disease_diagnosis_UseCase decision_support_system_generate_heart_disease_diagnosis_usecase;


    public Medical_staff_Actor(
    ) {
    }



    public Decision_support_system_Check_treatment_recommendation_for_diagnosed_disease_UseCase getDecision_support_system_check_treatment_recommendation_for_diagnosed_disease_usecase() {
        return decision_support_system_check_treatment_recommendation_for_diagnosed_disease_usecase;
    }

    public void setDecision_support_system_check_treatment_recommendation_for_diagnosed_disease_usecase(Decision_support_system_Check_treatment_recommendation_for_diagnosed_disease_UseCase decision_support_system_check_treatment_recommendation_for_diagnosed_disease_usecase) {
        this.decision_support_system_check_treatment_recommendation_for_diagnosed_disease_usecase = decision_support_system_check_treatment_recommendation_for_diagnosed_disease_usecase;
    }
    public Decision_support_system_Input_heart_disease_symptoms_UseCase getDecision_support_system_input_heart_disease_symptoms_usecase() {
        return decision_support_system_input_heart_disease_symptoms_usecase;
    }

    public void setDecision_support_system_input_heart_disease_symptoms_usecase(Decision_support_system_Input_heart_disease_symptoms_UseCase decision_support_system_input_heart_disease_symptoms_usecase) {
        this.decision_support_system_input_heart_disease_symptoms_usecase = decision_support_system_input_heart_disease_symptoms_usecase;
    }
    public Decision_support_system_Generate_heart_disease_diagnosis_UseCase getDecision_support_system_generate_heart_disease_diagnosis_usecase() {
        return decision_support_system_generate_heart_disease_diagnosis_usecase;
    }

    public void setDecision_support_system_generate_heart_disease_diagnosis_usecase(Decision_support_system_Generate_heart_disease_diagnosis_UseCase decision_support_system_generate_heart_disease_diagnosis_usecase) {
        this.decision_support_system_generate_heart_disease_diagnosis_usecase = decision_support_system_generate_heart_disease_diagnosis_usecase;
    }

}