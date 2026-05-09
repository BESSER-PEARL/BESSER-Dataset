





import java.util.List;
import java.util.ArrayList;

public class AssistantMVC_ExamItem  {

    private String value;
    private boolean optional;
    private String question;



    public AssistantMVC_ExamItem(
        String value,        boolean optional,        String question    ) {
        this.value = value;
        this.optional = optional;
        this.question = question;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public boolean getOptional() {
        return optional;
    }

    public void setOptional(boolean optional) {
        this.optional = optional;
    }
    public String getQuestion() {
        return question;
    }

    public void setQuestion(String question) {
        this.question = question;
    }


}