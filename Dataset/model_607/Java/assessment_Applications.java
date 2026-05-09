





import java.util.List;
import java.util.ArrayList;

public class assessment_Applications  {






    private assessment_Assessment assessment_assessment;




    private assessment_Assessment assessment_assessment;




    private List<assessment_Application> assessment_applications;




    private assessment_Application assessment_application;


    public assessment_Applications(
    ) {
        this.assessment_applications = new ArrayList<>();
    }

    public assessment_Applications(
        ArrayList<assessment_Application> assessment_applications    ) {
        this.assessment_applications = assessment_applications;
    }


    public assessment_Assessment getAssessment_assessment() {
        return assessment_assessment;
    }

    public void setAssessment_assessment(assessment_Assessment assessment_assessment) {
        this.assessment_assessment = assessment_assessment;
    }
    public assessment_Assessment getAssessment_assessment() {
        return assessment_assessment;
    }

    public void setAssessment_assessment(assessment_Assessment assessment_assessment) {
        this.assessment_assessment = assessment_assessment;
    }
    public List<assessment_Application> getAssessment_applications() {
        return assessment_applications;
    }

    public void addAssessment_application(Assessment_application assessment_application) {
        this.assessment_applications.add(assessment_application);
    }
    public assessment_Application getAssessment_application() {
        return assessment_application;
    }

    public void setAssessment_application(assessment_Application assessment_application) {
        this.assessment_application = assessment_application;
    }

}