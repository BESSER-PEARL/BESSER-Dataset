





import java.util.List;
import java.util.ArrayList;

public class AssistantMVC_Exam extends Observable {

    private String question;



    public AssistantMVC_Exam(
        String question    ) {
        super(
        );
        this.question = question;
    }


    public String getQuestion() {
        return question;
    }

    public void setQuestion(String question) {
        this.question = question;
    }


}