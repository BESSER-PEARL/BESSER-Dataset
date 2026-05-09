





import java.util.List;
import java.util.ArrayList;

public class AssistantMVC_OpenView extends ExamView {

    private String question;



    public AssistantMVC_OpenView(
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