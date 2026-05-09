





import java.util.List;
import java.util.ArrayList;

public class mvc_Controller extends Annotable {

    private String name;





    private List<mvc_EventAction> mvc_eventactions;




    private List<mvc_ControllerView> mvc_controllerviews;




    private mvc_Component mvc_component;


    public mvc_Controller(
        String name    ) {
        super(
        );
        this.name = name;
        this.mvc_eventactions = new ArrayList<>();
        this.mvc_controllerviews = new ArrayList<>();
    }

    public mvc_Controller(
        String name        ArrayList<mvc_EventAction> mvc_eventactions,        ArrayList<mvc_ControllerView> mvc_controllerviews    ) {
        this.name = name;
        this.mvc_eventactions = mvc_eventactions;
        this.mvc_controllerviews = mvc_controllerviews;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<mvc_EventAction> getMvc_eventactions() {
        return mvc_eventactions;
    }

    public void addMvc_eventaction(Mvc_eventaction mvc_eventaction) {
        this.mvc_eventactions.add(mvc_eventaction);
    }
    public List<mvc_ControllerView> getMvc_controllerviews() {
        return mvc_controllerviews;
    }

    public void addMvc_controllerview(Mvc_controllerview mvc_controllerview) {
        this.mvc_controllerviews.add(mvc_controllerview);
    }
    public mvc_Component getMvc_component() {
        return mvc_component;
    }

    public void setMvc_component(mvc_Component mvc_component) {
        this.mvc_component = mvc_component;
    }

}