





import java.util.List;
import java.util.ArrayList;

public class AssistantMVC_ExamItem  {

    private boolean optional;





    private AssistantMVC_Exam assistantmvc_exam;


    public AssistantMVC_ExamItem(
        boolean optional    ) {
        this.optional = optional;
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