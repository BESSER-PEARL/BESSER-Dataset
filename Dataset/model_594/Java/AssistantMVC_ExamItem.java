





import java.util.List;
import java.util.ArrayList;

public class AssistantMVC_ExamItem extends Observable {

    private String value;
    private boolean optional;





    private AssistantMVC_Exam assistantmvc_exam;


    public AssistantMVC_ExamItem(
        String value,        boolean optional    ) {
        super(
        );
        this.value = value;
        this.optional = optional;
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

    public AssistantMVC_Exam getAssistantmvc_exam() {
        return assistantmvc_exam;
    }

    public void setAssistantmvc_exam(AssistantMVC_Exam assistantmvc_exam) {
        this.assistantmvc_exam = assistantmvc_exam;
    }

}