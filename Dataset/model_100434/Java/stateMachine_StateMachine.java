





import java.util.List;
import java.util.ArrayList;

public class stateMachine_StateMachine  {

    private String name;
    private String package;





    private List<stateMachine_State> statemachine_states;




    private List<stateMachine_Event> statemachine_events;




    private List<stateMachine_DocumentField> statemachine_documentfields;




    private stateMachine_State statemachine_state;




    private List<stateMachine_Role> statemachine_roles;


    public stateMachine_StateMachine(
        String name,        String package    ) {
        this.name = name;
        this.package = package;
        this.statemachine_states = new ArrayList<>();
        this.statemachine_events = new ArrayList<>();
        this.statemachine_documentfields = new ArrayList<>();
        this.statemachine_roles = new ArrayList<>();
    }

    public stateMachine_StateMachine(
        String name,        String package        ArrayList<stateMachine_State> statemachine_states,        ArrayList<stateMachine_Event> statemachine_events,        ArrayList<stateMachine_DocumentField> statemachine_documentfields,        ArrayList<stateMachine_Role> statemachine_roles    ) {
        this.name = name;
        this.package = package;
        this.statemachine_states = statemachine_states;
        this.statemachine_events = statemachine_events;
        this.statemachine_documentfields = statemachine_documentfields;
        this.statemachine_roles = statemachine_roles;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPackage() {
        return package;
    }

    public void setPackage(String package) {
        this.package = package;
    }

    public List<stateMachine_State> getStatemachine_states() {
        return statemachine_states;
    }

    public void addStatemachine_state(Statemachine_state statemachine_state) {
        this.statemachine_states.add(statemachine_state);
    }
    public List<stateMachine_Event> getStatemachine_events() {
        return statemachine_events;
    }

    public void addStatemachine_event(Statemachine_event statemachine_event) {
        this.statemachine_events.add(statemachine_event);
    }
    public List<stateMachine_DocumentField> getStatemachine_documentfields() {
        return statemachine_documentfields;
    }

    public void addStatemachine_documentfield(Statemachine_documentfield statemachine_documentfield) {
        this.statemachine_documentfields.add(statemachine_documentfield);
    }
    public stateMachine_State getStatemachine_state() {
        return statemachine_state;
    }

    public void setStatemachine_state(stateMachine_State statemachine_state) {
        this.statemachine_state = statemachine_state;
    }
    public List<stateMachine_Role> getStatemachine_roles() {
        return statemachine_roles;
    }

    public void addStatemachine_role(Statemachine_role statemachine_role) {
        this.statemachine_roles.add(statemachine_role);
    }

}