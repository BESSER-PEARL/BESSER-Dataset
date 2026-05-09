





import java.util.List;
import java.util.ArrayList;

public class rosmodel_State  {

    private String name;





    private List<rosmodel_Transition> rosmodel_transitions;




    private rosmodel_Action rosmodel_action;




    private rosmodel_Action rosmodel_action;




    private List<rosmodel_Event> rosmodel_events;




    private rosmodel_State rosmodel_state;




    private rosmodel_Transition rosmodel_transition;




    private rosmodel_Transition rosmodel_transition;




    private rosmodel_Node rosmodel_node;




    private List<rosmodel_Action> rosmodel_actions;


    public rosmodel_State(
        String name    ) {
        this.name = name;
        this.rosmodel_transitions = new ArrayList<>();
        this.rosmodel_events = new ArrayList<>();
        this.rosmodel_actions = new ArrayList<>();
    }

    public rosmodel_State(
        String name        ArrayList<rosmodel_Transition> rosmodel_transitions,        ArrayList<rosmodel_Event> rosmodel_events,        ArrayList<rosmodel_Action> rosmodel_actions    ) {
        this.name = name;
        this.rosmodel_transitions = rosmodel_transitions;
        this.rosmodel_events = rosmodel_events;
        this.rosmodel_actions = rosmodel_actions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<rosmodel_Transition> getRosmodel_transitions() {
        return rosmodel_transitions;
    }

    public void addRosmodel_transition(Rosmodel_transition rosmodel_transition) {
        this.rosmodel_transitions.add(rosmodel_transition);
    }
    public rosmodel_Action getRosmodel_action() {
        return rosmodel_action;
    }

    public void setRosmodel_action(rosmodel_Action rosmodel_action) {
        this.rosmodel_action = rosmodel_action;
    }
    public rosmodel_Action getRosmodel_action() {
        return rosmodel_action;
    }

    public void setRosmodel_action(rosmodel_Action rosmodel_action) {
        this.rosmodel_action = rosmodel_action;
    }
    public List<rosmodel_Event> getRosmodel_events() {
        return rosmodel_events;
    }

    public void addRosmodel_event(Rosmodel_event rosmodel_event) {
        this.rosmodel_events.add(rosmodel_event);
    }
    public rosmodel_State getRosmodel_state() {
        return rosmodel_state;
    }

    public void setRosmodel_state(rosmodel_State rosmodel_state) {
        this.rosmodel_state = rosmodel_state;
    }
    public rosmodel_Transition getRosmodel_transition() {
        return rosmodel_transition;
    }

    public void setRosmodel_transition(rosmodel_Transition rosmodel_transition) {
        this.rosmodel_transition = rosmodel_transition;
    }
    public rosmodel_Transition getRosmodel_transition() {
        return rosmodel_transition;
    }

    public void setRosmodel_transition(rosmodel_Transition rosmodel_transition) {
        this.rosmodel_transition = rosmodel_transition;
    }
    public rosmodel_Node getRosmodel_node() {
        return rosmodel_node;
    }

    public void setRosmodel_node(rosmodel_Node rosmodel_node) {
        this.rosmodel_node = rosmodel_node;
    }
    public List<rosmodel_Action> getRosmodel_actions() {
        return rosmodel_actions;
    }

    public void addRosmodel_action(Rosmodel_action rosmodel_action) {
        this.rosmodel_actions.add(rosmodel_action);
    }

}