





import java.util.List;
import java.util.ArrayList;

public class Assessment  {

    private String Type_of_Assessment;
    private String Name;
    private String Total_Score;





    private Attendance attendance;




    private Performance performance;




    private Survey survey;


    public Assessment(
        String Type_of_Assessment,        String Name,        String Total_Score    ) {
        this.Type_of_Assessment = Type_of_Assessment;
        this.Name = Name;
        this.Total_Score = Total_Score;
    }


    public String getType_of_assessment() {
        return Type_of_Assessment;
    }

    public void setType_of_assessment(String Type_of_Assessment) {
        this.Type_of_Assessment = Type_of_Assessment;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getTotal_score() {
        return Total_Score;
    }

    public void setTotal_score(String Total_Score) {
        this.Total_Score = Total_Score;
    }

    public Attendance getAttendance() {
        return attendance;
    }

    public void setAttendance(Attendance attendance) {
        this.attendance = attendance;
    }
    public Performance getPerformance() {
        return performance;
    }

    public void setPerformance(Performance performance) {
        this.performance = performance;
    }
    public Survey getSurvey() {
        return survey;
    }

    public void setSurvey(Survey survey) {
        this.survey = survey;
    }

}