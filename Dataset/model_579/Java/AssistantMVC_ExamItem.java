





import java.util.List;
import java.util.ArrayList;

public class AssistantMVC_ExamItem extends Observable {

    private String question;



    public AssistantMVC_ExamItem(
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