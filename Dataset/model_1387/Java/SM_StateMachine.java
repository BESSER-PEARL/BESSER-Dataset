





import java.util.List;
import java.util.ArrayList;

public class SM_StateMachine  {






    private SM_State sm_state;




    private List<SM_State> sm_states;


    public SM_StateMachine(
    ) {
        this.sm_states = new ArrayList<>();
    }

    public SM_StateMachine(
        ArrayList<SM_State> sm_states    ) {
        this.sm_states = sm_states;
    }


    public SM_State getSm_state() {
        return sm_state;
    }

    public void setSm_state(SM_State sm_state) {
        this.sm_state = sm_state;
    }
    public List<SM_State> getSm_states() {
        return sm_states;
    }

    public void addSm_state(Sm_state sm_state) {
        this.sm_states.add(sm_state);
    }

}