





import java.util.List;
import java.util.ArrayList;

public class HSM_Transition  {

    private String effect;
    private String trigger;





    private HSM_StateMachine hsm_statemachine;




    private HSM_State hsm_state;




    private HSM_State hsm_state;




    private HSM_CompositeState hsm_compositestate;




    private HSM_CompositeState hsm_compositestate;




    private HSM_StateMachine hsm_statemachine;


    public HSM_Transition(
        String effect,        String trigger    ) {
        this.effect = effect;
        this.trigger = trigger;
    }


    public String getEffect() {
        return effect;
    }

    public void setEffect(String effect) {
        this.effect = effect;
    }
    public String getTrigger() {
        return trigger;
    }

    public void setTrigger(String trigger) {
        this.trigger = trigger;
    }

    public HSM_StateMachine getHsm_statemachine() {
        return hsm_statemachine;
    }

    public void setHsm_statemachine(HSM_StateMachine hsm_statemachine) {
        this.hsm_statemachine = hsm_statemachine;
    }
    public HSM_State getHsm_state() {
        return hsm_state;
    }

    public void setHsm_state(HSM_State hsm_state) {
        this.hsm_state = hsm_state;
    }
    public HSM_State getHsm_state() {
        return hsm_state;
    }

    public void setHsm_state(HSM_State hsm_state) {
        this.hsm_state = hsm_state;
    }
    public HSM_CompositeState getHsm_compositestate() {
        return hsm_compositestate;
    }

    public void setHsm_compositestate(HSM_CompositeState hsm_compositestate) {
        this.hsm_compositestate = hsm_compositestate;
    }
    public HSM_CompositeState getHsm_compositestate() {
        return hsm_compositestate;
    }

    public void setHsm_compositestate(HSM_CompositeState hsm_compositestate) {
        this.hsm_compositestate = hsm_compositestate;
    }
    public HSM_StateMachine getHsm_statemachine() {
        return hsm_statemachine;
    }

    public void setHsm_statemachine(HSM_StateMachine hsm_statemachine) {
        this.hsm_statemachine = hsm_statemachine;
    }

}