





import java.util.List;
import java.util.ArrayList;

public class Assessment  {

    private String Total_Score;
    private String Name;
    private String Type_of_Assessment;





    private Performance performance;




    private Survey survey;




    private Attendance attendance;


    public Assessment(
        String Total_Score,        String Name,        String Type_of_Assessment    ) {
        this.Total_Score = Total_Score;
        this.Name = Name;
        this.Type_of_Assessment = Type_of_Assessment;
    }


    public String getTotal_score() {
        return Total_Score;
    }

    public void setTotal_score(String Total_Score) {
        this.Total_Score = Total_Score;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getType_of_assessment() {
        return Type_of_Assessment;
    }

    public void setType_of_assessment(String Type_of_Assessment) {
        this.Type_of_Assessment = Type_of_Assessment;
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
    public Attendance getAttendance() {
        return attendance;
    }

    public void setAttendance(Attendance attendance) {
        this.attendance = attendance;
    }

}