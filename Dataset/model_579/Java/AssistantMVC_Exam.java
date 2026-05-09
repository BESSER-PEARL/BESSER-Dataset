





import java.util.List;
import java.util.ArrayList;

public class AssistantMVC_Exam extends Observable {






    private List<AssistantMVC_ExamItem> assistantmvc_examitems;


    public AssistantMVC_Exam(
    ) {
        super(
        );
        this.assistantmvc_examitems = new ArrayList<>();
    }

    public AssistantMVC_Exam(
        ArrayList<AssistantMVC_ExamItem> assistantmvc_examitems    ) {
        this.assistantmvc_examitems = assistantmvc_examitems;
    }


    public List<AssistantMVC_ExamItem> getAssistantmvc_examitems() {
        return assistantmvc_examitems;
    }

    public void addAssistantmvc_examitem(Assistantmvc_examitem assistantmvc_examitem) {
        this.assistantmvc_examitems.add(assistantmvc_examitem);
    }

}