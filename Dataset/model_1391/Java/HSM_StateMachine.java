





import java.util.List;
import java.util.ArrayList;

public class HSM_StateMachine  {






    private List<HSM_State> hsm_states;




    private HSM_State hsm_state;


    public HSM_StateMachine(
    ) {
        this.hsm_states = new ArrayList<>();
    }

    public HSM_StateMachine(
        ArrayList<HSM_State> hsm_states    ) {
        this.hsm_states = hsm_states;
    }


    public List<HSM_State> getHsm_states() {
        return hsm_states;
    }

    public void addHsm_state(Hsm_state hsm_state) {
        this.hsm_states.add(hsm_state);
    }
    public HSM_State getHsm_state() {
        return hsm_state;
    }

    public void setHsm_state(HSM_State hsm_state) {
        this.hsm_state = hsm_state;
    }

}