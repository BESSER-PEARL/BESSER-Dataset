





import java.util.List;
import java.util.ArrayList;

public class statemachine_Transition  {

    private String name;





    private statemachine_MyFSM statemachine_myfsm;




    private statemachine_State statemachine_state;




    private statemachine_State statemachine_state;


    public statemachine_Transition(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public statemachine_MyFSM getStatemachine_myfsm() {
        return statemachine_myfsm;
    }

    public void setStatemachine_myfsm(statemachine_MyFSM statemachine_myfsm) {
        this.statemachine_myfsm = statemachine_myfsm;
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

}