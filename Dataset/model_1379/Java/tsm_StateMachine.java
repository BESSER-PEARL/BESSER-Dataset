





import java.util.List;
import java.util.ArrayList;

public class tsm_StateMachine extends NamedElement {






    private tsm_State tsm_state;




    private List<tsm_State> tsm_states;


    public tsm_StateMachine(
    ) {
        super(
        );
        this.tsm_states = new ArrayList<>();
    }

    public tsm_StateMachine(
        ArrayList<tsm_State> tsm_states    ) {
        this.tsm_states = tsm_states;
    }


    public tsm_State getTsm_state() {
        return tsm_state;
    }

    public void setTsm_state(tsm_State tsm_state) {
        this.tsm_state = tsm_state;
    }
    public List<tsm_State> getTsm_states() {
        return tsm_states;
    }

    public void addTsm_state(Tsm_state tsm_state) {
        this.tsm_states.add(tsm_state);
    }

}