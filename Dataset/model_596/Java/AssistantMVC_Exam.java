





import java.util.List;
import java.util.ArrayList;

public class AssistantMVC_Exam  {

    private String question;





    private List<AssistantMVC_ExamItem> assistantmvc_examitems;




    private List<AssistantMVC_View> assistantmvc_views;




    private List<AssistantMVC_Controller> assistantmvc_controllers;


    public AssistantMVC_Exam(
        String question    ) {
        this.question = question;
        this.assistantmvc_examitems = new ArrayList<>();
        this.assistantmvc_views = new ArrayList<>();
        this.assistantmvc_controllers = new ArrayList<>();
    }

    public AssistantMVC_Exam(
        String question        ArrayList<AssistantMVC_ExamItem> assistantmvc_examitems,        ArrayList<AssistantMVC_View> assistantmvc_views,        ArrayList<AssistantMVC_Controller> assistantmvc_controllers    ) {
        this.question = question;
        this.assistantmvc_examitems = assistantmvc_examitems;
        this.assistantmvc_views = assistantmvc_views;
        this.assistantmvc_controllers = assistantmvc_controllers;
    }

    public String getQuestion() {
        return question;
    }

    public void setQuestion(String question) {
        this.question = question;
    }

    public List<AssistantMVC_ExamItem> getAssistantmvc_examitems() {
        return assistantmvc_examitems;
    }

    public void addAssistantmvc_examitem(Assistantmvc_examitem assistantmvc_examitem) {
        this.assistantmvc_examitems.add(assistantmvc_examitem);
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