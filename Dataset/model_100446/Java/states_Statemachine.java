





import java.util.List;
import java.util.ArrayList;

public class states_Statemachine  {

    private String name;
    private boolean initial;
    private int value;





    private List<states_Event> states_events;




    private List<states_State> states_states;




    private states_Module states_module;


    public states_Statemachine(
        String name,        boolean initial,        int value    ) {
        this.name = name;
        this.initial = initial;
        this.value = value;
        this.states_events = new ArrayList<>();
        this.states_states = new ArrayList<>();
    }

    public states_Statemachine(
        String name,        boolean initial,        int value        ArrayList<states_Event> states_events,        ArrayList<states_State> states_states    ) {
        this.name = name;
        this.initial = initial;
        this.value = value;
        this.states_events = states_events;
        this.states_states = states_states;
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
    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }

    public List<states_Event> getStates_events() {
        return states_events;
    }

    public void addStates_event(States_event states_event) {
        this.states_events.add(states_event);
    }
    public List<states_State> getStates_states() {
        return states_states;
    }

    public void addStates_state(States_state states_state) {
        this.states_states.add(states_state);
    }
    public states_Module getStates_module() {
        return states_module;
    }

    public void setStates_module(states_Module states_module) {
        this.states_module = states_module;
    }

}