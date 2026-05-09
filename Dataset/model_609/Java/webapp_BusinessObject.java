





import java.util.List;
import java.util.ArrayList;

public class webapp_BusinessObject  {

    private String package;
    private String name;





    private List<webapp_Action> webapp_actions;




    private webapp_Action webapp_action;




    private List<webapp_BusinessObject> webapp_businessobjects;




    private webapp_Model webapp_model;




    private webapp_Model webapp_model;


    public webapp_BusinessObject(
        String package,        String name    ) {
        this.package = package;
        this.name = name;
        this.webapp_actions = new ArrayList<>();
        this.webapp_businessobjects = new ArrayList<>();
    }

    public webapp_BusinessObject(
        String package,        String name        ArrayList<webapp_Action> webapp_actions,        ArrayList<webapp_BusinessObject> webapp_businessobjects    ) {
        this.package = package;
        this.name = name;
        this.webapp_actions = webapp_actions;
        this.webapp_businessobjects = webapp_businessobjects;
    }

    public String getPackage() {
        return package;
    }

    public void setPackage(String package) {
        this.package = package;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<webapp_Action> getWebapp_actions() {
        return webapp_actions;
    }

    public void addWebapp_action(Webapp_action webapp_action) {
        this.webapp_actions.add(webapp_action);
    }
    public webapp_Action getWebapp_action() {
        return webapp_action;
    }

    public void setWebapp_action(webapp_Action webapp_action) {
        this.webapp_action = webapp_action;
    }
    public List<webapp_BusinessObject> getWebapp_businessobjects() {
        return webapp_businessobjects;
    }

    public void addWebapp_businessobject(Webapp_businessobject webapp_businessobject) {
        this.webapp_businessobjects.add(webapp_businessobject);
    }
    public webapp_Model getWebapp_model() {
        return webapp_model;
    }

    public void setWebapp_model(webapp_Model webapp_model) {
        this.webapp_model = webapp_model;
    }
    public webapp_Model getWebapp_model() {
        return webapp_model;
    }

    public void setWebapp_model(webapp_Model webapp_model) {
        this.webapp_model = webapp_model;
    }

}