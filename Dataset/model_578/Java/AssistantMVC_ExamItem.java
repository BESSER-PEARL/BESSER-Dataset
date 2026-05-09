





import java.util.List;
import java.util.ArrayList;

public class AssistantMVC_ExamItem extends Observable {

    private boolean optional;
    private String question;
    private String value;





    private AssistantMVC_Exam assistantmvc_exam;


    public AssistantMVC_ExamItem(
        boolean optional,        String question,        String value    ) {
        super(
        );
        this.optional = optional;
        this.question = question;
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
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public AssistantMVC_Exam getAssistantmvc_exam() {
        return assistantmvc_exam;
    }

    public void setAssistantmvc_exam(AssistantMVC_Exam assistantmvc_exam) {
        this.assistantmvc_exam = assistantmvc_exam;
    }

}