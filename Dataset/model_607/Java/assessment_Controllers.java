





import java.util.List;
import java.util.ArrayList;

public class assessment_Controllers  {






    private assessment_Controller assessment_controller;




    private assessment_Application assessment_application;




    private assessment_Application assessment_application;




    private List<assessment_Controller> assessment_controllers;


    public assessment_Controllers(
    ) {
        this.assessment_controllers = new ArrayList<>();
    }

    public assessment_Controllers(
        ArrayList<assessment_Controller> assessment_controllers    ) {
        this.assessment_controllers = assessment_controllers;
    }


    public assessment_Controller getAssessment_controller() {
        return assessment_controller;
    }

    public void setAssessment_controller(assessment_Controller assessment_controller) {
        this.assessment_controller = assessment_controller;
    }
    public assessment_Application getAssessment_application() {
        return assessment_application;
    }

    public void setAssessment_application(assessment_Application assessment_application) {
        this.assessment_application = assessment_application;
    }
    public assessment_Application getAssessment_application() {
        return assessment_application;
    }

    public void setAssessment_application(assessment_Application assessment_application) {
        this.assessment_application = assessment_application;
    }
    public List<assessment_Controller> getAssessment_controllers() {
        return assessment_controllers;
    }

    public void addAssessment_controller(Assessment_controller assessment_controller) {
        this.assessment_controllers.add(assessment_controller);
    }

}