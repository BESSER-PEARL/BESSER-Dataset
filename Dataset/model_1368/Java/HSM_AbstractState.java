





import java.util.List;
import java.util.ArrayList;

public class HSM_AbstractState  {

    private String name;





    private HSM_StateMachine hsm_statemachine;




    private HSM_Transition hsm_transition;




    private HSM_Transition hsm_transition;




    private HSM_StateMachine hsm_statemachine;


    public HSM_AbstractState(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public HSM_StateMachine getHsm_statemachine() {
        return hsm_statemachine;
    }

    public void setHsm_statemachine(HSM_StateMachine hsm_statemachine) {
        this.hsm_statemachine = hsm_statemachine;
    }
    public HSM_Transition getHsm_transition() {
        return hsm_transition;
    }

    public void setHsm_transition(HSM_Transition hsm_transition) {
        this.hsm_transition = hsm_transition;
    }
    public HSM_Transition getHsm_transition() {
        return hsm_transition;
    }

    public void setHsm_transition(HSM_Transition hsm_transition) {
        this.hsm_transition = hsm_transition;
    }
    public HSM_StateMachine getHsm_statemachine() {
        return hsm_statemachine;
    }

    public void setHsm_statemachine(HSM_StateMachine hsm_statemachine) {
        this.hsm_statemachine = hsm_statemachine;
    }

}