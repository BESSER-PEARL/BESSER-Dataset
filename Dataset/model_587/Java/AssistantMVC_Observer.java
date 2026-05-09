





import java.util.List;
import java.util.ArrayList;

public class AssistantMVC_Observer  {






    private AssistantMVC_Controller assistantmvc_controller;




    private AssistantMVC_Observable assistantmvc_observable;


    public AssistantMVC_Observer(
    ) {
    }



    public AssistantMVC_Controller getAssistantmvc_controller() {
        return assistantmvc_controller;
    }

    public void setAssistantmvc_controller(AssistantMVC_Controller assistantmvc_controller) {
        this.assistantmvc_controller = assistantmvc_controller;
    }
    public AssistantMVC_Observable getAssistantmvc_observable() {
        return assistantmvc_observable;
    }

    public void setAssistantmvc_observable(AssistantMVC_Observable assistantmvc_observable) {
        this.assistantmvc_observable = assistantmvc_observable;
    }

}