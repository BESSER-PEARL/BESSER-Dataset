





import java.util.List;
import java.util.ArrayList;

public class states_Statemachine  {

    private int value;
    private String name;
    private boolean initial;





    private states_Module states_module;




    private List<states_Event> states_events;


    public states_Statemachine(
        int value,        String name,        boolean initial    ) {
        this.value = value;
        this.name = name;
        this.initial = initial;
        this.states_events = new ArrayList<>();
    }

    public states_Statemachine(
        int value,        String name,        boolean initial        ArrayList<states_Event> states_events    ) {
        this.value = value;
        this.name = name;
        this.initial = initial;
        this.states_events = states_events;
    }

    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getInitial() {
        return initial;
    }

    public void setInitial(boolean initial) {
        this.initial = initial;
    }

    public states_Module getStates_module() {
        return states_module;
    }

    public void setStates_module(states_Module states_module) {
        this.states_module = states_module;
    }
    public List<states_Event> getStates_events() {
        return states_events;
    }

    public void addStates_event(States_event states_event) {
        this.states_events.add(states_event);
    }

}