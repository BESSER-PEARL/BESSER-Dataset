





import java.util.List;
import java.util.ArrayList;

public class Survey  {

    private String Score;
    private String Question;
    private String Name;



    public Survey(
        String Score,        String Question,        String Name    ) {
        this.Score = Score;
        this.Question = Question;
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
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }


}