





import java.util.List;
import java.util.ArrayList;

public class Assessment__Self_Assessment  {

    private String Name;
    private String Score;
    private String Question;





    private Assessment assessment;


    public Assessment__Self_Assessment(
        String Name,        String Score,        String Question    ) {
        this.Name = Name;
        this.Score = Score;
        this.Question = Question;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getScore() {
        return Score;
    }

    public void setScore(String Score) {
        this.Score = Score;
    }
    public String getQuestion() {
        return Question;
    }

    public void setQuestion(String Question) {
        this.Question = Question;
    }

    public Assessment getAssessment() {
        return assessment;
    }

    public void setAssessment(Assessment assessment) {
        this.assessment = assessment;
    }

}