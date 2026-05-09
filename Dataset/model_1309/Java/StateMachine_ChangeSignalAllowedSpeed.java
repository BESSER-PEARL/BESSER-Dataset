





import java.util.List;
import java.util.ArrayList;

public class StateMachine_ChangeSignalAllowedSpeed extends ActionExpression {

    private String newAllowedSpeed;



    public StateMachine_ChangeSignalAllowedSpeed(
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


}