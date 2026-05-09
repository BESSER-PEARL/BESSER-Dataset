





import java.util.List;
import java.util.ArrayList;

public class mvc_Action extends Annotable {

    private String name;





    private mvc_Event mvc_event;




    private mvc_Event mvc_event;




    private mvc_Controller mvc_controller;




    private List<mvc_Event> mvc_events;




    private mvc_EventAction mvc_eventaction;


    public mvc_Action(
        String name    ) {
        super(
        );
        this.name = name;
        this.mvc_events = new ArrayList<>();
    }

    public mvc_Action(
        String name        ArrayList<mvc_Event> mvc_events    ) {
        this.name = name;
        this.mvc_events = mvc_events;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public mvc_Event getMvc_event() {
        return mvc_event;
    }

    public void setMvc_event(mvc_Event mvc_event) {
        this.mvc_event = mvc_event;
    }
    public mvc_Event getMvc_event() {
        return mvc_event;
    }

    public void setMvc_event(mvc_Event mvc_event) {
        this.mvc_event = mvc_event;
    }
    public mvc_Controller getMvc_controller() {
        return mvc_controller;
    }

    public void setMvc_controller(mvc_Controller mvc_controller) {
        this.mvc_controller = mvc_controller;
    }
    public List<mvc_Event> getMvc_events() {
        return mvc_events;
    }

    public void addMvc_event(Mvc_event mvc_event) {
        this.mvc_events.add(mvc_event);
    }
    public mvc_EventAction getMvc_eventaction() {
        return mvc_eventaction;
    }

    public void setMvc_eventaction(mvc_EventAction mvc_eventaction) {
        this.mvc_eventaction = mvc_eventaction;
    }

}