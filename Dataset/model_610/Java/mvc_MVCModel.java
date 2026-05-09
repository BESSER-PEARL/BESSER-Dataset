





import java.util.List;
import java.util.ArrayList;

public class mvc_MVCModel extends Annotable {

    private String version;
    private String name;





    private List<mvc_Event> mvc_events;




    private List<mvc_Component> mvc_components;




    private List<mvc_Controller> mvc_controllers;




    private List<mvc_Model> mvc_models;


    public mvc_MVCModel(
        String version,        String name    ) {
        super(
        );
        this.version = version;
        this.name = name;
        this.mvc_events = new ArrayList<>();
        this.mvc_components = new ArrayList<>();
        this.mvc_controllers = new ArrayList<>();
        this.mvc_models = new ArrayList<>();
    }

    public mvc_MVCModel(
        String version,        String name        ArrayList<mvc_Event> mvc_events,        ArrayList<mvc_Component> mvc_components,        ArrayList<mvc_Controller> mvc_controllers,        ArrayList<mvc_Model> mvc_models    ) {
        this.version = version;
        this.name = name;
        this.mvc_events = mvc_events;
        this.mvc_components = mvc_components;
        this.mvc_controllers = mvc_controllers;
        this.mvc_models = mvc_models;
    }

    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<mvc_Event> getMvc_events() {
        return mvc_events;
    }

    public void addMvc_event(Mvc_event mvc_event) {
        this.mvc_events.add(mvc_event);
    }
    public List<mvc_Component> getMvc_components() {
        return mvc_components;
    }

    public void addMvc_component(Mvc_component mvc_component) {
        this.mvc_components.add(mvc_component);
    }
    public List<mvc_Controller> getMvc_controllers() {
        return mvc_controllers;
    }

    public void addMvc_controller(Mvc_controller mvc_controller) {
        this.mvc_controllers.add(mvc_controller);
    }
    public List<mvc_Model> getMvc_models() {
        return mvc_models;
    }

    public void addMvc_model(Mvc_model mvc_model) {
        this.mvc_models.add(mvc_model);
    }

}