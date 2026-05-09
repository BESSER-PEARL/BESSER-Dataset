





import java.util.List;
import java.util.ArrayList;

public class webapp_Controller  {






    private webapp_WebApp webapp_webapp;




    private List<webapp_Action> webapp_actions;




    private List<webapp_Validator> webapp_validators;


    public webapp_Controller(
    ) {
        this.webapp_actions = new ArrayList<>();
        this.webapp_validators = new ArrayList<>();
    }

    public webapp_Controller(
        ArrayList<webapp_Action> webapp_actions,        ArrayList<webapp_Validator> webapp_validators    ) {
        this.webapp_actions = webapp_actions;
        this.webapp_validators = webapp_validators;
    }


    public webapp_WebApp getWebapp_webapp() {
        return webapp_webapp;
    }

    public void setWebapp_webapp(webapp_WebApp webapp_webapp) {
        this.webapp_webapp = webapp_webapp;
    }
    public List<webapp_Action> getWebapp_actions() {
        return webapp_actions;
    }

    public void addWebapp_action(Webapp_action webapp_action) {
        this.webapp_actions.add(webapp_action);
    }
    public List<webapp_Validator> getWebapp_validators() {
        return webapp_validators;
    }

    public void addWebapp_validator(Webapp_validator webapp_validator) {
        this.webapp_validators.add(webapp_validator);
    }

}