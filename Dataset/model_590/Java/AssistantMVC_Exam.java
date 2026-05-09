





import java.util.List;
import java.util.ArrayList;

public class AssistantMVC_Exam extends Observable {






    private List<AssistantMVC_View> assistantmvc_views;


    public AssistantMVC_Exam(
    ) {
        super(
        );
        this.assistantmvc_views = new ArrayList<>();
    }

    public AssistantMVC_Exam(
        ArrayList<AssistantMVC_View> assistantmvc_views    ) {
        this.assistantmvc_views = assistantmvc_views;
    }


    public List<AssistantMVC_View> getAssistantmvc_views() {
        return assistantmvc_views;
    }

    public void addAssistantmvc_view(Assistantmvc_view assistantmvc_view) {
        this.assistantmvc_views.add(assistantmvc_view);
    }

}