





import java.util.List;
import java.util.ArrayList;

public class assessment_Views  {






    private assessment_Application assessment_application;




    private assessment_Application assessment_application;




    private List<assessment_View> assessment_views;




    private assessment_View assessment_view;


    public assessment_Views(
    ) {
        this.assessment_views = new ArrayList<>();
    }

    public assessment_Views(
        ArrayList<assessment_View> assessment_views    ) {
        this.assessment_views = assessment_views;
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
    public List<assessment_View> getAssessment_views() {
        return assessment_views;
    }

    public void addAssessment_view(Assessment_view assessment_view) {
        this.assessment_views.add(assessment_view);
    }
    public assessment_View getAssessment_view() {
        return assessment_view;
    }

    public void setAssessment_view(assessment_View assessment_view) {
        this.assessment_view = assessment_view;
    }

}