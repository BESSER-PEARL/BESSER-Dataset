





import java.util.List;
import java.util.ArrayList;

public class NHSM_StateMachine  {






    private List<NHSM_State> nhsm_states;




    private NHSM_State nhsm_state;


    public NHSM_StateMachine(
    ) {
        this.nhsm_states = new ArrayList<>();
    }

    public NHSM_StateMachine(
        ArrayList<NHSM_State> nhsm_states    ) {
        this.nhsm_states = nhsm_states;
    }


    public List<NHSM_State> getNhsm_states() {
        return nhsm_states;
    }

    public void addNhsm_state(Nhsm_state nhsm_state) {
        this.nhsm_states.add(nhsm_state);
    }
    public NHSM_State getNhsm_state() {
        return nhsm_state;
    }

    public void setNhsm_state(NHSM_State nhsm_state) {
        this.nhsm_state = nhsm_state;
    }

}