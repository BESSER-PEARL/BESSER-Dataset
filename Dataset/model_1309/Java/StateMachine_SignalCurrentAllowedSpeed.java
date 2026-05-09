





import java.util.List;
import java.util.ArrayList;

public class StateMachine_SignalCurrentAllowedSpeed extends GuardExpression {

    private String currentAllowedSpeed;





    private StateMachine_Signal statemachine_signal;


    public StateMachine_SignalCurrentAllowedSpeed(
        String currentAllowedSpeed    ) {
        super(
        );
        this.currentAllowedSpeed = currentAllowedSpeed;
    }


    public String getCurrentallowedspeed() {
        return currentAllowedSpeed;
    }

    public void setCurrentallowedspeed(String currentAllowedSpeed) {
        this.currentAllowedSpeed = currentAllowedSpeed;
    }

    public StateMachine_Signal getStatemachine_signal() {
        return statemachine_signal;
    }

    public void setStatemachine_signal(StateMachine_Signal statemachine_signal) {
        this.statemachine_signal = statemachine_signal;
    }

}