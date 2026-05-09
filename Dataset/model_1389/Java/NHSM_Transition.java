





import java.util.List;
import java.util.ArrayList;

public class NHSM_Transition  {

    private int cost;
    private String effect;
    private String trigger;





    private NHSM_State nhsm_state;




    private NHSM_State nhsm_state;




    private NHSM_StateMachine nhsm_statemachine;




    private NHSM_StateMachine nhsm_statemachine;


    public NHSM_Transition(
        int cost,        String effect,        String trigger    ) {
        this.cost = cost;
        this.effect = effect;
        this.trigger = trigger;
    }


    public int getCost() {
        return cost;
    }

    public void setCost(int cost) {
        this.cost = cost;
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

    public NHSM_State getNhsm_state() {
        return nhsm_state;
    }

    public void setNhsm_state(NHSM_State nhsm_state) {
        this.nhsm_state = nhsm_state;
    }
    public NHSM_State getNhsm_state() {
        return nhsm_state;
    }

    public void setNhsm_state(NHSM_State nhsm_state) {
        this.nhsm_state = nhsm_state;
    }
    public NHSM_StateMachine getNhsm_statemachine() {
        return nhsm_statemachine;
    }

    public void setNhsm_statemachine(NHSM_StateMachine nhsm_statemachine) {
        this.nhsm_statemachine = nhsm_statemachine;
    }
    public NHSM_StateMachine getNhsm_statemachine() {
        return nhsm_statemachine;
    }

    public void setNhsm_statemachine(NHSM_StateMachine nhsm_statemachine) {
        this.nhsm_statemachine = nhsm_statemachine;
    }

}