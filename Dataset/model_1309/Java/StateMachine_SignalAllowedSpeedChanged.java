





import java.util.List;
import java.util.ArrayList;

public class StateMachine_SignalAllowedSpeedChanged extends TriggerExpression {

    private String newAllowedSpeed;





    private StateMachine_Signal statemachine_signal;


    public StateMachine_SignalAllowedSpeedChanged(
        String newAllowedSpeed    ) {
        super(
        );
        this.newAllowedSpeed = newAllowedSpeed;
    }


    public String getNewallowedspeed() {
        return newAllowedSpeed;
    }

    public void setNewallowedspeed(String newAllowedSpeed) {
        this.newAllowedSpeed = newAllowedSpeed;
    }

    public StateMachine_Signal getStatemachine_signal() {
        return statemachine_signal;
    }

    public void setStatemachine_signal(StateMachine_Signal statemachine_signal) {
        this.statemachine_signal = statemachine_signal;
    }

}