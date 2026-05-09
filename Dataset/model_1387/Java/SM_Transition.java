





import java.util.List;
import java.util.ArrayList;

public class SM_Transition  {

    private String trigger;
    private String effect;





    private SM_State sm_state;




    private SM_State sm_state;




    private SM_StateMachine sm_statemachine;




    private SM_StateMachine sm_statemachine;


    public SM_Transition(
        String trigger,        String effect    ) {
        this.trigger = trigger;
        this.effect = effect;
    }


    public String getTrigger() {
        return trigger;
    }

    public void setTrigger(String trigger) {
        this.trigger = trigger;
    }
    public String getEffect() {
        return effect;
    }

    public void setEffect(String effect) {
        this.effect = effect;
    }

    public SM_State getSm_state() {
        return sm_state;
    }

    public void setSm_state(SM_State sm_state) {
        this.sm_state = sm_state;
    }
    public SM_State getSm_state() {
        return sm_state;
    }

    public void setSm_state(SM_State sm_state) {
        this.sm_state = sm_state;
    }
    public SM_StateMachine getSm_statemachine() {
        return sm_statemachine;
    }

    public void setSm_statemachine(SM_StateMachine sm_statemachine) {
        this.sm_statemachine = sm_statemachine;
    }
    public SM_StateMachine getSm_statemachine() {
        return sm_statemachine;
    }

    public void setSm_statemachine(SM_StateMachine sm_statemachine) {
        this.sm_statemachine = sm_statemachine;
    }

}