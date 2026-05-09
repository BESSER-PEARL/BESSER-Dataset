





import java.util.List;
import java.util.ArrayList;

public class AssistantMVC_Controller extends Observer {






    private AssistantMVC_Exam assistantmvc_exam;


    public AssistantMVC_Controller(
    ) {
        super(
        );
    }



    public AssistantMVC_Exam getAssistantmvc_exam() {
        return assistantmvc_exam;
    }

    public void setAssistantmvc_exam(AssistantMVC_Exam assistantmvc_exam) {
        this.assistantmvc_exam = assistantmvc_exam;
    }

}