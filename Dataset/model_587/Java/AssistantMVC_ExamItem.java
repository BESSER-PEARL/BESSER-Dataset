





import java.util.List;
import java.util.ArrayList;

public class AssistantMVC_ExamItem extends Observable {

    private String question;





    private AssistantMVC_Exam assistantmvc_exam;


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

    public AssistantMVC_Exam getAssistantmvc_exam() {
        return assistantmvc_exam;
    }

    public void setAssistantmvc_exam(AssistantMVC_Exam assistantmvc_exam) {
        this.assistantmvc_exam = assistantmvc_exam;
    }

}