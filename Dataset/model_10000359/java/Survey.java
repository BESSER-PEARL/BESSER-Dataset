





import java.util.List;
import java.util.ArrayList;

public class Survey  {

    private String Score;
    private String Name;
    private String Question;



    public Survey(
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


}