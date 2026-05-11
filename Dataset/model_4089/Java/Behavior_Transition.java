





import java.util.List;
import java.util.ArrayList;

public class Behavior_Transition extends NamedElement {






    private Behavior_State behavior_state;




    private Behavior_Event behavior_event;




    private List<Behavior_State> behavior_states;




    private Behavior_Component behavior_component;




    private Behavior_Event behavior_event;




    private Behavior_State behavior_state;


    public Behavior_Transition(
    ) {
        super(
        );
        this.behavior_states = new ArrayList<>();
    }

    public Behavior_Transition(
        ArrayList<Behavior_State> behavior_states    ) {
        this.behavior_states = behavior_states;
    }


    public Behavior_State getBehavior_state() {
        return behavior_state;
    }

    public void setBehavior_state(Behavior_State behavior_state) {
        this.behavior_state = behavior_state;
    }
    public Behavior_Event getBehavior_event() {
        return behavior_event;
    }

    public void setBehavior_event(Behavior_Event behavior_event) {
        this.behavior_event = behavior_event;
    }
    public List<Behavior_State> getBehavior_states() {
        return behavior_states;
    }

    public void addBehavior_state(Behavior_state behavior_state) {
        this.behavior_states.add(behavior_state);
    }
    public Behavior_Component getBehavior_component() {
        return behavior_component;
    }

    public void setBehavior_component(Behavior_Component behavior_component) {
        this.behavior_component = behavior_component;
    }
    public Behavior_Event getBehavior_event() {
        return behavior_event;
    }

    public void setBehavior_event(Behavior_Event behavior_event) {
        this.behavior_event = behavior_event;
    }
    public Behavior_State getBehavior_state() {
        return behavior_state;
    }

    public void setBehavior_state(Behavior_State behavior_state) {
        this.behavior_state = behavior_state;
    }

}