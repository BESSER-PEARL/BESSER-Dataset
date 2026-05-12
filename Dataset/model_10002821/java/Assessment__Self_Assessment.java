





import java.util.List;
import java.util.ArrayList;

public class Assessment__Self_Assessment  {

    private String Score;
    private String Name;
    private String Question;





    private Assessment assessment;


    public Assessment__Self_Assessment(
        String Score,        String Name,        String Question    ) {
        this.Score = Score;
        this.Name = Name;
        this.Question = Question;
    }


    public String getScore() {
        return Score;
    }

    public void setScore(String Score) {
        this.Score = Score;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
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