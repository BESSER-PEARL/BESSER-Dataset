





import java.util.List;
import java.util.ArrayList;

public class sm_StateMachine extends Graph {






    private sm_State sm_state;




    private List<sm_State> sm_states;




    private sm_State sm_state;


    public sm_StateMachine(
    ) {
        super(
        );
        this.sm_states = new ArrayList<>();
    }

    public sm_StateMachine(
        ArrayList<sm_State> sm_states    ) {
        this.sm_states = sm_states;
    }


    public sm_State getSm_state() {
        return sm_state;
    }

    public void setSm_state(sm_State sm_state) {
        this.sm_state = sm_state;
    }
    public List<sm_State> getSm_states() {
        return sm_states;
    }

    public void addSm_state(Sm_state sm_state) {
        this.sm_states.add(sm_state);
    }
    public sm_State getSm_state() {
        return sm_state;
    }

    public void setSm_state(sm_State sm_state) {
        this.sm_state = sm_state;
    }

}