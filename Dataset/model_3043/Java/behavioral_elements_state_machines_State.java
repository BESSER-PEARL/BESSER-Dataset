





import java.util.List;
import java.util.ArrayList;

public class behavioral_elements_state_machines_State extends StateVertex {






    private Action action;




    private Action action;




    private List<Event> events;




    private Action action;




    private List<Transition> transitions;


    public behavioral_elements_state_machines_State(
    ) {
        super(
        );
        this.events = new ArrayList<>();
        this.transitions = new ArrayList<>();
    }

    public behavioral_elements_state_machines_State(
        ArrayList<Event> events,        ArrayList<Transition> transitions    ) {
        this.events = events;
        this.transitions = transitions;
    }


    public Action getAction() {
        return action;
    }

    public void setAction(Action action) {
        this.action = action;
    }
    public Action getAction() {
        return action;
    }

    public void setAction(Action action) {
        this.action = action;
    }
    public List<Event> getEvents() {
        return events;
    }

    public void addEvent(Event event) {
        this.events.add(event);
    }
    public Action getAction() {
        return action;
    }

    public void setAction(Action action) {
        this.action = action;
    }
    public List<Transition> getTransitions() {
        return transitions;
    }

    public void addTransition(Transition transition) {
        this.transitions.add(transition);
    }

}