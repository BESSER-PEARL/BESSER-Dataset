





import java.util.List;
import java.util.ArrayList;

public class sm_StateMachine  {






    private List<sm_State> sm_states;


    public sm_StateMachine(
    ) {
        this.sm_states = new ArrayList<>();
    }

    public sm_StateMachine(
        ArrayList<sm_State> sm_states    ) {
        this.sm_states = sm_states;
    }


    public List<sm_State> getSm_states() {
        return sm_states;
    }

    public void addSm_state(Sm_state sm_state) {
        this.sm_states.add(sm_state);
    }

}