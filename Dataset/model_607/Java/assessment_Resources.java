





import java.util.List;
import java.util.ArrayList;

public class assessment_Resources  {






    private assessment_Application assessment_application;




    private List<assessment_Resource> assessment_resources;




    private assessment_Resource assessment_resource;




    private assessment_Application assessment_application;


    public assessment_Resources(
    ) {
        this.assessment_resources = new ArrayList<>();
    }

    public assessment_Resources(
        ArrayList<assessment_Resource> assessment_resources    ) {
        this.assessment_resources = assessment_resources;
    }


    public assessment_Application getAssessment_application() {
        return assessment_application;
    }

    public void setAssessment_application(assessment_Application assessment_application) {
        this.assessment_application = assessment_application;
    }
    public List<assessment_Resource> getAssessment_resources() {
        return assessment_resources;
    }

    public void addAssessment_resource(Assessment_resource assessment_resource) {
        this.assessment_resources.add(assessment_resource);
    }
    public assessment_Resource getAssessment_resource() {
        return assessment_resource;
    }

    public void setAssessment_resource(assessment_Resource assessment_resource) {
        this.assessment_resource = assessment_resource;
    }
    public assessment_Application getAssessment_application() {
        return assessment_application;
    }

    public void setAssessment_application(assessment_Application assessment_application) {
        this.assessment_application = assessment_application;
    }

}