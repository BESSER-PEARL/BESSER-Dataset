





import java.util.List;
import java.util.ArrayList;

public class WebApp_ActionMapping  {






    private WebApp_Action webapp_action;




    private List<WebApp_Controller> webapp_controllers;


    public WebApp_ActionMapping(
    ) {
        this.webapp_controllers = new ArrayList<>();
    }

    public WebApp_ActionMapping(
        ArrayList<WebApp_Controller> webapp_controllers    ) {
        this.webapp_controllers = webapp_controllers;
    }


    public WebApp_Action getWebapp_action() {
        return webapp_action;
    }

    public void setWebapp_action(WebApp_Action webapp_action) {
        this.webapp_action = webapp_action;
    }
    public List<WebApp_Controller> getWebapp_controllers() {
        return webapp_controllers;
    }

    public void addWebapp_controller(Webapp_controller webapp_controller) {
        this.webapp_controllers.add(webapp_controller);
    }

}