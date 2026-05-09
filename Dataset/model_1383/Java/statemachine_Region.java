





import java.util.List;
import java.util.ArrayList;

public class statemachine_Region  {






    private List<statemachine_State> statemachine_states;




    private statemachine_ComplexState statemachine_complexstate;




    private statemachine_Pseudostate statemachine_pseudostate;


    public statemachine_Region(
    ) {
        this.statemachine_states = new ArrayList<>();
    }

    public statemachine_Region(
        ArrayList<statemachine_State> statemachine_states    ) {
        this.statemachine_states = statemachine_states;
    }


    public List<statemachine_State> getStatemachine_states() {
        return statemachine_states;
    }

    public void addStatemachine_state(Statemachine_state statemachine_state) {
        this.statemachine_states.add(statemachine_state);
    }
    public statemachine_ComplexState getStatemachine_complexstate() {
        return statemachine_complexstate;
    }

    public void setStatemachine_complexstate(statemachine_ComplexState statemachine_complexstate) {
        this.statemachine_complexstate = statemachine_complexstate;
    }
    public statemachine_Pseudostate getStatemachine_pseudostate() {
        return statemachine_pseudostate;
    }

    public void setStatemachine_pseudostate(statemachine_Pseudostate statemachine_pseudostate) {
        this.statemachine_pseudostate = statemachine_pseudostate;
    }

}