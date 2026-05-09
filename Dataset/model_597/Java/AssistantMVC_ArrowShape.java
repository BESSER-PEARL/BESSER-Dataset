





import java.util.List;
import java.util.ArrayList;

public class AssistantMVC_ArrowShape  {

    private String value;
    private String question;



    public AssistantMVC_ArrowShape(
        String value,        String question    ) {
        this.value = value;
        this.question = question;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getQuestion() {
        return question;
    }

    public void setQuestion(String question) {
        this.question = question;
    }


}