





import java.util.List;
import java.util.ArrayList;

public class UHSM_Transition extends TracedClass {

    private String effect;
    private String trigger;
    private String name;





    private UHSM_State uhsm_state;




    private UHSM_StateMachine uhsm_statemachine;




    private UHSM_State uhsm_state;


    public UHSM_Transition(
        String effect,        String trigger,        String name    ) {
        super(
        );
        this.effect = effect;
        this.trigger = trigger;
        this.name = name;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public UHSM_State getUhsm_state() {
        return uhsm_state;
    }

    public void setUhsm_state(UHSM_State uhsm_state) {
        this.uhsm_state = uhsm_state;
    }
    public UHSM_StateMachine getUhsm_statemachine() {
        return uhsm_statemachine;
    }

    public void setUhsm_statemachine(UHSM_StateMachine uhsm_statemachine) {
        this.uhsm_statemachine = uhsm_statemachine;
    }
    public UHSM_State getUhsm_state() {
        return uhsm_state;
    }

    public void setUhsm_state(UHSM_State uhsm_state) {
        this.uhsm_state = uhsm_state;
    }

}