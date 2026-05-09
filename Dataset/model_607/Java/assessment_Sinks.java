





import java.util.List;
import java.util.ArrayList;

public class assessment_Sinks  {






    private assessment_Application assessment_application;




    private assessment_Application assessment_application;




    private List<assessment_Sink> assessment_sinks;




    private assessment_Sink assessment_sink;


    public assessment_Sinks(
    ) {
        this.assessment_sinks = new ArrayList<>();
    }

    public assessment_Sinks(
        ArrayList<assessment_Sink> assessment_sinks    ) {
        this.assessment_sinks = assessment_sinks;
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
    public List<assessment_Sink> getAssessment_sinks() {
        return assessment_sinks;
    }

    public void addAssessment_sink(Assessment_sink assessment_sink) {
        this.assessment_sinks.add(assessment_sink);
    }
    public assessment_Sink getAssessment_sink() {
        return assessment_sink;
    }

    public void setAssessment_sink(assessment_Sink assessment_sink) {
        this.assessment_sink = assessment_sink;
    }

}