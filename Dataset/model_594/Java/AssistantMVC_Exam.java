





import java.util.List;
import java.util.ArrayList;

public class AssistantMVC_Exam extends Observable {






    private List<AssistantMVC_View> assistantmvc_views;




    private List<AssistantMVC_Controller> assistantmvc_controllers;


    public AssistantMVC_Exam(
    ) {
        super(
        );
        this.assistantmvc_views = new ArrayList<>();
        this.assistantmvc_controllers = new ArrayList<>();
    }

    public AssistantMVC_Exam(
        ArrayList<AssistantMVC_View> assistantmvc_views,        ArrayList<AssistantMVC_Controller> assistantmvc_controllers    ) {
        this.assistantmvc_views = assistantmvc_views;
        this.assistantmvc_controllers = assistantmvc_controllers;
    }


    public List<AssistantMVC_View> getAssistantmvc_views() {
        return assistantmvc_views;
    }

    public void addAssistantmvc_view(Assistantmvc_view assistantmvc_view) {
        this.assistantmvc_views.add(assistantmvc_view);
    }
    public List<AssistantMVC_Controller> getAssistantmvc_controllers() {
        return assistantmvc_controllers;
    }

    public void addAssistantmvc_controller(Assistantmvc_controller assistantmvc_controller) {
        this.assistantmvc_controllers.add(assistantmvc_controller);
    }

}