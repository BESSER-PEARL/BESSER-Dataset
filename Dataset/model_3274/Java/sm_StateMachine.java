





import java.util.List;
import java.util.ArrayList;

public class sm_StateMachine  {

    private String name;





    private List<sm_State> sm_states;




    private List<sm_State> sm_states;




    private sm_State sm_state;




    private sm_State sm_state;


    public sm_StateMachine(
        String name    ) {
        this.name = name;
        this.sm_states = new ArrayList<>();
        this.sm_states = new ArrayList<>();
    }

    public sm_StateMachine(
        String name        ArrayList<sm_State> sm_states,        ArrayList<sm_State> sm_states    ) {
        this.name = name;
        this.sm_states = sm_states;
        this.sm_states = sm_states;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<sm_State> getSm_states() {
        return sm_states;
    }

    public void addSm_state(Sm_state sm_state) {
        this.sm_states.add(sm_state);
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
    public sm_State getSm_state() {
        return sm_state;
    }

    public void setSm_state(sm_State sm_state) {
        this.sm_state = sm_state;
    }

}