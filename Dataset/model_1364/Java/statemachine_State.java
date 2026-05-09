





import java.util.List;
import java.util.ArrayList;

public class statemachine_State extends Declaration {

    private int id;
    private String label;





    private List<statemachine_State> statemachine_states;




    private statemachine_Transition statemachine_transition;




    private statemachine_State statemachine_state;




    private statemachine_Transition statemachine_transition;


    public statemachine_State(
        int id,        String label    ) {
        super(
        );
        this.id = id;
        this.label = label;
        this.statemachine_states = new ArrayList<>();
    }

    public statemachine_State(
        int id,        String label        ArrayList<statemachine_State> statemachine_states    ) {
        this.id = id;
        this.label = label;
        this.statemachine_states = statemachine_states;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public List<statemachine_State> getStatemachine_states() {
        return statemachine_states;
    }

    public void addStatemachine_state(Statemachine_state statemachine_state) {
        this.statemachine_states.add(statemachine_state);
    }
    public statemachine_Transition getStatemachine_transition() {
        return statemachine_transition;
    }

    public void setStatemachine_transition(statemachine_Transition statemachine_transition) {
        this.statemachine_transition = statemachine_transition;
    }
    public statemachine_State getStatemachine_state() {
        return statemachine_state;
    }

    public void setStatemachine_state(statemachine_State statemachine_state) {
        this.statemachine_state = statemachine_state;
    }
    public statemachine_Transition getStatemachine_transition() {
        return statemachine_transition;
    }

    public void setStatemachine_transition(statemachine_Transition statemachine_transition) {
        this.statemachine_transition = statemachine_transition;
    }

}