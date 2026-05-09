





import java.util.List;
import java.util.ArrayList;

public class assessment_Models  {






    private List<assessment_Model> assessment_models;




    private assessment_Application assessment_application;




    private assessment_Model assessment_model;




    private assessment_Application assessment_application;


    public assessment_Models(
    ) {
        this.assessment_models = new ArrayList<>();
    }

    public assessment_Models(
        ArrayList<assessment_Model> assessment_models    ) {
        this.assessment_models = assessment_models;
    }


    public List<assessment_Model> getAssessment_models() {
        return assessment_models;
    }

    public void addAssessment_model(Assessment_model assessment_model) {
        this.assessment_models.add(assessment_model);
    }
    public assessment_Application getAssessment_application() {
        return assessment_application;
    }

    public void setAssessment_application(assessment_Application assessment_application) {
        this.assessment_application = assessment_application;
    }
    public assessment_Model getAssessment_model() {
        return assessment_model;
    }

    public void setAssessment_model(assessment_Model assessment_model) {
        this.assessment_model = assessment_model;
    }
    public assessment_Application getAssessment_application() {
        return assessment_application;
    }

    public void setAssessment_application(assessment_Application assessment_application) {
        this.assessment_application = assessment_application;
    }

}