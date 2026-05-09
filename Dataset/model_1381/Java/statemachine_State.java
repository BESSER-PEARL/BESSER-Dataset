





import java.util.List;
import java.util.ArrayList;

public class statemachine_State  {

    private String time;





    private statemachine_FSM statemachine_fsm;




    private statemachine_FSM statemachine_fsm;




    private List<statemachine_State> statemachine_states;


    public statemachine_State(
        String time    ) {
        this.time = time;
        this.statemachine_states = new ArrayList<>();
    }

    public statemachine_State(
        String time        ArrayList<statemachine_State> statemachine_states    ) {
        this.time = time;
        this.statemachine_states = statemachine_states;
    }

    public String getTime() {
        return time;
    }

    public void setTime(String time) {
        this.time = time;
    }

    public statemachine_FSM getStatemachine_fsm() {
        return statemachine_fsm;
    }

    public void setStatemachine_fsm(statemachine_FSM statemachine_fsm) {
        this.statemachine_fsm = statemachine_fsm;
    }
    public statemachine_FSM getStatemachine_fsm() {
        return statemachine_fsm;
    }

    public void setStatemachine_fsm(statemachine_FSM statemachine_fsm) {
        this.statemachine_fsm = statemachine_fsm;
    }
    public List<statemachine_State> getStatemachine_states() {
        return statemachine_states;
    }

    public void addStatemachine_state(Statemachine_state statemachine_state) {
        this.statemachine_states.add(statemachine_state);
    }

}