





import java.util.List;
import java.util.ArrayList;

public class statemachine_Transition  {

    private int Id;





    private statemachine_State statemachine_state;




    private statemachine_State statemachine_state;




    private statemachine_StateMachine statemachine_statemachine;


    public statemachine_Transition(
        int Id    ) {
        this.Id = Id;
    }


    public int getId() {
        return Id;
    }

    public void setId(int Id) {
        this.Id = Id;
    }

    public statemachine_State getStatemachine_state() {
        return statemachine_state;
    }

    public void setStatemachine_state(statemachine_State statemachine_state) {
        this.statemachine_state = statemachine_state;
    }
    public statemachine_State getStatemachine_state() {
        return statemachine_state;
    }

    public void setStatemachine_state(statemachine_State statemachine_state) {
        this.statemachine_state = statemachine_state;
    }
    public statemachine_StateMachine getStatemachine_statemachine() {
        return statemachine_statemachine;
    }

    public void setStatemachine_statemachine(statemachine_StateMachine statemachine_statemachine) {
        this.statemachine_statemachine = statemachine_statemachine;
    }

}