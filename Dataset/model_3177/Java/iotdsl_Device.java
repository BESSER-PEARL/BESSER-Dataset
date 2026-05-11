





import java.util.List;
import java.util.ArrayList;

public class iotdsl_Device  {

    private String name;





    private iotdsl_Attribute iotdsl_attribute;




    private List<iotdsl_Transition> iotdsl_transitions;




    private iotdsl_Iot iotdsl_iot;




    private iotdsl_Device iotdsl_device;




    private List<iotdsl_State> iotdsl_states;




    private List<iotdsl_Event> iotdsl_events;


    public iotdsl_Device(
        String name    ) {
        this.name = name;
        this.iotdsl_transitions = new ArrayList<>();
        this.iotdsl_states = new ArrayList<>();
        this.iotdsl_events = new ArrayList<>();
    }

    public iotdsl_Device(
        String name        ArrayList<iotdsl_Transition> iotdsl_transitions,        ArrayList<iotdsl_State> iotdsl_states,        ArrayList<iotdsl_Event> iotdsl_events    ) {
        this.name = name;
        this.iotdsl_transitions = iotdsl_transitions;
        this.iotdsl_states = iotdsl_states;
        this.iotdsl_events = iotdsl_events;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public iotdsl_Attribute getIotdsl_attribute() {
        return iotdsl_attribute;
    }

    public void setIotdsl_attribute(iotdsl_Attribute iotdsl_attribute) {
        this.iotdsl_attribute = iotdsl_attribute;
    }
    public List<iotdsl_Transition> getIotdsl_transitions() {
        return iotdsl_transitions;
    }

    public void addIotdsl_transition(Iotdsl_transition iotdsl_transition) {
        this.iotdsl_transitions.add(iotdsl_transition);
    }
    public iotdsl_Iot getIotdsl_iot() {
        return iotdsl_iot;
    }

    public void setIotdsl_iot(iotdsl_Iot iotdsl_iot) {
        this.iotdsl_iot = iotdsl_iot;
    }
    public iotdsl_Device getIotdsl_device() {
        return iotdsl_device;
    }

    public void setIotdsl_device(iotdsl_Device iotdsl_device) {
        this.iotdsl_device = iotdsl_device;
    }
    public List<iotdsl_State> getIotdsl_states() {
        return iotdsl_states;
    }

    public void addIotdsl_state(Iotdsl_state iotdsl_state) {
        this.iotdsl_states.add(iotdsl_state);
    }
    public List<iotdsl_Event> getIotdsl_events() {
        return iotdsl_events;
    }

    public void addIotdsl_event(Iotdsl_event iotdsl_event) {
        this.iotdsl_events.add(iotdsl_event);
    }

}