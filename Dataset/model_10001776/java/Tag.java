





import java.util.List;
import java.util.ArrayList;

public class Tag  {






    private List<Question> questions;


    public Tag(
    ) {
        this.questions = new ArrayList<>();
    }

    public Tag(
        ArrayList<Question> questions    ) {
        this.questions = questions;
    }


    public List<Question> getQuestions() {
        return questions;
    }

    public void addQuestion(Question question) {
        this.questions.add(question);
    }

}