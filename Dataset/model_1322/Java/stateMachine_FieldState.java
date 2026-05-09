





import java.util.List;
import java.util.ArrayList;

public class stateMachine_FieldState  {

    private String state;





    private stateMachine_DocumentField statemachine_documentfield;




    private stateMachine_State statemachine_state;


    public stateMachine_FieldState(
        String state    ) {
        this.state = state;
    }


    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }

    public stateMachine_DocumentField getStatemachine_documentfield() {
        return statemachine_documentfield;
    }

    public void setStatemachine_documentfield(stateMachine_DocumentField statemachine_documentfield) {
        this.statemachine_documentfield = statemachine_documentfield;
    }
    public stateMachine_State getStatemachine_state() {
        return statemachine_state;
    }

    public void setStatemachine_state(stateMachine_State statemachine_state) {
        this.statemachine_state = statemachine_state;
    }

}