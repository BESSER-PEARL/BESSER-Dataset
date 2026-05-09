





import java.util.List;
import java.util.ArrayList;

public class hsm_AbstractState  {

    private String name;





    private hsm_StateMachine hsm_statemachine;




    private hsm_Transition hsm_transition;




    private hsm_StateMachine hsm_statemachine;




    private hsm_Transition hsm_transition;


    public hsm_AbstractState(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public hsm_StateMachine getHsm_statemachine() {
        return hsm_statemachine;
    }

    public void setHsm_statemachine(hsm_StateMachine hsm_statemachine) {
        this.hsm_statemachine = hsm_statemachine;
    }
    public hsm_Transition getHsm_transition() {
        return hsm_transition;
    }

    public void setHsm_transition(hsm_Transition hsm_transition) {
        this.hsm_transition = hsm_transition;
    }
    public hsm_StateMachine getHsm_statemachine() {
        return hsm_statemachine;
    }

    public void setHsm_statemachine(hsm_StateMachine hsm_statemachine) {
        this.hsm_statemachine = hsm_statemachine;
    }
    public hsm_Transition getHsm_transition() {
        return hsm_transition;
    }

    public void setHsm_transition(hsm_Transition hsm_transition) {
        this.hsm_transition = hsm_transition;
    }

}